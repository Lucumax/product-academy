---
name: conduct-causal-confidence-review
description: >-
  Verdict on the causal strength of a claim or decision: whether an observed outcome was actually
  caused by the claimed decision, versus merely correlated, versus narrative. Use this when someone
  is about to build a doctrine, a roadmap, or a career on "X caused Y" and you need a reproducible
  causal verdict plus the evidence that would change it.
type: assess
version: 0.1.0
best_for:
  - "A post-launch review is about to credit a decision for an outcome and you want to test the causality"
  - "A claim 'our change caused the improvement' appears and you need it graded"
  - "A case is being added to the catalog and needs its causal_confidence rating"
  - "A lesson is about to be extracted from a single success or failure and you want to check it generalizes"
  - "Two explanations of the same outcome are competing and you need to know which is more causal"
doctrine:
  - "07_cases/case_catalog.md"
  - "PRN-0014"
  - "PRN-0003"
  - "PRN-0007"
  - "08_contradictions/register.yaml"
  - "evidence/final/CLAIMS_LEDGER.md"
license: CC BY 4.0
---

## Purpose

The Academy rates every case on `causal_confidence` and every claim on whether its evidence establishes causation or just association. This skill turns that discipline into a decision: given a claim of the form "decision D caused outcome O," it returns a causal verdict, a confidence, and the specific evidence that would change the verdict.

Invoke it whenever a causal claim is load-bearing — in a post-mortem, a lessons-learned session, a case write-up, or a funding decision. Do NOT invoke it to grade whether evidence exists at all (`audit-decision-evidence`) or to certify a source (`run-source-tier-check`). It assumes the evidence is recorded and asks what it establishes.

## Input

Bring the causal claim: what was done, what happened, and why you think the two are connected. If the claim matches a case in `07_cases/case_catalog.md`, bring the case ID and its existing `causal_confidence` rating. Bring whatever you know about: baseline (trend before the change), counterfactual (what would have happened otherwise), and alternative explanations already considered. If you do not know the baseline, that is an assumption, not a gap that blocks the review.

## Method

One question at a time. "Unknown" answers are recorded as assumptions and the review continues.

