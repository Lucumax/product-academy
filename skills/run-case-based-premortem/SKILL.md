---
name: run-case-based-premortem
description: >-
  Assumes a decision, launch, or initiative has failed badly, then produces a
  RANKED set of failure scenarios (probability x severity) with mitigations,
  early warning signals, and owners — calibrated explicitly against real
  Academy cases (Knight Capital, Boeing 737 MAX, Theranos, Netflix Qwikster).
  Invoke before any significant commitment, before any Type-1 decision (where
  Framework 1 makes it mandatory), when a team is overly confident, before a
  launch or planning cycle, and for simulator scenarios that require a
  pre-mortem. Overcomes optimism bias by asking "it failed — why?", not "what
  could go wrong?".
type: assist
version: 0.1.0
best_for:
  - "A Type-1 (irreversible) decision is about to be made and a pre-mortem is required by Framework 1"
  - "A high-confidence team about to commit — the pre-mortem is a bias-correction tool"
  - "Before a launch, quarter, or any significant resource commitment"
  - "Pressure-testing a decision memo before it is finalized"
  - "Simulator practice that requires a multi-path pre-mortem (e.g. SCENARIO_03 AI severe failures)"
doctrine:
  - "09_tools/PRE_MORTEM_TEMPLATE.md"
  - "01_core_doctrine/DECISION_FRAMEWORKS.md (Framework 8: FMEA for Product Decisions)"
  - "07_cases/case_catalog.md (CASE-0001, CASE-0005, CASE-0018, CASE-0019 — causal_confidence framing)"
  - "PRN-0003, PRN-0007"
license: CC BY 4.0
---

## Purpose

This skill exists to make the pre-mortem a decision instrument with ranked
output, not a brainstorm. The Academy's `09_tools/PRE_MORTEM_TEMPLATE.md`
establishes the discipline: frame it as "it failed — why?", write specific
causal narratives (not risk categories), produce early warning signals and
mitigations with named owners, and never file it away after one session. This
skill adds two things the template does not: it RANKS the failure scenarios by
probability x severity, and it CALIBRATES each scenario against a real Academy
case so the user can say "this is the Knight Capital pattern" rather than "bad
things might happen".

Invoke it before a significant commitment, before a Type-1 decision (mandatory
per Framework 1), when a team is overconfident, or before launch/quarterly
planning. Do NOT invoke it for reversible, low-stakes decisions where the cost
of the ritual exceeds the value of what it protects (PRN-0003), and do not run
it when the user wants a document — the output is the ranked scenario table and
verdict, not a report.

## Input

What the user should bring, in plain language:

- Decision: the decision, launch, or initiative being pre-mortemed.
- Scenario date: when the failure is imagined to be visible (the template
  suggests 12–18 months out).
- Stakeholders: who would be affected by failure.
- Key assumptions: the load-bearing claims the plan rests on.
- Known failure history: similar initiatives that failed, in this organization
  or elsewhere (used for probability calibration).
- If the user does not know some of these, record them as assumptions and
  continue — but an "unknown" answer on a load-bearing assumption must appear
  in the assumption-inversion step.

## Method

One question at a time. "Unknown" answers become explicit assumptions, never
silent defaults.

1. **Set the scenario** (template §1). Write it specifically: "It is [date]. We
   [decision]. It failed. The failure was visible to [stakeholders]. The
   consequences included [consequences]." Vague scenarios produce vague
   pre-mortems.
2. **Elicit 3–5 failure narratives** (template §2). Each needs a headline, a
   causal chain from root cause to visible failure, why we did not see it
   coming, who was affected, and severity 1–5. Enforce specificity: "the
   project was late" is not a narrative; "the compliance work uncovered a data
   model dependency that required 3 weeks of refactoring, which delayed the
   customer feature by 5 weeks, which triggered an RFP with a competitor" is.
   Include organizational and market failure modes, not just technical ones
   (template common mistake 3).
3. **Estimate probability for each narrative.** Calibrate, do not guess:
   reference classes and base rates from similar initiatives. Counter the
   default optimism — probability optimism is FMEA failure mode 1 and the
   template's reason for existing.
4. **Compute exposure = severity × probability, rank descending.** Keep the
   ranking; it is the contract of this skill.
