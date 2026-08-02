# Insurance Field Guide

## Quick Scan — Before Any Product Decision

1. **Does this product change the underwriting process?** If yes: will it change risk selection, risk assessment, classification, pricing, or terms? How will you know if the change improves or degrades the loss ratio?
2. **Does this product use data that proxies for protected characteristics?** If yes: have you tested for disparate impact? Can you document the actuarial justification for every rating factor?
3. **Does this product make decisions that must be explainable to consumers, regulators, or courts?** If yes: can you generate specific, individualized reasons for every adverse decision? Is the explanation layer designed into the product, not added after?
4. **Have you designed the underwriting-to-claims feedback loop?** You will not know if the product's underwriting is working for 12-36 months. How are you measuring early claims indicators? What triggers an underwriting review?
5. **Who is the actual user — the agent, the consumer, or the underwriter?** If you optimize for the wrong primary user, no amount of product quality will compensate.

## Regulatory Triggers

### You change underwriting criteria → State unfair discrimination laws, Reg B (if credit-related), emerging AI regulation

Any change to underwriting must be tested for: (a) actuarial justification — does the factor predict loss experience?, (b) fairness — does the factor proxy for a protected characteristic?, (c) state regulatory compliance — each state has its own unfair trade practices act. Colorado's SB21-169 requires algorithmic testing for bias in insurance.

### You change rates → State rate regulation (prior approval or file-and-use)

Rate changes must be filed with each state. Prior approval states require approval before use — this is a regulatory milestone on your product timeline, not an administrative afterthought. Rate filings are documents of 50-500+ pages with actuarial justification. Budget 3-6 months for rate approval in prior approval states.

### You use AI/ML in underwriting → NAIC AI Principles, state algorithmic accountability laws

AI in insurance must meet: (a) fairness — no unfair discrimination, (b) accountability — the insurer remains responsible for decisions, (c) compliance — with all applicable laws, (d) transparency — consumers and regulators can understand how decisions are made, (e) safe and robust design — error rates are understood and controlled. Colorado, Connecticut, and other states are implementing specific AI governance requirements.

### You change policy forms or terms → State form filing requirements

Policy forms (the contract document) must be filed with state regulators. Changes to coverage, exclusions, conditions, definitions — anything that changes the contractual promise — requires form filing. Certain lines and states have more flexibility (commercial lines in some states), but the default is that form changes require filing.

### You distribute through a new channel → Producer licensing and appointment requirements

If a third party is selling, soliciting, or negotiating insurance, they must be licensed as a producer in each state. Embedded insurance (insurance sold at the point of another transaction) must be structured to avoid unlicensed activity. The distinction between "referring" (does not require a license) and "soliciting" (requires a license) is jurisdictional and fact-specific.

### You handle claims data → Unfair claims settlement practices acts, privacy requirements

Claims handling is regulated. Unreasonable delay, inadequate investigation, and failure to communicate are violations of state unfair claims settlement practices acts. If your product automates claims decisions, it must not create a pattern of violations.

## Stakeholder Map

| Stakeholder | What They Care About | Veto Power |
|-------------|---------------------|------------|
| **Underwriting leadership** | Loss ratio, combined ratio, risk selection quality | Sets underwriting appetite and guidelines |
| **Actuarial** | Rate adequacy, classification accuracy, reserve adequacy | Reviews and signs rate filings; can block products with unsupported pricing |
| **Claims** | Loss adjustment expense, claims leakage, customer experience during claims | Process owners for the product's most important touchpoint |
| **Compliance** | State regulatory compliance, market conduct exams, complaint response | Can block products with unresolved compliance issues |
| **Legal** | Policy language, coverage litigation, regulatory interpretation | Reviews every policy form; owns coverage dispute defense strategy |
| **Distribution (agents/brokers)** | Commission, ease of doing business, product competitiveness | Controls customer access in agent-centric lines |
| **Reinsurance** | Portfolio risk, treaty terms, exposure aggregation | Can refuse to provide reinsurance capacity for poorly designed products |
| **State regulators (50 jurisdictions)** | Solvency, market conduct, consumer protection | Can disapprove rates, forms, or market conduct; can impose fines, restrictions, or license revocation |
| **Policyholders** | Coverage, price, claims experience | Churn; complaint to regulator; litigation |

## Risk Checklist

### Underwriting risk
- [ ] Loss ratio expectations defined and monitored
- [ ] Adverse selection detection designed (monitor risk profile by acquisition channel, segment, and time-to-claim)
- [ ] Risk appetite clearly documented — what risks will NOT be underwritten?
- [ ] Underwriting guidelines communicated to distribution channels
- [ ] Underwriting exception tracking and authority framework

