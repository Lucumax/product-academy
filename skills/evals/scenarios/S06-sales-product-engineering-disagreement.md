# Scenario 6 — Sales / Product / Engineering Disagreement

**Domain:** B2B SaaS. **Type:** conflicting stakeholders, goal/incentive/risk stacking.

## Context

A customer-facing AI triage feature. Sales: "Launch now or the two biggest deals this quarter
are at risk." Engineering: "Reliability isn't there; launching is unsafe." Product: "The
evaluation contract says the accuracy bar isn't met yet." The team has met three times with no
progress.

## Inputs available (imperfect)

- Sales quotes: "deals at risk," quota pressure.
- Engineering quotes: "cannot guarantee," "unsafe."
- Product: an evaluation contract exists; the pre-committed accuracy bar is not met.
- No written strategy statement covering AI launch.
- Reversibility: the feature is flag-gated (reversible) if launched to a restricted set.

## Skills applied and run record

**1. `align-stakeholders-on-decision` (full).** Typed the three positions: Sales — GOAL
(launch protects deals) + INCENTIVE (quota); Engineering — RISK (downside unacceptable);
Product — FACT (contract threshold not met). Key diagnostic: the sides are on three different
axes; no single piece of evidence settles all three. Resolutions: FACT axis → the evaluation
contract readout IS the fact (pre-committed thresholds); GOAL/INCENTIVE axis → adjudicate
against strategy (none exists — flagged STUCK-ON-GOALS-OR-INCENTIVES on that axis) and flag
Sales' metric for realignment if strategy says reliability-first; RISK axis → reversibility
design (flag-gated restricted launch + named rollback authority converts "unsafe" into
"bounded"). Decision rights: TYPE-2-with-escalation; decider = head of product, deadline set.
Verdict: `ALIGNMENT-MAP` with one axis stuck on goals (no strategy to adjudicate).

**2. `check-ai-evaluation-contract` (full, for the FACT axis).** The contract exists with a
pre-committed bar; the bar is not met. Verdict: `CONTRACT-COMPLETE` as a document — the
five checks are present — and the *thresholds themselves* are the fact: the launch cannot
happen until the accuracy bar is reached. (This is the correct read: the contract is not
gappy; the feature is simply not ready per the contract's own numbers.) Confidence High.

**3. `make-go-no-go-call` (fast).** With the fact axis settled (not ready), the GO bar fails.
Verdict: `PAUSE`-shaped (a resolvable blocker: reach the contract bar, or explicitly
restrict-and-flag with named rollback authority). The alignment map's decision-rights
assignment lets Product name the decider instead of the team re-meeting.

## Verdict produced

ALIGNMENT-MAP: facts say not-ready (contract), risk resolves via flag-gated restricted launch
with a named rollback authority, goals are stuck until a strategy statement adjudicates
reliability-vs-revenue — and that strategy gap, not the team, is the blocker. Decider named:
head of product, with a deadline.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact cross-functional deadlock. |
| Correctness | 5 | Three-axis typing is the correct diagnosis; contract bar correctly governs the fact axis. |
| Actionability | 4 | Decider + deadline + restricted-launch path concrete; the strategy-gap escalation is a pointer to leadership. |
| Uncertainty handling | 4 | No-strategy assumption exposed; risk tolerance per side named; confidence Medium on the goal axis. |
| Evidence use | 5 | The contract threshold treated as the fact; incentive and goal claims correctly NOT sent for "more data." |
| Proportionality | 4 | Three skills on a contested launch; fast mode where possible. |
| Avoidance of framework theater | 5 | The category-error guard (facts vs goals) is exactly what unblocked it; no forced CON mapping. |
| Clarity of final decision | 5 | Decider named, deadline set, one blocked axis named with its unblock. |

**Mean: 4.6.** Weakness noted: the goal-axis resolution depends on a strategy document that
does not exist; the portfolio has no skill to *produce* a strategy statement — it can only
flag the gap.
