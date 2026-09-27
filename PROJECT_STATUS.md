# Jordan Licon Photography project status

Updated: 2026-09-11

Execution update: 2026-09-16

- Fresh Ahrefs Site Audit crawl completed and reported 12 actual issues before this local pass.
- Ahrefs confirmed the homepage meta description was 175 characters; it was shortened locally.
- Added complete Open Graph and X card metadata to current indexable HTML pages.
- Added a social image fallback where public pages had no Open Graph image.
- Shortened the credits page description to fit the local audit limit.
- Marked the legacy `wix-export/pattern-1-landing.html` page `noindex, nofollow`.
- Local checks pass for metadata coverage, food portfolio JavaScript syntax, sitemap exclusions, and sampled JSON-LD.
- Ahrefs live crawl observed the apex HTTP URL redirecting with `301` to the `www` HTTPS URL, and the canonical homepage and sitemap returned `200`. This should still be confirmed after the next production publish.
- The Ahrefs crawl showed 78 oversized image resources, mostly remote Headshot Crew JPEGs. Image resizing or replacement remains a separate production change.

## Purpose

This file is the starting point for new Codex tasks. Check the live site and the relevant account before relying on dated figures below.

## Site and publishing

- Local site root: `/Users/thecave/Documents/Codex/2026-04-29/here-is-the-website-i-am`
- Production site: `https://www.jordanliconphotography.com/`
- GitHub repository: `jorlicon/JordanLiconPhotographer`, branch `main`
- This local folder is not a Git checkout. Do not run commits here or assume `git status` describes the published site.
- Publishing has previously used a temporary repository clone. Inspect `push-website-to-github.command` and compare production before publishing.
- Never publish unless Jordan explicitly asks.

## Business facts

- Business name: Jordan Licon Photography
- Address: 2201 E Mills Ave, El Paso, TX 79901, United States
- Phone: +1 915 226 6037
- Website: `https://www.jordanliconphotography.com/`
- Business email: `jordanliconphotography@gmail.com`
- Client portal: `https://jordan-licon-photography.bloom.io/login`

## Current site work

- Canonical public URLs use the `www` host.
- The sitemap contains current indexable public pages only.
- Legacy URL redirects, internal service links, and priority title/meta updates were published in September 2026.
- Homepage mobile image sizing and desktop font-loading changes were completed locally according to `SEO-PRIORITY-FIXES-STATUS.md`; verify production before assuming both are live.
- Blog structure and image metadata were normalized. Several generic imported images were replaced with original portfolio work. Remaining questionable blog images still need a visual review.
- Portfolio copy was rewritten around buyer needs and more specific calls to action.
- The Bloom client portal, chat widget, and satisfaction badge were added during earlier work. Verify the live widget and button color before changing them again.
- The magazine lightbox contains additional covers and supports previous/next movement. Mobile layout and image loading received follow-up fixes. Test the live version before editing.

## Search Console

Last figures observed in this task on 2026-09-06:

- 39 indexed pages
- 47 not indexed pages
- 25 old URLs returning 404, with validation started
- 16 crawled but not indexed, with validation started
- 3 discovered but not indexed, with validation started
- 1 page with redirect
- 1 apex-host redirect error: `https://jordanliconphotography.com/`
- 1 Facebook UTM URL treated as an alternate page with a proper canonical tag; this is expected and does not need indexing

The reported non-indexed examples were mostly Wix-era or lower-priority URLs. Do not request indexing for obsolete URLs. Inspect current canonical service, portfolio, and public blog pages individually before requesting indexing.

The apex redirect error may require a Cloudflare redirect or DNS fix. Confirm the live redirect chain first. Start Search Console validation only after the live response is correct and the UI shows a confirmation.

## External services

- Cloudflare was planned for canonical-host redirects, HSTS, security headers, and cache rules. Account-side completion has not been confirmed in this handoff.
- Google Business Profile address correction was pending review in the last listing report.
- Bing Places was verified and pending publication after importing the corrected address.
- Yelp was claimed and had correct core business details.
- Foursquare received a free listing submission; paid claiming was declined.
- Work is limited to free listings unless Jordan approves a specific charge.
- Detailed listing history is in `LOCAL-LISTING-PROGRESS.md`.

## Advertising asset

- Interactive preview: `campaign-drafts/headshot-animation/your-next-introduction.html`
- Final video: `campaign-drafts/headshot-animation/headshot-story-ben-hartley-15s.mp4`
- Source music: `campaign-drafts/headshot-animation/introduction-music.wav`
- Renderer: `campaign-drafts/headshot-animation/render-visualization.mjs`
- The final video is 15 seconds, 1080 x 1920, 30 fps, with AAC audio and ten distinct portraits.
- The inline visualization timeout was fixed by replacing heavy embedded assets with a compressed portrait sprite and removing the host integration that timed out.

## Working rules

- Inspect the current file and live page before editing; some reports contain older snapshots.
- Preserve original photography and avoid synthetic-looking blog imagery.
- Keep portfolio language focused on the buyer's problem, process, and usable business result.
- Ask before deleting account data, tags, analytics properties, or third-party configurations.
- Ask before paid subscriptions, advertising spend, or paid directory claims.
- Do not repeat indexing requests or validation while an existing Search Console process is running.

