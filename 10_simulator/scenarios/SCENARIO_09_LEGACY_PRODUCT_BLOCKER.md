# Scenario 09: The $40M Legacy Product Blocking Modernization

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-009 |
| **title** | The $40M Legacy Product Blocking Modernization |
| **leadership_level** | Director, VP Product, CPO |
| **primary_tension** | Profitable legacy vs. platform modernization |
| **key_capability** | Platform strategy, migration, and organizational transformation |
| **estimated_time** | 50 minutes |
| **related_principles** | PRN-0005 (Platform Thinking), PRN-0004 (PMF as Condition), PRN-0008 (Platform Product Management), PRN-0013 (Product Sunset Decisions) |

## Situation

You are the **VP of Product / CPO** at **MediCore**, a healthcare technology company providing electronic health record (EHR) and practice management software to independent physician practices. The company is 25 years old, 1,200 employees, $115M ARR, profitable, privately held. You report to the CEO.

MediCore has two products:

### Legacy: MediCore Classic ($40M ARR, 3,200 customers)

Classic is the original product, built in 1998 as a client-server Windows application. Over 25 years, it has accumulated deep functionality for independent practices — scheduling, billing, clinical documentation, e-prescribing, lab orders, patient portal. It has 3,200 customers, mostly solo practitioners and small practices (1-5 physicians). These customers are loyal — average tenure is 11 years. They know Classic intimately. Many of them built their practices on it.

Classic runs on a discontinued technology stack (Delphi front-end, InterBase database). The 14 engineers who maintain it are all 50+ years old. Two have announced retirement in the next 18 months. The codebase is 2.4 million lines with no automated tests. Every change is manual QA. Deployment is quarterly — customers download an installer from the customer portal.

Classic generates $40M ARR with 85% gross margins. It is the financial engine of the company. It funds everything else.

### Modern: MediCore Cloud ($18M ARR, 900 customers, growing 40% YoY)

Cloud is the modern platform, launched 5 years ago. Web-based, cloud-native, API-first, built on AWS with a modern tech stack (React, Go, PostgreSQL). It has a cleaner UX, mobile access, FHIR-compliant APIs for health system integration, and a marketplace for third-party apps. It was designed to win new customers — larger practices (5-50 physicians) and practice groups that demand interoperability, mobile access, and modern UX.

