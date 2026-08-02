# Metrics Tree Template

## Purpose

A metrics tree decomposes a high-level business outcome (like revenue growth or customer retention) into its constituent drivers, sub-drivers, and leading indicators. It answers the question: "If we want to move Outcome X, what levers can we pull, and how will we know if we're pulling the right ones?"

A metrics tree serves three functions: (1) it creates shared understanding of how the business works, (2) it identifies the specific levers product teams can influence, (3) it connects product actions to business outcomes so teams can see how their work matters.

## When to Use

- You're setting up a measurement system for a product or business
- You need to connect team-level metrics to company-level outcomes
- You're designing OKRs and need to ensure they ladder up to business results
- You're diagnosing why a business outcome isn't moving despite product investment
- You need alignment across teams on what metrics matter and why
- You're onboarding a new team or leader who needs to understand how the business works

## Template Structure

### 1. The North Star

Define the single metric that best captures the value your product delivers to customers. This is NOT a revenue metric — it's a value metric:
- Good: "Weekly active teams using collaborative features" (Slack-style), "Nights booked" (Airbnb-style)
- Bad: "Revenue" (lagging, doesn't measure value), "DAU" (too broad, doesn't capture value)

Your North Star should be: (a) measurable, (b) connected to customer value, (c) leading indicator of business outcomes, (d) actionable by product teams.

### 2. The Tree

Build the tree from top to bottom:

```
NORTH STAR METRIC
│
├── DRIVER 1: [Acquisition metric]
│   ├── Sub-driver 1.1: [Specific lever]
│   │   ├── Leading indicator: [Early signal]
│   │   └── Leading indicator: [Early signal]
│   └── Sub-driver 1.2: [Specific lever]
│       ├── Leading indicator: [Early signal]
│       └── Leading indicator: [Early signal]
│
├── DRIVER 2: [Engagement/Activation metric]
│   ├── Sub-driver 2.1: [Specific lever]
│   └── Sub-driver 2.2: [Specific lever]
│
├── DRIVER 3: [Retention/Expansion metric]
│   ├── Sub-driver 3.1: [Specific lever]
│   └── Sub-driver 3.2: [Specific lever]
│
└── COUNTER-METRICS: [What should NOT change]
    ├── Counter-metric 1
    └── Counter-metric 2
```

### 3. Metric Definitions

For each metric in the tree, define:

| Metric | Definition | Source | Frequency | Owner | Target | Threshold |
|--------|------------|--------|-----------|-------|--------|-----------|
| Metric name | Precise definition (formula, inclusion/exclusion criteria) | Where the data comes from | How often it's measured | Who is accountable | Desired value | Value that triggers escalation |

Without definitions, metrics are ambiguous. "Active users" means different things to different people. Define it precisely.

### 4. Leading vs. Lagging Indicators

Tag each metric as leading or lagging:
- **Leading indicators:** Predict future outcomes. Change before the outcome changes. Examples: activation rate, feature adoption, pipeline velocity, time-to-value.
- **Lagging indicators:** Confirm past outcomes. Change after the outcome has already changed. Examples: revenue, churn, NPS.

A good metrics tree has more leading than lagging indicators. If your tree is mostly lagging indicators, you're measuring history, not predicting the future.

### 5. Counter-Metrics

For each major driver, define a counter-metric — something that could get worse if teams optimize too aggressively for the driver. Without counter-metrics, you get Goodhart's Law: "When a measure becomes a target, it ceases to be a good measure."

Examples:
- If you optimize for "new user signups," counter-metric: "signup-to-activation rate" (to catch low-quality signups)
- If you optimize for "feature adoption," counter-metric: "support ticket volume for that feature" (to catch confusing features that get adopted but create frustration)
- If you optimize for "revenue per customer," counter-metric: "customer satisfaction" (to catch price gouging)

### 6. Team-to-Metric Mapping

Map each metric to the team(s) that can influence it. This is how you connect team work to business outcomes:

| Metric | Influencing Team(s) | How They Influence It | Current Baseline |
|--------|--------------------|-----------------------|-----------------|
| Activation rate | Growth, Onboarding | Improve first-run experience, reduce time-to-value | 32% |
| Feature adoption | Core Product, Education | Build features users need, teach users to use them | 22% (new features) |

### 7. Review Cadence

- **Weekly:** Leading indicators reviewed by product teams
- **Monthly:** Driver metrics reviewed by product leadership
- **Quarterly:** North Star and business outcomes reviewed by executive team
- **Triggers:** What metric movements trigger an escalation or deep dive?

---

## Filled Example: SaaS Collaboration Platform

### 1. The North Star
**Weekly Active Collaborators (WAC):** The number of unique users who create, edit, or comment on shared documents in a given week. This captures the core value — collaborative work on shared content. It's measurable, leading (predicts retention and expansion), and actionable by product teams.

### 2. The Tree

