# SEO Action Plan - Jordan Licon Photography

## Completed Local Fixes

1. Removed the crawlable truncated backup page by renaming `index.truncated-2026-05-06.html` to `index.truncated-2026-05-06.html.bak`.
2. Converted all canonical tags to absolute production URLs.
3. Added or repaired meta descriptions on every crawlable page.
4. Shortened long titles and long descriptions into crawler-friendly ranges.
5. Improved the blog index title for stronger topical relevance.
6. Added BreadcrumbList schema to all crawlable pages.
7. Added missing BlogPosting schema to article pages.
8. Added ImageGallery schema to the portrait and fashion portfolio.
9. Added Service schema to the drone services page.
10. Converted the three home page Photography Services cards to semantic images with alt text and dimensions.
11. Added default alt text to portfolio lightbox images.
12. Rechecked local links, local assets, image alt text, metadata, canonicals, and JSON-LD.

## Local Verification Result

The local audit now returns clean results:

- Missing descriptions: `0`
- Bad description lengths: `0`
- Missing H1s: `0`
- Multiple H1s: `0`
- Broken local links: `0`
- Missing local assets: `0`
- Images missing alt text: `0`
- Bad canonicals: `0`
- Bad title lengths: `0`
- JSON-LD parse errors: `0`
- Missing breadcrumbs: `0`

## Deployment Checklist

1. Deploy the updated local files when you are ready.
2. Confirm `index.truncated-2026-05-06.html.bak` is not uploaded as a public HTML page.
3. Submit the sitemap in Google Search Console after deployment.
4. Run Google PageSpeed Insights for mobile and desktop.
5. Validate representative pages in Schema Validator:
   - Home page
   - Headshot portfolio
   - Food portfolio
   - Portrait/fashion portfolio
   - Drone services
   - One blog post
6. Run a live broken-link checker against the deployed domain.

## Live-Only Path to a True 100

The intranet build is clean by local SEO checks. A true public 100 still depends on live deployment behavior: Core Web Vitals, compression, cache headers, server response codes, external links, and Google indexing. Those should be tested after you explicitly ask me to update/deploy GitHub.
