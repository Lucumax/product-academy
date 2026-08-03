# Scenario X09 — Experiment With a Proxy Metric and Possible Harm

**Domain:** Consumer app. **Situation:** experiment design, risk.

## Context

A social app ("Signal") wants to test a change that surfaces more notifications to drive
engagement. The proposed primary metric is "daily notification opens." Engineering can
instrument it. Product leadership wants a decision on whether to run the experiment and how.

Concern raised by a team member: more notifications could increase churn for the least
engaged users (the ones who see the most notifications relative to their engagement), even if
aggregate opens go up. The company has previously had a retention problem in this exact
segment, and there is a support-cost dimension nobody has priced.

## Inputs available (imperfect)

- Proposed metric: daily notification opens (direction up).
- A historical baseline for daily opens exists.
- No pre-committed threshold for what counts as a win.
- No plan for what to do if opens rise but retention falls.
- No segment plan (engagement tiers) before the experiment.
- No rollback plan.

## Ask

You have one page to design how this experiment should be specified before it runs, including
what would count as a win, a stop, and a harm signal. State your reasoning.
