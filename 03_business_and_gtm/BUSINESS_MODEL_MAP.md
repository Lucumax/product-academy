# Business Model Map

## Overview

This document maps the business and go-to-market domains that product leaders at the Principal+ level must understand. Each section provides the core concepts, how they interact with product decisions, common failure modes, and practice exercises.

## 1. Pricing and Packaging

### Why Pricing Is a Product Decision

Pricing is not a finance exercise — it is a product lever. The price communicates value. The packaging determines who can access what. The pricing model shapes user behavior. A product with the right pricing for its value will grow faster than a product with better features and worse pricing.

### Pricing Models

**Value-Based Pricing:** Price is set based on the value delivered to the customer, not the cost of delivering it. A product that saves a customer $100,000/year can be priced at $10,000-$30,000/year regardless of whether it costs $1,000 or $5,000 to deliver.

- Best for: products with clear, quantifiable value delivery
- Worst for: products where value is hard to quantify or varies dramatically across customers
- Product implication: you must understand the customer's economic model to price effectively

**Cost-Plus Pricing:** Price is set as cost of delivery plus a margin.

- Best for: commodity products with thin margins and known costs
- Worst for: software products (where marginal cost approaches zero and value is disconnected from cost)
- Product implication: this model systematically underprices software — avoid it

**Competitive Pricing:** Price is set relative to competitors.

- Best for: products in established markets with well-understood pricing
- Worst for: differentiated products (you are pricing your differentiation at zero) or new categories (no competitor to reference)
- Product implication: you compete on the competitor's terms, not your own value

**Usage-Based Pricing:** Price is based on consumption (API calls, seats, data volume, compute time).

- Best for: products where usage correlates with value (API products, infrastructure, AI models)
- Worst for: products where value is not usage-correlated (a CRM where adding more users does not mean more value per user)
- Product implication: usage-based pricing aligns product value with revenue — when customers get more value, you get more revenue. But it makes revenue less predictable and requires metering infrastructure.

**Tiered/Good-Better-Best:** Price varies by plan level with feature differentiation.

- Best for: products with natural segmentation (individual vs team vs enterprise, SMB vs mid-market vs large enterprise)
- Worst for: products where one size genuinely fits all
- Product implication: the tier structure IS the product strategy — what features go in which tier defines who your product serves and how you capture value from different segments

### Packaging Design Principles

1. **The decoy effect.** A three-tier structure works better than two because the middle tier becomes the default choice when the top tier is expensive and the bottom tier is limited.
2. **Feature differentiation must be visible.** If the difference between tiers is not clear in the buying experience, customers default to the cheapest tier.
3. **Anchoring.** The highest-priced tier sets the anchor. Even if few customers buy it, it makes the middle tier look like good value.
4. **The upgrade path must be obvious.** Customers must know what they get by upgrading and when they should upgrade (usage thresholds, feature unlocks).
5. **Packaging changes are product changes.** Changing what features are in which tier changes who uses what. Treat packaging changes with the same care as feature changes.

### Common Pricing Failure Modes

1. **Underpricing to drive growth.** "We will win the market with low prices and raise them later." Raising prices is harder than setting them right initially. Customers anchor on the initial price. Competitors respond. The market expects the lower price.
2. **Overpricing based on potential value.** Pricing based on what the product COULD be worth rather than what it IS worth when the customer buys it. The customer evaluates current value, not the roadmap.
3. **Pricing by committee.** Every stakeholder has an opinion on pricing. The result is usually compromise pricing that serves no strategy. The product leader should own pricing, with input from sales and finance.
4. **One-size-fits-all pricing.** Charging the same price to a 10-person startup and a 10,000-person enterprise. The value delivered and the willingness to pay are different. The pricing should reflect that.
5. **Never changing pricing.** Pricing set 3 years ago when the product, market, and competitive landscape were different. Pricing should be reviewed at least annually.

### Practice: Pricing Teardown

Take a product you manage. For each of these questions, write the answer:
1. What is the primary value metric? (What correlates with the value the customer gets? Seats? Usage? Outcomes?)
2. What is the customer's alternative? (What do they do today? What does it cost them?)
3. What is the value gap? (How much better is your product than the alternative? Can you quantify it?)
4. What fraction of the value gap do you capture in pricing? (Typically 10-30% for SaaS)
5. When was the last time pricing was reviewed with primary research (not internal opinion)?
6. What is the biggest pricing mistake you are making right now? (Underpricing? Wrong value metric? Poor packaging?)

---

## 2. Unit Economics

### Core Concepts

