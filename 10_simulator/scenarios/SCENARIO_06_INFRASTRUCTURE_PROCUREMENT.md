# Scenario 06: 18-Month Procurement Cycle, 14-Month Runway

| Field | Value |
|-------|-------|
| **scenario_id** | SIM-006 |
| **title** | 18-Month Procurement Cycle, 14-Month Runway |
| **leadership_level** | VP Product, CPO, Founder |
| **primary_tension** | Runway vs. long enterprise sales cycles |
| **key_capability** | Founder resource allocation under existential constraint |
| **estimated_time** | 45 minutes |
| **related_principles** | PRN-0012 (Founder Product Leadership), PRN-0004 (Product-Market Fit as Condition), PRN-0010 (Economic Moats) |

## Situation

You are the **Founder and CEO** of **GridSight**, a startup building AI-powered predictive maintenance software for electric utility grid infrastructure. Your platform uses machine learning on sensor data (thermal imaging, vibration analysis, partial discharge detection) to predict equipment failures on transformers, switchgear, and transmission lines before they cause outages.

GridSight is 3 years old. You have 22 employees, $7M in total funding ($2M seed, $5M Series A led by a climate-tech VC), and you are burning $1.5M per month. Your current runway is **14 months**. You have no revenue.

### The Product and the Problem

GridSight's product works. In pilot deployments with three utilities, your system:
- Predicted 87% of equipment failures an average of 23 days before they occurred
- Reduced unplanned outage minutes by 34% in pilot regions
- Was estimated to save $2.3M per year per utility in avoided outage costs and optimized maintenance scheduling

The three pilot utilities — **Midwest Electric Cooperative** (MEC), **Southwest Power & Light** (SPL), and **Northeast Grid Operations** (NGO) — have all expressed strong interest in full deployments. Their feedback is consistent: "This is the best predictive maintenance tool we've seen. We want this."

### The Procurement Problem

Utility procurement cycles are 18-24 months. The process works like this:

1. **Request for Information (RFI):** Utility issues a formal request describing the problem. Vendors respond with capabilities. (2-3 months)
2. **Request for Proposal (RFP):** Utility issues a detailed specification. Vendors submit formal proposals with pricing. (3-4 months)
3. **Evaluation and Shortlisting:** Utility evaluates proposals, conducts demos, checks references. (3-4 months)
4. **Negotiation and Contracting:** Legal, procurement, and security review. For a startup with no track record, this phase can be brutal — security audits, financial stability reviews, insurance requirements, performance bonds. (4-6 months)
5. **Board Approval:** Many utilities (especially municipal and cooperative) require board approval for contracts above certain thresholds. (1-3 months)
6. **Pilot to Production:** After contract signature, deployment planning, data integration, and change management. (3-6 months before first revenue recognition)

Total: 18-24 months from "we want this" to first dollar of revenue.

### The Math That Keeps You Awake

Your Series A was raised on a narrative: "Three utilities in pilot, strong results, clear path to commercialization." Your board expected to see first revenue by month 16 of the Series A. You are at month 10 of the Series A. You have 14 months of runway. The fastest possible procurement cycle is 18 months.

The math doesn't work.

You've explored accelerants:
- **Push the utilities faster:** Not possible. Procurement cycles are governed by state utility commission regulations, public bidding laws, and internal policies that none of the three utilities are willing to bend.
- **Sell to smaller utilities:** The procurement cycle for small municipal utilities is 12-15 months — still tight, and the contract values are $50K-$200K annually, not enough to meaningfully extend runway.
- **Raise a bridge round:** Your VCs are supportive but have signaled that they expect to see commercial traction (signed contracts, not just pilots) before leading a bridge. Your lead investor, **Catherine**, told you last quarter: "We believe in the vision, but we need to see market validation. A signed contract changes everything."
- **Cut burn:** You're already lean. You could cut from $1.5M/month to $1.2M/month by reducing headcount (losing 4-5 people), which extends runway from 14 to 17 months — still short of 18.
- **Generate revenue from services:** You could offer consulting/implementation services to the pilot utilities. This might generate $200K-$400K over 6-12 months, but it would distract the team from product development and dilute the "we're a software company" narrative with investors.

### The Alternative Paths

**Path A: Wait It Out.** Continue supporting the pilots, push the three utilities through procurement, and hope to have a signed contract before runway ends. This is the plan you sold to the board. The math says it probably doesn't work.

**Path B: Bridge Round Now.** Go to your VCs and existing investors and ask for a bridge round ($3-5M) NOW, before the runway becomes a crisis. This requires admitting that the Series A timeline was wrong, but it's better to do it from a position of relative strength (14 months of runway, strong pilot results) than from desperation (3 months of runway, panicked ask).

**Path C: Pivot to a Different Market.** Utilities are slow but large. What if you targeted industrial customers instead — manufacturing plants, data centers, oil and gas facilities — that have their own electrical infrastructure and faster procurement cycles? The product would need modification (different sensor types, different failure modes), but the procurement cycle might be 3-6 months instead of 18-24.

