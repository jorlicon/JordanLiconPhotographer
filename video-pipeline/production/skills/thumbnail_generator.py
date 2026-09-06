#!/usr/bin/env python3
"""Thumbnail generator — used by step 7 when the job's format wants one
(only long-form-youtube does by default; see formats/*.yaml thumbnail.generate).

Extracts still frames at given timestamps (or picks evenly-spaced
candidates if none given) from the finished render, for you to pick a
thumbnail from — this does not auto-select "the best" frame or add text.
"""
import argparse
from pathlib import Path

import ffmpeg


def probe_duration(input_path: str) -> float:
    return float(ffmpeg.probe(input_path)["format"]["duration"])


def extract_frame(input_path: str, timestamp: float, out_path: str) -> None:
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    (
        ffmpeg.input(input_path, ss=timestamp)
        .output(out_path, vframes=1, **{"q:v": 2})
        .overwrite_output()
        .run()
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the finished/rendered clip")
    parser.add_argument("--out-dir", required=True, help="Directory to write candidate thumbnail JPEGs into")
    parser.add_argument(
        "--at", action="append", type=float, default=[],
        help="Specific timestamp(s) in seconds to extract, e.g. --at 4.5 --at 12.0. "
        "If omitted, extracts 5 evenly-spaced candidates.",
    )
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    timestamps = args.at
    if not timestamps:
        duration = probe_duration(args.input)
        n = 5
        timestamps = [duration * (i + 1) / (n + 1) for i in range(n)]

    for i, t in enumerate(timestamps, start=1):
        out_path = out_dir / f"thumb-{i:02d}-{t:.1f}s.jpg"
        extract_frame(args.input, t, str(out_path))
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
