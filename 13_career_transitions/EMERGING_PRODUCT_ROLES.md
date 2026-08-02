# Emerging Product Roles: AI Product Management and the Evolving Career

Product management is fragmenting. The generalist role — the person who owns a product end to end, from problem selection to economics to launch — is being pulled apart by three pressures: a technical surface that has grown beyond what one person can hold in a working lifetime, a set of products whose constraints (probabilistic outputs, platform economics, data governance, agentic behavior) no longer fit a single mental model, and a labor market that rewards specialization with titles faster than it rewards capability with evidence.

This file is about that fragmentation. It takes the claim seriously that the role is evolving. It takes the counter-claim equally seriously: that much of what is marketed as "AI product management," "agent product management," or "data product management" is relabeled classical judgment applied to new material. The honest position is that **the role is genuinely splitting AND most of the individual claims about emerging roles are unverified practitioner doctrine**. The field is young. The titles are young. No one has measured an "AI PM" career end to end — not one cohort, not one promotion cycle, not one ten-year longitudinal study. Everything in this file about the *durability* of these roles is therefore **[P]** (practitioner doctrine) or **[I]** (inference), and the document says so explicitly wherever it matters.

The epistemic labels used throughout this file follow the Academy convention: **[E]** empirically documented, **[P]** practitioner doctrine, **[I]** inference, **[D]** open debate among practitioners, **[R]** practical recommendation. Where a claim about an emerging role is asserted without a label, assume it is **[P]** or **[I]** until labeled otherwise.

The through-line, stated plainly at the start: **the capability is more durable than the title, and the generalist base is more durable than the specialization.** [I] Everything in this file — the splitting mechanism, the AI PM analysis, the durability assessments, the positioning and hiring guidance — is an elaboration of that one claim.

---

## The Splitting of Product Management

### Why the role is fragmenting

The mechanism of fragmentation is not mysterious. It is the same mechanism that splits any professional category: when the total body of relevant knowledge, constraint types, and failure modes exceeds what a single practitioner can hold, the role splits along the clearest fault lines. Product management is splitting along three axes:

1. **Technical surface.** A senior PM in 2015 needed to reason about web, mobile, APIs, databases, and growth mechanics. A senior PM today is asked to reason about model evaluation, retrieval architectures, prompt/system design, inference economics, agent permission boundaries, platform governance, data contracts, and workflow automation — each of which is a deep field in its own right. [I] No individual can maintain working fluency across all of it while also holding the business and organizational load of the role. The split here is not a choice; it is a consequence of information physics. [I]

2. **Constraint diversity.** Classical software fails loudly, deterministically, and observably. AI products fail silently, probabilistically, and on a spectrum (see the failure taxonomy in [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md)). A product whose failure modes are different *in kind* demands a different operational discipline — evaluation contracts, distribution-shift monitoring, rollback thresholds — than a product whose bugs are deterministic. The constraint set is not a superset of classical product constraints; it includes categories that do not exist in classical products, such as silent performance degradation without any code change. [E] Documented failure modes are the one part of this story that is genuinely empirical.

3. **Market and organizational signaling.** Companies create job titles faster than they create capability definitions. [I] New titles are cheap; new capability development is expensive. When "AI PM," "data product manager," and "head of agentic products" postings multiply, the market is responding to both real capability demand and to signaling pressure — the desire to look current, to attract a shrinking pool of labeled talent, and to give boards something to point at. This is not evidence that the underlying capabilities are distinct; it is evidence that the labor market has discovered that specialization sells. [P] Every technology wave since the PC did this. The titles change; the mechanism does not. [I]

### The fragmentation is happening at the level of titles before it happens at the level of capability

This is the central observation of this file: **titles are ahead of capability**. [I]

Consider what "AI product management" meant when the label first circulated and what it means now. The label did not arrive with a body of demonstrated practice, validated methods, or a curriculum. It arrived as a job posting category. The capabilities it refers to — evaluation design, judgment under probabilistic uncertainty, model-vs-system reasoning — exist and are real, but they are a reweighting and extension of the capability model in [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md), not a new profession that appeared whole. A candidate hired today as an "AI PM" is, in the durable base rate, [P] a classical PM with good judgment whose product happens to use a model — plus a smaller but real increment of genuinely new evaluation and failure-mode literacy.

The ordering matters. In a healthy profession, the sequence is: demonstrated capability first, then a curriculum, then a credential, then a title. In the emerging roles, the sequence has run backward: the title came first, the credential market followed, and the demonstrated capability base is still being assembled. [I] This is not a reason to dismiss the emerging roles; it is a reason to be skeptical of anyone — employer or candidate — who treats the title as carrying the same evidentiary weight as the capability.

### The two readings of the split

The splitting therefore has two readings:

- **The strong reading:** the role is dividing into distinct careers, each with its own capability profile, trajectory, and economic value — like the split of "computer programmer" into frontend/backend/devops/data/SRE a generation ago. Under this reading, a PM must choose a track early, and the choice is consequential for the rest of a career.

- **The weak reading:** the role is gaining specialization *within* a common base, like the split of "doctor" into specialties that still share a single medical education. Under this reading, specialization is a deepening of a shared foundation, and the foundation is what transfers.

The evidence favors the weak reading over the strong one, but the market prices titles as if the strong reading were true. [D] Practitioners disagree here — some argue AI PM is a genuinely distinct discipline that will formalize like ML engineering did; others argue it is a passing label that will dissolve back into general PM as evaluation tooling standardizes, the way "mobile PM" dissolved into general PM once mobile became table stakes. [P]

The consequence for a PM choosing a career is asymmetrical. If the weak reading is right and you bet on the strong reading — leaving the generalist base to chase a specialized title — you lose the foundation and hold a repriceable label. If the strong reading is right and you bet on the weak reading — holding the generalist base while deepening one specialization — you keep the foundation and the specialization, and you lose only the first-mover advantage on the label. [I] The asymmetry means the weak reading is the correct bet even when uncertain. [R]

### What the split is NOT

- The split is not the obsolescence of generalist judgment. Everything that makes a senior PM valuable — problem selection, economics, cross-functional influence, sequencing — remains the load-bearing part of every emerging specialization. [I]
- The split is not a linear ladder of new titles to chase. Most emerging titles will not outlive the wave that created them. [I]
- The split is not uniform across companies. The degree of specialization demanded depends on the product archetype ([archetype_catalog.md](../04_product_archetypes/archetype_catalog.md)), the organizational stage, and the maturity of the company's evaluation infrastructure. A 10-person company that hires an "AI PM" is hiring a generalist with an AI product; a 500-person AI-native company may genuinely need an evaluation specialist. [P]
- The split is not a law of nature. It is a current state, and it will re-converge. The pattern in every previous technology wave is divergence during the wave and re-convergence after it, when the genuinely new capability gets absorbed into the general base. [I]

### The organizational economics of the split

The split also has an organizational-economic driver, and understanding it makes the durability analysis sharper. [I] A company faces a choice: train a generalist PM to acquire a new specialization (slow, uncertain, requires a manager who can develop the capability), or hire a labeled specialist from the market (fast, but the label does not verify capability). When the wave is young, the hire option is systematically preferred because the training option is slow and the label appears to de-risk the decision. [I]

That preference has a predictable consequence: the market produces many labeled specialists of variable quality, and the companies that hired on label discover — some fast, some slow — that the label is a weak signal. [P] This is not a critique of the specialists; it is an observation about information economics. The leader who internalizes it gets an arbitrage: while competitors overpay for labels, the leader can build the shared evaluation infrastructure that develops the capability in generalists, and can evaluate labeled candidates against the same capability standard everyone else skips. [R]

The arbitrage is time-limited. As the wave matures, the base rate of labeled specialists improves (the survivors of the wave become genuinely good), the label signal strengthens, and the arbitrage closes. [I] The window to build capability-first is now. [R]

---

## AI Product Management

AI product management is the most developed emerging specialization. It is the most developed for three reasons: the underlying technology changed the failure regime of software, a large amount of capital flowed through AI products and forced real practice, and a body of practitioner literature accumulated quickly. That makes it both the most real of the emerging roles and the best test case for the "new vs. relabeled" question.

### What AI PM actually requires

