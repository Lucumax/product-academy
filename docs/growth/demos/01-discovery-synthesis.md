# Demonstration 1 — When Interviews Say "Build It" But Usage Says Nobody Uses It

**One-paragraph version:** A fitness app interviewed 25 active users about a "habit streaks"
feature. Most said they love it; usage data shows 6% of daily users ever touch it. The plain
prompt answer is "users love streaks — invest." The `synthesize-customer-discovery` skill
returns a different verdict: `BEHAVIOR-CONTRADICTS`, with a bounded test that separates users
who *say* streaks matter from users whose behavior *proves* it.

**Install:** `npx skills add Lucumax/product-academy`

---

## 1. Scenario

A consumer fitness app ("Stride") is deciding whether to double down on a "habit streaks"
feature. Interviews are enthusiastic; usage is not. The team is split: growth says "listen to
your users," the analyst says "nobody uses it."

## 2. Raw input

- 25 interviews with active users.
- 22 mention streaks positively; the 5 most engaged "showcase" users rave about it.
- Behavioral data: streaks used by **6% of DAU**; median weekly sessions flat at **3.1**.
- No cohort split of streak-users vs non-streak-users on retention.
- No population-scale survey of stated intent.

All of this is fictional fixture data (see `skills/evals/external/scenarios/X04-interview-vs-usage.md`).

## 3. Baseline prompt (no skill)

> "Summarize these 25 interviews about the habit streaks feature and recommend whether to
> invest."

## 4. Baseline output (shape)

A bullet list of what users said about streaks, weighted toward the loudest quotes, concluding
"users love streaks — invest in it." No weighting by repetition across sources, no comparison
of stated enthusiasm against usage behavior, no acknowledgement that the loudest voices are
the already-engaged top decile.

## 5. Skill invocation (copy-paste)

> Run the `synthesize-customer-discovery` skill. Input: 25 interviews — 22 mention "streaks
> keep me coming back", 5 showcase users rave. Usage data: streaks used by 6% of DAU, weekly
> sessions flat at 3.1. Return the weighted synthesis and what to trust.

## 6. Skill-enabled output (the artifact)

```
Verdict: BEHAVIOR-CONTRADICTS
Themes:
  - "streaks keep me coming back" — REPEATED observation (22/25) BUT interview-only (E5),
    and the loudest voices are the already-engaged top decile (segment skew)
  - "weekly engagement is flat at 3.1 sessions" — behavioral observation (E3), population-wide
Stated-vs-actual: enthusiasm (22/25) vs 6% DAU feature usage — discrepancy flagged
Evidence rule applied: for "what people do" claims, behavior (E3/E4) outranks stated intent (E5)
Next action: streak-user vs non-streak-user retention cohort split (E4) — does streaks
  CAUSE retention or merely ATTEND it?
Confidence: medium (behavior cross-check exists; cohort split does not yet)
What would change the verdict: a segment split showing streaks drive retention in one cohort
```

## 7. Material differences

| | Baseline (prompt) | Skill-enabled |
|---|---|---|
| Verdict | "Invest in streaks" | `BEHAVIOR-CONTRADICTS` |
| Evidence weighting | Loudest quotes win | Repeated-vs-anecdote rule by independent source |
| Stated vs actual | Not compared | Compared explicitly (E5 vs E3) |
| Selection bias | Invisible | Named (showcase users = top decile) |
| Next action | "Invest" | A bounded cohort test that discriminates cause from accompaniment |
| Refuses to over-fund | No | Yes — refuses to fund on interview enthusiasm alone |

## 8. Limitations

- The skill cannot run the cohort split itself; it names the test and hands it to an owner.
- Given only interviews (no behavioral data), the verdict would be `THIN-DISCOVERY`, not
  `BEHAVIOR-CONTRADICTS` — the behavior data is load-bearing.
- This demonstrates the decision artifact the skill is designed to produce. It does **not**
  prove the skill beats a well-crafted bespoke prompt — that is what the blinded external
  evaluation (`skills/evals/external/`) exists to test. Do not quote this as a comparison.

## 9. Copy-paste command or prompt

Install once:

```bash
npx skills add Lucumax/product-academy --skill synthesize-customer-discovery
```

Then paste the skill invocation (section 5) into your agent with your own interview notes and
usage data.

## 10. Relevant skill and workflow links

- Skill: [`synthesize-customer-discovery`](https://lucumax.github.io/product-academy/skills/synthesize-customer-discovery/)
- Related: [`conduct-causal-confidence-review`](https://lucumax.github.io/product-academy/skills/conduct-causal-confidence-review/) — grades whether streaks caused retention after the cohort test
- Related: [`design-product-experiment`](https://lucumax.github.io/product-academy/skills/design-product-experiment/) — turns the cohort test into a pre-committed experiment
- Workflow: [`product-bet`](https://lucumax.github.io/product-academy/skills/workflows/product-bet/) — where the synthesis feeds the bet decision
- Evidence taxonomy: [`_shared/SKILL_CONTRACT.md`](https://github.com/Lucumax/product-academy/blob/main/skills/_shared/SKILL_CONTRACT.md)
- Fictional fixture: [`X04-interview-vs-usage.md`](https://github.com/Lucumax/product-academy/blob/main/skills/evals/external/scenarios/X04-interview-vs-usage.md)
