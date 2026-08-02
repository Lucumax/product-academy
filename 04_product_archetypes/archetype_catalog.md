# Product Archetype Catalog

This catalog describes all 13 product archetypes with their distinctive characteristics, product leadership demands, common failure modes, and industry-specific variations. Use it to understand your current archetype, prepare for transitions, and recognize when you're applying the wrong mental model.

---

## Archetype 1: Consumer / Social

**Examples:** Instagram, TikTok, Duolingo, Strava, Spotify, WhatsApp, Roblox, Calm

### Distinctive Characteristics

- **User is the customer and the user.** No buyer/user split. The person who uses the product is the person who chooses it and (usually) pays for it.
- **Engagement depth matters more than feature breadth.** Consumer products live or die on habit formation, not feature checklists. The quality of the core loop determines everything.
- **Taste and craft are competitive moats.** In crowded consumer markets, the intangible qualities of the product — how it feels, how delightful it is, how coherent the experience — are often the only durable differentiation.
- **Distribution is a product problem.** Growth mechanics (viral loops, network invites, content-driven acquisition) are product features, not marketing activities.
- **Monetization is often indirect.** Ad-supported, freemium, subscription, or hybrid models. The relationship between engagement and revenue is complex and often nonlinear.
- **Data scale enables personalization.** Consumer products generate behavioral data at scale that enables recommendation, personalization, and optimization — but also creates privacy and ethical considerations.

### Product Leadership Demands

- **Product judgment and taste** (Capability 1.4): Paramount. Consumer products succeed or fail on the quality of micro-decisions about interaction design, visual polish, and experience coherence.
- **Data and evaluation fluency** (Capability 1.6): Heavy experimentation culture. Must design metrics that distinguish engagement from addiction, growth from spam.
- **Customer and domain understanding** (Capability 1.3): Requires behavioral psychology sophistication. Must understand user motivations, habits, and social dynamics at a level beyond what users can articulate.
- **Risk judgment** (Capability 1.8): Content moderation, privacy, addiction, and societal impact risks are salient. Consumer products can cause harm at scale.
- **Adoption architecture**: Onboarding, first-use experience, habit formation mechanics, and re-engagement triggers are core product capabilities.

### Common Failure Modes

1. **Optimizing for engagement at the expense of user well-being.** The engagement trap: what drives metrics may harm users. Eventually the users notice, or regulators do.
2. **Feature creep destroying simplicity.** Consumer products start simple and accumulate features. Each feature adds cognitive load. The accumulated complexity eventually kills the experience.
3. **Growth hacking without product value.** Driving acquisition before the product delivers real value. Users arrive and leave. The growth numbers look good for a quarter, then collapse.
4. **Monetization that degrades the experience.** Ads that feel intrusive. Paywalls that feel arbitrary. Monetization mechanics that create perverse incentives for users.
5. **Misreading cultural context.** Consumer products exist in cultural context. What works in one market or demographic may fail or offend in another. Global consumer products require cultural fluency.
6. **Confusing A/B test wins with product improvement.** Optimizing a local metric through testing while degrading the holistic experience. The product becomes a Frankenstein of locally optimized parts.

### Industry-Specific Variations

- **Social media:** Network effects and content moderation are dominant dynamics. Platform responsibility and societal impact are board-level concerns.
- **Health and fitness:** Habit formation and behavior change are the product. Retention is the hardest problem.
- **Music and audio:** Licensing, creator economics, and recommendation quality are central.
- **Dating:** Trust and safety, identity verification, and the paradox of success (users who succeed leave).
- **News and information:** Content quality, misinformation risk, and the tension between engagement and accuracy.
- **Education-adjacent consumer:** Must balance engagement with learning outcomes. Gamification that doesn't produce learning is entertainment, not education.

---

## Archetype 2: Enterprise / B2B SaaS

**Examples:** Salesforce, Workday, ServiceNow, Slack, Notion, Figma (enterprise), Datadog

### Distinctive Characteristics

- **Buyer/user split.** The person who buys (economic buyer, procurement, IT) is often not the person who uses. Both must be served, and their needs frequently conflict.
- **Multi-stakeholder complexity.** Enterprise products must serve end users, administrators, IT/security teams, procurement, and executives — each with different needs and evaluation criteria.
- **Adoption is a product discipline.** Enterprise adoption requires organizational change management, training, migration from legacy systems, and administrator tooling. These are product features, not sales activities.
- **Sales partnership is structural, not optional.** Product and sales must work as partners. Product that ignores sales constraints ships features no one buys. Sales that ignores product constraints sells features that don't exist.
- **Security, compliance, and reliability are table stakes.** Enterprise buyers evaluate products on criteria that consumer users never consider: SOC 2, GDPR, SSO, RBAC, audit logs, uptime SLAs.
- **Revenue is multi-dimensional.** Land-and-expand, seat-based pricing, usage-based pricing, platform fees. Revenue growth comes from acquisition, expansion, and retention — all requiring product support.

### Product Leadership Demands

- **Cross-functional influence** (Capability 2.2): Must partner deeply with sales, customer success, marketing, and professional services. The PM who can't work with sales will be bypassed.
- **Adoption and change management** (Capability 3.1): Central. Enterprise products that aren't adopted haven't succeeded, regardless of feature quality.
- **Business economics** (Capability 1.7): Pricing, packaging, and monetization strategy are strategic weapons. Must understand CAC, LTV, churn, expansion revenue, and the economics of different customer segments.
- **Risk judgment** (Capability 1.8): Security incidents, data breaches, and compliance failures are existential risks. Must balance feature velocity against enterprise-grade reliability.
- **Customer and domain understanding** (Capability 1.3): Must understand the customer's organizational context — their workflows, their compliance requirements, their procurement processes, their political dynamics.

### Common Failure Modes

1. **Building for the buyer, ignoring the user.** Products that win RFPs but fail in daily use. The procurement checklist is satisfied; the user experience is miserable.
2. **Building for the user, ignoring the buyer.** Products that users love but can't get past security review or procurement. Beautiful product, zero revenue.
3. **Sales-driven roadmap.** Building whatever the largest customer or the most vocal salesperson demands. The product becomes a collection of custom features with no coherent strategy.
4. **Product-driven roadmap that ignores sales reality.** Building what's strategically elegant while ignoring the features that actually close deals. The strategy is beautiful; the company misses its numbers.
5. **Enterprise "consumerization" cargo cult.** Applying consumer product practices (move fast, ship often, minimal process) without understanding why enterprise products have more process. Enterprise customers can't tolerate breaking changes.
6. **Customization death spiral.** Building custom features for individual customers until the product is unmaintainable and the engineering team is burned out.
7. **Pricing that leaves money on the table or kills adoption.** Underpricing erodes margins; overpricing blocks adoption. The right price captures value without preventing growth.

