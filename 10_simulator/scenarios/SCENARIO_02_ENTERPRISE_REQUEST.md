# Scenario 02: The Enterprise Request That Weakens the Platform

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-002 |
| **title** | The Enterprise Request That Weakens the Platform |
| **leadership_level** | Principal PM, Director |
| **primary_tension** | Revenue vs. platform integrity |
| **key_capability** | Strategic coherence |
| **estimated_time** | 40 minutes |
| **related_principles** | PRN-0002 (Strategy Is What You Say No To), PRN-0008 (Platform Strategy), PRN-0010 (Economic Moats) |

## Situation

You are a **Director of Product** at **AtlasData**, a data integration platform that connects enterprise SaaS tools into a unified data layer. The company is Series C, 280 employees, $45M ARR, growing 40% year-over-year. Your platform processes ~50 million data syncs per day across 200+ connector integrations.

AtlasData's core value proposition is a **unified, consistent data model**. When you connect Salesforce, HubSpot, and NetSuite, the platform normalizes all data into a single schema so customers can query across tools without understanding each tool's native data model. This normalization layer is your competitive moat — it's what makes AtlasData different from point-to-point integration tools.

Your largest enterprise customer, **Meridian Global** (a Fortune 500 manufacturing conglomerate), represents $8M ARR — about 18% of total revenue. They have been a customer for 4 years and have expanded from 3 business units to 12. Their contract has 18 months remaining. Your VP of Sales, **Derek**, has been cultivating an expansion deal that would add another $2M in ARR, bringing Meridian to $10M annually.

### The Request

Meridian's CIO, **Patricia Okonkwo**, has a request: she wants AtlasData to support **raw pass-through mode** — the ability to sync data directly from source to destination without normalization. Her argument is pragmatic:

"We have 47 Salesforce instances across our business units. We don't need you to normalize Salesforce data because we already have a team of 12 data engineers who handle normalization internally. What we need is high-speed, high-volume raw data sync. Your normalization layer adds latency (3-8 seconds per sync) and makes it harder for our team to work with the data the way they already know. If you can offer raw pass-through, we'll expand by $2M ARR. If not, we'll need to evaluate alternatives like Fivetran or a custom Kafka implementation."

This pass-through capability would require:
- A new sync mode that bypasses the normalization layer
- Separate API endpoints, monitoring, and error handling
- Different SLA commitments (higher throughput, lower consistency)
- ~10-12 person-weeks of engineering effort

### Why This Weakens the Platform

Adding raw pass-through mode creates several strategic problems:

1. **Data model fragmentation.** Today, every customer's data goes through the same normalization pipeline. This means platform improvements (better deduplication, richer schema mapping) benefit all customers. If Meridian bypasses normalization, they create a divergent data path that won't benefit from platform improvements.

2. **Precedent risk.** If Meridian gets pass-through, your next five largest enterprise customers will demand it too. Within 18 months, you'll be maintaining two separate product architectures — the normalization platform and the pass-through pipeline — each with its own feature requests, bugs, and engineering demands.

3. **Strategic dilution.** Your product strategy document for this year explicitly states: "AtlasData's differentiation is unified, normalized data access. We do not compete on raw data movement speed. We compete on data quality and consistency." Adding pass-through mode contradicts this strategy. Your team will ask legitimate questions: "If we're building pass-through, does the strategy still matter? What else are we willing to compromise?"

4. **Engineering morale.** Your senior engineering team joined AtlasData specifically because they wanted to build a normalization platform. Several staff engineers have expressed frustration when enterprise requests pull the architecture in a different direction. Your principal architect, **Dr. Elena Vasquez**, has told you privately: "If we build pass-through, we're admitting that our core architecture is optional. If it's optional for Meridian, it's optional for everyone. The normalization layer becomes a tax instead of a feature."

5. **Competitive positioning.** If AtlasData offers raw pass-through, you're competing directly with Fivetran, Stitch, and other ETL tools that have been doing raw data movement for years. They have 10x the engineering investment in that use case. You're entering their market from a position of weakness.

### The Financial Context

- Meridian: $8M ARR today, potential $10M ARR with expansion. Gross margin: 78%.
- Entire platform: $45M ARR. Your team of 35 engineers (5 teams).
- Losing Meridian would mean: $8M ARR hole, negative signal to other enterprise customers, potential domino effect in the enterprise segment.
- The $2M expansion represents 4.4% of total ARR — material but not existential.
- Your CEO, **Amir**, is a former enterprise sales executive who views large customer retention as the highest priority. His stated philosophy: "Never lose a whale."

