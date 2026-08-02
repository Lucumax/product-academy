# Opportunity Assessment Template

## Purpose

An opportunity assessment evaluates whether a new market, segment, product area, or major initiative is worth pursuing. It is the structured answer to "should we do this?" before any significant resources are committed. Unlike a business case (which is often a justification document), an opportunity assessment is an honest evaluation — it should be equally useful for concluding "no" as "yes."

This template is designed for opportunities large enough to warrant structured analysis but not so large that they require a full strategy process. For major strategic bets, combine with the Product Strategy Template.

## When to Use

- Evaluating a new market or customer segment
- Considering a major product expansion
- Responding to a large customer request that could become a product direction
- Assessing a partnership or platform play
- Pre-work for annual planning or investment decisions
- Any situation where someone says "we should do X" and the commitment is >10% of team capacity for >1 quarter

## Template Structure

### 1. Opportunity Summary

In 3-5 sentences: What is the opportunity? Who is the customer? What problem do they have? What value would we create? What is the rough scale?

### 2. Problem Validation

- **What is the problem?** Be specific — not "they need better analytics" but "procurement managers at mid-size manufacturers spend 12 hours/week manually reconciling supplier invoices because their ERP and procurement systems don't share a common data format"
- **How acute is the problem?** Frequency (daily? quarterly?), severity (minor annoyance? existential risk?), trend (getting better or worse?)
- **Evidence quality:** What evidence supports the problem's existence? Rate confidence (High/Medium/Low)

### 3. Market Assessment

- **TAM (Total Addressable Market):** Total global market size if you captured 100% (top-down estimate from industry reports or bottom-up from customer counts × price)
- **SAM (Serviceable Addressable Market):** The portion of TAM you can realistically reach with your current or planned capabilities
- **SOM (Serviceable Obtainable Market):** What you can actually capture in a defined timeframe (3-5 years) given competition, GTM capacity, and brand
- **Growth rate:** Is this market growing, stable, or shrinking? At what rate?
- **Market structure:** Concentrated (few large buyers) or fragmented (many small buyers)? Winner-take-most or fragmented market share?

### 4. Customer and Buyer Dynamics

- **Target customer profile:** Specific, not generic. Include: company size, industry, role of the buyer, role of the user, budget authority, buying process
- **Willingness to pay:** Evidence that customers will pay for this solution. Pilot results, willingness-to-pay surveys, comparable solutions in adjacent markets
- **Switching behavior:** What do customers use today? What would make them switch? How high are switching costs?
- **Buying process:** Who decides? What is the procurement process? How long does it take?

### 5. Competitive Landscape

- **Current alternatives:** What do customers do today to solve this problem? (Manual processes, spreadsheets, competing products, workarounds with existing tools)
- **Direct competitors:** Who sells a product that directly addresses this need?
- **Indirect competitors:** Who solves the same underlying problem with a different approach?
- **Future competitors:** Who could enter this market easily? (Adjacent companies, platform companies adding features)
- **Competitive advantage:** Why would we win? What is our "unfair advantage" — technology, data, distribution, brand, team expertise, existing customer relationships?

### 6. Strategic Fit

- **Alignment with product strategy:** Does this reinforce or dilute the strategy?
- **Alignment with company goals:** Does it advance revenue, retention, expansion, competitive positioning?
- **Platform leverage:** Does this create capabilities that benefit other products or customers?
- **Distraction cost:** What would we NOT do if we pursue this? What existing commitments would be deferred or degraded?

### 7. Feasibility Assessment

- **Technical feasibility:** Can we build this? With what technology? In what timeframe?
- **Data requirements:** What data do we need? Do we have it? If not, how do we get it?
- **People requirements:** What skills do we need? Do we have them? If not, can we hire for them?
- **Partner dependencies:** Are there third-party dependencies (APIs, data providers, regulatory approvals)?
- **Key unknowns:** What don't we know that could kill this opportunity? How will we find out?

### 8. Economic Model

- **Revenue model:** How will we make money? (Subscription, transaction fee, marketplace, advertising, data licensing)
- **Unit economics at scale:** Target gross margin, CAC, LTV, payback period
- **Investment required:** What does it cost to validate (discovery), build (MVP), and scale (GA)?
- **Time to revenue:** How long from investment to first dollar? How long to breakeven?
- **Sensitivity:** What variables most affect the economics? (Price, CAC, churn, market size)

### 9. Risk Assessment

