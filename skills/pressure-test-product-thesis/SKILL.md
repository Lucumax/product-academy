---
name: pressure-test-product-thesis
description: >-
  Produces a verdict on whether a stated product thesis is falsifiable and
  coherent — and whether it is actually a thesis or a belief dressed up as one.
  Invoke before committing resources to a bet, before a funding or board
  presentation, whenever someone says "the plan" without being able to say what
  would disprove it, or when the team cannot agree on what success would look
  like. Uses the Theranos failure pattern (CASE-0019) as the reference failure.
type: assess
version: 0.1.0
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
  - "CON-0002 (discovery vs conviction)"
  - "CASE-0019 (Theranos)"
  - "09_tools/PRODUCT_THESIS_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

This skill answers one question: **is the thing being presented as a product thesis actually a testable bet, or is it a belief that cannot be disproven?** A thesis is a claim about a specific customer, a specific problem, and a specific mechanism that you commit to testing. A belief is a claim you are not willing to put at risk. The distinction matters because beliefs quietly absorb resources while producing no information — the Theranos pattern (CASE-0019) is what happens when a thesis can never be falsified.

Invoke this skill when a decision is about to be made on the strength of a claim: committing budget, hiring against it, presenting to the board, or doubling down on an existing bet. Invoke it when a strategy conversation keeps producing direction but no test. Invoke it when two factions interpret the same evidence differently and neither can name the evidence that would settle it.

Do NOT invoke this skill when the user wants to write a thesis document — point them to `09_tools/PRODUCT_THESIS_TEMPLATE.md`. Do NOT invoke it when the user wants a full strategy review — that is a portfolio decision and this skill is a single-claim diagnostic. Do NOT invoke it for a reversible feature tweak; the cost of running the discipline outweighs the value.

## Input

What the user should bring:

- The thesis as it is currently stated (verbatim if possible — one or two sentences).
- What evidence currently exists for it, and where that evidence came from (customer discovery, pilots, market reports, demos, executive belief).
- What decision is pending on the strength of this thesis.
- Who holds the technical or domain fluency to verify the core claim.

If the user arrives with only "we think X will be big," the skill still works — the method below will expose the thesis as underspecified, which is a verdict in itself. If the user refuses to state a falsification condition, record that refusal and return BELIEF-PRESENTED-AS-THESIS; that is the point of the skill.

## Method

Work through these questions in order. Ask the user directly; do not infer answers. If the user answers "unknown," record it as a stated assumption and continue — never silently assume.

1. **State the thesis as a claim.** Ask: "Complete this sentence: We bet that [specific customer segment] has [specific problem], that [specific mechanism] solves it, and that the world changes in [specific way] if we are right." If any of the four slots cannot be filled, the claim is underspecified and you can stop early — record what is missing.
2. **What would disprove it?** This is the core question. Ask: "Articulate the evidence that would prove this thesis wrong. What would have to be true — or fail to happen — for you to conclude the bet is lost?" A defensible answer names a measurable outcome and a timeframe. A strong answer: "If fewer than 3 of the first 5 enterprise pilots convert to paid within 90 days of trial end, the willingness-to-pay assumption is wrong." A weak answer: "If we can't get traction" — that is a feeling, not a condition. "We'll just keep iterating" is not an answer at all.
3. **Are you willing to run that test?** Ask: "What is the experiment, who runs it, when does it start, and what pre-committed threshold turns its result into a Go or No-Go decision?" The willingness to run the test is what separates a thesis from a belief (CASE-0019, what_was_learned 1). A test that cannot fail, or whose threshold is set after the results arrive, is not a test. If the user answers "we'll know when we see it," record it and return BELIEF-PRESENTED-AS-THESIS.
4. **What is the evidence, really?** Classify what currently supports the thesis: is it discovery-derived (from actual customer investigation, PRN-0008), or is it presentation-derived (demos, fundraising narrative, prestige endorsement)? Ask specifically: "Of the evidence we have, how much came from talking to people who live with the problem, versus from demos we showed them, versus from internal conviction?" The Theranos failure was discovery replaced by presentation — demos and board prestige standing in for validation (CASE-0019, failure_modes).
5. **Who can technically falsify it?** Ask: "Who in the decision chain has enough technical fluency to challenge the core claim, and are they empowered to raise it?" If the answer is no one, flag the CASE-0019 technical-fluency failure mode — a board of prestige is not a board of verification. If the answer is "we hired X but nobody listens to them," that is the same failure with a different costume.
6. **What does this thesis say no to?** Apply PRN-0002. Ask: "If this thesis is right, what will we explicitly not do?" A thesis that excludes nothing is a wish list, not a bet. Push for at least three concrete exclusions — a market, a segment, a use case, a platform, a channel. Inability to name exclusions means the thesis is not yet a decision; it is a direction of travel.
7. **Record assumptions.** Anything answered "unknown" goes into the verdict as a stated assumption with the confidence it carries. The assumption's effect on the verdict is recorded too: if the "unknown" is the falsification condition itself, the verdict cannot be FALSIFIABLE-THESIS regardless of how confident everyone feels.