**Path D: Channel Partnership.** Partner with a large established vendor that already sells to utilities — Siemens, GE, ABB, Schneider Electric. They have existing procurement vehicles, relationships, and trust. They could resell GridSight as part of their grid modernization offerings. The downside: they'll take 30-50% of revenue, you'll lose some product control, and the partnership negotiation itself might take 6 months.

**Path E: Acquire a Revenue Stream.** Use remaining cash to acquire a small utility software company that already has contracts and cash flow. This is high-risk, highly distracting, and probably uses most of your remaining cash — but it could buy you the procurement runway you need.

**Path F: Something Else.** None of the above may be the right answer.

### Your Personal Context

This is your first company. You were a senior engineer at a grid equipment manufacturer before starting GridSight. You have deep domain expertise but limited experience with fundraising, enterprise sales cycles, and cash management. Your co-founder (CTO) is your best friend from graduate school. You have 22 employees who joined because they believed in the mission of preventing grid failures and reducing wildfire risk from faulty equipment.

Three of your engineers have visas tied to their employment. If the company runs out of money, they have 60 days to find new jobs or leave the country.

You haven't slept well in weeks.

## Characters

**Catherine Okonkwo (Lead Investor, Board Member).** Partner at Terra Ventures, a $400M climate-tech fund. Smart, direct, supportive but not sentimental. Has seen 40+ portfolio companies navigate the "pilot to revenue" gap. Her guidance has been: "Show me a signed contract, and I can raise you a B round. Show me pilot results without contracts, and I can't." Motivated by: fund returns, portfolio performance, not losing a promising investment to bad timing.

**Dr. James Chen (CTO, Co-Founder).** Your best friend. Brilliant ML engineer. Built the predictive models. Less comfortable with business strategy but trusts your judgment. Has been working 70-hour weeks for 3 years. Motivated by: mission, loyalty to you, building technology that matters.

**Maria Vega (VP of Business Development).** Joined 9 months ago from an enterprise software company. Has relationships with utility procurement teams. Has been managing the three pilot relationships. Increasingly anxious about the timeline. Has told you privately: "I can get these deals done, but I can't change the speed of utility procurement. It's not a relationship problem — it's a structural one." Motivated by: closing her first deals, career credibility, not being at a company that runs out of money.

**Amir Hassan (VP of Engineering).** Manages the 12-person engineering team. Has been pushing for a "platformization" investment to make the product easier to deploy across multiple utility environments. Worried that the team is burning out from supporting three separate pilot deployments with slightly different configurations. Motivated by: engineering excellence, team health, building a sustainable product.

**The Pilot Champions (external).** At each of the three utilities, you have a champion — a senior engineer or manager who loves GridSight and is pushing for procurement internally. They have limited power over the procurement timeline but are your best source of information about what's happening inside the procurement process. They are risking their internal credibility by advocating for a startup.

## Constraints

- 14 months of runway at current burn rate. This is your hard constraint.
- Utility procurement cycles: 18-24 months minimum.
- No revenue today. All three pilots are unpaid (they were relationship-building investments).
- Your VCs want commercial traction before leading a bridge or Series B.
- 22 employees depending on the company's survival.
- The product works. This is not a "does the product solve the problem?" question — it's a "can we survive long enough to get paid for solving the problem?" question.
- Your CTO and co-founder is your best friend. Whatever you do, you need to bring him with you.

## Your Role

You are the Founder and CEO. Every decision is yours. There is no executive team to delegate to — you are the executive team. You have a board (investors) who need to be managed. You have employees who need to be led. You have a co-founder who needs to be your partner in whatever comes next. And you have a product that could genuinely prevent grid failures, wildfires, and power outages — if you can survive long enough.

## Response Format

### Part 1: Assumptions

Key areas: Is a bridge round actually possible without signed contracts, or is Catherine's signal definitive? Can any of the three pilots be accelerated through the procurement process? What is the actual probability of closing at least one contract before runway ends? Could the company survive on dramatically reduced burn for long enough? Would an industrial pivot be faster or would it just trade one set of problems for another? What does your CTO think about each option (you should know this before you make decisions)?

### Part 2: Decision

Describe your decision with:
- **What you will do.** Specific actions in the next 30, 60, and 90 days. Resource allocation changes.
- **What you will NOT do.** Which paths are you explicitly rejecting and why?
- **The conversation with Catherine.** What do you ask for? What do you commit to? How do you frame the situation?
- **The conversation with your team.** What do you tell the 22 employees? How transparent are you about the runway risk?
- **The conversation with your CTO/co-founder.** How do you bring James into the decision?
- **Success criteria.** What has to happen in the next 6 months for you to believe the company will survive?

### Part 3: Pre-Mortem

