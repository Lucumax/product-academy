# Decision Frameworks

## Framework 1: One-Way vs Two-Way Door Decision Classification

### When to Use

Before making any product decision that involves resource commitment, customer-facing change, or strategic direction. Use this framework to determine how much analysis, approval, and reversibility planning a decision requires.

### The Framework

Classify every significant product decision as Type 1 (one-way door) or Type 2 (two-way door):

**Type 1 (One-Way Door):** The decision is irreversible or extremely expensive to reverse. Examples: major architectural choices, brand name changes, pricing model restructuring, entering a new market with significant capital commitment, sunsetting a product with contractual obligations, decisions with regulatory compliance implications.

**Type 2 (Two-Way Door):** The decision is reversible at acceptable cost. Examples: A/B testing a feature, changing a UI flow, adjusting pricing for a segment, launching a feature that can be rolled back, most feature prioritization decisions.

### Decision Rules

For Type 2 decisions:
- Make the decision as close to the information as possible (the team, not the executive)
- Spend no more than 10% of the decision's implementation cost on analysis
- Require a reversal plan (how will we know we were wrong? how fast can we reverse?)
- Standard escalation is not required; inform, don't ask permission

For Type 1 decisions:
- Require broader input (cross-functional, multi-level)
- Spend analysis effort proportional to irreversibility cost
- Require explicit reversibility design (can we make this more reversible?)
- Require a pre-mortem (what would make this decision fail?)
- Escalate to the appropriate level based on the scale of commitment

### Common Failure Modes

1. **Treating Type 2 decisions as Type 1** (over-analysis, slow decisions, executive bottlenecks). This is the most common failure — organizations that apply Type 1 process to Type 2 decisions out of habit, risk aversion, or political dynamics.
2. **Treating Type 1 decisions as Type 2** (under-analysis, catastrophic outcomes). Less common but more dangerous — organizations that apply "move fast" to decisions that cannot be reversed.
3. **Misclassifying decisions** due to organizational incentives (executives classifying decisions as Type 1 to maintain control; teams classifying decisions as Type 2 to avoid oversight).
4. **False reversibility**: claiming a decision is Type 2 when the reversal mechanism has never been tested or would take so long that the damage is done before reversal.

### Example Application

**Decision:** Whether to change the pricing model from per-seat to usage-based.

**Classification:** Type 1. Changing pricing models is hard to reverse — existing customers are on contracts, new customers sign up under the new model, and reverting creates confusion and trust erosion. This decision should involve finance, sales, and executive input, with modeling of multiple scenarios and a phased rollout plan.

**Decision:** Whether to A/B test a new onboarding flow.

**Classification:** Type 2. If the new flow performs worse, revert to the old flow. This decision can be made by the growth team without executive approval, with the constraint that the experiment must have a defined success metric, a stopping rule, and a rollback plan.

### Practice Exercise

Review the last 20 product decisions in your organization. Classify each as Type 1 or Type 2. For each, assess whether the decision process was appropriate to the classification. Identify the most common misclassification pattern and design a process change to address it.

---

## Framework 2: RICE-LM — Prioritization with Leadership Multipliers

### When to Use

When prioritizing across multiple initiatives with competing resource demands. RICE (Reach, Impact, Confidence, Effort) is the standard PM prioritization framework. RICE-LM adds three multipliers relevant to Principal+ decision-making: Leverage, Market timing, and Strategic coherence.

### The Framework

**Base RICE Score** = (Reach × Impact × Confidence) / Effort

- **Reach:** How many users/customers will this affect in a given period? (1-10 scale or quantitative estimate)
- **Impact:** How much will this move the needle for those users? (1 = minimal, 3 = moderate, 10 = massive)
- **Confidence:** How confident are you in the reach and impact estimates? (20% = wild guess, 50% = some data, 80% = validated, 100% = known)
- **Effort:** How much person-time will this require? (person-months or relative scale)

**RICE-LM Multipliers** (each 0.5x to 2.0x, multiply the base score):

1. **Leverage (L):** Does this initiative create capability that enables future initiatives? Building a platform API creates leverage; building a one-off feature does not.
   - 2.0x: Creates reusable platform capability that multiple teams/products will build on
   - 1.0x: Standard initiative with no significant leverage
   - 0.5x: One-off that creates no lasting capability

