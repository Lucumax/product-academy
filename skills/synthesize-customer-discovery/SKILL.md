---
name: synthesize-customer-discovery
description: >-
  Produces a discovery synthesis from interview and observation notes: themes weighted by
  repeated observation versus loud anecdotes, per-segment breakdowns, and the open questions
  that separate a real problem from an enthusiastic story. Invoke after a round of customer
  discovery when the notes are unsorted, when interview enthusiasm contradicts usage behavior,
  or when "we talked to customers" is being offered as validation without a synthesis.
type: assist
version: 0.1.0
best_for:
  - "A round of interviews is done and the notes are unsorted"
  - "Interview enthusiasm contradicts usage behavior — which do you trust?"
  - "'We talked to customers' is offered as validation with no synthesis"
  - "Deciding what to test next: which problem has the strongest evidence, not the loudest advocate?"
  - "Preparing a discovery readout that separates observation from interpretation"
doctrine:
  - "PRN-0008 (discovery beats requests)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0011 (leading indicators beat lagging)"
  - "CON-0002 (discovery vs conviction)"
  - "09_tools/OPPORTUNITY_ASSESSMENT_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Discovery produces notes; notes are not evidence. This skill synthesizes raw discovery
material into a decision artifact that separates **what users actually said and did** from
**what the team hopes it means**, and — critically — weights **repeated observation** over
**loud anecdotes**. The output is a synthesis table that tells the team which problem to test
next, on the strength of evidence, not the charisma of the most recent interview.

Invoke it after a round of discovery when the notes are unsorted, when enthusiasm contradicts
behavior, or when "we talked to customers" is being waved around as validation without a
synthesis underneath it.

## Use when

- A round of interviews or observations is complete and the notes are unsorted.
- Interview enthusiasm contradicts usage behavior — the synthesis must resolve which to trust.
- "We talked to customers" is offered as validation without a synthesis.
- You must decide what to test next, on evidence rather than volume of anecdotes.
- You need a discovery readout that separates observation from interpretation.

## Do not use when

- The user wants to run the interviews — this is a synthesis skill, not a moderation guide.
- The user wants a transcript dump or verbatim archive — that is notes, not synthesis.
- There is no raw discovery material at all — the skill will flag the absence and name the
  cheapest discovery to run first; it cannot synthesize nothing.
- A reversible micro-decision — Fast mode or skip.

## Inputs

Required inputs:

- The raw material: interview notes, session recordings summaries, survey open-ends, support
  tickets, usability observations, with enough provenance (who, when, what context) to weight them.
- The number and profile of participants per source.

Optional inputs:

- Behavioral data for the same population (usage, cohorts) to cross-check stated vs actual behavior.
- The problem frame (from `frame-product-problem`) being tested.

## Missing-data behavior

- No provenance on a note → weight it as an anecdote, not an observation; mark it "unsourced."
- No behavioral cross-check → record the behavior gap as an open question; the synthesis
  cannot resolve stated-vs-actual without it.
- A single-source theme (one participant, one ticket) → mark as anecdote, never a repeated
  observation.

## Context classification

- **Early discovery (pre-PMF):** the synthesis feeds the problem frame and thesis; tolerate
  more anecdote weight, but label it.
- **Post-PMF refinement:** behavior cross-check is mandatory; stated enthusiasm alone cannot
  move the roadmap.
- **Contested readout (two stakeholders read it differently):** PRN-0014 applies — the
  synthesis names the discriminating test.

## Fast mode

Run for a quick synthesis on a small round. Three questions:

1. What were the raw observations — what did people actually say and do (not what you concluded)?
2. Which themes appeared in multiple, independent sources?
3. Which claim has the weakest evidence despite the most enthusiasm?

Output: the top 3 themes with a repeated-vs-anecdote label, the single most load-bearing
finding, and the one thing behavior contradicts. No full segment breakdown.

## Full mode

Adds: per-segment theme breakdowns, a repeated-vs-anecdote weighting table for every theme,
the stated-vs-actual comparison against behavioral data, and the open-questions list with the
cheapest test for each. Flags interviewer interference (leading questions inflating a theme).

## Method

One question at a time. "Unknown" answers are recorded as stated assumptions.

1. Inventory the raw material. List each source: interviews, surveys, tickets, observations, with participant counts and provenance. Separate first-person observation from secondhand summary.
2. Extract themes as claims. "Finance teams cannot see outstanding approvals" is a claim; "users want dashboards" is a solution, not a theme.
3. Weight by repetition. A theme in 3 of 5 interviews across two segments is a repeated observation; a theme in 1 emotional interview is a loud anecdote. Count independent sources, not mentions within one session.
4. Check stated vs actual. Where behavioral data exists for the same population, compare what users said they do with what usage shows. Interview enthusiasm contradicted by usage resolves toward behavior (E3/E4 beats E5 for "do" claims).
5. Break down by segment. Does the theme hold across segments, or is it one segment's pain? PRN-0014 — the aggregate can hide the truth.
6. Separate observation from interpretation. Every theme row gets a "what was observed" column and a "what we inferred" column. Inference is labeled, never folded in.
7. Name the open questions and the cheapest test for each. The top open question is usually the stated-vs-actual gap.
8. Produce the synthesis table and verdict.

