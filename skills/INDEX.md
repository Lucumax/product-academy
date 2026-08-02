# Product Academy — Agent Skill Pack

Evidence-backed product **decisions**, executable by AI agents (Claude Code, Codex, Cursor,
ChatGPT, OpenCode) at the moment you have to decide.

**The Academy is the map. These skills turn the map into a decision.**

Every skill returns a **verdict or artifact** (GO/NO-GO, HEALTHY/DECAYING,
FALSIFIABLE-THESIS, a problem frame, a ranked backlog, an experiment spec…) with a confidence
label, its assumptions, the evidence that would change it, and a **next action** — never just
a formatted memo.

## 60-second start

1. **Install** (see below) or read the skills here in the repo.
2. **Pick your job** from the finder below.
3. **Copy-paste** the invocation for your agent.
4. The agent asks you 3–8 questions, marks "unknown" as assumptions, and returns a decision
   artifact with a next action.

If you only remember one rule: **reversible decision → fast mode; irreversible decision →
full mode.** Every skill has both.

## What problem can these skills solve?

| If your situation is… | Start here |
|---|---|
| "We should build X" but nobody has said what problem or outcome | [frame-product-problem](frame-product-problem/SKILL.md) |
| Interviews done, notes unsorted, enthusiasm vs usage conflict | [synthesize-customer-discovery](synthesize-customer-discovery/SKILL.md) |
| More opportunities than capacity, a big customer request landed | [prioritize-product-opportunities](prioritize-product-opportunities/SKILL.md) |
| A change is proposed and "we'll see if it works" is the plan | [design-product-experiment](design-product-experiment/SKILL.md) |
| Sales/Product/Engineering stuck; two reasonable people arguing past each other | [align-stakeholders-on-decision](align-stakeholders-on-decision/SKILL.md) |
| Is our PMF healthy or decaying? Is growth real? | [assess-product-market-fit-health](assess-product-market-fit-health/SKILL.md) |
| A decision is being defended with "the data" | [audit-decision-evidence](audit-decision-evidence/SKILL.md) |
| "It's reversible" — verify, don't accept | [classify-decision-reversibility](classify-decision-reversibility/SKILL.md) |
| Is this bet a thesis or a belief? | [pressure-test-product-thesis](pressure-test-product-thesis/SKILL.md) |
| "Our change caused the improvement" | [conduct-causal-confidence-review](conduct-causal-confidence-review/SKILL.md) |
| Before a Type-1 commitment, an overconfident team, a launch | [run-case-based-premortem](run-case-based-premortem/SKILL.md) |
| AI feature launch, model swap, post-incident | [check-ai-evaluation-contract](check-ai-evaluation-contract/SKILL.md) |
| Budget, headcount, kill review — the actual call | [make-go-no-go-call](make-go-no-go-call/SKILL.md) |

The full job→skill→workflow map lives in [PORTFOLIO_MAP.md](PORTFOLIO_MAP.md).

## Install

- **Any agent (native CLI, verified):** `npx skills add Lucumax/product-academy` — lists the 14 skills and installs your selection
- **Claude Code:** `/plugin marketplace add Lucumax/product-academy` then `/plugin install evidence-pack`
- **Claude.ai / Desktop:** download a ZIP and upload it
- **Codex / Cursor:** download a ZIP and drop it in `.agents/skills/` (Codex) or
  `.cursor/skills/` (Cursor); see the `INSTALL.md` in each ZIP

ZIP bundles (starter / all) are attached to GitHub Releases on this repo. Each skill is
self-contained (`SKILL.md` + `references/`); the shared contract
([`_shared/SKILL_CONTRACT.md`](_shared/SKILL_CONTRACT.md)) defines the evidence taxonomy and
output format all skills use.

## The 14 active skills

Active skills (the deprecated `run-source-tier-check` routing stub is listed separately below):

