# Scenario 2 — Poor Activation, Strong Retention Among Activated Users

**Domain:** SaaS (PLG). **Type:** mature product, product-health diagnosis.

## Context

A PLG SaaS product (10k signups/month) has an activation problem: only 8% of signups reach
the "core action" within 14 days. But among activated users, 6-month retention is 91% and
NRR is 118%. Leadership argues about whether the product is healthy: "we have a retention
machine" vs "we are bleeding the top of the funnel."

## Inputs available (imperfect)

- Activation rate 8% (14-day core action), flat over 4 quarters.
- Activated-cohort 6-month retention 91%, stable; NRR 118%.
- Funnel data: the drop happens at step 2 (workspace setup) for 60% of drop-offs.
- No activation cohort analysis by signup source; no onboarding-experiment history.
- Revenue up 12% YoY.

## Skills applied and run record

**1. `assess-product-market-fit-health` (full, archetype PLG-SaaS).** Dimensions scored
separately: product value — strong for activated users (retention 91%, NRR 118% → E4 cohort
evidence); acquisition efficiency — unmeasured (no source-level activation cohorts); retention
— healthy; expansion — healthy; activation* (the funnel gate) — decaying: activation flat at
8% while acquisition spend grew. No universal Sean Ellis threshold applied (archetype battery).
Verdict: `DECAYING` on the acquisition→activation path, with retention healthy — the verdict
explicitly separates the two so leadership cannot argue past each other. Innovator's Dilemma
check: roadmap is balanced, no trap signal. Next action: source-level activation cohort (E4)
to find which acquisition sources under-activate.

**2. `scan-contradictions-assumptions` (fast).** Top assumptions: (1) the 8% activation is
the product's true ceiling, not a funnel bug; (2) activated-user retention will hold if
activation doubles. TOP-ASSUMPTION: retention durability under a doubled activation rate —
if activation widens to lower-intent users, retention may decay. Next action: cohort the
experiment by intent source.

**3. `design-product-experiment` (full).** Corrective experiment for the decaying dimension:
"reducing step-2 setup friction raises 14-day activation from 8% toward 12% without lowering
activated-cohort retention." Primary metric: 14-day activation, baseline 8%; guardrail metric:
activated-cohort 90-day retention ≥ 88%. Interpretation rule pre-committed; stop rules set
(6 weeks / 20k signups; early stop on guardrail breach). Competing hypotheses: signup-source
mix shift, onboarding email regression. Rollback: flag. Verdict: SPEC-READY.

## Verdict produced

DECAYING on the activation path, HEALTHY on retention. The corrective experiment is specified
with a retention guardrail so the team cannot "fix" activation by degrading retention.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact PLG activation-vs-retention diagnostic. |
| Correctness | 5 | Verdict correctly separated dimensions; the 8%-activation signal was not papered over by the 91% retention. |
| Actionability | 5 | Corrective experiment with metric, guardrail, and stop rules. |
| Uncertainty handling | 4 | Retention-durability assumption named; confidence Medium; source-cohort flip named. |
| Evidence use | 5 | E4 cohort + E3 funnel used and ranked by claim; internal evidence carried the verdict. |
| Proportionality | 4 | Full chain on a quarterly-class decision; acceptable, fast modes used where possible. |
| Avoidance of framework theater | 4 | No forced CON sweep; the contradiction step earned its place on the retention-durability assumption. |
| Clarity of final decision | 5 | DECAYING + one corrective experiment + guardrail. |

**Mean: 4.6.** Strongest run of the suite. Weakness noted: the funnel drill-down (which step-2
sub-step kills activation) is not a skill capability — it relies on the user's funnel data.