The AI module ([Module 05](../05_ai_product_management/README.md)) is the Academy's treatment of the craft. The emerging-role question is: **what does the person managing an AI product need that a classical PM does not?** The honest answer, capability by capability:

- **Evaluation contracts.** The most important new artifact. Before building, the AI PM defines success and failure in product terms: a severity-weighted failure taxonomy, launch thresholds, rollback thresholds, and a monitoring plan that detects silent degradation. Classical PM defines success metrics and rolls back features on flags; it does not, as a standard practice, define a severity-weighted failure taxonomy for probabilistic output, or specify the performance level at which the system must come offline, or monitor for degradation that occurs *when nobody changed anything*. This is a genuinely new discipline. [I] See [EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md) and the working template in [TOOLS.md](../05_ai_product_management/TOOLS.md).

- **A new failure taxonomy.** Silent failures, hallucination/fabrication, confidence miscalibration, distribution shift, feedback-loop degradation, cascading agent failures, prompt injection — these are not classical bug categories. They are documented, empirical properties of AI systems. [E] The taxonomy in [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md) is the reference. The PM who manages an AI product without this taxonomy is flying blind, the same way a PM who manages a payments product without understanding reconciliation is flying blind. This is genuinely new: classical software has no analog for "the system will be wrong a known fraction of the time, in ways that look plausible, and it will get worse without any change to our code."

- **Model-vs-system reasoning.** The model is not the product. System design — data, retrieval, context assembly, tool use, validation, orchestration, human-in-the-loop — matters more than model selection for most of the product's quality. [P] This is a real analytical frame, and it is partially new: it parallels architecture literacy for classical systems (see Capability 1.5, Technical Fluency, in [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md)) but adds categories (context assembly, inference economics, retrieval failure, tool-use boundaries) that a classical PM never had to reason about. The disciplined version is [MODEL_VS_SYSTEM.md](../05_ai_product_management/MODEL_VS_SYSTEM.md).

- **Trust and adoption as a first-class engineering concern.** AI adoption is trust-constrained, not just utility-constrained: users over-trust AI in some contexts (automation bias) and under-trust it in others (algorithm aversion), and a single visible error destroys more trust than multiple invisible successes build. [E] The consequence — that adoption strategy is part of the product design, not a launch activity — is classical adoption capability applied to a constraint set that behaves differently. See [ADOPTION.md](../05_ai_product_management/ADOPTION.md). This is largely relabeled capability (Capability 3.1, Adoption and Change Management) with new failure dynamics.

- **Governance as a product discipline.** Tiered, proportional governance — with the governance burden scaling with the consequence of the use case — is a real new responsibility, and a regulatory surface (notably the EU AI Act) is genuinely new. [E] A PM who treats governance as a compliance checkbox will ship more slowly with more incidents than one who builds it into the evaluation contract. See [GOVERNANCE.md](../05_ai_product_management/GOVERNANCE.md). What is new here is the *surface* (new regulations, new accountability structures); what is relabeled is the underlying judgment — risk management (Capability 1.8) and outcome ownership (Capability 2.4) applied to probabilistic systems.

### An example: the medical-coding workflow

To make the difference concrete, take the medical-coding workflow used throughout [WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md): medical coders review clinical documentation and assign ICD-10, CPT, and HCPCS codes for reimbursement.

A classical PM managing this as software builds the coder's workbench: the interface, the lookup tools, the audit trail, the queue. Success is measured in throughput, error rate relative to a static standard, and user satisfaction. The failure modes are deterministic bugs — a lookup that returns the wrong code, a screen that loses state.

An AI PM managing the same workflow adds an entire layer. Before building, they write an evaluation contract: what fraction of encounters may be auto-coded without review, what severity weight a wrong code carries (a miscoded encounter can mean a denied claim, an audit finding, or — at the worst — fraud exposure), what the launch threshold is, and what rollback trigger exists if the error rate drifts. They design for silent failure — a plausible-but-wrong code with no system error — which is precisely the failure mode a classical software PM never had to design for. They monitor distribution shift: the model was evaluated on urban hospital notes; will it hold on rural clinic notes with different documentation habits? They manage the governance tier (high consequence, human-in-the-loop required, explainability) and the trust question (will coders trust and verify an auto-coded encounter, or rubber-stamp it into automation bias?). [I]

That example shows the split cleanly. The *evaluation discipline* is genuinely new. The *judgment* about what codes matter, what errors cost, and how the workflow actually runs is the same judgment a strong PM always applies. The AI PM's title is new; roughly two-thirds of the work it names is the generalist base. [I]

### The evaluation contract as the defining artifact of the role

If there is one artifact that defines AI PM as more than relabeled generalism, it is the evaluation contract. It deserves closer treatment than the summary above, because it is where the genuinely-new capability is most concentrated and where practitioners most reliably separate. [I]

An evaluation contract is a contract in the literal sense: a mutual, binding specification between the product organization and the system. It says, in writing, *what the system must do to be allowed to serve users, what it must stop doing to be taken off-line, and how the organization will know which of those conditions is true.* The classical analog — a PRD plus success metrics — is not a contract, because it specifies intent, not obligation. The evaluation contract specifies obligation: a severity-weighted failure taxonomy, launch thresholds as specific numbers, rollback thresholds as specific numbers, and a monitoring plan that detects degradation when nothing was changed. [I] The full structure lives in [EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md), and a working template is in [TOOLS.md](../05_ai_product_management/TOOLS.md).

What makes it a *contract* rather than a document is that both sides are bound. The system is bound: it may not launch until the thresholds are met, and it must be rolled back when they are breached. The organization is bound: it commits to the monitoring, the human-escalation pathway, the audit cadence, and the discipline of honoring the rollback trigger when it fires — even when the system looks fine. The most common AI product governance failure is not the absence of a contract; it is the presence of a contract that the organization ignores when the rollback trigger fires because "it seems to be working." A contract that is not honored is a decoration. [P]

Three properties separate a good evaluation contract from a performative one:

1. **Specific numbers, not ranges.** "Task success rate below 85% for six consecutive hours" is a trigger. "If quality degrades meaningfully" is not. The specificity is what makes the contract enforceable and what forces the organization to confront its real thresholds in advance, when they can be reasoned about calmly, rather than in the middle of an incident. [R]

2. **Silent-failure coverage.** The monitoring plan must include signals that do not look like system errors: human-review sampling, user override rates, downstream business-metric drift. A contract that monitors only latency and 5xx rates will miss the failure mode — silent, plausible, wrong — that defines AI product risk. [R] This is the point made explicitly in the rollback section of [EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md).

3. **An owner and a review cadence.** A contract without an owner is a draft. The contract specifies who owns it, who reviews it, and what events trigger a review (a model-provider change, a new user population, a regulatory change, an incident). AI systems drift; the contract that governs them must be re-specified on a schedule, not ossified at launch. [R]

The reason the evaluation contract is the defining artifact of the role is that writing one well requires exactly the capability blend that separates AI PM from generalist: evaluation fluency (Capability 1.6), risk judgment (Capability 1.8), domain understanding to weight failure severities (Capability 1.3), and outcome ownership to enforce it (Capability 2.4). It is the one artifact where the genuinely-new capability and the generalist base are both on display, inseparable. [I]

### How AI PM varies across archetypes

The AI PM role is not uniform; it shifts with the product archetype, and the shift is worth mapping because it tells a PM which version of the role they are actually being asked to perform. [I] The archetype catalog ([archetype_catalog.md](../04_product_archetypes/archetype_catalog.md)) defines the frame; the AI PM variation is:

- **Enterprise + AI.** Evaluation contracts dominate. Consequence tiers are high; the buyer/user split means the evaluation contract must serve two audiences — the enterprise buyer who demands explainability and audit, and the end user who demands reliability. Governance is a sales requirement, not just a compliance matter. The AI PM here is an evaluation-and-governance specialist first. [I]

- **Consumer + AI.** Trust and adoption dominate. Users have no procurement process forcing acceptance; they churn the moment the AI feature disappoints. The AI PM here is a trust-and-retention specialist: overpromising is the dominant failure mode, and the evaluation contract must include trust metrics, not just task success. [I]

- **Platform + AI.** The AI capability is one surface among many; the PM's challenge is sequencing and blast radius — an AI failure in platform infrastructure ripples across every consumer. The evaluation contract must be written for machine consumers, and the severity weighting must account for cascading blast radius. [I]

