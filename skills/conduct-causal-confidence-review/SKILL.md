---
name: conduct-causal-confidence-review
description: >-
  Verdict on the causal strength of a claim: whether an observed outcome was actually caused
  by the claimed decision or change, versus merely correlated, versus narrative. Use when
  someone is about to build a roadmap, a post-launch review, a case write-up, or an expansion
  bet on "X caused Y" and you need a reproducible causal verdict plus the evidence that would
  change it. Integrates with design-product-experiment (before) and audit-decision-evidence
  (evidence exists before causality is graded).
type: assess
version: 0.2.0
best_for:
  - "A post-launch review is about to credit a decision for an outcome and you want to test the causality"
  - "A claim 'our change caused the improvement' appears and needs grading"
  - "An experiment readout is about to be declared a win or a loss"
  - "A lesson is about to be extracted from a single success or failure and you want to check it generalizes"
  - "Two explanations of the same outcome are competing and you need to know which is more causal"
doctrine:
  - "PRN-0014 (same data, opposite conclusions; segment test)"
  - "PRN-0003 (turned out fine != right approach)"
  - "PRN-0007 (reversibility as the practical response to causal uncertainty)"
  - "07_cases/case_catalog.md (causal_confidence ratings)"
  - "08_contradictions/register.yaml (CON-0007 experimentation vs judgment)"
  - "evidence/final/CLAIMS_LEDGER.md"
license: CC BY 4.0
---

## Purpose

Every product organization routinely makes "X caused Y" claims: the onboarding redesign caused
the activation lift; the pricing change caused the churn drop; the AI feature caused the
retention gain. This skill grades those claims with a reproducible verdict — is it causal,
correlated, or a story told after the fact? — and names the specific evidence that would
change the verdict.

Invoke it whenever a causal claim is load-bearing: post-launch credit, experiment readouts,
case write-ups, lessons-learned, expansion or kill decisions. Do NOT invoke it to grade
whether evidence exists at all (`audit-decision-evidence`) or to certify a source's
credibility (sub-mode of the same). It assumes evidence is recorded and asks what it
establishes.

## Use when

- A post-launch review credits a decision for an outcome.
- Someone claims "our change caused the improvement" and the claim will shape the roadmap.
- An experiment readout is about to become a decision (SCALE / ITERATE / STOP).
- A lesson is about to be extracted from a single success or failure.
- Two explanations of the same outcome compete for funding.

## Do not use when

- The question is "is the evidence adequate" — use `audit-decision-evidence`.
- The causal claim is about a reversible, low-stakes change where the cost of the review
  exceeds the decision's value (a two-week experiment with no downstream commitment) — Fast
  mode or skip.
- The user wants a statistical analysis (p-values, power) — this skill is a judgment scaffold
  over whatever statistics exist; it does not compute them.
- The outcome is a one-off with no baseline, counterfactual, or segments available and nobody
  will ever collect them — the verdict will be `NARRATIVE` or `INSUFFICIENT-INFO`, and the
  honest answer is "do not build doctrine on this," not a forensic deep-dive.

## Inputs

Required inputs:

- The causal claim stated as a sentence: "D caused O" (what was done, what happened, why the two are connected).
- The baseline: O's trend before D, or a control group (if you do not know it, that is an assumption, not a blocker).

Optional inputs:

- The counterfactual (what would have happened otherwise).
- Alternative explanations already considered.
- Segment breakdowns of O.
- A catalog case ID if the claim matches one.

## Missing-data behavior

- No baseline → recorded as an assumption; the verdict cannot exceed `CORRELATED` on that
  claim regardless of how good the story is.
- No counterfactual → recorded as an assumption; `CAUSAL` is unreachable without a plausible
  counterfactual.