2. **Market timing (M):** Is there a market window that makes this more or less urgent?
   - 2.0x: Market window closing; competitor moving; regulatory change imminent
   - 1.0x: No particular timing pressure
   - 0.5x: Market not ready; initiative is premature

3. **Strategic coherence (S):** Does this reinforce the product strategy, or does it pull in a different direction?
   - 2.0x: Directly advances the core strategy and makes other strategic bets more likely to succeed
   - 1.0x: Consistent with strategy but not amplifying it
   - 0.5x: Pulls in a different direction; dilutes strategic focus (even if individually attractive)

**Final Score** = Base RICE × L × M × S

### Decision Rules

- Initiatives scoring in the top quartile are candidates for immediate resourcing
- Initiatives scoring in the bottom quartile should be explicitly rejected (not deferred — strategy is what you say no to)
- The multipliers should be debated, not calculated — their purpose is to surface strategic considerations that pure RICE misses
- A high RICE initiative that scores 0.5x on Strategic Coherence is a trap — individually attractive but strategically dilutive

### Common Failure Modes

1. **False precision:** treating RICE scores as objective measurements rather than structured estimates. The framework's value is the conversation it forces, not the number it produces.
2. **Effort gaming:** teams underestimate effort to inflate scores. Require calibration — compare estimated effort to actual effort on past initiatives.
3. **Reach maximization:** optimizing for broad, shallow impact at the expense of deep, narrow impact that may be more strategically valuable.
4. **Leverage inflation:** every initiative claims to create leverage. Require specificity: what exactly will this enable that was not possible before? Who will use it, and when?

### Example Application

**Initiative A:** Build a new reporting dashboard for enterprise customers.
- Reach: 50 customers (5), Impact: moderate (5), Confidence: 80%, Effort: 3 person-months
- Base RICE: (5 × 5 × 0.8) / 3 = 6.67
- Leverage: 1.0x (one-off feature), Market timing: 1.0x, Strategic coherence: 1.0x
- RICE-LM: 6.67

**Initiative B:** Build a public API for core product data.
- Reach: 200 developer teams (7), Impact: high (8), Confidence: 60%, Effort: 6 person-months
- Base RICE: (7 × 8 × 0.6) / 6 = 5.6
- Leverage: 2.0x (platform capability), Market timing: 1.5x (competitor announced similar API), Strategic coherence: 2.0x (platform strategy)
- RICE-LM: 5.6 × 2.0 × 1.5 × 2.0 = 33.6

Despite lower base RICE, Initiative B is strategically the better investment because of its leverage, timing, and strategic coherence.

### Practice Exercise

Take your current prioritized backlog. Score the top 5 initiatives with RICE-LM. Compare the ranking to the current priority order. Where does RICE-LM disagree with the current order? Is RICE-LM revealing strategic considerations that the current process missed, or is the current order correct for reasons RICE-LM does not capture?

---

## Framework 3: The Sunset Decision Framework

### When to Use

When considering whether to discontinue a product, feature, or service that has active users. This framework forces the decision through four gates before the tactical questions of "how" and "when" are addressed.

### The Framework

**Gate 1: Strategic Fit**
- Does this product/feature serve the current product strategy?
- If we were building our product portfolio from scratch today, would we include this?
- Is this product consuming resources (engineering, support, executive attention) disproportionate to its strategic value?
- If the answer to the first two questions is "no" and the third is "yes," proceed to Gate 2.

**Gate 2: User Impact Assessment**
- How many active users? (Distinguish: registered vs. monthly active vs. daily active)
- What is the user profile? (Enterprise with contracts? Consumer free users? Internal teams?)
- What is the emotional attachment level? (Beloved power-user tool? Utility with no loyalty?)
- What is the cost of graceful transition? (Data export? Migration path? Extended sunset period?)
- If the user base is small OR the user base can be gracefully transitioned at acceptable cost, proceed to Gate 3.

**Gate 3: Trust Cost Calculation**
- How will this sunset affect user trust in other products?
- Are there influential users (journalists, developers, power users) whose reaction will amplify?
- Is there a third-party ecosystem dependent on this product/API?
- What is the minimum viable graceful sunset — what must we do to preserve trust?
- If the trust cost is acceptable OR can be managed through graceful sunset, proceed to Gate 4.