- **Healthcare + AI.** The governance tier is maximum and the failure stakes are existential. The evaluation contract is a safety case; the regulatory surface (and the human-in-the-loop requirements) are non-negotiable and come first. The AI PM here is a risk-and-governance specialist with deep domain fluency. [I]

The variation matters for two reasons. First, it is why a single "AI PM" hire cannot be evaluated with a single rubric — a consumer AI PM and a healthcare AI PM share perhaps half their capability profile. [I] Second, it is why a PM choosing among AI opportunities should match the archetype to their own capability base: the evaluation-heavy archetypes reward Capability 1.6 and 1.8; the trust-heavy archetypes reward Capability 3.1 and 1.4. Choose the archetype whose dominant capabilities are your strengths, not the archetype whose title is loudest. [R]

### What is genuinely new vs. relabeled

This is the question most "AI PM" content dances around, and it deserves a direct answer. **[D]** Practitioners genuinely disagree on the split, and there is no measurement that settles it — no validated job-analysis study of what AI PMs actually do versus classical PMs, no controlled comparison of outcomes. The Academy's assessment, labeled as inference, is:

- **Genuinely new, roughly 30-40% of the incremental capability:** evaluation contracts and their monitoring discipline; the severity-weighted failure taxonomy and silent-failure detection; distribution-shift awareness as an operational category; model-vs-system reasoning with its specific sub-frames (retrieval, context, tool-use, inference economics); managing probabilistic performance as a product property rather than an engineering bug; governance of probabilistic systems under a new regulatory surface; and the discipline of designing for graceful failure rather than for zero failure. [I]

- **Relabeled, roughly 60-70%:** problem selection, customer and domain understanding, product judgment, business economics, prioritization and sequencing, cross-functional influence, adoption and change management, executive communication. Every one of these is the same judgment applied to new constraints. [I] A PM who could pick problems, reason about economics, and drive adoption for an enterprise SaaS product can do the same for an AI product once they learn the evaluation and failure-mode material. The reverse is not true: a PM who has only ever learned "AI vocabulary" without the underlying judgment is not a product leader at all. [P]

- **The honest calibration:** the genuinely-new component is concentrated, real, and consequential — but it is small relative to the generalist base, and it is learnable in months, not years, for a PM with strong fundamentals. The marginal value of an "AI PM" over a strong generalist is the size of that new component, not the size of the title. [I]

Two corollaries follow. First, **"AI PM is just PM with a new toolkit" is false** — the new toolkit changes the failure regime you are accountable for, and accountability for silent probabilistic failure is a different job than accountability for deterministic software. Second, **"AI PM is a wholly new profession" is also false** — the load-bearing capabilities are the same ones the Academy has always taught, and a PM who masters evaluation contracts but cannot do problem selection is not a product leader; they are a QA-specialist with a model. Both simplifications are marketing, and neither survives contact with a real P&L. [D]

### How AI PM differs from classical PM, in operational terms

The difference shows up in the daily operating cadence, not in the title. Four differences matter:

1. **The definition of "done" is probabilistic.** Classical PMs ship features and measure usage. AI PMs ship a system whose behavior cannot be fully specified in advance, and they are accountable for a *performance distribution* — a task-success rate, a severity-weighted error rate, a rollback threshold — not a feature checklist. The evaluation contract is the acceptance criterion, and it lives for the life of the product, not until launch. [I]

2. **Degradation is a standing operational risk.** A classical product degrades when someone ships a regression. An AI product degrades when the world changes — user behavior shifts, the model provider updates a model, a data source changes — and no one changed anything on your side. Distribution shift is not an incident; it is a background condition you must monitor. [E] See [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md).

3. **The system, not the model, is the unit of management.** Benchmarks measure the model; the product is the system. The AI PM's job is to keep the system performing in product terms — latency, cost per task, severity-weighted error rate, human-escalation rate — which requires reasoning across retrieval, orchestration, validation, and fallback layers, not just "which model." [P] See [MODEL_VS_SYSTEM.md](../05_ai_product_management/MODEL_VS_SYSTEM.md).

4. **Trust is measured and managed as a product property.** You do not assume adoption because the model is impressive; you design for verification, transparency, and recourse, and you measure the trust-destroying failure of overpromising. [E] See [ADOPTION.md](../05_ai_product_management/ADOPTION.md).

There is a fifth difference worth naming, because it appears on every one of the AI-adjacent roles in this file: **the cost structure of being wrong is no longer linear and local.** A classical bug affects one user, one screen, one transaction, and is bounded by the feature. An AI failure can propagate — a bad retrieval poisons a summary, a cascading agent error compounds across steps, a feedback loop entrenches a bad behavior at scale. The AI PM's risk judgment operates on a different blast-radius distribution. [I]

### The capability profile of a strong AI PM

Mapped to the capability model ([CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md)), a strong AI PM is:

- **Capability 1.6 (Data and Evaluation Fluency)**, elevated to the central capability: offline metrics, online metrics, human evaluation, severity weights, distribution-shift detection. This is the capability that separates AI PMs from PMs who manage AI products. [I]
- **Capability 1.5 (Technical Fluency)**, extended to model evaluation, retrieval, context assembly, tool-use, and inference economics — the difference between model capability and product capability. [I]
- **Capability 1.8 (Risk Judgment)**, extended to probabilistic and model-safety risk, which is novel and poorly understood. [P]
- **Capability 1.1 (Problem Selection)**, with the added skill of distinguishing "the model can't do this yet" from "this will never work," and of knowing when AI is the wrong answer entirely ([WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md)). [I]
- **Capability 2.4 (Outcome Ownership)**, extended to distinguishing model quality from product quality from business impact. [P]
- **Capability 3.1 (Adoption and Change Management)**, extended to trust-building for probabilistic systems. [I]

The pattern is visible: the genuinely-new load is concentrated in evaluation, failure-mode, and system reasoning. Everything else is the generalist base. This is the single most useful fact in this file for a PM deciding where to invest. [R]

### Agentic products and eval-driven design

The most consequential frontier of AI PM is agentic and eval-driven products, and it deserves treatment here rather than only in the "beyond AI" section, because it is where the genuinely-new component of AI PM grows largest. [I]

An agentic product — a tool-using, multi-step system — has properties that even a single-call AI feature does not: it can take actions with real-world consequence, its errors compound across steps, and its behavior is too complex to specify procedurally. The product consequence is that **the evaluation suite becomes the product specification.** [P] You cannot write a PRD that specifies what a capable agent does across an open state space; you can only define the evaluation suite that measures whether it behaves acceptably, and then hold the system to it. This is eval-driven product design, and it is the clearest genuinely-new practice in the entire emerging-role landscape. [I]

The capability demands are correspondingly new. The PM must reason about agent architecture as a product concern — when agents add value versus when a deterministic workflow suffices, how to bound agent authority, where human-in-the-loop checkpoints go, how the system observes and recovers itself ([AGENT_ARCHITECTURE.md](../05_ai_product_management/AGENT_ARCHITECTURE.md)). They must extend the failure taxonomy to cascading failures, tool-permission errors, cost explosion, and feedback-loop degradation ([FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md)). And they inherit the maximum tier of the governance pyramid, because agentic action with consequence is where autonomous decisions affect safety, rights, and financial standing ([GOVERNANCE.md](../05_ai_product_management/GOVERNANCE.md)). [I]

The skeptical note is the same as everywhere in this file: the *capability* is real and durable, but the *role* is not yet distinct. Most of what is sold as "agent PM" or "AI-native PM" is AI PM with higher stakes and more vocabulary. The practitioners who succeed in agentic products will be the ones with evaluation discipline; the ones who fail will be the ones who mistook tooling fluency for product capability. [D]

---

## Beyond AI: Other Emerging Specializations

The five specializations below are the ones most commonly cited as emerging. For each: what it is, what capability it demands, and how durable it is. The pattern from AI PM repeats: real capability at the core, relabeled framing at the edges, and titles running ahead of capability.

### Platform / API Product Management

