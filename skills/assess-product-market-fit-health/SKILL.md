---
name: assess-product-market-fit-health
description: >-
  Verdict on whether product-market fit is a healthy current condition, decaying, never
  achieved, or simply unmeasured — calibrated to the product's archetype (enterprise,
  product-led SaaS, consumer subscription, marketplace, developer tool, usage-based,
  regulated, episodic, internal platform, pre-revenue). Separates product value, retention,
  acquisition efficiency, expansion, monetization, competitive pull, user dependence, and
  market constraints instead of forcing one universal indicator battery. Invoke for a
  quarterly health review, before a pivot, when revenue holds but usage erodes, or when a
  vanity metric is offered as proof of PMF.
type: assess
version: 0.2.0
best_for:
  - "Quarterly PMF health review of an existing product"
  - "Revenue is fine but usage/enthusiasm is drifting — is PMF decaying?"
  - "Before a major pivot or market entry: is current PMF real or assumed?"
  - "A vanity metric (e.g. signups, MAU) is being cited as proof of PMF"
  - "Disagreement between 'the numbers look good' and 'customers seem disengaged'"
doctrine:
  - "PRN-0004 (PMF is a condition, not a milestone)"
  - "PRN-0011 (leading indicators beat lagging)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0005 (PM owns problem not solution)"
  - "04_product_archetypes/ (archetype-specific health signals)"
  - "CASE-0003 (Google Reader sunset)"
  - "SRC-BOOK-0010 (Innovator's Dilemma, Tier B)"
  - "09_tools/PRODUCT_THESIS_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

This skill answers one question: **is product-market fit a healthy current condition for this
product, or is it decaying — or was it never achieved?** PMF is not a milestone you pass once
and celebrate; it is a condition that must be maintained as markets evolve, competitors
emerge, and customer needs change (PRN-0004). The danger is that the lagging indicators people
actually watch — revenue, retention — stay fine for quarters after the condition has started
to rot.

This skill is calibrated to the product's **archetype**. There is no single universal
indicator battery: Sean Ellis-style "very disappointed" scores fit product-led consumer-ish
products, not enterprise, marketplaces, or regulated products. The skill separates PMF into
independent dimensions and judges each with archetype-appropriate evidence, so it doubles as a
general **product-health diagnosis** tool: activation, retention, engagement, and unit
economics are inputs, not afterthoughts.

## Use when

- Quarterly PMF health review of an existing product.
- Revenue is fine but usage/enthusiasm is drifting — is PMF decaying?
- Before a major pivot or market entry: is current PMF real or assumed?
- A vanity metric (signups, MAU) is cited as proof of PMF.
- "The numbers look good" vs "customers seem disengaged" disagreement.
- A general product-health review: activation poor but retention strong among activated
  users; acquisition strong but liquidity/monetization weak.

## Do not use when

- The user wants a revenue forecast or a churn analysis — that is finance, not PMF health.
- The product is pre-PMF and its job is to find PMF, not maintain it — the verdict set
  includes `NEVER-ACHIEVED` for the boundary case, but the skill is calibrated to assess an
  existing condition.
- The user refuses to produce any evidence at all — the verdict will be `UNMEASURED`, which
  is itself the finding, and a list of the measurements to stand up.
- A reversible, low-stakes metric question (e.g. "should we move one button") — Fast mode only,
  or skip.

## Inputs

Required inputs:

- The product's archetype (from the context-classification table below) — this selects the
  evidence battery.
- For each dimension that applies to the archetype: current value AND trend over at least 3
  periods (a snapshot is not a trend).
- The customer segment(s) being assessed, and the date of the last systematic reassessment.

Optional inputs:

- Lagging indicators (revenue, retention, churn) for the Innovator's Dilemma check.
- The thesis document, to check the verdict against its falsification conditions.

## Missing-data behavior

- Missing a dimension's data → record as a stated assumption; the dimension is marked
  `UNMEASURED` and its absence named in the verdict.
- No leading indicators at all → `UNMEASURED` overall, with the specific measurements to
  stand up for this archetype.
- "Unknown" on trend → a snapshot cannot support any verdict above `UNMEASURED` on that
  dimension; the trend is the signal, not the level.