**Gate 4: Reversibility and Alternatives**
- Can the product be transitioned rather than killed? (Open-sourced? Transferred to a partner? Reduced to maintenance mode?)
- If we sunset and later regret it, can we reverse? (Code still exists? Users would come back?)
- Is there a strategic scenario (acquisition, pivot, market shift) where this product becomes valuable again?
- If the product cannot be transitioned and reversal is unlikely to be needed, proceed to execution.

### Decision Rules

- If the product fails Gate 1 but passes Gates 2-3, consider transitioning rather than killing (open-source, transfer, maintenance mode)
- If the product passes Gate 1 but is under-resourced, the problem is resource allocation, not sunset
- If the product fails Gate 1 and the trust cost (Gate 3) is high, invest in a graceful sunset — the trust cost of a bad sunset exceeds the engineering cost of a good one
- If the product fails all gates, sunset with the minimum viable graceful process

### Common Failure Modes

1. **Strategic avoidance:** the product clearly fails Gate 1 but the organization avoids the decision because it is politically difficult.
2. **User minimization:** underestimating the user base, the emotional attachment, or the influence of the users who remain.
3. **Trust cost denial:** assuming "users will get over it" without evidence.
4. **Sunset as the default for any non-strategic product** without considering transition options.
5. **Perpetual maintenance mode:** keeping the product alive with zero investment because nobody will make the sunset decision — the worst outcome for users (product degrades) and the organization (resources consumed).

### Example Application

**Product:** An internal analytics dashboard built 3 years ago, used by 40 people across 3 teams, consuming one engineer at 20% for maintenance. New company-wide analytics platform is being rolled out.

- Gate 1 (Strategic Fit): No — redundant with new platform. Proceed.
- Gate 2 (User Impact): 40 internal users. Low emotional attachment. Data export via CSV is sufficient. Cost: 1 week of engineering for export and redirect. Proceed.
- Gate 3 (Trust Cost): Internal users. Trust cost is low. Communicate the new platform and migration timeline. Proceed.
- Gate 4 (Reversibility): Code exists but would not be revived. Transition: migration to new platform. Recommend sunset with 60-day notice, data export, and migration support.

### Practice Exercise

Identify a product or feature in your organization that is a candidate for sunset — something that exists, has users, but is not strategic. Apply the Sunset Decision Framework. Where does it get stuck? (Usually Gate 1 is clear but Gate 2-3 create organizational resistance.)

---

## Framework 4: The Build-Buy-Partner Decision Framework

### When to Use

When deciding whether to build a capability internally, buy a third-party solution, or partner with another company to provide the capability. This framework goes beyond the standard "build if it differentiates, buy if it doesn't" to account for long-term optionality, organizational capability development, and ecosystem dynamics.

### The Framework

Evaluate the decision across five dimensions. Each dimension scores toward Build (B), Buy (Bu), or Partner (P). The overall recommendation is the weight of the evidence, not a mechanical tally.

**Dimension 1: Strategic Differentiation**
- Is this capability a source of competitive advantage for your product?
- Would having this capability in-house enable product decisions that buying would constrain?
- Does this capability control the user experience in a way that matters?
- **B:** High differentiation — this is why customers choose us
- **Bu:** Low differentiation — this is infrastructure, not product

**Dimension 2: Time-to-Capability**
- How fast do you need this capability?
- Is there a market window that would close during a build?
- Is the build timeline predictable or uncertain?
- **Bu:** Need it now; build would take too long
- **B:** Build timeline is acceptable and the capability is not urgently needed

**Dimension 3: Build Competence**
- Does your organization have the skills to build and maintain this?
- Would building this develop organizational capability that is valuable for future products?
- Is the domain one where your engineers would be effective or would they be learning from scratch?
- **B:** Organization has relevant competence; building develops valuable capability
- **Bu:** No relevant competence; building would be a distraction from core work

**Dimension 4: Vendor Risk**
- Is the vendor market competitive (multiple vendors) or concentrated (one dominant vendor)?
- What is the switching cost if the vendor raises prices, changes terms, or is acquired?
- Does the vendor's roadmap align with your product's needs?
- **B:** Vendor risk is high (single vendor, high switching cost, misaligned incentives)
- **Bu:** Vendor market is competitive, switching costs are acceptable, exits exist

**Dimension 5: Long-Term Optionality**
- Does owning this capability create options for future product directions?
- Would building now be cheaper than buying now and building later if you need more control?
- Is this capability likely to become MORE differentiating over time?
- **B:** Owning creates valuable optionality; differentiation likely to increase
- **Bu:** Unlikely to become differentiating; buy now, switch later if needed

