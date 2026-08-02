---
name: check-ai-evaluation-contract
description: >-
  Produces a verdict on whether an AI product's evaluation contract is complete
  — whether launch thresholds, rollback triggers, a monitoring plan, a failure
  taxonomy, and a defined human-baseline comparison exist and are defined
  BEFORE building. Invoke before AI build starts, at the launch decision, before
  a model swap, or after an incident that revealed the product had no agreed
  definition of good and bad. Uses 05_ai_product_management/EVALUATION_CONTRACTS.md
  and FAILURE_MODES.md as the reference standard.
type: assess
version: 0.1.0
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

This skill produces a verdict on the single most important artifact in AI product management: the evaluation contract. An evaluation contract defines what "good" and "bad" mean for an AI system before a line of code is written — the conditions under which it launches, the conditions under which it is rolled back, and how it is monitored in production (05_ai_product_management/EVALUATION_CONTRACTS.md, TL;DR). Without one, an AI product is flying blind: probabilistic failure is silent, feedback arrives slowly and noisily, and degradation is invisible without baselines.

Invoke this skill when a decision depends on whether an AI product has a complete, usable contract: before build starts, at the launch gate, before a model swap, after an incident, or during an audit of multiple AI products. It is a completeness and quality check, not a re-derivation of the contract itself.

Do NOT invoke this skill to write the contract — point to `09_tools/EVALUATION_CONTRACT_TEMPLATE.md` and `05_ai_product_management/EVALUATION_CONTRACTS.md` for drafting. Do NOT invoke it for non-AI features where deterministic failure (exceptions, crashes) is the norm; the contract exists because AI fails silently. Do NOT invoke it after launch as a substitute for the actual monitoring the contract demands.

## Input

What the user should bring:

- The evaluation contract document itself, or the answers to the five core checks if no document exists.
- The workflow the system performs and who consumes its output.
- The current stage: pre-build, at launch, or in production.
- Any incident history that has already revealed contract gaps.

If the user arrives with no contract and only a demo, that is not an empty-handed arrival — it is the answer to the first question and the skill returns `NO-CONTRACT`. If the user has a contract that covers only model accuracy and nothing else, the skill returns `CONTRACT-GAPPY`, not `NO-CONTRACT` — that distinction matters for remediation.

## Method

Work through these questions in order. Ask the user directly. If the user answers "unknown," record it as a stated assumption and continue — never silently assume.

1. **Does a written contract exist, created before building?** Ask: "Is there a document that defines success and failure for this system, and was it written before significant build investment?" If no, return `NO-CONTRACT` — record what the team is relying on instead (demos, vibe, "we'll iterate").
2. **Failure taxonomy.** Ask: "List every way this system could be wrong, with a severity weight for each." The taxonomy is the most important section (EVALUATION_CONTRACTS.md, Part 3 Step 3). Check for severity weighting (not just error counts) and for the domain-critical failure modes: hallucination/fabrication, omission, distribution shift, confidence miscalibration, bias, prompt injection, cascading failure (FAILURE_MODES.md). A taxonomy that covers only "accuracy" has missed the point. Test the taxonomy the way the module does: "Can you imagine a failure that does not fit any category? If yes, the category is missing." A strong taxonomy for a claims-summarization product names hallucination (severity 4-5, detection: citation verification), omission of a material clause (severity 4, detection: key-fact coverage), and distribution shift as users change input style (severity 2-4, detection: embedding drift). A taxonomy of "wrong answer / right answer" fails this step.
3. **Launch thresholds.** Ask: "What must be true, in numbers, before this system is exposed to users?" Check for mandatory gates: task success rate, severe-error rate, golden-example accuracy, latency, cost, bias/privacy audit, tested rollback (EVALUATION_CONTRACTS.md, Section 11). Vague thresholds — "good enough," "95%" with no evaluation set definition — fail this check. A defensible answer is numeric and framed against a defined set: "Task success rate >= 92% on a 500-example production-sourced set, severity 4-5 error rate <= 0.1%, all 20 golden examples pass, p95 latency <= 800ms." The set, the metric, and the bar are all named.
4. **Rollback triggers.** Ask: "What specific signal, measured over what window, takes this system offline or reverts to fallback?" This is the most commonly missing half of a contract. Check specifically for the silent-failure rollback signals: human-review sampling error rate, user opt-out/override rate, satisfaction drop, downstream business metric degradation — not just system errors (EVALUATION_CONTRACTS.md, Section 12, "SILENT FAILURE ROLLBACK"). An AI system that only rolls back on 5xx errors cannot detect its own most dangerous failure mode. A strong answer: "Roll back if severity 4-5 errors exceed 5 in an hour, OR if human-review sampling finds error rate > 3% over 48h, OR if the user override rate rises above 25% for three consecutive days." A rollback section that names only "monitor errors and latency" fails this step.
5. **Monitoring plan.** Ask: "How will you know, within what timeframe, that the system is degrading?" Check for cadenced monitoring (real-time / hourly-daily / weekly / monthly), distribution-shift detection, golden-example regression, and named ownership of each cadence (Section 13). The principle from MODEL_VS_SYSTEM.md applies: monitor the system, not just the model. Ask: "Who is paged when a weekly human-review sample finds the error rate above threshold, and who investigates?" A plan with cadences but no named owner is a plan on paper.
6. **Human-baseline comparison.** Ask: "What is the human performance level this system is being compared against, and how will you know when AI has matched or exceeded it?" A contract without a defined human baseline cannot set defensible launch thresholds, and cannot tell you when the baseline itself has shifted (Section 14, monthly human-baseline re-run). If humans review all outputs by default, that is a different value proposition — flag it as an augmented workflow, not an automated one (EVALUATION_CONTRACTS.md, Mistake 5).
7. **Ownership and cadence.** Ask: "Who owns this contract, when is it reviewed, and what triggers a re-review?" A contract with no owner and no review date is a document, not a contract.

