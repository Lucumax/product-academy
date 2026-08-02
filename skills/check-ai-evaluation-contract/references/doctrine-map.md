# Doctrine Map — check-ai-evaluation-contract

Stable Academy references used by this skill. All IDs verified against the
Academy registry on 2026-08-02.

## AI module (05_ai_product_management)

| File | Use in this skill |
|------|-------------------|
| EVALUATION_CONTRACTS.md | Reference standard: launch/rollback/monitor thresholds, silent-failure rollback, failure taxonomy |
| FAILURE_MODES.md | Failure taxonomy: hallucination, omission, distribution shift, silent failure as meta-failure |
| MODEL_VS_SYSTEM.md | Monitor the system, not just the model |
| GOVERNANCE.md | Contract as the product-facing layer of proportional governance |
| ADOPTION.md | Trust and organizational-change context for monitoring signals |
| WORKFLOW_SELECTION.md | Precondition: the contract is built for an AI-appropriate workflow |
| AGENT_ARCHITECTURE.md | Cascading-failure analysis for agent systems |

## Principles (01_core_doctrine/PRINCIPLES.md)

| ID | Title | Use in this skill |
|----|-------|-------------------|
| PRN-0011 | Leading Indicators Beat Lagging Indicators | Monitoring must track behaviors that precede outcomes (override, opt-out, satisfaction) |

## Contradictions (08_contradictions/register.yaml)

| ID | Question | Use in this skill |
|----|----------|-------------------|
| CON-0011 | Human-in-the-loop vs full automation | Contract must define which outputs need review, and measure review rate |

## Cases (07_cases/case_catalog.md)

| ID | Title | Use in this skill |
|----|-------|-------------------|
| CASE-0018 | Boeing 737 MAX | Failure modes analyzed for design conditions but not failure conditions |
| CASE-0019 | Theranos | Launch without validation; presentation standing in for a contract |

## Tools (09_tools)

| File | Use in this skill |
|------|-------------------|
| EVALUATION_CONTRACT_TEMPLATE.md | Drafting aid; completeness checks are its acceptance criteria |

## Sources (sources/registry.yaml)

| ID | Tier | Title |
|----|------|-------|
| SRC-POST-0094 | C | NTSB and international investigative reports, Lion Air 610 / Ethiopian 302 |
| SRC-POST-0101 | A | John Carreyrou, WSJ Investigation of Theranos |
