# SEMrush-Style SEO Audit Report

Date: 2026-08-24

Scope: public GitHub Pages site files for `www.jordanliconphotography.com`.

## Result

Public-page audit result: PASS

- Public HTML pages checked: 41
- Broken internal links: 0
- Missing local image/video assets: 0
- Empty image sources: 0
- Missing image alt attributes: 0
- Duplicate public page titles: 0
- Duplicate public meta descriptions: 0
- Missing canonicals: 0
- Noindex pages in sitemap: 0
- Invalid JSON-LD structured data: 0
- Direct media-file links formatted as page links: 0
- Indexed public pages below 350 words: 0
- Public pages with only one incoming internal link: 0

## SEMrush Issue Review

The Chrome SEMrush campaign showed 5 Errors, 2 Warnings, and 4 Notices. Each item was reviewed against the current website files.

| SEMrush issue | Local fix/status |
| --- | --- |
| 28 structured data items are invalid | Fixed. JSON-LD now parses cleanly across public HTML files. |
| 14 pages have duplicate meta descriptions | Fixed. Public indexed pages now have unique meta descriptions. |
| 12 issues with duplicate title tags | Fixed. Public indexed pages now have unique title tags. |
| 3 internal links are broken | Fixed. Local internal-link crawl reports 0 broken internal links. |
| 1 page returned a 4XX status code | Fixed in site files. Legacy/internal bad references are gone and `success.html` is no longer in the sitemap. |
| 6 pages have a low word count | Fixed. Thin public indexed service/policy pages were expanded with useful content. |
| 3 pages have low text-HTML ratio | Improved. Drone, commercial, food, policy, and accessibility pages now include stronger crawlable copy. |
| 38 resources are formatted as page link | Fixed. Direct image/video file anchors were removed or converted to buttons/lightbox controls. |
| 16 pages have only one incoming internal link | Fixed locally. Blog related-link blocks and service cross-links were added. |
| 6 orphaned pages in sitemaps | Fixed locally. Sitemap URLs now have internal paths from the blog, homepage, service pages, or footer navigation. |
| 2 subdomains don't support HSTS | Platform-level. `_headers` includes HSTS, but GitHub Pages does not serve custom security headers for custom domains. Full resolution requires Cloudflare or another CDN/proxy that can set HSTS headers. |

## Fixes Completed

- Replaced broken legacy Wix/about links with current internal destination pages.
- Corrected the recognition link in `credits.html`.
- Shortened and clarified the architectural portfolio title and meta description.
- Removed `success.html` from the sitemap because it is intentionally noindexed.
- Updated sitemap `lastmod` values to `2026-08-24`.
- Added crawler exclusions for backups, Wix exports, exported ad graphics, and private design mockups.
- Marked private mockup/ad pages as `noindex, nofollow` where needed.
- Added safe placeholder `src` values and descriptive alt text for hidden lightbox images.
- Rewrote duplicate blog/page metadata so indexed articles have unique titles and descriptions.
- Added related article links across blog posts.
- Added internal links from the headshot service page to executive, actor, and corporate headshot pages.
- Expanded accessibility, privacy, terms, drone, commercial, and food pages to remove thin-content warnings.
- Converted embedded-video “Play” file links into in-page video controls.
- Updated the contact-form success redirect to the official domain.

## Notes

The original SEMrush export was not provided in the chat, so this report uses a local SEMrush-style crawl against the current website files. The crawl intentionally excludes archived backups and private mockups because those are not part of the public indexed site.
