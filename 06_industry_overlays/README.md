# Industry Overlays

## What Is an Industry Overlay?

The core product leadership doctrine is industry-agnostic. The principles of empowered teams, strategic choice, reversible decisions, and continuous discovery apply whether you build consumer software or grid-scale energy systems. But regulated industries impose constraints, risks, and decision patterns that layer on top of the core doctrine — they do not replace it.

An **industry overlay** is a set of industry-specific additions to the core doctrine. It covers:

- **Regulatory frameworks** that constrain product decisions
- **Economic structures** that shape business models and unit economics
- **Risk categories** that do not exist (or are weaker) in unregulated industries
- **Stakeholder maps** with actors who have veto power beyond users and buyers
- **Product archetypes** that make sense only within that industry
- **Failure modes** specific to product leadership in that domain
- **Decision frameworks** adapted for regulated contexts

An overlay is not a textbook. It assumes you understand product management fundamentals. It adds what changes when the product operates under regulatory regimes, physical constraints, long-lived assets, sovereign counterparties, or institutional customers with procurement processes measured in years.

## The Regulated Product Value Model

Standard product value models optimize for **customer value** — the value users or buyers receive from the product. Growth-stage product leaders are taught to maximize this. But in regulated industries, the value model is more complex:

```
Product Value = Customer Value + Institutional Value + Economic Value - Expected Downside - Control Burden
```

**Customer Value** — The direct benefit to end users: faster mortgage closing, lower insurance premiums, more reliable electricity, faster infrastructure permitting.

**Institutional Value** — The benefit to the institution deploying the product: regulatory compliance achieved, audit readiness, capital efficiency, risk reduction, stakeholder confidence, reputational protection. Institutional buyers often value this more than customer value.

**Economic Value** — Revenue, cost reduction, market access, balance-sheet efficiency. In financial services, this includes capital consumption. In energy, this includes capacity payments and avoided costs. In development finance, this includes mobilization ratios.

**Expected Downside** — The probability-weighted cost of adverse outcomes: regulatory fines, enforcement actions, reputational damage, operational losses, litigation, loss of license to operate. In regulated industries, downside is not just churn or bad PR — it is existential.

**Control Burden** — The product, process, and organizational cost of operating under regulatory control: audits, examinations, reporting, model documentation, compliance reviews, third-party risk assessments, business continuity planning. Control burden is a cost center that product leaders must design for, not resent.

A product that delivers high customer value but fails to address institutional value or control burden will not be adopted by regulated institutions. A product leader who cannot articulate the institutional value and the approach to expected downside cannot get a regulated-industry product funded.

## The Overlay Structure

Each industry overlay follows a consistent structure:

1. **Industry Architecture** — How the industry works: who are the actors, how does money flow, what are the dominant business models
2. **Regulatory Landscape** — The key regulatory frameworks and their product implications
3. **Economic Fundamentals** — The unique economic drivers product leaders must understand
4. **Risk Categories** — Risks that are industry-specific and must be designed for
5. **Stakeholder Map** — The actors who can veto product decisions
6. **Product Archetypes** — The types of products that exist in this industry
7. **Decision Frameworks** — Adapted frameworks for product decisions in this context
8. **Key Failure Modes** — What product leaders get wrong in this industry
9. **Career Implications** — What it means to build a product career in this industry

## Available Overlays

| Overlay | File | Key Regulatory Frameworks |
|---------|------|--------------------------|
| Financial Services | `FINANCIAL_SERVICES.md` | Basel III/IV, SR 11-7, Dodd-Frank, PSD2, GDPR, DORA, NYDFS Part 500 |
| Insurance | `INSURANCE.md` | Solvency II, IFRS 17, NAIC model laws, state-level rate regulation |
| Power and Energy | `POWER_AND_ENERGY.md` | FERC Orders, NERC CIP, state PUC regulation, PURPA, RTO/ISO tariffs |
| Infrastructure and Development Finance | `INFRASTRUCTURE_AND_DEVELOPMENT_FINANCE.md` | World Bank Procurement, Equator Principles, Paris Agreement, national procurement |

## How to Use the Overlays

If you are joining a regulated industry for the first time, read the full overlay before your first product decision. The failure modes section will prevent the most common mistakes. The decision frameworks will give you a structure for your first months.

If you are a career product leader in a regulated industry, use the overlay as a reference when facing a new sub-domain. The product archetypes section will help you understand adjacent businesses in your institution.

If you are evaluating a regulated-industry opportunity, read the overlay to assess fit. The career implications section will help you decide whether the trade-offs are worth it for you.

## Field Guides

The `handbook/INDUSTRY_FIELD_GUIDES/` directory contains condensed, actionable field guides derived from these overlays. They are designed for reference during product work, not for initial learning. Read the overlay first, then use the field guide as a checkpoint.

## Quality Gate

Per QUALITY_GATES.md: "A regulated-industry module discusses only UX and growth" is a failure condition. Every overlay must address regulatory constraints, institutional economics, risk categories, and the product implications of operating under regulatory supervision. If an overlay reads like a consumer-product playbook, it fails the quality gate.
