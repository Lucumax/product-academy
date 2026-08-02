# Evaluation Contract Template

## Purpose

An evaluation contract is a shared agreement between a product team and its stakeholders (leadership, cross-functional partners) about how the team's work will be evaluated. It answers: "What does success look like for this team, how will we measure it, over what timeframe, and who decides?" The contract prevents the most common evaluation failure — where teams are told to focus on outcomes but are actually evaluated on outputs.

This is distinct from OKRs (which define objectives and key results) and from a team charter (which defines how the team works). The evaluation contract defines how the team will be JUDGED.

## When to Use

- Setting up a new product team
- Changing a team's mission or focus
- When there's confusion about how a team's performance is evaluated
- When a team is being measured on outputs (features shipped) but told to focus on outcomes
- When a team is being evaluated on metrics they cannot influence
- As part of quarterly or annual planning to align expectations

## Template Structure

### 1. Team Identity

- **Team name and mission:** What does this team exist to do?
- **Team composition:** Roles and headcount
- **Key stakeholders:** Who has a stake in this team's success? (Manager, peer teams, dependent teams, executives)

### 2. Success Definition

**Primary outcome (12-month horizon):**
What is the single most important outcome this team should achieve in the next 12 months? This is NOT a feature or a project — it's a customer or business outcome the team can influence.

**Secondary outcomes (12-month horizon):**
What other outcomes matter? (Limit to 2-3 to maintain focus.)

**Leading indicators (quarterly):**
What metrics will show progress toward the primary outcome on a quarterly basis? These should be leading (predict the primary outcome) and actionable (the team can influence them).

**Counter-indicators (quarterly):**
What metrics should NOT degrade as the team pursues its primary outcome?

### 3. What the Team Controls

For each outcome, specify what the team CAN and CANNOT control:
- **Directly controlled:** What the team can change through its own decisions and work
- **Influenced:** What the team can affect but not control (requires cross-functional support, market conditions, user behavior)
- **Outside control:** What affects the outcome but is outside the team's influence (macroeconomic factors, competitor actions, regulatory changes)

This section prevents teams from being held accountable for outcomes they cannot influence.

### 4. Evaluation Framework

**How will the team be evaluated?**

| Dimension | Weight | Measured By | Evaluated By | Cadence |
|-----------|--------|-------------|-------------|---------|
| Outcome achievement | % | Primary + secondary outcome metrics | Manager + stakeholders | Quarterly |
| Decision quality | % | Pre-mortem accuracy, experiment velocity, learning rate | Manager + peer review | Quarterly |
| Execution quality | % | Delivery predictability, quality metrics, stakeholder satisfaction | Engineering counterpart + stakeholders | Quarterly |
| Team health | % | Engagement survey, retention, team 360 feedback | Manager + team | Quarterly |

The weights should reflect what the organization values. If outcome achievement is 70% but the team only controls 30% of the factors that influence the outcome, the weights are misaligned with reality.

### 5. Decision Rights

What decisions can the team make independently vs. require escalation?

| Decision Type | Team Authority | Escalation Required |
|--------------|----------------|-------------------|
| Feature prioritization within scope | Full authority | — |
| Changing team scope or mission | Recommend | Manager approval |
| Technology choices | Full authority (within architecture guidelines) | Principal architect for deviations |
| Hiring/firing | Recommend | Manager + HR approval |
| Budget reallocation (<$X) | Full authority | — |
| Budget reallocation (>$X) | Recommend | Manager approval |
| Customer commitments (timelines, features) | Recommend | Manager OR stakeholder approval |
| Experiment design and launch | Full authority (within guardrail metrics) | Manager for experiments with >$X risk |

### 6. Resource Commitment

What resources does the team have to achieve its outcomes?
- **Headcount:** Current and planned
- **Budget:** Discretionary and allocated
- **Leadership support:** Executive sponsor, escalation path
- **Cross-functional support:** Design, research, data science, marketing, sales enablement
- **Constraints:** What resources are NOT available that the team might expect?

### 7. Guardrails and Boundaries

What constraints does the team operate within?
- **Strategic boundaries:** Markets, segments, use cases the team should NOT pursue
- **Technical boundaries:** Architecture decisions that require broader alignment
- **Brand/UX boundaries:** Design system compliance, brand voice, accessibility standards
- **Legal/regulatory boundaries:** Compliance requirements, data handling, privacy
- **Ethical boundaries:** User segments or use cases that are off-limits

### 8. Stakeholder Commitments

