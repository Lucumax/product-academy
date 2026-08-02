# Skills — Product Academy Evidence Pack

This folder is the **source of truth** for the Product Academy's agent-skill pack. Installable
ZIPs are built from here by `scripts/package_skills.py` and attached to GitHub Releases on the
Academy repo.

## What these skills are

Each skill turns one product-management job into an executable decision for an AI agent. The
contract is strict: a skill must return a **verdict or decision artifact** with a **confidence
label**, **stated assumptions**, **what-would-change-it**, and a **next action** — never just
a memo.

Two modes per skill:

- **Fast mode** — for reversible, ordinary decisions: minimal questions, provisional verdict,
  explicit uncertainty, clear next action, no research ceremony.
- **Full mode** — for Type-1 and high-stakes decisions: source verification, internal evidence
  analysis, contradiction review, causal-confidence assessment, premortem, reproducible verdict.

## Which skill should I use?

Use the **skill finder** in [`INDEX.md`](INDEX.md) (organized by PM job) or the full
[`PORTFOLIO_MAP.md`](PORTFOLIO_MAP.md) (job → trigger → skill → artifact → workflow → maturity).
If the situation is a multi-step bet, launch, experiment, or health review, start at the
matching workflow in [`workflows/`](workflows/).

## What does a good request look like?

A good request states the decision, the situation, and what evidence exists — and lets the
skill ask the rest. Bad: "help me with my product." Good: *"Run the make-go-no-go-call skill —
we want to fund the AI triage assistant this quarter; strategy excludes customer-facing AI
without an evaluation contract; evidence is one pilot; it's one-way-door."* Copy-paste
templates are in [`INDEX.md`](INDEX.md).

## What output will you receive?

A JSON-shaped verdict artifact per the shared output envelope in
[`_shared/SKILL_CONTRACT.md`](_shared/SKILL_CONTRACT.md): verdict, confidence, evidence basis
(15-type taxonomy), assumptions, what-would-change-it, next action, reversal conditions. Every
skill ends with a concrete next action an owner can take.

## Before / after example

**Before** (no skill): "We should build an AI triage assistant. Sales loves it." → the team
argues for three meetings.

**After** (`pressure-test-product-thesis` then `check-ai-evaluation-contract`): the thesis is
typed `BELIEF-PRESENTED-AS-THESIS` (no falsification condition, demo-only evidence); the
evaluation contract is `NO-CONTRACT`. The next action: write the falsification test and the
contract before build spend. The argument becomes a decision.

## Directory layout

```
skills/
  INDEX.md                  landing + skill finder + copy-paste invocations
  PORTFOLIO_MAP.md          job → skill → workflow map
  _shared/SKILL_CONTRACT.md shared evidence taxonomy + output schema + fast/full contract
  workflows/                end-to-end composable workflows (product-bet, launch-gate, …)
  evals/                    evaluation scenarios, rubric, honest report
  quality/                  portfolio audit and disposition history
  <skill-name>/SKILL.md     the executable skill contract
  <skill-name>/references/  doctrine map with stable Academy IDs
```

## Authoring or editing a skill

1. Copy an existing production skill's structure (or `_template/SKILL.template.md`) into
   `skills/<kebab-name>/SKILL.md`.
2. Fill the frontmatter (name, description, type, version, best_for, doctrine, license) and
   the required sections (see `_shared/SKILL_CONTRACT.md` §1).
3. Every skill must have Fast mode and Full mode, an Output schema, a Verdict Contract with a
   Next action, Reversal conditions, and Composition hooks.
4. Add `references/doctrine-map.md` listing exact Academy IDs.
5. Run `python scripts/validate_skills.py` — it must pass.

**Type discipline:** `assess` returns a scored verdict against thresholds; `assist` guides
reasoning to a decision artifact. `run-source-tier-check` is deprecated — its job is the
source-credibility sub-mode of `audit-decision-evidence`.

## Validating

```bash
python scripts/validate_skills.py
```

This runs in CI on every push. It checks: frontmatter parses, required fields + sections
exist, `type` is valid, fast/full modes present, output schema present, the Verdict Contract
has all sub-parts, every doctrine reference resolves, skill identifiers are unique, internal
links and workflow references resolve, deprecated skills route to a `replaced_by`, and the
portfolio map / plugin manifest stay consistent with the skill set.

## How skills cite doctrine

- Principles: `PRN-0001` … `PRN-0016`
- Contradictions: `CON-0001` … `CON-0013`
- Cases: `CASE-0001` … `CASE-0019` (with `causal_confidence` ratings)
- Sources: `SRC-*` (in `sources/registry.yaml`, tiers A–E)
- Tools: `09_tools/<TEMPLATE>.md`

Skills **cite** these by stable ID and never reproduce third-party content. The Academy is the
evidence and judgment layer; the skills are the execution layer — a skill must be usable
without reading the Academy.

## Publishing

The pack is released from this source to the Academy repo's GitHub Releases: ZIP bundles
(starter / all), per-platform install docs (`INSTALL.md`), and the `.claude-plugin` marketplace
manifest.
