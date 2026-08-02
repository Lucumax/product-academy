# Scenario 01: Two Engineers, Three Strategic Demands, One Regulatory Deadline

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-001 |
| **title** | Two Engineers, Three Strategic Demands, One Regulatory Deadline |
| **leadership_level** | Senior PM, Principal PM |
| **primary_tension** | Resource scarcity vs. strategic trade-offs |
| **key_capability** | Triage under constraint |
| **estimated_time** | 35 minutes |
| **related_principles** | PRN-0002 (Strategy Is What You Say No To), PRN-0003 (Cost of Delay vs. Imperfection), PRN-0005 (Platform Thinking) |

## Situation

You are a Senior PM or Principal PM at **FinClear**, a B2B fintech company that provides transaction reconciliation software to mid-market banks and credit unions. The company has 85 employees, $12M ARR, and is post-Series A with 18 months of runway.

Your product is a reconciliation engine that processes ~2 million transactions per day across 40 institutional customers. The engine matches, flags, and resolves discrepancies between transaction records from multiple sources. Your largest customer, **RegionalOne Bank**, represents 35% of ARR ($4.2M) and has been with FinClear for 3 years.

You lead a team of **two backend engineers** (Alex and Jordan). Alex is a staff-level engineer with 12 years of experience, deep domain knowledge, and is the only person who fully understands the reconciliation matching algorithm. Jordan is a senior engineer with 5 years of experience, strong generalist, but has only been on the team for 4 months and is still ramping up on the domain. You have no dedicated frontend engineer, no designer, and no data scientist. Your engineering manager is stretched across three teams.

### The Three Demands

**Demand 1: RegionalOne Bank Feature Request**
RegionalOne's CTO has requested a custom rule engine that would let their operations team define reconciliation matching rules without involving FinClear's engineering team. They've been asking for this for 9 months. Their contract is up for renewal in 4 months. Your CEO has told you this is "the top priority" because losing RegionalOne would be "catastrophic." The feature is estimated at 6-8 person-weeks of backend work plus 2-3 weeks of frontend work (which you'd need to borrow from another team or contract out). RegionalOne's CTO has mentioned in passing that a competitor, ClearLedger, has been "very responsive" to their needs.

**Demand 2: Platform Migration**
Your CTO has been advocating for migrating the reconciliation engine from a monolithic PostgreSQL-backed architecture to an event-driven architecture using Kafka and a dedicated rules engine. The current architecture processes transactions in batch windows (every 4 hours) and cannot support real-time reconciliation, which several prospects have demanded. The CTO argues this migration is essential for the next phase of growth and will unlock a 10x improvement in processing speed. It is estimated at 12-16 person-weeks of focused engineering effort. Delaying it means another 6+ months of prospects saying "we'll evaluate you again when you support real-time."

**Demand 3: EU Regulatory Compliance (PSD3/PSR)**
The European Union's Payment Services Directive 3 (PSD3) and Payment Services Regulation (PSR) introduce new requirements for transaction reconciliation and reporting that take effect in **6 weeks**. If FinClear does not comply, it cannot process transactions for any EU-based customer. You currently have 3 EU customers ($1.8M ARR combined) and a pipeline of 7 EU prospects worth an estimated $4M in potential ARR. Non-compliance means losing existing EU revenue, the entire EU pipeline, and potential regulatory fines. The compliance work is estimated at 3-4 person-weeks. It is tedious, non-strategic work involving data retention policies, audit trail generation, and reporting format changes. Nobody wants to do it. The CTO has characterized it as "distraction work" but acknowledges it's legally required.

## Characters

**Sarah (CEO).** Former VP of Product at a large fintech. Founder. Deeply concerned about RegionalOne retention. Tendency to over-index on the largest customer's demands. Has been known to change priorities based on the last conversation she had. Motivated by: survival, avoiding dependence on any single customer, getting to Series B.

**Marcus (CTO).** 20-year engineering veteran. Believes the platform migration is the single most important technical decision the company will make this year. Has been pushing for the migration for 6 months. Feels his technical judgment is being overridden by short-term business pressures. Motivated by: technical excellence, scalability, being proven right about architectural decisions.

**Elena (VP Sales).** Carries the RegionalOne relationship and the EU pipeline. Her compensation is 60% commission-based. RegionalOne renewal is her largest single account. EU pipeline is her growth story for the board. Motivated by: hitting quota, closing deals, keeping customers happy.

