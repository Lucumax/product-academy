# Workflow: Product Bet

Decision: **should we commit to this product bet?** The terminal artifact is a
GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK verdict.

## Entry conditions

- A new product, major feature, or market bet is proposed and will consume real resources
  (budget, headcount, a release slot).
- The bet is large enough that a wrong commitment costs more than this workflow costs to run.
- If the bet is small and reversible (a two-week pilot with a flag), use the **fast variant**;
  if it is a one-way door, use the **full variant** — see below.

## Required inputs

- The initiative as currently stated (even one sentence).
- The written product strategy (or a statement that none exists).
- Anyone who has already asserted evidence (interviews, market reports, demos).

## Skill chain and handoff artifacts

| Step | Skill | Handoff artifact to next step |
|---|---|---|
| 0 | `classify-decision-reversibility` | TYPE-1 / TYPE-2 class + process budget + mode gate for every subsequent step |
| 1 | `frame-product-problem` | Problem frame: user problem, segment, business outcome, solution, unsupported assumptions |
| 2 | `synthesize-customer-discovery` (if discovery material exists) | Synthesis table: weighted themes, stated-vs-actual, top open question |
| 3 | `prioritize-product-opportunities` (if competing with other bets) | Ranked list with uncertainty + the bet's rank and next decision |
| 4 | `pressure-test-product-thesis` | FALSIFIABLE / BELIEF / UNDERSPECIFIED verdict + falsification test spec |
| 4.5 | `check-ai-evaluation-contract` (only for AI bets) | CONTRACT-COMPLETE / GAPPY / NO-CONTRACT |
| 4.5 | `scan-contradictions-assumptions` (optional) | Assumption register; top assumptions feed the premortem |
| 5 | `audit-decision-evidence` | Per-claim verdicts + overall GO/CONDITIONAL/NO-GO/LEARN |
| 5.5 | `assess-product-market-fit-health` (only for launched bets being re-funded) | PMF/health verdict; confirms the bet is worth doubling |
| 6 | `run-case-based-premortem` | Ranked failure scenarios + DEFENSIBLE verdict + mitigations/owners |
| 7 | `make-go-no-go-call` | **Final verdict** + thresholds met/missed + next action |
| 7.5 | `align-stakeholders-on-decision` (only when the bet is contested) | Disagreement map + named decider and deadline, feeding the verdict's sign-off |

## Fast variant

For reversible bets (TYPE-2, bounded downside, pilot/flag-shaped):

- Step 1 (frame) in Fast mode; skip 2 unless discovery notes already exist; skip 3 unless
  the bet competes for a scarce slot; step 4 (thesis) in Fast mode; skip 4.5 for non-AI
  bets and for uncontested assumptions; step 5 (evidence audit) in Fast mode; skip 5.5
  unless re-funding a launched bet; skip 6 (premortem) unless the team is visibly
  overconfident; skip 7.5 unless the bet is contested; step 7 (GO/NO-GO) in Fast mode.
- Stop conditions: a `NO-GO` from the strategy gate or a Fast-mode evidence `NO-GO` ends the
  workflow immediately.
- Time budget: one working session.

## Full variant

For Type-1 bets and any bet where a Fast-mode verdict would be Low confidence on a
load-bearing claim:

- All steps in Full mode. The premortem (6) is mandatory for TYPE-1 (Framework 1).
- `classify-decision-reversibility` runs before step 5 to set the mode and the process budget.
- Step 7 must report which thresholds were met and missed, and any PROCEED-AT-RISK verdict
  requires explicit written acceptance plus a named reversal owner.

## Final output

- The `make-go-no-go-call` verdict artifact, plus the chained artifacts (frame, synthesis,
  thesis, evidence audit, premortem) as the decision's support.
- One sentence for leadership: the verdict, the confidence, and the single highest-risk
  assumption the bet still carries.

## Stop conditions

- Strategy gate `NO-GO` — stop immediately; no score overrides the strategy.
- Evidence audit `NO-GO` on a one-way door — stop; the bet is not defensible.
- `BELIEF-PRESENTED-AS-THESIS` with no falsification test scheduled — stop and fix the thesis
  before committing.
- PROCEED-AT-RISK without written acceptance — stop; the call is not made.

## Reversal

Any committed bet keeps its premortem monitoring plan: the ranked scenarios become the
monitoring cadence, and a fired early-warning signal triggers re-running the workflow from
step 5.
