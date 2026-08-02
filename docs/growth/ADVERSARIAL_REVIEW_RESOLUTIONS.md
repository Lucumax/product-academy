# Adversarial Review Record — Discoverability Sprint

Date: 2026-08-02. Reviewer: independent adversarial subagent (second model) on branch
`skills-discoverability-growth-v1`. Disposition returned: **NOT_READY** (flips to
ACCEPT_WITH_BOUNDED_FIXES after the top-five fixes). The reviewer re-ran `npx skills add`,
rebuilt the site, inspected release ZIPs, and hit the live deployment.

## Findings and resolutions

| # | Severity | Finding | Resolution |
|---|---|---|---|
| 1 | CRITICAL | Doubled-base canonical + og:url on every page (`/product-academy/product-academy/…`) because `site` const already included the base while `Astro.url.pathname` also includes it | `Base.astro` now builds `canonical = new URL(Astro.url.pathname, "https://lucumax.github.io").href`; verified in rendered output (single `/product-academy/`) |
| 2 | MAJOR | All internal navigation root-relative and not base-prefixed — storefront nav dead-ended on the subpath | `Base.astro` nav, brand, footer, `ContinueLearning`, and every `/skills/`, workflow, install, 404, and homepage skills link now use `b(path) = Astro.base + path`; verified in rendered output |
| 3 | MAJOR | Workflow pages half-empty (CRLF broke `^## Entry` regex) and meta descriptions carried raw markdown `**…**` | `parseSkillWorkflows` normalizes CRLF and strips `**`; `skillWorkflows.json` now has non-empty entry/final sections; rendered pages verified |
| 4 | MAJOR | Count math inconsistent ("10 hardened + 5 added" = 15; INDEX said 15) | README and INDEX now state 14 active skills explicitly (9 hardened + 5 new; deprecated stub separated) |
| 5 | MAJOR | SEO test suite encoded the bugs (asserted broken nav href; never checked canonical value or workflow content) | Tests updated to assert single-base canonical construction, `Astro.base` nav helper, and non-empty workflow entry/final sections |
| 6 | MAJOR | The three demos were linked nowhere | README "Try it yourself" section + `/skills/` landing demo links added |
| 7 | MINOR | Machine-generated kebab titles and mid-sentence description truncation on skill pages | `[id].astro` now title-cases names and ellipsizes descriptions; workflow titles also title-cased |
| 8 | MINOR | Homepage still curriculum-first | Skills hero is prominent above the fold (second section); retained Academy identity (curriculum is the site's broader purpose) |
| 9 | MINOR | Contrast of muted text below WCAG AA | Flagged; `--ink-3` on near-black is ~3.7:1. Accepted as a pre-existing style-system trade-off for this sprint; revisit in the next cycle |
| 10 | MINOR | "(verified)" install claims outran the matrix (remote main still lists 16 pre-merge) | `INSTALLATION_MATRIX.md` now states remote pre-merge state and a re-test-after-merge note |
| 11 | MINOR | Matrix "known limitations" contradicted observed CLI behavior | Corrected: the CLI lists 14 on the hardened tree (template renamed; deprecated stub excluded) |
| 12 | MINOR | `skills/INDEX.md` omitted the native install route | `npx skills add Lucumax/product-academy` added as the first install row |
| 13 | MINOR | Cosmetic count drift (README "84 tests" vs 93; runbook "384 pages" vs 390) | Fixed in this commit pass |

## Residual (documented, not silently dropped)

- Pre-existing root-relative internal links in older curriculum content pages (outside the
  `/skills/` storefront) are not all converted this sprint; the shared primary navigation is
  base-correct. A site-wide link sweep is a follow-up item.
- The homepage intentionally retains the Academy curriculum hero above the skills section.
- Independent behavioral evaluation of the skills remains an open requirement (from the
  hardening sprint); the discoverability sprint does not fabricate evaluation evidence.
