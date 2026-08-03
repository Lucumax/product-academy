# Demonstration 3 — Making a GO/NO-GO Call When the Pressure Says Launch

**One-paragraph version:** A payments product is pressured to launch a billing change to match
a competitor. The plain prompt answer is a pros/cons list where "protect the deals" survives.
The `make-go-no-go-call` skill classifies the launch as a one-way door, grades the missing
reliability evidence as `NO-EVIDENCE`, and returns `NO-GO` on the full launch as posed — with
a reversible path (phased, grandfathered, rehearsed rollback) instead.

**Install:** `npx skills add Lucumax/product-academy`

---

## 1. Scenario

A payments-integration product ("Anchor"). A competitor just shipped a similar feature; the
CEO and Sales want to launch now to protect position. The launch changes billing contracts —
it is not behind a feature flag.

## 2. Raw input

- Initiative: launch the new billing integration this quarter.
- Strategy: none written.
- Reliability evidence: no load test at expected peak; one SEV-2 last month; rollback path
  for the new billing contract never executed.
- Reversibility: the launch changes billing contracts (Type-1, one-way door).
- Competitive pressure: 3 deals in play, single-source claim, no loss baseline.

All of this is fictional fixture data.

## 3. Baseline prompt (no skill)

> "Should we launch now to match the competitor?"

## 4. Baseline output (shape)

A pros/cons list — competitive window vs reliability risk — ending with a hedge like "weigh
the risks." No reversibility classification, no reliability evidence bar, no decision
threshold. The natural reading ("we should launch to protect the deals") survives the list.

## 5. Skill invocation (copy-paste)

> Run the `make-go-no-go-call` skill. Initiative: launch the new billing integration this
> quarter. Strategy: none written. Evidence: no load test, one SEV-2 last month, rollback
> never executed. Effort: one quarter. This is one-way-door. Use full mode.

## 6. Skill-enabled output (the artifact)

```
Verdict: NO-GO on the full launch (as posed); PROCEED-AT-RISK surfaced and declined
Thresholds evaluated:
  strategy gate     — no written strategy (assumption; verdict weakened, not decisive)
  reversibility     — TYPE-1 (contract change; rollback untested; reversal latency exceeds
                       the damage window) -> premortem required
  evidence          — "works at peak": NO-EVIDENCE (no load test)
                       "we can support the billing change": NO-EVIDENCE (rollback never run)
                       "competitive window justifies risk": UNDER-SUPPORTED (3 deals in play,
                       single-source, no loss baseline)
  risk-adjusted     — expected value positive only if the no-evidence claims hold
Next action: phased, grandfathered rollout — load test + rehearsed rollback before the
  billing change touches existing contracts; re-run the gate with the evidence in hand.
```

## 7. Material differences

| | Baseline (prompt) | Skill-enabled |
|---|---|---|
| Verdict | "Weigh the risks" | `NO-GO` (as posed) + `PROCEED-AT-RISK` surfaced and declined |
| Reversibility | Not classified | Type-1 (one-way door); premortem required |
| Evidence | Not graded | Named `NO-EVIDENCE` / `UNDER-SUPPORTED` per load-bearing claim |
| Proceeding anyway | Silent | A distinct, labeled verdict with explicit risk acceptance required |
| Path forward | None | Phased, grandfathered, rehearsed-rollback design |

## 8. Limitations

- The "phased, grandfathered rollout" is advice produced by the reversibility skill's process
  budget, not a first-class artifact the pack drafts for you.
- The demo does not prove this beats an expert PM's judgment or a competitor's skill; it
  demonstrates that the chain produces a threshold-based verdict with a named flip.

## 9. Copy-paste command or prompt

Install once:

```bash
npx skills add Lucumax/product-academy --skill make-go-no-go-call
```

Then paste the skill invocation (section 5) into your agent with your own initiative,
strategy, and evidence.

## 10. Relevant skill and workflow links

- Skill: [`make-go-no-go-call`](https://lucumax.github.io/product-academy/skills/make-go-no-go-call/)
- Related: [`classify-decision-reversibility`](https://lucumax.github.io/product-academy/skills/classify-decision-reversibility/) — the Type-1 call
- Related: [`run-case-based-premortem`](https://lucumax.github.io/product-academy/skills/run-case-based-premortem/) — required for Type-1 commitments
- Related: [`audit-decision-evidence`](https://lucumax.github.io/product-academy/skills/audit-decision-evidence/) — the per-claim evidence grading
- Workflow: [`launch-gate`](https://lucumax.github.io/product-academy/skills/workflows/launch-gate/)
- Evidence taxonomy: [`_shared/SKILL_CONTRACT.md`](https://github.com/Lucumax/product-academy/blob/main/skills/_shared/SKILL_CONTRACT.md)
