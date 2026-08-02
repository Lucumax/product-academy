# Independent Adversarial Review Record

Date: 2026-08-02.
Reviewer: independent adversarial subagent (second model), dispatched after implementation.
Scope reviewed (read-only): the audit, portfolio map, shared contract, all 15 SKILL.md files,
4 workflows, 12 eval fixtures + rubric + report, tests/validator, onboarding docs, plugin
manifest, packager.
Disposition returned: **ACCEPT_WITH_BOUNDED_FIXES** (content strong; defects concentrated in
governance, packaging, and evaluation layers).

This file records the reviewer's findings and the resolution of each. It is the Phase 9
record that `EVALUATION_REPORT.md` and `rubric.md` reference. The reviewer's full report was
not copied verbatim; the material findings and their resolutions are tracked below.

## Findings and resolutions

| # | Severity | Finding | Resolution |
|---|---|---|---|
| F1 | MAJOR | Claude Code `/plugin marketplace add` requires a `marketplace.json` manifest; only `plugin.json` existed | Added `.claude-plugin/marketplace.json` |
| F2 | MAJOR | ZIPs were not self-contained: full-mode steps and handoffs referenced Academy files (09_tools/, register.yaml, case catalog, evidence/final) not shipped | Full-mode lookups marked optional with inline fallback where the Academy repo is absent (scan-contradictions, causal-review, evidence-audit, ai-contract); INSTALL.md now states what is and is not in the ZIP |
| F3 | MAJOR | Core ZIP shipped docs (INDEX/PORTFOLIO_MAP/workflows) referencing the other 6 skills it did not contain | Core ZIP now ships INSTALL.md + a CORE_README.md listing the starter skills; no doc inside a ZIP references unshipped skills |
| F4 | MAJOR | Audit was a stale snapshot: scored only the 10 original skills, findings #3/#6 contradicted the new tree, baseline said "10 skills / 57 tests" | Audit updated: post-audit disposition header, corrected baseline (14 active + 1 deprecated, 80 tests), new-skill scores, findings marked RESOLVED |
| F5 | MAJOR | "Phase 9 independent review" was a phantom reference in the eval report and rubric | Review record committed to `skills/quality/ADVERSARIAL_REVIEW_2026-08-02.md`; eval report and rubric reference this file |
| F6 | MAJOR | Scoring circular and over-asserted; two fixture run-records used invented verdicts (S06 "CONTRACT-GAPPY-to-NO-CONTRACT boundary"; S03 ambiguous resolution) | Eval report reframed Correctness as self-run internal consistency (not independent validation); S06 and S03 fixtures corrected to the skills' real verdict sets |
| F7 | MAJOR | Tests validated structure only: identical Fast/Full text, `"verdict": "TBD"`, unparsed JSON fences all passed; `scan-contradictions` shipped a literal placeholder verdict | Tests/validator hardened: JSON fence parsed and validated, Fast≠Full asserted, schema verdict enums cross-checked against the Verdict Contract, workflow step numbers validated, `assist-output` placeholder replaced with `ASSIST-ARTIFACT` |
| m1 | MINOR | Ghost workflow step "7.5" referenced by two skills; duplicate 4.5 rows in product-bet | Step 7.5 and 5.5 added to product-bet; 4.5 rows disambiguated; step-number validation added |
| m2 | MINOR | PORTFOLIO_MAP duplicate H1; maturity labels contradicted the legend | Duplicate H1 removed; legend redefined; new skills labeled `solid`, check-ai-evaluation-contract `stable` |
| m3 | MINOR | Slot overlap between frame-product-problem and pressure-test-product-thesis | Noted in product-bet (thesis reuses the frame's slots); kept both because the jobs differ |
| m4 | MINOR | Hard thresholds (10%, ≥50%, 2+ corroboration, severity≥4) presented as gates without qualifiers | Labeled as context-adjusted rules of thumb in the relevant verdict contracts |
| m5 | MAJOR/MINOR | Workflows over-chained; fast paths heavier than advertised; mode selection not enforced | make-go-no-go fast cut to 4 questions; explicit mode gates added to experiment-decision, launch-gate, product-health-review; product-bet fast variant pruned |
| m6 | MINOR | check-ai-evaluation-contract description made Academy modules "the reference standard" | Description reworded to the five-check standard with the modules cited, not required |
| m7 | MINOR | Two worked examples weak (make-go-no-go stopped at strategy gate; PMF marketplace mini-example hedged) | make-go-no-go example rewritten to walk the threshold ladder; PMF marketplace line corrected to a clear decision rule |
| m8 | MAJOR/MINOR | "See the INSTALL.md in each ZIP" was false; Claude.ai ZIP-upload and OpenCode claims unverified | INSTALL.md is now written inside both ZIPs; ZIP-upload/OpenCode wording qualified |
| m9 | MINOR/MAJOR | Undocumented gaps: build-vs-buy, metrics design, sunsetting, roadmap communication | Recorded in PORTFOLIO_MAP "Gaps remaining"; strategy-statement gap already documented; the four new gaps added |
| m10 | MINOR | frame-product-problem "Next action" was a routing menu, not an owner-able step | Rewritten to a single owner-able step per the shared contract |

## Unresolved (documented, not silently dropped)

- Independent *behavioral* evaluation (a third model running the 12 fixtures blind) is not
  performed this cycle; the eval report says so and lists it as a requirement for a genuine
  9/10.
- Build-vs-buy, metrics design, sunsetting, roadmap communication, strategy-statement
  production, and portfolio-grade prioritization remain documented gaps.
