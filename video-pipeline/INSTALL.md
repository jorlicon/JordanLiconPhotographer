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
- ~15GB free disk (whisperX models + vendored repos), more for multi-hour raw footage

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

## 4. Vendored reference repos (optional, clone as needed)

These are pulled in as read-only references/inspiration for the agent
scripts rather than hard runtime dependencies — they're research-stage
projects, not stable libraries to pip-install. Clone whichever you want to
borrow techniques or code from into `video-pipeline/vendor/` (gitignored):

```bash
mkdir -p vendor && cd vendor

# AI-driven orchestration reference implementations
git clone https://github.com/browser-use/video-use.git
git clone https://github.com/HKUDS/VideoAgent.git

# Editing/timeline & templating references
git clone https://github.com/diffusionstudio/editor.git
git clone https://github.com/aorthey/video_manipulation.git

# Claude-specific workflow patterns
git clone https://github.com/digitalsamba/claude-code-video-toolkit.git
git clone https://github.com/ComposioHQ/awesome-claude-skills.git

cd ..
```

Do not run these as black-box services in production — they're a source
of ideas/code to fold into `scripts/` and `agents/` deliberately, reviewed
before use, same as any third-party dependency.

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
