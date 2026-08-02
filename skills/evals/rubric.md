# Evaluation Rubric

Each scenario fixture is scored on eight dimensions, 1–5. Scores are awarded only where the
scenario run demonstrates the behavior; a missing demonstration is scored, not excused.

## Dimensions

1. **Relevance** — does the scenario map to a real PM job the skill claims to serve?
   - 5: exact match to a high-frequency PM job.
   - 1: the skill has no business being applied here.

2. **Correctness** — does the skill's method, applied faithfully, produce the verdict the
   evidence supports (judged against the scenario's ground truth)?
   - 5: verdict matches the evidence-grounded answer; no category errors.
   - 1: verdict is contradicted by the fixture's own evidence.

3. **Actionability** — does the output include a concrete next action, artifact, or decision
   the PM can execute?
   - 5: next action has what/who/by-when, and it follows from the verdict.
   - 1: output is descriptive only.

4. **Uncertainty handling** — are unknowns recorded as assumptions with effect, confidence
   capped honestly, and flip-evidence named?
   - 5: every unknown is an explicit assumption with effect; confidence and flip conditions present.
   - 1: unknowns silently padded or confidence inflated.

5. **Evidence use** — does the run use the shared taxonomy and rank evidence by
   claim-evidence match (including internal product evidence)?
   - 5: evidence typed, weighted by match, internal evidence treated as first-class.
   - 1: evidence ignored or published-source-biased.

6. **Proportionality** — does the skill scale its process to the decision's reversibility and stakes?
   - 5: fast/full mode selection matches the stakes; no ceremony for reversible calls.
   - 1: full ritual applied to a reversible, low-stakes call (or vice versa).

7. **Avoidance of framework theater** — does the output use the framework as a scaffold, not
   a performance? No forced-fit vocabulary, no required-but-useless fields.
   - 5: every framework element earns its place in the decision.
   - 1: vocabulary and structure substitute for substance.

8. **Clarity of final decision / next step** — is the final decision or next step unambiguous?
   - 5: one clear decision/next step; a reviewer could execute it.
   - 1: the output ends in a meeting, a memo, or a shrug.

## Scoring rule

A dimension is scored 1–5 based on the run record. Aggregate scores are the mean across
dimensions. **No scenario is awarded a perfect 5.0 unless every dimension demonstrates 5** —
the default expectation for this cycle is 3.0–4.2, with failures recorded, not hidden.

## Method of application

For each scenario, the authoring agent applied the relevant skill's Method section
step-by-step to the fixture inputs, following the skill's own instructions (recording
"unknown" as assumptions, applying the fast/full selection rule, rendering the output schema,
naming the next action). This is a **scripted self-run**, not an independent third-party
evaluation: it validates that the skills are internally consistent and usable on realistic
input, not that they outperform alternative tools. Independent structural and reasoning
review of the fixtures and skills by a second agent is recorded in
`../quality/ADVERSARIAL_REVIEW_2026-08-02.md`.
