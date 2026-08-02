---
name: audit-decision-evidence
description: >-
  Audits whether a product decision is adequately supported by evidence, claim by claim.
  Use this when a decision is being made, defended, or post-launch reviewed, and you need a
  reproducible verdict on whether the evidence behind each of its claims meets the Academy's
  evidence bar.
type: assess
version: 0.1.0
best_for:
  - "A product decision is about to be made and you want the evidence checked before committing"
  - "A decision memo or PRD cites sources and you need each claim's support graded"
  - "A leader is defending a call with 'the data' and you want to test whether the data actually supports it"
  - "A post-launch review asks whether the evidence that justified the decision held up"
  - "Two stakeholders disagree on whether a decision is evidence-backed and you need a reproducible verdict"
doctrine:
  - "PRN-0014"
  - "PRN-0003"
  - "PRN-0007"
  - "SOURCE_POLICY.md"
  - "sources/registry.yaml"
  - "evidence/final/CLAIMS_LEDGER.md"
  - "evidence/final/CORROBORATION_MATRIX.md"
license: CC BY 4.0
---

## Purpose

The Academy's evidence discipline holds that every claim must be traceable to a documented source with a defensible tier. This skill turns that discipline into a decision: given a product decision, it decomposes the decision into the claims it rests on, grades the evidence for each claim against the tier policy, and returns a verdict per claim plus an overall decision verdict.

Invoke it when a decision is imminent and its evidentiary basis has not been systematically checked, or when someone is defending a call by pointing at "the data." Do NOT invoke it to produce a documentation artifact — if the goal is a written evidence review for a file, say so and offer the adjacent skill; this skill outputs a verdict, not a memo. Do NOT use it to settle whether a source's tier is correct (that is `run-source-tier-check`) or whether a causal relationship actually holds (that is `conduct-causal-confidence-review`); this skill assumes the tier is correct and asks whether the claim is adequately supported by whatever tier it has.

## Input

Bring the decision stated as one sentence, the claims it rests on (or let the skill extract them), and the evidence/sources cited for each claim. If the claim is a canonical Academy claim, bring its claim ID (CLM-xxxx) or cite it. If you arrive empty-handed, the skill will ask you to state the decision and then extract the claims with you — you cannot audit claims that have not been stated.

## Method

Work one question at a time. If the user answers "unknown" at any step, record it as an explicit assumption and continue. Never silently assume.

1. What is the decision? State it as a single sentence that names the action and the expected outcome.
2. What must be true for this decision to be correct? Every distinct "must be true" statement is a claim. Write each down. A decision that rests on three claims has three audits.
3. For each claim: what evidence is cited? Look up the source in `sources/registry.yaml`. If the source's tier is itself in doubt, defer that claim to `run-source-tier-check` and record it.
4. Is a single Tier A source sufficient, or does this claim need corroboration? Apply the tier rules from `SOURCE_POLICY.md` (Tier A single source sufficient; Tier B requires corroboration; Tier C may not anchor; Tier E may not support claims).
5. Is the claim contested? Check `evidence/final/CLAIMS_LEDGER.md` (`contested` field) and the counter-claim sources. A contested claim with unaddressed Tier A counter-evidence is not adequately supported.
6. Is there counter-evidence in the register that the decision ignores? Search the registry for the claim topic and note opposing sources, with their tiers.
7. Corroboration check: is the claim corroborated by 2+ independent supporting sources per `evidence/final/CORROBORATION_MATRIX.md`? If single-source, that fact is itself a finding.
8. Record every "unknown" as an assumption. Then produce the verdict.

## Verdict Contract

Return a decision artifact, not a memo:

- **Verdict (per claim):** one of `ADEQUATELY-SUPPORTED` / `UNDER-SUPPORTED` / `INSUFFICIENT-INFO`.
- **Verdict (decision):** one of `GO` / `CONDITIONAL` / `NO-GO` / `LEARN`.
- **Confidence:** High/Medium/Low with reasoning. Confidence is low when any load-bearing assumption is an "unknown."
- **Citations:** for each claim, the source IDs (e.g. `SRC-BOOK-0001`, tier) and the ledger entries (`CLM-xxxx`) used. Cite, don't quote.
- **Stated assumptions:** every "unknown" recorded as an explicit assumption, with the claim it weakens.
- **What would change the verdict:** name the specific evidence that would flip each claim (e.g. "a second independent Tier B source" or "resolution of the contested status of CLM-0022").

### Worked example