## Context classification

Archetype determines the evidence battery. The shared taxonomy in `_shared/SKILL_CONTRACT.md`
(§3) defines the signature evidence per archetype; the PMF dimension table below applies it.

| Archetype | Lead indicators to assess (non-exhaustive) | Strong evidence types |
|---|---|---|
| B2B enterprise | Implementation success, expansion NRR, referenceability, win/loss, renewal intent | E8 sales/loss, E4 cohort, E11 financial |
| Product-led SaaS | Activation, self-serve conversion, feature adoption, NRR, activation cohorts | E3 analytics, E4 cohort, E11 financial |
| Consumer subscription | Retention curve, churn, DAU/WAU, re-subscription intent, payback | E4 cohort, E3 analytics, E5 interviews |
| Marketplace | Liquidity (fill rate, time-to-match), take rate, both-side retention | E3 analytics, E4 cohort, E11 financial |
| Developer tool / API | Time-to-first-value, sandbox→prod conversion, API adoption, community pull | E3 analytics, E9 market, E6 usability |
| Usage-based product | Consumption growth, seat growth, overage, net expansion | E3 analytics, E11 financial |
| Regulated product | Compliance outcomes, audit results, reliability, renewal | E10 incidents, E11 financial, E9 market |
| Episodic product | Re-engagement, event-to-event interval, repeat-use intent | E4 cohort, E3 analytics, E5 interviews |
| Internal platform | Adoption, developer velocity, incident rate, org pull | E3 analytics, E10 incidents |
| Pre-revenue / pre-launch | Signal proxies: pilots, LOIs, waitlists, interview conviction, design partners | E5 interviews, E9 market, E6 usability |

## Fast mode

Run for a quick health pulse on a reversible question (or as a first pass before a full
review). Four questions, using the archetype's evidence battery:

1. What is the archetype, and which 2–3 dimensions matter most for it?
2. For those dimensions: do you have current values and a trend over 3+ periods?
3. Is any dimension clearly declining for 3+ periods, or is the roadmap dominated by
   existing-customer requests while emerging needs go unserved?
4. Do the lagging indicators (revenue, retention) disagree with the leading ones?

Provisional verdict: `HEALTHY` / `DECAYING` / `NEVER-ACHIEVED` / `UNMEASURED` per the verdict
contract, using only the top 2–3 dimensions. Confidence capped at Medium. Next action: the
single cheapest measurement that would firm up the weakest dimension.

## Full mode

Adds: all applicable dimensions assessed with 3+ period trends; the Innovator's Dilemma
roadmap check; the PRN-0014 same-data-opposite-conclusions discriminating-test design; the
segmentation check (is decay confined to one segment?); and a written reversal condition for
the verdict.

## Method

Work through these questions in order. Ask the user directly. "Unknown" answers are recorded
as stated assumptions and the assessment continues.

1. **Classify the archetype.** Which row of the table applies? This sets the evidence battery. If two apply (e.g. B2B enterprise + usage-based), assess both — never average them.
2. **Separate the dimensions.** Score each applicable PMF dimension separately: product value, retention, acquisition efficiency, expansion, monetization, competitive pull, user dependence, market constraints. A product can be strong on retention and weak on monetization; the verdict must not conflate them.
3. **Is each dimension measured?** Ask for current value + 3+ period trend per applicable dimension. If a dimension has no data, mark it `UNMEASURED` and name the measurement to stand up.
4. **Product value.** For the archetype: activation quality (PLG), implementation success (enterprise), liquidity (marketplace), time-to-first-value (dev tool), compliance-reliability (regulated), signal quality (pre-revenue). Ask what happens if the product disappears — Sean Ellis applies only where a survey base is meaningful; for other archetypes use the archetype-appropriate proxy.
5. **Retention / repeat use.** Ask for cohort retention or re-engagement trend. Falling depth — users staying registered but engaging less — is the behavioral precursor to silent departure. Watch the trap where MAU looks stable because registrations grow while per-user engagement falls.
6. **Acquisition efficiency.** Ask how new customers arrive and whether organic share is declining while paid spend is flat. For marketplaces, ask liquidity rather than signup volume; for enterprise, win/loss in evaluated deals.
7. **Expansion and monetization.** Ask net revenue retention or expansion trend (enterprise/SaaS/usage), re-subscription intent (consumer/episodic), take rate (marketplace). This is where a "growth" product with no monetization shows its gap.
8. **Competitive pull and market constraints.** Ask win/loss trend and any market constraint (regulation, dependency, distribution) that cap the product's pull. The Innovator's Dilemma check: is the roadmap dominated by existing-customer requests while emerging needs go unserved?
9. **Same data, opposite conclusions (PRN-0014).** If two stakeholders read the dashboard differently, name the discriminating metric and design the test (a cohort split) rather than argue.
10. **Record assumptions and render the verdict** per the contract.

