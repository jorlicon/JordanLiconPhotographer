#!/usr/bin/env python3
"""Step 2 — Rough cut.

whisperX transcribes the raw clip word-by-word, filler words are cut,
audio is polished (loudness-normalized), and a clean script is written
out alongside a keep-range EDL that step 3+ and to_premiere.py both read.

Outputs (all under --work-dir):
  transcript.json   — full word-level whisperX transcript (before filler removal)
  edl.json          — {"segments": [{"start", "end"}, ...]} of kept ranges
  script.md         — the cleaned script text, corrections applied, one
                       sentence-ish line per kept segment with its time range
  rough-cut.mp4      — rendered rough cut (kept ranges concatenated, audio
                       loudness-normalized) — written only if --render is passed
"""
import argparse
import json
import re
from pathlib import Path

import ffmpeg
import whisperx

DEFAULT_FILLERS = {
    "um", "umm", "uh", "uhh", "uhm", "erm", "hm", "hmm",
    "like", "y'know", "you know", "i mean", "sort of", "kind of",
}

# a gap this long between consecutive kept words starts a new segment
# rather than bridging it — avoids stitching across a real pause/breath
SEGMENT_GAP_SECONDS = 0.6

PRESETS_DIR = Path(__file__).parent.parent / "presets"


def transcribe(input_path: str, model_size: str, language: str, device: str, batch_size: int) -> dict:
    compute_type = "float16" if device == "cuda" else "int8"
    model = whisperx.load_model(model_size, device, language=language, compute_type=compute_type)
    audio = whisperx.load_audio(input_path)
    result = model.transcribe(audio, batch_size=batch_size)

    align_model, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
    aligned = whisperx.align(result["segments"], align_model, metadata, audio, device)

    words = [
        {"word": w["word"], "start": w["start"], "end": w["end"]}
        for segment in aligned["segments"]
        for w in segment.get("words", [])
        if "start" in w and "end" in w
    ]
    return {"language": result["language"], "words": words}


def is_filler(word: str, fillers: set) -> bool:
    cleaned = re.sub(r"[^\w']", "", word).lower()
    return cleaned in fillers


def kill_filler(transcript: dict, fillers: set) -> tuple[list, list]:
    """Returns (kept_words, segments) — kept_words excludes filler tokens,
    segments groups them into contiguous [start, end] ranges."""
    kept_words = [w for w in transcript["words"] if not is_filler(w["word"], fillers)]

    segments = []
    for w in kept_words:
        if segments and w["start"] - segments[-1]["end"] <= SEGMENT_GAP_SECONDS:
            segments[-1]["end"] = w["end"]
            segments[-1]["words"].append(w)
        else:
            segments.append({"start": w["start"], "end": w["end"], "words": [w]})

    return kept_words, segments


def load_corrections() -> dict:
    path = PRESETS_DIR / "caption-corrections.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text()).get("corrections", {})


def apply_corrections(text: str, corrections: dict) -> str:
    # longest keys first so a longer phrase match wins over a shorter substring
    for wrong in sorted(corrections, key=len, reverse=True):
        text = re.sub(re.escape(wrong), corrections[wrong], text, flags=re.IGNORECASE)
    return text


def write_script(segments: list, corrections: dict, out_path: Path) -> None:
    lines = ["# Rough-cut script\n"]
    for seg in segments:
        text = " ".join(w["word"] for w in seg["words"]).strip()
        text = apply_corrections(text, corrections)
        lines.append(f"- `[{seg['start']:.2f}-{seg['end']:.2f}]` {text}")
    out_path.write_text("\n".join(lines) + "\n")


def render_rough_cut(input_path: str, segments: list, out_path: str) -> None:
    trimmed = []
    for seg in segments:
        clip = ffmpeg.input(input_path, ss=seg["start"], to=seg["end"])
        trimmed.append(clip.video)
        trimmed.append(clip.audio)

    joined = ffmpeg.concat(*trimmed, v=1, a=1).node
    video, audio = joined[0], joined[1]
    # loudnorm polishes/normalizes audio in one pass — "polish audio" per the diagram
    audio = audio.filter("loudnorm", i=-16, tp=-1.5, lra=11)

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    ffmpeg.output(video, audio, out_path, vcodec="libx264", acodec="aac", crf=18).overwrite_output().run()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to raw footage")
    parser.add_argument("--work-dir", required=True, help="Directory to write transcript.json/edl.json/script.md into")
    parser.add_argument("--model", default="large-v3")
    parser.add_argument("--language", default="en")
    parser.add_argument("--device", default="cuda", choices=["cuda", "cpu"])
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument(
        "--filler", action="append", default=[],
        help="Additional filler word/phrase to cut, beyond the built-in list. Repeatable.",
    )
    parser.add_argument("--render", action="store_true", help="Also render rough-cut.mp4")
    args = parser.parse_args()

    work_dir = Path(args.work_dir)
    work_dir.mkdir(parents=True, exist_ok=True)

    transcript = transcribe(args.input, args.model, args.language, args.device, args.batch_size)
    (work_dir / "transcript.json").write_text(json.dumps(transcript, indent=2))

    fillers = DEFAULT_FILLERS | {f.lower() for f in args.filler}
    kept_words, segments = kill_filler(transcript, fillers)
    print(f"Kept {len(kept_words)}/{len(transcript['words'])} words after filler removal "
          f"({len(segments)} segments)")

    edl = {"segments": [{"start": s["start"], "end": s["end"]} for s in segments]}
    (work_dir / "edl.json").write_text(json.dumps(edl, indent=2))

    corrections = load_corrections()
    write_script(segments, corrections, work_dir / "script.md")

    if args.render:
        render_rough_cut(args.input, segments, str(work_dir / "rough-cut.mp4"))
        print(f"Wrote {work_dir / 'rough-cut.mp4'}")

    print(f"Wrote transcript.json, edl.json, script.md to {work_dir}")


if __name__ == "__main__":
    main()