Decision: "Launch a self-serve tier for the fintech data product this quarter." Claims extracted: (1) demand exists, (2) self-serve does not cannibalize enterprise deals, (3) we can support the tier at current headcount. Audit result: claim 1 supported by SRC-BOOK-0004 and CLM-0008 (Tier A, corroborated) — `ADEQUATELY-SUPPORTED`; claim 2 rests on a single Tier B practitioner post, corroboration status "no" — `UNDER-SUPPORTED`; claim 3 cites no source — `INSUFFICIENT-INFO`, recorded as an assumption. Decision verdict: `CONDITIONAL` (one under-supported claim, one insufficient-claim, but the launch is reversible via feature flag per PRN-0007). What would flip it: a second independent Tier B source or a documented Tier A case on self-serve cannibalization would move claim 2 to `ADEQUATELY-SUPPORTED`; headcount analysis (Tier A internal, documented) would resolve claim 3. Confidence: Medium — two of three claims are gated on recorded assumptions.

## Thresholds

A second reviewer must be able to reproduce the verdict from the same inputs.

Claim-level:

- `ADEQUATELY-SUPPORTED` — one of: (a) at least one Tier A source supports the claim and no Tier A counter-evidence exists in the register, or (b) 2+ independent Tier B sources agree and no Tier A counter-evidence exists, or (c) the claim is corroborated per the CORROBORATION_MATRIX and its contested status is False or the contest is addressed.
- `UNDER-SUPPORTED` — one of: only a single Tier B source, or Tier C source(s), or a contested claim whose Tier A counter-evidence is unaddressed, or corroboration status is "no."
- `INSUFFICIENT-INFO` — no source recorded for the claim, or the only sources are Tier E (pending verification), or Tier D without disclosed and considered commercial incentive.

Decision-level:

- `GO` — every claim is `ADEQUATELY-SUPPORTED`.
- `CONDITIONAL` — at least one claim is `UNDER-SUPPORTED` or `INSUFFICIENT-INFO`, AND the decision is reversible with bounded downside per PRN-0007, AND no catastrophic failure mode is present.
- `NO-GO` — an `UNDER-SUPPORTED` or `INSUFFICIENT-INFO` claim is load-bearing AND the decision is one-way-door with catastrophic failure mode (PRN-0003 non-applicability conditions apply).
- `LEARN` — the decision has already shipped; the audit grades what the decision rested on so the reversal_conditions of PRN-0003/PRN-0007 can be checked.

## Evidence & Doctrine

- `SOURCE_POLICY.md` — tier definitions. Tier A: "firsthand operator account with concrete decisions and outcomes." Tier B: "Experienced practitioner or educator with transparent reasoning." Tier C: "Useful but weakly verified experiential evidence." Tier E: "pending verification." Registry counts (verified): A=65, B=44, C=73, E=2.
- `evidence/final/CLAIMS_LEDGER.md` — 35 claims, each with evidence level, contested status, supporting and counter-claim sources. Cite `CLM-xxxx`, don't reproduce the ledger.
- `evidence/final/CORROBORATION_MATRIX.md` — which claims have 2+ independent supporting sources.
- `PRN-0014` — the same data can support opposite conclusions; the audit exists because data rarely resolves an argument on its own.
- `PRN-0003` / `PRN-0007` — set the reversibility gates that separate `CONDITIONAL` from `NO-GO`.

## Common Pitfalls

- **Data as a weapon (PRN-0014):** the requester brings only the data that supports their position. Correction: the audit is per claim, and every claim requires the counter-evidence search in step 6 before a verdict.
- **Popularity as evidence:** a best-selling book is cited as if it were firsthand. Correction: tier by content per `SOURCE_POLICY.md`, not by reach.
- **Single-source anchor:** a claim rests on one famous Tier A source and is treated as settled. Correction: check the CORROBORATION_MATRIX; single-source claims are explicitly weaker doctrine.
- **Discovery theater (PRN-0008):** "we talked to customers" is offered as evidence without a documented method or claims. Correction: an anecdote with no source record is `INSUFFICIENT-INFO`, not evidence.
- **Auditing the memo, not the decision:** grading citations someone wrote down rather than the claims the decision actually needs. Correction: extract claims from the decision logic first (step 2); the cited sources are only relevant where they support a claim.

## Related Skills

- `run-source-tier-check` — the "before" half; if a source's tier is in question, resolve it first, then audit.
- `scan-contradictions-assumptions` — the "after" half; this skill grades the evidence, that one exposes the silent assumptions and live contradictions underneath the same claims.
- `conduct-causal-confidence-review` — for the decision's central claim, replaces "adequately supported" with "causally established."
