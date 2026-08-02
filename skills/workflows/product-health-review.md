# Workflow: Product Health Review

Decision: **is this product healthy, and what is the corrective investment?** The terminal
artifact is a health verdict plus a prioritized corrective action (experiment, investment
decision, or pivot).

## Entry conditions

- A scheduled health review (quarterly PMF/health review) or an ad-hoc "something feels off"
  trigger.
- A vanity metric is being cited as proof of health.
- Growth is fine but engagement, retention, or liquidity is quietly eroding.

## Required inputs

- The product archetype (see `assess-product-market-fit-health` context table).
- Current values and trends for the archetype's leading dimensions (over 3+ periods where possible).
- Lagging indicators (revenue, retention) for the Innovator's Dilemma check.

## Skill chain and handoff artifacts

| Step | Skill | Handoff artifact to next step |
|---|---|---|
| 1 | `assess-product-market-fit-health` (archetype-adaptive) | Health verdict (HEALTHY/DECAYING/NEVER-ACHIEVED/UNMEASURED) + per-dimension status |
| 2 | `synthesize-customer-discovery` (if interview/usage evidence is contested) | Stated-vs-actual comparison for the contested dimension |
| 3 | `scan-contradictions-assumptions` | Assumption register for the health readout; top assumptions named |
| 4 | `design-product-experiment` (for a DECAYING/UNMEASURED dimension) | Corrective experiment spec |
| 5 | `prioritize-product-opportunities` (for investment decisions) | Ranked corrective opportunities with uncertainty |
| 6 | `make-go-no-go-call` (for an investment or pivot decision) | **Final decision** on the corrective investment |

## Mode gate

Start with the health assessment in Fast mode (top 2–3 dimensions). Only escalate to the
full variant when the fast verdict is DECAYING, NEVER-ACHIEVED, UNMEASURED on a load-bearing
dimension, or a pivot is on the table. A HEALTHY fast verdict ends the workflow — do not run
the contradiction scan and corrective-experiment steps on a healthy product.

## Fast variant

For a quarterly pulse where the verdict is likely HEALTHY:

- Step 1 in Fast mode (top 2–3 dimensions); skip 2 unless interview and usage data conflict;
  skip 3; step 4 or 5 only if a dimension is decaying; step 6 only if an investment decision
  is pending.
- Stop conditions: verdict HEALTHY with no decaying dimension → the review ends with the next
  review date set.
- Time budget: half a day.

## Full variant

For any DECAYING / NEVER-ACHIEVED / UNMEASURED verdict, or when a pivot is on the table:

- All steps in Full mode. Step 1 assesses all applicable dimensions; step 2 runs the
  stated-vs-actual check when the readout is contested (PRN-0014); step 3 exposes the
  assumptions behind the health claims.
- A DECAYING verdict produces a corrective experiment spec (step 4) tied to the decaying
  dimension, so the next review can measure the correction.
- A NEVER-ACHIEVED verdict routes to `frame-product-problem` + `pressure-test-product-thesis`
  — the product needs a different problem, not maintenance.

## Final output

- The health verdict with per-dimension status and confidence.
- The corrective action: for DECAYING — the experiment spec and owner; for UNMEASURED — the
  measurements to stand up and the owner; for NEVER-ACHIEVED — the reframe decision.
- The next review date and the monitoring cadence.
- One sentence for leadership: the verdict, the confidence, and the single dimension most at
  risk.

## Stop conditions

- NEVER-ACHIEVED → the corrective workflow is not maintenance but reframing; stop the
  "optimize the feature" track and start problem re-derivation.
- A DECAYING dimension with no measurement standing up to measure it → UNMEASURED for that
  dimension; the finding names the measurement first.
- The corrective experiment's harm threshold fires → stop the experiment and roll back.

## Reversal

The review's corrective experiment keeps its pre-committed interpretation and rollback rules
(step 4 artifact). The next scheduled review re-runs the workflow from step 1 with the
experiment's result as input.
