# Doctrine Map — run-source-tier-check

Exact registry, policy, ledger, and doctrine IDs this skill draws on.

## Source policy (SOURCE_POLICY.md, sources/registry.yaml)

- Tier A (65 sources) — firsthand operator / official docs / rigorous case or postmortem / primary regulatory. May support canonical doctrine alone.
- Tier B (44 sources) — credible practitioner/educator with transparent reasoning. Requires corroboration.
- Tier C (73 sources) — community discussion / talk / podcast anecdote. Hypotheses only.
- Tier D (0 in registry; defined in policy) — commercial/promotional; incentive must be disclosed.
- Tier E (2 sources) — pending verification; may not support claims.

Registry is `sources/registry.yaml` (184 records). Required fields include `evidence_tier`, `firsthand`, `commercial_incentive`, `transcript_status`, `canonical_claims_supported`.

## Transcript statuses (SOURCE_POLICY.md)

- VERIFIED_CREATOR_TRANSCRIPT / VERIFIED_PLATFORM_CAPTIONS / ASR_DERIVED_TRANSCRIPT / CREATOR_SUMMARY_ONLY / SECONDARY_SUMMARY_ONLY / TRANSCRIPT_UNAVAILABLE.

## Principles (01_core_doctrine/PRINCIPLES.md)

- PRN-0014 — Same Data Can Support Opposite Conclusions — rationale for fixing what a source is allowed to carry.
- CON-0007 (08_contradictions/register.yaml) — experimentation vs judgment; tier checks prevent "data as authority."

## Evidence artifacts (evidence/final/)

- SOURCE_EVIDENCE_STRENGTH.md — per-source anchor vs corroborating placement.
- CLAIMS_LEDGER.md — per-claim supporting sources; tier-inflated source appearing here flags the claim.

## Worked example sources (all verified present in registry)

- SRC-BOOK-0001 (A, anchor) — Cagan, Inspired.
- SRC-BOOK-0015 (B) — Rumelt, Good Strategy Bad Strategy.
- SRC-POST-0011 (A, counter-evidence) — Knight Capital.
- SRC-POST-0061 (B) — Twitter 280-character analysis.
- SRC-BOOK-0029 (B) — A/B testing interpretation (PRN-0014 evidence).
