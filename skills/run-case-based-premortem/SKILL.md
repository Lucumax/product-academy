---
name: run-case-based-premortem
description: >-
  Assumes a decision, launch, or initiative has failed badly, then produces a RANKED set of
  failure scenarios (probability × severity) with mitigations, early warning signals, and
  owners — calibrated against real Academy cases (Knight Capital, Boeing 737 MAX, Theranos,
  Netflix Qwikster). Invoke before any significant commitment, before any Type-1 decision
  (Framework 1 makes it mandatory), when a team is overly confident, before a launch or
  planning cycle. Overcomes optimism bias by asking "it failed — why?", not "what could go wrong?".
type: assist
version: 0.2.0
best_for:
  - "A Type-1 (irreversible) decision is about to be made and a premortem is required by Framework 1"
  - "A high-confidence team about to commit — the premortem is a bias-correction tool"
  - "Before a launch, quarter, or any significant resource commitment"
  - "Pressure-testing a decision memo before it is finalized"
  - "Simulator practice that requires a multi-path pre-mortem"
doctrine:
  - "09_tools/PRE_MORTEM_TEMPLATE.md"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 8: FMEA for Product Decisions)"
  - "07_cases/case_catalog.md (CASE-0001, CASE-0005, CASE-0018, CASE-0019)"
  - "PRN-0003, PRN-0007"
license: CC BY 4.0
---

## Purpose

This skill makes the premortem a decision instrument with ranked output, not a brainstorm.
It asks "it failed — why?" and produces specific causal narratives (not risk categories),
early warning signals, and mitigations with named owners. Two things distinguish it from a
generic premortem template: it RANKS the failure scenarios by probability × severity, and it
CALIBRATES each scenario against a real Academy case so the user can say "this is the Knight
Capital pattern" rather than "bad things might happen."

Invoke it before a significant commitment, before a Type-1 decision (mandatory per Framework
1), when a team is overconfident, or before a launch or planning cycle. Do NOT invoke it for
reversible, low-stakes decisions where the cost of the ritual exceeds the value of what it
protects (PRN-0003), and do not run it when the user wants a document — the output is the
ranked scenario table and verdict, not a report.

## Use when

- A Type-1 (irreversible) decision is about to be made and a premortem is required.
- A high-confidence team is about to commit — the premortem is a bias-correction tool.
- Before a launch, quarter, or any significant resource commitment.
- Pressure-testing a decision memo before it is finalized.
- Any decision where optimism is highest and scrutiny is lowest.

## Do not use when

- Reversible, low-stakes decisions where the ritual costs more than it protects (PRN-0003).
- The user wants a document — render the ranked table and verdict, then write it up.
- The team cannot produce specific narratives and will not be pressed to — a "50% for
  everything" or category-level premortem is a performance, not a decision tool.
- Pre-PMF exploration where "try things and learn" already prices in failure — a premortem on
  each micro-experiment is overhead.

## Inputs

Required inputs:

- Decision: the decision, launch, or initiative being premortemed.
- Scenario date: when the failure is imagined to be visible (template suggests 12–18 months out).
- Stakeholders: who would be affected by failure.
- Key assumptions: the load-bearing claims the plan rests on.

Optional inputs:

- Known failure history: similar initiatives that failed, in this organization or elsewhere (for probability calibration).
- The reversibility classification (TYPE-1/TYPE-2) if already done.

## Missing-data behavior

- "Unknown" on a load-bearing assumption must appear in the assumption-inversion step — an
  unexamined load-bearing assumption is itself a top failure scenario.
- No failure history → record that probabilities are uncalibrated; use base rates from the
  catalog or state the assumption explicitly. Never substitute confidence for calibration.

## Context classification

- **TYPE-1, high stakes:** Full mode mandatory — case calibration, exposure ranking,
  assumption inversion, reversibility assessment, no-go conditions.
- **TYPE-2, moderate stakes:** Fast mode — top-3 scenarios, signals, owners, no catalog
  calibration required.
- **Pre-launch / overconfident team:** Full mode; the point is bias correction, so push on
  organizational and market failure modes, not just technical ones.

## Fast mode

Run for moderate-stakes, reversible decisions, or as a first pass. Five steps:

1. Set the scenario: "It is [date]. We [decision]. It failed. Consequences included [consequences]."
2. Elicit 3 failure narratives (headline + causal chain + severity 1–5). Enforce specificity — "the project was late" is not a narrative.
3. Estimate probability for each (reference-calibrated where possible).
4. Compute exposure = severity × probability; rank descending.
5. Design one early warning signal and one mitigation with an owner for the top scenario only.

