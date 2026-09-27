# GA4 measurement findings

**Property:** Jordan Licon Photography - GA4  
**Report window:** August 26 to September 22, 2026  
**Source:** Google Analytics 4 interface, Traffic acquisition, Lead acquisition, Tech details, and Realtime reports

## What the data says

The site recorded **279 sessions**, **231 engaged sessions**, an **82.8% engagement rate**, and **27 seconds of average engagement time per session** during the 28-day window. There were **1,429 events** and **$0 in reported revenue**.

Organic Search produced **26 sessions**, with an **88.46% engagement rate**, **47 seconds of average engagement time per session**, and **5.77 events per session**. Organic Social produced more visits, with **57 sessions**, but engagement was weaker at **54.39%**, with **6 seconds** of average engagement time. This points to a better-qualified search audience and a social landing-page problem worth testing.

Direct traffic supplied **173 sessions**, or **62.01%** of the total, but averaged only **15 seconds** per session. That combination can mean real branded traffic, missing campaign tags, or visits arriving without usable referral data. It should not be treated as proof of brand demand until campaign tagging is improved.

Referral traffic was small at **16 sessions**, but it had the longest average engagement time at **3 minutes 11 seconds** and **17.94 events per session**. Its reported session key-event rate was only **31.25%**, so the referring URLs and the event definition need review.

AI Assistant traffic was also small, with **6 sessions**, a **100% engagement rate**, and **40 seconds** of average engagement time. It is too small for a trend claim, but the visits are worth preserving through clear service copy, internal links, and structured data.

## Lead measurement problem

The Lead acquisition report recorded:

- **1 new lead** in total;
- **0 qualified leads**;
- **0 converted leads**;
- the one new lead was attributed to Direct.

The Traffic acquisition report showed **781 key events**, which cannot be treated as 781 inquiries. The key-event total is much larger than the new-lead total, so other events are currently marked as key events or are being counted in a way that is too broad for business decisions.

The first measurement repair is to identify every event included in the key-event total and keep only a confirmed inquiry completion event, such as `generate_lead`, as the primary lead key event. The website should also pass a stable `form_name`, `project_type`, and `page_location` with the lead event so the report can show which service pages produce inquiries.

## Browser and mobile signal

GA4 recorded **210 active users** in the browser report. Chrome accounted for **151 users** and Safari for **33**. Safari in-app accounted for **16 users**, but only **2 engaged sessions**, a **12.5% engagement rate**, and **0 seconds** of average engagement time. This is a strong signal to test the inquiry flow from Instagram and other in-app browsers, especially on mobile.

The website should be tested in Safari in-app with these checks:

1. The inquiry form opens without a layout shift.
2. The project-type and budget controls can be opened and selected.
3. The submit button remains visible above any floating inquiry button.
4. The success page loads and records exactly one `generate_lead` event.
5. UTM parameters survive the form submission and success-page redirect.

## Missing information

These are the data gaps blocking better website decisions:

1. The exact event names behind the 781 key events.
2. Page-level sessions, engagement, and leads for the homepage, headshot pages, architecture pages, food page, and commercial page.
3. The actual landing pages for Organic Social, Referral, and AI Assistant sessions.
4. Device category and mobile versus desktop performance.
5. Search query and landing-page joins from Search Console.
6. Source URLs behind Referral traffic.
7. UTM-tagged campaign data for Instagram, Facebook, email, directory links, and outreach.
8. Whether the single recorded lead was a real completed inquiry or a test submission.

## Website work that follows from the evidence

### 1. Repair measurement before changing page copy

Audit the GA4 key-event list and remove generic events from the lead view. Keep `generate_lead` as the business conversion only after one controlled test confirms the event receipt. Add the form fields described above as event parameters. This gives every later content decision a reliable outcome signal.

### 2. Make the inquiry path stronger for social and in-app traffic

Safari in-app traffic is the clearest technical warning in this snapshot. Test the mobile form, remove any obstruction from the floating inquiry control, shorten the first screen of the form, and keep the most useful qualification fields visible in a predictable order: name, email, phone, project type, timeline, budget, location, usage needs, and project notes.

### 3. Improve organic landing-page depth

Organic visitors stay longer than social visitors, but Organic Search is only 9.32% of sessions. Keep the existing service-page structure and strengthen the pages already mapped to search intent: El Paso headshots, executive headshots, corporate teams, architecture and interiors, commercial photography, food photography, drone services, and cinematography. Each page should link to one relevant proof section and one direct inquiry path.

### 4. Tag every off-site campaign

Use consistent UTMs for Instagram, Facebook, email, directory profiles, referral partners, and outbound proposals. At minimum, use `utm_source`, `utm_medium`, and `utm_campaign`. This will reduce the oversized Direct bucket and show which outreach sources produce engaged visits and actual inquiries.

### 5. Investigate Referral traffic before building backlink pages

The referral audience is highly engaged, but the source names are missing from this report. Identify the referring domains and landing pages first. Then decide whether the right response is a partner link, a portfolio proof page, or a clearer call to action on the receiving page.

## Recommended 30-day test

For the next 30 days, measure one clean funnel:

`landing_page -> service_page_view -> inquiry_start -> generate_lead`

Break it down by `sessionSource`, device category, project type, and landing page. The first success target is not more pageviews. It is a trustworthy count of completed inquiries by source and page.

Until that funnel is working, the site should not be judged by the 781 key-event number.
