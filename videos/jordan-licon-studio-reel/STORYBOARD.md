---
format: 1080x1920
duration: 20s
message: "An industrial-chic El Paso photography studio, ready for your next shoot."
arc: Establish → Explore → Prove capability → Scale → Comfort → Brand
audience: photographers and creatives considering booking this studio for shoots
mode: autonomous
music: warm cinematic ambient underscore, slow build, no vocals
---

## Video direction

**Palette** — from `frame.md` (Cartesian, brand-remixed): `bg-primary` #f0ebe2 (closing card ground), `text-primary` #060606 ink, `accent`/`line` #8a8072 / #b8985f warm taupe-to-brass, `text-secondary` #5A5A5A. Room frames are full-bleed photography — the palette governs only the closing card's type/hairline/geo-ring.

**Standard media treatment (apply to every `<img>` in Frames 1–5)** — the "cinematic lighting" grade, identical on all five studio photos for a consistent film stock: preset `deep-contrast` at intensity ~0.85, layered with correction `{ highlights: -0.5, whites: -0.1, shadows: +0.15, blacks: -0.1, contrast: +0.15, temperature: +0.2, vibrance: +0.1, saturation: -0.05 }` (tames the blown window highlights, deepens shadow falloff, pushes warm), plus finishing `{ vignette: 0.3, vignetteFeather: 0.65, grain: 0.12, grainSize: 0.3 }` for filmic depth. Frame 4 (warehouse) additionally needs `temperature` pulled slightly less warm than the others (source has a cool/green cast) — worker may trim the correction's warmth ~30% on that one frame only so it doesn't fight the source cast; every other value stays identical across all five.

**Motion grammar + reveal model** — this is a **photographic walkthrough, not a UI/SaaS product demo**: no blueprint in the bank fits a pure architectural-interior reveal, so every room frame (1–5) is `blueprint: compose`, built from the Camera vocabulary in `motion-language.md` (`push / focus / drift` → `multi-phase-camera`; `zoom-to-target` → `coordinate-target-zoom`). Each room frame is ONE continuous, single-direction camera move across its full duration — never a multi-element reveal sequence (there is no text/UI to stagger). Long-tail `power3`-family eases throughout; no bounce, no overshoot. Frame 6 (the brand close) is the one frame with type, and follows `titlecard-reveal`'s calm register.

**Rhythm / held-frame allocation** — Frame 1 opens near-still (a slow push only, symmetrical composition holding its own weight) so the film starts quiet. Frames 2–4 carry the most camera movement (push/pan/pull) since they're the "explore the space" core. Frame 5 is the deliberate held breather before the brand close: push for its first ~40%, then settle and hold still (no back-half drift) — the ease beat earns stillness, not more motion. Frame 6 holds fully static once the lockup settles (allowed: one subtle jitter at most).

**Negative list** — no UI chrome, no cursors, no bouncy easing, no lazy breathing/scale-pulse loops, no back-half pan/push on any frame (front-load a single committed camera direction instead, decided at t=0), no on-screen text on Frames 1–5 (let the room speak — brief calls for minimal text), no populist accent color beyond Cartesian's brass/taupe on Frame 6, no real cursor or browser chrome anywhere.

**Caption band** — bottom ~17% kept clear on every frame even though captions are disabled for this silent film (bottom-edge consistency).

## Frame 1 — Window room, establishing

- scene: Symmetrical window-lit room — vintage Coca-Cola machine, pampas grass, iron stool, brick wall, warm pooled light
- voiceover:
- duration: 3.5s
- transition_in: crossfade
- status: outline
- src: compositions/frames/01-window-room.html
- type: hook
- persuasion: Visual spectacle / establishing
- beat: curiosity
- blueprint: compose
- focal: assets/01-window-room.jpg
- roles: 01-window-room.jpg = background (full-bleed, no dim — no overlaid text)
- asset_candidates: assets/01-window-room.jpg — window-light room with vintage Coca-Cola machine and pampas grass, brick wall

narrativeRole: The cold open. A quiet, graphic, almost-still frame that says "this is a real, considered space" before anything moves.
keyMessage: The room is beautiful even standing still.

Scene 1 (0.0–3.5s): full-bleed centered composition, symmetrical window dead-center per the source photo. A single slow **push** (`multi-phase-camera`, one phase only, no drift-then-repush) creeps in ~4–6% over the full duration on a long-tail `power3` ease — barely perceptible at any instant, but the frame is visibly closer by the cut. No other motion; the frame's own graphic symmetry (window / Coca-Cola machine / stool) carries the beat standing nearly still.

## Frame 2 — Loft, wide reveal

- scene: Wide push across the main shooting floor — factory windows, hanging bulbs, vintage daybed, full room scale
- voiceover:
- duration: 3.5s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-loft-wide.html
- type: feature_showcase
- persuasion: Show-don't-tell proof
- beat: intrigue building to aspiration
- blueprint: compose
- focal: assets/02-loft-wide.jpg
- roles: 02-loft-wide.jpg = background (full-bleed, no dim — no overlaid text)
- asset_candidates: assets/02-loft-wide.jpg — wide natural-light loft with exposed pipes, iron bed prop, sheer curtains

narrativeRole: Opens the space up — this is the hero shooting floor, not just one corner.
keyMessage: There's real room to work here.

