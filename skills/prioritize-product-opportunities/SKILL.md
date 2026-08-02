---
name: prioritize-product-opportunities
description: >-
  Produces a ranked opportunity list that exposes uncertainty and strategic dependencies
  instead of mechanically calculating RICE. Invoke when the backlog has more candidate
  opportunities than capacity, when a "big customer asks for a bespoke feature" must be
  weighed against the rest of the roadmap, or when the team needs a defensible order that
  states its assumptions out loud. Returns a ranking with per-item uncertainty, strategic
  dependencies, and the next decision each item needs.
type: assist
version: 0.1.0
best_for:
  - "More candidate opportunities than capacity; a defensible order is needed"
  - "A large customer requests a bespoke feature — where does it really rank?"
  - "Quarterly roadmap selection that must expose its assumptions, not hide them behind a score"
  - "Two opportunities depend on the same scarce resource and one must yield"
  - "After discovery synthesis, converting themes into an ordered backlog"
doctrine:
  - "PRN-0002 (strategy is saying no)"
  - "PRN-0003 (cost of delay exceeds cost of imperfection)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 2 RICE-LM, decision rules)"
  - "09_tools/OPPORTUNITY_ASSESSMENT_TEMPLATE.md"
  - "09_tools/METRICS_TREE_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Prioritization is a decision, and RICE-style scores are a structured conversation dressed up
as measurement. This skill produces a **ranked opportunity list that exposes its own
uncertainty and its strategic dependencies** — so the order is defensible not because the
numbers are precise, but because the assumptions are visible.

Every ranked item carries: the evidence behind its reach/impact/confidence, the uncertainty
in that evidence (a range, not a point), and the strategic dependencies (which items share a
resource, which are prerequisites, which the strategy excludes). The output is an order plus
the next decision each item needs — not a number to be worshipped.

## Use when

- The backlog has more candidates than capacity and a defensible order is needed.
- A large customer requests a bespoke feature and it must be weighed against everything else.
- Quarterly roadmap selection must expose assumptions, not hide them behind a score.
- Two opportunities depend on the same scarce resource and one must yield.
- After discovery synthesis, converting themes into an ordered backlog.

## Do not use when

- The decision is already a go/no-go on a single initiative — use `make-go-no-go-call`.
- The user wants a portfolio investment-allocation model (cross-team capacity, ROI
  optimization) — this is single-backlog ranking; portfolio-level allocation is a gap
  documented in the portfolio map.
- A reversible micro-decision — ranking ceremony exceeds the value.
- There is only one candidate — a one-item list does not need ranking.

## Inputs

Required inputs:

- The candidate opportunities, each stated as a problem frame (see `frame-product-problem`) or
  at minimum with a segment and a business outcome.
- The capacity context: the scarce resource (people, platform, dependency, release slot).
- The written strategy, or a statement that none exists (recorded as an assumption).

Optional inputs:

- Evidence per opportunity: the taxonomy type and confidence behind reach, impact, feasibility.
- Effort per opportunity (relative scale is fine).
- Known dependencies between opportunities.

## Missing-data behavior

- No evidence for an opportunity's impact → score its confidence low and expose it, rather
  than padding the number. An opportunity with zero evidence is ranked on potential but
  flagged "evidence-gap."
- No strategy → the strategy gate is recorded as unmet; ranking proceeds but every item is
  flagged "strategy-unchecked."
- Effort unknown → use relative scale (S/M/L); never invent person-months.

## Context classification

- **Backlog triage (many small items):** Fast mode — a coarse rank with exposed uncertainty is enough.
- **Quarterly selection (committed capacity):** Full mode — strategy gate, dependencies, and
  per-item next decisions.
- **Large-customer bespoke request:** Full mode with an explicit check that the request is
  scored as one opportunity among many, not auto-promoted by revenue or loudness.

## Fast mode

Run for ordinary backlog decisions. Five steps:

1. List the candidates as problem frames (or note which lack a frame).
2. Apply the strategy gate: drop items the written strategy excludes (PRN-0002).
3. For each item, estimate reach × impact × confidence / effort as a RANGE, not a point.
4. Rank by the mid-point, then annotate the top and bottom with their biggest uncertainty.
5. Resolve ties by the item with the stronger evidence base.

Output: a ranked list with per-item range, the biggest uncertainty per top item, and the
single item that should be dropped first. No dependency map in fast mode.

## Full mode

Adds: the strategy gate with the PRN-0002 Exclusion Test (a strategy must name what it will
not do); a dependency map (which items share a resource, which are prerequisites); the
large-customer-request test (scored as one item, not auto-promoted); the RICE-LM multiplier
debate (Framework 2) as an explicit conversation; and per-item "next decision" statements.

## Method

One question at a time. "Unknown" answers are recorded as stated assumptions.

1. Inventory the candidates. Each must have a problem frame (segment + business outcome) or be flagged as lacking one.
2. Strategy gate (PRN-0002). Drop items the written strategy excludes; if no written strategy exists, record that and flag every item "strategy-unchecked."
3. For each item: what is the reach, impact, and confidence — as ranges? The confidence scale is 20% wild guess / 50% some data / 80% validated / 100% known (Framework 2). Where does each item sit, and on what evidence?
4. Effort: relative scale (S/M/L) or person-months.
5. Score a base range: (reach × impact × confidence) / effort. The multipliers (L/M/S strategic, timing, leverage) are a debate, not a calculation — argue them explicitly and record the debate.
6. Map dependencies: which items share a scarce resource, which are prerequisites for others, which the strategy excludes. A dependency can demote an item even with a great score.
7. The large-customer-request test: if the backlog's loudest item is a bespoke request, score it as one opportunity among many. Note its revenue value, but do not auto-promote it (a bespoke feature that serves one account is a retention decision, not a market decision — check CON-0009).
8. Rank: order by the mid-point, then adjust for dependencies, strategy, and evidence quality. Report the order with its uncertainty and the reason for each top-3 placement.
9. For each top item: what is the next decision it needs (test the assumption? run an experiment? go/no-go)?

