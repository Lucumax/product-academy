# Build vs. Buy Template

## Purpose

A build vs. buy analysis evaluates whether to build a capability in-house, buy it from a vendor, integrate with a partner, or use an open-source solution. It answers: "Should we invest our engineering capacity in building this, or should we acquire it from outside?" The analysis is about comparative advantage — where should your scarce engineering resources be deployed for maximum strategic impact?

This template is for decisions about significant capabilities. It is NOT for trivial decisions (a UI library, a logging service) where the answer is almost always "buy" and the cost of analysis exceeds the cost of a wrong decision.

## When to Use

- Evaluating whether to build or buy a significant product capability
- Deciding whether to integrate with a third-party API vs. build in-house
- Assessing a potential acquisition target (technology acquisition)
- Deciding whether to replace a homegrown system with a vendor solution
- Evaluating an open-source alternative to a build or buy decision

## Template Structure

### 1. The Capability

- **What capability are we evaluating?** Be specific — not "analytics" but "a real-time dashboard showing customer behavior across web and mobile with cohort analysis, funnel visualization, and CSV export."
- **Why do we need it?** What product, customer, or business need does it serve?
- **What happens if we do nothing?** What is the cost of not having this capability?

### 2. Build Assessment

**Advantages of building:**
- Customization: Can we build exactly what we need? How much does customization matter?
- Integration: How tightly does this need to integrate with our existing systems? Build excels at deep integration.
- Control: Do we need full control over the roadmap, data, and architecture?
- Strategic differentiation: Is this capability a source of competitive advantage? If yes, building is usually the right answer. If no, buying is usually the right answer.

**Disadvantages of building:**
- Cost: What is the estimated engineering investment? Include: initial build, ongoing maintenance, future feature development, infrastructure.
- Time: How long to build the MVP? To reach parity with vendor options?
- Opportunity cost: What else could the engineering team build instead?
- Talent: Do we have the skills to build this? If not, can we hire for them?

**Build cost estimate:**
- Initial build: X person-months × $Y/person-month = $Z
- Annual maintenance: X person-months/year × $Y/person-month = $Z/year
- Infrastructure: $Z/year
- Total 3-year cost: $Z

### 3. Buy Assessment

**Advantages of buying:**
- Speed: How quickly can we integrate and go live?
- Maturity: Does the vendor solution have capabilities we wouldn't build for years?
- Maintenance: The vendor handles updates, security, scaling, bug fixes.
- Ecosystem: Does the vendor have integrations, APIs, or a marketplace we can leverage?

**Disadvantages of buying:**
- Cost: What is the vendor pricing? Include: base price, per-user/per-usage fees, implementation cost, ongoing support cost.
- Customization constraints: Can the vendor solution be customized to our specific needs? If not, how much do we compromise?
- Vendor risk: What if the vendor raises prices, gets acquired, goes out of business, or changes their roadmap?
- Integration friction: How well does the vendor solution integrate with our existing systems?
- Data control: Where does our data live? Who has access? What happens to our data if we leave the vendor?
- Strategic risk: Are we building on a platform we don't control? Could the vendor become a competitor?

**Buy cost estimate:**
- Annual license: $Z/year
- Implementation: $Z (one-time)
- Integration: X person-months × $Y/person-month = $Z (one-time)
- Ongoing support/management: X person-months/year × $Y/person-month = $Z/year
- Total 3-year cost: $Z

### 4. Partner/Open-Source/Alternative Assessment

Beyond build and buy, consider:
- **Partner/integrate:** Integrate with an existing product via API (not acquiring it, but connecting to it). Lower cost than buying, less control.
- **Open source:** Use or adapt an open-source solution. Free to acquire, but costs engineering time to implement, customize, and maintain.
- **Hybrid:** Build the parts that are strategically differentiating; buy/partner for the rest.

### 5. Comparative Analysis

A structured comparison across key dimensions:

| Dimension | Build | Buy | Partner/OS | Weight |
|-----------|-------|-----|------------|--------|
| Time to market | | | | |
| 3-year total cost | | | | |
| Strategic differentiation | | | | |
| Customization/fit | | | | |
| Integration depth | | | | |
| Control and flexibility | | | | |
| Risk (vendor, talent, execution) | | | | |
| Maintenance burden | | | | |
| Data control and security | | | | |

Score each option on each dimension (1-5) and apply weights based on strategic priority. The total score is informative but not determinative — judgment still matters.

### 6. Recommendation

