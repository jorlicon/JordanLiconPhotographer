# Wix Integration Guide - Jordan Licon Photography
**Date:** May 5, 2026  
**Site:** https://jordanliconphotogr.wixsite.com/website-3  
**Goal:** Embed optimized SEO pages directly into Wix using HTML embed elements

---

## Overview

You have two main options for embedding the optimized HTML pages into Wix:

### **Option A: Quick & Easy (Recommended for most users)**
- Create new Wix pages
- Use Wix's HTML embed element to insert code snippets
- Keep Wix's native navigation/header
- Minimal technical setup

### **Option B: Advanced (More control)**
- Use Wix Velo (custom code)
- Embed entire pages as iframes
- More complex but more control over styling

**We'll focus on Option A** - it's straightforward and maintains SEO value.

---

## How Wix HTML Embeds Work

Wix allows you to embed custom HTML/CSS/JavaScript using:
1. **HTML Embed Element** - In the Wix Editor
2. **Site Code/Custom Code** - In Wix Settings
3. **Wix Velo** - Advanced code editor

**Important:** Wix embeds code as snippets within their page structure, not as standalone pages. This means:
- ✅ You can use `<style>` tags to apply custom CSS
- ✅ You can embed `<script>` tags (including schema markup)
- ✅ You can use `<div>` containers with custom content
- ❌ You cannot use full `<html>` and `<body>` tags
- ❌ Some CSS may be overridden by Wix's default styles

---

## Step-by-Step Integration Process

### **PHASE 1: Prepare Your Wix Site**

#### Step 1: Log into Wix
1. Go to https://www.wix.com and log in
2. Click on your site "website-3"
3. Click "Edit Site" to open the Wix Editor

#### Step 2: Create New Pages for Your SEO Content
In Wix Editor, create these new pages:

1. **Executive Headshots** page
   - Page name: "Executive Headshots"
   - URL slug: "/executive-headshots-el-paso" (if possible)
   - Keep blank for now - we'll add content

2. **Actor Headshots** page
   - Page name: "Actor Headshots"
   - URL slug: "/actor-headshots-el-paso"

3. **Corporate Team Headshots** page
   - Page name: "Corporate Team Headshots"
   - URL slug: "/corporate-team-headshots-el-paso"

4. **Blog: Professional Headshot Guide** page
   - Page name: "Professional Headshot Photography Guide"
   - URL slug: "/blog/professional-headshot-photography-guide"

5. **Blog: LinkedIn Profile Photo Guide** page
   - Page name: "LinkedIn Profile Photo Guide"
   - URL slug: "/blog/linkedin-profile-photo-guide"

#### Step 3: Set Up Site Code for Schema Markup
1. In Wix Editor, go to **Settings** → **Custom Code** (or **Advanced** → **Code**)
2. Go to **Custom Code** tab
3. Add this in the **Head** section:

```html
<!-- Schema Markup for Organization -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ProfessionalService",
  "@id": "https://jordanliconphotography.com",
  "name": "Jordan Licon Photography",
  "url": "https://jordanliconphotography.com",
  "telephone": "+1-915-226-6037",
  "email": "info@jordanliconphotography.com",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2201 East Mills Ave, 2nd Floor",
    "addressLocality": "El Paso",
    "addressRegion": "TX",
    "postalCode": "79901",
    "addressCountry": "US"
  },
  "areaServed": ["El Paso, TX", "Las Cruces, NM", "Southwest USA"],
  "image": "https://static.wixstatic.com/media/00f94f_131ad6e3db184ac383b9669a5fcc72da~mv2.jpeg",
  "description": "Professional photography services in El Paso including executive headshots, architectural photography, drone photography, and commercial work.",
  "sameAs": []
}
</script>
```

---

### **PHASE 2: Embed the Executive Headshots Page**

#### Step 1: Add HTML Embed Element to the Page
1. Open the **Executive Headshots** page in Wix Editor
2. Click **Add** (+ button)
3. Search for **"HTML"**
4. Select **"HTML Embed"** (NOT "HTML iframe")
5. Click to add it to your page

