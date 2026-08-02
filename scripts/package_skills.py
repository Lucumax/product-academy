#!/usr/bin/env python3
"""
Package the skill pack into installable ZIPs + install docs for GitHub
Releases. Produces dist/skills/:
  - product-academy-skills-all.zip      every skill
  - product-academy-skills-core.zip     the 10 P0 skills
  - INSTALL.md                          per-platform instructions

Portable (zipfile from stdlib). Run from repo root:
    python scripts/package_skills.py
"""

import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
DIST = ROOT / "dist" / "skills"

SKIP = {"_template", "__pycache__"}


def collect_skills():
    return sorted(d.name for d in SKILLS.iterdir() if d.is_dir() and d.name not in SKIP)


def make_zip(zip_name, skill_names):
    dest = DIST / zip_name
    with zipfile.ZipFile(dest, "w", zipfile.ZIP_DEFLATED) as zf:
        for name in skill_names:
            src = SKILLS / name
            for f in src.rglob("*"):
                if f.is_file():
                    zf.write(f, f.relative_to(SKILLS))
    return dest


def write_install_doc():
    lines = [
        "# Install the Product Academy Skill Pack",
        "",
        "These skills make the Academy's evidence discipline executable by AI agents at the moment of a decision. Every skill returns a verdict (GO/NO-GO, TIER-MATCHED/INFLATED, PASS/FAIL/LEARN) with a confidence label and citations back to Academy doctrine.",
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
        "3. Reference skills by name in your prompt (e.g. `run-source-tier-check`)",
        "",
        "## Cursor",
        "",
        "1. Download `product-academy-skills-all.zip`",
        "2. Unzip and place the folders in `.cursor/skills/`",
        "3. Reference by name in a conversation",
        "",
        "## Skill anatomy",
        "",
        "Each skill is a folder: `SKILL.md` (the contract) + `references/` (doctrine map). The `SKILL.md` has: Purpose, Input, Method, Verdict Contract (verdict + confidence + citations + assumptions + what-would-flip-it), Thresholds, Evidence & Doctrine, Common Pitfalls, Related Skills.",
        "",
        "## Source of truth",
        "",
        "The authoritative sources live at `skills/` in the Academy monorepo (`github.com/Lucumax/product-academy`), validated by `scripts/validate_skills.py`. License: CC BY 4.0.",
    ]
    (DIST / "INSTALL.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    skills = collect_skills()
    print(f"Packaging {len(skills)} skills...")
    all_zip = make_zip("product-academy-skills-all.zip", skills)
    core_zip = make_zip("product-academy-skills-core.zip", skills[:10])
    write_install_doc()

    print(f"  all:  {all_zip} ({all_zip.stat().st_size} bytes)")
    print(f"  core: {core_zip} ({core_zip.stat().st_size} bytes)")
    print("  INSTALL.md written")
    print("Done. Upload dist/skills/* to a GitHub Release.")


if __name__ == "__main__":
    main()