**Customer Acquisition Cost (CAC):** Total sales and marketing cost to acquire a customer, divided by the number of customers acquired in a period.

- Fully loaded CAC includes sales salaries, marketing spend, tooling, and allocated overhead. "Marketing spend / new customers" is not fully loaded CAC.
- CAC payback period: how many months of gross margin does it take to recover the CAC? A healthy SaaS company typically targets <12 months.

**Lifetime Value (LTV):** The total gross margin a customer generates over their lifetime.

- LTV = Average Revenue Per Account (ARPA) × Gross Margin % / Churn Rate
- The most common error: using net revenue retention (expansion offsets churn) to calculate LTV when you should be using gross churn (the probability a customer leaves entirely). Expansion from remaining customers does not offset a lost customer's entire contribution.

**LTV:CAC Ratio:** The relationship between what a customer is worth and what it costs to acquire them.

- A ratio of 3:1 or higher is generally healthy for SaaS.
- A ratio below 3:1 means you are spending too much to acquire customers relative to their value — either CAC is too high or LTV is too low.
- A ratio above 5:1 may mean you are underinvesting in growth.

**Contribution Margin:** Revenue minus variable costs (typically hosting, support, payment processing, but not R&D or G&A).

- Contribution margin tells you whether each additional customer adds or subtracts value.
- A negative contribution margin means you lose money on every customer. This is acceptable temporarily for growth (market capture) but must converge to positive.

**Net Revenue Retention (NRR):** Revenue from existing customers at the end of a period divided by revenue from the same customers at the start of the period.

- NRR >100% means existing customers are expanding (upgrades, more seats, more usage) faster than they are churning or contracting.
- NRR >120% is considered best-in-class for SaaS.
- NRR is a lagging indicator — it tells you what happened, not why. Investigate churn reasons and expansion drivers separately.

### How Unit Economics Should (and Should Not) Influence Product Decisions

**Should influence:**
- Pricing decisions (unit economics tell you the minimum viable price)
- Feature prioritization (features that improve retention or expansion have calculable LTV impact)
- Target customer segments (segments with poor unit economics are not viable regardless of product fit)
- Build-vs-buy decisions (the cost of building must be evaluated against the unit economics of the alternative)

**Should NOT influence:**
- Strategic bets (entering a new market may have terrible unit economics initially — that is the nature of a bet)
- Product quality investments (improving activation, onboarding, performance may not have directly attributable unit economic impact but is essential)
- Long-term platform investments (the unit economics of building a platform may never justify the investment on a direct-attribution basis — the value comes from enablement)

### Common Unit Economics Failure Modes