## Evidence classification

Uses the shared taxonomy. Interview evidence (E5) establishes problem, intent, and language —
not behavior. Usability observation (E6) establishes whether users can use it. Behavioral
analytics (E3) and cohort evidence (E4) establish what users actually do. When they disagree,
behavior wins for "do" claims; the synthesis says so explicitly. A theme supported only by
E15 (unsourced assertion) is labeled unsupported.

## Output schema

```json
{
  "skill": "synthesize-customer-discovery",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "SYNTHESIS-READY | THIN-DISCOVERY | BEHAVIOR-CONTRADICTS",
  "themes": [
    {"theme": "...", "weight": "repeated | anecdote | unsupported",
     "segment": "...", "observed": "...", "inferred": "...",
     "evidence_types": ["E5", "E3"]}
  ],
  "stated_vs_actual": [{"stated": "...", "actual": "...", "discrepancy": "..."}],
  "open_questions": [{"question": "...", "cheapest_test": "...", "owner": "..."}],
  "confidence": "high | medium | low",
  "evidence_basis": ["E5", "E3", "E4"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `SYNTHESIS-READY` (enough independent observations to rank themes and the
  highest-evidence theme is testable) / `THIN-DISCOVERY` (too few independent sources — no
  theme reaches "repeated"; the output names the minimum discovery to run next) /
  `BEHAVIOR-CONTRADICTS` (a stated theme is contradicted by behavioral data; the synthesis
  says which to trust and why).
- **Theme weighting rule:** a theme is `repeated` only if it appears across 2+ independent
  sources with provenance *(rule of thumb — "independent" means different participants or
  datasets, not five quotes from one session)*; `anecdote` if it appears in 1–2 sources or
  lacks provenance; the table carries both the observation and the inference separately.
- **Confidence:** High when themes rest on multiple independent sources AND a behavior
  cross-check exists; Medium with partial behavioral data; Low when the synthesis is
  interview-only or provenance is thin.
- **Assumptions:** every "unknown," with effect.
- **What would change the verdict:** for THIN-DISCOVERY, more independent interviews/tickets;
  for BEHAVIOR-CONTRADICTS, a corrected measurement or a segment split resolving the discrepancy.
- **Next action:** the top open question's cheapest test, with an owner — usually the
  stated-vs-actual check or the highest-evidence theme's experiment.

### Worked example

Five interviews with ops leads: all five say "we'd be very disappointed without the scheduling
feature." Usage data for the same cohort shows scheduling used by 2 of 17 accounts in the last
30 days, and the three accounts that churned last quarter had scheduling active but unused.
Themes: "ops leads say scheduling is critical" — repeated observation (5/5, but stated intent);
"accounts that churn have scheduling provisioned but unused" — repeated observation from
behavioral data. Stated-vs-actual: enthusiasm contradicted by usage → verdict
`BEHAVIOR-CONTRADICTS`. Trust the usage: the synthesis recommends testing whether unused
scheduling signals a different problem (implementation gap, not feature demand) before
building more scheduling. Next action: 3 churned-account win/loss teardowns (E8) + a usage
cohort cut on active schedulers (E4).

## Failure modes

- **Loud anecdote as theme.** One vivid interview becomes the roadmap. Correction: the
  repeated-vs-anecdote rule — count independent sources, not emotion.
- **Interview enthusiasm as demand.** "Everyone we asked loved it." Correction: stated intent
  (E5) is not behavior (E3/E4); run the stated-vs-actual check.
- **No provenance.** Notes without who/when/context. Correction: weight them as anecdotes;
  "unsourced" is a label, not a deletion.
- **Aggregate blindness.** A theme that is really one segment's pain presented as universal. Correction: segment breakdown is mandatory in full mode.
- **Interpretation folded into observation.** "Users were frustrated" recorded as fact. Correction: separate "what was observed" from "what we inferred" per theme.
- **Discovery theater (PRN-0008).** "We talked to customers" used as validation with no synthesis. Correction: a readout without a weighted synthesis table is not validation.

## Reversal conditions

- A repeated theme is contradicted by a corrected measurement → re-weight.
- The stated-vs-actual gap is closed by a segment split (enthusiasm real in one segment) → re-grade by segment.
- New discovery material doubles the independent-source count on a theme → re-synthesize.
- The cheapest test on an open question resolves it → fold the result into the next synthesis.

## Composition hooks

- **before:** `frame-product-problem` (the problem hypothesis this synthesis tests).
- **after:** `pressure-test-product-thesis` (the highest-evidence theme becomes the thesis);
  `prioritize-product-opportunities` (synthesized themes are ranked opportunities);
  `design-product-experiment` (the top open question becomes the experiment);
  `assess-product-market-fit-health` (interview intent feeds the product-value dimension).
- **workflow:** product-bet (step 2).

## Related Skills

- `frame-product-problem` — defines the problem hypothesis this synthesis tests.
- `pressure-test-product-thesis` — turns the highest-evidence theme into a falsifiable bet.
- `design-product-experiment` — tests the top open question.
- `assess-product-market-fit-health` — uses interview intent as one input against behavior.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
