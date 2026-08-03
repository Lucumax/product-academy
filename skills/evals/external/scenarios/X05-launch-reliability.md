# Scenario X05 — Irreversible Launch With Weak Reliability Evidence

**Domain:** Enterprise platform. **Situation:** sponsor pressure, high stakes.

## Context

A payments-integration product ("Anchor") is under competitive pressure. A competitor just
shipped a similar capability, and the CEO and Sales want to launch Anchor's new billing
integration this quarter "to protect the deals." The launch changes billing contracts for
existing customers — it is not behind a feature flag. Engineering has no load test at the
expected peak, there was one SEV-2 last month on a related system, and the rollback path for
the new billing contract has never been executed. There is no written product strategy.

Three enterprise deals are in play; if Anchor doesn't launch this quarter, Sales says two of
them are at risk. There is no loss baseline (what the win rate or loss rate actually is
without this feature).

## Inputs available (imperfect)

- No load test at expected peak.
- One SEV-2 last month (reliability track record).
- Rollback for the billing change never rehearsed.
- No written strategy.
- 3 deals in play; single-source claim ("they'll churn"), no loss baseline.

## Ask

You have one page to recommend whether to launch this quarter as posed, and how. State your
reasoning and the evidence you are relying on or missing.