## Evidence classification

Uses the shared 15-type taxonomy. The governing rule: **a PMF claim is graded by the match
between the claim and the evidence type, for this archetype.** Cohort/retention evidence (E4),
behavioral analytics (E3), sales/loss evidence (E8), and financial evidence (E11) are the
workhorses. Interview evidence (E5) establishes problem and intent, not behavior — interview
enthusiasm contradicted by usage behavior (E3/E4) resolves toward behavior. Published research
(E13) and doctrine (E12) frame, never decide, this product's condition.

## Output schema

```json
{
  "skill": "assess-product-market-fit-health",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "HEALTHY | DECAYING | NEVER-ACHIEVED | UNMEASURED",
  "archetype": "B2B-enterprise | PLG-SaaS | consumer-subscription | marketplace | dev-tool-API | usage-based | regulated | episodic | internal-platform | pre-revenue",
  "dimensions": [
    {"dimension": "product_value | retention | acquisition_efficiency | expansion | monetization | competitive_pull | user_dependence | market_constraints",
     "status": "healthy | decaying | never-achieved | unmeasured", "trend": "...", "evidence_types": ["E4"]}
  ],
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E4", "E8"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** one of
  - `HEALTHY` — PMF is a maintained current condition: the applicable leading dimensions are
    measured over 3+ periods and stable or improving, and no Innovator's Dilemma signal exists.
  - `DECAYING` — PMF was achieved but is eroding: one or more applicable leading dimensions
    declining for 3+ periods, or the Innovator's Dilemma trap (lagging indicators holding
    while leading indicators rot).
  - `NEVER-ACHIEVED` — the applicable leading dimensions never reached healthy levels, or a
    pre-PMF product is being treated as if fit were a formality. PMF is not a state that can
    decay; it must first exist.
  - `UNMEASURED` — the applicable dimensions are not tracked, so no condition can be assessed.
    This is a finding, not an admission of defeat: it names the measurements to stand up.
- **Dimension scoring:** each applicable dimension is scored healthy / decaying /
  never-achieved / unmeasured separately. The overall verdict is driven by the weighted
  leading dimensions, not by any single universal threshold.
- **Confidence:** High when the user supplies current values and 3+ period trends for all
  applicable leading dimensions; Medium when data is partial; Low when the verdict leans on
  assumptions.
- **Evidence basis:** taxonomy types used per dimension.
- **Assumptions:** every "unknown," with its effect on the verdict.
- **What would change the verdict:** for `DECAYING`, the flip is 2 consecutive periods of
  reversal in the decaying dimension, or a discriminating cohort test showing the decay is a
  segment artifact. For `UNMEASURED`, the flip is 2 periods of the dimensions being tracked.
  For `HEALTHY`, the flip is a leading dimension entering a 3-period decline or the
  Innovator's Dilemma signal appearing. For `NEVER-ACHIEVED`, the flip is a reassessment
  showing the earlier read was measurement error.
- **Next action:** for DECAYING, name the dimension and the corrective experiment (see
  `design-product-experiment`); for UNMEASURED, stand up the named measurements; for HEALTHY,
  set the next review date; for NEVER-ACHIEVED, re-derive the problem (`frame-product-problem`).

### Worked example

A **B2B enterprise** product reports: implementation success 84% (flat), expansion NRR 118%
(up from 112%), win rate 50% in evaluated deals (down from 68% over four quarters), and a
roadmap dominated by top-20-account asks for the last two quarters with a new entrant serving
an emerging need. Revenue is up 12% YoY. Scoring: retention/expansion healthy; competitive
pull decaying (win-rate trend); market constraints — Innovator's Dilemma signal present. Verdict:
`DECAYING` — the enterprise battery does not include Sean Ellis, and no 40% threshold is
applied; the win-rate and roadmap signals carry the verdict, and the revenue number is cited
as the Innovator's Dilemma signal, not as health. The discriminating move for the contested
reading is a deal-level win/loss teardown split by segment and deal size.

A **marketplace** reporting high signup volume but low liquidity (fill rate 12%, time-to-match
11 days) scores acquisition unmeasured-as-health (signups are not PMF) and retention/liquidity
decaying → `DECAYING` or `NEVER-ACHIEVED` depending on history, with liquidity named as the
measurement to stand up.

## Failure modes

- **Revenue as health.** Revenue is the laggiest of lagging indicators; decay accumulates for quarters before it shows. Correction: the leading dimensions are the verdict input; revenue is context only.
- **Vanity metric as PMF.** Signups, MAU, or demo requests cited as proof. Correction: apply the archetype battery — for marketplaces, liquidity; for enterprise, win/loss and expansion; for SaaS, activation cohorts.
- **Universal-threshold cargo cult.** Applying a 40% "very disappointed" bar to an enterprise or marketplace product. Correction: the archetype selects the battery; Sean Ellis applies only where the survey base is meaningful.
- **Retention masking dissatisfaction.** "Customers haven't left, so they're satisfied." Survivorship — they may be trapped by switching costs. Correction: usage depth and "what would you use instead" catch trapped users.
- **Snapshot instead of trend.** A single healthy reading with no history. Correction: require 3+ periods of trend before any verdict above `UNMEASURED`.
- **The Innovator's Dilemma trap.** Optimizing for existing customers while emerging needs go unserved, with lagging indicators nodding along. Correction: run the explicit roadmap check.
- **Leading-indicator cargo cult.** Tracking metrics without validating they predict outcomes for THIS product. Correction: every 12 months, validate that the leading indicators actually lead.
- **Celebrated-and-forgotten.** A PMF milestone from 2 years ago cited as current evidence. Correction: `UNMEASURED` until current data exists; the milestone proves nothing.
- **Treating NEVER-ACHIEVED as DECAYING.** A product that never had PMF does not need maintenance; it needs a different problem. Correction: check for any period of health before assigning the decay verdict.

## Reversal conditions

- A decaying dimension reverses for 2 consecutive periods → upgrade.
- A leading dimension enters a 3-period decline → downgrade.
- A discriminating cohort test shows decay is a segment artifact → re-grade by segment.
- The archetype changes (a pivot) → re-run with the new battery.
- A leading-indicator validation finds the indicator no longer leads → replace it.

## Composition hooks

- **before:** `frame-product-problem` (defines which problem and segment PMF is assessed
  against); `pressure-test-product-thesis` (the thesis defined what PMF should look like;
  this skill reports whether that bet pays off); `synthesize-customer-discovery` (interview
  intent evidence feeds the product-value dimension).
- **after:** `design-product-experiment` (a DECAYING dimension needs a corrective experiment);
  `prioritize-product-opportunities` (which opportunity restores the decaying dimension);
  `make-go-no-go-call` (pivot or kill); `scan-contradictions-assumptions` (assumptions behind
  contested readings).
- **workflow:** product-health-review (entry), product-bet (step 7.5 for launched bets).

## Related Skills

- `pressure-test-product-thesis` — the "before" half: the thesis defined what PMF should look like; this skill reports whether that bet is paying off as a maintained condition.
- `design-product-experiment` — a DECAYING dimension names the corrective experiment to run.
- `synthesize-customer-discovery` — interview evidence feeds the product-value dimension.
- `check-ai-evaluation-contract` — for AI products, the contract's monitoring generates the leading indicators this skill judges.
- `frame-product-problem` — re-derives the problem when the verdict is NEVER-ACHIEVED.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy, archetype table, and output schema.
