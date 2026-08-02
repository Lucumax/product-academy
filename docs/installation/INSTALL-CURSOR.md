# Install with Cursor

Cursor reads skills from a project's `.cursor/skills/` directory (skill folders containing a
`SKILL.md`).

## Steps

1. Download [`product-academy-skills-all.zip`](https://github.com/Lucumax/product-academy/releases/latest).
2. Unzip it.
3. Copy the skill folders into `.cursor/skills/` at the root of the project. Copy
   `SKILL_CONTRACT.md` alongside them.
4. Reference a skill by name in a conversation, e.g.:

```
Run the prioritize-product-opportunities skill. Input: backlog [list], capacity [X].
Rank it with uncertainty exposed.
```

## Notes

- No `$ARGUMENTS` templating is used, so prompts behave consistently across Cursor, Codex,
  Claude Code, and OpenCode.
- Status: **VERIFIED (ZIP build); DOCUMENTED_ONLY (in-product discovery)** — confirm in a
  logged-in Cursor session and record the result in the installation matrix.
