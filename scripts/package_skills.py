#!/usr/bin/env python3
"""
Package the skill pack into installable ZIPs + install docs for GitHub
Releases. Produces dist/skills/:
  - product-academy-skills-all.zip       every active skill + shared contract + workflows
  - product-academy-skills-core.zip      the 8 highest-frequency PM skills (starter set)
  - INSTALL.md                           per-platform instructions (also inside both ZIPs)

Each ZIP is self-contained: it carries INSTALL.md plus (for the core ZIP) a CORE_README
that lists the starter skills, so no doc inside a ZIP references a skill that is not
shipped. Academy doctrine (09_tools/, sources/, evidence/) is intentionally NOT bundled —
skills cite it by stable ID and full-mode steps are optional when the Academy repo is not
present; see the shared contract.

Portable (zipfile from stdlib). Run from repo root:
    python scripts/package_skills.py
"""

import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist" / "skills"

SKIP = {"_template", "quality", "evals", "__pycache__"}
TOP_LEVEL_DOCS = ["INDEX.md", "README.md", "PORTFOLIO_MAP.md"]
SHARED = "_shared"
WORKFLOWS = "workflows"

# The 8 highest-frequency PM skills (starter set). See PORTFOLIO_MAP.md.
CORE_SKILLS = [
    "frame-product-problem",
    "synthesize-customer-discovery",
    "prioritize-product-opportunities",
    "design-product-experiment",
    "align-stakeholders-on-decision",
    "assess-product-market-fit-health",
    "classify-decision-reversibility",
    "make-go-no-go-call",
]


def collect_active_skills():
    active = []
    for d in sorted(SKILLS.iterdir()):
        if not d.is_dir() or d.name in SKIP or d.name == SHARED or d.name == WORKFLOWS:
            continue
        if d.name.startswith("_"):
            continue
        fm_file = d / "SKILL.md"
        if fm_file.exists():
            text = fm_file.read_text(encoding="utf-8")
            m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
            if m and "deprecated:" in m.group(1) and "true" in m.group(1):
                continue
        active.append(d.name)
    return sorted(active)


