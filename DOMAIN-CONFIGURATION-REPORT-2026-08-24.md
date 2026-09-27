# Domain Configuration Report - August 24, 2026

Domain tested: `https://www.jordanliconphotography.com/`

## Summary

The GitHub Pages configuration is correct, and public DNS resolvers are returning the correct GitHub Pages records. The only remaining issue observed during testing is propagation/cache: a normal public request from this network is still being answered by Wix/Pepyaka, while a forced request to GitHub Pages serves the website successfully.

## Correct Items

- `www.jordanliconphotography.com` resolves to `jorlicon.github.io.`
- `jordanliconphotography.com` resolves to the four GitHub Pages A records:
  - `185.199.108.153`
  - `185.199.109.153`
  - `185.199.110.153`
  - `185.199.111.153`
- GitHub repository contains the custom domain file:
  - `CNAME` = `www.jordanliconphotography.com`
- GitHub raw content for `index.html` is reachable with `200 OK`.
- When `www.jordanliconphotography.com` is forced to a GitHub Pages IP, GitHub serves the homepage with `200 OK`.
- Email-related records were not changed during the migration.

## Temporary Item Observed

- A normal request to `https://www.jordanliconphotography.com/` still returned a Wix/Pepyaka `404` from this network during the test.
- Because public DNS already points to GitHub, this is most consistent with propagation or edge cache delay after the DNS switch.

## Recommendation

Wait for DNS and edge cache propagation. Wix indicated DNS changes may take up to 48 hours. Once the domain reliably loads from GitHub Pages, enable or confirm HTTPS enforcement in GitHub Pages settings.

## Final Status

Configuration: correct.

Expected remaining wait: propagation/cache only.
