# GEO Analysis - Jordan Licon Photography

Date: 2026-09-06

## Readiness Score

Current GEO readiness: 82/100 after this first optimization pass.

The site already has strong service-specific pages, local business schema, review signals, a sitemap, an `llms.txt` file, and crawlable public HTML. The biggest remaining opportunities are expanding source-like answer passages across priority service pages, strengthening off-site entity consistency, and adding more expert/citation material that AI systems can confidently quote.

## What Was Added

- Expanded `llms.txt` with answer-ready summaries for the business, location, services, and credibility.
- Added query intent routing in `llms.txt` so AI crawlers can map common search intents to the best page.
- Added explicit allow rules in `robots.txt` for major AI/search crawlers including GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, PerplexityBot, Googlebot, and Bingbot.
- Added a homepage "Quick Answers" section with self-contained, citable passages.
- Added SpeakableSpecification schema selectors for the new homepage answer blocks.

## Platform Readiness

Google AI Overviews: Good foundation. The site has crawlable pages, local/service schema, FAQ content, and direct answer blocks.

ChatGPT browsing/SearchGPT style answers: Improved. `llms.txt` now gives direct summaries and routing guidance, and robots explicitly allows OpenAI crawlers.

Perplexity: Improved. The new answer blocks and `llms.txt` summaries make the business easier to cite with a source link.

Claude and other web-aware assistants: Improved. The robots policy and concise source-style summaries reduce ambiguity.

## Crawlability

Public pages appear intended to be crawlable. Utility and legacy pages remain disallowed in `robots.txt`, which is correct for index hygiene. The sitemap remains declared at:

https://www.jordanliconphotography.com/sitemap.xml

## Passage Citability

The homepage now includes direct answers to:

- What is Jordan Licon Photography?
- Where is Jordan Licon Photography located?
- What services does Jordan Licon Photography offer?
- Why choose Jordan Licon Photography?

These are written as complete passages so answer engines can quote or summarize them without stitching context from several sections.

## Remaining Priority Changes

1. Add similar answer-ready blocks to the main service pages: headshots, architecture, commercial production, food, drone, and editorial portraits.
2. Add stronger author/about references on blog posts so AI systems can connect advice content back to Jordan Licon as the expert source.
3. Add sameAs links for confirmed external profiles only after verifying the exact URLs: Google Business Profile, Facebook, Yelp, Apple Business, Headshot Crew, Instagram, IMDb, and Chamber profile if public.
4. Add cited proof points where available: publications, awards, memberships, brand credits, review profile links, and licensing/credential pages.
5. Keep NAP consistent everywhere: Jordan Licon Photography, 2201 East Mills Ave, 2nd Floor, El Paso, TX 79901, +1 915 226 6037.
6. Continue resolving Google Search Console indexing issues so answer engines discover only canonical public pages.

## Content Opportunities

- Create a concise "Best commercial photographer in El Paso" evidence page focused on process, portfolio categories, credentials, service area, and buyer FAQs.
- Create short glossary-style pages for executive headshots, architectural photography, food photography, and drone production in El Paso.
- Add blog posts that answer comparison and buying-intent queries, such as "How much do commercial headshots cost in El Paso?" and "What should businesses look for in an architectural photographer?"
