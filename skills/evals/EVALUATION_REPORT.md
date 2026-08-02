# Skills Evaluation Report

Date: 2026-08-02. Method: scripted self-runs of the skills against 12 realistic fixtures
(see `scenarios/`), scored against `rubric.md` (8 dimensions, 1–5). Independent adversarial
review of the fixtures, the skills, and the packaging is recorded in
`../quality/ADVERSARIAL_REVIEW_2026-08-02.md` (a second agent's structural and reasoning
review; it returned ACCEPT_WITH_BOUNDED_FIXES, and its findings are tracked there).

**Honesty statement.** The fixture runs are **authoring-agent self-runs**, not independent
third-party evaluations. Two limits follow and are not argued away:

1. **"Correctness" below means internal consistency**: the run produced the verdict the
   skill's own contract and the fixture's evidence support, judged by the author. It is NOT
   independent validation that the verdict matches ground truth a second model would confirm.
   The aggregate "Dim mean" is a measure of self-consistency and usability, not of
   superiority over alternative tools.
2. No scenario was awarded a score the run record did not demonstrate — but the run records
   are narrative reconstructions of the skill methods, not transcripts or tool output.

The portfolio is **not** claimed to be 9/10 — the gap analysis below says what that would
take, including independent behavioral evaluation.

## Coverage of the scenario matrix

| Scenario | Domain | Situation | Skills exercised |
|---|---|---|---|
| S01 bespoke feature request | B2B enterprise | conflicting stakeholders, customer pressure | frame, prioritize, go-no-go |
| S02 activation vs retention gap | PLG SaaS | product health, mature | PMF/health, contradictions, experiment |
| S03 AI demo vs evaluation design | AI | high-risk launch, weak evidence | thesis, eval-contract, premortem, go-no-go |
| S04 interview vs usage behavior | consumer | weak evidence, conflicting signals | discovery synthesis, causal review, prioritize |
| S05 launch before reliability | enterprise/platform | irreversible-ish, sponsor pressure | reversibility, premortem, evidence, go-no-go |
| S06 sales/product/eng disagreement | B2B SaaS | conflicting stakeholders | alignment, eval-contract, go-no-go |
| S07 marketplace liquidity | marketplace | health misdiagnosis by vanity metric | PMF/health, discovery, prioritize |
| S08 vanity metric as PMF proof | early-stage | early-stage, weak evidence | thesis, PMF/health, evidence |
| S09 dev tool time-to-value | developer tooling | mature, activation diagnosis | frame, experiment, discovery, PMF/health |
| S10 reversible button move | SaaS | reversible, low-stakes | reversibility, go-no-go (fast) |
| S11 pricing restructure | SaaS | irreversible, high-risk | reversibility, evidence, premortem, go-no-go |
| S12 founder non-falsifiable thesis | early-stage | early-stage, weak evidence | frame, thesis, evidence, PMF/health |

## Scores by scenario and dimension

| Scenario | Rel | Cor | Act | Unc | Ev | Pro | Theater | Clarity | Mean |
|---|---|---|---|---|---|---|---|---|---|
| S01 | 5 | 5 | 4 | 4 | 4 | 4 | 4 | 5 | 4.4 |
| S02 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | 5 | 4.6 |
| S03 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4.6 |
| S04 | 5 | 5 | 4 | 4 | 5 | 3 | 4 | 5 | 4.4 |
| S05 | 5 | 5 | 4 | 4 | 4 | 4 | 5 | 5 | 4.5 |
| S06 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 5 | 4.6 |
| S07 | 5 | 5 | 4 | 4 | 5 | 4 | 4 | 5 | 4.5 |
| S08 | 5 | 5 | 4 | 5 | 5 | 4 | 5 | 5 | 4.75 |
| S09 | 5 | 5 | 5 | 5 | 5 | 4 | 4 | 5 | 4.6 |
| S10 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 5 | 4.75 |
| S11 | 5 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 4.75 |
| S12 | 5 | 5 | 4 | 5 | 5 | 4 | 4 | 5 | 4.5 |
| **Dim mean** | **5.0** | **5.0** | **4.2** | **4.4** | **4.75** | **4.1** | **4.3** | **5.0** | **4.56** |

