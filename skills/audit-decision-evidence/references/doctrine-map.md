# Doctrine Map — audit-decision-evidence

Exact registry, ledger, and doctrine IDs this skill draws on.

## Principles (01_core_doctrine/PRINCIPLES.md)

- PRN-0014 — The Same Data Can Support Opposite Conclusions — the core rationale for the per-claim audit.
- PRN-0003 — Cost of Delay Exceeds Cost of Imperfection — reversibility gate between CONDITIONAL and NO-GO.
- PRN-0007 — Reversible by Design — defines what "bounded downside" means in the thresholds.
- PRN-0008 — Customer Discovery Produces Better Decisions Than Customer Requests — source of the "discovery theater" pitfall.

## Source policy (SOURCE_POLICY.md, sources/registry.yaml)

- Tier A (65 sources) — firsthand operator / official docs, single source sufficient.
- Tier B (44 sources) — credible practitioner, requires corroboration.
- Tier C (73 sources) — community, may not anchor.
- Tier D (0 in registry; defined in policy) — commercial, incentive must be disclosed.
- Tier E (2 sources) — pending verification, may not support claims.

## Evidence artifacts (evidence/final/)

- CLAIMS_LEDGER.md — 35 claims (CLM-0001..CLM-0035) with evidence level, contested status, supporting/counter sources.
- CORROBORATION_MATRIX.md — corroborated vs uncorroborated claim lists.
- SOURCE_EVIDENCE_STRENGTH.md — per-source anchor vs corroborating status (used in step 6 counter-evidence check).

## Cited claim examples (usable in worked verdicts)

- CLM-0001 (Tier A, corroborated, contested) — empowered teams.
- CLM-0005 (Tier B, single source) — strategy kernel.
- CLM-0018 (Tier B, single source) — LLM jagged frontier.
- CLM-0022 (Tier B, contested) — Innovator's Dilemma.
