# Measurement Plan

Track only signals that exist. No fabricated numbers. This is the funnel:

```text
Search or social impression
→ repository/site visit
→ skill page or README engagement
→ installation/download
→ first successful use
→ return use
→ star
→ issue/contribution/share
```

## Signals and where to read them

| Signal | Source | Tool |
|---|---|---|
| GitHub unique visitors, referring sites | GitHub → Insights → Traffic | manual / `gh api` |
| Clones | GitHub → Insights → Traffic (Clone graph) | manual / `gh api` |
| Stars / forks / watchers | GitHub API | `scripts/snapshot_metrics.py` |
| Issues / discussions / external contributors | GitHub API | `scripts/snapshot_metrics.py` |
| Release downloads | GitHub API (release assets) | `scripts/snapshot_metrics.py` |
| skills.sh installations | skills.sh leaderboard page for the repo | manual (only once a page exists) |
| Site search impressions / clicks / indexed pages | Google Search Console | manual (after runbook) |
| Install-command success | clean-environment install tests | manual, recorded in `INSTALLATION_MATRIX.md` |
| Starter-pack downloads | Release asset counts | `scripts/snapshot_metrics.py` |
| Return use | cannot be measured without invasive analytics — intentionally not tracked | — |

## Automation

`python scripts/snapshot_metrics.py` writes a dated snapshot to
`docs/growth/metrics/snapshot-YYYY-MM-DD.json` using the public GitHub API
(`GITHUB_TOKEN` env var, read-only scope). Run it at each release and commit the snapshot so
history accrues. **No invasive analytics are added to the site or the CLI.**

## Milestones (conditions, not guarantees)

### Stage 1 — Proof of activation
- External users can discover and install successfully (install matrix green).
- First-use demos run end-to-end.
- Installation failures are collected and understood.
- First independent PM feedback exists (evaluation request).

### Stage 2 — Repeatable distribution
- One or more channels consistently generate qualified visitors.
- Installations and stars rise after releases.
- Users return or contribute (issues, discussions, PRs).
- External references/backlinks appear.

### Stage 3 — Compounding ecosystem position
- Directory visibility (skills.sh, agent-skill directories, awesome lists).
- Community contributions (skills, examples, fixes).
- Independent recommendations.
- Steady installation telemetry.
- Credible comparative evidence.

## Interpretation rules

- A star spike without installs or issues is a signal about the storefront, not the product.
- Installs without returns signal an activation failure; investigate demos and first-use.
- Search impressions without visits signal a title/description mismatch.
- No vanity targets: each milestone's acceptance is the condition listed, not a raw number.
