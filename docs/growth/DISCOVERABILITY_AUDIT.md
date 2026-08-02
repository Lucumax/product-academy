# Discoverability Audit

Date: 2026-08-02. Branch: `skills-discoverability-growth-v1`. Author: principal
open-source product-growth engineer (adversarial review pass).

Scope: the public acquisition and activation surface of
`github.com/Lucumax/product-academy` and its agent-skill pack.

Evidence labels used throughout: **[V]** verified (observed directly via GitHub API,
the deployed site, or a tested command); **[I]** inference (reasoned from verified facts,
not independently confirmed — e.g. search ranking, which requires a live browser I did not
use).

## 1. Current public state (verified)

| Item | State | Evidence |
|---|---|---|
| Repository | `Lucumax/product-academy` | **[V]** git remote |
| Default branch | `main` | **[V]** |
| Stars / forks / watchers | 0 / 0 / 0 | **[V]** GitHub API |
| Topics | none (empty array) | **[V]** GitHub API |
| About description | "Evidence-backed product leadership curriculum (Senior PM → CPO) with a guided web app. Doctrine, cases, contradictions, a 180-source evidence registry, an interactive simulator, and role-based learning journeys." | **[V]** GitHub API |
| Homepage | `https://lucumax.github.io/product-academy/` | **[V]** GitHub API |
| Latest release | `skills-v0.2.0` (14 active skills + shared contract + workflows; supersedes v0.1.0) | **[V]** `gh release view` |
| Hardened portfolio on `main` | present (`a6e7b17`) | **[V]** git |
| Skills source | `skills/` with 14 active SKILL.md + 1 deprecated stub | **[V]** validator |
| Tests | 84 passed; Academy 660/660 | **[V]** ran locally |
| Deployed site | `https://lucumax.github.io/product-academy/` | **[V]** Pages API + deploy run success |
| Site nav destinations | Start, Journeys, Doctrine, Simulator, Cases, Sources — **no Skills** | **[V]** `Base.astro` |
| Site build `site` config | `https://product-academy.example.com` (**placeholder**) | **[V]** `astro.config.mjs` |
| Site canonical / OG / robots / sitemap | **absent** | **[V]** `Base.astro`, no sitemap integration, no `robots.txt` |

## 2. What a visitor sees in ten seconds (verified)

- **GitHub repo page:** an "Academy" described as a curriculum with a 180-source evidence
  registry. The word "skills" is not in the About line. A PM searching for a tool cannot tell
  what the skill pack is or how to install it from the storefront.
- **Homepage (site):** curriculum-first — guided journeys, doctrine, cases, contradictions,
  sources, simulator. No agent-skill proposition above the fold, no install path, no Skills
  nav. **[V]** inspected nav + layout.
- **README:** a skills section was added in the hardening cycle, but the hero is still
  Academy/curriculum language; the ten-second comprehension test (what/who/which skill/how to
  install) is not met above the fold. **[V]**

## 3. Search and directory state

### GitHub discoverability

- Description and README lead with "curriculum," "doctrine," "evidence registry." A query
  like "product management skills Claude" matches the top competitors (6,199★
  Product-Manager-Skills, 1,212★ lenny-skills), not this repo. **[I]**
- Empty topics → GitHub's topic browsing does not surface the repo. **[V]**

### Google / external search

- No site surface is optimized for skills queries (no `/skills/` pages, no per-skill pages,
  placeholder `site` config, no sitemap, no metadata). **[V]** for the absence of artifacts;
  the ranking consequence is **[I]** but structurally unavoidable.
- The curriculum pages exist but are titled around doctrine/cases, not "AI skill for X."
  **[V]**

### Agent-skill directories / installers

- `skills.sh` CLI: the repo is **not verified** to be indexed; `npx skills add
  Lucumax/product-academy --list` must be tested (Phase 4). No badge, no page. **[I until tested]**
- Claude Code marketplace: `.claude-plugin/marketplace.json` + `plugin.json` exist and were
  added in the hardening cycle; the `/plugin marketplace add` path is documented. Whether
  Claude Code's marketplace discovery lists it is not verifiable from here (requires a logged-in
  Claude Code session). **[I]**
