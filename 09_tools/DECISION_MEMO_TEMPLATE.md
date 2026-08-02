# Decision Memo Template

## Purpose

A decision memo is a structured document that communicates a significant, contestable decision to stakeholders. It makes the decision logic transparent, the alternatives visible, and the trade-offs explicit. A good decision memo enables a stakeholder to evaluate your decision without reading your mind — and to disagree productively because the reasoning is laid out clearly.

Unlike a PRD (which describes what to build) or a strategy document (which describes direction), a decision memo describes a choice and why you made it. Its audience is typically executives, cross-functional peers, and anyone who needs to understand (or challenge) a consequential decision.

## When to Use

- You're making a decision that affects multiple teams or functions
- The decision has significant resource, strategy, or revenue implications
- You need executive alignment or approval (but the decision should ideally be made, not escalated)
- You anticipate disagreement and want to create a structured basis for discussion
- You're documenting a decision for future reference (organizational memory — "why did we decide this?")
- You're making a Type 1 (one-way door) decision that requires broader input

## Template Structure

### Header
- **Decision Title:** A specific, descriptive title (not "Q3 Planning" but "Decision to Defer Platform Migration in Favor of Regulatory Compliance Deadline")
- **Author:** Name and role
- **Date:** Date of the memo
- **Status:** [Proposed / Recommended / Decided / Implemented]
- **Decision Type:** Type 1 (hard to reverse) or Type 2 (easy to reverse) — see Framework 1
- **Consulted:** People who provided input
- **Decider:** Person or group with decision authority

### 1. The Situation (1-2 paragraphs)

What problem or opportunity necessitates a decision? Be specific and brief. The reader should understand the context within 60 seconds.

Don't: "We need to decide our Q3 priorities."
Do: "We have a regulatory compliance deadline in 6 weeks (PSD3) that requires 3-4 person-weeks of engineering work, a platform migration that requires 12-16 person-weeks, and a customer retention risk from our largest customer who has requested a custom feature. Our engineering capacity is 2 people. The math requires us to choose."

### 2. The Decision (1-3 sentences)

State the decision clearly. This is not a recommendation — it's the actual decision you're making or proposing. Use active language: "We will..." not "It is recommended that..."

### 3. Rationale (3-5 paragraphs)

Why this decision? Organize around:
- **Strategic alignment:** How does this decision connect to the product strategy and company goals?
- **Evidence:** What data, research, or analysis supports this decision?
- **Constraints:** What constraints (resource, time, regulatory, organizational) shaped the decision?
- **Risk assessment:** What are the risks of this decision and how are they being mitigated?

### 4. Alternatives Considered (1 paragraph each)

For each alternative you considered but rejected, describe:
- What the alternative was
- Why it was attractive (what problem it solved)
- Why it was rejected (specific reasons, not "it wasn't the best option")

A decision memo with only one alternative ("do nothing") is weak. A decision memo with 3+ alternatives that were seriously evaluated is strong. Include at least one alternative that was genuinely tempting — it shows you considered uncomfortable options.

### 5. Trade-offs and Sacrifices (explicit)

What are you NOT doing as a result of this decision? What are you sacrificing? Who loses? Be specific:
- "We are deferring the platform migration by at least one quarter, which means real-time processing capabilities (and the prospects who require them) are delayed until Q4 at the earliest."
- "We are accepting that engineering velocity will be lower in Q3 because the compliance work consumes 40% of capacity."
- "We are risking the RegionalOne renewal because their feature request is being deferred by 8 weeks."

If you can't identify specific sacrifices, your decision may not be a real trade-off — you might just be prioritizing rather than deciding.

### 6. Stakeholder Impact

For each key stakeholder group:
- **Who:** Name or role
- **Impact:** How the decision affects them (positive or negative)
- **Likely reaction:** What they'll probably think/feel/do
- **Communication plan:** How and when you'll communicate the decision to them

### 7. Implementation Plan

- **Key actions:** What needs to happen, in what sequence, by when?
- **Owner:** Who is accountable for each action?
- **Dependencies:** What must be true for this to succeed?
- **First step:** What happens in the next 48 hours?

### 8. Success and Failure Metrics

- **Success metrics:** How will we know this decision was right? (Leading indicators, not just lagging)
- **Counter-metrics:** What metrics should NOT move in the wrong direction?
- **Evaluation cadence:** When will we review whether the decision is working?

### 9. Reversal Conditions

