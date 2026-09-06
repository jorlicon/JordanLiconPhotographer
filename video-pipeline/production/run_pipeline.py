#!/usr/bin/env python3
"""Orchestrator for the 7-step production pipeline (see README.md).

Runs the scripted steps in order and stops to print instructions whenever
a step needs a human or a creative pass, rather than guessing:

  1. Intake          — scripted (file copy)
  2. Rough cut        — scripted (rough_cut.py)
                         [off-ramp available any time: to_premiere.py]
  3. Graphics         — scripted PLAN only (graphics_plan.py), then STOPS —
                         build the actual composition via /hyperframes or
                         /general-video using work/graphics-plan.json
  4. Second pass      — MANUAL, always stops here for your review
  5. Captions         — scripted (embedded_captions.py), skipped for formats
                         with captions disabled
  6. Background music — scripted (background_music.py), skipped if no
                         --music / job.yaml music path is given
  7. Export           — scripted (finalize.sh + prune.sh)

Run with --resume-from to continue a job past a stopped step once you've
done the manual part (e.g. --resume-from 4 after building graphics and
compositing your review draft into work/composited.mp4).
"""
import argparse
import subprocess
import sys
from pathlib import Path

import yaml

PRODUCTION_DIR = Path(__file__).parent
SKILLS_DIR = PRODUCTION_DIR / "skills"

STEPS = ["intake", "rough_cut", "graphics_plan", "second_pass", "captions", "background_music", "export"]


def load_job(job_path: Path) -> dict:
    job = yaml.safe_load(job_path.read_text())
    job["_dir"] = job_path.parent
    return job


def step_intake(job: dict) -> None:
    raw_dir = job["_dir"] / "raw"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_clip = Path(job["raw_clip"])
    dest = raw_dir / raw_clip.name
    if dest.exists():
        print(f"[1/7 intake] {dest} already present, skipping copy")
        return
    if not raw_clip.exists():
        raise SystemExit(f"[1/7 intake] raw_clip not found: {raw_clip}")
    dest.write_bytes(raw_clip.read_bytes())
    print(f"[1/7 intake] copied {raw_clip} -> {dest}")


def step_rough_cut(job: dict) -> Path:
    work_dir = job["_dir"] / "work"
    raw_clip = job["_dir"] / "raw" / Path(job["raw_clip"]).name
    subprocess.run([
        sys.executable, str(SKILLS_DIR / "rough_cut.py"),
        "--input", str(raw_clip),
        "--work-dir", str(work_dir),
        "--model", job.get("model", "large-v3"),
        "--device", job.get("device", "cuda"),
        "--render",
    ], check=True)
    print(f"[2/7 rough cut] done — review work/script.md, or run to_premiere.py to hand off to Premiere Pro")
    return work_dir


def step_graphics_plan(job: dict, work_dir: Path) -> None:
    subprocess.run([
        sys.executable, str(SKILLS_DIR / "graphics_plan.py"),
        "--script", str(work_dir / "script.md"),
        "--format", job["format"],
        "--out", str(work_dir / "graphics-plan.json"),
    ], check=True)
    print(
        "[3/7 graphics] plan written. STOPPING HERE — build the composition:\n"
        f"    hand {work_dir / 'graphics-plan.json'} to /hyperframes or /general-video,\n"
        f"    then save the composited draft as {work_dir / 'composited.mp4'}\n"
        "    and re-run with --resume-from 4."
    )


def step_captions(job: dict, work_dir: Path) -> Path:
    composited = work_dir / "composited.mp4"
    if not composited.exists():
        raise SystemExit(f"[5/7 captions] expected {composited} from your step-3/4 work — not found")

    subprocess.run([
        sys.executable, str(SKILLS_DIR / "embedded_captions.py"),
        "--transcript", str(work_dir / "transcript.json"),
        "--format", job["format"],
        "--out", str(work_dir / "caption-plan.json"),
    ], check=True)
    print(f"[5/7 captions] plan written to {work_dir / 'caption-plan.json'} "
          "(hand it to /embedded-captions for the polished on-beat render)")
    return composited


def step_background_music(job: dict, work_dir: Path, current: Path) -> Path:
    music = job.get("music")
    if not music:
        print("[6/7 background music] no music configured for this job — skipping")
        return current

    scored = work_dir / "scored.mp4"
    subprocess.run([
        sys.executable, str(SKILLS_DIR / "background_music.py"),
        "--input", str(current),
        "--music", str(music),
        "--out", str(scored),
    ], check=True)
    print(f"[6/7 background music] wrote {scored}")
    return scored


def step_export(job: dict, current: Path) -> None:
    subprocess.run(["bash", str(SKILLS_DIR / "finalize.sh"), str(job["_dir"]), str(current)], check=True)
    subprocess.run(["bash", str(SKILLS_DIR / "prune.sh"), str(job["_dir"])], check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--job", required=True, help="Path to job.yaml")
    parser.add_argument(
        "--resume-from", type=int, default=1, choices=range(1, 8),
        help="Step number to resume from (1-7) — use after completing a manual step",
    )
    args = parser.parse_args()

    job_path = Path(args.job)
    job = load_job(job_path)
    work_dir = job["_dir"] / "work"

    if args.resume_from <= 1:
        step_intake(job)
    if args.resume_from <= 2:
        step_rough_cut(job)
    if args.resume_from <= 3:
        step_graphics_plan(job, work_dir)
        if args.resume_from <= 3:
            return  # always stop after planning graphics — steps 3/4 need you

    if args.resume_from == 4:
        composited = work_dir / "composited.mp4"
        if not composited.exists():
            raise SystemExit(
                f"[4/7 second pass] {composited} not found — composite your reviewed draft there, "
                "then re-run with --resume-from 5"
            )
        print(f"[4/7 second pass] found {composited} — proceeding to captions")

    current = step_captions(job, work_dir)
    current = step_background_music(job, work_dir, current)
    step_export(job, current)


if __name__ == "__main__":
    main()
