# Production Pipeline — 7 steps, every job, raw to done

This is the second, job-oriented pipeline in `video-pipeline/`: a fixed
7-step sequence that every edit goes through regardless of output format,
with exactly two steps (Graphics, Captions) branching by format. It sits
alongside — not instead of — the finishing/promo scripts one level up
(`video-pipeline/scripts/`), which remain a separate, simpler two-output
pipeline (long-form cut + social clips) for jobs that don't need the full
review/graphics/format machinery below.

```
1. Intake          copy raw clip into projects/<job>/raw/
2. Rough cut       whisperX cut, kill filler, polish audio, makes the script  ──► (off-ramp: to_premiere.py)
3. Graphics        plan beats, then build the graphics                        [format-specific]
4. Second pass     you review, incremental re-composite                       [manual]
5. Captions        short-form only, burn-in on-beat                           [format-specific]
6. Background music  optional, sidechain duck, re-normalize                  [optional]
7. Export          promote to outputs/<job>.final.mp4                        → ship
```

## Format variants — only steps 3 & 5 change

| | short-explainer | short-tiktok-raw | long-form-youtube |
|---|---|---|---|
| format | 9:16, 1080×1920 | 9:16, 1080×1920 | 16:9, 1920×1080 |
| graphics (step 3) | top-half cards | hook card → raw | glass + zoom |
| captions (step 5) | centered, locked | low, under face | none (rely on YouTube CC) |
| thumbnail | usually skip | skip | always |

Config per variant lives in `formats/*.yaml`. Everything else — intake,
rough cut, review, music, export — runs identically no matter the format.

## Directory layout

```
video-pipeline/production/
  README.md            — this file
  ASSETS.md             — how Envato Elements / Audiio assets get into a job
  formats/               — the 3 format variants above (steps 3 & 5 config)
    short-explainer.yaml
    short-tiktok-raw.yaml
    long-form-youtube.yaml
  presets/                — locked, brand-level style presets (do not fork per-job)
    signature-style.json     — default graphics look (fonts, colors, card motion)
    captions-style.json      — default caption typography (the quiet rail)
    tiktok-raw-style.json    — native/raw graphics treatment for TikTok
    liquid-glass-style.json  — glassmorphism treatment for long-form
    caption-corrections.json — upstream brand-name & recurring spelling fixes
  agents/
    graphics_plan_agent.md  — system prompt for the step-3 beats-planning agent
  skills/                 — one script per pipeline step
    rough_cut.py            — step 2
    to_premiere.py          — step 2 off-ramp (dashed path in the diagram)
    graphics_plan.py        — step 3 (plan only — see "Graphics is a two-stage step" below)
    embedded_captions.py    — step 5
    background_music.py     — step 6
    thumbnail_generator.py  — helper used by step 7 when a format wants a thumbnail
    finalize.sh             — step 7
    prune.sh                — step 7 cleanup
  run_pipeline.py         — orchestrator: runs 1→2→(3 plan)→[you: 3 build, 4]→5→6→7
  job.example.yaml        — per-job manifest template
  projects/               — created per job at runtime (gitignored except raw manifests)
    <job>/
      raw/                — step 1 output
      work/               — intermediate artifacts (transcript, EDL, caption plan, ...)
      assets/             — Envato/Audiio files you've downloaded for this job (see ASSETS.md)
      outputs/            — step 7 output: <job>.final.mp4
```

## Engine: HyperFrames toolkit

Graphics (step 3) and, for short-form captions (step 5), the actual pixel
rendering is done by **HyperFrames** — the HTML-based video engine already
installed at the repo root (`.claude/skills/hyperframes*`,
`.agents/skills/hyperframes*`, tracked by `skills-lock.json`). That
installation is managed by the skills registry — **never hand-edit those
directories**; update via `npx skills update hyperframes` the same way it
was installed.

### Graphics is a two-stage step

`graphics_plan.py` does **not** render pixels. It reads the rough-cut
script/EDL plus the job's format config and locked style preset, and asks
a Claude agent (`agents/graphics_plan_agent.md`) to propose a beat-by-beat
graphics plan as JSON (`work/graphics-plan.json` — timestamp, beat type,
text, which preset it draws from). Building the actual HyperFrames HTML
composition from that plan is a creative/authoring pass — hand
`work/graphics-plan.json` to the `/hyperframes` or `/general-video` skill
as your brief, the same way any other HyperFrames project gets built. This
matches the diagram's own arrow: "graphics-plan → HyperFrames", not
"graphics-plan → finished video."

### Step 5 (captions) is format-specific, and skipped for long-form

`embedded_captions.py` reads the rough-cut transcript, applies
`caption-corrections.json`, and applies the format's caption spec (style,
position, timing) to produce a caption plan. For `long-form-youtube`
(captions: none — rely on YouTube's own CC), the script is a no-op by
design; don't force burned-in captions onto that format.

## Step 4 is manual, on purpose

There is no script for "Second pass." You (or whoever is doing the
creative review — "Jason" in the diagram) look at the composited draft
from step 3, give feedback, and `run_pipeline.py` re-composites
incrementally rather than re-running steps 1-3 from scratch. This is a
human checkpoint, not an automation gap.

## Running a job

```bash
cd video-pipeline/production
cp job.example.yaml projects/my-job/job.yaml   # edit: format, raw clip path
python run_pipeline.py --job projects/my-job/job.yaml
```

`run_pipeline.py` walks the 7 steps in order, stopping to print
instructions whenever a step needs you (graphics authoring, the step-4
review, or confirming background music assets are in place) rather than
guessing on your behalf.

See `ASSETS.md` before step 3 or step 6 on any job that needs stock music,
SFX, or licensed graphics from Envato Elements or Audiio.
