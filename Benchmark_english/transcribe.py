#!/usr/bin/env python3
"""Transcribe all English clips in this folder with WhisperX."""

import warnings
warnings.filterwarnings("ignore")

import whisperx
import os
import time
import json

def main():
    device = "cpu"
    compute_type = "int8"

    print("Loading WhisperX large-v3 model...", flush=True)
    model = whisperx.load_model("large-v3", device, compute_type=compute_type, language="en")
    print("Model loaded.\n", flush=True)

    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)

    files = sorted([f for f in os.listdir(".") if f.endswith((".m4a", ".ogg"))])
    print(f"Found {len(files)} audio files to transcribe.\n", flush=True)

    results = []

    for i, f in enumerate(files, 1):
        print(f"[{i}/{len(files)}] {f}", flush=True)

        start = time.time()
        audio = whisperx.load_audio(f)
        result = model.transcribe(audio, batch_size=4, language="en")
        elapsed = time.time() - start

        segments = result.get("segments", [])
        text = " ".join(seg["text"].strip() for seg in segments)

        txt_name = os.path.splitext(f)[0] + ".txt"
        with open(txt_name, "w") as out:
            out.write(text)

        word_count = len(text.split())
        results.append({
            "file": f,
            "time_s": round(elapsed, 1),
            "segments": len(segments),
            "chars": len(text),
            "words": word_count,
        })

        print(f"  Done in {elapsed:.1f}s | {len(segments)} segments | {word_count} words", flush=True)
        print(f"  Preview: {text[:120]}...\n", flush=True)

    with open("results.json", "w") as f:
        json.dump(results, f, indent=2)

    total_time = sum(r["time_s"] for r in results)
    total_words = sum(r["words"] for r in results)
    print(f"All done! {len(results)} files transcribed.", flush=True)
    print(f"Total processing time: {total_time:.0f}s ({total_time/60:.1f} min)", flush=True)
    print(f"Total words: {total_words}", flush=True)


if __name__ == "__main__":
    main()