Then produce the verdict per the contract below.

## Verdict Contract

- **Verdict:** one of
  - `CONTRACT-COMPLETE` — a written contract exists, covers all five core checks (failure taxonomy, launch thresholds, rollback triggers, monitoring plan, human-baseline comparison) with specific numbers and named owners, and includes silent-failure detection.
  - `CONTRACT-GAPPY` — a contract exists but one or more core checks are missing, vague, or unowned. Common gaps: no rollback threshold, no silent-failure signals, no human baseline, unweighted failure taxonomy, thresholds as ranges rather than numbers.
  - `NO-CONTRACT` — no written contract exists before build, or the team is relying on presentation rather than a defined contract.
- **Confidence:** High / Medium / Low, with reasoning. High when the contract is explicit and the user can produce the numbers; Medium when answers came partly from memory; Low when key checks were answered "unknown" and the verdict depends on them.
- **Citations:** cite the specific doctrine section driving each check, e.g. `05_ai_product_management/EVALUATION_CONTRACTS.md` (Section 11 launch, Section 12 rollback, Section 13 monitoring), `05_ai_product_management/FAILURE_MODES.md` (failure taxonomy), `05_ai_product_management/MODEL_VS_SYSTEM.md` (monitor the system, not the model).
- **Stated assumptions:** every "unknown" recorded, with the effect each would have on the verdict.
- **What would change the verdict:** for `NO-CONTRACT`, the flip is a written contract covering the five checks. For `CONTRACT-GAPPY`, the flip is the specific missing check being filled with numbers and an owner. For `CONTRACT-COMPLETE`, the flip is discovery that thresholds are numbers on paper but unenforced in production — the contract is then complete as a document but not as a decision tool.

Example verdict output (shape to copy, not to memorize):

```
Verdict: CONTRACT-GAPPY
Confidence: Medium — launch thresholds and failure taxonomy exist; rollback and human baseline were answered from memory.
Citations:
  - Failure taxonomy: 05_ai_product_management/FAILURE_MODES.md (silent failure as meta-failure)
  - Rollback requirement: 05_ai_product_management/EVALUATION_CONTRACTS.md (Section 12, silent-failure rollback)
  - Human baseline: 05_ai_product_management/EVALUATION_CONTRACTS.md (Section 14, monthly re-run)
Stated assumptions:
  - Exact rollback numbers not yet written down (unknown); verdict would upgrade if the document contains them.
What would change the verdict: a written rollback section with numeric silent-failure
  triggers (override rate, human-review error rate) and a defined human-baseline comparison.
```

## Thresholds

A second reviewer must reproduce the verdict from the same inputs.

- **NO-CONTRACT** — no written contract exists AND no defined launch/rollback/monitoring thresholds exist anywhere (a deck, a memo, or a post-hoc rationale does not count). The team is deciding readiness by demo or schedule.
- **CONTRACT-GAPPY** — a written contract exists AND at least one of the five core checks is missing, vague, or unowned: (a) no failure taxonomy with severity weights, (b) no numeric launch thresholds, (c) no rollback trigger with a timeframe, or (d) no defined human-baseline comparison, or (e) no named monitoring owner/cadence. A rollback section that contains only system-error signals (5xx, outage) is a gap, not a rollback threshold — silent failures require non-system-error signals.
- **CONTRACT-COMPLETE** — a written contract exists AND all of: (a) failure taxonomy with severity weights covering the domain-critical failure modes including silent ones, (b) numeric launch thresholds on an explicitly defined evaluation set, (c) rollback triggers with specific metrics and timeframes including silent-failure signals, (d) a monitoring plan with cadence and ownership including distribution-shift detection, (e) a defined human-baseline comparison with a re-run cadence, and (f) a named owner and review date. If any check is "unknown" and materially affects the call, drop to the highest-confidence verdict consistent with the knowns.