Then produce the verdict per the contract below.

## Verdict Contract

- **Verdict:** one of
  - `FALSIFIABLE-THESIS` — the claim is specific, a disproof condition exists and is stated in measurable terms, the test is actually scheduled, and the evidence is genuine.
  - `BELIEF-PRESENTED-AS-THESIS` — the claim is specific enough but either no disproof condition can be articulated, or the team refuses to run the test. This is the Theranos pattern (CASE-0019): the thesis is being maintained, not tested.
  - `UNDERSPECIFIED` — the claim cannot be tested because one or more of the four slots (segment, problem, mechanism, outcome) is missing or too vague to measure.
- **Confidence:** High / Medium / Low, with reasoning. Lower confidence when the thesis is promising but the disproof condition depends on assumptions marked "unknown" in the method.
- **Citations:** cite the doctrine that drives each conclusion, e.g. `PRN-0005`, `PRN-0008`, `CASE-0019`, `09_tools/PRODUCT_THESIS_TEMPLATE.md`, plus the source behind the claim where available.
- **Stated assumptions:** every "unknown" the user answered, listed explicitly, with the effect each would have on the verdict if it resolved the wrong way.
- **What would change the verdict:** the specific evidence that would flip the call. For `BELIEF-PRESENTED-AS-THESIS`, the flip is a written, scheduled falsification test with a pre-committed No-Go threshold. For `UNDERSPECIFIED`, the flip is a filled claim with measurable slots. For `FALSIFIABLE-THESIS`, the flip is the falsification test coming back negative, or the test never running.

Example verdict output (shape to copy, not to memorize):

```
Verdict: BELIEF-PRESENTED-AS-THESIS
Confidence: High — all four claim slots filled; no disproof condition survives prompting.
Citations:
  - Claim specificity: 09_tools/PRODUCT_THESIS_TEMPLATE.md (Falsification Conditions)
  - Presentation-derived evidence: CASE-0019 (discovery replaced by presentation)
  - No exclusions: PRN-0002
Stated assumptions:
  - Market size data not validated (unknown); would matter only if the claim itself were tested.
What would change the verdict: a written test with a named owner, start date, and
  pre-committed No-Go threshold (e.g., <3 of 5 pilots convert within 90 days).
```

## Thresholds

A second reviewer must be able to reproduce the verdict from the same inputs. Use these checks:

- **UNDERSPECIFIED** — one or more of the four claim slots (customer segment, problem, mechanism, outcome) is missing, vague ("better", "faster", "any business"), or uses a non-measurable descriptor. A claimed falsification condition that names no number, no behavior, and no timeframe is also an underspecification, not a falsification condition.
- **BELIEF-PRESENTED-AS-THESIS** — the claim is specific (all four slots filled) AND at least one of: (a) no disproof condition can be articulated despite prompting, (b) a disproof condition exists but no test is scheduled and no owner is named, (c) the test is scheduled but there is no pre-committed No-Go threshold, or (d) the "evidence" is entirely presentation-derived (demos, prestige, internal conviction) with no customer- or experiment-derived component.
- **FALSIFIABLE-THESIS** — all four of: (a) four slots filled with measurable descriptors, (b) a disproof condition naming a measurable outcome and a timeframe, (c) a scheduled test with a named owner and a pre-committed Go/No-Go threshold, (d) at least one piece of discovery- or experiment-derived evidence that is not just presentation. One borderline slot may be marked as a stated assumption without dropping the verdict.

