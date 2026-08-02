# Executive One-Pager Template

## Purpose

An executive one-pager communicates a decision, strategy, or recommendation to executive leadership in one page. It is designed for an audience that has limited time, needs to understand the strategic implications quickly, and may need to make or approve a decision based on the content. A good one-pager enables an executive to have an informed opinion after 3-5 minutes of reading.

This is NOT a summary of a longer document (though it may reference one). It is a standalone communication designed for executive consumption. If the executive needs more detail, provide the longer document separately.

## When to Use

- You need executive approval for a decision or resource allocation
- You're escalating a strategic choice that exceeds your decision authority
- You're providing a board-level update on a significant initiative
- You're communicating a strategy change that leadership needs to understand and support
- You're making a recommendation that requires executive sponsorship

## Template Structure

### Header
- **To:** Executive audience
- **From:** Author
- **Date:** 
- **Subject:** Specific, decision-oriented title (not "Q3 Update" but "Recommendation to Defer Platform Migration to Q4 in Favor of Regulatory Compliance")

### 1. The Situation (2-3 sentences)

What is happening that requires executive attention? Frame the situation in terms the executive cares about — revenue risk, competitive threat, strategic opportunity, organizational challenge. Be specific. No background that the executive already knows.

### 2. The Recommendation (1-2 sentences)

What are you recommending? Be direct and specific. Use active language: "I recommend we..." or "We recommend that the executive team approve..."

If the decision is the executive's to make (not yours to recommend), frame it as a choice: "You have two options. Option A: [describe]. Option B: [describe]. I recommend Option A because..."

### 3. Why This Matters (3-5 bullet points)

