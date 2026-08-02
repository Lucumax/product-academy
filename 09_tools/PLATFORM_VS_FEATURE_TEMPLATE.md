# Platform vs. Feature Template

## Purpose

A platform vs. feature analysis evaluates whether an investment should be a one-off feature (solving an immediate customer need) or a platform capability (creating reusable infrastructure that enables multiple features, teams, or products). It answers: "Should we solve this specific problem, or should we build the capability to solve this class of problem?"

This is one of the most consequential product architecture decisions because platform investments have higher upfront cost, longer time-to-value, and greater strategic leverage. Getting it wrong — building a feature when you should have built a platform, or building a platform when a feature would have sufficed — is a common and expensive mistake.

## When to Use

- You're evaluating a significant new capability that could be built as a feature or as a reusable platform
- Multiple teams or products need similar capabilities
- You're deciding whether to invest in infrastructure that doesn't deliver immediate customer value but unlocks future velocity
- A customer request could be solved as a point solution or as a generalized capability
- You're making a build vs. buy decision where "build" could mean platform

## Template Structure

### 1. The Problem and the Need

- **What problem are we solving?** Describe the underlying need, not the proposed solution.
- **Who has this problem?** One customer? One segment? Multiple segments? All customers? Internal teams?
- **How is it solved today?** Workaround, manual process, not solved?
- **What happens if we don't solve it?** What is the cost of inaction?

### 2. Feature Approach

**Description:** Build a specific solution for the specific need. Deliver customer value as quickly as possible. Do not invest in generalization.

**Scope:** What exactly would the feature do? For whom? What would it NOT do?

**Advantages:**
- Faster time-to-value for the specific need
- Lower upfront investment
- Simpler to design — fewer stakeholders, fewer constraints
- Can validate the problem before investing in a platform

**Disadvantages:**
- Does not enable future use cases — each new need requires new investment
- May create technical debt if later generalized
- May fragment the product if multiple teams build overlapping point solutions

**Cost estimate:** Engineering person-weeks, calendar time to MVP, ongoing maintenance.

### 3. Platform Approach

**Description:** Build a generalized capability that can be used by multiple features, teams, or products. The platform capability is an investment in future velocity and coherence.

**Scope:** What would the platform capability do? What use cases would it serve? Who would use it (internal teams, external developers, customers)?

**Advantages:**
- Creates leverage — one investment enables multiple features
- Reduces future cost and time for similar needs
- Creates product coherence (same capability, consistent UX)
- Can become a competitive moat (platforms are harder to copy than features)
- Can enable third-party innovation (if exposed as an API)

**Disadvantages:**
- Higher upfront investment
- Longer time to first customer value
- More complex to design — must generalize across use cases
- Risk of over-engineering: building a platform for use cases that never materialize
- Requires ongoing investment (platforms need maintenance, documentation, support)

**Cost estimate:** Engineering person-weeks for the platform capability, calendar time to MVP, ongoing maintenance and support, opportunity cost of deferred features.

### 4. The Leverage Question

What future use cases would the platform enable? Be specific:

| Future Use Case | Value | Without Platform: Cost to Build as Feature | With Platform: Additional Cost | Platform Savings |
|-----------------|-------|-------------------------------------------|-------------------------------|-----------------|
| Use case 1 | | | | |
| Use case 2 | | | | |
| Use case 3 | | | | |
| Total | | | | |

If total platform savings exceed the incremental cost of building platform vs. feature, the platform approach has positive ROI. But this requires the future use cases to actually materialize — which is the key assumption.

### 5. Confidence Assessment

For each future use case, rate your confidence that it will actually materialize:
- **High confidence:** Customer demand is validated, it's on the roadmap, it's clearly valuable
- **Medium confidence:** Reasonably likely based on customer feedback and market trends
- **Low confidence:** Speculative — could be valuable but unvalidated

The platform approach makes sense when there are multiple HIGH confidence future use cases. If most future use cases are low confidence, the feature approach is safer.

### 6. Risk Assessment

**Feature approach risks:**
- Re-work risk: If we later need to generalize, how expensive is the refactor?
- Fragmentation risk: Will multiple teams build overlapping point solutions?
- Competitive risk: Will a competitor build a platform and outpace us?

**Platform approach risks:**
- Over-engineering risk: Building for use cases that never materialize
- Delayed value risk: The current need goes unsolved while we build the platform
- Adoption risk: Will internal teams/external developers actually use the platform?
- Maintenance risk: Platform requires ongoing investment — will the organization sustain it?

### 7. Recommendation

- **Recommendation:** Feature / Platform / Phased (feature first, generalize later)
- **Key trade-off:** What are we gaining and sacrificing?
- **If phased:** At what point do we generalize? What triggers the transition?
- **Reversal conditions:** Under what conditions would we change this decision?

