# SEO Implementation Execution Log

Updated: 2026-09-08

Semrush rule: do not spend the free monthly Semrush Site Audit crawl until the current implementation cycle is complete and the user explicitly approves the crawl.

## Hourly Schedule

Status: Active via Codex automation `hourly-seo-implementation-follow-up`.

The schedule should continue only while there are open actions. When all actions are complete and no new action is present, pause the automation and report completion.

## Checklist

| Area | Status | Notes |
| --- | --- | --- |
| Cloudflare / HSTS | Blocked by account/DNS setup | Live headers still show GitHub Pages and no `Strict-Transport-Security`. Cloudflare rules are documented in `CLOUDFLARE-SEO-RULES-2026-08-30.md`. |
| Google Business Profile | Verified, needs optimization review | Correct account is `jordanliconphotography@gmail.com`. Profile is verified and shows 2201 E Mills Ave, El Paso, TX 79901. |
| Review workflow | Implemented locally | Review request, follow-up, and reply templates created in `REVIEW-GENERATION-WORKFLOW.md`. Direct Google review link still needs to be copied from GBP. |
| Author / trust signals | Implemented locally | Visible author/reviewed blocks and `dateModified` schema added to 22 blog posts. |
| Backlinks / local mentions | Implemented locally | Outreach tracker and templates created in `LOCAL-AUTHORITY-OUTREACH.md`. |
| Internal linking / orphan check | Complete locally | Local crawl found no sitemap URLs with zero inbound links and no public utility pages missing `noindex`. |
| Analytics / UTMs | Published | Stale `utm_` and `fbclid` parameters were removed from Bloom booking links. GA4 stream `G-8RM5RMX40Y` points to `https://www.jordanliconphotography.com`. GTM container `GTM-TMDNZGQ` Version 2 is live with Google Tag `G-8RM5RMX40Y`. The site files containing the GTM container and conversion listener have been published. |
| Conversion tracking | Implemented locally | Added a sitewide `data-jlp-conversion-tracking` listener to public HTML pages so Bloom booking, Bloom portal, `mailto:`, `tel:`, contact-anchor, submit-button, and form-submit interactions push clean `dataLayer` events for GTM/GA4. |
| Canonical brand URLs | Implemented locally | Homepage social preview and schema image URLs now use `www.jordanliconphotography.com` instead of the old GitHub Pages URL. |
| Confirmed profile links | Implemented locally | Added the confirmed Headshot Crew profile to homepage business/person `sameAs` entries alongside Instagram and IMDb. |
| Content refresh | Published, continuing by priority | Article schema descriptions, empty intro placeholders, and simple guide publish dates were cleaned up. Generic-looking image replacement is complete for the local commercial photography trends article, the indexed drone photography article, and six additional older blog posts; see `CONTENT-REFRESH-LOG.md`. |
| Six Figure Photography website feedback | Published | Homepage service-path copy now emphasizes buyer outcomes and dream-client fit; public-facing `AI generated` image alt wording was replaced with professional service descriptions. Homepage hero copy now uses the preferred storyteller/creator positioning. |
| Bloom widget styling | Reverted and published | Removed the Bloom-specific gray button override from every public HTML page so the Bloom inquiry button returns to its default/original styling. The Bloom widget embed remains installed. |
| Service / portfolio positioning copy | Published | Headshot, portrait/fashion, executive, actor, corporate team, drone, cinematography, and commercial service pages were refreshed with buyer-specific credibility language influenced by Ben Harley / Six Figure Photography feedback. |
| Publish | Complete | Published to `main` in `jorlicon/JordanLiconPhotographer`. GitHub Pages build/deploy run `34209047319` completed successfully. Latest commit: `050ffb6` (`Refine buyer-focused copy and blog imagery`). |

## Current Evidence

- `https://www.jordanliconphotography.com/` returns `HTTP 200` from `server: GitHub.com`.
- `https://jordanliconphotography.com/` returns `301` to the `www` host.
- HSTS is not present in live response headers.
- The correct Google Business Profile account shows one verified business.
- Clean Bloom links now resolve to canonical booking, discovery, and client login URLs on the published site.
- Homepage social image metadata now uses the official domain.
- Homepage business/person schema now includes the confirmed Headshot Crew profile.
- All 22 public blog posts have non-empty article schema descriptions.
- `post/embracing-local-commercial-photography-trends.html` now uses existing food/restaurant portfolio imagery instead of generic Wix-era visual placeholders; its Open Graph image, article schema image, alt text, dimensions, and captions were updated and JSON-LD parses successfully.
- `post/elevating-visuals-with-drone-photography-and-videography.html` now uses existing drone/architecture portfolio imagery instead of generic Wix-era visual placeholders; its Open Graph image, article schema image, alt text, dimensions, captions, and `blog.html` archive card were updated and JSON-LD parses successfully.
- Existing Analytics stream `G-8RM5RMX40Y` is associated with the `Jordan Licon Photography - GA4` property and now has URL `https://www.jordanliconphotography.com`.
- GTM Version 2 is live and contains the corrected Google Tag destination `G-8RM5RMX40Y`.
- Public HTML scan found no remaining missing/empty image alt attributes and no remaining `AI generated` wording outside non-public backup/Stitch files.
- Published homepage now adds a clearer service-path introduction and more buyer-specific copy for headshots, architecture, and commercial production.
- Published homepage hero now reads: “For El Paso brands, executives, restaurants, architects, and agencies, Jordan Licon creates photography and cinematography that turns real work into a clear visual story, helping clients see the value, character, and credibility behind the business.”
- Published homepage service-path card now reads “Headshots for leaders and performers” instead of the older executive/actor/pageantry sentence.
- Bloom gray-button override was removed from all 42 public HTML pages that include the Bloom widget, restoring the original Bloom button styling.
- Published service and portfolio pages now use stronger buyer-outcome language: credible leadership portraits, casting clarity, aligned team headshots, aerial coverage for decisions and records, cinematography for story/trust/campaign use, and commercial imagery planned around actual placements.
- Sitewide conversion listener is present on 57 public HTML pages; the only scanned HTML file without it is `.stitch/source-index-for-mimic.html`, which is a design/source artifact rather than a public page.
- GitHub Pages deployment completed successfully. Non-blocking workflow annotation remains: GitHub is forcing `actions/upload-artifact@v4` from Node.js 20 to Node.js 24; this did not block deployment.
- GitHub Pages deployment for service/portfolio copy refresh completed successfully. Commit: `a230ca9` (`Refresh service portfolio positioning copy`). Run `34166754933`.
- GitHub Pages deployment for the homepage storyteller copy, buyer-specific CTA refresh, and six additional real blog image replacements completed successfully. Latest commit: `050ffb6` (`Refine buyer-focused copy and blog imagery`). Run `34209047319`.
