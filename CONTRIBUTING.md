# Contributing

Thank you for being here. This repository wants contributors and advocates, not spectators.

The core product is the **agent-skill pack** (`skills/`). The bar for a new skill is
evidence-aware decision artifacts, not generic templates. We would rather improve one skill's
usefulness than add ten skills nobody runs weekly.

## Ways to contribute

1. **Report a broken install or a skill that misbehaves.** Use the bug template — include the
   platform, the exact command/prompt, and what you expected.
2. **Suggest a missing PM job** (not a missing framework). Use the skill-request template and
   describe the *job* and the *artifact* you need, not the methodology you want.
3. **Improve a skill's worked example or failure modes.** The fastest high-value contribution:
   a weak worked example or an unlisted failure mode.
4. **Run the eval scenarios** (`skills/evals/scenarios/`) and report results honestly —
   including where a skill failed. Independent evaluation is our biggest open gap.
5. **Fix documentation, install guides, or the `skills/` website section.**
6. **Distribute** — share a demo, add the repo to a relevant directory, or teach with it.
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
python scripts/validate_academy.py   # 660 quality-gate checks
python scripts/validate_skills.py    # skill-pack contract checks
python -m pytest -q                  # test suite (84+)
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
