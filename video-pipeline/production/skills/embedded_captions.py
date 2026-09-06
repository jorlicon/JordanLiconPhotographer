#!/usr/bin/env python3
"""Step 5 — Captions (short-form only, burn-in on-beat).

Reads the rough-cut transcript, groups words into caption cues per the
format's caption spec (position/timing) and the captions-style preset
(typography), applies caption-corrections.json, and writes a caption plan.

For long-form-youtube (captions.enabled: false), this is a deliberate
no-op — that format relies on YouTube's own auto-generated CC. Pass
--burn-in to also render captions directly with ffmpeg drawtext for a
quick draft; for the polished on-beat treatment described in the diagram,
hand caption-plan.json to the /embedded-captions skill instead, which
implements the full rail/embed model (see captions-overlay).
"""
import argparse
import json
import re
from pathlib import Path

import ffmpeg
import yaml

PRODUCTION_DIR = Path(__file__).parent.parent
PRESETS_DIR = PRODUCTION_DIR / "presets"
FORMATS_DIR = PRODUCTION_DIR / "formats"

# on-beat timing groups words into short per-cue chunks; locked timing
# groups by sentence-ish pause instead — see group_on_beat vs group_locked
ON_BEAT_MAX_WORDS = 3
LOCKED_GAP_SECONDS = 0.6


def load_format(format_name: str) -> dict:
    return yaml.safe_load((FORMATS_DIR / f"{format_name}.yaml").read_text())


def load_json(name: str) -> dict:
    return json.loads((PRESETS_DIR / f"{name}.json").read_text())


def load_corrections() -> dict:
    return load_json("caption-corrections").get("corrections", {})


def apply_corrections(text: str, corrections: dict) -> str:
    for wrong in sorted(corrections, key=len, reverse=True):
        text = re.sub(re.escape(wrong), corrections[wrong], text, flags=re.IGNORECASE)
    return text


def group_on_beat(words: list) -> list:
    cues = []
    for i in range(0, len(words), ON_BEAT_MAX_WORDS):
        chunk = words[i:i + ON_BEAT_MAX_WORDS]
        cues.append({"start": chunk[0]["start"], "end": chunk[-1]["end"], "text": " ".join(w["word"] for w in chunk)})
    return cues


def group_locked(words: list) -> list:
    cues = []
    for w in words:
        if cues and w["start"] - cues[-1]["end"] <= LOCKED_GAP_SECONDS:
            cues[-1]["end"] = w["end"]
            cues[-1]["text"] += " " + w["word"]
        else:
            cues.append({"start": w["start"], "end": w["end"], "text": w["word"]})
    return cues


def build_caption_plan(transcript: dict, format_config: dict, style: dict, corrections: dict) -> dict:
    caption_config = format_config.get("captions", {})
    if not caption_config.get("enabled", True):
        return {"enabled": False, "note": caption_config.get("note", ""), "cues": []}

    words = transcript["words"]
    timing = caption_config.get("timing", "locked")
    cues = group_on_beat(words) if timing == "on-beat" else group_locked(words)

    for cue in cues:
        cue["text"] = apply_corrections(cue["text"].strip(), corrections)

    return {
        "enabled": True,
        "position": caption_config.get("position", "centered"),
        "timing": timing,
        "style": style,
        "cues": cues,
    }


def burn_in_ffmpeg(input_path: str, plan: dict, out_path: str) -> None:
    video = ffmpeg.input(input_path).video
    audio = ffmpeg.input(input_path).audio

    y_expr = "h-260" if plan["position"] == "low-under-face" else "(h-text_h)/2"
    for cue in plan["cues"]:
        text = cue["text"].replace(":", r"\:").replace("'", r"\'")
        video = video.drawtext(
            text=text,
            fontsize=64,
            fontcolor=plan["style"].get("color", "#ffffff"),
            borderw=plan["style"].get("stroke", {}).get("width_px", 3),
            bordercolor=plan["style"].get("stroke", {}).get("color", "#000000"),
            x="(w-text_w)/2",
            y=y_expr,
            enable=f"between(t,{cue['start']},{cue['end']})",
        )

    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    ffmpeg.output(video, audio, out_path, vcodec="libx264", acodec="aac", crf=20).overwrite_output().run()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transcript", required=True, help="Path to transcript.json from rough_cut.py")
    parser.add_argument("--format", required=True, choices=["short-explainer", "short-tiktok-raw", "long-form-youtube"])
    parser.add_argument("--out", required=True, help="Path to write caption-plan.json")
    parser.add_argument("--input", help="Rendered clip to burn captions into (required with --burn-in)")
    parser.add_argument("--burn-in", help="Also render a quick-draft burned-in MP4 to this path")
    args = parser.parse_args()

    format_config = load_format(args.format)
    if not format_config.get("captions", {}).get("enabled", True):
        print(f"Format {args.format} has captions disabled ({format_config['captions'].get('note', '')}) — skipping.")
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(json.dumps({"enabled": False, "cues": []}, indent=2))
        return

    style = load_json(format_config["captions"]["style"])
    corrections = load_corrections()
    transcript = json.loads(Path(args.transcript).read_text())

    plan = build_caption_plan(transcript, format_config, style, corrections)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(plan, indent=2))
    print(f"Wrote {len(plan['cues'])} caption cues to {out_path}")

    if args.burn_in:
        if not args.input:
            raise SystemExit("--input is required with --burn-in")
        burn_in_ffmpeg(args.input, plan, args.burn_in)
        print(f"Wrote {args.burn_in}")
    else:
        print("For polished on-beat captions rather than a plain ffmpeg burn-in, "
              f"hand {out_path} to the /embedded-captions skill.")


if __name__ == "__main__":
    main()