| Skill | Type | What it returns |
|---|---|---|
| [frame-product-problem](frame-product-problem/SKILL.md) | assist | Problem frame: user problem, segment, business outcome, solution, assumptions |
| [synthesize-customer-discovery](synthesize-customer-discovery/SKILL.md) | assist | Weighted theme table: repeated vs anecdote, stated vs actual |
| [prioritize-product-opportunities](prioritize-product-opportunities/SKILL.md) | assist | Ranked backlog with exposed uncertainty + strategic dependencies |
| [design-product-experiment](design-product-experiment/SKILL.md) | assist | Experiment spec: hypothesis, metric, pre-committed interpretation & stop rules |
| [align-stakeholders-on-decision](align-stakeholders-on-decision/SKILL.md) | assist | Disagreement map: facts / goals / incentives / risk / decision rights |
| [assess-product-market-fit-health](assess-product-market-fit-health/SKILL.md) | assess | HEALTHY / DECAYING / NEVER-ACHIEVED / UNMEASURED, archetype-adaptive |
| [audit-decision-evidence](audit-decision-evidence/SKILL.md) | assess | Per-claim evidence verdicts + GO / CONDITIONAL / NO-GO / LEARN |
| [scan-contradictions-assumptions](scan-contradictions-assumptions/SKILL.md) | assist | Assumption register + discovered tensions (discovery-first) |
| [conduct-causal-confidence-review](conduct-causal-confidence-review/SKILL.md) | assess | CAUSAL / CORRELATED / NARRATIVE / INSUFFICIENT-INFO |
| [make-go-no-go-call](make-go-no-go-call/SKILL.md) | assess | GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK |
| [classify-decision-reversibility](classify-decision-reversibility/SKILL.md) | assist | TYPE-1 / TYPE-2 / RECLASSIFIED-TYPE-1 + process budget |
| [run-case-based-premortem](run-case-based-premortem/SKILL.md) | assist | Ranked failure scenarios + DEFENSIBLE verdict |
| [pressure-test-product-thesis](pressure-test-product-thesis/SKILL.md) | assess | FALSIFIABLE-THESIS / BELIEF-PRESENTED-AS-THESIS / UNDERSPECIFIED |
| [check-ai-evaluation-contract](check-ai-evaluation-contract/SKILL.md) | assess | CONTRACT-COMPLETE / GAPPY / NO-CONTRACT |
| [run-source-tier-check](run-source-tier-check/SKILL.md) | assess | **DEPRECATED** → merged into `audit-decision-evidence` |

## Skill anatomy

Every production skill has the same sections: Purpose; Use when; Do not use when; Inputs;
Missing-data behavior; Context classification; **Fast mode**; **Full mode**; Method; Evidence
classification; Output schema; Verdict Contract (verdict + confidence + evidence basis +
assumptions + what-would-change-it + **next action**); Failure modes; Reversal conditions;
Worked example; Composition hooks. The shared contract
([`_shared/SKILL_CONTRACT.md`](_shared/SKILL_CONTRACT.md)) defines the 15-type evidence
taxonomy and the JSON output envelope.

## Copy-paste invocations

**Claude Code / Codex / Cursor / OpenCode — replace the bracketed text:**

```
Run the frame-product-problem skill. Input: "We should build a [X] for [customers]."
We have no problem statement yet. Return the problem frame and the next action.
```

```
Run the make-go-no-go-call skill. Input: we want to [fund/ship X]. Strategy: [paste or
say none]. Evidence: [claims + what backs them]. Effort: [X]. This is [reversible /
not]. Use full mode if it's one-way-door.
```

```
Run assess-product-market-fit-health in full mode. Archetype: [PLG SaaS / marketplace /
enterprise / dev tool / ...]. Leading signals: [paste metrics + trends]. We're arguing
about whether growth is real.
```

```
Run align-stakeholders-on-decision. Decision: [one line]. Sales says "[quote]",
Engineering says "[quote]", Product says "[quote]". What's actually going on, and who
should decide by when?
```

## Workflows (end-to-end)

| Workflow | From → to |
|---|---|
| [Product Bet](workflows/product-bet.md) | Problem framing → discovery → prioritization → thesis → evidence audit → premortem → GO/NO-GO |
| [Experiment Decision](workflows/experiment-decision.md) | Framing → experiment design → causal review → evidence audit → SCALE/ITERATE/STOP |
| [Launch Gate](workflows/launch-gate.md) | Reversibility → evidence → premortem → AI contract (when applicable) → GO/PAUSE/NO-GO |
| [Product Health Review](workflows/product-health-review.md) | Health diagnosis → contradiction scan → corrective experiment/investment decision |

## Evaluation

The pack ships with a 12-scenario evaluation suite (`evals/scenarios/`), a rubric
(`evals/rubric.md`), and an honest report of what was verified and what remains
(`evals/EVALUATION_REPORT.md`). The portfolio audit and disposition history are in
[`quality/SKILL_PORTFOLIO_AUDIT.md`](quality/SKILL_PORTFOLIO_AUDIT.md).

## Type discipline

- **`assess`** — returns a scored verdict against explicit thresholds.
- **`assist`** — guides reasoning to a decision artifact.
- Every skill produces a **next action**, not just a description.

## License

CC BY 4.0, matching the Academy. Skills cite Academy doctrine by stable ID — they don't
reproduce third-party content. See `LICENSE` and `COPYRIGHT_AND_ACCESS_POLICY.md`.

## Source of truth

The authoritative skill sources live in the Academy monorepo at `skills/` (validated by
`scripts/validate_skills.py`). Installable ZIPs are built by `scripts/package_skills.py` and
attached to GitHub Releases on this repo.
