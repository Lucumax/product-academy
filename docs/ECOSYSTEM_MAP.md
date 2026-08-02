# Ecosystem Map

**Generated from:** Ecosystem Cartographer report (`evidence/agent_runs/ecosystem_cartographer.md`)
**Status:** Condensed reference — see cartographer report for full evidence trails.

---

## System 1: VSH Quality Fabric (vsh-v0.4)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Multi-agent engineering quality gates and lifecycle tools. Deterministic Python CLI for manifest-first software validation. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Agents\vsh-v0.4` |
| **Primary Objects** | Issue manifest schema, quality gates (7 total), critic review protocol, merge queue (dry-run), telemetry records (JSONL), 12 CLI commands |
| **Authority Boundary** | Owns: software quality gates, build checks. Does NOT own: research governance, sales strategy, portfolio prioritization, human approval. |
| **Reuse Candidates** | Manifest-first workflow pattern, critic review protocol, deterministic gate framework, 890-test quality benchmark |
| **Duplication Risks** | Must NOT duplicate: VSH CLI, build-specific gates, merge queue |
| **Integration Points** | Manifest-first pattern applicable to Academy learning-module manifests. Critic protocol applicable to peer review. |

---

## System 2: ops-hub

| Aspect | Detail |
|--------|--------|
| **Purpose** | Private operating system for shipping apps fast. Agent constitutions, skills, templates, playbooks, project briefs, decision logs, SME-JV pitch infrastructure. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Agents\ops-hub` |
| **Primary Objects** | Agent constitutions (AGENTS.md, CODEX.md), skill bundles (SKILL.md + `_authoring/` pattern), templates, project folders, ADR decisions, sprint allocator |
| **Authority Boundary** | Owns: initiative registration, prioritization, sequencing, tracking, stage status. Does NOT own: domain execution, gate overrides, product-level judgment. |
| **Reuse Candidates** | Agent constitution pattern, ADR-style decision logging, skill authoring pattern, playbook structure, sprint allocation formula |
| **Duplication Risks** | Must NOT duplicate: ops-hub repo itself, SME-JV pitch infrastructure, cockpit routing rules |
| **Integration Points** | Academy should register as ops-hub initiative. Curriculum modules should follow skill-authoring patterns. |

---

## System 3: kernel-spec

| Aspect | Detail |
|--------|--------|
| **Purpose** | Cross-cutting kernel specification for Walter's Domain OS portfolio. Universal primitives every Domain OS must conform to. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Agents\kernel-spec` |
| **Primary Objects** | Manifest schema (30 required fields), portfolio registry (12 entries), telemetry schema (29 required fields), run-folder convention, approval vocabulary (5 statuses, 13 human-only actions), evidence contract |
| **Authority Boundary** | Owns: cross-cutting kernel primitives (manifest shape, telemetry, run-folder, approval vocabulary). Does NOT own: domain acceptance criteria, implementation, build execution. |
| **Reuse Candidates** | Manifest schema template, run-folder convention, telemetry schema, approval vocabulary, evidence contract, portfolio registry pattern |
| **Duplication Risks** | Must NOT duplicate: kernel specification itself, portfolio registry of existing systems |
| **Integration Points** | Academy should adopt run-folder convention for student work. Course manifests should validate against derivative of kernel manifest schema. |

---

## System 4: Hermes

| Aspect | Detail |
|--------|--------|
| **Purpose** | Bounded campaign-orchestration runtime. Decomposes objectives into tasks, manages execution state, reports results. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Hermes` |
| **Primary Objects** | STATE.json, LEDGER.jsonl, packet generation, state machine (9 states), 5 CLI verbs, lockfile, reconciliation engine |
| **Authority Boundary** | Owns: campaign/task decomposition, queue/execution state. Does NOT own: portfolio prioritization, authorization/budgets, software release, human approval, autonomous dispatch. |
| **Reuse Candidates** | State machine pattern, append-only ledger for audit trail, packet decomposition pattern, reconciliation pattern, lockfile pattern |
| **Duplication Risks** | Must NOT duplicate: Hermes runtime, packet schema |
| **Integration Points** | State machine and ledger patterns applicable to cohort progress tracking and assignment orchestration. |

---

## System 5: agent-skills (Addy Osmani)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Production-grade engineering skills for AI coding agents. 24 skill modules across 8 slash commands covering full development lifecycle. |
| **Path** | `C:\Walter\100 day plan\AI Agents\agent-skills` |
| **Primary Objects** | 8 slash commands, 24 skills, CLI installer (`npx skills add`), plugin integrations (70+ agents), 3-tier CI eval framework |
| **Authority Boundary** | Owns: engineering skill definitions for software development. Does NOT own: product leadership curriculum, domain-specific pedagogy. |
| **Reuse Candidates** | SKILL.md format and `_authoring/` pattern, slash-command pattern, idea-refine skill, source-driven-development pattern, doubt-driven-development pattern |
| **Duplication Risks** | Must NOT duplicate: technical engineering skills, CLI distribution mechanism |
| **Integration Points** | Academy should author product-leadership skills following SKILL.md pattern. Slash-command pattern maps to `/product-brief`, `/market-analysis`, `/roadmap`, etc. |

---

## System 6: InfraPrep

| Aspect | Detail |
|--------|--------|
| **Purpose** | Launch pack for testing a Managed Agentic Infrastructure Preparation Facility. Beachhead in energy/climate infrastructure in Latin America/Caribbean. |
| **Path** | `C:\Walter\100 day plan\AI Agents\InfraPrep` |
| **Primary Objects** | Stage gates (0-7), launch sequence (10-step JSON), portfolio routing table, 5 JSON manifests, acceptance tests (30 criteria), governance documents |
| **Authority Boundary** | Owns: domain preparation workflow execution. Does NOT own: portfolio prioritization, authorization, buyer discovery, software builds, orchestration. |
| **Reuse Candidates** | Stage-gate framework, go/no-go scorecard pattern, portfolio routing table, independent review requirement, five-buyer-confirmation threshold |
| **Duplication Risks** | Must NOT duplicate: infrastructure preparation workflow, PAL authorization model, launch pack |
| **Integration Points** | Stage-gate framework is teachable pattern for product investment gating. Academy could serve as Product Forge "project" for PMF validation. |

---

## System 7: Agents-front-office (Legacy + PAL)

| Aspect | Detail |
|--------|--------|
| **Purpose** | Older consolidated snapshot of agent portfolio front-office. Contains copies of subsystems PLUS full PAL implementation and VSH roadmaps. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Agents-front-office` |
| **Primary Objects** | PAL (238 tests, Fastify REST API, SQLite, hash-chained audit ledger), VSH roadmaps (v0.30-v0.55), duplicate subsystems (vsh-v0.4, ops-hub, kernel-spec) |
| **Authority Boundary** | Owns: PAL control plane (authorization, budgets, permissions). Canonical vsh-v0.4, ops-hub, kernel-spec live in `Agents/`. |
| **Reuse Candidates** | PAL audit ledger pattern, autonomy-level policy engine (A0-A2), PAL threat model, VSH strategic roadmaps |
| **Duplication Risks** | Must NOT duplicate: PAL implementation, older subsystem copies, branch strategy |
| **Integration Points** | Hash-chained audit ledger applicable to secure grade/progress tracking. VSH roadmaps are real-world product evolution case study. |

