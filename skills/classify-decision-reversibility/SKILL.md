---
name: classify-decision-reversibility
description: >-
  Classifies a decision as Type-1 (one-way door, irreversible or very expensive to reverse)
  or Type-2 (two-way door, reversible at acceptable cost) and sets the required analysis and
  process budget, escalation level, and artifacts. Run before any significant product decision
  to determine how much process it deserves, and whenever a team claims a decision is
  reversible — verify the reversal mechanism actually exists before accepting the claim.
  Catches the "assumed reversible but isn't" failure (Knight Capital: reversal took 45 minutes
  while $10M/minute burned).
type: assist
version: 0.2.0
best_for:
  - "Any significant decision, before choosing how much analysis and approval it gets"
  - "A team claims a decision is reversible — verify the reversal mechanism exists and is tested"
  - "Setting the process budget: how much analysis, what escalation, what artifacts are required"
  - "Deciding whether to move fast per PRN-0003 or slow down per Framework 1"
  - "Designing a Type-1 decision to be more reversible (feature flags, phased rollout, API versioning)"
doctrine:
  - "PRN-0007, PRN-0003, PRN-0012"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 1: One-Way vs Two-Way Door Classification)"
  - "09_tools/DECISION_MEMO_TEMPLATE.md, 09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md"
  - "07_cases/case_catalog.md (CASE-0001, CASE-0005, CASE-0018, CASE-0019)"
license: CC BY 4.0
---

## Purpose

This skill stops the three most common decision-process failures from Framework 1: treating
Type-2 decisions as Type-1 (over-analysis, executive bottlenecks — the most common), treating
Type-1 decisions as Type-2 (under-analysis, catastrophic outcomes — less common but more
dangerous), and false reversibility, where a decision is claimed reversible but the reversal
mechanism has never been tested or takes so long the damage is done first (the Knight Capital
pattern, CASE-0005).

Invoke it at the start of any decision with resource commitment, customer-facing change, or
strategic direction. The output is a process assignment (verdict + process budget + escalation
+ artifacts), not a memo.

## Use when

- Any significant decision, before choosing how much analysis and approval it gets.
- A team claims a decision is reversible — verify the reversal mechanism exists and is tested.
- Setting the process budget for a quarter or a major initiative.
- Deciding whether to move fast (PRN-0003) or slow down (Framework 1).
- Designing a Type-1 decision to be more reversible.

## Do not use when

- The decision is so small the classification itself costs more than the decision is worth.
- The user wants a document — the output is a process assignment, not a memo.
- The decision is already committed and irreversible — the classification still informs the
  post-mortem but there is no process budget to set.

## Inputs

Required inputs:

- Decision: the exact decision and the scope of its commitment (budget, headcount, contracts, brand, pricing, data, compliance, safety).
- Cost of being wrong: expected loss if wrong, and how probable being wrong is.
- Cost to reverse: money, time, trust, and contracts that reversal would consume.
- Reversal mechanism: how would you reverse, who would trigger it, has it ever been executed, how long does it take end-to-end?
- Escalation context: who has authority at what level of commitment.

Optional inputs:

- The irreversibility dimensions the decision touches (architecture, brand, pricing model, market entry, sunset, regulatory).
- The decision's damage window: how long between "we were wrong" and "we are permanently harmed."

## Missing-data behavior

- "Unknown" on costs, mechanism, or escalation → record as assumptions; the classification is
  downgraded accordingly (a reversal mechanism that has never been exercised defaults to
  unverified, i.e. the Knight test fails).
- "Unknown" on whether the decision is reversible → treat as TYPE-1 until demonstrated
  otherwise. Claiming reversibility on intent is the failure this skill exists to catch.

## Context classification

- **Framework 1 trigger dimensions:** resource commitment, customer-facing change, strategic
  direction. Any one of these → run this skill.
- **Irreversible dimensions list:** architecture, brand, pricing-model restructuring, market
  entry with capital commitment, contract-laden sunset, regulatory. One hit → TYPE-1.
- **Stakes:** the decision's committed value sets the proportional analysis budget.

## Fast mode

A rule of thumb for ordinary decisions. Three checks:

1. Does any Framework 1 irreversible dimension apply (architecture, brand, pricing model, market entry, contract-laden sunset, regulatory)? If yes → TYPE-1.
2. Is reversal cost < 10% of committed value AND time-to-reverse < time-to-permanent-damage AND the reversal is a standard pattern (rollback, feature flag, A/B with rollback)? If all three → TYPE-2.
3. Is the reversal claim untested, authority unnamed, or latency unmeasured? If so → RECLASSIFIED-TYPE-1.

Provisional verdict + process budget in minutes. If any answer is "unknown" and the decision
is large, escalate to Full mode.

## Full mode

Adds the PRN-0007 Reversibility Assessment (6 questions), the Knight test (has the mechanism
been executed end-to-end? who triggers it, by name? what is the damage window during
reversal?), the convenience check (who benefits from each classification), and the full
process-budget + escalation + artifacts assignment.

## Method

One question at a time. "Unknown" answers become explicit assumptions, never silent defaults.

1. State the decision and its commitment scope. Write what is being committed and at what scale.
2. List the irreversible dimensions. Check the Framework 1 Type-1 examples: major architecture, brand name, pricing-model restructuring, market entry with capital commitment, contract-laden sunset, regulatory. One irreversible dimension makes the decision Type-1 regardless of the others.
3. Run the PRN-0007 Reversibility Assessment: (a) expected cost if wrong, (b) probability of being wrong, (c) cost to make the decision reversible, (d) how quickly you would detect you are wrong, (e) how quickly you could reverse, (f) is cost-of-reversibility less than cost-of-wrong × probability-of-wrong?
4. The Knight test: the reversal mechanism must be real, not theoretical — has it ever been executed end-to-end? How long does it take? Who triggers it — named by name, not role? What is the damage window during reversal?
5. Compare reversal latency to the damage window. If time-to-reverse exceeds time-to-permanent-damage, the decision is effectively Type-1 even if it looks reversible. This is the Knight Capital case in one sentence.
6. The convenience check: executives classify decisions as Type-1 to keep control; teams classify decisions as Type-2 to avoid oversight. Ask who benefits from each classification.
7. Classify. Render TYPE-1, TYPE-2, or RECLASSIFIED-TYPE-1 per the verdict contract, then set the process budget, escalation level, and required artifacts.

## Evidence classification

Uses the shared taxonomy. Cost figures are financial evidence (E11); reversal-mechanism
claims are behavioral/operational evidence (E10, E3) — a mechanism that has never been
exercised is E15 (unsupported assertion) until demonstrated. Case calibrations come from the
catalog (E12-grade practitioner evidence, CASE-0005 etc.).

## Output schema

