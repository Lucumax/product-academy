# Installation Matrix

Statuses: **VERIFIED** (executed end-to-end this sprint) · **PARTIALLY_VERIFIED** (mechanism
verified, in-product discovery requires a logged-in session) · **DOCUMENTED_ONLY** (instructed,
depends on a platform feature I cannot operate) · **UNSUPPORTED** (does not work / not claimed).

Test date: 2026-08-02. Environment: Windows, Node 24, `npx` (skills.sh CLI), clean temporary
directories under `%LOCALAPPDATA%\Temp\opencode\`.

## `skills` CLI (skills.sh) — the native route

| Path | Status | Exact command | Result |
|---|---|---|---|
| List available skills | **VERIFIED** | `npx -y skills add <repo-or-path> --list` | Clones repo, discovers skills, prints the list. On the fixed tree: **14 skills**. Note: current remote `main` still shows 16 (template + deprecated stub) until this branch is merged. |
| Install one skill | **VERIFIED** | `npx -y skills add <repo-or-path> make-go-no-go-call --yes` | Created `.agents/skills/make-go-no-go-call/SKILL.md` + `references/doctrine-map.md` (246 lines, intact). Installed for universal agents (Codex, OpenCode, Gemini CLI, Amp, +12) and symlinked for Claude Code. |
| Install all skills | **PARTIALLY_VERIFIED** | `npx -y skills add <repo-or-path>` (no selector) | Interactive selector is offered; not fully exercised. Equivalent coverage is available via the all-skill ZIP. |
| Remote `Lucumax/product-academy` form | **VERIFIED (mechanism)** | `npx -y skills add Lucumax/product-academy --list` | Works and clones from GitHub; results reflect remote `main`, which is still pre-merge during this sprint. Re-test after merge. |

**Telemetry note (skills.sh):** the CLI sends anonymous aggregate install telemetry used to
rank skills on the skills.sh leaderboard. No repository page or leaderboard entry exists yet;
one is created by usage, not by claim. The install-count badge is added only if/when a
skills.sh page exists and the description is accurate.

## Claude Code

| Path | Status | Notes |
|---|---|---|
| Marketplace plugin | **DOCUMENTED_ONLY** | `.claude-plugin/marketplace.json` + `plugin.json` exist and are valid; `/plugin marketplace add Lucumax/product-academy` → `/plugin install evidence-pack` is documented. Requires a logged-in Claude Code session to confirm end-to-end. |
| ZIP / repo skill folders | **PARTIALLY_VERIFIED** | Skill folders are Claude Code skill-shaped (folder + `SKILL.md` + references). Manual wiring documented. |

## ZIP downloads (GitHub Releases)

| Path | Status | Notes |
|---|---|---|
| `product-academy-skills-all.zip` (14 skills + shared contract + workflows + docs) | **VERIFIED** | Built by CI, downloaded from the release, contents inspected (all 14 skill folders, `SKILL_CONTRACT.md`, 4 workflows, `INDEX.md`, `PORTFOLIO_MAP.md`, `INSTALL.md`). |
| `product-academy-skills-core.zip` (8-skill starter) | **VERIFIED** | Built by CI; self-contained (`INSTALL.md`, `CORE_README.md`, shared contract, 8 skill folders). |
| Manual Codex `.agents/skills/` | **PARTIALLY_VERIFIED** | ZIP contents are the correct shape; in-product discovery confirmed in a logged-in Codex session is pending. |
| Manual Cursor `.cursor/skills/` | **PARTIALLY_VERIFIED** | Same ZIP shape; logged-in session confirmation pending. |

## Claude.ai / Desktop and ChatGPT

| Path | Status | Notes |
|---|---|---|
| Upload ZIP as project knowledge | **DOCUMENTED_ONLY** | Depends on the plan's knowledge features; cannot be operated from here. |

## Known limitations

- The deprecated `run-source-tier-check` routing stub is listed by the `skills` CLI (its
  frontmatter name/description are valid, and the CLI's full-depth listing path does not honor
  `metadata.internal`). Its description explicitly begins "DEPRECATED… merged into
  `audit-decision-evidence`", so an installer is immediately routed. The skill template was
  renamed to `_template/SKILL.template.md` so the CLI no longer lists a placeholder skill.
- `metadata.internal: true` is set on the template and deprecated stub; it is honored at
  install time but not by the CLI's `--list` full-depth path (upstream behavior).