---

## System 8: Research for TIAA

| Aspect | Detail |
|--------|--------|
| **Purpose** | Research preparation for a TIAA Sr. Director interview. 6-agent swarm research operation. |
| **Path** | `C:\Walter\Research for TIAA` |
| **Primary Objects** | MASTER_RESEARCH_PLAN.md, INTERVIEW_PREP.md, research reports, market data ($434.6B DC managed account AUM) |
| **Authority Boundary** | Owns: interview research for specific job application. Does NOT own: any operational system. |
| **Status** | Complete. 6 research streams verified. |
| **Reuse Candidates** | 6-agent swarm research methodology, competitive landscape analysis template, evidence classification from kernel-spec |
| **Integration Points** | Research -> Product Forge -> VSH pipeline demonstrates end-to-end product creation workflow. |

---

## System 9: Product Forge

| Aspect | Detail |
|--------|--------|
| **Purpose** | File-first AI-assisted Product Operating System. Turns messy product context into evidence-backed briefs, hypotheses, backlogs, and execution-ready work packets. |
| **Path** | `C:\Walter\100 day plan\AI Agents\Product Forge\product_forge_v0_1` |
| **Primary Objects** | Product brief, claim classification (5 types), sources inventory, hypotheses with confidence tracking, journey maps, scored backlog (8-field scoring), 12 JSON schemas, VSH export bridge |
| **Authority Boundary** | Owns: product discovery, buyer/problem validation, value hypothesis, delivery model, pilot scope, pricing. Does NOT own: agent orchestration, execution, dashboard/SaaS UI. |
| **Reuse Candidates** | Claim classification system, product brief template, evidence discipline, Decision Card format, validation plan pattern, scored backlog methodology |
| **Duplication Risks** | Must NOT duplicate: Product Forge package, VSH export bridge |
| **Integration Points** | Academy should use Product Forge as teaching tool and methodology reference. Claim classification system should be Day 1 module. |

---

## System 10: MIT

| Aspect | Detail |
|--------|--------|
| **Purpose** | MIT AI/LLM course materials repository. Lecture recordings, transcripts, team projects, adjudicated course learnings. |
| **Path** | `C:\Walter\100 day plan\AI Agents\MIT` |
| **Primary Objects** | 13 lecture sessions, course materials, 8 adjudication documents, team projects, readings (AI Index Report 2026, Agentic AI Use Cases) |
| **Authority Boundary** | Owns: educational consumption and personal learning. Does NOT own: any operational system. |
| **Reuse Candidates** | Adjudication methodology, course project recommendation framework, research idea triage, claims/evidence audit approach |
| **Duplication Risks** | Must NOT duplicate: MIT course content, lecture recordings/transcripts |
| **Integration Points** | Adjudication methodology should be adopted as Academy's curriculum quality assurance process. |

---

## Cross-Cutting Observations

### Key Warnings
1. **Duplication**: `Agents/` and `Agents-front-office/` have substantial overlap (vsh-v0.4, ops-hub, kernel-spec). `Agents/` is canonical.
2. **PAL location**: Registry says PAL is in `Agents/portfolio-autonomy-layer/`; actual code is in `Agents-front-office/portfolio-autonomy-layer/`.
3. **Isolated systems**: Hermes (no remote), Product Forge (no git), InfraPrep (launch pack, not OS), agent-skills (external dependency).
4. **Stale folders**: `Agents-front-office/master` marked historical; Hermes subdirectories explicitly non-runtime.
