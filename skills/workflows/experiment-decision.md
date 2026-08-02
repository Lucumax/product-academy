# Workflow: Experiment Decision

Decision: **what do we do with this experiment?** The terminal artifact is a
SCALE / ITERATE / STOP decision grounded in a pre-committed interpretation rule and a
post-hoc causal check.

## Entry conditions

- A change was proposed and an experiment was run (or is about to be run) to test an
  assumption.
- The readout will commit capacity (scale to all users), trigger iteration, or stop the work.
- If the change is small and reversible with a clear metric, use the **fast variant**; if it
  is an AI feature, a high-traffic surface, or a bet that will scale, use the **full variant**.

## Required inputs

- The change tested, one sentence.
- The assumption it tested, and the primary metric.
- The pre-committed interpretation and stop rules (or a statement that none were set — which
  is itself a finding the workflow surfaces).

## Skill chain and handoff artifacts

| Step | Skill | Handoff artifact to next step |
|---|---|---|
| 1 | `frame-product-problem` (if not yet framed) | Problem frame; the assumption under test |
| 2 | `design-product-experiment` (if not yet designed) | Experiment spec: hypothesis, metric, baseline, interpretation rule, stop rules, rollback |
| 3 | `conduct-causal-confidence-review` | CAUSAL / CORRELATED / NARRATIVE verdict on "the change caused the outcome" |
| 4 | `audit-decision-evidence` | Evidence adequacy verdict for the scale/iterate/stop decision |
| 5 | Decision: SCALE / ITERATE / STOP (fast), or `make-go-no-go-call` for a scaling bet | **Final decision** + next action + reversal conditions |

## Mode gate

Run `classify-decision-reversibility` first. If the change is TYPE-2 (reversible, bounded
downside), use the **fast variant** below and stop — do not run the full chain on a
flag-gated change. Escalate to the full variant only for AI surfaces, high-traffic surfaces,
or bets that will scale irreversibly.

## Fast variant

For reversible, ordinary experiments:

- Step 2 in Fast mode if the spec is missing; step 3 (causal review) in Fast mode; skip step
  4 unless the scaling decision is material.
- Decision rule: the pre-committed interpretation rule decides. Win threshold met and
  causal review says at least CORRELATED → SCALE (with rollback). Null → STOP or ITERATE.
  Harm threshold fired → STOP and roll back.
- Stop conditions: harm threshold fired → STOP immediately and execute rollback; this ends
  the workflow.
- Time budget: one readout session.

## Full variant

For AI features, high-traffic surfaces, and bets that will scale to most users:

- All steps in Full mode. The causal review (3) runs the segment test and alternative
  explanations; the evidence audit (4) grades the scaling decision's claims.
- A SCALE verdict on a Type-1 or high-traffic surface requires the rollback plan from the
  spec to be live and owned.
- For AI features, the readout feeds back into `check-ai-evaluation-contract`: a null or harm
  result may mean the contract's thresholds or rollback triggers need revising, not just the
  feature.

## Final output

- The decision: SCALE (with the rollback plan and the segment it scales to) / ITERATE (with
  the specific change to make and the re-test) / STOP (with the evidence that says stop).
- The causal verdict and the pre-committed rule it was judged against.
- One sentence for leadership: the decision, the confidence, and the metric that carried it.

## Stop conditions

- Harm threshold fired → STOP and rollback; do not re-interpret.
- Causal review returns NARRATIVE or INSUFFICIENT-INFO on a bet the team wants to scale →
  STOP scaling; run the discriminating test instead.
- No pre-committed interpretation rule existed → the readout is void as a decision; the
  output is the rule that should have been set, and the experiment is re-run or re-interpreted
  with the rule.

## Reversal

A SCALE decision keeps the rollback trigger from the spec. If the trigger fires, roll back
and re-run the workflow from step 3 with the trigger as a fact.
