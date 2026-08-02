# Ecosystem Cartographer Report — Boundary Analysis of Adjacent Repositories

**Generated:** 2026-08-01
**Author:** Ecosystem Cartographer Agent
**Canonical Output:** `C:\Walter\100 day plan\AI Agents\product-leadership-academy\evidence\agent_runs\ecosystem_cartographer.md`
**Status:** READ-ONLY reconnaissance — no files were mutated.

---

## Scope

This report inspects 10 adjacent repositories/locations relative to the Product Leadership Academy, identifying purpose, boundaries, reusable assets, risks of duplication, and integration points.

---

## SYSTEM 1: VSH Quality Fabric (vsh-v0.4)

### 1. Purpose
Multi-agent engineering quality gates and lifecycle tools. A deterministic Python CLI fabric for manifest-first VSH (Virtual Software House) work. Provides JSON schema validation, allowed-files enforcement, dependency audits, validation runners, mutation/evals, critic review, merge-queue dry-run, telemetry, and agent-run logging.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Agents\vsh-v0.4`

Note: A near-identical copy exists at `C:\Walter\100 day plan\AI Agents\Agents-front-office\vsh-v0.4`. The `Agents/` version is presumed canonical (part of the ops-hub-agent-os monorepo).

### 3. Primary Objects
- **Issue Manifest** — A machine-checkable JSON work unit (`quality/schema/issue-manifest.schema.json`)
- **Quality Gates** — Manifest check, allowed-files (fnmatch globs), dependency check, validation runner (subprocess with expected exit codes), mutation/evals, critic review
- **Critic Review** — Read-only QA verdict (APPROVE or CHANGES REQUESTED) from a different model than the worker
- **Merge Queue** — Dry-run only; human conductor approval required
- **Telemetry Record** — JSONL agent-run telemetry
- **Failure Pattern Tracker** — JSONL failure log
- **12 CLI Commands** — `check-manifest`, `check-allowed-files`, `check-dependencies`, `run-validation`, `run-mutation-evals`, `generate-merge-packet`, `log-agent-run`, `merge-queue`, and more

### 4. Inputs
- Issue manifest JSON (schema-validated)
- Code diffs and changed-file lists
- Subprocess validation commands
- Dependency file change lists

### 5. Outputs
- Gate pass/fail results (JSON)
- Validation reports
- Critic verdicts (structured markdown)
- Merge packets
- Telemetry records (JSONL)
- Execution packets

### 6. Authority Boundary
- **Owns:** Software quality gates, implementation validation, deterministic build checks
- **Does NOT own:** Research governance, sales strategy, project-finance judgment, portfolio prioritization, human approval (Walter)

### 7. What the Academy May Reuse
- Manifest-first workflow pattern (machine-checkable work units before execution)
- Critic review protocol (different-model read-only QA)
- Merge-queue discipline (dry-run only, human approval required)
- Deterministic gate framework (schemas, allowed-files, dependency audits)
- 890-test pytest suite as a quality benchmark

### 8. What the Academy Must NOT Duplicate
- The VSH CLI itself (`vsh_quality` package)
- Software-build-specific gates (not applicable to product leadership pedagogy)
- Merge queue (software-only concern)

### 9. Potential Integration Point
The manifest-first, evidence-disciplined workflow pattern is directly applicable to Academy curricula: each learning module could be a manifest; each assignment a gate. The critic protocol is applicable to peer review. Telemetry patterns could inform learning analytics.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README, AGENTS.md, pyproject.toml, manifest schema, CLI docs, OPUS_HANDOVER.md, portfolio-registry.json (890 tests, 34 test files) all read and cross-referenced.

---

## SYSTEM 2: ops-hub (Agents/ops-hub)

### 1. Purpose
Private operating system for shipping apps fast and productizing AI services for SMEs. A single repo housing agent constitutions, skills, templates, playbooks, project briefs, decision logs, and SME-JV pitch infrastructure. Serves as source of truth for *how we work*, separate from app repos.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Agents\ops-hub`

Note: A near-identical but diverged copy exists at `C:\Walter\100 day plan\AI Agents\Agents-front-office\ops-hub`. The `Agents/ops-hub` version is the active one (opencode-focused, CODEX.md present). The `Agents-front-office/ops-hub` version is legacy (Claude Code-focused, CLAUDE.md present, no CODEX.md).

### 3. Primary Objects
- **Agent Constitutions** — AGENTS.md (universal), CODEX.md (Codex CLI orientation), CLAUDE.md, KIMI.md, GEMINI.md
- **Skills** — Reusable SKILL.md capability bundles with `_authoring/` master pattern
- **Templates** — Product briefs, GitHub issues, SME proposals
- **Projects** — One folder per active project with brief + app repo link
- **Playbooks** — Triad workflow, token economics, brand voice
- **Decisions** — ADR-style architectural and business decisions
- **Pitch** — SME-JV positioning, pricing tiers, discovery scripts
- **n8n** — Workflow specs for n8n engineer
- **Sprint Allocator** — Primary runtime component (formula v1.0, 25 AC)

### 4. Inputs
- Project briefs
- Agent constitutions and role specifications
- Business decisions requiring ADR logging

### 5. Outputs
- Portfolio records, current gate, approved next actions
- Sprint allocations
- Evidence links, budget consumption status

### 6. Authority Boundary
- **Owns:** Initiative registration, prioritization, sequencing, tracking, stage status, resource assignment, dependency tracking, decision history
- **Does NOT own:** Domain work execution, gate overrides, product-level judgment (Walter owns)

