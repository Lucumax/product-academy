# AI Product Governance: Proportional Frameworks for Real Products

**Status:** v0.1.0
**Depends on:** WORKFLOW_SELECTION.md, EVALUATION_CONTRACTS.md, FAILURE_MODES.md

---

## TL;DR

AI governance is not a compliance checkbox. It is a product design discipline that determines what your AI system is allowed to do, how it accounts for its decisions, how it protects users, and how your organization maintains accountability. Done well, governance is a competitive advantage: it builds user trust, accelerates regulatory approval, reduces incident frequency, and limits liability. Done poorly, it's an after-the-fact scramble that produces documents nobody reads and controls nobody follows.

This file provides a proportional governance framework where the governance burden scales with the risk of the AI use case, not a one-size-fits-all approach.

---

## Part 1: Proportional Governance — The Core Principle

### The Governance Risk Pyramid

```
                    ┌─────────┐
                    │ MAXIMUM │  Autonomous decisions affecting
                    │GOVERNANCE│  human safety, legal rights,
                    ├─────────┤  financial standing, or life
                    │  HIGH   │  opportunities
                    │GOVERNANCE│
                    ├─────────┤
                    │ MEDIUM  │  Decisions with moderate
                    │GOVERNANCE│  consequence, transparency
                    ├─────────┤  required
                    │  LIGHT  │
                    │GOVERNANCE│  Low-stakes decisions,
                    ├─────────┤  informational outputs,
                    │ MINIMAL │  internal tools
                    │GOVERNANCE│
                    └─────────┘
```

### Risk Tier Classification

Before choosing governance controls, classify your AI use case:

| Tier | Description | Examples | Governance Requirement |
|------|-------------|----------|----------------------|
| **Tier 1: Minimal** | No decision-making; informational only; no user-facing AI; internal analytics | Internal code search, automated test generation, log analysis | Basic documentation; no formal governance beyond standard engineering |
| **Tier 2: Low** | User-facing informational outputs; optional AI assistance; user retains control | Grammar suggestions, meeting summaries, content tagging, "you might like" recommendations | Transparency notice; opt-out capability; basic accuracy monitoring |
| **Tier 3: Moderate** | AI recommendations influencing human decisions; AI automates tasks with moderate consequence | Customer support chatbot, resume screening recommendations, content moderation flagging | Evaluation contract; human override; bias testing; regular accuracy audits; user feedback mechanism |
| **Tier 4: High** | AI makes or substantially influences consequential decisions; autonomous action with significant consequence | Loan approval recommendations, insurance underwriting, medical diagnosis support, hiring recommendations, legal document analysis | Full evaluation contract; human-in-the-loop; bias and fairness audits; explainability; regulatory compliance docs; incident response plan; independent audit |
| **Tier 5: Maximum** | AI makes autonomous decisions affecting human safety, fundamental rights, life opportunities; controls physical systems | Autonomous medical treatment decisions, fully automated hiring/firing, autonomous vehicle control, critical infrastructure, law enforcement AI | All Tier 4 plus: mandatory human oversight with veto; real-time monitoring with auto-shutdown; safety case documentation; regulatory pre-approval; continuous third-party auditing; public transparency reporting |

**Note for EU AI Act:** The Act uses a similar tiered approach. Tier 4-5 here roughly maps to "high-risk AI systems" under the Act. Tier 5 may include "unacceptable risk" uses that are prohibited entirely.

### How to Use the Tier System

1. **Classify your use case honestly.** Most teams overestimate their risk tier ("it's just a chatbot") or underestimate it ("it's fine, we have human review"). Classify based on the worst-case consequence, not the average case.

2. **Apply governance requirements for that tier.** Requirements are cumulative — don't skip lower-tier requirements.

3. **Reclassify when the product changes.** A chatbot that starts processing payments moves from Tier 3 to Tier 4. A recommendation system that starts making autonomous decisions moves from Tier 2 to Tier 3. Governance is not a one-time classification.

4. **Err on the side of the higher tier** when uncertain. The cost of over-governing is moderate. The cost of under-governing can be catastrophic.

---

## Part 2: Human Oversight Models

### The Oversight Spectrum