### Industry-Specific Variations

- **Horizontal SaaS (CRM, collaboration, productivity):** Broad applicability, more consumer-like UX expectations, competitive differentiation through ecosystem and integrations.
- **Vertical SaaS (healthcare, legal, construction):** Deep domain expertise required. Generalist PM skills are insufficient. The market is smaller but defensibility is higher.
- **SMB SaaS:** Self-serve adoption, product-led growth, lower price points, higher volume. More consumer-like in acquisition; still enterprise in retention.
- **Mid-market SaaS:** Hybrid sales and product-led motions. The hardest segment to design for because both self-serve and sales-assisted paths must work.
- **Enterprise (F500):** Long sales cycles, complex procurement, extensive security reviews, high-touch implementation. The product is only part of what's being sold.

---

## Archetype 3: Platform / Infrastructure

**Examples:** AWS, Stripe, Twilio, Shopify (platform), internal developer platforms, API products

### Distinctive Characteristics

- **Customers are developers or internal teams.** The user is technically sophisticated. They evaluate the product on API design, documentation quality, reliability, and performance — not visual polish.
- **Value is indirect.** Platform products create value by enabling other products. Measuring platform value requires understanding the products built on top of it.
- **Adoption has a long time constant.** Platforms take years to achieve widespread adoption. The investment profile is fundamentally different from consumer or enterprise products.
- **Build-vs-buy is a constant tension.** Every platform capability could be built in-house by potential consumers. The platform must be sufficiently better than what teams could build themselves to justify adoption.
- **Breaking changes are expensive.** Once adopted, platform APIs and behaviors become contracts. Changing them breaks dependent systems. Migration is always harder than expected.
- **The "platform tax" problem.** How is the platform funded? Internal platforms that charge back to teams create perverse incentives. External platforms that raise prices trigger build-vs-buy reevaluation.

### Product Leadership Demands

- **Technical fluency** (Capability 1.5): Highest technical fluency requirement of any archetype. Must understand distributed systems, API design, scalability, reliability engineering.
- **Strategic sequencing** (Capability 2.1): Critical. Building platform capabilities before teams are ready to consume them is wasted investment. Building them too late creates technical debt and migration costs.
- **Organizational multiplication** (Capability 3.2): Platform success is measured by the success of the products built on it. This requires sophisticated proxy metrics and organizational influence.
- **Product judgment** (Capability 1.4): API design, documentation quality, consistency of mental models — these are taste dimensions that are invisible to non-technical stakeholders.
- **Adoption and change management** (Capability 3.1): Internal platform adoption requires developer relations, migration support, and documentation — all product capabilities.

### Common Failure Modes

1. **Building the platform before the use case.** "If we build it, they will come." They won't. Platforms that aren't extracted from real, proven use cases are solutions in search of problems.
2. **Over-generalizing too early.** Building for hypothetical future use cases instead of concrete current ones. The platform becomes a beautiful, abstract, unused edifice.
3. **Under-generalizing (one-off platform features).** Building capabilities that only serve one team's specific use case. The platform becomes a collection of point solutions with a shared brand.
4. **Ignoring the adoption experience.** Building powerful capabilities with unusable interfaces, incomplete documentation, or painful migration paths. Technical excellence doesn't matter if no one can use it.
5. **The platform team as bottleneck.** Every team must go through the platform team for everything. The platform that was supposed to accelerate development slows it down.
6. **Competing with internal customers.** The platform team builds end-user features instead of platform capabilities because end-user features are more visible and rewarding.
7. **Funding model failure.** The platform is underfunded because it's seen as overhead, or it's overfunded because it's politically favored. Neither produces the right investment level.

### Industry-Specific Variations

- **Internal platforms:** Adoption is mandated or incentivized, not voluntary. Funding model and governance are the hardest problems. The platform team's relationship with product teams is the critical dynamic.
- **External API platforms (Stripe, Twilio):** Developer experience is the product. Documentation, SDKs, sandboxes, and community are strategic investments, not support functions.
- **Cloud infrastructure (AWS, GCP, Azure):** Scale economics, reliability at unprecedented levels, and the "undifferentiated heavy lifting" value proposition. Competition is brutal.
- **Platform-as-a-service (Heroku, Vercel, Render):** Abstraction level is the key design decision. Too much abstraction limits power users; too little fails to deliver platform value.
- **E-commerce platforms (Shopify, BigCommerce):** The platform serves merchants whose success determines platform success. Ecosystem of apps and partners is critical.

---

## Archetype 4: Marketplace / Network

**Examples:** Uber, Airbnb, eBay, Steam, Upwork, Etsy, DoorDash, Thumbtack

### Distinctive Characteristics

- **Two-sided (or multi-sided) dynamics.** The product must create value for at least two distinct user groups simultaneously. Changes that benefit one side often harm the other.
- **Liquidity is the fundamental metric.** A marketplace without sufficient supply doesn't attract demand. Without sufficient demand, supply leaves. The "cold start" problem is the hardest in product management.
- **Network effects are the primary moat.** The value of the marketplace increases with participation. This creates winner-take-most dynamics and makes market entry extremely difficult — if you can achieve liquidity.
- **Trust and safety are existential.** Marketplaces intermediate between strangers. Fraud, safety incidents, and quality problems can destroy trust and collapse the marketplace.
- **Take rate and subsidy are strategic levers.** The marketplace's revenue model (take rate) and investment in growth (subsidy to one or both sides) must be managed dynamically as the marketplace matures.
- **Disintermediation risk.** Once supply and demand connect, they may transact outside the marketplace. The product must provide ongoing value that justifies the take rate.

### Product Leadership Demands

- **Business economics** (Capability 1.7): Marketplace economics are complex — cross-side effects, liquidity thresholds, take rate optimization, subsidy strategy. Requires economic thinking, not just product thinking.
- **Data and evaluation fluency** (Capability 1.6): Marketplace experiments are harder because changes to one side affect the other, often with delays. Causal inference in two-sided systems is challenging.
- **Risk judgment** (Capability 1.8): Trust and safety, regulatory risk (especially for labor marketplaces), and competitive dynamics (network effects create winner-take-most markets).
- **Portfolio allocation** (Capability 1.9): Must balance supply-side and demand-side investments. The optimal mix changes with marketplace maturity. Optimizing each side independently produces bad outcomes.
- **Strategic sequencing** (Capability 2.1): Liquidity must be achieved market by market, category by category. Premature scaling is destructive.

### Common Failure Modes