## Useful records

- `SEO-PRIORITY-FIXES-STATUS.md`
- `INDEXING-IMPLEMENTATION-LOG-2026-08-30.md`
- `CONTENT-REFRESH-LOG.md`
- `LOCAL-LISTING-PROGRESS.md`
- `CLOUDFLARE-SEO-RULES-2026-08-30.md`
- `SEO-REDIRECT-MAP-2026-08-30.csv`
- `FINALIZED-IMAGE-FOLDERS.md`

## Execution update: 2026-09-16 continued

- Search Console was rechecked in the verified domain property using the signed-in Jordan Licon account. Breadcrumbs: 17 valid, 0 invalid. Image Metadata: 24 valid, 0 invalid. Videos: 4 valid, 0 invalid; the report still lists 2 valid video items with a missing `creator.url` field.
- Added `url` to the two creator objects in the indexable homepage video JSON-LD. Local schema validation and `assets/js/food-portfolio.js` syntax validation pass.
- Local image audit found 496 image tags and 0 missing or empty `alt` values.
- Ahrefs remains a pre-publication baseline: its fresh crawl recorded 12 active issue groups, including 20 incomplete Open Graph records, 6 missing X cards, 4 missing Open Graph tags, and 78 oversized image resources. The oversized-image count is largely third-party Headshot Crew media and needs rights-safe replacement or permission before rehosting.
- Replaced public internal links to `index.html` with directory-root links (`./`, `../`, and their fragment forms) so crawlers consolidate normal inlinks on the canonical homepage URL.
- Repointed blog cards and related-article links away from four legacy `noindex` duplicates to their current canonical numbered articles.
- Generated 900 px and 1600 px responsive derivatives for the six largest Sierra Crest and Evolve Credit Union architecture images, reducing individual downloads from 2.6-20 MB to roughly 104-476 KB, and updated `architecture.html` with `srcset`, `sizes`, accurate dimensions, lazy loading, and async decoding.
- Replaced the 1.9 MB Santa Fe architecture video poster references with the existing 1200x599 optimized JPEG (about 206 KB), including page media and social preview metadata. The original remains intact.
- Replaced the remaining architecture-page image loads above 500 KB with 1600 px derivatives: the Oculus panorama is about 485 KB, the CDA Sportspark poster about 291 KB, and the El Paso Zoo image about 502 KB. Originals remain intact.
- Confirmed `food-photography-portfolio.html` loads `assets/js/food-portfolio.min.js`; the file passes Node syntax validation. The older Ahrefs JavaScript warning predates the current reference.
- No production publish or Search Console validation request was made during this pass. The hourly SEO task remains active while live fixes and production verification are outstanding.

## Execution checkpoint: 2026-09-21

- Search Console review confirmed 37 indexed URLs and 46 not indexed URLs in the URL-prefix property. The report grouped them as 28 not found, 3 alternate canonical URLs, 12 crawled but not indexed, and 3 discovered but not indexed.
- The 404 examples include old Wix-era paths, but also current local blog paths. These must be checked on the deployed site before any deletion or validation request.
- Local sitemap audit passed: all 37 sitemap URLs map to existing files, every sitemap page has a canonical tag, and no sitemap page has a `noindex` directive.
- Local image audit passed: 481 image tags were checked and none had empty alt text. `assets/js/food-portfolio.min.js` passed Node syntax validation.
- No files were deleted, no production publish was made, and no Search Console indexing or validation request was submitted. The existing heartbeat automation was updated to continue the indexing plan hourly and deactivate after the live priority checks are complete.

## Live verification: 2026-09-21

- Chrome verified `post/perfecting-your-corporate-headshot-photography.html` returns the complete public article and Search Console reports “URL is on Google” and “Page is indexed.”
- Chrome verified `post/exploring-jordan-licon-photography-in-el-paso.html` returns the complete public article and Search Console reports “URL is on Google” and “Page is indexed.”
- Search Console Sitemaps reports `/sitemap.xml` as `Success`, last read Sep 17, 2026, with 37 discovered pages and 0 discovered videos.
- Search Console still shows the prior 46-not-indexed snapshot: 28 404s, 3 canonical alternates, 12 crawled-not-indexed, and 3 discovered-not-indexed. No new indexing request or validation was submitted because the checked priority URLs are already indexed and the remaining 404s are legacy/history entries.
- Jordan approved removal of the obsolete local utility and ad files. A backup was created at `backups/utility-files-2026-09-21.tar.gz` before deletion. The approved files were removed locally, their `robots.txt` entries were cleared, and the 37-URL sitemap still passes its local existence check.

## Publication: 2026-09-21

- Published commit `a6e03df8` to `jorlicon/JordanLiconPhotographer` `main`.
- The deployed utility URL `https://www.jordanliconphotography.com/website-style-options.html` returns the site's 404 page.
- The deployed sitemap returns HTTP 200. The live `robots.txt` response was still serving an older cached copy during verification; GitHub `main` contains the corrected version.
