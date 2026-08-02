# Scenario 07: The CEO's Conference-Driven AI Demand

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-007 |
| **title** | The CEO's Conference-Driven AI Demand |
| **leadership_level** | Principal PM, Director, VP Product |
| **primary_tension** | Executive pressure vs. validated user need |
| **key_capability** | Upward management, strategic influence |
| **estimated_time** | 40 minutes |
| **related_principles** | PRN-0002 (Strategy Is What You Say No To), PRN-0014 (AI Product Decisions), PRN-0007 (GtM and Product Alignment) |

## Situation

You are the **VP of Product** at **Mercury Logistics**, a B2B logistics platform that connects mid-market retailers (200-800 stores) with warehousing, inventory management, and last-mile delivery providers. The company is 320 employees, $48M ARR, growing 35% year-over-year. Your platform processes 1.8 million shipments per month across 900 retail customers and 1,400 warehouse/fulfillment partners.

Your product is a workflow coordination platform. It doesn't predict, recommend, or generate — it routes, tracks, and reconciles. Retailers enter shipment requirements, the platform matches them with warehouse capacity, routes the shipments, tracks them through delivery, and reconciles invoices. The platform's value is in operational reliability — it handles a massive coordination problem with 99.7% accuracy. When a shipment is supposed to arrive at Store #247 on Tuesday, it arrives at Store #247 on Tuesday.

### The CEO's Demand

Your CEO, **Victor Strand**, just returned from the annual National Retail Federation (NRF) conference. Every session he attended was about AI. Every vendor booth had an AI demo. Every speaker said "if you're not building AI into your product, you're falling behind."

At the Monday morning executive staff meeting, Victor was energized in a way you haven't seen in months:

"Here's what we're going to do. Every major logistics company is adding AI. We need an AI-powered shipment predictor. Something that tells retailers 'this shipment has a 73% chance of being delayed' or 'this carrier has an elevated risk profile this week.' We ship this next quarter. The market is moving fast. We can't afford to be the company that missed AI."

He assigned you ownership of the "AI Shipment Predictor" initiative. He wants:
- A demo for the next board meeting (6 weeks from now)
- A beta release in Q2 (3 months from now)
- A GA launch in Q3 (6 months from now)
- A press release positioning Mercury as "AI-powered logistics" that he can send to the NRF conference organizers

### The Reality Check

After the meeting, you spent the afternoon with your team doing a rapid assessment:

**The Data Reality:**
- Your platform has operational data (shipment history, carrier performance, warehouse capacity). This is good data.
- You do not have the external data that would make a delay prediction accurate — weather data, traffic data, port congestion data, labor dispute data, carrier financial health data. Without these, any "AI prediction" is essentially a historical average with a confidence interval.
- Your data science team is one person (Dr. Sarah Park, a recent hire who joined to work on route optimization, not delay prediction).

**The User Need Reality:**
- Your PM for Retail Experience, **Diego**, went back through 18 months of customer research, feature requests, and support tickets. He found zero customer requests for "AI shipment delay prediction." Zero.
- What customers DO ask for: faster exception handling (when a shipment is actually delayed, help me fix it faster), better inventory visibility (how much inventory do I have in transit right now?), and carrier performance benchmarking (which carriers are consistently late to which regions?).
- When Diego described the "AI delay predictor" concept to 5 customers last week (without attributing it to Victor), the most common response was: "That's interesting, but what I actually need is..." followed by one of the three actual needs above.

**The Engineering Reality:**
- Your 42-person engineering team is fully allocated on Q1-Q2 roadmap commitments: a warehouse capacity optimization project (critical for partner retention), a carrier API standardization project (reducing integration time from 4 weeks to 3 days), and a compliance project for new California warehousing regulations.
- The capacity optimization project is 60% complete and has 8 engineers working on it. Pulling engineers from it would delay it by at least a quarter.
- No one on the engineering team has significant experience building production ML systems. Sarah is excellent but she's one person.

**The Market Reality:**
- You checked. Project44, FourKites, and Shippeo already offer AI-powered shipment visibility and delay prediction. They've been doing it for 5+ years. They have the external data integrations. They're good at it.
- Competing with them on AI prediction would mean entering a market where you have no data advantage, no talent advantage, and competitors with a 5-year head start.

In summary: Victor wants you to ship an AI feature that customers haven't asked for, using data you don't have, with a team you don't have, in a timeline that's impossible, to compete in a market where established players already dominate — and he wants to do it because he went to a conference.

### The Organizational Dynamics

This isn't the first time Victor has returned from a conference with a new priority. Two years ago, it was "we need blockchain for supply chain transparency" (the team spent 3 months building a proof of concept that no customer ever asked for). Last year, it was "we need a marketplace model like Uber Freight" (the team spent 2 months scoping before the economics proved unworkable at Mercury's scale).