5. **Pattern-match each top scenario to an Academy case.** Say the pattern
   out loud: untested reversal mechanism / speed without assurance = Knight
   Capital (CASE-0005); change communicated without the customer's mental
   model = Qwikster (CASE-0001); non-falsifiable thesis insulated from
   verification = Theranos (CASE-0019); competitive pressure overriding
   irreversibility = Boeing 737 MAX (CASE-0018). Name the case and its
   causal_confidence. A pattern claim requires the mechanism to actually be
   present — the Theranos pattern requires that the decision-maker is insulated
   from verification.
6. **Design early warning signals** (template §4) for each ranked scenario:
   a leading metric, a qualitative signal, an external signal, observable 4–8
   weeks before the failure becomes obvious.
7. **Design mitigations** (template §5) with what to monitor, cadence, a NAMED
   owner, a specific trigger, and the action taken. Use the FMEA logic
   (Framework 8): reduce probability, reduce severity/blast radius, or improve
   detectability.
8. **Run assumption inversion** (template §6) and the reversibility assessment
   (template §7) for the plan as a whole, including the point of no return.
9. **Render the ranked table and verdict** against Thresholds. The ranked
   scenarios become a monitoring plan with owners, not a filed document.

## Verdict Contract

WHAT THIS SKILL MUST RETURN. The output is a decision artifact, not a memo:

- **Ranked failure scenarios:** a table of the top 3–5 scenarios, each with
  probability, severity, exposure (severity × probability), the matched
  Academy case, its early warning signals, and its mitigation with owner and
  trigger. Sorted by exposure.
- **Verdict:** DEFENSIBLE / DEFENSIBLE-WITH-MITIGATIONS / NOT-DEFENSIBLE.
  - DEFENSIBLE — residual exposure of every top-3 scenario is at or below the
    acceptable threshold after mitigations are in place and owned.
  - DEFENSIBLE-WITH-MITIGATIONS — the decision holds only if the named
    mitigations, owners, and triggers actually land; each is a condition, not
    a hope.
  - NOT-DEFENSIBLE — at least one top scenario cannot be mitigated below the
    threshold, or a no-go condition (irreversible harm with no mitigation) is
    present.
- **Confidence:** High / Medium / Low with reasoning. High when narratives are
  specific (named characters, mechanisms, dates) and probabilities are
  reference-calibrated; Low when the team produced risk categories instead of
  narratives or "50% for everything because I'm uncertain".
- **Citations:** stable Academy doctrine/source IDs and CASE ids for each
  scenario and threshold (e.g. `CASE-0005`, `09_tools/PRE_MORTEM_TEMPLATE.md §2`,
  `Framework 8`).
- **Stated assumptions:** everything answered "unknown", with the impact each
  has on the verdict.
