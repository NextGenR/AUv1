"""
Module 4: Delayed Payments, Dispute Resolution & Section 43B(h) (Q76 - Q100)
Focuses on MSMED Act Sections 15-19, MSEFC Conciliation & Arbitration, 75% / 50% Pre-deposit,
TReDS Onboarding for CPSEs, MSME Samadhaan, and Section 43B(h) Income Tax disallowance.
"""

def get_questions():
    m = "Delayed Payments & Dispute Resolution"
    return [
        {
            "id": "MSME_076",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "Under Section 15 of the MSMED Act 2006, what is the maximum statutory period allowed for a buyer to make payment to an MSE supplier where there is a written agreement between the parties?",
            "options": {
                "A": "30 days from delivery",
                "B": "45 days from the day of acceptance",
                "C": "60 days from invoice generation",
                "D": "90 days from dispatch"
            },
            "correct_option": "B",
            "explanation": "Section 15 of the MSMED Act stipulates that in no case shall the agreed period of payment between the buyer and the supplier exceed 45 days from the day of acceptance or the day of deemed acceptance of goods or services."
        },
        {
            "id": "MSME_077",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "If there is NO written agreement between the buyer and the MSE supplier, what is the statutory deadline (the 'appointed day') for making payment under the MSMED Act 2006?",
            "options": {
                "A": "Within 7 days",
                "B": "Within 15 days following the day of acceptance",
                "C": "Within 30 days",
                "D": "Within 45 days"
            },
            "correct_option": "B",
            "explanation": "Where there is no explicit written agreement between the buyer and supplier, the statutory payment deadline defaults to the 'appointed day', which is defined as the day following immediately after the expiry of the period of 15 days from the day of acceptance."
        },
        {
            "id": "MSME_078",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Regarding the penal interest payable on delayed payments under Section 16 of the MSMED Act 2006, consider the following statements:\n1. The buyer is liable to pay compound interest with monthly rests to the supplier.\n2. The interest rate is fixed at three times the Bank Rate notified by the Reserve Bank of India.\n3. The penal interest paid by the buyer can be deducted as an allowable business expense under the Income Tax Act.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "A",
            "explanation": "Statements 1 and 2 are correct. Section 16 mandates compound interest at 3 times the RBI Bank Rate with monthly rests. Statement 3 is incorrect because Section 23 of the MSMED Act explicitly forbids the buyer from claiming this penal interest as a deductible business expenditure under the Income Tax Act."
        },
        {
            "id": "MSME_079",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Which statutory quasi-judicial authority is established at the state/district level under the MSMED Act 2006 to adjudicate delayed payment disputes between buyers and MSEs?",
            "options": {
                "A": "National Company Law Tribunal (NCLT)",
                "B": "Micro and Small Enterprises Facilitation Council (MSEFC)",
                "C": "Debt Recovery Tribunal (DRT)",
                "D": "District Consumer Disputes Redressal Commission"
            },
            "correct_option": "B",
            "explanation": "Under Section 20 of the MSMED Act 2006, State Governments establish Micro and Small Enterprises Facilitation Councils (MSEFCs) to hear and resolve claims related to delayed payments and penal interest."
        },
        {
            "id": "MSME_080",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "According to the dispute resolution timeline specified in the MSMED statutory framework and Mindmap notes, consider the following statements:\n1. The MSEFC must first conduct conciliation / mediation, which is mandated to be completed within 90 days.\n2. If conciliation fails, the dispute is taken up for arbitration, with procedural guidelines aiming for completion within 30 days.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. The statutory framework sets a 90-day time limit for conciliation proceedings. If conciliation is unsuccessful, the council initiates arbitration or refers it to an alternative dispute resolution center with an accelerated target completion time of 30 days."
        },
        {
            "id": "MSME_081",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Hard",
            "question": "Under Section 19 of the MSMED Act 2006, what pre-deposit requirement is mandated before any court can entertain an application by a buyer to set aside an MSEFC arbitral decree?",
            "options": {
                "A": "10% of the awarded amount",
                "B": "25% of the awarded amount",
                "C": "50% of the awarded amount",
                "D": "75% of the awarded amount"
            },
            "correct_option": "D",
            "explanation": "Section 19 of the MSMED Act 2006 mandates that no application for setting aside any decree, award or order made by an MSEFC or arbitrator shall be entertained by any court unless the appellant (buyer) deposits 75% of the awarded amount with the court."
        },
        {
            "id": "MSME_082",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "In recent reform proposals and the MSMED Amendment discourse highlighted in the Mindmap notes, what adjustment is discussed regarding the pre-deposit requirement for challenging arbitral awards?\n1. Reducing the onerous pre-deposit threshold to 50% of the awarded amount to balance dispute resolution and appeal access.\n2. Eliminating the pre-deposit requirement completely for all private corporate buyers.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "A",
            "explanation": "Statement 1 is correct. The Mindmap notes ('50% of the awarded amount -> dispute resolution') reference proposed amendments to calibrate the pre-deposit requirement from 75% to 50% to rationalize dispute resolution while still discouraging frivolous appeals."
        },
        {
            "id": "MSME_083",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Which dedicated electronic portal was established by the Ministry of MSME to enable micro and small enterprises to register and track complaints against delayed payments by buyers and CPSEs?",
            "options": {
                "A": "MSME Sambandh",
                "B": "MSME Samadhaan",
                "C": "MSME Sampark",
                "D": "e-Sanjeevani"
            },
            "correct_option": "B",
            "explanation": "The MSME Samadhaan Portal is the dedicated digital platform where registered MSEs can file applications online against buyers for non-payment of dues. It provides real-time transparency and tracking of cases handled by state MSEFCs."
        },
        {
            "id": "MSME_084",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "With reference to Section 43B(h) of the Income Tax Act, 1961, consider the following statements:\n1. It was introduced to enforce timely payments to Micro and Small enterprises within the limits specified in the MSMED Act (15 to 45 days).\n2. If payment is not made within the statutory timeline, the buyer cannot claim the expenditure as a tax deduction in that financial year.\n3. Section 43B(h) applies equally to Medium enterprises and wholesale/retail traders.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "A",
            "explanation": "Statements 1 and 2 are correct. Section 43B(h) disallows deduction of expenditure incurred on purchases from MSEs unless payment is made within the MSMED Act deadlines (15 or 45 days). Statement 3 is incorrect because Section 43B(h) applies ONLY to Micro and Small enterprises (MSEs), NOT Medium enterprises, and does not apply to traders."
        },
        {
            "id": "MSME_085",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Under Section 43B(h) of the Income Tax Act, when does an enterprise get a tax deduction for an overdue expense that was disallowed in the prior year due to non-payment within 45 days?",
            "options": {
                "A": "The deduction is permanently forfeited and can never be claimed",
                "B": "In the previous year through an amended tax return",
                "C": "In the subsequent financial year in which the payment is actually made",
                "D": "After paying a 50% penalty to the Ministry of MSME"
            },
            "correct_option": "C",
            "explanation": "Section 43B operates on an actual payment basis. If an expense is disallowed in Year 1 because it remained unpaid beyond the 45-day window as of March 31, the deduction is not permanently lost—it is allowed in the subsequent financial year in which the payment is actually cleared."
        },
        {
            "id": "MSME_086",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the unintended market distortion known as 'Fear of Business Loss' resulting from Section 43B(h):\n1. Large buyers may cancel purchase orders from registered MSEs to avoid the rigid 45-day cash outflow mandate.\n2. Large buyers may shift procurement toward unregistered suppliers, large non-MSME corporations, or medium enterprises where the 45-day rule does not apply.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements describe the unintended market distortion reported in industry notes: to maintain working capital flexibility (often 90-120 day payment cycles), some corporate buyers choose to procure from large corporations, Medium enterprises, or unregistered units rather than registered MSEs subject to Section 43B(h)."
        },
        {
            "id": "MSME_087",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the primary role of the Trade Receivables Discounting System (TReDS) in tackling delayed payments?",
            "options": {
                "A": "It mandates that all MSME invoices are converted into sovereign debt guarantees",
                "B": "It operates an electronic platform where MSE trade invoices are competitively discounted by banks and financiers at transparent market rates without waiting for buyer payment",
                "C": "It acts as a court of law to issue arrest warrants against corporate buyers",
                "D": "It provides free insurance for imported industrial machinery"
            },
            "correct_option": "B",
            "explanation": "TReDS is an institutional auction platform regulated by the Reserve Bank of India. Once a buyer uploads/accepts an MSE supplier's invoice on TReDS, multiple financiers bid against each other to discount the invoice, giving the MSE immediate liquidity while the financier collects payment from the buyer on the due date."
        },
        {
            "id": "MSME_088",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Regarding the mandatory onboarding on the TReDS platform as mandated by the Government of India, consider the following statements:\n1. All Central Public Sector Enterprises (CPSEs) are mandatorily required to onboard onto the TReDS platform.\n2. All corporate entities with a minimum turnover threshold (specified under relevant notifications) are required to onboard onto TReDS.\n3. Onboarding on TReDS is compulsory for agricultural farmers.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "A",
            "explanation": "Statements 1 and 2 are correct. The Ministry of MSME made it mandatory for all CPSEs and companies with a prescribed turnover threshold to register on TReDS platforms to ensure seamless invoice discounting for MSE vendors. Farmers are not subject to TReDS corporate onboarding mandates."
        },
        {
            "id": "MSME_089",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "How does invoice financing on TReDS protect MSE suppliers against the default risk of large corporate buyers?",
            "options": {
                "A": "Financing on TReDS is typically executed on a 'Without Recourse' basis to the MSE supplier",
                "B": "The MSE supplier is held personally liable for the corporate buyer's default",
                "C": "The Central Government directly writes off the buyer's balance sheet",
                "D": "The supplier forfeits their factory machinery to the financier"
            },
            "correct_option": "A",
            "explanation": "Factoring and invoice discounting on TReDS is executed on a 'without recourse' basis to the MSE seller. Once the invoice is discounted and funds are disbursed to the MSE, the financier collects directly from the buyer; if the buyer defaults, the financier cannot recover the funds from the MSE supplier."
        },
        {
            "id": "MSME_090",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the integration of Government e-Marketplace (GeM) with TReDS:\n1. It enables automated creation of invoices from GeM orders directly onto the TReDS platform.\n2. It accelerates working capital realization for small businesses supplying goods to public sector departments.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. The GeM-TReDS integration links public procurement contracts directly to invoice discounting, allowing government suppliers to convert accepted public procurement bills into instant cash liquidity through participating financial institutions."
        },
        {
            "id": "MSME_091",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Can an enterprise categorized as a 'Medium Enterprise' file an application for recovery of delayed payments before the Micro and Small Enterprises Facilitation Council (MSEFC)?",
            "options": {
                "A": "Yes, Medium enterprises have equal rights under Sections 17 and 18 of the MSMED Act",
                "B": "No, the statutory delayed payment provisions under the MSMED Act apply exclusively to Micro and Small Enterprises (MSEs)",
                "C": "Yes, but only if the dispute amount exceeds ₹100 crore",
                "D": "Yes, provided they pay a 10% processing fee to the State Government"
            },
            "correct_option": "B",
            "explanation": "The statutory protections for delayed payments (Sections 15 to 25 of the MSMED Act 2006), including the right to approach the MSEFC, apply strictly to 'Micro and Small Enterprises' (MSEs). Medium enterprises cannot file delayed payment references under the MSMED Act."
        },
        {
            "id": "MSME_092",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding disclosure requirements in the annual balance sheet of a corporate buyer under Section 22 of the MSMED Act 2006:\n1. The buyer must disclose the principal amount and interest due to MSE suppliers remaining unpaid at the end of each accounting year.\n2. The buyer must disclose the amount of interest accrued and remaining unpaid at the end of the year.\n3. The company's statutory auditors must verify and report these MSME unpaid dues.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. Section 22 of the MSMED Act mandates that buyers who are required to get their accounts audited under any law must explicitly disclose in their annual statements: principal and interest unpaid to MSEs, interest paid, and cumulative interest accrued and unpaid."
        },
        {
            "id": "MSME_093",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the jurisdiction of an MSEFC to entertain a delayed payment reference from a supplier?",
            "options": {
                "A": "Jurisdiction is determined by the location of the corporate buyer's registered headquarters",
                "B": "Jurisdiction is determined by the location of the MSE supplier within whose territorial jurisdiction the supplier is located",
                "C": "Jurisdiction is determined exclusively by the Supreme Court of India",
                "D": "The supplier can only file in the High Court of Delhi"
            },
            "correct_option": "B",
            "explanation": "Under Section 18(4) of the MSMED Act 2006, the MSEFC located in the area where the supplier is located has the statutory jurisdiction to act as arbitrator or conciliation center, protecting small local suppliers from having to litigate in distant buyer jurisdictions."
        },
        {
            "id": "MSME_094",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the provisions of the Arbitration and Conciliation Act, 1996, in relation to the MSMED Act 2006:\n1. The provisions of the Arbitration and Conciliation Act, 1996 apply to conciliation and arbitration proceedings conducted by the MSEFC.\n2. The statutory provisions of the MSMED Act override any private contract between the parties that specifies a different arbitration venue or procedure.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. Section 18 of the MSMED Act incorporates the Arbitration and Conciliation Act, 1996. The Supreme Court has repeatedly held that the MSMED Act, being special legislation with an overriding non-obstante clause (Section 24), supersedes any private arbitration agreements between the parties."
        },
        {
            "id": "MSME_095",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Why is the 90-day mediation provision highlighted in the Mindmap notes critical for MSME supplier-buyer relationships?",
            "options": {
                "A": "It mandates the immediate closure of the buyer's business",
                "B": "It offers an informal, fast-track, non-adversarial mechanism to resolve billing disputes without destroying ongoing business relationships",
                "C": "It requires the supplier to waive 90% of their outstanding payments",
                "D": "It forces all disputes to be handled by international commercial courts"
            },
            "correct_option": "B",
            "explanation": "Litigation often ruptures business commercial relationships permanently. The statutory 90-day conciliation/mediation process gives suppliers and buyers a neutral forum to reach mutually acceptable settlement terms and structured payment schedules without the expense and hostility of protracted court trials."
        },
        {
            "id": "MSME_096",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the 'Securitisation of Trade Receivables' proposed to assist MSME liquidity:\n1. It will enable trade receivables on TReDS to be bundled into tradeable debt instruments for institutional investors.\n2. It expands liquidity beyond commercial banks to insurance companies and pension funds.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct as outlined in the ForumIAS policy notes. By converting discounted trade receivables into standardized securities, large institutional pools of capital (insurance, pension, mutual funds) can invest in MSME working capital debt, lowering borrowing costs for the entire ecosystem."
        },
        {
            "id": "MSME_097",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the consequence under the MSMED Act if an MSE supplier fails to file an Udyam registration before entering into a transaction with a buyer?",
            "options": {
                "A": "The supplier cannot claim the statutory delayed payment benefits under Chapter V of the MSMED Act for transactions executed prior to registration",
                "B": "The supplier is barred from doing business in India",
                "C": "The buyer is exempt from paying for the goods delivered",
                "D": "The supplier's goods are impounded by customs authorities"
            },
            "correct_option": "A",
            "explanation": "The Supreme Court of India (Silpi Industries case) affirmed that to claim the statutory benefits of the MSMED Act (including penal interest and MSEFC references), an enterprise must have been registered under the MSMED Act/Udyam as on the date of entering into the contract of supply."
        },
        {
            "id": "MSME_098",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the non-obstante clause in Section 24 of the MSMED Act 2006:\n1. The provisions of Sections 15 to 23 of the MSMED Act have overriding effect over anything inconsistent contained in any other law for the time being in force.\n2. A corporate buyer cannot use clauses in its private purchase orders to contract out of the 45-day payment deadline.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. Section 24 provides an explicit non-obstante clause, meaning statutory delayed payment rights take precedence over any inconsistent provisions in general contract law or private purchase orders."
        },
        {
            "id": "MSME_099",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Under the MSME Samadhaan workflow, who reviews the delayed payment application filed by an MSE?",
            "options": {
                "A": "The Reserve Bank of India Governor",
                "B": "The respective State/UT Micro and Small Enterprises Facilitation Council (MSEFC)",
                "C": "The Central Board of Direct Taxes",
                "D": "The International Court of Arbitration"
            },
            "correct_option": "B",
            "explanation": "The MSME Samadhaan portal routes applications directly to the respective State or UT MSEFC having jurisdiction over the MSE supplier for examination, issuance of notice to the buyer, conciliation, and subsequent arbitration if needed."
        },
        {
            "id": "MSME_100",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding delayed payments as a macro-economic impediment:\n1. Delayed payments tie up scarce working capital, preventing MSMEs from honoring payroll, purchasing raw materials, and investing in upgrades.\n2. Chronic delays trigger cascading defaults across supply chains, turning otherwise solvent manufacturing units into Non-Performing Assets (NPAs).\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. Working capital liquidity is the lifeblood of small business. When receivables are held up for 90 to 180 days by large buyers, MSMEs cannot service bank loans, leading to working capital starvation, supplier distress, and cascading insolvency."
        }
    ]