#### Step 2: Copy and Paste the Code Snippet

Click on the HTML embed element and select **Edit Code**. Paste this code:

```html
<style>
  body{margin:0;background:#060606;color:#f0ebe2;font-family:Arial,sans-serif;line-height:1.65}
  main{max-width:1080px;margin:auto;padding:36px 24px}
  a{color:#b8985f}
  h1{font-family:Georgia,serif;font-size:clamp(32px,6vw,52px);line-height:.95;font-weight:300;margin:0 0 24px 0}
  h2{font-family:Georgia,serif;font-size:clamp(24px,4vw,36px);font-weight:300;margin:36px 0 18px 0}
  h3{font-family:Georgia,serif;font-size:18px;font-weight:400;margin:24px 0 12px 0}
  p{margin:0 0 16px 0}
  .intro-text{font-size:18px;line-height:1.8;margin:24px 0}
  ul,ol{margin:16px 0;padding-left:24px}
  li{margin:8px 0}
  .grid{display:grid;gap:18px;margin:36px 0}
  @media(min-width:760px){.grid{grid-template-columns:repeat(3,1fr)}}
  .card,.faq{border:1px solid rgba(240,235,226,.15);padding:24px;background:#141414;margin:24px 0}
  .proof{display:grid;gap:12px;margin:28px 0}
  @media(min-width:760px){.proof{grid-template-columns:repeat(3,1fr)}}
  .proof div{border-top:1px solid rgba(240,235,226,.18);padding-top:14px;font-size:14px}
  .btn{display:inline-block;margin:12px 12px 0 0;padding:14px 20px;border:1px solid #f0ebe2;color:#060606;background:#f0ebe2;text-decoration:none;font-weight:bold;cursor:pointer}
  .btn:hover{background:#d4cfc0}
  .pricing-table{border-collapse:collapse;width:100%;margin:24px 0}
  .pricing-table th,.pricing-table td{padding:12px;border:1px solid rgba(240,235,226,.15);text-align:left}
  .pricing-table th{background:#141414;font-weight:bold}
  .highlight{background:rgba(184,152,95,.1);padding:16px;border-left:3px solid #b8985f;margin:24px 0}
</style>

<main>
  <h1>Executive Headshots in El Paso</h1>
  
  <p class="intro-text">Professional leadership portraits for C-suite executives, founders, business owners, and corporate leaders. Cinematic lighting, polished portraiture, and expression coaching to convey confidence, authority, and approachability.</p>
  
  <div class="proof">
    <div><strong>5.0 Google Rating</strong><br>Trusted by executives, entrepreneurs, and corporate teams across El Paso.</div>
    <div><strong>Professional Studio & On-Location</strong><br>Private studio sessions or on-site at your corporate office.</div>
    <div><strong>From $350</strong><br>Includes 1 finalized headshot, 3 outfits, and usage-ready files.</div>
  </div>

  <h2>Why Executive Headshots Matter</h2>
  <p>Your professional headshot is often the first impression potential clients, partners, and stakeholders have of you. An executive portrait signals professionalism, trustworthiness, and leadership presence.</p>
  
  <p>Professional headshots are used for:</p>
  <ul>
    <li><strong>LinkedIn profiles</strong> - Stand out in your network with a polished, approachable image</li>
    <li><strong>Corporate websites</strong> - Build credibility on your company's leadership page</li>
    <li><strong>Marketing materials</strong> - Use in press releases, email signatures, and branding</li>
    <li><strong>Speaking engagements</strong> - Professional image for conference websites and promotional materials</li>
    <li><strong>Networking events</strong> - Make a strong impression at industry gatherings</li>
  </ul>

  <h2>What's Included in Your Executive Headshot Session</h2>
  
  <div class="grid">
    <div class="card">
      <h3>Consultation</h3>
      <p>Pre-session discussion about your brand, industry, and desired image.</p>
    </div>
    <div class="card">
      <h3>Cinematic Lighting</h3>
      <p>Professional studio lighting that flatters your features and conveys confidence.</p>
    </div>
    <div class="card">
      <h3>Direction & Coaching</h3>
      <p>Expert guidance on posture, angles, and expression for natural, confident results.</p>
    </div>
  </div>

  <h2>Headshot Pricing</h2>
  <table class="pricing-table">
    <tr><th>Package</th><th>Price</th><th>Includes</th></tr>
    <tr><td>Individual Executive Headshot</td><td>$350</td><td>1 finalized headshot + 3 outfits + retouching + digital files</td></tr>
    <tr><td>Additional Finalized Headshots</td><td>$200 each</td><td>Alternative looks from same session</td></tr>
    <tr><td>Extended Session (6 outfits)</td><td>$500</td><td>2 finalized headshots + 6 outfits + retouching</td></tr>
  </table>

  <div class="highlight">
    <strong>Studio Location:</strong> 2201 East Mills Ave, 2nd Floor, El Paso, TX 79901
  </div>

  <h2>Executive Headshot FAQ</h2>
  <p><strong>Q: What should I wear to my executive headshot session?</strong><br>
  A: Wear solid colors or subtle patterns. Business attire is standard—think what you'd wear to a client meeting.</p>
  
  <p><strong>Q: How long does a session take?</strong><br>
  A: Individual sessions typically take 45-60 minutes, including setup, consultation, outfit changes, and proofing.</p>

  <p><strong>Q: Do you retouch executive headshots?</strong><br>
  A: Yes. Professional retouching is included in all sessions.</p>

  <a class="btn" href="https://jordan-licon-photography.bloom.io">Book Executive Headshot Session</a>
  <a class="btn" href="/headshot-portfolio">View Headshot Portfolio</a>
</main>

<script type="application/ld+json">
{
  "@context":"https://schema.org",
  "@type":"Service",
  "name":"Executive Headshot Photography",
  "provider":{
    "@type":"ProfessionalService",
    "name":"Jordan Licon Photography",
    "url":"https://jordanliconphotography.com/",
    "telephone":"+1-915-226-6037",
    "email":"info@jordanliconphotography.com",
    "address":{
      "@type":"PostalAddress",
      "streetAddress":"2201 East Mills Ave, 2nd Floor",
      "addressLocality":"El Paso",
      "addressRegion":"TX",
      "postalCode":"79901",
      "addressCountry":"US"
    }
  },
  "serviceType":"Executive headshot photography",
  "areaServed":["El Paso, TX","Las Cruces, NM","Southwest USA"],
  "offers":{
    "@type":"AggregateOffer",
    "lowPrice":"350",
    "highPrice":"1950",
    "priceCurrency":"USD"
  }
}
</script>
```