def write_install_doc():
    lines = [
        "# Install the Product Academy Skill Pack",
        "",
        "These skills turn evidence-backed product decisions into executable verdicts for AI",
        "agents (Claude Code, Codex, Cursor, ChatGPT, OpenCode). Every skill returns a verdict",
        "or decision artifact with a confidence label, stated assumptions, what-would-change-it,",
        "and a next action. The shared contract (`_shared/SKILL_CONTRACT.md`) defines the",
        "evidence taxonomy and output format.",
        "",
        "## Claude Code",
        "",
        "```bash",
        "/plugin marketplace add Lucumax/product-academy",
        "/plugin install evidence-pack",
        "```",
        "",
        "## Claude.ai / Claude Desktop",
        "",
        "1. Download `product-academy-skills-all.zip`",
        "2. Upload the ZIP in your skills settings",
        "",
        "## Codex (OpenAI)",
        "",
        "1. Download `product-academy-skills-all.zip`",
        "2. Unzip and place the folders in `.agents/skills/` in your project",
        "3. Reference skills by name in your prompt (e.g. `make-go-no-go-call`)",
        "",
        "## Cursor",
        "",
        "1. Download `product-academy-skills-all.zip`",
        "2. Unzip and place the folders in `.cursor/skills/`",
        "3. Reference by name in a conversation",
        "",
        "## Generic agents (OpenCode, etc.)",
        "",
        "1. Download `product-academy-skills-all.zip` or point the agent at `skills/` in the repo",
        "2. Drop the skill folders in your agent's skills directory (see your agent's docs)",
        "3. Reference by name, or start from a workflow in `workflows/`",
        "",
        "## Quick start",
        "",
        "1. Pick your job in `INDEX.md` (skill finder organized by PM job).",
        "2. Copy-paste the invocation into your agent.",
        "3. Answer the skill's questions; 'unknown' is recorded as an assumption.",
        "4. The skill returns a verdict and a next action.",
        "",
        "Rule of thumb: reversible decision → fast mode; irreversible decision → full mode.",
        "",
        "## Skill anatomy",
        "",
        "Each skill is a folder: `SKILL.md` (the contract) + `references/` (doctrine map).",
        "Every production skill has Fast mode and Full mode, an Output schema, a Verdict Contract",
        "with a Next action, Reversal conditions, and Composition hooks. See `_shared/SKILL_CONTRACT.md`.",
        "",
        "## What is NOT in the ZIP",
        "",
        "The Academy's doctrine files (09_tools/, 01_core_doctrine/, sources/, evidence/, and",
        "the AI product-management modules) are not bundled. Skills cite them by stable ID;",
        "full-mode steps that reference them are optional when the Academy repo is not present.",
        "For the full source of truth see github.com/Lucumax/product-academy.",
        "",
        "## Source of truth",
        "",
        "The authoritative sources live at `skills/` in the Academy monorepo",
        "(`github.com/Lucumax/product-academy`), validated by `scripts/validate_skills.py`.",
        "License: CC BY 4.0.",
    ]
    (DIST / "INSTALL.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_core_readme(core_skills):
    lines = [
        "# Product Academy Skill Pack — Starter Set",
        "",
        "This is the **core starter ZIP**: the 8 highest-frequency PM skills. For the full",
        "portfolio (14 skills) including the evidence/judgment layer (thesis pressure-test,",
        "evidence audit, premortem, causal review, contradiction scan, AI evaluation",
        "contract), download `product-academy-skills-all.zip`.",
        "",
        "## Skills in this ZIP",
        "",
    ]
    for s in core_skills:
        lines.append(f"- `{s}`")
    lines += [
        "",
        "## Not in this ZIP",
        "",
        "- `run-source-tier-check` (deprecated; merged into `audit-decision-evidence`).",
        "- `pressure-test-product-thesis`, `audit-decision-evidence`, `scan-contradictions-assumptions`,",
        "  `conduct-causal-confidence-review`, `run-case-based-premortem`, `check-ai-evaluation-contract`",
        "  — download the all ZIP for these.",
        "",
        "## Install",
        "",
        "See `INSTALL.md` in this ZIP. The shared contract is in `_shared/SKILL_CONTRACT.md`.",
        "Academy doctrine files are not bundled; full-mode steps that reference them are",
        "optional without the Academy repo. License: CC BY 4.0.",
    ]
    (DIST / "CORE_README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def add_zip_member(zf, path, arcname):
    zf.write(path, arcname)


def make_all_zip(zf, skill_names):
    for doc in TOP_LEVEL_DOCS:
        src = SKILLS / doc
        if src.exists():
            zf.write(src, src.relative_to(SKILLS))
    zf.write(SKILLS / SHARED / "SKILL_CONTRACT.md", "SKILL_CONTRACT.md")
    for wf in sorted((SKILLS / WORKFLOWS).glob("*.md")):
        zf.write(wf, wf.relative_to(SKILLS))
    zf.write(DIST / "INSTALL.md", "INSTALL.md")
    for name in skill_names:
        src = SKILLS / name
        for f in src.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(SKILLS))


def make_core_zip(zf, skill_names):
    zf.write(DIST / "INSTALL.md", "INSTALL.md")
    zf.write(DIST / "CORE_README.md", "CORE_README.md")
    zf.write(SKILLS / SHARED / "SKILL_CONTRACT.md", "SKILL_CONTRACT.md")
    for name in skill_names:
        src = SKILLS / name
        for f in src.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(SKILLS))


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    skills = collect_active_skills()
    core = [s for s in CORE_SKILLS if s in skills]
    print(f"Packaging {len(skills)} active skills...")

    write_install_doc()
    write_core_readme(core)

    all_dest = DIST / "product-academy-skills-all.zip"
    with zipfile.ZipFile(all_dest, "w", zipfile.ZIP_DEFLATED) as zf:
        make_all_zip(zf, skills)

    core_dest = DIST / "product-academy-skills-core.zip"
    with zipfile.ZipFile(core_dest, "w", zipfile.ZIP_DEFLATED) as zf:
        make_core_zip(zf, core)

    print(f"  all:  {all_dest} ({all_dest.stat().st_size} bytes)")
    print(f"  core: {core_dest} ({core_dest.stat().st_size} bytes)")
    print("  INSTALL.md + CORE_README.md written (both inside the ZIPs)")
    print("Done. Upload dist/skills/* to a GitHub Release.")


if __name__ == "__main__":
    main()
