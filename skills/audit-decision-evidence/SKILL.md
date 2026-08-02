---
name: audit-decision-evidence
description: >-
  Verdict on whether a product decision is adequately supported by evidence, claim by claim,
  using a shared evidence taxonomy that ranks internal product evidence (experiments, cohorts,
  analytics, interviews, support, win/loss) alongside published sources. Run before committing
  to a decision, when a leader defends a call with "the data", at post-launch review, or when
  two stakeholders disagree on whether a decision is evidence-backed. Supersedes the former
  run-source-tier-check skill: source credibility is now a sub-mode of this audit.
type: assess
version: 0.2.0
best_for:
  - "A product decision is about to be made and its evidence has not been checked claim by claim"
  - "A decision memo or PRD cites evidence and you need each claim's support graded"
  - "A leader is defending a call with 'the data' and you want to test whether the data actually supports it"
  - "A post-launch review asks whether the evidence that justified the decision held up"
  - "Two stakeholders disagree on whether a decision is evidence-backed and you need a reproducible verdict"
  - "Sub-mode: a source's credibility (influencer post, vendor report, unverified claim) is in question"
doctrine:
  - "PRN-0014 (same data, opposite conclusions)"
  - "PRN-0003 (cost of delay exceeds cost of imperfection)"
  - "PRN-0007 (reversible by design)"
  - "PRN-0008 (discovery beats requests)"
  - "SOURCE_POLICY.md (tier criteria, popularity is not evidence)"
  - "evidence/final/CLAIMS_LEDGER.md"
  - "evidence/final/CORROBORATION_MATRIX.md"
  - "08_contradictions/register.yaml"
license: CC BY 4.0
---

## Purpose

This skill answers one question: **does the evidence a decision rests on actually support it?**
It decomposes the decision into the claims it needs to be true, grades the evidence for each
claim against a shared evidence taxonomy that treats internal product evidence (experiments,
cohorts, analytics, interviews, support, win/loss) as first-class evidence, and returns a
verdict per claim plus an overall decision verdict.

Invoke it when a decision is imminent and its evidentiary basis has not been systematically
checked, or when someone is defending a call by pointing at "the data." Do NOT invoke it to
produce a documentation artifact — if the goal is a written evidence review for a file, render
the verdict first and then write the memo. Do NOT use it to grade whether a causal relationship
actually holds (that is `conduct-causal-confidence-review`); this skill asks whether the claim
is supported, not whether it is proven.

## Use when

- A commitment is imminent (budget, headcount, release slot) and the evidence has not been audited.
- A decision memo cites evidence and you need each claim graded.
- A leader defends a call with "the data" and you want to test whether the data supports it.
- A post-launch review asks whether the justification held up.
- Two stakeholders disagree on whether a decision is evidence-backed.
- A single source is carrying a load-bearing claim and its credibility is in question (sub-mode).

## Do not use when

- The user wants a written evidence review file, not a verdict — render the verdict, then point at the memo template.
- The question is causal ("did X cause Y") — use `conduct-causal-confidence-review`.
- The decision is pre-PMF exploration where the strategy is deliberately "try things and learn" (PRN-0003 non-applicability) — the audit will still run, but expect `LEARN`-shaped verdicts, not `GO`/`NO-GO`.
- The decision is reversible and low-stakes (a button copy change) — use Fast mode or skip; auditing a two-way door the same way as a Type-1 launch is process theater.

## Inputs

Required inputs (minimum for a useful provisional verdict):

- The decision as one sentence: the action and the expected outcome.
- The claims it rests on — every distinct "this must be true" statement. If not stated, the skill will extract them with you.
- For each load-bearing claim, the evidence: what it is, what type it is (see Evidence classification), where it came from (collection method, sample, date).

Optional inputs (upgrade the verdict to full):

- The source identity for any published/practitioner evidence (author, organization, publication, date, commercial incentive).
- Counter-evidence already known to the team.
- The decision's reversibility class (TYPE-1/TYPE-2) — speeds context classification.

## Missing-data behavior

- A claim with **no recorded evidence** is `NO-EVIDENCE` — that is a finding, not a gap to pad. Record it.
- A claim whose evidence cannot be traced (no collection method, sample, or date for internal evidence; no verifiable identity for published evidence) is `INSUFFICIENT-INFO`.
- An "unknown" on a load-bearing claim downgrades confidence to at most Medium and is recorded as an assumption with its effect. Never silently assume the evidence exists because the claim feels true.

## Context classification

- **TYPE-1 decision** (irreversible): Full mode mandatory. An `UNDER-SUPPORTED` load-bearing claim on a one-way door is `NO-GO`, not `CONDITIONAL` (PRN-0003 non-applicability, PRN-0007).
- **TYPE-2 decision** (reversible): Fast mode is the default; `CONDITIONAL` is an acceptable verdict while the reversible mechanism exists (feature flag, pilot, phased rollout).
- **Post-launch**: the audit runs in `LEARN` shape — grade what the decision rested on so reversal conditions can be checked.

