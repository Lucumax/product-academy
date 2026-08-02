# Doctrine Map — run-case-based-premortem

Exact Academy IDs referenced by this skill. All verified to exist in this repo.

## Tools (`09_tools/`)
- `PRE_MORTEM_TEMPLATE.md` — canonical method: scenario, failure narratives (severity 1–5), common root causes, early warning signals, mitigations with owners, assumption inversion, reversibility assessment

## Decision Frameworks (`01_core_doctrine/DECISION_FRAMEWORKS.md`)
- Framework 8 — FMEA for Product Decisions (RPN = P × S × D; severity ≥ 8 mitigated regardless of probability; named reversal authority; specific triggers)
- Framework 1 — One-Way vs Two-Way Door (pre-mortem mandatory for Type-1 decisions)

## Principles (`01_core_doctrine/PRINCIPLES.md`)
- `PRN-0003` — Cost of Delay Exceeds Cost of Imperfection (counterevidence is CASE-0005 / CASE-0018; Tier A)
- `PRN-0007` — Best Product Decisions Are Reversible by Design (reversibility assessment, point of no return; Tier A)

## Cases (`07_cases/case_catalog.md`)
- `CASE-0005` — Knight Capital: untested reversal, blast radius not limited (causal_confidence: high)
- `CASE-0018` — Boeing 737 MAX: competitive pressure overrides certification irreversibility (high)
- `CASE-0019` — Theranos: thesis asserted, not falsified, insulated from verification (high)
- `CASE-0001` — Netflix Qwikster: stacked changes communicated without the customer's mental model (high)

## Simulator (`10_simulator/scenarios/`)
- `SCENARIO_03_AI_SEVERE_FAILURES.md` — rubric requires a 3-path pre-mortem (model fix / organizational / external stakeholder)
