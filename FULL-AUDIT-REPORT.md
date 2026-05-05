# SEO Audit Report - Jordan Licon Photography Home Page

Scope: single-page SEO audit for `index.html`, reviewed as the future home page at `https://www.jordanliconphotography.com/`.

Score confidence: Medium. This audit used local HTML evidence, local link/file checks, JSON-LD parsing, and the SEO skill readability script. Live-only checks such as PageSpeed, robots.txt, sitemap, server headers, and external HTTP status were not confirmed from the local file.

## Audit Summary

Overall Score: 77/100

On-Page SEO: 74/100
Content Quality: 72/100
Technical SEO: 82/100
Schema: 80/100
Images & Media: 70/100
Local / AI Search Readiness: 80/100

Top 3 Issues:

1. Title and meta description are both longer than best-practice ranges.
2. The H1 is beautiful but does not include the primary service/location keyword.
3. Several visual sections use CSS background images, which search engines and accessibility tools cannot interpret as well as semantic `<img>` elements.

Top 3 Opportunities:

1. Reframe the H1 and first-screen copy around `El Paso commercial photographer` while preserving the premium editorial tone.
2. Add stronger conversion-oriented internal links from the home page to dedicated service pages.
3. Add Breadcrumb schema and consider replacing or de-emphasizing FAQ schema with more service-specific schema.

## Evidence Snapshot

- Title: `Jordan Licon - El Paso Commercial Photographer & Cinematographer` (`64` characters)
- Meta description: `176` characters
- Canonical: `https://www.jordanliconphotography.com/`
- H1 count: `1`
- H1 text: `Cinematic light. Editorial eye.`
- Images using `<img>`: `13`
- Images missing alt text: `0`
- Images missing width/height: `0`
- CSS background image references: `17`
- JSON-LD blocks: `2`, both valid
- JSON-LD types: `WebPage`, `FAQPage`
- Local file references checked: `42`
- Missing local references: `0`
- Placeholder links: `0`
- Missing hash anchors: `0`
- Word count from local extraction: approximately `2,107`
- Readability script output: Flesch `0`, grade `26.5`; confidence is limited because compact/minified HTML causes some section text to concatenate.

## Findings Table

| Area | Severity | Confidence | Finding | Evidence | Fix |
|---|---:|---:|---|---|---|
| On-page metadata | Warning | Confirmed | Title is slightly too long for clean SERP display. | Title is `64` characters; target is usually around `50-60`. | Shorten to something like `El Paso Commercial Photographer | Jordan Licon`. |
| On-page metadata | Warning | Confirmed | Meta description is too long and may truncate. | Meta description is `176` characters; target is usually around `150-160`. | Rewrite to about `150-155` characters with primary service, location, and conversion intent. |
| Heading intent | Warning | Confirmed | H1 does not include the primary keyword or location. | H1 is `Cinematic light. Editorial eye.` | Keep the line as brand copy, but add an H1 or immediately adjacent hero line containing `El Paso commercial photographer and cinematographer`. |
| Content quality | Warning | Likely | Copy reads premium but can become dense for search and users. | Readability script reported Flesch `0`, grade `26.5`; extraction is imperfect because compact HTML concatenates sections. | Break long service descriptions into shorter paragraphs and add concise summaries near each service section. |
| Image SEO | Warning | Confirmed | CSS background images are visually strong but weak semantically. | `17` background image URLs detected; background images do not support alt text. | Convert key talent, architecture, and commercial client visuals to semantic `<img>` elements where practical. |
| Image performance | Warning | Likely | Remote images and video embeds may affect LCP and total page weight. | Hero image is remote and high priority; local videos are `1.7M` and `6.0M`; many Wix/static remote images are used. | Use local optimized AVIF/WebP derivatives for hero and key gallery assets; keep lazy loading below the fold. |
| Schema | Info | Confirmed | ProfessionalService schema is strong, but FAQ schema has limited rich-result eligibility. | JSON-LD includes `WebPage` with `ProfessionalService` graph and separate `FAQPage`; both parse as valid. | Keep if useful, but add BreadcrumbList and more page-specific Service schema for headshots, architecture, commercial photography, and drone services. |
| Local SEO | Pass | Confirmed | Strong local business signals are present. | Address, phone, email, `areaServed`, `sameAs`, offers, rating, and service topics appear in JSON-LD. | Keep consistent with Google Business Profile and all live citations. |
| Internal linking | Pass | Confirmed | Internal link structure is broad and clean. | `40` internal links detected; missing local references: `0`; placeholder links: `0`. | Continue using descriptive anchors to service pages and blog posts. |
| Accessibility / media | Warning | Confirmed | Embedded video poster URLs are remote Facebook CDN URLs. | Two video posters point to `scontent-hou1-1.xx.fbcdn.net`. | Replace with local poster images for reliability, performance, and long-term stability. |

## Positive Signals

- The page has a correct canonical URL.
- Open Graph and Twitter card metadata exist.
- There is exactly one H1.
- All detected `<img>` elements have alt text and explicit dimensions.
- Local internal links and asset references resolve.
- The page includes strong E-E-A-T signals: credits, institutions, reviews, address, phone, email, and service pages.
- The page has conversion paths for headshots, commercial inquiry, architecture, blog, and authority pages.

## Priority Recommendations

1. Tighten title and meta description.
2. Add primary keyword/location to the hero text without losing the brand line.
3. Convert the most important CSS background images into semantic `<img>` cards.
4. Replace remote Facebook poster images with local poster files.
5. Add BreadcrumbList schema.
6. Add service-specific schema blocks for the major service pages/sections.
7. Run live PageSpeed and server checks after publishing.

## Unknowns and Follow-Ups

- Core Web Vitals are unknown because this was a local file audit.
- robots.txt, sitemap.xml, and llms.txt were not verified on the live domain.
- External link HTTP status was not verified in this local pass.
- Google Business Profile consistency was not checked.
- Real search performance and queries require Google Search Console data.

