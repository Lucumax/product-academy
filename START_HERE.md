# START HERE — 60-second onboarding

You are a product manager with an AI agent (Claude Code, Codex, Cursor, OpenCode, ChatGPT).
These skills make your agent produce **decision artifacts instead of generic memos** — with
evidence, assumptions, and a next action. Here is how to start using them in one minute.

## The one rule

> **Reversible decision → fast mode. Irreversible decision → full mode.**

Every skill runs both ways. If a decision can be undone cheaply, the fast mode asks a few
questions and gives a provisional verdict. If it is a one-way door, full mode adds the
evidence audit, contradiction review, and premortem.

## In the next 60 seconds

1. **Install** (pick your platform in the [README](README.md#install)) or just open `skills/` in this repo.
2. **Pick your job** from the prompts below.
3. **Copy-paste** the prompt into your agent.
4. Answer its questions — it records "I don't know" as an explicit assumption rather than padding.
5. You get a verdict or artifact with a **next action**.

## Copy-paste prompts (one per job)

Replace the bracketed text. These are starter shapes — the skill will ask the rest.

**Frame a product problem**
```
Run the frame-product-problem skill. Input: "We should build [X] for [customers]."
We have no problem statement yet. Return the problem frame and the next action.
```

**Synthesize customer interviews**
```
Run the synthesize-customer-discovery skill. Input: our interview notes are here:
[notes or file]. Five of five people said [X], but usage data shows [Y]. Return a
weighted synthesis table and what to trust.
```

**Prioritize opportunities**
```
Run the prioritize-product-opportunities skill. Backlog: [list]. Capacity: [X] per
quarter. Strategy: [paste or say none]. A big customer asked for [Z]. Rank the
backlog with uncertainty exposed.
```

**Design an experiment**
```
Run the design-product-experiment skill. Change: [X]. Assumption it tests: [A].
Primary metric we expect to move: [M], baseline [B]. Return an experiment charter
with pre-committed interpretation and stop rules.
```

**Align stakeholders**
```
Run the align-stakeholders-on-decision skill. Decision: [one line]. Sales says
"[quote]", Engineering says "[quote]", Product says "[quote]". What is actually
going on, and who should decide by when?
```

**Make a GO/NO-GO call**
```
Run the make-go-no-go-call skill. Input: we want to [fund/ship X]. Strategy:
[paste or say none]. Evidence: [claims + what backs them]. Effort: [X]. This is
[reversible / not]. Use full mode if it is one-way-door.
```

**Evaluate an AI feature**
```
Run the check-ai-evaluation-contract skill. Input: we are about to launch [AI
feature]. We have [a demo / a written contract / nothing]. Stage: [pre-build /
at launch]. Return the contract verdict and the gaps to fill.
```

## What you get back

Every skill returns an artifact in the same shape: **verdict** (or artifact), **confidence**,
**evidence basis** (which evidence types were used), **assumptions** (everything answered
"unknown"), **what would change the verdict**, and a **next action** with an owner. The full
contract is in [`skills/_shared/SKILL_CONTRACT.md`](skills/_shared/SKILL_CONTRACT.md).

## Want more depth?

- **Skill finder by PM job:** [`skills/INDEX.md`](skills/INDEX.md)
- **Job → skill → workflow map:** [`skills/PORTFOLIO_MAP.md`](skills/PORTFOLIO_MAP.md)
- **End-to-end workflows:** [`skills/workflows/`](skills/workflows/)
- **What's honestly known and not:** [`skills/evals/EVALUATION_REPORT.md`](skills/evals/EVALUATION_REPORT.md)

## Not technical?

Use ChatGPT or Claude.ai: download the [all-skill ZIP](https://github.com/Lucumax/product-academy/releases/latest), upload it where your assistant accepts project knowledge, and paste the prompts above. You do not need a terminal.