**Partner (P) Consideration:**
- Is there a partner who can provide the capability while you build organizational knowledge?
- Is this a capability where a joint go-to-market creates more value than either build or buy alone?
- Partner is often the right intermediate step: partner now, build later if it becomes differentiating.

### Decision Rules

- **Default to Buy** unless differentiation, competence, and optionality all favor Build
- **Partner** is the right choice when time-to-capability is urgent, build competence is developing, and vendor risk is manageable through partnership terms
- **Build** requires at least 3 of the 5 dimensions to strongly favor Build. One dimension weakly favoring Build is not enough.
- **Re-evaluate annually**: build decisions age into maintenance burdens; buy decisions accumulate vendor risk; partner decisions require relationship management

### Common Failure Modes

1. **Not-invented-here:** building everything because the organization values building over buying, even for commodity capabilities.
2. **Buy-and-forget:** buying a solution but failing to invest in integration, adoption, and ongoing vendor management — the tool is purchased and never deployed.
3. **Build without TCO:** accounting for build cost but not maintenance cost. The total cost of ownership for internally built capabilities is typically 3-5x the initial build cost over 5 years.
4. **Vendor lock-in denial:** assuming that because there are alternatives today, there will always be alternatives. Markets consolidate. Vendors get acquired.
5. **Partner as avoidance:** using "partnership" as a way to avoid making the build-vs-buy decision.

### Example Application

**Decision:** Build or buy a customer support ticketing system for an enterprise SaaS product.

- Differentiation: Low (every SaaS company has a ticketing system). Buy.
- Time-to-capability: We need it for the enterprise launch in 6 months. Build would take 9+ months. Buy.
- Build Competence: We do not have support operations engineers. Building would be a distraction. Buy.
- Vendor Risk: Many vendors (Zendesk, Intercom, Freshdesk, Help Scout). Competitive market. Buy.
- Optionality: Unlikely to become differentiating. If it does, switch later. Buy.
- **Recommendation: Buy.** All five dimensions favor buying.

**Decision:** Build or buy a real-time data pipeline for a data product.

- Differentiation: High — the quality and speed of our data pipeline IS the product. Build.
- Time-to-capability: Customers are asking for it now. Buying an off-the-shelf pipeline might be faster. Build (modified) or Partner.
- Build Competence: We have data engineers. Building develops capability that applies to future products. Build.
- Vendor Risk: Pipeline vendors are consolidating. Confluent dominates Kafka. Medium risk. Build.
- Optionality: Owning the pipeline enables product directions that buying would constrain. Build.
- **Recommendation: Build.** Four of five dimensions favor building. Consider partnering with a vendor for the initial version while building internal capability.

### Practice Exercise

Take a current build-vs-buy decision in your organization. Evaluate it against the five dimensions. Does the framework's recommendation match the actual decision? If not, what is driving the discrepancy — is the framework missing a factor, or is the organization making a decision that the framework would flag as a mistake?

---

## Framework 5: The Strategy Cascade — From Company Strategy to Team Backlog

### When to Use

When translating high-level company strategy into actionable team-level work. This framework addresses the most common strategy failure mode: company strategy that is clear at the executive level but does not actually shape what teams build.

### The Framework

The cascade has five levels. Each level must be explicitly connected to the level above and below. A gap at any level means strategy is not flowing to execution.

**Level 1: Company Strategy**
- What is the company's mission, vision, and strategic position?
- What markets do we serve and not serve? What is our competitive advantage?
- This is the CEO and board level. Product leadership must translate, not create.

**Level 2: Product Strategy**
- Given the company strategy, what is the product strategy?
- What problems do we solve, for whom, and how do we differentiate?
- What are we explicitly NOT building? (Strategy is exclusion)
- What are the 2-3 strategic bets that will define the next 12-24 months?
- Who owns this: CPO/VP Product with CEO alignment.

**Level 3: Product Area Strategy**
- For each product area or domain, how does the product strategy translate?
- What are the specific outcomes this area is responsible for?
- What capabilities must this area develop or improve?
- How does this area's strategy relate to other areas? (Dependencies, shared platform)
- Who owns this: Director/Group PM with VP Product alignment.

