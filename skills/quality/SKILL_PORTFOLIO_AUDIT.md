# Skill Portfolio Audit

Author: principal product-systems engineer (adversarial review pass).
Date: 2026-08-02.
Scope: every skill in `skills/` as of commit `16eef8d`, plus the pack's
packaging, indexes, validator, and plugin manifest.
Baseline gates at audit time: `scripts/validate_skills.py` PASS (10 skills);
`python -m pytest -q` 57 passed.

## Post-audit disposition (implemented 2026-08-02)

The dispositions below were **implemented in the same cycle** (branch
`skill-hardening-product-manager-v1`). Current tree state: 14 active skills +
1 deprecated routing stub; `scripts/validate_skills.py` PASS (14 active + 1
deprecated); `python -m pytest -q` **80 passed** (57 original + 23 skill-pack).
The 5 new skills added by this cycle are scored in the section at the end of
this file. Findings #3 and #6 in the portfolio-level findings below are
historical — they describe the pre-hardening portfolio and are **resolved**
by this cycle (see the disposition table).

## How to read the scoring

Each existing skill is scored 1–10 on ten dimensions. Higher is better,
**including** "Academy overfitting risk" where 10 = low overfitting risk
(generalizes beyond the Academy) and 1 = high overfitting risk (only useful
inside the Academy's taxonomy/registry).

- **PM relevance** — does it solve a recognizable product-management job?
- **Frequency** — how often a working PM hits this situation?
- **Actionability** — does it produce a concrete artifact / next action?
- **Differentiation** — is it better than a generic prompt / RICE template?
- **Input realism** — can a PM supply the inputs from real work, imperfectly?
- **Output quality** — is the verdict contract reproducible and decision-grade?
- **Proportionality** — does process scale to the risk of the decision?
- **Composability** — does it chain into and out of other skills?
- **Agent usability** — can Claude/Codex/Cursor/OpenCode consume it without the Academy?
- **Overfitting risk** — how Academy-internal are its inputs, vocabulary, and gates?

Dispositions: KEEP / REWRITE / MERGE / DEPRECATE / REPOSITION.

---

## 1. `audit-decision-evidence` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 7 | Grading a decision claim-by-claim is a real job; framing assumes an Academy registry. |
| Frequency | 5 | Pre-decision and post-launch reviews, not weekly. |
| Actionability | 6 | Per-claim verdict is actionable, but depends on registry/corroboration machinery. |
| Differentiation | 6 | Evidence grading is rare in skill packs; the tier vocabulary is the weak part. |
| Input realism | 5 | Assumes claims can be mapped to `SRC-*` registry IDs; real PMs have internal evidence. |
| Output quality | 7 | Verdict contract (per-claim + decision verdict) is strong. |
| Proportionality | 5 | No fast path; full audit ceremony even for reversible calls. |
| Composability | 6 | Chained to tier-check, contradictions, causal review. |
| Agent usability | 7 | Well structured; requires registry files to be present. |
| Overfitting risk | 3 | Ledger, corroboration matrix, A–E tiers, `CLM-` IDs are all Academy-internal. |

**Disposition: REWRITE.** Fold `run-source-tier-check` in as a sub-mode.
Expand evidence taxonomy beyond published sources to include the internal
product evidence a PM actually holds (analytics, cohorts, interviews, support,
sales, experiments, incidents). Add fast/full modes and a missing-data rule
("record the absence; never pad it").

## 2. `run-source-tier-check` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 3 | Certifying a source's evidence tier is a researcher's job, not a PM's. |
| Frequency | 3 | A PM does this rarely; when they do, they want a credibility call, not a tier. |
| Actionability | 5 | Verdict is crisp; the fix (correct the tier) is not a PM action. |
| Differentiation | 5 | Fine, but the A–E tier system is Academy-specific. |
| Input realism | 4 | Requires registry metadata most PMs never produce. |
| Output quality | 6 | Reproducible, well-documented. |
| Proportionality | 4 | Heavy formal apparatus for a simple credibility question. |
| Composability | 5 | Only composes with other Academy evidence skills. |
| Agent usability | 7 | Clean structure. |
| Overfitting risk | 3 | Entirely built on `SOURCE_POLICY.md` tiers. |

**Disposition: MERGE (into `audit-decision-evidence`), standalone DEPRECATED.**
Keep the "popularity is not evidence" and "commercial incentive" tests as a
sub-check inside the evidence audit. Remove the standalone folder from the
plugin manifest and index; add a deprecated-routing note. Rationale: the job
it serves ("is this source credible enough to support this claim?") is one
step of evidence auditing, and the standalone skill adds navigation cost.

## 3. `scan-contradictions-assumptions` (assist)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 8 | Assumption surfacing before a locked decision is directly useful. |
| Frequency | 7 | Stakeholder stalemates and pre-commitment reviews are common. |
| Actionability | 7 | Ranked assumption list + contradiction verdicts; the "top assumption" is concrete. |
| Differentiation | 7 | Assumption registers are common; the tension/polarity framing is rarer. |
| Input realism | 6 | Works from a decision statement; the CON-mapping step needs the register. |
| Output quality | 7 | Reproducible ranking rule (blast radius). |
| Proportionality | 6 | 13-contradiction sweep is heavy for a reversible call. |
| Composability | 7 | Feeds premortem, evidence audit, causal review. |
| Agent usability | 7 | Method is linear and askable. |
| Overfitting risk | 4 | High risk of force-fitting decisions into CON-0001..0013. |

**Disposition: REWRITE.** Discovery-first: surface assumptions and
contradictions from the user's actual situation; then map relevant items to
the Academy registry as a *reference set*, never a closed ontology. Add fast
mode (assumption register only, no CON sweep) and make the CON-mapping an
optional full-mode step.

## 4. `conduct-causal-confidence-review` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 8 | "X caused Y" scrutiny is load-bearing in post-launch and expansion calls. |
| Frequency | 5 | Monthly-class, not weekly. |
| Actionability | 7 | Verdict + what-would-flip-it is decision-grade. |
| Differentiation | 8 | Causal-confidence grading is rare and valuable. |
| Input realism | 6 | Requires baseline/counterfactual/segments; PMs have these imperfectly. |
| Output quality | 8 | Strong verdict contract, aligned to the case catalog scale. |
| Proportionality | 5 | No fast mode for reversible, low-stakes causal questions. |
| Composability | 6 | Chains with evidence audit and contradictions. |
| Agent usability | 7 | Linear method. |
| Overfitting risk | 6 | Moderate; catalog scale is reference, not required. |

**Disposition: REWRITE.** Keep the causal-grading core (it is the portfolio's
sharpest differentiator) but reframe for PM situations (post-launch credit,
experiment readouts, expansion bets), add fast/full modes, and connect to the
new experiment-design skill as the "before" half.

## 5. `make-go-no-go-call` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 9 | The central PM decision. |
| Frequency | 6 | Several times a year per initiative; gates and quarterly reviews. |
| Actionability | 9 | GO/NO-GO/PAUSE/SEEK-MORE-EVIDENCE/PROCEED-AT-RISK with thresholds. |
| Differentiation | 8 | Verdict contract beats generic pros/cons. |
| Input realism | 7 | Strategy, evidence tiers, confidence, effort, value range are all supply-able. |
| Output quality | 9 | Reproducible threshold ladder. |
| Proportionality | 6 | Full ladder is heavy; a fast variant for reversible/low-risk calls is missing. |
| Composability | 8 | Intended as the terminal node of a decision workflow. |
| Agent usability | 8 | Clean; the `$ARGUMENTS`-free design helps. |
| Overfitting risk | 7 | RICE-LM and the strategy gate are near-universal; low overfitting. |

**Disposition: REWRITE.** Add a fast mode (reversible, low-stakes calls use a
compressed question set and a provisional verdict with explicit uncertainty).
Strengthen the SEEK-MORE-EVIDENCE guard against disguised indecision. Output
schema to match the shared contract.

## 6. `classify-decision-reversibility` (assist)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 9 | Every significant decision deserves a reversibility check. |
| Frequency | 8 | Weekly for working PMs. |
| Actionability | 8 | Process budget + escalation + required artifacts. |
| Differentiation | 7 | Type-1/Type-2 is well known; the Knight test is the differentiator. |
| Input realism | 8 | Costs, reversal mechanism, escalation are knowable. |
| Output quality | 8 | Reproducible TYPE-1/TYPE-2/RECLASSIFIED thresholds. |
| Proportionality | 8 | The whole point is proportionality; well handled. |
| Composability | 8 | First node of the launch/workflow chain. |
| Agent usability | 8 | Linear, askable. |
| Overfitting risk | 6 | Amazon two-door framing is standard; light Academy vocabulary. |

**Disposition: KEEP (hardened).** Add the shared-contract sections that are
missing (missing-data behavior, context classification, output schema,
reversal conditions as explicit flip-lines) and a fast rule-of-thumb mode.
Content is sound; treat as the reference for how a decision-gate skill should
be built.

## 7. `run-case-based-premortem` (assist)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 8 | Pre-commitment failure surfacing is a genuine PM job. |
| Frequency | 5 | Pre-launch / pre-commit / Type-1 gate; not weekly. |
| Actionability | 8 | Ranked scenarios, signals, owners, mitigations — very concrete. |
| Differentiation | 8 | Case-calibrated scenarios ("this is the Knight Capital pattern") are rare. |
| Input realism | 6 | Requires failure narratives from the team; PMs can supply, but it is effortful. |
| Output quality | 8 | Exposure ranking + DEFENSIBLE verdict ladder. |
| Proportionality | 6 | No fast variant; the full ritual is heavy for reversible calls. |
| Composability | 7 | Feeds GO/NO-GO; depends on reversibility classification. |
| Agent usability | 7 | Method is clear; the case-calibration step needs the catalog. |
| Overfitting risk | 6 | Case IDs are reference; the method is standard premortem discipline. |

**Disposition: REWRITE.** Add a fast variant (single-pass top-3 scenarios,
no catalog calibration) and an explicit guard against "pattern-name
inflation" (case pattern requires its mechanism, not its brand). Keep the
ranking contract.

## 8. `pressure-test-product-thesis` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 8 | Falsifiability before resource commitment is a core PM discipline. |
| Frequency | 6 | Per new bet / board cycle. |
| Actionability | 8 | FALSIFIABLE/BELIEF/UNDERSPECIFIED verdict + flip conditions. |
| Differentiation | 8 | "Thesis vs belief" is sharper than generic "validate your idea." |
| Input realism | 7 | A stated thesis + evidence + pending decision is exactly what a PM has. |
| Output quality | 8 | Reproducible slot-based thresholds. |
| Proportionality | 6 | No fast mode; 7-question method is heavy for reversible bets. |
| Composability | 8 | Before-half for AI contract, PMF, GO/NO-GO. |
| Agent usability | 8 | Clean. |
| Overfitting risk | 7 | Theranos is a universal cautionary case, not Academy-specific. |

**Disposition: REWRITE.** Add fast/full modes and an explicit tie to the new
`frame-product-problem` skill (a thesis that cannot fill the four slots is
usually a framing failure). Keep the falsifiability core.

## 9. `check-ai-evaluation-contract` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 8 | For AI PMs this is the launch gate. |
| Frequency | 5 | Per AI build / model swap / incident review. |
| Actionability | 9 | CONTRACT-COMPLETE/GAPPY/NO-CONTRACT with specific gap names. |
| Differentiation | 9 | Almost no other skill pack has an evaluation-contract check. |
| Input realism | 7 | Contract, stage, workflow are supply-able; exact numbers often live in the doc. |
| Output quality | 9 | Five-check standard, silent-failure rollback, human baseline. |
| Proportionality | 6 | No fast mode for low-risk AI features. |
| Composability | 7 | Pairs with thesis (before) and PMF health (after). |
| Agent usability | 8 | Clean, linear. |
| Overfitting risk | 7 | The five checks generalize; the module file names are Academy-internal. |

**Disposition: KEEP (hardened).** Add fast mode (a 3-question readiness
pre-check), missing-data behavior, output schema, and reversal conditions.
This is a flagship skill; do not dilute it.

## 10. `assess-product-market-fit-health` (assess)

| Dimension | Score | Note |
|---|---|---|
| PM relevance | 9 | PMF health is a top-of-mind board/leadership question. |
| Frequency | 7 | Quarterly review plus ad-hoc "is PMF decaying?" |
| Actionability | 8 | HEALTHY/DECAYING/NEVER-ACHIEVED/UNMEASURED verdicts drive action. |
| Differentiation | 7 | Leading-vs-lagging framing is good; the indicator set is not. |
| Input realism | 5 | Sean Ellis / organic-share / win-loss presumes self-serve or sales products; poor for marketplaces, enterprise, episodic, internal platforms. |
| Output quality | 8 | Reproducible thresholds; the 40% Sean Ellis universal is a liability. |
| Proportionality | 6 | Four-indicator sweep with no lightweight variant. |
| Composability | 7 | After-half of thesis; before-half of GO/NO-GO. |
| Agent usability | 8 | Clean. |
| Overfitting risk | 4 | Universal thresholds + a fixed four-indicator battery = overgeneralized. |

**Disposition: REWRITE (repositioned to also cover product-health diagnosis).**
Make the assessment adaptive to product archetype (enterprise, PLG SaaS,
consumer subscription, marketplace, dev tool, usage-based, regulated,
episodic, internal platform, pre-revenue). Separate PMF into independent
dimensions: product value, retention, acquisition efficiency, expansion,
monetization, competitive pull, user dependence, market constraints. Remove
the universal 40% threshold as a hard gate; keep it only where the archetype
and evidence support it. Because it now also reads activation/retention/
engagement/unit-economics signals, it serves the general "product health
diagnosis" job, closing the portfolio's biggest execution gap.

---

## Portfolio-level findings

1. **Evidence taxonomy is published-source-centric.** All evidence grading
   assumes `SRC-*` registry IDs and A–E tiers. A PM's strongest evidence is
   often internal (cohort retention, funnel analytics, interview patterns,
   support data, sales loss reports, incidents). The taxonomy must be expanded.
   → **RESOLVED:** shared 15-type taxonomy (`_shared/SKILL_CONTRACT.md`), internal
   evidence first-class; `audit-decision-evidence` rewritten.

2. **No fast mode anywhere.** Every skill runs one ceremony regardless of
   decision reversibility or stakes. Reversible, low-risk calls get the same
   process as Type-1 launches. → **RESOLVED:** fast/full contract enforced by
   validator and tests; mode gates added to all workflows.

3. **Six high-frequency PM jobs are missing entirely:**
   framing a product problem, synthesizing customer discovery, prioritizing
   opportunities, designing an experiment, aligning stakeholders on a
   decision, and general product-health diagnosis.
   → **RESOLVED:** five new skills added (frame, synthesize, prioritize,
   design-experiment, align-stakeholders); product-health gap solved by the
   archetype-adaptive repositioning of skill #10.

4. **PMF skill overgeneralizes** Sean Ellis/organic/win-loss across all
   products. → **RESOLVED:** archetype-adaptive rewrite; no universal 40%.

5. **Contradiction scan risks closed-ontology force-fitting.** The 13
   Academy contradictions are treated as a checklist applied to every decision.
   → **RESOLVED:** discovery-first rewrite; registry is a reference set.

6. **No workflows, no evals, no finder.** The pack is 10 standalone verdict
   skills. Nothing tells a PM which skill starts where, how they chain, or
   what a good request looks like. → **RESOLVED:** 4 workflows, 12 eval
   scenarios + rubric + report, finder in `INDEX.md`.

7. **Packaging is coherent** (validator, packager, plugin manifest, CI release
   workflow, `dist/` artifacts) but hard-codes "the 10 P0 skills" and the
   manifest skill list, both of which must change with the portfolio.
   → **RESOLVED:** packager + manifest updated for 14 active skills; core
   ZIP is a self-contained 8-skill starter.

## Disposition summary (implemented 2026-08-02)

| Skill | Disposition | Status |
|---|---|---|
| audit-decision-evidence | REWRITE (+ absorbs run-source-tier-check) | implemented |
| run-source-tier-check | MERGE → audit-decision-evidence; DEPRECATE standalone | implemented (routing stub) |
| scan-contradictions-assumptions | REWRITE (discovery-first) | implemented |
| conduct-causal-confidence-review | REWRITE (fast/full, PM framing) | implemented |
| make-go-no-go-call | REWRITE (fast/full, proportionality) | implemented |
| classify-decision-reversibility | KEEP (hardened to shared contract) | implemented |
| run-case-based-premortem | REWRITE (fast variant, pattern-inflation guard) | implemented |
| pressure-test-product-thesis | REWRITE (fast/full, framing tie-in) | implemented |
| check-ai-evaluation-contract | KEEP (hardened to shared contract) | implemented |
| assess-product-market-fit-health | REWRITE (archetype-adaptive + product health) | implemented |

## New skills added this cycle (Phase 5)

All five are `assist`-type decision artifacts. Scores are initial assessments
pending field repetition; they are the same 10 dimensions, abbreviated.

| Skill | PM relevance | Frequency | Actionability | Differentiation | Input realism | Output quality | Proportionality | Composability | Agent usability | Overfitting risk |
|---|---|---|---|---|---|---|---|---|---|---|
| frame-product-problem | 9 | 9 | 8 | 7 | 9 | 8 | 8 | 9 | 9 | 8 |
| synthesize-customer-discovery | 8 | 7 | 8 | 9 | 8 | 8 | 7 | 8 | 8 | 9 |
| prioritize-product-opportunities | 9 | 9 | 8 | 7 | 8 | 8 | 7 | 8 | 8 | 8 |
| design-product-experiment | 8 | 8 | 9 | 8 | 8 | 9 | 8 | 9 | 8 | 9 |
| align-stakeholders-on-decision | 8 | 7 | 8 | 9 | 9 | 8 | 8 | 7 | 8 | 9 |

## Non-negotiable acceptance gates from this audit

- Every surviving skill ships the shared contract (fast/full, missing-data,
  context classification, output schema, reversal conditions, composition).
- Deprecated skills still resolve: index/validator route to their replacement.
- No universal PMF thresholds survive without an archetype qualifier.
- No evidence claim may depend on published sources alone.