```
   NONE        IN-THE-LOOP       ON-THE-LOOP      IN-COMMAND
   |               |                  |                |
   v               v                  v                v
AI acts        Human reviews     Human monitors    Human decides
autonomously   every AI          AI decisions;     AI advises
               decision          can override      only
```

| Model | Description | When to Use | When NOT to Use |
|-------|-------------|-------------|-----------------|
| **No human oversight** | AI acts independently; no human reviews outputs | Tier 1-2 use cases; trivial consequences of error; internal tools; informational outputs only | Any decision with legal, financial, safety, or rights implications; anything user-facing that could cause harm if wrong |
| **Human-in-the-loop** | Human must approve every AI output before it takes effect | Tier 4-5 use cases; high-stakes decisions; regulated industries; autonomous actions with consequence | High-volume, low-stakes decisions where human review eliminates automation value; real-time requirements where human review latency is unacceptable |
| **Human-on-the-loop** | Human monitors AI decisions in aggregate; can intervene and override; not reviewing every decision | Tier 3 use cases; moderate-stakes decisions; customer-facing AI where user can escalate; content moderation | High-stakes decisions where a single error could be catastrophic; decisions where errors are hard to detect in aggregate |
| **Human-in-command** | Human makes decisions; AI provides analysis, recommendations, or options; human has final authority | Any tier where AI is an advisor, not a decision-maker; strategic decisions; creative work; situations where accountability must rest with a human | Fully automated workflows where human involvement defeats the purpose |
| **Human-in-the-loop-for-exceptions** | AI acts autonomously for standard cases; human reviews only when confidence is low, output is flagged, or user requests escalation | Tier 3-4 use cases with high volume and mostly standard cases; customer support automation; document processing with exception queues | Cases where the AI's confidence signal is poorly calibrated; cases where "standard" vs "exception" distinction is unreliable |

### Designing Effective Human Oversight

Human oversight often fails not because of bad intent but because of bad design. Common failure patterns:

**Failure Pattern 1: Automation Bias — The Rubber Stamp Problem**

When humans review AI outputs, they tend to accept them without scrutiny. This is automation bias: the assumption that "the computer checked it, so it must be right."

Counter-measures:
- Randomly insert known errors into the review queue (calibration checks). Measure whether reviewers catch them.
- Require reviewers to articulate their reasoning for accepting an output, not just a checkbox.
- Track individual reviewer acceptance rates. If someone accepts 99.7% of AI outputs, they're rubber-stamping.
- Rotate reviewers to prevent complacency.

**Failure Pattern 2: Alert Fatigue — Too Many Escalations**

If the AI escalates too many cases to humans, reviewers become overwhelmed and start approving everything to clear the queue.

Counter-measures:
- Calibrate escalation thresholds so only genuinely uncertain/suspicious cases are escalated.
- Measure and limit escalation rate. Target: 5-15% of cases escalated. Above 30%, re-examine your thresholds.
- Prioritize the escalation queue by severity, not first-in-first-out.
- Staff the review team adequately. If reviewers are overwhelmed, add capacity or reduce scope.

**Failure Pattern 3: Skill Atrophy — Human Skills Decay**

When humans primarily review AI outputs rather than doing the task themselves, their own skills decay. Over time, they become less able to detect AI errors because they've lost the capability to do the task independently.

Counter-measures:
- Require humans to complete some tasks independently (without AI assistance) to maintain skill.
- Periodically benchmark human-only performance against AI-assisted performance.
- Rotate between AI-assisted work and independent work.

**Failure Pattern 4: The "Human in Name Only" Review**

The human reviewer lacks the authority, time, or information to meaningfully override the AI's decision, making the review a formality.

Counter-measures:
- Ensure reviewers have the authority to override the AI's output and that their overrides take effect.
- Provide reviewers with the information they need to make an independent judgment (not just the AI's output, but evidence, alternatives, and the AI's reasoning).
- Measure override rate. If it's near zero, investigate whether reviewers feel empowered to override.
- Require a reason for every override acceptance AND rejection.

### The Oversight SLA

For any human oversight arrangement, define:

```
OVERSIGHT SLA:

Review type: [Every decision / Exception only / Sampling]
Target review time: [X minutes from escalation to human review]
Maximum review time: [Y minutes; after this, what happens? Auto-approve? Auto-escalate? Return to user?]
Reviewer qualifications: [What training, certification, or experience is required?]
Reviewer capacity: [How many cases per hour per reviewer? How many reviewers available?]
Override authority: [Can the reviewer override any decision? Are there limits?]
Override documentation: [What must the reviewer document when they override?]
Calibration checks: [How often are known errors inserted? What's the expected detection rate?]
```