- **Recommendation:** Build / Buy / Partner / Hybrid — with specific rationale
- **Key trade-off:** What are we gaining and what are we sacrificing?
- **Risk mitigation:** What are the biggest risks of this recommendation and how will we mitigate them?
- **Reversal conditions:** Under what conditions would we change this decision?

### 7. Implementation Plan

- **Key steps:** What happens to execute the decision?
- **Timeline:** When does the capability become available to customers?
- **Success criteria:** How will we know this was the right decision?
- **Review point:** When will we revisit this decision? (Vendor contracts, build milestones, market changes)

---

## Filled Example: Analytics Dashboard for Compliance Platform

### 1. The Capability
- **What:** A customer-facing analytics dashboard showing compliance program health — control coverage %, evidence collection status, audit readiness score, team activity metrics, and trend analysis over time. Customers need to report compliance status to their boards and auditors.
- **Why:** Top-3 request from pilot customers. 34/40 customer interviews cited "reporting to management" as a critical need that our product doesn't address. Competitors (Vanta, Drata) have analytics dashboards.
- **Do nothing cost:** Lose deals to competitors who have dashboards. Customer satisfaction declines as they adopt workarounds (exporting data to Excel, building their own dashboards). Estimated: 15-20% reduction in competitive win rate.

### 2. Build Assessment

**Advantages:**
- Customization: We can build dashboards that exactly match our compliance data model (control frameworks, evidence status, audit readiness). Generic analytics won't understand "SOC 2 control coverage" or "GDPR Article 30 compliance."
- Integration: Deep integration with our compliance data model. The dashboard will reflect real-time compliance status from our core product.
- Strategic differentiation: Compliance analytics IS potentially a strategic differentiator — if we build it, customers can answer "are we compliant right now?" which is the core value proposition.

**Disadvantages:**
- Cost: Estimated 6-8 person-months for MVP. Our team is 4 engineers with a full roadmap.
- Time: 4-5 months to MVP. Competitors already have dashboards.
- Talent: We have strong backend engineers but limited frontend data visualization experience. May need to hire or contract.

**Build cost estimate:**
- Initial build: 7 person-months × $15K/person-month = $105K
- Annual maintenance: 1 person-month/year × $15K = $15K/year
- Infrastructure: $6K/year (hosted charting library + additional database capacity)
- Total 3-year cost: $105K + ($15K + $6K) × 3 = $168K

### 3. Buy Assessment

**Vendor evaluation:** Evaluated 3 embedded analytics vendors: Looker Embedded, Cube.js, Metabase Embedded.

**Advantages:**
- Speed: Could integrate in 4-6 weeks vs. 4-5 months to build. Solves the competitive gap faster.
- Maturity: Vendor dashboards have drill-down, filtering, export, scheduling, and theming capabilities that would take years to build internally.
- Maintenance: Vendor handles dashboard performance, new visualization types, export formats.
- Talent: Don't need to hire frontend data visualization specialists.

**Disadvantages:**
- Customization: Cannot match our compliance-specific data model perfectly. "Control coverage %" is a custom metric that generic analytics doesn't understand. Would need to pre-compute compliance metrics and feed them to the vendor as generic "metrics."
- Cost: Pricing for embedded analytics at our scale (projected 200 customers in Year 1, 1,000 in Year 3):
  - Looker Embedded: $25K/year base + $5/user/month → ~$75K/year at 200 users, ~$300K/year at 1,000 users
  - Cube.js (self-hosted open core): Free core, $20K/year for enterprise features
- Vendor risk: Looker is Google-owned. Google has a history of changing pricing and deprecating products.
- Data control: Customer compliance data would flow through a third-party analytics service (or at minimum, query results would). This is sensitive data (SOC 2 evidence, audit documentation).

**Buy cost estimate (Looker Embedded):**
- Annual license: $75K (Year 1), $150K (Year 2), $300K (Year 3) — scaling with customer growth
- Implementation: 6 person-weeks × $15K/person-month = $22.5K (one-time)
- Integration maintenance: 0.5 person-month/year × $15K = $7.5K/year
- Total 3-year cost: $22.5K + $75K + $150K + $300K + ($7.5K × 3) = $570K

### 4. Partner/Open-Source Assessment

**Cube.js (open core):**
- Open-source core provides dashboard building blocks (query engine, caching, charting). We build the UI layer on top.
- Cost: Free core + $20K/year enterprise (multi-tenant, SSO, white-label). Customization required: ~3 person-months initial build + 0.5 person-months/month ongoing.
- 3-year cost: (3 person-months × $15K) + ($20K × 3) + (0.5 × 12 × 3 × $15K/12) = $45K + $60K + $90K = $195K
- Control: High. We own the data pipeline. Cube handles query performance and caching. We customize the UI for compliance-specific metrics.
- Risk: Medium. Cube.js is open-source with a commercial entity behind it. Lower vendor risk than proprietary solutions.

