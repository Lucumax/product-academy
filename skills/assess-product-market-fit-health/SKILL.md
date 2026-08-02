---
name: assess-product-market-fit-health
description: >-
  Produces a verdict on whether product-market fit is a healthy current
  condition or decaying, using leading indicators — Sean Ellis score, organic
  growth, usage depth, competitive win/loss — NOT lagging ones like revenue and
  retention. Invoke for a quarterly PMF health review, before a big pivot, when
  revenue holds but usage is quietly eroding, or when the board asks whether
  PMF is at risk. Uses PRN-0004 (PMF is a condition, not a milestone) and
  PRN-0011 (leading indicators beat lagging).
type: assess
version: 0.1.0
best_for:
  - "Quarterly PMF health review of an existing product"
  - "Revenue is fine but usage/enthusiasm is drifting — is PMF decaying?"
  - "Before a major pivot or market entry: is current PMF real or assumed?"
  - "Post-launch, 2+ years out: has the condition been maintained or celebrated and forgotten?"
  - "Disagreement between 'the numbers look good' and 'customers seem disengaged'"
doctrine:
  - "PRN-0004 (PMF is a condition not a milestone)"
  - "PRN-0011 (leading indicators beat lagging)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0005 (PM owns problem not solution)"
  - "CON-0002 (discovery vs conviction)"
  - "CASE-0003 (Google Reader sunset)"
  - "SRC-BOOK-0010 (Innovator's Dilemma, Tier B)"
  - "09_tools/PRODUCT_THESIS_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

This skill answers one question: **is product-market fit a healthy current condition for this product, or is it decaying — or was it never achieved?** PMF is not a milestone you pass once and celebrate; it is a condition that must be maintained as markets evolve, competitors emerge, and customer needs change (PRN-0004). Products that had PMF lose it. The danger is that the lagging indicators people actually watch — revenue, retention — stay fine for quarters after the condition has started to rot.

Invoke this skill when a decision depends on the true state of the product-market relationship: a quarterly health review, a pivot decision, a "revenue is holding but something feels off" conversation, or a board question about whether PMF is at risk. The skill judges the condition from leading indicators (PRN-0011) and deliberately refuses to be comforted by lagging ones.

Do NOT invoke this skill for a pre-PMF product whose job is to find PMF, not maintain it — the verdict set includes `NEVER-ACHIEVED` for the boundary case, but the skill is calibrated to assess an existing condition. Do NOT invoke it when the user wants a revenue forecast or a churn analysis — that is finance, not PMF health. Do NOT invoke it when the user refuses to produce any leading-indicator data; the verdict will be `UNMEASURED`, which is itself the finding.

## Input

What the user should bring:

- The leading-indicator data for the product: Sean Ellis score (or the survey that produces it), organic growth rate from word-of-mouth, usage depth (active vs registered, weekly active vs daily), competitive win/loss rate in evaluated deals.
- The current values AND the trend over at least 3 quarters — a snapshot is not a trend.
- The lagging indicators for context only: revenue, retention, churn. These are checked to catch the Innovator's Dilemma trap, not to declare health.
- The customer segment(s) being assessed, and the date the product last had a systematic PMF reassessment.

If the user has only revenue and retention and no leading indicators, the skill still runs: the verdict is `UNMEASURED`, and the method shows exactly which four measurements to stand up.

## Method

Work through these questions in order. Ask the user directly. If the user answers "unknown," record it as a stated assumption and continue — never silently assume.

1. **Is PMF measured with leading indicators at all?** Ask: "What is the Sean Ellis 'very disappointed' score, the organic growth rate, usage depth, and competitive win/loss — and are they tracked over time?" If none exist, return `UNMEASURED` and list the four indicators to stand up (PRN-0004 practical tool, PMF Health Dashboard).
2. **Sean Ellis score.** Ask: "What fraction of active users would be 'very disappointed' if the product disappeared?" The threshold is 40% (PRN-0004 practice exercise). Record the score and the survey base — the score from all registrations, not just active users, is a different and weaker signal. A score of 38% against a 44% reading three quarters ago is a decaying signal even though it is close to the line; the trend matters more than the single point.
3. **Organic growth.** Ask: "What fraction of new customers arrive without paid acquisition — word of mouth, referral, inbound?" Declining organic share while paid spend is flat is an early decay signal; it predicts churn before revenue shows it. A strong answer is a trend: "organic was 45% of new customers in Q1, 41% in Q2, 36% in Q3." A weak answer is a claim of "strong word of mouth" with no measurement.
4. **Usage depth.** Ask: "What is weekly-active vs registered, and daily-active vs weekly? What is the trend?" Falling depth — users staying registered but engaging less — is the behavioral precursor to a silent customer departure. Watch for the trap where MAU looks stable because total registrations keep growing while per-user engagement falls; depth, not raw counts, is the signal.
5. **Competitive win/loss.** Ask: "In evaluated deals where the customer was choosing between us and a named alternative, what is the win rate, and is it changing?" A declining win rate is the leading edge of market-share loss. If the team has no win/loss tracking, record that as an unknown — it is one of the four indicators the UNMEASURED verdict names.
6. **The Innovator's Dilemma check.** Ask: "Who are we optimizing for? Is the roadmap dominated by requests from existing customers while emerging needs go unserved?" Cross-reference the leading indicators against the lagging ones: if revenue and retention are holding while the leading indicators decay, the product is likely optimizing for existing customers at the expense of emerging needs (SRC-BOOK-0010; PRN-0004 failure mode). This is the CASE-0003 pattern — a beloved-but-decaying product judged healthy on usage metrics that undercounted its true position. The concrete signal: the last several quarters of roadmap items are all "asks from the top 20 accounts" and nothing addresses a need a new entrant is serving.
7. **Same data, opposite conclusions.** If two stakeholders read the same dashboard differently, apply PRN-0014: name the discriminating metric and design the test rather than argue the interpretation. If the argument is "organic is flat but revenue grows," the discriminating question is whether the growth is retention-driven or acquisition-driven — a cohort split settles it.
8. **Record assumptions.** Any "unknown" is recorded with its effect on the verdict.

