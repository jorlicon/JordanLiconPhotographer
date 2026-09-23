# SEO Priority Fixes Status

Updated: 2026-09-06

## Step 1 - URL Consolidation

Status: Published, live verification pending.

Completed locally:
- Confirmed `sitemap.xml` only lists current canonical `https://www.jordanliconphotography.com/` URLs.
- Added legacy redirects to `_redirects` for old branded, architecture, food, stadium, and healthcare/property paths that have clear current equivalents.
- Added matching client-side fallback redirects to `404.html` for GitHub Pages behavior before edge redirects are available.
- Updated `SEO-REDIRECT-MAP-2026-08-30.csv` so the same new mappings can be mirrored in Cloudflare redirect rules later.

New redirect mappings added:
- `/jordanliconphotography` -> `/`
- `/elpasoarchitecturalphotographer` -> `/architectural-photographer-el-paso.html`
- `/elpasofoodphotographer` -> `/food-photography-portfolio.html`
- `/santa-fe-place-apartments` -> `/architecture.html`
- `/jefferson-high-school-stadium` -> `/architecture.html`
- `/franklin-high-school-stadium` -> `/architecture.html`
- `/las-palmas-del-sol` -> `/architecture.html`

Verification:
- No duplicate source paths in `_redirects`.
- No legacy URLs found in `sitemap.xml`.
- Current indexable HTML canonicals point to `https://www.jordanliconphotography.com/`.
- `404.html` legacy redirect map parses successfully.

Remaining:
- Live verification is still pending because this environment could not resolve `www.jordanliconphotography.com` during the follow-up curl check.
- Mirror the CSV mappings into Cloudflare bulk/page redirect rules once Cloudflare is active.

Publish record:
- Published to `jorlicon/JordanLiconPhotographer` on `main` in commit `ffee006`.

## Step 2 - Internal Linking

Status: Published.

Completed locally:
- Updated homepage service cards so Architecture points directly to `/architectural-photographer-el-paso.html` and Commercial points directly to `/el-paso-commercial-photographer.html` instead of only same-page section anchors.
- Added a service-link block to all 22 blog posts so articles pass authority to headshots, commercial photography, architectural photography, food photography, editorial portraits, and inquiry paths.

Verification:
- Confirmed all 22 post HTML files now include the service-link block.
- Confirmed the linked service/portfolio files exist locally.

Publish record:
- Published to `jorlicon/JordanLiconPhotographer` on `main` in commit `f60bc23`.

## Step 3 - Title And Meta CTR Tuning

Status: Published.

Completed locally:
- Tuned titles and meta descriptions for the homepage, headshot service page, commercial service page, architectural service page, food portfolio page, and editorial portrait portfolio page.
- Aligned copy with Search Console query opportunities: El Paso photographer, commercial photographer, professional headshots, architectural photographer, food photographer, and editorial portraits.
- Kept titles around 54-62 characters and descriptions around 125-139 characters to improve snippet clarity without keyword stuffing.

Verification:
- Confirmed the six priority pages have tuned title lengths between 54 and 62 characters.
- Confirmed the six priority pages have meta descriptions between 125 and 139 characters.

Publish record:
- Published to `jorlicon/JordanLiconPhotographer` on `main` in commit `f60bc23`.

## Step 4 - Mobile LCP

Status: Complete, status publish pending.

Completed locally:
- Confirmed the homepage preloads a smaller mobile hero image at `assets/optimized/home-hero-camryn-640.jpg` for mobile viewports.
- Confirmed the desktop hero preload remains scoped to desktop viewports.
- Confirmed homepage service-card images use the 480px optimized assets instead of the previously flagged 900px mobile sources.

Verification:
- No homepage references remain to `service-card-900-mobile` assets.
- No homepage service-card image uses the old `sizes="(min-width: 860px) 370px, 100vw"` pattern that caused oversized mobile selection.

Remaining:
- Re-run PageSpeed after GitHub Pages finishes deployment so the live mobile LCP result can be confirmed.

## Step 5 - Desktop CLS

Status: Complete, publish pending.

Completed locally:
- Changed the homepage Google Fonts loading from delayed async stylesheet loading to a normal stylesheet load.
- Kept the existing `display=optional` font behavior while preventing the hero text area from repainting after first render.

Why this matters:
- PageSpeed identified the homepage hero-bottom text block as the desktop layout shift culprit.
- The listed contributors were web fonts, so stabilizing first paint font metrics should reduce the desktop CLS score.

Remaining:
- Publish the homepage update.
- Re-run PageSpeed after GitHub Pages finishes deployment so the live desktop CLS result can be confirmed.