Output: the ranked table (top-3) and a provisional DEFENSIBLE / DEFENSIBLE-WITH-MITIGATIONS /
NOT-DEFENSIBLE verdict. No catalog calibration, no assumption-inversion step. If the top
scenario cannot be mitigated or the team produced only categories, escalate to Full mode.

## Full mode

Adds to fast mode:

1. Elicit 3–5 failure narratives covering technical, organizational, and external-stakeholder
   failure modes (template common mistake 3; the SCENARIO_03 rubric requires one of each).
2. Pattern-match each top scenario to an Academy case only when the mechanism is actually
   present (see pattern-inflation guard below).
3. Compute exposure, rank descending.
4. Design early warning signals (observable 4–8 weeks before failure) and mitigations with
   named owners, cadence, and triggers, using FMEA logic (reduce probability, reduce severity,
   improve detectability).
5. Run assumption inversion and the reversibility assessment (template §6–7), including the
   point of no return.
6. Render the ranked table and verdict. The ranked scenarios become a monitoring plan with
   owners, not a filed document.

## Method

One question at a time. "Unknown" answers become explicit assumptions, never silent defaults.

1. Set the scenario (template §1). Write it specifically: "It is [date]. We [decision]. It failed. The failure was visible to [stakeholders]. The consequences included [consequences]." Vague scenarios produce vague premortems.
2. Elicit 3–5 failure narratives (template §2). Each needs a headline, a causal chain from root cause to visible failure, why we did not see it coming, who was affected, and severity 1–5. Enforce specificity; include organizational and market failures, not just technical ones.
3. Estimate probability for each narrative. Calibrate, do not guess: reference classes and base rates from similar initiatives. Counter the default optimism.
4. Compute exposure = severity × probability; rank descending. Keep the ranking; it is the contract of this skill.
5. Pattern-match each top scenario to an Academy case. The case pattern requires its mechanism: untested reversal mechanism / speed without assurance = Knight Capital (CASE-0005); change communicated without the customer's mental model = Qwikster (CASE-0001); non-falsifiable thesis insulated from verification = Theranos (CASE-0019); competitive pressure overriding irreversibility = Boeing 737 MAX (CASE-0018). Name the case and its causal_confidence only when the mechanism is actually present.
6. Design early warning signals (template §4) for each ranked scenario: a leading metric, a qualitative signal, an external signal, observable 4–8 weeks before the failure becomes obvious.
7. Design mitigations (template §5) with what to monitor, cadence, a NAMED owner, a specific trigger, and the action taken. Use the FMEA logic: reduce probability, reduce severity/blast radius, or improve detectability.
8. Run assumption inversion (template §6) and the reversibility assessment (template §7) for the plan as a whole, including the point of no return.
9. Render the ranked table and verdict against the contract. The ranked scenarios become a monitoring plan with owners, not a filed document.

## Evidence classification

Uses the shared taxonomy. Failure-narrative probabilities are best calibrated against
reference classes (E9 market evidence, E10 operational incident history, E11 financial
evidence for cost of failure). Case pattern matches are practitioner evidence (E12) and only
valid when the mechanism is present. An "unknown" on a load-bearing assumption is E15 until
resolved.

## Output schema