1. **Chicken-and-egg paralysis.** Waiting for supply before attracting demand, and demand before attracting supply. Marketplaces must be hacked into existence — often through deliberate subsidy, single-player mode, or piggybacking on existing networks.
2. **Premature scaling.** Expanding to new geographies or categories before achieving liquidity in the core. The marketplace collapses everywhere instead of succeeding somewhere.
3. **Over-optimizing one side.** Making supply so happy that demand suffers (or vice versa). The optimal marketplace is slightly uncomfortable for both sides — each needs the other more than they'd prefer.
4. **Losing trust.** Safety incidents, fraud, or quality problems that erode user trust. Once lost, marketplace trust is extraordinarily hard to regain.
5. **Commoditization of supply.** When the marketplace makes supply interchangeable, suppliers lose loyalty. They'll go wherever they can get demand. The marketplace must provide value beyond access to demand.
6. **Ignoring the "after the transaction" experience.** Marketplaces that optimize for transaction completion but neglect what happens after (disputes, returns, quality problems, repeat usage).
7. **Regulatory blindness.** Labor marketplaces that ignore employment law. Housing marketplaces that ignore discrimination law. Financial marketplaces that ignore securities law.

### Industry-Specific Variations

- **Ride-sharing / delivery:** Real-time matching, geographic density, surge pricing dynamics. Supply is labor; regulatory risk is extreme.
- **Accommodation / experiences:** Trust and safety are paramount. Quality verification is hard. Supply is heterogeneous and non-fungible.
- **Freelance / labor marketplaces:** Matching quality determines marketplace value. Payment and dispute resolution are critical. Regulatory risk around worker classification.
- **E-commerce marketplaces (eBay, Etsy, Amazon Marketplace):** Search and discovery at scale. Counterfeit and fraud risk. Seller tools and analytics are competitive differentiators.
- **Dating / social marketplaces:** Women are the scarce resource. Men generate revenue. The gender dynamics create unique product challenges.
- **B2B marketplaces:** Higher transaction values, longer sales cycles, more complex matching. Trust and verification are even more critical.

---

## Archetype 5: AI / ML Products

**Examples:** ChatGPT, Midjourney, GitHub Copilot, Claude, Runway, character.ai, ML platforms

### Distinctive Characteristics

- **Model capability uncertainty.** Unlike deterministic software, AI models have probabilistic behavior, unpredictable failure modes, and capabilities that are discovered rather than specified. "Does it work?" is a harder question.
- **Data flywheels.** The most durable AI products have mechanisms by which usage improves the product — more data, better models, better products, more usage. Flywheels must be designed, not assumed.
- **Evaluation is a first-class product problem.** How do you know if the model is good enough? Offline metrics, online metrics, human evaluation, red-teaming — evaluation is complex and contested.
- **Safety and responsibility are product requirements.** AI products can cause harm in novel ways — bias amplification, hallucination, misuse, job displacement. Safety is not a compliance checkbox; it's a product design discipline.
- **Cost structure is different.** Inference costs, training costs, and model serving infrastructure create unit economics that are unlike traditional software. Margins may be lower than expected.
- **Pace of change is extreme.** The underlying technology is improving rapidly. What was impossible six months ago may be trivial today. Product roadmaps must account for capability jumps.

### Product Leadership Demands

- **Technical fluency** (Capability 1.5): Must understand model capabilities, limitations, and failure modes at a level that enables product judgment — not research-level depth, but enough to distinguish real capabilities from demo-ware.
- **Risk judgment** (Capability 1.8): AI-specific risks (bias, safety, hallucination, misuse, regulatory) are novel, evolving, and potentially existential for the product.
- **Data and evaluation fluency** (Capability 1.6): AI evaluation is uniquely challenging. Must design evaluation approaches that account for distribution shift, feedback loops, and the gap between proxy metrics and real outcomes.
- **Product judgment** (Capability 1.4): Must make product decisions under unprecedented uncertainty about what the technology can and cannot do. Must distinguish "we can't do this yet" from "this will never work" from "this works but shouldn't be shipped."
- **Business economics** (Capability 1.7): AI unit economics are evolving. Model costs, inference costs, and pricing strategy must be actively managed.

### Common Failure Modes

1. **Shipping a model, not a product.** The model is impressive. The product experience around it (onboarding, error handling, integration into workflow, trust-building) is missing. Users try it once, are impressed, and never return.
2. **Over-indexing on model quality.** Assuming that better benchmarks = better product. Users don't care about your BLEU score. They care about whether the product solves their problem reliably.
3. **Under-investing in evaluation.** Shipping AI features without robust evaluation. Users discover failures in production. Trust erodes and is hard to rebuild.
4. **Ignoring the "last mile" problem.** AI provides a capability, but turning that capability into a product that users adopt requires all the normal product work — which AI-obsessed teams often neglect.
5. **Prompt engineering as product strategy.** Treating prompt improvements as the primary product development activity. Prompts are fragile, hard to evaluate, and not a moat.
6. **Safety as afterthought.** Adding safety guardrails after incidents occur. By then, trust is damaged and regulatory scrutiny has begun.
7. **Building on a model that becomes commoditized.** If your product's only differentiation is the model it uses, and that model is available to everyone, you have no differentiation.

### Industry-Specific Variations

- **Foundation model providers (OpenAI, Anthropic, Google):** The hardest product and business problems. Must balance research progress against product reliability. Pricing and safety are strategic decisions with industry-wide implications.
- **AI-native applications (ChatGPT, Midjourney, Copilot):** Product experience is the differentiation. Must design for model uncertainty, build trust, and create workflows that incorporate AI naturally.
- **AI-enabled features in existing products:** Adding AI to non-AI products. Must decide which features should use AI and which shouldn't. The risk of over-use (AI for everything) is real.
- **ML platforms and tools:** Serving data scientists and ML engineers. Developer experience, model lifecycle management, and MLOps are the product capabilities.
- **AI in regulated industries (healthcare, finance, legal):** Regulatory constraints on AI use create additional requirements. Explainability, fairness, and human-in-the-loop may be non-negotiable.

---

## Archetype 6: Developer Tools

**Examples:** GitHub, GitLab, VS Code, Docker, Postman, Vercel, Stripe (API), Twilio (API)

### Distinctive Characteristics

- **Users are developers.** They are technically sophisticated, opinionated, and skeptical. They evaluate products on technical merit, not marketing. They will read your documentation, inspect your API, and benchmark your performance.
- **Documentation is the product.** For developer tools, documentation quality is as important as feature quality. Bad documentation means the product doesn't exist for most potential users.
- **Developer experience (DX) is the UX.** API design, SDK ergonomics, CLI usability, error message quality, getting-started time — these are the experience dimensions that matter.
- **Open source dynamics.** Many developer tools are built on or compete with open source. Open source strategy — what to open, what to keep proprietary, how to build community — is a product strategy question.
- **Adoption is bottom-up.** Developers adopt tools individually or in teams, often without organizational approval. The product must win individual developers before it can win the organization.
- **Community is a product asset.** Developer communities (forums, GitHub, Stack Overflow, Discord) provide support, advocacy, and product feedback. Community health is a product metric.