### 5. Comparative Analysis

| Dimension | Build | Buy (Looker) | Partner (Cube.js) | Weight |
|-----------|-------|-------------|-------------------|--------|
| Time to market | 2 (4-5 months) | 4 (4-6 weeks) | 3 (8-10 weeks) | 25% |
| 3-year total cost | 4 ($168K) | 2 ($570K) | 3 ($195K) | 20% |
| Strategic differentiation | 5 (fully custom) | 2 (generic) | 4 (custom UI, commodity backend) | 25% |
| Customization/fit | 5 | 2 | 4 | 15% |
| Risk | 3 (execution risk) | 2 (vendor lock-in, pricing) | 3 (open-source sustainability) | 10% |
| Data control | 5 | 1 | 4 | 5% |

Weighted scores: Build: 3.65, Buy: 2.45, Cube.js: 3.50

### 6. Recommendation
- **Recommendation:** Hybrid — Build using Cube.js as the analytics backend. We build the compliance-specific UI layer on top of Cube.js, which handles query performance, caching, and chart rendering. This gives us customization + speed + reasonable cost.
- **Key trade-off:** We compromise on time-to-market (8-10 weeks vs. 4-6 weeks for Looker) but gain customization and cost control. We compromise on "fully custom" (vs. pure build) but gain faster delivery and lower maintenance.
- **Risk mitigation:** Cube.js has an active open-source community and a commercial entity (Cube Dev, Inc.). If Cube.js becomes unsustainable, our UI layer is built on a standard API that could be ported to another backend. The investment is mostly in the UI (which we'd keep) not the backend integration.
- **Reversal conditions:** If Cube.js fails to meet performance requirements (>2 second query response at 1,000 customers), we switch to a proprietary backend but keep our custom UI. If compliance analytics proves to be a commodity feature (not a differentiator), we reconsider Looker for speed.

### 7. Implementation Plan
- **Week 1-2:** Cube.js proof of concept — test query performance with our compliance data model on a representative dataset (1,000 customers' worth of data).
- **Week 3-8:** Build compliance-specific UI (control coverage dashboard, evidence status tracker, audit readiness score). Integrate with Cube.js API.
- **Week 9-10:** Beta with 5 pilot customers. Iterate on design and metrics.
- **Week 11-12:** GA launch to all customers.
- **Success criteria:** (1) 50% of customers access dashboard at least weekly within 90 days of launch. (2) Customer-reported "reporting to management" pain score decreases by >30%. (3) Competitive win rate improves by >5%.
- **Review point:** 6 months post-launch. Evaluate: dashboard usage, customer satisfaction, competitive impact, Cube.js performance/cost at scale.

---

## Common Mistakes

1. **Defaulting to build.** Engineers (and product leaders with engineering backgrounds) tend to overvalue building and undervalue buying. The default question should be "why shouldn't we buy this?" not "why shouldn't we build this?"
2. **Underestimating maintenance cost.** Building is not a one-time cost. The true cost includes ongoing maintenance, feature requests, bug fixes, security updates, and infrastructure. A 3-year TCO analysis that ignores maintenance is dangerously incomplete.
3. **Ignoring the opportunity cost.** The cost of building is not just the engineering hours — it's what those engineers would have built instead. Every build decision is a decision NOT to build something else.
4. **Vendor cost optimism.** Vendors often quote attractively for Year 1 with escalators in Years 2-3. Model the full contract lifecycle, including renewal pricing, per-user growth, and feature tier upgrades.
5. **Build for differentiation, buy for commodity.** The core strategic question is: "Is this capability a source of competitive advantage?" If yes, build. If no, buy. Most build vs. buy errors come from misclassifying a commodity as a differentiator (building an in-house CRM) or a differentiator as a commodity (buying a generic solution for a core product capability).

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Strategy should define what's strategically differentiating vs. commodity.
- [Resource Allocation Memo](RESOURCE_ALLOCATION_MEMO.md): The build option consumes engineering capacity — what else is being sacrificed?
- [Risk-Adjusted Value Assessment](RISK_ADJUSTED_VALUE_ASSESSMENT.md): For comparing build vs. buy investment value.
- [Platform vs. Feature Template](PLATFORM_VS_FEATURE_TEMPLATE.md): Related decision — is this a platform capability or a feature?
