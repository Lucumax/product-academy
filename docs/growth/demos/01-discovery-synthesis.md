# Demo 1 — Customer-Discovery Synthesis

This is one of three public demonstrations. It shows a real skill turning a messy, realistic
input into a decision artifact.

## Raw scenario

A consumer fitness app interviewed 25 active users about a "habit streaks" feature. The
showcase users rave about it. Weekly usage data shows the feature is used by 6% of DAU, and
median weekly sessions are flat at 3.1.

Inputs available: 25 interviews (22 mention streaks positively; 5 showcase users rave),
behavioral data (6% DAU feature usage), no cohort split.

## Ordinary baseline

> **Baseline prompt (illustrative shape, not a specific model transcript):** "Summarize
> these 25 interviews about the habit streaks feature."
>
> **Generic output shape:** a bullet list of what users said about streaks, weighted toward
> the loudest quotes; a conclusion like "users love streaks, invest in it." No weighting by
> repetition, no stated-vs-actual comparison, no acknowledgement that the loudest voices are
> the already-engaged top decile.

## Skill invocation

> Run the `synthesize-customer-discovery` skill. Input: 25 interviews — 22 mention "streaks
> keep me coming back", 5 showcase users rave. Usage data: streaks used by 6% of DAU, weekly
> sessions flat at 3.1. Return the weighted synthesis and what to trust.

## Resulting artifact (per the skill's contract)

```
Verdict: BEHAVIOR-CONTRADICTS
Themes:
  - "streaks keep me coming back" — REPEATED observation (22/25) BUT interview-only (E5),
    and the loudest voices are the already-engaged top decile (segment skew)
  - "weekly engagement is flat at 3.1 sessions" — behavioral observation (E3), population-wide
Stated-vs-actual: enthusiasm (22/25) vs 6% DAU feature usage — discrepancy flagged
Next action: streak-user vs non-streak-user retention cohort split (E4) — does streaks
  CAUSE retention or merely ATTEND it?
```

## What materially improved

The generic output would have said "invest in streaks." The skill returned a
`BEHAVIOR-CONTRACTS` verdict that refuses to fund a feature on interview enthusiasm alone,
names the selection bias in the loud voices, and gives a test (cohort split) that discriminates
cause from accompaniment.

## Limitations

The skill cannot run the cohort split itself, and it relies on the user supplying behavioral
data — given only interviews, the verdict would be THIN-DISCOVERY rather than
BEHAVIOR-CONTRADICTS. This demo does not prove the skill beats a well-crafted bespoke prompt;
it demonstrates the decision artifact the skill is designed to produce.