What do stakeholders commit to do to support the team's success?
- **Manager commits to:** [specific commitments — e.g., "Unblock escalations within 48 hours," "Provide strategic context quarterly," "Protect team from priority churn"]
- **Cross-functional partners commit to:** [specific commitments — e.g., "Design reviews within 5 business days," "Sales will not commit features without product review"]
- **Team commits to:** [what the team commits to deliver to stakeholders — e.g., "Monthly progress updates," "Early visibility into timeline risks"]

### 9. Review and Adjustment

- **Review cadence:** When is this contract reviewed? (Quarterly recommended)
- **Adjustment triggers:** What would cause the contract to be renegotiated? (Strategy change, team restructure, resource change, major market shift)
- **Sunset clause:** When does this contract expire? (Contracts should have an end date, even if long — annual is typical)

---

## Filled Example: Core Learning Team Evaluation Contract

### 1. Team Identity
- **Team:** Core Learning (Course Authoring, Content Delivery, Assessment, Reporting)
- **Mission:** Enable mid-market companies to create, deliver, and measure employee training that drives measurable behavior change and compliance.
- **Composition:** 1 PM (Sandra), 4 engineers, 1 designer, 0.5 user researcher (shared)
- **Key stakeholders:** VP Product (manager), VP Engineering (Raj), VP Sales (Derek), VP Customer Success (Aisha), CEO (Maya)

### 2. Success Definition

**Primary outcome (12 months):**
Increase Net Revenue Retention (NRR) from 103% to 110% by reducing logo churn from 14% to 10% and increasing expansion revenue from 24% to 30% of new ARR.

**Secondary outcomes (12 months):**
- Increase feature adoption rate for new features from 22% to 40% (customers get value from what we build)
- Improve NPS from 39 to 50 (customers perceive increasing product value)

**Leading indicators (quarterly):**
- Time-to-first-value for new customers (target: <14 days from signup to first course completion)
- Active teams rate (% of customer accounts with >80% of licensed seats active in past 30 days)
- Feature depth adoption (% of customers using >5 product features)

**Counter-indicators (quarterly):**
- Support ticket volume per customer (should NOT increase >10% QoQ)
- Customer-reported bugs (should NOT increase >5% QoQ)
- System uptime (should NOT drop below 99.9%)

### 3. What the Team Controls

**Directly controlled:**
- Product features, UX, and quality
- Onboarding experience and time-to-first-value
- Feature discoverability and adoption
- Product reliability and performance

