---
name: run-source-tier-check
description: >-
  Verdict on whether a source's claimed evidence tier matches the tier it actually earned under
  the Academy's source policy. Use this when a source is cited to support a claim and its tier is
  in question, or when a source is proposed for addition to the registry and you need its tier assigned.
type: assess
version: 0.1.0
best_for:
  - "A source is cited in a decision memo and its tier A/B/C/D/E is contested"
  - "A claim is being supported by a single source and you need to check whether that source can carry it alone"
  - "A new source is proposed for the registry and needs a tier assigned"
  - "A source's tier was inherited (someone else assigned it) and you want to verify it"
  - "A 'Tier A because it is famous' argument appears and needs to be defused with the actual criteria"
doctrine:
  - "SOURCE_POLICY.md"
  - "sources/registry.yaml"
  - "PRN-0014"
  - "CON-0007"
  - "evidence/final/SOURCE_EVIDENCE_STRENGTH.md"
  - "evidence/final/CLAIMS_LEDGER.md"
license: CC BY 4.0
---

## Purpose

The Academy classifies every source into evidence tiers A through E, and the tier determines how much the source may support doctrine. This skill answers one question: does the tier a source claims (or was assigned) match the tier it actually earned under `SOURCE_POLICY.md`? The verdict is the decision: keep the tier, inflate it, or demote it.

Invoke it when a source is about to be relied on and its tier matters — which is every time a source is cited. Do NOT invoke it to grade whether a claim is adequately supported (that is `audit-decision-evidence`); this skill only certifies the source, not the claim.

## Input

Bring the source — either its registry ID (e.g. `SRC-BOOK-0001`) or enough of its identity (author, organization, publication, type) to look it up or characterize it — plus the tier currently claimed or assigned. If the source is not in the registry, the skill will tier it from first principles using the policy criteria. If you only have a claim and no source, that is an `audit-decision-evidence` problem, not a tier-check problem.

## Method

One question at a time. If the user answers "unknown", record it as an explicit assumption and continue.

1. What source are we checking, and what tier is claimed? Look it up in `sources/registry.yaml`. Record the `source_type`, `firsthand`, `author`, `organization`, `commercial_incentive`, and `transcript_status` fields.
2. Is this a firsthand operator account with concrete decisions and outcomes, or official product/company documentation, or a rigorous case/postmortem, or a primary regulatory/technical source? If yes, the source earns Tier A. (SOURCE_POLICY Tier A test.)
3. If not firsthand, is it an experienced practitioner or educator with transparent reasoning, concrete examples, and strong professional credibility? If yes, it earns Tier B — and can only support doctrine with corroboration.
4. Is it community discussion, a conference talk, or a podcast anecdote with weak verification? If yes, it earns Tier C — hypotheses only, never canonical doctrine alone.
5. Does the source carry a commercial or promotional incentive — influencer funnel, coaching, content marketing for a paid product? If yes, it is at most Tier D, and the incentive must be disclosed in the record.
6. Can the source's content actually be verified? If the transcript status is `TRANSCRIPT_UNAVAILABLE` or `SECONDARY_SUMMARY_ONLY`, or the provenance is unverifiable, it is at most Tier E and may not support claims.
7. Now the verdict: does the claimed tier equal the earned tier?
8. If the source is already in the registry: check its `canonical_claims_supported` field against its earned tier, and its placement in `evidence/final/SOURCE_EVIDENCE_STRENGTH.md` (anchor vs corroborating). A demoted source that still anchors claims is a finding.

## Verdict Contract

- **Verdict:** one of `TIER-MATCHED` / `TIER-INFLATED` / `TIER-DEFICIENT` / `INSUFFICIENT-INFO`.
  - `TIER-MATCHED` — claimed tier equals earned tier.
  - `TIER-INFLATED` — claimed tier is higher than earned (e.g. a Tier C talk presented as Tier A evidence). Always accompanied by the corrected tier.
  - `TIER-DEFICIENT` — claimed tier is lower than earned (rare, e.g. a firsthand operator recorded as community). Also accompanied by the corrected tier.
  - `INSUFFICIENT-INFO` — not enough verifiable metadata to tier the source; do not let it carry a claim until resolved.
- **Confidence:** High/Medium/Low with reasoning. Low when tiering rests on unverifiable fields (provenance, transcript status).
- **Citations:** the `SOURCE_POLICY.md` tier test used, the registry entry (`SRC-xxxx`), and the ledger/strength placement if relevant.
- **Stated assumptions:** any field the user did not know, recorded explicitly (e.g. "author's operator role not verified — assuming Tier B").
- **What would change the verdict:** the missing field that would flip it (e.g. "a VERIFIED_CREATOR_TRANSCRIPT would raise this to Tier A" or "documented commercial incentive drops it to Tier D").