**What it is.** Managing the product that is consumed by other products: the API, the developer platform, the internal platform, the marketplace infrastructure. In the current wave, this includes agent-facing APIs — surfaces built to be called by AI agents, not only by humans — and platform products whose consumers are other teams. This is not a new role; the platform is Archetype 3 in [archetype_catalog.md](../04_product_archetypes/archetype_catalog.md), and platform PM has existed for two decades. What is genuinely new is the expansion of the consumer class (from "other developers" to "other developers plus autonomous agents") and the corresponding new evaluation burden — an API's contract now includes behavior under agentic call patterns, cost-at-scale per call, and reliability expectations that a machine consumer cannot tolerate gracefully. [P]

**What capability it demands.** Technical fluency (Capability 1.5) at the highest level of the emerging set — you must reason about distributed systems, API design, versioning, backwards compatibility, and blast radius. Customer and domain understanding (Capability 1.3) with the "customer" being internal teams and external developers whose workflows are technical. Data and evaluation fluency (Capability 1.6) for the notoriously hard-to-measure outcomes of internal adoption and developer productivity. Risk judgment (Capability 1.8) for breaking changes with cascading blast radius.

**The platform discipline that transfers.** Platform PM is where the durability of the generalist base is easiest to see, because the platform has been a distinct archetype long enough to accumulate genuine practice. The capabilities that make a platform PM good — sequencing platform capabilities against consumer readiness, refusing premature abstraction, measuring internal adoption honestly, managing blast radius of breaking changes — are documented in [archetype_catalog.md](../04_product_archetypes/archetype_catalog.md) and in the Principal+ organizational-design material ([Module 02](../02_principal_plus/README.md)). None of this was invented by the AI wave. The AI wave added one new sub-problem: designing surfaces for machine consumers whose behavior you cannot fully predict, which folds into the evaluation discipline rather than replacing it. [I]

**Durability assessment.** **[I]** High. Platform economics are structural — the shift from applications to infrastructure and the growth of machine-consumed interfaces rest on durable technical change, not on a funding wave. The "emerging" label on this role is mostly relabeling an established specialty. What is genuinely new (agent-facing surfaces, inference-cost-aware API design) is an extension of an old discipline, not a new one. A PM considering this track is not betting on hype; they are betting on a century-old pattern of platform economics. [I]

### Developer-Adjacent Product Management

**What it is.** Product work for the people who build: developer tools, dev experiences, internal AI tooling, developer relations as a product function, and "productizing" the internal platform. This includes the large current wave of internal AI developer tooling — coding assistants, code review agents, internal "AI engineer" infrastructure — where the product is a developer-facing surface.

**What capability it demands.** Deep technical empathy and domain understanding of developer workflows (Capability 1.3 and 1.5); product judgment that manifests as API elegance and documentation quality rather than visual polish (Capability 1.4); adoption architecture for a user population that is technically sophisticated, skeptical, and sensitive to disruption of existing workflows (Capability 3.1). When the developer tool embeds a model — as coding assistants do — it inherits the full AI PM evaluation load: evaluation contracts for code-generation quality, failure-mode management for silently-wrong code, and trust management for a user base that will detect and punish unreliability immediately. [I]

**The specific new dynamic: evaluation of code generation.** Code-generation products are the purest case of the silent-failure problem, because the output looks plausible to exactly the audience least equipped to catch it — a developer reviewing AI-generated code that compiles and runs and is subtly wrong. The PM of such a product must design for verification, not trust: test harnesses, review checkpoints, and honesty about what the tool cannot be trusted to do. The durable capability here is not "developer relations"; it is evaluation-plus-adoption applied to the developer as the user. [P]

**Durability assessment.** **[I]** Medium-high for the capability, low-medium for the novelty of the title. Developer-tools PM is Archetype 6 in [archetype_catalog.md](../04_product_archetypes/archetype_catalog.md) — an established specialty. What is new is the AI layer: the evaluation of probabilistic code generation, and the collapse of "developer relations" and "developer tools" into a single product surface as adoption of internal AI tooling becomes a product problem rather than a training problem. The durable capability is the generalist base plus technical fluency plus the AI evaluation layer; the title "developer-adjacent PM" is likely to dissolve back into "developer tools PM" once the AI tooling wave matures. [I]

### Data Product Management

**What it is.** Managing data as a product: the datasets, feature stores, analytics surfaces, and internal data infrastructure that other products and teams consume. In the AI wave, this has expanded to include the data layer of AI systems — training/evaluation data, retrieval corpora, evaluation sets — where the quality of the data is the quality of the product. [P]

**What capability it demands.** Data and evaluation fluency as the central capability (Capability 1.6) — data contracts, quality measurement, lineage, governance of data as an asset. Cross-functional influence (Capability 2.2) with engineering and data-science counterparts. Customer and domain understanding of internal consumers (Capability 1.3). Risk judgment for data privacy and governance (Capability 1.8). Where the data product feeds a model, it inherits the AI evaluation discipline: distribution shift, drift detection, and the data flywheel assumptions in [WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md).

**The genuinely-new core: data as the evaluation surface.** For AI products, the data layer is no longer plumbing; it is the evaluation surface. A retrieval corpus with stale or poisoned entries degrades the product silently. An evaluation set that does not rotate allows overfitting to the canary. The PM who owns the data layer owns a piece of the product's quality that did not exist in classical products. This is a real extension, and it is where "data product manager" acquires a claim to novelty it did not have a decade ago. [I]

**Durability assessment.** **[I]** Medium. Data products are real and established (the analytics/data archetype is Archetype 12 in [archetype_catalog.md](../04_product_archetypes/archetype_catalog.md)), but "data product manager" has historically blurred with analytics PM, data engineering, and program management. The durable part is the governance and economics of data as an asset — that is structural. The non-durable part is the title's novelty: it has been "emerging" for over a decade and still does not have a settled boundary against analytics, BI, and data engineering. Treat this track as real capability with a contested title. [I]

### Workflow / Automation Product Management

**What it is.** Product work on automating knowledge work: process decomposition, automation of multi-step workflows, robotic process automation's AI successor, and the current crop of "AI employee" and workflow-automation products. The defining skill is workflow decomposition — breaking a real human workflow into subtasks and deciding, task by task, whether AI, a deterministic system, or a human should perform it, with the unit economics made explicit. [P]

**What capability it demands.** This is the most *process-capability-heavy* specialization: customer and domain understanding of the target workflow in detail (Capability 1.3); business economics of automation — cost per task, error cost, break-even error rate (Capability 1.7); data and evaluation fluency for measuring automated workflow quality (Capability 1.6); adoption and change management for displacing or augmenting human workflows (Capability 3.1). When the automation embeds a model, it inherits the full AI evaluation contract and failure-mode load — silent failures in automated workflows are costlier than silent failures in assisted workflows because no human is in the loop. [I] The methodology lives in [WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md).

**Why the capability is underrated.** Workflow decomposition sounds like process consulting, which sounds like the opposite of a prestigious product track. That is a market mispricing. The automation of knowledge work is one of the largest structural economic changes in the current period, and the person who can decompose a workflow, quantify its unit economics, and decide where automation creates value is doing the highest-leverage work in the set. The capability is durable precisely because it is unglamorous: it does not depend on which model is current, which agent framework is fashionable, or which label the market is using. [I]

**Durability assessment.** **[I]** High for the capability, low-medium for the title. Workflow automation rests on a durable structural change — the cost of automation fell by orders of magnitude, which changes which workflows it is economic to automate. That mechanism is real and will persist. But "workflow automation PM" is a description of activity, not a capability boundary: it will fold into AI PM (for model-based automation) and ops-product/operations roles (for the process and change-management half). The durable bet is the capability — workflow decomposition plus unit economics of automation — not the title. [I]

### AI-Native / Agent Product Management

**What it is.** Managing products whose core is an autonomous agent: tool-using systems that plan and take multi-step actions, multi-agent systems, and "eval-driven" products where the product's behavior is defined by its evaluation suite. This is the most hyped and least defined of the emerging labels.

**What capability it demands.** The genuinely-new core: agent architecture as a product concern — when agents add value versus when a deterministic workflow suffices, how to bound agent authority, human-in-the-loop placement, observability and recovery for multi-step systems ([AGENT_ARCHITECTURE.md](../05_ai_product_management/AGENT_ARCHITECTURE.md)). Eval-driven product design, where the evaluation suite *is* the product spec — a real and consequential shift, because an agent's behavior is defined by what you can measure about it, and the evaluation contract becomes the only mechanism for specifying behavior. [P] Cascading-failure awareness, because an error in one component propagates through the whole chain. Risk judgment at the highest severity end of the governance pyramid ([GOVERNANCE.md](../05_ai_product_management/GOVERNANCE.md)), since agentic action with consequence is where the maximum-governance tier applies.