## Evidence classification

Uses the shared taxonomy. Reach claims want market or analytics evidence (E9, E3); impact
claims want behavioral, cohort, or experiment evidence (E3, E4, E1); feasibility wants
operational evidence (E10, E11). Confidence labels (20/50/80/100) must be justified by the
evidence type — an impact estimate backed only by unsupported assertion (E15) is capped at
"wild guess" no matter how senior the proponent.

## Output schema

```json
{
  "skill": "prioritize-product-opportunities",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "RANKED | STRATEGY-UNCHECKED | INSUFFICIENT-FRAMES",
  "ranking": [
    {"opportunity": "...", "rank": 1, "reach_range": "...", "impact_range": "...",
     "confidence": "wild-guess | some-data | validated | known",
     "effort": "S | M | L", "biggest_uncertainty": "...",
     "dependency": "...", "next_decision": "...", "evidence_types": ["E3"]}
  ],
  "strategy_gate": {"status": "applied | no-strategy-stated", "excluded": ["..."]},
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E4"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `RANKED` (a defensible order with per-item uncertainty and dependencies
  exposed) / `STRATEGY-UNCHECKED` (ranking produced, but every item flagged because no written
  strategy exists — the order is provisional) / `INSUFFICIENT-FRAMES` (too many candidates
  lack problem frames to rank meaningfully; the output names which to frame first).
- **Ranking rule:** order by the score mid-point, adjusted for dependencies, strategy, and
  evidence quality. The rank is a hypothesis, not a measurement; the uncertainty ranges and
  next decisions are part of the artifact, not footnotes.
- **Confidence:** High when per-item scores rest on adequate evidence types and the strategy
  gate was applied; Medium when estimates rest on judgment; Low when candidates lack frames
  or evidence and the ranking is mostly potential.
- **Assumptions:** every "unknown," with effect.
- **What would change the verdict:** named evidence that moves an item's range (e.g. "the
  bespoke request becomes top-ranked only if a second and third account confirm the same
  workflow — currently it is single-account"); a strategy document arriving; a dependency
  resolving.
- **Next action:** per top item, its next decision; for the top item specifically, the test or
  go/no-go it needs before committing capacity.

### Worked example

Backlog: (A) bespoke "shared-deals dashboard" requested by one $2M account; (B) onboarding
time-to-first-value reduction; (C) API v2; (D) marketplace seller payout speedup. Strategy
written, excludes "single-account bespoke builds without a second-account pattern." Strategy
gate: A excluded unless evidence of a second-account pattern → A flagged. Scoring: B (reach 30
accounts, impact 15% activation lift, confidence 50% — one cohort signal E4, wild-guess
capped by no experiment) → mid-range high; D (reach 20 sellers, impact payout-friction, conf
80% — support + financial evidence E7/E11) → mid-range high with stronger evidence; C (high
effort, platform, low immediate reach) → demoted by dependency (blocks future items) not by
score. Ranked: B, D, A (conditional), C. A's next decision: confirm the pattern in a second
account before it can outrank D. The artifact exposes that A is a retention decision in a
market frame, and says so (CON-0009).

## Failure modes

- **RICE as measurement.** The score treated as truth. Correction: report ranges, expose the confidence labels, and treat the multiplier debate as part of the artifact.
- **Bespoke-request auto-promotion.** A $2M account's request jumps the queue because it is loud and has revenue attached. Correction: score it as one item; a single-account build is a retention decision, not a market bet.
- **Confidence inflation.** Every impact claim at 80%+ with no evidence. Correction: confidence is capped by the evidence type; an unsupported assertion is a wild guess by definition.
- **Strategy gate skipped.** No "no" written anywhere, so everything ranks. Correction: run the PRN-0002 Exclusion Test; a strategy that cannot name exclusions is not a strategy.
- **Dependency blindness.** Two items competing for the same engineer ranked as if independent. Correction: the dependency map is mandatory in full mode.
- **Aggregate priority theater.** A single ranked list where two segments have different top items. Correction: split the ranking by segment when the evidence disagrees (PRN-0014).

## Reversal conditions

- Evidence moves an item's range across a rank boundary → re-rank.
- A strategy document arrives or changes → re-run the gate.
- A dependency resolves (an engineer frees up, a prerequisite ships) → re-rank.
- The large customer escalates (threatens to leave) → that is a retention decision, handled
  via `align-stakeholders-on-decision` and `make-go-no-go-call`, not silent re-ranking.

## Composition hooks

- **before:** `frame-product-problem` (candidates must be framed); `synthesize-customer-discovery` (themes become ranked opportunities).
- **after:** `pressure-test-product-thesis` (the top opportunity's bet is made falsifiable);
  `make-go-no-go-call` (the top item's go/no-go); `design-product-experiment` (the top item's
  highest-risk assumption is tested); `assess-product-market-fit-health` (which opportunity
  restores a decaying dimension).
- **workflow:** product-bet (step 3).

## Related Skills

- `frame-product-problem` — candidates must carry a problem frame to rank.
- `synthesize-customer-discovery` — themes feed the candidate list.
- `make-go-no-go-call` — the top-ranked item's commitment verdict.
- `design-product-experiment` — tests the top item's highest-risk assumption.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
