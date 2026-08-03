# Product Management Skills for AI Agents

**Evidence-backed product management skills for Claude Code, Codex, Cursor, OpenCode, and ChatGPT — frame problems, synthesize discovery, prioritize, design experiments, align stakeholders, and make defensible GO/NO-GO decisions.**

Every skill returns a **decision artifact** — a problem frame, a weighted discovery synthesis, a ranked backlog, an experiment charter, a stakeholder map, a GO/NO-GO verdict — with a next action, not a generic memo. Each skill runs in **fast mode** (reversible decisions) or **full mode** (one-way doors).

```
Reversible decision  → fast mode  → verdict + next action in minutes
Irreversible decision → full mode → evidence audit + premortem + thresholds
```

## Install

| I use… | Get this |
|---|---|
| **Any agent (native CLI)** | `npx skills add Lucumax/product-academy` — then pick skills (verified). One skill only: add `--skill <name>` |
| **Claude Code** | `/plugin marketplace add Lucumax/product-academy` → `/plugin install evidence-pack` |
| **Claude.ai / Desktop** | download [`product-academy-skills-all.zip`](https://github.com/Lucumax/product-academy/releases/latest) and upload it |
| **Codex** | unzip [`product-academy-skills-all.zip`](https://github.com/Lucumax/product-academy/releases/latest) into `.agents/skills/` |
| **Cursor** | unzip into `.cursor/skills/` |
| **OpenCode / other agents** | point your agent at `skills/` in this repo, or the ZIP |
| **Not sure** | start with the [8-skill starter pack](https://github.com/Lucumax/product-academy/releases/latest) + [START_HERE.md](START_HERE.md) |

Full install matrix with statuses: [`docs/installation/INSTALLATION_MATRIX.md`](docs/installation/INSTALLATION_MATRIX.md).
Install guides: [Claude Code](docs/installation/INSTALL-CLAUDE-CODE.md) · [Codex](docs/installation/INSTALL-CODEX.md) · [Cursor](docs/installation/INSTALL-CURSOR.md) · [Claude.ai/Desktop](docs/installation/INSTALL-CLAUDE-DESKTOP.md) · [ChatGPT](docs/installation/INSTALL-CHATGPT.md)

## Start with the job you have

- **"We should build X"** — [frame-product-problem](skills/frame-product-problem/SKILL.md) → a one-page problem frame (user problem, segment, business outcome, solution, assumptions)
- **Interviews done, notes unsorted** — [synthesize-customer-discovery](skills/synthesize-customer-discovery/SKILL.md) → weighted themes (repeated observation vs loud anecdote)
- **More opportunities than capacity** — [prioritize-product-opportunities](skills/prioritize-product-opportunities/SKILL.md) → a ranked backlog with exposed uncertainty
- **"We'll see if it works"** — [design-product-experiment](skills/design-product-experiment/SKILL.md) → an experiment charter with pre-committed stop rules
- **Sales / Product / Engineering stuck** — [align-stakeholders-on-decision](skills/align-stakeholders-on-decision/SKILL.md) → facts vs goals vs incentives vs risk vs decision rights
- **Is PMF healthy or decaying?** — [assess-product-market-fit-health](skills/assess-product-market-fit-health/SKILL.md) → archetype-adaptive health verdict
- **The actual call: fund, ship, or kill** — [make-go-no-go-call](skills/make-go-no-go-call/SKILL.md) → GO / NO-GO / PAUSE / SEEK-MORE-EVIDENCE / PROCEED-AT-RISK

All 14 skills + the [skill finder](skills/INDEX.md) and 4 end-to-end [workflows](skills/workflows/) are in `skills/`.

## One worked example

Scenario: *"We should build an AI triage assistant. Sales loves it."*

| Without the skill | With `pressure-test-product-thesis` + `check-ai-evaluation-contract` |
|---|---|
| Three meetings arguing about the feature | `BELIEF-PRESENTED-AS-THESIS` (no falsification condition, demo-only evidence) + `NO-CONTRACT` (no evaluation contract) |
| A roadmap commitment based on enthusiasm | **Next action:** write the falsification test and the evaluation contract before any build spend |

A verdict and a next action — not a memo.

## Try it yourself (three public demos)

Run these with your own agent — each shows the raw scenario, the ordinary response shape,
the skill invocation, the artifact, and the honest limitations:

1. [Customer-discovery synthesis](docs/growth/demos/01-discovery-synthesis.md) — interview enthusiasm vs usage behavior
2. [Product experiment design](docs/growth/demos/02-experiment-design.md) — pre-committed stop rules before results
3. [High-stakes GO/NO-GO decision](docs/growth/demos/03-go-no-go-decision.md) — launch pressure vs missing reliability evidence

## What makes these different

- **Internal evidence is first-class.** The shared [evidence taxonomy](skills/_shared/SKILL_CONTRACT.md) ranks a 90-day retention cohort for *your* product above a best-selling book for claims about your users. Published research never auto-outranks your own experiments, cohorts, analytics, interviews, support, and win/loss data.
- **Evidence ≠ assumption ≠ inference.** Every skill separates them, records "unknown" as an explicit assumption, and names the evidence that would change the verdict.
- **Fast and full modes.** Proportionate process: minimal ceremony for reversible calls, full evidence audit + premortem for one-way doors.
- **Real decision artifacts.** Outputs follow a JSON-shaped contract with verdict, confidence, assumptions, what-would-change-it, and a next action.

## What's inside

- **14 active skills** (9 hardened from the original pack + 5 new high-frequency skills in
  the latest release; the former `run-source-tier-check` was merged into the evidence audit)
  covering high-frequency PM work *and* evidence/judgment: problem framing, discovery
  synthesis, prioritization, experiment design, stakeholder alignment, PMF health, evidence
  audit, causal review, GO/NO-GO, reversibility classification, premortem, thesis
  pressure-test, AI evaluation contract.
- **4 workflows:** [Product Bet](skills/workflows/product-bet.md), [Experiment Decision](skills/workflows/experiment-decision.md), [Launch Gate](skills/workflows/launch-gate.md), [Product Health Review](skills/workflows/product-health-review.md).
- **Shared contract** `skills/_shared/SKILL_CONTRACT.md` — the evidence taxonomy + output schema every skill uses.
- **Independent validation** — 12 eval scenarios, a rubric, an adversarial review, and a portfolio audit in `skills/evals/` and `skills/quality/`. Read the [evaluation report](skills/evals/EVALUATION_REPORT.md); it reports weaknesses, not just wins.

## The Academy behind it

This is the execution layer of the **Product Leadership Academy** — an evidence-backed product leadership curriculum (Senior PM → CPO) with doctrine, cases, contradictions, a 184-source evidence registry, an interactive simulator, and role-based learning paths. The skills turn the Academy's evidence and judgment layer into decisions you can run with an agent today. The curriculum remains in this monorepo (see the [structure table](#repository-structure) below) and in the [web app](https://lucumax.github.io/product-academy/).

## Start here

→ **[START_HERE.md](START_HERE.md)** — 60-second onboarding, copy-paste prompts for seven PM jobs, and the fast/full rule.

---

## Repository structure

| Area | Purpose |
|------|---------|
| `skills/` | The agent-skill pack (14 skills + workflows + shared contract) |
| `00_orientation/` … `13_career_transitions/` | Academy curriculum |
| `sources/`, `evidence/` | Evidence registry and processed evidence |
| `webapp/` | The Astro web app (guided journey, simulator, search) |
| `docs/growth/` | Discoverability audit, positioning, launch and measurement plans |

## Quick Start (web app)

```bash
cd webapp
npm install
npm run build      # imports content + builds static site + indexes search
npm run preview    # serve locally, or deploy dist/ anywhere static
```

## Validation

```bash
python scripts/validate_academy.py   # quality-gate checks (660+, count grows with content)
python scripts/validate_skills.py    # skill-pack contract checks
python -m pytest -q                  # 95 tests
```

## Contributing

Found a gap? A broken install? A framework worth formalizing? See [CONTRIBUTING.md](CONTRIBUTING.md) and the [issue templates](.github/ISSUE_TEMPLATE/). We want contributors and advocates, not spectators.

## License

Original content is [CC BY 4.0](LICENSE). Skills cite Academy doctrine by stable ID and never reproduce third-party content. See [COPYRIGHT_AND_ACCESS_POLICY.md](COPYRIGHT_AND_ACCESS_POLICY.md).

## Scope

See [SCOPE.md](SCOPE.md) for what the Academy is and is not.