#### Step 3: Adjust and Publish
1. Click **Done** to save the embed
2. Preview the page to check styling
3. If styling looks off, click the embed again and adjust CSS
4. When satisfied, **Publish** the page

---

### **PHASE 3: Add Links from Main Pages**

#### Step 1: Update Your Homepage
1. Open your **Home** page
2. Find the headshot section
3. Add buttons/links to the new pages:
   - Link text: "Executive Headshots" → `/executive-headshots-el-paso`
   - Link text: "Actor Headshots" → `/actor-headshots-el-paso`
   - Link text: "Corporate Team Headshots" → `/corporate-team-headshots-el-paso`

#### Step 2: Add to Navigation Menu
1. In Wix Editor, click the **Menu** button
2. Add the new pages to your navigation:
   - Headshots → Executive Headshots
   - Headshots → Actor Headshots
   - Headshots → Corporate Team Headshots
3. **Publish** changes

---

### **PHASE 4: Embed Remaining Pages**

Repeat the same process for:

1. **Actor Headshots page** - Use the `actor-headshots-el-paso.html` content
2. **Corporate Team Headshots page** - Use the `corporate-team-headshots-el-paso.html` content
3. **Blog pages** (2) - Use blog post content snippets

For blog posts, you can also use Wix's native blog feature instead of embeds.

---

## Managing Styling Issues

### Common Wix CSS Conflicts

Wix has default styles that might override your embedded CSS. Solutions:

**Option 1: Use `!important` flag**
```css
.btn {
  background: #f0ebe2 !important;
  color: #060606 !important;
}
```

**Option 2: Scope styles more specifically**
```css
.custom-headshot-page .btn {
  background: #f0ebe2;
}
```

**Option 3: Use Wix's custom CSS panel**
In Wix Editor:
- Click **Settings** → **Custom Code** → **Head**
- Add global CSS that won't conflict

---

## SEO Considerations for Embedded Content

### ✅ What Works
- Meta tags in Wix page settings
- Schema.org JSON-LD scripts (embeds work)
- H1/H2 heading hierarchy (preserved)
- Internal linking between pages
- Alt text on images

### ⚠️ What to Monitor
- Meta descriptions (set in Wix page settings, not in embed)
- Page titles (use Wix's SEO panel, not the embed)
- Canonical tags (Wix handles these automatically)
- Mobile responsiveness (test thoroughly)

### How to Set SEO Metadata in Wix
For each embedded page:
1. Click **Settings** (page settings)
2. Go to **SEO** tab
3. Set:
   - **Page title:** (e.g., "Executive Headshots El Paso | Jordan Licon")
   - **Meta description:** (from our pages)
   - **URL slug:** (match our URLs if possible)

---

## Quick Checklist

### Before Publishing
- [ ] Create all 5 new pages in Wix
- [ ] Add HTML embeds to each page
- [ ] Customize CSS if styling is off
- [ ] Test all buttons and links work
- [ ] Set SEO metadata for each page
- [ ] Add pages to navigation menu
- [ ] Update homepage with links to new pages
- [ ] Test on mobile devices
- [ ] Verify booking button (Bloom) works

### After Publishing
- [ ] Update sitemap in Google Search Console
- [ ] Submit updated sitemap to Google
- [ ] Check pages are crawlable (Wix robots.txt)
- [ ] Monitor search rankings for target keywords
- [ ] Track traffic to new pages
- [ ] Monitor conversion rate (inquiries/bookings)

---

## Alternative: Use Wix Blog Feature

For the 2 blog posts, consider using Wix's native blog instead:

**Pros:**
- Better SEO built-in
- Easier to manage
- Better mobile experience
- Social sharing built-in

**Cons:**
- Less design control
- May not match site styling perfectly

**How:**
1. Go to **Blog** section in Wix
2. Create new post
3. Copy content from our blog HTML
4. Format in Wix editor
5. Add internal links
6. Publish

---

## Troubleshooting

### Issue: Styling looks wrong
**Solution:** 
- Wix CSS is overriding your embedded CSS
- Add `!important` to your CSS rules
- Or use more specific selectors

### Issue: Buttons don't look right
**Solution:**
- Wix button styling may conflict
- Rename button class (e.g., `.booking-btn` instead of `.btn`)
- Update CSS accordingly

### Issue: Mobile looks bad
**Solution:**
- Embedded content may not be responsive
- Use media queries in your CSS
- Test on actual mobile device
- Adjust breakpoints for Wix layout

### Issue: Links don't work
**Solution:**
- Make sure Wix page exists first
- Use relative URLs: `/page-name`
- Or full URLs: `https://jordanliconphotogr.wixsite.com/website-3/page-name`

---

## Pro Tips

1. **Keep a backup** - Save original HTML files locally
2. **Test thoroughly** - Check all devices and browsers
3. **Monitor analytics** - Track which pages drive bookings
4. **Update regularly** - Keep content fresh and add new blog posts
5. **Use Wix's native features** - Blog, galleries, forms when possible
6. **Plan for growth** - This structure scales well if you add more services

---

## Next Steps

1. Log into your Wix account
2. Create the 5 new pages (step 1-2 above)
3. Add HTML embeds to each page (step 2)
4. Copy/paste the content snippets
5. Adjust styling as needed
6. Update navigation and homepage links
7. Set SEO metadata in Wix
8. Publish and test

---

**Questions?** Each page has the HTML snippet ready to copy/paste. The code is production-ready!

