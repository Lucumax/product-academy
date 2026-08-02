# Product Thesis Template

## Purpose

A product thesis is the fundamental bet your product makes about the market, the customer, and the value you create. It is the answer to: "If we are right about one thing, what is it?" A good thesis is specific, falsifiable, and guides decisions. A bad thesis is vague ("we help companies be more productive") and unfalsifiable. This template helps you articulate and pressure-test your product thesis.

## When to Use

- You're defining a new product or major initiative
- Your existing product strategy feels directionless and you need to return to fundamentals
- You're evaluating whether to pivot
- A new competitor has entered the market and you need to re-examine your assumptions
- You're preparing for a funding round or board presentation
- You've achieved product-market fit and want to document WHY you have it (to protect against PMF decay)

## Template Structure

### 1. The Core Thesis

State your thesis in 2-3 sentences. It should include:
- Who the customer is (specific segment, not "everyone")
- What problem they have (specific, acute, expensive problem)
- Why your solution is uniquely positioned to solve it
- What the world looks like if you succeed

**Example (weak):** "We help businesses manage their data better."

**Example (strong):** "Mid-market e-commerce companies ($10M-$100M GMV) cannot get a unified view of customer behavior across their storefront, email, and ads because their data lives in silos. Our platform normalizes cross-channel data into a single customer profile that updates in real time, enabling marketing teams to personalize campaigns without a data engineering team. If we succeed, mid-market retailers will compete on customer experience with the same sophistication as Amazon — without needing Amazon's engineering budget."

### 2. Market Evidence

What evidence supports the thesis? Separate into three categories:
- **Problem evidence:** Data that proves the problem is real, acute, and widespread (customer interviews, market research, industry data, your own experience)
- **Solution evidence:** Data that proves your approach works (pilot results, early customer outcomes, technical validation)
- **Market timing evidence:** Data that proves NOW is the right time (technology shifts, regulatory changes, competitive dynamics, behavior changes)

For each piece of evidence, rate your confidence (High/Medium/Low) and note what would change your mind.

### 3. Falsification Conditions

What evidence would prove your thesis wrong? Be specific:
- "If we cannot get enterprise customers to switch from their existing solution within 6 months of pilot..."
- "If customer acquisition cost (CAC) remains above $X after we've optimized the funnel for 3 quarters..."
- "If the technology shift we're betting on (e.g., LLM adoption in compliance workflows) doesn't materialize at the pace we expect..."

Falsification conditions are the most important part of a thesis. A thesis without falsification conditions is a belief, not a bet.

### 4. Assumptions Inventory

List ALL the assumptions your thesis depends on, organized by risk:
- **Existential assumptions:** If these are wrong, the thesis fails entirely (e.g., "customers are willing to switch from their existing solution")
- **Major assumptions:** If these are wrong, the thesis needs significant modification (e.g., "the total addressable market is at least $X")
- **Minor assumptions:** If these are wrong, the thesis still holds but execution changes (e.g., "customers prefer monthly billing to annual contracts")

For existential and major assumptions, specify:
- Current confidence level (High/Medium/Low)
- What evidence would increase confidence
- What you're doing to validate this assumption
- By when you'll know if it's true

### 5. Competitive Moat

What makes this thesis defensible? Identify:
- **Current moat:** What protects you today? (technology, data, network effects, brand, switching costs, team expertise)
- **Future moat:** What will protect you in 3-5 years as competitors catch up? (data network effects, ecosystem/platform lock-in, brand as category definer, regulatory advantage)
- **Moat vulnerability:** What could erode your moat? Be specific — not "a competitor could build the same thing" but "a competitor with an existing data integration platform could add our normalization layer as a feature"

### 6. Resource Requirements

What does this thesis require to succeed?
- Capital required to reach the next milestone
- Key hires needed (roles, not headcount)
- Technical capabilities that must be built
- Partnerships or integrations that are critical
- Time to validate key assumptions

### 7. Staging and Milestones

What are the stages of thesis validation?
- **Stage 1: Problem validation** (e.g., 20 customer interviews, 80% report the problem is acute)
- **Stage 2: Solution validation** (e.g., pilot with 5 customers, 3 achieve target outcomes)
- **Stage 3: Go-to-market validation** (e.g., 10 customers acquired through repeatable GtM motion, CAC < $X)
- **Stage 4: Scale validation** (e.g., 50 customers, NRR > 100%, expansion motion working)

For each stage, define: success criteria, timeline, investment required, and Go/No-Go decision criteria.

### 8. Reversal Conditions

Under what conditions would you abandon or significantly modify this thesis? Be specific. "Never" is not an acceptable answer — every thesis has conditions under which it should be abandoned. If you can't think of any, you haven't thought hard enough.

## Filled Example: Compliance Automation Platform

**Product:** Athena Compliance (automated compliance workflows for mid-market companies)

### Core Thesis
Mid-market companies (100-1,000 employees) spend $200K-$500K annually on compliance (SOC 2, GDPR, HIPAA) using manual processes and expensive consultants because existing compliance software is built for enterprises ($1M+ price tags) or startups (too limited for mid-market complexity). Our platform automates 80% of the manual work at 30% of the cost of consultants, enabling mid-market companies to achieve and maintain compliance without a dedicated compliance team. If we succeed, compliance becomes a continuous automated process rather than a periodic fire drill — and mid-market companies can sell to enterprise customers without compliance being the blocker.

