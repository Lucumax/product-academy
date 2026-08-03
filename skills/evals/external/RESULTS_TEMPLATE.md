# External Comparative Evaluation — Results Template

This template is completed **after** reviewers return forms and the blinding is broken. Do not
fill it in before results exist; the analysis plan is precommitted in `ANALYSIS_PLAN.md`.

## Administration

- Study dates: ___
- Number of reviewers who agreed: ___
- Number of reviewers who returned forms: ___
- Reviewer mix (roles): ___
- Scenarios actually scored: ___
- Blinding broken on: ___
- Any reviewer dropped (and why): ___

## Summary table (by condition)

Round one runs three conditions (D = UNAVAILABLE; record as N/A).

| Condition | Median score | Mean score | # scenarios | # reviewer-scores |
|---|---|---|---|---|
| A. Model alone | | | | |
| B. Strong one-off prompt | | | | |
| C. Product Academy skill | | | | |
| D. Competitor method | N/A (unavailable round one) | N/A | — | — |

## Per-scenario table

| Scenario | Condition order (after unblinding) | Mean score per condition | "Would use" winner | "Trust least" winner |
|---|---|---|---|---|
| X01 | | | | |
| … | | | | |

## Required analysis (each must be reported)

1. Median and mean score by condition (table above).
2. Pairwise preference: how often did reviewers pick each condition's output as "would use"?
   Report counts, not just percentages (small sample).
3. Failure count: number of outputs scored ≤ 2 on any dimension, by condition.
4. Ceremony penalty: correlation (if any) between the "excessive ceremony" score and the
   "decision usefulness" score, by condition.
5. Confidence-calibration assessment: do outputs that claim high confidence actually score
   higher on factual correctness? Do outputs overclaim relative to their evidence handling?
6. Performance by scenario type (contradictory-evidence scenarios vs reversible-decision
   scenarios vs AI/launch scenarios).
7. Disagreement among reviewers: note where reviewers split 2+ on the same output.
8. Qualitative failure themes: collect the free-text "material error or omission" answers by
   theme.

## Statistical honesty statement

State explicitly: with the sample sizes achieved (likely < 10 reviewers, ~16 scenarios), no
claim of statistical significance is made. Report medians and preference counts as
descriptive. If a difference looks large, call it "suggestive, not proven."

## Reversal checks (from ANALYSIS_PLAN.md)

For each reversal condition below, state whether it fired and the evidence:

- [ ] C did not outperform B → do not claim the pack improves performance.
- [ ] Value concentrated in 3–4 skills → narrow public positioning.
- [ ] Reviewers penalize ceremony → strengthen routing and fast mode.
- [ ] Artifact quality weak → prioritize templates over new skills.
- [ ] Competitor skills equal with less friction → investigate consolidation.

## Open items for next round

- Which scenarios were the least fair? Which conditions were weakest baselines?
- Which scenarios should be replaced, rewritten, or dropped?
