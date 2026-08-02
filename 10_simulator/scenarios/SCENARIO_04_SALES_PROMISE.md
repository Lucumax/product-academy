# Scenario 04: Sales Promised an Integration the Architecture Can't Support

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-004 |
| **title** | Sales Promised an Integration the Architecture Can't Support |
| **leadership_level** | Director, VP Product |
| **primary_tension** | Committed revenue vs. architectural reality |
| **key_capability** | Cross-functional negotiation and crisis management |
| **estimated_time** | 45 minutes |
| **related_principles** | PRN-0002 (Strategy Is What You Say No To), PRN-0006 (Technical Debt Decisions), PRN-0007 (GtM and Product Alignment) |

## Situation

You are the **VP of Product** at **SynapseHR**, a mid-market HRIS (Human Resources Information System) platform with 800 customers and $65M ARR. The company is 450 employees, late-stage growth, targeting an IPO in 18-24 months. SynapseHR competes with Workday (upmarket) and BambooHR (downmarket), positioning as the "most configurable HRIS for companies with 500-5,000 employees."

Your platform's core architecture is a monolithic Ruby on Rails application built in 2014. Over the years, the engineering team has extracted some services (payroll engine, time-tracking), but the core HR data model — employee records, organizational hierarchy, compensation bands, performance reviews — remains in the monolith. The monolith serves 8,000+ API requests per minute, has 47 direct database tables in the core schema, and is maintained by a team of 18 engineers who are increasingly vocal about the need for modernization.

### The Problem

Three weeks ago, without involving Product or Engineering, your SVP of Sales, **Brad Morrison**, closed a $3.2M annual deal with **Orion Industries**, a 4,200-employee manufacturing company. The deal included a custom integration requirement: Orion uses **SAP SuccessFactors** for performance management and **ADP Workforce Now** for payroll, and they need SynapseHR to bi-directionally sync employee data between both systems in real time.

Brad's signed contract commits SynapseHR to:
- **Bi-directional, real-time sync** between SynapseHR, SAP SuccessFactors, and ADP Workforce Now
- Employee master data (name, title, department, manager, compensation, employment status) synced within **60 seconds** of any change in any system
- Support for custom field mappings defined by Orion's HRIS team
- Delivery by **Q2 of next year** — approximately 7 months from now

The contract value is $3.2M annual (3-year term, ~$9.6M total). Orion's total contract represents about 5% of ARR — material but not existential. However, Brad has been the company's top revenue producer for 3 years running. He was promoted to SVP Sales 6 months ago. The CEO, **David Park**, announced the Orion deal at the all-hands last week as "proof that we can win enterprise."

### Why This Is a Problem

You learned about the Orion integration requirements when Brad forwarded you the signed contract with a note: "Hey — need engineering scoping on the SAP/ADP integration by Friday. Client kickoff is next week. This is a big one for us!"

Your Principal Architect, **Soren Lindqvist**, reviewed the requirements and came back with a sobering assessment:

1. **The monolith cannot support real-time bi-directional sync.** The core HR data model has no event system. Changes are written directly to database tables with no publish/subscribe mechanism. Building a real-time sync would require either (a) a complete rewrite of the data access layer to add an event system, or (b) database-level change data capture (CDC) with a stream processing layer, which is fragile because business logic lives in the Rails application, not the database.

2. **SAP SuccessFactors API is complex.** It uses a SOAP-based API with OData services. Your engineering team has zero experience with SAP integrations. Soren estimates 4-6 weeks just to understand the API well enough to scope the integration accurately.

3. **ADP Workforce Now is worse.** ADP's API documentation is notoriously incomplete. Several endpoints require certified partner status, which SynapseHR does not have. The certification process alone takes 8-12 weeks according to ADP's partner portal.

4. **Custom field mappings are a product, not a feature.** What Orion wants — the ability for their HRIS team to define custom field mappings without involving SynapseHR engineering — is essentially a configuration engine. Your platform has nothing like it. Building one is a 6-month project on its own.

5. **The 60-second SLA is probably impossible** given the architecture. Even optimistic estimates put end-to-end sync latency at 3-5 minutes with the current monolith. Real-time (<60 seconds) requires the event-driven architecture that Soren has been advocating for 18 months — the same modernization project that's been deferred because "there's no customer demand for real-time."

Soren's bottom line: "To deliver what Brad promised, we need to build the event-driven architecture we've been trying to get funded for 18 months, learn two complex enterprise APIs, build a configuration engine, and do it all in 7 months. That's 12-18 months of work at best, and that's if we stop everything else. This is not a scoping conversation. This is a crisis."

### The Deeper Problem

