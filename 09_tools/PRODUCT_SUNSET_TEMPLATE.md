# Product Sunset Template

## Purpose

A product sunset (or end-of-life) plan defines how to retire a product, feature, or version while minimizing customer harm, revenue loss, and organizational disruption. It answers: "How do we responsibly end something we built?" — a question that is as important to product leadership as "what should we build next?" because every product eventually reaches the end of its lifecycle.

This template is specifically for products with existing customers. It is NOT for killing an internal project that never launched (that's a different decision) or for pivoting (that's a strategy change).

## When to Use

- You're retiring a product that has active customers
- You're ending support for a version or platform
- You're consolidating multiple products into one
- You're sunsetting a feature that has meaningful adoption
- Regulatory or technical constraints require retirement
- You're making space for a new product that replaces an old one

## Template Structure

### 1. Sunset Decision Summary

- **What is being sunset:** Specific product, feature, version, or platform
- **Why:** The strategic, technical, or financial rationale
- **When:** Target retirement date and key milestones
- **Who decided:** Decision authority
- **What replaces it:** Migration path for customers (if any)

### 2. Current State Analysis

- **Active customers:** How many? What segments? What ARR is at risk?
- **Usage patterns:** How heavily do customers use what's being sunset? Which features/capabilities are critical vs. incidental?
- **Contractual obligations:** What commitments exist? (SLAs, support contracts, regulatory requirements)
- **Technical dependencies:** What internal systems depend on this product? What third-party integrations?

### 3. Customer Impact Assessment

Segment customers by the impact of sunset:

| Segment | Count | ARR | Impact | Migration Viability | Risk of Churn |
|---------|-------|-----|--------|--------------------|---------------|
| Heavy users, no migration path | | | Critical | Low | High |
| Heavy users, clear migration path | | | High | High | Medium |
| Light users, no migration path | | | Medium | Low | Medium |
| Light users, clear migration path | | | Low | High | Low |
| Inactive/non-users | | | None | N/A | None |

For each segment, map: what they use, what they'll lose, what the replacement path is, and what support they'll need.

### 4. Migration Strategy

If there's a replacement product:
- **Feature parity assessment:** What features exist in the replacement? What's missing? For missing features, is there a workaround, a timeline, or a decision to deprecate without replacement?
- **Data migration:** How does customer data move? Is it automated or manual? What data is lost?
- **Pricing transition:** How does pricing change? (Grandfathering, transition discounts, new pricing)
- **Timeline and milestones:** When does migration start? When must it be complete? What are the intermediate milestones?

If there is NO replacement product:
- **Customer off-boarding plan:** Data export, transition assistance, alternate vendor recommendations
- **Contract termination:** Notice periods, early termination terms, pro-rated refunds

### 5. Communication Plan

| Stakeholder | Message | Channel | Timing | Owner |
|-------------|---------|---------|--------|-------|
| Customers (directly affected) | What's happening, why, timeline, migration path, support | Email + in-app notification + account manager outreach | 12 months before sunset | VP Customer Success |
| Customers (indirectly affected) | What's happening, why, timeline (condensed) | Email | 6 months before sunset | Product Marketing |
| Internal teams (sales, support, CS) | Detailed brief, FAQ, talking points, escalation path | All-hands + documentation | Before customer communication | PM |
| Partners/integrators | Technical migration guide, API changes, support timeline | Partner portal + direct outreach | 9 months before sunset | Partner Manager |
| Public/market | Blog post, press if significant | Blog + PR | 6 months before sunset | Product Marketing |
| Investors/board | Strategic rationale, financial impact, migration progress | Board presentation | Before public communication | CEO/CPO |

### 6. Risk Management

- **Churn risk:** What % of affected customers are expected to churn? What is the revenue at risk?
- **Brand/reputation risk:** How might customers react publicly? What's the communication strategy to mitigate?
- **Legal/contractual risk:** Any breach of contract, SLA, or regulatory obligation?
- **Operational risk:** What could go wrong during migration or shutdown?
- **Data risk:** What happens to customer data? Retention, deletion, portability?
- **Mitigation for each risk:** Specific actions, owners, contingencies.

### 7. Resource Plan

- **Engineering:** What work is needed? (Migration tools, data export, API deprecation, shutdown procedures)
- **Customer Success/Support:** Migration support, customer communication, escalation handling
- **Sales:** Account management for at-risk customers, renewal conversations
- **Legal/Compliance:** Contract review, regulatory notification, data handling compliance
- **Timeline:** When does each function invest, and for how long?

### 8. Sunset Milestones

| Milestone | Date | Criteria | Owner |
|-----------|------|----------|-------|
| Internal announcement | | | |
| Customer announcement | | | |
| Migration period begins | | | |
| New sales stopped | | | |
| Feature freeze | | | |
| Migration deadline | | | |
| Service degradation (read-only) | | | |
| Service shutdown | | | |
| Data deletion (if applicable) | | | |

