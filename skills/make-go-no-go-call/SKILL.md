---
name: make-go-no-go-call
description: >-
  Produces a defensible verdict on whether an initiative should proceed, pause,
  or be killed, based on explicit evidence thresholds. Invoke when an initiative
  is about to receive budget, headcount, or a release slot; when an ongoing
  initiative has missed its evidence milestones and leadership must decide its
  fate; when two options compete for one scarce resource; when a sponsor is
  pushing to proceed despite low evidence; or at any review gate that needs a
  reproducible call. Returns GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK
  with the thresholds that were met or missed.
type: assess
version: 0.1.0
best_for:
  - "A proposed initiative is about to be funded or scheduled and needs a verdict before commitment"
  - "An ongoing initiative missed its evidence milestones and must be GO, killed, or paused"
  - "Two initiatives compete for one scarce resource and one must be rejected"
  - "A sponsor is pushing to proceed despite low evidence and the risk must be named"
  - "Quarterly planning, launch review, or kill review gates that need a reproducible call"
doctrine:
  - "PRN-0002, PRN-0003, PRN-0007, PRN-0009, PRN-0012"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 1: One-Way vs Two-Way Door; Framework 2: RICE-LM)"
  - "09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md, 09_tools/DECISION_MEMO_TEMPLATE.md, 09_tools/EVALUATION_CONTRACT_TEMPLATE.md"
  - "07_cases/case_catalog.md (CASE-0005, CASE-0018, CASE-0019)"
license: CC BY 4.0
---

## Purpose

This skill exists to make the GO/NO-GO call a decision, not a meeting. Academy
doctrine is unambiguous that strategy is what you say no to (PRN-0002), that
the most expensive decision is the one not made (PRN-0012), and that cost of
delay exceeds cost of imperfection in most decisions (PRN-0003). This skill
compresses those principles into a verdict contract with reproducible
thresholds so a second reviewer, or an agent, can reproduce the call from the
same inputs.

Invoke it when a commitment is imminent or a fate decision is pending. Do NOT
invoke it for pre-product-market-fit exploration where the strategy is
deliberately "find PMF by trying things" (PRN-0002 non-applicability), for
ranking a whole portfolio (use RICE-LM directly), or when the user actually
wants a document — in that case render the verdict first, then point to
`09_tools/DECISION_MEMO_TEMPLATE.md` for the write-up.

## Input

What the user should bring, in plain language. Empty-handed users get the
Method run with every unknown recorded as an assumption — the verdict will
then land on SEEK-MORE-EVIDENCE or PROCEED-AT-RISK, not GO.

- Initiative: what it is, one sentence, and the decision being asked.
- Strategy: the current written product strategy, or a statement that none
  exists (recorded as an assumption).
- Evidence: for each load-bearing claim (reach, impact, feasibility), what
  the claim is, what evidence tier backs it (A–E), and how confident you are
  (20% wild guess / 50% some data / 80% validated / 100% known — Framework 2
  confidence scale).
- Effort: person-months or relative scale.
- Value range: best / expected / worst case with probabilities summing to 100%.
- Failure risk: probability of complete failure, and the cost if it fails.
- Reversibility: is this Type-1 or Type-2 (Framework 1)? Or unknown.
- Cost of delay: what is lost per month of waiting.

## Method

One question at a time. If the user answers "unknown", record it as an explicit
assumption and continue — never silently assume.

1. **State the initiative and the decision.** Write the decision being asked
   in one sentence. If the decision is vague, stop and restate it before
   scoring anything.
2. **The strategy gate.** Is this initiative excluded by the current written
   strategy? PRN-0002: the test of a strategy is whether it prevents decisions
   that are individually tempting. If the strategy explicitly excludes it,
   record NO-GO now and stop — no score overrides the strategy gate. If there
   is no written strategy, record that as an assumption and continue (the
   verdict will be weakened).
3. **Classify reversibility.** Use Framework 1 (or the
   `classify-decision-reversibility` skill). A Type-1 decision cannot reach
   GO without an explicit reversibility design and a pre-mortem (Framework 1
   Type-1 rules).
4. **Score RICE-LM.** Base = (Reach × Impact × Confidence) / Effort, then the
   three multipliers L / M / S at 0.5x–2.0x (Framework 2). The multipliers
   are debated, not calculated — their purpose is to surface what pure RICE
   misses.
