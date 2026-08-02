# Financial Services Field Guide

## Quick Scan — Before Any Product Decision

Before committing to any product decision in financial services, answer these five questions. If you cannot answer all five with specificity, you are not ready to decide.

1. **Which regulator supervises this product area, and what would they examine?** Name the specific agency (OCC, Fed, CFPB, SEC, FINRA, FCA, ECB, etc.) and the specific regulation/framework they would examine against.
2. **Does this product contain or rely on a model?** If it uses a quantitative method for any decision (credit, fraud, pricing, risk), SR 11-7 or equivalent model governance applies. Model validation must review before deployment.
3. **What is the audit trail for every customer-impacting decision this product makes?** Can you reproduce any decision (loan approval, fraud flag, pricing determination) given the same inputs, and can you explain it to a regulator?
4. **Which control functions can veto this product?** Risk management, compliance, legal, model validation, information security, third-party risk management, audit — which ones have approval authority, and have they been engaged?
5. **What is the control burden budget for this product?** Estimate the ongoing cost of regulatory compliance, model validation, audit support, and regulatory reporting as a percentage of total product cost. If you cannot estimate it, you have not understood the product.

## Regulatory Triggers

Every feature, workflow, and data flow change must be checked against these triggers.

### You change a credit decision → ECOA/Regulation B adverse action notice requirements

Any change to how credit decisions are made must include the ability to generate specific, individualized reasons for decline. Black-box models require an explanation layer. Adverse action notices must be accurate for every decision.

### You add a data source → FCRA/GLBA/privacy regime triggers

Any new external data source used in consumer decisions implicates FCRA (if it is a consumer report), GLBA (if it involves financial data), GDPR (if it involves EU data), and/or CCPA (if it involves California data). Data sharing agreements, permissible purpose, and consumer disclosure obligations must be addressed before data flows begin.

### You introduce AI/ML → SR 11-7 model risk management

Any AI/ML system that produces quantitative outputs used in business decisions is a model. It requires: conceptual soundness documentation, development evidence (data, methodology, testing), independent validation, ongoing monitoring. Generative AI use cases that interact with customers face heightened regulatory scrutiny.

### You add a vendor → Third-party risk management

Any vendor that processes, stores, or transmits customer data or supports a significant business function requires third-party risk assessment: due diligence, contract provisions (audit rights, business continuity, data protection, termination assistance), ongoing monitoring, exit strategy.

### You touch payments → Sanctions screening, AML transaction monitoring

Any product that initiates, processes, or facilitates payments must include: sanctions screening (OFAC and other applicable lists), AML transaction monitoring, customer identification program (CIP/KYC), SAR filing capability.

### You change pricing → UDAAP/Consumer Duty, fair lending, usury limits

Any pricing change must be tested for: (a) unfair, deceptive, or abusive acts or practices (UDAAP), (b) fair lending / disparate impact (does pricing vary by protected characteristics?), (c) usury limits in all applicable jurisdictions, (d) fair value assessment (FCA Consumer Duty for UK products).

### You store or process data → Data protection, breach notification, data subject rights

Any product that stores personal data must: encrypt data at rest and in transit, support data subject requests (access, deletion, portability), comply with breach notification requirements (varies by jurisdiction — 72 hours under GDPR), maintain data retention and deletion policies.

## Stakeholder Map

| Stakeholder | What They Care About | Veto Power |
|-------------|---------------------|------------|
| **Business sponsor** | P&L, market share, competitive position | Approves funding |
| **Risk management** | Risk exposure (credit, market, operational), risk limits, risk appetite alignment | Can block products that exceed risk appetite |
| **Compliance** | Regulatory compliance, regulatory change management, examination readiness | Can block products with unresolved compliance issues |
| **Legal** | Contractual obligations, litigation risk, regulatory interpretation | Can block products with legal risk |
| **Model validation** | Model soundness, documentation, testing, ongoing monitoring | Can reject models — effectively blocking model-driven products |
| **Information security** | Security controls, vulnerability management, access management, data protection | Can block products with security gaps |
| **Third-party risk management** | Vendor risk, concentration risk, exit strategy | Can block products dependent on unapproved vendors |
| **Internal audit** | Control environment, process documentation, issue remediation | Can issue findings that require remediation; findings affect management ratings |
| **Finance/Treasury** | Capital consumption, liquidity impact, P&L attribution, transfer pricing | Can block products that consume excessive capital |
| **Regulator (external)** | Safety and soundness, consumer protection, market integrity | Can issue enforcement actions, restrict activities, revoke charters |

When any stakeholder with veto power is not engaged, you have execution risk — not because the stakeholder is unreasonable, but because you are asking them to absorb risk they have not evaluated.

