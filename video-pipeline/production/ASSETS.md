# Sourcing assets from Envato Elements and Audiio

Neither this pipeline nor any Claude Code session can log into your Envato
Elements or Audiio.com accounts — there's no credential or connector for
either, and no script here attempts to scrape or authenticate against
them. Every asset (music bed, SFX, stock B-roll, licensed graphic) has to
be **downloaded by you and placed in the job's `assets/` folder** before
the step that needs it runs.

## Per-job convention

```
projects/<job>/assets/
  assets.yaml       — manifest: what each file is, where it came from, license note
  music/
    <file>.mp3
  sfx/
    <file>.wav
  broll/
    <file>.mp4
  graphics/
    <file>.png
```

`assets.yaml` is a plain record, not something scripts parse automatically
— `background_music.py` and `graphics_plan.py` take file paths directly
via `--music`/`--broll`/etc. flags. Keep it anyway so a job's licensing
trail doesn't live only in your memory:

```yaml
# projects/my-job/assets/assets.yaml
music:
  - file: music/audiio-uplift-corporate.mp3
    source: https://audiio.com/track/12345
    license: Audiio subscription, cleared for client delivery
graphics:
  - file: graphics/envato-lower-third-pack-04.png
    source: https://elements.envato.com/item/XXXXXXX
    license: Envato Elements subscription license
```

## Workflow

1. Browse [Audiio](https://audiio.com/browse) or Envato Elements yourself
   and pick the track/asset for the job.
2. Download it through your account (both require an active login this
   session doesn't have).
3. Drop the file under `projects/<job>/assets/{music,sfx,broll,graphics}/`.
4. Add a line to `assets.yaml` recording where it came from and the
   license basis — this is what protects you if a client ever asks.
5. Point the relevant step at it by path:
   ```bash
   python skills/background_music.py \
     --input projects/my-job/work/rough-cut.mp4 \
     --music projects/my-job/assets/music/audiio-uplift-corporate.mp3 \
     --out projects/my-job/work/scored.mp4
   ```

## If you'd rather not download anything yet

`run_pipeline.py` doesn't block on missing assets — background music
(step 6) is explicitly optional, and graphics (step 3) can plan beats that
only reference a preset (colors/fonts/motion), not a licensed asset, until
you're ready. If a specific shot or graphic really can't be built without
a licensed asset you haven't pulled yet, follow the same rule used
elsewhere in this repo: insert a clearly labeled placeholder and list the
missing asset (a `MISSING-ASSETS.md` in the job folder) rather than
substituting unlicensed stock as if it were the real thing.
