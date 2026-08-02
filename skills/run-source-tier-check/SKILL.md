---
name: run-source-tier-check
description: >-
  DEPRECATED. This skill has been merged into audit-decision-evidence as the "source credibility
  sub-mode". Previously returned TIER-MATCHED / TIER-INFLATED / TIER-DEFICIENT verdicts on whether
  a source's claimed evidence tier matched its earned tier. Agents and users referencing this skill
  are routed to audit-decision-evidence, which applies the same credibility tests to any evidence —
  including internal product evidence — rather than only published sources.
type: assess
version: 0.2.0
deprecated: true
replaced_by: audit-decision-evidence
best_for:
  - "Routing: anyone invoking the former source-tier check should run audit-decision-evidence instead"
doctrine:
  - "SOURCE_POLICY.md"
  - "PRN-0014"
  - "evidence/final/CLAIMS_LEDGER.md"
license: CC BY 4.0
---

## Purpose

**This skill is deprecated.** The former job — grading whether a source's claimed evidence
tier matched its earned tier — is now the **source-credibility sub-mode** inside
[`audit-decision-evidence`](../audit-decision-evidence/SKILL.md). The sub-mode keeps the
credibility tests that mattered (firsthand? concrete outcomes? commercial incentive?
verifiable? popularity is not evidence) and applies them to internal product evidence as well
as published sources.

## Use when

- You were routed here by an old index, bookmark, or habit. Run
  [`audit-decision-evidence`](../audit-decision-evidence/SKILL.md) instead and use its
  source-credibility sub-mode (full-mode steps 6).

## Do not use when

- Anytime you would have used the old skill. The standalone verdict vocabulary
  (TIER-MATCHED / TIER-INFLATED / TIER-DEFICIENT) is retired; the taxonomy and thresholds of
  `audit-decision-evidence` replace it.

## Deprecated routing

- **Replacement:** `audit-decision-evidence` (evidence audit with source-credibility sub-mode).
- **Evidence taxonomy:** the shared 15-type taxonomy in `_shared/SKILL_CONTRACT.md` (§2),
  which ranks evidence by claim-evidence match, never by a blanket preference for published
  research.
- **Source tiering policy:** `SOURCE_POLICY.md` remains the reference for published-source
  tier definitions; its tests are applied inside the audit's credibility sub-mode.

## Failure modes

- **Dead link / stale habit:** an agent or PM still calls the old skill. Correction: the
  pack index and this stub both route to `audit-decision-evidence`; the validator enforces
  that this stub's `replaced_by` resolves.

## Reversal conditions

- None; this skill does not produce verdicts. If the pack is ever re-opened on whether
  standalone source certification is worth resurrecting (e.g. for a researcher audience),
  revisit via the portfolio map's gap list, not this stub.

## Worked example

Not applicable — deprecated.

## Composition hooks

- **before:** none.
- **after:** `audit-decision-evidence` (the replacement).
- **workflow:** none — routing only.

## Related Skills

- `audit-decision-evidence` — the replacement skill.
- `conduct-causal-confidence-review` — a tier-inflated source often masks a correlation presented as causation.
- `scan-contradictions-assumptions` — surfaces the assumptions that made an inflated source feel necessary.