### Product Leadership Demands

- **Technical fluency** (Capability 1.5): Very high. Must be able to use the product as a developer would, understand API design tradeoffs, and earn credibility with a highly technical user base.
- **Product judgment** (Capability 1.4): API design elegance, consistency of mental models, and "principle of least surprise" are taste dimensions that non-developers cannot evaluate.
- **Customer and domain understanding** (Capability 1.3): Must understand developer workflows deeply. Dogfooding is not optional — you must use the product in real development work.
- **Adoption architecture**: Developer adoption follows a distinct pattern: discover, evaluate (often via open source or free tier), adopt individually, expand within team, standardize organizationally. Each stage requires different product capabilities.
- **Business economics** (Capability 1.7): Developer tool monetization is tricky. Open source alternatives create price pressure. Free tiers must be generous enough for adoption but limited enough to drive revenue.

### Common Failure Modes

1. **Bad documentation.** The product is powerful but unusable because documentation is incomplete, outdated, or incomprehensible. This is the most common and most fatal developer tool failure.
2. **API inconsistency.** The API has different patterns, naming conventions, and behaviors across endpoints. Developers must learn each endpoint individually rather than applying a consistent mental model.
3. **Ignoring the getting-started experience.** The time from "I want to try this" to "I've done something useful" is the most important metric. Products that take hours to set up lose developers before they experience value.
4. **Over-monetizing too early.** Charging before the product has demonstrated value. Developers try the product, hit a paywall, and leave — often permanently.
5. **Building for the wrong abstraction level.** Too high-level, and power users are constrained. Too low-level, and it's not worth adopting over building in-house. Finding the right abstraction is the central design challenge.
6. **Open source community neglect.** Treating open source as a marketing channel rather than a community to nurture. Developers can tell the difference.
7. **Enterprise sales motion applied to developer adoption.** Top-down enterprise sales don't work for developer tools. Developers must want to use the product first; enterprise deals follow.

### Industry-Specific Variations

- **IDEs and editors (VS Code, JetBrains):** Extension ecosystems are critical. Performance and responsiveness are non-negotiable. Switching costs are high.
- **API products (Stripe, Twilio):** API design is the product. SDKs in multiple languages. Sandbox environments for testing. Reliability is paramount.
- **Infrastructure-as-code (Terraform, Pulumi):** Declarative configuration. State management. Provider ecosystems.
- **CI/CD and DevOps (GitHub Actions, CircleCI):** Configuration complexity is the primary pain point. Speed and reliability of execution.
- **Observability and monitoring (Datadog, Sentry):** Data volume and cost management. Alert quality vs. alert fatigue.
- **Databases and data tools (MongoDB, Snowflake):** Performance, scalability, and query languages. Developer experience in data tools is often neglected.

---

## Archetype 7: Hardware / Physical Products

**Examples:** iPhone, Tesla vehicles, Oculus, Peloton, Sonos, Nest, Ring, DJI drones

### Distinctive Characteristics

- **Irreversibility of decisions.** Hardware decisions cannot be updated over-the-air. A design flaw, component choice, or manufacturing process decision made today will be in customers' hands for years.
- **Long development cycles.** Hardware development timelines are measured in months or years, not weeks. The feedback loop between decision and customer response is orders of magnitude slower than software.
- **Manufacturing and supply chain are product constraints.** Tooling costs, component availability, manufacturing yields, and supply chain logistics shape what's possible. These constraints are unfamiliar to software-native PMs.
- **Systems integration complexity.** Hardware products involve electrical engineering, mechanical engineering, firmware, software, and industrial design. Coordination across these disciplines is the central product management challenge.
- **Quality and reliability are existential.** A software bug can be patched. A hardware defect requires recall, repair, or replacement — at massive cost to both the company and customer trust.
- **Software is a differentiator, not an afterthought.** Modern hardware products are increasingly defined by their software experience. The hardware enables; the software delivers the experience.

### Product Leadership Demands

- **Strategic sequencing** (Capability 2.1): Hardware development timelines make sequencing critical. Decisions made early constrain options later. The cost of a sequencing error is measured in years and millions.
- **Risk judgment** (Capability 1.8): Hardware risk is different — more binary, more irreversible, more expensive. Must evaluate technical risk, manufacturing risk, supply chain risk, and market timing risk simultaneously.
- **Cross-functional influence** (Capability 2.2): Must coordinate across engineering disciplines (EE, ME, FW, SW), industrial design, manufacturing, supply chain, quality, and regulatory — functions with different cadences, cultures, and constraints.
- **Business economics** (Capability 1.7): Gross margin is dominated by BOM (bill of materials) cost, manufacturing cost, and warranty cost. Pricing must account for these in ways software pricing doesn't.
- **Product judgment** (Capability 1.4): Hardware taste involves industrial design, materials, haptics, and physical interaction design — dimensions unfamiliar to software PMs.

### Common Failure Modes

1. **Software PMs applying software logic to hardware.** Optimizing for iteration speed in a domain where iteration is slow and expensive. Making commitments before understanding irreversibility.
2. **Hardware PMs ignoring software.** Treating software as a checklist item rather than the primary experience differentiator. The hardware is beautiful; the companion app is terrible.
3. **Feature creep during development.** Adding features after tooling has begun. Each addition costs months and millions. The product arrives late, over budget, and with compromised quality.
4. **Supply chain optimism.** Assuming components will be available, yields will be high, and manufacturing will go smoothly. Supply chain surprises are the norm, not the exception.
5. **Inadequate testing.** Testing hardware is harder than testing software. Environmental testing, reliability testing, safety testing, regulatory testing — skipping or shortcutting any of these creates catastrophic risk.
6. **Over-investing in hardware, under-investing in ecosystem.** The hardware is great but the accessories, services, and developer ecosystem that create lock-in are missing.
7. **Pricing that doesn't account for channel margins.** Hardware sold through retail channels loses 30–50% to channel margin. Consumer hardware pricing must account for this.

### Industry-Specific Variations

- **Consumer electronics:** Mass-market pricing, retail distribution, brand and marketing importance. Annual release cycles create intense pressure.
- **Automotive:** Extreme safety and reliability requirements. 5–7 year development cycles. Regulatory complexity across jurisdictions.
- **Medical devices:** Regulatory approval (FDA, CE) dominates development timelines. Clinical validation required. Post-market surveillance obligations.
- **IoT and smart home:** Connectivity reliability, interoperability standards, and security (IoT security is notoriously poor) are product requirements.
- **Robotics and drones:** Mechatronics complexity. Safety systems are non-optional. Regulatory frameworks are evolving.
- **Wearables:** Miniaturization constraints. Battery life is the dominant design constraint. Comfort and fashion are product requirements.

