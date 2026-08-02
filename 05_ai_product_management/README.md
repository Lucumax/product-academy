# Module 05: AI Product Management

**Status:** v0.1.0 — Initial bounded release
**Audience:** Senior PM through CPO
**Prerequisites:** Modules 00–04 (Orientation, Core Doctrine, Principal+, Business & GTM, Product Archetypes)

---

## Purpose

This module provides the frameworks, tools, and mental models that product leaders need to make real AI product decisions. It is NOT about prompt engineering, "vibe coding," demo-driven development, or chasing model benchmarks. It IS about:

1. Selecting AI-appropriate workflows (and knowing when AI is the wrong answer)
2. Designing evaluation contracts that define success and failure before you build
3. Understanding system performance vs model performance
4. Anticipating and governing AI-specific failure modes
5. Architecting agent systems with appropriate safety boundaries
6. Driving adoption in products where trust and reliability are existential
7. Governing AI products in a shifting regulatory landscape

## Module Structure

```
05_ai_product_management/
├── README.md                     ← This file
├── WORKFLOW_SELECTION.md         ← Selecting AI-appropriate workflows and use cases
├── EVALUATION_CONTRACTS.md       ← Defining success and failure before building
├── MODEL_VS_SYSTEM.md            ← System performance vs model performance
├── FAILURE_MODES.md              ← Comprehensive AI product failure taxonomy
├── GOVERNANCE.md                 ← AI product governance frameworks
├── AGENT_ARCHITECTURE.md         ← Agent product architecture and safety
├── ADOPTION.md                   ← User trust, organizational change, measuring success
└── TOOLS.md                      ← Templates, checklists, and filled examples
```

## Recommended Reading Order

### First Read (Sequential)

1. **WORKFLOW_SELECTION.md** — Start here. Before you write a single line of an evaluation contract, you need to know whether the problem even warrants AI. This file forces you to distinguish "AI can do this" from "AI should do this."

2. **EVALUATION_CONTRACTS.md** — Once you've identified a viable workflow, define success and failure. The evaluation contract is the single most important artifact in AI product management. It answers: "How will we know if this is working?" and "At what point do we roll it back?"

3. **FAILURE_MODES.md** — Before you ship, understand what can break. This taxonomy covers silent failures, distribution shift, prompt injection, hallucination, cascading agent failures, and more. Internalize these before they become incidents.

4. **MODEL_VS_SYSTEM.md** — The model is not the product. This file covers architecture, data, retrieval, inference economics, and the build-vs-buy decision for AI components.

5. **AGENT_ARCHITECTURE.md** — When agents add value, how to bound their authority, multi-agent coordination, human-in-the-loop patterns, and recovery strategies.

6. **GOVERNANCE.md** — The legal and ethical framework. Proportional governance, the EU AI Act, audit requirements, and organizational accountability structures.

7. **ADOPTION.md** — You've built it. Now how do you get users to trust it, measure its success, and maintain it over time?

8. **TOOLS.md** — Reference templates, filled examples, and decision frameworks you can adapt for your own products.

### Targeted Reading (For Specific Decisions)

- **"Should we build this AI feature?"** → WORKFLOW_SELECTION.md + TOOLS.md (AI use case assessment template)
- **"How do we evaluate this AI product?"** → EVALUATION_CONTRACTS.md + TOOLS.md (evaluation contract template)
- **"We had a bad AI output. What went wrong?"** → FAILURE_MODES.md (identify the failure category and mitigation)
- **"Which model should we use?"** → MODEL_VS_SYSTEM.md + TOOLS.md (model selection framework)
- **"How do agents fit into our product?"** → AGENT_ARCHITECTURE.md
- **"What compliance requirements apply?"** → GOVERNANCE.md
- **"Users don't trust our AI features."** → ADOPTION.md
- **"I need to write a decision memo for leadership."** → TOOLS.md (AI product decision memo template)

## Key Concepts Map

```
AI-as-a-feature vs AI-as-the-product
        │
        ▼
┌─────────────────────────────────┐
│    WORKFLOW SELECTION           │
│    • Value vs novelty           │
│    • When NOT to use AI         │
│    • Workflow-centric thinking  │
└───────────┬─────────────────────┘
            │
            ▼
┌─────────────────────────────────┐
│    EVALUATION CONTRACTS         │
│    • Target workflow            │
│    • Failure taxonomy           │
│    • Launch/rollback thresholds │
│    • Monitoring plan            │
└───────────┬─────────────────────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌────────────┐ ┌──────────────────┐
│  MODEL VS  │ │  FAILURE MODES   │
│  SYSTEM    │ │  • Silent        │
│  • Arch    │ │  • Distribution  │
│  • Data    │ │  • Hallucination │
│  • Build   │ │  • Cascading     │
│  vs Buy    │ │  • Feedback loop │
└─────┬──────┘ └────────┬─────────┘
      │                 │
      └────────┬────────┘
               │
               ▼
┌─────────────────────────────────┐
│    AGENT ARCHITECTURE           │
│    • Permission models          │
│    • Multi-agent coordination   │
│    • Human-in-the-loop          │
│    • Observability              │
└───────────┬─────────────────────┘
            │
    ┌───────┴───────┐
    │               │
    ▼               ▼
┌────────────┐ ┌──────────────────┐
│ GOVERNANCE │ │   ADOPTION       │
│ • Regulatory│ │  • Trust        │
│ • Oversight │ │  • Org change   │
│ • Audit     │ │  • Measurement  │
└────────────┘ └──────────────────┘
```

## What This Module Is NOT

