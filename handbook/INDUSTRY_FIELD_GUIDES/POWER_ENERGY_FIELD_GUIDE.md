# Power and Energy Field Guide

## Quick Scan — Before Any Product Decision

1. **Does this product affect the physical power system?** If yes: have you modeled the physical constraints (thermal limits, voltage limits, stability limits, N-1)? Does it work when the grid is under stress, not just in normal conditions?
2. **Who is the buyer, and what is their regulatory incentive?** A utility buys to satisfy its PUC. An ISO/RTO buys to satisfy FERC market rules. A consumer buys based on price, convenience, or values. Your product must solve for the buyer's incentive, not the user's preference.
3. **What are the regulatory milestones?** FERC orders, PUC rate cases, NOPR-to-final-rule timelines, tariff filings, interconnection agreements. Map them before the product timeline.
4. **Is your revenue model exposed to wholesale market prices?** If yes: your product's economics depend on price forecasts with high uncertainty. Stress-test under multiple price scenarios.
5. **What is the implementation timeline, and can your stakeholders sustain commitment?** Energy products take 3-7+ years from concept to scale. Interim milestones and demonstrated progress are essential for maintaining momentum.

## Regulatory Triggers

### You connect to the bulk electric system → NERC CIP compliance

Any system within the Electronic Security Perimeter of a BES Cyber Asset is subject to NERC CIP standards (CIP-003 through CIP-013). This includes: cybersecurity policies, network segmentation, access controls, patch management, change management, incident response, supply chain risk management. Classification as a BES Cyber Asset subjects the product to regulatory compliance that may exceed development cost.

### You participate in wholesale markets → FERC jurisdiction, RTO/ISO market rules

Any product that bids into, clears in, or settles in wholesale electricity markets must comply with the RTO/ISO tariff (legally enforceable) and FERC regulations. Market manipulation is a FERC enforcement priority — algorithmic trading must include manipulation safeguards.

### You affect retail rates → State PUC jurisdiction, rate case process

Any product that changes how utility customers are charged or how utility costs are recovered requires PUC engagement. A new rate design (time-of-use, demand charges, subscription pricing) may require a tariff filing and PUC approval. Budget 6-18 months for a contested rate case.

### You generate electricity → Interconnection, permitting, environmental compliance

Interconnection to the grid requires: interconnection application, system impact study, facilities study, interconnection agreement. Permitting requires: local zoning, state environmental review, federal NEPA review (if on federal land or with federal involvement). Timeline: 3-7 years. You cannot sell power until you are interconnected and permitted.

### You control customer energy usage → Customer protection, data privacy

Demand response, smart thermostats, and behind-the-meter control products must respect: (a) customer consent — customers must knowingly opt in, (b) data privacy — energy usage data reveals occupancy patterns and behavior, (c) reliability — load control must not compromise critical medical equipment or essential services.

## Stakeholder Map

| Stakeholder | What They Care About | Can Stop You? |
|-------------|---------------------|---------------|
| **Utility** | Regulatory compliance, rate base growth, reliability metrics, O&M costs | Yes — the distribution and often retail interface belongs to the utility |
| **RTO/ISO** | Market efficiency, reliability, non-discriminatory access | Yes — controls wholesale market participation rules |
| **FERC** | Just and reasonable rates, market integrity, reliability | Yes — can reject market rules, tariff changes, or enforcement |
| **State PUC** | Consumer protection, rate reasonableness, utility performance, state policy goals | Yes — controls retail rates, utility investments, and resource planning |
| **NERC** | Reliability standards and enforcement | Yes — can levy fines for non-compliance with mandatory standards |
| **System Operator** | Real-time reliability, generation-load balance, transmission constraints | Yes — can curtail generation or disconnect for reliability threats |
| **Local government** | Zoning, permitting, community impacts, tax revenue | Yes — can deny permits or impose conditions that make projects uneconomic |
| **Community** | Visual impact, noise, property values, environmental justice, local benefits | Can delay or block through litigation and political opposition |
| **Environmental agencies** | Air quality, water quality, endangered species, land use | Yes — can deny permits required for construction and operation |
| **Off-taker / PPA counterparty** | Credit risk, price risk, supply reliability | Can refuse to sign PPA or terminate for non-performance |

## Risk Checklist

### Physical system risk
- [ ] Resource adequacy contribution quantified (capacity value, ELCC — Effective Load Carrying Capability)
- [ ] Interconnection studies completed (feasibility, system impact, facilities study)
- [ ] Transmission constraints modeled (will congestion erode your revenue?)
- [ ] Operating characteristics modeled (ramp rates, minimum load, start-up time, cycling limits)
- [ ] N-1 contingency compliance verified (system survives loss of your asset?)