---

## Archetype 8: Fintech / Financial Services

**Examples:** Stripe, Robinhood, Plaid, Wise, Chime, Ramp, Coinbase, Affirm

### Distinctive Characteristics

- **Trust is the foundation.** Financial products handle people's money. Trust is earned slowly and lost instantly. Every product decision must consider its effect on trust.
- **Regulatory constraints are pervasive.** Financial services are among the most heavily regulated industries. Compliance is not a separate function — it's a product requirement that shapes what can and cannot be built.
- **Transaction integrity is non-negotiable.** Money must move correctly, every time. "Eventually consistent" is not acceptable for financial transactions. The engineering standards are higher.
- **Fraud and security are existential threats.** Financial products are high-value targets. Fraud prevention, security, and identity verification are core product capabilities, not add-ons.
- **Complex stakeholder landscape.** Regulators, banking partners, payment networks, compliance officers, risk managers — in addition to the normal product stakeholders.
- **Revenue is often indirect or complex.** Interchange fees, float income, subscription fees, transaction fees, spreads. The business model may not be obvious to users.

### Product Leadership Demands

- **Risk judgment** (Capability 1.8): Financial risk, fraud risk, regulatory risk, reputational risk — all must be evaluated at a level of sophistication beyond other archetypes.
- **Technical fluency** (Capability 1.5): Transaction processing, reconciliation, idempotency, ledger systems — these are technical concepts that PMs must understand to make product decisions.
- **Business economics** (Capability 1.7): Fintech unit economics involve interchange, processing costs, fraud costs, capital costs, and regulatory costs. The economic model is complex.
- **Customer and domain understanding** (Capability 1.3): Financial behavior, financial anxiety, and financial literacy vary dramatically across segments. Empathy for users who are stressed about money is essential.
- **Cross-functional influence** (Capability 2.2): Must partner with compliance, legal, risk, and finance functions that have veto power over product decisions.

### Common Failure Modes

1. **"Move fast and break things" in finance.** Applying consumer software velocity to financial products. Breaking things in finance means losing people's money, violating regulations, or enabling fraud.
2. **Compliance as afterthought.** Building the product first, then asking legal and compliance to approve it. They won't. The product must be redesigned, often from scratch.
3. **Ignoring the edge cases.** Happy-path financial transactions are easy. It's the edge cases — disputes, chargebacks, fraud, reconciliation breaks, regulatory inquiries — that consume engineering resources and destroy trust.
4. **Underestimating fraud.** Every financial product that gains traction will be targeted by fraudsters. Fraud prevention must be designed in from day one, not added after losses occur.
5. **Regulatory arbitrage as strategy.** Building products that exploit regulatory gaps. Regulators eventually close the gaps. The product and the company may not survive.
6. **Opaque pricing and fees.** Hidden fees that users discover later. Trust is destroyed. In financial products, transparency is a competitive advantage, not a compliance obligation.
7. **Crypto/web3-specific:** Ignoring securities law. Poor key management. Smart contract vulnerabilities. "Code is law" philosophy that ignores real-world harm.

### Industry-Specific Variations

- **Payments (Stripe, Adyen, Square):** Reliability and latency are paramount. Payment network relationships are strategic assets. Fraud and dispute management at scale.
- **Consumer banking (Chime, Monzo, Revolut):** User experience is the differentiator over incumbent banks. Trust and deposit insurance perception matter enormously.
- **Investing and trading (Robinhood, Public, Wealthfront):** Behavioral design has ethical dimensions. Gamification that encourages harmful trading behavior is a real risk. Market structure understanding required.
- **Lending and credit (Affirm, Klarna, Upstart):** Underwriting and credit risk are core competencies. Fair lending regulations. The social impact of lending decisions.
- **Insurtech (Lemonade, Root):** Actuarial science meets product management. Claims experience determines customer satisfaction. Regulatory framework varies by state and country.
- **Crypto and DeFi:** Extreme volatility. Regulatory uncertainty. Security is the product. User experience for self-custody is a hard, unsolved problem.

---

## Archetype 9: Healthcare / Healthtech

**Examples:** Epic, Oscar Health, Omada Health, Tempus, Zocdoc, 23andMe, Ro

### Distinctive Characteristics

- **Patient safety is the ultimate constraint.** Healthcare products can harm or kill people. Safety is not a feature — it's a non-negotiable requirement that shapes every product decision.
- **Multi-stakeholder complexity on steroids.** Healthcare involves patients, providers, payers (insurers), employers, regulators, and pharmaceutical companies — each with different, often conflicting incentives.
- **Regulatory pathways are long and expensive.** FDA clearance/approval, HIPAA compliance, GDPR, state-level regulations. Regulatory strategy is a product strategy decision.
- **Clinical evidence requirements.** Healthcare products (especially those making clinical claims) require evidence of safety and efficacy. RCTs, real-world evidence, clinical validation — these are part of product development.
- **Reimbursement determines viability.** In the US healthcare system, products must be reimbursable by payers (insurance, Medicare/Medicaid) to be commercially viable. Reimbursement strategy is as important as product strategy.
- **Interoperability is a product requirement.** Healthcare data must flow between systems (EHRs, labs, pharmacies, payers). HL7, FHIR, and other standards are not optional.

### Product Leadership Demands

- **Risk judgment** (Capability 1.8): Patient safety risk, clinical risk, regulatory risk, data privacy risk. The consequences of being wrong are measured in human harm, not just business metrics.
- **Customer and domain understanding** (Capability 1.3): Healthcare domain expertise is not optional. Generalist PMs without healthcare experience will make dangerous mistakes.
- **Cross-functional influence** (Capability 2.2): Must partner with clinical, regulatory, legal, compliance, and medical affairs functions that have legitimate veto power.
- **Data and evaluation fluency** (Capability 1.6): Clinical evaluation methodologies (RCTs, observational studies, real-world evidence) are different from consumer product experimentation. Statistical significance has different meaning.
- **Adoption and change management** (Capability 3.1): Healthcare adoption involves clinical workflow integration, training, and often institutional policy changes. Adoption timelines are measured in months or years.

### Common Failure Modes

