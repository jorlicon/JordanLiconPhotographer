#!/usr/bin/env python3
"""Render the long-form client deliverable from a finishing-agent EDL.
Deterministic ffmpeg-python trim + concat + title overlay — no AI here,
the agent already made every editorial decision in step 2.
"""
import argparse
import json
from pathlib import Path

import ffmpeg


def render(input_path: str, edl: dict, out_path: str) -> None:
    segments = edl["segments"]
    if not segments:
        raise ValueError("EDL has no segments to render")

    trimmed_clips = []
    for seg in segments:
        clip = ffmpeg.input(input_path, ss=seg["start"], to=seg["end"])
        trimmed_clips.append(clip.video)
        trimmed_clips.append(clip.audio)

    joined = ffmpeg.concat(*trimmed_clips, v=1, a=1).node
    video, audio = joined[0], joined[1]

    for title in edl.get("titles", []):
        video = video.drawtext(
            text=title["text"].replace(":", r"\:"),
            fontsize=48,
            fontcolor="white",
            x="(w-text_w)/2",
            y="h-120",
            enable=f"between(t,{title['at']},{title['at'] + title['duration']})",
        )

    out_path_p = Path(out_path)
    out_path_p.parent.mkdir(parents=True, exist_ok=True)

    (
        ffmpeg.output(video, audio, str(out_path_p), vcodec="libx264", acodec="aac", crf=18)
        .overwrite_output()
        .run()
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to raw footage")
    parser.add_argument("--edl", required=True, help="Path to EDL JSON from step 2 (finishing mode)")
    parser.add_argument("--out", required=True, help="Path to write final MP4")
    args = parser.parse_args()

    edl = json.loads(Path(args.edl).read_text())
    render(args.input, edl, args.out)
    print(f"Wrote {args.out}")


if __name__ == "__main__":
    main()
