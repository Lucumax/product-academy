---
name: scan-contradictions-assumptions
description: >-
  Surfaces the silent assumptions a decision is making and maps which of the Academy's known
  contradictions (CON-0001..CON-0013) are live in it. Returns a ranked list of exposed
  assumptions plus a live/dormant/not-applicable verdict per contradiction. Use this to pressure-test
  a decision before it is locked, or to understand why two reasonable people are stuck.
type: assist
version: 0.1.0
best_for:
  - "A decision is about to be locked and you want its silent assumptions on the table first"
  - "Two stakeholders are arguing and each has evidence; you want the assumptions driving the disagreement exposed"
  - "You want to know which known Academy tensions this decision sits inside before you commit to one pole"
  - "A decision memo needs its assumption register and its contradiction mapping filled in"
  - "A post-mortem wants to know which assumption, if it had been wrong, would have changed the outcome"
doctrine:
  - "08_contradictions/register.yaml"
  - "09_tools/CONTRADICTION_ANALYSIS_TEMPLATE.md"
  - "PRN-0014"
  - "PRN-0008"
  - "07_cases/case_catalog.md"
license: CC BY 4.0
---

## Purpose

Decisions are made on claims, and claims are made on assumptions. Most of those assumptions are never stated. This skill makes them explicit and then maps them onto the Academy's contradiction register — because most decisions are not "pick the right side" problems, they are points on a known tension spectrum (CON-0001 through CON-0013). The output is an assist artifact: a ranked list of exposed assumptions and a per-contradiction verdict that tells you which tensions this decision is actually inside.

Invoke it before locking a decision, when a disagreement has stalled, or when a decision's framing feels too clean. Do NOT invoke it to grade evidence adequacy (that is `audit-decision-evidence`) or to certify sources (`run-source-tier-check`). Do NOT use it to "resolve" a contradiction — the register's position is that most tensions are polarities to navigate, not problems to solve; this skill tells you which polarity you are in, and `CONTRADICTION_ANALYSIS_TEMPLATE` navigates it.

## Input

Bring the decision and its position: what you are deciding, what you are leaning toward, and the claims the position rests on. If you have a decision memo, bring it. If you arrive with only the decision, the skill will extract claims with you. Bring any stakeholder disagreement you can see — the contradictions usually show up first as the disagreement.

## Method

One question at a time. "Unknown" answers are recorded as assumptions and the scan continues.

