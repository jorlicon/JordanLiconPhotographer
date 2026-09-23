# SEO ranking execution

Updated: 2026-09-20

## Work completed in this cycle

- Crawled all 37 sitemap pages locally.
- Confirmed every sitemap page has one H1, a unique title, a non-empty description, an indexable robots directive, and at least three internal links from other sitemap pages.
- Added GTM to `success.html` and added a `generate_lead` event on the confirmed inquiry page. This is a stronger lead signal than counting a submit-button click.
- Confirmed the open GTM workspace has no custom-event triggers. Updated the sitewide listener to queue standard Google tag event commands so `jlp_cta_click`, `jlp_form_submit`, and `generate_lead` can reach the existing Google tag without a second GA4 event tag.
- Added GA4 lead context to the inquiry flow: project type, form name, landing page, page title, referrer, and UTM values are retained through the confirmation redirect and sent with `generate_lead`.
- Added explicit Studio session and Natural light session choices to the inquiry form, plus search-focused copy for Railyard Studio and on-site corporate team headshots.
- Added a mobile form pass for in-app browsers: 16px controls to prevent iOS zoom, full-width submit and CTA buttons, and a stacked client-access block.
- Assigned one primary search intent to every commercial page in `SEO-KEYWORD-MAP.md`.
- Repositioned `cinematography.html` for the local commercial intent `El Paso cinematographer` while preserving film and DP proof.
- Removed four duplicate cards from `blog.html`. The archive now has one card per canonical article.
- Replaced heavy legacy blog archive PNG thumbnails with six existing optimized portfolio images. The replacements are about 148-344 KB each and are reused by topic, reducing repeat downloads through browser caching.
- Rewrote thin or generic archive summaries so each card states the question the article answers.
- Kept article consolidation pending Search Console evidence. Multiple headshot articles cover similar language, but deleting or redirecting a page without query data could remove an existing entry point.

## Why these changes can improve results

- A distinct query owner gives Google a clearer page to rank for each commercial need and reduces competition between pages on the same site.
- Commercial pages answer service-selection questions, while articles answer narrower research questions. This creates a direct route from discovery to inquiry.
- Real portfolio images support the site's credibility claims. Smaller reused files reduce the archive's image transfer cost and should make scrolling and returning visits faster.
- A confirmed thank-you-page event measures completed website inquiries. That makes it possible to judge pages by leads, not traffic alone.
- Duplicate archive cards waste crawl and internal-link attention on the same URLs. One card per article makes the archive easier to scan and its internal linking less distorted.

## Live checks required after publication

These checks depend on the published site or signed-in accounts. They are not evidence of a local code failure.

1. Use GTM Preview and GA4 DebugView to confirm `generate_lead` reaches GA4 once after a successful form submission. The inspected workspace had no custom-event triggers, so duplicate event tags were not present at that check.
2. Confirm the priority commercial pages are indexed in Search Console and inspect any page excluded as crawled or discovered but not indexed.
3. Check Search Console query overlap among the six headshot articles and the two drone articles before consolidating any content.
4. Re-run PageSpeed on mobile and desktop after deployment. Compare LCP, CLS, and image transfer size with the prior run.
5. Confirm HTTPS and HSTS headers. GitHub Pages did not provide HSTS in the last verified report; Cloudflare remains an account and DNS task.
6. Check Google Business Profile name, address, phone, services, and landing URL against the official address: 2201 E Mills Ave, El Paso, TX 79901.

## Monthly review

The active automation `monthly-seo-growth-review` runs on the first day of each month at 9:00 AM.

Each run should:

- separate branded from non-branded Search Console performance;
- compare queries and landing pages month over month;
- report organic inquiries, call clicks, email clicks, and Bloom booking actions;
- inspect priority-page indexing, crawl issues, structured data, HTTPS, and Core Web Vitals;
- use the free Semrush audit at most once in the monthly cycle;
- select no more than three actions supported by the evidence;
- avoid publishing or account changes without approval.

## Maturity and stop rule

One monthly cycle counts as mature when all of the following are true:

- priority commercial pages are indexed;
- analytics and confirmed-lead measurement are verified;
- every priority service has one distinct search intent and no unresolved cannibalization;
- no critical crawl, canonical, structured-data, HTTPS, or Core Web Vitals regression remains;
- no unresolved priority action remains.

After three consecutive mature monthly reviews, the automation should report completion and deactivate itself. A particular ranking position is not a maturity requirement because competitors and search results continue to change.

## Current state

- Local implementation: complete for this cycle.
- Publication: complete in commit `f56c5f1` (`Improve SEO intent and conversion measurement`).
- GitHub Pages deployment: run `35570733417` completed successfully on 2026-09-21.
- Live validation: homepage, blog, cinematography, inquiry confirmation, and sitemap returned `HTTP 200`. The live blog showed 18 unique optimized article cards; the live cinematography title and sitemap dates matched the release; the live confirmation page contained GTM and one `generate_lead` command.
- GA4 event receipt: still requires a real successful form submission or a controlled DebugView test. No test inquiry was submitted because that would create a false lead.
- Monthly automation: active until the maturity rule is met.