- **What would change the verdict:** the evidence or action that would flip it
  (e.g. "NOT-DEFENSIBLE becomes DEFENSIBLE-WITH-MITIGATIONS if the team adds a
  tested kill-switch and names a trigger authority").

## Thresholds

Reproducible criteria. A second reviewer must be able to reproduce the ranking
and verdict from the same inputs.

- **Exposure = Severity (1–5, per template §2) × Probability (0–100%).**
  Probability is reference-calibrated, not negotiated.
- **Ranking:** sort scenarios by exposure, descending; the top 3 carry the
  verdict.
- **Acceptable residual exposure:** after mitigations, no top-3 scenario may
  retain severity ≥ 4 with probability ≥ 25%. Severity is scored before and
  after mitigation (Framework 8: high-severity failure modes require mitigation
  regardless of probability).
- **NOT-DEFENSIBLE if ANY of the following:**
  1. A top-3 scenario has severity ≥ 4 AND probability ≥ 40% AND no mitigation
     brings residual below severity-4 / probability-25%.
  2. A top-3 scenario describes irreversible harm (safety, regulatory,
     financial ruin) and the decision proceeds without addressing the root
     cause — the Boeing (CASE-0018) or Theranos (CASE-0019) condition.
  3. Every scenario matches the same root cause and the plan does not
     diversify against it (the template's "common root causes" step is empty).
- **DEFENSIBLE requires ALL of the following:**
  1. Every top-3 scenario has residual exposure below the acceptable threshold.
  2. Each mitigation has a named owner, a cadence, and a specific trigger.
  3. The early warning signals are observable and would have been seen 4–8
     weeks before failure (template §4).
- **DEFENSIBLE-WITH-MITIGATIONS:** the top-3 scenarios clear the threshold
  ONLY with the named mitigations landing on schedule; verdict must list each
  mitigation as a condition with a review date.
- **No-go conditions** are surfaced as NOT-DEFENSIBLE regardless of score:
  a system that moves money or makes irreversible decisions with no kill-switch
  (CASE-0005), or a decision whose operators are not informed of a system that
  can override them (CASE-0018).

## Evidence & Doctrine

Academy references, cited not copied.

- `09_tools/PRE_MORTEM_TEMPLATE.md` — the canonical method: scenario framing,
  failure narratives (severity 1–5), common root causes, early warning signals,
  mitigation actions with owners, assumption inversion, reversibility
  assessment. This skill follows it section by section and adds ranking and
  case calibration. Tier A practice template.
- `01_core_doctrine/DECISION_FRAMEWORKS.md` — Framework 8 (FMEA): RPN =
  Probability × Severity × Detectability, severity ≥ 8 must be mitigated
  regardless of probability, reversal triggers must be specific and observable,
  reversal authority named by name not role. The ranking in this skill is a
  probability × severity adaptation of RPN. Framework 1 makes the pre-mortem
  mandatory for Type-1 decisions.
- `PRN-0003` (Cost of Delay Exceeds Cost of Imperfection) — the boundary this
  skill polices: its own counterevidence is CASE-0005 and CASE-0018, i.e. the
  pre-mortem is required precisely where speed-without-assurance would otherwise
  apply. Tier A.
- `PRN-0007` (Best Product Decisions Are Reversible by Design) — the
  reversibility assessment in template §7, including the "point of no return"
  and the failure mode of reversibility that takes so long the damage is done.
  Tier A.
- `07_cases/case_catalog.md` — CASE-0005 (Knight Capital: untested reversal,
  blast radius not limited, $440M in 45 minutes; causal_confidence high),
  CASE-0018 (Boeing 737 MAX: competitive pressure overrides certification
  irreversibility; causal_confidence high), CASE-0019 (Theranos: thesis
  asserted, not falsified, decision-makers insulated from verification;
  causal_confidence high), CASE-0001 (Netflix Qwikster: stacked changes
  communicated without the customer's mental model; causal_confidence high).
  Cite the case id and use its causal_confidence when claiming a pattern match.
- `10_simulator/scenarios/SCENARIO_03_AI_SEVERE_FAILURES.md` — a simulator
  scenario whose rubric requires a 3-path pre-mortem (model fix failure,
  organizational-incentive failure, external-stakeholder failure); the scoring
  rubric defines what specific vs. generic failure modes look like.

## Common Pitfalls

- **Pre-mortem as generic risk list.** "The project was late" is a category,
  not a narrative (template common mistake 1). Correction: force named
  characters, mechanisms, and dates; a narrative that cannot be dated cannot
  have early warning signals.
- **Doom session without mitigations.** The goal is not to feel bad; every
  narrative must produce a signal and an action (mistake 2). Correction: end
  each scenario with a named owner and trigger, or it does not count.
- **Technical-only failure modes.** Missing organizational, political, and
  market failures (mistake 3; the SCENARIO_03 rubric requires one of each).
  Correction: require at least one organizational and one external-stakeholder
  scenario.
- **Uncalibrated probabilities.** "50% for everything because I'm uncertain",
  or past-success optimism (FMEA failure mode 1). Correction: use reference
  classes; where none exist, state the base rate assumption explicitly.
- **Pattern-name inflation.** Claiming "this is the Knight Capital pattern"
  without the mechanism being present. Correction: the Knight pattern requires
  an untested/owned reversal mechanism; the Theranos pattern requires insulation
  from verification. Name the case only when the mechanism matches.
- **Pre-mortem without follow-through.** No owners, no cadence, filed and
  forgotten (mistake 4). Correction: the ranked table becomes the monitoring
  plan; signals are reviewed on the named cadence and mitigations executed on
  trigger. A pre-mortem with no owners is a performance, not a decision tool.
- **One-time exercise.** Run quarterly for the roadmap, pre-launch for major
  features (mistake 5). Correction: re-run when the decision changes or a
  signal fires.

## Related Skills

- `classify-decision-reversibility` — every TYPE-1 decision is required to run
  this pre-mortem before commitment; run after classification.
- `make-go-no-go-call` — this skill's ranked scenarios and verdict feed the
  risk-adjusted value step and the GO conditions (especially for Type-1
  decisions); run before the call is rendered.
- After the pre-mortem, the surviving plan is written up in
  `09_tools/DECISION_MEMO_TEMPLATE.md` (which depends on the pre-mortem) and
  its metrics locked in `09_tools/EVALUATION_CONTRACT_TEMPLATE.md`.