## What the numbers do and do not mean

- **Relevance and Clarity and Correctness at 5.0** are the honest strong points: every
  scenario mapped to a real PM job, every run produced an unambiguous decision that matched
  the fixture's evidence-grounded answer, and no category errors (facts-vs-goals,
  signups-vs-PMF, interview-vs-behavior) occurred.
- **Proportionality is the weakest dimension (4.1).** S04, S09, and S12 scored 3–4 because the
  portfolio still makes it easy to over-chain: nothing *enforces* the fast path, and several
  realistic weekly decisions pulled in three or four skills before the fast modes narrowed
  the work. The fast modes exist; the discipline is advisory.
- **Actionability (4.2)** is capped by design-detail gaps: the skills name the next action
  precisely but repeatedly hand off to the team or to Academy templates for the *artifact*
  itself (contract drafting, pilot design, instrumentation).
- **Uncertainty handling (4.4)** is strong but not perfect: S01 and S07 left some
  handoff-adjacent unknowns unrecorded.

## Verified strengths

1. The evidence taxonomy works: internal evidence (E3/E4/E7/E8) carried every product-health
   and experiment verdict, and claim-evidence mismatch (signups-as-PMF, interview-as-demand)
   was caught in every fixture where it appeared.
2. The fast/full contract is real and correct when used (S10 is the proof).
3. The reversibility + premortem + GO/NO-GO chain is the portfolio's strongest composition
   (S05, S11).
4. The alignment skill's fact/goal/incentive/risk/rights typing resolves a three-sided
   deadlock that evidence alone could not (S06).
5. Deprecated routing (source-tier → evidence audit sub-mode) held without breaking any run.

## Verified weaknesses (honest failures)

1. **Proportionality is advisory, not enforced.** Nothing prevents an agent from running the
   full chain on a button move. The contract says fast mode is default; there is no
   enforcement hook.
2. **Handoff-dependent artifacts.** The highest-leverage outputs — evaluation contracts,
   reversibility designs (grandfathering/phasing), corrective pilot specs for marketplace
   matching — are produced as pointers to Academy templates, not as first-class skill
   artifacts. The skills say *what* to build but not *how to draft it*.
3. **Marketplace and matching-model coverage is thin.** The PMF skill handles liquidity, but
   the corrective path for a matching-model change has no skill of its own; the experiment
   skill is written for a single metric change.
4. **Founder usability lags PM usability.** S12 shows a four-skill chain on a founder's
   pre-raise thesis. Each step is fast; the *sequence* reads as process to a founder. The
   index must route single-request entries so the chain is invisible when not needed.
5. **No strategy-production skill.** S06 and S11 both hit the "no written strategy" wall; the
   portfolio can flag the gap but not close it.
6. **Evals are self-runs.** No independent tool ran the fixtures; the
   [adversarial review](../quality/ADVERSARIAL_REVIEW_2026-08-02.md) is a structural and
   reasoning review by a second agent, not a behavioral A/B against another skill system.
   Independent behavioral evaluation remains an open requirement (see gap 3 below).

## What remains between this portfolio and a genuine 9/10

1. **Enforced proportionality.** A routing/entry gate (in the index and, where possible, the
   plugin) that selects fast vs full by reversibility class before any skill runs, plus an
   eval scenario where the agent is *tempted* to over-process and the gate stops it.
2. **First-class drafting artifacts.** Either new skills or explicit drafting sub-modes for
   the evaluation contract, the reversibility/grandfathering design, and the corrective pilot
   spec — turning pointers into deliverables.
3. **Independent behavioral evaluation.** Third-party or cross-model runs of the same 12
   fixtures, scored blind, to validate that the skills' verdicts hold outside the authoring
   context and to build a regression suite for future changes.
4. **Marketplace/algorithmic corrective guidance** and a **strategy-statement skill** to close
   the two documented gaps (S06, S07, S11).
5. **Founder/agent onboarding proof.** A measured test that a first-time user can route from a
   plain-language problem to the right skill in under 60 seconds (Phase 8 target).
