# Automated, Agent-Driven Video Editing Pipeline

Turns raw footage into finished deliverables with as little manual timeline
work as possible, using Claude agents to make the editorial decisions
(what to cut, how to pace, what to caption) and FFmpeg/whisperX to execute
them precisely.

Two pipelines share the same first two stages:

```
raw footage ──► 1. transcribe ──► 2. agent: editorial decisions ──┬──► 3. render finish   → client-ready cut
                (whisperX,          (Claude agent reads the           (ffmpeg-python)
                 word-level          transcript + shot list,
                 timestamps)         proposes an edit plan as JSON)
                                                                   └──► 4. render social clips → vertical/captioned
                                                                        (ffmpeg trim/crop +      promo clips
                                                                         Remotion captions)
```

## Why this shape

- **Transcription first, always.** Word-level timestamps (whisperX) turn
  "edit this video" into a text-editing problem an LLM is actually good
  at: it reasons over a transcript, not raw pixels.
- **The agent proposes, ffmpeg executes.** The Claude agent never touches
  video bytes. It outputs a structured edit-decision-list (EDL) as JSON —
  keep/cut ranges, caption text, title-card placement. A deterministic
  ffmpeg-python script renders that EDL. This keeps output reproducible
  and debuggable: you can inspect/edit the JSON before rendering.
- **One transcript, two outputs.** The same shoot naturally produces both
  a long-form delivery cut and short social clips, so both pipelines
  branch off the same transcribe+analyze stage instead of duplicating work.

## Directory layout

```
video-pipeline/
  INSTALL.md                  — install plan for all tooling
  requirements.txt            — Python deps (ffmpeg-python, whisperx, ...)
  config/pipeline.example.yaml
  scripts/
    01_transcribe.py          — footage -> word-level transcript (JSON)
    02_plan_edit.py           — transcript -> agent-proposed EDL (JSON)
    03_render_finish.py       — EDL -> client-ready cut (ffmpeg)
    04_generate_social_clips.py — EDL -> vertical captioned clips (ffmpeg)
  agents/
    finishing_agent.md        — system prompt/spec for the long-form cut agent
    promo_agent.md            — system prompt/spec for the social-clip agent
  remotion/                   — Remotion project, renders animated captions
    src/SocialClipCaptions.tsx  — the caption/title composition
    src/Root.tsx                 — registers it, derives duration per clip
  vendor/                     — committed source snapshots of 6 reference repos (see INSTALL.md)
  production/                 — separate 7-step, job-oriented, format-aware pipeline
                                 (intake -> rough cut -> graphics -> review -> captions ->
                                 music -> export); see production/README.md
```

## Running it

```bash
source venv/bin/activate

# 1. Transcribe raw footage with word-level timestamps
python scripts/01_transcribe.py --input raw/shoot-2026-09-01.mp4 --out work/transcript.json

# 2. Ask the agent to propose an edit plan (uses agents/finishing_agent.md as system prompt)
python scripts/02_plan_edit.py --transcript work/transcript.json --mode finishing --out work/edl.json
python scripts/02_plan_edit.py --transcript work/transcript.json --mode promo     --out work/edl_promo.json

# 3a. Render the long-form client deliverable
python scripts/03_render_finish.py --input raw/shoot-2026-09-01.mp4 --edl work/edl.json --out output/final-cut.mp4

# 3b. Render short vertical social clips — ffmpeg trims/crops to 9:16,
#     then Remotion renders the animated captions on top
python scripts/04_generate_social_clips.py --input raw/shoot-2026-09-01.mp4 --edl work/edl_promo.json --out output/social/
# Skip Remotion/Node entirely and burn in plain captions with ffmpeg instead:
python scripts/04_generate_social_clips.py --input raw/shoot-2026-09-01.mp4 --edl work/edl_promo.json --out output/social/ --captions ffmpeg
```

Every stage writes plain JSON/MP4 to disk, so you can stop after step 2,
hand-edit `edl.json`, and re-render — the agent's decision is always a
reviewable artifact, never a black box.

## Tools this is built on

| Role | Tool | Notes |
|---|---|---|
| Encode/decode/filter engine | [FFmpeg/FFmpeg](https://github.com/FFmpeg/FFmpeg) | required, installed via package manager |
| Python filtergraph API | [kkroening/ffmpeg-python](https://github.com/kkroening/ffmpeg-python) | required, `pip install` |
| Word-level transcription | [m-bain/whisperX](https://github.com/m-bain/whisperX) | required, `pip install` |
| Editorial decision agent | Claude (this repo's own agent prompts) | `agents/*.md` |
| Animated caption/title rendering | [remotion-dev/remotion](https://github.com/remotion-dev/remotion) | required for `--captions remotion` (the default); `remotion/` |
| AI orchestration reference | [browser-use/video-use](https://github.com/browser-use/video-use), [HKUDS/VideoAgent](https://github.com/HKUDS/VideoAgent) | optional, vendored for ideas |
| Timeline/templating reference | [diffusionstudio/editor](https://github.com/diffusionstudio/editor), [aorthey/video_manipulation](https://github.com/aorthey/video_manipulation) | optional, vendored for ideas |
| Claude-workflow patterns | [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit), [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | optional, vendored for ideas |

See `INSTALL.md` for the full install order and rationale for each.

## Status

This is a scaffold: the two agent specs, the four scripts, and the
Remotion caption composition are written and runnable end-to-end against
the required deps (ffmpeg, ffmpeg-python, whisperX, Remotion). The six
vendored reference repos under `vendor/` are committed source snapshots,
not wired in yet — they're there to crib specific techniques from as the
pipeline matures, not required dependencies.
