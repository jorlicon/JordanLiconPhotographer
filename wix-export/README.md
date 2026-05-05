# Wix Export - Pattern 1 Landing Page

## Files

- `pattern-1-landing.html` - Full self-contained HTML/CSS/JS landing page based on Stitch Pattern 1.
- `../assets/test-production-01.mp4` - Upload to Wix Media Manager if you want the first test-production video to play.
- `../assets/test-production-02.mp4` - Upload to Wix Media Manager if you want the second test-production video to play.

## Recommended Wix Placement

Use a full-width Wix HTML Embed element or a dedicated Wix page section that accepts custom HTML.

Recommended embed settings:

- Width: 100%
- Height: at least 7000px for the full page, or use Wix page structure to split sections.
- Page background: black / `#060606`
- Stretch to full width where possible.

## Media Upload Notes

Most images already use hosted `static.wixstatic.com` URLs and do not need uploading.

The only local files that need uploading are:

1. `assets/test-production-01.mp4`
2. `assets/test-production-02.mp4`

After uploading those two videos to Wix Media Manager, replace these strings in `pattern-1-landing.html`:

- `assets/test-production-01.mp4`
- `assets/test-production-02.mp4`

with the Wix Media Manager video URLs.

## Form Behavior

The inquiry form is Wix-safe and does not rely on Netlify. It opens a pre-filled email to:

`info@jordanliconphotography.com`

For CRM capture inside Wix, replace the HTML form with a native Wix Form using the same visible fields.

## Pricing Logic Included

- Individual headshot sessions start at `$350`.
- The base individual session includes `2 finalized headshots` and `3 outfits`.
- Additional finalized headshots are `$200 each`.
- The team calculator uses volume pricing for the first `2 finalized headshots per person`.
- Extra finalized headshots in the team calculator also use the same `$200 each` rate.

## Final Publish Checklist

- Paste the HTML into a Wix HTML Embed or custom-code area.
- Upload the two MP4 files and replace local video paths.
- Test navigation anchors: Headshots, Architecture, Commercial, Credits, Blog, Contact.
- Test the corporate headshot calculator sliders and add-ons.
- Test the inquiry form mailto behavior.
- Test both video players after replacing the MP4 URLs.
- Check desktop and mobile preview before publishing.
