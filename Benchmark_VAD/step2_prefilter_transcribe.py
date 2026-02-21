#!/usr/bin/env python3
"""Step 2: Pre-filter transcription pipeline.
- Silero VAD detects speech regions
- Extract speech regions as temp audio clips
- Transcribe each clip with faster-whisper (no VAD)
- Reassemble with original timestamps

Tests on:
1. research_talk_5min.m4a (full) — for comparison with previous tests
2. VeryReal_longgap_EN_CN_workhomesleep.ogg (sampled) — 3 chunks from different parts
"""

import warnings
warnings.filterwarnings("ignore")

import time
import json
import numpy as np
import torch
from silero_vad import load_silero_vad, get_speech_timestamps
import whisperx
from faster_whisper import WhisperModel
from pathlib import Path

SAMPLE_RATE = 16000


def silero_scan(audio_np, model):
    """Run Silero VAD and return speech timestamps in seconds."""
    audio_tensor = torch.from_numpy(audio_np)
    raw_ts = get_speech_timestamps(
        audio_tensor, model,
        sampling_rate=SAMPLE_RATE,
        threshold=0.3,
        min_speech_duration_ms=250,
        min_silence_duration_ms=500,
        speech_pad_ms=200,
    )
    return [{"start": t["start"] / SAMPLE_RATE, "end": t["end"] / SAMPLE_RATE} for t in raw_ts]


def merge_nearby_segments(segments, max_gap=1.0):
    """Merge speech segments that are close together to reduce number of clips."""
    if not segments:
        return []
    merged = [segments[0].copy()]
    for seg in segments[1:]:
        if seg["start"] - merged[-1]["end"] <= max_gap:
            merged[-1]["end"] = seg["end"]
        else:
            merged.append(seg.copy())
    return merged


def extract_audio_segment(audio_np, start_s, end_s):
    """Extract a segment from audio array."""
    start_sample = int(start_s * SAMPLE_RATE)
    end_sample = int(end_s * SAMPLE_RATE)
    return audio_np[start_sample:end_sample]


def transcribe_segments(audio_np, speech_segments, whisper_model, label=""):
    """Transcribe speech segments using pre-filter approach.

    For each speech segment:
    1. Extract audio
    2. Save as temp wav
    3. Transcribe with faster-whisper (no VAD)
    4. Map timestamps back to original
    """
    import soundfile as sf
    import tempfile
    import os

    all_results = []
    total_speech_time = sum(s["end"] - s["start"] for s in speech_segments)

    print(f"\n  Transcribing {len(speech_segments)} speech segments ({total_speech_time:.1f}s = {total_speech_time/60:.1f}min)")

    for i, seg in enumerate(speech_segments):
        seg_duration = seg["end"] - seg["start"]
        # Skip very short segments (< 0.5s) — likely noise
        if seg_duration < 0.5:
            continue

        seg_audio = extract_audio_segment(audio_np, seg["start"], seg["end"])

        # Write temp wav file
        tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
        sf.write(tmp.name, seg_audio, SAMPLE_RATE)
        tmp.close()

        try:
            # Transcribe with no VAD
            segments_iter, info = whisper_model.transcribe(
                tmp.name, beam_size=5, language="en", vad_filter=False
            )
            for s in segments_iter:
                # Map timestamps back to original audio time
                all_results.append({
                    "start": round(seg["start"] + s.start, 2),
                    "end": round(seg["start"] + s.end, 2),
                    "text": s.text.strip(),
                })
        finally:
            os.unlink(tmp.name)

        if (i + 1) % 5 == 0 or i == len(speech_segments) - 1:
            pct = (i + 1) / len(speech_segments) * 100
            print(f"    [{pct:5.1f}%] Segment {i+1}/{len(speech_segments)}", flush=True)

    return all_results


def format_results(results, label, elapsed):
    """Print and return formatted results."""
    print(f"\n{'='*70}")
    print(f"  {label} [{elapsed:.1f}s]")
    print(f"{'='*70}")

    prev_end = 0
    gaps = 0
    for r in results:
        gap = r["start"] - prev_end
        gap_str = f"  *** GAP {gap:.1f}s ***" if gap > 3 else ""
        if gap > 3:
            gaps += 1
        text_preview = r["text"][:80]
        print(f"  {r['start']:7.1f} - {r['end']:7.1f}  {text_preview}{gap_str}")
        prev_end = r["end"]

    full_text = " ".join(r["text"] for r in results)
    words = len(full_text.split())
    print(f"\n  Segments: {len(results)} | Words: {words} | Gaps>3s: {gaps}")
    return full_text


