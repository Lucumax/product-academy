# Live Acquisition and Activation Audit

Date: 2026-08-02. Branch: `skills-launch-validation-v1`. Audited as a first-time user from
clean temporary directories; no repository-local assumptions. Live site:
`https://lucumax.github.io/product-academy/` (deployed from commit `9c84756`).

## Scoring scale

1–5 on each dimension. 5 = excellent; 3 = acceptable; 1 = broken. "Do not give perfect
scores merely because links work." A 4+ on comprehension requires the artifact to actually
explain, not just to exist.

---

## Path A — Working PM browsing the site

Start: `https://lucumax.github.io/product-academy/skills/`.

| Question a 10-second scan must answer | Found? | Where |
|---|---|---|
| What is the product? | Yes | H1 "Product Management Skills for AI Agents" + hero sub "Evidence-backed product decisions…" |
| Who is it for? | Implied | "executable by Claude Code, Codex, Cursor, OpenCode, and ChatGPT" — agent names, not the audience. The PM audience is implied by the skills' job cards. |
| What task to start with? | Yes | "Find your skill by job" — 14 job cards ("We should build X", "Interviews done, notes unsorted", …) |
| What output will they receive? | Yes | "Every skill returns a decision artifact with a next action — in fast mode (reversible calls) or full mode (one-way doors)" |
| How to install? | Yes | Install bar at top + "Install" section (CLI, Claude Code, ZIP, Codex/Cursor) |
| How do fast and full differ? | Yes | Dedicated "Fast mode vs full mode" section with the rule of thumb |

**Ratings**

| Dimension | Score | Notes |
|---|---|---|
| Comprehension | 4 | Hero and job finder are strong; audience ("product managers") is only implied, never stated in the hero. |
| Friction | 3 | 14 cards + 4 workflow cards + install section on one page is information-dense; the above-the-fold works, the page below is long. |
| Successful completion | 4 | Every route (install, find, run) is reachable and functional. |
| Artifact usefulness | 4 | Job cards each carry a copy-paste invocation and describe the decision artifact returned. |
| Credibility | 4 | Honest "Verified end-to-end" claims only where the matrix backs them; no fabricated numbers. |
| Likelihood of reuse | 3 | Good for discovery; return use depends on whether the install actually helps (unproven, see Path C/E). |
| Likelihood of starring/sharing | 3 | Would earn a star from a PM who runs a demo successfully; no ask-for-star present (correct). |

**Found defects (Path A):**
1. **Workflow card descriptions were truncated mid-sentence** ("The terminal artifact is a" /
   "…The terminal"). Root cause: `webapp/scripts/import-content.mjs` regex `/^Decision: (.+)$/m`
   stopped at the first line break; three of four workflow `decision` strings were cut.
   **Fixed** (multi-line capture + collapse), rebuild verified. This was a real rendered-content
   bug, not cosmetic.

---

## Path B — GitHub visitor

Start: `https://github.com/Lucumax/product-academy`.

| Question | Found? | Where |
|---|---|---|
| Understand the product above the fold | Yes | README H1 "Product Management Skills for AI Agents" + bold one-liner; skills-first. |
| Distinguish from a curriculum-only repo | Yes | README leads with the skill pack; the Academy is explicitly "behind it" (secondary). |
| Install | Yes | Install table (6 rows) with `npx skills add`, Claude Code, ZIP paths. |
| See a demonstration | Yes | "Try it yourself (three public demos)" section linking the three demo files. |
| Identify evidence-backed differentiation | Yes | "What makes these different": internal-evidence-first taxonomy, evidence ≠ assumption ≠ inference, fast/full, JSON artifact contract. |
| Find contribution instructions | Yes | "Contributing" section → `CONTRIBUTING.md`. |
| Find the current release | Partial | "releases/latest" links exist in install table; no explicit "latest release" tag/note in the README body. A visitor must click a ZIP link to learn the release. |

**Ratings**

| Dimension | Score | Notes |
|---|---|---|
| Comprehension | 4 | Above-the-fold is clean and skills-first; one long-ish README but well-structured. |
| Friction | 4 | Install table is table-of-contents-able; demos are one click away. |
| Successful completion | 4 | All links resolve; install command verified (Path C). |
| Artifact usefulness | 3 | README shows a worked example table and demos; the product itself needs the install to be useful. |
| Credibility | 4 | Claims "verified" only where tested; evaluation report linked and honestly reports weaknesses. |
| Likelihood of reuse | 3 | Depends on first-use quality. |
| Likelihood of starring/sharing | 3 | A PM who reads it will star if the evidence-differentiation holds on use. |