### What Meridian Might Do

- Fivetran already supports raw data movement from Salesforce and NetSuite. Meridian's data engineering team has evaluated Fivetran and reported that it "meets their technical requirements" for the raw sync use case.
- However, Fivetran does not offer normalization. Meridian would need to keep AtlasData for the normalized view AND add Fivetran for raw sync — or build a custom solution.
- Meridian's data engineering VP, **Raj**, has told your team: "We'd prefer to consolidate on AtlasData, but if you can't support our workflow, we'll maintain parallel vendors."

## Characters

**Amir (CEO).** Former SVP of Enterprise Sales at a large SaaS company. Sees every customer conversation through the lens of retention and expansion. Has publicly stated: "If a $10M customer asks for something, we should think very carefully before saying no." Has overruled product decisions in the past when large customers were involved. Motivated by: revenue growth, board confidence, Series D valuation.

**Derek (VP Sales).** Owns the Meridian relationship. Has been working the expansion deal for 6 months. His Q4 commission depends significantly on closing this deal. Has told you: "Look, we're talking about adding a configuration flag. It's not a new product. Just give them the API endpoint without normalization — how hard can it be?" Motivated by: quota attainment, relationship management, closing the quarter.

**Dr. Elena Vasquez (Principal Architect).** 15 years of experience in data infrastructure. Designed the normalization engine. Sees the platform as her life's work. Has strong opinions and a direct communication style. Has said: "If we do this, I need you to tell me honestly whether we are a platform company or a services company, because right now we're pretending to be the first while acting like the second." Motivated by: architectural integrity, technical excellence, professional pride.

**Patricia Okonkwo (Meridian CIO, external).** Pragmatic, data-driven, not emotional. She has a budget and a roadmap and will choose the vendor that best serves Meridian's needs. Her relationship with AtlasData is good but transactional — she is not a champion or evangelist. Motivated by: internal SLAs, data engineering team productivity, cost efficiency.

**Linh (Senior PM, Enterprise segment).** Reports to you. Manages the enterprise product roadmap. Has been the one handling the escalation from Derek about Meridian. Is torn between customer empathy and strategic conviction. Motivated by: doing the right thing for the product, career growth, not being caught between you and Derek.

## Constraints

- Meridian contract has 18 months remaining. They cannot churn tomorrow.
- The $2M expansion deal: Derek wants to close this quarter (8 weeks remaining).
- 10-12 person-weeks of engineering to build pass-through mode. Plus ongoing maintenance in perpetuity.
- Your 2024 product strategy document explicitly excludes raw data movement as a product direction.
- Fivetran exists and does raw data movement well. Meridian has evaluated it.
- You have the authority to say no to this request, but Amir can override you.

## Your Role

You are Director of Product at AtlasData. You own the product strategy and roadmap for the entire platform. You report to the CEO (Amir). The enterprise PM (Linh) reports to you. You do not own the Meridian relationship (Derek does), but you own the product decisions that affect it. You can say no, but you must bring the argument to Amir — and Amir's default position is "don't lose the whale."

## Response Format

Your response must have exactly three parts.

### Part 1: Assumptions

List your assumptions beyond what is explicitly stated. Label each with confidence (High/Medium/Low) and explain why it matters.

Strong assumptions address things like: Is Meridian's threat credible or a negotiation tactic? If we say no, will they actually leave? If we build pass-through, will other enterprise customers actually follow? What is the real engineering cost of maintaining two architectures over 3 years? What would our best enterprise customers do if we held the line?

### Part 2: Decision

Describe your decision with:
- **What you will do.** Specific actions, alternatives explored, rationale.
- **What you will NOT do.** Explicit trade-offs. What revenue or relationship are you willing to risk?
- **How you will communicate.** What you say to Derek, Amir, Elena, and Patricia. In what order. What evidence you bring to each conversation.
- **What alternative value you will create for Meridian.** If you say no to pass-through, what DO you propose that addresses their underlying need (not their stated solution)?

### Part 3: Pre-Mortem

Assume your decision was implemented. 12 months later, it failed. Write a specific pre-mortem with at least 3 distinct failure paths that are specific to this scenario's characters, constraints, and competitive dynamics.

---

## Scoring Rubric (Scenario-Specific)

