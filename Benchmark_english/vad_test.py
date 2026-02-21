#!/usr/bin/env python3
"""Test 3 VAD approaches on research_talk_5min.m4a."""

import warnings
warnings.filterwarnings("ignore")

import time
import json

CLIP = "research_talk_5min.m4a"


def show_segments(segments, label):
    """Print segments with gap detection."""
    print(f"\n{'='*70}")
    print(f"  {label}")
    print(f"{'='*70}")
    prev_end = 0
    total_text = []
    gaps = []
    for seg in segments:
        gap = seg["start"] - prev_end
        gap_marker = f"  *** GAP {gap:.1f}s ***" if gap > 3 else ""
        if gap > 3:
            gaps.append({"from": prev_end, "to": seg["start"], "duration": gap})
        print(f"  {seg['start']:7.1f} - {seg['end']:7.1f}  {seg['text'][:80]}{gap_marker}")
        total_text.append(seg["text"].strip())
        prev_end = seg["end"]

    full_text = " ".join(total_text)
    print(f"\n  Segments: {len(segments)} | Words: {len(full_text.split())} | Gaps>3s: {len(gaps)}")
    return full_text, gaps


def test_1_no_vad():
    """faster-whisper directly, no VAD at all."""
    from faster_whisper import WhisperModel

    model = WhisperModel("large-v3", device="cpu", compute_type="int8")
    start = time.time()
    segments_iter, info = model.transcribe(
        CLIP, beam_size=5, language="en", vad_filter=False
    )
    segments = [{"start": s.start, "end": s.end, "text": s.text} for s in segments_iter]
    elapsed = time.time() - start

    text, gaps = show_segments(segments, f"Test 1: No VAD (faster-whisper direct) [{elapsed:.1f}s]")
    return {"method": "no_vad", "text": text, "time_s": elapsed, "gaps": gaps, "segments": len(segments)}


def test_2_low_threshold():
    """WhisperX with lower VAD onset threshold (0.2 instead of default 0.5)."""
    import whisperx

    model = whisperx.load_model("large-v3", "cpu", compute_type="int8", language="en",
                                 vad_options={"vad_onset": 0.2})
    start = time.time()
    audio = whisperx.load_audio(CLIP)
    result = model.transcribe(audio, batch_size=4, language="en")
    elapsed = time.time() - start

    segments = result.get("segments", [])
    text, gaps = show_segments(segments, f"Test 2: WhisperX VAD onset=0.2 [{elapsed:.1f}s]")
    return {"method": "whisperx_low_vad", "text": text, "time_s": elapsed, "gaps": gaps, "segments": len(segments)}


def test_3_silero_vad():
    """Silero VAD for speech detection, then faster-whisper for transcription."""
    import torch
    from silero_vad import load_silero_vad, get_speech_timestamps
    from faster_whisper import WhisperModel

    start = time.time()

    # Load Silero VAD
    silero_model = load_silero_vad(onnx=True)

    # Read audio at 16kHz for Silero
    import whisperx
    audio_np = whisperx.load_audio(CLIP)
    audio_tensor = torch.from_numpy(audio_np)

    # Get speech timestamps from Silero
    speech_timestamps = get_speech_timestamps(
        audio_tensor, silero_model,
        sampling_rate=16000,
        threshold=0.3,
        min_speech_duration_ms=250,
        min_silence_duration_ms=500,
        speech_pad_ms=200,
    )

    print(f"\n  Silero detected {len(speech_timestamps)} speech segments")
    for st in speech_timestamps[:10]:
        start_s = st["start"] / 16000
        end_s = st["end"] / 16000
        print(f"    {start_s:.1f}s - {end_s:.1f}s ({end_s - start_s:.1f}s)")
    if len(speech_timestamps) > 10:
        print(f"    ... and {len(speech_timestamps) - 10} more")

    # Now transcribe with faster-whisper using Silero's VAD segments
    # We'll use faster-whisper's built-in vad_filter=False and transcribe the whole thing
    # but only keep segments that overlap with Silero's speech regions
    whisper_model = WhisperModel("large-v3", device="cpu", compute_type="int8")
    segments_iter, info = whisper_model.transcribe(
        CLIP, beam_size=5, language="en", vad_filter=False
    )
    all_segments = [{"start": s.start, "end": s.end, "text": s.text} for s in segments_iter]

    # Filter: keep whisper segments that overlap with any Silero speech region
    def overlaps_speech(seg_start, seg_end, speech_ts):
        for st in speech_ts:
            s_start = st["start"] / 16000
            s_end = st["end"] / 16000
            if seg_start < s_end and seg_end > s_start:
                return True
        return False

    filtered = [s for s in all_segments if overlaps_speech(s["start"], s["end"], speech_timestamps)]
    elapsed = time.time() - start

    text, gaps = show_segments(filtered, f"Test 3: Silero VAD + faster-whisper [{elapsed:.1f}s]")
    return {"method": "silero_vad", "text": text, "time_s": elapsed, "gaps": gaps,
            "segments": len(filtered), "silero_speech_segments": len(speech_timestamps)}


if __name__ == "__main__":
    results = []

    print("Running 3 VAD tests on research_talk_5min.m4a...\n")

    r1 = test_1_no_vad()
    results.append(r1)

    r2 = test_2_low_threshold()
    results.append(r2)

    r3 = test_3_silero_vad()
    results.append(r3)

    # Save texts for comparison
    for r in results:
        fname = f"vad_test_{r['method']}.txt"
        with open(fname, "w") as f:
            f.write(r["text"])

    # Summary
    print(f"\n\n{'='*70}")
    print("  SUMMARY")
    print(f"{'='*70}")
    for r in results:
        print(f"  {r['method']:25s}  {r['time_s']:6.1f}s  {r['segments']:3d} segs  {len(r['text'].split()):5d} words  {len(r['gaps']):2d} gaps>3s")
