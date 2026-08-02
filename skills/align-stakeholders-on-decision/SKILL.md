---
name: align-stakeholders-on-decision
description: >-
  Produces a stakeholder alignment map for a contested decision: separates disagreement about
  facts, goals, incentives, risk tolerance, and decision rights, then names the single highest
  value move that unblocks the decision. Invoke when Sales, Product, and Engineering disagree,
  when a decision is stuck in meetings, or when two sides argue past each other because they
  are arguing about different things. The output is a decision-rights recommendation plus the
  specific evidence or owner each disagreement type needs.
type: assist
version: 0.1.0
best_for:
  - "Sales, Product, and Engineering disagree on a launch or roadmap call"
  - "A decision is stuck in repeated meetings with no progress"
  - "Two sides argue past each other — one citing facts, the other citing goals or incentives"
  - "A sponsor pushes to proceed and a team pushes to pause, and neither moves"
  - "Before an executive escalation, to present the disagreement precisely instead of as a turf war"
doctrine:
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0002 (strategy is saying no)"
  - "PRN-0012 (most expensive decision is the one you do not make)"
  - "CON-0006 (speed vs assurance)"
  - "CON-0009 (responsiveness vs vision)"
  - "09_tools/STAKEHOLDER_INCENTIVE_MAP.md"
  - "09_tools/DECISION_MEMO_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Most stakeholder deadlocks are not disagreements about the same thing. They are **five
