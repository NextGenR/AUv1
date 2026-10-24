"""
Module 3: Statutory Framework, MSMED Act & Classification Criteria (Q51 - Q75)
Focuses on MSMED Act 2006, 2020 Composite Criteria, Budget 2025-26 Limit Multipliers,
Exclusion of Exports, and Institutional Architecture.
"""

def get_questions():
    m = "Statutory Framework & Classification Limits"
    return [
        {
            "id": "MSME_051",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Easy",
            "question": "Under the revised composite classification criteria introduced on July 1, 2020, what two parameters are jointly used to classify an enterprise as Micro, Small, or Medium?\n1. Number of permanent full-time employees\n2. Investment in plant and machinery or equipment\n3. Annual turnover\n4. Electricity consumption in units\nSelect the correct answer using the code given below:",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1, 2 and 3 only",
                "D": "2, 3 and 4 only"
            },
            "correct_option": "B",
            "explanation": "Since the July 1, 2020 notification under the MSMED Act, India discarded the separate classification for manufacturing and service sectors and adopted a composite criteria based on two objective parameters: (1) Investment in Plant & Machinery/Equipment, and (2) Annual Turnover."
        },
        {
            "id": "MSME_052",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the 2020 composite definition thresholds for MSMEs:\n1. A Micro enterprise had investment up to ₹1 crore and turnover up to ₹5 crore.\n2. A Small enterprise had investment up to ₹10 crore and turnover up to ₹50 crore.\n3. A Medium enterprise had investment up to ₹50 crore and turnover up to ₹250 crore.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements accurately state the 2020 composite thresholds: Micro (₹1 Cr Inv / ₹5 Cr TO), Small (₹10 Cr Inv / ₹50 Cr TO), and Medium (₹50 Cr Inv / ₹250 Cr TO), maintaining a consistent 1:5 ratio between investment and turnover."
        },
        {
            "id": "MSME_053",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What critical rule applies to 'Exports of Goods and Services' when calculating the turnover of an enterprise for MSME classification under the MSMED regulations?",
            "options": {
                "A": "Export turnover is counted at double its invoice value",
                "B": "Export turnover is completely excluded from the calculation of annual turnover",
                "C": "Export turnover automatically disqualifies an enterprise from MSME status",
                "D": "Only agricultural exports are excluded while manufactured exports are included"
            },
            "correct_option": "B",
            "explanation": "To actively incentivize MSMEs to export without the fear of outgrowing their MSME classification and losing regulatory protections, the rules explicitly mandate that all export turnover of goods or services is excluded from the turnover ceiling."
        },
        {
            "id": "MSME_054",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "According to the Union Budget 2025-26 (PIB official release), by how much have the investment and turnover limits for MSME classification been increased?\n1. Investment limits have been increased by 2.5 times.\n2. Turnover limits have been increased by 2 times.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. The Budget 2025-26 officially raised the classification thresholds by 2.5 times for investment in plant and machinery/equipment, and by 2 times for annual turnover, specifically enabling MSMEs to scale operations without forfeiting government support."
        },
        {
            "id": "MSME_055",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Hard",
            "question": "Following the Budget 2025-26 revision (where investment limits increased by 2.5x and turnover by 2x), what are the revised ceilings for a 'Small Enterprise'?",
            "options": {
                "A": "Investment up to ₹15 crore and Turnover up to ₹75 crore",
                "B": "Investment up to ₹25 crore and Turnover up to ₹100 crore",
                "C": "Investment up to ₹50 crore and Turnover up to ₹200 crore",
                "D": "Investment up to ₹20 crore and Turnover up to ₹80 crore"
            },
            "correct_option": "B",
            "explanation": "Applying the Budget 2025-26 multipliers to the 2020 baseline for a Small Enterprise (previously ₹10 Cr investment and ₹50 Cr turnover): Investment ceiling = ₹10 Cr × 2.5 = ₹25 crore; Turnover ceiling = ₹50 Cr × 2 = ₹100 crore."
        },
        {
            "id": "MSME_056",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Hard",
            "question": "Following the Budget 2025-26 revision, what are the new classification ceilings for a 'Medium Enterprise'?",
            "options": {
                "A": "Investment up to ₹75 crore and Turnover up to ₹350 crore",
                "B": "Investment up to ₹100 crore and Turnover up to ₹400 crore",
                "C": "Investment up to ₹125 crore and Turnover up to ₹500 crore",
                "D": "Investment up to ₹150 crore and Turnover up to ₹600 crore"
            },
            "correct_option": "C",
            "explanation": "Applying the Budget 2025-26 multipliers to the 2020 baseline for a Medium Enterprise (previously ₹50 Cr investment and ₹250 Cr turnover): Investment ceiling = ₹50 Cr × 2.5 = ₹125 crore; Turnover ceiling = ₹250 Cr × 2 = ₹500 crore."
        },
        {
            "id": "MSME_057",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Hard",
            "question": "Following the Budget 2025-26 revision, what are the new classification ceilings for a 'Micro Enterprise'?",
            "options": {
                "A": "Investment up to ₹1.5 crore and Turnover up to ₹7.5 crore",
                "B": "Investment up to ₹2.0 crore and Turnover up to ₹8.0 crore",
                "C": "Investment up to ₹2.5 crore and Turnover up to ₹10.0 crore",
                "D": "Investment up to ₹3.0 crore and Turnover up to ₹12.0 crore"
            },
            "correct_option": "C",
            "explanation": "Applying the multipliers to the Micro baseline (previously ₹1 Cr investment and ₹5 Cr turnover): Investment ceiling = ₹1 Cr × 2.5 = ₹2.5 crore; Turnover ceiling = ₹5 Cr × 2 = ₹10.0 crore."
        },
        {
            "id": "MSME_058",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Prior to the 2020 reforms, how did the Micro, Small and Medium Enterprises Development (MSMED) Act 2006 classify enterprises?\n1. It maintained a strict separation between manufacturing enterprises and service enterprises.\n2. Manufacturing units were classified based on investment in plant and machinery, while service units were classified based on investment in equipment.\n3. Turnover was not a statutory classification criterion.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements accurately describe the pre-2020 framework under the MSMED Act 2006. Manufacturing and services had separate ceilings based solely on original acquisition cost of machinery/equipment, with turnover completely omitted, creating distortions as businesses added value."
        },
        {
            "id": "MSME_059",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "How is the value of 'Investment in Plant and Machinery or Equipment' verified for Udyam Registration?",
            "options": {
                "A": "Through physical on-site inspection by police authorities",
                "B": "Linked directly to the Written Down Value (WDV) as per Income Tax Return (ITR) filings",
                "C": "Through market value appraisals by private auction houses",
                "D": "Self-assessed without any PAN linkage"
            },
            "correct_option": "B",
            "explanation": "The Udyam registration system is directly integrated with the Central Board of Direct Taxes (CBDT) and Goods and Services Tax Network (GSTN). The investment value in plant and machinery is automatically pulled from the Written Down Value (WDV) at the end of the prior financial year as reported in the enterprise's filed Income Tax Return."
        },
        {
            "id": "MSME_060",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "In calculating the investment in plant and machinery for MSME classification, which of the following items are specifically excluded by statutory notification?\n1. Land and building\n2. Pollution control equipment\n3. Research and development equipment\n4. Industrial safety devices\nSelect the correct answer using the code given below:",
            "options": {
                "A": "1 only",
                "B": "1 and 2 only",
                "C": "2, 3 and 4 only",
                "D": "1, 2, 3 and 4"
            },
            "correct_option": "D",
            "explanation": "Statutory rules explicitly exclude the cost of land and building. Furthermore, under the MSMED calculation guidelines, investments in pollution control devices, research and development (R&D) machinery, and industrial safety devices are excluded to encourage enterprises to adopt green, safe, and innovative technology without breaching investment limits."
        },
        {
            "id": "MSME_061",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "If an enterprise satisfies the investment criterion of a 'Small' enterprise but its annual domestic turnover exceeds the 'Small' turnover ceiling and enters the 'Medium' range, how is the enterprise classified?",
            "options": {
                "A": "It remains classified as a Small enterprise",
                "B": "It is reclassified into the higher category as a Medium enterprise",
                "C": "It is disqualified from any MSME category and deemed a large corporation",
                "D": "It is given a three-year grace period during which it is classified as Micro"
            },
            "correct_option": "B",
            "explanation": "Under the composite criteria rules, if an enterprise crosses the ceiling limit specified for its present category in either of the two criteria of investment or turnover, it ceases to exist in that category and is placed in the next higher category."
        },
        {
            "id": "MSME_062",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the downward reclassification of an enterprise (e.g. from Medium to Small):\n1. An enterprise cannot be downgraded to a lower category even if its investment and turnover decline.\n2. An enterprise will be reclassified to a lower category only if both its investment and turnover fall below the ceilings of that lower category.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "B",
            "explanation": "Statement 2 is correct. To transition downward into a lower category, an enterprise must fall below the ceilings of BOTH criteria (investment and turnover). A drop in only one parameter does not trigger downward reclassification."
        },
        {
            "id": "MSME_063",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the official term for the permanent digital registration number issued to an enterprise upon successfully completing the Udyam portal registration?",
            "options": {
                "A": "Corporate Identity Number (CIN)",
                "B": "Udyam Registration Number (URN)",
                "C": "Permanent Account Number (PAN)",
                "D": "Director Identification Number (DIN)"
            },
            "correct_option": "B",
            "explanation": "Upon successful verification, the Ministry of MSME issues a dynamic electronic certificate containing a unique Udyam Registration Number (URN) with a dedicated QR code that can be verified in real time."
        },
        {
            "id": "MSME_064",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the integration of Udyam registration with other central databases:\n1. Udyam is fully integrated with the Income Tax (PAN) system.\n2. Udyam is fully integrated with the Goods and Services Tax Network (GSTN).\n3. Any change in an enterprise's turnover reported in GST returns automatically reflects in its MSME classification status.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. The Udyam Portal is dynamically synced with CBDT and GSTN. The system automatically fetches financial data annually to update enterprise classification without requiring the business owner to submit fresh paperwork."
        },
        {
            "id": "MSME_065",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "Which Ministry serves as the nodal administrative authority for formulating policies, programmes, and schemes for micro, small, and medium enterprises in India?",
            "options": {
                "A": "Ministry of Commerce and Industry",
                "B": "Ministry of Finance",
                "C": "Ministry of Micro, Small and Medium Enterprises",
                "D": "Ministry of Heavy Industries"
            },
            "correct_option": "C",
            "explanation": "The Ministry of Micro, Small and Medium Enterprises (M/o MSME) is the nodal central ministry responsible for designing policies, administering statutory acts (MSMED Act 2006), and implementing flagship schemes for the sector."
        },
        {
            "id": "MSME_066",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "With reference to the statutory National Board for Micro, Small and Medium Enterprises (NBMSME) established under the MSMED Act 2006, consider the following statements:\n1. The Union Minister in charge of the Ministry of MSME serves as its ex-officio Chairman.\n2. It reviews the factors affecting the promotion and development of MSMEs and recommends policy measures to the Central Government.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. Under Section 3 of the MSMED Act 2006, the Central Government establishes the National Board for MSME, chaired by the Union Minister of MSME, with members representing central ministries, state governments, industry associations, and the Reserve Bank of India."
        },
        {
            "id": "MSME_067",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Which statutory body constituted under the MSMED Act 2006 examines matters referred to it regarding classification criteria and recommendations under Section 7?",
            "options": {
                "A": "The Law Commission of India",
                "B": "The Advisory Committee on MSME",
                "C": "The Central Vigilance Commission",
                "D": "The Competition Commission of India"
            },
            "correct_option": "B",
            "explanation": "Section 7 of the MSMED Act 2006 mandates the constitution of an Advisory Committee, headed by the Secretary (MSME), to evaluate and advise the Central Government on classification criteria, thresholds, and development policies."
        },
        {
            "id": "MSME_068",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the mandatory nature of Udyam registration:\n1. Registration on the Udyam portal is completely free of charge.\n2. Enterprises are allowed to file multiple Udyam registrations for different branches under the same PAN.\n3. Having a valid PAN and Aadhaar is generally mandatory for Udyam registration.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "1 and 3 only",
                "C": "2 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "B",
            "explanation": "Statements 1 and 3 are correct: Udyam registration is 100% free of cost, and PAN and Aadhaar are required. Statement 2 is incorrect because the rules explicitly stipulate that only ONE Udyam Registration is permitted per enterprise/PAN; all branches and diverse activities must be included under that single registration."
        },
        {
            "id": "MSME_069",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the legal validity period of an Udyam Registration Certificate once issued by the Ministry of MSME?",
            "options": {
                "A": "Valid for exactly 3 years, requiring triennial renewal fees",
                "B": "Valid for lifetime of the enterprise unless suspended or cancelled",
                "C": "Valid for 5 years in urban areas and 10 years in rural areas",
                "D": "Valid on a financial-year basis, expiring on March 31 annually"
            },
            "correct_option": "B",
            "explanation": "An Udyam Registration Certificate is issued with permanent lifetime validity. It does not require periodic renewal, though its classification tier may dynamically upgrade or downgrade based on annual ITR and GSTN turnover filings."
        },
        {
            "id": "MSME_070",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding retail and wholesale trade under the MSMED Act:\n1. Retail and wholesale trades were historically included as MSMEs from the inception of the 2006 Act.\n2. In July 2021, the Government allowed retail and wholesale trade to register on Udyam, specifically restricting their benefits to Priority Sector Lending (PSL).\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "B",
            "explanation": "Statement 2 is correct. Retail and wholesale trades were previously excluded from MSMED registration. On July 2, 2021, the Ministry issued a notification permitting retail and wholesale traders to register on Udyam with benefits restricted primarily to Priority Sector Lending (PSL)."
        },
        {
            "id": "MSME_071",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What penalty provision exists under Section 27 of the MSMED Act 2006 for furnishing false information or failing to furnish mandatory information?",
            "options": {
                "A": "Immediate cancellation of all business licenses with no right to appeal",
                "B": "Imposition of fines on first conviction, and higher fines with possible imprisonment on subsequent convictions",
                "C": "Mandatory transfer of business ownership to a public sector enterprise",
                "D": "Deportation of the company directors"
            },
            "correct_option": "B",
            "explanation": "Section 27 of the MSMED Act 2006 prescribes statutory penalties for intentionally providing false information or failing to submit mandatory statistical returns, punishable with progressive monetary fines."
        },
        {
            "id": "MSME_072",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the calculation of turnover for an enterprise with multiple GSTINs registered under the same PAN:\n1. The turnover of each GSTIN is assessed completely independently to determine individual plant MSME status.\n2. The turnover and investment of all GSTINs linked to the same PAN are aggregated together to determine the overall classification of the enterprise.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "B",
            "explanation": "Statement 2 is correct. To prevent artificial fragmentation (splitting an enterprise into multiple small GSTINs to stay below thresholds), the rules mandate that all entities with the same Permanent Account Number (PAN) are treated as a single enterprise, and their total turnover and investment figures are aggregated."
        },
        {
            "id": "MSME_073",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Why did the Government raise the MSME classification thresholds in Budget 2025-26 by 2.5x for investment and 2x for turnover?",
            "options": {
                "A": "To reduce the total number of registered MSMEs in the country",
                "B": "To allow expanding enterprises to invest in modern capital machinery and increase sales without forfeiting priority credit and procurement benefits",
                "C": "To comply with mandatory directives issued by the International Monetary Fund",
                "D": "To force all medium enterprises to register on stock exchanges"
            },
            "correct_option": "B",
            "explanation": "The PIB Budget document highlights that increasing the investment and turnover limits by 2.5 times and 2 times allows businesses to scale operations, upgrade plant technology, hire workers, and improve operating efficiency without fear of losing critical MSME protections (such as collateral-free guarantees and public procurement quotas)."
        },
        {
            "id": "MSME_074",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "With reference to the National Digital Platform registration process specified in the Mindmap notes, consider the following statements:\n1. Registration on the Udyam National Digital Platform requires zero physical paperwork.\n2. It provides automatic integration with the MSME Samadhaan portal for delayed payments.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. The Udyam portal provides an end-to-end paperless registration workflow. Possessing an URN enables an enterprise to seamlessly log in and file delayed payment recovery applications on the statutory MSME Samadhaan portal."
        },
        {
            "id": "MSME_075",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Which of the following acts provides the overarching statutory foundation for the promotion, development, and enhancement of competitiveness of MSMEs in India?",
            "options": {
                "A": "The Companies Act, 2013",
                "B": "The Industries (Development and Regulation) Act, 1951",
                "C": "The Micro, Small and Medium Enterprises Development (MSMED) Act, 2006",
                "D": "The Insolvency and Bankruptcy Code, 2016"
            },
            "correct_option": "C",
            "explanation": "The Micro, Small and Medium Enterprises Development (MSMED) Act, 2006 is the principal parliamentary enactment providing for facilitating the promotion and development, enhancing the competitiveness of MSMEs, and establishing the dispute resolution mechanism for delayed payments."
        }
    ]
