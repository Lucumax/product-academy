# Scenario 8 — Vanity Metric as Proof of PMF

**Domain:** Early-stage product (pre-revenue). **Type:** early-stage, weak evidence.

## Context

A pre-revenue productivity tool. The founding team celebrates "10,000 signups" and "300 daily
active users" as proof of PMF in the board deck. There is no retention curve, no willingness-
to-pay signal, no cohort of repeat use. One investor asks: "what would make you think this ISN'T
working?"

## Inputs available (imperfect)

- 10k total signups; 300 DAU (3% DAU/signups).
- No cohort retention; no survey of "very disappointed"; no willingness-to-pay; no pilot or LOI.
- The "thesis": "teams will adopt our tool for weekly planning" — no falsification condition stated.

## Skills applied and run record

**1. `pressure-test-product-thesis` (full).** Slots: segment (teams) is vague; problem
(planning friction) unstated in customer terms; mechanism (tool) stated; outcome (adoption)
not measurable as stated. No falsification condition. Evidence: signups/demos only
(presentation-adjacent, no discovery base). Verdict: `UNDERSPECIFIED` → the team could not
articulate a disproof condition → effectively `BELIEF-PRESENTED-AS-THESIS` once prompted.
Next action: write the falsification test with a pre-committed NO-GO threshold (e.g. "of 40
trial teams, <8 reach weekly use by day 30 → the adoption assumption is wrong").

**2. `assess-product-market-fit-health` (full, archetype pre-revenue).** The archetype battery
uses signal proxies, not revenue: DAU/signups of 3% is a usage-depth signal but with no cohort
retention it cannot reach a verdict. Willingness-to-pay: none. Verdict: `UNMEASURED` — the
10k/300 numbers are not PMF evidence for a pre-revenue product; the output names the signal
battery to stand up (cohort retention, 40-trial activation, willingness-to-pay, 3 disconfirming
interviews). Confidence High on UNMEASURED (that verdict does not need the missing data — it
is the finding).

**3. `audit-decision-evidence` (fast).** Claim "we have PMF" — evidence: 10k signups (E3
registration volume), which does not match the claim type (a PMF claim needs cohort retention,
E4). Verdict: `NO-EVIDENCE`-shaped for the PMF claim; the numbers support "people register,"
nothing more.

## Verdict produced

UNMEASURED for PMF (the 10k/300 deck is explicitly re-labeled: signups are not PMF); the
thesis is UNDERSPECIFIED/BELIEF until a falsification condition and a signal battery exist.
The board deck's "proof" is graded as registration volume, which is the finding.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact early-stage vanity-metric scenario. |
| Correctness | 5 | UNMEASURED + UNDERSPECIFIED are the evidence-correct verdicts. |
| Actionability | 4 | Signal battery + falsification test concrete; will stand up in one sprint. |
| Uncertainty handling | 5 | Every missing signal named as a measurement to stand up, not padded; confidence honest. |
| Evidence use | 5 | Registration volume correctly refused as PMF evidence; claim-evidence mismatch named explicitly. |
| Proportionality | 4 | Three skills on a board-deck claim; fast modes used where possible; pre-revenue context tolerates it. |
| Avoidance of framework theater | 5 | No forced CON sweep; every skill step earned its place. |
| Clarity of final decision | 5 | One message: not measured yet, here is the battery and the falsification test. |

**Mean: 4.75.** Weakness noted: the strongest scenario, and it reveals the portfolio's bias
favoring evidence skills — for a pre-revenue team the *stand-up* (building the measurement)
still depends on the team's own analytics capacity; no skill generates the instrumentation.
