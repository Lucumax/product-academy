# External Comparative Evaluation — Analysis Plan (precommitted)

This plan is written **before any results exist** to prevent post-hoc rationalization. Do not
change the statistics here after seeing the data; deviations must be documented in the
results file.

## Design

- 16 scenarios (`scenarios/X01–X16`), four conditions:
  - **A — Model alone:** the model receives only the scenario and a one-line instruction.
  - **B — Strong one-off prompt:** the model receives the scenario plus the general PM prompt
    in `baseline-prompts/B-strong-prompt.md`. No Product Academy material.
  - **C — Product Academy skill:** the model receives the scenario plus the relevant Product
    Academy `SKILL.md` and its `references/` (and the shared contract where the skill cites it).
  - **D — Competitor method:** a relevant competing public skill or framework, where licensing
    and practical access permit. If no fair competitor condition can be built, **D is marked
    unavailable** for that scenario rather than approximated with a strawman.
- Outputs are anonymized and labeled only Output A–C. The mapping of condition → output label
  is randomized per scenario (`randomization-schema.json`, generated reproducibly by
  `scripts/generate_eval_schema.py`, seeded) and kept secret until scoring completes. Round
  one runs conditions A, B, C (D = UNAVAILABLE, see `CONDITION_D_AVAILABILITY.md`); the
  schema and form expose three output labels, so no empty reviewer slot exists.
- Reviewer target: 5–10 experienced PMs (mix: Senior PM, Principal/GPM, Director/VP, founder,
  AI PM). No reviewer is claimed recruited until they agree.

## Hypotheses (registered)

1. H1: Condition C (skill) scores higher than B (strong prompt) on decision usefulness,
   evidence handling, and actionability.
2. H2: Condition C is not penalized on excessive ceremony relative to A and B.
3. H3: Condition C is picked as "would use" more often than A and B.
4. H4: The skill's edge is concentrated in contradictory-evidence and AI/launch scenarios,
   not in reversible-decision scenarios.

## Analysis to run (in order)

1. **Median and mean score by condition**, overall and per dimension.
2. **Pairwise preference:** count of times each condition's output was chosen for "would use"
   and "would trust least," per scenario and overall.
3. **Failure count:** number of outputs scoring ≤ 2 on any dimension, by condition.
4. **Ceremony penalty:** compare "excessive ceremony" scores to "decision usefulness" scores
   within condition C; report the direction and size, and any scenario where ceremony was
   penalized while usefulness was rated high.
5. **Confidence-calibration assessment:** flag outputs that claim high confidence while
   scoring low on evidence handling or correctness (overclaiming); and outputs that hedge so
   much they lose actionability (underclaiming).
6. **Performance by scenario type:** group scenarios as (a) contradictory-evidence,
   (b) reversible/low-stakes, (c) irreversible/high-stakes, (d) AI/launch, (e) early-stage /
   sparse evidence; compare condition means within each group.
7. **Disagreement among reviewers:** where two reviewers give the same output scores 2+
   apart, list it and look for a pattern (e.g., role-based disagreement).
8. **Qualitative failure themes:** code the free-text "material error or omission" responses
   into themes and report the top themes per condition.

## Significance discipline

- Sample is expected to be small (≤ 10 reviewers). **No claim of statistical significance is
  made.** Report medians, means, and counts descriptively.
- If a between-condition difference is large, call it "suggestive, not proven."
- Report the achieved sample size and reviewer mix explicitly in the results.

## Reversal conditions (precommitted)

If any of the following is true of the results, act accordingly and say so:

1. **C does not outperform B** on the primary dimensions (decision usefulness, evidence
   handling, actionability) or on "would use" preference → **do not claim the pack improves
   performance.** Re-position the pack as a coverage/consistency product until evidence
   exists, or run a redesigned study.
2. **Value is concentrated in only 3–4 skills** (the rest of the pack scores at or below B) →
   narrow the public positioning to those skills and stop advertising the full 14-skill claim.
3. **Reviewers consistently penalize ceremony** in condition C → strengthen routing (route
   fast-mode by default) and make fast mode the documented default; reduce the ceremony
   burden of the chain.
4. **Artifact quality is weak** across the pack (low scores on artifact quality and
   willingness-to-reuse) → prioritize templates and drafting artifacts over any new skills.
5. **Competitor skills perform equally well with less friction** (condition D matches or
   beats C on usefulness while scoring better on ceremony) → investigate consolidation or
   feature-level integration, and do not claim differentiation against them.

## Reporting format

Complete `RESULTS_TEMPLATE.md` with the analysis above, the honesty statement, and the
reversal-check table.
