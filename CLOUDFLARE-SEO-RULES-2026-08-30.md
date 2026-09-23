# Cloudflare SEO Rules for jordanliconphotography.com

These rules are required outside the static GitHub Pages repository. GitHub Pages cannot reliably enforce apex-to-www redirects, HSTS, cache headers, or bulk URL redirects for legacy paths.

## Required DNS

- Apex `jordanliconphotography.com`: proxied through Cloudflare.
- `www.jordanliconphotography.com`: proxied through Cloudflare and pointed to the GitHub Pages target.

## Canonical Host Redirect

Create a permanent redirect rule:

- If hostname equals `jordanliconphotography.com`
- Then redirect to `https://www.jordanliconphotography.com${uri.path}`
- Status code: `301`
- Preserve query string: yes

## Legacy URL Redirects

Use the paths in `SEO-REDIRECT-MAP-2026-08-30.csv`.

- Apply `301` redirects only where the map has a clear equivalent destination.
- Keep unclear legacy paths as `404` or `410`; do not redirect every obsolete URL to the homepage.

## Security Headers

Set these response headers for all HTML pages:

```text
Strict-Transport-Security: max-age=31536000; includeSubDomains; preload
X-Content-Type-Options: nosniff
X-Frame-Options: SAMEORIGIN
Referrer-Policy: strict-origin-when-cross-origin
Permissions-Policy: camera=(), microphone=(), geolocation=()
```

## Cache Rules

- HTML: cache TTL 10 minutes or bypass cache if editing frequently.
- Images, CSS, JS, fonts: browser TTL 1 year, edge TTL 1 month.
- Sitemap and robots: browser TTL 10 minutes, edge TTL 1 hour.

## After Applying Rules

1. Confirm `https://jordanliconphotography.com/` returns a `301` to `https://www.jordanliconphotography.com/`.
2. Confirm `Strict-Transport-Security` appears on `https://www.jordanliconphotography.com/`.
3. Re-run Semrush Site Audit.
4. Re-submit `https://www.jordanliconphotography.com/sitemap.xml` in Google Search Console.