This isn't the first time Brad has sold something that doesn't exist. In the past 18 months:
- He sold a "global compliance module" that required 9 months of unplanned engineering work (delivered 4 months late)
- He promised a customer SSO with Azure AD that the platform didn't support (engineering did a heroic 6-week sprint to deliver something partial)
- He sold a "compensation planning module" using a slide deck from a PM who had sketched out a vision but hadn't started building anything

Each time, Brad's response has been some version of: "You guys always figure it out. That's what makes this company great." The pattern is clear: Brad sells first, asks questions later, and counts on Product and Engineering to absorb the risk. So far, it's worked — the company has grown from $18M to $65M ARR in 3 years. But each crisis rescue has added architectural shortcuts, technical debt, and engineer burnout.

Your Director of Engineering, **Maria Gonzalez**, pulled you aside last week: "I have two senior engineers who told me they're looking because of the last Brad special. If this Orion thing turns into another death march, I'm going to lose people. Good people. The people we can't afford to lose."

## Characters

**David Park (CEO).** Former management consultant. Believes in "bias for action" and "customer obsession." Praised Brad at the all-hands. Has not yet internalized the gap between what was sold and what can be built. Motivated by: growth trajectory, IPO readiness, looking decisive to the board.

**Brad Morrison (SVP Sales).** Top producer. Believes his job is to close deals and your job is to figure out how to deliver. Has a point: every time he's done this before, Product and Engineering have made it work. The pattern has been reinforced. Motivated by: quota, commission, reputation as the person who brings in the big deals.

**Maria Gonzalez (Director of Engineering).** 10 years at the company. Built the original monolith. Knows every technical skeleton in every closet. Deeply respected by the engineering team. At her limit with the "sell first, build later" pattern. Motivated by: engineering team health, technical sustainability, not being the person who says "we can't" (but increasingly forced into that role).

**Soren Lindqvist (Principal Architect).** Joined 2 years ago specifically to modernize the architecture. Has been consistently overruled on modernization priorities. Feels vindicated that the Orion deal proves his point but is frustrated that it took a crisis to validate what he's been saying. Motivated by: architectural integrity, being listened to, building something that won't collapse under its own weight.

**Lisa Tran (VP Customer Success).** Will be responsible for the Orion relationship after the sale. Already nervous about overpromising. Has seen this pattern before — the customer signs based on sales promises, then Customer Success spends 18 months apologizing. Motivated by: customer trust, renewal rates, not being the cleanup crew.

**Orion Industries HRIS team (external).** Not characters you can manage, but they signed a contract with specific commitments. If SynapseHR cannot deliver, they have legal remedies — including contract cancellation, damages, and reputational harm in the HR tech community (which is small and gossipy).

## Constraints

- Signed contract with specific commitments. Legal obligations exist.
- Orion kickoff is next week. Brad has already told them "the engineering team is excited about this integration."
- Q2 delivery target: 7 months from now.
- Engineering capacity: 18 engineers on the core platform, already allocated to roadmap commitments. No slack.
- SAP SuccessFactors and ADP both require partner certifications you don't have.
- The monolith architecture is the bottleneck. Modernization is needed regardless of Orion.
- Maria's team is at risk of attrition if this becomes another crisis project.
- IPO in 18-24 months. Major customer disputes or contract cancellations are disclosure items.

## Your Role

You are VP of Product. You report to the CEO (David). You do not manage Brad — you are peers at the VP level, both reporting to David. You manage the product organization (PMs, design, product operations) and partner with Maria (Director of Engineering) on engineering capacity decisions. You do not directly manage engineering resources, but you influence roadmap and priority decisions jointly with Maria.

You cannot unilaterally cancel the Orion deal — that would require David's approval, and David just celebrated it publicly. You cannot magically make the engineering possible — the laws of physics (and Rails monoliths) apply.

## Response Format

### Part 1: Assumptions

Key areas to address: What is negotiable in the Orion contract? Can the delivery timeline, scope, or SLA be renegotiated? What is Brad's actual leverage with Orion? Does Orion understand what they bought? What is David's appetite for an honest conversation about the gap between sales and product? What is the real attrition risk in engineering?

### Part 2: Decision

Describe your decision with:
- **What you will do.** Immediate actions (this week), medium-term actions (next 90 days), long-term structural changes.
- **What you will NOT do.** What you are explicitly refusing, even under pressure.
- **Sequence of conversations.** Who you talk to first, second, third. What you ask for from each person. What you prepare before each conversation.
- **The Orion conversation.** Who leads it, what is communicated, what alternative is offered.
- **The structural fix.** How do you prevent this from happening again?

### Part 3: Pre-Mortem

Assume your approach failed. 12 months later, the situation is worse, not better. Write a specific pre-mortem with at least 3 distinct failure paths.

---

## Scoring Rubric (Scenario-Specific)

