# Scenario X10 — Reversible UI Decision

**Domain:** SaaS. **Situation:** reversible, low-stakes.

## Context

A SaaS dashboard ("Panel") wants to move the "create report" button from the top-right of the
main view to the left sidebar. It is a cosmetic navigation change, fully reversible, no data
changes, no contract changes. The designer prefers the new location; a long-time user
complained on social media that the current placement is hard to find.

The team is split about whether to run a two-week A/B test before the move. One person wants
a full experiment with statistical analysis; another wants to just ship it and watch. There
is no evidence that either placement affects any core metric, and the button is reachable in
both layouts.

## Inputs available (imperfect)

- The change is behind a feature flag and reversible in minutes.
- No metric is expected to move meaningfully; no baseline exists for button clicks.
- One social complaint; designer preference.

## Ask

You have one page to recommend how much process this decision deserves, and what you would
actually do. State your reasoning.