1. **CAC underestimation.** Underestimating the fully loaded cost of acquisition. Sales team cost + marketing spend + sales tooling + allocated office space + sales management overhead = actual CAC. The "marketing spend / new customers" number is usually half of actual CAC.
2. **LTV overestimation.** Using optimistic churn assumptions, ignoring cohort-level churn patterns, or using NRR to back-calculate LTV (which assumes expansion from remaining customers will offset lost customers' contribution forever).
3. **Segment blindness.** Reporting blended unit economics that mask significant differences between customer segments. A product may have great unit economics in one segment and terrible unit economics in another. Blended metrics hide this.
4. **Ignoring time value of money.** LTV calculations that do not discount future cash flows overstate the present value of long-lifetime customers.
5. **Unit economics as a ceiling, not a floor.** Using unit economics to kill initiatives that are strategically important but have poor short-term unit economics. The unit economics of entering a new market will always look bad initially.

### Practice: Unit Economics Audit

For a product you manage, calculate: (1) Fully loaded CAC, (2) LTV (using gross churn, not net revenue retention), (3) LTV:CAC ratio, (4) CAC payback period, (5) Contribution margin, (6) Net Revenue Retention.

Identify the weakest metric. What product decision would most improve it?

---

## 3. Go-To-Market Models

### Product-Led Growth (PLG)

The product is the primary driver of acquisition, activation, and expansion. Users discover the product, try it (usually free or freemium), experience value, and convert to paid — with minimal or no sales involvement.

**When PLG works:**
- The product has a strong individual-user value proposition (Slack, Figma, Notion, Dropbox)
- The product can demonstrate value quickly (time-to-value is measured in minutes, not weeks)
- The product has viral or network characteristics (collaboration tools, communication tools)
- The target market is large enough that self-serve acquisition economics work

**When PLG fails:**
- The product requires organizational change to deliver value (ERP, HRIS, CRM at enterprise scale)
- The value only emerges at team or company level (individual users cannot evaluate it)
- The buying process requires procurement, security review, or executive approval
- The product's value proposition is complex and requires explanation

**The PLG product leader's responsibilities:**
- Optimize time-to-value — users must experience the product's value within minutes of signing up
- Build the product to sell itself — the product experience must drive conversion to paid
- Design for virality — the product should generate its own growth through collaboration, sharing, or network effects
- Measure product-qualified accounts (PQAs) — which accounts are getting value and are ready for sales outreach?

### Sales-Led Growth (SLG)

Sales is the primary driver of acquisition. The product is sold through outbound prospecting, inbound lead qualification, and relationship-based selling.

**When SLG works:**
- The product has high ACV ($50K+) that justifies sales investment
- The buying process involves multiple stakeholders and requires executive alignment
- The product requires customization, integration, or professional services
- The market is concentrated (few large customers) rather than diffuse (many small customers)

**When SLG fails:**
- The product's ACV is too low to support a sales team
- The market is large and diffuse — sales cannot reach enough customers efficiently
- Self-serve competitors with better product experience are winning the market
- The product can be evaluated and adopted without a sales process

**The SLG product leader's responsibilities:**
- Partner with sales to understand what customers need and what the sales team needs to sell effectively
- Maintain product coherence while responding to enterprise customer requirements
- Define what is "product" vs "professional services" vs "custom development"
- Ensure that the product roadmap is not captured by the largest deals

### Hybrid (Product-Led Sales)

Product-led acquisition with sales-led expansion. Users discover and adopt the product on their own. When usage reaches a threshold (the "sales trigger"), a sales team engages to drive expansion.

This is the dominant model for enterprise SaaS companies that started PLG and are moving upmarket (Figma, Notion, Slack pre-acquisition).

**Key design decisions:**
- What is the sales trigger? (Number of seats? Usage volume? Specific feature adoption? Account characteristics?)
- What happens when sales engages? (Does the product experience change? Does pricing change?)
- How does the product support the sales motion? (Usage data for sales? Product-qualified account scoring?)

### Channel and Partner GTM

The product is sold through partners — resellers, system integrators, agencies, or platforms.

**When channel GTM works:**
- The product is part of a larger solution that partners assemble (Salesforce AppExchange, AWS Marketplace)
- The market is geographically distributed and direct sales cannot reach every region
- Partners have relationships and trust that your company cannot build directly
- The product requires implementation or integration that partners provide

**When channel GTM fails:**
- The product is simple enough that partners add cost without adding value
- Partners' incentives are not aligned with the product's growth strategy
- The product team loses contact with end customers (partners own the relationship)

---

## 4. Product-Finance Interface

### How Product Leaders Should Work with Finance

The product-finance relationship is often adversarial — product wants to invest; finance wants to constrain. This is counterproductive. The best product leaders treat finance as a partner in resource allocation, not an obstacle.

**What to bring to finance:**
- A clear product strategy that explains WHY investments are needed
- Unit economics that show how product investments translate to business outcomes
- Honest uncertainty ranges — "we have 60% confidence this will produce $X in incremental revenue within Y months"
- Leading indicators that will show whether the investment is working before the lagging financial indicators move

**What not to bring to finance:**
- "Trust me, this is strategic" without any quantification of strategic value
- Optimistic projections designed to get funding rather than reflect realistic expectations
- Product metrics without business translation — "this will improve NPS by 10 points" without explaining what that means for revenue or retention

### Business Cases

A business case is a structured argument for an investment. The product leader should own the assumptions and the narrative; finance should validate the model and challenge the assumptions.

**Structure of a product business case:**
1. **The strategic rationale.** Why this investment now? What happens if we do not make it?
2. **The investment required.** Headcount, capital, time, opportunity cost (what are we NOT doing because of this?).
3. **The expected return.** Revenue, retention, competitive position, strategic optionality. Include uncertainty ranges.
4. **The assumptions.** What must be true for this to work? Which assumptions are highest-risk?
5. **The leading indicators.** How will we know in 3-6 months whether this is working?
6. **The kill criteria.** At what point would we stop this investment?

### Resource Allocation

At Director+ level, resource allocation IS strategy. The product leader who cannot connect resource allocation to product strategy is not doing strategy — they are managing a backlog.

**Principles:**
- Zero-based budgeting: do not assume that last year's allocation is the right starting point. Every year, re-justify every major investment.
- Funding the strategy, not the org chart: resources should follow strategy, not the other way around. If the strategy says "invest in platform," but the org chart concentrates resources in feature teams, the org chart is wrong.
- Dynamic reallocation: the annual plan is a snapshot. Reallocate quarterly based on what you have learned. The biggest competitive advantage is the willingness to move resources faster than your competitors.

---

## 5. Product-Sales Interface

### The Most Important Organizational Relationship in Enterprise SaaS

In enterprise SaaS companies, the product-sales interface is the difference between a product that wins in the market and a product that frustrates customers, salespeople, and product teams equally. Most product failures in enterprise companies are failures of this interface.

### The Product-Sales Alignment Spectrum

| Position | Characteristics | Risks |
|----------|----------------|-------|
| **Sales-driven** | Product builds what the largest deals require | Product loses coherence; roadmap becomes a collection of custom features; PMs become sales engineers |
| **Sales-aligned** | Product incorporates sales input into an independent strategy | The ideal position. Sales input informs strategy; strategy constrains what is built. |
| **Sales-oblivious** | Product ignores sales input entirely | Product may be elegant but unsellable; sales invents capabilities to win deals; trust erodes |

The goal is sales-aligned, not sales-driven. Sales alignment means: (a) product leadership understands what the sales team needs to be successful, (b) the product strategy accounts for enterprise customer requirements, (c) sales has input into the roadmap but not control over it, (d) there is a clear process for handling custom requests that fall outside the product strategy.

### The Custom Development Trap

Enterprise customers will ask for custom features, integrations, and modifications. The default response should be "no" — the product should serve the market, not individual customers. But sometimes "yes" is the right answer.

**When to say yes:**
- The request represents a genuine market need that multiple customers have (the requesting customer is the canary)
- The customer's contract value justifies the development cost, AND the capability can be productized for other customers
- The request is for integration or configuration (using existing platform capabilities), not custom code
- The customer is strategically important to the company's market position

**When to say no:**
- The request is genuinely unique to one customer and cannot be productized
- The development cost exceeds the contract value (even considering strategic value)
- The request would create a precedent that makes it harder to say no to future customers
- The request pulls the product in a direction that contradicts the product strategy

**How to say no:**
- Acknowledge the customer's need — it is real and important to them
- Explain why the request does not fit the product strategy — not "we don't want to" but "here is the strategy and here is why this request does not align"
- Offer alternatives — can the customer achieve their goal through existing features? Through a partner? Through a different approach?
- If appropriate, commit to reviewing the request when the strategy or product evolves

### Roadmap Communication to Sales

The sales team needs to know what is coming so they can sell effectively. The product team fears that sharing the roadmap creates commitments. These are both legitimate concerns. The resolution is structured roadmap communication.

**Principles:**
- Share themes and problems, not features and dates. "We are investing in enterprise admin capabilities in H2" — not "we will ship SSO on September 15."
- Distinguish between commitments, bets, and explorations. Sales should know what is committed (sold with confidence), what is a bet (directionally likely), and what is an exploration (may or may not ship).
- Never let sales promise a feature with a specific date unless the product team has committed to that date. The fastest way to destroy product-sales trust is for sales to promise something product cannot deliver.
- Give sales the information they need to protect deals that depend on upcoming features — "if a customer needs X, we can discuss how to handle their specific timeline."

### The Product-Sales Operating Cadence

- **Weekly:** product leadership available for deal-specific questions (escalation path for sales)
- **Monthly:** product updates to sales leadership on roadmap progress, changes, and new capabilities
- **Quarterly:** joint product-sales review — what is working, what is not, what do we need from each other?
- **Semi-annually:** sales input into product strategy — what are customers asking for? What are competitors doing? What does the sales team need to win?

---

## Practice: The Product-Business Integration Audit

For a product you manage, answer these questions:

**Pricing:**
1. When was pricing last changed?
2. What is the primary value metric? Does pricing align with it?
3. What is the biggest pricing mistake we are making?

**Unit Economics:**
4. What is our LTV:CAC ratio? Is it trending up or down?
5. What is our NRR? What is driving it — expansion or retention?
6. Which customer segment has the best unit economics? The worst?

**GTM:**
7. What is our GTM model? Is it working? How do we know?
8. What is the biggest GTM constraint on growth — acquisition, activation, or expansion?
9. Are our GTM model and our product model aligned?

**Product-Finance:**
10. Does our resource allocation reflect our product strategy?
11. When was the last time we killed an investment because the leading indicators showed it was not working?

**Product-Sales:**
12. Is our relationship with sales better described as aligned, driven, or oblivious?
13. What percentage of the roadmap is driven by specific customer requests?
14. When was the last time a sales commitment forced a product commitment we could not meet?

The answers to these questions ARE your product-business integration agenda.
