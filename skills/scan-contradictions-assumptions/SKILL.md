---
name: scan-contradictions-assumptions
description: >-
  Surfaces the silent assumptions a decision is making and the tensions inside it — discovered
  from the user's actual situation first, then mapped to the Academy's contradiction register
  (CON-0001..CON-0013) as a reference set, never a closed ontology. Returns a ranked assumption
  register and a live/dormant/not-applicable verdict per relevant tension. Use to pressure-test
  a decision before it is locked, or to understand why two reasonable people are stuck.
type: assist
version: 0.2.0
best_for:
  - "A decision is about to be locked and you want its silent assumptions on the table first"
  - "Two stakeholders are arguing, each with evidence; you want the assumptions driving the disagreement exposed"
  - "A decision memo needs an assumption register"
  - "A post-mortem wants to know which assumption, if wrong, would have changed the outcome"
  - "Before a launch or Type-1 commitment, to find the tension the plan is silently inside"
doctrine:
  - "08_contradictions/register.yaml (reference set, not closed ontology)"
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0008 (discovery beats requests)"
  - "PRN-0003, PRN-0007 (reversibility terms for blast-radius ranking)"
  - "07_cases/case_catalog.md"
license: CC BY 4.0
---

## Purpose

Decisions are made on claims, and claims are made on assumptions — most of which are never
stated. This skill surfaces those assumptions from the user's actual situation **before**
consulting any doctrine, then maps the relevant ones to the Academy's contradiction register.
The register is a reference library of tensions the Academy has catalogued; it is a starting
point for naming what is live, not a checklist every decision must be jammed into.

The output is an assist artifact: a ranked list of exposed assumptions and a per-tension
verdict that tells you which polarities this decision is actually inside, and which pole it
currently favors.

## Use when

- A decision is about to be locked and its silent assumptions should be on the table first.
- Two stakeholders are stuck and each has evidence; you want the assumptions driving the disagreement.
- A decision memo needs an assumption register.
- A post-mortem asks which assumption, if wrong, would have changed the outcome.
- Before a Type-1 commitment, to name the tension the plan sits inside before committing.

## Do not use when

- The question is evidence adequacy — use `audit-decision-evidence`.
- The user wants the Academy's contradiction register enumerated for its own sake — that is a
  research task, not a decision job.
- The decision is reversible and low-stakes (a minor copy or layout change) — running an
  assumption scan costs more than the decision is worth. Use Fast mode or skip.
- You want to "resolve" a tension. This skill names the polarity you are in; it does not
  dissolve it.

## Inputs

Required inputs:

- The decision and the position being taken (one sentence each).
- The claims the position rests on (or a decision memo).

Optional inputs:

- Stakeholder disagreement you can see — tensions usually show up first as disagreement.
- The decision's reversibility class (TYPE-1/TYPE-2).

## Missing-data behavior

- If the decision is stated but claims cannot be articulated, the skill extracts claims with
  you — a decision with no claims cannot have its assumptions surfaced.
- "Unknown" answers are recorded as assumptions and the scan continues. An assumption with
  high blast radius and unknown status is automatically a top candidate to test.

## Context classification

- **TYPE-2, low stakes:** Fast mode — assumption register only, no tension sweep.
- **TYPE-1, high stakes:** Full mode — assumption register plus tension discovery and
  registry mapping; feeds the premortem.
- **Stalemate:** Full mode with explicit attention to the disagreement — the top assumption
  driving the two positions is the deliverable.

## Fast mode

Run for reversible or ordinary decisions. Four steps:

1. What is the decision, and the position being taken?
2. What must be true for this position to be correct? (1–3 claims.)
3. What does each claim silently assume? (One assumption per claim minimum.)
4. Rank by blast radius = probability of being wrong × cost of being wrong × (1/reversibility).

Output: the ranked assumption register with the TOP-ASSUMPTION named, each assumption tied to
the claim it supports. No registry mapping, no contradiction sweep. If the fast-mode output
shows a high-blast-radius assumption that cannot be tested cheaply, offer Full mode.

## Full mode

Adds to fast mode:

1. After surfacing assumptions, **discover tensions from the situation**: ask what the
   decision is trading off — speed vs assurance? responsiveness vs vision? discovery vs
   conviction? build vs buy? Let the situation generate the tension before consulting the
   registry.
2. **Map to the registry as a reference set** *(optional — works without the Academy repo)*:
   for each discovered tension, look it up in `08_contradictions/register.yaml` if you have
   the Academy repo available. If the registry has a matching entry (by question and failure
   modes, not by keyword), cite it and use its pole conditions as the check. If the registry
   is not available, name the tension from the situation alone — the registry is a reference
   set, never a closed ontology, and never required to produce a usable verdict.
3. For each relevant tension: name both poles, note which pole the current position favors,
   and check the register's `context_where_a_stronger` / `context_where_b_stronger` conditions.
4. If the decision matches a catalog case, cite the case and its recorded assumptions.
5. Rank assumptions by blast radius; the top one is the one to test first.

## Method

One question at a time. "Unknown" answers are recorded as assumptions and the scan continues.

1. What is the decision, and the position being taken? One sentence each.
2. What must be true for this position to be correct? (Same claim extraction as `audit-decision-evidence`.) Write the claims down.
3. For each claim: what does it silently assume about the customer, the market, the team, the timeline, the counterfactual? Produce one assumption per claim minimum. "Unknowns" behind a claim are assumptions too.
4. What is this decision trading off? Name the tension in your own words before opening the registry.
5. Does the registry describe this tension? (CON-0001..0013.) Cite it only if the register's question or failure modes genuinely describe the trade-off. No forced fit.
6. For each live tension: name both poles, the favored pole, and the conditions where the other pole wins.
7. Rank the assumptions by blast radius: probability wrong × cost of wrong × (1/reversibility) (PRN-0003/PRN-0007 terms). State the three factors for the top three so the ranking is checkable.
8. Name the TOP-ASSUMPTION: the one that, if falsified, changes the decision from GO to NOT-GO or materially changes the position.