1. **Consumer tech PMs applying consumer logic to healthcare.** "Move fast, validate with A/B tests, iterate based on engagement metrics." In healthcare, some things can't be A/B tested because the downside risk is patient harm.
2. **Ignoring clinical workflow.** Building products that are medically sound but don't fit into how clinicians actually work. Clinicians won't use products that slow them down or add administrative burden.
3. **Underestimating regulatory requirements.** Treating FDA clearance as a checklist item rather than a development framework. The FDA process shapes product requirements; ignoring it until late in development means expensive rework.
4. **Building for the wrong stakeholder.** Optimizing for patients when payers make the purchasing decision. Optimizing for providers when patients choose the product. Healthcare stakeholder analysis is essential.
5. **Data silo naivety.** Assuming healthcare data will be available, clean, and interoperable. It won't. Healthcare data integration is a major engineering and business development challenge.
6. **Ignoring health equity.** Building products that work for affluent, tech-savvy, English-speaking populations while failing to serve others. Healthcare disparities are a product design problem.
7. **AI-specific:** Clinical AI without rigorous validation. Models that perform well in research but fail in clinical settings due to distribution shift. Algorithmic bias in healthcare AI has life-or-death consequences.

### Industry-Specific Variations

- **Provider-facing (EHRs, clinical decision support):** Clinical workflow integration is everything. Clinician burnout and administrative burden are the problems to solve. Epic and Cerner dominate; interoperability with them is non-optional.
- **Patient-facing (telehealth, digital therapeutics, wellness):** Engagement and behavior change are central. Clinical validation separates real products from wellness fads. Reimbursement is the commercial hurdle.
- **Payer-facing (care management, claims, analytics):** Cost reduction and quality improvement are the value propositions. Data integration from multiple sources is the engineering challenge.
- **Pharma and life sciences:** Drug development is the core business. Product management serves clinical trials, real-world evidence, and commercial operations. Scientific expertise requirements are extreme.
- **Digital therapeutics (prescription digital products):** FDA clearance as a medical device. Clinical trial evidence required. Reimbursement through pharmacy benefits. This is essentially a pharmaceutical product development model.

---

## Archetype 10: Edtech / Education

**Examples:** Coursera, Duolingo, Khan Academy, Canvas, Udemy, Quizlet, MasterClass

### Distinctive Characteristics

- **Learning outcomes are the ultimate metric — and the hardest to measure.** Engagement is easy to measure. Learning is hard. Products that optimize for engagement may not produce learning.
- **Pedagogy matters.** Educational products must be built on sound learning science, not just good UX. Gamification without pedagogy is entertainment, not education.
- **Institutional adoption is a long cycle.** Selling to schools, universities, and districts involves procurement, pilot programs, committee approvals, and academic calendars. Sales cycles of 12–24 months are common.
- **Multiple user types with different needs.** Students, teachers, administrators, parents, and employers all interact with educational products — each with different goals and evaluation criteria.
- **Content is a core product asset.** The quality, accuracy, and pedagogical design of content determines educational effectiveness. Content strategy is a product strategy.
- **Accessibility and equity are non-negotiable.** Educational products must serve diverse learners, including those with disabilities. Accessibility is a legal requirement and a moral imperative.

### Product Leadership Demands

- **Data and evaluation fluency** (Capability 1.6): Measuring learning outcomes is intrinsically difficult — long time horizons, confounding factors, ethical constraints on experimentation with students.
- **Customer and domain understanding** (Capability 1.3): Must understand learning science, pedagogical approaches, and the institutional context of education. Generalist PMs need significant domain development.
- **Product judgment** (Capability 1.4): Balancing engagement and learning outcomes. Making learning feel effortless is not the same as making it effective. Desirable difficulty is a product design principle.
- **Adoption and change management** (Capability 3.1): Institutional adoption requires teacher training, curriculum integration, and administrative buy-in. The product is only part of what's being adopted.
- **Risk judgment** (Capability 1.8): Student data privacy (FERPA, COPPA), content accuracy, and the risk of products that don't actually produce learning.

### Common Failure Modes

1. **Optimizing for engagement at the expense of learning.** Making a product that students love but doesn't teach them anything. The Edtech unicorn graveyard is full of engaging products with zero learning efficacy.
2. **Building for students, ignoring teachers.** Products that bypass teachers rather than empowering them. Teachers are gatekeepers to classroom adoption. Alienating them guarantees failure.
3. **Ignoring the academic calendar.** Launching products in November and wondering why schools aren't adopting. School purchasing happens on an annual cycle, typically in spring for the following fall.
4. **Content as an afterthought.** Building a platform and expecting content to materialize. Content quality determines educational effectiveness. Content strategy must be part of product strategy from day one.
5. **Underestimating institutional sales complexity.** Assuming schools will adopt products like consumers adopt apps. They won't. Institutional edtech is enterprise sales with additional complexity (committees, pilots, grants, procurement rules).
6. **Accessibility neglect.** Products that aren't accessible to students with disabilities. This is a legal violation, a moral failure, and a product design deficiency.
7. **One-size-fits-all approach.** Assuming all learners are the same. Adaptive learning, differentiated instruction, and accommodations for diverse learners are product requirements.

### Industry-Specific Variations

- **K-12:** District-level purchasing. Teacher adoption is critical but teachers don't control budgets. Alignment with state standards (Common Core, etc.). FERPA/COPPA compliance. Accessibility requirements.
- **Higher education:** Institutional purchasing through committees. LMS integration (Canvas, Blackboard, Moodle). Faculty autonomy in tool selection. Accreditation implications.
- **Corporate learning and development:** ROI measurement. Integration with HR systems. Compliance training requirements. Skills taxonomies and career pathing.
- **Consumer learning (Duolingo, MasterClass, Skillshare):** More like consumer products. Engagement and retention dominate. Learning outcomes are harder to measure and easier to neglect.
- **Professional certification and credentials:** Assessment integrity. Employer recognition. Stackable credentials and career outcomes.

---

## Archetype 11: Gaming / Entertainment

**Examples:** Fortnite, Roblox, Minecraft, Netflix, Spotify, Disney+, HBO, Steam

### Distinctive Characteristics

- **The product is an experience, not a tool.** Gaming and entertainment products are consumed for their own sake. The user's goal is enjoyment, not productivity. This changes everything about product judgment.
- **Creative production is part of the product.** Games, shows, and music require creative talent — writers, designers, artists, composers. The product organization must integrate creative and technical functions.
- **Engagement is deep and emotional.** Users form strong emotional attachments to games and entertainment products. They identify with characters, communities, and creators. This creates both opportunity and responsibility.
- **Monetization has ethical dimensions.** Loot boxes, battle passes, microtransactions, and attention-based monetization raise ethical questions about addiction, exploitation, and fairness. These are product design decisions.
- **Communities are part of the product.** Gaming communities, fan communities, and creator communities are assets that must be nurtured and ecosystems that can turn toxic. Community management is a product function.
- **Platform dynamics.** Games and entertainment products exist in platform ecosystems (console, mobile, streaming) with platform-specific constraints, revenue shares, and audience behaviors.

### Product Leadership Demands

