#!/usr/bin/env python3
"""Render short vertical social clips from a promo-agent EDL.

Two stages per clip:
  1. ffmpeg-python trims the source to the clip window and crops/scales to
     the target aspect ratio (fast, deterministic).
  2. Remotion renders the animated captions on top of that trimmed clip
     (video-pipeline/remotion — see remotion/src/SocialClipCaptions.tsx),
     for nicer typography/animation than ffmpeg's plain drawtext.

Pass --captions ffmpeg to skip Remotion and burn in plain captions with
ffmpeg instead (no Node/npm required).
"""
import argparse
import json
import shutil
import subprocess
import tempfile
import uuid
from pathlib import Path

import ffmpeg

REMOTION_DIR = Path(__file__).parent.parent / "remotion"
REMOTION_PUBLIC_DIR = REMOTION_DIR / "public"


def trim_and_crop(input_path: str, clip: dict, out_path: str, aspect_ratio: str) -> None:
    stream = ffmpeg.input(input_path, ss=clip["start"], to=clip["end"])
    video, audio = stream.video, stream.audio

    if aspect_ratio == "9:16":
        # crop to a centered vertical frame, then scale to a standard reel size
        video = video.filter("crop", "ih*9/16", "ih").filter("scale", 1080, 1920)

    (
        ffmpeg.output(video, audio, out_path, vcodec="libx264", acodec="aac", crf=18)
        .overwrite_output()
        .run()
    )


def burn_captions_remotion(trimmed_path: str, clip: dict, out_path: str) -> None:
    clip_start = clip["start"]
    duration = clip["end"] - clip_start
    captions = [
        {"text": c["text"], "start": c["start"] - clip_start, "end": c["end"] - clip_start}
        for c in clip.get("captions", [])
    ]

    # Remotion only serves video assets it can resolve via staticFile(), which
    # means the file has to live under remotion/public/ — an absolute path
    # elsewhere on disk 404s against Remotion's own render server. Copy the
    # ffmpeg-trimmed clip in under a unique name, pass just that name as the
    # videoSrc prop, and clean it up once the render is done either way.
    REMOTION_PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    public_filename = f"clip-{uuid.uuid4().hex}.mp4"
    public_path = REMOTION_PUBLIC_DIR / public_filename
    shutil.copyfile(trimmed_path, public_path)

    try:
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
            json.dump(
                {
                    "videoSrc": public_filename,
                    "durationInSeconds": duration,
                    "captions": captions,
                },
                f,
            )
            props_path = f.name

        subprocess.run(
            [
                "npx",
                "remotion",
                "render",
                "src/index.ts",
                "SocialClipCaptions",
                str(Path(out_path).resolve()),
                f"--props={props_path}",
            ],
            cwd=REMOTION_DIR,
            check=True,
        )
    finally:
        public_path.unlink(missing_ok=True)


def burn_captions_ffmpeg(trimmed_path: str, clip: dict, out_path: str) -> None:
    clip_start = clip["start"]
    video = ffmpeg.input(trimmed_path).video
    audio = ffmpeg.input(trimmed_path).audio

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

    (
        ffmpeg.output(video, audio, out_path, vcodec="libx264", acodec="aac", crf=20)
        .overwrite_output()
        .run()
    )


def render_clip(input_path: str, clip: dict, out_path: str, aspect_ratio: str, captions_engine: str) -> None:
    with tempfile.TemporaryDirectory() as tmp:
        trimmed_path = str(Path(tmp) / "trimmed.mp4")
        trim_and_crop(input_path, clip, trimmed_path, aspect_ratio)

        Path(out_path).parent.mkdir(parents=True, exist_ok=True)
        if captions_engine == "remotion":
            burn_captions_remotion(trimmed_path, clip, out_path)
        else:
            burn_captions_ffmpeg(trimmed_path, clip, out_path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to raw footage")
    parser.add_argument("--edl", required=True, help="Path to EDL JSON from step 2 (promo mode)")
    parser.add_argument("--out", required=True, help="Output directory for clip MP4s")
    parser.add_argument("--aspect-ratio", default="9:16")
    parser.add_argument("--captions", choices=["remotion", "ffmpeg"], default="remotion")
    args = parser.parse_args()

    edl = json.loads(Path(args.edl).read_text())
    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    clips = sorted(edl["clips"], key=lambda c: c.get("rank", 0))
    for i, clip in enumerate(clips, start=1):
        out_path = out_dir / f"clip-{i:02d}-rank{clip.get('rank', i)}.mp4"
        render_clip(args.input, clip, str(out_path), args.aspect_ratio, args.captions)
        print(f"Wrote {out_path} — {clip.get('hook', '')}")


if __name__ == "__main__":
    main()