## Evidence classification

- Assumptions are graded as statements of the form "X assumes that [state of the world]" —
  checkable propositions, not vague fears.
- Tension relevance is graded by the register entry's own question/failure-modes text, not by
  keyword similarity.
- The Academy registry is treated as catalogued practitioner evidence (E12 in the shared
  taxonomy); it informs, never overrides, the situation's own signals.

## Output schema

```json
{
  "skill": "scan-contradictions-assumptions",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "ASSIST-ARTIFACT",
  "top_assumption": {"statement": "...", "claim": "...", "blast_radius_factors": {"probability": "...", "cost": "...", "reversibility": "..."}},
  "assumption_register": [
    {"statement": "...", "supports_claim": "...", "rank": 1}
  ],
  "tensions": [
    {"tension": "...", "registry_match": "CON-0009 | none", "status": "LIVE | DORMANT | NOT-APPLICABLE",
     "favored_pole": "...", "other_pole_wins_when": "..."}
  ],
  "confidence": "high | medium | low",
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** `ASSIST-ARTIFACT` — an assist artifact, not a scored verdict: the ranked
  assumption register, the TOP-ASSUMPTION, and per-tension status.
- **Per-tension status:** `LIVE` (the decision makes the trade-off the tension describes and
  the pole choice matters) / `DORMANT` (tension exists in background, decision does not force
  it) / `NOT-APPLICABLE` (the tension's subject matter does not touch this decision).
- **Confidence:** High/Medium/Low. Low when the decision's claims are themselves underspecified.
- **Evidence basis:** the claims and situation-derived tensions; the registry entries cited.
- **Assumptions:** every "unknown" the user gave, recorded explicitly.
- **What would change the verdict:** for each LIVE tension, the register conditions or
  reversal conditions that would move it to DORMANT or flip the favored pole.
- **Next action:** test the TOP-ASSUMPTION — the cheapest discriminating evidence, with an owner.

### Worked example

Decision: "Build the top-requested enterprise feature this quarter, on the timeline sales
requested." Claims: the request is representative; shipping it retains the account; it does
not break the roadmap. Exposed assumptions: (1) loudest enterprise accounts are representative
of the market, (2) retention is elastic to this specific feature, (3) the roadmap has slack
for an unplanned bet. Tension discovered from the situation: "customer responsiveness vs
coherent vision" — before opening the registry. Registry match: CON-0009 `LIVE` (the decision
forces the trade-off). CON-0002 `DORMANT` (requests honored without discovery of the underlying
problem). Ranked: assumption 1 is TOP-ASSUMPTION (high failure probability, high cost,
decision reversible but reputation cost is not). Confidence: High. Next action: review the last
20 closed-won/lost enterprise deals to test whether the request's representativeness holds
(E8). What would change it: CON-0009 drops to DORMANT if the feature is defensible under the
register's `context_where_a_stronger` (mature enterprise SaaS with feature-competitive market)
— responsive by strategy, not by default.

## Failure modes

- **Silent assumption passing as fact:** "we assume churn will drop" stated as "churn will
  drop." Correction: every claim gets an explicit assumption statement.
- **Discovery theater (PRN-0008):** "we validated it with customers" masking the assumption
  that those customers represent the market. Correction: representativeness goes on the
  assumption register.
- **Forced-fit contradictions:** jamming every decision into CON-0001..0013 so the scan looks
  thorough. Correction: discovery-first — the tension comes from the situation; the registry
  is consulted, not applied. The thresholds require the register entry to actually describe
  the decision's trade-off.
- **Framing one pole as bad:** returning "we are on the right side of CON-0006." Correction:
  both poles are legitimate; the verdict names the favored pole and the conditions where the
  other wins.
- **Data as a weapon (PRN-0014):** using the assumption list to win the argument instead of
  to expose it. Correction: the deliverable is the ranked list; who is "right" is a separate
  meeting.
- **Vague fear as assumption:** "users might not like it" without a checkable proposition.
  Correction: restate as "assumes that [observable state of the world]" or drop it.

## Reversal conditions

- An assumption on the register resolves the wrong way — the TOP-ASSUMPTION is falsified, so
  the position must change.
- A LIVE tension's context shifts to the other pole's `context_where_*` conditions.
- New evidence contradicts a claim whose assumption was ranked low — re-rank.

## Composition hooks

- **before:** `frame-product-problem` (a clean problem frame makes claim/assumption extraction
  faster); `audit-decision-evidence` (grade the claims whose assumptions you are exposing).
- **after:** `run-case-based-premortem` (top assumptions become premortem failure narratives);
  `conduct-causal-confidence-review` (grades how strongly the TOP-ASSUMPTION is established);
  `align-stakeholders-on-decision` (assumption register explains why the two sides disagree).
- **workflow:** product-bet (step 4.5), product-health-review (step 3).

## Related Skills

- `audit-decision-evidence` — grade the evidence for the claims whose assumptions you expose.
- `conduct-causal-confidence-review` — for the TOP-ASSUMPTION, establishes how strongly it is established.
- `run-case-based-premortem` — top assumptions feed failure narratives.
- `align-stakeholders-on-decision` — a disagreement is usually two different assumption sets.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