### Pricing risk
- [ ] Rate adequacy analysis performed (current rates covering expected losses + expenses + profit?)
- [ ] Classification factors actuarially justified (correlated with loss experience, not prohibited factors)
- [ ] Disparate impact testing conducted for all rating factors
- [ ] Rate filing status tracked for every state
- [ ] Competitive position monitored (are rates in market relative to competitors with similar books?)

### Claims risk
- [ ] Claims reserving adequacy (case reserves + IBNR adequate?)
- [ ] Claims fraud detection integrated into FNOL and investigation workflow
- [ ] Claims handling compliant with unfair claims settlement practices acts
- [ ] Litigation risk monitored (claims with attorney representation, litigation rates by line/region)

### Distribution risk
- [ ] Producer licensing verified for all distribution channels
- [ ] Producer training on product — can they explain coverage accurately?
- [ ] Compensation structures compliant with state law and aligned with customer outcomes
- [ ] Concentration risk monitored — dependence on single distributor or channel?

### Regulatory risk
- [ ] Rate and form filing status tracked for all states and lines
- [ ] Market conduct exam history — any outstanding issues?
- [ ] Complaint ratios benchmarked (state average vs. your book)
- [ ] Regulatory change monitoring (NAIC model laws, state legislation, emerging AI regulation)

### Catastrophe risk
- [ ] Catastrophe modeling for property lines (hurricane, earthquake, flood, wildfire)
- [ ] Aggregate exposure limits — what is the maximum loss from a single event?
- [ ] Reinsurance coverage adequate for the modeled loss scenarios?
- [ ] Climate change impact on catastrophe frequency and severity incorporated?

## Decision Patterns

### Pattern: "Let's streamline the application — fewer questions, faster decisions."

Ask: what data are you NOT collecting, and what would it have told you? Every question removed from an application eliminates a data point used for risk classification. If you remove a question and the remaining data cannot distinguish good risks from bad risks, you are creating adverse selection — bad risks are more likely to apply when screening is lighter. The test: run the streamlined application on historical data. Does it produce the same classification as the full application? If not, what is the expected loss ratio impact?

### Pattern: "Let's automate this underwriting decision — the model is better than the underwriters."

Show the evidence. Where does the model disagree with underwriters? When the model is more conservative than underwriters, what do actual claims outcomes show? When the model is less conservative, what do actual claims outcomes show? Deploy the model as a recommendation, not a decision, for an observation period. Track override rates and outcomes. Increase automation as evidence justifies it. Transition, don't replace, human judgment.

### Pattern: "Let's offer a lower price to win business."

Know your loss cost before competing on price. Your loss cost is YOUR expected loss cost based on YOUR book, YOUR underwriting, YOUR claims management — not the market's loss cost. A competitor with better underwriting can profit at a price where you lose money. If your combined ratio is 105% and the competitor's is 95%, matching their price means doubling your loss.

### Pattern: "We'll use telematics/IoT data for better underwriting."

Promising, but check: (a) do customers understand what data is collected and how it is used?, (b) is the data collection compliant with state privacy laws?, (c) does the telematics data actually predict claims better than existing rating factors — is the incremental predictiveness worth the data collection cost?, (d) does the telematics score correlate with protected characteristics (e.g., driving patterns that differ by neighborhood)?

### Pattern: "Let's embed insurance in a partner's product flow."

Check carefully: (a) who is the producer? Is the partner licensed?, (b) what is the partner's role — referring (does not require license) or soliciting (requires license)?, (c) is the embedded flow clear that insurance is being offered — not misleading about who is providing coverage?, (d) does the embedded flow perform adequate underwriting, or is it optimized for conversion at the expense of risk selection?

## Failure Mode Check

| Failure Mode | Early Warning Sign | Mitigation |
|-------------|-------------------|------------|
| Underwriting without feedback loops | The team measures conversion and premium growth but not early claims indicators | Build claims feedback into product metrics: claims reported within 3, 6, 12 months of inception by underwriting cohort. |
| Ignoring adverse selection | Your highest conversion rates are in your riskiest segments | Compare risk profile of new applicants to existing book. Channel analysis: is this channel attracting risks you did not intend to underwrite? |
| Treating insurance as a UX problem | The product is beautiful but the combined ratio has not improved | Distinguish between distribution UX (conversion) and product economics (loss ratio, expense ratio). The most valuable work improves the combined ratio. |
| Automating bias | The model produces decisions that differ by protected characteristics — but "it's statistically valid" | Test for disparate impact BEFORE deployment. Use fairness metrics. Monitor fairness continuously in production. |
| Price-competing without knowing loss costs | Pricing is set to "be competitive" — at market rates — without knowing if rates cover your costs | Know your loss cost. Compete on value (coverage, service, claims) unless you have a structural cost advantage. |
| Selling DTC without screening for adverse selection | Direct channel conversion is 3x agent channel — celebration time | That 3x conversion may be adverse selection — people who cannot get coverage through agents are trying DTC. Check risk profiles. |
| Automating claims without detecting fraud | Claims processing speed is up, customer satisfaction is up — but fraud detection was an afterthought | Build fraud detection into FNOL and claims workflows. Speed is important; not paying fraudulent claims is more important. |