- **Market risk:** Is the problem real? Will customers pay?
- **Execution risk:** Can we build it? Can we sell it?
- **Competitive risk:** Can competitors block us or catch up?
- **Technology risk:** Does the technology exist and is it mature enough?
- **Regulatory risk:** Are there legal or compliance barriers?
- **Organizational risk:** Does the organization have the appetite and capacity for this?

### 10. Recommendation

- **Go / No-Go / Conditional Go:** Clear recommendation with conditions
- **Next step:** What happens if we proceed? (Specific action, owner, timeline)
- **Decision authority:** Who makes the final decision? What do they need to decide?

---

## Filled Example: AI-Powered Compliance Assistant

### 1. Opportunity Summary
Mid-market companies spend $200K-$500K/year on compliance consulting because existing compliance software doesn't automate the evidence collection and auditor preparation workflow. An AI-powered compliance assistant that ingests evidence from source systems (AWS, GitHub, Jira) and auto-generates auditor-ready documentation could reduce consulting costs by 60-80% while maintaining compliance quality. TAM: $2.1B (75,000 mid-market US companies × $28K average software spend). This aligns with our strategy of automating compliance workflows for mid-market companies.

### 2. Problem Validation
- **Problem:** Compliance officers spend 60-70% of their time manually collecting and formatting evidence for auditors. A SOC 2 Type II audit requires ~200 pieces of evidence across 15 control areas. Each piece must be collected from a source system, formatted, annotated, and organized. This is repetitive, error-prone, and expensive.
- **Acuity:** High. 34/40 customer interviews rated this as a top-3 pain. Average time spent: 15 hours/week. Average consulting spend: $280K/year. Trend: Getting worse as compliance requirements increase (new frameworks, more frequent audits, enterprise customer demands).
- **Evidence quality:** High. Validated through 40 interviews, 4 pilot customers, and secondary research on compliance spending trends.

### 3. Market Assessment
- **TAM:** $2.1B (75,000 mid-market US companies × $28K average software spend)
- **SAM:** $840M (companies with 100-1,000 employees that undergo at least one compliance audit per year)
- **SOM:** $21M in Year 3 (1,000 customers × $21K average ACV)
- **Growth rate:** Market growing 20-25% annually driven by: increasing compliance requirements, AI making automation feasible, enterprise procurement requiring vendor compliance
- **Market structure:** Fragmented. No dominant player. Vanta and Drata lead in startup SOC 2. No clear leader in mid-market multi-framework compliance.

### 4. Customer and Buyer Dynamics
- **Target customer:** Companies 100-1,000 employees, typically B2B SaaS, fintech, or health-tech. Buyer: CISO or VP of Engineering. User: Compliance officer or whoever "owns compliance" (often a shared responsibility). Budget: $15K-$50K/year for compliance software.
- **Willingness to pay:** Early evidence is positive. 4 pilot customers paying $1,500/month on average. Customers report the alternative (consulting) costs $200K-$500K/year, making software a clear savings even at $30K-$40K/year.
- **Switching behavior:** Current solution is usually manual (spreadsheets, shared drives) or consultants. Switching cost is low for manual processes, high for established consultant relationships.
- **Buying process:** CISO evaluates tools, makes recommendation to CFO/CEO. Purchase decision typically 4-8 weeks. Often triggered by an upcoming audit deadline.

### 5. Competitive Landscape
- **Current alternatives:** Manual processes (spreadsheets, documents), consultants, or lightweight tools (Jira, Notion, Google Docs)
- **Direct competitors:** Vanta, Drata, Secureframe (focused on startup SOC 2), Thoropass, Laika
- **Indirect competitors:** GRC platforms (ServiceNow, Archer — enterprise-focused, too expensive and complex for mid-market), MSSPs offering compliance as a service
- **Future competitors:** Existing GRC players could move downmarket. Cloud providers (AWS, Azure) could bundle compliance tools.
- **Competitive advantage:** Deep domain expertise (founders with 15+ years compliance experience). AI-first approach (competitors are rules-based or use AI as a feature, not the foundation). Mid-market focus (competitors are optimized for startups or enterprises).

### 6. Strategic Fit
- **Alignment:** Directly advances our strategy of automating compliance for mid-market. This is the core product vision.
- **Company goals:** Supports revenue growth ($21M SOM in Year 3), retention (compliance is recurring need), competitive positioning (AI-first differentiation).
- **Platform leverage:** AI evidence collection engine becomes a platform capability usable across compliance frameworks (SOC 2, GDPR, HIPAA, ISO 27001).
- **Distraction cost:** High. Building this requires focused investment from the entire engineering team for 6-9 months. No other major product initiatives during this period.

