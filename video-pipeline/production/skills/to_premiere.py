#!/usr/bin/env python3
"""Step 2 off-ramp — export the rough-cut EDL as an FCPXML sequence so the
raw footage and cut points can be opened directly in Premiere Pro for
manual finishing, instead of continuing through steps 3-7 here.

Premiere Pro imports FCPXML (File > Import) and rebuilds a sequence from
it referencing the original media file by path — nothing is re-encoded.
"""
import argparse
import json
from pathlib import Path
from xml.sax.saxutils import escape

FPS = 30  # frame rate assumed for frame-accurate timecode; override with --fps if the source differs


def seconds_to_frames(seconds: float, fps: int) -> int:
    return round(seconds * fps)


def build_fcpxml(input_path: str, segments: list, fps: int) -> str:
    media_name = Path(input_path).name
    media_abs = str(Path(input_path).resolve())

    clipitems = []
    timeline_cursor = 0
    for i, seg in enumerate(segments, start=1):
        in_frame = seconds_to_frames(seg["start"], fps)
        out_frame = seconds_to_frames(seg["end"], fps)
        duration = out_frame - in_frame
        clipitems.append(f"""
        <clipitem id="clipitem-{i}">
          <name>{escape(media_name)}</name>
          <duration>{duration}</duration>
          <rate><timebase>{fps}</timebase></rate>
          <start>{timeline_cursor}</start>
          <end>{timeline_cursor + duration}</end>
          <in>{in_frame}</in>
          <out>{out_frame}</out>
          <file id="file-1">
            <name>{escape(media_name)}</name>
            <pathurl>file://localhost{escape(media_abs)}</pathurl>
            <rate><timebase>{fps}</timebase></rate>
          </file>
        </clipitem>""")
        timeline_cursor += duration

    total_duration = timeline_cursor

    return f"""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE xmeml>
<xmeml version="5">
  <sequence>
    <name>rough-cut</name>
    <duration>{total_duration}</duration>
    <rate><timebase>{fps}</timebase></rate>
    <media>
      <video>
        <track>{"".join(clipitems)}
        </track>
      </video>
      <audio>
        <track>{"".join(clipitems)}
        </track>
      </audio>
    </media>
  </sequence>
</xmeml>
"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, help="Path to the raw footage referenced by the EDL")
    parser.add_argument("--edl", required=True, help="Path to edl.json from rough_cut.py")
    parser.add_argument("--out", required=True, help="Path to write the .fcpxml")
    parser.add_argument("--fps", type=int, default=FPS)
    args = parser.parse_args()

    edl = json.loads(Path(args.edl).read_text())
    xml = build_fcpxml(args.input, edl["segments"], args.fps)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(xml)
    print(f"Wrote {out_path} — import into Premiere Pro via File > Import")


if __name__ == "__main__":
    main()
