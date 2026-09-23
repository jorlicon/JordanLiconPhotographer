# Tracking and UTM Map

Updated: 2026-09-07

## Current State

- No GA4 measurement ID was found in the local site files.
- The live public homepage currently does not load `gtag`, `dataLayer`, Google Analytics collection requests, or the GTM container.
- The local sitemap-listed public pages now include the standard GTM container snippet for `GTM-TMDNZGQ`; this is not live until the website is published.
- Booking links now point to clean canonical Bloom URLs without stale `utm_` or `fbclid` parameters.
- Google Analytics is open in Chrome for account/property `Jordan Licon Photography - GA4`.
- The existing website stream now uses measurement ID `G-8RM5RMX40Y` and URL `https://www.jordanliconphotography.com`.
- Google Tag Manager container `GTM-TMDNZGQ` is published as Version 2, named `GA4 tracking for current website`.
- The GTM Google Tag now points to exactly `G-8RM5RMX40Y`; the malformed `G-8RM5RMX40Y{{Page Hostname}}` value has been corrected.
- GTM diagnostics reports: "Tag stopped sending data" and recommends adding another administrator.
- The main tracked conversion destinations are:
  - `https://jordan-licon-photography.bloom.io/Professional-Headshot`
  - `https://jordan-licon-photography.bloom.io/discovery`
  - `https://jordan-licon-photography.bloom.io/login`

## Recommended GA4 Events

Use these event names once Google Analytics is connected:

| Event | Trigger |
| --- | --- |
| `click_inquire` | User clicks the main Inquire button or scrolls to the inquiry form. |
| `click_client_login` | User clicks the Bloom client portal login button. |
| `click_book_headshot` | User clicks a headshot booking button. |
| `click_start_consultation` | User clicks a commercial/project consultation button. |
| `submit_project_inquiry` | User submits the local inquiry form. |
| `click_email_brief` | User clicks a mailto commercial inquiry link. |
| `click_phone` | User clicks a phone link. |

## Recommended External Campaign UTMs

Use UTMs only on links placed outside the website. Do not add UTMs to internal navigation or normal on-site booking buttons.

| Channel | Example |
| --- | --- |
| Google Business Profile website button | `?utm_source=google&utm_medium=organic&utm_campaign=google_business_profile` |
| Google Business Profile appointment link | `?utm_source=google&utm_medium=organic&utm_campaign=gbp_appointment` |
| Instagram bio | `?utm_source=instagram&utm_medium=social&utm_campaign=profile_link` |
| Facebook page button | `?utm_source=facebook&utm_medium=social&utm_campaign=page_button` |
| Yelp website link | `?utm_source=yelp&utm_medium=referral&utm_campaign=business_listing` |
| Email signature | `?utm_source=email&utm_medium=signature&utm_campaign=general` |

## Next Account-Level Action

Publish the website changes that install `GTM-TMDNZGQ`, then verify live collection in Tag Assistant and GA4 Realtime. The publish path is currently blocked because `/private/tmp/JordanLiconPhotographer-upload` is missing and the local GitHub CLI token for `jorlicon` is invalid.
