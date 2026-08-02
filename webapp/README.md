# Product Academy Web App

A beautiful, static web interface for the [Product Leadership Academy](https://github.com/Lucumax/product-leadership-academy) — an evidence-backed product leadership curriculum from Senior PM through CPO.

This is the **`webapp/` folder of the Academy monorepo**. It consumes the Academy content from the repo root — no separate source to configure. Built with [Astro](https://astro.build) + [Pagefind](https://pagefind.app). Output is fully static (no server required).

## What it does

- **Read** — Every document in the Academy, rendered with clean typography.
- **Explore** — Structured browsers for the 16 canonical principles, 18 cases, 13 contradictions, and 180-source evidence registry.
- **Trace** — Epistemic labels `[E] [P] [I] [D] [R]` styled visually, and every claim links to its sources; every principle links to its contradictions and cases.
- **Search** — Full-text search across all 320+ pages.
- **Learn** — Role-based learning paths as navigable pages.

## Quick start

```bash
# 1. Install dependencies
npm install

# 2. Build (imports content from the Academy repo, builds, indexes search)
npm run build

# 3. Serve the static output
npm run preview
```

## Content source

The webapp is a **consumer** of the Academy repo — it never modifies it. Because it lives inside the repo (`webapp/`), the importer reads from the repo root by default.

Override the source path if needed:

```bash
export PRODUCT_ACADEMY_SOURCE=/path/to/product-leadership-academy
npm run build
```

`src/content/` and `src/data/` are generated artifacts (gitignored). Re-run `npm run content:import` any time the Academy content changes.

## Structure

```
product-academy/
├── scripts/
│   └── import-content.mjs        # Parses Academy markdown/YAML → structured JSON
├── src/
│   ├── content/                  # Generated: copied markdown
│   ├── data/                     # Generated: parsed principles/cases/sources/etc.
│   ├── components/
│   │   ├── Markdown.astro        # Markdown renderer w/ epistemic labels
│   │   └── Search.astro          # Pagefind search UI
│   ├── layouts/Base.astro        # Global nav + layout
│   ├── lib/markdown.js           # markdown-it + label/ref post-processing
│   ├── pages/                    # Home, principles, cases, contradictions, sources, paths, tracks, docs
│   └── styles/global.css
└── astro.config.mjs
```

## Routes

| Route | What |
|-------|------|
| `/` | Dashboard: stats, tracks, learning paths, source tiers |
| `/principles/` · `/principles/PRN-0001/` | Doctrine index + evidence-chain detail |
| `/cases/` · `/cases/CASE-0001/` | Case library + detail with causal confidence |
| `/contradictions/` · `/contradictions/CON-0001/` | Tension register with both sides |
| `/sources/` · `/sources/SRC-BOOK-0001/` | Evidence registry by tier + "cited in" graph |
| `/paths/` · `/paths/senior-pm-path/` | Role-based curricula |
| `/tracks/<id>/` | Every track's documents |
| `/doc/<track>/<file>/` | Any raw document, rendered |

## Ecosystem boundary

Per the Academy Constitution, this project **does not modify or duplicate execution logic** from the Academy or Product Forge. It is a pure presentation layer over the Academy's content. If a source repo is unavailable, the importer fails loudly rather than fabricating content.