# ============================================================
# MAIN
# ============================================================

print("Loading models...", flush=True)
silero_model = load_silero_vad(onnx=True)
whisper_model = WhisperModel("large-v3", device="cpu", compute_type="int8")
print("Models loaded.\n")


# ============================================================
# Test A: 5-min research talk (full, for comparison)
# ============================================================
print("="*70)
print("  TEST A: research_talk_5min.m4a (pre-filter approach)")
print("="*70, flush=True)

start = time.time()
audio_5min = whisperx.load_audio("research_talk_5min.m4a")
speech_5min = silero_scan(audio_5min, silero_model)
merged_5min = merge_nearby_segments(speech_5min, max_gap=1.0)
print(f"  Silero: {len(speech_5min)} segments -> {len(merged_5min)} after merging (gap<=1s)")

results_5min = transcribe_segments(audio_5min, merged_5min, whisper_model, "5min")
elapsed_5min = time.time() - start

text_5min = format_results(results_5min, "Pre-filter: research_talk_5min", elapsed_5min)
with open("prefilter_5min_research.txt", "w") as f:
    f.write(text_5min)
print(f"  Saved to prefilter_5min_research.txt")


# ============================================================
# Test B: 6h file — sample 3 regions
# ============================================================
print(f"\n\n{'='*70}")
print("  TEST B: 6h file (sampled regions)")
print("="*70, flush=True)

start = time.time()

# Load the full audio
t0 = time.time()
audio_6h = whisperx.load_audio("VeryReal_longgap_EN_CN_workhomesleep.ogg")
total_dur = len(audio_6h) / SAMPLE_RATE
print(f"  Audio loaded: {total_dur/60:.1f}min in {time.time()-t0:.1f}s")

# Silero scan
t0 = time.time()
speech_6h = silero_scan(audio_6h, silero_model)
print(f"  Silero scan: {len(speech_6h)} segments in {time.time()-t0:.1f}s")

# Merge nearby segments
merged_6h = merge_nearby_segments(speech_6h, max_gap=1.5)
total_speech = sum(s["end"] - s["start"] for s in merged_6h)
print(f"  After merging: {len(merged_6h)} segments, {total_speech/60:.1f}min total speech")

# Filter out very short segments (<1s) — likely noise
substantial = [s for s in merged_6h if s["end"] - s["start"] >= 1.0]
print(f"  Substantial (>=1s): {len(substantial)} segments")

# Sample 3 regions: early, middle, late speech
# Find segments in different time ranges
early = [s for s in substantial if s["start"] < total_dur * 0.4]
middle = [s for s in substantial if total_dur * 0.4 <= s["start"] < total_dur * 0.7]
late = [s for s in substantial if s["start"] >= total_dur * 0.7]

print(f"\n  Speech distribution:")
print(f"    Early  (0-40%):    {len(early)} segments")
print(f"    Middle (40-70%):   {len(middle)} segments")
print(f"    Late   (70-100%):  {len(late)} segments")

# Pick up to ~5 min of speech from each region (or all if less)
def pick_segments(segs, max_duration=300):
    """Pick segments up to max_duration seconds total."""
    picked = []
    total = 0
    for s in segs:
        dur = s["end"] - s["start"]
        if total + dur > max_duration:
            break
        picked.append(s)
        total += dur
    return picked

sample_early = pick_segments(early, 300)
sample_middle = pick_segments(middle, 300)
sample_late = pick_segments(late, 300)

for region_name, sample in [("Early", sample_early), ("Middle", sample_middle), ("Late", sample_late)]:
    if not sample:
        print(f"\n  {region_name}: No segments to transcribe")
        continue

    sample_dur = sum(s["end"] - s["start"] for s in sample)
    time_range = f"{sample[0]['start']/60:.1f}min - {sample[-1]['end']/60:.1f}min"
    print(f"\n  {region_name} sample: {len(sample)} segments, {sample_dur:.1f}s speech, range: {time_range}")

    t0 = time.time()
    results = transcribe_segments(audio_6h, sample, whisper_model, region_name)
    elapsed = time.time() - t0

    text = format_results(results, f"6h {region_name} ({time_range})", elapsed)
    fname = f"prefilter_6h_{region_name.lower()}.txt"
    with open(fname, "w") as f:
        f.write(text)
    print(f"  Saved to {fname}")

total_elapsed = time.time() - start
print(f"\n  Total 6h test time: {total_elapsed:.1f}s ({total_elapsed/60:.1f}min)")
print("\nDone!")