---

## Part 3: Agent Permission Models

### The Principle of Least Privilege for Agents

AI agents should have the minimum permissions necessary to perform their function. This is the same principle that governs human access control, applied to non-human actors.

### Permission Dimensions

| Dimension | Question | Example Constraints |
|-----------|----------|-------------------|
| **Read access** | What data can the agent access? | Can read: customer profile, order history. Cannot read: other customers' data, financial records, HR records |
| **Write access** | What can the agent create, modify, or delete? | Can create: support tickets, draft responses. Cannot modify: account settings, billing information, production code without PR |
| **Execute access** | What actions can the agent take? | Can execute: search queries, read-only API calls. Cannot execute: database writes, payment processing, email sending to external recipients |
| **Financial access** | Can the agent spend money, issue refunds, or commit resources? | Max refund: $0 (agent cannot issue refunds). Max discount: 10% (agent can offer discounts up to 10%). Max compute spend: $100/day |
| **User impersonation** | Can the agent act as a specific user? | Agent always identified as AI. Never impersonates a human. Actions attributed to "AI Assistant" not to specific users |
| **Cross-tenant access** | Can the agent access data from multiple users/tenants? | Single-tenant isolation enforced at infrastructure level. Agent cannot access data from User B when serving User A |

### Permission Enforcement

Permissions must be enforced at the infrastructure level, not the prompt level. A prompt saying "do not access financial data" is not a security control. Infrastructure-level enforcement means:

- **API scopes:** The agent's API key has restricted scopes. It literally cannot call the financial data API.
- **Database permissions:** The agent's database user has SELECT on specific tables/views, not on the full database.
- **Tool restrictions:** Each tool the agent can use has built-in parameter validation. A "send email" tool validates that the recipient domain is internal. A "create record" tool validates that the record type is in the allowed list.
- **Rate limiting:** The agent is rate-limited per action type, per user, per time window.
- **Cost limits:** The agent's API calls are capped at a daily budget.

### The Permission Escalation Pattern

Agents may need elevated permissions for specific tasks. Rather than granting permanent elevated access, use a just-in-time escalation pattern:

1. Agent identifies need for elevated permission (e.g., "I need to issue a refund")
2. Agent creates an escalation request with context (order ID, refund amount, reason)
3. Request routed to human approver (or an automated approval system for low-risk cases)
4. Upon approval, agent receives a time-limited, scope-limited elevated permission token
5. Agent performs the action
6. Token expires

This preserves the principle of least privilege while allowing agents to perform higher-permission actions when necessary.

---

## Part 4: Audit Trails

### What to Log

AI systems should maintain audit trails that answer: who/what did what, when, why, and with what result.

