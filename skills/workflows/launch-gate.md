# Workflow: Launch Gate

Decision: **are we ready to launch?** The terminal artifact is a GO / PAUSE / NO-GO launch
verdict with the thresholds met or missed and a named reversal authority.

## Entry conditions

- A feature, product, or AI capability is approaching exposure to users.
- The launch is significant enough to warrant a gate (customer-facing, resource-committing,
  or high-stakes). For a trivial flag-gated change, use the **fast variant**.

## Required inputs

- The launch scope: what is being exposed, to whom, on what timeline.
- The evidence the launch rests on (test results, pilot data, evaluation contract if AI).
- The written strategy and the launch plan.

## Skill chain and handoff artifacts

| Step | Skill | Handoff artifact to next step |
|---|---|---|
| 1 | `classify-decision-reversibility` | TYPE-1 / TYPE-2 / RECLASSIFIED-TYPE-1 + process budget + escalation level |
| 2 | `audit-decision-evidence` | Per-claim verdicts + overall GO/CONDITIONAL/NO-GO for the launch claims |
| 3 | `run-case-based-premortem` | Ranked launch-failure scenarios + mitigations + owners |
| 4 | `check-ai-evaluation-contract` (only when the launch includes AI behavior) | CONTRACT-COMPLETE / GAPPY / NO-CONTRACT |
| 5 | `align-stakeholders-on-decision` (if the launch is contested) | Alignment map: typed disagreements + decision rights |
| 6 | `make-go-no-go-call` | **Final verdict** (GO / PAUSE / NO-GO) + thresholds + next action |

## Mode gate

Run `classify-decision-reversibility` first (step 1). A TYPE-2, flag-gated launch uses the
**fast variant** and stops after the evidence check — do not run the premortem and alignment
steps on a reversible launch. TYPE-1, AI, and high-traffic launches go to the full variant.

## Fast variant

For reversible, low-stakes launches (a flag-gated feature with bounded downside):

- Step 1 in Fast mode (confirm TYPE-2); step 2 (evidence audit) in Fast mode; skip 3 unless
  the team is overconfident; skip 4 for non-AI; skip 5 unless there is visible disagreement;
  step 6 in Fast mode.
- Stop conditions: evidence `NO-GO` or a GAPPY/NO-CONTRACT AI verdict on a user-facing AI
  surface ends the workflow — do not launch a silent-failure surface without a rollback trigger.
- Time budget: one review session.

## Full variant

For TYPE-1 launches, AI launches, and high-traffic surfaces:

- All steps in Full mode. The premortem (3) is mandatory for TYPE-1.
- Step 4 is mandatory for any AI behavior: a `NO-CONTRACT` verdict is a launch blocker unless
  the surface is flag-gated with a named rollback authority.
- Step 5 runs when Sales/Product/Engineering disagree; the decision-rights assignment from the
  alignment map feeds step 6's escalation.

## Final output

- The launch verdict: GO (with the named rollback authority and monitoring owner) / PAUSE
  (with the blocker, owner, and re-review date) / NO-GO (with the threshold missed).
- The chained artifacts: reversibility class, evidence verdict, premortem monitoring plan,
  and (for AI) the evaluation-contract verdict.
- One sentence for leadership: the verdict, the confidence, and the single largest residual
  launch risk.

## Stop conditions

- AI surface with `NO-CONTRACT` and no rollback design → NO-GO for that surface.
- Evidence `NO-GO` on a one-way-door launch → NO-GO; do not proceed at risk on a Type-1
  without escalation.
- Premortem `NOT-DEFENSIBLE` → NO-GO until the top scenario is mitigated.
- PROCEED-AT-RISK without written acceptance and a named reversal owner → stop; the call is
  not made.

## Reversal

A GO launch keeps the premortem monitoring plan and the rollback trigger. If a signal fires,
execute the rollback and re-run the gate from step 2 with the incident as evidence.