### Market Evidence
- **Problem evidence (Confidence: High):** 40 customer interviews with mid-market CISOs and compliance officers. 34/40 reported compliance as a top-3 operational pain. Average spend on compliance consulting: $280K/year. Average time spent by internal teams on compliance: 15 hours/week.
- **Solution evidence (Confidence: Medium):** MVP deployed at 4 early customers. Average time savings: 12 hours/week. Customer-reported NPS: 45. But sample size is small and early adopters may not represent the broader market.
- **Market timing evidence (Confidence: Medium):** Three tailwinds: (1) AI is making evidence collection automatable in ways that weren't possible 2 years ago, (2) enterprise procurement increasingly requires SOC 2/GDPR compliance from vendors of all sizes, (3) compliance talent is increasingly expensive and scarce.

### Falsification Conditions
1. If we cannot achieve $100K ARR with CAC payback < 12 months within 18 months of GA launch, the mid-market segment may not have willingness to pay for automated compliance.
2. If customer retention (logo churn) exceeds 15% annually after the first year, the product may not be delivering enough ongoing value to justify subscription pricing.
3. If AI-powered evidence collection from source systems (AWS, GitHub, Jira) proves technically infeasible or requires per-system integrations that are uneconomical, our automation advantage vs. manual processes is reduced to an incremental improvement.

### Assumptions Inventory
- **Existential:** Mid-market companies will pay for compliance software (not just consulting). Confidence: Medium. Validating via: pilot conversion rates and willingness-to-pay surveys.
- **Existential:** AI can automate 80%+ of manual evidence collection. Confidence: Low. Validating via: technical prototype of automated evidence collection from 3 common systems. Target: prototype complete in 8 weeks.
- **Major:** The market is large enough ($500M+ TAM) to support a venture-scale business. Confidence: Medium. Validating via: bottom-up TAM analysis using industry data on mid-market company counts and compliance spending.

### Competitive Moat
- **Current:** Deep domain expertise in compliance workflows (founders have 15+ years combined compliance experience). Early mover in mid-market compliance automation.
- **Future:** Data network effect — the platform learns compliance patterns across customers and improves automation for all. Integration depth — once we're integrated into a customer's infrastructure (AWS, GitHub, Jira), switching costs are high.
- **Vulnerability:** Vanta and Drata could expand downmarket and add mid-market features. They have brand recognition and funding we lack.

### Resource Requirements
- $3M to reach $1M ARR (18 months)
- Key hires: 2 senior engineers (backend, ML), 1 GTM lead, 1 customer success
- Technical: automated evidence collection from AWS, GitHub, Jira, Okta
- Partnerships: auditor relationships (compliance is sold through auditor recommendations)

### Staging and Milestones
- Stage 1 (Complete): Problem validated — 34/40 interviews confirmed acute pain
- Stage 2 (In Progress): Solution validated — 4 pilot customers, targeting 10 with measurable outcomes by Q2
- Stage 3 (Next): GTM validated — target $100K ARR, CAC < $12K, payback < 12 months by Q4
- Stage 4 (Future): Scale validated — target $1M ARR, NRR > 110% by Q4 next year

### Reversal Conditions
1. If 3 of the next 5 pilots fail to achieve >50% time savings, the solution hypothesis is likely wrong.
2. If CAC exceeds $20K after GTM optimization (6 months of iteration), the unit economics don't work for venture scale.
3. If a well-funded competitor achieves >50% market share in mid-market compliance automation within 24 months, the window may have closed.

---

## Common Mistakes

1. **Thesis as marketing copy.** "We help businesses work better together" is a tagline, not a thesis. A thesis makes a specific, falsifiable claim about a specific customer and a specific problem.
2. **No falsification conditions.** If you can't describe what would prove your thesis wrong, you have a belief, not a thesis. Beliefs are fine for motivation but dangerous for resource allocation.
3. **Confidence inflation.** Every assumption labeled "High confidence" is a red flag. High confidence should be reserved for assumptions validated by multiple independent sources of evidence.
4. **Moat as aspiration.** "Our moat will be brand" when you have zero brand recognition is wishful thinking. Your moat should be based on what exists today or what you have a clear, credible path to building.
5. **Resource requirements as afterthought.** A thesis that requires $20M to validate with a $2M bank account is not a bet — it's a fantasy. Resource requirements must connect to your actual financial reality.

## Dependencies

- [Product Principles Template](../09_tools/PRODUCT_PRINCIPLES_TEMPLATE.md): Your product principles should align with your thesis
- [Risk-Adjusted Value Assessment](../09_tools/RISK_ADJUSTED_VALUE_ASSESSMENT.md): For evaluating the thesis as an investment
- [Decision Memo Template](../09_tools/DECISION_MEMO_TEMPLATE.md): For communicating a thesis change to stakeholders
- [Core Doctrine: PRN-0004](../01_core_doctrine/PRINCIPLES.md): PMF as a condition, not a milestone — your thesis defines what PMF looks like for your product
