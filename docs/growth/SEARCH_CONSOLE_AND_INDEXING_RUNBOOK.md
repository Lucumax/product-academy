# Search Console & Indexing Runbook

This runbook is for **Walter** — it documents the account-access steps that cannot be
performed from this sprint (no credentials). Do not claim any of these were completed;
each is listed with its exact action and the manual access it requires.

## 0. Current verified state (2026-08-02)

- `site:` in `webapp/astro.config.mjs` is `https://lucumax.github.io` with
  `base: "/product-academy"` — canonical URLs, sitemap URLs, nav links, and asset paths are
  all `/product-academy/`-correct.
- `robots.txt` exists and declares the sitemap.
- `@astrojs/sitemap` generates `sitemap-index.xml` + `sitemap-0.xml` with absolute canonical
  URLs, 384 pages including all `/skills/` and `/skills/workflows/` pages.
- Every page has a unique `<title>`, meta description, canonical, Open Graph, and Twitter
  metadata (via `Base.astro`).
- A `404.html` is generated.
- Social-preview images: `webapp/public/og-skills.png` (site) and
  `docs/growth/assets/social-preview-1280x640.png` (GitHub).

## 1. Google Search Console

Requires a Google account authorized for the domain.

1. Add a **Domain property** `lucumax.github.io` (or the URL-prefix property
   `https://lucumax.github.io/product-academy/`).
2. Verify ownership:
   - For a GitHub Pages URL-prefix property, add the provided HTML meta tag to
     `webapp/src/layouts/Base.astro` `<head>`, rebuild, and deploy; or
   - Use the DNS TXT method on the `lucumax.github.io` domain if you control it.
3. Submit the sitemap: **Sitemaps → Submit** `https://lucumax.github.io/product-academy/sitemap-index.xml`.
4. **URL Inspection** for these key pages and click "Request Indexing" after each content
   change:
   - `/product-academy/skills/`
   - `/product-academy/skills/make-go-no-go-call/`
   - `/product-academy/skills/frame-product-problem/`
   - `/product-academy/skills/synthesize-customer-discovery/`
   - `/product-academy/skills/workflows/`
5. After the next release, re-request indexing for changed pages.

## 2. Bing Webmaster Tools

1. Import from Google Search Console (one click) or verify via the same meta-tag method.
2. Submit the same sitemap URL.

## 3. GitHub repository metadata (needs repo admin)

1. **About → Description**: use the recommended description from
   `docs/growth/POSITIONING_DECISION.md`.
2. **About → Website**: `https://lucumax.github.io/product-academy/skills/`.
3. **Topics**: the recommended 20-topic list in `docs/growth/POSITIONING_DECISION.md` (topics
   section) — apply in repo Settings → Topics.
4. **Social preview**: upload `docs/growth/assets/social-preview-1280x640.png` in
   Settings → General → Social preview.

## 4. Post-launch checklist (run after merge + deploy)

- [ ] Sitemap reachable: `curl https://lucumax.github.io/product-academy/sitemap-index.xml`
- [ ] robots reachable: `curl https://lucumax.github.io/product-academy/robots.txt`
- [ ] One skill page loads and its canonical equals its URL.
- [ ] Search Console shows the property and has submitted the sitemap.
- [ ] Re-request indexing for the changed pages.
- [ ] Verify 404: `/product-academy/this-page-does-not-exist` returns the 404 page.
- [ ] LinkedIn/`og:` checker returns the og image for `/skills/`.

## 5. Directory submissions requiring accounts (not performed)

- skills.sh page: created by usage of `npx skills add` (telemetry); do not fabricate one.
- awesome-list PRs and agent-skill directories: listed in `LAUNCH_AND_DISTRIBUTION_PLAN.md`;
  each requires an account and a contribution, none performed here.

## 6. What to NOT do

- Do not submit `https://product-academy.example.com` anywhere (placeholder retired).
- Do not claim Search Console/Bing ownership was performed this sprint (no credentials).
