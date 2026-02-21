#!/usr/bin/env python3
"""Step 1: Silero VAD scan on the full 6h file + 5min research talk.
Outputs speech segment timestamps and statistics."""

import warnings
warnings.filterwarnings("ignore")

import time
import json
import torch
from silero_vad import load_silero_vad, get_speech_timestamps
import whisperx

FILES = [
    ("research_talk_5min.m4a", "5min_research"),
    ("VeryReal_longgap_EN_CN_workhomesleep.ogg", "6h_long"),
]

print("Loading Silero VAD...", flush=True)
model = load_silero_vad(onnx=True)

results = {}

for filename, label in FILES:
    print(f"\n{'='*70}")
    print(f"  Scanning: {filename} ({label})")
    print(f"{'='*70}", flush=True)

    start = time.time()

    # Load audio at 16kHz
    t0 = time.time()
    audio_np = whisperx.load_audio(filename)
    total_duration = len(audio_np) / 16000
    print(f"  Audio loaded: {total_duration:.1f}s ({total_duration/60:.1f}min) in {time.time()-t0:.1f}s")

    audio_tensor = torch.from_numpy(audio_np)

    # Run Silero VAD
    t0 = time.time()
    speech_timestamps = get_speech_timestamps(
        audio_tensor, model,
        sampling_rate=16000,
        threshold=0.3,
        min_speech_duration_ms=250,
        min_silence_duration_ms=500,
        speech_pad_ms=200,
    )
    vad_time = time.time() - t0
    print(f"  VAD completed in {vad_time:.1f}s")

    # Compute statistics
    segments = []
    total_speech = 0
    gaps = []
    prev_end = 0

    for st in speech_timestamps:
        s_start = st["start"] / 16000
        s_end = st["end"] / 16000
        duration = s_end - s_start
        total_speech += duration
        gap_before = s_start - prev_end
        if prev_end > 0:
            gaps.append({"from": prev_end, "to": s_start, "duration": gap_before})
        segments.append({
            "start": round(s_start, 2),
            "end": round(s_end, 2),
            "duration": round(duration, 2),
            "gap_before": round(gap_before, 2) if prev_end > 0 else None,
        })
        prev_end = s_end

    total_silence = total_duration - total_speech
    speech_pct = (total_speech / total_duration) * 100

    # Gap distribution
    gap_durations = [g["duration"] for g in gaps]
    gap_buckets = {
        "<1s": sum(1 for g in gap_durations if g < 1),
        "1-5s": sum(1 for g in gap_durations if 1 <= g < 5),
        "5-30s": sum(1 for g in gap_durations if 5 <= g < 30),
        "30s-5min": sum(1 for g in gap_durations if 30 <= g < 300),
        "5-30min": sum(1 for g in gap_durations if 300 <= g < 1800),
        "30min+": sum(1 for g in gap_durations if g >= 1800),
    }

    # Print summary
    print(f"\n  Total duration:    {total_duration/60:.1f} min ({total_duration/3600:.2f} hrs)")
    print(f"  Speech segments:   {len(segments)}")
    print(f"  Total speech:      {total_speech/60:.1f} min ({speech_pct:.1f}%)")
    print(f"  Total silence:     {total_silence/60:.1f} min ({100-speech_pct:.1f}%)")
    print(f"  VAD scan time:     {vad_time:.1f}s")
    print(f"\n  Gap distribution:")
    for bucket, count in gap_buckets.items():
        if count > 0:
            print(f"    {bucket:>10s}: {count}")

    if gap_durations:
        print(f"\n  Longest gaps:")
        sorted_gaps = sorted(gaps, key=lambda g: g["duration"], reverse=True)
        for g in sorted_gaps[:10]:
            mins = g["duration"] / 60
            from_m = g["from"] / 60
            to_m = g["to"] / 60
            if g["duration"] >= 60:
                print(f"    {from_m:.1f}min - {to_m:.1f}min  ({mins:.1f} min gap)")
            else:
                print(f"    {g['from']:.1f}s - {g['to']:.1f}s  ({g['duration']:.1f}s gap)")

    # Print first 20 and last 10 segments
    print(f"\n  First 20 speech segments:")
    for seg in segments[:20]:
        gap_str = f"  [gap {seg['gap_before']:.1f}s]" if seg['gap_before'] and seg['gap_before'] > 2 else ""
        print(f"    {seg['start']/60:7.2f}min - {seg['end']/60:7.2f}min  ({seg['duration']:.1f}s){gap_str}")

    if len(segments) > 20:
        print(f"\n  Last 10 speech segments:")
        for seg in segments[-10:]:
            gap_str = f"  [gap {seg['gap_before']:.1f}s]" if seg['gap_before'] and seg['gap_before'] > 2 else ""
            print(f"    {seg['start']/60:7.2f}min - {seg['end']/60:7.2f}min  ({seg['duration']:.1f}s){gap_str}")

    elapsed = time.time() - start
    print(f"\n  Total time: {elapsed:.1f}s")

    results[label] = {
        "file": filename,
        "total_duration_s": round(total_duration, 2),
        "speech_segments": len(segments),
        "total_speech_s": round(total_speech, 2),
        "total_silence_s": round(total_silence, 2),
        "speech_pct": round(speech_pct, 1),
        "vad_time_s": round(vad_time, 1),
        "gap_buckets": gap_buckets,
        "segments": segments,
    }

# Save full results
with open("silero_vad_scan.json", "w") as f:
    json.dump(results, f, indent=2)
print(f"\n\nFull results saved to silero_vad_scan.json")
