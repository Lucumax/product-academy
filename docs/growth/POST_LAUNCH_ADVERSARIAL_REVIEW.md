# Post-Launch Adversarial Review

Status: **COMPLETE — 2026-08-02.** Performed by an independent subagent that was given the
branch, the changed files, the live site, the release, and the evaluation package, and asked
to verify everything itself (it re-ran tests, the build, installs, ZIP inspection, live HTTP,
and the GitHub API). It did not rely on the sprint summary.

Branch reviewed: `skills-launch-validation-v1` (not merged). Live commit: `9c84756`.
Release: `skills-v0.3.0`.

## Review scope (failure classes requested)

Fabricated/overstated claims; fake comparison fairness; weak baselines; leading reviewer
questions; scenarios leaking expected answers; unjustified SEO claims; broken install paths;
promotional launch messages; stars-before-value calls to action; privacy/consent; metrics
that cannot be collected; documentation without adoption value; import-script correctness;
metadata accuracy; metrics-baseline honesty; demo-vs-contract accuracy.

## Findings and resolutions

### MAJOR (1) — eval blinding protocol assumed 4 conditions, round one runs 3

- **Finding:** `CONDITION_D_AVAILABILITY.md` marks competitor condition D unavailable for
  round one (A, B, C only), but the randomization schema, reviewer form, and README exposed
  four output labels (A–D). With D unavailable, the label assigned to D would have no output,
  breaking the form and leaking that a fourth method was withheld. The protocol could not be
  executed as documented.
- **Fix:** regenerated `randomization-schema.json` for **three output labels (A/B/C)** with a
  reproducible generator (`scripts/generate_eval_schema.py`, seeded, deterministic). Updated
  `reviewer-form.md` and `reviewer-rubric.md` to three columns/outputs, `README.md` to make
  round-one three-condition explicit and executable, and `RESULTS_TEMPLATE.md` / `ANALYSIS_PLAN.md`
  to record D as N/A. No empty reviewer slots can now occur.
- **Status:** RESOLVED.

### MINOR (7)

1. **LinkedIn post asserted generic-AI behavior as fact.** The demo labels its baseline output
   as an illustrative *shape*, but the public post stated it as established behavior. Added
   "in my tests" + "(Illustrative shape; the demo notes its limits honestly)" to
   `channel-1-linkedin.md`. RESOLVED.
2. **"Seeded" randomization was not reproducible** (hardcoded table, no generator). Added
   `scripts/generate_eval_schema.py` that reproduces the schema exactly; schema records its
   generator. RESOLVED.
3. **Blinding weaker than claimed** (condition A outputs are short, condition C outputs are
   long/structured; reviewers can guess by format). Added an explicit "Blinding caveat"
   section to `README.md` and corrected the "The blinding is real" claim. RESOLVED (stated
   limitation, not a design change).
4. **Deprecated `run-source-tier-check` stub installable by name.** Documented in
   `INSTALLATION_MATRIX.md` Known Limitations (the advertised paths surface 14; only the
   explicit `--skill run-source-tier-check` path reaches it). RESOLVED (documentation).
5. **Stale "remote main shows 16 skills until merged" claim.** The matrix predated the merge;
   remote `main` at `9c84756` lists 14. Corrected both matrix rows and the Known Limitations
   section, and upgraded the "install all skills" row from PARTIALLY_VERIFIED to VERIFIED
   (executed). RESOLVED.
6. **"Open discussions: 0" semantically false** (discussions are disabled; GraphQL returns 0
   for a disabled feature). `scripts/snapshot_metrics.py` now records
   `discussions_enabled` and sets `open_discussions: null` when disabled; baseline and
   snapshot note the distinction. RESOLVED.
7. **Baseline download counts mismatched the snapshot** (baseline said v0.3.0 = 1/0 while the
   snapshot said 2/1). Re-ran the snapshot, corrected `BASELINE_AFTER_V0.3.0.md` to match the
   snapshot at measurement date, and added an explicit volatility warning (download counts
   move on every download and GitHub caching is delayed). RESOLVED.

### INFO (2)

- Description char count nit: documented 155, actual 154. Corrected.
- `README.md`/`CONTRIBUTING.md` hardcoded the gate count (663) while the validator reports a
  dynamic count (now 668). Changed to "660+, count grows with content" so it cannot drift.

### Post-review validation finding (discovered during final validations, resolved)

- **`scripts/check_links.py` reports 268 "broken links" in a working checkout** while
  `validate_academy.py` Gate 7 (the authoritative gate, which excludes `node_modules` and
  `webapp`) passes 668/668 and a clean `main` worktree reports **0 broken**. The 268 are all
  pre-existing artifacts of the import pipeline (`webapp/src/content/` copies whose
  repo-relative links resolve against the webapp tree) and `webapp/node_modules` READMEs —
  not regressions. The only *new* broken links this branch introduced were the demo files'
  `../../../skills/...` relative links, which render correctly in the repo but break on the
  published `/doc/docs/growth-demos-*/` web pages. Fixed by switching demo links to absolute
  site URLs (skills/workflow pages) and GitHub blob URLs (repo-only references); verified the
  rendered HTML and the live targets return 200. RESOLVED.

## Verified clean (no finding)

- **No fabricated traction** anywhere: repo verifiably at 0 stars/0 forks/0 watchers;
  recruitment and posting explicitly marked unsent; metadata matches the live API exactly.
- **No weak baseline:** `B-strong-prompt.md` is a genuinely strong senior-PM prompt (it even
  already contains "behavior beats stated intent" — a hard baseline, not a strawman).
- **No leading reviewer questions**; rubric explicitly invites "the special method is not
  better" outcomes.
- **No scenario leaks the expected answer** (all 16 X-scenarios are neutral; the internal
  S01–S12 fixtures with run records are not reused in the external set).
- **No unjustified SEO claims:** Search Console ownership/sitemap submission explicitly marked
  not-done everywhere.
- **Install paths verified working:** `--list` → 14; `--skill` → 1; full `--yes` → 14; both
  ZIPs verified on the live release.
- **No stars-before-value calls to action**; all four channel drafts lead with a problem/demo
  and refuse star-asks.
- **Privacy/consent adequate:** reviewer IDs not names, consent-first recruitment, no issue
  template asks for secrets, metrics only public GitHub data.
- **Import-script fix technically correct** (verified against all four workflow files and the
  built output); regression test added and passing (95 tests).
- **Metadata execution doc accurate** (description/homepage/topics match the API; social
  preview PNG is 1280×640, ~94 KB, identical bytes to the site OG image).
- **Demos 1–3 accurate against their skill contracts.**

## Verdict

No unresolved critical or major defects. The branch is not dishonest and not broken for
launch. The single major finding (eval blinding protocol) is fixed and the eval package is
now executable as documented. Nothing in the review requires holding the launch; the launch
plan itself already forbids claiming eval results until reviewers score forms.

| Severity | Count | Resolved |
|---|---|---|
| CRITICAL | 0 | — |
| MAJOR | 1 | 1 |
| MINOR | 7 | 7 |
| INFO | 2 | 2 |