### Cross-Functional Negotiation

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Blames Brad. Proposes "we need to tell Brad to stop doing this." No recognition that Brad's behavior has been systematically reinforced by the organization. |
| 3 | Recognizes that the problem is systemic (not just Brad) and that fixing it requires structural changes to how deals are scoped, approved, and communicated. Proposes a clear escalation path for the Orion situation. |
| 4 | Navigates the peer-to-VP dynamic with Brad: doesn't make him the enemy, but makes the constraints visible. Proposes a deal desk, technical pre-sale review, or other structural mechanism. Designs the conversation with David to make the systemic problem visible without looking like you're undermining Brad. |
| 5 | Reframes the conversation from "Brad broke the rules" to "our go-to-market motion has outgrown our product development capacity, and we need to align them." Proposes changes to sales compensation (penalizing deals that require unplanned engineering), product-sales collaboration process, and executive decision rights. |

### Architectural Triage

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes building the full integration on the monolith ("we'll figure it out like we always do"). Ignores Soren's and Maria's warnings. |
| 3 | Recognizes the architectural constraint. Proposes a scoped-down version of the integration (e.g., batch sync instead of real-time, one-directional instead of bi-directional, standard mappings instead of custom). |
| 4 | Uses the Orion crisis as leverage for the architectural modernization that was already needed. Proposes: "We can deliver a phased approach — batch sync in 7 months on the current architecture, real-time in 18 months on the event-driven architecture. Orion gets a migration path, and we get the architecture investment we've been deferring." |
| 5 | Designes the delivery plan as a series of progressive commitments: 30-day technical discovery (Soren leads), 90-day MVP with limited scope, 180-day phase 2 with expanded scope, 365-day full feature set. Each phase has an explicit success criteria and go/no-go for the next. Customer pays for the discovery phase regardless. |

### Upward Management (CEO Communication)

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Goes to David with "Brad screwed up" — brinksmanship, no plan, asking David to choose sides. |
| 3 | Goes to David with the situation, the constraints, and a recommended approach. Frames the problem as "we have a commitment we need to meet and here's how we can meet most of it." |
| 4 | Anticipates David's concerns (IPO trajectory, board optics, not wanting to undermine Brad publicly) and addresses them preemptively. Proposes a communication plan for the all-hands correction, for the board, and for Orion. |
| 5 | Makes David the owner of the strategic choice, not the referee of a dispute. Frames: "David, you have two choices. Option A: we deliver what Brad sold, which requires stopping 6 roadmap initiatives, hiring 4 engineers, and accepting a 50% chance of missing the Q2 deadline. Option B: we deliver a phased version that meets Orion's core needs in Q2 and the full scope in Q4, which preserves our roadmap but risks Orion walking. Which matters more to you right now — this deal or this year's roadmap?" |

### Structural Prevention

| Score | What We Look For |
|-------|-----------------|
| 1-2 | No structural fix proposed. "We'll have better communication." |
| 3 | Proposes a deal review process where Product/Engineering reviews contracts before signature. |
| 4 | Proposes changes to the incentive system: sales compensation penalized for deals requiring >X person-weeks of unplanned engineering; product and engineering leaders have approval rights on non-standard commitments; a "product-sales council" that reviews pipeline quarterly. |
| 5 | Addresses the root cause: the company's growth strategy has been "sell whatever the customer asks for and figure it out later." Proposes a strategic choice: "Either we formalize this as our business model (build a professional services arm, staff for custom integrations, price accordingly) or we commit to a product-led model (standard integrations only, accept that some deals will be lost). The middle ground is burning out our engineers and accumulating technical debt." |

---

## Facilitator Notes

**Common traps:**
1. Proposing to hire a team of SAP/ADP specialists to solve the problem in 7 months — ignores the hiring timeline, the monolith constraint, and the certification requirement.
2. Proposing to cancel the Orion deal — ignores David's public announcement, Brad's power in the organization, and the legal reality of a signed contract.
3. Proposing "we'll pair-program with the customer" — Orion is not a co-development partner. They bought a product, not a joint venture.
4. Ignoring the pattern. The response must address not just Orion but the systemic "sell first, build later" dynamic that produced this crisis.

**Discussion prompts:**
- If you were Brad, how would you want the VP of Product to handle this situation with you?
- Is Brad the problem, or is Brad a symptom? What would have to change in the organization for Brad's behavior to stop?
- What would you do if David said: "I hear you, but we need this deal. Figure it out." ?
- At what point does the pattern become a cultural problem that requires executive team intervention?

**Related Academy Content:**
- [PRN-0002](../../01_core_doctrine/PRINCIPLES.md): Strategy is what you say no to
- [PRN-0007](../../01_core_doctrine/PRINCIPLES.md): GtM and product alignment
- [Contradiction: Sales promises vs. product reality](../../08_contradictions/)
