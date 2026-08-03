# Channel 4 — One AI-Agent Community

Status: **DRAFT — DO NOT POST.** Focuses on skill design and agent reliability, not PM
education. Leads with the experiment-design demonstration: precommitted interpretation,
guardrails, stop conditions, rollback trigger.

## Community type

One AI-agent community: Claude Code, Codex, Cursor, or OpenCode users — the people who will
actually install and run agent skills. The post is about how to design skills that make
agents *reliable* on a consequential task, using product-experiment design as the worked
example.

## Post draft

> The difference between "we'll see if it works" and a spec that can't be gamed.
>
> A skill for AI agents that design product experiments has to do one hard thing: make the
> agent commit to the interpretation BEFORE results exist. Otherwise the agent — like a
> human team — will rationalize whatever happened.
>
> Here's the shape (from an open-source PM skill pack I maintain):
>
> ```
> assumption: removing the checkout confirmation raises completed orders
>   without raising returns or support
> primary_metric: completed-orders rate, up, baseline 3.1%
> interpretation_rule:
>   win  = +0.3pp AND returns <= +0.1pp AND support <= +5%
>   null = within +-0.3pp
>   harm = returns or support breach the thresholds
> stop_rules:
>   early stop = 2 weeks if harm threshold breached
>   minimum    = 6 weeks or 20k sessions before calling null
> rollback: feature flag, trigger = harm threshold, authority = PM on call
> competing_hypotheses: tool latency, seasonal checkout shift
> ```
>
> Three design choices worth stealing for any agent skill:
>
> 1. **Guardrails as thresholds, not vibes.** "Don't hurt users" becomes "returns and support
>    may not breach these numbers." An agent can enforce a number; it can't enforce a vibe.
> 2. **Stop rules are part of the spec.** Early-stop, minimum window, null call — written
>    before the run. The readout is then a decision, not a negotiation.
> 3. **Rollback is first-class.** Named mechanism, trigger signal, authority. If the harm
>    threshold fires, the spec says who flips the flag and on what signal.
>
> What I'm less sure about, and want your critical take on:
> - What's the failure mode when an agent *writes* these rules about its own work?
> - How do you stop an agent from post-hoc rewriting "win" after the results arrive?
> - For agent skills generally: is pre-committing thresholds in the skill text enough, or do
>   you need the harness to enforce it?
>
> The pack is at [link to /skills/]. Install: `npx skills add Lucumax/product-academy`.
> I'm here for the reliability discussion, not the install count.
