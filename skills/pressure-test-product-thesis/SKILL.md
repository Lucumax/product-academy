---
name: pressure-test-product-thesis
description: >-
  Produces a verdict on whether a stated product thesis is falsifiable and coherent — and
  whether it is actually a thesis or a belief dressed up as one. Invoke before committing
  resources to a bet, before a funding or board presentation, whenever someone says "the plan"
  without being able to say what would disprove it, or when the team cannot agree on what
  success would look like. Uses the Theranos failure pattern (CASE-0019) as the reference failure.
type: assess
version: 0.2.0
best_for:
  - "New product or major initiative: verdict before resources are committed"
  - "Pre-funding / pre-board: is the story we are about to tell a testable bet?"
  - "A bet that has been running for a while: has it drifted into belief?"
  - "Pivot or reversal decision: is the incumbent thesis falsifiable at all?"
  - "Stakeholder disagreement: two camps cannot articulate what would settle the bet"
doctrine:
  - "PRN-0002 (strategy is saying no)"
  - "PRN-0005 (PM owns problem not solution)"
  - "PRN-0008 (discovery vs requests)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "CASE-0019 (Theranos)"
  - "09_tools/PRODUCT_THESIS_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

This skill answers one question: **is the thing being presented as a product thesis actually
a testable bet, or is it a belief that cannot be disproven?** A thesis is a claim about a
specific customer, a specific problem, and a specific mechanism that you commit to testing. A
belief is a claim you are not willing to put at risk. The distinction matters because beliefs
quietly absorb resources while producing no information — the Theranos pattern (CASE-0019) is
what happens when a thesis can never be falsified.

Invoke it when a decision is about to be made on the strength of a claim: committing budget,
hiring against it, presenting to the board, or doubling down on an existing bet. Do NOT
invoke it when the user wants to write a thesis document — point them to
`09_tools/PRODUCT_THESIS_TEMPLATE.md`. Do NOT invoke it for a reversible feature tweak; the
cost of the discipline outweighs the value.

## Use when

- A new product or major initiative needs a verdict before resources are committed.
- Pre-funding / pre-board: is the story a testable bet?
- A running bet may have drifted into belief.
- A pivot or reversal decision: is the incumbent thesis falsifiable at all?
- Two camps cannot articulate what would settle their disagreement.

## Do not use when

- The user wants to write a thesis document — use the thesis template.
- The user wants a full strategy review — that is a portfolio decision; this is a single-claim diagnostic.
- The decision is a reversible, low-stakes feature tweak.
- The thesis has already been pressure-tested and committed with a live, monitored
  falsification test — the job is then `assess-product-market-fit-health`, not another thesis check.

## Inputs

Required inputs:

- The thesis as currently stated (verbatim if possible — one or two sentences).
- What evidence currently exists for it, and where it came from (discovery, pilots, market reports, demos, executive belief).
- What decision is pending on the strength of this thesis.

Optional inputs:

- Who holds the technical or domain fluency to verify the core claim.
- The reversibility class of the bet.

## Missing-data behavior

- Arriving with only "we think X will be big" still works — the method exposes the thesis as
  underspecified, which is a verdict in itself.
- Refusing to state a falsification condition → record the refusal and return
  `BELIEF-PRESENTED-AS-THESIS`; that is the point of the skill.
- "Unknown" on the falsification condition → the verdict cannot be `FALSIFIABLE-THESIS`
  regardless of how confident everyone feels.

## Context classification

- **TYPE-1, high-stakes bet** (funding, major commitment): Full mode — falsification test must
  be written, scheduled, and owned with a pre-committed threshold.
- **TYPE-2, reversible bet** (a feature or pilot with bounded downside): Fast mode — is there
  a falsification condition at all? If yes and cheap to test, the bet is live.
- **Pre-funding / board:** Full mode — presentation-derived evidence is the specific hazard.

## Fast mode

Run for reversible or ordinary bets. Four questions:

1. State the thesis as a claim: "We bet that [segment] has [problem], that [mechanism] solves it, and that [outcome] follows."
2. What would disprove it? Name a measurable outcome and a timeframe.
3. Are you willing to run that test? Is there a scheduled test with a pre-committed threshold?
4. What is the evidence, really? Does any of it come from customer investigation (discovery) rather than demos or internal conviction?

