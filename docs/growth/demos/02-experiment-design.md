# Demo 2 — Product Experiment Design

One of three public demonstrations. It shows the `design-product-experiment` skill producing a
pre-committed experiment charter — the interpretation and stop rules exist *before* results.

## Raw scenario

A SaaS product wants to remove a two-step confirmation from checkout to increase completed
orders. Baseline completed-orders rate is 3.1% over the last 8 weeks. The team's plan is "we'll
see if it works."

## Ordinary baseline

> **Baseline prompt (illustrative shape):** "Design an experiment for removing the checkout
> confirmation step."
>
> **Generic output shape:** a description of A/B testing, a suggested metric (conversion), a
> vague "run it for a few weeks and see." No pre-committed threshold, no harm guardrail, no
> rollback trigger — the interpretation is left to whatever happens.

## Skill invocation

> Run the `design-product-experiment` skill. Change: remove the two-step confirmation.
> Assumption: it raises completed orders without raising returns or support. Primary metric:
> completed-orders rate, baseline 3.1%. Return the experiment charter.

## Resulting artifact (per the skill's contract)

```
Verdict: SPEC-READY
Spec:
  assumption: removing the confirmation raises completed orders without raising
    returns or support contacts
  primary_metric: completed-orders rate, direction up, baseline 3.1% (8 weeks)
  interpretation_rule:
    win  = +0.3pp completed orders AND returns ≤ +0.1pp AND support ≤ +5%
    null = within ±0.3pp
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

## What materially improved

The generic output leaves the decision to whatever happens; the skill pre-commits the
thresholds so the readout is a decision, not a negotiation. It adds a harm guardrail (returns,
support) so the team cannot optimize completed orders at the cost of returns, and a rollback
trigger per PRN-0007.

## Limitations

The skill deliberately avoids statistical machinery (power/sample-size) — teams with heavy
traffic still need that appendix. It cannot run the experiment. It does not claim superiority
over a carefully-written bespoke prompt; it standardizes the discipline so the artifact is
repeatable across agents and teams.
