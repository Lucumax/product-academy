# Scenario 11 — Irreversible Pricing Restructure

**Domain:** SaaS. **Type:** irreversible / high-risk decision.

## Context

A company plans to move from per-seat to usage-based pricing for all new contracts. This is a
pricing-model restructuring — a Framework 1 irreversible dimension. The CFO wants a decision in
two weeks. There is no historical data on usage-based adoption (the company is per-seat today).

## Inputs available (imperfect)

- Pricing model change → contract, brand, and billing restructure.
- No usage-based pricing experience in the company; one competitor's public case (published,
  E13-grade practitioner evidence).
- Data: existing per-seat accounts' usage telemetry exists (E3) but was never analyzed for
  pricing implications.
- Finance: a rough sensitivity model with wide ranges (E11).

## Skills applied and run record

**1. `classify-decision-reversibility` (full).** Irreversible dimension: pricing-model
restructuring. Reversal would require re-contracting (expensive, slow). Verdict: `TYPE-1`,
High confidence. Process: premortem mandatory, escalation to head of product + finance,
explicit reversibility design (grandfather existing contracts, phase by segment, set a
2-quarter review gate with a named trigger authority and a measured reversal latency).

**2. `audit-decision-evidence` (full).** Claims: (a) usage-based pricing increases revenue —
evidence: one competitor's public case (E13, single source, no internal base) → UNDER-SUPPORTED;
(b) existing accounts will tolerate the change — evidence: no survey, no contract analysis →
NO-EVIDENCE; (c) we can model the economics — evidence: a wide-range sensitivity model (E11) →
INSUFFICIENT-INFO on accuracy. Decision verdict: `NO-GO` on the two-week decision as posed
(load-bearing claims under-supported on a Type-1), with the specific evidence to upgrade.

**3. `run-case-based-premortem` (full).** Top scenarios: (1) revenue collapse from mispricing
— severity 5, probability 30%; pattern: pricing-as-reversible (Qwikster-analog: a
customer-visible change communicated as a done deal, CASE-0001 mechanism: change without the
customer's mental model — present); (2) grandfathering complexity breaks billing — severity 4,
probability 40%; no case match; (3) the CFO's two-week deadline forces a decision without
evidence — severity 4, probability 50%; no case match. Verdict: `DEFENSIBLE-WITH-MITIGATIONS`
only with the grandfathering + phasing + review-gate design. The mitigation design from the
reversibility step is the artifact that makes this defensible.

**4. `make-go-no-go-call` (full).** GO conditions fail on evidence (condition 4) and the
Type-1 premortem/design condition (condition 6 — now partially met by the reversibility
design). Verdict: `SEEK-MORE-EVIDENCE` is rejected (no discriminating test can resolve pricing
revenue in two weeks); the correct verdict is `PAUSE`-on-the-deadline: decide the *process*
now (grandfathering, phasing, review gate), defer the *pricing numbers* until the usage
telemetry is analyzed and a pilot cohort is priced. Next action: analyze existing usage
telemetry (E3) for pricing distribution; run a grandfather-cohort pilot with the named trigger
authority.

## Verdict produced

PAUSE on the two-week "pick the numbers" decision; PROCEED-with-the-reversibility-design now.
The pricing restructure proceeds as a phased, grandfathered, review-gated program, with the
numeric decision deferred until the evidence exists — and the deadline is explicitly refused
as a reason to decide without evidence (PRN-0003 boundary).

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact irreversible pricing scenario. |
| Correctness | 5 | TYPE-1 + NOT-GO-on-numbers + phased design is the evidence-correct call. |
| Actionability | 4 | Phased program + telemetry analysis + pilot concrete; the pilot's pricing method is a pointer to finance. |
| Uncertainty handling | 5 | Competitor-case weakness, no-internal-base, wide sensitivity ranges all recorded as assumptions; flip evidence named. |
| Evidence use | 5 | E13 single-source correctly demoted vs E3 telemetry available but unanalyzed; internal evidence first-class. |
| Proportionality | 5 | Full chain proportionate to a Type-1 pricing restructure. |
| Avoidance of framework theater | 4 | Qwikster analog required its mechanism (customer-visible change) before naming; clean. |
| Clarity of final decision | 5 | Decide the process now, defer the numbers, refuse the deadline-as-evidence. |

**Mean: 4.75.** Weakness noted: the reversibility-design step (grandfathering, phasing,
review gate) is the highest-leverage output, but it lives inside a skill whose contract
emphasizes classification; the *design* output deserves to be a first-class artifact.
