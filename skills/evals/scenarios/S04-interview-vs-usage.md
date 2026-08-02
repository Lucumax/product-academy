# Scenario 4 — Interview Enthusiasm vs Usage Behavior

**Domain:** Consumer subscription. **Type:** weak evidence, conflicting signals.

## Context

A consumer fitness app. Interviews with 25 active users: all five showcased users and most
others say "the new habit streaks feature is the reason I keep coming back." Product wants to
double down on streaks. Weekly usage data shows streaks engaged by 6% of DAU, and the users
who cite streaks in interviews are the top-decile already-engaged cohort.

## Inputs available (imperfect)

- 25 interviews: 22 mention streaks positively; 5 showcase users rave.
- Behavioral data: streaks feature used by 6% of DAU; median weekly session count flat at 3.1.
- No cohort split of streak-users vs non-users on retention.
- No survey (stated intent at population scale).

## Skills applied and run record

**1. `synthesize-customer-discovery` (full).** Themes extracted: (1) "streaks keep me coming
back" — repeated observation (22/25) BUT interview-only (E5), and the loudest voices are the
already-engaged top decile (segment skew); (2) "weekly engagement is flat at 3.1 sessions" —
behavioral observation (E3) across the population. Stated-vs-actual check: stated enthusiasm
(22/25) vs behavior (6% DAU feature usage) — discrepancy flagged. Verdict:
`BEHAVIOR-CONTRADICTS`. Trust the behavior for the "causes return" claim: interview intent is
a loyalty artifact, not a mechanism. Next action: a streak-user vs non-streak-user retention
cohort split (E4) to test whether streaks *cause* retention or merely *attract* it.

**2. `conduct-causal-confidence-review` (fast).** Claim: "streaks caused the retention of the
top decile." Baseline: no pre-feature retention for streak-users; alternatives: the top decile
was already high-retention before streaks; selection bias (engaged users use streaks, not
vice versa). Verdict: `CORRELATED` at best; the causal claim is a survivorship artifact until
a cohort split exists. Next action: the discriminating cohort test.

**3. `prioritize-product-opportunities` (fast).** "Invest in streaks" ranked on current
evidence: impact confidence capped at "wild guess" (E5 intent only, contradicted by E3
usage). Demoted below opportunities with behavioral support. Verdict: RANKED with streaks
flagged `evidence-gap`.

## Verdict produced

BEHAVIOR-CONTRADICTS: the roadmap should not double down on streaks until the cohort split
tests whether streaks cause or merely accompany retention. Interview enthusiasm is recorded
as intent, not demand.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact stated-vs-actual trap. |
| Correctness | 5 | Behavior correctly preferred for a "causes return" claim; selection bias named. |
| Actionability | 4 | Cohort split next action is concrete; prioritization demotion actionable. |
| Uncertainty handling | 4 | Population-scale intent unknown recorded; Medium confidence; flip named (cohort result). |
| Evidence use | 5 | E5 vs E3/E4 ranking was explicit and correct — the portfolio's core differentiator. |
| Proportionality | 3 | Two skills on a feature-level question; fast modes used but the chain still felt heavy for a weekly decision. |
| Avoidance of framework theater | 4 | No forced CON sweep; causal review used fast. |
| Clarity of final decision | 5 | One decision: do not invest until the cohort split. |

**Mean: 4.4.** Weakness noted: this scenario is where the portfolio most needed a single
"resolve stated-vs-actual" step; today it composes two skills and the composition is not yet
documented as a named workflow.