1. What is the decision and what is the position being taken? One sentence each.
2. What must be true for this position to be correct? (Same claim extraction as `audit-decision-evidence`.) Write the claims down.
3. For each claim, what does it assume silently? Ask of each: what is this claim taking for granted about the customer, the market, the team, the timeline, the counterfactual? Produce one assumption per claim minimum. If the claim has "unknowns" behind it, those are assumptions too.
4. Which assumptions does the Academy's doctrine contradict? Match each assumption to the principle(s) in `01_core_doctrine/PRINCIPLES.md` that assert the opposite is often true. A claim that assumes a problem is well-understood contradicts PRN-0008's discovery-first position, for example.
5. Which contradiction does this decision sit inside? For each of CON-0001..CON-0013 in `08_contradictions/register.yaml`, ask: does this decision make the kind of trade-off the contradiction describes? A decision to ship fast on a payment feature is inside CON-0006 (speed vs assurance). A decision to build what the biggest customer asks is inside CON-0009.
6. For each live contradiction: name both poles from the register, and note which pole the current position favors, with the register's `context_where_a_stronger` / `context_where_b_stronger` conditions as the check.
7. Rank the assumptions by blast radius: probability it is wrong x cost of being wrong x reversibility (PRN-0003/PRN-0007 terms). The top assumption is the one to test first.
8. If the decision maps to a known case, cite the case and its assumptions list (each case in `07_cases/case_catalog.md` records its assumptions — e.g. CASE-0001's assumption that "customers will eventually understand the strategic logic").

## Verdict Contract

- **Verdict:** for each contradiction reviewed, one of `LIVE` / `DORMANT` / `NOT-APPLICABLE`, plus a `TOP-ASSUMPTION` naming the single assumption whose failure changes the decision most.
  - `LIVE` — the decision makes the trade-off the contradiction describes, and the choice of pole matters to the outcome.
  - `DORMANT` — the tension exists in the background but the decision does not force the trade-off.
  - `NOT-APPLICABLE` — the contradiction's subject matter does not touch this decision.
- **Assumption register:** the ranked list of exposed assumptions, each tied to the claim it supports and the doctrine it contradicts, ordered by blast radius.
- **Confidence:** High/Medium/Low with reasoning. Low when the decision's claims are themselves under-specified.
- **Citations:** the contradiction IDs (CON-0001..0013) with their titles from the register, the principles (PRN-xxxx), and any matched case (CASE-xxxx).
- **Stated assumptions:** every "unknown" the user gave, recorded explicitly.
- **What would change the verdict:** for each `LIVE` contradiction, the condition from the register's `context_where_*` lists or `reversal_conditions` that would move it to `DORMANT` or flip the favored pole.

### Worked example

Decision: "Build the top-requested enterprise feature this quarter, on the timeline sales requested." Claims: the request is representative; shipping it retains the account; it does not break the roadmap. Exposed assumptions: (1) the loudest enterprise accounts are representative of the market, (2) retention is elastic to this specific feature, (3) the roadmap has slack for an unplanned bet. Contradiction scan: CON-0009 `LIVE` (customer responsiveness vs coherent vision — the decision forces the trade-off); CON-0002 `DORMANT` (discovery vs conviction — requests are being honored without discovery of the underlying problem); CON-0001 `NOT-APPLICABLE`. Ranked: assumption 1 is `TOP-ASSUMPTION` (high failure probability, high cost, decision reversible but reputation cost is not). Confidence: High. What would change it: CON-0009 drops to `DORMANT` if the feature is defensible under the register's `context_where_a_stronger` (mature enterprise SaaS with feature-competitive market) — i.e., if the decision is responsive by strategy, not by default.

## Thresholds

A second reviewer must reproduce the assumption list and the live set from the same inputs.

- An assumption must be recorded as a statement of the form "X assumes that [state of the world]." Vague fears are not assumptions; restate them as checkable propositions or drop them.
- A contradiction is `LIVE` only if the decision's own trade-off appears in the register entry's `question` or `failure_modes`, or its pole descriptions. If the register entry does not describe this decision's tension, it is not live — do not force-fit.
- Ranking rule: blast radius = (estimated probability the assumption fails) x (estimated cost of that failure, in the decision's own terms) x (1 / reversibility of the decision). State the three factors per top-three assumption so the ranking is checkable.
- The `TOP-ASSUMPTION` must be one that, if falsified, changes the decision from GO to NOT-GO or materially changes the position.

## Evidence & Doctrine

- `08_contradictions/register.yaml` — 13 contradictions (CON-0001..CON-0013), each with `question`, both poles, `strongest_evidence_a/b`, `context_where_a_stronger/b_stronger`, `failure_modes`, `reversal_conditions`. Cite the ID and title; do not reproduce entries.
- `09_tools/CONTRADICTION_ANALYSIS_TEMPLATE.md` — the navigation method for any `LIVE` contradiction (position for now, shift conditions, guardians, monitoring). This skill ends where that template begins.
- `PRN-0014` — the reason assumptions drive interpretation: the same data supports opposite conclusions because each side imports different assumptions.
- `PRN-0008` — discovery vs requests; feeds step 4's contradiction matching and the "discovery theater" pitfall.
- `07_cases/case_catalog.md` — each case records its assumptions and failure modes; CASE-0001 (assumption that customers would accept the logic), CASE-0003 (assumption that usage metrics captured user value), CASE-0005 (assumption that dormant code was harmless).

## Common Pitfalls

- **Silent assumption passing as fact:** "we assume churn will drop" stated as "churn will drop." Correction: every claim gets an explicit assumption statement; unstated assumptions are the failure being fixed.
- **Discovery theater (PRN-0008):** "we validated it with customers" masking an assumption that those customers represent the market. Correction: the assumption list includes representativeness; check the contradiction register's discovery vs conviction poles.
- **Framing one pole as bad (CONTRADICTION_ANALYSIS_TEMPLATE mistake #1):** the scan returns "we are on the right side of CON-0006." Correction: both poles are legitimate; the verdict names the favored pole and the conditions where the other pole wins.
- **Forced-fit contradictions:** jamming every decision into a contradiction so the scan looks thorough. Correction: the thresholds require the register entry to actually describe the decision's trade-off.
- **Data as a weapon (PRN-0014):** using the assumption list to win the argument instead of to expose it. Correction: the deliverable is the ranked list; who is "right" is a separate meeting.

## Related Skills

- `audit-decision-evidence` — the "before" half: grade the evidence for the claims whose assumptions you are exposing.
- `run-source-tier-check` — certifies the sources behind the claims first, so assumption-spotting is not distracted by source disputes.
- `conduct-causal-confidence-review` — for the `TOP-ASSUMPTION`, establishes how strongly it is actually established.
