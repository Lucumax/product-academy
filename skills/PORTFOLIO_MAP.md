# Product Management Skill Portfolio Map

This map is the reverse index of the skill pack: it starts from the **job a PM
has today** and routes to the skill that produces the decision artifact. It is
the primary navigation document for both humans and agents.

Maturity levels: `stable` (verified across multiple eval scenarios),
`solid` (one eval pass + review), `new` (added this cycle, one eval pass),
`reference` (doctrine/tooling, not an executable skill).

## How to read

- **Job** — the PM task in plain language.
- **Trigger** — the situation that means "run this now."
- **Skill** — the entry point (`link`).
- **Artifact** — the concrete output you get back.
- **Workflow** — the end-to-end flow this job feeds or begins.
- **Maturity** — see above.
- **Gap** — what still needs work for this job.

## High-frequency PM execution

| Job | Trigger | Skill | Artifact | Workflow | Maturity | Gap |
|---|---|---|---|---|---|---|
| Frame a product problem | "We should build X" with no stated user problem or business outcome | [frame-product-problem](frame-product-problem/SKILL.md) | One-page problem frame: user problem, affected segment, business outcome, proposed solution, unsupported assumptions | Product Bet (entry) | solid | No standup guide for recurring discovery briefs |
| Synthesize customer discovery | Interviews done, notes unsorted, loud anecdotes vs repeated observations unresolved | [synthesize-customer-discovery](synthesize-customer-discovery/SKILL.md) | Discovery synthesis table: themes, evidence weight, segments, open questions | Product Bet (step 2) | solid | No interviewer-interference checklist yet |
| Prioritize opportunities | More candidate opportunities than capacity; RICE gives false precision | [prioritize-product-opportunities](prioritize-product-opportunities/SKILL.md) | Ranked opportunity list with exposed uncertainty + strategic dependencies, not a fake score | Product Bet (step 3) | solid | Needs a portfolio-grade (cross-team) variant |
| Design a product experiment | A change is proposed; "we'll see if it works" is the plan | [design-product-experiment](design-product-experiment/SKILL.md) | Experiment spec: metric, primary hypothesis, pre-committed interpretation & stop rules | Experiment Decision (entry) | solid | No full factorial / multi-variant extension |
| Align stakeholders on a decision | Sales/Product/Engineering disagree; meeting stuck on "what are we even arguing about" | [align-stakeholders-on-decision](align-stakeholders-on-decision/SKILL.md) | Disagreement map: facts / goals / incentives / risk tolerance / decision rights, with next action | Launch Gate (step 5) | solid | No decision-rights escalation template bundled |
| Diagnose product health | "Growth is fine but something feels off"; vanity metric as proof | [assess-product-market-fit-health](assess-product-market-fit-health/SKILL.md) | Health verdict (HEALTHY/DECAYING/…/UNMEASURED) with archetype-appropriate leading indicators | Product Health Review (entry) | stable | Funnel-level (activation->retention) drill-downs still thin |

## Differentiated evidence and judgment

