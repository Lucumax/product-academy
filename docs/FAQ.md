# FAQ

## What is this?

A pack of 14 product-management **skills for AI agents**. Each skill is a `SKILL.md` that
tells your agent how to produce a decision artifact (problem frame, weighted discovery
synthesis, ranked backlog, experiment charter, stakeholder map, GO/NO-GO verdict) with a next
action.

## How is this different from a set of prompts or templates?

The skills are **evidence-aware**. They use a shared evidence taxonomy in which your own
product evidence (experiments, cohorts, analytics, interviews, support, win/loss) is
first-class â€” a 90-day retention cohort for your product beats a best-selling book for claims
about your users. Every skill separates evidence from assumption from inference, records
"I don't know" as an explicit assumption, and names what would change the verdict.

## Do I need the Academy curriculum to use the skills?

No. The skills cite Academy doctrine by stable ID, but each skill is self-contained: it has a
Purpose, Use when / Do not use when, Inputs, Missing-data behavior, Fast mode, Full mode,
Method, Evidence classification, Output schema, and a worked example. The Academy is the
evidence and learning layer behind the skills, not a prerequisite.

## What is fast mode vs full mode?

- **Fast mode** â€” for reversible, ordinary decisions: a few questions, a provisional verdict,
  explicit uncertainty, a next action. No research ceremony.
- **Full mode** â€” for one-way doors and high-stakes calls: evidence audit, contradiction
  review, causal-confidence assessment, and a premortem where required.

Rule of thumb: reversible â†’ fast; irreversible â†’ full.

## Which skill should I start with?

Match your situation in the [finder](../skills/INDEX.md) or [START_HERE.md](../START_HERE.md).
Common entries: "we should build X" â†’ `frame-product-problem`; "interviews done, notes
unsorted" â†’ `synthesize-customer-discovery`; "more work than capacity" â†’
`prioritize-product-opportunities`; "the actual call" â†’ `make-go-no-go-call`.

## Is it free? What is the license?

The repository and skills are [CC BY 4.0](../LICENSE).

## Does it work with my agent?

Skills are plain structured Markdown with no `$ARGUMENTS` templating, so they work with
Claude Code, Claude.ai/Desktop, Codex, Cursor, OpenCode, ChatGPT, and any agent that reads
structured knowledge. See the [installation guides](installation/).

## How do I contribute a skill?

See [CONTRIBUTING.md](../CONTRIBUTING.md) and the issue templates. The bar is evidence-aware
decision artifacts, not generic templates â€” skills must teach the *why* and expose
assumptions.

## Is this claimed to be a 9/10? Are there benchmarks?

No. The [evaluation report](../skills/evals/EVALUATION_REPORT.md) reports what was verified
(self-consistency, structure, packaging) and what is not yet verified (independent behavioral
evaluation). No adoption, star, install, or benchmark number is claimed anywhere in this
repository.

## How do I report a problem?

Open an issue using the [bug template](../.github/ISSUE_TEMPLATE/bug_report.yml) or a discussion.
