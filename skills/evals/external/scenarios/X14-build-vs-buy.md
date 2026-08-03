# Scenario X14 — Build-versus-Buy Decision

**Domain:** Platform team. **Situation:** architecture/strategy decision.

## Context

A data-heavy SaaS ("Orchard") needs a workflow-automation capability for its enterprise
customers: customers want to define rules that trigger actions (e.g., "when a field changes,
notify X and update Y"). The engineering lead proposes building it in-house because the
company's own workflows depend on it. A vendor offers a mature embedded workflow engine with
a strong enterprise reference base, at a license cost equal to roughly one engineering
quarter.

The company's stated strategy is to differentiate on domain workflows, not on generic
automation plumbing. Building in-house would take 2–3 quarters of platform time and would
definitely be used by the product (the product's own workflow needs are already real).
Buying would ship customer-facing value faster but commits the company to a vendor's roadmap
for a capability it considers strategic.

## Inputs available (imperfect)

- Vendor product is mature, referenced, and integrates cleanly.
- In-house estimate: 2–3 quarters of platform time.
- Company strategy: differentiate on domain workflows, not generic plumbing.
- The product's own internal workflow need is real and current.
- No vendor-relationship or data-residency concerns identified yet.

## Ask

You have one page to recommend build, buy, or a hybrid, and what you would need to decide
confidently. State your reasoning.
