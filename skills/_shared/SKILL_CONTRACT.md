# Shared Skill Contract (v1)

Every production skill in this pack conforms to this contract. A skill either
contains each contract element inline or references this file explicitly and
follows its conventions. The validator (`scripts/validate_skills.py`) enforces
that every production `SKILL.md` has the required sections; this file defines
what those sections mean and how they stay consistent across the pack.

## 1. Required sections in every production SKILL.md

Order is normative for agent parsing:

1. `## Purpose` — the decision the skill produces, and when NOT to run it.
2. `## Use when` — concrete trigger situations (3–6 bullets).
3. `## Do not use when` — explicit exclusions (reversible/low-risk calls,
   document requests, adjacent skills' jobs).
4. `## Inputs` — Required inputs (the minimum to reach a useful provisional
   verdict) and Optional inputs (what upgrades the verdict from provisional to
   full).
5. `## Missing-data behavior` — what the skill does when a required input is
   "I don't know": record as an explicit assumption, downgrade confidence,
   name the cheapest way to resolve it. Never silently pad.
6. `## Context classification` — how the skill adapts to the situation:
   decision reversibility (Type-1/Type-2 per `classify-decision-reversibility`),
   product archetype (from the taxonomy in §3), stakes, and time budget.
7. `## Fast mode` — the compressed run for reversible or ordinary decisions:
   minimum questions, provisional verdict, explicit uncertainty, clear next
   action, no research ceremony.
8. `## Full mode` — the rigorous run: source verification, internal evidence
   analysis, contradiction review, causal-confidence assessment, premortem,
   decision thresholds, reproducible verdict.
9. `## Method` — step-by-step reasoning, one question at a time. "Unknown"
   answers become stated assumptions, never silent defaults.
10. `## Evidence classification` — how this skill sorts evidence: the shared
    taxonomy (§2) plus any skill-specific weighting rule. Ranking depends on
    the claim being evaluated, never on a blanket preference for published
    research.
11. `## Output schema` — the machine-parseable shape of the artifact (§5).
12. `## Verdict Contract` — the decision/action contract (§4): verdict set,
    confidence label, assumptions, what-would-change-it, and the **next
    action** the verdict mandates.
13. `## Failure modes` — named failure modes with concrete corrections.
14. `## Reversal conditions` — the observable conditions under which the
    verdict should be revisited or rolled back.
15. `## Worked example` — one realistic, calibrated example from input to
    verdict.
16. `## Composition hooks` — which skills run before/after, and the artifact
    handoff between them (see `workflows/`).
17. `## Related Skills` — explicit cross-links.

The old standalone `## Common Pitfalls` section is renamed `## Failure modes`;
`## Thresholds` content folds into `## Verdict Contract`.

## 2. Evidence taxonomy (shared)

Every skill that grades evidence uses these 15 types. **No type outranks
another by default.** Ranking is decided by the specific claim being
evaluated — a claim about user behavior is best served by behavioral product
analytics or a controlled experiment; a claim about a market shift may be best
served by market evidence or published research.

| # | Evidence type | What it is | Strong for | Weak when |
|---|---|---|---|---|
| E1 | Controlled experiment | Randomized A/B, holdout, pre-registered test | Causal claims about user behavior | Small n, short duration, novelty effects |
| E2 | Quasi-experiment | Cohort/segment comparison, difference-in-difference, natural experiment | Causal claims without full randomization | Selection, confounds |
| E3 | Behavioral product analytics | Funnel, session, feature-usage telemetry | What users actually do | "Do" != "why"; self-select bias |
| E4 | Cohort / retention evidence | Retention curves, activation cohorts, NRR by cohort | Whether value persists | Requires cohort hygiene |
| E5 | Customer interview | Structured/unstructured user conversations | Needs, jobs-to-be-done, problem framing | Loud anecdotes; what people say != do |
| E6 | Usability observation | Task-based observation, prototype testing | Whether users can use it | Non-representative participants |
| E7 | Support evidence | Tickets, contact reasons, bug reports, escalation | What breaks, friction points | Only the loudest/failing users |
| E8 | Sales / loss evidence | Win-loss notes, lost-deal reviews, deal forensics | Why people buy/decline | Salesperson incentives, small sample |
| E9 | Market evidence | TAM/SAM, competitor analysis, pricing signal, GTM response | Market-level claims | Secondhand; quickly stale |
| E10 | Operational incident | Outage, SEV, reliability event postmortems | Risk/reliability claims | Rare events, hindsight bias |
| E11 | Financial evidence | Unit economics, CAC/LTV, margin, forecast | Business-model claims | Gaming, misattribution |
| E12 | Practitioner doctrine | Published frameworks, expert opinion, books, talks | Framing, heuristics, options | Universal claims; authority != evidence |
| E13 | Published research | Peer-reviewed or rigorous industry research | Generalizable mechanisms | External validity to your context |
| E14 | Inference | Reasoned derivation from other evidence | Filling measured gaps | Passing off assumption as fact |
| E15 | Unsupported assertion | Claim with no traceable basis | Nothing — flagged for resolution | Everything |

Source-tier checking (the deprecated `run-source-tier-check`) survives inside
`audit-decision-evidence` as the credibility test applied to **any** of these
types, including internal evidence (E3–E8, E10–E11) which must name the
collection method, the sample, and the date.

## 3. Context classification

Two axes every skill should classify:

**A. Decision reversibility** (from `classify-decision-reversibility`):
- `TYPE-1` — irreversible or very expensive to reverse → Full mode is
  mandatory, premortem and escalation required.
- `TYPE-2` — reversible at acceptable cost → Fast mode is the default; Full
  mode optional.
- `RECLASSIFIED-TYPE-1` — claimed reversible but not demonstrated → treat as
  Type-1 until the reversal is tested.

**B. Product archetype** (drives what counts as evidence and which thresholds
apply, especially in PMF/health and experiment skills):

| Archetype | Signature evidence | PMF/health proxy |
|---|---|---|
| B2B enterprise | Win/loss, expansion NRR, implementation success, referenceability | Renewal + expansion, not Sean Ellis |
| Product-led SaaS | Activation, self-serve conversion, feature adoption, NRR | Activation + retention cohorts + monetization |
| Consumer subscription | Retention curve, churn, DAU/WAU, payback | Cohort retention + willingness-to-re-subscribe |
| Marketplace | Liquidity, fill rate, take rate, time-to-first-match | Both-side retention + liquidity, not organic share |
| Developer tool / API | Time-to-first-value, API adoption, sandbox→prod | Activation + usage depth + community pull |
| Usage-based product | Seat/consumption growth, overage, expansion | Usage growth + net expansion |
| Regulated product | Compliance evidence, audit outcomes, safety | Compliance + reliability, not virality |
| Episodic product | Re-engagement, event-to-event interval | Repeat-usage cadence + intent |
| Internal platform | Adoption, developer velocity, incident rate | Adoption + reliability + org pull |
| Pre-revenue / pre-launch | Signal proxies: pilots, LOIs, waitlists, interviews | Signal quality + cohort-of-signals, never fake revenue |

## 4. Verdict / decision contract

Every verdict output must contain:

- **Verdict:** one of a small, skill-specific set of labels.
- **Confidence:** High / Medium / Low, with the single biggest reason for the
  downgrade, if any.
- **Evidence basis:** the evidence types (§2) actually used, and which claims
  each supports.
- **Assumptions:** everything answered "unknown", each with the effect it has
  on the verdict.
- **What would change the verdict:** the specific, named evidence that flips
  it (not "more data").
- **Next action:** the concrete, owner-able step the verdict mandates. A
  verdict without a next action is a memo.

## 5. Output schema

Every skill's artifact is a fenced JSON block with this envelope. Skills add
skill-specific fields.

```json
{
  "skill": "skill-name",
  "version": "0.2.0",
  "mode": "fast | full",
  "verdict": "VALUE",
  "confidence": "high | medium | low",
  "evidence_basis": ["E3", "E5"],
  "assumptions": [{"statement": "...", "effect_on_verdict": "..."}],
  "what_would_change_the_verdict": "...",
  "next_action": {"what": "...", "who": "...", "by_when": "..."},
  "reversal_conditions": ["..."]
}
```

## 6. Fast vs full mode rules

- **Fast mode** is the default for TYPE-2 decisions. Minimum question set,
  provisional verdict, explicit uncertainty, next action, no research
  ceremony. If a fast-mode run hits an "unknown" on a load-bearing input, it
  does NOT auto-escalate to full mode; it returns the provisional verdict with
  the assumption named and offers Full mode as the option.
- **Full mode** is mandatory for TYPE-1 decisions and for decisions where the
  fast-mode verdict would be Low confidence on a load-bearing claim. It may
  include source verification, internal evidence analysis, contradiction
  review, causal-confidence assessment, premortem, and reproducible
  thresholds. Process must never exceed the risk of the decision (PRN-0003).

## 7. Reversal conditions

Every skill names the observable conditions under which its verdict is
revisited: a metric hitting a threshold, a named owner triggering a rollback,
or evidence that contradicts a stated assumption. Reversal is cheap to
specify and expensive to retrofit — specify it in the same session as the
verdict.

## 8. Composition hooks

Skills compose by passing artifacts. The `## Composition hooks` section of
each skill names:

- **before** — skills whose artifact is required or recommended input.
- **after** — skills that consume this skill's artifact.
- **workflow** — the named workflow(s) this skill participates in.

The canonical compositions are defined in `workflows/` and are validated to
reference only existing skills.

## 9. Academy doctrine references

Skills cite doctrine by stable ID (`PRN-xxxx`, `CON-xxxx`, `CASE-xxxx`,
`SRC-xxxx`, `09_tools/<FILE>.md`, `05_ai_product_management/<FILE>.md`). The
Academy is the *evidence and judgment layer*; the skills are the *execution
layer*. A skill must be usable without reading the Academy — doctrine is
cited, not required reading. Citation = short line + ID + location, never
reproduction.