```
WEEKLY ACTIVE COLLABORATORS (WAC)
│
├── DRIVER 1: New Team Activation
│   ├── Signup-to-collaboration rate
│   │   ├── Leading: Time to first collaborative action (days)
│   │   └── Leading: % of signups completing onboarding within 7 days
│   ├── Team invitation acceptance rate
│   │   ├── Leading: Invitation email open rate
│   │   └── Leading: % of invited users who create account within 48 hours
│   └── First-week retention
│       ├── Leading: % of new users returning on Day 2
│       └── Leading: % of new users returning on Day 7
│
├── DRIVER 2: Collaboration Depth
│   ├── Documents per active user per week
│   │   ├── Leading: Document creation rate (new docs/user/week)
│   │   └── Leading: Template usage rate (% of new docs from templates)
│   ├── Collaborators per document
│   │   ├── Leading: Share rate (% of docs shared with ≥1 person)
│   │   └── Leading: Comment rate (comments/doc/week)
│   └── Collaboration frequency
│       ├── Leading: Sessions per user per week
│       └── Leading: Real-time co-editing sessions per week
│
├── DRIVER 3: Team Retention
│   ├── Team weekly active rate
│   │   ├── Leading: % of teams with ≥3 WAC in past week
│   │   └── Leading: % of teams with WAC decline for 2+ consecutive weeks
│   ├── Seat expansion
│   │   ├── Leading: Seats added per team per quarter
│   │   └── Leading: % of teams at seat limit (needing upgrade)
│   └── Feature depth adoption
│       ├── Leading: % of teams using ≥3 product features
│       └── Leading: Advanced feature adoption rate (workflows, integrations)
│
└── COUNTER-METRICS
    ├── Support ticket volume (per 1000 WAC)
    ├── Bug report rate (per release)
    ├── Churn survey: % citing "too complex" as reason
    └── Page load time (p95, seconds)
```

### 3. Metric Definitions (Sample)

| Metric | Definition | Source | Frequency | Owner | Target | Threshold |
|--------|------------|--------|-----------|-------|--------|-----------|
| WAC | Unique users who performed ≥1 create, edit, or comment action on a shared document in the trailing 7 days. Excludes: view-only actions, actions on private documents. | Product analytics DB | Weekly | Head of Growth | +15% QoQ | <5% QoQ triggers deep dive |
| Signup-to-collaboration rate | % of new signups who perform ≥1 collaborative action within 14 days of signup. Numerator: users with collaborative action. Denominator: all new signups in the cohort. | Product analytics DB | Weekly (by cohort) | Growth PM | 45% | <30% triggers onboarding review |
| Time to first collaborative action | Median days from signup to first collaborative action. Only includes users who eventually collaborate. | Product analytics DB | Weekly (by cohort) | Growth PM | <3 days | >5 days triggers onboarding review |

### 4. Leading vs. Lagging

- **Leading:** Signup-to-collaboration rate, time to first action, Day 2 retention, share rate, session frequency, teams with WAC decline
- **Lagging:** WAC (semi-lagging — reflects past week but predicts future), quarterly revenue, annual churn, NPS

### 5. Counter-Metrics Rationale
- **Support tickets per 1000 WAC:** If teams optimize for WAC by shipping features fast but poor quality, support tickets rise.
- **Bug report rate:** If engineering velocity increases at the expense of quality, this catches it.
- **Churn survey complexity:** If teams add features to drive WAC but the product becomes too complex, this catches it.
- **Page load time:** If the product gets feature-bloated and slow, WAC may hold steady while user satisfaction drops.

### 6. Team-to-Metric Mapping

| Metric | Influencing Team(s) | How They Influence It | Baseline |
|--------|--------------------|-----------------------|----------|
| Signup-to-collaboration rate | Onboarding, Core Product | Improve first-run experience, reduce setup friction, smart defaults | 32% |
| Collaborators per document | Collaboration, Sharing | Improve share flow, real-time co-editing, notifications | 1.8 |
| Team weekly active rate | Retention, Core Product | Improve habit formation, notification relevance, value reinforcement | 62% |
| Feature depth adoption | Education, Platform | In-app discovery, contextual prompts, integrations marketplace | 28% |

### 7. Review Cadence
- **Weekly:** Growth team reviews leading indicators (signup-to-collaboration rate, Day 2/7 retention). Core product team reviews collaboration depth metrics.
- **Monthly:** Product leadership reviews all driver metrics + counter-metrics. Deep dive on any metric outside threshold.
- **Quarterly:** Executive team reviews WAC trend + business outcomes (revenue, retention, NPS). Strategy adjustments based on driver performance.
- **Triggers:** WAC growth <5% QoQ → deep dive. Counter-metric exceeds 2x baseline → investigation. Two consecutive weeks of declining Day 7 retention → onboarding sprint.

---

## Common Mistakes

1. **North Star as revenue.** Revenue is a result of value creation, not a measure of it. Your North Star should measure the value you create for customers.
2. **Metrics tree as exhaustive taxonomy.** You don't need to measure everything. Focus on the metrics that have the strongest causal relationship to your North Star.
3. **No counter-metrics.** Every optimization has a dark side. Without counter-metrics, you optimize blindly.
4. **Undefined metrics.** "Engagement" means nothing until you define it precisely. Two teams using the same metric name with different definitions is a recipe for confusion.
5. **Metrics without owners.** If nobody is accountable for a metric, it won't be managed. Metrics ownership should be specific (named person, not "the team").
6. **Annual metrics review.** Metrics trees should evolve as you learn what actually drives outcomes. Review and update at least quarterly.

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Strategy defines what outcomes matter. The metrics tree operationalizes them.
- [Experiment Design Template](EXPERIMENT_DESIGN_TEMPLATE.md): Experiments target specific metrics in the tree.
- [Evaluation Contract Template](EVALUATION_CONTRACT_TEMPLATE.md): For defining how a team will be evaluated against metrics in the tree.
- [Core Doctrine: PRN-0009](../01_core_doctrine/PRINCIPLES.md): Metrics and counter-metrics principle.