Under what conditions would we reverse or modify this decision?
- Specific metric triggers (e.g., "If customer churn exceeds 5% in the quarter following implementation")
- Qualitative triggers (e.g., "If the engineering lead reports that the compliance work has uncovered a data model dependency that will add 3+ weeks")
- Time-based triggers (e.g., "If the migration has not started by Q4, we escalate to the CTO for a different approach")
- Who decides to reverse: The same person/group who made the original decision?

---

## Filled Example: Engine Platform Migration Decision

### Header
- **Decision Title:** Defer Platform Migration to Q4 in Favor of PSD3 Regulatory Compliance and RegionalOne Feature Delivery
- **Author:** Alex Chen, Principal PM, Reconciliation Platform
- **Date:** 2026-03-15
- **Status:** Recommended (pending CEO approval)
- **Decision Type:** Type 1 (schedule commitment to largest customer, hard to reverse)
- **Consulted:** Marcus (CTO), Elena (VP Sales), Alex (Staff Engineer), Jordan (Engineer)
- **Decider:** Sarah (CEO)

### 1. The Situation
Our reconciliation platform faces three competing demands with 8 person-weeks of engineering capacity over the next 8 weeks: (1) RegionalOne has requested a custom rule engine (our largest customer, 35% of ARR, contract renewal in 4 months), (2) CTO advocates for migrating to an event-driven architecture to enable real-time processing, (3) PSD3 regulatory compliance requires data retention and audit trail changes by April 30 (6 weeks). The engineering team is 2 people (Alex and Jordan). Alex is the only person with deep domain knowledge. The math requires us to sequence, not parallelize.

### 2. The Decision
We will defer the platform migration to Q4. We will complete PSD3 compliance work in weeks 1-3 (Jordan leads, Alex advises), then deliver a scoped version of the RegionalOne rule engine in weeks 4-8 (Alex leads, Jordan supports). We will communicate the migration delay to Marcus (CTO) before end of week and the RegionalOne timeline to Elena (VP Sales) with a specific commitment: rule engine MVP by May 15.

### 3. Rationale
- **Strategic alignment:** Compliance is non-negotiable — missing the deadline means losing EU operations. RegionalOne retention is existential (35% ARR). Platform migration is strategically important but not urgent — it can be deferred by one quarter without existential risk.
- **Evidence:** Compliance work estimated at 3 person-weeks (Jordan can do ~70% independently, needs Alex for domain-specific logic). RegionalOne feature estimated at 4 person-weeks (Alex is essential — Jordan cannot design the rule engine independently). Migration estimated at 14 person-weeks (cannot be completed in 8 weeks even if prioritized).
- **Constraints:** Alex is a single point of failure. His time is the binding constraint. We cannot hire in the next 8 weeks.
- **Risk mitigation:** We will communicate the migration delay to the CTO proactively with a specific Q4 commitment. We will scope the RegionalOne feature to MVP (core rule types only, deferring advanced rule types to phase 2).

### 4. Alternatives Considered
- **Alternative A: Do all three in parallel.** Rejected because: Alex cannot context-switch across compliance, customer feature, and architectural migration simultaneously without quality risk. Jordan cannot independently lead any of the three in full. Parallel execution would mean all three are late and poorly done.
- **Alternative B: Prioritize migration, defer compliance.** Rejected because: non-compliance means EU operations shutdown, regulatory fines, and loss of EU pipeline ($1.8M existing + $4M pipeline). This is an existential risk we cannot accept.
- **Alternative C: Prioritize migration, defer RegionalOne.** Rejected because: RegionalOne renewal is in 4 months. Their CTO has explicitly requested a timeline on the rule engine and mentioned competitor interest. Deferring to Q4 risks losing a $4.2M customer — also existential.
- **Alternative D: Scoped migration (event system only, defer rules engine).** Considered because: the event system is the architectural foundation and could be built in 4-5 weeks. Rejected because: the event system alone doesn't deliver customer value — it's a platform capability that enables future features. Building it without the rules engine would be a partially-completed migration that satisfies neither the CTO's vision nor customer demand.

### 5. Trade-offs and Sacrifices
- The platform migration is deferred by one quarter. This means real-time processing capabilities are delayed until Q4 at earliest. Prospects who require real-time will be told "Q4" and may choose competitors in the interim.
- Marcus (CTO) will be disappointed. He has been advocating for this migration for 6 months. This is the third time it has been deferred.
- Engineering velocity in Q3 will include migration work, which means future feature velocity is pre-committed.
- We are accepting that the RegionalOne feature is MVP scope — advanced rule types (chained rules, conditional logic) are deferred to a phase 2 that may not happen if the renewal is not secured.