**The hype-to-capability ratio.** This is the specialization where the gap between the market's pricing and the underlying capability base is largest. Job postings for "agent PM" demand vocabulary: fluency with agent frameworks, orchestration patterns, tool-calling conventions. The capability that actually determines outcomes — the ability to write an evaluation contract for a multi-step system, to design bounded authority, to specify recovery — is rarely screened for, because it is hard to screen for and the vocabulary is easy to screen for. [P] The market is therefore selecting, at the margin, for the wrong thing. The candidate who can articulate where an agent's evaluation suite would fail, and what the human-in-the-loop design should be, is worth several of the candidates who can name the frameworks. [R]

**Durability assessment.** **[I]** This is the clearest case of titles running ahead of capability. The *capability* is durable — agent systems are a real product category with real, documented failure modes (cascading failures, tool-use permission errors, cost explosion, feedback-loop degradation in [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md)) — and the evaluation discipline for agentic systems will become a permanent part of AI PM. The *title* and the *hype* are not durable. Most "agent PM" job postings demand vocabulary rather than capability: fluency with agent names and frameworks without the ability to write an evaluation contract for a multi-step system. The honest assessment is that agent PM is a sub-specialty of AI PM, not a new profession, and the practitioners who succeed in it will be the ones with evaluation discipline, not the ones with the most agent vocabulary. [D] Practitioners split on this: some genuinely believe agentic systems require a new discipline (multi-agent coordination, permission architecture, recovery design are not trivial), and others hold that it is AI PM with higher stakes. The Academy's position is that the capabilities are new-ish and consequential but the *role* is not yet distinct enough to be its own track. [I]

### How these specializations interact

The five specializations are not five separate ladders; they are five overlapping profiles over the same base, and the overlap matters more than the boundaries. [I] A platform PM who owns an agent-facing API is doing AI PM. An AI PM who owns the retrieval corpus is doing data product PM. A workflow-automation PM whose automation embeds a model is doing AI PM with a process lens. Developer-adjacent PM inherits the entire AI evaluation load when the devtool embeds a model. The specializations are *aspects* of a portfolio, not silos, and the strongest practitioners move between them as the work requires. [I]

This has two consequences for a career. First, the overlap is a hedge: a PM who develops evaluation fluency and workflow decomposition is simultaneously positioned for four of the five tracks, because those two capabilities sit at the intersection of all of them. [I] Second, the overlap is a warning about titles: a specialization defined as a boundary will misallocate you, because the work does not respect the boundary. Position for the intersection, not the silo. [R]

### A brief history of role waves

The durability test becomes sharper with history, because the pattern is old. [P] Over the past three decades, the market has periodically declared that product management was splitting into a new permanent taxonomy. Each wave produced titles, then blurred them:

- **The "growth hacker" wave.** Growth was declared a distinct discipline, then absorbed into general PM as experimentation became table stakes. The capability survived; the title vanished. [P]
- **The "API / platform PM" wave.** API product management was declared emerging, then became platform PM, which was declared emerging again when agent-facing surfaces arrived. The capability accumulated; the title kept being reissued. [P]
- **The "data / big data PM" wave.** Declared emerging, never settled its boundary against analytics and data engineering, and is still being declared emerging today. The capability survived; the title never consolidated. [P]
- **The "AI PM" wave, current.** Being declared emerging now, with the same structure as its predecessors: real capability at the core, relabeled framing at the edges, and a title market running ahead of the capability base. [P]

The lesson of the history is not that every wave is hype; it is that every wave overstates the novelty of its titles and understates the durability of its capabilities. The "growth hacker" capability — experimentation fluency — is now a core expectation. The "API PM" capability — platform economics — accumulated into a permanent archetype. The capability was the durable part every time, and the title was the repriceable part every time. [I] The pattern is consistent enough to be the strongest inference in this file: the current AI wave will follow the same shape, with evaluation discipline and workflow decomposition as the capabilities that survive into the base, and the specialized titles as the labels that blur. [I]

---

## Durable Bets vs. Hype

The central question for a PM allocating the next several years of their career: which of these specializations rests on durable structural change, and which rests on a wave? The evidence-honest answer is that we cannot know with certainty — none of these tracks has been measured end to end, and every durability claim below is **[I]** (inference) or **[P]** (doctrine). But the reasoning that separates a durable bet from a wave is available, and it is a reasoning skill, not a data lookup.

### The durability test

Apply three tests to any specialization claim:

1. **The structural-change test.** Does the specialization rest on a change in how value is created (durable), or on a change in funding, attention, and hiring (a wave)? A change in the *cost structure* of a category — AI lowering the cost of evaluation, automation lowering the cost of workflows — is structural. A change in the *number of job postings* is not structural; it is a lagging indicator of funding. [I]

2. **The disappeared-buzzword test.** If the label vanished tomorrow, would the capability still be needed? Evaluation contracts would still be needed, because AI products still fail silently. Data governance would still be needed, because data is still an asset. A "chief AI officer" or "head of agent products" title would not be needed at all — the work would be absorbed by existing roles. [I]

3. **The base-rate test.** Is there a demonstrated base rate of capability, or only practitioner claims? Documented failure modes and documented regulatory obligations are a base rate. Testimonials about "the AI product leader of the future" are not. The more a claim rests on practitioner assertion rather than on observable constraint, the more it is a wave. [I]

**A worked example of the test.** Take "data product management." Structural change: data became the evaluation surface of AI products, and data governance became regulatory — that is structural. Disappeared-buzzword: if "data PM" vanished, the data-layer work of AI products would still need owning, but it would be absorbed into AI PM and engineering; the analytics half would be absorbed into analytics — the capability survives, the label does not. Base rate: the role has been "emerging" for a decade with no settled boundary — weak base rate. Verdict: real capability, contested title, a medium bet. [I] The same test applied to "AI-native/agent PM" yields: structural change yes (agentic systems are real), buzzword survival partial (the eval-driven capability survives, the "agent PM" label does not), base rate weak (no measured track). Verdict: highest hype-to-capability ratio in the set. [I]

### The assessment, specialization by specialization

- **AI product management.** **[I]** Durable capability, semi-durable title. The underlying change is structural: probabilistic software has different failure economics than deterministic software, and that does not revert. But the *separate track* is contestable — as evaluation tooling standardizes and general PMs absorb evaluation contracts and failure-mode literacy the way they absorbed mobile constraints, the marginal value of the separate label will shrink. The bet is durable if you bet on the capability; it is a wave if you bet on the title. This is the most defensible bet of the set, with the caveat that the career itself is unproven. [I]

- **Platform / API product management.** **[I]** Durable, but mostly relabeled. Platform economics are the most structurally-grounded bet here — the platform is a two-decade-old archetype. The "emerging" component (agent-facing surfaces, inference-cost-aware design) is a real extension but a small increment over an established discipline. Lowest hype, highest durability. [I]

- **Developer-adjacent PM.** **[I]** Durable capability, moderate novelty. The AI developer-tooling wave has a real product core (evaluation of code generation, devtools-as-product adoption), but the role dissolves into the established developer-tools archetype. Bet on technical fluency and the AI evaluation layer; do not bet on the label. [I]

- **Data product management.** **[I]** Semi-durable. Data governance and data economics are durable; the title is not — it has been "emerging" for a decade without settling its boundary against analytics and data engineering. Real capability, contested label. [I]

- **Workflow / automation PM.** **[I]** High-capability durability, low title durability. The change in the cost of automation is structural and large. But the title is a description of activity that will be absorbed into AI PM and ops roles. The capability — workflow decomposition, unit economics of automation — is a durable and under-appreciated bet that transfers across roles. [I]

- **AI-native / agent PM.** **[I]** The most hyped, the least defined. The capability core (agent architecture, eval-driven design) is durable but is a sub-specialty of AI PM, not a new profession. Most of the "agent PM" market is vocabulary with no base-rate evidence. Highest hype-to-capability ratio in the set. [D]

### The meta-observation

