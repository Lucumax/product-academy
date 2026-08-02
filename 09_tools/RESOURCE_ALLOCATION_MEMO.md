# Resource Allocation Memo

## Purpose

A resource allocation memo makes explicit the trade-offs in how you invest your most constrained resources — typically engineering capacity, but also budget, leadership attention, and organizational focus. It is the answer to: "If we're doing X, what are we NOT doing?" and "Why is this the right allocation of scarce resources?"

This tool is distinct from a roadmap (which shows what you're building when) and a strategy document (which shows direction). It is specifically about the allocation decision — the how much, to what, and at what cost to other things.

## When to Use

- Quarterly or annual planning when you're making explicit resource allocation decisions
- When you're asked to take on additional work and need to make the trade-off visible
- When you're proposing a significant shift in resource allocation
- When the organization is spread too thin and needs to focus
- When you're making the case for additional resources
- Before a board meeting or executive review where resource allocation will be discussed

## Template Structure

### 1. Resource Pool Definition

Define the resource pools you're allocating from. Be specific:
- **Engineering capacity:** X person-weeks per quarter (after accounting for on-call, interviews, meetings, PTO)
- **Budget:** $X per quarter for discretionary spending
- **Leadership attention:** X hours/week of key decision-makers
- **Organizational focus:** How many concurrent initiatives can the organization support without quality degradation?

The most common failure of resource allocation is pretending resources are infinite. Start by defining the pools honestly.

### 2. Current Allocation

Where are resources allocated today? This should be a table or visual:

| Initiative | Engineering (person-weeks) | Budget ($K) | % of Total | Outcome Sought |
|------------|---------------------------|-------------|------------|----------------|
| Initiative A | 24 | $120 | 40% | Reduce churn by 15% |
| Initiative B | 18 | $80 | 30% | Increase expansion by 20% |
| Initiative C | 12 | $40 | 20% | Competitive parity |
| Maintenance/BAU | 6 | $10 | 10% | System reliability |

**Total must sum to 100% of available capacity.** If your current allocation sums to >100% (which it usually does if you're honest), that's the problem — you're already over-allocated.

### 3. Proposed Allocation

What is the proposed allocation? Same format, new numbers. The delta between current and proposed is the decision.

| Initiative | Current % | Proposed % | Delta | Rationale |
|------------|-----------|------------|-------|-----------|
| Initiative A | 40% | 50% | +10% | Churn is worsening; need more investment |
| Initiative B | 30% | 20% | -10% | Expansion motion is working; can sustain with less |
| Initiative C | 20% | 10% | -10% | Competitive parity is achieved; shift to offense |
| Maintenance | 10% | 10% | 0% | Stable |

### 4. What Gets Stopped or Reduced

This is the most important section. Be explicit about what is losing resources and why:
- **Stopped entirely:** Initiatives that are being killed. Why are they being killed? Who needs to know?
- **Reduced:** Initiatives that are being scaled back. By how much? What is being deferred?
- **Deferred:** Initiatives that are being paused. Until when? What triggers resumption?
- **Protected:** Initiatives that will NOT be touched. Why are they protected?

### 5. What Gets Added or Increased

- **New investments:** What is being added? Why now?
- **Increased investments:** What is getting more resources? What is the expected return?
- **One-time investments:** What is a one-time allocation (e.g., migration, compliance project) that will release resources later?

### 6. Trade-off Analysis

For each significant shift (increase or decrease), articulate the trade-off:
- **What we gain:** The expected benefit of the shift
- **What we lose:** The cost or risk of the shift
- **Who benefits:** Which stakeholders, customers, or metrics benefit?
- **Who loses:** Which stakeholders, customers, or metrics are negatively affected?
- **Risk:** What could go wrong with this shift?

### 7. Dependencies and Constraints

- **What must be true for this allocation to work?**
- **What external dependencies could disrupt this allocation?** (e.g., hiring timeline, partner delivery, regulatory changes)
- **What is the single point of failure?** (e.g., one key engineer, one critical system)

### 8. Governance and Reallocation Triggers

- **Review cadence:** How often will this allocation be reviewed?
- **Reallocation triggers:** What would cause a reallocation? (e.g., competitive move, customer loss, technical emergency)
- **Decision authority:** Who can approve reallocations? Within what bounds?

---

## Filled Example: Q3 Resource Allocation for Reconciliation Platform

### 1. Resource Pool Definition
- **Engineering capacity:** 24 person-weeks per quarter (Alex: 11 person-weeks effective, Jordan: 10 person-weeks effective, after on-call, meetings, PTO)
- **Budget:** $50K discretionary per quarter
- **Leadership attention:** PM available 30 hours/week for product work (after stakeholder management, cross-team coordination)
- **Organizational focus:** 2 concurrent major initiatives maximum (3 causes context-switching overhead >25%)

### 2. Current Allocation (Q2 Actual)

| Initiative | Person-weeks | % of Total | Outcome Sought |
|------------|-------------|------------|----------------|
| RegionalOne Rule Engine Design | 8 | 33% | Customer retention (35% ARR) |
| Carrier API Standardization | 8 | 33% | Reduce integration time 4 weeks → 3 days |
| Maintenance/BAU | 4 | 17% | System reliability |
| EU Pipeline Feature Requests | 4 | 17% | Win EU prospects |

**Actual allocation summed to ~100% but maintenance was under-invested (4 person-weeks vs. needed 6). EU pipeline work was ad-hoc and poorly defined.**

### 3. Proposed Allocation (Q3)

| Initiative | Current % | Proposed % | Delta | Rationale |
|------------|-----------|------------|-------|-----------|
| PSD3 Compliance (NEW) | 0% | 25% | +25% | Regulatory deadline April 30 — non-negotiable |
| RegionalOne Rule Engine MVP | 33% | 40% | +7% | Migration design complete; now building MVP |
| Carrier API Standardization | 33% | 0% | -33% | DEFERRED to Q4 — cannot parallelize with compliance + RegionalOne |
| Maintenance/BAU | 17% | 20% | +3% | Correcting Q2 under-investment |
| EU Pipeline Features | 17% | 15% | -2% | Reduced scope; one critical EU prospect feature only |

### 4. What Gets Stopped or Reduced
- **Deferred:** Carrier API Standardization. This was a key Q2-Q3 initiative to reduce integration time from 4 weeks to 3 days. Deferring to Q4 means: (a) 6 prospects in pipeline who need faster integrations may not close in Q3, (b) existing carriers continue to experience 4-week integration times, (c) Elena (VP Sales) will be disappointed.
- **Reduced:** EU pipeline features. Only one critical feature for a high-probability prospect will be built. Other EU prospects will be deferred to Q4.
- **Protected:** Maintenance/BAU. Corrected from Q2 under-investment. Cannot risk system reliability degradation during compliance work.

### 5. What Gets Added or Increased
- **New:** PSD3 Compliance (6 person-weeks). Data retention policy changes, audit trail generation, reporting format changes. Jordan leads with Alex review.
- **Increased:** RegionalOne Rule Engine MVP (10 person-weeks, up from 8). Alex leads design and implementation. Expanded scope from design to MVP delivery (core rule types only).
- **One-time:** Compliance work releases 6 person-weeks back to the pool in Q4.

### 6. Trade-off Analysis
- **Deferring Carrier API:** Gain — compliance is met, RegionalOne is prioritized. Lose — carrier integration velocity, prospect pipeline velocity, Elena's confidence. Risk — a competitor improves their integration experience and we lose competitive advantage in carrier onboarding.
- **Adding PSD3 Compliance:** Gain — EU operations continue, regulatory risk mitigated, EU pipeline preserved. Lose — 6 person-weeks that could have gone to product features. Risk — compliance scope may be larger than estimated (current estimate: medium confidence).

### 7. Dependencies and Constraints
- PSD3 compliance scope must not exceed 8 person-weeks. If it does, RegionalOne timeline is at risk.
- Alex is the single point of failure. If Alex is unavailable for >1 week, all plans are re-evaluated.
- Jordan's ramp-up on compliance domain must succeed. If Jordan cannot lead compliance independently, Alex is pulled from RegionalOne.

### 8. Governance and Reallocation Triggers
- **Review cadence:** Monthly allocation review with CTO and CEO
- **Reallocation triggers:** (a) Compliance scope exceeds 8 person-weeks, (b) Alex attrition risk increases, (c) RegionalOne CTO demands a timeline we cannot meet, (d) competitor announces faster carrier integration
- **Decision authority:** PM proposes, CEO approves. Reallocations within ±10% of plan are PM authority.

---

## Common Mistakes

1. **Allocation >100%.** The most common and most damaging mistake. If your allocation sums to >100%, you're lying to yourself about what can be done. The gap between plan and reality will be absorbed by quality, morale, or deadlines.
2. **No explicit "stopped" list.** A resource allocation that only talks about what you're starting is not an allocation — it's a wish list. You must identify what you're stopping, reducing, or deferring.
3. **Treating people as interchangeable units.** "We have 20 person-weeks" ignores that different people have different skills, domain knowledge, and context-switching costs. Alex (staff engineer with deep domain knowledge) is not interchangeable with Jordan (senior engineer still ramping up).
4. **Underestimating maintenance/BAU.** Teams typically need 15-25% of capacity for maintenance, on-call, bug fixes, and operational overhead. Allocating <15% to BAU is a recipe for quality degradation.
5. **False precision.** Person-weeks to one decimal place suggest more certainty than exists. Use ranges for uncertain estimates.
6. **Allocation as annual exercise.** Resource allocation should be reviewed at least quarterly. Annual allocation plans that aren't revisited are fiction by Q2.

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Strategy should drive allocation
- [Risk-Adjusted Value Assessment](RISK_ADJUSTED_VALUE_ASSESSMENT.md): For comparing investment alternatives
- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): For communicating a significant reallocation
- [Stakeholder Incentive Map](STAKEHOLDER_INCENTIVE_MAP.md): For anticipating reactions to reallocation