| Audit Element | For Human Reviewers | For AI Agents |
|--------------|-------------------|---------------|
| **Identity** | Which human reviewer? | Which agent/agent version? |
| **Action** | What decision or override? | What action was taken? |
| **Input** | What did the reviewer see? (AI output, evidence, alternatives) | What was the input/context at the time of action? |
| **Output** | What was the reviewer's decision? | What was the agent's output/action? |
| **Reasoning** | Why did the reviewer accept/override? | What was the agent's reasoning (chain-of-thought)? |
| **Timestamp** | When did the review occur? | When did the action occur? |
| **Session context** | What was the full interaction? | What was the conversation or workflow state? |
| **Model version** | N/A (human reviewers don't have versions) | Which model version and system prompt version were used? |
| **Confidence** | N/A | What was the model's confidence (if measurable)? |

### Audit Trail Design Principles

1. **Immutable:** Audit records must be append-only with no update or delete capability. Use a write-once data store or append-only log.

2. **Tamper-evident:** It should be possible to detect if audit records have been modified. Cryptographic chaining (like blockchain but simpler) can provide tamper evidence.

3. **Time-synchronized:** All audit records must have accurate, synchronized timestamps. "I think this happened around Tuesday" is not an audit trail.

4. **Complete:** The audit trail must capture the full context of each decision — not just the output, but the inputs, reasoning, model version, and system state that produced it.

5. **Queryable:** Stakeholders (compliance, legal, support, engineering) must be able to query the audit trail efficiently. "We have the logs somewhere" is not governance.

6. **Retained:** Audit records must be retained for a defined period based on regulatory requirements and business need. Define retention periods by use case tier.

### Audit Trail Retention Guidelines

| Use Case Tier | Minimum Retention | Rationale |
|--------------|------------------|-----------|
| Tier 1 (Minimal) | 30 days | Debugging and operational needs only |
| Tier 2 (Low) | 90 days | User dispute resolution |
| Tier 3 (Moderate) | 1 year | Regulatory inquiries, customer disputes, pattern analysis |
| Tier 4 (High) | 3-7 years | Regulatory requirements (financial services: 7 years; healthcare: varies by jurisdiction; employment: varies) |
| Tier 5 (Maximum) | 7+ years or permanent | Critical safety systems, law enforcement applications, fundamental rights decisions |

---

## Part 5: User Trust and Disclosure

### The Transparency Obligation

Users have a right to know when they're interacting with AI and what the AI is doing. This is not just an ethical obligation — it's increasingly a legal one (EU AI Act, California AI transparency laws, etc.).

### Disclosure Requirements by Interaction Type

| Interaction Type | Minimum Disclosure | Best Practice |
|-----------------|-------------------|---------------|
| **AI-generated content** (text, images, audio, video) | Label as AI-generated | Label + provenance information + ability to verify |
| **AI-assisted human work** (AI suggestions, not final output) | Indicate AI involvement | Indicate + explain what AI contributed + human sign-off visible |
| **AI chatbot/conversational agent** | Clear indication that user is talking to AI | Indication + ability to request human + clear statement of AI's capabilities and limitations |
| **AI decision-making** (automated decisions) | Notice that decision was automated + right to human review | Notice + explanation of factors considered + human review process + appeal mechanism |
| **AI behind the scenes** (recommendations, personalization, ranking) | Notice in privacy policy or terms of service | In-context explanation ("You're seeing this because...") + controls to adjust or disable |
| **AI processing personal data** | Notice in privacy policy | Specific consent where required + data processing explanation + opt-out capability |

### The "Explanation Problem"

A common governance requirement is "the system must explain its decisions." This is harder than it sounds:

- **LLM-generated explanations are not ground truth.** When you ask a model "why did you give that answer?", it generates a plausible-sounding explanation — which may or may not reflect the actual reasoning process. The model doesn't have introspective access to its own reasoning; it generates an explanation the same way it generates any text.

- **Complex models have complex reasoning.** A model's output is the result of billions of parameter interactions. There is no simple causal chain to explain.

- **Explanations can be misleading.** A model might explain its decision in terms of factors that didn't actually influence it, or omit factors that did.

**Solutions to the explanation problem:**

1. **Post-hoc explanation with caveats:** "Based on our analysis, the key factors influencing this decision were [factors]. Note: this explanation is an approximation of the model's reasoning and may not capture all factors or their relative importance."

2. **Feature attribution:** For some model types, you can calculate which input features most influenced the output. This is more reliable than LLM-generated explanations but less interpretable.

3. **Counterfactual explanations:** "This decision would have been different if [factor] had been different." Counterfactuals are often more useful than "why" explanations.

4. **Process transparency (instead of output explanation):** "This decision was made by evaluating [criteria list] against [data sources used]. A human reviewer [did/did not] review the decision." This is less satisfying than "why?" but more honest and auditable.

5. **Human review as explanation:** "An AI system recommended this decision. A qualified human reviewed and approved it. Contact [channel] to request further explanation."

**PM principle:** Don't promise perfect explainability that you can't deliver. Be honest about what you can and cannot explain. Process transparency is often more valuable than pseudo-explanations.

---

## Part 6: Privacy and Security

### AI-Specific Privacy Considerations

AI systems introduce privacy risks that traditional software does not:

1. **Training data memorization:** Models can memorize and reproduce training data, including PII, private communications, and proprietary information. This is not a bug — it's inherent to how neural networks learn.

2. **Inference-time data exfiltration:** User inputs sent to AI APIs may be logged, stored, or used for training by the provider. Without proper data processing agreements, sensitive data may be exposed.

3. **Unintended inference:** AI can infer sensitive attributes (health conditions, political views, income) from seemingly non-sensitive inputs.

4. **Cross-user data leakage:** In multi-tenant systems, AI context or fine-tuning may leak data between users.

5. **Prompt injection for data theft:** Attackers can use prompt injection to extract data from the model's context, training data, or connected systems.

### Privacy Protection Framework

| Protection | What It Does | When Required |
|-----------|-------------|---------------|
| **Data Processing Agreement (DPA)** | Contractually binds AI provider to handle data per your requirements | Always when sending data to a third-party AI provider |
| **PII Scrubbing** | Remove personally identifiable information before sending to AI | Tier 3+ use cases with personal data |
| **On-premise/private cloud deployment** | Keep data within your infrastructure | Tier 4-5 use cases; regulated industries; sensitive data |
| **Zero-retention policy** | Provider does not retain or train on your data | Any use case with sensitive or regulated data |
| **Data isolation** | Separate data by tenant/user so no cross-contamination | Multi-tenant products |
| **Differential privacy** | Add noise to data so individual records cannot be reconstructed | Training on sensitive data; publishing model statistics |
| **Synthetic data** | Generate artificial data for training instead of using real data | When real data cannot be used for privacy reasons |
| **Data minimization** | Only send the minimum data necessary for the inference | Always — less data = less risk |
| **Consent management** | Obtain and track user consent for AI processing | GDPR, CCPA, and similar regulations |
| **Data Subject Access Request (DSAR) support** | Ability to locate, export, and delete user data | GDPR, CCPA |
| **Right to explanation support** | Ability to explain automated decisions | GDPR Article 22, EU AI Act |

### Security Considerations Beyond Standard AppSec

AI products have security considerations beyond standard application security:

1. **Prompt injection is a new attack surface.** Traditional WAF rules don't catch it. Input validation designed for SQL injection doesn't catch "ignore all previous instructions."

2. **Model weights are intellectual property.** If you self-host models, model weights must be protected like source code and trade secrets.

3. **Inference APIs are a data exfiltration vector.** A malicious prompt could extract data from the model's context or connected systems.

4. **Training pipelines are attack surfaces.** If an attacker can poison your training data or fine-tuning data, they can control your model's behavior.

5. **Agent permissions create blast radius.** An agent with write access to production systems is a powerful attack vector if prompt-injected.

**Security governance requirements:**

- Threat model your AI system specifically, not just your application generically
- Include AI-specific attack vectors in penetration tests
- Red-team your AI system before launch and periodically after
- Maintain a vulnerability disclosure program for AI-specific vulnerabilities
- Have an incident response plan that covers AI-specific incidents (model compromise, prompt injection attack, training data breach)

---

## Part 7: Regulatory Considerations

### Key Regulatory Frameworks

This is not legal advice. Consult your legal team for compliance requirements specific to your product and jurisdiction.

#### EU AI Act

The EU AI Act (effective in phases through 2026-2027) classifies AI systems by risk and imposes proportional requirements:

| Category | Description | Requirements | Examples |
|----------|-------------|-------------|----------|
| **Unacceptable Risk** | Prohibited entirely | Cannot be placed on the EU market | Social scoring by governments, real-time remote biometric identification in public spaces (with limited exceptions), AI that manipulates human behavior to cause harm, AI that exploits vulnerabilities of protected groups |
| **High Risk** | Permitted with conformity assessment | Risk management system, data governance, technical documentation, record-keeping, transparency, human oversight, accuracy/robustness/cybersecurity | AI in medical devices, vehicles, recruitment, credit scoring, law enforcement, border control, administration of justice, critical infrastructure, education, essential services |
| **Limited Risk** | Transparency obligations | Inform users they're interacting with AI; label AI-generated content | Chatbots, emotion recognition systems, deepfake generation |
| **Minimal Risk** | No specific obligations | Voluntary codes of conduct encouraged | AI in video games, spam filters, inventory management |

**High-risk requirements in detail:**

1. **Risk management system:** Continuous, iterative process throughout the AI system's lifecycle
2. **Data governance:** Training/validation/testing data must be relevant, representative, and free from errors to the extent possible; must account for the specific context of use
3. **Technical documentation:** Must demonstrate compliance with requirements before market placement
4. **Record-keeping:** Automatic logging of events during system operation
5. **Transparency:** Users must be informed they're interacting with an AI system unless obvious
6. **Human oversight:** Measures to enable human oversight must be built into the system
7. **Accuracy, robustness, cybersecurity:** Appropriate levels of accuracy, resilience to errors, security against attacks

**PM implications:**
- If your product is sold in the EU or affects EU persons, the AI Act applies
- High-risk classification adds 6-12 months to launch timeline (conformity assessment, documentation, audit)
- Budget for compliance: external audit, legal review, documentation, ongoing monitoring
- Build compliance into product development, not retroactively

#### GDPR (General Data Protection Regulation)

Key AI-relevant provisions:

- **Article 22:** Right not to be subject to solely automated decisions with legal or similarly significant effects. This means: (a) if your AI makes decisions that have legal or significant effects, and (b) there's no meaningful human involvement, affected individuals can opt out and demand human review.
- **Article 13-15:** Right to meaningful information about the logic involved in automated decision-making.
- **Article 35:** Data Protection Impact Assessment (DPIA) required for processing that is likely to result in high risk to individuals — which covers many AI use cases.

#### US State Laws

- **Colorado AI Act (effective 2026):** Requires developers and deployers of high-risk AI systems to use reasonable care to protect consumers from algorithmic discrimination. Requires impact assessments, disclosure, and adverse decision appeals.
- **NYC Local Law 144:** Requires bias audits for automated employment decision tools.
- **California:** Multiple AI-related bills in progress covering transparency, safety, and discrimination.

#### Industry-Specific Regulations

- **Healthcare (HIPAA):** AI systems handling PHI must comply with HIPAA privacy and security rules. AI diagnosis/treatment recommendations may require FDA clearance as medical devices (SaMD).
- **Financial Services:** AI-driven lending decisions subject to Fair Lending laws (ECOA, FCRA). Model risk management guidance (SR 11-7) applies.
- **Employment:** AI hiring/promotion tools subject to EEOC guidance on disparate impact. NYC Local Law 144 requires bias audits.
- **Insurance:** State-level regulations on AI in underwriting and claims. NAIC model bulletin on AI.

### Regulatory Strategy for Product Leaders

1. **Map your regulatory exposure early.** Which jurisdictions? Which regulations? Which risk tier? Don't wait until launch to figure this out.

2. **Build compliance into the evaluation contract.** Many regulatory requirements (documentation, risk assessment, bias testing, human oversight) overlap with good AI product management. The evaluation contract framework (EVALUATION_CONTRACTS.md) covers most high-risk requirements.

3. **Maintain a regulatory inventory.** Track which regulations apply, which requirements are in-scope, and the status of each.

4. **Budget for compliance.** External legal review, conformity assessment, bias audits, documentation, monitoring. Budget for 5-15% of development cost for Tier 3, 15-30% for Tier 4-5.

5. **Engage regulators early** if your product operates in a novel regulatory space. Voluntary engagement builds credibility and reduces surprise.

6. **Monitor the regulatory landscape.** Subscribe to regulatory updates. Assign someone to track changes. The landscape is shifting rapidly.

---

## Part 8: Organizational Accountability

### Who Is Accountable?

AI governance fails when nobody is clearly accountable. Define accountability explicitly:

| Role | Accountability |
|------|---------------|
| **Product Lead** | Overall AI product governance. Signs off on evaluation contract, risk classification, launch readiness. Accountable for product-level decisions about AI behavior. |
| **Engineering Lead** | Technical implementation of governance controls. Security, monitoring, audit trails, permission enforcement. |
| **Legal/Compliance** | Regulatory compliance. Reviews risk classification, disclosure language, data processing agreements. |
| **Data Science/ML Lead** | Model selection, training data governance, bias testing methodology, evaluation methodology. |
| **Executive Sponsor** | Organizational accountability. Signs off on Tier 4-5 deployments. Owns AI governance budget. |

### Governance Bodies

For organizations with significant AI deployment:

| Body | Composition | Cadence | Responsibilities |
|------|------------|---------|-----------------|
| **AI Governance Committee** | Product, Engineering, Legal, Compliance, Ethics (if exists), Executive Sponsor | Monthly | Reviews new AI use cases, risk classifications, governance exceptions, incident reports |
| **AI Ethics Review Board** | Diverse perspectives: product, legal, ethics, domain experts, external advisors, community representatives | Quarterly or per-use-case for Tier 4-5 | Reviews high-risk use cases for fairness, societal impact, and ethical considerations |
| **AI Incident Response Team** | Engineering, Security, Product, Legal, Communications | On-call rotation, activated on incident | Responds to AI-specific incidents: prompt injection attacks, bias incidents, harmful outputs, model compromise |

### Governance Documentation

| Document | Owner | Update Cadence | Purpose |
|----------|-------|---------------|---------|
| **AI Use Case Register** | Product | Continuous | Inventory of all AI systems in the product, their risk tier, governance status, and evaluation contract |
| **Evaluation Contract** | Product | Per major release or quarterly | Defines success, failure, monitoring, and thresholds for one AI workflow (see EVALUATION_CONTRACTS.md) |
| **Risk Assessment** | Product + Legal | Per major release or regulatory change | Documents risk classification rationale, identifies hazards, assesses severity and likelihood |
| **Bias and Fairness Assessment** | Data Science/ML | Per model change, at least annually | Documents bias testing methodology, results, and mitigation measures |
| **Data Protection Impact Assessment (DPIA)** | Privacy/Legal | Before processing personal data with AI, updated on significant change | GDPR requirement for high-risk processing |
| **Transparency Disclosure** | Product + Legal | Per release | User-facing documentation of AI involvement, its capabilities and limitations |
| **Incident Response Plan** | Security + Product | Annually, updated after each incident | Procedures for detecting, containing, investigating, and recovering from AI incidents |
| **Vendor AI Assessment** | Legal + Procurement | Before contract, annually thereafter | Assessment of AI providers' compliance, data handling, security, and AI governance |

---

## Part 9: Governance by Product Archetype

Different product archetypes (from Module 04) have different governance profiles:

### API Products

**Governance focus:** Data handling, authorization, model extraction prevention, rate limiting, terms of service governing acceptable use.

**Key question:** Are your customers using your AI API for uses you haven't governed? (If you provide a general-purpose AI API, customers will use it for Tier 4-5 use cases whether you intended it or not.)

### Platform Products

**Governance focus:** Multi-tenancy, data isolation, customer-controlled AI behavior, customer accountability for their own AI governance.

**Key question:** Where does your governance responsibility end and your customer's begin? (Document this boundary explicitly.)

### Workflow/Productivity Tools

**Governance focus:** Accuracy, user trust, human-in-the-loop design, disclosure, opt-out.

**Key question:** Are users treating AI suggestions as authoritative when they shouldn't be? (Measure acceptance rate and correlate with accuracy.)

### Consumer Products

**Governance focus:** Content safety, age-appropriate design, transparency, parental controls where applicable.

**Key question:** What happens when a vulnerable user (child, person in crisis) interacts with your AI? (Design for these scenarios explicitly.)

### Regulated Industry Products

**Governance focus:** Full regulatory compliance, audit trails, human oversight, bias testing, documentation sufficient for regulatory submission.

**Key question:** Can you produce the documentation a regulator would request within 30 days? (If not, start building it now.)

---

## Practical Application

1. Classify your AI product or feature using the five-tier risk system. What tier is it? What governance requirements apply?

2. Design your human oversight model. Which model (in-the-loop, on-the-loop, etc.) applies? How will you prevent automation bias and alert fatigue?

3. Define your agent permission model. What can your AI agent read, write, execute? How are permissions enforced?

4. Map your regulatory exposure. Which regulations apply? Which requirements are you meeting? Which have gaps?

5. Assign organizational accountability. Who is accountable for what? Is it documented? Do they know they're accountable?

---

## Discussion Prompts

1. Has your organization classified its AI use cases by risk tier? If not, what's the highest-risk AI use case you have, and why hasn't it been classified?

2. What's your current human oversight model? Are reviewers rubber-stamping AI outputs? How would you know?

3. If a regulator asked you to explain how your AI product makes decisions, could you provide a meaningful explanation? If not, what would you need to build?

4. Does your organization have an AI incident response plan? Has it been tested with a simulated AI incident?

5. Is there an AI governance gap between what your legal team assumes you're doing and what your product team is actually doing? How would you find out?