**Note:** repository About metadata (description, website, topics) was applied this sprint
(see `GITHUB_METADATA_EXECUTION.md`); the live About block now shows the skills-first
description and `/skills/` website. Social-preview upload remains manual (no API).

---

## Path C — Native installer

Clean directory: `%TEMP%\opencode\cli-*`. Commands run 2026-08-02 (Node 24, `npx` 11.16.0).

| Test | Command | Result |
|---|---|---|
| List | `npx skills add Lucumax/product-academy --list` | **14 skills** discovered and listed with descriptions. |
| Install one skill | `npx skills add Lucumax/product-academy --skill make-go-no-go-call --yes` | "Installed 1 skill" → `.agents/skills/make-go-no-go-call/SKILL.md` + `references/doctrine-map.md`; Claude Code symlink created. |
| Install all (full) | `npx skills add Lucumax/product-academy --yes` | Installed **14** skill folders into `.agents/skills/`, each with `SKILL.md` + `references/`. |

Notes:
- The `--skill <name> --yes` form is required for a single skill; a bare
  `add <repo> <name> --yes` was observed to install everything (CLI behavior, not ours).
  The README/site only advertise the bare command, so a user wanting one skill must discover
  `--skill`. Low friction for the full install (the advertised path), medium friction for a
  targeted install.
- Two target-agent structures tested: universal `.agents/skills/` (Codex/OpenCode/etc.) and
  the Claude Code symlink created by the CLI. Claude Code *marketplace* install
  (`/plugin marketplace add`) is `DOCUMENTED_ONLY` — it requires a logged-in session and was
  not executed here (consistent with the installation matrix).
- Starter-set install: the CLI offers no "starter set" concept; the 8-skill starter pack is
  ZIP-only. Acceptable, but a user who wants fewer skills must choose the ZIP or use `--skill`.

**Ratings**

| Dimension | Score | Notes |
|---|---|---|
| Comprehension | 4 | `--list` output is clear and each skill has a useful description. |
| Friction | 4 | One command; no config; works from a clean dir. |
| Successful completion | 5 | Single and full installs both succeeded; files verified on disk. |
| Artifact usefulness | 4 | Installed skills are immediately usable (SKILL.md + doctrine map). |
| Credibility | 4 | CLI telemetry is skills.sh's own; no fabricated leaderboard claims here. |
| Likelihood of reuse | 4 | Install is the strongest part of the experience. |
| Likelihood of starring/sharing | 4 | A successful native install is the single best moment to earn a star. |

---

## Path D — ZIP user

Downloaded `product-academy-skills-all.zip` and `product-academy-skills-core.zip` from the
public `skills-v0.3.0` release and extracted into clean directories.

| Check | All ZIP | Core ZIP |
|---|---|---|
| Extraction | Flat, clean | Flat, clean |
| Folder layout | `INDEX.md`, `README.md`, `PORTFOLIO_MAP.md`, `SKILL_CONTRACT.md`, `INSTALL.md`, `workflows/` (4), 14 skill folders | `CORE_README.md`, `INSTALL.md`, `SKILL_CONTRACT.md`, 8 skill folders |
| Installation instructions | `INSTALL.md` covers Claude Code, Claude.ai/Desktop, Codex, Cursor, generic agents | Same `INSTALL.md` + `CORE_README.md` |
| Skill count | 14 | 8 |
| References | Each skill ships `references/doctrine-map.md` | Same |
| Workflows | 4 | none (documented as all-ZIP only) |
| Deprecated skill surfaced? | No `run-source-tier-check` in either ZIP | No |
| Dev-only files required? | No scripts/build artifacts needed for use | No |

**Ratings**

