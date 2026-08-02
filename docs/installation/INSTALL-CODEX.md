# Install with Codex (OpenAI)

Codex reads skills from a project's `.agents/skills/` directory (skill folders containing a
`SKILL.md`).

## Steps

1. Download [`product-academy-skills-all.zip`](https://github.com/Lucumax/product-academy/releases/latest).
2. Unzip it.
3. Copy the skill folders (e.g. `frame-product-problem/`, `make-go-no-go-call/`) into
   `.agents/skills/` at the root of the project where you use Codex. Copy
   `SKILL_CONTRACT.md` alongside them (the skills reference it).
4. Reference a skill by name in your prompt, e.g.:

```
Run the frame-product-problem skill. Input: "We should build X for Y." Return the problem frame.
```

## Notes

- Skills deliberately use no `$ARGUMENTS` templating, so the same instructions work across
  runtimes.
- The ZIP is verified to build with the 14 active skills; end-to-end discovery inside a
  logged-in Codex session is confirmed by running it. Status: **VERIFIED (ZIP build);
  DOCUMENTED_ONLY (in-product discovery)** until a logged-in session test is recorded in
  the installation matrix.