Assume the company ran out of money 14 months from now. You are writing a letter to your future self from beyond the grave of the company. What happened? Be specific. At least 3 distinct failure paths. Include: what you wish you had done differently, what signals you missed, and what you would tell a founder in your position today.

---

## Scoring Rubric (Scenario-Specific)

### Founder Resource Allocation

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Proposes one path without evaluating alternatives. Does not acknowledge that all paths have serious risks. |
| 3 | Evaluates multiple paths with explicit trade-offs. Recognizes that runway math is the binding constraint and makes decisions accordingly. |
| 4 | Sequences actions across multiple paths simultaneously: starts the bridge conversation now (before it's urgent), pursues the channel partnership in parallel, and prepares contingency plans (burn reduction, industrial pivot exploration). Does not put all chips on one bet. |
| 5 | Reframes the problem from "how do we survive?" to "what would make us easy to fund?" Identifies the specific signal that would unlock capital (signed contract, LOI, partnership, revenue milestone) and designs a plan that maximizes the probability of creating that signal within 12 months, while also having a plan for what happens if the signal doesn't materialize. |

### Stakeholder and Incentive Mapping

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Treats all stakeholders as aligned ("everyone wants the company to succeed"). No recognition of the different incentives of VCs, employees, co-founder, and utility champions. |
| 3 | Distinguishes between each stakeholder's incentives: Catherine needs a fund-returning investment; the team needs job security; James needs to believe in the mission and trust your leadership; the utility champions need to not be embarrassed by advocating for a startup that fails. |
| 4 | Designs specific communications for each stakeholder that address their incentives: Catherine gets a probabilistic model showing when contracts are likely to close and what bridge capital is needed to get there; the team gets transparency calibrated to their ability to handle uncertainty; the utility champions get support (case studies, ROI models, reference calls) to strengthen their internal advocacy. |
| 5 | Creates a narrative that serves all stakeholders: "GridSight is the best solution to a real problem. The procurement cycle is the challenge, not the product. Our job is to build a bridge from where we are to where the contracts are. Here's exactly what that bridge looks like and what each of you needs to do." |

### Decision Quality Under Existential Threat

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Panic decisions: drastic cuts, pivot to something random, hope for a miracle. No structured evaluation. |
| 3 | Clear-eyed assessment of options with probability estimates. Makes a decision with a defined evaluation point. |
| 4 | Designs the decision as a portfolio of bets: primary path (push procurement + bridge round), secondary path (channel partnership), fallback path (services revenue + burn reduction). Allocates resources across paths explicitly. Does not pretend certainty where there is none. |
| 5 | Defines the "kill criteria" for the current strategy: "If by month 6 we do not have a signed LOI from at least one utility AND a term sheet for a bridge, we will pivot to [specific alternative]." The decision includes not just what to do, but when to admit it's not working. |

### Leadership Communication

| Score | What We Look For |
|-------|-----------------|
| 1-2 | Hides the runway risk from the team to "protect morale." Or overshares and creates panic. |
| 3 | Communicates honestly with appropriate calibration: the leadership team knows the full picture, the broader team knows the situation and the plan without unnecessary anxiety. |
| 4 | Creates a narrative that is honest AND motivating: "We have a product that works, customers who want it, and a timeline that is tight but manageable if we execute. Here's our plan to bridge the gap. I'm going to be transparent with you about where we are every month. If the plan needs to change, you'll hear it from me first." |
| 5 | Uses the existential constraint as a focusing mechanism: "We have 14 months to prove that the utility industry will pay for what we've built. Every decision from now on is measured against that goal. If something doesn't get us closer to a signed contract, we don't do it. This is clarifying, not scary." |

---

## Facilitator Notes

**Common traps:**
1. Assuming Catherine will fund a bridge round because "the product works." VCs fund traction, not product quality. Pilot results without contracts are not traction.
2. Assuming "we'll just close one of the three pilots faster." Utility procurement doesn't speed up for startups. The regulations, bidding laws, and board processes are structural, not negotiable.
3. Proposing "we'll raise a Series B now" — Series B investors expect $2-5M ARR. You have $0.
4. Treating this as a product problem. It's not. The product works. The problem is time and cash.
5. Ignoring the personal dimension: co-founder relationship, employee visas, personal burnout.

**Discussion prompts:**
- If you had to cut the team by 30%, who would you cut and how would you decide?
- What would you need to see in the next 60 days to feel confident the company survives?
- If you were Catherine, what would make you write a bridge check?
- Is there a version of this company that generates revenue in 3-6 months instead of 18-24? What would you have to sacrifice?
- If the company fails, what was the failure? Was it the product, the market, the timing, or the fundraising?

**Related Academy Content:**
- [PRN-0012](../../01_core_doctrine/PRINCIPLES.md): Founder product leadership
- [PRN-0004](../../01_core_doctrine/PRINCIPLES.md): PMF as a condition, not a milestone
- [Framework 4](../../01_core_doctrine/DECISION_FRAMEWORKS.md): Risk-adjusted value assessment
