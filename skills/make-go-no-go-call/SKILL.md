---
name: make-go-no-go-call
description: >-
  Produces a defensible verdict on whether an initiative should proceed, pause, be killed, or
  seek more evidence, based on explicit thresholds. Invoke when an initiative is about to
  receive budget, headcount, or a release slot; when an ongoing initiative missed its evidence
  milestones; when two options compete for one scarce resource; when a sponsor pushes to
  proceed despite low evidence; or at any review gate that needs a reproducible call. Returns
  GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK with the thresholds met or missed.
type: assess
version: 0.2.0
best_for:
  - "A proposed initiative is about to be funded or scheduled and needs a verdict before commitment"
  - "An ongoing initiative missed its evidence milestones and must be GO, killed, or paused"
  - "Two initiatives compete for one scarce resource and one must be rejected"
  - "A sponsor is pushing to proceed despite low evidence and the risk must be named"
  - "Quarterly planning, launch review, or kill review gates that need a reproducible call"
doctrine:
  - "PRN-0002 (strategy is what you say no to)"
  - "PRN-0003 (cost of delay exceeds cost of imperfection)"
  - "PRN-0007 (reversible by design)"
  - "PRN-0012 (most expensive decision is the one you do not make)"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 1 one-way/two-way door; Framework 2 RICE-LM)"
  - "09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md"
  - "07_cases/case_catalog.md (CASE-0005, CASE-0018, CASE-0019)"
license: CC BY 4.0
---

## Purpose

This skill makes the GO/NO-GO call a decision, not a meeting. Strategy is what you say no to
(PRN-0002); the most expensive decision is the one not made (PRN-0012); cost of delay exceeds
cost of imperfection in most decisions (PRN-0003). This skill compresses those principles
into a verdict contract with reproducible thresholds so a second reviewer, or an agent, can
reproduce the call from the same inputs.

Invoke it when a commitment is imminent or a fate decision is pending. Do NOT invoke it for
pre-PMF exploration where the strategy is deliberately "find PMF by trying things"; for
ranking a whole portfolio (use prioritization, then bring the top candidate here); or when the
user actually wants a document — render the verdict first, then point to
`09_tools/DECISION_MEMO_TEMPLATE.md`.

## Use when

- An initiative is about to receive budget, headcount, or a release slot.
- An ongoing initiative missed its evidence milestones and its fate is being decided.
- Two initiatives compete for one scarce resource.
- A sponsor pushes to proceed despite low evidence and the risk must be named.
- Any review gate needs a reproducible call.

## Do not use when

- Pre-PMF exploration where "try things and learn" is the strategy (PRN-0003 non-applicability).
- Ranking a whole portfolio — use `prioritize-product-opportunities` first, then call the top candidate.
- The user wants a decision memo — render the verdict, then write the memo.
- The decision is reversible and low-stakes (a routine, two-way-door feature with bounded
  downside) — Fast mode gives a verdict in minutes; if even that feels heavy, the call is
  already made and this skill is optional.

## Inputs

Required inputs:

- Initiative: what it is, one sentence, and the decision being asked.
- Strategy: the current written product strategy, or a statement that none exists (recorded as an assumption).
- For each load-bearing claim (reach, impact, feasibility): the evidence type + confidence (20% wild guess / 50% some data / 80% validated / 100% known — Framework 2 scale).
- Effort: person-months or relative scale.

Optional inputs:

- Value range (best/expected/worst with probabilities), failure risk and cost, reversibility
  class, cost of delay, the portfolio boundary (top-quartile RICE-LM), and the premortem
  output if run.

## Missing-data behavior

- A load-bearing claim with no evidence is flagged (the Theranos signature, CASE-0019) — it is
  `SEEK-MORE-EVIDENCE` or `PROCEED-AT-RISK` territory, never a silent pass.
- "Unknown" on reversibility → treat as TYPE-1 for threshold purposes until classified
  (`classify-decision-reversibility`).