### 7. What the Academy May Reuse
- Universal agent constitution pattern (AGENTS.md as highest-priority rule file)
- ADR-style decision logging (`/decisions/`)
- Skill authoring pattern (`_authoring/` master pattern for SKILL.md)
- Playbook structure for operational workflows
- Sprint allocation formula (v1.0)

### 8. What the Academy Must NOT Duplicate
- The ops-hub repo itself (it is the portfolio control tower)
- SME-JV pitch infrastructure (commercial, not pedagogical)
- Codex/Claude/Kimi/Gemini cockpit routing rules

### 9. Potential Integration Point
The Academy should register itself as an initiative in ops-hub for portfolio tracking. The Academy`s curriculum modules should follow the skill-authoring patterns established here.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README, AGENTS.md, BOOTSTRAP.md, CODEX.md, directory structure all read. Portfolio-registry.json confirms 25 tests, all passing.


---

## SYSTEM 3: kernel-spec

### 1. Purpose
The cross-cutting kernel specification for Walter`s Domain OS portfolio. Defines the universal primitives that every Domain OS must conform to: manifest schema, portfolio registry, telemetry schema, run-folder convention, approval vocabulary, and evidence contract.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Agents\kernel-spec`

Note: A duplicate exists at `C:\Walter\100 day plan\AI Agents\Agents-front-office\kernel-spec`. The `Agents/` version is canonical (tagged `kernel-spec-v0.1.0`, fresh-clone verified).

### 3. Primary Objects
- **Manifest Schema** (`manifest.schema.json`) — v0.1 task contract (scope, gates, artifacts, model routing, approvals, risk, telemetry requirements). 30 required fields.
- **Portfolio Registry** (`portfolio-registry.json` + schema) — Canonical machine-readable registry of every component in the portfolio. 12 entries.
- **Telemetry Schema** (`telemetry.schema.json`) — Run telemetry record for file-based audit and dashboard ingestion. 29 required fields.
- **Run-Folder Convention** — `runs/<YYYY-MM-DD>/<run_id>/` with required files (manifest.json, prompt.md, gate-results.json, telemetry.json, approval-record.json, critic-review.md, final-packet.md)
- **Approval Vocabulary** — 5 statuses (`not_required`, `pending`, `approved`, `rejected`, `revoked`), 13 human-only actions
- **Evidence Contract** — Schema, design memo, validation script, track-A report

### 4. Inputs
- Task manifests (validated against manifest.schema.json)
- Telemetry records (validated against telemetry.schema.json)
- Portfolio entries

### 5. Outputs
- Validated manifests and telemetry
- Run folders conforming to convention
- Portfolio registry reports
- Approval records

### 6. Authority Boundary
- **Owns:** Cross-cutting kernel primitives (manifest shape, telemetry shape, run-folder shape, approval vocabulary, evidence contract)
- **Does NOT own:** Domain-specific acceptance criteria, implementation, build execution

### 7. What the Academy May Reuse
- **Manifest schema** — Directly applicable as a template for Academy learning-module manifests
- **Run-folder convention** — Applicable to Academy student project folders and evidence collection
- **Telemetry schema** — Could inform learning-progress tracking
- **Approval vocabulary** — Applicable to Academy submission/review workflow
- **Evidence contract** — Directly applicable to Academy evidence-collection standards
- **Portfolio registry pattern** — Could be used to register Academy modules

### 8. What the Academy Must NOT Duplicate
- The kernel specification itself (it is the normative reference)
- Portfolio registry of existing systems (Academy is a consumer, not a maintainer)

### 9. Potential Integration Point
The Academy should adopt the kernel run-folder convention for student work. Academy course manifests should validate against a derivative of the kernel manifest schema. The telemetry schema should inform learning-progress data collection.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — manifest.schema.json (451 lines), portfolio-registry.json (304 lines), portfolio-registry.schema.json (179 lines), telemetry.schema.json (250 lines), run-folder-convention.md, approval.vocabulary.md, evidence-contract/README.md all read. 42 tests, all pass, fresh-clone verified.

---

## SYSTEM 4: Hermes

### 1. Purpose
A bounded campaign-orchestration runtime. Decomposes objectives into tasks, manages execution state, and reports results. Phase 1 establishes core state infrastructure: init, enqueue, status, reconcile, and packet generation.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Hermes`

No duplicate exists. Standalone repository with no GitHub remote.

### 3. Primary Objects
- **STATE.json** — Durable execution state (atomic reads/writes)
- **LEDGER.jsonl** — Append-only JSONL event log (replay for resumability)
- **Packet** — Morning/resume task packets (decomposed objectives into tasks)
- **State Machine** — QUEUED -> AUTHORIZED -> DISPATCHED -> HEARTBEAT_OBSERVED -> COMPLETED_VERIFIED / COMPLETED_UNVERIFIED / FAILED / ESCALATED / STATE_UNKNOWN_PRESUMED_DEAD / CHECKPOINT
- **5 CLI Verbs** — `init`, `enqueue`, `status`, `reconcile`, `packet`
- **Lockfile** — Exclusive runtime lock with stale detection
- **Reconciliation** — PID/artifact/git reconciliation

### 4. Inputs
- Packet JSON (task definitions)
- Objectives (for decomposition)
- State directory specification

### 5. Outputs
- Morning packets
- State transitions and status reports
- Reconciliation results
- Evidence collection coordination