### Market risk
- [ ] Wholesale price scenarios modeled (base, high, low, extreme)
- [ ] Basis risk quantified (locational price difference from hub price)
- [ ] Ancillary service revenue opportunities assessed (regulation, reserves, capacity)
- [ ] Market rule change risk assessed (e.g., energy market redesign, capacity market design changes)
- [ ] Off-taker credit risk assessed (if relying on PPA revenue)

### Regulatory risk
- [ ] Required FERC filings identified and timeline estimated
- [ ] Required PUC proceedings identified and timeline estimated
- [ ] NERC compliance obligations identified (CIP, BAL, etc.)
- [ ] Environmental permits identified and timeline estimated
- [ ] Renewable energy credit (REC) eligibility and market rules understood

### Revenue risk
- [ ] PPA duration and counterparty credit quality (if PPA-based)
- [ ] Merchant revenue exposure with stress scenarios (if merchant)
- [ ] REC/add-er revenue and market outlook (if clean energy)
- [ ] Tax credit qualification risk (ITC/PTC prevailing wage, apprenticeship, domestic content, energy community)
- [ ] Inflation exposure (PPA escalation, construction cost escalation, O&M escalation)

### Execution risk
- [ ] Supply chain lead times and concentration risk
- [ ] EPC contractor experience with technology type and project scale
- [ ] Permitting and siting timeline risk (with history of local support/opposition)
- [ ] Interconnection queue position and timeline risk
- [ ] Construction seasonality (can you pour concrete in winter?)

### Operational risk
- [ ] Cyber risk assessed (is your product a NERC CIP asset?)
- [ ] Physical security assessed (substation security, equipment protection)
- [ ] Extreme weather resilience (flood, wind, fire, ice)
- [ ] Performance guarantees and liquidated damages exposure (PPA, EPC, O&M contracts)
- [ ] Degradation and performance uncertainty (solar degradation rate, wind turbine availability)

## Decision Patterns

### Pattern: "The market price forecast shows attractive returns."

Forecasts are uncertain. In energy, price uncertainty is structural — it comes from fuel price volatility, load growth uncertainty, renewable penetration effects, policy changes, and transmission constraints. Always run: base case, low price case (what if gas stays cheap?), high price case (what if gas spikes?), canary case (what specific condition would make the project uneconomic?). If the canary case is plausible, structure the financing or contracting to survive it.

### Pattern: "Let's optimize the battery for energy arbitrage."

Batteries have multiple revenue streams: energy arbitrage, frequency regulation, spinning reserve, capacity, and (for behind-the-meter) demand charge reduction and backup power. Co-optimize across all streams. A battery that only does energy arbitrage is leaving money on the table and is more exposed to arbitrage spread compression. The optimal dispatch changes over the battery's life as markets evolve.

### Pattern: "We'll launch in all the major RTOs."

RTO markets have different rules, different products, different price dynamics, and different interconnection processes. Launch in ONE RTO, learn what works, then adapt for the next. An energy product that works in ERCOT (energy-only market, no capacity market) may fail in PJM (energy + capacity market, different ancillary service products). Each RTO is effectively a separate market with its own product requirements.

### Pattern: "The consumer app is great — we just need utility distribution."

Consumer energy apps face a structural challenge: the utility is not a distribution channel for consumer apps. Utilities buy solutions to regulatory obligations — reliability, energy efficiency, DER integration mandates. Frame the consumer app as a solution to a utility obligation, with consumer adoption as the evidence, not the goal.

### Pattern: "Technology costs are declining — our business case improves every year."

