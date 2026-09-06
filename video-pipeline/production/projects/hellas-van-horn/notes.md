# Hellas / Van Horn Eagles Stadium — job notes

Source: local DaVinci Resolve project **"2026-08-04 Hellas - Van Horn"**.
Target: 5-minute overview video (`long-form-youtube` format).

## Starting fresh — do not conform the existing v9 timeline

The Resolve project already has a built timeline ("Van Horn - v9", ~5:50)
assembled from raw footage at
`/Volumes/JordanExternalDrive6 SSD/Pictures/2026/2026-08-04 Hellas - Van Horn/`
(Mavic Mini 2, Phantom 4 Pro, iPhone 17 Pro Max, a7R IV stills, audio).
**The client/editor has reviewed v9 and rejected it — a lot of the cuts
aren't good. Do not use v9 as this job's `raw_clip`.** Start this pipeline
from the raw camera sources instead, re-cutting from scratch.

Practical step before `rough_cut.py` can run: the raw sources are four
unsynced cameras plus separate audio — whisperX needs one coherent video
file, not four. Do a **multicam sync pass in Resolve first** (align the
sources, flatten to one exported file — no creative cutting decisions at
this stage, just sync), then point `raw_clip` at that export.

## Why this job can't run past scaffolding in this session

This is a remote Claude Code session with no path to:
- **DaVinci Resolve** — it's a local desktop app, reachable only through a
  local `davinci-resolve-mcp` server running on your machine. Not
  connectable from here.
- **A GPU** — `rough_cut.py` (step 2) needs one for whisperX; this
  environment has none.
- **Envato Elements / Audiio.com** — no login/connector for either.

So steps 1-2 (and therefore everything after, since it's all downstream of
the transcript) have to run in a session opened locally, on this repo's
`main`, with DaVinci Resolve and a GPU actually available.

## To pick this up locally

1. Open a Claude Code session in a local clone of this repo, on `main`
   (that's what makes `/licanpipeline` and the `davinci-resolve-mcp` skill
   both available — `/licanpipeline` needs the repo, `davinci-resolve-mcp`
   needs your local MCP server connected).
2. Export the raw footage from the "2026-08-04 Hellas - Van Horn" DaVinci
   project to `video-pipeline/production/projects/hellas-van-horn/raw/`
   (or update `job.yaml`'s `raw_clip` path to wherever you export it).
3. Invoke `/licanpipeline` and pick up from step 1 — `job.yaml` here is
   already set up (`format: long-form-youtube`).

## What's already researched (see conversation for full detail)

**Company**: Hellas (hellas.com), Austin TX — America's largest sports
contractor: turf, tracks, courts, sports lighting. NFL + high-school/college
client roster.

**The Van Horn project**: Culberson County–Allamore ISD, ~$6M renovation of
Van Horn Eagles Stadium — Matrix® Synthetic Turf, epiQ TRACKS™ V300 (400m),
new field house w/ weight room, Major Play® softball turf w/ lights,
scoreboards, bleachers, dugout. Public press ties this to a 2014 opening —
**unconfirmed whether the 2026-08-04 project is a new phase, an anniversary
piece, or something else**. Check the actual DaVinci project/footage for
what this shoot is really about before finalizing the script.

**Video style**: `hellas.com` and `youtube.com` are blocked by this
environment's network egress — style below is inferred from search-result
video titles only, NOT verified by watching actual Hellas footage. Confirm
against 1-2 real Hellas videos before locking the visual treatment.
Hellas's own video titles follow: *"[Activity] with Hellas Construction at
[School], [City], TX"* — suggests a recurring case-study/documentary format
across many projects. Their own tagline: *"building home field advantage
for small towns and cities in West Texas."*

## Draft 5-minute beat structure (pending your review)

| Time | Beat |
|---|---|
| 0:00–0:20 | Cold open — aerial establishing shot, small-town/big-investment contrast |
| 0:20–1:00 | Company intro — who Hellas is, stat graphics |
| 1:00–2:30 | The Van Horn story — challenge, scope, installation footage, interview |
| 2:30–3:30 | Community impact — game-day footage, "home field advantage" theme |
| 3:30–4:30 | Craftsmanship — install process, durability, drone flyover |
| 4:30–5:00 | Close — logo, CTA, contact |

Format is `long-form-youtube`: 16:9, glass+zoom graphics preset, no burned
captions (rely on YouTube CC), thumbnail always generated. Feed this beat
structure as extra context to `graphics_plan.py` / the `/hyperframes`
authoring pass once the rough cut exists.