### 7. Feasibility Assessment
- **Technical feasibility:** Medium. AI-driven evidence collection from source systems (AWS, GitHub, Jira) is technically feasible using LLMs for natural language understanding of evidence documents. But accuracy requirements are high — auditors reject insufficient evidence. Prototype needed.
- **Data requirements:** Need access to customer source systems (APIs for AWS CloudTrail, GitHub audit logs, Jira issue history). Need training data for evidence classification (what constitutes valid evidence for each control).
- **People requirements:** Need 2 ML engineers (we have 0). Need compliance domain expertise (we have it in Priya).
- **Partner dependencies:** May need auditor partnerships for validation of AI-generated evidence.
- **Key unknowns:** Can AI achieve 95%+ accuracy in evidence classification? Will auditors accept AI-generated evidence? Will customers trust automated evidence collection enough to reduce consulting spend?

### 8. Economic Model
- **Revenue model:** SaaS subscription, tiered by company size and number of frameworks. Target ACV: $21K (mid-point of $15K-$50K range).
- **Unit economics:** Target gross margin 80% (cloud infrastructure is primary COGS). Target CAC < $15K. Target LTV > $100K (5-year customer life). Payback < 12 months.
- **Investment required:** $1.2M for MVP (6 months, 6 engineers). $3M for GA (12 months, 12 engineers + GTM team).
- **Time to revenue:** 12 months to first GA revenue. 24 months to $1M ARR if GTM motion works.
- **Sensitivity:** Most sensitive to: AI accuracy (if <90%, product doesn't work), CAC (if >$20K, unit economics break), churn (if >15%, LTV collapses).

### 9. Risk Assessment
- **Market risk:** Low. Problem is validated. Willingness to pay evidence is positive but limited.
- **Execution risk:** Medium. Technical feasibility is uncertain. ML hiring is competitive.
- **Competitive risk:** Medium. Well-funded competitors. But they're not focused on mid-market multi-framework.
- **Technology risk:** Medium. AI accuracy requirements are high. Edge cases could be problematic.
- **Regulatory risk:** Low. We're not doing compliance — we're providing software for compliance teams.
- **Organizational risk:** Medium. Focus is required. The company must commit to this as the primary initiative.

### 10. Recommendation
- **Conditional Go.** Proceed with a 3-month technical prototype focused on evidence classification accuracy. Go/No-Go decision at month 3 based on: (a) AI accuracy >90% on evidence classification task, (b) at least 2 of 4 pilot customers express willingness to pay for the AI-powered version at target price, (c) ability to hire at least 1 ML engineer.
- **Next step:** Assemble prototype team (Mikhail + 1 contract ML engineer). Define accuracy benchmarks and test dataset. Begin customer conversations about willingness to pay for AI-powered compliance.
- **Decision authority:** CEO (founder) with input from CTO and lead investor.

---

## Common Mistakes

1. **TAM inflation.** "The market for productivity software is $50B." Cool. Your specific segment is much smaller. Use bottom-up estimates whenever possible.
2. **Competitive denial.** "We have no competitors" almost always means "we haven't looked hard enough." Manual processes and spreadsheets are competitors. "Do nothing" is a competitor.
3. **Confusing stated need with willingness to pay.** Customers will tell you a problem is important. Whether they'll pay to solve it is a different question. Distinguish between problem validation and willingness-to-pay validation.
4. **Ignoring the distraction cost.** Every "yes" to a new opportunity is a "no" to something else. Be explicit about what you're sacrificing.
5. **Overweighting upside, underweighting risk.** Optimism bias is real. Pressure-test your upside assumptions and spend extra time on the risk section.
6. **Assessment as justification.** If you've already decided and you're using the assessment to justify the decision, be honest about it. At minimum, identify what evidence would change your mind.

## Dependencies

- [Product Thesis Template](PRODUCT_THESIS_TEMPLATE.md): The opportunity should align with or evolve the thesis
- [Risk-Adjusted Value Assessment](RISK_ADJUSTED_VALUE_ASSESSMENT.md): For comparing this opportunity against alternatives
- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): For opportunities that become strategic bets
- [Experiment Design Template](EXPERIMENT_DESIGN_TEMPLATE.md): For designing validation experiments for key unknowns
