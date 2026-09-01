#!/usr/bin/env python3
"""Render short vertical social clips with burned-in captions from a
promo-agent EDL. Deterministic ffmpeg-python — crop to 9:16, trim to the
clip window, burn in the agent's caption chunks.
"""
import argparse
import json
from pathlib import Path

import ffmpeg


def render_clip(input_path: str, clip: dict, out_path: str, aspect_ratio: str) -> None:
    stream = ffmpeg.input(input_path, ss=clip["start"], to=clip["end"])
    video, audio = stream.video, stream.audio

    if aspect_ratio == "9:16":
        # crop to a centered vertical frame, then scale to a standard reel size
        video = video.filter("crop", "ih*9/16", "ih").filter("scale", 1080, 1920)

    clip_start = clip["start"]
    for cap in clip.get("captions", []):
        video = video.drawtext(
            text=cap["text"].replace(":", r"\:").replace("'", r"\'"),
            fontsize=64,
            fontcolor="white",
            borderw=3,
            bordercolor="black",
            x="(w-text_w)/2",
            y="h-260",
            enable=f"between(t,{cap['start'] - clip_start},{cap['end'] - clip_start})",
        )

    out_path_p = Path(out_path)
    out_path_p.parent.mkdir(parents=True, exist_ok=True)
    (
        ffmpeg.output(video, audio, str(out_path_p), vcodec="libx264", acodec="aac", crf=20)
        .overwrite_output()
        .run()
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to raw footage")
    parser.add_argument("--edl", required=True, help="Path to EDL JSON from step 2 (promo mode)")
    parser.add_argument("--out", required=True, help="Output directory for clip MP4s")
    parser.add_argument("--aspect-ratio", default="9:16")
    args = parser.parse_args()

    edl = json.loads(Path(args.edl).read_text())
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    clips = sorted(edl["clips"], key=lambda c: c.get("rank", 0))
    for i, clip in enumerate(clips, start=1):
        out_path = out_dir / f"clip-{i:02d}-rank{clip.get('rank', i)}.mp4"
        render_clip(args.input, clip, str(out_path), args.aspect_ratio)
        print(f"Wrote {out_path} — {clip.get('hook', '')}")


if __name__ == "__main__":
    main()