- Codex/Cursor/OpenCode: ZIP installs are documented and the ZIPs are verified to build;
  no directory listing/ranking is claimed. **[V]** for the mechanism, **[I]** for ranking.

## 4. Competitive benchmark (verified)

| Repo | Stars | Description | First-screen pattern |
|---|---|---|---|
| deanpeters/Product-Manager-Skills | 6,199 | "Product Management skills framework built on battle-tested methods for Claude Code, Cowork, Codex, and AI agents." | ASCII hero + badges; "Why This Exists"; task-based nav; install table ("Choose your setup"); downloads shelf; platform list; changelog; contributing |
| RefoundAI/lenny-skills | 1,212 | "86 product management skills from Lenny's Podcast for Claude Code and AI agents." | Audience/authority-led; numbered skill list; install + platform docs |
| kuchin/awesome-cto | 35,265 | Curated list for CTOs | Curated-list pattern (table of contents, categorized links) |
| jorgef/engineeringladders | 8,536 | "A framework for Engineering Managers" | Framing + ladder content, low install friction (markdown) |

Pattern the leader exploits that we lack:

1. **Positioning-first hero** — the product is stated in the first line as skills for agents,
   with badges and an install path in the first screen.
2. **Task-based navigation** — "What You Can Get Done" grouped by PM job, each linked to a
   skill.
3. **Zero-friction install table** — one row per platform; "not sure → starter pack."
4. **Downloads shelf** (`/dist`) — a browsable download path in-repo, not only Releases.
5. **Visible update cadence** — frequent, dated releases in the README ("What's New").
6. **Audience/authority** — a named practitioner author with an existing audience.
7. **Platform breadth list** — "Works with" a long agent list.

## 5. Scored assessment (1–10)

| Dimension | Score | Basis |
|---|---|---|
| GitHub discoverability | 2 | Empty topics, curriculum-first description, no skills keywords, zero stars |
| Google discoverability | 2 | No indexable skills pages, placeholder site config, no sitemap/metadata |
| Agent-directory discoverability | 2 | Not verified in skills.sh; no directory listings; marketplace present but unverifiable |
| Positioning clarity | 3 | Skills section exists in README but hero is curriculum-first |
| Differentiation clarity | 5 | Evidence-backed decisions is a real differentiator but not stated first |
| Installation friction | 6 | ZIPs + marketplace manifest exist and build; README install is above the fold now |
| First-use activation | 4 | Copy-paste prompts exist; no per-skill demos, no visual proof, no playground |
| Trust | 4 | Real validation gates, honest evals, CC BY 4.0, zero stars/forks, no named maintainer |
| Shareability | 3 | No social preview, no demos, no shareable landing pages |
| Contribution readiness | 3 | No CONTRIBUTING, no issue templates, no roadmap, no "good first issue" |
| Conversion to star | 3 | Nothing above the fold makes a visitor want to star; no ask |
| Conversion to installation | 4 | Install paths work but are not the first thing a visitor sees |
| **Overall** | **3.4** | **Skill product ≈8/10 internally; public acquisition surface ≈3.4/10** |

## 6. Root-cause summary

The skill product outruns its storefront. Nothing verifiable is broken in the product
(validated, packaged, released); almost everything a first-time visitor or a search engine
touches is curriculum-shaped or missing. The single highest-leverage fixes, in order:

1. Reposition the storefront around the skill product (README hero + About + homepage).
2. Make `/skills/` a real, indexable site section with a per-skill and per-workflow page.
3. Fix the placeholder `site` URL, add canonical/OG/robots/sitemap.
4. Add topics + social preview + CONTRIBUTING/issue templates.
5. Test and, where real, surface native install paths (skills.sh CLI).

## 7. What this audit does not claim

- No live Google search was executed (no browser); ranking claims are labeled **[I]** and are
  structural inferences from missing artifacts, which is a safe direction even when exact
  positions are unknown.
- No skills.sh index status is claimed; it is tested in Phase 4.
- No star, install, or adoption number is claimed anywhere in this sprint.
