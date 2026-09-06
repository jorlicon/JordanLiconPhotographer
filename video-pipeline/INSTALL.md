# Video Pipeline — Install Plan

This installs the tools behind the automated, agent-driven video editing
workflow described in `README.md`. Run this on the machine that will
actually edit video (your workstation or a render box) — **not** inside a
Claude Code web/remote session, since nothing outside this git repo
persists there.

All ~9 tools surfaced in research are covered below, grouped by the role
they play. Install in this order — later stages depend on earlier ones.

## 0. Prerequisites

- macOS/Linux workstation with a GPU — **required, not optional, for footage running
  hours long**. whisperX at `large-v3`/`float16` needs ~10GB VRAM (a 3060 12GB,
  4070, or better works; 6-8GB cards should use `--model medium` or CPU
  `int8` instead). On GPU, transcription runs roughly 20-40x realtime, so an
  hour of footage takes a few minutes; on CPU the same hour can take
  well over an hour. NVIDIA/CUDA is what whisperX and ffmpeg's hardware
  encoder (`h264_nvenc`, worth using for long exports) both target — Apple
  Silicon works for lighter loads but isn't the CUDA path whisperX assumes.
- Python 3.10+
- Node.js 18+ (for Remotion, the caption/title renderer)
- Git
- ~15GB free disk (whisperX models), plus ~250MB already committed under
  `vendor/`, more for multi-hour raw footage

## 1. Core processing engine (required)

```bash
# FFmpeg/FFmpeg — the actual encode/decode/filter engine everything below wraps
brew install ffmpeg        # macOS
# or: sudo apt install ffmpeg   # Debian/Ubuntu

cd video-pipeline
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt   # installs kkroening/ffmpeg-python, whisperx, pyyaml, etc.
```

On Debian/Ubuntu you may hit `Failed building wheel for antlr4-python3-runtime`
(a whisperX → omegaconf dependency pinned to a version with no prebuilt
wheel, which fails to build against modern setuptools). Fix:

```bash
SETUPTOOLS_USE_DISTUTILS=stdlib pip install -r requirements.txt
```

`kkroening/ffmpeg-python` gives us a Python filtergraph API instead of
hand-built CLI strings — this is what `scripts/03_render_finish.py` and
`scripts/04_generate_social_clips.py` build on.

## 2. Transcription & forced alignment (required)

```bash
pip install whisperx   # m-bain/whisperX — already in requirements.txt
```

whisperX gives word-level timestamps, which is what lets an agent decide
"cut from word X to word Y" instead of guessing at second-level cut points.
Used by `scripts/01_transcribe.py`.

## 3. Caption/title rendering (required for nicer social clip typography)

```bash
# remotion-dev/remotion — renders the animated caption overlays used by
# scripts/04_generate_social_clips.py. Lives in video-pipeline/remotion/
# as its own small Node project (Remotion is a React/Node tool, separate
# from the Python side).
cd remotion
npm install
cd ..
```

If you'd rather skip Node entirely, pass `--captions ffmpeg` to
`scripts/04_generate_social_clips.py` to burn in plain ffmpeg `drawtext`
captions instead — no visual polish, but zero extra dependencies.

On first render, Remotion downloads its own headless Chromium — this just
works on a normal machine with internet access. It only fails in a locked-down
sandbox that blocks `remotion.media`; if you hit that, point Remotion at any
Chromium/Chrome you already have installed instead:

```bash
export REMOTION_BROWSER_EXECUTABLE=/path/to/chromium-or-chrome
```

(`remotion.config.ts` picks this up automatically when set — see that file.)

## 4. Vendored reference repos (already committed, nothing to install)

`video-pipeline/vendor/` carries a full, committed source snapshot (no
`.git` history, no submodules) of six repos surfaced during tooling
research. They're read-only references/inspiration for the agent scripts
rather than hard runtime dependencies — research-stage projects, not
stable libraries this pipeline `pip install`s or `npm install`s:

| Directory | Upstream | Role |
| --- | --- | --- |
| `vendor/video-use/` | [browser-use/video-use](https://github.com/browser-use/video-use) | AI-driven video-editing agent orchestration reference |
| `vendor/VideoAgent/` | [HKUDS/VideoAgent](https://github.com/HKUDS/VideoAgent) | Multi-modal prompt → timeline-graph orchestration reference; bundles its own nested third-party tools (`tools/seed-vc`, DiffSinger, ImageBind, CosyVoice, fish-speech) and demo assets |
| `vendor/editor/` | [diffusionstudio/editor](https://github.com/diffusionstudio/editor) | Canvas-based JS timeline/editing library reference |
| `vendor/video_manipulation/` | [aorthey/video_manipulation](https://github.com/aorthey/video_manipulation) | Python template-driven video assembly reference |
| `vendor/claude-code-video-toolkit/` | [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) | Claude Code-oriented video rendering/orchestration template |
| `vendor/awesome-claude-skills/` | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | Index of Claude skill/workflow utilities |

Each keeps its own `README`/license/dependency files as shipped upstream —
consult those before running anything inside a `vendor/` directory
standalone (e.g. `vendor/editor/` is a separate npm project, `vendor/VideoAgent/`
has its own `requirements.txt`/`pyproject.toml`). Nothing under `vendor/`
is imported by `scripts/` or `agents/` automatically; treat it as a source
of ideas/code to fold in deliberately, reviewed before use, same as any
third-party dependency, and do not run any of it as a black-box service in
production.

## 5. Verify

```bash
ffmpeg -version
python3 -c "import ffmpeg, whisperx; print('ok')"
(cd remotion && npx remotion versions)
```

## 6. Configure

Copy and edit the pipeline config:

```bash
cp config/pipeline.example.yaml config/pipeline.yaml
```

Set `raw_footage_dir`, `output_dir`, and the Anthropic API key env var
(`ANTHROPIC_API_KEY`) used by the agent decision steps.

Once this is done, see `README.md` for how to run the two pipelines.