### 6. Authority Boundary
- **Owns:** Campaign/task decomposition, queue and execution state, task transitions, retries (max_remediation_rounds), durable progress, resumability, escalation state tracking
- **Does NOT own:** Portfolio prioritization (Ops Hub), authorization/budgets/permissions (PAL), software release judgment (VSH), irreversible human approval (Walter), autonomous dispatch (Phase 2, not started), network communication

### 7. What the Academy May Reuse
- State machine pattern (explicit transitions with ledger replay for resumability)
- Append-only ledger for audit trail
- Packet decomposition pattern (objective -> tasks)
- Reconciliation pattern (PID/artifact/git checks)
- Lockfile pattern for exclusive access

### 8. What the Academy Must NOT Duplicate
- The Hermes runtime itself (campaign orchestration, not learning management)
- Packet schema (domain-specific to task execution)

### 9. Potential Integration Point
If the Academy ever requires campaign-style orchestration (e.g., cohort progress tracking across multiple students/assignments), Hermes` state machine and ledger patterns are directly applicable. The packet-generation pattern could inform assignment-generation workflows.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README, AGENTS.md, ARCHITECTURE.md, REPOSITORY_MANIFEST.md, PHASE1_VALIDATION_REPORT.md, PAL_INTEGRATION_CONTRACT_DRAFT.md all read. Cross-referenced with portfolio-registry.json (125 tests, all pass). Source code layout confirmed (7 source files, 14 test files).


---

## SYSTEM 5: agent-skills (Addy Osmani)

### 1. Purpose
Production-grade engineering skills for AI coding agents. 24 skill modules across 8 slash commands covering the full development lifecycle: DEFINE -> PLAN -> BUILD -> VERIFY -> REVIEW -> SHIP.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\agent-skills`

External open-source project (MIT license) by Addy Osmani. Consumed as a dependency, not forked.

### 3. Primary Objects
- **8 Slash Commands** — `/spec`, `/plan`, `/build`, `/test`, `/review`, `/webperf`, `/code-simplify`, `/ship`
- **24 Skills** — api-and-interface-design, browser-testing-with-devtools, ci-cd-and-automation, code-review-and-quality, code-simplification, context-engineering, debugging-and-error-recovery, deprecation-and-migration, documentation-and-adrs, doubt-driven-development, frontend-ui-engineering, git-workflow-and-versioning, idea-refine, incremental-implementation, interview-me, observability-and-instrumentation, performance-optimization, planning-and-task-breakdown, security-and-hardening, shipping-and-launch, source-driven-development, spec-driven-development, test-driven-development, using-agent-skills
- **CLI** — `npx skills add addyosmani/agent-skills`
- **Plugin Integrations** — Claude Code marketplace, Cursor rules, Antigravity CLI, Codex, Copilot, Cline (70+ agents)
- **Evals** — 3-tier CI eval framework, 24 automated tests

### 4. Inputs
- `npx skills` CLI commands
- Plugin marketplace install requests
- Manual SKILL.md file copies

### 5. Outputs
- Installed SKILL.md bundles for target IDEs/agents
- Agent behavior modifications (rules in agent context windows)

### 6. Authority Boundary
- **Owns:** Engineering skill definitions and agent behavior specifications for software development lifecycle
- **Does NOT own:** Product leadership curriculum, domain-specific pedagogy (this is about how to build software, not how to lead product)

### 7. What the Academy May Reuse
- **Skill authoring pattern** — The SKILL.md format and `_authoring/` master pattern (also adopted by ops-hub) as a template for Academy module authoring
- **Slash-command pattern** — `/spec`, `/plan`, `/build` mapped to product leadership equivalents (`/product-brief`, `/market-analysis`, `/roadmap`)
- **Idea-refine skill** — Methodology for requirements interrogation, directly applicable to product discovery teaching
- **Interview-me skill** — Requirements interrogation, one question at a time
- **Source-driven-development** — Evidence-first pattern, applicable to product decision-making
- **Doubt-driven-development** — Inversion pattern for questioning assumptions

### 8. What the Academy Must NOT Duplicate
- The technical engineering skills (code-review, CI/CD, frontend-engineering, etc.) — these are for software builders, not product leaders
- The `npx skills` CLI distribution mechanism

### 9. Potential Integration Point
The Academy should author its own skills following the same SKILL.md pattern, installable via the same `npx skills` CLI. Product-leadership-specific skill modules can coexist alongside engineering skills. The slash-command pattern (`/product-brief`, `/market-analysis`, `/roadmap`, `/stakeholder-map`, `/decision-card`) maps cleanly.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README.md (379 lines), skills/ directory (24 subdirectories), CLI integration docs, plugin.json, CONTRIBUTING.md all read. Portfolio-registry.json confirms external dependency status, 24 tests, CI present.

---

## SYSTEM 6: InfraPrep

