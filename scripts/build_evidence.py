#!/usr/bin/env python3
"""
Generate processed evidence artifacts into evidence/final/.

Consumes research/extracted_claims/claims_inventory.yaml and the source
registry to produce three artifacts:
  1. CLAIMS_LEDGER.md        - every extracted claim, its sources, strength
  2. SOURCE_EVIDENCE_STRENGTH.md - per-source evidence assessment
  3. CORROBORATION_MATRIX.md - which claims are corroborated by which sources

This is the "evidence/final" layer that makes the Academy's evidence-backed
claim verifiable rather than metadata-only.
"""

import sys
from collections import defaultdict
from pathlib import Path

try:
    import yaml
except ImportError:
    print("pyyaml required"); sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "evidence" / "final"
CLAIMS_FILE = ROOT / "research" / "extracted_claims" / "claims_inventory.yaml"
REGISTRY = ROOT / "sources" / "registry.yaml"


def load():
    claims = yaml.safe_load(CLAIMS_FILE.read_text(encoding="utf-8"))["claims"]
    registry = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))["sources"]
    source_by_id = {s["source_id"]: s for s in registry}
    return claims, source_by_id


def fmt_source(src):
    if not src:
        return "_unresolved_"
    tier = src.get("evidence_tier", "?")
    author = src.get("author", "")
    title = src.get("title", "")
    return f"**{src['source_id']}** (T{tier}) — {title}" + (f" — {author}" if author else "")


def gen_claims_ledger(claims, sources):
    lines = [
        "# Claims Ledger",
        "",
        "Processed evidence: every extracted claim, its supporting sources,",
        "evidence level, and contested status. Generated from",
        "`research/extracted_claims/claims_inventory.yaml`.",
        "",
        f"Total claims: {len(claims)}",
        "",
        "---",
        "",
    ]
    for i, c in enumerate(claims, 1):
        lines.append(f"## {c['claim_id']}: {c['statement']}")
        lines.append("")
        lines.append(f"- **Evidence level:** {c.get('evidence_level', '?')}")
        lines.append(f"- **Contested:** {c.get('contested', False)}")
        lines.append("- **Supporting sources:**")
        for sid in c.get("source_ids", []):
            lines.append(f"  - {fmt_source(sources.get(sid))}")
        if c.get("counter_claim_sources"):
            lines.append("- **Counter-claim sources:**")
            for sid in c["counter_claim_sources"]:
                lines.append(f"  - {fmt_source(sources.get(sid))}")
        if c.get("corroboration"):
            lines.append(f"- **Corroboration:** {c['corroboration']}")
        if c.get("notes"):
            lines.append(f"- **Notes:** {c['notes']}")
        if c.get("applicable_modules"):
            lines.append(f"- **Applicable modules:** {', '.join(c['applicable_modules'])}")
        lines.append("")
        if i != len(claims):
            lines.append("---")
            lines.append("")
    return "\n".join(lines)


def gen_source_strength(claims, sources):
    # Aggregate claim support by source
    used = defaultdict(lambda: {"support": 0, "counter": 0, "claims": []})
    for c in claims:
        for sid in c.get("source_ids", []):
            used[sid]["support"] += 1
            used[sid]["claims"].append(c["claim_id"])
        for sid in c.get("counter_claim_sources", []):
            used[sid]["counter"] += 1
            used[sid]["claims"].append(c["claim_id"])

    lines = [
        "# Source Evidence Strength",
        "",
        "Per-source assessment of how much canonical weight the Academy",
        "actually places on each source, derived from the claims ledger.",
        "",
        "Tier definitions: A = firsthand operator / official; B = credible practitioner;",
        "C = community; E = pending verification.",
        "",
        "| Source | Tier | Supports claims | Opposes claims | Assessment |",
        "|--------|------|-----------------|----------------|------------|",
    ]
    for sid in sorted(used):
        src = sources.get(sid)
        if not src:
            continue
        tier = src.get("evidence_tier", "?")
        support = used[sid]["support"]
        counter = used[sid]["counter"]
        if tier == "A" and support >= 2:
            assessment = "Anchor source — multiple canonical claims rest on it"
        elif tier == "A":
            assessment = "Firsthand but narrowly used"
        elif tier == "B" and support:
            assessment = "Corroborating source"
        else:
            assessment = "Context/counter source"
        lines.append(
            f"| {sid} | {tier} | {support} | {counter} | {assessment} |"
        )
    lines.extend([
        "",
        "## Notes",
        "",
        "- Only sources referenced by at least one claim are listed.",
        "- Tier A sources used by multiple claims are the Academy's evidential anchors.",
        "- Tier B/C/E sources provide corroboration or opposition, never anchor status alone.",
    ])
    return "\n".join(lines)


def gen_corroboration_matrix(claims):
    lines = [
        "# Corroboration Matrix",
        "",
        "Which claims are supported by multiple independent sources. A claim is",
        "'corroborated' when it has 2+ distinct supporting sources.",
        "",
        "| Claim | Statement | Supporting sources | Corroborated |",
        "|-------|-----------|--------------------|--------------|",
    ]
    for c in claims:
        sids = c.get("source_ids", [])
        corrob = len(sids) >= 2
        lines.append(
            f"| {c['claim_id']} | {c['statement'][:70]} | {len(sids)} | {'YES' if corrob else 'no'} |"
        )
    lines.extend([
        "",
        "## Uncorroborated claims (single-source)",
        "",
        "These rest on one source and should be treated as weaker doctrine:",
        "",
    ])
    single = [c for c in claims if len(c.get("source_ids", [])) < 2]
    if single:
        for c in single:
            lines.append(f"- **{c['claim_id']}** — {c['statement']}")
    else:
        lines.append("None.")
    return "\n".join(lines)


def main():
    claims, sources = load()
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "CLAIMS_LEDGER.md").write_text(gen_claims_ledger(claims, sources), encoding="utf-8")
    (OUT / "SOURCE_EVIDENCE_STRENGTH.md").write_text(gen_source_strength(claims, sources), encoding="utf-8")
    (OUT / "CORROBORATION_MATRIX.md").write_text(gen_corroboration_matrix(claims), encoding="utf-8")
    print(f"Wrote {len(claims)} claims into evidence/final/ (3 artifacts)")


if __name__ == "__main__":
    main()
