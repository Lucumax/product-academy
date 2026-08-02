---
# Canonical SKILL.md template for the Product Academy skill pack.
# Every skill MUST conform to this exact structure. The skills validator
# (scripts/validate_skills.py) enforces: required frontmatter, required
# sections, and the presence of a Verdict Contract with thresholds.
#
# Copy this template, fill it in, and place it in skills/<skill-name>/SKILL.md
# with supporting files in skills/<skill-name>/references/.
name: kebab-case-skill-name
description: >-
  What this skill does and when to invoke it, in plain language (this is the
  line agents read to decide whether to run the skill). Anthropics-compatible.
type: assess|assist
version: 0.1.0
best_for:
  - "3-5 trigger scenarios: the situations where a PM/agent should run this skill"
doctrine:
  - "Stable Academy doctrine IDs this skill draws on, e.g. PRN-0003, CON-0008, 09_tools/PRE_MORTEM_TEMPLATE.md"
license: CC BY 4.0
---

## Purpose

Why this skill exists, when to invoke it, and — explicitly — when NOT to.
The Academy is the map; this skill turns the map into a decision. If the
user is asking for a document rather than a decision, say so and offer the
adjacent skill that produces documents.

## Input

What the user should bring. Plain language only — do NOT use `$ARGUMENTS`
templating (it breaks Codex/ChatGPT/Cursor). State what happens if the user
arrives empty-handed.

## Method

Step-by-step reasoning, one question at a time. Ask the user the fewest
questions needed to reach a verdict, then apply Academy doctrine. If the
user answers a step with "unknown", record that as an explicit assumption
and continue — never silently assume.

## Verdict Contract

WHAT THIS SKILL MUST RETURN. The output is a decision artifact, not a memo:

- **Verdict:** one of a small set of explicit verdicts (e.g. GO / NO-GO /
  PAUSE; TIER-MATCHED / TIER-INFLATED; PASS / FAIL / LEARN)
- **Confidence:** per-verdict confidence label (High / Medium / Low) with
  the reasoning
- **Citations:** stable Academy doctrine/source IDs for each claim in the
  verdict (e.g. `PRN-0003`, `SRC-BOOK-0001`, `08_contradictions/register.yaml`)
- **Stated assumptions:** anything the user did not know, recorded explicitly
- **What would change the verdict:** the evidence that would flip the call

## Thresholds

Explicit, checkable criteria for each verdict. "The verdict is GO only if
all of the following hold…". Thresholds must be specific enough that a
second reviewer (or an agent) can reproduce the same verdict from the same
inputs. Where the Academy's own material defines thresholds (e.g. evaluation
contracts, scoring rubrics, evidence tiers), cite and use them.

## Evidence & Doctrine

The Academy references this skill draws on, with stable IDs. Where a source
is Tier A/B/C/E, say so. Cite, don't copy: quote at most a short line with
a source location, then link/point to the Academy registry. Never reproduce
third-party content.

## Common Pitfalls

Named failure modes and how to correct them, drawn from the Academy's
failure-mode discipline (PRN-0008 "discovery theater", PRN-0014 "data as a
weapon", PRN-0002 "strategy as communication rather than resource
allocation"). Every pitfall must have a concrete correction.

## Related Skills

Other skills in this pack that chain with this one (e.g. this skill is the
"after" half of that skill's "before").