### Strategic Coherence

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats this as a customer request management problem ("we should do what the customer wants" or "we should never compromise strategy"). No recognition of the tension between short-term revenue and long-term platform integrity. |
| 3 | Recognizes the strategic tension and articulates a clear position. Acknowledges that this is a strategy test, not just a feature request. |
| 4 | Evaluates not just "should we build pass-through?" but "what would have to be true for pass-through to be the right strategic move?" Shows understanding that the decision is not about the feature — it's about the company's identity and competitive positioning. |
| 5 | Reframes the problem from "Meridian wants X" to "what is the underlying need and what are 3 ways to meet it that don't compromise the platform?" Identifies the organizational dynamic (a CEO with an enterprise sales background and a VP Sales compensated on deal closure) as the structural cause of the tension. |

### Incentive Analysis

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Assumes all stakeholders want "what's best for the company." No analysis of conflicting incentives. |
| 3 | Identifies that Derek is compensated on deal closure, Amir prioritizes revenue retention, and Elena prioritizes architectural integrity. Recognizes the incentive conflict. |
| 4 | Maps the specific mechanics: Derek's commission structure, Amir's board commitments about enterprise retention, Elena's identity investment in the platform. Shows how each person's incentives would lead them to a different answer to the same question. |
| 5 | Proposes how to change the incentive conversation: reframe the question for Amir from "should we accommodate Meridian?" to "is $2M ARR worth bifurcating our architecture and competing with Fivetran from behind?" For Derek, propose a compensation adjustment or alternative deal structure. For Elena, propose a platform investment that addresses Meridian's underlying need without pass-through. |

### Decision Quality

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Binary yes/no. No exploration of middle-ground options. No recognition that the answer might be conditional ("yes, if..." or "no, but..."). |
| 3 | Explores at least 2-3 distinct alternatives (build pass-through, say no, build something else that addresses the underlying need, offer a pricing concession, etc.). |
| 4 | Considers alternatives that operate on different levels: a technical alternative (faster normalization pipeline), a commercial alternative (discount to offset switching cost), a strategic alternative (position this as a managed service, not a platform feature). |
| 5 | Designs the communication as a strategic intervention: frames the decision for Amir as a board-level strategic choice about what kind of company AtlasData is; frames for Derek in terms of his commission and reputation; frames for Patricia as a commitment to solving her real problem (speed) rather than her stated solution (pass-through). |

### Executive Communication

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Cannot articulate the decision in terms relevant to Amir. Technical arguments about architecture. |
| 3 | Frames the decision for Amir in business terms: revenue risk, competitive risk, strategic risk. |
| 4 | Anticipates Amir's likely objection ("we can't lose a $10M customer") and has a specific response that connects to his incentives (board confidence, valuation, not any single customer). |
| 5 | Creates a decision memo for Amir that makes the alternatives and their consequences visible without forcing a recommendation. Asks Amir to own the strategic choice: "Are we a normalization platform that can command premium pricing, or are we a data movement tool competing with Fivetran? You need to decide, because the Meridian decision is where that choice becomes real." |

---

## Facilitator Notes

**Common traps:**
1. Assuming Meridian will definitely churn if you say no. They have 18 months on their contract. The switching cost of moving 12 business units off the platform is enormous. Patricia's threat may be a negotiation tactic.
2. Proposing "we'll build it as a separate product" — this doesn't solve the precedent problem and doubles the maintenance burden.
3. Assuming the underlying need is pass-through when it might be "our data engineers want to use the tools they know" — the solution might be better API documentation, faster sync speeds within the normalization layer, or a different integration approach.
4. Proposing a pure compromise ("we'll do a limited version") that makes nobody happy — slower than Fivetran but broken enough to anger Elena.

**Discussion prompts:**
- If you were Amir's coach, what would you want him to understand about this decision?
- What would AtlasData look like in 3 years if you say yes to this request? What if you say no?
- Is there a world where pass-through IS the right strategy? What would have to change?
- How do you communicate a "no" to Derek in a way that preserves your working relationship?
- If Amir overrules you and says "build it," what do you do?

**Related Academy Content:**
- [PRN-0002](../../01_core_doctrine/PRINCIPLES.md): Strategy is what you say no to
- [PRN-0008](../../01_core_doctrine/PRINCIPLES.md): Platform product management
- [Contradiction: CON-0009](../../08_contradictions/): Customer revenue vs. product strategy
