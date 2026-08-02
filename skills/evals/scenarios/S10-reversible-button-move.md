# Scenario 10 — Reversible Decision With No Evidence

**Domain:** SaaS. **Type:** reversible, low-stakes — proportionality test.

## Context

A SaaS product wants to move a "Save" button from the header to the footer of the settings
page, behind a feature flag. The change is trivial, reversible, and low-stakes. The PM is
tempted to run the full evidence-governance ceremony "to be safe."

## Inputs available (imperfect)

- The change: button relocation, flag-gated, one-week rollback.
- No analytics on button-click rate from the header (the button is rarely used).
- No user-visible downside if wrong.

## Skills applied and run record

**1. `classify-decision-reversibility` (fast).** No irreversible dimension; reversal cost ≈ 0;
standard pattern (flag). Verdict: `TYPE-2`, High confidence. Process budget: analysis ≤ 10% of
implementation cost; decide at the team level.

**2. `make-go-no-go-call` (fast).** Strategy gate passes (no exclusion). Reversibility passes
(TYPE-2). Claims: impact claim has no evidence (no header click analytics) → but the decision
is reversible with bounded downside → CONDITIONAL/GO with the risk labeled negligible.
Verdict: `GO`, Medium confidence, with the note that the "no evidence" is a finding about
instrumentation, not a blocker. Next action: ship the flag, add a click event to the new
position, and let the flag's on/off comparison be the evidence (E3).

**3. Proportionality audit (self-check).** The full portfolio chain (frame → discovery →
thesis → evidence audit → premortem → GO/NO-GO) was NOT run. The correct entry was the
reversibility classification + fast GO/NO-GO, which the portfolio's fast/full contract
mandates. This scenario exists to test whether the fast path actually exists.

## Verdict produced

GO (flag-gated), with the correct process being two fast-mode steps, not the full chain. The
portfolio's proportionality rule (process must not exceed the risk of the decision) held.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The exact proportionality scenario. |
| Correctness | 5 | TYPE-2 + fast GO is the correct, unceremonious call. |
| Actionability | 5 | Ship the flag, instrument, compare — one clear action. |
| Uncertainty handling | 4 | No-analytics recorded as an instrumentation finding, not a blocker; Medium confidence. |
| Evidence use | 4 | The flag comparison becomes the E3 evidence; adequate for the stakes. |
| Proportionality | 5 | The fast path existed and was used; no ceremony. |
| Avoidance of framework theater | 5 | Nothing was performed; the two steps earned their place. |
| Clarity of final decision | 5 | GO with the flag, instrument, decide on the comparison. |

**Mean: 4.75.** Note: this scenario deliberately validates the fast/full contract. The risk is
that a PM or agent still runs the full chain out of habit — the fast modes exist but nothing
*enforces* them; the contract is advisory.
