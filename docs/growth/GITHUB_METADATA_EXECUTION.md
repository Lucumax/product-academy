# GitHub Metadata Execution

Executed on the `skills-launch-validation-v1` branch. All API calls are authenticated as
`Lucumax` via `gh` (token scopes include `repo`). Repository visibility remains **public**
and was not changed. Branch protections were not touched.

## Repository description

| Field | Value |
|---|---|
| Previous | `Evidence-backed product leadership curriculum (Senior PM → CPO) with a guided web app. Doctrine, cases, contradictions, a 180-source evidence registry, an interactive simulator, and role-based learning journeys.` |
| Proposed | `Evidence-backed product management skills for AI agents — discovery, prioritization, experiments, stakeholder alignment, and defensible product decisions.` |
| Applied | Same as proposed (154 chars, within GitHub's 350-char limit). |

Command:

```bash
gh api -X PATCH repos/Lucumax/product-academy \
  -f description="Evidence-backed product management skills for AI agents — discovery, prioritization, experiments, stakeholder alignment, and defensible product decisions." \
  -f homepage="https://lucumax.github.io/product-academy/skills/" \
  --jq '{description, homepage}'
```

Verification:

```json
{
  "description": "Evidence-backed product management skills for AI agents — discovery, prioritization, experiments, stakeholder alignment, and defensible product decisions.",
  "homepage": "https://lucumax.github.io/product-academy/skills/"
}
```

## Repository website

| Field | Value |
|---|---|
| Previous | `https://lucumax.github.io/product-academy/` |
| Proposed | `https://lucumax.github.io/product-academy/skills/` |
| Applied | `https://lucumax.github.io/product-academy/skills/` |

Applied with the same PATCH call above. Verified via:

```bash
gh api repos/Lucumax/product-academy --jq '.homepage'
# https://lucumax.github.io/product-academy/skills/
```

## Repository topics

| Field | Value |
|---|---|
| Previous | `[]` (none) |
| Proposed | 15 topics (approved list, below) |
| Applied | 15 topics, verified through the API |

Applied topics (15, the full approved set):

`agent-skills`, `ai-agents`, `claude-code`, `codex`, `cursor`,
`customer-discovery`, `decision-making`, `evidence-based`, `llm`, `opencode`,
`product-experiments`, `product-leadership`, `product-management`,
`product-manager`, `product-strategy`

Command (topics requires an array body, so the array was piped to `gh`):

```powershell
$body = @{ names = @("product-management","product-manager","agent-skills","ai-agents","claude-code","codex","cursor","opencode","product-strategy","customer-discovery","product-experiments","product-leadership","decision-making","evidence-based","llm") } | ConvertTo-Json -Compress
$body | gh api -X PUT repos/Lucumax/product-academy/topics --input - --jq '.names'
```

Verification (all 15 returned, sorted by GitHub):

```json
["agent-skills","ai-agents","claude-code","codex","cursor","customer-discovery","decision-making","evidence-based","llm","opencode","product-experiments","product-leadership","product-management","product-manager","product-strategy"]
```

## Social preview

The prepared asset exists:

- Path: `docs/growth/assets/social-preview-1280x640.png`
- Dimensions: 1280 x 640 px (verified via System.Drawing)
- File size: 95,956 bytes (~94 KB, under GitHub's 1 MB limit)
- Format: PNG

GitHub does **not** provide a supported REST API path to upload a repository social
preview image (no documented `PATCH /repos/{owner}/{repo}` field and no dedicated
endpoint exists as of 2026-08-02). No API path was invented. This remains a manual action.

### Manual action required (Walter)

1. Open `https://github.com/Lucumax/product-academy/settings/` (Settings → General).
2. Scroll to **Social preview**.
3. Click **Edit**, upload `docs/growth/assets/social-preview-1280x640.png`
   (1280×640 PNG, ~94 KB — already within GitHub's size recommendations of ≥640×320 and
   <1 MB).
4. Click **Set social preview**.
5. Verify the preview renders correctly. If it does not render (e.g. the filename with the
   `-1280x640` suffix mis-triggers caching), re-upload the same bytes under a fresh name.

The same image is also used as the site's Open Graph image at
`webapp/public/og-skills.png` (identical 95,956-byte file), so social cards for
`/skills/` and sub-pages already carry the visual; this upload only fixes the GitHub
repository card.

## Items requiring Walter's manual action

| # | Item | Why manual | Reference |
|---|---|---|---|
| 1 | Upload social preview image | No GitHub API endpoint exists | `docs/growth/GITHUB_METADATA_EXECUTION.md` |
| 2 | (Optional) Confirm the image renders on a test share | UI-only check | Section "Social preview" above |