## Fast mode

Run for reversible, ordinary decisions. Ask three questions, get a provisional verdict.

1. **What is the decision?** One sentence.
2. **What are the load-bearing claims?** (Usually 1–3.)
3. **What evidence exists for each?** Name the evidence type and one line of provenance.

Provisional verdict: per claim, `SUPPORTED` / `UNDER-SUPPORTED` / `NO-EVIDENCE`; overall,
`GO` (all claims supported) / `CONDITIONAL` (at least one under-supported, decision is
reversible with bounded downside) / `NO-GO` (a load-bearing claim has no evidence and the
decision is not reversible). Confidence is capped at Medium in fast mode. Next action: name
the single weakest claim and the cheapest evidence that would firm it up. No research
ceremony, no counter-evidence sweep.

## Full mode

Mandatory for TYPE-1 decisions and for any decision where fast-mode confidence would be Low
on a load-bearing claim. Adds to fast mode:

1. Extract claims from decision logic (not from the memo's citations).
2. For each claim, classify the evidence using the shared taxonomy (E1–E15 in the shared contract).
3. Grade adequacy per claim: is the evidence type a good match for the claim type? A claim
   about user behavior graded on an interview (E5) is weaker than one graded on behavioral
   analytics (E3) or a controlled experiment (E1) — but an interview is still evidence.
4. **Counter-evidence search**: search for evidence that contradicts the claim, including
   internal evidence (lost deals, churned cohorts, support tickets, incidents). Ignored
   counter-evidence is itself a finding.
5. **Corroboration check**: is the claim corroborated by 2+ independent evidence items of
   adequate type? *(Rule of thumb — the point is "not single-source", not a magic count; two
   evidence items from the same team's same dataset are one item.)* Single-source support is
   explicitly weaker. (The Academy's
   `evidence/final/CORROBORATION_MATRIX.md` is a reference for published sources when
   available; it is not required — the corroboration rule applies to internal evidence too.)
6. **Source credibility** (the former `run-source-tier-check` sub-mode): for any published or
   practitioner evidence (E9, E12, E13) and any internal evidence carrying a claim, apply the
   credibility tests — is it firsthand with concrete outcomes? Does it carry a commercial or
   promotional incentive? Is it verifiable? If a source is credited beyond what it earned,
   that is a finding. Popularity is not evidence (SOURCE_POLICY).
7. **Contested-claim check**: is the claim contested, and is the counter-position addressed
   with evidence rather than dismissal?
8. Record every "unknown" as an assumption. Render the verdict.

## Method

Work one question at a time. "Unknown" answers become stated assumptions, never silent defaults.

1. What is the decision? State it as a single sentence naming the action and the expected outcome.
2. What must be true for this decision to be correct? Each distinct "must be true" is a claim.
3. For each claim: what evidence exists, and what type is it? Name collection method, sample, and date for internal evidence; author/organization/date for published evidence.
4. Is the evidence type a good match for the claim? (A behavioral claim wants behavioral evidence; a business-model claim wants financial evidence.)
5. Is there counter-evidence the decision ignores? Name it.
6. Is the claim corroborated by 2+ independent evidence items?
7. Is any load-bearing evidence of doubtful credibility? Run the sub-mode credibility tests.
8. Record assumptions. Render per-claim and overall verdicts.

## Evidence classification

Uses the shared 15-type taxonomy from `_shared/SKILL_CONTRACT.md` (§2). There is no default
ranking: a claim is graded by the match between claim and evidence type. In particular,
internal product evidence (E1–E4, E6–E8, E10–E11) is *not* automatically below published
research (E13) or practitioner doctrine (E12). For a claim about this product's users,
behavioral analytics and cohort retention usually outrank an expert's book.

## Output schema

```json
{
  "skill": "audit-decision-evidence",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "GO | CONDITIONAL | NO-GO | LEARN",
  "per_claim": [
    {"claim": "...", "verdict": "SUPPORTED | UNDER-SUPPORTED | INSUFFICIENT-INFO | NO-EVIDENCE",
     "evidence_types": ["E3", "E4"], "weakness": "..."}
  ],
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E5"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## Verdict Contract

- **Verdict (per claim):** `ADEQUATELY-SUPPORTED` / `UNDER-SUPPORTED` / `INSUFFICIENT-INFO` / `NO-EVIDENCE`.
- **Verdict (decision):** `GO` (every load-bearing claim adequately supported) /
  `CONDITIONAL` (at least one under-supported or no-evidence claim, but the decision is
  reversible with bounded downside per PRN-0007) / `NO-GO` (a load-bearing claim is
  under-supported or has no evidence AND the decision is one-way-door with catastrophic
  failure mode) / `LEARN` (already shipped; grades what the decision rested on).
- **Confidence:** High/Medium/Low. High only when every load-bearing claim has adequate-type
  evidence with traceable provenance; Medium when one load-bearing claim rests on an
  assumption; Low when a load-bearing claim is `INSUFFICIENT-INFO`.
- **Evidence basis:** the taxonomy types used per claim.
- **Assumptions:** every "unknown", with the claim it weakens and the effect on the verdict.
- **What would change the verdict:** named evidence that flips each claim (e.g. "a 90-day
  cohort of the self-serve tier showing net expansion would move claim 2 to SUPPORTED").
- **Next action:** the single cheapest step that would firm up the weakest claim, with an owner.

### Worked example

Decision: "Launch a self-serve tier for the fintech data product this quarter." Claims:
(1) demand exists, (2) self-serve does not cannibalize enterprise deals, (3) we can support
the tier at current headcount. Evidence: (1) 140 waitlist signups (E9 market evidence, sample
and date recorded) + 22 interviews of which 18 described the exact workflow (E5) →
`ADEQUATELY-SUPPORTED`. (2) a practitioner post claiming "self-serve never cannibalizes
enterprise" (E12, single source, author funnels to a coaching program) → credibility check
fails the commercial-incentive test; no internal loss/deal data → `UNDER-SUPPORTED`.
(3) headcount plan asserted with no staffing model → `NO-EVIDENCE`. Decision verdict:
`CONDITIONAL` (one under-supported claim, one no-evidence claim, but the launch is reversible
via feature flag per PRN-0007). Confidence: Medium. Next action: pull the last 12 enterprise
loss/expansion reviews for self-serve cross-sell signal (E8) and produce a one-page staffing
model (E11). What would change it: cohort or loss evidence showing cannibalization is
bounded, plus a staffing model.

## Failure modes

- **Data as a weapon (PRN-0014):** the requester brings only evidence that supports their position. Correction: the audit requires the counter-evidence search (full-mode step 4) before any verdict.
- **Published-over-internal bias:** a peer-reviewed paper is treated as automatically stronger than the product's own cohort data. Correction: grade by claim-evidence match; a 90-day retention cohort for this product usually beats an external study about another product.
- **Popularity as evidence:** a best-selling book cited as firsthand. Correction: apply the credibility sub-mode — content and outcomes, not reach (SOURCE_POLICY).
- **Single-source anchor:** one famous source treated as settled. Correction: corroboration check; single-source claims are explicitly weaker.
- **Discovery theater (PRN-0008):** "we talked to customers" with no method, sample, or quotes. Correction: an untraceable anecdote is `INSUFFICIENT-INFO`, not evidence.
- **Auditing the memo, not the decision:** grading citations someone wrote down rather than the claims the decision actually needs. Correction: extract claims from decision logic first; citations are only relevant where they support a claim.
- **Absence padding:** treating "no evidence found" as "probably fine." Correction: `NO-EVIDENCE` is a verdict, not an invitation to assume.

## Reversal conditions

- New counter-evidence for a claim the verdict marked `ADEQUATELY-SUPPORTED` — re-audit that claim.
- An assumption marked "unknown" resolves the wrong way — re-render the affected claim and overall verdict.
- A credibility sub-mode finding is appealed with primary evidence (e.g. a verifiable operator transcript for a source judged promotional) — re-run the sub-mode.
- A post-launch metric contradicts the launch-time evidence — the `LEARN` verdict's reversal conditions are the trigger.

## Composition hooks

- **before:** `classify-decision-reversibility` (decides whether to run fast or full); `frame-product-problem` (defines the claims to audit when a problem statement exists).
- **after:** `conduct-causal-confidence-review` (grades the central claim's causality, not just support); `scan-contradictions-assumptions` (surfaces the assumptions under the audited claims); `make-go-no-go-call` (consumes this verdict as its evidence-gate input).
- **workflow:** product-bet (step 5), experiment-decision (step 4), launch-gate (step 2).

## Related Skills

- `scan-contradictions-assumptions` — the "after" half: this skill grades the evidence; that one exposes the silent assumptions underneath the same claims.
- `conduct-causal-confidence-review` — for the decision's central claim, replaces "adequately supported" with "causally established."
- `make-go-no-go-call` — consumes the decision verdict as its evidence-gate input.
- `classify-decision-reversibility` — sets the audit's mode (fast vs full) and the CONDITIONAL/NO-GO boundary.
- `_shared/SKILL_CONTRACT.md` — the evidence taxonomy and output schema this skill uses.