### 1. Purpose
A launch pack for a bounded initiative to test a Managed Agentic Infrastructure Preparation Facility. The beachhead domain is early-stage energy and climate infrastructure pipeline preparation in Latin America and the Caribbean. NOT a Domain OS yet — becomes one only after Gate 5 passes on 25+ real projects.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\InfraPrep`

No duplicate exists.

### 3. Primary Objects
- **Stage Gates (0-7)** — Portfolio Fit, Buyer/Problem Proof, Benchmark Design, Technical/Domain Proof, Paid Pilot Proof, Renewal/Repeatability, Domain OS Designation
- **Launch Sequence** — 10-step JSON specifying owner, action, and gate for each step
- **Portfolio Routing** — Explicit mapping of which system owns what (Ops Hub, PAL, Product Forge, VSH, Hermes, Outreach OS, Claude, Walter)
- **Manifests** — 5 JSON manifests (launch_sequence, ops_hub_initiative, pal_authorization, product_forge_brief, vsh_mvp_issue)
- **Validation** — Acceptance tests (governance, evidence, numbers, domain, product, security)
- **Governance** — Decision rights, portfolio routing, risk policy
- **Gates** — Stage gates, go/no-go scorecard, goals and OKRs

### 4. Inputs
- Unstructured infrastructure project pipelines
- Hermes orchestration commands
- PAL authorization for each stage

### 5. Outputs
- Evidence-backed advance/hold/redesign/stop recommendations
- Buyer maps, interview targets, interview scripts
- Benchmark designs and expert rubrics
- Decision packets after each gate
- (After Gate 5) A formal Domain OS

### 6. Authority Boundary
- **Owns:** Domain preparation workflow execution (before Gate 5)
- **Does NOT own:** Portfolio prioritization (Ops Hub), authorization (PAL), buyer discovery (Product Forge), software builds (VSH), orchestration (Hermes), irreversible approval (Walter)

### 7. What the Academy May Reuse
- **Stage-gate framework** — The 0-7 gate progression with explicit evidence requirements for each gate is a model for Academy course progression gates
- **Go/no-go scorecard pattern** — Applicable to Academy assessment rubrics
- **Portfolio routing table** — Clean boundary specification between systems
- **Independent review requirement** — Every artifact reviewed by a different model/role than the author
- **Acceptance test checklist format** — Governance, evidence, numbers, domain, product, security categories
- **Five-buyer-confirmation threshold** — Evidence standard for problem proof (applicable to product discovery teaching)

### 8. What the Academy Must NOT Duplicate
- The infrastructure preparation workflow (domain-specific to energy/climate infrastructure)
- The PAL authorization model (owned by PAL)
- The launch pack itself (operational, not pedagogical)

### 9. Potential Integration Point
The Academy can serve as a Product Forge "project" — applying the same buyer/problem discovery methodology to validate the Academy`s own product-market fit. The stage-gate framework is a teachable pattern for product leadership (how to gate product investments).

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README, HANDOFF_TO_HERMES.md, PORTFOLIO_ROUTING.md, STAGE_GATES.md, launch_sequence.json, ACCEPTANCE_TESTS.md, DECISION_RIGHTS.md, RISK_POLICY.md, GO_NO_GO_SCORECARD.md all read. Portfolio-registry.json confirms IPF-001, Gate 0 PROCEED.


---

## SYSTEM 7: Agents-front-office

### 1. Purpose
An older, consolidated snapshot of the full agent portfolio front-office. Contains copies of vsh-v0.4, ops-hub, kernel-spec, PLUS the full PAL (Portfolio Autonomy Layer) implementation and VSH roadmaps from v0.30 to v0.55. Appears to be a preserved working directory from before the opencode transition.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Agents-front-office`

### 3. Primary Objects
- **Duplicate subsystems** — vsh-v0.4/, ops-hub/, kernel-spec/ (older versions of the subsystems in Agents/)
- **PAL (Portfolio Autonomy Layer)** — Full implementation at `portfolio-autonomy-layer/`. TypeScript, 238 vitest tests, Fastify REST API, SQLite (sql.js), append-only hash-chained audit ledger, autonomy-level policy engine (A0-A2), mock Hermes adapter. Slice 0 verified. Slice 1 partially implemented.
- **VSH Roadmaps** — Extensive strategic documents: v0.30 through v0.55 (Portfolio OS, Token Allocation OS, Routing, Visual Doctrine)
- **Projects** — directcallhomes/
- **Architecture** — june-2026-reflections, portfolio-consolidation-review
- **Branch Strategy** — main is canonical, master is historical/stale, m1-vsh-factory-v1 is milestone lineage

### 4. Inputs
- Agent constitutions (CLAUDE.md primary)
- Project briefs
- Claude Code/Sonnet as default cockpit

### 5. Outputs
- PAL: task queues, approval services, policy enforcement, audit logging, budget management
- Ops Hub: initiative tracking, sprint planning

### 6. Authority Boundary
- **Owns:** PAL control plane (authorization, budgets, permissions, policy, approval boundaries). This is the ONLY location with the PAL implementation.
- **Does NOT own:** The canonical versions of vsh-v0.4, ops-hub, and kernel-spec (those live in Agents/)

### 7. What the Academy May Reuse
- **PAL audit ledger pattern** — Append-only, hash-chained, cryptographic integrity verification — applicable to Academy grade/progress recording
- **PAL autonomy-level policy engine** — A0-A2 levels with default deny — applicable to Academy access control
- **PAL threat model** — Security analysis pattern
- **VSH Roadmaps** — Strategic planning methodology from v0.21 through v0.55, demonstrating product evolution thinking

### 8. What the Academy Must NOT Duplicate
- The PAL implementation itself (portfolio control plane)
- The older subsidiary copies of vsh-v0.4, ops-hub, kernel-spec (use canonical versions in Agents/)
- The branch strategy (repo-specific)

### 9. Potential Integration Point
PAL`s hash-chained audit ledger pattern is directly applicable to secure grade/progress tracking. The autonomy-level policy engine could model Academy role-based access (student, reviewer, instructor, admin). The VSH roadmaps are a real-world case study in product evolution strategy.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README, portfolio-autonomy-layer/README.md, VSH_ROADMAP_v0_50_PORTFOLIO_OS.md (2980 lines), VSH_ROADMAP_v0_40.md, architecture/june-2026-reflections, OPENCODE_CLEANUP_BRIEF.md, SPRINT_P0_PROMPT.md all read. Portfolio-registry.json confirms PAL: 238 tests, TypeScript, Slice 0 verified.