- **Product judgment and taste** (Capability 1.4): Paramount. Entertainment products succeed or fail on creative quality, not feature checklists. Taste is not optional — it's the core competency.
- **Data and evaluation fluency** (Capability 1.6): Engagement metrics are abundant. The risk is optimizing for engagement at the expense of creative quality or user well-being.
- **Business economics** (Capability 1.7): Monetization model design is a product strategy decision with ethical dimensions. Free-to-play, subscription, premium, and hybrid models each create different incentives.
- **Risk judgment** (Capability 1.8): Content moderation, community toxicity, addiction mechanics, and the exploitation of vulnerable users (especially children) are salient risks.
- **Cross-functional influence** (Capability 2.2): Must bridge creative and technical functions that have different cultures, values, and success metrics.

### Common Failure Modes

1. **Data-driven design destroying creative quality.** Optimizing game design by A/B testing every element. The result is a local maximum that's globally mediocre. Data informs creative decisions; it doesn't make them.
2. **Monetization that feels exploitative.** Pay-to-win mechanics, predatory loot boxes, aggressive advertising. Users feel exploited. Trust erodes. Eventually regulators intervene.
3. **Ignoring community health.** Toxic communities drive away users. Neglecting moderation and community management undermines the product.
4. **Chasing trends without understanding them.** Building a battle royale because Fortnite succeeded. Building a streaming service because Netflix succeeded. The execution and creative vision determine success, not the category.
5. **Live service burnout.** Games-as-a-service that demand constant engagement. Players burn out. The product that was designed for retention drives users away through exhaustion.
6. **Platform dependency.** Building exclusively for one platform (console, mobile, streaming service) creates dependency on the platform's policies, revenue share, and audience access.
7. **Content investment without product strategy.** Streaming services that spend billions on content without a clear product strategy for discovery, retention, and differentiation.

### Industry-Specific Variations

- **AAA gaming:** Blockbuster budgets ($100M+). Long development cycles. High risk, high reward. Creative vision and execution quality determine outcomes. Service-based revenue models are replacing one-time purchases.
- **Indie gaming:** Small teams, creative risk-taking, platform discovery challenges. The product management discipline is often informal or absent — creative vision substitutes for structured product thinking.
- **Mobile gaming:** Free-to-play dominates. User acquisition economics determine viability. Engagement and monetization optimization are the core product capabilities. Ethical boundaries are frequently tested.
- **Streaming video (Netflix, Disney+):** Content investment dwarfs product investment. Recommendation and discovery are the primary product challenges. Churn reduction through content and product.
- **Streaming music (Spotify, Apple Music):** Licensing economics dominate. Discovery and personalization are product differentiators. Creator economics and compensation are strategic issues.
- **Social / UGC gaming (Roblox, Fortnite Creative):** Platform dynamics. Creator economics. Content moderation at scale. The boundary between player and creator is the product.

---

## Archetype 12: Market Data / Analytics

**Examples:** Bloomberg Terminal, Tableau, Datadog, Snowflake, Looker, Amplitude, Mixpanel

### Distinctive Characteristics

- **The product delivers insight, not action.** Analytics products help users understand what's happening and decide what to do — but the action happens elsewhere. The value chain is: data → insight → decision → action → outcome. The product controls only the first two or three links.
- **Data quality is the product.** If the data is wrong, the insights are wrong, and the decisions are wrong. Data accuracy, completeness, timeliness, and provenance are product quality dimensions.
- **Trust in the data is earned, not assumed.** Users must trust the data before they'll act on it. Building and maintaining data trust is a product requirement that spans data engineering, product design, and communication.
- **The user ranges from novice to expert.** Analytics products must serve users who want a simple dashboard and users who want to write complex queries. The breadth of user sophistication is extreme.
- **Integration and connectivity are barriers to entry.** Analytics products must connect to wherever data lives — databases, warehouses, SaaS tools, APIs. The breadth and quality of integrations determine the product's addressable market.
- **The "so what" gap.** Analytics products show users what's happening but often don't help them understand what to do about it. Closing the gap from insight to action is the frontier of analytics product design.

### Product Leadership Demands

- **Data and evaluation fluency** (Capability 1.6): Highest data fluency requirement. Must understand data modeling, statistical reasoning, visualization best practices, and the difference between correlation and causation at a deep level.
- **Technical fluency** (Capability 1.5): Must understand data infrastructure — databases, warehouses, ETL/ELT, query languages, data modeling. Cannot evaluate product decisions without this understanding.
- **Product judgment** (Capability 1.4): Visualization design, information architecture, and the "principle of least surprise" in data presentation are taste dimensions that require deliberate development.
- **Customer and domain understanding** (Capability 1.3): Analytics products serve analysts, data scientists, business users, and executives — each with different mental models and needs. Understanding these differences is essential.

### Common Failure Modes

1. **Building for analysts, ignoring business users.** The product has powerful query capabilities but is unusable by anyone without SQL skills. 80% of potential users are excluded.
2. **Building for business users, ignoring analysts.** Dashboards are beautiful but inflexible. Power users can't answer novel questions. They export to Excel and never return to the product.
3. **Data trust erosion.** Inconsistencies between dashboards, data freshness issues, unexplained changes in metrics. Users lose trust in the data. Once lost, trust is extraordinarily hard to regain.
4. **Dashboard proliferation without decision impact.** Organizations build hundreds of dashboards. Most are never looked at. Of those that are, most don't change decisions. Dashboard count is a vanity metric.
5. **Visualization over insight.** Beautiful visualizations that obscure rather than reveal. Form over function in data presentation.
6. **Performance neglect.** Queries that take minutes to return. Dashboards that take seconds to load. Performance is a product feature — slow analytics products don't get used.
7. **Alert fatigue.** Alerting systems that cry wolf. Users learn to ignore alerts. When something important happens, no one notices.

### Industry-Specific Variations

- **Business intelligence (Tableau, Looker, Power BI):** Visualization and exploration are core. The semantic layer / metrics layer is the hardest product design problem. AI-assisted analysis is the current frontier.
- **Product analytics (Amplitude, Mixpanel, Heap):** Event-based data models. Behavioral analysis workflows. Experimentation integration. The boundary between product analytics and CDPs (customer data platforms) is blurring.
- **Infrastructure monitoring (Datadog, New Relic, Grafana):** Real-time data. Alerting quality. The volume of data is extreme. Cost management is a product feature.
- **Data warehouses and lakes (Snowflake, Databricks, BigQuery):** Performance, scalability, and cost management. The "data platform" expansion — from storage to compute to governance to AI/ML.
- **Financial data (Bloomberg, Refinitiv, FactSet):** Data accuracy is non-negotiable. Latency matters (milliseconds for trading). Terminal/workstation experience — high information density for expert users.
- **Embedded analytics:** Analytics capabilities embedded in other products. Multi-tenancy, white-labeling, and data isolation are product requirements.

