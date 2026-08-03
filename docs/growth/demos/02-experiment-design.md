# Demonstration 2 — Pre-Committing What a "Win" Means Before the Results Exist

**One-paragraph version:** A SaaS product wants to remove a checkout confirmation step.
The plain prompt answer is "A/B test it for a few weeks and see." The `design-product-experiment`
skill returns a `SPEC-READY` charter with a win threshold, a null band, a harm guardrail, and
a rollback trigger — all written before the experiment runs, so the readout is a decision,
not a negotiation.

**Install:** `npx skills add Lucumax/product-academy`

---

## 1. Scenario

A SaaS product ("Panel") wants to remove a two-step confirmation from checkout to increase
completed orders. The team's plan is "we'll see if it works."

## 2. Raw input

- Change: remove the two-step confirmation from checkout.
- Assumption: it raises completed orders without raising returns or support contacts.
- Primary metric: completed-orders rate, baseline **3.1%** over the last 8 weeks.
- No pre-committed win threshold, no stop rules, no rollback plan.

All of this is fictional fixture data.

## 3. Baseline prompt (no skill)

> "Design an experiment for removing the checkout confirmation step."

## 4. Baseline output (shape)

A description of A/B testing, a suggested metric (conversion), and "run it for a few weeks
and see." No pre-committed threshold, no harm guardrail, no rollback trigger. The
interpretation is left to whatever happens after the results arrive.

## 5. Skill invocation (copy-paste)

> Run the `design-product-experiment` skill. Change: remove the two-step confirmation.
> Assumption: it raises completed orders without raising returns or support. Primary metric:
> completed-orders rate, baseline 3.1%. Return the experiment charter.

## 6. Skill-enabled output (the artifact)

```
Verdict: SPEC-READY
Spec:
  assumption: removing the confirmation raises completed orders without raising
    returns or support contacts
  primary_metric: completed-orders rate, direction up, baseline 3.1% (8 weeks)
  interpretation_rule:
    win  = +0.3pp completed orders AND returns <= +0.1pp AND support <= +5%
    null = within +-0.3pp
    harm = returns or support breach the thresholds
  stop_rules:
    early stop = 2 weeks if harm threshold breached
    minimum    = 6 weeks or 20k sessions before calling null
    null call  = 6 weeks with no signal
  competing_hypotheses: the A/B tool changed latency; seasonal checkout shift
  rollback: feature flag, trigger = harm threshold, authority = PM on call
Next action: hand the spec to engineering; after the readout, run
  conduct-causal-confidence-review using the baseline and competing hypotheses.
```

## 7. Material differences

| | Baseline (prompt) | Skill-enabled |
|---|---|---|
| Interpretation rule | None — "we'll see" | Pre-committed win/null/harm thresholds |
| Harm guardrail | None | Returns and support thresholds (cannot optimize orders at the cost of returns) |
| Rollback | None | Named trigger + authority (PRN-0007) |
| Competing hypotheses | None | Latency and seasonality named as checks |
| Readout | A negotiation | A decision against pre-committed rules |

## 8. Limitations

- The skill deliberately avoids statistical machinery (power/sample size); high-traffic teams
  still need that appendix.
- It cannot run the experiment.
- It does not claim superiority over a carefully-written bespoke prompt; it standardizes the
  discipline so the artifact is repeatable across agents and teams.

## 9. Copy-paste command or prompt

Install once:

```bash
npx skills add Lucumax/product-academy --skill design-product-experiment
```

Then paste the skill invocation (section 5) into your agent with your own change, metric, and
baseline.

## 10. Relevant skill and workflow links

- Skill: [`design-product-experiment`](https://lucumax.github.io/product-academy/skills/design-product-experiment/)
- Related: [`conduct-causal-confidence-review`](https://lucumax.github.io/product-academy/skills/conduct-causal-confidence-review/) — grades whether the change caused the outcome
- Related: [`make-go-no-go-call`](https://lucumax.github.io/product-academy/skills/make-go-no-go-call/) — the readout feeds the scale/iterate/stop decision
- Workflow: [`experiment-decision`](https://lucumax.github.io/product-academy/skills/workflows/experiment-decision/)
- Evidence taxonomy: [`_shared/SKILL_CONTRACT.md`](https://github.com/Lucumax/product-academy/blob/main/skills/_shared/SKILL_CONTRACT.md)