- "Unknown" on strategy → the strategy gate is recorded as unmet; the verdict is weakened.
- No portfolio boundary → GO requires a stated floor set BEFORE scoring, or the call defaults
  to SEEK-MORE-EVIDENCE on the RICE-LM threshold.

## Context classification

- **TYPE-2, low stakes, reversible:** Fast mode. The verdict can be GO or CONDITIONAL quickly;
  analysis budget ≤ 10% of implementation cost.
- **TYPE-1, irreversible, high stakes:** Full mode mandatory — strategy gate, premortem,
  risk-adjusted value, escalation.
- **Portfolio competition:** Full mode with explicit comparison against the boundary.

## Fast mode

Run for reversible or ordinary decisions. Four questions, provisional verdict:

1. State the initiative and the decision.
2. Strategy gate: is this excluded by the written strategy? If explicitly excluded → NO-GO, stop.
3. Reversibility: is it TYPE-2 (reversible)? If TYPE-1 or unknown → Fast mode is not
   appropriate; escalate to Full mode.
4. Load-bearing claims: name each claim's evidence type and confidence (wild guess / some
   data / validated / known). Any claim with no evidence → flag. Does value plausibly exceed
   cost, with failure risk bounded? (A one-line "yes/no/unclear" is enough — no worksheets.)

Render provisional verdict: `GO` (reversible, all load-bearing claims have at least some
evidence, value plausibly exceeds cost) / `PAUSE` (evidence fine, a resolvable blocker) /
`SEEK-MORE-EVIDENCE` (a load-bearing claim is weak and a cheap discriminating test exists) /
`NO-GO` (strategy exclusion or expected value clearly negative).

Confidence is capped at Medium in Fast mode. Next action: name the weakest claim and the
cheapest test that would firm it, or the blocker owner and review date. No RICE-LM scoring,
no risk-adjusted value worksheet, no premortem.

## Full mode

Adds to fast mode, in order:

1. Strategy gate with the PRN-0002 Exclusion Test — the strategy must name things it will not do.
2. Reversibility classification via `classify-decision-reversibility` (TYPE-1 requires reversibility design + premortem before GO).
3. RICE-LM scoring with explicit multiplier debate (Framework 2) — the score is a structured conversation, not a measurement.
4. Evidence audit per load-bearing claim (evidence type from the shared taxonomy + confidence).
5. Risk-adjusted value (expected value net of failure risk; use the Academy's
   `09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md` worksheet if available, or the method inline:
   expected value − build cost − failure risk × cost of failure, with reversibility and
   optionality noted as adjustments).
6. Cost-of-delay test (PRN-0003/PRN-0012): would the information that improves the decision arrive in a relevant timeframe? If not, decide now.
7. Render the verdict against the thresholds, item by item, and report which were met/missed.
8. If PROCEED-AT-RISK: stop and get explicit acceptance plus a named reversal owner before the call is considered made.

## Method

One question at a time. "Unknown" answers are recorded as explicit assumptions and the review continues.

1. State the initiative and the decision being asked. If the decision is vague, restate it before scoring anything.
2. Strategy gate: is this initiative excluded by the current written strategy? If excluded → NO-GO, stop. No score overrides the strategy gate.
3. Classify reversibility (Framework 1 or `classify-decision-reversibility`). A TYPE-1 decision cannot reach GO without an explicit reversibility design and a completed premortem.
4. Score RICE-LM: Base = (Reach × Impact × Confidence) / Effort, then the L/M/S multipliers at 0.5x–2.0x. The multipliers are debated, not calculated — their purpose is to surface what pure RICE misses.
5. Evidence audit: for each load-bearing claim, record evidence type and confidence. Flag any claim asserted with no evidence at all — the Theranos signature (CASE-0019).
6. Risk-adjusted value: expected value vs build cost, risk of complete failure, reversibility, optionality, learning value. The adjusted score is input to judgment, not the verdict.
7. Cost-of-delay test: is the information that would improve the decision going to arrive in a relevant timeframe? If not, decide now. If yes and waiting is cheap, SEEK-MORE-EVIDENCE or PAUSE may be correct.
8. Render the verdict against the Thresholds, item by item, and report which thresholds were met and missed.
9. If PROCEED-AT-RISK: stop and get explicit acceptance plus a named owner for the reversal plan before the call is considered made.