**Level 4: Team Objectives**
- Given the product area strategy, what are this team's objectives?
- Objectives are outcomes (what will be true when we succeed), not outputs (what we will build).
- Each objective must trace to a strategic bet or capability from the product area strategy.
- Who owns this: PM with Director/Group PM alignment.

**Level 5: Team Backlog**
- Given the team objectives, what initiatives, experiments, and features will we invest in?
- Each backlog item must trace to a team objective.
- If a backlog item cannot trace to a team objective, why is it in the backlog?
- Who owns this: PM with team input. Director/Group PM reviews for strategic coherence, not tactical decisions.

### The Cascade Test

At any level, ask: "If I showed this to the team at the level below, would they make different decisions than if I showed them the level above alone?" If the answer is no, the cascade is not adding value — the intermediate levels are translation without transformation.

For example: if the product area strategy adds no specificity beyond the product strategy, it is not doing its job. The Director should add: specific outcomes for this area, specific capabilities to develop, specific dependencies to manage.

### Decision Rules

- Strategy at each level should be reviewed quarterly and updated semi-annually
- The cascade should be written, not oral — "everyone knows the strategy" is the most common strategy failure mode
- If a team's backlog items cannot be traced to objectives, either the backlog is wrong or the objectives are too vague to guide decisions
- The cascade is a communication tool as much as a planning tool — it should be the document that answers "why are we building this?" for anyone in the organization

### Common Failure Modes

1. **The missing middle:** Company strategy and team backlogs exist, but Levels 2-4 are missing. Teams interpret company strategy independently, producing fragmentation.
2. **Strategy as aspiration:** Level 1-3 are aspirational ("be the market leader") without specific choices ("we will serve X segment with Y differentiation and explicitly not serve Z segment").
3. **Cascade as waterfall:** treating the cascade as a one-time annual plan rather than a living document that evolves with learning.
4. **Backlog without traceability:** teams have backlogs with no connection to objectives. "Why are we building this?" cannot be answered beyond "it's on the backlog."
5. **Translation without transformation:** each level adds words but not decisions. The cascade should get more specific, not just restated, at each level.

### Example Application

**Company Strategy (Level 1):** "Become the leading platform for enterprise workflow automation." (This is still too vague — a good strategy would add: for what types of workflows? With what differentiation?)

**Product Strategy (Level 2):** "Focus on IT and HR workflow automation for mid-market enterprises (500-5000 employees). Differentiate on no-code workflow builder (vs. competitors' code-heavy approach). Explicitly not serving: custom enterprise deployments under 500 employees, CRM workflows, or consumer automation."

**Product Area Strategy (Level 3 — Platform Area):** "Build the workflow execution engine that all product areas depend on. Outcomes: (a) workflow execution reliability >99.9%, (b) new workflow types can be added to the builder in <2 weeks by any product area, (c) developer API for custom workflow triggers."

**Team Objectives (Level 4 — Workflow Engine Team):** "Objective 1: Migrate workflow execution to new event-driven architecture to achieve >99.9% reliability (currently 99.5%). Objective 2: Build workflow trigger SDK so product areas can add new workflow types independently."

**Team Backlog (Level 5):** "Initiative 1: Event-driven architecture migration (traces to Objective 1). Initiative 2: Trigger SDK alpha (traces to Objective 2). Initiative 3: Workflow execution monitoring dashboard (traces to Objective 1)."

### Practice Exercise

Take your current company or product strategy. Can you trace it through all five levels? Identify the level where the cascade breaks — where a reasonable person cannot connect the level above to the level below. If you are a team PM, does your backlog trace to objectives? If you are a Director, does your product area strategy add specificity beyond the product strategy?

---

## Framework 6: The Product-Organization Co-Design Framework

### When to Use

When scaling a product organization, reorganizing teams, or launching a new product area that requires team formation. This framework applies Conway's Law deliberately: design the organization to produce the desired product architecture.

### The Framework

Co-design the product architecture and organizational structure through four steps.

**Step 1: Define the Desired Product Architecture**
- What are the key components or bounded contexts of the product?
- How do they depend on each other? (Data dependencies, API dependencies, UX dependencies)
- Which dependencies should be loose (async, API-mediated) and which should be tight (shared UX, shared data model)?
- Draw the architecture. This is the target product structure.

**Step 2: Define the Organizational Structure**
- For each bounded context, what team(s) should own it?
- Where do team boundaries align with architecture boundaries? (Good)
- Where do team boundaries cross architecture boundaries? (Coordination required)
- Where do multiple teams share a bounded context? (Risk of divergence)