Scene 1 (0.0–3.5s): full-bleed, framed wide/asymmetric (the room's depth runs toward the windows at frame-right). One continuous **push + lateral drift** (`multi-phase-camera`, single phase, committed direction chosen at t=0 — drifting slightly toward the windows as it pushes) on `power3`, ~6–8% scale change over the shot. No back-half re-direction — one vector, held to the cut.

## Frame 3 — Lighting studio, gear

- scene: Cyc-wall and seamless backdrop corner — softbox, grip stand, rolling cart, warm pendant light
- voiceover:
- duration: 3.5s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/03-lighting-corner.html
- type: feature_showcase
- persuasion: Show-don't-tell proof
- beat: confidence
- blueprint: compose
- focal: assets/03-lighting-corner.jpg
- roles: 03-lighting-corner.jpg = background (full-bleed, no dim — no overlaid text)
- asset_candidates: assets/03-lighting-corner.jpg — cyc-wall lighting studio corner, softboxes and grip gear, tan backdrop

narrativeRole: The turn — from "pretty room" to "working production studio." Proves it's shoot-ready, not just staged.
keyMessage: This is a real production space with real gear.

Scene 1 (0.0–3.5s): full-bleed, asymmetric 60/40 (the softbox + grip stand cluster off-center). A **zoom-to-target** (`coordinate-target-zoom`) push tightens onto the gear cluster rather than the frame's geometric center — this is the beat that proves production-readiness, so the camera commits to the equipment, not the room. Single continuous move, `power3`, no counter-drift.

## Frame 4 — Warehouse, scale

- scene: Raw exposed-beam warehouse floor receding into shadow, cool mixed light
- voiceover:
- duration: 3s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/04-warehouse.html
- type: feature_showcase
- persuasion: Scale & atmosphere proof
- beat: awe
- blueprint: compose
- focal: assets/04-warehouse.jpg
- roles: 04-warehouse.jpg = background (full-bleed, no dim — no overlaid text; landscape source, cover-fit crop to 9:16)
- asset_candidates: assets/04-warehouse.jpg — raw industrial warehouse space, exposed wood beams and columns

narrativeRole: A brief atmospheric beat that widens the sense of scale beyond the finished rooms.
keyMessage: There's more building here than one room.

Scene 1 (0.0–3.0s): full-bleed cover-fit crop centered on the receding column line (the depth cue). One continuous slow **pull-back** (`multi-phase-camera`, single phase, starts slightly tighter and eases out ~5%) reading as the space opening up rather than closing in — the inverse direction from Frames 1–3, marking this as the "scale" beat. `power3`, no drift.

## Frame 5 — Lounge, comfort

- scene: Leather sectional in warm sunset light, kitchen and shooting floor beyond
- voiceover:
- duration: 3.5s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/05-lounge-kitchen.html
- type: benefit_highlight
- persuasion: Show-don't-tell proof
- beat: ease
- blueprint: compose
- focal: assets/05-lounge-kitchen.jpg
- roles: 05-lounge-kitchen.jpg = background (full-bleed, no dim — no overlaid text)
- asset_candidates: assets/05-lounge-kitchen.jpg — lounge/kitchen area with leather sofa, big windows, fridge

narrativeRole: The human beat — somewhere to land between takes. Softens the sequence before the brand close.
keyMessage: Clients are looked after here too.

Scene 1 (0.0–1.4s): full-bleed, centered on the sunlit sofa cushions. A brief **push** (`multi-phase-camera`) settles onto the seating — ~3% scale change, `power3`.
Scene 2 (1.4–3.5s): the push resolves and HOLDS — no further drift, no re-push, no breathing. This is the video's deliberate breather: the ease beat is earned by stillness, at most a **subtle jitter** (`sine-wave-loop`, low amplitude) keeps the hold from reading dead.

## Frame 6 — Brand close

- scene: Centered closing plate — studio wordmark, logo mark, and website on the near-black brand ground
- voiceover:
- duration: 3s
- transition_in: zoom-through
- status: outline
- src: compositions/frames/06-brand-close.html
- type: branding
- persuasion: Brand authority
- beat: trust + belonging
- blueprint: titlecard-reveal (Adapt)
- focal: capture/assets/jl-logo-512.png
- roles: jl-logo-512.png = cutout (centered brand mark, lay type around it)
- asset_candidates: capture/assets/jl-logo-512.png — Jordan Licon Photography logo mark

narrativeRole: Resolve the walkthrough into the brand — who this is and where to find them.
keyMessage: Jordan Licon Photography — El Paso studio — jordanliconphotography.com

Adapt: keep titlecard-reveal's single-restrained-move + hold signature (no wordmark-collapse, no card-chain — this is one calm card, per Cartesian's Closing Plate treatment). Ground `bg-primary`, centered, a faint centered geo-ring (~40cqw, solid+dashed per `frame.md`'s Closing Plate) drifts in behind.
Scene 1 (0.0–0.4s): static `bg-primary` ground, centered geo-ring already faintly present (no draw-on — it's atmosphere, not a focal element). Establishes the calm card before anything commits.
Scene 2 (0.4–1.6s): the ONE move — the logo mark (`jl-logo-512.png`) fades in + settles at ~95%→100% scale dead-center (`spring-pop-entrance`, smooth long-tail settle, no overshoot), with the taupe `label` "EL PASO PHOTOGRAPHY STUDIO" fading in just above it on the same beat.
Scene 3 (1.6–3.0s): the `h1`/`display` wordmark "Jordan Licon" (ink, sentence case, Fraunces) settles below the mark, then one short ink `horizontal-accent` line draws beneath it, with the `attribution` line "jordanliconphotography.com" resolving last, uppercase taupe. Holds fully static to the cut — at most subtle jitter on the geo-ring, nothing else moves.
