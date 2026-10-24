"""
Module 7: PMEGP, SFURTI, Public Procurement Policy & RAMP (Q151 - Q175)
Focuses on PMEGP ceilings (₹50L mfg / ₹20L service, 15/25/35% subsidies, geo-tagging, 2-day EDP),
SFURTI (513 approved, 376 functional, ₹1,336 cr grant, 2.2L artisans),
Public Procurement Policy (25% mandate, 4% SC/ST, 3% women, 358 items, ₹74,717 cr achieved in 2023-24).
"""

def get_questions():
    m = "PMEGP, SFURTI & Public Procurement Policy"
    return [
        {
            "id": "MSME_151",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "What is the maximum admissible project cost for setting up a new enterprise in the manufacturing sector under the Prime Minister's Employment Generation Programme (PMEGP)?",
            "options": {
                "A": "₹10 lakh",
                "B": "₹25 lakh",
                "C": "₹50 lakh",
                "D": "₹1 crore"
            },
            "correct_option": "C",
            "explanation": "Under PMEGP, the maximum project cost admissible for establishing a new unit in the manufacturing sector is ₹50 lakh (raised from the earlier ₹25 lakh ceiling), while for the service sector it is ₹20 lakh."
        },
        {
            "id": "MSME_152",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "What is the maximum admissible project cost for setting up a new enterprise in the service sector under PMEGP?",
            "options": {
                "A": "₹10 lakh",
                "B": "₹20 lakh",
                "C": "₹35 lakh",
                "D": "₹50 lakh"
            },
            "correct_option": "B",
            "explanation": "Under PMEGP guidelines, the maximum admissible project cost for setting up a new business in the service or business sector is ₹20 lakh."
        },
        {
            "id": "MSME_153",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the margin money subsidy rates under PMEGP for General Category applicants:\n1. 15% of the project cost in urban areas.\n2. 25% of the project cost in rural areas.\n3. The beneficiary's own contribution is 10% of the project cost.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. For General Category applicants under PMEGP, the beneficiary contributes 10% of the project cost as equity, while the Government provides a margin money subsidy of 15% in urban areas and 25% in rural areas."
        },
        {
            "id": "MSME_154",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the subsidy structure under PMEGP for Special Category beneficiaries (SC, ST, OBC, Women, Transgenders, etc.):\n1. The margin money subsidy is 25% in urban areas.\n2. The margin money subsidy is 35% in rural areas.\n3. The beneficiary's own contribution is restricted to only 5% of the project cost.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. For Special Categories, the required beneficiary contribution is reduced to just 5%, while the Government provides an enhanced margin money subsidy of 25% in urban areas and 35% in rural areas."
        },
        {
            "id": "MSME_155",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Which of the following groups/regions were specifically included in the 'Special Category' under PMEGP in recent developments as noted by PIB?\n1. Units in Aspirational Districts\n2. Transgenders\n3. High-Net-Worth Individuals\nSelect the correct answer using the code given below:",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "A",
            "explanation": "The official PIB document highlights that in a notable recent development, units located in Aspirational Districts and Transgender entrepreneurs have been explicitly incorporated into the Special Category to access enhanced 25%/35% subsidies."
        },
        {
            "id": "MSME_156",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What technological innovation has been initiated for PMEGP units to capture product details and create direct market linkages as per official notes?",
            "options": {
                "A": "Mandatory installation of facial recognition CCTV cameras",
                "B": "Geo-tagging of all funded PMEGP units",
                "C": "Issuance of cryptocurrency tokens",
                "D": "Satellite tracking of daily worker attendance"
            },
            "correct_option": "B",
            "explanation": "As cited in the PIB document, geo-tagging of PMEGP units has been initiated to capture the exact physical location, product details, and production capacities of units, facilitating traceability, quality monitoring, and market linkages."
        },
        {
            "id": "MSME_157",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What training is provided free of cost to prospective entrepreneurs under PMEGP before or after project sanction?",
            "options": {
                "A": "6-month full-time polytechnic diploma",
                "B": "2-day free Entrepreneurship Development Programme (EDP) training",
                "C": "Foreign language proficiency certification",
                "D": "Military tactical training"
            },
            "correct_option": "B",
            "explanation": "Prospective entrepreneurs under PMEGP receive a free 2-day Entrepreneurship Development Programme (EDP) training to equip them with foundational business planning, accounting, and compliance knowledge."
        },
        {
            "id": "MSME_158",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "According to the official PIB achievements for PMEGP in 2023-24, consider the following statements:\n1. PMEGP supported 89,118 micro-enterprises across various sectors.\n2. The scheme disbursed ₹3,093.87 crore as margin money subsidy.\n3. It generated an estimated 7,12,944 employment opportunities.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are exact achievements recorded in the PIB document for FY 2023-24: 89,118 enterprises supported, ₹3,093.87 crore margin money subsidy disbursed, generating 7,12,944 jobs."
        },
        {
            "id": "MSME_159",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "Which statutory organization serves as the single National Nodal Agency for implementing PMEGP at the national level?",
            "options": {
                "A": "National Small Industries Corporation (NSIC)",
                "B": "Khadi and Village Industries Commission (KVIC)",
                "C": "Small Industries Development Bank of India (SIDBI)",
                "D": "National Bank for Agriculture and Rural Development (NABARD)"
            },
            "correct_option": "B",
            "explanation": "Khadi and Village Industries Commission (KVIC), a statutory body under the Ministry of MSME, is the national nodal agency implementing PMEGP across the country."
        },
        {
            "id": "MSME_160",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "With reference to the Scheme of Fund for Regeneration of Traditional Industries (SFURTI), consider the following statements:\n1. It was originally launched in 2005-06 and comprehensively revamped in 2014-15.\n2. Its primary objective is to organize traditional artisans and industries into clusters to improve competitiveness and product marketability.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. SFURTI was launched in 2005-06 and revamped in 2014-15. It organizes traditional artisans into sustainable geographic collectives and clusters to upgrade their technology, establish Common Facility Centres (CFCs), and increase earnings."
        },
        {
            "id": "MSME_161",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Regarding the official milestones of SFURTI as of December 12, 2024 (cited in the PIB release), consider the following statements:\n1. Since 2014-15, SFURTI has approved the formation of 513 clusters.\n2. Exactly 376 clusters have successfully become functional.\n3. A total grant of ₹1,336 crore has been extended, generating sustainable employment for around 2,20,800 artisans.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are exact milestones documented in the PIB release: 513 clusters approved, 376 functional, ₹1,336 crore grants disbursed, supporting 2,20,800 artisans."
        },
        {
            "id": "MSME_162",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Easy",
            "question": "What is the mandatory minimum percentage of annual procurement that Central Ministries, Departments, and CPSEs must source from Micro and Small Enterprises (MSEs) under the Public Procurement Policy?",
            "options": {
                "A": "10 per cent",
                "B": "15 per cent",
                "C": "20 per cent",
                "D": "25 per cent"
            },
            "correct_option": "D",
            "explanation": "Under the Public Procurement Policy for Micro and Small Enterprises (MSEs) notified in 2012 (and revised in 2018), Central Ministries, Government Departments, and Central Public Sector Enterprises (CPSEs) must mandatorily procure at least 25% of their total annual purchases of goods and services from MSEs."
        },
        {
            "id": "MSME_163",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Within the overall 25% mandatory annual public procurement target from MSEs, what specific sub-targets are earmarked for disadvantaged entrepreneur groups?\n1. 4 per cent is earmarked for MSEs owned by Scheduled Castes or Scheduled Tribes (SC/ST).\n2. 3 per cent is earmarked for MSEs owned by Women entrepreneurs.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. Within the overarching 25% quota, the policy establishes targeted sub-allocations: 4% reserved for SC/ST-owned MSEs and 3% reserved exclusively for Women-owned MSEs."
        },
        {
            "id": "MSME_164",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "How many items are exclusively reserved for procurement from Micro and Small Enterprises under the Public Procurement Policy?",
            "options": {
                "A": "125 items",
                "B": "250 items",
                "C": "358 items",
                "D": "500 items"
            },
            "correct_option": "C",
            "explanation": "As explicitly specified in the official PIB document, exactly 358 items are exclusively reserved for procurement from MSEs by all central government buyers, ensuring protected domestic demand for traditional small-scale manufacturing products."
        },
        {
            "id": "MSME_165",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the performance of the Public Procurement Policy for MSEs in the fiscal year 2023-24:\n1. Total procurement by Central Ministries, Departments, and CPSEs from MSEs was ₹74,717 crore.\n2. This procurement constituted 43.71% of their total annual procurement, substantially exceeding the 25% mandate.\n3. The procurement directly benefited 2,58,413 MSEs.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are exact achievements recorded in the PIB document: ₹74,717 crore procured from MSEs in 2023-24, achieving an impressive 43.71% share (well above the 25% statutory target) and benefiting 2,58,413 MSE enterprises."
        },
        {
            "id": "MSME_166",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Which portal was launched by the Ministry of MSME to monitor the public procurement of goods and services from MSEs by CPSEs?",
            "options": {
                "A": "MSME Sambandh",
                "B": "MSME Samadhaan",
                "C": "MSME Sampark",
                "D": "Udyam Portal"
            },
            "correct_option": "A",
            "explanation": "The MSME Sambandh Portal is the designated public procurement monitoring portal where CPSEs report their monthly and annual procurement progress from MSEs, tracking adherence to the 25%, 4% (SC/ST), and 3% (Women) quotas."
        },
        {
            "id": "MSME_167",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding tender benefits provided to MSEs under the Public Procurement Policy:\n1. MSEs are provided tender sets free of cost.\n2. MSEs are exempt from the payment of Earnest Money Deposit (EMD).\n3. In tenders where an MSE quotes within a price band of L1 + 15%, the MSE is allowed to supply a portion of the requirement by matching the L1 price.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. The policy grants MSEs free tender documents, EMD waivers, and a price-matching preference (within the L1 + 15% band, MSEs can supply up to 25% of the tender order by matching the lowest L1 quote from a non-MSE)."
        },
        {
            "id": "MSME_168",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Under SFURTI, what is the core infrastructure established within an artisan cluster to provide access to shared high-value machinery?",
            "options": {
                "A": "Common Facility Centre (CFC)",
                "B": "Private Corporate Headquarters",
                "C": "Special Economic Customs Bonded Warehouse",
                "D": "Stock Exchange Trading Floor"
            },
            "correct_option": "A",
            "explanation": "The core infrastructure funded under SFURTI is the Common Facility Centre (CFC), which houses expensive specialized processing machinery, design software, and quality testing labs that individual artisans could never afford independently."
        },
        {
            "id": "MSME_169",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the implementation architecture of PMEGP at the state and district levels:\n1. State KVIC Directorates implement PMEGP in rural areas.\n2. District Industries Centres (DICs) implement PMEGP in both rural and urban areas.\n3. State Khadi and Village Industries Boards (KVIBs) participate in implementation.\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "D",
            "explanation": "All three statements are correct. While KVIC is the single national agency, state-level implementation is decentralized across State KVIC Directorates, State KVIBs, and District Industries Centres (DICs), with financing channeled through commercial and regional rural banks."
        },
        {
            "id": "MSME_170",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What is the minimum educational qualification required for a beneficiary applying for a PMEGP project costing above ₹10 lakh in manufacturing or above ₹5 lakh in services?",
            "options": {
                "A": "No minimum qualification required",
                "B": "At least 8th standard pass",
                "C": "Graduation degree in commerce",
                "D": "Polytechnic engineering diploma"
            },
            "correct_option": "B",
            "explanation": "Under PMEGP guidelines, for projects costing above ₹10 lakh in the manufacturing sector and above ₹5 lakh in the business/service sector, the beneficiary must possess a minimum educational qualification of at least having passed 8th standard."
        },
        {
            "id": "MSME_171",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Medium",
            "question": "Consider the following statements regarding the 'Second Loan for Upgradation' under PMEGP for well-performing existing units:\n1. Existing PMEGP units that have repaid their initial bank loans successfully can apply for a second loan for technological upgradation.\n2. The maximum project cost for upgradation is up to ₹1 crore for manufacturing and up to ₹25 lakh for services.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. To address the problem of dwarfism, PMEGP introduced a Second Loan component for existing high-performing units to expand: up to ₹1 crore for manufacturing units and up to ₹25 lakh for service units, with a 15% subsidy (20% for NER/Hills)."
        },
        {
            "id": "MSME_172",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "Under the Public Procurement Policy, what qualifies an enterprise as 'owned by SC/ST' or 'owned by Women'?",
            "options": {
                "A": "At least 10% of employees must belong to SC/ST or Women",
                "B": "In case of proprietary MSE, the proprietor must be SC/ST or Woman; in partnership, at least 51% share must be held by SC/ST or Women partners",
                "C": "The enterprise must have its registered factory in a tribal area",
                "D": "The board of directors must include a government civil servant"
            },
            "correct_option": "B",
            "explanation": "Under the policy definitions, an MSE is considered owned by SC/ST or Women if: (a) for proprietary concerns, the sole proprietor is SC/ST or Woman; (b) for partnership enterprises, at least 51% shareholding is held by SC/ST or Women; (c) for private limited companies, at least 51% of equity shares are held by SC/ST or Women."
        },
        {
            "id": "MSME_173",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements regarding the institutional objectives of the RAMP scheme:\n1. It facilitates capacity building of State MSME departments to develop State Strategic Investment Plans (SIPs).\n2. It supports MSMEs in achieving Green/ZED (Zero Defect Zero Effect) certification.\n3. It is funded partially via a loan from the International Monetary Fund (IMF).\nWhich of the statements given above are correct?",
            "options": {
                "A": "1 and 2 only",
                "B": "2 and 3 only",
                "C": "1 and 3 only",
                "D": "1, 2 and 3"
            },
            "correct_option": "A",
            "explanation": "Statements 1 and 2 are correct. Statement 3 is incorrect because RAMP is funded by the World Bank (IBRD), not the International Monetary Fund (IMF). It aims to improve Centre-State coordination through Strategic Investment Plans and promotes ZED environmental certification."
        },
        {
            "id": "MSME_174",
            "module": m,
            "question_type": "single_choice_fact",
            "difficulty": "Medium",
            "question": "What happens if a CPSE fails to meet the 4% procurement target from SC/ST-owned MSEs or 3% from Women-owned MSEs in a given financial year?",
            "options": {
                "A": "The CPSE's operating license is automatically suspended",
                "B": "The shortfall must be reported on the MSME Sambandh portal, and the CPSE must provide detailed justifications in its annual report",
                "C": "The CPSE directors are subjected to mandatory criminal prosecution",
                "D": "The CPSE must transfer 50% of its profits to private micro-enterprises"
            },
            "correct_option": "B",
            "explanation": "Procurement performance is monitored transparently on the MSME Sambandh portal and reviewed at the Cabinet Secretariat and Parliamentary Committee level. Any shortfall must be officially reported, justified, and accounted for in the annual performance evaluation (MoU ratings) of CPSEs."
        },
        {
            "id": "MSME_175",
            "module": m,
            "question_type": "statement_based",
            "difficulty": "Hard",
            "question": "Consider the following statements comparing SFURTI and PMEGP:\n1. PMEGP focuses primarily on individual enterprise creation in the non-farm sector.\n2. SFURTI focuses on collective cluster-based regeneration of traditional village industries and artisan guilds.\nWhich of the statements given above is/are correct?",
            "options": {
                "A": "1 only",
                "B": "2 only",
                "C": "Both 1 and 2",
                "D": "Neither 1 nor 2"
            },
            "correct_option": "C",
            "explanation": "Both statements are correct. PMEGP is primarily an individual beneficiary-oriented scheme supporting micro-enterprise creation via bank credit and margin money subsidies. SFURTI, by contrast, is a cluster-level collective development intervention focused on traditional crafts, common facility centers, and artisan clusters."
        }
    ]