Declining costs are good. They also mean your competitors (and your customers' alternatives) improve every year. A solar-plus-storage project that is economic today may face competition from even cheaper solar-plus-storage being built next year. The value of being first is the PPA price you lock in; the risk is being undercut by cheaper projects that enter later. Model the competitive dynamics, not just your own cost decline.

## Failure Mode Check

| Failure Mode | Early Warning Sign | Mitigation |
|-------------|-------------------|------------|
| Ignoring physical constraints | The product treats energy as a digital good — location-independent, storable, instantly deliverable | Before designing product logic, draw the one-line diagram. Understand the physical path from generation to load. |
| Underestimating regulatory timeline | Timeline shows "regulatory approval: 3 months" for a process that takes 18-24 months | Map every regulatory milestone with realistic duration based on precedent. Build product roadmap around regulatory roadmap. |
| Building for consumers when buyers are utilities | User testing shows strong NPS; utilities show no interest | Understand the utility's regulatory obligations and PUC expectations. Frame the product in utility language: reliability, cost recovery, regulatory compliance. |
| Ignoring interconnection | Project pipeline shows 2 GW/year; interconnection queue shows 5-year backlog and $50M+ upgrade costs per project | Model interconnection cost and timeline as first-order constraints. Prioritize sites with available interconnection capacity. Build interconnection management into the product. |
| Optimizing for one revenue stream | Product maximizes energy revenue but ignores regulation, reserves, and capacity value | Co-optimize across ALL revenue streams. The revenue stack is the product — design for the full stack. |
| Treating grid as infinite sink/source | Product assumes grid can absorb any export and supply any import at the market price | Model grid constraints at the project location. What is the local load? What is the local hosting capacity? Will your project be the one that triggers upgrade requirements? |
| Assuming linear adoption curves | EV/solar/storage adoption modeled as smooth S-curve | Model constraints: charger deployment rate, grid capacity, supply chain (battery minerals), policy (tax credits, mandates). The binding constraint determines the adoption ceiling. |

## Key Metrics

### For generation products
- **Levelized Cost of Energy (LCOE):** Total lifecycle cost per MWh. Used for comparing technologies.
- **Net Capacity Factor:** Actual output / maximum possible output. Tells you how much energy the asset actually produces.
- **Capacity value / ELCC:** How much firm capacity does this resource contribute to resource adequacy?
- **Revenue per MW:** Total revenue (energy + ancillary services + capacity + RECs) per MW of capacity.
- **PPA price vs. market price spread:** Are you locking in above-market or below-market revenue?

### For grid products
- **SAIDI / SAIFI:** System reliability indices. If your product affects reliability, you must demonstrate impact (positive or at least non-negative).
- **Congestion cost:** Cost of transmission constraints preventing lowest-cost dispatch. Products that reduce congestion have value = congestion cost reduction.
- **Interconnection queue processing time:** Months from application to agreement. If your product accelerates this, the value is the avoided delay cost for generation projects.
- **Hosting capacity:** MW of DER that can be accommodated on a distribution circuit without upgrades. Products that increase hosting capacity enable DER growth.

### For DER products
- **Value stack:** Total customer and grid value per kW per year: energy savings + demand charge reduction + backup value + grid service revenue + REC value.
- **Payback period:** Years until cumulative savings exceed installed cost. Below 7 years for residential, below 5 years for commercial/industrial is typical threshold.
- **Self-consumption rate (solar-plus-storage):** Percentage of solar generation consumed on-site vs. exported. Higher is generally better (retail rate > export rate).
- **Backup duration:** Hours of backup power the battery provides during an outage. Must meet customer expectations.

## Language to Use

| Say This | Not This |
|----------|----------|
| "We need the one-line diagram and the interconnection study before we can model project economics." | "The site has great solar resource — let's proceed." |
| "What is the project's ELCC — how much capacity credit does it earn in this RTO?" | "It generates during peak hours." |
| "We should co-optimize dispatch across energy, regulation, and reserves." | "We'll buy low and sell high." |
| "The regulatory milestones are: PUC rate case (18 months), FERC market rule change (24 months), and interconnection study (18 months)." | "Regulatory approval takes a while." |
| "What is the binding constraint on our adoption curve?" | "Adoption will follow a standard S-curve." |
| "We should model merchant revenue under base, low, and extreme price scenarios." | "The price forecast looks good." |
| "The utility's incentive under PBR is to improve SAIDI — our product advances that metric." | "Utilities need to modernize their grids." |
| "This distribution circuit's hosting capacity is 2 MW — our project would require an upgrade." | "Let's deploy DERs everywhere." |

## Quick Reference: RTO/ISO Markets

| RTO/ISO | Region | Key Characteristics | Product Considerations |
|---------|--------|---------------------|----------------------|
| PJM | Mid-Atlantic, Midwest | Capacity market (RPM), energy market, ancillary services | Capacity market is material revenue. Interconnection queue is deep. |
| ERCOT | Texas | Energy-only market, no capacity market | Price spikes during scarcity events. No capacity revenue. High renewable penetration. |
| CAISO | California | Energy market, resource adequacy program, high renewable penetration | Duck curve (midday solar oversupply). Resource adequacy is bilateral, not centralized capacity market. |
| MISO | Midwest | Energy market, capacity market (resource adequacy construct) | High wind penetration. Transmission-constrained in north-south direction. |
| NYISO | New York | Energy market, capacity market (ICAP), ancillary services | Capacity market with locational requirements (NYC vs. rest of state). |
| ISO-NE | New England | Energy market, capacity market (FCM), ancillary services | Gas-dependent. Winter reliability concerns. |
| SPP | Central US | Energy market, resource adequacy requirement | High wind penetration. Integrated marketplace includes both day-ahead and real-time. |

## Top 5 Things Product Leaders Get Wrong in Energy

1. They treat electricity like a digital good — ignoring that it cannot be stored, must be balanced in real time, and follows the laws of physics, not software.
2. They build a 2-year product plan on a timeline that requires 5 years of regulatory approvals — and are surprised when year 2 arrives and the product cannot launch.
3. They optimize for the consumer experience when the buyer is a regulated utility whose incentives are set by a Public Utility Commission.
4. They model a single revenue stream (energy arbitrage for a battery, PPA for a solar farm) and ignore the full value stack — leaving money on the table.
5. They ignore the interconnection queue — treating it as an administrative detail when it is the binding constraint on new generation deployment in most markets.
