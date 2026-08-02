# Quality Gates

## Repository Fails When

A canonical claim has no source.
A transcript has unknown provenance.
A transcript or quotation is invented.
A quotation lacks a timestamp, page, section, or equivalent location.
Paid or private material has been copied improperly.
A doctrine omits applicability conditions.
A disputed doctrine omits credible opposition.
A case presents retrospective narrative as proven causation.
An AI module lacks evaluations and failure modes.
A regulated-industry module discusses only UX and growth.
Principal+ is reduced to feature prioritization.
An industry module ignores product archetype.
Source marketing incentives are concealed.
Product Forge responsibilities are duplicated.
Proposed integrations are presented as implemented.
Adjacent repositories are modified.
Sensitive local information is copied into the Academy.
The final handbook contains unsupported factual claims.
A scenario rubric rewards vocabulary more than judgment.
The repo is mostly scaffolding rather than usable content.

## Gates

### Gate 1: Repository Integrity
- All required directories and files exist
- .gitignore is present and correct
- No secrets, credentials, or sensitive data in repository
- No binary artifacts or caches committed

### Gate 2: Schema Compliance
- All YAML files parse correctly
- All JSON files are valid JSON
- Source records validate against source schema
- Case records validate against case schema

### Gate 3: Source Integrity
- All source IDs are unique
- Referenced source IDs exist in registry
- No source marked as Tier E supports canonical claims
- Transcript statuses use allowed enum values
- Exact quotations have verifiable source locations

### Gate 4: Doctrine Integrity
- Every canonical claim has at least one qualifying source (Tier A or corroborated Tier B)
- Every disputed doctrine presents credible opposition
- Applicability conditions are stated for every principle
- Contradiction register includes both sides with evidence

### Gate 5: Content Quality
- Cases include causal-confidence fields
- AI module includes evaluation contracts and failure taxonomy
- Industry modules declare product archetype applicability
- Principal+ material goes beyond feature prioritization
- Handbook is coherent and useful (not generic filler)

### Gate 6: Ecosystem Integrity
- Product Forge integration is labelled current or proposed
- No adjacent repository was modified
- No Product Forge execution artifacts duplicated in Academy

### Gate 7: Link and Reference Integrity
- All internal markdown links resolve
- Cross-references between files are valid
- No broken references to source IDs or case IDs

### Gate 8: Test Quality
- Tests enforce meaningful doctrine, not just file existence
- No manual validation represented as passed unless actually performed
- Validation is reproducible via `python -m pytest -q`

## Pre-Commit Checklist

```bash
python -m pytest -q
python scripts/validate_academy.py
git diff --stat  # Review all changes
git status       # Confirm no unintended files
```