**Alex (Staff Engineer).** The only person who understands the matching algorithm. Quiet, deeply knowledgeable, resistant to context switching. Has expressed frustration about being pulled between competing priorities. Has mentioned that if forced to work on the compliance project, it will delay everything else by weeks because of context-switching cost. Motivated by: doing technically interesting work, being respected for expertise, not burning out.

**Jordan (Senior Engineer).** Smart, eager, still ramping up. Can execute independently on well-defined tasks but cannot yet design complex systems. Has been working on the RegionalOne feature for 2 weeks and has made progress on the rule engine design. Motivated by: learning the domain, shipping features, building trust with Alex.

**RegionalOne CTO (James).** Not a character you can directly manage, but a presence in every conversation about priorities. Has a reputation for being demanding and for playing vendors against each other. His email to Sarah last week said: "We need a timeline on the rule engine or we need to have a different conversation about our relationship."

## Constraints

**Hard constraints:**
- Regulatory deadline: 6 weeks. Non-negotiable. EU operations shut down if missed.
- Engineering capacity: 2 backend engineers. No ability to hire before the deadline.
- Alex and Jordan combined: ~8 person-weeks of capacity in the next 6 weeks (after accounting for meetings, on-call, and existing maintenance burden).
- RegionalOne contract renewal: 4 months. If they don't renew, 35% of ARR is at risk.
- No frontend capacity on your team. Any frontend work requires borrowing from another team or contracting.

**Soft constraints:**
- Alex's domain knowledge is a single point of failure. Burning him out or losing him is an existential risk.
- Jordan is ramping up and cannot be assigned to the most complex work independently.
- Sarah (CEO) has said RegionalOne is "the top priority" — diverging from this requires managing upward.
- Marcus (CTO) feels ignored and may escalate or disengage if migration is deferred again.
- Elena (VP Sales) will resist any decision that threatens the RegionalOne renewal or the EU pipeline.
- The compliance work is demotivating for engineers — assigning it poorly risks attrition.

## Your Role

You are the product leader for the reconciliation product. You report to the CEO (Sarah) with a dotted line to the CTO (Marcus). You have authority over the team's priorities but not over hiring or budget. You cannot add headcount. You cannot extend the regulatory deadline. You can negotiate scope, sequencing, and communication with stakeholders.

## Response Format

Your response must have exactly three parts.

### Part 1: Assumptions

List your assumptions beyond what is explicitly stated in the scenario. For each assumption:
- State the assumption clearly
- Label confidence: High (>80% certain), Medium (50-80%), Low (<50%)
- Explain why the assumption matters for your decision

A weak assumption: "The team is capable of executing." A strong assumption: "I'm assuming the compliance work requires deep domain knowledge of the reconciliation algorithm and cannot be done by Jordan alone without Alex's guidance. Confidence: medium. This matters because if Jordan CAN do it independently, we can parallelize and have Alex focus on RegionalOne."

### Part 2: Decision

Describe your decision with:
- **What you will do.** Specific actions, sequencing, resource allocation, timeframe.
- **What you will NOT do.** Explicit trade-offs and sacrifices.
- **Rationale.** Why this plan vs. the alternatives you considered.
- **Stakeholder communication plan.** How you will communicate to Sarah, Marcus, Elena, Alex, and Jordan. What you will say to each, in what order, and when.

### Part 3: Pre-Mortem

Assume your decision was implemented. It is now 12 months later. The outcome was a failure. Write a specific, mechanistic pre-mortem that answers:

1. **What failed?** Name the specific failure mechanism (not "the project was late" but "the compliance work uncovered a data model dependency that required Alex's expertise for 2 weeks, which cascaded into the RegionalOne feature being delayed by 3 weeks, which triggered James to open a formal RFP process with ClearLedger").
2. **Why did it fail?** What did you fail to anticipate? What assumption was wrong?
3. **Early warning signals.** What indicators could you have monitored that would have told you the failure was coming 4-6 weeks before it was obvious?
4. **What would you do differently?** Given what you know now, what would you change about your original decision?
5. **Second-order effects.** What happened as a consequence of the failure that went beyond the immediate problem?

Identify at least 3 distinct failure paths.

---

## Scoring Rubric (Scenario-Specific)

### Problem Framing

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Frames this as a simple prioritization problem ("we need to rank the three demands"). Misses the single-point-of-failure risk (Alex), the CEO's incentive structure, or the regulatory deadline's non-negotiability. |
| 3 | Identifies that this is a resource constraint problem with a hard deadline, a single-point-of-failure risk, and competing strategic bets. Distinguishes between the demands' urgency and importance. |
| 4 | Reframes the problem: "This is not a prioritization problem — it's a risk management problem. We have one engineer who holds critical knowledge, a hard regulatory deadline, and a customer retention risk. The real question is how to manage existential risk to the business, not how to rank features." |
| 5 | Identifies the organizational design flaw (team of 2 with a single point of failure is structurally unsound regardless of prioritization) and addresses it as part of the response. |