- No segment data → recorded as an assumption; the aggregate may hide the truth (PRN-0014
  Simpson's paradox) — a segment test is the cheapest upgrade.
- "Unknown" answers never silently default to "probably causal."

## Context classification

- **TYPE-2, low stakes** (an experiment on a reversible change): Fast mode is enough — the
  decision is "keep / iterate / stop," and a provisional causal read plus a guard against
  over-crediting is proportional.
- **TYPE-1, high stakes** (expansion, kill, platform bet): Full mode — baseline, counterfactual,
  segments, alternative explanations, and a naming of the discriminating test.
- **Post-launch / retrospective:** Full mode with a special guard against hindsight narrative
  (CASE-0003 pattern).

## Fast mode

Run for reversible, ordinary decisions. Four questions:

1. State "D caused O."
2. Was there a baseline or control showing O's prior trend, and did it break with D?
3. Name two other things that could explain O (market tailwind, seasonality, another change shipped at the same time, regression to the mean).
4. Does D precede O with a plausible mechanism?

Provisional verdict: `CAUSAL` only if baseline broke AND alternatives are materially ruled out
AND mechanism is plausible — otherwise `CORRELATED`. If there is no baseline at all, the
verdict is at most `CORRELATED` with Medium confidence. Next action: name the single
discriminating check that would firm it up (a segment split, a holdout, an intermediate
metric). No research ceremony.

## Full mode

Adds to fast mode:

1. Check the case catalog for a graded analog *(optional — works without the Academy repo)*:
   `07_cases/case_catalog.md` causal_confidence ratings, if the Academy repo is available.
   Without it, name the alternative explanations from the situation itself.
2. Establish the baseline rigorously: prior trend, control group, or reference class.
3. Name and examine at least two alternative explanations with evidence, not assertion.
4. Verify timing and mechanism; check reverse causation (O could be driving D).
5. Run the segment test (PRN-0014): does the effect hold across segments, or is it one subgroup?
6. Establish the counterfactual: if D had not happened, would O still have occurred?
7. Grade against the catalog scale: high / medium / low / correlation_only / retrospective_narrative.
8. Name the discriminating test or metric that would separate the causal explanation from its rivals.

## Method

One question at a time. "Unknown" answers are recorded as assumptions and the review continues.

1. State the claim precisely: "D caused O."
2. Was there a baseline? What was O's trend before D? A change that continues an existing trend is weak causal evidence; a change that breaks a flat or adverse trend is strong.
3. What else could explain O? Name at least two alternatives (market tailwind, seasonal effect, survivor bias, selection, regression to the mean, another change shipped at the same time).
4. Is the timing right? Does D precede O with a plausible mechanism, and is there any reason O could be driving D (reverse causation)?
5. Could the aggregate hide the truth? Run the segment test: does O hold across segments, or is the aggregate driven by one subgroup?
6. What is the counterfactual? If D had not happened, would O still have occurred? "Unknown" here is an assumption.
7. Grade the causal confidence: high / medium / low / correlation_only / retrospective_narrative.
8. Name the evidence that would change the verdict: the discriminating test that separates the causal explanation from its rivals.

## Evidence classification

Uses the shared taxonomy. Controlled experiments (E1) and quasi-experiments (E2) are the
strongest causal bases. Cohort/retention evidence (E4) and behavioral analytics (E3) can
support causal claims when combined with baseline and segments. Interviews (E5) and
practitioner doctrine (E12) cannot establish causation. A causal claim graded only on
interviews or anecdotes is `NARRATIVE` regardless of how many people said so.

## Output schema

```json
{
  "skill": "conduct-causal-confidence-review",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "CAUSAL | CORRELATED | NARRATIVE | INSUFFICIENT-INFO",
  "confidence": "high | medium | low",
  "evidence_basis": ["E1", "E4"],
  "checks": {"baseline": "passed | failed | unknown", "alternatives": "passed | failed | unknown",
             "timing_mechanism": "passed | failed | unknown", "segments": "passed | failed | unknown",
             "counterfactual": "passed | failed | unknown"},
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** one of
  - `CAUSAL` — mechanism + timing + counterfactual all hold; alternative explanations materially ruled out with evidence, not assertion; segment test does not contradict.
  - `CORRELATED` — D and O move together but mechanism or counterfactual is not established; treat as association, not causation.
  - `NARRATIVE` — a plausible story with no discriminating evidence; the retrospective explanation of an outcome (the Google Reader trust-damage pattern).
  - `INSUFFICIENT-INFO` — not enough recorded evidence to grade; do not build doctrine on it.
- **Confidence:** High/Medium/Low. High only when the verdict rests on multiple independent checks (baseline, counterfactual, segments, alternatives).
- **Evidence basis:** the taxonomy types used and the checks that passed/failed.
- **Assumptions:** every "unknown" (baseline, counterfactual, mechanism), recorded with effect.
- **What would change the verdict:** the specific evidence that flips it — e.g. "a control group with the same baseline and no D" or "a documented mechanism with a measured intermediate variable."
- **Next action:** run the named discriminating test, or explicitly decline to build doctrine on the claim.

### Worked example

Claim: "Our new onboarding flow caused the 15% activation lift last quarter." Baseline:
activation flat for four quarters, then broke upward with the launch (passes). Mechanism:
plausible but intermediate metric not measured (fails). Alternatives: a competitor's outage
drove users to us that same quarter, not examined (fails). Segments: lift concentrated in one
segment, another flat (fails). Counterfactual: unknown (assumption). Verdict: `CORRELATED`,
Confidence: Medium. Next action: segment-level activation excluding the outage window, or a
holdout cohort. Without one of these, treat the onboarding as associated, not causal — do not
extract a doctrine from it. Reversal: a segment-split result showing the effect in the
unaffected segment would upgrade toward CAUSAL.

## Failure modes

- **Survivorship bias:** crediting a decision because the outcome was good, ignoring decisions with the same logic that failed. Correction: run the counterfactual and the catalog's `what_does_not_transfer` lists.
- **Narrative hindsight (CASE-0003):** "Google killed Reader, therefore trust damage — pattern proven." Correction: a story about an outcome is not a mechanism; demand the discriminating evidence.
- **Tailwind attribution:** "the metric went up because of us" when the market rose regardless. Correction: always name the market tailwind as an alternative explanation.
- **Confusing 'turned out fine' with 'right' (PRN-0003):** a decision that produced a good outcome from a bad process. Correction: grade the decision-outcome link, not the outcome's quality.
- **Segment blindness (PRN-0014, Simpson's paradox):** the aggregate says "worked," the segments say "worked for power users, flat for everyone." Correction: the segment test is mandatory in full mode.
- **Experiment credit creep:** declaring a statistically significant but tiny effect a "win." Correction: significance is not importance; the next action must name the decision the effect justifies.

## Reversal conditions

- The discriminating test comes back against the causal explanation — downgrade the verdict and the doctrine built on it.
- A segment split reveals the aggregate effect was one subgroup — re-grade.
- A previously "unknown" baseline is reconstructed and contradicts the trend-break assumption.
- A post-launch metric contradicts the mechanism (e.g. the measured intermediate variable does not move).

## Composition hooks

- **before:** `design-product-experiment` (pre-register the causal claim, baseline, and
  discriminating test before data exists); `audit-decision-evidence` (confirm evidence is
  recorded before grading what it establishes).
- **after:** `make-go-no-go-call` (the causal verdict feeds the evidence gate for
  scale/iterate/stop); `run-case-based-premortem` (a weak causal basis becomes a failure
  narrative).
- **workflow:** experiment-decision (step 3).

## Related Skills

- `design-product-experiment` — the "before" half: define the causal question and the
  discriminating test before the data exists.
- `audit-decision-evidence` — the evidence-adequacy half: confirm the evidence exists before grading what it establishes.
- `scan-contradictions-assumptions` — surfaces the assumptions (baseline, counterfactual, mechanism) that this review then grades.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