## Key Metrics

### Combined ratio = Loss Ratio + Expense Ratio
The fundamental profitability metric in insurance. Combined ratio below 100% = underwriting profit. Combined ratio above 100% = underwriting loss (investment income may still make the line profitable, but underwriting discipline has failed).

### Loss ratio = Incurred Losses / Earned Premium
Measures underwriting quality. Loss ratio by line, by segment, by channel, by underwriter, by rating factor. Monitored monthly but evaluated over 12-24 month development periods because claims develop over time.

### Expense ratio = Underwriting Expenses / Written Premium
Measures operational efficiency. Includes commissions, underwriting expenses, administrative costs, premium taxes. Target: drive below 30% for personal lines, below 35% for commercial lines. Technology should reduce expense ratio — if it does not, the business case is questionable.

### Policy retention / renewal rate
Higher retention is generally good — customer acquisition cost is amortized over a longer life. But check: are you retaining good risks and losing bad risks, or the reverse? If retention is high because good risks are leaving (your price is too high for them) and bad risks are staying (they cannot get better rates elsewhere), high retention is a warning sign.

### Quote-to-bind ratio
Measures conversion efficiency. Too high: may indicate under-screening (writing risks you should not). Too low: may indicate uncompetitive pricing, poor distribution experience, or agent-broker disengagement. Context matters.

### Claims satisfaction (Net Promoter Score)
CSAT after claims. Claims experience drives retention and word-of-mouth more than any other touchpoint. If claims NPS is significantly below policyholder NPS, claims is undermining the product.

## Language to Use

| Say This | Not This |
|----------|----------|
| "We need actuarial justification for this rating factor before we can use it in pricing." | "The model found this variable is predictive." |
| "What is the expected loss ratio impact of this underwriting change?" | "This will improve conversion." |
| "We should compare early claims emergence for the new underwriting to the existing book before scaling." | "The model works — let's roll it out." |
| "Does this telematics variable correlate with any protected characteristic?" | "More data always improves the model." |
| "We need rate filing preparation time in the product timeline." | "We'll handle the regulatory stuff after development." |
| "What is the combined ratio target for this product?" | "Is the product profitable?" |
| "We should design the claims FNOL to collect structured data for reserving while making it feel empathetic for the claimant." | "Claims is a cost center — automate it." |
| "Let's monitor the risk profile of this new distribution channel before scaling volume." | "The partnership is live — let's push volume." |
| "The agent is our user — we need to design for their workflow, not the policyholder's." (in agent-distributed lines) | "We're designing a great customer experience." |

## Quick Reference: Lines of Business

| Line | Key Metrics | Regulatory Intensity | Tech Adoption |
|------|-------------|---------------------|---------------|
| Personal Auto | Frequency × Severity, loss ratio by territory | High (mandatory coverage, rate regulation) | High (telematics, digital claims, comparison platforms) |
| Homeowners | Catastrophe exposure, protection class, replacement cost | Moderate-High (form-heavy, CAT concentration) | Medium (drone inspection, IoT, digital quoting) |
| Workers' Comp | Loss ratio by class code, experience mod, medical cost inflation | High (mandatory, bureau rates, state funds) | Medium (claims, provider networks, payroll integration) |
| Commercial P&C (small) | BOP package, class-based rating, retention | Moderate | Growing (digital platforms, instant quoting) |
| Commercial P&C (large) | Loss ratio by account, underwriting judgment, relationship retention | Moderate-Low | Low (bespoke underwriting, complex risk) |
| Life Insurance | Mortality vs. expected, lapse rates, expense ratio | High (reserve requirements, illustration regulation) | Growing (accelerated UW, digital platforms, no-med-exam) |
| Health Insurance | Medical loss ratio (MLR), risk adjustment, provider network | Highest (ACA, Medicare, Medicaid) | Medium (member portals, telehealth, claims) |
| Reinsurance | Combined ratio, capital efficiency, diversification | Moderate | Variable (modeling tools, placement platforms) |

## Top 5 Things Product Leaders Get Wrong in Insurance

1. They optimize for conversion without checking whether the additional applicants are good risks.
2. They automate underwriting without building the claims feedback loop that tells them whether the automation is working.
3. They treat insurance as a UX problem when the product is the coverage, the pricing, and the claims promise — UX is packaging.
4. They deploy ML models trained on historical data without testing for bias — and discover through regulatory action that the model encoded past discrimination.
5. They price to the market without knowing their own loss cost — and discover years later (when claims develop) that every policy was losing money.