---

## Filled Example: Compliance Rule Engine

### 1. The Problem and the Need
- **Problem:** Compliance officers need to define custom validation rules for evidence collection. Example: "For SOC 2 CC-4.2, if a user has admin access to production AND their access was granted >90 days ago, flag as non-compliant unless there's an access review within the last 90 days." Each customer's compliance requirements are slightly different, and hard-coded rules don't cover the variation.
- **Who has this problem?** All customers doing SOC 2 (currently 4 pilots, projected 50+ customers within 2 years). Also applicable to other frameworks (GDPR, HIPAA, ISO 27001) with different rule types.
- **How solved today?** Compliance officers manually review evidence. For each control, they check the evidence, apply their organization's policies, and flag issues. This is ~40% of their weekly compliance work.
- **Cost of inaction:** Our value proposition is "automated compliance." If customers still have to manually review 40% of controls, we're not delivering on the promise. Competitors (Vanta, Drata) are building configurable rule engines.

### 2. Feature Approach
**Description:** Build a "Custom Rule Builder" feature that lets SOC 2 customers define 5 pre-set rule types (access review rule, evidence freshness rule, configuration drift rule, coverage gap rule, exception tracking rule). Each rule type has a fixed template with configurable parameters (time thresholds, scope, severity).

**Scope:** SOC 2 only. 5 rule types. UI-based rule configuration (no code). Rules execute on evidence collection triggers.

**Advantages:** Solves the immediate need for SOC 2 customers (our current market). Delivers value in 6-8 weeks. Validates that customers will actually configure custom rules. Lower investment with clearer ROI.

**Disadvantages:** If we later expand to GDPR, HIPAA, ISO 27001, we'll need to build new rule types for each framework. Rule types are framework-specific, so the feature approach creates a multiplication problem: frameworks × rule types = engineering effort.

**Cost:** 8 person-weeks (2 engineers × 4 weeks). Calendar: 6-8 weeks to MVP.

### 3. Platform Approach
**Description:** Build a "Compliance Rules Engine" — a generalized rule evaluation engine that can ingest compliance data (evidence, controls, frameworks), apply any rule defined in a domain-specific language, and produce compliance status outputs. The engine is framework-agnostic. Rules are defined in a configuration format (JSON/YAML) that can be created via UI or API. The engine is a platform capability that multiple products (SOC 2, GDPR, HIPAA, ISO 27001) can use.

**Scope:** Framework-agnostic rule engine. Event-driven evaluation pipeline. Rule definition API + UI rule builder. Extensible operator library (comparison, temporal, set-based, cross-reference). User-facing: same 5 SOC 2 rule types as Feature approach, but built ON the engine rather than as point solutions.

**Advantages:** One rule engine serves all compliance frameworks (current and future). New rule types can be added by defining them in the configuration format, not by building new features. Third-party developers could define custom rule types via API. Creates a competitive moat — a generalized compliance rules engine is harder to replicate than a SOC 2 rule builder.

**Disadvantages:** Higher upfront investment. Longer time to first customer value. Risk of over-engineering — if we only ever do SOC 2, the generalization is wasted. More complex to design — must anticipate future framework requirements.

**Cost:** 18 person-weeks (2 engineers × 9 weeks). Calendar: 14-16 weeks to MVP.

### 4. The Leverage Question

| Future Use Case | Value | Without Platform (Feature Cost) | With Platform (Additional Cost) | Platform Savings |
|-----------------|-------|----------------------------------|--------------------------------|-----------------|
| SOC 2 custom rules (current need) | High | 8 person-weeks (already budgeted) | 18 person-weeks (platform build) | -10 person-weeks (platform costs MORE) |
| GDPR custom rules (Q3 need) | High | 6 person-weeks (new rule types) | 2 person-weeks (new rule definitions) | +4 person-weeks saved |
| HIPAA custom rules (Q4 need) | Medium | 8 person-weeks | 2 person-weeks | +6 person-weeks saved |
| ISO 27001 rules (next year) | Medium | 6 person-weeks | 2 person-weeks | +4 person-weeks saved |
| Customer-defined rules via API (strategic) | High | 12+ person-weeks (would need a platform anyway) | 3 person-weeks (API layer on engine) | +9 person-weeks saved |
| Partner/auditor rules via API (strategic) | Medium | Not feasible as feature | 2 person-weeks | Infinite (not possible without platform) |
| Total (18 months) | | 40 person-weeks | 29 person-weeks | +11 person-weeks saved |

Platform breaks even at the GDPR use case (Q3) and becomes net positive after that.