The pattern is well-known in the company. Engineers call these "Victor's conference features." The cycle is: Victor announces at an executive meeting → a team is pulled off real work → they build something half-baked → it ships to tepid response → it's quietly deprecated → Victor has moved on to the next conference.

Your Director of Engineering, **Priya**, texted you after the executive meeting: "Please tell me we're not doing another conference feature. My team just got momentum on the warehouse project. If I pull them off again, I'm going to lose people."

## Characters

**Victor Strand (CEO).** Charismatic, visionary, easily inspired by shiny objects. Genuinely wants the company to succeed and believes he's pushing the team to be innovative. Doesn't understand (or doesn't want to understand) the gap between his vision and the operational reality. Has never built a product himself. Motivated by: being seen as an innovative leader, keeping up with market trends, board confidence.

**Priya Sharma (Director of Engineering).** Has been at Mercury for 4 years. Has survived three "Victor's conference features" and is tired of it. Runs a disciplined engineering organization. Motivated by: engineering team morale, shipping real value, not starting things that won't finish.

**Diego Reyes (Senior PM, Retail Experience).** Reports to you. Has deep customer empathy and strong research skills. Was the one who did the rapid customer research on the AI feature. Has a folder on his desktop called "Things Victor Asked For That Customers Didn't" — it has 14 items in it, only 2 of which ever shipped. Motivated by: building things customers actually need, being a good PM, not burning political capital on lost causes.

**Dr. Sarah Park (Data Scientist).** Joined 3 months ago. Was excited to work on route optimization. Has zero interest in building a delay predictor with incomplete data — she knows it won't be accurate and her name will be on it. Has told you: "I can build something, but it won't be good. If we're going to do AI, let's do it right, not fast." Motivated by: professional integrity, doing rigorous work, not being blamed for a half-baked product.

**The Board.** Meets quarterly. Next meeting is in 6 weeks. The board has been asking about AI because all boards are asking about AI. Victor wants to show them something. The board's sophistication on AI varies — some members could spot a demo that has no real data behind it, others just want to see "we're doing AI."

## Constraints

- Engineering is at capacity. Any AI project requires stopping something else.
- No external data integrations for delay prediction. Building them would take 3-6 months just for data acquisition.
- One data scientist. No ML engineering team.
- Board meeting in 6 weeks. Victor needs something to show.
- Q2 beta target (3 months) is technically impossible for anything meaningful.
- Customer research shows no demand for the specific feature Victor wants.
- Established competitors exist. Entering their market with an inferior product is a losing strategy.

## Your Role

You are VP of Product at Mercury Logistics. You report to Victor (CEO). You lead a team of 5 PMs covering different product surfaces. You do not manage engineering (Priya does), but you partner with her on roadmap and capacity decisions. You are responsible for the product strategy and roadmap.

Your challenge is not just "how do we build this thing?" — it's "how do I manage upward, protect my team, preserve the real roadmap, and either redirect Victor's energy toward something useful or convince him this is a bad idea — without being seen as the person who 'doesn't get innovation' or 'isn't being a team player'?"

## Response Format

### Part 1: Assumptions

Key areas: Is Victor's interest genuine or performative (for the board)? Can Victor be influenced by data, or does he make decisions emotionally? What would satisfy the board's AI interest without shipping a product? Is there a version of "AI in logistics" that DOES serve customer needs and IS feasible? What would happen if you said no directly vs. if you redirected vs. if you complied?

### Part 2: Decision

Describe your decision with:
- **What you will do.** Your approach to Victor, the timeline, what you will ship and when.
- **What you will NOT do.** What you're explicitly refusing, even if Victor pushes.
- **The reframe.** How do you translate "Victor wants AI" into something that is (a) genuinely useful to customers, (b) feasible with your resources, and (c) positions Mercury well for the market?
- **The board demo.** What will you actually show at the board meeting in 6 weeks?
- **How you protect the real roadmap.** Which existing commitments do you defend, and how?

### Part 3: Pre-Mortem

Assume the AI initiative failed. 12 months later, Victor is disappointed, the team is demoralized, and Mercury is no closer to being "AI-powered." Write a pre-mortem with at least 3 distinct failure paths. Include: failure of the approach you chose, failure from Victor's reaction to your approach, and failure from competitive or market dynamics.

---

## Scoring Rubric (Scenario-Specific)

### Upward Management and Influence

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Either complies with Victor's demand without pushback ("the CEO wants it, we build it") or refuses outright ("this is stupid, we're not doing it"). Neither approach manages upward effectively. |
| 3 | Brings data to Victor (customer research, competitive analysis, resource constraints) and proposes an alternative. Treats the conversation as a persuasion exercise. |
| 4 | Reframes Victor's desire into something that is strategically coherent, operationally feasible, and genuinely valuable to customers. Doesn't say "no" — says "yes, and here's the version that actually works." Positions the alternative as "the AI strategy that wins" rather than "the compromise version." |
| 5 | Anticipates Victor's underlying needs (board optics, competitive anxiety, desire to be seen as innovative) and addresses them separately from the product decision. The board needs to see AI investment — show them the AI roadmap (which includes route optimization, exception handling, and carrier benchmarking), not just a delay predictor demo. Victor needs to feel like he's leading — make him the sponsor of an AI strategy that's real, not a demo. |

### Strategic Redirection

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes building exactly what Victor asked for. Or proposes building nothing. |
| 3 | Proposes an alternative AI feature that addresses a real customer need (exception handling AI, carrier performance prediction, inventory forecasting). Connects it to the data you actually have. |
| 4 | Reframes "AI in logistics" as a strategic capability, not a feature. Proposes an AI strategy with phases: Phase 1 builds the data infrastructure (unified data layer, external data integrations), Phase 2 applies AI to the highest-value customer need (exception handling), Phase 3 expands to additional use cases. Victor gets a narrative for the board ("we're building AI infrastructure that will power multiple features"), and the team gets to build something real. |
| 5 | Makes Victor the champion of the reframed strategy. He's not being managed — he's leading an AI initiative that is strategically sound. The board demo shows customer research that validates the approach, a phased roadmap that shows ambition without recklessness, and a clear rationale for why Mercury's AI strategy is different from (and better than) competitors'. |

### Resource Protection

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Pulls engineers from critical projects without a fight. Accepts that the roadmap must be sacrificed for the CEO's demand. |
| 3 | Advocates for protecting the most critical roadmap items (warehouse optimization, carrier API standardization). Proposes a small, focused AI investment that doesn't gut existing commitments. |
| 4 | Creates explicit trade-off visibility: "If we do X AI work in Q2, we delay the warehouse optimization by Y weeks, which costs us Z in partner retention risk. Victor, is that trade-off worth it to you?" Makes the cost of the AI investment visible at the CEO level so the decision is explicit, not a default. |
| 5 | Frames the resource conversation as a strategic choice, not a capacity negotiation: "We have one engineering organization. It can build one thing well or two things poorly. The warehouse optimization is a known, high-ROI investment that customers are asking for. The AI shipment predictor is an unknown, speculative investment that customers haven't asked for. We can do both if we staff up — here's what that would cost. If we can't staff up, we need to choose." |

### Team and Morale Management

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Ignores the morale impact. Just tells the team "we're doing what the CEO wants." |
| 3 | Acknowledges the team's frustration. Communicates the decision rationale honestly. |
| 4 | Involves the team in the reframe: "Victor wants AI. We know what customers actually need. Let's figure out the AI strategy that makes customers happy AND satisfies Victor's board requirements. Diego, what do customers need? Sarah, what's feasible with our data? Priya, what capacity do we have? Let's design the answer together." |
| 5 | Positions the team as strategic partners in the reframe, not victims of a CEO demand. When the reframed AI strategy is presented to Victor, it's a team effort with shared ownership. Priya, Diego, and Sarah all have a stake in the outcome. Their expertise is valued and visible. |

---

## Facilitator Notes

**Common traps:**
1. Assuming Victor is an idiot. He's not — he's a CEO making decisions based on incomplete information and competitive anxiety. Your job is to provide better information, not to dismiss his concerns.
2. Building a demo that has no path to becoming a real product. Victor will ask "when does this ship?" and "a demo is not a product" will be the answer to a question you should have anticipated.
3. Proposing "we'll build a small AI feature" without connecting it to customer value. A useless AI feature is worse than no AI feature — it sets the expectation that "Mercury's AI isn't very good."
4. Complaining to Priya or Diego about Victor instead of managing the situation. Your team is looking to you for leadership, not commiseration.

**Discussion prompts:**
- If Victor won't budge and demands the delay predictor, what do you do?
- What would you need to see from Victor to trust that his AI demand is strategic rather than performative?
- Is Victor the problem, or is the board dynamic that makes Victor feel he needs an AI story the problem?
- How would you handle this differently if you were a Director of Product (not a VP)?
- What is the actual cost of building the wrong AI feature? (Consider: engineering time, market positioning, customer trust, team morale.)

**Related Academy Content:**
- [PRN-0002](../../01_core_doctrine/PRINCIPLES.md): Strategy is what you say no to
- [PRN-0014](../../01_core_doctrine/PRINCIPLES.md): AI product management
- [Framework 2](../../01_core_doctrine/DECISION_FRAMEWORKS.md): RICE-LM prioritization
