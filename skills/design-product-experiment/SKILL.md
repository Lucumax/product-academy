---
name: design-product-experiment
description: >-
  Produces an experiment specification for a product change: the primary hypothesis, the
  metric, the pre-committed interpretation rule, and the stop rules — all defined BEFORE the
  results exist. Invoke when a change is proposed and "we'll see if it works" is the plan,
  when an experiment is being read out and nobody agreed on what a win looks like, or when a
  team wants to test an assumption without statistical ceremony. Pairs with
  conduct-causal-confidence-review to keep post-experiment credit honest.
type: assist
version: 0.1.0
best_for:
  - "A change is proposed and 'we'll see if it works' is the plan"
  - "An experiment is about to run and nobody has agreed what a win or stop looks like"
  - "A corrective experiment is needed for a decaying product-health dimension"
  - "An assumption from a problem frame or thesis needs a cheap test"
  - "AI feature evaluation: pre-commit the interpretation and rollback rule before results"
doctrine:
  - "PRN-0003 (cost of delay exceeds cost of imperfection)"
  - "PRN-0007 (reversible by design)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "CON-0007 (experimentation vs judgment)"
  - "09_tools/EXPERIMENT_DESIGN_TEMPLATE.md"
  - "09_tools/METRICS_TREE_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Most experiments fail before they run: the team disagrees on the metric, the "win" threshold
is invented after the results arrive, and the stop rule does not exist. This skill produces
the **experiment specification** — the primary hypothesis, the primary metric, the
pre-committed interpretation rule, and the stop rules — written before the data exists, so
the readout is a decision, not a negotiation.

The output is a one-page spec that can be read by an engineer to implement the test, by a
reviewer to check it, and by the causal-confidence review afterwards to grade whether the
outcome was caused by the change.

## Use when

- A change is proposed and "we'll see if it works" is the plan.
- An experiment is about to run and nobody has agreed what a win or a stop looks like.
- A decaying product-health dimension needs a corrective experiment.
- An assumption from a problem frame or thesis needs a cheap test.
- An AI feature needs a pre-committed interpretation and rollback rule before results.

## Do not use when

- The decision is about strategy or architecture, not a testable behavior change — judgment,
  not experiment (CON-0007); run `make-go-no-go-call` instead.
- The user wants statistical machinery (power analysis, Bayesian modeling) — this is a
  judgment scaffold over whatever statistics exist; it does not compute them.
- The user wants a full experiment write-up with analysis — the spec is the before; analysis
  is the after, handled with `conduct-causal-confidence-review`.
- A reversible micro-change where the experiment ceremony exceeds the change's value.

## Inputs

Required inputs:

- The change being tested, one sentence.
- The assumption it tests (from a problem frame, thesis, or health dimension).
- The primary metric that would move if the assumption holds, and the direction of the expected move.

Optional inputs:

- The baseline value of the primary metric.
- The population/segment the experiment covers.
- The known alternatives to the change and any competing hypotheses.

## Missing-data behavior

- No baseline → the spec names the baseline collection as a precondition; an experiment
  without a baseline cannot be interpreted (a causal review will refuse CAUSAL without it).
- No pre-committed threshold → the spec is incomplete; "we'll know when we see it" is the
  failure mode this skill exists to fix.
- Primary metric unknown → the spec stops and asks the team to pick the metric that best
  represents the assumption; the output names the candidates.

## Context classification

- **TYPE-1 / high stakes** (a change that is expensive or hard to reverse, or an AI feature
  facing users): Full mode with explicit rollback triggers and, for AI, a cross-reference to
  the evaluation contract.
- **TYPE-2 / low stakes** (a reversible change behind a flag or a cheap A/B): Fast mode —
  hypothesis, metric, threshold, stop rule, done.
- **Corrective experiment** (a decaying health dimension): Full mode — the metric must tie to
  the decaying dimension so the readout feeds the health verdict.

## Fast mode

Run for reversible, ordinary experiments. Four questions:

1. What assumption does this test, in one sentence?
2. What is the primary metric, and which direction proves the assumption?
3. What pre-committed threshold turns the result into a decision (keep / iterate / stop)?
4. What is the stop rule — how long, what sample, and when do you call it?

Output: a four-line spec — assumption, metric, interpretation rule, stop rule. If the team
cannot name the metric or the threshold, the spec flags that the experiment is not ready.

## Full mode

Adds: the baseline and collection method; the segment and population; named competing
hypotheses; the pre-registered causal question ("did the change cause the outcome?" — the
handoff to the causal review); and for AI features, the rollback trigger and human-review
sampling (cross-referencing the evaluation contract).

## Method

One question at a time. "Unknown" answers are recorded as stated assumptions.

1. State the assumption being tested. It must be a checkable proposition, not a hope: "changing X moves metric M in direction D for segment S."
2. Choose the primary metric. Which metric would move if the assumption holds? Name it and the direction. The metric must represent the assumption, not a vanity proxy. If the team's candidate metric is a vanity metric, say so.
3. Establish the baseline. What is the current value, over what window, measured how? No baseline → the experiment cannot be interpreted; baseline collection is a precondition.
4. Pre-commit the interpretation rule. What result counts as a win, what as a null, what as evidence of harm? The threshold is set BEFORE results; a threshold set after results is not a threshold.
5. Pre-commit the stop rules. When do you stop early (harm, implausible magnitude)? What is the minimum sample or time window? When do you call it null?
6. Name competing hypotheses. What else could explain the outcome (seasonality, another change shipping, regression to the mean)? These become the causal review's checks.
7. Define the rollback. How is this reversed, who triggers it, and what observable signal triggers it? For AI: cross-reference the evaluation contract's rollback section.
8. Write the spec. One page: assumption, metric, baseline, interpretation rule, stop rules, competing hypotheses, rollback.

