---
name: frame-product-problem
description: >-
  Produces a problem frame for a product initiative: the user problem, the affected segment,
  the business outcome, the proposed solution, and the unsupported assumptions — separated so
  the team can disagree on the right thing before anyone builds the wrong thing. Invoke at the
  start of any initiative when "we should build X" appears without a stated problem or outcome,
  when a request arrives that is really a solution in disguise, or when a team cannot agree on
  what problem they are solving.
type: assist
version: 0.1.0
best_for:
  - "The start of any initiative: 'we should build X' with no stated problem or outcome"
  - "A customer request arrives that is a solution in disguise ('we need a dashboard')"
  - "The team cannot agree on what problem they are actually solving"
  - "Before discovery, thesis, prioritization, or experiment work — framing is the precondition"
  - "A bet is drifting: re-deriving what problem the existing solution was meant to solve"
doctrine:
  - "PRN-0005 (PM owns problem not solution)"
  - "PRN-0008 (discovery beats requests)"
  - "PRN-0002 (strategy is saying no)"
  - "09_tools/PRODUCT_THESIS_TEMPLATE.md"
  - "04_product_archetypes/"
license: CC BY 4.0
---

## Purpose

Most product failure begins as a framing failure: someone proposes a solution ("we need a
dashboard", "we should move to a freemium model", "we should build an AI copilot") and the
team argues about the solution before agreeing on the problem. This skill forces the
separation that prevents that: **user problem, affected segment, business outcome, proposed
solution, and unsupported assumptions** — each written separately, each allowed to be wrong
without dragging the others down.

The output is a one-page problem frame: a decision artifact that says what problem we are
solving, for whom, to what business end, and what we have not verified yet.

## Use when

- "We should build X" appears without a stated problem or outcome.
- A request arrives that is a solution in disguise.
- The team cannot agree on what problem they are solving.
- Before any discovery, thesis, prioritization, or experiment work.
- A running bet has drifted and the original problem needs re-deriving.

## Do not use when

- The problem is already crisp and agreed and the team wants a decision — skip framing and run
  `prioritize-product-opportunities` or `make-go-no-go-call` directly.
- The user wants a full PRD or spec — framing is the first page, not the document.
- A reversible micro-decision (button copy, layout) — framing ceremony exceeds the decision's value.
- The user wants the solution decided first — the skill will refuse to confirm a solution
  without a problem; that refusal is the point.

## Inputs

Required inputs:

- The initiative as it currently stands (even one sentence: "we should build X").
- Who is asking for it, and what triggered it (customer request, internal idea, competitor move, data signal).

Optional inputs:

- Any existing problem statements, discovery notes, or business-outcome language.
- The product archetype, if known.

## Missing-data behavior

- Arriving with only "we should build X" is normal — the skill extracts the problem by
  questioning. A problem that cannot be stated in customer terms is itself a finding.
- "Unknown" on the business outcome → the frame is marked incomplete; a frame without a
  business outcome cannot feed prioritization.
- "Unknown" on the segment → the frame names the segment as the first discovery question.

## Context classification

- **Pre-discovery:** the frame defines what discovery must test — the problem hypothesis.
- **Pre-prioritization:** the frame must be complete enough to rank (has a segment and a
  business outcome).
- **Pre-build:** the frame is checked against the thesis template — a solution-only framing is
  a red flag (PRN-0005).

## Fast mode

Run for ordinary, reversible decisions. Three questions:

1. What is the user problem, in the customer's words (not the feature's)?
2. What is the business outcome we expect if we solve it well?
3. What is the proposed solution, stated as a means not an end?

Output: a three-line frame (problem / outcome / solution) with a flag for anything unsupported.
If the problem cannot be stated, the output is "problem not yet stated" plus the single
discovery question to ask next. No assumptions sweep in fast mode.

## Full mode

Adds the affected segment (with the pain's severity and frequency), the unsupported-assumption
list (each assumption tied to the claim it supports), the "what would make this frame wrong"
check, and the strategy-alignment check (does this frame serve the written strategy, PRN-0002?).

## Method

One question at a time. "Unknown" answers are recorded as stated assumptions.

1. What is being proposed? Capture the initiative as stated, including any features or solutions already implied.
2. What problem does it solve, in the customer's words? Ask "What is the job the user is trying to do, and what is getting in the way?" Push past solution language — "we need a dashboard" is a solution; the problem might be "finance teams cannot see who has outstanding approvals."
3. Who is the affected segment? Name the specific customers, with severity and frequency of the pain. A segment of "everyone" is a warning.
4. What is the business outcome? Name the measurable business result expected if the problem is solved well (revenue, retention, cost, activation). Without one, the frame cannot be prioritized.
5. What is the proposed solution? State it as a means, not an end. If the solution was the original ask, demote it to one candidate.
6. What is unsupported? List every assumption: about the problem, the segment, the outcome, the solution's feasibility. Each becomes a discovery or test target.
7. What would make this frame wrong? Name the evidence that would falsify the problem, the segment, or the outcome.
8. Does it serve the strategy? Apply PRN-0002 — does this frame fit what the strategy says we will do (and will not do)? If it is excluded, say so.

## Evidence classification

Uses the shared taxonomy. A frame is a hypothesis container, so its inputs are mostly E15
(unsupported assertions) and E5 (interview/problem evidence) at this stage — that is expected
and fine. The frame's job is to *mark* what is unsupported so later skills (discovery
synthesis, thesis pressure-test, experiment design) convert E15 → E3/E4/E5 evidence. Do not
demand evidence for a frame; demand that it *names what lacks evidence*.