---

## Archetype 13: Internal Tools / Operations

**Examples:** Internal admin panels, customer support tools, content management systems, operations dashboards, internal workflow tools, sales enablement tools

### Distinctive Characteristics

- **Users are colleagues, not customers.** Internal tool users are within the same organization. This changes the user research dynamic (easier access, more honest feedback, higher tolerance for rough edges) and the prioritization dynamic (internal users don't generate revenue).
- **Value is indirect and hard to measure.** Internal tools create value by making other functions more efficient or effective. Measuring this value requires understanding the workflows they support.
- **Build-vs-buy decisions are constant.** Every internal tool could potentially be replaced by a SaaS product. The build decision must be justified by specific, identifiable advantages over available alternatives.
- **Prioritization is perpetually contested.** Internal tools compete for resources against customer-facing products. The internal tool PM must constantly justify why investment in internal tools is more valuable than investment in customer-facing features.
- **User adoption can be mandated but shouldn't be.** Internal tools that require mandates to achieve adoption are failing. If the tool is genuinely better, users will adopt it voluntarily. Mandated adoption masks usability problems.
- **The "internal customer" dynamic.** Internal users are "customers" but they can't leave. This creates perverse incentives — the PM can ignore user needs without immediate consequences, or can over-serve internal users at the expense of company outcomes.

### Product Leadership Demands

- **Customer and domain understanding** (Capability 1.3): Must understand internal users' workflows, pain points, and context as deeply as any PM understands external customers. Easier access doesn't mean easier understanding.
- **Business economics** (Capability 1.7): Must build the economic case for internal tool investment. ROI models for internal tools are harder because the value is indirect. Must quantify productivity improvements, error reduction, and decision quality.
- **Product judgment** (Capability 1.4): Internal tools have historically been under-invested in design and UX. This is changing. Internal tool quality affects employee satisfaction, productivity, and error rates — all of which have measurable business impact.
- **Cross-functional influence** (Capability 2.2): Must influence resource allocation decisions that favor internal tools over customer-facing products. This is one of the hardest influence challenges in product management.

### Common Failure Modes

1. **"It's just an internal tool" syndrome.** Under-investing in design, testing, and reliability because "it's internal." Internal tools with poor UX create errors, slow down operations, and frustrate employees. These have real business costs.
2. **Building without understanding the workflow.** Shipping internal tools based on what stakeholders say they want, without observing actual workflows. The tool is built; nobody uses it because it doesn't fit how work actually happens.
3. **Build when buy would be better.** Building custom internal tools that are worse and more expensive than available SaaS alternatives. The allure of "building exactly what we need" versus the reality of maintaining internal software.
4. **Buy when build would be better.** Adopting SaaS tools that don't fit the workflow and then contorting the workflow to fit the tool. The organization becomes a patchwork of misconfigured SaaS products.
5. **No product management.** Treating internal tools as engineering projects without product management. Engineers build what's technically interesting. Users get what's built. Nobody measures whether it's actually better.
6. **The "superuser" trap.** Designing for the most vocal internal user — who is often an outlier in expertise and needs. The tool works for them and no one else.
7. **Migration neglect.** Building a new internal tool without planning migration from the old one. Users stay on the old tool because switching costs are too high.

### Industry-Specific Variations

- **Customer support tools:** Agent efficiency and customer satisfaction must be balanced. Knowledge management and AI-assisted responses are current frontiers. The tool shapes the customer experience.
- **Sales enablement and CRM:** Sales team adoption is the perennial challenge. CRM data quality is the perennial problem. The tool must make salespeople more effective without adding administrative burden.
- **Content management systems:** Editorial workflow, content governance, and multi-channel publishing. The tension between flexibility and structure is the central design challenge.
- **Operations and logistics tools:** Real-time data, exception handling, and operational reliability. Downtime has immediate business impact. The cost of an error is measured in operational failures.
- **Internal developer tools:** CI/CD, deployment, monitoring, incident management. Developer experience expectations are high. Build-vs-buy decisions are particularly acute.
- **HR and people tools:** Employee experience, manager workflows, compliance requirements. Sensitive data handling. Integration with payroll, benefits, and other HR systems.

---

## Archetype Interaction Patterns

When products span multiple archetypes, the demands compound. Here are the most common interaction patterns and their implications:

### Platform + Marketplace
A platform that enables a marketplace (e.g., Shopify + app store, Salesforce + AppExchange). The platform must serve both direct users and third-party developers. Governance, quality control, and revenue sharing become product design problems.

### Enterprise + AI
Enterprise SaaS with AI features. Must satisfy enterprise requirements (security, compliance, reliability) while shipping AI capabilities that are inherently probabilistic. The tension between "it works 95% of the time" and "enterprise customers need it to work 100% of the time" is the central challenge.

### Consumer + Fintech
Consumer products with financial features (e.g., social payments, investing). Must deliver consumer-grade UX with financial-grade reliability, security, and regulatory compliance. The "move fast" consumer culture and the "don't break things" fintech culture collide.

### Healthcare + AI
AI in healthcare. Must satisfy clinical validation requirements, FDA regulatory pathways, and patient safety standards while operating at the frontier of AI capability. The stakes are the highest of any archetype combination.

### Hardware + Platform
Hardware products that become platforms (e.g., iPhone + App Store, Oculus + app ecosystem). Hardware determines the platform's capabilities; the platform determines the hardware's value. Managing this co-evolution is the central leadership challenge.

### Marketplace + Enterprise
Marketplaces for enterprise services (e.g., Upwork Enterprise, managed marketplaces). Must satisfy enterprise procurement, security, and compliance requirements while maintaining marketplace liquidity and trust dynamics.

---

## Using This Catalog

1. **Identify your primary archetype(s).** Which archetypes describe the products you lead? Most products span 1–3 archetypes.
2. **Study the distinctive characteristics.** What's different about your archetype that a PM from another archetype wouldn't understand?
3. **Audit your leadership against the demands.** Are you developing the capabilities most critical for your archetype? Or are you developing capabilities that are more important for a different archetype?
4. **Study the failure modes.** Which failure mode are you most at risk of? What would you change to prevent it?
5. **Study an adjacent archetype.** If your product might evolve into a platform, study Archetype 3. If you might add AI features, study Archetype 5. If you might serve enterprise customers, study Archetype 2.
6. **Recognize archetype interactions.** If your product spans multiple archetypes, understand the compound demands and conflicting requirements.

---

*This catalog is a reference, not a classification exercise. Products don't fit neatly into archetypes — they exhibit dynamics from multiple archetypes. The goal is to recognize which dynamics are most salient for your leadership decisions, not to find the perfect label.*
