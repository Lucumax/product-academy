# Product Forge Integration Boundary

**Status:** PROPOSED — No mechanical integration has been implemented.
**Last reviewed:** 2026-08-01

This document defines the conceptual boundary between the Product Leadership Academy
and the Product Forge Product Operating System. It describes what the Academy MAY
export and what Product Forge MAY return. All integration points are **proposed**
unless explicitly marked as **verified**.

---

## Integration Purpose

The Academy teaches product leadership. Product Forge executes product discovery
and definition. When a student applies Academy doctrine to a real initiative, the
handoff between "learning" and "doing" crosses this boundary. The Academy provides
the decision framework; Product Forge provides the execution artifacts.

---

## What the Academy May Export (proposed)

| Export | Format | Description |
|--------|--------|-------------|
| **Doctrine Reference** | `principle_id` + context | Which canonical principle applies to this product situation |
| **Decision Framework** | Structured markdown | One-way/two-way door classification, reversibility assessment, strategy exclusion list |
| **Case Pattern** | `case_id` + key_transfer | Relevant case study pattern to apply |
| **Product Archetype** | Enum from schema | Which archetype the initiative maps to |
| **Industry Constraint** | String + overlay reference | Regulatory, market, or organizational constraints |
| **Evaluation Rubric** | Scoring guide | How to evaluate product decision quality (judgment, not features) |
| **Recommended Template** | Template path | Which Product Forge template to start from |
| **Practice Result** | Structured feedback | Simulator output, assessment scores, reflection notes |

### Example Doctrine Reference (proposed)

```json
{
  "academy_export": {
    "type": "doctrine_reference",
    "principle_id": "PRN-0003",
    "title": "The Cost of Delay Exceeds the Cost of Imperfection",
    "applicable_context": "Two-way door decision with bounded failure cost",
    "decision_framework": "one_way_vs_two_way_door",
    "reversibility_assessment": {
      "cost_if_wrong": "low",
      "probability_wrong": "medium",
      "reversibility_cost": "low",
      "recommendation": "decide_fast"
    }
  }
}
```

---

## What Product Forge May Return (proposed)

| Return | Format | Description |
|--------|--------|-------------|
| **Actual Product Decision** | Decision Card (v0.2) | One-screen verdict artifact with rationale |
| **Hypothesis** | JSON schema | Structured hypothesis with before/after confidence |
| **Validation Plan** | JSON schema | How the hypothesis will be tested |
| **Validation Result** | Structured report | Outcome of validation with evidence |
| **Product Outcome** | Summary report | What shipped and what happened |
| **Reversal** | Decision Card | Decision to reverse a previous decision |
| **Post-Launch Review** | Structured analysis | Comparison of expected vs actual outcomes |
| **Anonymized Learning Case** | Case template | Real decision, sanitized for Academy use |

### Example Handoff Package (proposed)

```json
{
  "handoff": {
    "academy_export": {
      "principle_id": "PRN-0003",
      "framework": "one_way_vs_two_way_door",
      "case_pattern": "CASE-0001",
      "archetype": "consumer",
      "rubric_id": "decision_quality_v1"
    },
    "product_forge_input": {
      "brief_id": "PF-EXAMPLE-001",
      "claim_class": "hypothesis_to_validate",
      "initial_confidence": "medium"
    }
  }
}
```

---

## Boundary Rules

1. **The Academy does not execute product work.** It provides frameworks, not deliverables.
2. **Product Forge does not teach.** It produces artifacts, not curriculum.
3. **Integration is at the data boundary.** Files or structured JSON passed between systems.
4. **No database shared.** No runtime dependency. Each system is independently operational.
5. **All integration is proposed until mechanically verified.** Do not claim otherwise.

---

## What Is NOT Shared

- Product Forge's execution artifacts (briefs, backlogs, work packets) are NOT stored in the Academy.
- Academy content (principles, cases, assessments) is NOT stored in Product Forge.
- The Academy does not invoke Product Forge automatically (no API calls, no subprocess).
- Product Forge does not read Academy files at runtime.

---

## Verification Status

| Integration Point | Status | Verified By | Date |
|-------------------|--------|-------------|------|
| Doctrine reference -> Product Forge brief | proposed | — | — |
| Case pattern -> Decision Card | proposed | — | — |
| Evaluation rubric -> Validation plan | proposed | — | — |
| Simulator result -> Product Forge context | proposed | — | — |
| Product Forge outcome -> Anonymized case | proposed | — | — |

**No integration has been mechanically verified.** This document serves as a design
specification for future integration work.
