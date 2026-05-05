# Comprehensive SEO Improvement Plan - Jordan Licon Photography
**Date: May 5, 2026**

## Executive Summary
This plan builds on the successful SEO audit (77/100) and implements advanced strategies to improve rankings, drive qualified leads, and strengthen domain authority. Focus is on headshot photography as the priority service.

---

## Phase 1: Content Strategy & Keyword Targeting

### 1.1 Headshot Service Pages (Priority)
**Create dedicated landing pages for high-intent keywords:**

- `executive-headshots-el-paso.html` - Target: "executive headshot photographer el paso"
  - Corporate leaders, founders, C-suite
  - Professional polish, trust signals
  - Local El Paso authority

- `actor-headshots-el-paso.html` - Target: "actor headshot photographer el paso"
  - Casting-friendly headshots
  - Expression coaching
  - Industry credibility

- `corporate-team-headshots-el-paso.html` - Target: "corporate headshots el paso"
  - Team headshots
  - Consistent branding
  - Multi-person sessions

### 1.2 Content Expansion Strategy

**For each headshot sub-service page, add:**
- 600-800 word keyword-rich content
- Dedicated H1 with service + location keyword
- 4-5 benefits specific to that headshot type
- Pricing and package info
- Local trust proof (address, phone, hours)
- Service-specific FAQ (5-7 questions)
- Dedicated CTA buttons
- Internal links to portfolio and booking

**Keywords to target:**
- "headshot photographer el paso" (primary)
- "executive headshot el paso" (secondary)
- "professional headshot photography el paso"
- "actor headshots el paso"
- "corporate team headshots el paso"
- "pageant headshot photographer el paso"
- "professional headshots near me"
- "linkedin profile photo el paso"

---

## Phase 2: Internal Linking & Topical Clusters

### 2.1 Headshot Cluster Architecture

```
Homepage (index.html)
  ├─ El Paso Headshot Photographer (hub)
  │  ├─ Executive Headshots (satellite)
  │  ├─ Actor Headshots (satellite)
  │  ├─ Corporate Team Headshots (satellite)
  │  └─ Headshot Portfolio
  │
  └─ Blog Posts (linked from hubs)
     ├─ "Professional Headshot Tips"
     ├─ "LinkedIn Profile Photo Guide"
     ├─ "Corporate Headshot Best Practices"
     └─ "Actor Headshot Do's and Don'ts"
```

### 2.2 Internal Linking Improvements

**From homepage:**
- Strengthen headshot CTA with descriptive anchor text
- Link to specific sub-service pages
- Link to relevant blog posts from each service section

**From service pages:**
- Mutual linking between headshot sub-services
- Link from each to the main headshot hub
- Link to 2-3 relevant blog posts
- Link to portfolio with keyword-rich anchor text

**From blog posts:**
- Link back to relevant service pages
- Create breadcrumb trails
- Build topical relevance

---

## Phase 3: Schema Markup Enhancements

### 3.1 Additional Schema to Implement

**1. Individual Service schemas** (in addition to existing):
```json
{
  "@type": "Service",
  "name": "Executive Headshot Photography",
  "provider": { "name": "Jordan Licon Photography" },
  "areaServed": "El Paso, TX",
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Executive Headshot Packages",
    "itemListElement": [
      {
        "@type": "Offer",
        "name": "Individual Executive Headshot",
        "price": "350",
        "priceCurrency": "USD",
        "description": "1 finalized headshot, 3 outfits, usage-ready files"
      }
    ]
  }
}
```

**2. FAQSchema enhancements:**
- 10+ targeted questions per service page
- Answer format: 80-150 characters for rich snippets

**3. LocalBusiness schema strengthening:**
- Add `openingHoursSpecification` when available
- Add `priceRange` for services
- Add service area map coordinates

---

## Phase 4: Content Quality & Readability

### 4.1 Improvements to Implement

**Headshot service pages:**
- Use shorter paragraphs (2-4 sentences max)
- Add numbered lists for benefits
- Use descriptive subheadings for scanning
- Highlight key pricing info in bold
- Add trust signals prominently (Google rating, years, credentials)

**Homepage headshot section:**
- Add a dedicated "Why Choose Jordan for Headshots?" subsection
- Expand with before/after comparisons or testimonial callouts
- Link to headshot blog posts from this section

### 4.2 Readability Target
- Flesch Reading Ease: 55-70 (conversational, professional)
- Sentences: 12-20 words average
- Paragraphs: 3-5 sentences max

---

## Phase 5: Blog Optimization