**Influenced (not controlled):**
- Customer retention (influenced by product quality AND customer success interactions AND customer's internal adoption)
- Expansion revenue (influenced by product capabilities AND sales effectiveness AND customer budget cycles)
- NPS (influenced by product AND support quality AND account management AND billing experience)

**Outside control:**
- Macroeconomic conditions affecting customer training budgets
- Competitive moves (competitor pricing, features)
- Customer organizational changes (new leadership, budget freezes, layoffs)

### 4. Evaluation Framework

| Dimension | Weight | Measured By | Evaluated By | Cadence |
|-----------|--------|-------------|-------------|---------|
| Outcome achievement | 50% | NRR, logo churn, expansion revenue, NPS trends | Manager (VP Product) + CEO review | Quarterly |
| Decision quality | 25% | Pre-mortem accuracy (did we anticipate failure modes?), experiment velocity (experiments/quarter), learning documentation (post-launch reviews completed) | Manager + peer PM review | Quarterly |
| Execution quality | 15% | Cycle time, on-time delivery, quality metrics (bugs/regressions) | Engineering Manager (peer) + Manager | Quarterly |
| Team health | 10% | Team engagement survey, retention, 360 feedback | Manager + team | Quarterly |

**Note on Outcome Achievement:** Because the team only partially controls retention and NPS (influenced by CS, sales, market), outcome achievement is evaluated on TREND and DIRECTION, not absolute values. "NRR moved from 103% to 107% and the team can articulate how their work contributed" is success even if the target was 110%.

### 5. Decision Rights

| Decision Type | Team Authority | Escalation Required |
|--------------|----------------|-------------|
| Feature prioritization within Core Learning scope | Full authority | — |
| Experiment design and launch (within guardrails) | Full authority | Manager for experiments with >$10K/month revenue risk |
| Customer commitments (timelines) | Team defines, communicates to CS | Manager for commitments to top-20 accounts |
| Technology choices | Full authority (within architecture standards) | Principal architect for new technology introductions |
| UX changes that affect NPS or core workflows | Full authority (with user research validation) | Manager for major redesigns |
| Scope changes that affect other teams | Recommend | Manager + affected team approval |
| Hiring recommendations | Recommend | Manager + HR |

### 6. Resource Commitment
- **Headcount:** 4 engineers, 1 PM, 1 designer, 0.5 user researcher (shared). PM hiring planned for Q3.
- **Budget:** $15K/quarter discretionary (user research incentives, prototyping tools, team development)
- **Leadership support:** Executive sponsor: VP Product. Escalation path: PM → VP Product → CEO.
- **Cross-functional support:** User research (shared, 20 hours/week). Data science (on request, 2-week SLA). Customer insights from CS team (monthly churn analysis, quarterly voice-of-customer report).
- **Constraints:** No dedicated data analyst. No dedicated technical writer. Engineering capacity is 4 engineers with no planned additions.

### 7. Guardrails and Boundaries
- **Strategic boundaries:** Core Learning scope is course authoring, content delivery, assessment, and reporting. The team does NOT work on: integrations, platform infrastructure, mobile apps, AI/ML features. If a customer need requires one of these, it's escalated to the appropriate team.
- **Technical boundaries:** Must use approved tech stack (React, Go, PostgreSQL). New technology introductions require principal architect review. Cannot modify shared authentication or data pipeline without platform team coordination.
- **UX boundaries:** Must comply with design system. Major UX pattern changes require design team review. Accessibility: WCAG 2.1 AA compliance required for all customer-facing features.
- **Legal/regulatory:** Training content may include PII — data handling must comply with GDPR and CCPA. SCORM/xAPI compliance for content interoperability.

### 8. Stakeholder Commitments
- **Manager (VP Product) commits to:** Provide strategic context quarterly (strategy updates, competitive intelligence, market trends). Unblock escalations within 48 hours. Protect the team from priority churn (feature requests from sales, CEO conference features). Advocate for the team's resource needs. Provide honest, timely feedback on performance.
- **VP Sales (Derek) commits to:** Not promise features or timelines without product review. Share competitive loss reasons within 2 weeks. Provide quarterly pipeline context. Participate in quarterly product-sales alignment session.
- **VP Customer Success (Aisha) commits to:** Share churn analysis monthly. Provide voice-of-customer report quarterly. Escalate at-risk accounts with product-related concerns within 1 week. Participate in quarterly product-CS alignment session.
- **Team commits to:** Monthly progress updates to stakeholders (one-pager: outcomes, learnings, next priorities). Early visibility into timeline risks (>2 week deviation triggers communication). Post-launch reviews for significant features. Quarterly self-assessment against this contract.

### 9. Review and Adjustment
- **Review cadence:** Quarterly review with manager + key stakeholders. Annual comprehensive review.
- **Adjustment triggers:** Strategy change at company or product level. Team restructure or mission change. Resource change (>20% headcount change). Market shift that renders current outcomes irrelevant. Consecutive quarters where team cannot influence primary outcome despite good decisions (the outcome may be the wrong one for this team).
- **Sunset:** This contract is valid for 12 months (through Q4 2027). Renew or replace at that time. Can be renegotiated earlier by mutual agreement.

---

## Common Mistakes

1. **Holding teams accountable for outcomes they don't control.** "The team's success metric is revenue growth" when the team builds a feature used by 5% of customers. The team does not control revenue growth. Connect team outcomes to things the team can actually influence.
2. **Outputs disguised as outcomes.** "Ship 10 features" is an output. "Increase feature adoption to 40%" is an outcome. The evaluation contract should measure outcomes.
3. **Weights that don't match reality.** If outcome achievement is 80% of evaluation but the team only controls 20% of what drives the outcome, the evaluation is unfair and will demotivate the team.
4. **No counter-indicators.** Evaluating a team solely on "increase engagement" without monitoring "and don't increase fraud" creates perverse incentives.
5. **Contract as one-way commitment.** The contract should specify what stakeholders commit to the team, not just what the team commits to stakeholders. This builds mutual accountability.
6. **Set and forget.** The contract is a living document. If it hasn't been reviewed in 6+ months, it's probably irrelevant to the team's actual work.

## Dependencies

- [Product Principles Template](PRODUCT_PRINCIPLES_TEMPLATE.md): Principles inform what the evaluation should reward and penalize.
- [Metrics Tree Template](METRICS_TREE_TEMPLATE.md): The team's outcomes should connect to the company's metrics tree.
- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): The team's mission and outcomes should align with product strategy.
- [Resource Allocation Memo](RESOURCE_ALLOCATION_MEMO.md): The resource commitment section should reflect actual resource allocation.