Cloud is growing 40% year-over-year. Customer satisfaction is high (NPS 58 vs. Classic's NPS 31). The 900 customers on Cloud are the growth engine of the company.

### The Problem

These two products are not integrated. They share no code, no data model, no infrastructure, no design system. They are two separate companies operating under one brand.

This creates escalating problems:

1. **Dual maintenance cost.** You maintain two completely separate engineering organizations — 14 engineers on Classic, 85 engineers on Cloud. The Classic team costs money and adds no strategic value beyond keeping the lights on. Their institutional knowledge is walking out the door as retirement approaches.

2. **No migration path.** Classic customers cannot migrate to Cloud because there is no data migration tool. Their 20+ years of patient records, billing history, and clinical documentation are locked in a proprietary database format. Building a migration tool is estimated at 6-9 person-months of specialized work (someone has to understand the InterBase schema AND the new PostgreSQL schema).

3. **Features must be built twice.** When regulations change (new billing codes, updated clinical quality measures, new privacy requirements), both products need updates. Each regulatory change costs 2-4x what it would cost if there were one platform.

4. **Brand confusion.** Prospects ask "which MediCore are you?" Customers on Classic ask "why isn't my product getting new features?" Customers on Cloud ask "why are you still supporting that old product?"

5. **Talent problem.** You cannot hire engineers who want to work on Delphi and InterBase. The Classic team is literally dying out (retirement, not mortality). In 2-3 years, you will not have the expertise to maintain Classic even if you want to.

6. **Strategic paralysis.** Every strategic decision — enter a new market, build an AI feature, pursue a partnership — runs into the question: "Which product? Classic or Cloud? Both? If both, how?"

### The Customer Problem

You've tried to migrate Classic customers to Cloud. Over the past 3 years:
- You offered a "migration discount" (50% off Cloud for the first year)
- You assigned a dedicated migration support team (3 people)
- You built some migration tooling (manual, labor-intensive, requires a support engineer to run it)

Results: 84 customers migrated (2.6% of Classic base). The most common reasons for NOT migrating:
- "Cloud doesn't have [specific feature] that I use every day." (There are 200+ features in Classic that don't exist in Cloud — most of them edge cases used by 1-3% of customers, but each of them is critical to someone.)
- "I've been using Classic for 18 years. I know where everything is. I don't want to learn a new system."
- "Cloud costs more." (Cloud is priced per-provider-per-month; Classic was a one-time license with annual maintenance. For a solo practitioner, Cloud costs ~$600/month vs. Classic at ~$200/month in maintenance.)
- "The migration process is too hard." (Data migration is manual and error-prone. Some practices have reported data integrity issues after migration.)
- "I'm retiring in 5 years. I don't need a new system."

Meanwhile, prospects are choosing Cloud competitors (Athenahealth, Kareo, DrChrono) over MediCore because the sales process gets complicated: "Well, we have this modern product but also this legacy product, and here's how they're different..."

### The Financial Reality

| | Classic | Cloud | Total |
|---|---------|-------|-------|
| ARR | $40M | $18M | $58M (Note: other products account for remaining $57M to reach $115M) |
| Gross Margin | 85% | 72% | — |
| Engineering Cost | $2.1M/yr | $15.3M/yr | $17.4M |
| Customer Count | 3,200 | 900 | — |
| Churn Rate | 3%/yr | 8%/yr | — |
| Growth Rate | -5%/yr | +40%/yr | — |

Classic is slowly shrinking but still generates ~$34M in annual gross profit. Cloud is growing but still losing money on a fully-loaded basis (engineering + cloud infrastructure + support).

If you turned off Classic tomorrow, you'd lose $40M ARR overnight. The company would not survive. If you do nothing, Classic slowly dies over 5-10 years while draining engineering resources and blocking Cloud's growth. If you force migration, you risk losing the Classic customers who pay the bills.

### The Options

**Option A: Aggressive Migration.** Invest heavily in migration tooling, feature parity, and migration incentives. Goal: migrate 80% of Classic customers to Cloud within 3 years. Cost: $8-12M in engineering and migration support. Risk: customers who can't or won't migrate churn, losing $10-20M ARR.

**Option B: Maintain Both Indefinitely.** Accept that Classic and Cloud are separate businesses. Invest in keeping Classic alive (hire Delphi developers from wherever you can find them, build a Classic maintenance team in a low-cost location). Cloud grows independently. Classic slowly shrinks but continues generating cash. Risk: Classic becomes unmaintainable when the last Delphi developer retires. Cloud is held back by the dual-product overhead.

**Option C: Sell Classic.** Find a private equity firm or a maintenance-mode software company (there are companies that specialize in this) to acquire the Classic business. Use the proceeds to invest in Cloud. Risk: the sale process is distracting, the valuation may be disappointing, and customers may react badly to being "sold."

**Option D: Feature Freeze Classic.** Stop adding features to Classic. Maintain it for security and regulatory compliance only. Invest all new development in Cloud. Classic customers who need new capabilities must migrate. Risk: accelerates Classic churn. May violate regulatory obligations if compliance updates are considered "features."

**Option E: Build a Bridge.** Build a "Classic-on-Cloud" compatibility layer — a version of Classic that runs on the Cloud infrastructure with a Classic-like UX but Cloud's data model and APIs. This is the most ambitious option. Cost: $15-20M, 2-3 years. Risk: it's technically speculative and may fail.

## Characters

**Dr. Robert Chen (CEO).** Physician-founder who wrote the first version of Classic in 1998. Now 62. Has deep loyalty to the Classic customer base — these are the customers who made the company. Emotionally attached to Classic but intellectually knows it's a dead end. Motivated by: legacy, customer loyalty, doing right by the people who built his company, not being the CEO who destroyed the business.

**Maria Santos (CFO).** Joined 3 years ago from a PE-backed healthcare SaaS company. Sees Classic as a cash cow that should be milked, not killed. "Why would we turn off a product generating $34M in gross profit? The math doesn't work." Motivated by: financial performance, EBITDA, not making a bet that destroys $40M in revenue.

**James Okonkwo (VP Engineering for Cloud).** Leads the 85-person Cloud engineering team. Frustrated that his team's velocity is slowed by dual-product overhead (regulatory updates, shared services, context-switching). Wants Classic gone so his team can focus. Has said: "Every hour we spend on Classic compatibility is an hour we don't spend beating Athenahealth." Motivated by: engineering focus, competitive velocity, building something great.

**Linda Park (VP Engineering for Classic).** Has maintained Classic for 17 years. Knows every line of code. Is 58 and planning to retire in 5 years. Loyal to the product and the customers. Worried about what happens to her customers if Classic is shut down. Motivated by: customer care, professional legacy, not seeing her life's work discarded.

**Sarah Williams (VP Customer Success).** Manages relationships with both Classic and Cloud customers. Hears the frustration from both sides. Classic customers feel abandoned. Cloud customers wonder why the company is "distracted." Motivated by: customer satisfaction, retention, not being caught in the middle.

**The Classic Customer Advisory Board (external).** 12 long-tenured Classic customers who advise on the product. They have been vocal that "forcing us to Cloud is a betrayal." Several have said they'll switch to a competitor rather than migrate. They're not bluffing — they switched from paper to Classic in 2000 and they'll switch again if they have to.

## Constraints

- Classic generates $40M ARR. You cannot turn it off without catastrophic financial consequences.
- The Classic engineering team's institutional knowledge is exiting via retirement.
- Classic customers have genuine reasons for not migrating — it's not just inertia.
- The company cannot afford to invest equally in both products.
- Regulatory compliance requires ongoing investment in BOTH products as long as both are live.
- Building feature parity between Classic and Cloud is a multi-year, multi-million-dollar effort.

## Your Role

You are VP of Product / CPO at MediCore. You report to Dr. Chen (CEO). You own the product strategy for both Classic and Cloud. You are accountable for the transition from a two-product company to a one-platform company — or for making the strategic case that a two-product company is sustainable. This is the most consequential decision you will make in this role.

## Response Format

### Part 1: Assumptions

Key areas: What is the actual rate of Classic's decline? How long can Classic be maintained before the engineering talent constraint becomes critical? What features do Classic customers ACTUALLY need vs. what features do they say they need? How many Classic customers would actually churn if you forced migration? What would a PE firm pay for Classic? Can the Cloud platform be adapted to serve solo practitioners at a price point they can afford?

### Part 2: Decision

Describe your strategy with:
- **The strategy.** What is your approach to the Classic-Cloud transition? Which option (or combination) do you choose?
- **The timeline.** Over what time horizon? What are the phases?
- **Resource allocation.** How much investment in Classic maintenance, migration tooling, Cloud feature parity, customer incentives?
- **What you will NOT do.** What options are you explicitly rejecting and why?
- **The customer communication plan.** What do you tell Classic customers? When? How?
- **The organizational communication plan.** What do you tell Linda's team? James's team? The board?

### Part 3: Pre-Mortem

Assume your strategy failed. 3 years from now, Classic is still generating $25M ARR but declining, Cloud is at $35M ARR but growing slower than expected, the dual-product overhead is worse than ever, and the company has lost 2 years of competitive positioning. Write a specific pre-mortem with at least 3 distinct failure paths.

---

## Scoring Rubric (Scenario-Specific)

### Platform Strategy

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes killing Classic or maintaining both without a transition plan. No recognition of the financial, technical, and human dimensions of the problem. |
| 3 | Articulates a clear transition strategy with a timeline and resource plan. Recognizes that you cannot kill Classic overnight but must begin the transition. |
| 4 | Designs a phased transition that accounts for the financial dependency (Classic funds Cloud), the technical constraints (migration tooling must be built), and the customer resistance (incentives must be designed). Each phase has defined success criteria and exit conditions. |
| 5 | Reframes the problem from "how do we migrate Classic customers?" to "how do we build a platform that serves ALL independent practices — from solo practitioners to 50-physician groups — with a sustainable business model?" The answer might be "Cloud with a Classic-priced tier" or "Cloud with a Classic compatibility mode" or "a single platform with modular pricing." The strategy is not about migrating customers — it's about building a platform that makes migration unnecessary because the value proposition solves for everyone. |

### Financial and Resource Allocation

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Ignores the financial math. Proposes spending $20M on migration without addressing who pays for it or what happens to the business if migration fails. |
| 3 | Builds a financial model: how much does the transition cost, how much revenue is at risk, what is the expected ROI, over what time horizon? |
| 4 | Models multiple scenarios: best case (80% migration in 3 years, 10% churn), expected case (50% migration in 5 years, 20% churn), worst case (20% migration, 40% churn, regulatory penalty). Uses scenario planning to identify the irreversible commitments and the decision points. |
| 5 | Designs the transition as a portfolio of financial bets: invest in migration tooling (fixed cost, reduces per-customer migration cost), invest in Classic-compatible Cloud pricing (reduces churn risk), invest in sales/marketing for Cloud (grows the modern business faster to offset Classic decline). Each investment has a defined return expectation and a stop-loss. |

### Customer Empathy and Segmentation

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats Classic customers as a homogeneous group. "They're all resistant to change." |
| 3 | Segments Classic customers: those who will migrate willingly (early adopters), those who will migrate with incentives, those who will only migrate when forced, those who will churn no matter what. Designs different approaches for each segment. |
| 4 | Understands WHY each segment resists. For the retiring solo practitioner, migration is genuinely not worth it — design an end-of-life plan. For the growing practice that needs modern features, migration is urgent — prioritize their migration path. For the practice that uses 3 specific Classic features that Cloud lacks — build those 3 features, not all 200. |
| 5 | Designs the customer journey for each segment over 5 years: the retiree gets a graceful sunset (5 years of maintenance with declining cost), the grower gets a migration white-glove service, the feature-dependent practice gets a commitment to specific feature parity with a timeline. Each segment knows what to expect and when. |

### Organizational Leadership

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats the transition as a technical project. Ignores the human dimension — Linda's team, Dr. Chen's emotional attachment, the Classic customer community. |
| 3 | Recognizes the human dimension and addresses it: Linda's team gets a role in the Cloud transition (their domain expertise is valuable), Dr. Chen's emotional attachment is acknowledged and channeled into a "legacy preservation" narrative, Classic customers are communicated to with respect and a clear value proposition. |
| 4 | Creates a narrative that honors the past while building the future: "Classic built this company. The best way to honor what Classic achieved is to build a platform that serves independent practices for the next 25 years. The Cloud platform is that platform. Classic customers are not being abandoned — they're being invited to the future." |
| 5 | Aligns the organization around the transition as a strategic imperative, not a product decision. The CFO sees the financial logic. The CEO sees the legacy preservation. The Cloud team sees competitive velocity. The Classic team sees a respected role in the transition. The customers see a clear path. The board sees a coherent strategy for sustainable growth. This is organizational leadership, not product management. |

---

## Facilitator Notes

**Common traps:**
1. Underestimating the emotional dimension. Dr. Chen built Classic. Customers have run their practices on it for 20 years. Linda has maintained it for 17 years. This is not just a platform migration — it's an identity transition.
2. Proposing a "big bang" migration — "we'll move everyone to Cloud in 2 years." This ignores the feature parity gap (200+ missing features), the pricing gap (3x cost increase for solo practitioners), and the emotional resistance.
3. Treating Classic as a "bad product" to be "upgraded" from. Classic customers don't think their product is bad. They think it works perfectly for their needs and the "upgrade" is an expensive disruption they didn't ask for.
4. Ignoring the regulatory dimension. HIPAA compliance, clinical quality measures, and billing codes change regularly. Both products need ongoing investment as long as they're live with patient data.

**Discussion prompts:**
- If you were a Classic customer (a solo practitioner, 60 years old, retiring in 5 years), what would you want MediCore to do?
- What is the actual cost of maintaining Classic indefinitely? Is the $34M gross profit worth the engineering cost, the talent problem, the strategic drag, and the brand confusion?
- Is there a version of Cloud that could serve solo practitioners at $200/month? What would you have to cut?
- How would you handle the Classic Customer Advisory Board if they demand that you commit to maintaining Classic "forever"?
- What would you do if Linda (VP Eng, Classic) resigned tomorrow?

**Related Academy Content:**
- [PRN-0005](../../01_core_doctrine/PRINCIPLES.md): Platform thinking
- [PRN-0013](../../01_core_doctrine/PRINCIPLES.md): Product sunset decisions
- [09_tools/PRODUCT_SUNSET_TEMPLATE.md](../../09_tools/PRODUCT_SUNSET_TEMPLATE.md)
- [09_tools/PLATFORM_VS_FEATURE_TEMPLATE.md](../../09_tools/PLATFORM_VS_FEATURE_TEMPLATE.md)
