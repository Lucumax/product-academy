# Channel 1 — LinkedIn Launch Assets

Status: **DRAFT — DO NOT POST.** Review with Walter before any posting. Lead with the
discovery-contradiction demonstration; invite critical use, not stars.

Primary link targets: `https://lucumax.github.io/product-academy/skills/` and the demo
write-up (which becomes live at `/doc/docs/growth-demos-01-discovery-synthesis/` after merge).

---

## Primary post

> Your AI agent can summarize 25 interviews. Can it tell you when the interviews are lying?
>
> A consumer fitness app interviewed 25 active users about a "habit streaks" feature. 22 of
> 25 said they love it. Usage data: 6% of daily users ever touch the feature. Sessions flat.
>
> Ask a generic AI to summarize the interviews and — in my tests — it says: "users love
> streaks — invest." It listens to the loudest voices, which are usually your most engaged —
> already-converted — users. (Illustrative shape; the demo notes its limits honestly.)
>
> The pattern is everywhere: stated enthusiasm ≠ observed behavior. Interviews tell you what
> people *think* they want; usage tells you what they *do*. When they conflict, a claim about
> why people come back needs behavior to back it.
>
> I'm hardening a small, evidence-aware skill pack for PMs. The discovery skill returns
> BEHAVIOR-CONTRADICTS with a bounded test — compare retention for streak-users vs
> non-streak-users — instead of funding a feature on enthusiasm.
>
> Full demo (fictional data, honest limits included):
> [link to demo 1 / skills page]
>
> Install (verified): `npx skills add Lucumax/product-academy`
>
> I'm not asking for a star. I'm asking for the failure modes: where does stated intent win
> over behavior, and what do I have wrong? If you run it and it produces garbage, I want that
> too.

## Shorter alternate

> 22 of 25 users raved about a feature. Usage: 6% of daily users use it.
>
> A generic AI says "invest in streaks." It heard the loudest voices — the top decile already
> using the product.
>
> The skill returns BEHAVIOR-CONTRADICTS and a cohort test: do streaks cause retention, or
> just accompany the already-engaged?
>
> I built an evidence-aware PM skill pack. Demo (fictional data):
> [link] · Install: `npx skills add Lucumax/product-academy`
>
> No star-ask. Tell me where it's wrong.

## Technical follow-up

> Why fast mode and full mode?
>
> Product decisions aren't all equally risky. Moving a button is a two-way door; changing
> billing contracts is a one-way door.
>
> The skill pack scales the process to the risk: reversible calls get a few questions and a
> provisional verdict in minutes; irreversible calls get an evidence audit, a premortem, and
> explicit decision thresholds before anyone commits.
>
> Same discipline, proportionate ceremony. That's the design principle behind the pack —
> and the reason "run everything through every framework" is the failure mode we're trying to
> avoid. [Link to /skills/]

## First-comment text (on the primary post)

> Context: these are 14 open-source skills built on a shared evidence taxonomy — your own
> experiments, cohorts, and analytics outrank a best-selling book for claims about your users.
> The scenario above is fictional fixture data. The skill can't run the cohort split itself —
> it names the test and hands it to an owner. Full limitations are in the demo.

## Suggested image

`docs/growth/assets/demo-1-discovery-contradiction.png` (1280×640) — the "Interviews say
build it. Usage says 6% use it." visual. Matches the site's social-preview style.

---

## Response templates

### Genuine question

> Good question. [Answer; if about the evidence rule:] the taxonomy treats stated intent (E5)
> and behavior (E3/E4) as different evidence types, and for a "do" claim behavior carries more
> weight. Here's the full contract: [link to skills/_shared/SKILL_CONTRACT.md]. Happy to
> clarify.

### Skeptical criticism

> Fair. [If it's about the demo being fictional:] the scenario is fictional fixture data and
> the demo says so — it shows the shape of the artifact, not a real win. [If it's a specific
> flaw:] that's exactly the kind of failure I'm collecting. I'll record it and fix it. This
> is a tool to pressure-test, not a magic answer.

### Installation problem

> Thank you — installation failures are the most useful feedback there is. Can you paste the
> exact command you ran, your agent and version, and the error? I'll reproduce it and add it
> to the install matrix.

### Competing resource recommendation

> Thanks — I'll look at it. If it does this better with less friction, that's the signal the
> eval is for, and I'd rather know than not.
