# Scenario 1 — The Bespoke Feature Request

**Domain:** B2B enterprise. **Type:** conflicting stakeholders, large-customer pressure.

## Context

A $2M account (10% of ARR) requests a bespoke "shared-deals dashboard" and hints it may walk
if not delivered this quarter. Sales is pushing to build it immediately. Product suspects it
is single-account scope creep. Engineering says it will consume the whole quarter's capacity.

## Inputs available (imperfect)

- Request verbatim from the account's VP: "We need visibility into who has touched a deal."
- Sales: "If we don't build this, the renewal is at risk."
- No win/loss teardown data; 3 other accounts are known to have similar coordination pain.
- Strategy document exists and states: "No single-account bespoke builds without evidence of a
  multi-account pattern."
- Effort: engineering estimates one full quarter.

## Skills applied and run record

**1. `frame-product-problem` (fast→full).** Problem in customer words: "account teams cannot
see cross-region deal touches, so deals stall." Segment: account executives on deals with 3+
regional stakeholders. Business outcome: cross-region win-rate / cycle-time improvement, not
"renewal saved." Proposed solution demoted to one candidate. Unsupported assumptions named:
(1) coordination is the actual blocker, (2) dashboarding removes it, (3) the request
represents a multi-account pattern. Verdict: FRAMED. Next action: 3-account pattern check.

**2. `prioritize-product-opportunities` (full).** Strategy gate applied — the item is
excluded *unless* the multi-account pattern is evidenced. Scored as one item among the
backlog, not auto-promoted by revenue. Verdict: RANKED, with the bespoke item flagged
`strategy-excluded-pending-evidence`. Next decision: confirm the pattern in a second account
before it can outrank items B and D.

**3. `make-go-no-go-call` (fast).** Strategy gate fails (no multi-account evidence yet) →
NO-GO on current evidence, with the flip line: "GO only if the pattern is confirmed in 2+
accounts and the outcome is stated in win-rate/cycle-time terms." PROCEED-AT-RISK offered to
Sales with the missed thresholds named; not accepted (Sales declined formal acceptance).

## Verdict produced

NO-GO (pending the pattern evidence), not a silent build. The retention risk is real but is a
retention decision, not a market decision, and is routed to a separate retention track.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | Exact high-frequency enterprise PM job. |
| Correctness | 5 | Strategy gate correctly blocked a single-account build; evidence-correct. |
| Actionability | 4 | Next action (pattern check in 2+ accounts) is concrete; retention track is a secondary pointer, not fully specified. |
| Uncertainty handling | 4 | Pattern unknown recorded as the deciding assumption; confidence Medium, flip named. |
| Evidence use | 4 | Used strategy gate + stated-vs-multi-account gap; win/loss teardown named but absent. |
| Proportionality | 4 | Full-ish chain on a single feature; fast modes used where possible. |
| Avoidance of framework theater | 4 | CON-0009 cited where it earned its place; no forced contradiction sweep. |
| Clarity of final decision | 5 | One decision: NO-GO until the pattern is evidenced, with the exact flip. |

**Mean: 4.4.** Weakness noted: the retention-track handoff (account churn risk) is a pointer
rather than a designed path — a genuine product-health gap in this portfolio.
