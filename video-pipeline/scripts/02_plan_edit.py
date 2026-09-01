#!/usr/bin/env python3
"""Send a transcript to a Claude agent (finishing_agent.md or
promo_agent.md) and get back a structured edit-decision-list (EDL) as
JSON. This is the only stage that calls an LLM — every other stage is
deterministic ffmpeg.
"""
import argparse
import json
import os
from pathlib import Path

import anthropic

SCRIPT_DIR = Path(__file__).parent
AGENTS_DIR = SCRIPT_DIR.parent / "agents"

MODE_TO_PROMPT_FILE = {
    "finishing": "finishing_agent.md",
    "promo": "promo_agent.md",
}


def plan_edit(transcript: dict, mode: str, model: str, extra_instructions: str = "") -> dict:
    system_prompt = (AGENTS_DIR / MODE_TO_PROMPT_FILE[mode]).read_text()
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    user_content = json.dumps(transcript)
    if extra_instructions:
        user_content += f"\n\nAdditional instructions: {extra_instructions}"

    response = client.messages.create(
        model=model,
        max_tokens=4096,
        system=system_prompt,
        messages=[{"role": "user", "content": user_content}],
    )

    text = "".join(block.text for block in response.content if block.type == "text")
    return json.loads(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--transcript", required=True, help="Path to transcript JSON from step 1")
    parser.add_argument("--mode", required=True, choices=list(MODE_TO_PROMPT_FILE))
    parser.add_argument("--out", required=True, help="Path to write EDL JSON")
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--notes", default="", help="Extra instructions for this run, e.g. target length")
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set")

    transcript = json.loads(Path(args.transcript).read_text())
    edl = plan_edit(transcript, args.mode, args.model, args.notes)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(edl, indent=2))
    print(f"Wrote EDL to {out_path}")


if __name__ == "__main__":
    main()