| Dimension | Score | Notes |
|---|---|---|
| Comprehension | 4 | `INDEX.md`/`PORTFOLIO_MAP.md` + `INSTALL.md` explain structure and install. |
| Friction | 3 | Requires manual unzip + placing folders; the CLI path is strictly easier. |
| Successful completion | 4 | Extracts and is structurally correct for the documented agents. |
| Artifact usefulness | 4 | Self-contained; references are stable IDs, and the ZIP documents that Academy doctrine files are optional. |
| Credibility | 4 | Accurate about what is/isn't included ("What is NOT in the ZIP"). |
| Likelihood of reuse | 3 | ZIP is a fallback for non-CLI users; CLI is primary. |

---

## Path E — Demonstration user

All three prepared demos (`docs/growth/demos/01..03`) were run against the skill contracts and
their reference fixtures.

| Demo | Skill | Prompt understandable | Inputs available | Artifact matches stated example | Internal refs block execution? |
|---|---|---|---|---|---|
| 1 Discovery synthesis | `synthesize-customer-discovery` | Yes | 25 interviews + usage data fully specified | Yes — `BEHAVIOR-CONTRADICTS`, cohort split next action, matches contract worked example | No |
| 2 Experiment design | `design-product-experiment` | Yes | change + baseline + assumption specified | Yes — `SPEC-READY` with pre-committed thresholds, matches contract worked example | No |
| 3 GO/NO-GO | `make-go-no-go-call` | Yes | initiative, strategy, evidence, reversibility specified | Yes — NO-GO / PROCEED-AT-RISK surfaced + declined, matches contract threshold ladder | No |

Notes:
- Each demo explicitly states the input the skill needs and where it comes from; no demo
  requires an internal Academy file to run (doctrine maps are stable IDs, optional).
- The three demo artifacts are contract-consistent reconstructions: Demo 2 is literally the
  skill contract's worked example, and Demos 1 and 3 are original compositions consistent
  with their skills' verdict contracts and threshold ladders. That is the honest framing
  ("per the skill's contract"), and it means the demos are *reproducible shapes*, not claims
  that any given model returns them verbatim. The audit cannot verify a specific third-party
  model transcript (none exists publicly yet); the demos must be run by external PMs to
  become independent evidence. This is the intended Phase-3 gap.

**Ratings**

| Dimension | Score | Notes |
|---|---|---|
| Comprehension | 4 | Scenario → baseline → invocation → artifact → limitations is a clean pedagogical arc. |
| Friction | 3 | Requires the user to copy-paste into their own agent; no one-click runner. |
| Successful completion | 4 | Contract-consistent outputs; inputs fully specified. |
| Artifact usefulness | 4 | The discovery-contradiction and GO/NO-GO artifacts are the kind of output a PM would reuse. |
| Credibility | 4 | Honest "limitations" sections; explicitly refuses to claim superiority. |
| Likelihood of reuse | 3 | A PM who runs Demo 1 is likely to try the skill for real. |
| Likelihood of starring/sharing | 3 | Demo 1 (behavior contradicts enthusiasm) is the most shareable; the audit recommends it lead the launch. |

---

## Summary

| Path | Comprehension | Friction | Completion | Artifact | Credibility | Reuse | Star/share |
|---|---|---|---|---|---|---|---|
| A. Site | 4 | 3 | 4 | 4 | 4 | 3 | 3 |
| B. GitHub | 4 | 4 | 4 | 3 | 4 | 3 | 3 |
| C. CLI install | 4 | 4 | 5 | 4 | 4 | 4 | 4 |
| D. ZIP | 4 | 3 | 4 | 4 | 4 | 3 | 3 |
| E. Demos | 4 | 3 | 4 | 4 | 4 | 3 | 3 |

### Critical / major findings

1. **WORKFLOW-CARD TRUNCATION (major, found & fixed).** Live `/skills/` rendered three workflow
   descriptions cut mid-sentence. Fixed in `import-content.mjs`; regression test added;
   rebuild verified. Will be live after merge/deploy.
2. **Single-skill CLI affordance (minor).** The site/README advertise the bare install command;
   a targeted single-skill install needs the `--skill` flag. Add a one-line note.
3. **No independent model transcript for the demos (structural, by design).** Demos are
   contract-consistent worked examples, not third-party transcripts. External PM runs are the
   Phase-3 dependency; do not present demos as independent proof.

### What would block launch

Nothing in this audit blocks an evidence-led launch. The install path (C) and ZIP (D) are the
strongest; the site (A) and demos (E) are credible and honest. The single rendered-content bug
found here must be deployed before linking `/skills/` widely.
