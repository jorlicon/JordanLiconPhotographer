#!/usr/bin/env python3
"""Transcribe raw footage into a word-level timestamped JSON transcript
using whisperX (m-bain/whisperX). This is the required first stage for
both the finishing and promo pipelines.
"""
import argparse
import json
from pathlib import Path

import whisperx


def transcribe(
    input_path: str, model_size: str, language: str, device: str, batch_size: int
) -> dict:
    # float16 needs a GPU; CPU falls back to int8 or transcription will error out
    compute_type = "float16" if device == "cuda" else "int8"
    model = whisperx.load_model(
        model_size, device, language=language, compute_type=compute_type
    )
    audio = whisperx.load_audio(input_path)
    # batch_size is what actually uses the GPU efficiently on long footage —
    # raise it if you have VRAM to spare, lower it if you hit OOM
    result = model.transcribe(audio, batch_size=batch_size)

    align_model, metadata = whisperx.load_align_model(
        language_code=result["language"], device=device
    )
    aligned = whisperx.align(
        result["segments"], align_model, metadata, audio, device
    )

    words = [
        {"word": w["word"], "start": w["start"], "end": w["end"]}
        for segment in aligned["segments"]
        for w in segment.get("words", [])
        if "start" in w and "end" in w
    ]
    return {"language": result["language"], "words": words}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to raw footage (video/audio file)")
    parser.add_argument("--out", required=True, help="Path to write transcript JSON")
    parser.add_argument("--model", default="large-v3", help="whisperX model size")
    parser.add_argument("--language", default="en")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    parser.add_argument(
        "--batch-size", type=int, default=16, help="Lower if you hit GPU OOM on long footage"
    )
    args = parser.parse_args()

    transcript = transcribe(
        args.input, args.model, args.language, args.device, args.batch_size
    )

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(transcript, indent=2))
    print(f"Wrote {len(transcript['words'])} words to {out_path}")


if __name__ == "__main__":
    main()
