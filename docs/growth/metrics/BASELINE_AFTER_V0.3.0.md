# Metrics Baseline After v0.3.0

- **Measurement date:** 2026-08-02
- **Repository state:** public, default branch `main`, live commit `9c84756`
  (`skills-launch-validation-v1` is the working branch; the snapshot reflects remote `main`)
- **Snapshot file:** `docs/growth/metrics/snapshot-2026-08-02.json`
- **Snapshot command:** `GITHUB_TOKEN=... python scripts/snapshot_metrics.py`
- **Author:** this snapshot was taken by the maintainer with a read-only token against the
  public API. It is the baseline this sprint's launch will be measured against.

## Current public metrics

| Metric | Value | Source |
|---|---|---|
| Stars | 0 | GitHub API `stargazers_count` |
| Forks | 0 | GitHub API `forks_count` |
| Watchers (subscribers) | 0 | GitHub API `subscribers_count` |
| Open issues | 0 | GitHub API (issues, open) |
| Open PRs | 0 | GitHub API (pulls, open) |
| Discussions enabled | No | GitHub API `has_discussions` (feature disabled — not "0 discussions") |
| Open discussions | N/A | GraphQL returns 0 for a disabled feature; not a real metric |
| External contributors (non-owner) | 0 | GitHub API (contributors) |
| Release downloads (v0.3.0, all-zip) | 3 | GitHub API (release asset download_count) |
| Release downloads (v0.3.0, core-zip) | 2 | GitHub API |
| Release downloads (v0.2.0, all-zip) | 2 | GitHub API |
| Release downloads (v0.2.0, core-zip) | 1 | GitHub API |
| Release downloads (v0.1.0, all-zip) | 0 | GitHub API |
| Release downloads (v0.1.0, core-zip) | 0 | GitHub API |

> Download counts are volatile: they move every time anyone (including the maintainer's own
> tests) downloads a ZIP, and GitHub caches are delayed. The numbers above are what the
> snapshot captured at the measurement date. For launch-delta measurement, the comparison is
> "count on launch date" vs "count 14–30 days later" — never a single snapshot read in
> isolation.

## Release-to-release comparison (download counts at snapshot date)

| Release | Published | all.zip | core.zip |
|---|---|---|---|
| v0.1.0 | 2026-08-02T19:51Z | 0 | 0 |
| v0.2.0 | 2026-08-02T22:14Z | 2 | 1 |
| v0.3.0 | 2026-08-02T23:47Z | 3 | 2 |

The download counts are near-zero and are, in the likely case, the maintainer's own test
downloads — the repository is one day old, not a failed product. Do not read meaning into
them yet; the baseline exists so future deltas are measurable.

## Repository metadata at this snapshot

- Description (new): "Evidence-backed product management skills for AI agents — discovery,
  prioritization, experiments, stakeholder alignment, and defensible product decisions."
- Homepage (new): `https://lucumax.github.io/product-academy/skills/`
- Topics (new): 15 (agent-skills, ai-agents, claude-code, codex, cursor, customer-discovery,
  decision-making, evidence-based, llm, opencode, product-experiments, product-leadership,
  product-management, product-manager, product-strategy)

## What is unavailable at this snapshot

- **GitHub traffic (visitors, unique visitors, clones, referring sites):** GitHub's Traffic
  API requires a token with specific scope and only reports the last 14 days; the repo is one
  day old, so this is empty and will be measured after real traffic exists. Requires manual
  check (repo → Insights → Traffic) as well.
- **Site analytics:** the site deliberately has no invasive analytics (per measurement plan).
- **skills.sh leaderboard / install telemetry:** no page exists; created by usage, not by
  claim. Do not fabricate.

## What requires manual access (Walter)

- **Google Search Console:** no property verified, no sitemap submitted, no impressions data.
  See `SEARCH_CONSOLE_AND_INDEXING_RUNBOOK.md` and the manual-action list below.
- **Bing Webmaster Tools:** same status.
- **GitHub Traffic:** Insights → Traffic requires the logged-in account.

## Interpretation limitations

1. This is a **one-day-old repository**. Zero stars/forks/installs is the truthful baseline;
   any growth claim must be measured against this, not against an assumed starting point.
2. The download counts on v0.2.0/v0.3.0 are likely the maintainer's own tests and the verify
   cycle; they are not external demand. Do not treat them as adoption.
3. `watchers` uses `subscribers_count` (the GitHub API field); it is 0.
4. Discussions are disabled on the repo; the snapshot records `discussions_enabled: false`
   and `open_discussions: null` rather than a misleading "0".
5. Return use and first-use success cannot be measured without invasive analytics and are
   intentionally not tracked; the measurement plan's funnel interpretation rules apply.

## Funnel interpretation rules that apply from this baseline

- Stars without installs → attractive positioning, unproven value.
- Installs without successful first use → activation failure; investigate demos/first-use.
- Search impressions without clicks → title/description mismatch.
- Visits without installs → positioning or installation friction.
- Issues and critical feedback are stronger evidence than passive stars.

## Search Console manual actions for Walter (none performed)

1. Add a **URL-prefix property** `https://lucumax.github.io/product-academy/` (or Domain
   property `lucumax.github.io`) in Search Console.
2. Verify ownership:
   - URL-prefix: add the provided HTML meta tag to `webapp/src/layouts/Base.astro` `<head>`,
     rebuild, deploy; or
   - Domain: DNS TXT record on `lucumax.github.io` if that domain is controllable.
3. Submit sitemap: **Sitemaps → Submit** `https://lucumax.github.io/product-academy/sitemap-index.xml`.
4. Request indexing for priority pages after submission:
   - `/product-academy/skills/`
   - `/product-academy/skills/make-go-no-go-call/`
   - `/product-academy/skills/frame-product-problem/`
   - `/product-academy/skills/synthesize-customer-discovery/`
   - `/product-academy/skills/workflows/`
5. Capture the **starting search impression baseline** (currently expected to be empty —
   the property is new and unindexed; record the actual empty state).
6. Repeat the measurement at **7, 14, and 30 days** and record against this baseline.
7. Do the same in Bing Webmaster Tools (import from Search Console is one click once the
   property exists).