### 9. Post-Sunset Review

After the sunset is complete (typically 1-3 months after shutdown):
- What went well in the sunset process?
- What went poorly?
- How many customers migrated vs. churned vs. stayed until shutdown?
- What was the actual vs. projected revenue impact?
- What would we do differently next time?

---

## Filled Example: MediCore Classic End-of-Life Plan

### 1. Sunset Decision Summary
- **What:** MediCore Classic (Windows client-server EHR, built 1998)
- **Why:** Classic runs on a discontinued technology stack (Delphi/InterBase). The 14-person engineering team has 2 retirements pending in 18 months, after which the product becomes unmaintainable. The strategic direction is to consolidate on MediCore Cloud.
- **When:** 3-year phased sunset. New sales stop: Dec 2026. Feature freeze: Jun 2027. Service shutdown: Dec 2028.
- **Who decided:** CEO (Dr. Chen) with CPO recommendation. Board reviewed Q2 2026.
- **What replaces it:** MediCore Cloud with Classic-compatible pricing tier and migration tooling.

### 2. Current State Analysis
- **Active customers:** 3,200 practices (average: solo or 2-physician). $40M ARR. Average tenure: 11 years.
- **Usage patterns:** 87% use core clinical workflow (documentation, e-prescribing, lab orders). 62% use billing module. 23% use advanced scheduling. <5% use 200+ niche features that don't exist in Cloud.
- **Contractual obligations:** Annual maintenance contracts. 30-day termination notice. No long-term contracts (Classic was sold as perpetual license + annual maintenance).
- **Technical dependencies:** InterBase database (unsupported). Windows-only client. No cloud dependencies.

### 3. Customer Impact Assessment

| Segment | Count | ARR | Impact | Migration Viability | Churn Risk |
|---------|-------|-----|--------|--------------------|------------|
| High Classic usage, retiring within 5 years (physician age 60+) | ~900 | $11M | Critical — this is their practice's operating system | Low — not worth the switching cost | Low if we maintain until retirement; high if forced |
| High Classic usage, not retiring, willing to consider Cloud | ~1,200 | $15M | High — but they see the value of modern capabilities | Medium — need migration support and feature parity for core workflows | Medium |
| High Classic usage, hostile to Cloud | ~400 | $6M | Critical — they view forced migration as betrayal | Low — emotional resistance | High |
| Moderate Classic usage (uses a subset of features) | ~500 | $5M | Medium — they use what they need and don't care about the rest | High — core features exist in Cloud | Low |
| Low Classic usage (maybe evaluating alternatives anyway) | ~200 | $3M | Low — they're likely to leave regardless | N/A | Already high |

### 4. Migration Strategy
- **Feature parity:** Cloud already covers 80% of Classic's core clinical and billing workflows. Remaining 20% gap is niche features used by <5% of customers. Strategy: build the top 10 missing features by usage frequency (covers 15% of the gap), sunset the remaining 5% without replacement but with workaround documentation.
- **Data migration:** Automated migration tool (released Q3 2026) migrates patient records, billing history, and appointments. Manual review required for custom templates and macros (cannot be automated due to proprietary Classic format).
- **Pricing transition:** Classic-compatible Cloud tier at $299/month (vs. Classic maintenance at $200/month and standard Cloud at $600/month). Grandfathering: Classic customers who migrate by Dec 2027 lock in $249/month for 3 years.
- **Timeline:** Phase 1 (2026): Migration tool, Cloud feature parity for top 10 gaps, pricing announcement. Phase 2 (2027): Active migration support, white-glove service for high-value accounts. Phase 3 (2028): Final migration push, communication to remaining accounts, service shutdown Dec 2028.

### 5. Communication Plan

| Stakeholder | Message | Channel | Timing | Owner |
|-------------|---------|---------|--------|-------|
| Classic customers | "Classic is entering its final chapter. We've built Cloud to carry forward what you love about Classic, with modern capabilities. Here's your migration path, timeline, and dedicated support." | Email from CEO + account manager call + in-app notification | Jan 2027 (12 months before shutdown) | CEO + VP CS |
| Classic Customer Advisory Board | Pre-brief before public announcement. Address their concerns directly. Ask for their partnership in the transition. | Private dinner at annual user conference | Nov 2026 (before public announcement) | CEO + CPO |
| Cloud customers | "We're investing fully in Cloud. The Classic transition enables us to focus engineering on the features you've been asking for." | Email + in-app | Jan 2027 | Product Marketing |
| Classic engineering team | "Your expertise is critical to the transition. We need your help building the migration tooling and supporting customers. After the transition, opportunities exist on the Cloud team." | Team meeting + 1:1s | Nov 2026 | VP Engineering |
| Sales team | FAQ, talking points, objection handling, pricing/packaging for migration conversations | Sales enablement session | Dec 2026 | Product Marketing |