---

## SYSTEM 8: Research for TIAA

### 1. Purpose
Research preparation for a TIAA Sr. Director, Accumulation Advice Product Management interview. A 6-agent swarm research operation covering managed accounts competitive landscape, market data, participant behavior, regulatory environment, and digital advice technology.

### 2. Canonical Path
`C:\Walter\Research for TIAA`

Not part of the AI Agents portfolio. A separate research workspace.

### 3. Primary Objects
- **MASTER_RESEARCH_PLAN.md** — Consolidated findings from 6 research streams (259 lines). Verified market data, competitive landscape, participant behavior, regulatory analysis.
- **INTERVIEW_PREP.md** — Interview preparation
- **RESEARCH_PLAN.md** — Original research plan
- **PROCESS.md** — Research process documentation
- **Reports** — Generated research reports
- **Audio** — Interview/training recordings
- **ChatGPT Prep** — AI-assisted preparation materials

### 4. Inputs
- Public market data (Cerulli, NEPC, Morningstar, EBRI, Vanguard, TIAA Institute)
- Competitive intelligence on managed account providers

### 5. Outputs
- Research reports
- Interview preparation materials
- Market sizing data ($434.6B DC managed account AUM)
- Competitive landscape analysis (EFE #1 at 45% market share, Empower, Morningstar, Fidelity, Alight, Vanguard, TIAA)

### 6. Authority Boundary
- **Owns:** Interview research and preparation for a specific job application
- **Does NOT own:** Any operational system or ongoing product

### 7. What the Academy May Reuse
- **6-agent swarm research methodology** — Teachable pattern for product research
- **Competitive landscape analysis template** — Structured market intelligence gathering
- **Evidence classification from kernel-spec** — confirmed_public_fact, source_backed_inference, hypothesis_to_validate
- **The TIAA public research itself** — Serves as a complete example of product-intelligence research that was used by Product Forge (`example_tiaa_public_product_intelligence`)

### 8. What the Academy Must NOT Duplicate
- The specific TIAA interview content (private, job-specific)
- The TIAA competitive analysis as a standalone product

### 9. Potential Integration Point
The complete research -> Product Forge -> VSH pipeline (TIAA research -> Product Forge example project -> VSH manifest export) demonstrates the end-to-end product creation workflow and should be featured as an Academy case study.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — MASTER_RESEARCH_PLAN.md (259 lines), directory listing (12 entries) all read. Cross-referenced with Product Forge example project.


---

## SYSTEM 9: Product Forge

### 1. Purpose
A file-first AI-assisted Product Operating System that turns messy product context into evidence-backed product briefs, UX hypotheses, prioritized backlogs, and execution-ready work packets. Designed for senior operators, product strategists, consultants, and AI-enabled builders in complex or regulated domains.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\Product Forge\product_forge_v0_1`

Note: NOT a git repository. Portability is blocked.

### 3. Primary Objects
- **Product Brief** — Structured intake and product definition
- **Claims** — Five classifications: confirmed_public_fact, source_backed_inference, hypothesis_to_validate, private_strategy, unsafe_claim
- **Sources** — Structured source inventory with provenance
- **Hypotheses** — Validation plans with before/after confidence
- **Journey Maps** — With emotion, friction_intensity, trust_barrier, decision_burden, moment_of_truth, compliance_sensitivity
- **Epics & Stories** — Scored backlog with impact, confidence, effort, risk, leverage, urgency, evidence_strength, priority_score
- **Work Packets** — Execution-ready, VSH-compatible
- **Decision Card** — One-screen verdict artifact (v0.2)
- **12 JSON Schemas** — claim, decision_card, epic, hypothesis, journey_map, project_state, risk, source, sprint, story, validation_plan, work_packet
- **VSH Export Bridge** — `scripts/export_vsh_manifest.js` converts work packets to VSH issue manifests

### 4. Inputs
- Project context (messy, unstructured)
- Competitive intelligence
- Market data
- Source materials

### 5. Outputs
- Product briefs
- Evidence registers
- User/stakeholder maps
- Journey maps with friction hypotheses
- Prioritized, scored backlogs
- UX and risk critiques
- VSH-compatible execution work packets
- Decision cards
- External-safe and internal-max-automation packages

### 6. Authority Boundary
- **Owns:** Product discovery and definition, buyer/problem validation, value hypothesis, delivery model, pilot scope, pricing, willingness-to-pay proof
- **Does NOT own:** Agent running/orchestration, execution of work packets (VSH owns), dashboard/SaaS UI, auth, billing, cloud

### 7. What the Academy May Reuse
- **Claim classification system** — Directly teachable as a product-leadership core competency
- **Product brief template** — Starting point for Academy student projects
- **Evidence discipline** — Five-level claim classification with source provenance
- **Decision Card format** — One-screen verdict template applicable to product decisions
- **Validation plan pattern** — Hypothesis-driven product validation
- **Scored backlog methodology** — 8-field scoring (impact, confidence, effort, risk, leverage, urgency, evidence_strength, priority_score)
- **VSH bridge** — Demonstrates the product -> engineering handoff

### 8. What the Academy Must NOT Duplicate
- The Product Forge package itself (it governs product, but the Academy teaches product leadership — different concerns)
- The VSH export bridge (operational, not pedagogical)

### 9. Potential Integration Point
The Academy should use Product Forge as both a teaching tool (students use it for their capstone projects) and a methodology reference. The claim classification system should be a Day 1 module. The Decision Card format should be a core Academy artifact. The Product Forge -> VSH bridge demonstrates the complete product-to-engineering pipeline.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — README.md (90 lines), schemas/ (12 JSON schemas), config/, prompts/, skills/, tests/ all read. Portfolio-registry.json confirms 12 tests, no git, portability blocked.

---

## SYSTEM 10: MIT

### 1. Purpose
MIT AI/LLM course materials repository. Contains lecture recordings (audio + transcripts), readings, team project materials, adjudicated course learnings, and MIT professional education materials.

### 2. Canonical Path
`C:\Walter\100 day plan\AI Agents\MIT`

Not part of the AI Agents portfolio operational stack. Educational reference material.

### 3. Primary Objects
- **Lectures** — 13 sessions with English/Spanish audio (m4a) and transcripts (txt)
- **Course Materials** — MIT_AI_LLM_Course_Master_Plan.docx, MIT_AI_System_Architecture_Practitioner_Manual.docx
- **Course Plans** — MIT AILLM Schedule July 2025, MIT AILLM SUM 2026 Schedule
- **Team Projects** — MIT_TEAM3_OPENAI_SDK_PACK, team 3 materials
- **Adjudicated Learnings** — 8 adjudication documents (claims audit, architecture cross-reference, research idea triage, approved candidate backlog, course project recommendation)
- **Readings** — AI Index Report 2026, Agentic AI Use Cases, RE-Bench paper, Google Agents Companion
- **Books** — Reference books
- **Pre-Readings** — Additional reading materials
- **Playbooks** — Pre-course action map, networking playbook, showcase workbook

### 4. Inputs
- MIT course lectures and materials
- AI/LLM professional education content

### 5. Outputs
- Adjudicated learnings (claims audited, ideas triaged, projects recommended)
- Course completion artifacts
- Team project work (OpenAI SDK integration)

### 6. Authority Boundary
- **Owns:** Educational consumption and personal learning
- **Does NOT own:** Any operational system

### 7. What the Academy May Reuse
- **Adjudication methodology** — The MIT_COURSE_ADJUDICATED folder demonstrates an evidence-based learning audit process (claims audit, architecture cross-reference, independent review) that the Academy should emulate for curriculum quality assurance
- **Course project recommendation framework** — From adjudicated documents
- **Research idea triage methodology** — Systematic evaluation of candidate ideas against evidence
- **Course structure** — MIT`s LLM curriculum structure as a reference for Academy course design
- **Claims and evidence audit** — Directly applicable to Academy content quality standards

### 8. What the Academy Must NOT Duplicate
- The MIT course content (proprietary educational material)
- The lecture recordings and transcripts (licensed MIT content)

### 9. Potential Integration Point
The adjudication methodology used to process MIT course learnings should be directly adopted as the Academy`s curriculum quality assurance process. The pattern of: collect learnings -> audit claims against evidence -> cross-reference with architecture -> triage ideas -> produce approved backlog — is the exact same evidence-discipline pipeline the Academy should apply to its own content.

### 10. Confidence and Evidence Path
**Confidence: HIGH** — Directory listing (53 entries), MIT_COURSE_ADJUDICATED/ (8 adjudication documents), lecture transcripts sampled, course plans read. Content is reference/educational, not operational.


---

## Cross-Cutting Analysis

### Repository Sprawl Observations

1. **Significant duplication** between `Agents/` and `Agents-front-office/`:
   - `vsh-v0.4` exists in both locations (22 vs 22 entries, structurally identical at root)
   - `ops-hub` exists in both locations but with **diverged content**: `Agents/ops-hub` has CODEX.md and is opencode-focused; `Agents-front-office/ops-hub` has CLAUDE.md and is Claude Code-focused
   - `kernel-spec` exists in both locations (9 vs 9 entries, structurally identical)
   - `Agents-front-office` additionally contains PAL (238 tests, Slice 0 verified) and 7 VSH roadmap documents not present in `Agents/`
   - Total files duplicated: approximately 40-50 files across vsh-v0.4, ops-hub, and kernel-spec

2. **Canonical vs. snapshot ambiguity**: `Agents/` appears to be the "live" workspace (with opencode transition), but `Agents-front-office/` contains the PAL implementation that `Agents/` references but doesn`t contain directly. The PAL monorepo metadata says it`s in `Agents/portfolio-autonomy-layer` but that path doesn`t exist — it`s actually in `Agents-front-office/portfolio-autonomy-layer`.

3. **Product Forge isolation**: Not a git repository, not integrated into any portfolio workflow, and has portability blocked. Yet it produces VSH-compatible work packets. This is a critical loose end.

4. **Hermes isolation**: Standalone repo with no GitHub remote, no integration with the monorepo, yet InfraPrep and portfolio-registry both reference it as a core runtime.

### Overlapping Responsibilities

| Function | Primary Owner | Secondary/Overlap |
|----------|--------------|-------------------|
| Task decomposition | Hermes | VSH (issue manifests), Product Forge (work packets) |
| Quality gates | VSH | kernel-spec (manifest validation), InfraPrep (stage gates) |
| Portfolio tracking | ops-hub | PAL (budget/permissions), kernel-spec (portfolio-registry) |
| Agent constitutions | ops-hub (AGENTS.md) | Every repo has its own AGENTS.md |
| Skill authoring | ops-hub | agent-skills (external, 24 skills), Product Forge (product skills) |
| Evidence discipline | kernel-spec (evidence-contract) | Product Forge (claim classification), InfraPrep (acceptance tests) |
| Approval flow | PAL | kernel-spec (approval.vocabulary), Hermes (AUTHORIZED state) |
| Manifest-first workflow | VSH | kernel-spec (manifest.schema), InfraPrep (5 launch manifests), Product Forge (work packets -> VSH manifests) |
| Decision cards | Product Forge (v0.2) | VSH (DECISION_CARD_TEMPLATE.md) |

### Stale Folders

1. **Agents-front-office/master branch** — Explicitly marked as "historical/stale" in README branch policy. Should not be used as base for new work.

2. **Agents-front-office/vsh-v0.2** and **Agents-front-office/vsh-v0.21** — Older VSH versions preserved in same directory. vsh-v0.4 is the current version.

3. **Hermes/canonical/**, **Hermes/claude-orchestration/**, **Hermes/morning-packets/**, **Hermes/product-assessments/** — All explicitly marked as "historical reference material, not part of the active runtime" in AGENTS.md.

4. **Agents/vsh-v0.4/vendor/** — Contains vendored dependencies, size unknown.

5. **Agents-front-office/.gitattributes** and **opencode.json.bak** — Artifacts suggesting configuration churn.

6. **TIAA Research** — Marked "Research Complete — 6 Streams Verified." No longer active. Completed deliverable.

### Naming Ambiguity

1. **ops-hub vs. Agents-front-office** — The `Agents-front-office/README.md` says "# ops-hub" as its title, creating confusion about whether it IS ops-hub or CONTAINS ops-hub. The branch strategy section clarifies that these are different repos but the naming collision is problematic.

2. **VSH version numbering** — VSH v0.2-beta (README says v0.2 beta), v0.4 (directory name), v0.21.2 (portfolio registry current baseline), v0.30-v0.55 (roadmap documents). Multiple version schemes in simultaneous use.

3. **Domain OS vs. Application vs. Workflow** — The portfolio registry classifies InfraPrep as `application` type, but the InfraPrep README says it`s not yet a Domain OS (won`t be until Gate 5). Product Forge is classified as `domain_os` but calls itself a "Product Operating System." The classification vocabulary is inconsistently applied.

4. **ops-hub vs. ops-hub (Agents vs Agents-front-office)** — Two repos with the same name and substantially similar README but different cockpit strategies (opencode vs Claude Code). No clear documentation of which is canonical for which purpose.

### Unclear Authority Boundaries

1. **Manifest schema authority**: `kernel-spec/manifest.schema.json` defines the canonical manifest shape, but `VSH/quality/schema/issue-manifest.schema.json` defines VSH-specific manifests, and `InfraPrep/04_manifests/` contains 5 additional manifest formats. Is kernel-spec the schema-of-schemas or just guidance?

2. **PAL location**: The portfolio-registry says PAL is in `Agents/portfolio-autonomy-layer/` (monorepo), but the actual PAL code is in `Agents-front-office/portfolio-autonomy-layer/`. The authority boundary between these two codebases for PAL is undocumented.

3. **Hermes relationship**: Hermes has no GitHub remote and is not in any monorepo. It`s referenced by portfolio-registry, InfraPrep, and PAL (via mock adapter). Is it frozen? Will it be integrated into the monorepo? The ARCHITECTURE.md says Phase 2 "has not been started."

4. **Product Forge integration**: Works with VSH via export bridge but is not a git repo and has no portfolio entry with a remote URL. It references `example_tiaa_public_product_intelligence` which sources from the completed TIAA research. The integration lifecycle is unclear.

### Overall Ecosystem Topology

```
+------------------------------------------------------------------+
|                         Walter (Human)                            |
|              Portfolio Allocation, Irreversible Approval          |
+------------------------------+-----------------------------------+
                               |
          +--------------------+-----------------------+
          |                    |                       |
          v                    v                       v
+------------------+  +------------------+  +-------------------------+
|   Agents/        |  | Agents-front-    |  |  Standalone Systems     |
|   (CANONICAL)    |  | office/          |  |                         |
|                  |  | (LEGACY/PAL)     |  |  * Hermes               |
|  * kernel-spec   |  |                  |  |  * Product Forge        |
|  * ops-hub       |  |  * vsh-v0.4      |  |  * agent-skills (ext)   |
|  * vsh-v0.4      |  |  * ops-hub       |  |  * InfraPrep            |
|                  |  |  * kernel-spec   |  |  * MIT (educational)    |
|                  |  |  * PAL <-------- |  |  * TIAA Research (done) |
|                  |  |                  |  |                         |
+--------+---------+  +--------+---------+  +-----------+-------------+
         |                     |                        |
         |     DUPLICATED      |       ISOLATED         |
         |<------------------->|       SYSTEMS          |
         |                     |                        |
         v                     v                        v
+------------------------------------------------------------------+
|                     Portfolio Registry                             |
|          12 entries: deal-os, vsh, pal, hermes, kernel-spec,      |
|          product-forge, job-search, outreach-os,                  |
|          academic-paper-os, infraprep, ops-hub, agent-skills       |
+------------------------------------------------------------------+
```

**Key topology observations:**

1. **The portfolio has two hubs**: `Agents/` (current, opencode-focused) and `Agents-front-office/` (legacy snapshot + PAL). The PAL implementation is trapped in the legacy directory while the canonical systems reference it from the current directory.

2. **Four systems are not integrated into either hub**: Hermes (no remote), Product Forge (no git), InfraPrep (launch pack, not OS), and agent-skills (external dependency).

3. **Three administrative systems form the portfolio backbone**: kernel-spec (schema authority), ops-hub (portfolio tracking), PAL (authorization). But PAL`s actual code location contradicts the registry.

4. **Two domain systems are operational**: VSH (software quality) and Deal OS (deal analysis, not inspected here). Additional Domain OSes (Outreach OS, Academic Paper OS, InfraPrep-as-OS) are in various stages of development.

5. **The Product Leadership Academy will be the next leaf** in this topology, drawing from kernel-spec conventions, ops-hub registration, agent-skills patterns, and (optionally) Hermes orchestration.


---

## Recommendations for the Academy

### Immediate Actions
1. **Register the Academy as an initiative in ops-hub** with a unique ID (e.g., `PLA-001`)
2. **Adopt the kernel-spec run-folder convention** for Academy student work from Day 1
3. **Author Academy skill modules** using the agent-skills SKILL.md pattern
4. **Use Product Forge`s claim classification** as the foundation for the Academy`s evidence-discipline curriculum
5. **Request PAL authorization** for Academy resources following the InfraPrep stage-gate model

### Architecture Decisions to Make
1. Should the Academy live in `Agents/` (canonical) or as a standalone repo like Hermes?
2. Should Academy student progress be tracked via Hermes state machine or PAL task queue?
3. Should Academy content be versioned and tagged like kernel-spec (v0.1.0)?
4. Should the Academy produce VSH-compatible manifests for capstone software projects?

### Risks to Monitor
1. The `Agents/` vs `Agents-front-office/` duplication must be resolved before the Academy integrates with any duplicated system
2. Product Forge must be git-initialized before it can be meaningfully integrated
3. Hermes` lack of a remote and Phase 2 stall creates integration risk for any campaign-orchestration dependency
4. The manifest schema version (0.1) may change — Academy should track kernel-spec closely

---

## Evidence Inventory

| File | Repository | Lines Read | Key Finding |
|------|-----------|------------|-------------|
| README.md | vsh-v0.4 | 69 | VSH Quality Fabric v0.2-beta, manifest-first, 12 CLI commands |
| AGENTS.md | vsh-v0.4 | 66 | 12 forbidden actions, 9-step manifest-first workflow |
| pyproject.toml | vsh-v0.4 | 22 | vsh-quality 0.2.0-beta, jsonschema dependency |
| README.md | ops-hub (Agents) | 56 | opencode + DeepSeek cockpit, SME-JV pitch |
| AGENTS.md | ops-hub (Agents) | 87 | Universal agent constitution, opencode as runtime |
| manifest.schema.json | kernel-spec | 451 | 30 required fields, v0.1 task contract |
| portfolio-registry.json | kernel-spec | 304 | 12 portfolio entries, all systems catalogued |
| portfolio-registry.schema.json | kernel-spec | 179 | 12 approved component_ids, 9 component_types |
| run-folder-convention.md | kernel-spec | 65 | Standardized run folder with 9 required files |
| approval.vocabulary.md | kernel-spec | 69 | 5 approval statuses, 13 human-only actions |
| telemetry.schema.json | kernel-spec | 250 | 29 required fields for telemetry records |
| README.md | Hermes | 63 | Phase 1 frozen, 125 tests, Python stdlib only |
| ARCHITECTURE.md | Hermes | 112 | State machine, system boundaries, package layout |
| AGENTS.md | Hermes | 78 | Repository structure, CLI verbs, dependencies |
| REPOSITORY_MANIFEST.md | Hermes | 76 | Full file inventory, 7 source files, 14 test files |
| README.md | agent-skills | 379 | 24 skills, 8 slash commands, 70+ agent integrations |
| README.md | InfraPrep | 64 | Launch pack, 5-stage gate system, non-goal guardrails |
| PORTFOLIO_ROUTING.md | InfraPrep | 108 | Explicit routing between Ops Hub, PAL, Product Forge, VSH |
| STAGE_GATES.md | InfraPrep | 112 | Gates 0-7 with pass evidence and failure responses |
| launch_sequence.json | InfraPrep | 65 | 10-step sequence with owners and gate assignments |
| ACCEPTANCE_TESTS.md | InfraPrep | 49 | 6 categories, 30 acceptance criteria |
| HANDOFF_TO_HERMES.md | InfraPrep | 50 | Mission, orchestration behavior, first assignment |
| README.md | Agents-front-office | 59 | ops-hub titled, Claude Code cockpit, branch policy |
| README.md | PAL | 36 | Slice 0: task/approval/heartbeat contracts, 238 tests |
| README.md | Product Forge | 90 | File-first AI Product OS, 5 claim types, VSH bridge |
| MASTER_RESEARCH_PLAN.md | TIAA Research | 259 | 6 research streams verified, $434.6B market |
| VSH_ROADMAP_v0_50.md | Agents-front-office | 2980 | Full VSH strategic roadmap document |
| OPUS_HANDOVER.md | vsh-v0.4 | 159 | Codex-to-Opus handoff documenting construction history |
| MIT_COURSE_ADJUDICATED/ | MIT | 8 files | Evidence-based learning adjudication methodology |