| Job | Trigger | Skill | Artifact | Workflow | Maturity | Gap |
|---|---|---|---|---|---|---|
| Audit the evidence behind a decision | A call is being made/defended and its evidence has not been checked claim-by-claim | [audit-decision-evidence](audit-decision-evidence/SKILL.md) | Per-claim verdicts + overall GO/CONDITIONAL/NO-GO/LEARN | Product Bet (step 5), Experiment Decision (step 4) | stable | Fast mode still leans on a single scorer |
| Check whether a source/claim is credible enough | "This data proves it"; the source is an influencer post or an unverified claim | `audit-decision-evidence` (sub-mode) | Source credibility verdict (use/corrobate/ignore) per claim | — | stable | Deprecated `run-source-tier-check` routing maintained in index |
| Surface assumptions and live tensions | Two reasonable people are stuck; the decision feels too clean | [scan-contradictions-assumptions](scan-contradictions-assumptions/SKILL.md) | Assumption register (ranked by blast radius) + discovered tensions | Product Health Review (step 3) | solid | Academy CON-registry is still the only tension reference |
| Grade causal strength of "X caused Y" | Post-launch credit, experiment readout, expansion bets | [conduct-causal-confidence-review](conduct-causal-confidence-review/SKILL.md) | CAUSAL / CORRELATED / NARRATIVE / INSUFFICIENT-INFO + flip evidence | Experiment Decision (step 3) | stable | No Bayesian-input variant for quantitative teams |
| Run a premortem | Type-1 decision, overconfident team, pre-launch | [run-case-based-premortem](run-case-based-premortem/SKILL.md) | Ranked failure scenarios + exposure + DEFENSIBLE verdict | Product Bet (step 6), Launch Gate (step 3) | stable | Case-calibration step optional in fast mode only |
| Classify decision reversibility | Any significant commitment; "it's reversible" claims | [classify-decision-reversibility](classify-decision-reversibility/SKILL.md) | TYPE-1 / TYPE-2 / RECLASSIFIED-TYPE-1 + process budget | Launch Gate (entry) | stable | None material |
| Check an AI evaluation contract | AI feature pre-build / launch / model swap / post-incident | [check-ai-evaluation-contract](check-ai-evaluation-contract/SKILL.md) | CONTRACT-COMPLETE / GAPPY / NO-CONTRACT | Launch Gate (step 4) | stable | No contract lifecycle (re-review) workflow yet |
| Pressure-test a product thesis | Pre-funding, pre-commit, "we'll iterate until it works" | [pressure-test-product-thesis](pressure-test-product-thesis/SKILL.md) | FALSIFIABLE / BELIEF-PRESENTED-AS-THESIS / UNDERSPECIFIED | Product Bet (step 4) | stable | None material |
| Make the GO/NO-GO call | Budget, headcount, release slot, kill review | [make-go-no-go-call](make-go-no-go-call/SKILL.md) | GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK + thresholds | Product Bet (step 7), Launch Gate (step 6) | stable | PROCEED-AT-RISK acceptance is single-owner, not signed multi-party |

## Maturity legend

- `stable` — existed before this hardening cycle, verified against 2+ eval scenarios this
  cycle, and structurally reviewed.
- `solid` — authored or substantially rewritten this cycle, verified against 2+ eval
  scenarios, structurally reviewed; needs field repetition across a real cycle to earn
  `stable`.
- `reference` — doctrine/tooling consumed by skills, not a skill itself
  (see `../08_contradictions/`, `../09_tools/`, `../sources/registry.yaml`).

## Gaps remaining (by priority)

1. **Portfolio-grade prioritization.** `prioritize-product-opportunities`
   handles a single backlog; cross-team portfolio ranking (competing for
   scarce shared capacity) needs a group-PM variant.
2. **Interviewer-interference guidance.** `synthesize-customer-discovery`
   flags leading questions in evidence weight, but a training checklist for
   avoiding them is out of scope for a skill.
3. **Experiment power analysis.** `design-product-experiment` deliberately
   avoids statistical ceremony, but teams with traffic need a
   power/sample-size appendix to avoid underpowered tests.
4. **Evaluation-contract lifecycle.** `check-ai-evaluation-contract` is a
   point-in-time gate; a "contract drift" re-review cadence is a future skill.
5. **Launch readiness ≠ AI readiness.** The Launch Gate workflow composes
   `check-ai-evaluation-contract` when AI is involved; a generic
   launch-readiness checklist (support, docs, pricing, legal) is deliberately
   left to `09_tools/POST_LAUNCH_REVIEW_TEMPLATE.md` rather than duplicated.

## Workflows (see `workflows/`)

| Workflow | Entry job | Exit artifact |
|---|---|---|
| [product-bet](workflows/product-bet.md) | Frame a problem | GO/NO-GO verdict on funding a bet |
| [experiment-decision](workflows/experiment-decision.md) | Frame a problem / design an experiment | SCALE / ITERATE / STOP decision |
| [launch-gate](workflows/launch-gate.md) | Reversibility classification | GO / PAUSE / NO-GO launch verdict |
| [product-health-review](workflows/product-health-review.md) | Diagnose product health | Corrective experiment or investment decision |

## Deprecated / merged

| Old skill | Disposition | Replacement |
|---|---|---|
| `run-source-tier-check` | MERGE | `audit-decision-evidence` (sub-mode) |
