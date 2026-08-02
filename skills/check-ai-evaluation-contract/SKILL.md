---
name: check-ai-evaluation-contract
description: >-
  Verdict on whether an AI product's evaluation contract is complete — whether launch
  thresholds, rollback triggers, a monitoring plan, a failure taxonomy, and a defined
  human-baseline comparison exist and are defined BEFORE building. Invoke before AI build
  starts, at the launch decision, before a model swap, or after an incident that revealed the
  product had no agreed definition of good and bad. Uses a five-check evaluation-contract
  standard (failure taxonomy, launch thresholds, rollback triggers, monitoring plan, human
  baseline) informed by the Academy's AI product-management modules.
type: assess
version: 0.2.0
best_for:
  - "Pre-build gate: the AI feature has no written definition of success or failure"
  - "Launch decision: 'are we ready to expose this to users?'"
  - "Model swap or provider update: will the existing contract still hold?"
  - "Post-incident review: 'the system degraded and nobody could define how badly'"
  - "Portfolio audit: comparing completeness of evaluation contracts across AI products"
doctrine:
  - "PRN-0011 (leading indicators beat lagging)"
  - "05_ai_product_management/EVALUATION_CONTRACTS.md"
  - "05_ai_product_management/FAILURE_MODES.md"
  - "05_ai_product_management/MODEL_VS_SYSTEM.md"
  - "05_ai_product_management/GOVERNANCE.md"
  - "CON-0011 (human-in-the-loop vs automation)"
  - "CASE-0018 (Boeing), CASE-0019 (Theranos)"
  - "09_tools/EVALUATION_CONTRACT_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

This skill produces a verdict on the single most important artifact in AI product
management: the evaluation contract. An evaluation contract defines what "good" and "bad"
mean for an AI system before a line of code is written — the conditions under which it
launches, the conditions under which it is rolled back, and how it is monitored in
production. Without one, an AI product is flying blind: probabilistic failure is silent,
feedback arrives slowly and noisily, and degradation is invisible without baselines.

Invoke it when a decision depends on whether an AI product has a complete, usable contract:
before build starts, at the launch gate, before a model swap, after an incident, or during an
audit of multiple AI products. It is a completeness and quality check, not a re-derivation of
the contract itself.

## Use when

- An AI feature has no written definition of success or failure (pre-build gate).
- A launch decision: "are we ready to expose this to users?"
- A model swap or provider update: will the existing contract still hold?
- A post-incident review: the system degraded and nobody could define how badly.
- A portfolio audit: comparing evaluation-contract completeness across AI products.

## Do not use when

- The user wants to write the contract — the drafting aids are the Academy's
  `09_tools/EVALUATION_CONTRACT_TEMPLATE.md` and `05_ai_product_management/EVALUATION_CONTRACTS.md`
  (in the Academy repo) or any equivalent drafting scaffold you have.
- The feature is not AI (deterministic failure — exceptions, crashes — is the norm); the
  contract exists because AI fails silently.
- After launch, as a substitute for the actual monitoring the contract demands.
- The AI feature is reversible and low-stakes with bounded downside (a non-critical
  suggestion surface behind a flag) — use Fast mode; a full five-check audit is disproportionate.

## Inputs

Required inputs:

- The evaluation contract document itself, or answers to the five core checks if no document exists.
- The workflow the system performs and who consumes its output.
- The current stage: pre-build, at launch, or in production.

Optional inputs:

- Incident history that has already revealed contract gaps.
- The decision's reversibility class.

## Missing-data behavior

- Arriving with no contract and only a demo is not an empty-handed arrival — it is the answer
  to the first question and the skill returns `NO-CONTRACT`.
- A contract covering only model accuracy → `CONTRACT-GAPPY`, not `NO-CONTRACT` — that
  distinction matters for remediation.
- "Unknown" on a core check → the verdict cannot be `CONTRACT-COMPLETE`; drop to the
  highest-confidence verdict consistent with the knowns.

## Context classification

- **TYPE-1, high stakes** (money, safety, irreversible user harm, large surface): Full mode —
  all five checks with numbers and named owners, silent-failure rollback required.
- **TYPE-2, low stakes** (reversible AI feature, flag-gated, bounded downside): Fast mode —
  a readiness pre-check is proportional.
- **Pre-build vs at-launch vs in-production:** pre-build missing a contract is the worst
  case; in-production, a GAPPY verdict names what must be retrofitted.

## Fast mode

Run for reversible AI features with bounded downside. Three questions:

1. Does a written contract exist, created before building, defining success and failure?
2. What is the failure taxonomy — the ways this system could be wrong, severity-weighted?
3. Are there rollback triggers with specific signals and timeframes, including silent-failure
   signals (not just system errors)?

Provisional verdict: `CONTRACT-COMPLETE` (all three present with numbers and owners) /
`CONTRACT-GAPPY` (a contract exists but one of the three is missing or vague) / `NO-CONTRACT`
(nothing written). Confidence capped at Medium. Next action: fill the single largest gap.
If the feature is high-stakes, escalate to Full mode.

## Full mode

Adds to fast mode: numeric launch thresholds on an explicitly defined evaluation set;
the monitoring plan with cadence, named ownership, and distribution-shift detection
(monitor the system, not just the model — MODEL_VS_SYSTEM); the human-baseline comparison
with a re-run cadence; and a named contract owner with a review date. Includes the
silent-failure rollback requirement.

## Method

Work through these questions in order. Ask the user directly. "Unknown" answers are recorded
as stated assumptions and the process continues.

1. Does a written contract exist, created before building? Ask: "Is there a document that defines success and failure for this system, and was it written before significant build investment?" If no, return `NO-CONTRACT` — record what the team is relying on instead (demos, vibe, "we'll iterate").
2. Failure taxonomy. Ask: "List every way this system could be wrong, with a severity weight for each." Check for severity weighting (not just error counts) and the domain-critical failure modes: hallucination/fabrication, omission, distribution shift, confidence miscalibration, bias, prompt injection, cascading failure. Test it: "Can you imagine a failure that does not fit any category? If yes, the category is missing."
3. Launch thresholds. Ask: "What must be true, in numbers, before this system is exposed to users?" A defensible answer is numeric and framed against a defined set — the set, the metric, and the bar are all named. Vague thresholds fail this check.
4. Rollback triggers. Ask: "What specific signal, measured over what window, takes this system offline or reverts to fallback?" Check specifically for silent-failure rollback signals: human-review sampling error rate, user opt-out/override rate, satisfaction drop, downstream business-metric degradation — not just system errors. An AI system that only rolls back on 5xx errors cannot detect its own most dangerous failure mode.
5. Monitoring plan. Ask: "How will you know, within what timeframe, that the system is degrading?" Check for cadenced monitoring, distribution-shift detection, golden-example regression, and named ownership of each cadence. Monitor the system, not just the model. Ask: "Who is paged when a weekly human-review sample finds the error rate above threshold, and who investigates?"
6. Human-baseline comparison. Ask: "What is the human performance level this system is being compared against, and how will you know when AI has matched or exceeded it?" A contract without a defined human baseline cannot set defensible launch thresholds, and cannot tell you when the baseline itself has shifted.
7. Ownership and cadence. Ask: "Who owns this contract, when is it reviewed, and what triggers a re-review?" A contract with no owner and no review date is a document, not a contract.

## Evidence classification