```json
{
  "skill": "run-case-based-premortem",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "DEFENSIBLE | DEFENSIBLE-WITH-MITIGATIONS | NOT-DEFENSIBLE",
  "ranked_scenarios": [
    {"scenario": "...", "severity": 4, "probability": 0.3, "exposure": 1.2,
     "case_pattern": "CASE-0005 | none", "early_warning_signal": "...",
     "mitigation": "...", "owner": "...", "trigger": "..."}
  ],
  "confidence": "high | medium | low",
  "evidence_basis": ["E9", "E10", "E11"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Ranked failure scenarios:** a table of the top 3–5 scenarios, each with probability,
  severity, exposure, the matched Academy case, its early warning signals, and its mitigation
  with owner and trigger, sorted by exposure.
- **Verdict:** `DEFENSIBLE` (residual exposure of every top-3 scenario at or below the
  acceptable threshold after mitigations are in place and owned) /
  `DEFENSIBLE-WITH-MITIGATIONS` (the decision holds only if the named mitigations, owners, and
  triggers land; each is a condition, not a hope) / `NOT-DEFENSIBLE` (at least one top
  scenario cannot be mitigated below the threshold, or a no-go condition is present).
- **Exposure = Severity (1–5) × Probability (0–100%).** Probability is reference-calibrated,
  not negotiated.
- **Acceptable residual exposure:** after mitigations, no top-3 scenario may retain severity
  ≥ 4 with probability ≥ 25% *(rule of thumb for a moderate-stakes product decision — tighten
  for safety/money-moving systems, loosen for exploratory bets)*. High-severity failure modes
  require mitigation regardless of probability (Framework 8).
- **NOT-DEFENSIBLE if ANY of:** a top-3 scenario has severity ≥ 4 AND probability ≥ 40% with
  no mitigation bringing residual below severity-4/probability-25% *(thresholds are
  heuristics — the intent is "a probable, severe, unmitigated failure"; adjust for the
  decision's stakes)*; a top-3 scenario describes irreversible harm and proceeds without
  addressing the root cause (Boeing/Theranos condition); every scenario matches the same root
  cause and the plan does not diversify against it.
- **Confidence:** High when narratives are specific and probabilities reference-calibrated;
  Low when the team produced risk categories instead of narratives or "50% for everything."
- **Assumptions:** everything answered "unknown," with impact on the verdict.
- **What would change the verdict:** the evidence or action that would flip it (e.g.
  "NOT-DEFENSIBLE becomes DEFENSIBLE-WITH-MITIGATIONS if the team adds a tested kill-switch
  and names a trigger authority").
- **Next action:** the ranked table becomes a monitoring plan — schedule the cadence, assign
  the owners, and set the review trigger.

### Worked example

Decision: "Ship the AI triage assistant to all enterprise customers next quarter." Scenarios:
(1) silent-failure harm — the assistant confidently mis-triages a customer-critical issue,
severity 5, probability 30%, exposure 1.5 → pattern CASE-0019-analog (launch without
validation), mitigation: monitored evaluation contract with human-review sampling and a
rollback trigger, owner: AI PM, trigger: error rate > 3% over 48h → residual below threshold.
(2) Sales overpromising — competitive pressure ships capabilities the assistant cannot
deliver, severity 4, probability 40% → pattern CASE-0018-analog (competitive pressure
overriding assurance), mitigation: launch-scope sign-off from Sales with named escalation,
owner: head of Sales, trigger: first overpromise complaint. (3) Org blind spot — no one owns
the model's degradation monitoring, severity 4, probability 50% → no case match, mitigation:
named monitoring owner + weekly review, trigger: shift-detection alert. Verdict:
DEFENSIBLE-WITH-MITIGATIONS — the decision holds only if the three mitigations land.
Confidence: Medium (probabilities partly uncalibrated; no prior AI-launch failure history).

## Failure modes

- **Pre-mortem as generic risk list.** "The project was late" is a category, not a narrative. Correction: force named characters, mechanisms, and dates; a narrative that cannot be dated cannot have early warning signals.
- **Doom session without mitigations.** The goal is not to feel bad; every narrative must produce a signal and an action. Correction: end each scenario with a named owner and trigger, or it does not count.
- **Technical-only failure modes.** Missing organizational, political, and market failures. Correction: require at least one organizational and one external-stakeholder scenario.
- **Uncalibrated probabilities.** "50% for everything because I'm uncertain," or past-success optimism. Correction: use reference classes; where none exist, state the base-rate assumption explicitly.
- **Pattern-name inflation.** Claiming "this is the Knight Capital pattern" without the mechanism being present. Correction: the Knight pattern requires an untested/owned reversal mechanism; the Theranos pattern requires insulation from verification. Name the case only when the mechanism matches.
- **Pre-mortem without follow-through.** No owners, no cadence, filed and forgotten. Correction: the ranked table becomes the monitoring plan; signals are reviewed on the named cadence and mitigations executed on trigger.
- **One-time exercise.** Correction: re-run when the decision changes or a signal fires.

## Reversal conditions

- A named early warning signal fires → execute the mitigation on trigger.
- The decision changes materially (scope, timeline, key assumptions) → re-run the premortem.
- A mitigation owner changes without handover → the plan is void until reassigned.
- Post-launch, a failure mode not on the table appears → add it and re-rank.

## Composition hooks

- **before:** `classify-decision-reversibility` (every TYPE-1 must premortem before commit);
  `scan-contradictions-assumptions` (top assumptions become failure narratives);
  `pressure-test-product-thesis` (a non-falsifiable thesis is a premortem scenario);
  `check-ai-evaluation-contract` (for AI bets, contract gaps are premortem scenarios).
- **after:** `make-go-no-go-call` (ranked scenarios and verdict feed the risk-adjusted value
  step and the GO conditions); `align-stakeholders-on-decision` (mitigation owners are
  stakeholders who must sign).
- **workflow:** product-bet (step 6), launch-gate (step 3).

## Related Skills

- `classify-decision-reversibility` — every TYPE-1 decision is required to run this premortem before commitment.
- `make-go-no-go-call` — this skill's ranked scenarios feed the risk-adjusted value step and the GO conditions.
- `scan-contradictions-assumptions` — the assumptions it surfaces become failure narratives.
- `check-ai-evaluation-contract` — AI bets: contract gaps are the top premortem scenarios.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
