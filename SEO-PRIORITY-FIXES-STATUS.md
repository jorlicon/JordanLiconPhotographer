# SEO Priority Fixes Status

Updated: 2026-09-05

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
