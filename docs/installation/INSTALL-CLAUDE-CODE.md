# Install with Claude Code

The pack is a Claude Code plugin (marketplace `evidence-pack`).

## Marketplace install

```bash
/plugin marketplace add Lucumax/product-academy
/plugin install evidence-pack
```

This adds the repository's marketplace (`.claude-plugin/marketplace.json`) and installs the
`evidence-pack` plugin, which exposes the 14 skills.

## Manual install (no marketplace)

Clone or download the repo and point Claude Code at it, or download
[`product-academy-skills-all.zip`](https://github.com/Lucumax/product-academy/releases/latest)
and unpack the skill folders where your Claude Code setup reads skills.

## Verify

Run any skill by name, e.g.:

```
Run the make-go-no-go-call skill. Input: we want to fund the AI triage assistant;
strategy excludes customer-facing AI without an evaluation contract; it is one-way-door.
```

You should get a GO / NO-GO / PAUSE verdict with thresholds and a next action.

> Status: **DOCUMENTED_ONLY** — the manifest exists and is validated, but a logged-in
> Claude Code session is required to confirm marketplace discovery end-to-end. If
> `/plugin marketplace add` fails, use the manual install path above.
