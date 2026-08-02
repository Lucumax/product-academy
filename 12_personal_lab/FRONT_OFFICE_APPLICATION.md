# Agents Front Office — Academy Application

**Date:** 2026-08-01  
**Evidence labels applied throughout**

---

## 1. Product or Initiative

**Agents Front Office (ops-hub)** — "Private operating system for shipping apps fast and productizing AI services for SMEs." A single repository housing agent constitutions, skills, templates, playbooks, project briefs, decision logs, and the SME-JV pitch infrastructure. The operating system for how Walter's agentic stack builds and sells software. *(Local-source fact: from README.md and repo structure)*

**Key components (from README.md):**
- Agent constitutions (CLAUDE.md, KIMI.md, GEMINI.md, AGENTS.md) — rules for each model
- Skills (`/skills/`) — Reusable SKILL.md capability bundles
- Templates (`/templates/`) — Document templates for product briefs, proposals
- Projects (`/projects/`) — One folder per active project
- Playbooks (`/playbooks/`) — Operating model: triad workflow, token economics, brand voice
- Decisions (`/decisions/`) — ADR-style decision log
- Pitch (`/pitch/`) — SME-JV positioning, pricing, discovery scripts
- n8n (`/n8n/`) — Workflow specs for automation

**The Triad Architecture (from README.md):**
- Top (architect/control): Claude Opus 4.7 — Strategy, hard reviews, novel skills, JV/sales
- Middle (planner/reviewer): Kimi K2.6 or DeepSeek V4 Pro reasoning — Decomposition, repo audits, acceptance criteria, diff review
- Bottom (builder): DeepSeek V4 Pro — Bulk implementation via OpenCode

**Current state:** Bootstrap. Strategic seed files complete. Stubs for expansion. *(Local-source fact)*

---

## 2. Product Archetype

**Primary:** AI-Enabled Workflow Product (Archetype 5 in `archetype_catalog.md`)

**Why AI-Enabled Workflow:**
- The product IS an AI workflow — agentic systems orchestrated to produce software outputs *(Local-source fact)*
- Model capability uncertainty: each agent (Claude, Kimi, DeepSeek) has different strengths, failure modes, and cost profiles *(Local-source fact)*
- Evaluation is a first-class problem: how do you know if the agentic output is good enough? *(Inference)*
- Cost structure is unusual: token consumption economics rather than traditional software costs *(Local-source fact)*
- The "product" is primarily consumed by AIs (agents), not humans directly *(Inference)*

**Secondary:** Internal Tools / Operations (Archetype 13)
- The front office serves Walter's internal operations for building and selling software
- Success is measured by throughput, quality, and revenue of projects built through the system *(Inference)*