If fewer than all checks hold for a verdict, return the highest-confidence lower verdict rather than forcing a fit. Confidence is High when every check holds with no material "unknowns"; Medium when one or two checks hold by a margin; Low when the verdict rests on assumptions the user could not verify.

Worked example for calibration. Claim: "Mid-market finance teams will switch from spreadsheets to our reconciliation tool." Underspecified: no problem, no mechanism, no outcome. BELIEF-PRESENTED-AS-THESIS if the team adds "we'll iterate until it works" as the disproof condition with no test, or cites three friendly pilot logos as validation. FALSIFIABLE-THESIS when the claim becomes: "Of 20 mid-market finance teams currently on spreadsheets, at least 12 will adopt weekly use of the reconciliation tool within 60 days of trial, measured by logins, with a pre-committed decision to pivot to the spreadsheet-audit segment if we land below 8." The falsification condition, the test, and the threshold are all explicit.

## Evidence & Doctrine

- `PRN-0002` — strategy as exclusion; a thesis must imply what the organization will not do. Tier: principle, high confidence.
- `PRN-0005` — the PM owns the problem, not the solution; the thesis must state the problem in customer terms, not as a build.
- `PRN-0008` — discovery beats requests; evidence for a thesis must come from investigation of the problem, not from requests or presentation.
- `PRN-0014` — the same data supports opposite conclusions; when two camps cite the same evidence, the skill is to design the discriminating test rather than argue the interpretation.
- `CON-0002` — continuous discovery vs concentrated conviction; conviction-driven bets are legitimate but must still be falsifiable, which is exactly what Theranos never was.
- `CASE-0019` — Theranos. Failure pattern: thesis asserted not validated; discovery replaced by presentation; no decision-maker had technical fluency; secrecy prevented falsification. What does not transfer: the criminal fraud. What transfers: the failure of falsification. Sources: `SRC-POST-0101` (WSJ investigation, Tier A), `SRC-POST-0102` (Bad Blood, Tier A), `SRC-POST-0104` (SEC charges, Tier A).
- `09_tools/PRODUCT_THESIS_TEMPLATE.md` — the falsification conditions section is the most important part of the template: "A thesis without falsification conditions is a belief, not a bet."

Cite, don't copy. Quote at most a short line with a location, then point at the registry.

## Common Pitfalls

- **Falsification theater.** Naming a disproof condition but scheduling no test and no No-Go threshold. Correction: treat an untested falsification condition as a belief with a rhetorical flourish. The scheduled test is the verification.
- **Confidence inflation.** Every assumption labeled "high confidence" without multiple independent sources. Correction: require two independent evidence sources before allowing a High confidence label on any assumption.
- **Discovery replaced by presentation.** Board approval, press, or a working demo cited as evidence the thesis is true — the Theranos substitution. Correction: separate "evidence we have" from "evidence we have been told to believe"; presentation evidence cannot fill a discovery slot.
- **Prestige as verification.** A board or investor roster with no technical fluency vouching for a technical claim. Correction: name the person who can technically falsify the claim and confirm they are empowered to raise it.
- **No exclusions.** A thesis so broad it commits the organization to everything. Correction: apply PRN-0002 — five things this thesis says no to.
- **Moat as aspiration.** "Our moat will be brand" with zero brand equity. Correction: current moat and credible path to a future moat must be stated separately.
- **Reversibility denial.** Treating an irreversible, high-consequence claim like a reversible feature bet and shipping "to learn." Correction: apply the CASE-0019 boundary — the speed-over-quality principle stops at irreversible decisions.

## Related Skills

- `check-ai-evaluation-contract` — run after a FALSIFIABLE-THESIS verdict on an AI product; the thesis's falsification test is executed through an evaluation contract.
- `assess-product-market-fit-health` — run when the thesis's predicted outcome is PMF; this skill tells you whether the bet is actually paying off in a maintained condition.
- `09_tools/PRODUCT_STRATEGY_TEMPLATE.md` — the "after" half for a thesis that passes; the strategy makes the thesis's exclusions explicit.