Provisional verdict: `FALSIFIABLE-THESIS` (specific claim + measurable disproof + scheduled
test + pre-committed threshold) / `BELIEF-PRESENTED-AS-THESIS` (specific claim but no disproof
or no scheduled test) / `UNDERSPECIFIED` (a slot is missing or too vague). Confidence capped
at Medium. Next action: fill the missing slot or write the falsification test.

## Full mode

Adds to fast mode:

1. Verify the claim slots precisely (segment, problem, mechanism, outcome) with measurable descriptors.
2. Test the falsification condition: does it name a number, a behavior, and a timeframe? A condition that cannot fail is not a condition.
3. Verify the test is scheduled with a named owner and a pre-committed GO/NO-GO threshold set BEFORE the results arrive.
4. Classify the evidence as discovery-derived (from actual customer investigation, PRN-0008) vs presentation-derived (demos, prestige, conviction). The Theranos failure was discovery replaced by presentation.
5. Check technical falsifiability: who in the decision chain can technically challenge the core claim, and are they empowered to raise it? No one → CASE-0019 technical-fluency flag.
6. Apply PRN-0002: if this thesis is right, what will we explicitly not do? Push for at least three concrete exclusions.
7. Record every "unknown" with its effect on the verdict.

## Method

Work through these questions in order. Ask the user directly; do not infer answers. "Unknown"
answers are recorded as stated assumptions and the process continues.

1. State the thesis as a claim. Complete: "We bet that [customer segment] has [problem], that [mechanism] solves it, and that the world changes in [specific way] if we are right." If any slot cannot be filled, the claim is underspecified and you can stop early.
2. What would disprove it? This is the core question. A defensible answer names a measurable outcome and a timeframe. "We'll just keep iterating" is not an answer.
3. Are you willing to run that test? What is the experiment, who runs it, when does it start, and what pre-committed threshold turns its result into a GO or NO-GO decision? A test that cannot fail, or whose threshold is set after results arrive, is not a test.
4. What is the evidence, really? Classify it: discovery-derived (actual customer investigation, PRN-0008) or presentation-derived (demos, fundraising narrative, prestige endorsement)?
5. Who can technically falsify it? Is there a person with enough technical fluency to challenge the core claim, and are they empowered to raise it? If no one, flag the CASE-0019 technical-fluency failure.
6. What does this thesis say no to? Apply PRN-0002. Push for at least three concrete exclusions — a market, a segment, a use case, a platform, a channel.
7. Record assumptions. Any "unknown" goes into the verdict as a stated assumption with the confidence it carries.

## Evidence classification

Uses the shared taxonomy. Discovery-derived evidence (E5 interviews, E6 usability, E3/E4
behavioral and cohort evidence) is the base that can make a thesis credible.
Presentation-derived evidence (demos, prestige, board endorsement) is E15-grade for
validation purposes — it can buy attention, not truth. A thesis whose evidence is entirely
presentation-derived is `BELIEF-PRESENTED-AS-THESIS` regardless of how polished the demo is.

## Output schema

