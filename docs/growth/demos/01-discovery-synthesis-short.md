# Demo 1 — Interviews vs Usage (README-short version)

When interviews say users want a feature but usage data disagrees, which evidence should win?

**The setup (fictional):** a fitness app interviewed 25 active users about a "habit streaks"
feature. 22 were positive; 5 showcase users raved. Usage data: streaks used by **6% of DAU**,
weekly sessions flat at **3.1**.

**The trap:** generic AI output sums up the interviews and says "users love streaks — invest."
It listens to the loudest voices (the already-engaged top decile) and never compares stated
enthusiasm against observed behavior.

**What the skill returns** (`synthesize-customer-discovery`):

```
Verdict: BEHAVIOR-CONTRADICTS
- "streaks keep me coming back" — repeated observation (22/25) BUT interview-only (E5),
  and the loudest voices are the already-engaged top decile (segment skew)
- "weekly engagement flat at 3.1" — behavioral observation (E3), population-wide
Next action: streak-user vs non-streak-user retention cohort split — does streaks
  CAUSE retention or merely ATTEND it?
```

**Why:** for a claim about why people return, behavior (E3/E4) outranks stated intent (E5).
The skill refuses to fund a feature on interview enthusiasm alone, names the selection bias,
and hands back a bounded test that discriminates cause from accompaniment.

**Try it:**

```bash
npx skills add Lucumax/product-academy --skill synthesize-customer-discovery
```

Full write-up: [`01-discovery-synthesis.md`](01-discovery-synthesis.md) — scenario, raw
input, baseline prompt and output, skill invocation, artifact, differences, limitations, and
links.

**Honest limits:** the skill can't run the cohort split; with interviews only it returns
`THIN-DISCOVERY`, not `BEHAVIOR-CONTRADICTS`. This demonstrates the artifact the skill is
designed to produce — it does not prove the skill beats a well-crafted bespoke prompt (that
is what the blinded external evaluation is for).
