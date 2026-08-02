# Scenario 7 — Marketplace With Acquisition But Poor Liquidity

**Domain:** Marketplace. **Type:** mature product, health misdiagnosis by vanity metric.

## Context

A freelance-services marketplace. Signups are strong and growing (30k/month, +20% QoQ). The
board cites signup growth as proof of health. But liquidity is poor: fill rate (booked
projects / posted projects) is 12%, and median time-to-first-match is 11 days. Supply-side
cohorts churn fast: 70% of new providers never complete a second job.

## Inputs available (imperfect)

- Signups 30k/month (+20% QoQ).
- Fill rate 12%; median time-to-first-match 11 days.
- Provider cohort: 70% of new providers never complete a second job (E4).
- Demand-side: 45% of posted projects never get a qualifying application.
- No take-rate or margin data; no demand-side retention curve.

## Skills applied and run record

**1. `assess-product-market-fit-health` (full, archetype marketplace).** Dimension scoring:
acquisition — signups healthy (E3); but signups are NOT the PMF signal for a marketplace;
liquidity — decaying/unmeasured-at-12%-fill with an 11-day match (E3/E4); both-side retention —
decaying (70% of providers never complete a second job, E4); monetization — unmeasured (no
take-rate data). The verdict explicitly refuses to treat signups as health: `DECAYING` on
liquidity/retention, with acquisition healthy. Confidence Medium (take-rate missing). Next
action: stand up the take-rate and demand-side retention curves; the discriminating question
is whether the 11-day match is a demand problem, a supply problem, or a matching-model problem.

**2. `synthesize-customer-discovery` (fast, optional).** Provider interviews (from the notes):
"jobs don't come fast enough" — anecdote (few sources) vs the cohort signal (70% second-job
churn, repeated). Stated-vs-actual: providers state "no work," cohort data shows one-job
retention collapse. Resolves toward the cohort. Verdict: thin on the demand side, but the
behavioral signal is the one to trust.

**3. `prioritize-product-opportunities` (fast).** Corrective candidates: matching-model change
(E4/E3-supported, high leverage), supply acquisition (would worsen liquidity if demand can't
absorb), demand-side marketing (improves fill if supply quality holds). Ranked with the
matching-model change first, on liquidity evidence. Each item's next decision named.

## Verdict produced

DECAYING on liquidity and both-side retention; signup growth explicitly re-labeled as a
vanity metric for this archetype. Corrective priority: the matching/liquidity problem, with
the take-rate measurement stood up first.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact marketplace vanity-metric trap. |
| Correctness | 5 | Signups correctly refused as a PMF proxy; liquidity/retention carried the verdict. |
| Actionability | 4 | Measurement stand-up + corrective priority concrete; the matching-model fix is a direction, not a design. |
| Uncertainty handling | 4 | Take-rate and demand-retention gaps recorded as assumptions; Medium confidence; flip named. |
| Evidence use | 5 | E4 provider cohort and E3 liquidity correctly weighted over E9/E12 market optimism; internal evidence first-class. |
| Proportionality | 4 | Full health review appropriate for a board-facing claim. |
| Avoidance of framework theater | 4 | No forced CON sweep; archetype battery earned its place. |
| Clarity of final decision | 5 | One verdict, one corrective priority, one measurement to stand up. |

**Mean: 4.5.** Weakness noted: the "matching-model change" corrective is a direction without a
spec; the corrective experiment skill is written for a single metric change, not a matching
algorithm change — a genuine gap for marketplace teams.