### 6. Risk Management
- **Churn risk:** Expected churn: 15-25% of Classic customers ($6M-$10M ARR). Mitigation: migration pricing incentives, white-glove migration service, extended support for retiring practitioners.
- **Brand risk:** "MediCore abandons loyal customers" narrative. Mitigation: CEO communication emphasizes "25-year journey" and "building the next 25 years." Customer choice: maintain Classic in security-only mode for practices unwilling to migrate (extended support at higher cost).
- **Legal risk:** Maintenance contracts require "reasonable support." 3-year notice period exceeds any reasonable standard. Data export capability must be provided.
- **Operational risk:** Migration tool bugs, data integrity issues during migration. Mitigation: phased migration (start with low-risk volunteer practices, learn, iterate, scale).
- **Data risk:** Customer data in InterBase format must be migrated or exported. After shutdown, data must be retained for regulatory compliance (HIPAA: 6 years). Data retention plan: exported to standard format, stored in encrypted Cloud storage, accessible on customer request.

### 7. Resource Plan
- **Engineering (2026-2028):** Migration tool: 6 person-months. Feature parity (top 10 gaps): 12 person-months. Cloud Classic-compatible tier: 4 person-months. Total: ~22 person-months over 2 years.
- **Customer Success:** Dedicated migration support team (4 people during peak migration period, 2027-2028). White-glove migration for top 200 accounts (by ARR).
- **Sales:** Migration conversations integrated into renewal discussions. Account managers trained on Cloud value proposition for Classic users.
- **Legal:** Contract review (maintenance terms), data retention compliance, regulatory notification if applicable.

### 8. Sunset Milestones

| Milestone | Date | Criteria | Owner |
|-----------|------|----------|-------|
| Board approval | Q2 2026 | Board reviews and approves sunset plan | CEO |
| Internal announcement | Nov 2026 | All internal teams briefed, FAQs distributed, enablement complete | CPO + VP People |
| Customer Advisory Board pre-brief | Nov 2026 | CAB informed, concerns addressed, partnership secured | CEO + CPO |
| Public announcement | Jan 2027 | Email, in-app, blog post, PR (if significant) | Product Marketing |
| New sales stopped | Jan 2027 | Classic no longer sold to new customers | VP Sales |
| Migration tool GA | Q3 2026 | Migration tool released, tested with 20 volunteer practices | VP Engineering |
| Feature freeze | Jun 2027 | No new features added to Classic. Security/compliance updates only. | VP Engineering |
| Migration incentive deadline | Dec 2027 | Grandfathering pricing lock expires | VP CS |
| Service degradation | Jun 2028 | Classic becomes read-only (data access, no new data entry) | VP Engineering |
| Service shutdown | Dec 2028 | Classic servers decommissioned. Data retained per compliance requirements. | VP Engineering |

### 9. Post-Sunset Review (Projected)
To be completed Q1 2029. Key questions: What % of customers migrated to Cloud? What % churned? What % extended support? Actual revenue impact vs. projection? Customer satisfaction with migration process? Lessons for future sunsets (platform version upgrades, feature deprecations).

---

## Common Mistakes

1. **Sunset as surprise.** Customers should have 12+ months of notice for major product sunsets. Short notice generates anger, churn, and reputational damage that could have been avoided.
2. **No migration path.** Telling customers "we're shutting down your product, good luck" is a betrayal of trust. Even if there's no perfect replacement, provide data export, alternate vendor recommendations, and transition support.
3. **Underestimating emotional attachment.** Customers who have used a product for 15+ years have real emotional investment. Treat the sunset with respect — acknowledge the history, honor the relationship, and make the transition worthy of the loyalty.
4. **Sunset as purely technical exercise.** A sunset is primarily a customer relationship and communication challenge. The technical work (shutting down servers, migrating data) is the easy part.
5. **No post-sunset review.** Learn from every sunset. The patterns will recur — version upgrades, platform migrations, feature deprecations. Build organizational muscle for managing product endings.

## Dependencies

- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): The sunset should be part of a broader strategy — what are you making space for?
- [Decision Memo Template](DECISION_MEMO_TEMPLATE.md): The sunset decision should be documented as a formal decision.
- [Stakeholder Incentive Map](STAKEHOLDER_INCENTIVE_MAP.md): Sunset decisions affect many stakeholders. Map their incentives before communicating.
- [Core Doctrine: PRN-0013](../01_core_doctrine/PRINCIPLES.md): Product sunset decisions principle.