Why should the executive care? Connect to:
- Revenue impact (dollars, not percentages)
- Strategic implications (competitive position, market opportunity, strategic coherence)
- Risk (what happens if we don't act, what happens if we get this wrong)
- Organizational implications (team impact, morale, capability)

Every bullet should answer "so what?" — not just state a fact but explain why the fact matters at the executive level.

### 4. The Trade-Off (explicit)

What are we sacrificing? Every recommendation has a cost. Be explicit:
- "We recommend prioritizing X over Y. This means Y will be delayed by Z months."
- "We are accepting that [metric] will likely decrease from A to B in the short term."
- "We are risking [specific risk] in exchange for [specific benefit]."

If you cannot articulate the trade-off, your recommendation is incomplete or you're avoiding the uncomfortable part.

### 5. Alternatives Considered (brief)

What alternatives did you evaluate and reject? (2-3 alternatives, 1 sentence each, including why rejected).

This demonstrates that the recommendation is a choice among options, not the only idea you had.

### 6. Key Risks and Mitigations (3-4)

What are the biggest risks of the recommended approach? How will you mitigate each? Be specific — "execution risk" is not a risk. "The compliance work scope may be 2x our estimate, which would delay the RegionalOne feature by 3-4 weeks" is a risk.

### 7. What We Need From You

What action do you need from the executive?
- **Decision:** Approve the recommendation
- **Input:** Provide guidance on [specific question]
- **Support:** Sponsor the initiative with [specific stakeholder]
- **Resource:** Approve [specific allocation]
- **Communication:** Communicate to [specific audience]

Be specific about what you need and by when. "Approval by Friday" is better than "your thoughts."

### 8. Next Steps

If approved, what happens next?
- Immediate next action (next 48 hours)
- Key milestones (next 30/60/90 days)
- When the executive will next hear about this

---

## Filled Example: Recommendation for FinClear Q3 Resource Allocation

**To:** Sarah Chen, CEO
**From:** Alex Chen, Principal PM, Reconciliation Platform
**Date:** March 15, 2026
**Subject:** Recommendation: Defer Platform Migration to Q4, Prioritize PSD3 Compliance and RegionalOne Feature

### 1. The Situation
We have 8 person-weeks of engineering capacity (2 engineers) over the next 8 weeks and three competing demands totaling 23-27 person-weeks: (1) PSD3 regulatory compliance (deadline: April 30, non-negotiable), (2) RegionalOne custom rule engine (contract renewal in 4 months, 35% of ARR at risk), (3) CTO's platform migration (12-16 weeks, enables real-time processing). We cannot do all three. We must sequence.

### 2. The Recommendation
Complete PSD3 compliance in Weeks 1-3 (Jordan leads, Alex reviews). Build RegionalOne rule engine MVP in Weeks 4-8 (Alex leads, Jordan supports). Defer platform migration to Q4 with a firm commitment to start.

### 3. Why This Matters
- **Revenue protection:** RegionalOne represents $4.2M ARR (35% of total). Their CTO has explicitly requested a timeline on the rule engine and mentioned competitor interest. Losing RegionalOne would be catastrophic for renewal rate and Series B positioning.
- **Regulatory survival:** Missing the PSD3 deadline means we cannot operate in the EU. We have $1.8M existing EU revenue and $4M in EU pipeline. Non-compliance is not a risk — it's a shutdown event.
- **Platform migration is deferrable:** The migration enables future velocity but is not urgent. Deferring to Q4 costs us 2 quarters of real-time processing capability. Prospects who require real-time will be told "Q4." This is a real but manageable cost.
- **Team stability:** Alex is our single point of failure for the reconciliation algorithm. Asking him to context-switch across all three projects risks burnout and attrition. The recommended sequencing protects our most critical engineer.

### 4. The Trade-Off
We are deferring the CTO's platform migration by one quarter. This is the third time the migration has been deferred. The CTO will be frustrated. Real-time processing capabilities (and the prospects who require them) are delayed. We are accepting that our competitive position on "real-time" will not improve in Q3. In exchange, we meet our regulatory obligations and protect our largest customer relationship.

### 5. Alternatives Considered
- **Do all three in parallel:** Rejected. 8 person-weeks of capacity cannot cover 23-27 person-weeks of demand without quality, timeline, or morale consequences. This is mathematically impossible, not just difficult.
- **Prioritize migration, defer compliance:** Rejected. Non-compliance means EU shutdown. Not acceptable.
- **Prioritize migration, defer RegionalOne:** Rejected. RegionalOne CTO has signaled competitive evaluation. The risk of losing $4.2M ARR for a migration that can wait one quarter is not justified.

### 6. Key Risks and Mitigations
- **Risk: Compliance scope is larger than estimated (3 person-weeks).** Mitigation: Week 1 is dedicated to scope confirmation. If scope exceeds 5 person-weeks, we will evaluate contractor support or request a 2-week extension (regulators have granted extensions for good-faith efforts in prior deadlines).
- **Risk: RegionalOne CTO rejects MVP scope (core rule types only).** Mitigation: Elena (VP Sales) will pre-brief the CTO on the timeline and scope, framing MVP as "Phase 1 of a multi-phase rollout." If the CTO demands full scope, we escalate for a strategic decision (may need to trade off migration start date or hire a contractor).
- **Risk: Alex attrition.** Mitigation: Alex leads the high-visibility RegionalOne project with clear ownership. We monitor his workload and sentiment weekly. If attrition signals appear, we escalate immediately.
- **Risk: Migration deferred indefinitely.** Mitigation: Q4 migration commitment is documented in the Q3 roadmap with a named owner (CTO + PM) and a defined scope. Migration start is gated on RegionalOne MVP completion, which is our primary Q3 deliverable.

### 7. What We Need From You
**Decision:** Approve the recommended sequencing (compliance → RegionalOne → migration) by Friday, March 18.
**Support:** Communicate the migration deferral to Marcus (CTO) before the executive staff meeting on Monday. I will brief him separately, but he needs to hear from you that this is a sequencing decision, not a rejection of the migration.

### 8. Next Steps
- **Friday (March 18):** Your approval. I brief Marcus (CTO) on the rationale. Elena briefs RegionalOne CTO on the timeline.
- **Monday (March 21):** Executive staff meeting — alignment on Q3 priorities.
- **Week of March 21:** Compliance sprint begins (Jordan leads). RegionalOne scoping sessions (Alex + Elena).
- **April 30:** PSD3 compliance deadline.
- **May 15:** RegionalOne rule engine MVP target.
- **You'll next hear from me:** Bi-weekly progress update (first: April 1). Immediate escalation if any of the key risks materialize.

---

## Common Mistakes

1. **Too long.** If it doesn't fit on one page (printed), it's not a one-pager. Executives will not read a three-page "one-pager." Edit ruthlessly.
2. **Background over recommendation.** Executives need to know what you're recommending and why, not the entire history of the project. Assume they know the context unless they don't. When in doubt, cut background.
3. **No explicit trade-off.** A recommendation without a trade-off sounds like "everything is great and this has no cost." Executives know everything has a cost. Be honest about the cost.
4. **Hiding the ask.** "Your thoughts" is not an ask. Be specific about what action you need, from whom, by when. Executives appreciate clarity.
5. **No risk section.** Every recommendation has risks. Not acknowledging them signals either overconfidence or incomplete thinking. Executives respect leaders who see the downsides.
6. **Written for yourself.** The one-pager should answer the questions the executive will have, not the questions you find interesting. Think about what keeps the executive up at night and address that.

## Dependencies

- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): The one-pager is a compressed version of the decision memo for executive audiences.
- [Stakeholder Incentive Map](STAKEHOLDER_INCENTIVE_MAP.md): Understanding executive incentives makes the one-pager more effective.
- [Risk-Adjusted Value Assessment](RISK_ADJUSTED_VALUE_ASSESSMENT.md): Reference if the executive wants to see the underlying analysis.
