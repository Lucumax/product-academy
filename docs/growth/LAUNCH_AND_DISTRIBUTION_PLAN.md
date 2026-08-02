# Launch & Distribution Plan

Prepared 2026-08-02. **Nothing here is posted.** Every draft must be reviewed by Walter before
external use, and every post must lead with a demonstration or a learning — never "please star
my repo." No adoption, star, install, or endorsement number may be claimed that has not
actually occurred.

## Target user segments

1. Working PMs (Senior → Principal → Group) who already use AI agents and want decision-grade
   output, not generic memos.
2. Product leaders / Directors / VPs who make high-stakes calls (GO/NO-GO, PMF, launch) and
   want the evidence and premortem discipline.
3. Founders doing product work with an agent (fast, cheap, self-contained install).
4. AI product managers (the `check-ai-evaluation-contract` skill is rare in competing packs).

## Relevant communities and channels

| Channel | Why | Value proposition per channel |
|---|---|---|
| GitHub (repo + releases + discussions) | Primary distribution node | Skills-first storefront, native `npx skills add`, verified installs |
| Product management communities (e.g. PM forums, Slack/Discord groups, Lenny's community) | Audience is the exact target | A skill that turns interviews into a weighted readout, not a framework dump |
| AI-agent communities (Claude Code, Codex, Cursor, OpenCode) | Distribution via agents | A native-install skill pack with verified `npx skills add` |
| Newsletter / blog (LinkedIn, Substack) | Long-form trust | The evidence-aware differentiator + the three demos |
| Agent-skill directories & awesome lists | Permanent listing | Linkable, installable, license-clear |
| PM educators / university programs | Credibility + distribution | Evidence layer is teachable material |

## Launch sequencing

1. **Pre-launch (this sprint):** merge `skills-discoverability-growth-v1`; deploy `/skills/`;
   apply About/topics/social preview; publish `skills-v0.3.0`.
2. **Verify:** run the Search Console runbook; confirm installs from a clean environment.
3. **Week 1 — GitHub-first:** release announcement; repository discussions seeded with the
   three demos; invite 3–5 PM reviewers to run the demos and report honestly.
4. **Week 2 — Community:** one product-management community post + one AI-agent community
   post (each leading with Demo 1 or Demo 2); direct outreach to ~20 practitioners.
5. **Week 3 — External:** LinkedIn launch post + technical follow-up; Product Hunt (only if
   the timing and description are judged appropriate); Show HN only if it adds a real
   demonstration.
6. **Ongoing:** release cadence + newsletter loop + contribution invites.

## Reusable drafts

### GitHub release announcement (v0.3.0)

> **Product Management Skills for AI Agents — v0.3.0**
>
> This release is the discoverability pass on the skill pack. What's new:
> - A `/skills/` section on the site — find a skill by PM job, read every skill's full
>   contract, and install in one command.
> - Verified native install: `npx skills add Lucumax/product-academy`.
> - Three public demonstrations (discovery synthesis, experiment design, GO/NO-GO) — run them
>   yourself.
> - Fix: the skill template and deprecated stub are no longer listed as installable by the
>   skills CLI.
>
> Install: `npx skills add Lucumax/product-academy`, or download the ZIP.
> Honest status: 14 skills, structurally validated, independently reviewed
> (ACCEPT_WITH_BOUNDED_FIXES), self-run evals — comparative evaluation is the open gap.

### LinkedIn launch post (draft)

> Your AI agent can write a memo. Can it make a decision?
>
> I hardened a small, evidence-aware skill pack for product managers: 14 skills that turn
> messy PM situations into decision artifacts. One example — 25 interviews all saying "users
> love streaks", while usage data says 6% of DAU touch the feature. The discovery-synthesis
> skill returns BEHAVIOR-CONTRADICTS and a cohort test to run — instead of "invest in
> streaks."
>
> Install: `npx skills add Lucumax/product-academy` (verified) or read the demo:
> [link to /skills/]
>
> What it is not: not "best/ultimate", no benchmarks, no fabricated numbers. What it is: an
> evidence taxonomy in which your own cohort data outranks a best-selling book.

### LinkedIn technical follow-up (draft)

> The design principle behind the skill pack: fast mode for reversible decisions, full mode
> for one-way doors. Reversible → a few questions and a provisional verdict. Irreversible →
> evidence audit, premortem, decision thresholds. The same discipline, scaled to the risk.

### Product Hunt submission (draft — submit only if appropriate)

> **Product Management Skills for AI Agents** — evidence-backed decisions for Claude, Codex,
> Cursor, and OpenCode. Frame problems, synthesize discovery, prioritize, design experiments,
> and make GO/NO-GO calls. Native install; decision artifacts, not memos.

### Hacker News "Show HN" (draft — only if it adds a demonstration)

> Show HN: I turned a product-leadership curriculum's evidence layer into installable AI
> skills. Fast/full modes, internal-evidence-first taxonomy, 12 honest eval scenarios, an
> independent review that said accept-with-fixes. Demos: [link]. The interesting claim is not
> that it's better — it's that a skill can carry an evidence discipline a plain prompt drops.

### Product-management community post (draft)

> Lead with Demo 1 (interview enthusiasm vs usage behavior). Ask the community: how do you
> decide whether interview enthusiasm is real demand? Offer the synthesis skill as one answer,
> and invite honest feedback — especially where it fails.

### AI-agent community post (draft)

> Lead with Demo 2 (experiment design with pre-committed stop rules). Show the difference
> between "we'll see if it works" and a spec with a harm guardrail and rollback trigger.

### Direct outreach (draft — to ~20 practitioners/maintainers, one-to-one)

> I maintain an evidence-aware PM skill pack ([link]). Your [work/audience] on [topic] is
> exactly who I'd like to pressure-test it — I'm looking for honest feedback on the discovery
> synthesis and GO/NO-GO skills, and for a fair comparison against your own prompts. No ask
> for a star; I'd genuinely value a critical read.

### Independent PM evaluation request (draft)

> I'm recruiting 5–10 experienced PMs to run three skill demos and score them against a plain
> prompt on decision usefulness, ceremony, and confidence calibration. Blinded, honest, and
> the results will be published even if unfavorable. [Link]

### Contributor invitation (draft)

> The fastest high-value contribution is a better worked example or a failure mode we missed.
> Guidelines and the skill bar are in CONTRIBUTING.md.

## Contributor and sharing loop

- Every released skill links back to the repo and `CONTRIBUTING.md`.
- Honest changelog on every release (people share real change).
- A `#thanks` channel pattern via GitHub discussions for users who report a useful failure.
- Issues triaged for "good first issue" candidates (weak worked examples, docs).

## Founder/maintainer voice

Direct, evidence-first, and honest about limits. No hype, no "9/10", no fabricated traction.
The voice is: "we built a decision tool and here is exactly what it does, how to run it, and
where it still needs to prove itself."

## Measurable conversion funnel

```
Search or social impression
→ repository/site visit
→ skill page or README engagement
→ installation/download
→ first successful use
→ return use
→ star
→ issue/contribution/share
```

Metrics per stage are tracked in `MEASUREMENT_PLAN.md`.

## Partnership candidates (no claim any will promote us)

- PM educators and course authors (evidence layer as curriculum material).
- PM newsletters (Demos 1–3 as content).
- Product and AI-agent community organizers.
- Maintainers of relevant awesome lists and agent-skill directories.
- University / professional-education programs running PM or AI-PM courses.
