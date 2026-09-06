---
name: licanpipeline
description: Runs Jordan Licon Photographer's own 7-step video production pipeline (intake, rough cut, graphics, review, captions, background music, export) already implemented at video-pipeline/production/ in this repo, with format variants for short-explainer, short-tiktok-raw, and long-form-youtube deliverables. Use this skill whenever the user wants to edit, cut, produce, or finish a video from raw footage for this business — "run the pipeline", "edit this footage", "make the TikTok cut", "produce the YouTube version", "process this shoot for [client]", "/licanpipeline" — even if they don't name the pipeline or its steps explicitly. This wraps the existing pipeline; do not reimplement its logic inline or invent a different workflow.
---

# Lican Pipeline

This skill is the entry point for running a video through Jordan Licon
Photographer's bespoke 7-step production pipeline. The pipeline itself
already exists at `video-pipeline/production/` in this repo — this skill
tells you how to actually drive it for a real job, not how it works
internally (that's `video-pipeline/production/README.md`).

**Before doing anything else, read these three files in full:**
- `video-pipeline/production/README.md` — the 7 steps, the 3 format
  variants, the locked presets, the directory layout.
- `video-pipeline/production/ASSETS.md` — how Envato Elements / Audiio
  assets get into a job.
- `video-pipeline/production/job.example.yaml` — the per-job config shape.

They're short and this skill assumes you've read them — don't guess at
flags or paths the pipeline's own scripts already document.

## The 7 steps, in one line each

1. **Intake** — copy the raw clip into `projects/<job>/raw/`.
2. **Rough cut** — `rough_cut.py`: whisperX transcribes, filler words are
   cut, audio is loudness-normalized, a clean script is written. Off-ramp:
   `to_premiere.py` exports an FCPXML if the job is finishing in Premiere
   Pro instead of continuing here.
3. **Graphics** *(format-specific)* — `graphics_plan.py` asks an agent to
   propose a beat-by-beat graphics plan as JSON. It does not render
   anything.
4. **Second pass** — a human reviews the composited draft. Always manual.
5. **Captions** *(format-specific)* — `embedded_captions.py` builds a
   caption plan (skipped entirely for `long-form-youtube`, which relies on
   YouTube's own CC).
6. **Background music** *(optional)* — `background_music.py` sidechain-
   ducks a music bed under the voice track and re-normalizes.
7. **Export** — `finalize.sh` promotes the render to
   `projects/<job>/outputs/<job>.final.mp4`, `prune.sh` cleans up.

Only steps 3 and 5 change between the three formats
(`short-explainer`, `short-tiktok-raw`, `long-form-youtube`) — everything
else runs identically. `run_pipeline.py` is the orchestrator; it runs the
scripted steps and deliberately stops wherever a human or a creative pass
is required, rather than guessing.

## Running a job end to end

1. **Gather what you need**, if the user hasn't already given it:
   - the raw clip (a local path, or something to be transferred in)
   - which format: `short-explainer`, `short-tiktok-raw`, or `long-form-youtube`
   - whether a music bed is ready yet (fine if not — step 6 is optional)

2. **Set up the job**:
   ```bash
   cd video-pipeline/production
   mkdir -p projects/<job>
   cp job.example.yaml projects/<job>/job.yaml
   # edit projects/<job>/job.yaml: job, format, raw_clip, music (if any)
   ```

3. **Run steps 1-3**:
   ```bash
   python run_pipeline.py --job projects/<job>/job.yaml
   ```
   This copies the raw clip in, runs the whisperX rough cut, and writes
   `work/graphics-plan.json` — then stops on purpose.

4. **Build the graphics** — read `work/graphics-plan.json`, then invoke
   the `/hyperframes` or `/general-video` skill using that plan as your
   brief to actually author the HyperFrames composition. This is a
   creative authoring pass, not something `run_pipeline.py` can do for
   you (see the production README's "Graphics is a two-stage step").

5. **Wait for the step-4 review** — once the reviewed/composited draft is
   saved as `work/composited.mp4`, you're clear to continue. Don't
   fabricate this step or skip straight past it; it's in the pipeline
   because someone needs to actually look at the cut.

6. **Resume steps 5-7**:
   ```bash
   python run_pipeline.py --job projects/<job>/job.yaml --resume-from 5
   ```
   This builds the caption plan, mixes in music if one was given, and
   exports `projects/<job>/outputs/<job>.final.mp4`.

7. **For polished, on-beat captions** rather than the plain ffmpeg draft
   `embedded_captions.py` can burn in, hand `work/caption-plan.json` to
   the `/embedded-captions` skill instead.

## Constraints — don't work around these

- **whisperX needs a GPU.** Step 2 cannot run end-to-end inside a Claude
  Code remote/web session — there's no GPU and no real footage there. In
  that context, still scaffold the job (`job.yaml`, directory layout) and
  prepare what you can (e.g. draft the graphics-plan agent call), but say
  plainly that the actual render happens on the user's own workstation
  per `video-pipeline/INSTALL.md`. Don't claim a render completed if it
  didn't.
- **`graphics_plan.py` needs `ANTHROPIC_API_KEY`** set in the environment
  it runs in (it calls the Anthropic API directly, separate from you).
- **Envato Elements and Audiio.com require a login this session doesn't
  have.** Never invent, scrape, or substitute an asset for either — ask
  the user to download it through their own account and drop it under
  `projects/<job>/assets/` per `ASSETS.md`. If a job needs one you don't
  have yet, say so and offer to placeholder it rather than proceeding as
  if it were in hand.
- **The locked presets are brand-level, not per-job.** `signature-style`,
  `captions-style`, `tiktok-raw-style`, `liquid-glass-style`, and
  `caption-corrections` in `video-pipeline/production/presets/` define
  the look — don't invent a new color, font, or motion style outside them
  for a single job without checking with the user first.