### 5. Confidence Assessment
- **SOC 2 custom rules:** HIGH confidence. Validated by 4 pilot customers and competitive analysis.
- **GDPR custom rules:** HIGH confidence. 2 of 4 pilots are doing both SOC 2 and GDPR. Multiple prospects in pipeline.
- **HIPAA custom rules:** MEDIUM confidence. Healthcare vertical is our target expansion. Validated by 12 prospect interviews.
- **ISO 27001 rules:** MEDIUM confidence. International expansion planned but timeline uncertain.
- **Customer-defined rules via API:** LOW confidence. Vision-level capability. No customer has explicitly asked for API-accessible rule definition.
- **Partner/auditor rules:** LOW confidence. No partner discussions yet. Speculative.

### 6. Risk Assessment
**Feature approach risks:**
- Re-work risk (HIGH): If we build SOC 2 rule types as point solutions and then generalize later, the refactor cost is estimated at 12-14 person-weeks (rebuilding rule types on the engine + data migration). This is roughly the same as building the platform upfront.
- Fragmentation risk (MEDIUM): If the team builds framework-specific rule types independently, we'll have inconsistent rule behavior across SOC 2, GDPR, HIPAA.
- Competitive risk (LOW): Competitors are also building framework-specific rule builders. Nobody has a generalized engine yet. But the first to build one gains a structural advantage.

**Platform approach risks:**
- Over-engineering risk (MEDIUM): We're building for 5 future use cases, 2 of which are low confidence. The platform may be more general than we need.
- Delayed value risk (HIGH): The current SOC 2 customers have been asking for custom rules for 2 months. A 16-week platform build means 4 months before they see any value. In a competitive market, 4 months is a long time.
- Adoption risk (LOW): Internal teams will use the engine because it's the only way to build rules. External adoption (API) is speculative but not required for ROI.
- Maintenance risk (MEDIUM): Platform requires ongoing investment. But rule engine maintenance is likely cheaper than maintaining 4+ framework-specific rule builders.

### 7. Recommendation
- **Recommendation:** Phased approach. Phase 1: Build the generalized compliance rules engine (platform) but scope the initial release to SOC 2 rule types only. This delivers customer value for SOC 2 while building the platform foundation. Phase 2: Add GDPR and HIPAA rule definitions (low incremental cost because the engine already exists). Phase 3: Expose API for customer-defined rules (if and when validated).

- **Key trade-off:** We accept 8 additional weeks of development time (16 weeks vs. 8 weeks for feature approach) to build the platform foundation. In exchange, subsequent frameworks add weeks instead of months, and we have a differentiated platform capability. The risk is that the 8-week delay hurts competitive positioning in SOC 2 — mitigated by keeping the Phase 1 scope tight (5 rule types, not an infinitely flexible engine).

- **Trigger for Phase 2 generalization:** SOC 2 custom rules are live with >80% customer satisfaction (measured 30 days post-launch). At least 1 GDPR pilot customer has confirmed need for GDPR-specific rules.

- **Reversal conditions:** If SOC 2 rule builder adoption is <30% of customers within 90 days of launch (customers don't actually want to configure rules), the platform investment was premature. If we lose >2 SOC 2 deals specifically because we lack custom rules (and the 16-week timeline was the factor), reconsider whether a faster feature approach would have been better.

---

## Common Mistakes

1. **Platform for platform's sake.** Building a platform because "platforms are cool" or "we're a platform company now." Platform investments should be driven by clear leverage, not identity.
2. **Feature for every use case.** Building point solutions for every customer request without looking for patterns. The accumulation of point solutions creates a fragmented, unmaintainable product.
3. **Platform for a single use case.** Building a generalized platform when there's only one known use case. Wait until you have at least 2-3 validated use cases before generalizing.
4. **Underestimating platform maintenance.** Platforms require documentation, support, deprecation policies, versioning, migration tooling, and developer relations. The initial build is the easy part.
5. **Platform as waterfall project.** You don't need to build the entire platform before delivering any value. Phased approaches (build the engine with a narrow first use case, generalize incrementally) reduce risk and time-to-value.

## Dependencies

- [Build vs. Buy Template](BUILD_VS_BUY_TEMPLATE.md): Related decision — if you're not building the platform, could you buy it?
- [Product Strategy Template](PRODUCT_STRATEGY_TEMPLATE.md): Platform strategy should be part of product strategy — does the platform approach reinforce your strategic position?
- [Resource Allocation Memo](RESOURCE_ALLOCATION_MEMO.md): Platform investments often require dedicated team capacity and sustained commitment.
- [Core Doctrine: PRN-0005, PRN-0008](../01_core_doctrine/PRINCIPLES.md): Platform thinking and platform product management principles.