## Risk Checklist

### Credit risk
- [ ] Expected loss (PD × LGD × EAD) modeled for the product
- [ ] Credit underwriting standards defined and documented
- [ ] Portfolio concentration limits defined (single name, industry, geography)
- [ ] Provisioning impact under CECL/IFRS 9 assessed
- [ ] Credit monitoring and early warning indicators designed
- [ ] Collections and loss mitigation process defined

### Market risk
- [ ] Interest rate risk exposure quantified
- [ ] FX risk exposure quantified (if multi-currency)
- [ ] VaR/ES framework applicable to the product
- [ ] Counterparty credit risk identified and limited

### Operational risk
- [ ] Process failures identified and controls designed
- [ ] System availability requirements defined (RTO/RPO)
- [ ] Incident management process established
- [ ] Business continuity and disaster recovery tested

### Compliance risk
- [ ] Applicable regulations identified (not generically — specifically)
- [ ] Regulatory reporting requirements defined
- [ ] Compliance testing plan established
- [ ] Regulatory change monitoring process in place

### Conduct risk
- [ ] Fairness assessment (UDAAP, Consumer Duty, fair lending)
- [ ] Suitability framework (if product involves recommendations)
- [ ] Vulnerable customer accommodations
- [ ] Complaint handling process designed

### Model risk
- [ ] Model inventory entry created
- [ ] Model documentation initiated during development
- [ ] Independent validation scheduled before deployment
- [ ] Ongoing monitoring plan (drift detection, performance metrics)
- [ ] Model retirement/change management process defined

### Cyber risk
- [ ] Penetration testing completed
- [ ] Vulnerability management process established
- [ ] Access controls implemented (least privilege, MFA)
- [ ] Data encryption (at rest and in transit)
- [ ] Incident response plan tested

### Third-party risk
- [ ] Vendor due diligence completed
- [ ] Contract includes regulatory-required provisions
- [ ] Vendor risk tier assigned (critical, significant, routine)
- [ ] Exit strategy defined (if vendor fails)
- [ ] Ongoing monitoring plan established

## Decision Patterns

### Pattern: "Should we ship this feature faster or get compliance review first?"

Always get compliance review first. The cost of retrospective compliance — rebuilding the feature, remediating customer-impacting issues, responding to regulatory examination questions — is 3-10x the cost of upfront compliance. The feature that ships 2 weeks late because of compliance review is 2 weeks late. The feature that ships without compliance review and creates a regulatory finding is a multi-quarter problem.

### Pattern: "The model is good enough — can we skip validation this cycle?"

No. Model validation is a regulatory requirement, not a quality preference. A model that is deployed without validation is a finding. The finding will require retrospective validation — which will take longer and be more painful than prospective validation because the model is already in production affecting customers.

### Pattern: "The vendor has great technology but won't share their model documentation."

Walk away. If the vendor cannot provide documentation sufficient for independent validation, the model cannot be used. Vendor pushback on model documentation is a red flag — it means the vendor either does not understand financial services requirements or is unwilling to meet them. Either is disqualifying.

### Pattern: "Let's A/B test the pricing change."

You cannot A/B test pricing changes in financial services without careful design. Differential pricing across test groups may violate fair lending requirements if the test groups differ in protected characteristics. Any pricing test requires: (a) legal and compliance pre-approval of the test design, (b) fairness assessment of the test groups, (c) a plan for equalization (compensating the disadvantaged group) or the test is structured to avoid differential treatment (e.g., geographies rather than individuals as test units).

### Pattern: "We'll use AI to make this decision."

Start with: "Is this decision explainable? Is this decision auditable? Is this decision fair?" If the AI/ML approach cannot meet these three requirements, it is not suitable for the use case. Accept that some financial decisions will use simpler, more transparent models (GLMs, decision trees, rule engines) because explainability and auditability are non-negotiable.

## Failure Mode Check

| Failure Mode | Early Warning Sign | Mitigation |
|-------------|-------------------|------------|
| Ignoring control burden | Product timeline has no line items for compliance review, model validation, or legal review | Build the control timeline before the product timeline. Every review gate is a milestone. |
| Treating compliance as a checkbox | Compliance is listed as a final step before launch | Include compliance and legal stakeholders in product design from Day 1. Design for compliance, not compliance after design. |
| Underestimating integration complexity | Integration plan is a single line: "Integrate with bank systems" | Map every system, every data flow, every security boundary, every process handoff. Estimate integration effort based on actual complexity. |
| Building for users, ignoring control functions | User adoption is high but control functions have not been briefed | Map every stakeholder with veto power. Design features for their requirements — auditability, explainability, monitoring, documentation. |
| Pricing without understanding full cost stack | The product is priced "competitively" — meaning at market rates without knowing if rates cover costs | Build a full unit economics model including cost of funds, expected credit losses, provision impact, capital charge, operational costs, and control burden. |
| Confusing fintech speed with bank safety | Frequent production changes without corresponding control rigor | Speed and safety are designed together. Invest in automated testing, continuous compliance monitoring, pre-approved change patterns, model governance automation. |