## Evidence classification

Uses the shared taxonomy. Evidence adequacy is graded per claim: reach claims want market or
analytics evidence (E9, E3); impact claims want behavioral or cohort evidence (E3, E4) or an
experiment (E1); feasibility claims want engineering/operational evidence (E10, E11, E3). A
"load-bearing claim at ≥ 50% confidence with evidence tier E13/E1 or internal E3/E4" clears
the GO bar; a claim backed only by unsupported assertion (E15) or interviews (E5) does not.

## Output schema

```json
{
  "skill": "make-go-no-go-call",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "GO | NO-GO | PAUSE | SEEK-MORE-EVIDENCE | PROCEED-AT-RISK",
  "confidence": "high | medium | low",
  "thresholds_evaluated": [{"threshold": "...", "met": false}],
  "evidence_basis": ["E3", "E4"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict:** one of
  - `GO` — proceed and commit resources.
  - `NO-GO` — do not proceed; explicitly reject (not defer).
  - `PAUSE` — do not proceed now, do not kill; a resolvable non-evidence blocker exists and will be re-reviewed on a date.
  - `SEEK-MORE-EVIDENCE` — a load-bearing claim is under-evidenced but a discriminating test can resolve it within a defined window. Returns an evidence plan, owner, and review date. Never disguised indecision.
  - `PROCEED-AT-RISK` — the user declines the GO bar but insists on proceeding despite missed thresholds. Always Low confidence, never a default, requires explicit acceptance + a named reversal owner.
- **GO requires ALL of:** (1) strategy gate passes; (2) no RICE-LM multiplier at 0.5x; (3) RICE-LM at or above the stated boundary/floor; (4) every load-bearing claim has adequate-type evidence at ≥ 50% confidence *(rule of thumb — lower the bar only with explicit written risk acceptance, raise it for irreversible bets)*; (5) risk-adjusted value positive; (6) TYPE-2, or TYPE-1 with reversibility design and completed premortem.
- **NO-GO if ANY of:** strategy explicitly excludes it; risk-adjusted expected value ≤ 0; a load-bearing claim has zero evidence and removing it collapses the case; bottom-quartile RICE-LM.
- **SEEK-MORE-EVIDENCE if:** a load-bearing claim is below the GO bar AND a discriminating test exists within a defined window. If no test exists and waiting is expensive, decide (PRN-0003, PRN-0012).
- **PAUSE if:** evidence clears the GO bar but a resolvable non-evidence blocker exists (dependency, resource conflict, strategy under review, org change). Returns the blocker, owner, and re-review date.
- **Confidence:** High (load-bearing evidence adequate-type at ≥ 50% confidence, call not close); Medium (material estimates rest on judgment); Low (any load-bearing claim is weak or asserted; always for PROCEED-AT-RISK).
- **Evidence basis:** taxonomy types per claim.
- **Assumptions:** every "unknown," with effect on the verdict.
- **What would change the verdict:** named evidence per threshold (e.g. "NO-GO becomes GO if the strategy exclusion is removed in writing"; "SEEK-MORE-EVIDENCE becomes GO if the pilot returns cohort evidence at ≥ 50% confidence").
- **Next action:** the verdict's mandated step — commit, reject, re-review date, evidence plan with owner, or explicit risk acceptance.

### Worked example

Decision: "Fund the AI triage assistant as a $2M bet this quarter." To show the threshold
ladder rather than only the strategy gate, assume the strategy **allows** customer-facing AI
if it has a monitored evaluation contract. Walk the GO conditions:

1. **Strategy gate:** passes (with the monitored-contract condition attached).
2. **RICE-LM multipliers:** reach multiplier 0.5x — the assistant targets a narrow support
   segment with no distribution plan → a trap (condition 2 fails).
3. **RICE-LM boundary:** with no portfolio, the team must state a floor before scoring; they
   decline → treated as unmet (condition 3 fails).
4. **Load-bearing claims:** "accuracy meets the bar" — no evaluation contract yet, only a
   demo (E15) → below the adequate-type ≥ 50% confidence bar (condition 4 fails); "adoption"
   — one pilot with cohort evidence (E4, 80% confidence) passes.
5. **Risk-adjusted value:** expected value net of failure risk is positive but hinges on the
   accuracy claim that has no evidence (condition 5 fails on a load-bearing assumption).
6. **Reversibility:** the $2M build is flag-gated → TYPE-2 (condition 6 passes).

Verdict: `SEEK-MORE-EVIDENCE` — a discriminating test exists: run `check-ai-evaluation-contract`
and a flag-gated pilot with human-review sampling; if the contract is CONTRACT-COMPLETE and
the pilot returns cohort evidence (E4) at ≥ 80% on the accuracy claim, re-run the ladder and
expect GO. If no contract can be written in the window, `NO-GO` — deciding on the demo is the
Theranos pattern (CASE-0019). Next action: draft the evaluation contract (owner: AI PM, by
next Friday) and schedule the pilot. Flip: the contract plus pilot cohort evidence.

This demonstrates the ladder: the strategy gate alone would have stopped too early either way;
the multiplier, boundary, evidence, and value thresholds are what actually carried the call.

## Failure modes

- **Strategy as a wish list.** GO because no one wrote the "no." Correction: run the PRN-0002 Exclusion Test — a strategy must name things it will not do.
- **Deciding fast on everything.** Applying PRN-0003 to a Type-1 decision (Boeing pattern). Correction: run Framework 1 first; Type-1 needs a premortem and escalation before GO.
- **Proceeding anyway, unlabeled.** Proceeding with low evidence while calling it GO. Correction: force the distinct PROCEED-AT-RISK verdict and name the missed thresholds.
- **False precision in RICE.** Treating the score as a measurement instead of a structured conversation. Correction: report the score as a range and debate the multipliers explicitly.
- **Survivorship bias.** "The last one worked." Correction: calibrate probabilities against reference classes, not anecdotes.
- **Disguised indecision.** "More evidence" when the disagreement is about interpretation, not information (PRN-0014). Correction: SEEK-MORE-EVIDENCE is only valid when a discriminating test exists.
- **Process for reversible calls.** A full RICE-LM + risk-adjusted-value ceremony for a two-way door. Correction: Fast mode is the default for TYPE-2.

## Reversal conditions

- A strategy exclusion is removed or added in writing.
- The discriminating test resolves a load-bearing claim the other way.
- A blocker clears (PAUSE → GO) or a re-review date arrives.
- A PROCEED-AT-RISK initiative misses its evidence milestones — the named reversal plan triggers.

## Composition hooks

- **before:** `classify-decision-reversibility` (GO condition 6); `frame-product-problem` (problem and business outcome stated); `prioritize-product-opportunities` (the candidate is ranked); `audit-decision-evidence` (evidence gate); `run-case-based-premortem` (TYPE-1 requirement, feeds risk-adjusted value); `pressure-test-product-thesis` (is the bet falsifiable?); `check-ai-evaluation-contract` (AI bets).
- **after:** `align-stakeholders-on-decision` (the verdict needs stakeholder sign-off); `09_tools/DECISION_MEMO_TEMPLATE.md` (write-up).
- **workflow:** product-bet (step 7), launch-gate (step 6).

## Related Skills

- `classify-decision-reversibility` — run before; GO condition 6 depends on its classification.
- `run-case-based-premortem` — required for TYPE-1 before GO.
- `audit-decision-evidence` — the evidence gate this verdict consumes.
- `pressure-test-product-thesis` — is the underlying bet falsifiable?
- `check-ai-evaluation-contract` — AI bets: GO requires a monitored contract.
- `_shared/SKILL_CONTRACT.md` — evidence taxonomy and output schema.
