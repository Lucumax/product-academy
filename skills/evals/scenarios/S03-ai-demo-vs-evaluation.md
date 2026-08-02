# Scenario 3 — AI Feature: Impressive Demos, Weak Evaluation Design

**Domain:** AI product. **Type:** high-risk launch, weak evaluation evidence.

## Context

An AI "claims-summarization" feature has a stunning demo: the model summarizes legal
contracts fluently. The team wants to launch to all enterprise customers next quarter. There
is no written evaluation contract. Leadership is confident because "the demos are great."

## Inputs available (imperfect)

- Demo output quality: excellent on the 5 prepared examples.
- No failure taxonomy, no severity weights, no launch thresholds, no rollback triggers, no
  human-baseline comparison, no monitoring plan.
- Engineering says "we'll iterate after launch."
- The surface is customer-facing in legal workflows (high stakes).

## Skills applied and run record

**1. `pressure-test-product-thesis` (full).** Claim slots: segment (enterprise legal), problem
(contract-review bottleneck), mechanism (AI summarization), outcome (faster review). Falsification
condition: none articulable beyond "we'll iterate." Evidence: entirely presentation-derived
(demos). Verdict: `BELIEF-PRESENTED-AS-THESIS`, High confidence. Next action: write the
falsification test with a pre-committed NO-GO threshold.

**2. `check-ai-evaluation-contract` (full).** Five checks all fail: no failure taxonomy
(accuracy-only if any), no numeric launch thresholds, no rollback triggers including
silent-failure signals, no monitoring plan with owners, no human baseline. The demo is not a
contract. Verdict: `NO-CONTRACT`, High confidence. The output names what must exist before
build/launch spend continues and specifically the silent-failure rollback requirement
(hallucination/omission severity weights, human-review sampling, override-rate trigger).

**3. `run-case-based-premortem` (full).** Top scenarios: (1) silent mis-summarization of a
material clause — severity 5, probability 30%, pattern: launch-without-validation
(Theranos-analog, mechanism present: decision-makers insulated from verification); (2)
distribution shift as users vary contract style — severity 4, probability 40%, no case match;
(3) no one owns degradation monitoring — severity 4, probability 50%, no case match.
Verdict: `NOT-DEFENSIBLE` on the current state — a top-3 scenario (severity 4, probability
50%) has no mitigation in place and the team has declined to add one; the premortem names the
mitigations (evaluation contract with monitoring, named owners, rollback triggers) that would
move the verdict to `DEFENSIBLE-WITH-MITIGATIONS` if and only if they land.

**4. `make-go-no-go-call` (full).** GO conditions 4 and 6 fail (load-bearing claims have no
adequate evidence; AI surface has no contract). Verdict: `NO-GO` on launch; `SEEK-MORE-EVIDENCE`
is explicitly rejected as a softer label because no discriminating test window exists until a
contract and a pilot are designed. Next action: build the evaluation contract, run a
flag-gated pilot with human-review sampling, then re-run the gate.

## Verdict produced

NO-GO on launch until a written evaluation contract and a pilot with silent-failure rollback
exist. The demo is explicitly not evidence.

## Scores

| Dimension | Score | Note |
|---|---|---|
| Relevance | 5 | The canonical AI launch gate scenario. |
| Correctness | 5 | NO-CONTRACT + BELIEF verdicts match the fixture's ground truth. |
| Actionability | 4 | Next actions concrete; the contract-drafting pointer is a reference, not a built artifact. |
| Uncertainty handling | 5 | Every missing check recorded as a named gap, not an assumption; confidence High. |
| Evidence use | 5 | Demo correctly demoted to presentation (E15-grade for validation); contract standard cited. |
| Proportionality | 4 | Full chain appropriate to a customer-facing legal surface. |
| Avoidance of framework theater | 4 | No forced CON mapping; premortem case-matches required mechanisms before naming. |
| Clarity of final decision | 5 | NO-GO with the exact preconditions for GO. |

**Mean: 4.6.** Weakness noted: the "build the contract" next action points at the Academy
template but the skill does not draft one; a drafting skill would close the loop.
