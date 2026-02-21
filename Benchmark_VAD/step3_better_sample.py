#!/usr/bin/env python3
"""Step 3: Better sampling from 6h file.
- Uses Silero segments directly (no aggressive merging)
- Caps individual whisper chunks at 60s to prevent hallucination
- Samples from two different speech blocks
"""

import warnings
warnings.filterwarnings("ignore")

import time
import json
import numpy as np
import torch
import soundfile as sf
import tempfile
import os
from silero_vad import load_silero_vad, get_speech_timestamps
import whisperx
from faster_whisper import WhisperModel

SAMPLE_RATE = 16000
MAX_CHUNK_S = 60  # Max seconds per whisper chunk to prevent hallucination


def silero_scan(audio_np, model):
    """Run Silero VAD, return speech timestamps in seconds."""
    audio_tensor = torch.from_numpy(audio_np)
    raw_ts = get_speech_timestamps(
        audio_tensor, model,
        sampling_rate=SAMPLE_RATE,
        threshold=0.3,
        min_speech_duration_ms=250,
        min_silence_duration_ms=500,
        speech_pad_ms=150,  # slightly less padding than before
    )
    return [{"start": t["start"] / SAMPLE_RATE, "end": t["end"] / SAMPLE_RATE} for t in raw_ts]


def split_long_segments(segments, max_duration=MAX_CHUNK_S):
    """Split segments longer than max_duration into smaller chunks."""
    result = []
    for seg in segments:
        dur = seg["end"] - seg["start"]
        if dur <= max_duration:
            result.append(seg)
        else:
            # Split into chunks
            pos = seg["start"]
            while pos < seg["end"]:
                chunk_end = min(pos + max_duration, seg["end"])
                result.append({"start": pos, "end": chunk_end})
                pos = chunk_end
    return result


def transcribe_chunk(audio_np, start_s, end_s, whisper_model):
    """Extract and transcribe a single chunk, return results with original timestamps."""
    start_sample = int(start_s * SAMPLE_RATE)
    end_sample = int(end_s * SAMPLE_RATE)
    chunk_audio = audio_np[start_sample:end_sample]

    tmp = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    sf.write(tmp.name, chunk_audio, SAMPLE_RATE)
    tmp.close()

    results = []
    try:
        segments_iter, info = whisper_model.transcribe(
            tmp.name, beam_size=5, language="en", vad_filter=False
        )
        for s in segments_iter:
            text = s.text.strip()
            if text:
                results.append({
                    "start": round(start_s + s.start, 2),
                    "end": round(start_s + s.end, 2),
                    "text": text,
                })
    finally:
        os.unlink(tmp.name)

    return results


def print_results(results, label):
    """Print formatted results."""
    print(f"\n{'='*70}")
    print(f"  {label}")
    print(f"{'='*70}")
    prev_end = 0
    for r in results:
        gap = r["start"] - prev_end
        gap_str = f"  *** GAP {gap:.1f}s ***" if gap > 3 else ""
        text_preview = r["text"][:80]
        t_min = r["start"] / 60
        print(f"  {t_min:7.2f}min  {r['start']:8.1f} - {r['end']:8.1f}  {text_preview}{gap_str}")
        prev_end = r["end"]

    full_text = " ".join(r["text"] for r in results)
    words = len(full_text.split())
    print(f"\n  Segments: {len(results)} | Words: {words}")
    return full_text


# ============================================================
print("Loading models...", flush=True)
silero_model = load_silero_vad(onnx=True)
whisper_model = WhisperModel("large-v3", device="cpu", compute_type="int8")
print("Models loaded.\n", flush=True)

# Load 6h audio
t0 = time.time()
audio = whisperx.load_audio("VeryReal_longgap_EN_CN_workhomesleep.ogg")
print(f"Audio loaded in {time.time()-t0:.1f}s\n", flush=True)

# Silero scan
t0 = time.time()
speech_segs = silero_scan(audio, silero_model)
print(f"Silero: {len(speech_segs)} speech segments in {time.time()-t0:.1f}s")

# Filter substantial segments
substantial = [s for s in speech_segs if s["end"] - s["start"] >= 1.0]
print(f"Substantial (>=1s): {len(substantial)}")

# Split long segments to prevent hallucination
chunks = split_long_segments(substantial, MAX_CHUNK_S)
print(f"After splitting (max {MAX_CHUNK_S}s): {len(chunks)} chunks\n")

# Sample 1: Early speech block (202-210 min)
sample1 = [s for s in chunks if 202*60 <= s["start"] <= 210*60]
sample1_dur = sum(s["end"] - s["start"] for s in sample1)
print(f"Sample 1 (202-210min): {len(sample1)} chunks, {sample1_dur:.1f}s speech")

# Sample 2: Later speech block (268-285 min)
sample2 = [s for s in chunks if 268*60 <= s["start"] <= 285*60]
sample2_dur = sum(s["end"] - s["start"] for s in sample2)
print(f"Sample 2 (268-285min): {len(sample2)} chunks, {sample2_dur:.1f}s speech")

# Transcribe Sample 1
print(f"\n--- Transcribing Sample 1 ({len(sample1)} chunks) ---", flush=True)
t0 = time.time()
results1 = []
for i, chunk in enumerate(sample1):
    r = transcribe_chunk(audio, chunk["start"], chunk["end"], whisper_model)
    results1.extend(r)
    if (i+1) % 5 == 0 or i == len(sample1) - 1:
        print(f"  [{i+1}/{len(sample1)}]", flush=True)
elapsed1 = time.time() - t0

text1 = print_results(results1, f"Sample 1: 202-210min [{elapsed1:.1f}s]")
with open("prefilter_6h_sample1_202_210.txt", "w") as f:
    f.write(text1)

# Transcribe Sample 2
print(f"\n--- Transcribing Sample 2 ({len(sample2)} chunks) ---", flush=True)
t0 = time.time()
results2 = []
for i, chunk in enumerate(sample2):
    r = transcribe_chunk(audio, chunk["start"], chunk["end"], whisper_model)
    results2.extend(r)
    if (i+1) % 5 == 0 or i == len(sample2) - 1:
        print(f"  [{i+1}/{len(sample2)}]", flush=True)
elapsed2 = time.time() - t0

text2 = print_results(results2, f"Sample 2: 268-285min [{elapsed2:.1f}s]")
with open("prefilter_6h_sample2_268_285.txt", "w") as f:
    f.write(text2)

print(f"\n\nTotal time: {elapsed1 + elapsed2:.1f}s ({(elapsed1+elapsed2)/60:.1f}min)")
print("Done!")
