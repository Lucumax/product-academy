# Scenario 9 — Developer Tool With Time-to-First-Value Problem

**Domain:** Developer tool / API. **Type:** mature product, activation diagnosis.

## Context

A developer analytics SDK. Signups are healthy and organic. But time-to-first-value is poor:
median time from signup to first successful data query is 9 days, and 55% of new dev accounts
never complete the first query. Eng proposes a "new onboarding wizard." Product has no evidence
the wizard fixes the drop.

## Inputs available (imperfect)

- Median time-to-first-value: 9 days; 55% of accounts never reach first query (E3).
- Funnel: drop concentrated in the API-key + first-call step.
- Docs pages visited before drop: logged (E3).
- No survey of stalled developers; no support-ticket analysis on onboarding.
- Competitive benchmark: none.

## Skills applied and run record

**1. `frame-product-problem` (fast).** Problem: "developer accounts stall at the first API call
and never see value." Segment: new accounts without existing API experience. Business outcome:
time-to-first-value reduction and first-query completion (activation), not "wizard shipped."
Solution (the wizard) demoted to one candidate. Assumptions: (1) the first-call step is the
blocker (supported by funnel E3 — highest-evidence assumption); (2) a wizard removes it
(unsupported); (3) activation lifts retention (unsupported). Verdict: FRAMED.

**2. `design-product-experiment` (full).** Assumption under test: "reducing first-call setup
friction raises 14-day first-query completion from 45% toward 55%." Primary metric: first-query
completion within 14 days, baseline 45%; guardrail: docs satisfaction and support-contact rate.
Interpretation and stop rules pre-committed (4 weeks / 2k new accounts; early stop on
guardrail breach). Competing hypotheses: the drop is a documentation gap, not a wizard gap; the
signup-source mix shifted. Rollback: flag. Verdict: SPEC-READY. Crucially, the spec refuses to
assume the wizard is the fix — the experiment discriminates wizard-vs-docs-vs-both.

**3. `synthesize-customer-discovery` (fast, optional).** Support tickets (E7) reviewed: 3 of 12
onboarding tickets complain about the API-key step; anecdote-level, but consistent with the
funnel. No interviews. Verdict: THIN-DISCOVERY; the funnel is the signal.

**4. `assess-product-market-fit-health` (fast, dev-tool archetype).** Activation dimension
(dev-tool time-to-first-value) decaying; usage depth among activated healthy; acquisition
healthy (organic). Verdict: DECAYING on the activation path only.

## Verdict produced

DECAYING on the dev-tool activation path; the corrective experiment discriminates
wizard-vs-docs-vs-both before any build. Time-to-first-value is the metric, and the 55% stall
is the signal, not the 9-day median alone.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact dev-tool activation scenario. |
| Correctness | 5 | Funnel evidence correctly identified the step; the experiment correctly refuses to assume the wizard. |
| Actionability | 5 | A discriminating experiment spec with metric, guardrail, stop rules. |
| Uncertainty handling | 5 | Wizard-as-fix and retention-elasticity assumptions named; flip conditions present. |
| Evidence use | 5 | E3 funnel + E7 tickets typed and weighted; internal evidence carried it. |
| Proportionality | 4 | Four skills on a feature-level experiment; fast modes where possible, still a heavy chain for the fix. |
| Avoidance of framework theater | 4 | Health review added the DECAYING label but the experiment was the substance. |
| Clarity of final decision | 5 | Run the discriminating experiment; do not build the wizard blind. |

**Mean: 4.6.** Weakness noted: four skills for one feature decision feels like more process
than the fix deserves; a tighter experiment-first chain (frame → experiment → readout) would
serve this frequency better than the full health review.