### Worked example

Source: a LinkedIn influencer thread claiming "our A/B tests at three companies show X," cited in a decision memo as Tier B. Check: not a firsthand operator account with documented role (author identity unverified), content unverifiable beyond the post, and the thread funnels to a paid cohort program. Earned tier: at most Tier D (commercial/promotional) with `INSUFFICIENT-INFO` on provenance. Claimed Tier B — verdict `TIER-INFLATED`, corrected to Tier D, and the memo's claim that rested on it is flagged for re-audit. What would change it: a documented operator role plus verifiable test methodology (Tier B), or disclosure that the thread is marketing with the incentive recorded (Tier D, then `TIER-MATCHED`). Confidence: Medium — the commercial incentive is visible, but the author's operator status could not be confirmed either way.

## Thresholds

A second reviewer must reach the same verdict from the same metadata.

- `TIER-MATCHED` — the source satisfies every criterion of its claimed tier and fails none of the higher-tier tests.
- `TIER-INFLATED` — the source fails at least one criterion of the claimed tier; correct it downward to the highest tier whose tests it passes.
- `TIER-DEFICIENT` — the source satisfies the tests of a higher tier than claimed; correct it upward.
- `INSUFFICIENT-INFO` — one or more of the following cannot be established from the record: authorship/organization, whether it is firsthand, provenance/verifiability, or transcript status.

Tier tests, from SOURCE_POLICY (short quote, then point to policy):

- Tier A: "Firsthand operator account with concrete decisions and outcomes. Official product or company documentation." May support canonical doctrine alone.
- Tier B: "Experienced practitioner or educator with transparent reasoning, concrete examples, and strong professional credibility." May support doctrine with corroboration.
- Tier C: "Community discussion, conference talk, podcast anecdote." May generate hypotheses and case leads; cannot support canonical doctrine alone.
- Tier D: "Influencer summary, coaching funnel, promotional framework, content marketing." Discovery only unless corroborated by A/B.
- Tier E: "Anonymous unsupported assertion, AI-generated reconstruction, unverifiable aggregation." Exclude from canonical doctrine.

## Evidence & Doctrine

- `SOURCE_POLICY.md` — the canonical tier definitions; quote at most one line per tier, then point to the policy.
- `sources/registry.yaml` — 184 sources (verified counts: A=65, B=44, C=73, E=2). Note: Tier D is defined in policy but currently unoccupied in the registry — a source with a commercial incentive that is not disclosed would be the first.
- `evidence/final/SOURCE_EVIDENCE_STRENGTH.md` — per-source anchor/corroborating placement.
- `evidence/final/CLAIMS_LEDGER.md` — per-claim supporting sources; a tier-inflated source that appears as a supporting source flags the claim.
- `PRN-0014` — tier discipline exists because the same source can be spun either way; the tier check fixes what the source is allowed to carry.
- `CON-0007` — experimentation vs judgment tension; tier checks are how the Academy keeps "the data" from silently becoming "the authority."

## Common Pitfalls

- **Popularity as evidence (SOURCE_POLICY):** "best-selling book, therefore Tier A." Correction: tier by content — a widely-cited practitioner framework with transparent reasoning is Tier B even when famous.
- **Author fame as firsthand:** a famous author quoted about someone else's operation. Correction: `firsthand` is about the source's own decisions, not the author's reputation.
- **Unlabelled ASR:** quotes lifted from an auto-generated transcript presented as a creator's words. Correction: check `transcript_status`; `ASR_DERIVED_TRANSCRIPT` must be labelled and spot-checked.
- **Inherited tier, unexamined:** registry entries copied forward. Correction: this skill exists to re-run the tests; `INSUFFICIENT-INFO` beats a confidently wrong A.
- **Commercial incentive amnesia (PRN-0014 'data as a weapon' family):** a vendor source presented as neutral analysis. Correction: Tier D disclosure is mandatory; a hidden incentive inflates the tier by definition.

## Related Skills

- `audit-decision-evidence` — the "after" half; run this first to certify sources, then audit the claims they support.
- `conduct-causal-confidence-review` — a tier-inflated source often masks a correlation presented as causation.
- `scan-contradictions-assumptions` — surfaces the assumptions that made the inflated tier feel necessary.