### 5.1 Existing Blog Audit
Review the 23 existing blog posts for:
- Keyword targeting (do they target service keywords?)
- Internal linking (do they link back to service pages?)
- Metadata quality (title, description under limits?)
- Word count (1,200+ for competitive keywords)

### 5.2 High-Impact Blog Content
**Create/optimize for headshot keywords:**
1. "Professional Headshot Photography Guide"
   - 1,800 words
   - Target: "professional headshot", "what makes a good headshot"
   - Internal links to all headshot service pages

2. "Executive Headshot Photography: Complete Guide for El Paso Leaders"
   - 1,500 words
   - Target: "executive headshot", "professional portrait"
   - Link to executive headshot page

3. "LinkedIn Profile Photo Guide for El Paso Professionals"
   - 1,200 words
   - Target: "linkedin profile photo", "professional linkedin headshot"
   - Link to headshot pages

4. "Corporate Headshot Session Planning Checklist"
   - 1,000 words
   - Target: "corporate headshots", "team headshots"
   - Link to corporate headshot page

---

## Phase 6: Technical & Performance

### 6.1 Image Optimization
- Verify all images have descriptive alt text with keywords where appropriate
- Use modern formats (AVIF/WebP) for hero images
- Optimize video posters for Core Web Vitals
- Add loading="lazy" to below-fold images

### 6.2 Page Speed Priorities
- Monitor LCP (Largest Contentful Paint)
- Optimize Google Fonts loading
- Minimize third-party Wix image dependencies
- Use preconnect for critical domains

### 6.3 Mobile Optimization
- Verify responsive design on headshot pages
- Test CTA button sizing for mobile
- Check form usability on mobile booking flows

---

## Phase 7: Local SEO Strengthening

### 7.1 Local Trust Signals
- Add Google Business Profile review links (if available)
- Verify address consistency: `2201 East Mills Ave, 2nd Floor, El Paso, TX 79901`
- Add service area map/visual (El Paso, Las Cruces, Southwest)
- Link to local photography awards or recognitions if available

### 7.2 Local Keywords
- Ensure "El Paso" appears in all service pages naturally
- Target nearby cities: Las Cruces, Juárez references
- Consider "near me" keyword variations in FAQ

---

## Phase 8: Conversion Optimization

### 8.1 CTA Improvements
- **Primary CTA**: "Book a Headshot Session" (consistent across pages)
- **Secondary CTA**: "View Portfolio & Pricing"
- **Tertiary CTA**: "Get Team Pricing Estimate"

### 8.2 Lead Capture Points
- Booking page integration (Bloom widget - already present)
- Email inquiry form option
- Phone number prominently displayed
- Portfolio viewing encouraged before booking

---

## Implementation Priority Matrix

| Phase | Priority | Timeline | Impact |
|-------|----------|----------|--------|
| 1 | High | Week 1-2 | Content for new keyword targeting |
| 2 | High | Week 2 | Better crawl path, topical authority |
| 3 | Medium | Week 2-3 | Rich snippets, CTR improvement |
| 4 | Medium | Week 1-3 | User engagement, dwell time |
| 5 | High | Week 3-4 | Long-tail traffic, authority |
| 6 | Medium | Week 4 | Core Web Vitals improvement |
| 7 | Medium | Ongoing | Local rankings boost |
| 8 | High | Week 1-2 | Conversion rate improvement |

---

## Success Metrics

**Track these KPIs post-implementation:**

1. **Organic Search**
   - Keyword rankings (track top 5 headshot keywords)
   - Organic traffic increase (target: +40% in 3 months)
   - Click-through rate from SERPs

2. **Engagement**
   - Average session duration
   - Pages per session
   - Blog post engagement

3. **Conversions**
   - Headshot inquiry volume
   - Booking rate
   - Lead quality (industry mix)

4. **Technical**
   - Core Web Vitals scores
   - Mobile usability
   - Crawl errors (should be zero)

---

## Deployment Checklist

- [ ] Create new headshot sub-service pages
- [ ] Expand homepage headshot section
- [ ] Implement enhanced schema markup
- [ ] Create/optimize blog content
- [ ] Build internal linking structure
- [ ] Update metadata on all pages
- [ ] Verify 404 redirects (if any old URLs)
- [ ] Submit updated sitemap to GSC
- [ ] Test mobile responsiveness
- [ ] Run PageSpeed audit
- [ ] Deploy to production
- [ ] Monitor rankings for 2-4 weeks
- [ ] Adjust strategy based on data

---

## Next Steps

1. Review this plan with stakeholder
2. Prioritize quick wins (homepage CTAs, blog optimization)
3. Begin content creation for new service pages
4. Implement internal linking strategy
5. Deploy in phases to monitor impact

