# Semrush Issue Action Plan

Date: 2026-08-26
Site: https://www.jordanliconphotography.com/

## Fixed Locally

1. Invalid structured data items
   - Added complete business fields to repeated `ProfessionalService` JSON-LD objects:
     `@id`, `image`, `telephone`, `email`, `priceRange`, `address`, and `areaServed`.
   - Trimmed oversized gallery schema on the three portfolio pages to representative ImageObject entries.
   - Confirmed local JSON-LD parse/completeness check returns `schema_problems 0`.

2. Broken internal image
   - Confirmed `assets/food/display/live-food-44.jpg` exists locally and is a valid JPEG.
   - Confirmed the live image URL returned `HTTP/2 200` during verification, so Semrush's `503` appears transient.

3. Low text-to-HTML ratio
   - Moved food and portrait portfolio inline CSS/JS into external assets.
   - Removed duplicated inline gallery arrays by deriving lightbox data from existing DOM images.
   - Added concise visible service copy to the food, headshot, and portrait portfolio pages.
   - Local ratios after fixes:
     - `food-photography-portfolio.html`: `0.105`
     - `headshot-portfolio.html`: `0.108`
     - `portrait-fashion-portfolio.html`: `0.132`

## Requires Hosting/CDN Change

4. No HSTS support
   - Static HTML cannot add the `Strict-Transport-Security` response header on GitHub Pages.
   - To clear this Semrush notice, put the domain behind a host/CDN that can set headers, such as Cloudflare, or move hosting to a platform that supports custom response headers.
   - Recommended header after HTTPS is stable:
     `Strict-Transport-Security: max-age=31536000; includeSubDomains; preload`

## Published / Verified

1. Published code fixes
   - Commit `c9d176a0a59ddd36375cd27de7466c096d957ad5` was pushed to `main`.
   - GitHub Pages reported the build as completed for that commit.

2. Live verification
   - `https://www.jordanliconphotography.com/food-photography-portfolio.html`
     now returns a text/HTML ratio of `0.105` with valid JSON-LD.
   - `https://www.jordanliconphotography.com/headshot-portfolio.html`
     now returns a text/HTML ratio above the Semrush threshold with valid JSON-LD.
   - `https://www.jordanliconphotography.com/portrait-fashion-portfolio.html`
     now returns a text/HTML ratio of `0.132` with valid JSON-LD.
   - `https://www.jordanliconphotography.com/assets/food/display/live-food-44.jpg`
     returns `HTTP/2 200` live.

3. Google Search Console
   - Priority URLs checked: drone portfolio, portrait/fashion portfolio, and blog.
   - All three were already indexed when checked.
   - Videos, Breadcrumbs, and Image Metadata enhancement reports showed `Invalid 0`.
   - No validation button was visible on those clean reports.

## Still Pending

1. Rerun Semrush Site Audit
   - The fixes need a fresh Semrush crawl before the Semrush dashboard clears them.
   - The signed-in Semrush page was readable, but browser click dispatch failed while trying to press `Rerun campaign`.
   - Manual fallback: open Semrush Site Audit and click `Rerun campaign`.

2. Confirm Search Console after recrawl
   - If Search Console later shows a `Validate fix` or `Start validation` button for Videos, Breadcrumbs, or Image Metadata, use it.
   - If priority URLs become unindexed, request indexing from URL Inspection.

3. Implement HSTS at hosting/CDN layer
   - The `_headers` file already contains `Strict-Transport-Security`, but GitHub Pages does not apply `_headers` to HTTP responses.
   - Live headers still show `server: GitHub.com` and no `Strict-Transport-Security` header.
   - To clear the HSTS notice, route the domain through Cloudflare or another CDN/host that can inject response headers.
