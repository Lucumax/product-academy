# Scenario 5 — Launch Pressure Before Reliability Evidence

**Domain:** B2B enterprise / platform. **Type:** irreversible-ish, high-risk, sponsor pressure.

## Context

A payments-integration product. A key competitor just shipped a similar feature. The CEO and
Sales want to launch now to protect market position. The reliability evidence is missing: no
load test at expected peak, one SEV-2 in the last month, and the rollback path for the new
integration has never been executed. The launch cannot be quietly rolled back — it changes the
billing contract for existing customers.

## Inputs available (imperfect)

- Competitive pressure: competitor launched 2 weeks ago; 3 deals are "in play."
- Reliability: one SEV-2 last month; no load test; rollback never executed; expected peak
  transaction volume 4× current.
- Billing-contract change → reversal would require re-negotiating contracts (not a flag).
- Strategy: no written statement covering this.

## Skills applied and run record

**1. `classify-decision-reversibility` (full).** Irreversible dimension present (contract
change with legal renegotiation); reversal mechanism untested (rollback never executed);
latency to reverse (re-negotiation cycle) exceeds the damage window. Verdict: `TYPE-1`
(effectively irreversible on the billing surface). Process: premortem mandatory, escalation to
the level matching the commitment, explicit reversibility design (phase the billing change,
grandfather a cohort).

**2. `run-case-based-premortem` (full).** Top scenarios: (1) peak-load outage — severity 5,
probability 40% (no load test), pattern: speed-without-assurance (Knight Capital-analog,
mechanism present: unverified reliability gating a money-moving system); (2) billing-change
lock-in with a defect — severity 5, probability 35%, pattern: Boeing-analog (competitive
pressure overriding an assurance requirement); (3) rollback impossible when discovered —
severity 5, probability 45%. Verdict: `NOT-DEFENSIBLE` — a top-3 scenario is severity ≥ 4 with
probability ≥ 40% and no mitigation brings it under the bar (no load test, no tested rollback).

**3. `audit-decision-evidence` (full).** Claims: (a) the feature works at peak — NO-EVIDENCE;
(b) we can support the billing change — NO-EVIDENCE (rollback never executed); (c) competitive
window justifies risk — evidence: 3 deals in play, E8 sales evidence, single-source, no
loss-data baseline → UNDER-SUPPORTED. Decision verdict: `NO-GO` (load-bearing claims missing
on a Type-1 surface).

**4. `make-go-no-go-call` (full).** Strategy gate: no written strategy (assumption, weakened
verdict). GO conditions 4, 5, 6 fail. Verdict: `NO-GO` on the full launch;
`PROCEED-AT-RISK` offered to the CEO with missed thresholds named and a required tested-rollback
design; the CEO declined formal acceptance. Recommend: phased launch on a grandfathered cohort
with a load test and a rehearsed rollback before the billing change touches existing contracts.

## Verdict produced

NO-GO on the irreversible full launch; PROCEED-AT-RISK surfaced (declined); the correct path
is a phased, grandfathered rollout with load test + rehearsed rollback.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact sponsor-pressure-before-reliability scenario. |
| Correctness | 5 | Type-1 classification and NOT-DEFENSIBLE premortem match the fixture. |
| Actionability | 4 | Phased/grandfathered rollout path is concrete; contract-drafting detail is a pointer. |
| Uncertainty handling | 4 | No-strategy and unmeasured peak recorded; flip conditions named. |
| Evidence use | 4 | E10 (SEV-2), E8 (deals) used; the load-test absence correctly scored NO-EVIDENCE. |
| Proportionality | 4 | Full chain appropriate to a money-moving Type-1; fast modes not available here and rightly so. |
| Avoidance of framework theater | 5 | Every step earned its place; no forced vocabulary. |
| Clarity of final decision | 5 | NO-GO + the exact preconditions (load test, rehearsed rollback, grandfathered cohort). |

**Mean: 4.5.** Weakness noted: the "phased, grandfathered rollout" design is offered as advice
but no skill designs the phasing — it comes from the reversibility skill's process budget,
not a dedicated mechanism.