```json
{
  "skill": "classify-decision-reversibility",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "TYPE-1 | TYPE-2 | RECLASSIFIED-TYPE-1",
  "process_budget": {"analysis_cap": "...", "decision_level": "...", "premortem_required": false},
  "escalation_level": "...",
  "required_artifacts": ["..."],
  "confidence": "high | medium | low",
  "evidence_basis": ["E11", "E10"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `TYPE-1` (irreversible) / `TYPE-2` (reversible) / `RECLASSIFIED-TYPE-1`
  (claimed reversible, verified not — treated as Type-1 until the reversal mechanism is demonstrated).
- **Process budget:** TYPE-2 → analysis ≤ 10% of implementation cost *(rule of thumb — raise
  it where the reversal mechanism is unproven, lower it for routine flag-gated changes)*,
  decide as close to the information as possible, inform rather than ask permission. TYPE-1 →
  analysis proportional to irreversibility cost, broader cross-functional input, premortem
  required, explicit reversibility design, escalation to the level matching the commitment scale.
- **Escalation level:** the named person or body that must sign off, matched to commitment scale.
- **Required artifacts:** TYPE-2 → reversal plan with a tested trigger. TYPE-1 → premortem +
  decision memo + named reversal authority.
- **TYPE-2 requires ALL of:** reversal cost < 10% of committed value *(rule of thumb — a
  bounded-cost heuristic, not a law; adjust where reversal costs are lumpy or hard to
  estimate)*; time-to-reverse < time-to-permanent-damage; the mechanism has been executed
  end-to-end at least once or is a standard pattern with a track record; a named trigger
  authority with a specific, observable trigger condition; no irreversible dimension applies.
- **TYPE-1 if ANY of:** an irreversible dimension applies; reversal cost ≥ 10% of committed
  value *(see the rule-of-thumb note above)*; time-to-reverse ≥ time-to-permanent-damage; the
  decision is precedent-setting.
- **RECLASSIFIED-TYPE-1 if:** claimed or assumed TYPE-2, but the reversal mechanism is
  untested, or the authority is unnamed, or measured latency exceeds the damage window (CASE-0005).
- **Confidence:** High when the reversal mechanism has actually been executed and the cost
  figures are real; Medium when costs are estimates; Low when the reversal claim rests on intent.
- **Assumptions:** everything answered "unknown," with effect on the classification.
- **What would change the verdict:** named evidence that flips it (e.g. "RECLASSIFIED-TYPE-1
  becomes TYPE-2 if the team runs a tested dry-run, names a trigger authority, and measures
  latency under the damage window").
- **Next action:** execute the assigned process — write the reversal plan, schedule the
  premortem, or escalate.

### Worked example

Decision: "Move our pricing from per-seat to usage-based for all new contracts." Commitment:
all new contracts, pricing model restructuring (an irreversible dimension) → TYPE-1.
Reversibility design: grandfather existing contracts (reverses the customer-facing blast),
phase new contracts by segment, set a 2-quarter review gate with named trigger authority and a
measured reversal latency (6 weeks) under the damage window (revenue impact for 2 quarters).
The decision can be re-classified toward TYPE-2-*by-design* once the grandfathering and
phasing are executed and the trigger authority is named. Until then it is TYPE-1: premortem
required, escalation to the head of product + finance, decision memo with reversal section.

## Failure modes

- **Treating Type-2 as Type-1.** Over-analysis and executive bottlenecks. Correction: the budget rule is hard — ≤ 10% of implementation cost — and the decision goes to the team closest to the information.
- **Treating Type-1 as Type-2.** "Move fast" applied to something irreversible (Boeing pattern). Correction: run the irreversible-dimensions check first; one hit and it is Type-1.
- **False reversibility.** The reversal mechanism has never been tested (CASE-0005). Correction: the Knight test — execute the reversal end-to-end before relying on it; measure latency against the damage window.
- **Reversibility theater.** Mechanisms built but no one has the authority or courage to use them (PRN-0007 failure mode). Correction: name the trigger authority by name, not role, and define the trigger condition in observable terms before the decision is made.
- **Misclassification for convenience.** Executives classify Type-2 as Type-1 to keep control; teams classify Type-1 as Type-2 to avoid oversight. Correction: ask who benefits, and document it in the decision memo.
- **Budget applied to the wrong thing.** Spending the whole budget on forecasting instead of reversibility design. Correction: PRN-0007 — when outcomes are uncertain, invest in reversibility, not prediction.

## Reversal conditions

- A previously untested reversal mechanism is successfully executed end-to-end → RECLASSIFIED-TYPE-1 becomes TYPE-2.
- A named trigger authority and measurable latency are added and measured under the damage window → upgrade.
- An irreversible dimension is removed by design (grandfathering, phasing, contractual escape) → re-classify.
- The decision's committed value changes materially → re-run the 10% and damage-window checks.

## Composition hooks

- **before:** `frame-product-problem` (the decision being classified is usually a framed problem/opportunity).
- **after:** `run-case-based-premortem` (every TYPE-1 must premortem before commit); `make-go-no-go-call` (GO condition 6); `align-stakeholders-on-decision` (escalation and decision rights); `09_tools/DECISION_MEMO_TEMPLATE.md` (Decision Type field).
- **workflow:** launch-gate (step 1), product-bet (step 0).

## Related Skills

- `make-go-no-go-call` — uses this skill's classification as GO condition 6; run this first.
- `run-case-based-premortem` — Framework 1 requires a premortem for every TYPE-1 decision.
- `align-stakeholders-on-decision` — decision rights and escalation come from this classification.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
