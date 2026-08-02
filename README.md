# Product Leadership Academy

An evidence-backed education system for product leaders from Senior PM through CPO — **with a web app** for guided learning.

This is a monorepo. The **content** (doctrine, cases, sources, curriculum) lives at the root. The **web app** — a guided learning journey with progress tracking, an interactive simulator, and full-text search — lives in [`webapp/`](webapp/).

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
| `sources/` | The evidence registry (180 sources, ranked by tier) |
| `evidence/final/` | Processed evidence artifacts (claims ledger, corroboration matrix) |

## Validation

```bash
python scripts/validate_academy.py   # 657 quality-gate checks
python -m pytest -q                  # 57 tests
```

## License

The Academy's original content is licensed under [CC BY 4.0](LICENSE). See [COPYRIGHT_AND_ACCESS_POLICY.md](COPYRIGHT_AND_ACCESS_POLICY.md) for how third-party source material is handled.

## Scope

See [SCOPE.md](SCOPE.md) for what the Academy is and is not.