**Step 3: Identify the Gaps — Coordination Mechanisms**
- For each place where team boundaries do not match architecture boundaries, what coordination mechanism bridges the gap?
- Options: shared OKRs, regular sync meetings, platform team contracts, design system, shared code ownership, liaison roles
- The cost of coordination mechanism is proportional to the mismatch between org structure and product architecture. Reduce mismatches, not coordination mechanisms.

**Step 4: Plan the Transition**
- How do you move from the current structure to the target structure?
- Teams need stability — do not reorganize more than once per year without exceptional reason
- The transition should have a clear end state, a timeline, and success criteria
- During transition, delivery velocity will decrease — plan for it

### Decision Rules

- Align team boundaries with product architecture boundaries wherever possible
- If two teams share a bounded context, merge them OR split the bounded context. Do not maintain shared ownership indefinitely.
- If one team owns multiple bounded contexts, split the team OR merge the contexts. One team should own one bounded context.
- Coordination mechanisms are a tax, not a solution. If you keep adding coordination mechanisms, the org structure is wrong.

### Common Failure Modes

1. **Org chart based on people, not product:** the structure is designed around who you have, not what the product needs. The product becomes the shape of the people, not the shape of the problem.
2. **Reorganization as strategy substitute:** reorganizing instead of making strategic decisions. If the strategy is unclear, no org structure will produce good outcomes.
3. **The eternal reorganization:** teams are perpetually in transition, never achieving the stability needed for domain expertise and shipping rhythm.
4. **Platform teams as a dumping ground:** creating a "platform team" for everything that does not fit elsewhere, creating a catch-all with no coherent mission.

### Example Application

**Situation:** A product with three user-facing surfaces (web app, mobile app, API) and shared backend services. Currently organized by surface (Web Team, Mobile Team, API Team) each with their own backend logic.

**Problem:** Backend logic is duplicated across teams. Changes to core business logic require coordination across all three teams. New features take 3x as long because they must be built three times.

**Step 1 — Desired Architecture:** Shared backend services with three thin presentation layers (web, mobile, API) that call the same services.

**Step 2 — Org Structure:** Reorganize from surface-based teams to capability-based teams: Core Services Team (owns backend business logic), Web Experience Team, Mobile Experience Team, API Experience Team. Each experience team builds on Core Services APIs.

**Step 3 — Coordination:** Core Services Team provides APIs with SLAs. Experience teams consume APIs. Coordination is through API contracts, not meetings. Weekly architecture sync for API changes.

**Step 4 — Transition:** 3-month transition. Month 1: Core Services Team formed, begins extracting shared logic. Month 2: Experience teams formed, begin migrating to Core Services APIs. Month 3: Old surface teams dissolved. Expect 30% velocity reduction during transition.

### Practice Exercise

Map your current product architecture and organizational structure. Identify the top 3 mismatches. For each, propose either an organizational change or a coordination mechanism. Estimate the cost of the current mismatch (in velocity, quality, or coordination overhead).

---

## Framework 7: The Stakeholder Alignment Framework

### When to Use

When making a product decision that requires alignment from multiple stakeholders with competing interests (sales, engineering, design, marketing, finance, executive). This framework is designed for Principal+ PMs who must influence without authority across organizational boundaries.

### The Framework

Execute four steps in sequence. Do not skip to Step 4 (the decision meeting) without completing Steps 1-3.

**Step 1: Stakeholder Map**
- For the decision, list every stakeholder whose support, input, or non-opposition is required
- For each stakeholder, identify: (a) What do they care about? (their incentives and metrics), (b) What do they fear about this decision? (what could go wrong from their perspective?), (c) What information do they need that they do not have?, (d) What is their decision-making style? (data-driven? relationship-driven? authority-driven?)
- Identify the "blockers" — stakeholders who can stop the decision. Identify the "influencers" — stakeholders who can sway the blockers.

**Step 2: Pre-Alignment**
- Before any group meeting, meet individually with each blocker and key influencer
- In each 1:1: present the decision, ask what they need to be comfortable, listen to their concerns without defending, incorporate their input where it improves the decision
- The goal is not to convince them. The goal is to understand their position well enough that you can represent it accurately in the group meeting.
- If a blocker has an objection you cannot address, resolve it before the group meeting or adjust the decision.

