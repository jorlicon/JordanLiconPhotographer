#!/usr/bin/env python3
"""Step 3 — Graphics (plan stage only).

Reads the rough-cut script + the job's format config, asks a Claude agent
(agents/graphics_plan_agent.md) to propose a beat-by-beat graphics plan,
and writes it to work/graphics-plan.json.

This does NOT build the composition. Hand the resulting JSON to the
/hyperframes or /general-video skill as your brief to actually author the
HyperFrames HTML — see README.md's "Graphics is a two-stage step".
"""
import argparse
import json
import os
from pathlib import Path

import anthropic
import yaml

PRODUCTION_DIR = Path(__file__).parent.parent
AGENT_PROMPT = PRODUCTION_DIR / "agents" / "graphics_plan_agent.md"
PRESETS_DIR = PRODUCTION_DIR / "presets"
FORMATS_DIR = PRODUCTION_DIR / "formats"


def load_format(format_name: str) -> dict:
    path = FORMATS_DIR / f"{format_name}.yaml"
    if not path.exists():
        raise SystemExit(f"Unknown format {format_name!r} — no {path}")
    return yaml.safe_load(path.read_text())


def load_preset(preset_name: str) -> dict:
    path = PRESETS_DIR / f"{preset_name}.json"
    if not path.exists():
        raise SystemExit(f"Unknown preset {preset_name!r} — no {path}")
    return json.loads(path.read_text())


def plan_graphics(script_text: str, format_config: dict, preset: dict, model: str, max_tokens: int) -> dict:
    system_prompt = AGENT_PROMPT.read_text()
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    user_content = json.dumps({
        "script": script_text,
        "format": format_config,
        "preset": preset,
    })

    response = client.messages.create(
        model=model,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )
    text = "".join(block.text for block in response.content if block.type == "text")
    return json.loads(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--script", required=True, help="Path to script.md from rough_cut.py")
    parser.add_argument("--format", required=True, choices=["short-explainer", "short-tiktok-raw", "long-form-youtube"])
    parser.add_argument("--out", required=True, help="Path to write graphics-plan.json")
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--max-tokens", type=int, default=8192)
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set")

    format_config = load_format(args.format)
    preset = load_preset(format_config["graphics"]["preset"])
    script_text = Path(args.script).read_text()

    plan = plan_graphics(script_text, format_config, preset, args.model, args.max_tokens)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(plan, indent=2))

    missing = plan.get("missing_assets", [])
    print(f"Wrote {len(plan.get('beats', []))} beats to {out_path}")
    if missing:
        print("Missing assets flagged by the plan:")
        for item in missing:
            print(f"  - {item}")
    print(f"Next: hand {out_path} to /hyperframes or /general-video to build the composition.")


if __name__ == "__main__":
    main()