## Key Metrics

Standard SaaS metrics (DAU, NPS, churn) still matter but are insufficient. Add these:

### Risk-adjusted return metrics
- **Risk-adjusted return on capital (RAROC):** Return divided by economic capital required. The core profitability metric in banking. If RAROC < hurdle rate, the product does not cover its cost of capital.
- **Loss ratio (for lending products):** Actual losses / expected losses. Deviation from 100% indicates underwriting model performance. Above 100%: underpricing or under-reserving.
- **Net interest margin (NIM):** For deposit and lending products. Measures the spread between asset yield and funding cost.

### Control metrics
- **Audit findings:** Open findings, overdue remediations, severity. Leading indicator of regulatory risk.
- **Model performance drift:** PSI, CSI, or equivalent. Early warning of model degradation.
- **Regulatory exam cycle:** When is the next exam? What are the focus areas? Exams should not surprise the product team.
- **Complaint volume and trends:** CFPB complaints, internal complaints classified by root cause. Leading indicator of conduct risk.

### Operational metrics
- **Availability:** Is the product meeting its availability target? (Often 99.99%+)
- **Incident count and severity:** Operational incidents with customer impact or regulatory reportability.
- **Reconciliation breaks:** Number and dollar value of unreconciled items. Leading indicator of operational control quality.

## Language to Use

| Say This | Not This |
|----------|----------|
| "We need to engage model validation during development so they can review the documentation incrementally." | "We'll get model validation to sign off when it's done." |
| "The product's risk-weighted asset consumption is X, and we project a RAROC of Y." | "The unit economics look good." |
| "We need adverse action reason codes for every decision path." | "The customer will get an email if they're declined." |
| "Let's map the regulatory framework for this product — OCC, CFPB, state-level, and any applicable EU/UK regimes." | "We're regulated — compliance handles that." |
| "The control burden for this product is approximately X% of total cost, which is within our target range." | "Compliance will slow us down but we'll deal with it." |
| "What is the audit trail for this decision? Can we reproduce it?" | "The system made the decision — it's automated." |
| "We should structure this as a phased rollout with model monitoring before full deployment." | "Ship it and see what happens." |
| "This vendor's model documentation is insufficient for independent validation." | "The vendor's ML is best-in-class." |

## Quick Reference: Regulatory Frameworks by Domain

| Domain | US Key Frameworks | EU/UK Key Frameworks | Product Impact |
|--------|------------------|---------------------|----------------|
| Consumer lending | ECOA/Reg B, FCRA, TILA/Reg Z, UDAAP | Consumer Credit Directive, FCA Consumer Duty | Adverse action, disclosure, fairness |
| Deposits | Reg DD (Truth in Savings), Reg E (EFT), GLBA | PSD2, Deposit Guarantee Schemes Directive | Disclosures, fraud liability, data sharing (open banking) |
| Payments | Reg E, Reg J, Durbin Amendment | PSD2, SEPA, Wire Transfer Regulation | Fraud liability, interchange, open banking APIs |
| Investments | Securities Act, Exchange Act, Reg BI, FINRA rules | MiFID II, PRIIPs, UCITS | Suitability, disclosure, best execution |
| Trading/Capital Markets | Dodd-Frank, Volcker Rule, SEC Reg ATS | MiFID II/MiFIR, MAR, EMIR | Market structure, trade reporting, clearing |
| Wealth Management | Investment Advisers Act, ERISA, Reg BI | MiFID II, IDD | Fiduciary duty, suitability, fee transparency |
| AML/Sanctions | BSA, USA PATRIOT Act, OFAC | AMLD6, EU Sanctions | KYC/CIP, transaction monitoring, SAR/STR filing |
| Privacy | GLBA, CCPA, state laws | GDPR | Data rights, breach notification, cross-border transfers |
| Model Risk | SR 11-7, OCC 2011-12 | ECB TRIM, PRA SS3/18 | Model documentation, validation, monitoring |
| Operational Resilience | NYDFS Part 500, interagency guidance | DORA, NIS2 | ICT risk, incident reporting, testing, third-party risk |
| Capital | Basel III/IV (US rules), Dodd-Frank CCAR | CRR/CRD, Basel III | RWA calculation, stress testing, capital planning |
