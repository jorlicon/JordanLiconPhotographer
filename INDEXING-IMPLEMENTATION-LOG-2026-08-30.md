# Indexing Implementation Log - 2026-08-30

## Local Changes Completed

- Added consistent `index, follow, max-image-preview:large` robots directives to indexable service and portfolio pages that lacked an explicit robots tag.
- Added missing canonical tags to noindex utility/ad pages so audit tools have an explicit URL signal.
- Marked older duplicate blog articles as `noindex, follow` and pointed their canonicals to the preferred current article.
- Rebuilt `sitemap.xml` from indexable public pages only.
- Strengthened internal links to priority headshot, actor, architecture, drone, and commercial service pages.
- Added content depth and related links to `actor-headshots-el-paso.html` and `architectural-photographer-el-paso.html`.
- Added `SEO-REDIRECT-MAP-2026-08-30.csv` for Cloudflare redirect implementation.
- Added `CLOUDFLARE-SEO-RULES-2026-08-30.md` for canonical host, HSTS, security header, and cache configuration.

## Search Console Baseline

- Page indexing report last observed update: 2026-08-20.
- Sitemap last read: 2026-08-30.
- Sitemap status: Success.
- Search Console showed 6 indexed pages and 41 not indexed pages before these local changes were published.
- Main reported reasons: 28 Not found (404), 13 Crawled/Discovered currently not indexed.

## Blocked Outside Repository

- Cloudflare DNS, HSTS, cache rules, and apex-to-www redirects require Cloudflare account access or a connected Cloudflare integration.
- Google Business Profile alignment requires Google Business Profile access.
- External citation/backlink work requires manual profile/vendor updates or connected accounts.
