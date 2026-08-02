---
name: classify-decision-reversibility
description: >-
  Classifies a decision as Type-1 (one-way door, irreversible or very expensive
  to reverse) or Type-2 (two-way door, reversible at acceptable cost) and sets
  the required analysis and process budget, escalation level, and artifacts.
  Invoke before any significant product decision to determine how much process
  it deserves, and whenever a team claims a decision is reversible — verify the
  reversal mechanism actually exists before accepting the claim. Explicitly
  catches the "assumed reversible but isn't" failure (Knight Capital: reversal
  took 45 minutes while $10M/minute burned).
type: assist
version: 0.1.0
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

This skill exists to stop the two most common decision-process failures from
`01_core_doctrine/DECISION_FRAMEWORKS.md` Framework 1: treating Type-2 decisions
as Type-1 (over-analysis, slow decisions, executive bottlenecks — the most
common) and treating Type-1 decisions as Type-2 (under-analysis, catastrophic
outcomes — less common but more dangerous). It also catches the third and
deadliest failure: false reversibility, where a decision is claimed reversible
but the reversal mechanism has never been tested or takes so long that the
damage is done first. That is the Knight Capital pattern (CASE-0005): the
deployment was theoretically reversible, but shutdown took 45 minutes while
$10M per minute was lost.

Invoke it at the start of any decision with resource commitment, customer-facing
change, or strategic direction. Do NOT invoke it for decisions so small that
the classification itself costs more than the decision is worth, or when the
user wants a document — the output of this skill is a process assignment, not
a memo.

## Input

What the user should bring, in plain language:

- Decision: the exact decision and the scope of its commitment (budget,
  headcount, contracts, brand, pricing, data, compliance, safety).
- Cost of being wrong: expected loss if the decision is wrong, and how
  probable being wrong is.
- Cost to reverse: money, time, trust, and contracts that reversal would
  consume.
- Reversal mechanism: how would you reverse, who would trigger it, has it
  ever been executed, and how long does it take end-to-end?
- Escalation context: who has authority at what level of commitment.
- If the user does not know some of these, record each as an assumption and
  continue — the classification will be downgraded accordingly.

## Method

One question at a time. "Unknown" answers become explicit assumptions, never
silent defaults.

1. **State the decision and its commitment scope.** Write down what is being
   committed and at what scale. Framework 1: resource commitment, customer-facing
   change, and strategic direction are the triggers.
2. **List the irreversible dimensions.** Check the Framework 1 Type-1 examples:
   major architecture, brand name, pricing model restructuring, entering a
   market with capital commitment, sunsetting a product with contractual
   obligations, regulatory compliance. One irreversible dimension makes the
   decision Type-1 regardless of the others.
3. **Run the PRN-0007 Reversibility Assessment.** (a) expected cost if wrong,
   (b) probability of being wrong, (c) cost to make the decision reversible,
   (d) how quickly you would detect you are wrong, (e) how quickly you could
   reverse, (f) is the cost of reversibility less than cost-of-wrong ×
   probability-of-wrong?
4. **The Knight test.** The reversal mechanism must be real, not theoretical:
   has it ever been executed end-to-end? How long does it take? Who triggers it
   — named by name, not role (FMEA decision rule)? What is the damage window
   during reversal — the time between "we were wrong" and "we are safe"?
5. **Compare reversal latency to the damage window.** If time-to-reverse
   exceeds time-to-permanent-damage, the decision is effectively Type-1 even if
   it looks reversible. This is the Knight Capital case in one sentence.
6. **The convenience check.** Framework 1 failure mode 3: executives classify
   decisions as Type-1 to keep control; teams classify decisions as Type-2 to
   avoid oversight. Ask who benefits from each classification.
7. **Classify.** Render TYPE-1, TYPE-2, or RECLASSIFIED-TYPE-1 per Thresholds,
   then set the process budget, escalation level, and required artifacts.

## Verdict Contract

WHAT THIS SKILL MUST RETURN. The output is a process assignment, not a memo:

- **Verdict:** TYPE-1 (irreversible) / TYPE-2 (reversible) /
  RECLASSIFIED-TYPE-1 (claimed reversible, verified not — treated as Type-1
  until the reversal mechanism is demonstrated).
- **Process budget:** for TYPE-2, analysis ≤ 10% of the decision's
  implementation cost, decide as close to the information as possible, inform
  rather than ask permission (Framework 1). For TYPE-1, analysis proportional
  to irreversibility cost, broader cross-functional input, pre-mortem required,
  explicit reversibility design, escalate to the level matching the commitment
  scale.
- **Escalation level:** the named person or body that must sign off, matched
  to commitment scale.
- **Required artifacts:** reversal plan with a tested trigger for TYPE-2;
  pre-mortem + decision memo + named reversal authority for TYPE-1.
- **Confidence:** High / Medium / Low with reasoning. High when the reversal
  mechanism has actually been executed and the cost figures are real; Medium
  when costs are estimates; Low when the reversal claim rests on intent.
- **Citations:** stable Academy doctrine/source IDs for each classification
  driver (e.g. `Framework 1`, `PRN-0007`, `CASE-0005`).
- **Stated assumptions:** everything answered "unknown", with the effect each
  has on the classification.