### Decision Quality

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Tries to do all three things with the existing capacity. No recognition that the math doesn't work (8 person-weeks of capacity vs. ~20-27 person-weeks of demand). |
| 3 | Makes a clear choice with trade-offs. Does not pretend all three can be done. Specific about what is deferred and why. |
| 4 | Sequences work across time horizons (6-week regulatory sprint, then RegionalOne, then migration). Identifies scope reduction for each demand (e.g., "compliance work can be done at minimum viable level, not gold-plated"). Addresses the Alex bottleneck specifically. |
| 5 | Restructures the approach: proposes borrowing frontend capacity early, identifies which parts of the migration can be done in parallel with Jordan, creates a communication plan that manages CEO expectations and CTO frustration simultaneously. |

### Pre-Mortem Quality

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Generic failure modes: "the team couldn't deliver," "the customer churned." |
| 3 | Specific, causal failure mechanisms connected to the scenario's constraints (Alex burned out, Jordan couldn't ramp fast enough, compliance scope was underestimated). |
| 4 | Includes organizational failure modes (Sarah changed priorities mid-sprint, Marcus escalated to the board and got the migration prioritized over compliance, Elena promised RegionalOne a timeline you couldn't meet). |
| 5 | Identifies how the failures cascade: loss of Alex triggers loss of RegionalOne, which triggers down-round or acquisition. Shows understanding of how technical failure becomes business failure. |

### Stakeholder and Incentive Analysis

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Lists stakeholders without analyzing what they actually want or how they'll react. |
| 3 | Identifies each stakeholder's explicit goals and likely resistance points. Recognizes that Sarah says "top priority" but may not understand capacity constraints. |
| 4 | Maps the coalition dynamics: Marcus and Elena are natural allies (both want investment in growth), but they pull in opposite directions (migration vs. customer features). Sarah is the swing vote and the person most influenced by the last conversation. Alex is the silent veto player — if he leaves, all plans collapse. |
| 5 | Proposes specific mechanisms to align incentives: e.g., making the CTO the sponsor of the compliance work (it's infrastructure, it's engineering-led, it gives him ownership of a critical deliverable), or tying Elena's compensation conversation to the resource reality. |

---

## Facilitator Notes (For Group Practice)

**Common traps:**
1. Proposing to hire a contractor to solve the problem — violates the constraint of no hiring capacity. The scenario makes this explicit: you don't have budget or time to hire.
2. Proposing to extend the regulatory deadline — this is hard constraint. Non-compliance means EU operations shut down. There is no extension.
3. Pretending all three can be done: the math doesn't work. 8 person-weeks capacity vs. ~20-27 person-weeks of demand. A response that doesn't acknowledge this is scoring at the shallow level regardless of how well-structured it is.
4. Ignoring Alex's single-point-of-failure status. If Alex burns out or leaves, the company loses both the migration AND the RegionalOne feature AND probably the ability to maintain the existing system.

**Discussion prompts:**
- If you could only do one thing, which would it be and why?
- If you were Sarah (the CEO), would you agree with your own decision? Why or why not?
- What would you do if Alex told you tomorrow that he's received an offer from another company?
- Is there a version of the compliance work that takes 1 week instead of 3-4? What would you have to sacrifice?
- What is the actual cost of losing RegionalOne? Is it $4.2M or something else? (Consider: concentration risk reduction, signal to other customers, impact on Series B.)

**Related Academy Content:**
- [PRN-0002](../../01_core_doctrine/PRINCIPLES.md#prn-0002-strategy-is-what-you-say-no-to--everything-else-is-prioritization): Strategy is what you say no to
- [PRN-0003](../../01_core_doctrine/PRINCIPLES.md#prn-0003-the-cost-of-delay-exceeds-the-cost-of-imperfection): Cost of delay vs. imperfection
- [Framework 1](../../01_core_doctrine/DECISION_FRAMEWORKS.md#framework-1-one-way-vs-two-way-door-decision-classification): One-way vs. two-way door classification
- [Framework 3](../../01_core_doctrine/DECISION_FRAMEWORKS.md#framework-3-pre-mortem-protocol): Pre-mortem protocol
