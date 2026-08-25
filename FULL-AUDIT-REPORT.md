# SEO Audit Report - Jordan Licon Photography

Date: 2026-08-24

## Scope

This audit covered the local static website files in:

`/Users/thecave/Documents/Codex/2026-04-29/here-is-the-website-i-am`

The shared ChatGPT audit URL could not be read directly because it opened to the logged-out ChatGPT shell instead of the report content. I therefore ran a fresh local SEO pass using the installed SEO skill criteria and source-level checks.

## Results

Source-level SEO audit: 100/100 locally

- Public HTML pages checked: 53
- Missing titles: 0
- Title length issues: 0
- Duplicate title issues: 0
- Missing meta descriptions: 0
- Meta description length issues: 0
- Duplicate meta description issues: 0
- Missing canonicals: 0
- Restricted FAQPage schema: 0
- Missing image alt text: 0
- Missing image width/height attributes: 0
- Long alt text warnings: 0
- Thin blog posts under 1,500 words: 0

Structured data validation: 100/100 locally

- Schema warnings: 0
- The homepage schema graph now includes an explicit root `@type` for stricter validator compatibility.
- FAQPage schema was removed from pages where Google no longer supports FAQ rich results for this type of site. Visible FAQ content remains on-page for users.

Internal link validation: 100/100 locally

- HTML files checked: 52
- Missing local files/assets: 0
- Missing same-page anchors: 0
- Missing cross-page anchors: 0
- JavaScript-generated architecture and portrait category navigation now has crawl-safe static fallback targets plus enhanced smooth-scroll behavior for users.

## Fixes Implemented

- Marked the Stitch source mirror as `noindex, nofollow` so it does not compete with the main homepage.
- Removed unsupported `FAQPage` structured data blocks while preserving visible FAQ sections.
- Expanded all blog posts that were below the local SEO depth threshold.
- Improved several short meta descriptions.
- Shortened overlong image alt text.
- Added missing `width` and `height` attributes to images and lightbox placeholders.
- Fixed a dynamic architecture gallery thumbnail template to include explicit image dimensions.
- Updated category navigation links so static crawlers no longer see broken hash anchors.
- Added JavaScript enhancement so category links still scroll to the intended generated sections after page load.

## Remaining Items That Require Live Measurement

These cannot be guaranteed from static source files alone:

- Core Web Vitals / Lighthouse performance score
- Live indexability after Google recrawls the published site
- HTTPS/HSTS behavior from the hosting layer
- CDN cache headers and compression behavior
- Third-party crawl reports from SEMrush after republishing

Recommendation: after publishing, rerun SEMrush and PageSpeed Insights on `https://www.jordanliconphotography.com/`.
