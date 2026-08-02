# Skills — Product Academy Evidence Pack

This folder is the **source of truth** for the Product Academy's agent-skill
pack. The installable distribution lives in the `product-academy-skills`
repository; this is where the skills are authored and validated.

## What these skills are

Each skill turns one Academy doctrine capability into an executable decision
for an AI agent. The contract is strict: a skill must return a **verdict**
with a **confidence label** and **doctrine citations** — never just a memo.

## Authoring a new skill

1. Copy `_template/SKILL.md` to `skills/<kebab-name>/SKILL.md`
2. Fill in frontmatter (name, description, type, version, best_for, doctrine, license)
3. Write the 8 required sections (Purpose, Input, Method, Verdict Contract,
   Thresholds, Evidence & Doctrine, Common Pitfalls, Related Skills)
4. Add `references/doctrine-map.md` listing exact Academy IDs
5. Run `python scripts/validate_skills.py` — it must pass

**Type discipline:** `assess` returns a scored verdict against thresholds;
`assist` guides reasoning to a decision. Never a document-producing skill.

## Validating

```bash
python scripts/validate_skills.py
```

This runs in CI on every push. It checks: frontmatter parses, required
fields + sections exist, `type` is valid, the Verdict Contract has all four
sub-parts, and every doctrine reference resolves to a real Academy ID or
file path.

## How skills cite doctrine

- Principles: `PRN-0001` … `PRN-0016`
- Contradictions: `CON-0001` … `CON-0013`
- Cases: `CASE-0001` … `CASE-0019` (with `causal_confidence` ratings)
- Sources: `SRC-*` (in `sources/registry.yaml`, tiers A–E)
- Tools: `09_tools/<TEMPLATE>.md`

Skills **cite** these by stable ID and never reproduce third-party content.

## Publishing

The pack is released from this source to `product-academy-skills` via the
release pipeline: ZIP bundles (starter / all), per-platform install docs,
and the `.claude-plugin` marketplace manifest.