Across all six, one pattern holds: **the capability is more durable than the title, and the generalist base is more durable than the specialization.** [I] The engineering profession went through the same cycle: when "devops engineer" and "data engineer" labels appeared, the capability survived and the labels blurred. The same will happen here. A PM who invests in the capability — evaluation design, failure-mode literacy, model-vs-system reasoning, platform economics, workflow decomposition — retains the value regardless of which label the market uses at any given time. A PM who invests in the title is renting a label that the market will reprice. [R]

One further skeptical point deserves emphasis: **[P]** the entire "emerging role" discourse is practitioner doctrine operating on a short memory. Every generation of PMs has been told the role was splitting into a new permanent taxonomy; most of those taxonomies did not survive contact with the next technology wave. The durable move is not to predict which label wins; it is to hold the capability that every label on this list requires, which is the same capability model the Academy already teaches. [R]

### What would falsify these assessments

The durability assessments in this section are inferences, and an honest document states what evidence would overturn them. This is the calibration discipline the Academy applies to all claims, applied here to career bets. [R]

The durability assessments would be falsified by:

- **Evidence of a measured, durable track.** If a cohort study or validated job analysis showed that AI PMs systematically out-earn, out-promote, or out-perform generalists with equivalent capability over a multi-year horizon — after controlling for capability, not just label — the strong-reading case strengthens and the "semi-durable title" assessment would be wrong. No such study exists today. [I]

- **Evidence that the capability base does not diffuse.** If evaluation contracts and failure-mode literacy turned out to be genuinely non-transferable — requiring years to acquire, resisting absorption into general PM practice the way some deep technical specializations resist it — then AI PM would be a durable separate track, and the "will dissolve into the base like mobile PM did" hypothesis would be wrong. [I] The early evidence cuts the other way: evaluation thinking transfers readily to practitioners with strong fundamentals, which is why the base-rate of generalists moving into AI PM work is high. [P]

- **Evidence that the wave is not a wave.** If AI product investment proved durable across a full market cycle — through the downturn that every technology cycle eventually brings — the "structural change" label would be confirmed and the "wave" caveat would weaken. Until a full cycle has been observed, the caveat stands. [I]

- **Evidence that agentic systems break the pattern.** If eval-driven products and multi-agent systems demonstrably require a discipline that evaluation-contract-trained AI PMs cannot enter without a distinct multi-year apprenticeship, then "AI-native/agent PM" graduates from sub-specialty to track. The current evidence — that agent failures are extensions of the existing failure taxonomy, not a new species — supports the sub-specialty view, but the agentic field is young enough that this remains genuinely open. [D]

No honest document predicts the future; a calibrated document states what would change its mind. The assessments above are held provisionally, and the falsification conditions are the mechanism for updating them as evidence accumulates. [R]

---

## Positioning Without Chasing Titles

The capability-first position is simple: **position for the work, not the title; build the capability, then let the market attach whatever label it currently uses.** [R] Titles are repriced quarterly. Capability compounds. The practical question is what to build, what to learn, and what evidence to create.

### What to learn

The learning agenda, in priority order:

1. **Evaluation methodology for probabilistic systems.** Master the evaluation contract ([EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md)) and the failure taxonomy ([FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md)). This is the single highest-leverage new capability in the entire emerging-role set, and it transfers across AI PM, agent PM, workflow automation, and even classical roles (any product can benefit from severity-weighted failure thinking). [R]

2. **Model-vs-system reasoning.** Learn to separate model capability from product capability ([MODEL_VS_SYSTEM.md](../05_ai_product_management/MODEL_VS_SYSTEM.md)): retrieval, context assembly, tool use, inference economics, build-vs-buy. This is the analytical frame that prevents the most expensive AI product mistake — buying model benchmarks instead of building system quality. [R]

3. **Workflow decomposition and the unit economics of automation.** Learn to describe a workflow without mentioning AI, decompose it into subtasks, and quantify current cost, error cost, and the break-even error rate of automation ([WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md)). This is the most transferable and least-hyped skill in the set. [R]

4. **The generalist base, unshaken.** Do not skip problem selection, business economics, and adoption in favor of AI vocabulary. The capability model ([CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md)) is the foundation; the emerging-role material is an overlay. A PM who is fluent in evaluation contracts but weak on economics is a technician, not a candidate for leadership. [R]

### What not to learn

The learning agenda has a negative side, and it matters as much as the positive one, because the market's incentives push the wrong direction. [R]

1. **Do not lead with prompt engineering.** Prompting is an implementation detail, not a product strategy, and it is the most relabeled "AI PM skill" on the market. It will not survive as a distinguishing capability — it is a commodity skill with a short half-life, and the [Module 05](../05_ai_product_management/README.md) position is explicit: prompting is one lever among many in the system design, not the PM's craft. [R]

2. **Do not chase model vocabulary.** Knowing the current model names, benchmark scores, and framework conventions is a depreciating asset. It reads as current for about a year and then dates visibly. The durable asset is the reasoning that does not depend on which model is current: evaluation design, failure-mode analysis, system reasoning. [R]

3. **Do not invest in demo-driven development.** The ability to make a model produce an impressive demo is not a product capability; the ability to take a demo to production — with evaluation, governance, and adoption — is. The market rewards demos; the work that creates value is the production discipline. Optimize for the work, not the reward signal. [R]

4. **Do not sacrifice the base for the overlay.** The most expensive mistake in the current wave is a PM who spends two years acquiring AI vocabulary and evaluation tooling at the expense of problem selection, economics, and organizational influence. That PM becomes a technician with good timing. The PM who holds the base and adds the overlay becomes a product leader who happens to manage AI products. The two are not the same asset, and the market will eventually price the difference. [R]

### What to build and what evidence to create

The Academy's standard is that capability is evidenced, not asserted. The credibility-binder logic applies: build durable, public artifacts that demonstrate judgment. [R] For emerging-role positioning specifically, create these:

1. **Evaluation contracts for AI features you know.** Take a feature you have built, or a well-known AI product, and write the full evaluation contract: target workflow, failure taxonomy with severity weights, golden examples, launch and rollback thresholds, monitoring plan. Use the template in [TOOLS.md](../05_ai_product_management/TOOLS.md). This is the single artifact that most separates capability from vocabulary in an interview or promotion process, because it is a judgment artifact, not a knowledge artifact. [R]

2. **Failure-mode teardowns of real AI products.** Pick a widely-used AI product and produce a documented analysis of its failure modes: what silent failures exist, what distribution-shift risk it carries, where its evaluation contract would have to be tightened. A teardown demonstrates that you can reason about failure as a product property rather than a bug report. [R]

3. **A workflow economics analysis.** Take a workflow you own — or one you can observe — and produce the automation economics: current cost per task, error rate, break-even error rate, and the decomposition of which subtasks should be AI, deterministic, or human. This demonstrates the workflow-automation capability that is the least hyped and most transferable. [R]

4. **A model-vs-system analysis.** For an AI product you know, write where the product quality actually comes from: the model, or the system around it (retrieval, context, validation, human-in-the-loop). This demonstrates the analytical frame that separates system thinking from model-fetish thinking. [R]

5. **A capability-model mapping.** Map your current capability profile against the requirement of the specialization you are targeting, using the levels and evidence-of-excellence criteria in [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md). This is the honest gap analysis that prevents title-chasing: you will see precisely what capability the target role actually demands, and which parts of the label are window dressing. [R]

### Use the personal lab

The Personal Lab ([README.md](../12_personal_lab/README.md)) is the natural home for these artifacts. It exists precisely for this: applying Academy doctrine to real portfolio decisions with evidence labels and honest gap analysis. Build the evaluation contracts and teardowns as lab artifacts, revisited quarterly as the evidence changes. The lab's structure — problem thesis, evidence status, principal-level trade-offs, cheapest decisive test — is the same structure an evaluation contract needs, and building them together produces artifacts that are both career evidence and real decision support. [R]

### A worked capability-mapping example

To make the capability-mapping exercise concrete, take a fictional Senior PM with a strong enterprise-SaaS record mapping against the AI PM requirement. [I]