5. **Evidence audit.** For each load-bearing claim, record tier and
   confidence. Flag any load-bearing claim that is asserted with no evidence
   at all — that is the Theranos signature (CASE-0019: a thesis asserted,
   not validated).
6. **Risk-adjusted value.** Use `09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md`:
   expected value vs. build cost, risk of complete failure, reversibility,
   optionality, learning value. The adjusted score is an input to judgment,
   not the verdict.
7. **Cost-of-delay test.** PRN-0003 and PRN-0012: is the information that
   would improve the decision going to arrive in a relevant timeframe? If not,
   decide now. If yes, and the cost of waiting is low, SEEK-MORE-EVIDENCE or
   PAUSE may be the correct verdict rather than a decision.
8. **Render the verdict** against the Thresholds below, item by item, and
   report which thresholds were met and which were missed.
9. **If the verdict is PROCEED-AT-RISK**, stop and get explicit acceptance
   plus a named owner for the reversal plan before the call is considered made.

## Verdict Contract

WHAT THIS SKILL MUST RETURN. The output is a decision artifact, not a memo.

- **Verdict:** one of GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE /
  PROCEED-AT-RISK.
  - GO — proceed and commit resources.
  - NO-GO — do not proceed; explicitly reject (not defer).
  - PAUSE — do not proceed now, do not kill; a resolvable non-evidence
    blocker exists and will be re-reviewed on a date.
  - SEEK-MORE-EVIDENCE — the verdict cannot be rendered because a load-bearing
    claim is under-evidenced, but a discriminating test exists that can resolve
    it within a defined window. Returned with a specific evidence plan and a
    review date.
  - PROCEED-AT-RISK — the user declines the GO bar but insists on proceeding
    despite missed thresholds. This is a distinct, risky verdict, never a
    default, and always Low confidence.
- **Confidence:** High / Medium / Low with reasoning.
  - High: load-bearing evidence tier B or better at ≥ 50% confidence, and the
    call is not close.
  - Medium: material estimates rest on judgment rather than reference class.
  - Low: any load-bearing claim is tier D/E or asserted with no evidence; and
    always for PROCEED-AT-RISK.
- **Citations:** stable Academy doctrine/source IDs for each threshold
  evaluated (e.g. `PRN-0002`, `Framework 2`, `09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md`).
- **Stated assumptions:** everything the user answered "unknown" to, recorded
  explicitly with the impact each has on the verdict.
