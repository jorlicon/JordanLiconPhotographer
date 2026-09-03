# Missing assets — export from the DaVinci Resolve project

Source: **ENOVA MED SPA - CAMRYN** (local DaVinci Resolve project, not
reachable from this environment). Nothing below exists in this HyperFrames
project yet — every numbered item is currently a labeled placeholder in
`compositions/frames/`. Export each item, drop it into `assets/` (create
subfolders as convenient), then swap the matching placeholder for the real
media and re-run `npm run check`.

Per the client brief: no substitute stock/generic footage — if a shot below
isn't available, leave the placeholder in place rather than filling the gap
with anything else.

## Frame 1 — Location and introduction (0:00–0:06)

1. Exterior establishing shot — El Paso Country Club, Enova signage visible
2. Interior — reception / entrance
3. Treatment room — clean, styled, empty or nearly empty
4. Detail shots — clean linens, lighting fixtures, product staging
5. Camryn entering the space (walk-in or door shot)
6. Enova logo, high-resolution, transparent background (also needed for
   Frame 6)

## Frame 2 — Personalized experience (0:06–0:16)

7. Camryn greeted/welcomed at reception or in a treatment room
8. Camryn speaking with a provider (consultation)
9. Mirror moment — Camryn looking in a mirror
10. Individualized facial/skin assessment in progress (close-up, non-clinical)

## Frame 3 — Treatments and technology montage (0:16–0:30)

11. Facial treatment in progress (product application, clean hands)
12. Skincare product close-ups (bottles, packaging, textures)
13. OxyGeneo or Hydrafacial equipment in use
14. Morpheus8 device — preparation/equipment shot only, non-graphic
15. Injectable preparation — tasteful, discreet (no needle-in-skin close-up
    unless pre-approved by the client as appropriate)
16. PRP or PDRN detail shot — packaging/prep, not a graphic procedure shot
17. Massage therapy in progress
18. Body treatment / body contouring — equipment or prep shot

## Frame 4 — Trust and natural results (0:30–0:43)

19. Provider explaining a treatment to Camryn (professional interaction)
20. Facial mapping shot (marking/assessment, non-graphic)
21. Camryn relaxing + a confident beauty portrait (can reuse a portrait from
    Frame 5 if only one is available)

## Frame 5 — Emotional transformation (0:43–0:53)

22. Camryn enjoying the experience (candid, relaxed)
23. Final mirror reveal
24. Camryn walking through the spa, smiling naturally
25. **Polished final beauty portrait — also the thumbnail/cover-frame
    candidate.** Needs to be a strong standalone still; confirm before
    treating it as the thumbnail.

## Frame 6 — Closing CTA (0:53–0:60)

26. Enova logo (see item 6 — same asset)
27. Confirmed business details: website URL, phone number, Instagram/social
    handle — the brief did not supply these; get them from the client
28. Any additional brand mark / wordmark variant for a dark background (the
    closing card uses a dark green ground)
29. B-roll or a still to sit behind the closing card, if desired (currently a
    plain dark green card — works as-is, but real footage would lift it)

## Cross-cutting

30. **Locked voiceover audio** — the five VO lines are written into
    `STORYBOARD.md`/the frame files as text; they need to be recorded
    (professional VO artist, tone: warm, calm, confident) before the master
    can carry real narration or drive burned-in caption timing on the
    vertical adaptation.
31. **Licensed music bed** — "elegant, calming, modern wellness" with a
    subtle cinematic build. Needs sourcing/licensing per BRIEF.md § Audio;
    not yet selected.
32. **Natural/ambient sound** where available from the raw footage: doors,
    product application, towels, water, massage oils, treatment devices,
    room ambience.
33. Any patient-identifying information visible in real footage (charts,
    forms, screens) must be removed or blurred before use, per BRIEF.md
    Notes.

## Once assets land

1. Replace each frame's watermark placeholder with the real media
   (`<video>`/`<img>` clips per `hyperframes-core` § tracks-and-clips).
2. Add the VO audio as `<audio>` clips aligned to each frame's timing.
3. Add the music bed as a lower-track `<audio>` clip spanning the whole
   composition, ducked under the VO (`/hyperframes-audio`).
4. Build the 9:16 vertical adaptation and the burned-in-caption version once
   VO timing is real (captions need real word timings, not placeholder text).
5. Build the four social reels (`REELS.md`) — currently planned, not built.
6. Re-run `npm run check`, then `npm run render`.