Uses the shared taxonomy. A contract is behavioral/operational evidence (E3-grade: defined
monitoring metrics and rollback triggers) plus product design evidence (E6-equivalent: the
defined workflow). Absence of a contract is E15 (unsupported reliance on demos). The
reference standard (the Academy's AI modules) is practitioner doctrine (E12) — strong for
framing, never a substitute for the product's own measured signals.

## Output schema

```json
{
  "skill": "check-ai-evaluation-contract",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "CONTRACT-COMPLETE | CONTRACT-GAPPY | NO-CONTRACT",
  "checks": {
    "failure_taxonomy": "pass | fail | missing",
    "launch_thresholds": "pass | fail | missing",
    "rollback_triggers": "pass | fail | missing",
    "monitoring_plan": "pass | fail | missing",
    "human_baseline": "pass | fail | missing",
    "ownership_cadence": "pass | fail | missing"
  },
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E12"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** one of
  - `CONTRACT-COMPLETE` — a written contract exists, covers all five core checks with specific numbers and named owners, and includes silent-failure detection.
  - `CONTRACT-GAPPY` — a contract exists but one or more core checks are missing, vague, or unowned. Common gaps: no rollback threshold, no silent-failure signals, no human baseline, unweighted failure taxonomy, thresholds as ranges rather than numbers.
  - `NO-CONTRACT` — no written contract exists before build, or the team is relying on presentation rather than a defined contract.
- **NO-CONTRACT:** no written contract AND no defined launch/rollback/monitoring thresholds anywhere (a deck or post-hoc rationale does not count). The team is deciding readiness by demo or schedule.
- **CONTRACT-GAPPY:** a written contract exists AND at least one of the five core checks is missing, vague, or unowned. A rollback section containing only system-error signals is a gap — silent failures require non-system-error signals.
- **CONTRACT-COMPLETE:** a written contract exists AND all of: severity-weighted failure taxonomy covering domain-critical modes including silent ones; numeric launch thresholds on an explicitly defined evaluation set; rollback triggers with specific metrics and timeframes including silent-failure signals; a monitoring plan with cadence and ownership including distribution-shift detection; a defined human-baseline comparison with a re-run cadence; a named owner and review date.
- **Confidence:** High when the contract is explicit and the user can produce the numbers;
  Medium when answers came partly from memory; Low when key checks were answered "unknown."
- **Assumptions:** every "unknown," with effect on the verdict.
- **What would change the verdict:** for `NO-CONTRACT`, a written contract covering the five
  checks; for `CONTRACT-GAPPY`, the specific missing check filled with numbers and an owner;
  for `CONTRACT-COMPLETE`, discovery that thresholds are numbers on paper but unenforced in
  production.
- **Next action:** for NO-CONTRACT, draft the contract before further build spend; for GAPPY,
  fill the named gap with numbers and an owner; for COMPLETE, schedule the first enforcement
  review.

### Worked example

A contract that names only "model accuracy 95% on our test set" fails at the failure-taxonomy
check — no severity weights — and returns `CONTRACT-GAPPY`, not `NO-CONTRACT`, because a
contract exists. A contract that names accuracy, a severity-weighted taxonomy, launch gates,
rollback triggers including override-rate, a quarterly human-baseline re-run, and a named
owner returns `CONTRACT-COMPLETE` even if a supporting detail (e.g. exact p99 latency target)
is a stated assumption. The line between GAPPY and COMPLETE is drawn by the five core checks,
not by the completeness of the appendices.

## Failure modes

- **The accuracy trap.** "95% accuracy" with no defined evaluation set, no severity weighting, and no measurement method is meaningless. Correction: accuracy must be defined against the failure taxonomy.
- **Rollback amnesia.** Launch thresholds set, rollback thresholds absent. Correction: define explicit rollback triggers with metrics, timeframes, and procedure, including the silent-failure signals.
- **System-error-only monitoring.** Monitoring 5xx rates while the system returns plausible wrong answers at 200 OK. Correction: add human-review sampling, override-rate, opt-out, and business-metric correlation.
- **Human review as a crutch.** "We'll have humans check everything" with no review budget measured. Correction: specify which outputs require review by severity/confidence/novelty, and measure review rate against budget.
- **Contract as document.** A complete contract never enforced, never re-run against production, owned by nobody. Correction: named owner, review cadence, and review trigger events.
- **No human baseline.** Thresholds set against internal guesses instead of a measured human level. Correction: define the human baseline and re-run it on a cadence.
- **Optimizing for the evaluation set.** The same 50 examples tested weekly produce apparent improvement while real-world performance degrades. Correction: rotate examples, add production-sourced examples, keep held-out sets.
- **Contract ceremony for low-risk features.** A full five-check audit for a flag-gated suggestion surface. Correction: Fast mode is the default for reversible, bounded-downside AI features.

## Reversal conditions

- A threshold is breached in production → execute the rollback trigger and re-review the contract.
- A model swap or provider change invalidates a contract assumption → re-run the skill.
- An incident reveals a failure mode absent from the taxonomy → the taxonomy is incomplete; re-run.
- A "paper-complete" contract is found unenforced → downgrade the verdict.

## Composition hooks

- **before:** `pressure-test-product-thesis` (an AI thesis's falsification test is executed
  through an evaluation contract); `frame-product-problem` (the workflow and success definition
  come from the problem frame).
- **after:** `assess-product-market-fit-health` (the contract's monitoring produces the
  leading indicators PMF health is judged on); `make-go-no-go-call` (GO for AI bets requires a
  monitored contract); `run-case-based-premortem` (contract gaps are top AI-launch failure
  scenarios); `conduct-causal-confidence-review` (grading whether the AI change caused the outcome).
- **workflow:** launch-gate (step 4), product-bet (AI bets, step 4.5).

## Related Skills

- `pressure-test-product-thesis` — the "before" half for AI bets: the thesis defines the bet; the contract defines the test that executes its falsification condition.
- `assess-product-market-fit-health` — the "after" half for launched AI products: the contract's monitoring produces the leading indicators PMF health is judged on.
- `make-go-no-go-call` — AI bets require a monitored contract before GO.
- `conduct-causal-confidence-review` — grades whether an AI change actually caused the measured outcome.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