- **What would change the verdict:** the specific evidence that would flip the
  call (e.g. "NO-GO becomes GO if the strategy exclusion is removed in writing";
  "SEEK-MORE-EVIDENCE becomes GO if the pilot returns tier B evidence at ≥ 50%
  confidence").

## Thresholds

Reproducible criteria, evaluated in order. A second reviewer must be able to
reproduce the verdict from the same inputs.

**GO requires ALL of the following:**
1. Strategy gate passes: the initiative is not excluded by the written
   strategy (PRN-0002).
2. No RICE-LM multiplier scores 0.5x (no strategic, timing, or leverage trap —
   Framework 2).
3. Final RICE-LM ≥ the top-quartile boundary of the current portfolio, or —
   with no portfolio — ≥ a floor the decision-maker states BEFORE scoring.
4. Every load-bearing claim has evidence tier B or better AND confidence ≥ 50%
   (Framework 2 confidence scale).
5. Risk-adjusted value (expected value net of failure risk) is positive.
6. Reversibility: Type-2 (reversible), OR Type-1 with an explicit reversibility
   design and a completed pre-mortem (Framework 1, PRN-0007).

**NO-GO if ANY of the following:**
1. The strategy explicitly excludes the initiative (PRN-0002). No score
   overrides this.
2. Risk-adjusted expected value ≤ 0 net of failure risk.
3. A load-bearing claim is asserted with zero evidence, and removing that claim
   collapses the case (CASE-0019 non-falsifiability pattern).
4. Bottom-quartile RICE-LM (Framework 2 decision rules: bottom quartile is
   rejected, not deferred).

**SEEK-MORE-EVIDENCE if:**
- A load-bearing claim sits below the GO bar (tier C/D/E or confidence < 50%),
  AND a discriminating test exists that can resolve the ambiguity within a
  defined window (PRN-0014: design a test that discriminates between
  interpretations — do not demand more of the same data). Return the evidence
  plan, owner, and review date. Do not use it as disguised indecision: if no
  test exists and the cost of waiting is high, decide (PRN-0003, PRN-0012).

**PAUSE if:**
- Evidence is at or above the GO bar, but a resolvable non-evidence blocker
  exists (dependency blocked, resource conflict, strategy under formal review,
  org change pending). Return the blocker, the owner, and the re-review date.

**PROCEED-AT-RISK if:**
- The user declines the GO bar and directs proceeding anyway. Required output:
  (a) a list of the exact thresholds missed, (b) explicit written acceptance,
  (c) a named owner for a reversal plan with a tested trigger (PRN-0007), and
  (d) confidence labeled Low. This verdict must be surfaced as a decision that
  carries risk, never normalized.

## Evidence & Doctrine

Academy references, cited not copied.

- `PRN-0002` (Strategy Is What You Say No To) — the strategy gate. Tier A
  doctrine (high confidence). `01_core_doctrine/PRINCIPLES.md`.
- `PRN-0003` (Cost of Delay Exceeds Cost of Imperfection) — the delay test and
  its hard boundary for irreversible/catastrophic decisions. Tier A.
- `PRN-0007` (Best Product Decisions Are Reversible by Design) — GO condition 6
  and the PROCEED-AT-RISK reversal plan. Tier A.
- `PRN-0009` (Platform Decisions Are the Most Consequential) — raises the
  evidence bar for platform-class initiatives; if the initiative is a platform
  decision, treat it as Type-1 unless proven otherwise. Tier A.
- `PRN-0012` (Most Expensive Decision Is the One You Do Not Make) — against
  disguised indecision in SEEK-MORE-EVIDENCE. Tier A.
- `01_core_doctrine/DECISION_FRAMEWORKS.md` — Framework 1 (Type 1/Type 2 rules:
  ≤ 10% of implementation cost on analysis for Type-2, pre-mortem + escalation
  for Type-1) and Framework 2 (RICE-LM decision rules: top quartile resource,
  bottom quartile reject, 0.5x multipliers are traps).
- `09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md` — the risk-adjusted value step.
- `07_cases/case_catalog.md` — CASE-0005 (Knight Capital: proceeding on a
  routine deployment without safety evidence; causal_confidence high), CASE-0018
  (Boeing 737 MAX: competitive pressure overrode the evidence bar; causal_confidence
  high), CASE-0019 (Theranos: load-bearing claim asserted with zero evidence;
  causal_confidence high). Cite by CASE id when calibrating a failure scenario.

## Common Pitfalls

- **Strategy as a wish list.** GO because no one wrote the "no". Correction:
  run the PRN-0002 Exclusion Test — a strategy must name 5 things it will not
  do; if it cannot, treat the strategy gate as unmet.
- **Deciding fast on everything.** Applying PRN-0003 to a Type-1 decision
  (Boeing pattern). Correction: run Framework 1 first; Type-1 decisions need
  a pre-mortem and escalation before GO.
- **Proceeding anyway, unlabeled.** The most common real failure is proceeding
  with low evidence while calling it GO. Correction: force the distinct
  PROCEED-AT-RISK verdict and name the missed thresholds.
- **False precision in RICE.** Treating the score as a measurement instead of
  a structured conversation (Framework 2 failure mode). Correction: report the
  score as a range and debate the multipliers explicitly.
- **Survivorship bias.** "The last one worked." Past success is not a
  probability estimate (PRN-0003 failure mode). Correction: calibrate
  probabilities against reference classes, not anecdotes.
- **Disguised indecision.** "More evidence" when the disagreement is about
  interpretation, not information (PRN-0014 failure mode). Correction:
  SEEK-MORE-EVIDENCE is only valid when a discriminating test exists.

## Related Skills

- `classify-decision-reversibility` — run before this skill; GO condition 6
  depends on its Type-1/Type-2 classification.
- `run-case-based-premortem` — required for Type-1 decisions before GO; its
  ranked scenarios feed the risk-adjusted value step.
- After the verdict, hand the artifact to `09_tools/DECISION_MEMO_TEMPLATE.md`
  for the stakeholder write-up and to `09_tools/EVALUATION_CONTRACT_TEMPLATE.md`
  to lock the success and counter-metrics that the GO depends on.