**Third overlay:** Platform / Infrastructure (Archetype 3)
- provides a platform that agents operate on — skills, templates, playbooks are platform capabilities
- The value is indirect: the front office enables better and faster software delivery *(Inference)*
- Adoption within the agentic ecosystem is mandated, not voluntary (PRN-0001 applicability conditions don't fully apply)

**Archetype-specific characteristics that matter:**
- AI product failure mode #1 (from archetype_catalog): "Shipping a model, not a product" — the front office must be more than a collection of prompts
- AI product failure mode #5: "Prompt engineering as product strategy" — prompts are fragile, hard to evaluate, and not a moat
- AI product failure mode #2: "Over-indexing on model quality" — users care about whether the product works, not which model ran

---

## 3. Industry

**AI/Agent Tools** — The industry of products that help people build, orchestrate, and deploy AI agents. *(External fact)*

OR

**AI-Enabled Professional Services** — The front office positions for SME-JV partnerships: AI services sold to small and medium enterprises. *(Local-source fact: from pitch/ directory and README.md)*

The front office sits at the intersection of two industries:
1. AI tooling infrastructure (how you build with AI)
2. AI-enabled professional services (how you sell what AI builds)

**Key industry characteristics:**
- Rapidly evolving: agent capabilities, model capabilities, and tooling mature monthly *(External fact)*
- No established pricing models for agentic software development *(Unknown)*
- SME market for AI services is huge but skeptical — needs trust building *(Inference)*
- Competition from no-code platforms, horizontal AI tools, and traditional agencies *(External fact)*
- Token economics create a direct relationship between product quality and cost that traditional SaaS doesn't have *(Inference)*

---

## 4. Organizational Stage

**Seed-stage / Bootstrap** — The repository structure exists, strategic seed files are complete, but most stubs are not filled in. *(Local-source fact)*

**Stage-specific Academy doctrine:**
- Pre-PMF: "strategy is 'find PMF by trying things' and exclusion would be premature" (PRN-0002 non-applicability)
- Pre-PMF: focus on achieving initial PMF first (PRN-0004 non-applicability)
- The default should be speed over perfection (PRN-0003 applicability)
- The PM as builder (CON-0013, position A) is appropriate at this stage — Walter must be deeply involved in creation

**The key question at this stage:** Is the front office valuable enough that Walter would be "very disappointed" if it were unavailable? If the answer is "not yet," the focus should be on achieving that state for the primary workflow (shipping apps fast). *(Recommendation)*

---

## 5. Current User

**Walter (primary, currently sole user)** — Uses the front office to orchestrate agentic software development and prepare commercial positioning for SME services. *(Local-source fact)*

**Potential future users:**
- Other developers/builder-operators who want to replicate the agentic development model *(Inference)*
- SME clients who interact with the outputs (apps built through the system) *(Local-source fact: from pitch/SME-JV positioning)*
- n8n engineers implementing workflow specs *(Local-source fact)*

**User characteristics:**
- Technically sophisticated (must understand agent architectures, prompt engineering, software delivery) *(Inference)*
- Operates at the intersection of building and selling — not a pure developer or pure salesperson *(Inference)*
- Time-constrained and seeking leverage — the system exists to multiply output *(Inference)*

---

## 6. Buyer

**Walter** — Self-funded for the tooling layer. *(Local-source fact)*

**For the SME-JV commercial layer:** SMEs would be the buyers — small and medium enterprises purchasing AI-enabled software (apps) or AI services built through the front office. *(Local-source fact: from pitch/ directory)*

**Key buyer characteristics (SMEs):**
- Price-sensitive, results-oriented, skeptical of AI hype *(Inference)*
- Don't buy tools — they buy outcomes (a working app, automated workflow, improved process) *(Inference)*
- The sales motion is relationship-based for initial deals, potentially product-led for repeat *(Inference)*

**Buyer/user split:** For the commercial layer, the split exists. The SME (buyer) purchases; their team or customers (users) interact with the built product. *(Inference)*

---

## 7. Problem Thesis

**Claim:** Building quality software and bringing AI services to SMEs currently requires either (a) hiring expensive developers and PMs, or (b) using no-code/low-code tools with limited flexibility. An agentic development operating system — where AI agents collaborate under human direction using structured methodologies — can produce higher-quality software faster and cheaper than either alternative. For SMEs, this means access to custom AI-powered software that was previously only available to enterprises. *(Inference)*

**Decomposed sub-claims:**

1. **Problem existence (building efficiency):** Current software development is slower and more expensive than it could be with agentic systems → **Moderate evidence** (AI coding tools show productivity gains, but end-to-end agentic development is unproven at scale) *(External fact)*
2. **Problem existence (SME access):** SMEs cannot access custom AI-powered software at prices they can afford → **Moderate evidence** (enterprise AI tools are expensive, SME market is underserved) *(External fact)*
3. **Solution fit (triad architecture):** A three-tier agent architecture (architect, planner, builder) produces better results than a single agent → **Unknown** (theoretical rationale but no benchmark data) *(Unknown)*
4. **Solution fit (structured methodology):** Constitutions, skills, templates, and playbooks produce more consistent agentic output than ad-hoc prompting → **Plausible but unproven** (the Academy's evidence-based approach to product management provides a theoretical basis, but agentic methodologies are unproven) *(Inference)*
5. **Commercial viability:** SMEs will pay for AI-built software at prices that generate margin after token costs, human oversight time, and business overhead → **Unknown** *(Unknown)*

---

## 8. Evidence Status

**What we know (Local-source fact):**
- The repository structure exists with detailed constitutions for each agent
- The triad architecture assigns specific roles to specific models
- Skills, templates, and playbooks provide reusable methodology
- The branch policy and quality fabric exist for governance
- The SME-JV pitch infrastructure defines commercial positioning
- Sprint P0 and roadmap documents exist for near-term execution

**What we know (External fact):**
- AI coding assistants (Copilot, Claude Code, OpenCode) demonstrate meaningful developer productivity improvements
- Agentic systems can produce working software artifacts
- Multi-agent architectures (with different models for different tasks) are theoretically sound but operationally complex
- Token economics create a variable cost structure that must be managed actively
- SME AI adoption is a recognized market opportunity with limited penetration

**What we don't know (Unknown):**
- Whether the triad architecture produces measurably better results than a single strong model
- Whether the skill/constitution/template methodology meaningfully improves agentic output quality vs ad-hoc prompting
- Whether the operating system scales beyond Walter (single-user to multi-user)
- What the actual token costs are per project and whether they're economically sustainable
- Whether SMEs will pay for the output at prices that create profitable unit economics
- Whether the n8n workflow integration works in practice
- Model deprecation risk: what happens when a key model (Claude Opus, DeepSeek, Kimi) is deprecated or changes behavior?

---

## 9. Product-Leadership Questions

**From Academy AI doctrine (Module 05):**

1. **Workflow selection:** Which parts of the software development workflow are appropriate for AI? The triad architecture implicitly answers: architecture (high judgment, AI-assisted), planning/review (medium judgment, AI-primary), building (lower judgment, AI-primary). Is this classification correct? Has it been tested? *(Unknown)*
2. **Evaluation:** How do you know if the agentic output is good? What are the evaluation contracts for each tier? (Module 05, EVALUATION_CONTRACTS.md) *(Recommendation — define before scaling)*
3. **Failure modes:** What are the specific failure modes for each tier of the triad? Are there failure mode checklists? (Module 05, FAILURE_MODES.md) *(Unknown)*
4. **Governance:** What governance is proportional to consequence? Code generation has lower consequence than financial advice, but still matters when the output is deployed to customers. *(Recommendation — light but present)*

**From Academy core doctrine:**

5. **PRN-0002 (Strategy Is Exclusion):** What is the front office NOT going to do? Not build consumer apps? Not serve enterprises? Not compete with Vercel/Replit? *(Inference — exclude enterprise services, focus on SME apps)*
6. **PRN-0004 (PMF Is a Condition):** Is the front office itself a product that needs PMF, or an operating system for building products that need PMF? (Answer: both. The front office needs PMF with Walter; the products built through it need PMF with their markets.) *(Inference)*
7. **PRN-0006 (Pricing):** What is the pricing model for SME services? Project-based? Subscription? Outcome-based? The pitch directory should address this. *(Recommendation)*
8. **PRN-0009 (Platform Decisions):** Is the front office a platform that agents build on, or a factory that agents operate in? The "operating system" metaphor suggests platform. *(Inference — it's both, which creates tension)*

---

## 10. Principal-Level Trade-offs

**Trade-off 1: Methodology Investment vs. Shipping Velocity**
- Building constitutions, skills, templates, and playbooks takes time away from building actual products
- But methodology investment compounds — better skills produce better outputs with less oversight
- The optimal balance depends on how many projects the system will produce
- *(Recommendation):* For the first 3 projects, invest in methodology only after each project reveals what's needed. Build the skill AFTER you've done the thing manually twice. Don't build skills for things you haven't done yet (archetype_catalog Platform failure mode #1: building before the use case).

**Trade-off 2: General-Purpose OS vs. Specialized Factory**
- An "operating system" implies generality — it should work for any software project
- A "factory" implies specialization — optimized for specific types of projects
- The front office currently leans OS (general skills, templates, playbooks)
- *(Recommendation):* Start as a specialized factory (build only SME apps, only specific types). Generalize after proving the model works for the special case. This is the InfraPrep approach (wedge first, platform later) applied to the front office itself.

**Trade-off 3: Model Dependency vs. Model Abstraction**
- The constitutions are model-specific (CLAUDE.md, KIMI.md, GEMINI.md)
- This optimizes for current model capabilities but creates lock-in — changing models requires rewriting constitutions
- A model-agnostic skill layer would be more portable but less optimized
- *(Recommendation):* Keep model-specific constitutions for now (pre-PMF, optimize for quality). If model churn becomes costly, invest in a model-agnostic skill abstraction layer.

**Trade-off 4: Human-as-Builder vs. Human-as-Director**
- The triad architecture positions Walter as director with agents as builders
- But at this stage, Walter must be a builder too — the system can't run without him
- The transition from builder to director is a Principal+ capability (02_principal_plus, Capability 2)
- *(Recommendation):* Follow the Principal PM practice regimen — problem definition, customer contact, cross-functional influence, strategy review, decision audit. The front office is the vehicle for practicing Principal-level skills.

**Trade-off 5: Open Methodology vs. Proprietary Moat**
- The README says: "The methodology in /skills/, /playbooks/, and /pitch/ is the moat. Sell deliverables, not the repo."
- This is a deliberate strategy: methodology is proprietary, outputs are commercial
- But AI methodologies are hard to keep proprietary — anyone can reverse-engineer prompts and workflows
- *(Recommendation):* The moat is not methodological secrecy (unsustainable) but execution quality and customer relationships. The methodology can be transparent; the ability to execute it at quality is the differentiator.

---

## 11. Risks

**Risk 1: Model Capability/Cost Shift (High probability, Medium severity)**
- If a model in the triad changes pricing, deprecates, or is surpassed by a competitor model, the entire operating system needs recalibration
- Token costs are a variable expense that could make projects unprofitable if model prices increase
- *Mitigation:* Track token costs per project. Model the breakeven for each service tier. Maintain model alternatives (the triad architecture with interchangeable models provides some resilience).

**Risk 2: Methodology Fragility (Medium probability, High severity)**
- Skills and templates that work with today's models may fail with tomorrow's models (or even with model updates)
- Prompts are fragile artifacts — small changes in model behavior can break carefully crafted skill prompts
- *Mitigation:* Automated evaluation harness that tests skill outputs against known-good baselines after every model update. If a model update breaks a skill, detect it before it affects a customer project.

**Risk 3: Single-Person Dependency (High probability, Medium severity)**
- Walter is currently the only person who can operate the system
- If Walter is unavailable, the operating system stops
- This is acceptable at seed stage but becomes a scaling bottleneck
- *Mitigation:* Document the operating model to the point where another technically sophisticated person could operate it. The handoff documents (HANDOFF_TO_CLAUDE_CODE.md, HANDOFF_TO_HERMES.md, OPENCODE_CLEANUP_BRIEF.md) are a start.

**Risk 4: SMEs Don't Buy (Medium probability, High severity for commercial layer)**
- The SME-JV pitch assumes SMEs will pay for AI-built software
- SMEs may be skeptical, price-sensitive, or prefer established vendors
- The first paid customer is unproven
- *Mitigation:* Product Forge application to the SME-JV commercial thesis. Run customer discovery with 5 SMEs before investing in the pitch infrastructure beyond seed materials.

**Risk 5: Scope Proliferation (Medium probability, Medium severity)**
- The front office touches everything: agent management, skill development, project management, commercial pitch, workflow automation (n8n), decision logging
- Each of these could become its own product, diffusing focus
- *Mitigation:* Strategy Exclusion Test (PRN-0002). What will the front office NOT do? Define these explicitly. If it does everything, it does nothing well.

**Risk 6: Quality Variance Across Projects (Medium probability, Medium severity)**
- Agentic output quality varies by project complexity, domain familiarity, and model capability
- A project that works beautifully may be followed by one that fails
- Without evaluation contracts, it's hard to know when quality is slipping
- *Mitigation:* Define minimum quality gates for every project. If a project cannot pass the gate, escalate to human (Walter). Track pass/fail rates by project type.

---

## 12. Missing Validation

**Critical unknowns ranked:**

1. **End-to-end project throughput:** How many projects can the front office produce per month? What is the median time from project initiation to delivery? *(Recommendation):* Measure for the first 5 projects.
2. **Quality benchmark:** How does the agentic output compare to human-written code? To other AI tools? To what SMEs currently use? *(Recommendation):* For first 3 projects, have external reviewer assess quality.
3. **Token cost per project:** What is the total token cost (across all three tiers) for a typical project? *(Recommendation):* Track per-project token consumption from day one. Model against project revenue.
4. **Triad effectiveness:** Does three-tier architecture produce better results than a single strong model doing everything? *(Recommendation):* Run one project with the triad, one with a single model, compare quality/time/cost.
5. **SME willingness to pay:** Will SMEs pay for AI-built software, and at what price? *(Recommendation):* 5 SME discovery interviews before building beyond seed pitch materials.
6. **Skill reusability:** How often do skills get reused across projects? If rarely, the skill investment isn't paying off. *(Recommendation):* Track skill reuse per project.
7. **Model deprecation resilience:** What happens if a key model is deprecated? *(Recommendation):* Table-top exercise: swap one model in the triad for an alternative and measure impact on output quality.

---

## 13. Most Useful Academy Doctrine

| Doctrine | Relevance | Application |
|----------|-----------|-------------|
| **PRN-0002** (Strategy Is Exclusion) | High | Define what the front office will NOT do. This is the most urgent strategic question. |
| **PRN-0003** (Cost of Delay vs Imperfection) | High | Pre-PMF, speed matters more than methodology perfection |
| **PRN-0004** (PMF Is a Condition) | High | The front office needs PMF with Walter first; commercial services need separate PMF |
| **PRN-0005** (PM Owns the Problem) | Medium | The problem is "shipping apps fast and selling AI services" — methodology serves the problem |
| **PRN-0007** (Reversible by Design) | High | Skills and templates should be designed for easy update as models change |
| **PRN-0008** (Customer Discovery) | Critical | SME interviews before commercial investment |
| **PRN-0009** (Platform Decisions) | High | OS vs factory; methodology as platform vs methodology as process |
| **PRN-0010** (Org Design Is Product Design) | Medium | The triad architecture IS organizational design — Conway's Law for agents |
| **AI Workflow Selection** (Module 05) | Critical | Which parts of software development are appropriate for each tier of agent? |
| **AI Evaluation Contracts** (Module 05) | Critical | How to measure agentic output quality across the triad |
| **AI Failure Modes** (Module 05) | Critical | Failure mode checklist for each tier of the triad |
| **AI Model vs System** (Module 05) | High | System design (skills, templates, constitutions) matters more than model selection |
| **AI Governance** (Module 05) | Medium | Light governance for code generation; heavier governance for client-facing outputs |
| **AI Economics** (Module 05) | High | Token economics and pricing strategy for AI-delivered services |
| **CON-0013** (Builder vs Multiplier) | Medium | Walter's role evolution from builder to director of the agentic system |
| **CON-0010** (Build vs Buy) | Medium | How much of the front office infrastructure should be custom-built vs using existing tools? |
| **CON-0006** (Speed vs Quality) | High | Pre-PMF: speed matters. But client-facing outputs require quality. |
| **Decision Framework 1** (One-Way vs Two-Way Doors) | Medium | Classifying front office decisions by reversibility |
| **Decision Framework 2** (RICE-LM) | Medium | Prioritizing which skills, templates, and playbooks to build first |
| **CASE-0006** (Slack Platform Strategy) | High | Platform paradigm: what kind of "operating system" is the front office? |

---

## 14. Cheapest Decisive Test

**Test:** Complete one end-to-end project using the front office methodology end-to-end, and measure the results.

**Project selection:** Choose a project that is:
- Real (not a demo) — has an actual use case and outcome
- Right-sized — completable within 1-2 weeks
- Measurable — you can assess quality, time, and cost

**Measurements:**
1. **Time:** From project initiation to delivery, compared to estimated time without the front office
2. **Quality:** External review of the output (bug count, code quality, user experience)
3. **Token cost:** Total across all tiers
4. **Human time:** Walter's time spent directing, reviewing, and correcting agentic output
5. **Satisfaction:** Would Walter use this system for the next project?

**Cost:** 1-2 weeks of Walter's time + token costs for the project

**Decisive if:**
- The project takes 2x+ longer than estimated → methodology is slowing things down, not speeding up
- The project takes 0.5x or less than estimated → strong value signal
- Quality is below minimum acceptable threshold → methodology needs improvement or is inappropriate for this project type
- Token costs exceed what the project would generate in revenue → unit economics don't work
- Walter would not use the system again → front office fails the Sean Ellis test for its primary user

**If the test is ambiguous** (e.g., somewhat faster but quality is lower), run two more projects and aggregate results. Three projects is enough to establish a pattern.

---

## 15. What Would Reverse the Current View

**Current view:** The Agents Front Office is a promising operating system for agentic software development that combines structured methodology (constitutions, skills, templates) with tiered model architecture to produce better, faster, cheaper software than alternatives — with a commercial path through SME services. *(Recommendation)*

**The view should be reversed if:**
1. The end-to-end test shows the front office produces output slower than Walter working without it — the methodology cost exceeds its value
2. Token costs per project make the economics unviable for commercial services — the business model doesn't close
3. Model behavior changes break multiple skills and the maintenance cost of keeping skills current exceeds the value they provide
4. SME customer discovery reveals no willingness to pay for AI-built software — commercial thesis is falsified
5. A competing tool (Claude Code with built-in project management, another agent framework) makes the front office's methodology redundant
6. Walter stops using the front office for real projects — revealed preference shows the system isn't valuable enough

**The view should be strengthened if:**
1. End-to-end test shows significant time savings with acceptable quality
2. Token costs are well below project revenue, creating viable unit economics
3. Skills are reused across multiple projects without modification — methodology investment compounds
4. A second user (developer/operator) can operate the system with the documentation
5. An SME expresses interest in paying for a built app based on seeing the output quality
6. The first paid project is delivered, accepted, and the customer is willing to provide a reference

---

*This application should be revisited after the first 3 projects are completed through the front office. The current high proportion of "Unknown" and "Inference" labels is appropriate for a seed-stage initiative. The first 3 projects should convert many of these to "Local-source fact."*