- **What would change the verdict:** the specific evidence that would flip it
  (e.g. "RECLASSIFIED-TYPE-1 becomes TYPE-2 if the team runs a tested dry-run
  of the reversal, names a trigger authority, and measures latency under the
  damage window").

## Thresholds

Reproducible criteria. A second reviewer must be able to reproduce the
classification from the same inputs.

**TYPE-2 (reversible) requires ALL of the following:**
1. Reversal cost < 10% of the committed value of the decision.
2. Time-to-reverse < time-to-permanent-damage (reversal beats the damage
   window).
3. The reversal mechanism has been executed end-to-end at least once, or is a
   standard pattern with a demonstrable track record (rollback, feature flag,
   A/B test with rollback).
4. A named person has authority to trigger reversal, and the trigger condition
   is specific and observable (FMEA: not "if users are unhappy" but "if NPS
   drops below X and churn rises above Y").
5. No irreversible dimension from Framework 1's Type-1 list applies.

Process budget if TYPE-2: spend no more than 10% of implementation cost on
analysis; decide at the team level; require the reversal plan but no standard
escalation (inform, don't ask).

**TYPE-1 (irreversible) if ANY of the following:**
1. Any Framework 1 Type-1 dimension applies (architecture, brand, pricing model,
   market entry with capital, contract-laden sunset, regulatory).
2. Reversal cost ≥ 10% of committed value.
3. Time-to-reverse ≥ time-to-permanent-damage.
4. The decision is precedent-setting and will constrain many future decisions.

Process budget if TYPE-1: analysis proportional to irreversibility cost;
broader cross-functional, multi-level input; explicit reversibility design
(can we make part of this reversible?); pre-mortem required; escalate to the
level matching the scale of commitment.

**RECLASSIFIED-TYPE-1 (assumed reversible but isn't) if:**
- The decision was claimed or assumed TYPE-2, but the reversal mechanism is
  untested, or the reversal authority is not named, or measured reversal
  latency exceeds the damage window (CASE-0005). Treat as TYPE-1 until the
  reversal mechanism is demonstrated with a measured dry-run, a named owner,
  and latency under the damage window.

## Evidence & Doctrine

Academy references, cited not copied.

- `01_core_doctrine/DECISION_FRAMEWORKS.md` — Framework 1: the Type-1/Type-2
  classification, the decision rules (≤ 10% analysis for Type-2; pre-mortem,
  broader input, escalation for Type-1), and the four failure modes including
  false reversibility. This is the canonical source; Tier A doctrine.
- `PRN-0007` (Best Product Decisions Are Reversible by Design) — the
  Reversibility Assessment and the failure modes "assuming reversibility
  without testing it" and "reversibility that takes so long the damage is
  done before the reversal completes". Tier A.
- `PRN-0003` (Cost of Delay Exceeds Cost of Imperfection) — the budget logic:
  its applicability conditions require reversibility and bounded downside;
  its non-applicability conditions are exactly the Type-1 triggers. Tier A.
- `PRN-0012` (Most Expensive Decision Is the One You Do Not Make) — the
  boundary: do not use "irreversible" as cover for decision avoidance; the
  classification sets process, not paralysis. Tier A.
- `09_tools/DECISION_MEMO_TEMPLATE.md` — its header requires a Decision Type
  (Type 1/Type 2), so this skill runs before the memo is written.
- `09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md` — the Reversibility 1–5 scale
  used in portfolio comparison; consistent with, not a replacement for,
  Framework 1.
- `07_cases/case_catalog.md` — CASE-0005 (Knight Capital: theoretical
  reversibility, 45-minute shutdown latency, $440M loss; causal_confidence
  high — the canonical false-reversibility case), CASE-0001 (Netflix Qwikster:
  brand/pricing decision treated as reversible, reversed in 23 days at ~800K
  subscribers; causal_confidence high), CASE-0018 (Boeing 737 MAX:
  certification and training shortcuts made an irreversible-safety decision
  look procedural; causal_confidence high), CASE-0019 (Theranos: regulatory
  and medical decisions with irreversible patient harm; causal_confidence
  high).

## Common Pitfalls

- **Treating Type-2 as Type-1.** Over-analysis, executive bottlenecks, slow
  decisions — the most common failure (Framework 1 failure mode 1). Correction:
  the budget rule is hard — ≤ 10% of implementation cost — and the decision
  goes to the team closest to the information.
- **Treating Type-1 as Type-2.** "Move fast" applied to something irreversible
  (Framework 1 failure mode 2; Boeing pattern). Correction: run the irreversible
  dimensions check first; one hit and it is Type-1.
- **False reversibility.** The reversal mechanism has never been tested
  (CASE-0005). Correction: the Knight test — execute the reversal end-to-end
  before relying on it; measure latency against the damage window.
- **Reversibility theater.** Mechanisms built but no one has the authority or
  courage to use them (PRN-0007 failure mode). Correction: name the trigger
  authority by name, not role, and define the trigger condition in observable
  terms before the decision is made.
- **Misclassification for convenience.** Executives classify Type-2 as Type-1
  to keep control; teams classify Type-1 as Type-2 to avoid oversight
  (Framework 1 failure mode 3). Correction: ask who benefits from the
  classification, and document it in the decision memo.
- **Budget applied to the wrong thing.** Spending the whole budget on
  forecasting instead of reversibility design. Correction: PRN-0007 — when
  outcomes are uncertain, invest in reversibility, not prediction.

## Related Skills

- `make-go-no-go-call` — uses this skill's TYPE-1/TYPE-2 classification as GO
  condition 6; run this first.
- `run-case-based-premortem` — Framework 1 requires a pre-mortem for every
  TYPE-1 decision; chain this skill into it before committing.
- After classification, the process assignment feeds `09_tools/DECISION_MEMO_TEMPLATE.md`
  (Decision Type field, reversal conditions section) and
  `09_tools/EVALUATION_CONTRACT_TEMPLATE.md` (decision rights table).
