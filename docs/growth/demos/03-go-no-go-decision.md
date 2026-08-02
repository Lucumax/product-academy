# Demo 3 — High-Stakes GO/NO-GO Decision

One of three public demonstrations. It shows the evidence-governance chain turning a
competitive-pressure launch into a defensible call.

## Raw scenario

A payments-integration product. A competitor just shipped a similar feature; the CEO and
Sales want to launch now to protect position. But: no load test at expected peak, one SEV-2
last month, and the rollback path for the new billing contract has never been executed. The
launch changes billing contracts — it is not a feature flag.

## Ordinary baseline

> **Baseline prompt (illustrative shape):** "Should we launch now to match the competitor?"
>
> **Generic output shape:** a pros/cons list — competitive window vs reliability risk; a
> hedge like "weigh the risks"; no reversibility classification, no reliability evidence bar,
> no decision threshold. The natural reading of the situation ("we should launch to protect
> the deals") survives the list.

## Skill invocation

> Run the `make-go-no-go-call` skill. Initiative: launch the new billing integration this
> quarter. Strategy: none written. Evidence: no load test, one SEV-2 last month, rollback
> never executed. Effort: one quarter. This is one-way-door. Use full mode.

## Resulting artifact (per the skill's contract)

```
Verdict: NO-GO on the full launch (as posed); PROCEED-AT-RISK surfaced and declined
Thresholds evaluated:
  strategy gate     — no written strategy (assumption; verdict weakened, not decisive)
  reversibility     — TYPE-1 (contract change; rollback untested; reversal latency exceeds
                       the damage window) → premortem required
  evidence          — "works at peak": NO-EVIDENCE (no load test)
                       "we can support the billing change": NO-EVIDENCE (rollback never run)
                       "competitive window justifies risk": UNDER-SUPPORTED (3 deals in play,
                       single-source, no loss baseline)
  risk-adjusted     — expected value positive only if the no-evidence claims hold
Next action: phased, grandfathered rollout — load test + rehearsed rollback before the
  billing change touches existing contracts; re-run the gate with the evidence in hand.
```

## What materially improved

The generic output would have let the competitive-window argument carry the day. The skill
classified the decision as effectively irreversible (TYPE-1), named the missing reliability
evidence as NO-EVIDENCE rather than a shrug, surfaced PROCEED-AT-RISK as a *distinct, labeled*
verdict (not a silent "we're going anyway"), and produced a reversible design (phased,
grandfathered, rehearsed rollback) as the path forward.

## Limitations

The "phased, grandfathered rollout" is advice produced by the reversibility skill's process
budget, not a first-class artifact the pack drafts for you. The demo does not prove this beats
an expert PM's judgment or a competitor's skill; it demonstrates that the chain produces a
threshold-based verdict with a named flip.

## How to run these yourself

All three demos are the eval-scenario fixtures (`skills/evals/scenarios/`) run through the
skill contracts. Run them with your own agent: paste the "Skill invocation" prompt, and the
skill will ask the remaining questions.