different disagreement types stacked into one argument**: facts ("the data says X"), goals
("we are optimizing for different outcomes"), incentives ("our success metrics punish the
right call"), risk tolerance ("we are willing to take different risks"), and decision rights
("we cannot even agree who decides"). Until the disagreement is separated by type, no
evidence can resolve it, because the two sides are not even arguing the same axis.

This skill produces an **alignment map**: each disagreement typed, each type's resolution
path named, and a single highest-value move that unblocks the decision. It also names the
decision rights — who actually decides, per the reversibility and escalation logic — so the
conversation stops at the point of decision instead of circling.

## Use when

- Sales, Product, and Engineering disagree on a launch or roadmap call.
- A decision is stuck in repeated meetings with no progress.
- Two sides argue past each other — one citing facts, the other goals or incentives.
- A sponsor pushes to proceed and a team pushes to pause, and neither moves.
- Before an executive escalation, to present the disagreement precisely.

## Do not use when

- The disagreement is genuinely factual and resolvable by one experiment — the fastest path is
  `design-product-experiment`, not an alignment meeting.
- The user wants a stakeholder-communications plan or a slide deck — the alignment map is the
  diagnosis; the write-up is the memo template's job.
- One party is clearly decision-rights-empowered and the disagreement is moot — classify
  reversibility and decide (`classify-decision-reversibility`, `make-go-no-go-call`).
- The disagreement is about emotions or relationship repair, not a decision — this skill
  aligns on a decision, not on feelings.

## Inputs

Required inputs:

- The decision being contested, one sentence.
- The stakeholders involved and their stated positions.
- A sample of what each side is actually saying (quotes or paraphrases — they reveal the disagreement type).

Optional inputs:

- The written strategy, the reversibility classification, and any evidence either side cites.

## Missing-data behavior

- A stakeholder position with no rationale → the map marks it "position-without-reason" and
  the next action is one meeting to extract the type, not an assumption about it.
- No written strategy → goal-type disagreements cannot be adjudicated against strategy;
  recorded as an assumption.
- Reversibility unknown → decision rights cannot be assigned; escalate to
  `classify-decision-reversibility` as a precondition.

## Context classification

- **TYPE-1, high stakes:** decision rights matter — escalation is explicit; the alignment map
  must name the signing authority.
- **TYPE-2, low stakes:** decision rights default to the team closest to the information; the
  alignment map unblocks, it does not escalate.
- **Cross-functional launch:** incentives are usually the hidden type — Sales bonuses, Eng
  on-call, Product ownership metrics all point differently at the same decision.

## Fast mode

Run for a quick unblock on an ordinary decision. Four steps:

1. What is the decision, and who is stuck?
2. For each side, one line: what are they actually claiming? (fact, goal, incentive, risk, or rights)
3. Label the disagreement types. Are both sides arguing the same type?
4. For the dominant type, name the resolution path: facts → evidence; goals → strategy; incentives → realignment; risk → reversibility design; rights → named decider.

Output: the type-labelled one-liner for each side, the dominant disagreement type, and the
single unblocking action. No full map in fast mode.

## Full mode

Adds: the full five-type map with every stakeholder, the incentive realignment (which metrics
misalign and how to change them), the risk-tolerance comparison (each side's threshold for
proceeding), the decision-rights assignment (per reversibility and escalation), and the
pre-escalation packet for the named decider.

## Method

One question at a time. "Unknown" answers are recorded as stated assumptions.

1. State the decision and the stakeholders. One sentence for the decision; a named list for the stakeholders, with their stated position.
2. Collect what each side is actually saying. Quote or paraphrase verbatim — the phrasing reveals the disagreement type.
3. Type each disagreement. Classify each side's claim: FACT (a claim about the world, resolvable by evidence), GOAL (a claim about which outcome matters), INCENTIVE (a claim about whose metrics reward what), RISK (a claim about acceptable downside), or RIGHTS (a claim about who decides). A single side may be arguing two types.
4. Separate same-type from different-type disagreements. If both sides argue facts, one experiment may settle it (hand off to `design-product-experiment`). If one argues facts and the other goals, more evidence will NOT settle it — that is the key diagnostic.
5. Resolve goals against strategy (PRN-0002). If the written strategy picks a goal, the goal disagreement is adjudicated; if not, the strategy gap is the finding.
6. Expose incentives. Name whose metrics reward each position. If incentives fight the right call, realign the metric or name the person empowered to make the call despite it (STAKEHOLDER_INCENTIVE_MAP).
7. Compare risk tolerance. Ask each side their threshold: what downside are they willing to accept, and what evidence would move them? Risk disagreements are resolved by reversibility design (PRN-0007), not by debate.
8. Assign decision rights. Classify reversibility; the decider is the level matching the commitment scale. Name them, by name, and the decision memo field for the call.
9. Produce the alignment map: types, resolution path per type, and the single highest-value move.

## Evidence classification

Uses the shared taxonomy. FACT disagreements are settled by the best-fit evidence type (E1
experiment, E3 behavior, E4 cohort, E8 win/loss, E11 financial). GOAL and INCENTIVE
disagreements are NOT settled by evidence — they are settled by strategy (PRN-0002) and by
realigned incentives; evidence can only inform. RISK disagreements are settled by reversibility
design, with the cost-of-wrong × probability terms from PRN-0007. Labeling a goal disagreement
as a fact disagreement and demanding "more data" is a category error this skill exists to catch.

## Output schema

```json
{
  "skill": "align-stakeholders-on-decision",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "ALIGNMENT-MAP | DECIDER-NAMED | STUCK-ON-GOALS-OR-INCENTIVES",
  "decision": "...",
  "stakeholders": [
    {"stakeholder": "...", "position": "...", "disagreement_types": ["facts | goals | incentives | risk | rights"],
     "resolution_path": "..."}
  ],
  "dominant_type": "facts | goals | incentives | risk | rights",
  "decision_rights": {"decider": "...", "basis": "TYPE-1 | TYPE-2 | escalation", "deadline": "..."},
  "confidence": "high | medium | low",
  "evidence_basis": ["E1", "E8"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `ALIGNMENT-MAP` (disagreements typed and each has a resolution path; the
  highest-value move is named) / `DECIDER-NAMED` (the disagreements are real but the
  decision-rights assignment was the blocker — the named decider and deadline are the
  artifact) / `STUCK-ON-GOALS-OR-INCENTIVES` (the dominant disagreement is goals or
  incentives, no written strategy or metric realignment exists to resolve it; the output
  names the strategy gap or the metric change needed before alignment is possible).
- **Typing rule:** each stakeholder claim is classified fact/goal/incentive/risk/rights. If
  the two sides disagree on different types, no single piece of evidence settles it — that is
  the core diagnostic.
- **Confidence:** High when positions are verbatim and the types are unambiguous; Medium when
  a position's type is inferred; Low when positions are secondhand or the decision is vague.
- **Assumptions:** every "unknown," with effect.
- **What would change the verdict:** for STUCK-ON-GOALS-OR-INCENTIVES, a written strategy
  picking a goal, or a realigned metric; for any map, the resolution-path step completing.
- **Next action:** the single highest-value move — an experiment for a fact disagreement, a
  strategy adjudication for goals, a metric change for incentives, reversibility design for
  risk, or a named decider with a deadline for rights.

### Worked example

Decision: "Launch the AI triage assistant next quarter." Sales: "If we don't launch, the two
biggest deals this quarter are at risk" — GOAL + INCENTIVE (quota). Engineering: "We cannot
guarantee reliability; launch is unsafe" — RISK. Product: "The evaluation contract says the
accuracy bar is not met yet" — FACT. Typing: the sides are on three different axes. No amount
of accuracy data settles Sales' goal claim, and no reliability debate settles Product's fact
claim. Resolution: (1) the fact disagreement is settled by the evaluation contract readout —
the contract's pre-committed thresholds ARE the fact (E1/E12); (2) the goal/incentive
disagreement is adjudicated against strategy — does the strategy accept a two-deal-at-risk
trade for reliability? — and Sales' metric is flagged for realignment if the strategy says
reliability; (3) the risk disagreement is resolved by reversibility design — a flag-gated
launch to the two accounts with a named rollback authority converts "unsafe" into "bounded".
Decision rights: TYPE-2-with-escalation (flag-gated launch), decider = head of product,
deadline = Friday. Verdict: ALIGNMENT-MAP. Next action: the evaluation-contract readout for
the fact axis, plus the strategy adjudication for the goal axis.

## Failure modes

- **Category error: "we need more data" for a goal or incentive disagreement.** Evidence cannot settle "which outcome matters." Correction: type it; goals resolve to strategy, incentives to realignment.
- **Turf war presentation.** "Sales is being unreasonable" instead of "Sales is arguing a goal axis and an incentive axis." Correction: the typed map is the escalation packet; it depersonalizes the disagreement.
- **Risk debate as fact debate.** Arguing "it's risky" vs "it's fine" as if one of them is wrong about the world. Correction: risk resolves to reversibility design, not to evidence.
- **Decision rights avoided.** A meeting that keeps deciding nothing because no one is empowered. Correction: assign the decider by reversibility class and name them.
- **Incentive blindness.** Everyone arguing in good faith, but the metrics reward the wrong call. Correction: the incentive axis is exposed explicitly; realign or name who decides despite it.
- **Mobilization by schedule.** The loudest deadline wins. Correction: type the claims; a deadline is a goal-claim and resolves to strategy, not to volume.

## Reversal conditions

- The fact axis is settled by an experiment or readout → re-type the map; remaining types change.
- A strategy document arrives or changes → goal disagreements re-adjudicate.
- A metric is realigned → incentive disagreement resolves.
- The decider makes the call → the alignment map is closed; the decision proceeds under its reversal conditions.

## Composition hooks

- **before:** `classify-decision-reversibility` (decision rights and escalation basis);
  `frame-product-problem` (a common frame prevents cross-axis arguments);
  `scan-contradictions-assumptions` (two positions usually carry different assumptions);
  `audit-decision-evidence` (the fact axis's evidence is graded).
- **after:** `make-go-no-go-call` (the aligned decision's verdict); `09_tools/DECISION_MEMO_TEMPLATE.md` (the write-up with the named decider).
- **workflow:** launch-gate (step 5), product-bet (step 7.5).

## Related Skills

- `classify-decision-reversibility` — provides the decision-rights basis.
- `scan-contradictions-assumptions` — two positions usually rest on different assumptions; surface them first.
- `design-product-experiment` — the fact axis's fastest resolution.
- `make-go-no-go-call` — the aligned decision's verdict.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