Worked example for calibration. A contract that names only "model accuracy 95% on our test set" fails at step (a) — no severity weights, no failure taxonomy — and returns CONTRACT-GAPPY, not NO-CONTRACT, because a contract exists. A contract that names accuracy, a severity-weighted taxonomy, launch gates, rollback triggers including override-rate, a quarterly human-baseline re-run, and a named owner returns CONTRACT-COMPLETE even if a supporting detail (e.g., exact p99 latency target) is a stated assumption. The line between GAPPY and COMPLETE is drawn by the five core checks, not by the completeness of the appendices.

## Evidence & Doctrine

- `05_ai_product_management/EVALUATION_CONTRACTS.md` — the reference standard: defines success in product terms, failure taxonomy with severity weights, launch thresholds, rollback thresholds, ongoing monitoring, and the "silent failure rollback" requirement that triggers include non-system-error signals.
- `05_ai_product_management/FAILURE_MODES.md` — the failure taxonomy: hallucination, omission, confidence miscalibration, reasoning error, distribution shift, prompt injection, cascading failure, and silent failure as the meta-failure. Silent failures are "plausible-looking wrong answers with no system error" — the reason monitoring gaps exist.
- `05_ai_product_management/MODEL_VS_SYSTEM.md` — monitor the system, not the model; model-level metrics can look fine while the system fails on integration, context corruption, or distribution shift.
- `05_ai_product_management/GOVERNANCE.md` — proportional governance: the contract is the product-facing layer of governance; its completeness determines whether governance can operate.
- `PRN-0011` — leading indicators beat lagging; the monitoring plan must track behaviors that precede the outcomes (override rate, opt-out, satisfaction) not just revenue that trails them.
- `CON-0011` — human-in-the-loop vs automation; a contract that routes everything to humans has not automated anything — it must specify which outputs require review and measure the review rate against budget.
- `CASE-0018` — Boeing 737 MAX: failure modes analyzed for design conditions but not for the failure condition (single-sensor MCAS); the analog is a contract with golden-path thresholds but no failure-taxonomy depth.
- `CASE-0019` — Theranos: launch without independent validation, presentation standing in for a contract; the analog is shipping an AI system with no defined thresholds and no validation gate.
- `09_tools/EVALUATION_CONTRACT_TEMPLATE.md` — drafting aid; the completeness check above is the acceptance criteria for a filled-in template.

Cite, don't copy. Quote at most a short line with a location, then point at the module.

## Common Pitfalls

- **The accuracy trap.** "95% accuracy" with no defined evaluation set, no severity weighting, and no measurement method is a meaningless threshold. Correction: accuracy must be defined against the failure taxonomy — "95% task success rate where severity 3-5 counts as failure."
- **Rollback amnesia.** Launch thresholds set, rollback thresholds absent — "once it launches, it keeps working." Correction: define explicit rollback triggers with metrics, timeframes, and procedure, including the silent-failure signals.
- **System-error-only monitoring.** Monitoring 5xx rates and uptime while the system returns plausible wrong answers at 200 OK. Correction: add human-review sampling, override-rate, opt-out, and business-metric correlation to the monitoring plan.
- **Human review as a crutch.** "We'll have humans check everything" with no review budget measured. Correction: specify which outputs require review by severity/confidence/novelty, and measure review rate against budget — if it exceeds budget, the automation value proposition is void.
- **Contract as document.** A complete contract that is never enforced, never re-run against production, and owned by nobody. Correction: named owner, review cadence, and review trigger events (model change, incident, threshold breach).
- **No human baseline.** Thresholds set against internal guesses instead of a measured human performance level. Correction: define the human baseline and re-run it on a cadence; the baseline itself can shift.
- **Optimizing for the evaluation set.** The same 50 examples tested every week produce apparent improvement while real-world performance degrades. Correction: rotate examples, add production-sourced examples, keep held-out sets.

## Related Skills

- `pressure-test-product-thesis` — the "before" half for AI bets: the thesis defines the bet; the evaluation contract defines the test that executes the bet's falsification condition.
- `assess-product-market-fit-health` — the "after" half for launched AI products: the contract's monitoring produces the leading indicators that PMF health is judged on.
- `09_tools/EVALUATION_CONTRACT_TEMPLATE.md` — drafting tool referenced by remediation of a `CONTRACT-GAPPY` verdict.