The candidate's current base: Capability 1.1 (Problem Selection) at Senior-to-Principal level, evidenced by a documented record of killing low-value initiatives; Capability 1.7 (Business Economics) at Senior level, evidenced by unit-economic models for their product; Capability 2.2 (Cross-Functional Influence) at Senior level, evidenced by productive sales and success partnerships; Capability 1.6 (Data and Evaluation Fluency) at Senior level, evidenced by well-designed A/B experiments with clean causal reasoning.

Mapping against the AI PM profile from this file, the gaps are concentrated exactly where the genuinely-new capability lives: Capability 1.6 at Principal level (severity-weighted evaluation, distribution-shift detection, human evaluation) and the failure-mode overlay (Capability 1.8 extended to silent and probabilistic failure). The rest of the AI PM profile — problem selection, economics, adoption, influence — is already at or near the required level.

The resulting action plan is precise and small: learn the evaluation contract and failure taxonomy ([EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md), [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md)), build two evaluation-contract artifacts, and the candidate is credibly positioned for AI PM work without a single title change. [R]

The example generalizes. Because the genuinely-new component of every emerging role is small relative to the base, most Senior PMs mapping against an emerging-role requirement will find the same shape: strong on the base, gapped on the evaluation/failure overlay, and a months-long path to closure rather than a years-long one. If the gap is much larger — if the mapping shows gaps in problem selection or economics too — the honest reading is that the emerging role is not the problem; the base is, and the fix is foundational, not specialized. [I]

### The discipline against title-chasing

Three rules keep positioning honest:

1. **Never accept a title as a proxy for capability — yours or the market's.** If the work you are offered is evaluation and judgment under uncertainty, take it regardless of whether the title says "AI PM," "platform PM," or "product manager." If the work is vocabulary and demo-driven development, decline regardless of title. [R]

2. **Let capability define the role, not the reverse.** Apply the durability test to any role you are considering: does the work rest on structural change, survive the removal of the buzzword, and demand capability with a base rate? If yes, it is a bet on capability. If no, it is a bet on a label. [R]

3. **Build evidence before you need it.** The evaluation contract and teardown you build during a search is reactive and unconvincing; the ones you built continuously are evidence of practice. This is the credibility-binder principle applied to emerging roles. [R]

### The counter-argument, taken seriously

The capability-first position has a genuine cost, and it deserves an honest acknowledgment: it can lag a market that is temporarily rewarding titles. For a limited period, a person with the right title will be paid more and promoted faster than a person with the capability and no label, because the market's screening is imperfect and the imperfect screen prices the title. [I] This is real. The response is not to abandon capability-first; it is to price the lag correctly. The lag lasts as long as the wave, and the wave ends when the next wave arrives or when the base rate catches up. A capability-first PM who rides one wave is a specialist whose label expires; a capability-first PM who holds the base and deepens one durable capability rides every wave, because the capability is what the market eventually reprices to. [I] The asymmetry of outcomes — one label that expires versus one capability that compounds — is decisive. [R]

---

## For Leaders: Hiring and Building for Emerging Roles

The same splitting that creates career anxiety for PMs creates a hiring problem for leaders: how do you evaluate capability in a role whose capability definition is unsettled, and how do you build an organization that develops it rather than just labeling it?

### Evaluating candidates for emerging-role capability

The error to avoid is **evaluating vocabulary instead of capability**. Because the titles are ahead of the capability, most interview processes for "AI PM" or "data PM" inadvertently select for fluency with current vocabulary — model names, agent frameworks, evaluation jargon — rather than for judgment. [P] The fix is to evaluate the same way the Academy defines capability: ask for evidence, and probe for judgment under the new constraints.

Five evaluation moves:

1. **Ask for evaluation contracts, not talk.** Ask the candidate to bring an evaluation contract they wrote, or to produce one for a real workflow in an interview. Judge it the way you would judge any product artifact: does the failure taxonomy include severity weights? Are the launch and rollback thresholds specific numbers rather than ranges? Does the monitoring plan detect silent degradation, or only system errors? This separates capability from vocabulary in a way no question can. [R] The standard is in [EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md).

2. **Probe failure-mode reasoning with a concrete case.** Give the candidate a real product — ideally one of yours — and ask them to identify its failure modes and design mitigations. Judge whether they can reason about silent failure, distribution shift, and cascading failure as product properties, or whether they recite a taxonomy without applying it. [R] The taxonomy in [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md) is the reference for what fluency should look like.

3. **Separate model from system.** Ask what fraction of a product's quality comes from the model versus the system, and why. The candidate who says "the model" for most products is model-fetishist and will buy benchmarks instead of building products. The candidate who can articulate the system layers — retrieval, context, validation, orchestration — has the analytical frame that matters. [R]

4. **Test the generalist base, unflinchingly.** Do not let AI vocabulary mask weak fundamentals. Ask the candidate to do problem selection, pricing, or adoption reasoning on a product. An "AI PM" who cannot do economics is not a product leader; they are a specialist who will fail at the portfolio level. [R] The capability model ([CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md)) is the full standard.

5. **Beware the title-inflation screening.** Reject candidates who present titles as evidence, and reject processes that reward title-matching. A candidate with a strong generalist record and a single real evaluation-contract artifact beats a candidate with three "AI PM" titles and no artifacts, because the artifact is evidence and the titles are not. [R]

### A worked evaluation rubric for an AI PM candidate

To make the evaluation concrete, here is a scoring rubric for the artifact-based screen, applicable to any AI-adjacent role. Score each dimension 1-5, with 5 requiring specific, defensible judgment rather than vocabulary. [R]

1. **Failure taxonomy quality.** Does the candidate's taxonomy include severity weights, not just a list? Are the severities justified by consequence (what a severity-4 error actually costs), not by template? A score of 4-5 requires severity reasoning grounded in the domain, not a copied taxonomy. Standard: [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md).

2. **Threshold specificity.** Are launch and rollback thresholds specific numbers with timeframes ("task success below 85% for six hours"), or ranges and intentions ("when quality degrades")? Specificity is the contract being real. Standard: [EVALUATION_CONTRACTS.md](../05_ai_product_management/EVALUATION_CONTRACTS.md).

3. **Silent-failure awareness.** Does the monitoring plan include non-system-error signals — human-review sampling, override rates, downstream metric drift — or only latency and error codes? This is the single most discriminating dimension, because it separates candidates who understand the AI failure regime from those reciting a template. [I]

4. **Model-vs-system reasoning.** When asked where product quality comes from, does the candidate weight the system (retrieval, context, validation, orchestration) or the model? A 5 here requires articulating which system lever they would pull first, and why. Standard: [MODEL_VS_SYSTEM.md](../05_ai_product_management/MODEL_VS_SYSTEM.md).

5. **Generalist base under pressure.** On a problem-selection or economics question unrelated to AI, does the candidate hold the base? A candidate who collapses into AI vocabulary when the AI is removed is a specialist; the role needs a product leader. Standard: [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md).

6. **Governance proportionality.** Asked to govern a use case, does the candidate scale governance to consequence, or apply a one-size-fits-all checklist? A 5 requires reasoning about tiers, human-in-the-loop placement, and when the burden is disproportionate. Standard: [GOVERNANCE.md](../05_ai_product_management/GOVERNANCE.md).

A candidate scoring 4+ on dimensions 1-4 and 3+ on 5-6 is hireable for AI PM work on capability. A candidate scoring high on vocabulary but 1-2 on thresholds and silent-failure awareness is a credentialing hire and will fail at the first incident. [R] The rubric is intentionally artifact-based because artifacts survive the interview; vocabulary does not. [R]

### Building organizations that develop emerging-role capability

The organizational design question is: do you create distinct emerging-role tracks, or do you build shared infrastructure that every product team uses? The evidence-honest answer is that the shared infrastructure is the durable investment, and the distinct tracks are where the hype lives. [I]

Five building moves:

1. **Build evaluation and governance as shared infrastructure, not per-team heroics.** Evaluation contracts, failure taxonomies, monitoring standards, and the tiered governance framework are horizontal capabilities. The organization that creates a shared evaluation practice — templates, review forums, incident processes, audit cadence — multiplies capability across every AI product it builds. The organization that lets each team improvise its own gets a dozen inconsistent standards and a lot of vocabulary. [R] The governance framework in [GOVERNANCE.md](../05_ai_product_management/GOVERNANCE.md) provides the tiered structure; the template in [TOOLS.md](../05_ai_product_management/TOOLS.md) provides the shared artifact.