## Evidence classification

Uses the shared taxonomy. The experiment's outcome is controlled-experiment evidence (E1) or
quasi-experiment (E2) once it runs; before it runs, the spec is a container for a
pre-registered causal claim. The baseline is behavioral/cohort evidence (E3/E4). The spec
explicitly names which of its own elements are assumptions (E15/E5) until the experiment
converts them.

## Output schema

```json
{
  "skill": "design-product-experiment",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "SPEC-READY | SPEC-INCOMPLETE | NOT-A-TESTABLE-BEHAVIOR",
  "spec": {
    "assumption": "...",
    "primary_metric": {"metric": "...", "direction": "up | down", "baseline": "..."},
    "interpretation_rule": {"win": "...", "null": "...", "harm": "..."},
    "stop_rules": {"early_stop": "...", "min_sample_or_window": "...", "null_call": "..."},
    "competing_hypotheses": ["..."],
    "rollback": {"mechanism": "...", "trigger_signal": "...", "trigger_authority": "..."}
  },
  "confidence": "high | medium | low",
  "evidence_basis": ["E1", "E3", "E4"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `SPEC-READY` (assumption, primary metric, baseline, pre-committed
  interpretation rule, and stop rules all named) / `SPEC-INCOMPLETE` (one or more of the
  required elements missing; the output names exactly which) / `NOT-A-TESTABLE-BEHAVIOR` (the
  "experiment" is actually a strategy, architecture, or platform question that a behavior test
  cannot resolve — judgment, not experiment; CON-0007).
- **Pre-commitment rule:** the interpretation and stop rules are set before results exist. A
  threshold that appears only after the readout invalidates the experiment.
- **Confidence:** High when the metric, baseline, and thresholds are numeric and the team
  commits to them in writing; Medium when a threshold is a stated assumption; Low when the
  metric is contested or the baseline is missing.
- **Assumptions:** every "unknown," with effect.
- **What would change the verdict:** for SPEC-INCOMPLETE, the missing element; for
  NOT-A-TESTABLE-BEHAVIOR, evidence that the question is behavior-testable (a pilot where a
  random assignment exists).
- **Next action:** hand the spec to the engineering owner to implement, or to the causal
  review after the readout.

### Worked example

Assumption: "Removing the two-step confirmation from checkout increases completed orders
without increasing returns or support contacts." Primary metric: completed-orders rate,
direction up, baseline 3.1% over the last 8 weeks. Interpretation rule: win = +0.3pp or more
on completed orders AND returns ≤ +0.1pp AND support contacts ≤ +5%; null = within ±0.3pp;
harm = returns or support breach the thresholds. Stop rules: early stop at 2 weeks if harm
threshold breached; minimum 6 weeks or 20k sessions before calling null; call null at 6 weeks
if no signal. Competing hypotheses: the A/B tool itself changed latency; a seasonal checkout
shift. Rollback: feature flag, trigger = harm threshold, authority = PM on call. Verdict:
SPEC-READY. Handoff: after 6 weeks, `conduct-causal-confidence-review` grades whether the
change caused the outcome using the baseline and competing hypotheses as its checks.

## Failure modes

- **Threshold after results.** "It went up 0.4pp — that's a win!" when no threshold was set. Correction: the interpretation rule is pre-committed in the spec; a post-hoc threshold is a negotiation, not a result.
- **Vanity primary metric.** A metric that moves for reasons unrelated to the assumption. Correction: the metric must represent the assumption; if it cannot, the assumption is the problem.
- **No baseline.** Interpreting an experiment with no prior trend or control. Correction: baseline collection is a precondition; the causal review will refuse CAUSAL without it.
- **Stop-rule absence.** Running forever, or stopping at the first green day. Correction: pre-commit the minimum window and the early-stop conditions.
- **Strategy as experiment.** Testing a pricing-model change like a button color. Correction: NOT-A-TESTABLE-BEHAVIOR — a Type-1 question needs judgment, a premortem, and a decision, not an A/B.
- **Rollback amnesia.** A win ships permanently with no reversal path. Correction: the rollback section is part of the spec (PRN-0007).
- **Statistical theater.** Refusing to interpret a clear signal because "we need p < 0.05." Correction: significance is not importance; the spec's thresholds carry the decision.

## Reversal conditions

- The harm threshold fires → execute rollback immediately; the experiment is stopped.
- A competing hypothesis is confirmed (e.g. the change shipped alongside a tooling change) → the readout is null regardless of the metric; re-run cleanly.
- The segment proves heterogeneous → re-read by segment before generalizing.
- The metric's baseline shifts materially mid-experiment → the interpretation rule is re-baselined, not silently kept.

## Composition hooks

- **before:** `frame-product-problem` (the assumption being tested comes from the frame);
  `synthesize-customer-discovery` (the top open question becomes the assumption);
  `prioritize-product-opportunities` (the top item's highest-risk assumption);
  `assess-product-market-fit-health` (a decaying dimension's corrective experiment);
  `check-ai-evaluation-contract` (AI features: the contract's thresholds become the
  interpretation and rollback rules).
- **after:** `conduct-causal-confidence-review` (grades whether the change caused the outcome
  using the spec's baseline and competing hypotheses); `make-go-no-go-call` (the readout
  feeds the scale/iterate/stop decision).
- **workflow:** experiment-decision (step 2).

## Related Skills

- `conduct-causal-confidence-review` — the "after" half: grades whether the change caused the outcome.
- `assess-product-market-fit-health` — a decaying dimension names the corrective experiment.
- `check-ai-evaluation-contract` — AI features: contract thresholds are the interpretation and rollback rules.
- `frame-product-problem` — the assumption being tested comes from the frame.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
