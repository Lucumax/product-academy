# Product Academy — Agent Skill Pack

Evidence-backed product decisions, executable by AI agents (Claude Code,
Codex, Cursor, ChatGPT) at the moment you have to decide.

**The Academy is the map. These skills turn the map into a decision.**

Every skill returns a **verdict** (GO/NO-GO, TIER-MATCHED/TIER-INFLATED,
PASS/FAIL/LEARN…) with a confidence label and citations back to the
Academy's doctrine — never just a formatted memo. That is the difference
between an executable skill and a document dressed up as one.

## Install

- **Claude Code:** `/plugin marketplace add Lucumax/product-academy-skills`
  then `/plugin install evidence-pack`
- **Claude.ai / Desktop:** download a ZIP below and upload it
- **Codex / Cursor:** download a ZIP and drop it in `.agents/skills/` (Codex)
  or `.cursor/skills/` (Cursor); see `START_HERE.md`

## The 10 P0 skills

| Skill | Type | What it returns |
|-------|------|-----------------|
| [audit-decision-evidence](audit-decision-evidence/SKILL.md) | assess | Verdict on a decision's evidence adequacy, per claim |
| [run-source-tier-check](run-source-tier-check/SKILL.md) | assess | TIER-MATCHED / TIER-INFLATED / TIER-DEFICIENT |
| [scan-contradictions-assumptions](scan-contradictions-assumptions/SKILL.md) | assist | Ranked exposed assumptions + live contradictions |
| [conduct-causal-confidence-review](conduct-causal-confidence-review/SKILL.md) | assess | Causal strength verdict + what would flip it |
| [make-go-no-go-call](make-go-no-go-call/SKILL.md) | assess | GO / NO-GO / PAUSE / PROCEED-AT-RISK with thresholds |
| [classify-decision-reversibility](classify-decision-reversibility/SKILL.md) | assist | Type-1 / Type-2 / RECLASSIFIED-TYPE-1 |
| [run-case-based-premortem](run-case-based-premortem/SKILL.md) | assist | Ranked failure scenarios + DEFENSIBLE verdict |
| [pressure-test-product-thesis](pressure-test-product-thesis/SKILL.md) | assess | FALSIFIABLE-THESIS / BELIEF-PRESENTED-AS-THESIS |
| [check-ai-evaluation-contract](check-ai-evaluation-contract/SKILL.md) | assess | CONTRACT-COMPLETE / CONTRACT-GAPPY / NO-CONTRACT |
| [assess-product-market-fit-health](assess-product-market-fit-health/SKILL.md) | assess | HEALTHY / DECAYING / NEVER-ACHIEVED / UNMEASURED |

## Skill anatomy

Each skill is a folder with `SKILL.md` plus a `references/` bundle:

- **Purpose** — when to invoke, and when NOT to
- **Input** — what to bring (no `$ARGUMENTS` templating; works on every runtime)
- **Method** — one question at a time, recording "unknown" as an assumption
- **Verdict Contract** — the output: verdict + confidence + citations +
  stated assumptions + what-would-change-it
- **Thresholds** — reproducible pass/fail criteria
- **Evidence & Doctrine** — stable Academy IDs (PRN-/CON-/CASE-/SRC-)
- **Common Pitfalls** — named failure modes and corrections

## Type discipline

- **`assess`** — returns a scored verdict against explicit thresholds
- **`assist`** — guides reasoning to a decision

## License

CC BY 4.0, matching the Academy. Skills cite Academy doctrine by stable ID —
they don't reproduce third-party content. See `LICENSE` and
`COPYRIGHT_AND_ACCESS_POLICY.md` in the Academy repo.

## Source of truth

The authoritative skill sources live in the Academy monorepo at `skills/`
(validated by `scripts/validate_skills.py`). The installable pack is
published to `product-academy-skills`.