```json
{
  "skill": "pressure-test-product-thesis",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "FALSIFIABLE-THESIS | BELIEF-PRESENTED-AS-THESIS | UNDERSPECIFIED",
  "confidence": "high | medium | low",
  "claim_slots": {"segment": "...", "problem": "...", "mechanism": "...", "outcome": "..."},
  "falsification_condition": "...",
  "test_status": "scheduled-and-owned | scheduled-no-owner | none | threshold-after-results",
  "evidence_basis": ["E5", "E3"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** one of
  - `FALSIFIABLE-THESIS` — specific claim; disproof condition stated in measurable terms; test scheduled with a named owner; pre-committed GO/NO-GO threshold; at least one piece of discovery- or experiment-derived evidence.
  - `BELIEF-PRESENTED-AS-THESIS` — specific claim but no disproof condition, or no scheduled test, or no pre-committed threshold, or entirely presentation-derived evidence. The Theranos pattern: the thesis is being maintained, not tested.
  - `UNDERSPECIFIED` — one or more of the four slots is missing or too vague to measure.
- **Confidence:** High when every check holds with no material "unknowns"; Medium when one or
  two hold by a margin; Low when the verdict rests on assumptions the user could not verify.
- **Assumptions:** every "unknown," listed with effect.
- **What would change the verdict:** the specific evidence that flips the call — for
  `BELIEF-PRESENTED-AS-THESIS`, a written, scheduled falsification test with a pre-committed
  NO-GO threshold; for `UNDERSPECIFIED`, a filled claim with measurable slots; for
  `FALSIFIABLE-THESIS`, the test coming back negative or never running.
- **Next action:** the verdict's mandated step — write and schedule the falsification test, or
  fill the missing slot, or re-frame via `frame-product-problem`.

### Worked example

Claim: "Mid-market finance teams will switch from spreadsheets to our reconciliation tool."
Underspecified: no problem, no mechanism, no outcome. BELIEF-PRESENTED-AS-THESIS if the team
adds "we'll iterate until it works" as the disproof condition with no test, or cites three
friendly pilot logos as validation. FALSIFIABLE-THESIS when the claim becomes: "Of 20
mid-market finance teams currently on spreadsheets, at least 12 will adopt weekly use of the
reconciliation tool within 60 days of trial, measured by logins, with a pre-committed decision
to pivot to the spreadsheet-audit segment if we land below 8." The falsification condition,
the test, and the threshold are all explicit.

## Failure modes

- **Falsification theater.** Naming a disproof condition but scheduling no test and no NO-GO threshold. Correction: treat an untested falsification condition as a belief with a rhetorical flourish; the scheduled test is the verification.
- **Confidence inflation.** Every assumption labeled "high confidence" without independent evidence. Correction: require two independent evidence items before a High confidence label on any assumption.
- **Discovery replaced by presentation.** Board approval, press, or a working demo cited as evidence the thesis is true. Correction: separate "evidence we have" from "evidence we have been told to believe"; presentation evidence cannot fill a discovery slot.
- **Prestige as verification.** A board or investor roster with no technical fluency vouching for a technical claim. Correction: name the person who can technically falsify the claim and confirm they are empowered to raise it.
- **No exclusions.** A thesis so broad it commits the organization to everything. Correction: apply PRN-0002 — five things this thesis says no to.
- **Moat as aspiration.** "Our moat will be brand" with zero brand equity. Correction: current moat and credible path to a future moat must be stated separately.
- **Reversibility denial.** Treating an irreversible, high-consequence claim like a reversible feature bet. Correction: apply the CASE-0019 boundary — the speed-over-quality principle stops at irreversible decisions.

## Reversal conditions

- The falsification test comes back negative → the thesis is falsified; the bet is off, or a
  re-framed problem is tested.
- The falsification test never runs → the thesis degenerates to belief; re-run the skill.
- A new discovery evidence item changes the evidence classification → re-render.
- The claim's slots change materially → re-run.

## Composition hooks

- **before:** `frame-product-problem` (a thesis that cannot fill its four slots is usually a
  framing failure — run the frame first); `synthesize-customer-discovery` (the discovery-derived
  evidence base).
- **after:** `check-ai-evaluation-contract` (an AI thesis's falsification test is executed
  through an evaluation contract); `assess-product-market-fit-health` (when the predicted
  outcome is PMF, this skill reports whether the bet is paying off);
  `run-case-based-premortem` (a non-falsifiable thesis is a top premortem scenario);
  `make-go-no-go-call` (the falsifiable verdict feeds the evidence gate).
- **workflow:** product-bet (step 4).

## Related Skills

- `frame-product-problem` — the "before" half: problem, business outcome, solution, and assumptions separated before the thesis is stated.
- `synthesize-customer-discovery` — builds the discovery-derived evidence base the thesis needs.
- `check-ai-evaluation-contract` — an AI thesis's falsification test is executed through an evaluation contract.
- `assess-product-market-fit-health` — run when the thesis's predicted outcome is PMF.
- `make-go-no-go-call` — the verdict feeds the evidence gate.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
