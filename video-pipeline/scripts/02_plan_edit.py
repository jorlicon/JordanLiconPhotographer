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


# Above this many words (~2.5-3 hours of typical speech), a single-call EDL
# risks the model losing the thread over the whole transcript, not just
# hitting a token limit. Split multi-hour shoots into chapters/scenes and
# run this per chapter before that point — this script does not chunk for you.
WORD_COUNT_WARN_THRESHOLD = 30_000


def compact_transcript(transcript: dict) -> dict:
    # [word, start, end] tuples instead of {"word":..,"start":..,"end":..}
    # objects cut the token overhead sent to the API by roughly half on long
    # transcripts, since every repeated key name costs tokens.
    return {
        "language": transcript["language"],
        "words": [
            [w["word"], round(w["start"], 2), round(w["end"], 2)]
            for w in transcript["words"]
        ],
    }


def plan_edit(
    transcript: dict, mode: str, model: str, max_tokens: int, extra_instructions: str = ""
) -> dict:
    word_count = len(transcript["words"])
    if word_count > WORD_COUNT_WARN_THRESHOLD:
        print(
            f"WARNING: transcript has {word_count} words (~{word_count // 150} min of speech). "
            "Consider splitting this shoot into chapters and running this script per chapter — "
            "see the comment above WORD_COUNT_WARN_THRESHOLD."
        )

    system_prompt = (AGENTS_DIR / MODE_TO_PROMPT_FILE[mode]).read_text()
    system_prompt += (
        "\n\nThe transcript you receive encodes each word as a "
        "[word, start_seconds, end_seconds] array, not an object, to save space."
    )
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env

    user_content = json.dumps(compact_transcript(transcript))
    if extra_instructions:
        user_content += f"\n\nAdditional instructions: {extra_instructions}"

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
    parser.add_argument("--transcript", required=True, help="Path to transcript JSON from step 1")
    parser.add_argument("--mode", required=True, choices=list(MODE_TO_PROMPT_FILE))
    parser.add_argument("--out", required=True, help="Path to write EDL JSON")
    parser.add_argument("--model", default="claude-sonnet-5")
    parser.add_argument("--notes", default="", help="Extra instructions for this run, e.g. target length")
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=16384,
        help="Raise for long footage with many kept segments — the EDL for an hour-long "
        "shoot with hundreds of segments can exceed the previous 4096 default and get "
        "truncated mid-JSON.",
    )
    args = parser.parse_args()

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise SystemExit("ANTHROPIC_API_KEY is not set")

    transcript = json.loads(Path(args.transcript).read_text())
    edl = plan_edit(transcript, args.mode, args.model, args.max_tokens, args.notes)

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(edl, indent=2))
    print(f"Wrote EDL to {out_path}")


if __name__ == "__main__":
    main()