- **NOT an ML engineering guide** — You won't learn to fine-tune models or write PyTorch code here. That's engineering territory. But you WILL learn what questions to ask your ML team and how to tell good answers from bad ones.
- **NOT a prompt engineering tutorial** — Prompting is an implementation detail, not a product strategy. This module treats prompting as one lever among many in the system design, not as the primary activity of an AI PM.
- **NOT a demo-to-production recipe** — Demos are easy. Products are hard. This module focuses on the hard parts: evaluation, failure modes, governance, and adoption.
- **NOT vendor-neutral advocacy** — This module does not promote any specific AI provider. Build-vs-buy frameworks are presented as decision tools, not as endorsements.

## Core Principles

These principles run through every file in this module:

### 1. AI is never the starting point

Start with the user problem, the workflow, the job to be done. AI is a solution technology, not a problem definition. If you can't describe the problem without mentioning AI, you don't understand the problem well enough yet.

### 2. The model is not the product

Model benchmarks (MMLU, HumanEval, etc.) measure model performance on academic tasks. They do not measure product value. A model with 95% accuracy on a benchmark can produce 0% useful outputs in your product. System design — data, retrieval, prompting, tool use, UI, human-in-the-loop — matters more than model selection 90% of the time.

### 3. Evaluation precedes engineering

Before your team writes code, you must define what success looks like and what failure looks like — in product terms, with severity weights, launch thresholds, and rollback thresholds. If you cannot articulate this, you are not ready to build.

### 4. Failure modes are product features

In traditional software, an outright bug is a failure. In AI products, probabilistic failure is the default state. Your product's competitive advantage comes from how you handle inevitable failures — graceful degradation, human escalation, transparency, recovery pathways.

### 5. Governance is a product advantage

Companies that treat AI governance as a checkbox exercise will be forced into corner-cutting, trust-eroding, retroactive-compliance scrambles. Companies that build governance into the product from day one will ship faster with higher user trust and fewer regulatory surprises.

### 6. Adoption is earned, not assumed

Users do not adopt AI features because they're "smarter." They adopt them because the features are reliable, transparent, and make their work better in ways they can verify. Overpromising and underdelivering (the AI industry's dominant pattern) destroys trust faster than having no AI features at all.

## How to Use This Module

### Individual Study

Read the files in the recommended order. At the end of each file, apply the frameworks to a product you're currently working on or have worked on in the past. Answer the questions in the "Practical Application" section of each file.

### Team Discussion

Each file includes discussion prompts. Use these in team meetings to align your organization on AI product decisions. The WORKFLOW_SELECTION.md discussion prompts are particularly useful for product portfolio reviews where someone has proposed an AI feature.

### Decision Support

When facing a specific AI product decision — build vs buy, launch readiness, incident response, governance setup — navigate to the relevant file and use the frameworks. The TOOLS.md templates can be copied and adapted for your decision memos.

### Reference

After reading the full module, use individual files as reference material. The FAILURE_MODES.md taxonomy is useful during incident reviews. The GOVERNANCE.md frameworks are useful when regulatory requirements change.

## Prerequisites

Before engaging with this module, you should have internalized:

1. **The product archetype framework** (Module 04) — AI products behave differently depending on whether they're workflow tools, platforms, APIs, etc. The governance and adoption considerations shift by archetype.

2. **The Principal+ decision framework** (Module 02) — AI investment decisions (build vs buy, make vs partner, ship vs delay) are allocation decisions with uncertainty. The Principal+ framework provides the scaffolding for making these calls.

3. **Business and GTM models** (Module 03) — AI products have unique GTM challenges: trust-based adoption curves, compliance-driven sales cycles, cost structures that don't match traditional software margins.

## Integration with Product Forge

When an AI product decision graduates from Academy analysis to execution:

1. The evaluation contract becomes the acceptance criteria for Product Forge work units
2. The failure mode taxonomy becomes the monitoring and alerting specification
3. The governance framework becomes the compliance checklist for the VSH quality gates
4. The adoption plan becomes the GTM requirements in the Product Forge brief

The Academy does not duplicate Product Forge execution. It provides the pre-execution frameworks that make execution faster and more rigorous.

## Quality Gates (from QUALITY_GATES.md)

This module is held to the following quality standards:

- **Gate 5 (Content Quality):** AI module includes evaluation contracts and failure taxonomy — satisfied by EVALUATION_CONTRACTS.md and FAILURE_MODES.md
- **Gate 3 (Source Integrity):** All claims supported by Tier A or corroborated Tier B sources
- **Gate 4 (Doctrine Integrity):** Applicability conditions stated for every principle
- **Gate 8 (Test Quality):** Content can be validated via automated tests where applicable

---

## Module Progress Tracking

| File | Status | Read | Applied | Discussed |
|------|--------|------|---------|-----------|
| WORKFLOW_SELECTION.md | Complete | [ ] | [ ] | [ ] |
| EVALUATION_CONTRACTS.md | Complete | [ ] | [ ] | [ ] |
| FAILURE_MODES.md | Complete | [ ] | [ ] | [ ] |
| MODEL_VS_SYSTEM.md | Complete | [ ] | [ ] | [ ] |
| AGENT_ARCHITECTURE.md | Complete | [ ] | [ ] | [ ] |
| GOVERNANCE.md | Complete | [ ] | [ ] | [ ] |
| ADOPTION.md | Complete | [ ] | [ ] | [ ] |
| TOOLS.md | Complete | [ ] | [ ] | [ ] |

---

## Version History

- **v0.1.0 (2026-08-01):** Initial bounded release. All eight content files present with substantive frameworks, examples, and templates. Evaluation contracts and failure taxonomy satisfy Quality Gate 5.