**Step 3: Decision Memo**
- Write a decision memo that captures: (a) The decision to be made (one sentence), (b) The context and why this decision now, (c) The alternatives considered and why they were rejected, (d) The stakeholder input incorporated — naming who raised what concern and how it was addressed, (e) The recommendation, (f) The risks and mitigation, (g) The success criteria — how will we know if this was the right decision?
- Circulate the memo 48+ hours before the decision meeting. This gives stakeholders time to read, react, and prepare.

**Step 4: Decision Meeting**
- The meeting has one purpose: make the decision. It is not a presentation. It is not a discussion of context (that was in the memo).
- Agenda: (a) 5 minutes: restate the decision and recommendation, (b) 20 minutes: address concerns raised by stakeholders who read the memo, (c) 10 minutes: decision and next steps
- If the decision cannot be made in the meeting, the pre-alignment was insufficient. Go back to Step 2 for the unresolved stakeholders.

### Decision Rules

- A decision memo that does not acknowledge stakeholder concerns is a failure. If you cannot represent a stakeholder's objection accurately, you have not done the pre-alignment.
- A decision meeting where a blocker is surprised is a failure. No stakeholder should learn about the decision for the first time in the group meeting.
- If pre-alignment reveals that the decision does not have support, adjust the decision or delay it. Do not force a decision that lacks the support of the people who must execute it.

### Common Failure Modes

1. **The ambush meeting:** presenting a decision in a group meeting without pre-alignment. Stakeholders feel ambushed, defend their positions, and the meeting becomes a debate rather than a decision.
2. **Memo as CYA:** writing a memo to document the decision rather than to align stakeholders. The memo is a tool for alignment, not documentation.
3. **Stakeholder avoidance:** avoiding a stakeholder because "they will never agree." If they can block the decision, avoiding them guarantees the decision will fail.
4. **Pre-alignment as manipulation:** using pre-alignment to get stakeholders to agree without genuinely considering their concerns. Stakeholders who feel manipulated will undermine the decision later.
5. **The permanent alignment process:** using "we need more alignment" as an excuse to avoid making the decision. At some point, alignment must conclude and decision must occur.

### Example Application

**Decision:** Changing the pricing model from per-seat to usage-based for an enterprise SaaS product.

**Stakeholder Map:**
- VP Sales: Cares about quota attainment and commission. Fears: usage-based pricing is unpredictable and harder to sell; large deals become harder to forecast. Needs: data on how the change will affect deal sizes and sales cycles.
- CFO: Cares about revenue predictability and margin. Fears: revenue becomes too variable. Needs: financial model showing revenue impact under multiple scenarios.
- VP Engineering: Cares about team focus and technical debt. Fears: pricing change requires significant engineering (metering, billing). Needs: engineering effort estimate and timeline.
- CEO: Cares about growth rate and competitive position. Fears: change slows growth or alienates customers. Needs: competitive analysis and customer research.

**Pre-Alignment:** Meet with each stakeholder individually. Address VP Sales's forecasting concern with data from companies that made the same transition. Address CFO's predictability concern with the financial model. Address VP Engineering's effort concern with a phased rollout plan. Address CEO's growth concern with customer research showing willingness to pay increases with usage-based model.

**Decision Memo:** Write and circulate 48 hours before meeting. Include all stakeholder concerns and how they were addressed.

**Decision Meeting:** 35 minutes. Decision made. VP Sales commits to training the sales team on the new model. CFO commits to updating the financial model quarterly. VP Engineering commits to the phased rollout timeline.

### Practice Exercise

Identify a decision you need to make that requires stakeholder alignment. Complete Step 1 (Stakeholder Map). For each blocker, schedule a pre-alignment meeting. Write the decision memo. Do not skip to the decision meeting until Steps 1-3 are complete.

---

## Framework 8: The Failure Mode and Effects Analysis (FMEA) for Product Decisions

### When to Use

When making a high-stakes product decision where the cost of failure is significant — platform architecture choices, safety-critical features, regulated product changes, major pricing or packaging changes, data model changes that affect multiple teams.

### The Framework

Adapted from engineering FMEA methodology for product decisions. For each significant decision, evaluate:

**Step 1: Identify Failure Modes**
- What could go wrong if this decision is incorrect?
- List specific failure modes, not generic ones. Instead of "users don't like it," list "enterprise users with custom workflows cannot migrate because the new data model does not support nested objects."
- For each failure mode, identify: (a) What must be true for this failure to occur? (b) What is the probability (1-10)? (c) What is the severity if it occurs (1-10)? (d) What is the detectability — how quickly would we know (1-10, where 10 = immediately, 1 = months)?

**Step 2: Calculate Risk Priority Number (RPN)**
- RPN = Probability × Severity × Detectability
- Focus mitigation on failure modes with high RPN
- High severity failure modes require mitigation regardless of probability (a plane crash is low probability but maximum severity)

**Step 3: Design Mitigations**
- For each high-RPN failure mode: (a) Can we reduce the probability? (better analysis, smaller rollout, more testing), (b) Can we reduce the severity? (blast radius reduction, phased rollout, rollback plan), (c) Can we improve detectability? (monitoring, alerts, customer feedback loops)
- The combination of mitigations should bring the residual RPN below the acceptable threshold

**Step 4: Define Reversal Triggers**
- What observable signal would tell us the failure mode is occurring?
- At what threshold do we trigger reversal?
- Who has the authority to trigger reversal? (Must be defined in advance — during a failure is the wrong time to decide who decides)

### Decision Rules

- Any failure mode with severity 8+ must have mitigation regardless of probability
- Any failure mode with RPN > 200 must have documented mitigation and reversal trigger
- The reversal trigger must be specific and observable — not "if users are unhappy" but "if NPS drops below X and churn increases above Y"
- The person with reversal authority must be identified by name, not role

### Common Failure Modes

1. **Probability optimism:** underestimating the probability of failure modes because "we are good at this." Past success is not a probability estimate.
2. **Severity minimization:** downplaying the severity of failure modes because acknowledging them makes the decision harder to justify.
3. **Detectability overestimation:** assuming you will know quickly when something goes wrong. Most product failures are detected late because monitoring is for known failure modes, and the worst failures are ones you did not anticipate.
4. **Mitigation theater:** listing mitigations that are not actually implemented or tested (the rollback plan that has never been tested).

### Example Application

**Decision:** Migrate from a relational database to a document database for the core product data model.

**Failure Mode 1:** Data migration corrupts or loses customer data.
- Probability: 3 (migration is complex but well-tested)
- Severity: 10 (data loss is catastrophic)
- Detectability: 5 (corruption may not be immediately visible to all users)
- RPN: 3 × 10 × 5 = 150
- Mitigation: Run migration in parallel for 30 days with validation queries comparing old and new data stores. Automated alert if divergence exceeds 0.01%.
- Reversal trigger: Divergence exceeds 0.01% and cannot be resolved within 4 hours.

**Failure Mode 2:** Query performance degrades for complex reporting queries that were optimized for the relational database.
- Probability: 7 (document databases are not optimized for complex joins)
- Severity: 5 (reporting is slower but not broken)
- Detectability: 3 (performance degradation is gradual, users may not report it immediately)
- RPN: 7 × 5 × 3 = 105
- Mitigation: Performance benchmarks for top 20 query patterns, monitored continuously. Query optimization sprint before migration. Rollback plan for reporting queries (keep relational DB as reporting replica for 6 months).
- Reversal trigger: Top 20 query pattern performance degrades by more than 50% and optimization does not resolve within 2 weeks.

### Practice Exercise

Take a significant product decision your team is considering. Complete an FMEA with at least 3 failure modes. Calculate RPN for each. For the highest-RPN failure mode, design the mitigation and reversal trigger. Ask: is the residual risk acceptable?

---

## Framework Quick Reference

| Framework | Best For | Decision Level |
|-----------|----------|----------------|
| One-Way vs Two-Way Door | Deciding how much process a decision needs | All levels |
| RICE-LM Prioritization | Prioritizing initiatives with strategic weighting | Senior PM, Principal PM |
| Sunset Decision Framework | Deciding whether and how to sunset a product | Principal PM, Director, VP |
| Build-Buy-Partner | Deciding build vs buy vs partner for a capability | Principal PM, Director, VP |
| Strategy Cascade | Translating company strategy to team backlogs | Director, VP, CPO |
| Product-Organization Co-Design | Designing teams to produce the desired product | Director, VP, CPO |
| Stakeholder Alignment | Getting alignment for a decision across stakeholders | Principal PM, Director |
| FMEA for Product Decisions | Analyzing failure modes for high-stakes decisions | Principal PM, Director, VP |
