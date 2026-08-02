---
# Canonical SKILL.md template for the Product Academy skill pack.
# Every skill MUST conform to the shared contract. The validator
# (scripts/validate_skills.py) enforces: required frontmatter, required sections,
# fast/full mode presence, output schema presence, and a Verdict Contract with
# all sub-parts. See skills/_shared/SKILL_CONTRACT.md for the evidence taxonomy,
# output envelope, and fast/full rules.
#
# Copy this template, fill it in, and place it in skills/<skill-name>/SKILL.md
# with supporting files in skills/<skill-name>/references/.
name: kebab-case-skill-name
description: >-
  What this skill does and when to invoke it, in plain language (this is the line
  agents read to decide whether to run the skill). Anthropics-compatible.
type: assess|assist
version: 0.1.0
best_for:
  - "3-5 trigger scenarios: the situations where a PM/agent should run this skill"
doctrine:
  - "Stable Academy doctrine IDs this skill draws on, e.g. PRN-0003, CON-0008, 09_tools/PRE_MORTEM_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Why this skill exists, when to invoke it, and — explicitly — when NOT to. The Academy is the
map; this skill turns the map into a decision. If the user is asking for a document rather
than a decision, say so and offer the adjacent skill that produces documents.

## Use when

- Concrete trigger situation 1.
- Concrete trigger situation 2.
- Concrete trigger situation 3.

## Do not use when

- Reversible, low-stakes decisions — use Fast mode or skip.
- Adjacent skills' jobs (name them).
- Document requests — render the verdict, then point at the template.

## Inputs

Required inputs (the minimum for a useful provisional verdict):

- What the user must bring.

Optional inputs (what upgrades the verdict from provisional to full):

- What improves the verdict.

## Missing-data behavior

- What the skill does when a required input is "I don't know": record as an explicit
  assumption, downgrade confidence, name the cheapest way to resolve it. Never silently pad.

## Context classification

- How the skill adapts to decision reversibility (TYPE-1/TYPE-2), product archetype, stakes,
  and time budget.

## Fast mode

Run for reversible or ordinary decisions: minimum questions, provisional verdict, explicit
uncertainty, clear next action, no research ceremony. State the exact question set.

## Full mode

Run for Type-1 and high-stakes decisions: source verification, internal evidence analysis,
contradiction review, causal-confidence assessment, premortem, decision thresholds,
reproducible verdict. State what full mode adds.

## Method

Step-by-step reasoning, one question at a time. Ask the user the fewest questions needed to
reach a verdict. If the user answers a step with "unknown", record that as an explicit
assumption and continue — never silently assume.

## Evidence classification

How this skill sorts evidence using the shared 15-type taxonomy
(`_shared/SKILL_CONTRACT.md` §2): which types it relies on, and its weighting rule. Ranking
depends on the claim being evaluated, never on a blanket preference for published research.

## Output schema

```json
{
  "skill": "skill-name",
  "version": "0.1.0",
  "mode": "fast | full",
  "verdict": "...",
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E5"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

WHAT THIS SKILL MUST RETURN. The output is a decision artifact, not a memo:

- **Verdict:** one of a small set of explicit verdicts.
- **Confidence:** per-verdict confidence label (High / Medium / Low) with the reasoning.
- **Evidence basis:** the taxonomy types actually used.
- **Assumptions:** anything the user did not know, recorded explicitly with its effect.
- **What would change the verdict:** the specific evidence that would flip the call.
- **Next action:** the concrete, owner-able step the verdict mandates.

## Failure modes

Named failure modes and how to correct them. Every failure mode has a concrete correction.
(Formerly "Common Pitfalls".)

## Reversal conditions

The observable conditions under which the verdict should be revisited or rolled back.

## Worked example

One realistic, calibrated example from input to verdict.

## Composition hooks

- **before:** skills whose artifact is required or recommended input.
- **after:** skills that consume this skill's artifact.
- **workflow:** the named workflow(s) this skill participates in (`workflows/`).

## Related Skills

Other skills in this pack that chain with this one, plus the shared contract.