## Output schema

```json
{
  "skill": "frame-product-problem",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "FRAMED | PARTIALLY-FRAMED | PROBLEM-NOT-STATED",
  "frame": {
    "user_problem": "...",
    "affected_segment": "...",
    "business_outcome": "...",
    "proposed_solution": "..."
  },
  "unsupported_assumptions": [
    {"statement": "...", "supports": "problem | segment | outcome | solution"}
  ],
  "strategy_alignment": "aligned | excluded | no-strategy-stated",
  "confidence": "high | medium | low",
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `FRAMED` (problem, segment, outcome, and solution all stated, with assumptions
  named) / `PARTIALLY-FRAMED` (some slots filled, the missing ones named) /
  `PROBLEM-NOT-STATED` (the initiative is solution-only and the problem could not be extracted;
  the output is the single next discovery question).
- **Confidence:** High when the frame survives a "why" challenge on each slot and the
  assumptions are explicit; Medium when slots rest on stated assumptions; Low when the frame
  is mostly inference.
- **Evidence basis:** the taxonomy types the frame's claims rest on (usually E5/E15 at this stage).
- **Assumptions:** every "unknown," with effect.
- **What would change the verdict:** evidence that falsifies the problem, the segment, or the
  outcome — each named in the frame.
- **Next action:** the single highest-leverage owner-able step for the frame's state: for
  `PROBLEM-NOT-STATED`, run the named discovery question with a named owner; for
  `PARTIALLY-FRAMED`, fill the named missing slot; for `FRAMED` with unsupported assumptions,
  run the discovery or thesis step that tests the frame's highest-risk assumption (usually
  the problem assumption). One action, one owner, one date — not a menu.

### Worked example

Initiative: "Enterprise sales wants us to build a shared-deals dashboard this quarter."
Framing: problem — "sales leads cannot see who has touched a deal across regions, so deals
stall for lack of coordinated follow-up" (customer words, not the feature). Segment — account
executives on deals with 3+ stakeholders across regions, pain severity high at month-end, high
frequency. Business outcome — 5-point win-rate improvement on cross-region deals, or a 20%
reduction in deal cycle time. Solution — a shared-deals dashboard (demoted to one candidate).
Unsupported — "cross-region coordination is the actual blocker" (problem assumption),
"dashboarding is what removes it" (solution assumption), "win-rate is elastic to coordination"
(outcome assumption). Verdict: FRAMED. Next action: discovery — 5 win/loss teardowns + 4
interviewer sessions to convert the problem assumption into E8/E5 evidence before prioritizing.

## Failure modes

- **Solution-locked framing.** The team only ever discusses the dashboard, never the problem. Correction: demote the solution to one candidate; the problem is the agreement target.
- **Vague segment.** "Everyone," "any business." Correction: a segment is falsifiable — name severity, frequency, and the population.
- **Outcome-less frame.** A problem with no business outcome cannot be prioritized. Correction: name the measurable outcome or the frame stays incomplete.
- **Feature-first language.** "Users need a way to X" stated as the problem. Correction: restate in job-to-be-done terms — what is the user trying to accomplish and what blocks it?
- **Assumption hiding.** A frame that lists no unsupported assumptions. Correction: every frame has them; an empty list is a denial, not a fact.
- **Framing theater for reversible calls.** A ceremony for a button move. Correction: Fast mode or skip; framing pays for itself on bets, not on tweaks.

## Reversal conditions

- Discovery or evidence falsifies the problem → the frame is re-derived (problem changes).
- The segment turns out to have no pain severity/frequency → reframe or drop.
- The business outcome is found unmeasurable → replace with a measurable proxy.
- The strategy excludes the frame → stop; the frame is out of scope.

## Composition hooks

- **before:** none (entry skill); optionally `classify-decision-reversibility` for high-stakes bets.
- **after:** `synthesize-customer-discovery` (test the problem hypothesis);
  `pressure-test-product-thesis` (make the frame a falsifiable bet);
  `prioritize-product-opportunities` (rank the framed opportunity);
  `design-product-experiment` (test the highest-risk assumption);
  `audit-decision-evidence` (audit the claims the frame generates).
- **workflow:** product-bet (step 1), experiment-decision (step 1).

## Related Skills

- `synthesize-customer-discovery` — the problem hypothesis's first test.
- `pressure-test-product-thesis` — turns the frame into a falsifiable bet.
- `prioritize-product-opportunities` — ranks the framed opportunity against the backlog.
- `design-product-experiment` — tests the frame's highest-risk assumption.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
