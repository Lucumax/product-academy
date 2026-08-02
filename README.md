# Product Leadership Academy

An evidence-backed education system for product leaders from Senior PM through CPO — **with a web app** for guided learning.

This is a monorepo. The **content** (doctrine, cases, sources, curriculum) lives at the root. The **web app** — a guided learning journey with progress tracking, an interactive simulator, and full-text search — lives in [`webapp/`](webapp/).

## Agent Skills (AI decision pack)

Evidence-backed product management **skills for AI agents** — frame product problems,
synthesize customer discovery, prioritize opportunities, design experiments, align
stakeholders, and make defensible product decisions (GO/NO-GO, PMF health, AI evaluation
contracts, causal review, premortem). Every skill returns a verdict or decision artifact with
a next action, in fast mode (reversible calls) or full mode (one-way doors).

- **Install:** Claude Code `/plugin marketplace add Lucumax/product-academy` → `/plugin install evidence-pack`; or download a release ZIP for Claude.ai, Codex, Cursor, and generic agents.
- **Find your skill:** [`skills/INDEX.md`](skills/INDEX.md) (finder by PM job + copy-paste invocations)
- **Workflows:** [`skills/workflows/`](skills/workflows/) (product bet, experiment decision, launch gate, product health review)

> Note: `main`/skills is currently the pre-hardening ten-skill pack. The hardened 14-skill
> portfolio ships on the `skill-hardening-product-manager-v1` branch and as release
> `skills-v0.2.0`.

## Quick Start

**Read the content** — start with [00_orientation/](00_orientation/), the [Curriculum Map](CURRICULUM_MAP.md), and [Core Doctrine](01_core_doctrine/PRINCIPLES.md).

**Run the web app:**

```bash
cd webapp
npm install
npm run build      # imports content + builds static site + indexes search
npm run preview    # serve locally, or deploy dist/ anywhere static
```

The webapp reads content directly from this repo (monorepo layout) — no separate source to wire up.

## Structure

| Area | Purpose |
|------|---------|
| `00_orientation/` | Getting started and capability model |
| `01_core_doctrine/` | Canonical product leadership principles |
| `02_principal_plus/` | Principal PM and above capabilities |
| `03_business_and_gtm/` | Business economics and go-to-market |
| `04_product_archetypes/` | 13 product archetype patterns |
| `05_ai_product_management/` | AI product management |
| `06_industry_overlays/` | Industry-specific constraints |
| `07_cases/` | Decision case studies |
| `08_contradictions/` | Unresolved product leadership tensions |
| `09_tools/` | Practical templates and frameworks |
| `10_simulator/` | Practice scenarios |
| `11_learning_paths/` | Role-based learning paths |
| `12_personal_lab/` | Self-directed practice |
| `13_career_transitions/` | Landing product roles, credibility building, emerging roles |
| `webapp/` | The Astro web app (guided journey, simulator, search) |
| `handbook/`, `docs/` | Generated handbooks and integration docs |
| `sources/` | The evidence registry (184 sources, ranked by tier) |
| `evidence/final/` | Processed evidence artifacts (claims ledger, corroboration matrix) |

## Validation

```bash
python scripts/validate_academy.py   # 658 quality-gate checks
python -m pytest -q                  # 57 tests
```

## License

The Academy's original content is licensed under [CC BY 4.0](LICENSE). See [COPYRIGHT_AND_ACCESS_POLICY.md](COPYRIGHT_AND_ACCESS_POLICY.md) for how third-party source material is handled.

## Scope

See [SCOPE.md](SCOPE.md) for what the Academy is and is not.