### 6. Stakeholder Impact
- **Sarah (CEO):** Must approve the recommendation. Likely to agree because the trade-off logic is clear, but will want assurance that the migration is not deferred indefinitely. Communication: Decision memo + 15-min briefing before executive staff meeting.
- **Marcus (CTO):** Will be disappointed. Needs to understand that this is a sequencing decision, not a rejection of the migration. Communication: 1:1 before the memo is circulated. Frame it as "we are committing to Q4 migration start" with a specific ask: "What parts of the migration can be done in parallel with Q3 work?"
- **Elena (VP Sales):** Needs the RegionalOne timeline to manage the customer conversation. Will be satisfied that RegionalOne is prioritized but anxious about the MVP scope. Communication: Share the RegionalOne delivery plan (MVP May 15, phase 2 July 15) and ask her to manage the customer communication.
- **Alex (Staff Engineer):** Needs clarity on his focus for the next 8 weeks. Will be relieved that he's not being asked to context-switch across three projects. Communication: Share the sequencing plan and ask for his estimate validation.
- **Jordan (Engineer):** Needs clear ownership. Will be motivated by leading the compliance work (first time leading a significant project). Communication: Frame as a development opportunity — he owns compliance and builds credibility with the team.

### 7. Implementation Plan
- **This week:** CEO approval. CTO conversation (Marcus). RegionalOne timeline shared with Elena.
- **Week 1-3:** Compliance sprints. Jordan leads, Alex reviews. Target completion: April 5.
- **Week 4-8:** RegionalOne rule engine MVP. Alex leads design, Jordan implements testing. Target completion: May 15.
- **Q4:** Platform migration kickoff. Scope and resourcing TBD based on Q3 outcomes and any new constraints.

### 8. Success and Failure Metrics
- **Success:** PSD3 compliance completed by April 30 (confirmed by legal/compliance review). RegionalOne rule engine MVP delivered by May 15 with >3 core rule types supported. RegionalOne renewal closed by July 15.
- **Counter-metrics:** Platform migration NOT deferred beyond Q4. Engineering attrition (Alex specifically) — monitor for burnout signals. No new regulatory findings during compliance audit.
- **Evaluation cadence:** Bi-weekly check-in with Marcus on migration prep. Monthly review with Sarah on overall progress vs. plan.

### 9. Reversal Conditions
- If compliance work scope is discovered to be >5 person-weeks (vs. current estimate of 3), we re-evaluate the RegionalOne timeline and consider hiring a contractor for compliance.
- If Alex reports burnout or receives an external offer, all plans are re-evaluated — Alex is the single point of failure and his retention overrides all other priorities.
- If RegionalOne's CTO communicates that the MVP scope is insufficient for renewal, we escalate to Sarah for a strategic decision about whether to expand RegionalOne scope at the expense of Q4 migration.

---

## Common Mistakes

1. **Memo as persuasion, not decision support.** A decision memo should make the decision logic transparent so others can evaluate it. If it reads like a sales pitch, you're doing it wrong.
2. **No alternatives.** "We considered doing nothing" is not an alternative. A strong memo shows you seriously considered options that were genuinely attractive and explains why you rejected them.
3. **Trade-offs buried or missing.** Every decision has a cost. If your memo doesn't explicitly state what you're sacrificing, you haven't fully thought through the decision or you're avoiding the uncomfortable part.
4. **Decision drift.** The memo says "we will do X" but the implementation plan describes doing Y. The decision and the plan must be consistent.
5. **Audience mismatch.** A memo for the CEO should focus on strategic implications and risks. A memo for the engineering team should focus on technical rationale and implementation details. Know your audience.
6. **Memo as substitute for conversation.** The memo documents the decision — it doesn't make it. Have the conversation first. Share the memo as follow-up.

## Dependencies

- [One-Way vs. Two-Way Door Classification](../01_core_doctrine/DECISION_FRAMEWORKS.md#framework-1): Use before writing the memo to determine decision process
- [Stakeholder Incentive Map](STAKEHOLDER_INCENTIVE_MAP.md): Use to populate section 6
- [Pre-Mortem Template](PRE_MORTEM_TEMPLATE.md): Use to pressure-test the decision before finalizing
- [Executive One-Pager Template](EXECUTIVE_ONE_PAGER_TEMPLATE.md): For when the audience is exclusively executives