2. **Carve out distinct roles only where the capability requires it, not for signal.** A dedicated evaluation specialist, a dedicated platform PM, or a dedicated agent-safety owner is justified when the workload and consequence genuinely exceed what an embedded generalist can hold. Creating "chief AI officer" or "head of agent products" titles to signal currency to a board is a governance failure, not an org design. [R] The proportional-governance principle — burden scales with consequence — applies to role design as well as to product risk. [I]

3. **Develop emerging-role capability inside generalist roles first.** The strongest emerging-role talent will come from PMs who managed real AI products, wrote real evaluation contracts, and absorbed the failure taxonomy while holding a generalist portfolio — not from newly-minted specialists hired with vocabulary. Build rotation, allow PMs to deepen in the evaluation direction, and credit the deepening in promotion criteria. [P]

4. **Make the capability model the standard for the emerging roles, not a marketing document.** Define each emerging role as a profile over the existing capabilities with level expectations, evidence of excellence, and false positives — the way every other capability in [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md) is defined. A "senior AI PM" should be defined by Capability 1.6 at the Principal level plus the failure-mode overlay, not by "familiarity with LLMs." This is the anti-hype organizational move: it forces the emerging role to be defined by measurable capability rather than by title. [R]

5. **Design for the principal-plus failure modes of the emerging roles.** The organizational failure of an emerging-role bet is not a bad feature; it is a misallocated portfolio (too much capital chasing a wave), a governance gap (autonomous systems with maximum-consequence risk but minimum-governance controls), or a credentialing failure (promoting on vocabulary). These are Director/VP-level failures, and they are the ones the Principal+ material in [Module 02](../02_principal_plus/README.md) addresses — see [DIRECTOR_VP_TRANSITION.md](../02_principal_plus/DIRECTOR_VP_TRANSITION.md) for the organizational-design framing and [CPO_ROLE.md](../02_principal_plus/CPO_ROLE.md) for the portfolio-level accountability. [R]

### Compensation, ladders, and the credentialing trap

The title inflation of the emerging-role market creates a specific organizational failure inside the performance-management system, and it is a leadership responsibility to resist it. [I] The failure works like this: a wave inflates compensation for labeled roles faster than capability can be verified; the compensation signal then becomes a performance-management signal; and teams start promoting people into labeled roles not because their capability is measured but because the label carries market comp. The result is an internal credentialing system that prices vocabulary. [P]

The fix is to force the compensation and promotion conversation through the capability model. [R] A promotion to "Senior AI PM" should be justified by the same machinery as any promotion: documented capability at the target level, with evidence of excellence and absence of false positives, per [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md). The emerging-role overlay changes the *evidence* — an evaluation contract, a failure-mode analysis — but it does not change the *machinery*. [R] If a promotion package for an AI role cannot produce an evaluation contract or a failure-mode analysis as evidence, it is a credentialing promotion, and it should be treated as such. [R]

Two practical mechanisms help:

1. **Anchor the emerging-role ladder to the existing level definitions.** Do not create a parallel "AI PM I/II/III" ladder with its own criteria; map the emerging role onto the existing Senior/Principal/Director levels with a capability-profile overlay. This prevents the emerging ladder from becoming a separate credentialing currency. [R]

2. **Compensate for capability, not for label scarcity.** Label scarcity is a market signal that will revert; capability scarcity is the durable signal. The leader who pays a premium for the label alone is buying the wave; the leader who pays for demonstrated evaluation and failure-mode capability is buying the asset. The former will be repriced by the market; the latter will be repaid by the products. [I]

### A leadership reflection on the emerging-role question

There is a deeper reason leaders should resist title-driven org design, and it is worth naming. Every wave produces a cohort of leaders who built their credibility on the wave's vocabulary, and a smaller cohort who built it on the wave's capability. When the wave passes, the vocabulary cohort does not quietly disappear; it re-labels, carries the unearned credibility into the next wave, and is rewarded again. [P] The leader who refuses to play that game — who hires for capability, builds shared infrastructure, and defines roles by measurable capability — compounds a different asset: an organization whose judgment survives label changes. That is the entire thesis of the Academy applied to the emerging-role question, and it is the reason the capability-first standard is not merely career advice but leadership doctrine. [R]

### The honest bottom line for leaders

You will be pressured to look current: to create the emerging-role titles, to hire labeled specialists, to present an "AI strategy" that is really a headcount announcement. The evidence-honest response is to be more demanding than the market. [R] Evaluate candidates on the same standard the Academy applies to all capability: evidence over assertion, judgment under the new constraints, and a demonstrable base rate. Build the shared evaluation and governance infrastructure that develops the capability regardless of label. And refuse to let the labor market's title inflation set your capability bar. The organization that does this will hire fewer "AI PMs" and have more working AI products — which is the only outcome that matters. [R]

---

## Practical Application

These exercises are designed to convert the analysis in this file into artifacts. Complete them in order; each builds on the previous.

1. **Write an evaluation contract for an AI feature you know.** Take any AI feature you have shipped, used, or studied. Fill out the full evaluation contract: target workflow, failure taxonomy with at least 8 severity-weighted failure types, golden examples, launch and rollback thresholds as specific numbers, and a monitoring plan that detects silent degradation. Use the template in [TOOLS.md](../05_ai_product_management/TOOLS.md). This is the single most career-relevant artifact in this file.

2. **Produce a failure-mode teardown of a well-known AI product.** Choose a widely-used AI product. Document its likely failure modes using [FAILURE_MODES.md](../05_ai_product_management/FAILURE_MODES.md): what silent failures it could have, what distribution-shift risk it carries, what would trigger a rollback. Write it as a decision memo, not an essay — what would you change about its evaluation contract?

3. **Map your capability model against an emerging-role requirement.** Choose one emerging specialization from this file. Using [CAPABILITY_MODEL.md](../00_orientation/CAPABILITY_MODEL.md), write your current level for each capability the role demands, the evidence that supports that level, and the two capabilities where your gap is largest. This is the honest gap analysis that prevents title-chasing.

4. **Decompose a workflow you own into automation economics.** Take a workflow you know well. Describe it without mentioning AI, decompose it into subtasks, and quantify current cost per task, error rate, and the break-even error rate for automation. Then decide, subtask by subtask, which should be AI, deterministic, or human. Apply the methodology in [WORKFLOW_SELECTION.md](../05_ai_product_management/WORKFLOW_SELECTION.md).

5. **Run the relabeling test on a job posting.** Take a recent posting for an "AI PM," "agent PM," or "data PM" role. List every requirement. Classify each as genuinely-new capability, relabeled generalist capability, or vocabulary. Calculate the percentage in each bucket. Compare your result against the 30-40/60-70 split this file estimates, and justify any difference.

6. **Write a model-vs-system analysis.** For an AI product you know, write where the product's quality actually comes from: the model or the system around it. Identify the two system levers (retrieval, context assembly, validation, orchestration, human-in-the-loop) that would most improve product quality without a model change. Use the framework in [MODEL_VS_SYSTEM.md](../05_ai_product_management/MODEL_VS_SYSTEM.md). Archive exercises 1-6 as artifacts in your [personal lab](../12_personal_lab/README.md) and revisit them quarterly.

---

## Discussion Prompts

1. The splitting of product management is real, but titles are ahead of capability. In your organization, which emerging-role titles exist, and how much of what they do is genuinely new capability versus relabeled generalist work? How would you test that claim?

2. Where do you land on the [D] debate: is AI product management a distinct discipline that will formalize like ML engineering did, or is it a passing label that will dissolve back into general PM as evaluation tooling standardizes? What evidence would change your mind?

3. The 30-40% new / 60-70% relabeled split is this file's inference, not measurement. How would you actually measure the split — what evidence could distinguish genuine new capability from relabeling?

4. Apply the durability test (structural change, disappeared-buzzword, base rate) to a specialization you are considering. Which of the three tests fails for it, and what does that tell you about the bet you are making?

5. For leaders: how do you evaluate a candidate for an emerging role without defaulting to vocabulary screening? What artifact would you ask them to produce, and how would you judge it?

6. For the organization: would you rather hire labeled specialists or build shared evaluation and governance infrastructure that develops capability in generalists? What are the economics of each choice?

---

## Version History

- **v0.2.0 (2026-08-02):** Initial release.