1. State the claim precisely: "D caused O." If the claim is "our feature increased engagement," write it as a causal sentence so it can be tested.
2. Does the claim match a catalog case? If yes, read its `causal_confidence` rating and its `what_does_not_transfer` section — the Academy has already graded this territory.
3. Was there a baseline? What was O's trend before D? A change that continues an existing trend is weak causal evidence; a change that breaks a flat or adverse trend is strong.
4. What else could explain O? Name at least two alternative explanations (market tailwind, seasonal effect, survivor bias, selection, regression to the mean, another change shipped at the same time).
5. Is the timing right? Does D precede O with a plausible mechanism, and is there any reason O could be driving D instead (reverse causation)?
6. Could the aggregate hide the truth? Check segments (PRN-0014, Simpson's paradox): does O hold across segments, or is the aggregate effect driven by one subgroup while others show nothing or the reverse?
7. What is the counterfactual? If D had not happened, would O still have occurred? This is the crux question; "unknown" here is an assumption.
8. Grade the causal confidence against the case-catalog scale: high / medium / low / correlation_only / retrospective_narrative.
9. Name the evidence that would change the verdict: the discriminating test or metric that would separate the causal explanation from its rivals.

## Verdict Contract

- **Verdict:** one of `CAUSAL` / `CORRELATED` / `NARRATIVE` / `INSUFFICIENT-INFO`.
  - `CAUSAL` — mechanism + timing + counterfactual all hold; alternative explanations materially ruled out.
  - `CORRELATED` — D and O move together but mechanism or counterfactual is not established; treat as association, not causation.
  - `NARRATIVE` — a plausible story with no discriminating evidence; the retrospective explanation of an outcome (the Google Reader trust-damage pattern).
  - `INSUFFICIENT-INFO` — not enough recorded evidence to grade; do not build doctrine on it.
- **Confidence:** High/Medium/Low with reasoning. High only when the verdict rests on multiple independent checks (catalog rating, baseline, counterfactual, segment test).
- **Citations:** the case ID and its rating (e.g. `CASE-0004` — medium), the ledger claim (e.g. `CLM-0022`), and the principle (PRN-0014). Quote at most one short line with a source location.
- **Stated assumptions:** every "unknown" (baseline, counterfactual, mechanism) recorded explicitly.
- **What would change the verdict:** the specific evidence that flips it — e.g. "a control group with the same baseline and no D, or a documented mechanism with measured intermediate variable."

### Worked example

Claim: "Our new onboarding flow caused the 15% activation lift last quarter." Check: baseline — activation was flat for four quarters before, then broke upward with the launch (passes); mechanism — plausible but intermediate metric not measured (fails); alternatives — a competing product's outage drove users to us that same quarter, not examined (fails); segments — the lift is concentrated in one segment, another shows no change (fails). Catalog match: none exact, closest analog CASE-0004 (`medium`, tailwind confound). Verdict: `CORRELATED`, Confidence: Medium. What would change it: (a) segment-level activation for the unaffected segment showing lift after excluding the outage window, or (b) a measured intermediate variable (e.g. time-to-first-value decreasing with onboarding steps) establishing mechanism, or (c) an A/B holdout cohort. Without one of these, treat the onboarding as associated, not causal — do not extract a doctrine from it.

## Thresholds

A second reviewer must reproduce the verdict.

- `CAUSAL` — all four hold: (a) D precedes O with a plausible mechanism, (b) a baseline or control shows O's prior trend was flat or adverse and broke with D, (c) at least two named alternative explanations were examined and rejected with evidence, not assertion, (d) the causal relationship is not contradicted by the segment test.
- `CORRELATED` — (a) holds but one of (b), (c), (d) fails; or (a) holds but no baseline exists (recorded as assumption).
- `NARRATIVE` — no baseline, no mechanism, no counterfactual — only a story that connects D to O after the fact. Matches the catalog's `retrospective_narrative` rating (CASE-0015, CASE-0016, CASE-0017).
- `INSUFFICIENT-INFO` — D, O, or their timing cannot be established from the record.

Alignment with the catalog scale: `high` maps to `CAUSAL`; `medium` maps to `CORRELATED`; `low` maps to `CORRELATED` with Low confidence; `correlation_only` maps to `CORRELATED`; `retrospective_narrative` maps to `NARRATIVE`.

## Evidence & Doctrine

- `07_cases/case_catalog.md` — 19 cases with `causal_confidence` ratings: high (CASE-0001, 0005, 0007, 0011, 0018, 0019), medium (0002, 0004, 0006, 0008, 0010, 0012, 0013, 0014), low (CASE-0009), correlation_only (CASE-0003), retrospective_narrative (CASE-0015, 0016, 0017). Each case's `what_was_learned` and `what_does_not_transfer` encode where the causality does not generalize.
- `PRN-0014` — same data, opposite conclusions; the segment test and the "correlation as causation" failure mode are this principle operationalized.
- `PRN-0003` — "confusing 'the decision turned out fine' with 'speed was the right approach'" is a causal error this skill is built to catch; also sets the reversibility terms for the counterfactual.
- `PRN-0007` — reversibility design is the practical response to causal uncertainty.
- `08_contradictions/register.yaml` — CON-0007 (experimentation vs judgment): a `CAUSAL` verdict requires the kind of discriminating experiment the experimentation pole demands.
- `evidence/final/CLAIMS_LEDGER.md` — claim-level corroboration; uncorroborated claims are weak causal bases.

## Common Pitfalls

- **Survivorship bias:** crediting a decision because the outcome was good, ignoring the decisions that had the same logic and failed. Correction: run the counterfactual against the catalog's `what_does_not_transfer` lists, which exist to name where the causality breaks.
- **Narrative hindsight (CASE-0003):** "Google killed Reader, therefore trust damage — the pattern is proven." The catalog rates this `correlation_only`/`retrospective_narrative`. Correction: a story about an outcome is not a mechanism; demand the discriminating evidence.
- **Tailwind attribution (CASE-0004):** the Microsoft transformation is `medium`, not high, partly because the cloud market was rising regardless of who was CEO. Correction: always name the market tailwind as alternative explanation (b).
- **Confusing 'turned out fine' with 'right' (PRN-0003):** a decision that produced a good outcome from a bad process. Correction: grade the causality of the decision-outcome link, not the outcome's quality.
- **Segment blindness (PRN-0014, Simpson's paradox):** the aggregate says "worked," the segments say "worked for power users, flat for everyone." Correction: the segment test is mandatory in step 6, not optional.

## Related Skills

- `audit-decision-evidence` — the "before" half: confirm the evidence exists before grading what it establishes.
- `run-source-tier-check` — a causal claim built on a tier-inflated source is suspect on entry.
- `scan-contradictions-assumptions` — surfaces the assumptions (baseline, counterfactual, mechanism) that this review then grades.
