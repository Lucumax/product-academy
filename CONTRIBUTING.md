# Contributing

Thank you for being here. This repository wants contributors and advocates, not spectators.

The core product is the **agent-skill pack** (`skills/`). The bar for a new skill is
evidence-aware decision artifacts, not generic templates. We would rather improve one skill's
usefulness than add ten skills nobody runs weekly.

## Ways to contribute

1. **Report a broken install.** Use the *Installation problem* template (`.github/ISSUE_TEMPLATE/`)
   — include the platform, agent version, exact command, and the error. Install failures are
   the highest-value feedback there is.
2. **Report a bad or misleading skill output.** Use the *Skill output failure* template — a
   wrong verdict, overconfident claim, or a missed contradiction is better evidence than a star.
3. **Report excessive-process feedback.** If a skill made a small decision feel heavy, say so —
   that is a proportionality finding, and it is exactly the failure mode we track. Use the
   *Skill output failure* template and mark it proportionality, or open a discussion.
4. **Contribute a worked example** (a real situation or a clearly-labeled fictional one where
   a skill produced a useful artifact — or failed). Use the *Worked example contribution*
   template. This is the fastest high-value contribution.
5. **Request a missing PM scenario or archetype** (not a framework). Use the *Scenario request*
   template and describe the *situation* and the *artifact* you need. Scenario requests feed
   the skill finder, the worked examples, and the external evaluation set.
6. **Run the external evaluation** (`skills/evals/external/`) and report results honestly —
   including where a skill failed. Independent evaluation is our biggest open gap.
7. **Fix documentation, install guides, or the `skills/` website section.**
8. **Distribute** — share a demo, add the repo to a relevant directory, or teach with it.
   Do not spam; lead with a demonstration.

## Authoring a skill

1. Copy `skills/_template/SKILL.template.md` into `skills/<kebab-name>/SKILL.md`.
2. Fill the frontmatter and the required sections (see `skills/_shared/SKILL_CONTRACT.md` §1).
3. Every skill ships **Fast mode and Full mode**, an **Output schema**, a **Verdict Contract
   with a Next action**, **Reversal conditions**, and **Composition hooks**.
4. Add `references/doctrine-map.md` with stable Academy IDs.
5. Run `python scripts/validate_skills.py` and `python -m pytest -q` — both must pass.

The bar:

- Does it solve a recognizable PM job?
- Does it produce a concrete decision artifact or next action?
- Does it distinguish evidence, assumption, inference, and recommendation?
- Does it adapt to product context (reversibility, archetype)?
- Is the process proportional to the decision's risk?

## Quality gates

```bash
python scripts/validate_academy.py   # quality-gate checks (660+, count grows with content)
python scripts/validate_skills.py    # skill-pack contract checks
python scripts/package_skills.py     # build the release ZIPs
python -m pytest -q                  # test suite (95+)
```

For the webapp:

```bash
cd webapp && npm run build           # content import + Astro build + pagefind
```

## Honesty rules

- No fabricated adoption, star, install, or benchmark numbers, ever.
- No "best / ultimate / 9/10" claims without comparative evidence.
- No unverified install commands — every advertised install path must be tested and
  recorded in `docs/installation/INSTALLATION_MATRIX.md`.

## Licensing

CC BY 4.0. Skills cite Academy doctrine by stable ID and never reproduce third-party content.
By contributing you agree your work is licensed under the repository license.