Then produce the verdict per the contract below.

## Verdict Contract

- **Verdict:** one of
  - `HEALTHY` — PMF is a maintained current condition: Sean Ellis at or above 40% on active users, leading indicators stable or improving over 3+ quarters, and no Innovator's Dilemma signal.
  - `DECAYING` — PMF was achieved but is eroding: one or more leading indicators declining for 3+ quarters, or the Innovator's Dilemma trap present (lagging indicators holding while leading indicators rot).
  - `NEVER-ACHIEVED` — the leading indicators never reached healthy thresholds, or a pre-PMF product is being treated as if fit were a formality. PMF is not a state that can decay; it must first exist (PRN-0004 non-applicability).
  - `UNMEASURED` — the leading indicators are not tracked at all, so no condition can be assessed. This is a finding, not an admission of defeat: it names the measurements to stand up.
- **Confidence:** High / Medium / Low, with reasoning. High when the user supplies current values and 3+ quarter trends for all four leading indicators; Medium when data is partial; Low when the verdict leans on indicators answered "unknown."
- **Citations:** cite the doctrine behind each conclusion, e.g. `PRN-0004` (PMF as condition; 40% Sean Ellis threshold), `PRN-0011` (leading over lagging), `SRC-BOOK-0010` (Innovator's Dilemma, Tier B), `CASE-0003` (Google Reader: usage metrics masking a decaying position).
- **Stated assumptions:** every "unknown" with its effect on the verdict.
- **What would change the verdict:** for `DECAYING`, the flip is 2 consecutive quarters of reversal in the decaying indicator, or the discriminating cohort test showing the decay is a segment artifact, not a population trend. For `UNMEASURED`, the flip is 2 quarters of the four indicators being tracked. For `HEALTHY`, the flip is a leading indicator entering a 3-quarter decline or the Innovator's Dilemma signal appearing. For `NEVER-ACHIEVED`, the flip is a reassessment showing the leading indicators were actually healthy and the earlier read was measurement error.

Example verdict output (shape to copy, not to memorize):

```
Verdict: DECAYING
Confidence: Medium — three leading indicators have 3+ quarter trends; win/loss data is a stated assumption.
Citations:
  - Leading over lagging: PRN-0011
  - PMF as condition: PRN-0004 (PMF Health Dashboard; reversal conditions)
  - Innovator's Dilemma: SRC-BOOK-0010 (Tier B)
Stated assumptions:
  - Competitive win/loss rate not tracked (unknown); a healthy win/loss trend would soften but not flip the verdict.
What would change the verdict: a cohort split showing the organic-share decline is confined
  to low-value segments, or 2 quarters of reversal in Sean Ellis and organic share.
```

## Thresholds

A second reviewer must reproduce the verdict from the same inputs.

- **UNMEASURED** — fewer than 2 of the 4 leading indicators exist as tracked data over any history. No Sean Ellis score, no organic share, no usage depth, no win/loss — even if revenue and retention are strong.
- **NEVER-ACHIEVED** — at least 2 of the 4 leading indicators are measured AND none reach healthy thresholds in the most recent full quarter: Sean Ellis < 40% on active users, organic growth near zero, usage depth (DAU/WAU or WAU/registered) structurally low, and no evaluated-deal win rate. Distinguisher vs `DECAYING`: no period of health in the data.
- **DECAYING** — at least 2 of the 4 leading indicators measured AND one or more shows decline for 3 consecutive quarters, OR the Innovator's Dilemma trap is present: lagging indicators (revenue, retention) stable or growing while 2+ leading indicators decline for 3+ quarters. A single noisy quarter does not decay; 3 quarters of trend does (PRN-0004 reversal conditions).
- **HEALTHY** — all 4 leading indicators measured over 3+ quarters, Sean Ellis >= 40% on active users, no leading indicator in a 3-quarter decline, and no Innovator's Dilemma signal (roadmap not dominated by existing-customer requests at the expense of emerging needs).

Confidence: High when all four indicators have data and trends; Medium when three; Low when the verdict is driven by two indicators plus stated assumptions.

Worked example for calibration. A product reports: Sean Ellis 42% on active users (down from 48% three quarters ago), organic share 34% of new customers (down from 47%), DAU/WAU holding at 0.55, win rate 50% in evaluated deals (down from 68%), revenue up 12% YoY. The lagging indicator (revenue) is up; three of four leading indicators are down for 3+ quarters. This returns DECAYING, not HEALTHY, and the revenue number is cited as the Innovator's Dilemma signal, not as health — exactly the pattern PRN-0011 warns about. If the same product had flat-to-up leading indicators on all four, it returns HEALTHY with the revenue number as corroboration. The discriminating move for the contested reading is a cohort split: is the organic decline concentrated in new-vs-returning segments or across the board?

## Evidence & Doctrine

- `PRN-0004` — PMF is a condition, not a milestone; the PMF Health Dashboard (Sean Ellis score, organic growth rate, usage depth, competitive win/loss, "what would you use instead?") and the 40% "very disappointed" threshold; the failure modes list includes "measuring PMF with lagging indicators (revenue, retention) that show problems only after PMF has already decayed" and "optimizing for existing customers at the expense of emerging customer needs."
- `PRN-0011` — leading indicators beat lagging; by the time a lagging indicator signals a problem, the problem has been accumulating for quarters. Failure mode: "leading indicator cargo cult" — measuring behavioral metrics without validating they predict the outcome.
- `PRN-0014` — same data, opposite conclusions; when the dashboard is read two ways, design the discriminating test (e.g., a cohort split) instead of arguing.
- `PRN-0005` — the PM owns the problem, not the solution; decay analysis must return to the problem, not produce a feature list.
- `SRC-BOOK-0010` (Tier B) — The Innovator's Dilemma: incumbents lose markets by optimizing for existing customers and missing emerging needs. The canonical decay mechanism behind the `DECAYING` verdict.
- `CASE-0003` — Google Reader sunset: a product judged on usage decline that was actually still beloved and influential; the flip side of the trap — usage metrics that undercounted the product's real position. Source: `SRC-POST-0037` (Tier C).
- `CON-0002` — discovery vs conviction; sustained health requires ongoing discovery (PRN-0008), and the absence of it is itself a decay signal.
- `09_tools/PRODUCT_THESIS_TEMPLATE.md` — the thesis defines what PMF looks like for the product; a decay verdict should be checked against the thesis's falsification conditions.

Cite, don't copy. Quote at most a short line with a location, then point at the registry.

## Common Pitfalls

- **Revenue as health.** "Revenue is up, so we're fine." Revenue is the laggiest of lagging indicators; the decay has been accumulating for quarters by the time it shows. Correction: the four leading indicators are the verdict input; revenue is context only.
- **Retention masking dissatisfaction.** "Customers haven't left, so they're satisfied." Survivorship bias — they may be trapped by switching costs (PRN-0004 failure mode). Correction: usage depth and the "what would you use instead" question catch trapped users.
- **Snapshot instead of trend.** A single Sean Ellis score called "healthy" with no history. Correction: require 3 quarters of trend before any verdict above `UNMEASURED`.
- **The Innovator's Dilemma trap.** Optimizing for existing customers while emerging needs go unserved, with the lagging indicators nodding along. Correction: run the explicit check in Method step 6; a roadmap review is part of the assessment.
- **Leading-indicator cargo cult.** Tracking the four indicators without validating they predict retention or expansion for THIS product (PRN-0011 failure mode). Correction: every 12 months, validate that the leading indicators actually lead.
- **Celebrated-and-forgotten.** A PMF milestone celebration from 2 years ago cited as current evidence. Correction: `UNMEASURED` until current data exists; the milestone proves nothing.
- **Treating `NEVER-ACHIEVED` as `DECAYING`.** A product that never had PMF does not need maintenance; it needs a different problem. Correction: check for any period of health in the data before assigning the decay verdict.

## Related Skills

- `pressure-test-product-thesis` — the "before" half: the thesis defined what PMF should look like; this skill reports whether that bet is paying off as a maintained condition.
- `check-ai-evaluation-contract` — for AI products, the contract's monitoring plan generates the leading indicators this skill judges; a `CONTRACT-GAPPY` verdict explains why the PMF signal may be missing.
- `09_tools/PRODUCT_THESIS_TEMPLATE.md` — reassessment tool when the verdict is `DECAYING` or `NEVER-ACHIEVED` and the problem must be re-derived (PRN-0005).
