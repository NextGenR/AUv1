# -*- coding: utf-8 -*-
"""
50 Questions on FREEBIES vs WELFARE GOODS (Revdi Culture & Fiscal Federalism)
Across the 10 selected testing patterns:
1. mc, 2. tf, 3. multi, 4. flag, 5. riddle, 6. match, 7. order, 8. sort, 9. year, 11. flip
"""

freebies_questions = [
    # --- Pattern 1: mc (5 questions) ---
    {
        "id": "freebie_01",
        "topic": "Freebies & Welfare",
        "k": "mc",
        "q": "What core economic attribute fundamentally distinguishes 'Merit / Welfare Goods' from 'Electoral Freebies'?",
        "o": [
            "Merit goods are distributed exclusively by the private corporate sector",
            "Merit goods generate positive socio-economic externalities and enhance long-term human capital, whereas freebies focus on short-term private consumption",
            "Freebies require biometric Aadhaar authentication while merit goods do not",
            "Merit goods are strictly funded through external foreign loans"
        ],
        "a": 1,
        "kw": "Merit vs Non-Merit Distinction",
        "e": "Merit goods (primary health, schools, sanitation, PDS nutrition) generate positive societal externalities and augment human productivity. Freebies are non-merit private consumption transfers (free consumer electronics, free electricity beyond lifeline, unconditional poll doles) with near-zero capital formation.",
        "data": "Capital expenditure has a high fiscal multiplier of 2.5x–3.5x, whereas revenue consumption transfers yield <0.9x.",
        "ex": "Building a rural primary health center vs handing out free color television sets on election eve.",
        "mains": "The essential conceptual foundation for distinguishing legitimate welfare from populist 'revdi'."
    },
    {
        "id": "freebie_02",
        "topic": "Freebies & Welfare",
        "k": "mc",
        "q": "In which landmark 2013 judgment did the Supreme Court hold that election manifesto promises do NOT constitute a 'corrupt practice' under Section 123 of the RPA, 1951?",
        "o": [
            "Indra Sawhney v. Union of India",
            "S. Subramaniam Balaji v. State of Tamil Nadu",
            "Kesavananda Bharati v. State of Kerala",
            "Shayara Bano v. Union of India"
        ],
        "a": 1,
        "kw": "S. Subramaniam Balaji Precedent (2013)",
        "e": "In S. Subramaniam Balaji (2013), the Supreme Court ruled that manifesto promises made by political parties cannot be treated as 'corrupt practice' or bribery under Section 123 of the Representation of the People Act, 1951, though it directed the ECI to frame guidelines.",
        "data": "Challenge arose over free distribution of color TVs, mixer-grinders, and laptops by DMK and AIADMK in Tamil Nadu.",
        "ex": "Court held that promises made in manifestos are political commitments, not individual candidate bribery under election law.",
        "mains": "The definitive judicial authority governing electoral welfare promises in India."
    },
    {
        "id": "freebie_03",
        "topic": "Freebies & Welfare",
        "k": "mc",
        "q": "Which constitutional article enables the Union Government to regulate and restrict state off-budget borrowings and market loans when a state has outstanding central debt?",
        "o": [
            "Article 280",
            "Article 293(3)",
            "Article 356",
            "Article 360"
        ],
        "a": 1,
        "kw": "Article 293(3) Sub-National Borrowing Cap",
        "e": "Article 293(3) mandates that a State may not, without the consent of the Government of India, raise any loan if there is still outstanding any part of a loan made to the State by the Government of India. The Centre uses this to rein in off-budget freebie borrowings.",
        "data": "Ministry of Finance included state-guaranteed borrowings by state PSUs/SPVs within the net borrowing ceiling of 3% GSDP.",
        "ex": "Kerala and Punjab challenging Union borrowing limits before the Supreme Court under Article 131.",
        "mains": "Vital constitutional mechanism preserving macro-fiscal stability in cooperative federalism."
    },
    {
        "id": "freebie_04",
        "topic": "Freebies & Welfare",
        "k": "mc",
        "q": "According to projections submitted during 16th Finance Commission deliberations, state government spending commitments on non-merit guarantees and cash doles are projected to escalate to what staggering amount?",
        "o": [
            "About ₹50,000 Crore",
            "About ₹1.2 Lakh Crore",
            "About ₹4.14 Lakh Crore",
            "Over ₹15 Lakh Crore"
        ],
        "a": 2,
        "kw": "16th FC Fiscal Burden Projections",
        "e": "Projections prepared for 16th Finance Commission consultations indicate that cumulative annual state commitments on non-merit guarantees, electricity subsidies, and women cash schemes are rising toward ₹4.14 Lakh Crore.",
        "data": "₹4.14 Lakh Crore projected burden; already exceeding ₹1.71 Lakh Crore across 10 fiscally vulnerable states (RBI Study 2023).",
        "ex": "States like Karnataka (5 Guarantees costing ~₹52,000 Cr/yr) and Maharashtra (Ladki Bahin costing ~₹46,000 Cr/yr).",
        "mains": "Demonstrates the acute fiscal crowding-out threatening state capital investments."
    },
    {
        "id": "freebie_05",
        "topic": "Freebies & Welfare",
        "k": "mc",
        "q": "What ancient philosophical concept from the Katha Upanishad is frequently invoked by economists to critique populist freebies versus sustainable development?",
        "o": [
            "Dharma vs Adharma",
            "Shreya (Long-term righteous good) vs Preya (Short-term transient pleasure)",
            "Moksha vs Samsara",
            "Ahimsa vs Satya"
        ],
        "a": 1,
        "kw": "Philosophical Framework: Shreya vs Preya",
        "e": "In the Katha Upanishad, Yama explains to Nachiketa the distinction between 'Shreya' (the path of enduring good, wisdom, and long-term virtue) and 'Preya' (the path of immediate sensory gratification and fleeting pleasure). Freebies epitomize political addiction to Preya over Shreya.",
        "data": "Invoked in economic ethics to highlight inter-generational justice and fiscal sustainability.",
        "ex": "Giving free electricity today (Preya) at the cost of depleted water tables and bankrupt schools tomorrow (neglecting Shreya).",
        "mains": "Top-tier value addition for UPSC Essay and GS-4 Ethics papers."
    },

    # --- Pattern 2: tf (5 questions) ---
    {
        "id": "freebie_06",
        "topic": "Freebies & Welfare",
        "k": "tf",
        "q": "True or False: Under the FRBM Act guidelines and Finance Commission norms, states are mandated to maintain their annual Fiscal Deficit within a ceiling of 3% of their Gross State Domestic Product (GSDP).",
        "a": 0,
        "kw": "FRBM 3% GSDP Fiscal Deficit Ceiling",
        "e": "True! The standard FRBM statutory ceiling limits state fiscal deficits to 3% of GSDP, with an additional 0.5% conditional borrowing space tied to power sector reforms and capital expenditure milestones.",
        "data": "FRBM Act 2003 / 15th Finance Commission fiscal consolidation glide path targeting 3% by FY 2025-26.",
        "ex": "States exceeding 3% face restrictions on open market borrowings (OMBs) through RBI auctions.",
        "mains": "The bedrock fiscal anchor preserving macroeconomic solvency across Indian states."
    },
    {
        "id": "freebie_07",
        "topic": "Freebies & Welfare",
        "k": "tf",
        "q": "True or False: The Supreme Court in 2024 completely banned political parties from offering Unconditional Cash Transfers (UCTs) to women in their election manifestos.",
        "a": 1,
        "kw": "Judicial Restraint on Policy Banning",
        "e": "False! The Supreme Court recognized that fiscal policy and social welfare fall within the executive and legislative domain. The Court has refrained from an outright judicial ban, emphasizing political consensus, ECI guidelines, and expert committee recommendations instead.",
        "data": "Doctrine of Separation of Powers prevents the judiciary from micro-managing state budgetary allocations.",
        "ex": "Schemes like Ladli Behna (MP), Gruha Lakshmi (Karnataka), and Ladki Bahin (Maharashtra) continue legally.",
        "mains": "Highlights judicial self-restraint vs executive fiscal responsibility."
    },
    {
        "id": "freebie_08",
        "topic": "Freebies & Welfare",
        "k": "tf",
        "q": "True or False: Studies show that the Marginal Propensity to Consume (MPC) among low-income female recipients of cash transfers is near zero because they hoard all cash in bank vaults.",
        "a": 1,
        "kw": "High Marginal Propensity to Consume",
        "e": "False! Low-income households have a Marginal Propensity to Consume (MPC) close to 1.0 (they spend nearly 100% of received cash immediately on food, healthcare, clothing, and children's school needs), generating immediate local economic velocity.",
        "data": "Keynesian multiplier: ₹1,000 cash transfer to poor mothers circulates 3-4 times in local kirana and village markets.",
        "ex": "Field data from MP and Tamil Nadu showing cash transfers directly funding protein consumption and school stationery.",
        "mains": "The premier economic argument supporting well-targeted cash transfers."
    },
    {
        "id": "freebie_09",
        "topic": "Freebies & Welfare",
        "k": "tf",
        "q": "True or False: Providing 100% free unmetered electricity to farmers has historically led to severe over-extraction of groundwater and severe financial insolvency of state power DISCOMs.",
        "a": 0,
        "kw": "Free Power Ecological & Financial Distortion",
        "e": "True! Unmetered free power eliminates any incentive for water efficiency, causing catastrophic groundwater depletion (over-exploited blocks in Punjab and Haryana) while burdening DISCOMs with massive subsidy dues.",
        "data": "Punjab's water table falling by ~0.5 meters annually; State DISCOM debt crossed ₹6 Lakh Crore nationwide.",
        "ex": "Farmers leaving electric tubewells running 24/7 to flood paddy fields in semi-arid zones.",
        "mains": "Case study in how non-merit subsidies create ecological destruction and market failure."
    },
    {
        "id": "freebie_10",
        "topic": "Freebies & Welfare",
        "k": "tf",
        "q": "True or False: Capital Expenditure (Capex) in infrastructure has a lower economic multiplier effect on GDP growth than recurring revenue expenditure on consumer cash subsidies.",
        "a": 1,
        "kw": "Capex Multiplier Superiority",
        "e": "False! RBI and NIPFP studies prove that Capital Expenditure has a massive fiscal multiplier of 2.5x to 3.5x over 3 years, whereas revenue expenditure subsidies have a multiplier of less than 0.9x.",
        "data": "Capex multiplier: ₹1 invested yields ₹2.50 to ₹3.50 in GDP; Revenue doles yield <₹0.90.",
        "ex": "Building a rural highway creates freight logistics and permanent jobs; handing out free cash creates only temporary consumption.",
        "mains": "Core analytical argument against fiscal crowding-out."
    },

    # --- Pattern 3: multi (5 questions) ---
    {
        "id": "freebie_11",
        "topic": "Freebies & Welfare",
        "k": "multi",
        "q": "Tap all Directive Principles of State Policy (DPSP) in Part IV of the Constitution that mandate legitimate state welfare interventions:",
        "o": [
            "Article 38 (Promoting the welfare of the people and minimizing income inequalities)",
            "Article 39(b) & (c) (Securing equitable distribution of resources to subserve common good)",
            "Article 41 (Right to work, education, and public assistance in cases of unemployment or old age)",
            "Article 368 (Procedure for Constitutional Amendment)"
        ],
        "a": [0, 1, 2],
        "kw": "DPSP Constitutional Welfare Mandates",
        "e": "Articles 38, 39, and 41 form the constitutional bedrock of India's welfare state. Article 368 pertains to constitutional amendments, not welfare delivery.",
        "data": "Part IV of the Constitution enshrines the ideal of a socio-economic Welfare State.",
        "ex": "PDS food grain entitlements fulfilling Article 47 (raising nutrition) and Article 39(a).",
        "mains": "Essential constitutional justification for distinguishing genuine welfare from unconstitutional squandering."
    },
    {
        "id": "freebie_12",
        "topic": "Freebies & Welfare",
        "k": "multi",
        "q": "Tap all core economic and democratic pathologies associated with unchecked electoral freebies ('Revdi Culture'):",
        "o": [
            "Competitive Populism triggering an escalatory bidding war before polls",
            "Labharthi Clientelism converting sovereign citizens into passive dependents on state patronage",
            "Crowding out of Capital Expenditure (Capex) in healthcare, education, and roads",
            "Automatic eradication of all state-level public debt within 12 months"
        ],
        "a": [0, 1, 2],
        "kw": "Core Pathologies of Freebie Populism",
        "e": "Freebies fuel competitive populism, clientelistic dependence, and capex starvation. They dramatically INCREASE state public debt rather than eliminating it.",
        "data": "Debt-to-GSDP ratios crossing 40% in Punjab, Himachal Pradesh, and Andhra Pradesh.",
        "ex": "Cancelling planned hospital construction to finance election-eve cash handouts.",
        "mains": "Analytical framework for dissecting the costs of sub-national fiscal irresponsibility."
    },
    {
        "id": "freebie_13",
        "topic": "Freebies & Welfare",
        "k": "multi",
        "q": "Tap all genuine, verified benefits of targeted Unconditional Cash Transfers (UCTs) to women:",
        "o": [
            "Enhances female financial agency and intra-household decision-making autonomy",
            "Provides an immediate economic safety floor against food inflation and seasonal unemployment",
            "Delivers near-zero administrative leakage when routed via the JAM Trinity (DBT)",
            "Guarantees that India's manufacturing exports triple within 30 days"
        ],
        "a": [0, 1, 2],
        "kw": "Benefits of Targeted Women Cash Transfers",
        "e": "UCTs empower women, prevent acute starvation/poverty traps, and deliver leak-free transfers via DBT. They do NOT magically triple manufacturing exports.",
        "data": "Over 53 Crore Jan Dhan accounts, 80%+ Aadhaar-seeded, enabling direct delivery.",
        "ex": "Tamil Nadu's Kalaignar Magalir Urimai Thittam disbursing ₹1,000/month to over 1.15 Crore women.",
        "mains": "Balanced argumentation: recognizing the gender equity benefits of well-designed social security."
    },
    {
        "id": "freebie_14",
        "topic": "Freebies & Welfare",
        "k": "multi",
        "q": "Tap all states identified in RBI and CAG reports as experiencing severe sub-national fiscal stress (Debt-to-GSDP exceeding 35%–40%):",
        "o": [
            "Punjab (Debt-to-GSDP ~48%)",
            "Himachal Pradesh (Debt-to-GSDP ~42%)",
            "West Bengal (Debt-to-GSDP ~38%)",
            "State of Singapore"
        ],
        "a": [0, 1, 2],
        "kw": "Sub-National Fiscal Vulnerability Hotspots",
        "e": "Punjab, Himachal Pradesh, and West Bengal are among the most fiscally vulnerable Indian states, with massive debt burdens compounded by free power, Old Pension Scheme (OPS) reversions, and cash guarantees. Singapore is an independent foreign nation.",
        "data": "15th Finance Commission recommended a state debt ceiling of 20% of GSDP.",
        "ex": "Himachal Pradesh struggling to pay civil servant salaries on the 1st of the month in late 2024.",
        "mains": "Hard empirical evidence of the consequences of un-calibrated sub-national populism."
    },
    {
        "id": "freebie_15",
        "topic": "Freebies & Welfare",
        "k": "multi",
        "q": "Tap all structural reform measures recommended by experts to regulate election freebies without undermining genuine welfare:",
        "o": [
            "Mandating political parties to publish a costed 'Fiscal Impact Statement' with every poll manifesto",
            "Statutory classification of Merit vs Non-Merit goods by the 16th Finance Commission",
            "Bringing all state off-budget borrowings and contingent liabilities strictly onto official balance sheets",
            "Completely abolishing all government schools and public hospitals nationwide"
        ],
        "a": [0, 1, 2],
        "kw": "Structural Reform Toolkit for Freebies",
        "e": "Mandatory manifesto costing, clear statutory classification of merit goods, and accounting transparency under Article 293(3) are sensible institutional fixes. Abolishing public schools and hospitals is absurd.",
        "data": "15th Finance Commission Chairman N.K. Singh and RBI studies strongly advocate fiscal impact disclosure.",
        "ex": "ECI proposed modifying the Model Code of Conduct to require funding disclosures for manifesto promises.",
        "mains": "Actionable, reform-oriented 'Way Forward' for UPSC GS-2 and GS-3 answers."
    },

    # --- Pattern 4: flag (5 questions) ---
    {
        "id": "freebie_16",
        "topic": "Freebies & Welfare",
        "k": "flag",
        "q": "Spot the red flag: which scheme is traditionally classified as a 'Merit / Public Good' rather than a 'Non-Merit Freebie'?",
        "o": [
            "Free color television sets and mixer-grinders distributed during election victories",
            "Unconditional loan waivers for wealthy commercial defaulting borrowers",
            "The Public Distribution System (PDS) providing subsidized food grains to Antyodaya families",
            "Free gold coins for wedding gifts announced during poll campaigns"
        ],
        "a": 2,
        "kw": "Merit Good Identification",
        "e": "Red Flag! The PDS (National Food Security Act) is a MERIT GOOD essential for basic biological survival, childhood stunting reduction, and Article 21 human dignity. Color TVs, gold coins, and unconditional commercial loan waivers are non-merit private consumption freebies.",
        "data": "NFSA covers 81 Crore citizens, legally guaranteeing 5 kg food grains per person per month.",
        "ex": "Distinguishing food grain rations (Merit) from free consumer durables (Non-Merit).",
        "mains": "Critical distinction: never confuse foundational social security with electoral revdi."
    },
    {
        "id": "freebie_17",
        "topic": "Freebies & Welfare",
        "k": "flag",
        "q": "Spot the red flag: which statement regarding Section 123 of the Representation of the People Act (RPA) 1951 is FALSE?",
        "o": [
            "Section 123 defines 'corrupt practices' in elections, including bribery and undue influence",
            "Under S. Subramaniam Balaji (2013), manifesto promises by political parties are automatically punished with immediate disqualification under Section 123",
            "Section 123(1) punishes gifts or offers of gratification made by an individual candidate to induce a voter",
            "Section 123 corrupt practices can lead to the setting aside of an election by an Election Tribunal / High Court"
        ],
        "a": 1,
        "kw": "Section 123 RPA Jurisprudential Scope",
        "e": "Red Flag! In S. Subramaniam Balaji (2013), the Supreme Court held that manifesto promises do NOT fall under Section 123 and do NOT lead to disqualification. Section 123 applies strictly to individual candidates or their agents making direct private inducements.",
        "data": "Section 123(1) Bribery definition in RPA 1951.",
        "ex": "Distinction between a party manifesto promising pensions vs a candidate handing out ₹2,000 cash notes the night before voting.",
        "mains": "Precision legal knowledge essential for GS-2 Electoral Reforms questions."
    },
    {
        "id": "freebie_18",
        "topic": "Freebies & Welfare",
        "k": "flag",
        "q": "Spot the red flag: which statement regarding sub-national debt and state budgets in India is FACTUALLY INCORRECT?",
        "o": [
            "Several states have accumulated debt-to-GSDP ratios exceeding 40%",
            "State power distribution companies (DISCOMs) have accumulated aggregate financial losses exceeding ₹6 Lakh Crore",
            "The Constitution of India allows states to borrow directly from foreign foreign governments and the World Bank without any Central Government approval",
            "Off-budget borrowings via State Infrastructure Boards are increasingly counted under net borrowing ceilings"
        ],
        "a": 2,
        "kw": "Constitutional Bar on Direct Foreign Borrowing",
        "e": "Red Flag! Under Article 293(1), states CANNOT borrow outside India! External foreign commercial borrowings and multilateral loans (World Bank, ADB) can ONLY be raised through the Union Government of India.",
        "data": "Article 293(1) restricts state borrowing strictly to the territory of India upon the security of the Consolidated Fund of the State.",
        "ex": "External aid for state metro projects flowing through the Ministry of Finance / DEA.",
        "mains": "Core federal finance constitutional law under Part XII."
    },
    {
        "id": "freebie_19",
        "topic": "Freebies & Welfare",
        "k": "flag",
        "q": "Spot the red flag: which adverse impact is NOT associated with untargeted free electricity for agriculture?",
        "o": [
            "Severe depletion of deep underground groundwater aquifers",
            "Severe accumulation of regulatory dues and insolvency of state electricity DISCOMs",
            "Immediate 100% replacement of all coal-fired thermal power plants with green hydrogen",
            "Soil salinization and degradation caused by excessive flood irrigation"
        ],
        "a": 2,
        "kw": "Free Electricity Distortions",
        "e": "Red Flag! Free agricultural electricity does NOT replace coal with green hydrogen! In fact, it drives up dirty thermal power demand to pump water from ever-deeper tubewells, accelerating carbon emissions.",
        "data": "Agriculture consumes ~20% of India's electricity, mostly supplied free or heavily cross-subsidized by industrial tariffs.",
        "ex": "Tubewells in Sangrur and Moga boring down 300+ feet due to zero marginal cost of power.",
        "mains": "The Water-Energy-Food Nexus in Indian agriculture."
    },
    {
        "id": "freebie_20",
        "topic": "Freebies & Welfare",
        "k": "flag",
        "q": "Spot the red flag: which quote or perspective is MISATTRIBUTED?",
        "o": [
            "15th Finance Commission Chairman N.K. Singh warned that unfunded sub-national freebies are a 'passport to fiscal disaster'",
            "The Supreme Court of India in 2022 observed that 'nobody is against genuine welfare schemes that alleviate poverty'",
            "The Reserve Bank of India declared that all government social security schemes are illegal under the Banking Regulation Act",
            "Former CEA K.V. Subramanian emphasized the distinction between productive capital assets and unproductive consumption transfers"
        ],
        "a": 2,
        "kw": "Institutional Perspectives on Welfare",
        "e": "Red Flag! The RBI has NEVER declared social security illegal under the Banking Regulation Act! The RBI produces studies on State Finances warning about sub-national fiscal risks, but fully supports legal social security.",
        "data": "RBI Report on State Finances (June 2022) highlighted the vulnerability of the 10 most indebted states.",
        "ex": "RBI Governor emphasizing fiscal prudence while supporting DBT financial inclusion via Jan Dhan.",
        "mains": "Ensures factual precision when quoting institutional authorities."
    },

    # --- Pattern 5: riddle (5 questions) ---
    {
        "id": "freebie_21",
        "topic": "Freebies & Welfare",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a statutory fiscal rule enacted by Parliament in 2003.",
            "I impose disciplined ceilings on fiscal deficits, revenue deficits, and debt-to-GDP trajectories.",
            "States regularly bypass my constraints by floating special purpose vehicles (SPVs) to raise off-budget loans. Who am I?"
        ],
        "o": ["Fiscal Responsibility and Budget Management (FRBM) Act", "Monetary Policy Framework Agreement", "Finance Commission Act", "Insolvency and Bankruptcy Code (IBC)"],
        "a": 0,
        "kw": "FRBM Act Architecture",
        "e": "The Fiscal Responsibility and Budget Management (FRBM) Act, 2003! It sets binding targets to reduce fiscal deficits and eliminate revenue deficits, acting as India's primary legislative defense against fiscal profligacy.",
        "data": "N.K. Singh FRBM Review Committee recommended 60% general government debt-to-GDP (40% Centre + 20% States).",
        "ex": "Union Government enforcing FRBM limits to prevent competitive election borrowing.",
        "mains": "The central statutory framework for macroeconomic fiscal governance."
    },
    {
        "id": "freebie_22",
        "topic": "Freebies & Welfare",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am an economic concept describing the collateral damage of excessive populist revenue spending.",
            "Because states exhaust their revenues paying for free power and poll doles, they are forced to cancel investments in schools, hospitals, and highways.",
            "Economists refer to me as the phenomenon where consumption spending 'chokes' growth-inducing assets. Who am I?"
        ],
        "o": ["Capex Crowding-Out", "Dutch Disease", "Liquidity Trap", "Deflationary Spiral"],
        "a": 0,
        "kw": "Capex Crowding-Out Pathology",
        "e": "Capex Crowding-Out! When a state's revenue deficit balloons due to recurring consumption subsidies, borrowing caps force the government to slash discretionary capital expenditures, sacrificing future economic capacity.",
        "data": "Capital spending share in states dropping below 12% of total expenditure in heavily indebted states.",
        "ex": "Cancelling state highway widening projects to fund election-announced monthly doles.",
        "mains": "The definitive macro-economic critique of election freebie culture."
    },
    {
        "id": "freebie_23",
        "topic": "Freebies & Welfare",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a political science term describing voters who receive direct, targeted benefits from government schemes.",
            "I represent a shift from traditional caste-based identity voting to transaction-based welfare patronage.",
            "Critics argue that my overuse creates 'clientelism', where citizens vote based on individual handouts rather than public governance quality. Who am I?"
        ],
        "o": ["Labharthi (Beneficiary Class)", "Proletariat", "Swing Voter", "Electoral College"],
        "a": 0,
        "kw": "The 'Labharthi' Socio-Political Phenomenon",
        "e": "The 'Labharthi' (Beneficiary Class)! The systematic direct transfer of housing (PMAY), gas (Ujjwala), toilets (SBM), and cash creates a dedicated constituency of beneficiaries loyal to the delivering regime.",
        "data": "Tens of crores of citizens covered under DBT schemes across Union and State registers.",
        "ex": "Political parties targeting specific welfare transfer announcements directly at female heads of households.",
        "mains": "Crucial contemporary socio-political concept for GS-2 Governance and Society."
    },
    {
        "id": "freebie_24",
        "topic": "Freebies & Welfare",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a landmark welfare delivery architecture formed by combining zero-balance bank accounts, unique biometrics, and cellular telecommunications.",
            "I transformed India's welfare state by plugging catastrophic leakages and ghost beneficiary scams.",
            "I enable unconditional women's cash transfers to reach 10 Crore accounts in a single click. Who am I?"
        ],
        "o": ["JAM Trinity (Jan Dhan, Aadhaar, Mobile)", "Unified Payments Interface (UPI)", "DigiLocker", "ONDC Network"],
        "a": 0,
        "kw": "The JAM Trinity Infrastructure",
        "e": "The JAM Trinity (Jan Dhan - Aadhaar - Mobile)! It forms the digital plumbing of Direct Benefit Transfer (DBT), enabling leak-free cash delivery directly into beneficiary accounts without local intermediary cuts.",
        "data": "Cumulative DBT transfers exceeding ₹38 Lakh Crore across 300+ government schemes.",
        "ex": "Covid-19 emergency assistance transferred to 20 Crore women Jan Dhan accounts within 24 hours.",
        "mains": "India's greatest innovation in digital public finance delivery."
    },
    {
        "id": "freebie_25",
        "topic": "Freebies & Welfare",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am an autonomous constitutional body constituted every five years under Article 280 of the Constitution.",
            "I recommend the devolution of central taxes between the Union and the States and set fiscal consolidation trajectories.",
            "My 16th edition, chaired by Dr. Arvind Panagariya, is tasked with addressing state fiscal health and non-merit spending. Who am I?"
        ],
        "o": ["Finance Commission of India", "NITI Aayog", "Comptroller and Auditor General (CAG)", "Goods and Services Tax (GST) Council"],
        "a": 0,
        "kw": "Finance Commission of India (Article 280)",
        "e": "The Finance Commission of India! Mandated under Article 280 to recommend vertical and horizontal tax devolution and formulate conditional grants-in-aid to strengthen cooperative fiscal federalism.",
        "data": "16th Finance Commission constituted under Dr. Arvind Panagariya (December 2023).",
        "ex": "Recommending fiscal deficit glide paths and conditional performance incentives for states.",
        "mains": "The institutional fulcrum of Indian fiscal federalism."
    },

    # --- Pattern 6: match (5 questions) ---
    {
        "id": "freebie_26",
        "topic": "Freebies & Welfare",
        "k": "match",
        "q": "Match each constitutional article to its specific mandate in public welfare and finance:",
        "p": [
            ["Article 38", "State to secure social order and minimize income inequality"],
            ["Article 39(b)", "Material resources distributed to subserve common good"],
            ["Article 41", "Right to work, education and public assistance"],
            ["Article 293(3)", "Central consent required for state borrowing if debt exists"]
        ],
        "kw": "Constitutional Articles in Welfare & Finance",
        "e": "Articles 38, 39, and 41 are fundamental DPSPs guiding state welfare; Article 293(3) provides the Union's constitutional brake on reckless state borrowings.",
        "data": "Part IV (DPSPs) + Part XII (Finance, Borrowing).",
        "ex": "Citing Article 38 for cash safety nets vs Article 293(3) for borrowing limits.",
        "mains": "High-scoring constitutional mapping for GS-2 and GS-3 answers."
    },
    {
        "id": "freebie_27",
        "topic": "Freebies & Welfare",
        "k": "match",
        "q": "Match the state flagship cash guarantee scheme to its respective state government:",
        "p": [
            ["Ladli Behna Yojana", "Madhya Pradesh"],
            ["Gruha Lakshmi Scheme", "Karnataka"],
            ["Kalaignar Magalir Urimai Thittam", "Tamil Nadu"],
            ["Mukhyamantri Majhi Ladki Bahin", "Maharashtra"]
        ],
        "kw": "State Cash Guarantee Schemes",
        "e": "MP = Ladli Behna (₹1,250/mo); Karnataka = Gruha Lakshmi (₹2,000/mo); Tamil Nadu = Magalir Urimai (₹1,000/mo); Maharashtra = Ladki Bahin (₹1,500/mo).",
        "data": "Combined fiscal commitment across these 4 states exceeds ₹1.2 Lakh Crore annually.",
        "ex": "Direct cash transfers to over 4 Crore women across these four major states.",
        "mains": "Provides concrete contemporary empirical case studies in Mains answers."
    },
    {
        "id": "freebie_28",
        "topic": "Freebies & Welfare",
        "k": "match",
        "q": "Match the public expenditure type to its verified fiscal multiplier effect:",
        "p": [
            ["Capital Expenditure (Capex in Infrastructure)", "High Multiplier: 2.5x to 3.5x over 3 years"],
            ["Revenue Subsidies (Non-merit cash doles)", "Low Multiplier: Less than 0.9x"],
            ["PDS Food Security (Merit Nutritional Support)", "Sustains human capital & prevents stunting"],
            ["Free Agricultural Power", "Distorts water tables & burdens DISCOMs"]
        ],
        "kw": "Expenditure Multiplier Taxonomy",
        "e": "Capex generates massive downstream economic activity (2.5x-3.5x); revenue consumption doles create transient demand (<0.9x); merit goods build human capital; free power causes ecological/financial crisis.",
        "data": "Empirical studies by Reserve Bank of India and NIPFP.",
        "ex": "Comparing an express freight highway against an election-eve electronics handout.",
        "mains": "The core macro-economic justification for reforming expenditure composition."
    },
    {
        "id": "freebie_29",
        "topic": "Freebies & Welfare",
        "k": "match",
        "q": "Match each institutional leader or expert to their authoritative position on freebies:",
        "p": [
            ["N.K. Singh (15th FC Chairman)", "Unfunded sub-national freebies are a passport to fiscal disaster"],
            ["Supreme Court of India (2022)", "Need an expert committee to separate genuine welfare from freebies"],
            ["S. Subramaniam Balaji Bench (2013)", "Manifesto promises do not constitute Section 123 corrupt practices"],
            ["Yama (Katha Upanishad)", "Shreya (enduring good) vs Preya (transient temptation)"]
        ],
        "kw": "Authoritative Quotes & Benchmarks",
        "e": "N.K. Singh warned of fiscal bankruptcy; SC 2022 sought an apex expert body; Balaji 2013 set manifesto jurisprudence; Katha Upanishad provides the ethical philosophical lens.",
        "data": "Essential quotations to elevate GS-2, GS-3, and GS-4 answer scripts.",
        "ex": "Opening an answer with N.K. Singh's warning on sub-national bankruptcy.",
        "mains": "Attributed quotes create maximum evaluator impact."
    },
    {
        "id": "freebie_30",
        "topic": "Freebies & Welfare",
        "k": "match",
        "q": "Match the proposed reform measure to the governance problem it directly solves:",
        "p": [
            ["Mandatory Costing in Manifestos", "Forces parties to reveal funding sources before elections"],
            ["Article 293(3) Net Borrowing Ceilings", "Eliminates hidden off-budget debt raised via SPVs"],
            ["16th FC Classification of Merit Goods", "Prevents governments from disguising freebies as welfare"],
            ["Direct Benefit Transfer (DBT)", "Eliminates intermediary cuts and ghost beneficiaries"]
        ],
        "kw": "Problem-Solution Governance Matrix",
        "e": "Manifesto costing ends reckless promises; Art 293(3) caps off-budget debt; 16th FC classification prevents semantic confusion; DBT ends corruption leakages.",
        "data": "A 4-tier structural reform roadmap restoring fiscal integrity.",
        "ex": "Requiring a party promising ₹2,000/month to explain whether they will raise taxes or cut capital outlays.",
        "mains": "Action-oriented policy synthesis for GS-2 Governance."
    },

    # --- Pattern 7: order (5 questions) ---
    {
        "id": "freebie_31",
        "topic": "Freebies & Welfare",
        "k": "order",
        "q": "Order the lifecycle of a sub-national fiscal crisis caused by competitive freebie populism:",
        "o": [
            "Parties engage in competitive election-eve guarantee bidding",
            "Winning regime implements unbudgeted revenue consumption doles",
            "Recurring subsidy bills squeeze Capital Expenditure (Capex crowding-out)",
            "State floats off-budget SPVs and borrows at high market bond yields",
            "Debt-to-GSDP crosses 40%, triggering credit curbs and salary payment delays"
        ],
        "kw": "Causality of Sub-National Fiscal Insolvency",
        "e": "Competitive bidding -> Unbudgeted spending -> Capex starvation -> Off-budget borrowing -> Fiscal insolvency and credit rating downgrades.",
        "data": "Tracks the real trajectory witnessed in several highly indebted states.",
        "ex": "Punjab and Himachal Pradesh exhausting borrowing limits early in the financial year.",
        "mains": "Logical narrative sequencing for 15-marker economic essays."
    },
    {
        "id": "freebie_32",
        "topic": "Freebies & Welfare",
        "k": "order",
        "q": "Order the optimal sequence for reforming a state-level subsidy program from wasteful freebie to targeted welfare:",
        "o": [
            "Conduct universal socio-economic beneficiary audit using SECC & Aadhaar",
            "Eliminate dead, duplicate, and non-eligible affluent beneficiaries",
            "Convert in-kind and physical distribution into direct digital cash transfers (DBT)",
            "Institute strict sunset clauses and periodic graduation reviews",
            "Reallocate saved fiscal space into primary healthcare and school infrastructure"
        ],
        "kw": "Subsidy Rationalization Sequence",
        "e": "Audit -> De-duplication -> DBT transition -> Sunset clause institution -> Capex reallocation.",
        "data": "World Bank & NITI Aayog blueprint for subsidy rationalization.",
        "ex": "PDS Aadhaar de-duplication saving over ₹1.85 Lakh Crore in food grain leakage.",
        "mains": "Practical administrative roadmap for civil servants."
    },
    {
        "id": "freebie_33",
        "topic": "Freebies & Welfare",
        "k": "order",
        "q": "Order the primary expenditure components of a state budget by their long-term economic returns (highest return to lowest):",
        "o": [
            "Capital Investments in Highways, Power Grids & Medical Colleges (Multiplier > 2.5x)",
            "Merit Human Capital Outlays in Primary Education & Nutrition (DPSP Art 39/47)",
            "Lifeline Subsidized Drinking Water & Rural Sanitation (DPSP Art 41)",
            "Free Consumer White Goods & Unconditional Election Cash Doles (Multiplier < 0.9x)"
        ],
        "kw": "Budgetary Productive Hierarchy",
        "e": "Hard Capex (2.5x-3.5x) > Foundational Human Capital (Schools/Nutrition) > Lifeline utilities > Unconditional poll freebies (<0.9x).",
        "data": "Standard fiscal economics prioritization framework.",
        "ex": "State budgets systematically deprioritizing Capex to fund recurring bottom-tier consumption doles.",
        "mains": "Framework for evaluating budget quality and allocative efficiency."
    },
    {
        "id": "freebie_34",
        "topic": "Freebies & Welfare",
        "k": "order",
        "q": "Order the landmark judicial and institutional milestones in India's freebie debate chronologically:",
        "o": [
            "Enactment of the Fiscal Responsibility and Budget Management (FRBM) Act (2003)",
            "Supreme Court ruling in S. Subramaniam Balaji v. State of Tamil Nadu (2013)",
            "RBI produces landmark report warning of severe fiscal stress in 10 states (2022)",
            "Supreme Court bench heads hearings on apex expert committee on freebies (2022–2024)",
            "16th Finance Commission begins consultations on state non-merit spending (2024)"
        ],
        "kw": "Freebie Debate Historical Timeline",
        "e": "FRBM Act (2003) -> Balaji judgment (2013) -> RBI vulnerability study (2022) -> SC hearings on expert body (2022-24) -> 16th FC consultations (2024).",
        "data": "Two-decade evolution of the legal, fiscal, and institutional debate.",
        "ex": "From isolated Tamil Nadu election challenges to nationwide macroeconomic scrutiny.",
        "mains": "Chronological mastery demonstrating comprehensive depth."
    },
    {
        "id": "freebie_35",
        "topic": "Freebies & Welfare",
        "k": "order",
        "q": "Order the optimal structure for a 15-mark UPSC answer on: 'Revdi Culture vs Social Welfare: Reconciling Constitutional Mandates with Fiscal Prudence':",
        "o": [
            "Intro: Define Freebies vs Merit Goods + Katha Upanishad (Shreya vs Preya)",
            "Constitutional Canvas: DPSP Articles 38, 39, 41 vs FRBM 3% GSDP discipline",
            "The Case for Welfare: Basic income, women agency (UCTs), high rural MPC",
            "The Pathology of Freebies: Capex crowding out, Discom losses, sub-national debt",
            "Way Forward: 16th FC classification, manifesto costing, Article 293(3) oversight"
        ],
        "kw": "15-Marker Answer Architecture on Freebies",
        "e": "Conceptual intro -> Constitutional tension -> Pro-welfare justification -> Macroeconomic critique -> Structural institutional way forward.",
        "data": "The gold standard answer structure for GS-2 / GS-3 mains questions.",
        "ex": "Balances humanitarian empathy with cold macroeconomic realism.",
        "mains": "Guarantees top marks by avoiding one-sided partisan bias."
    },

    # --- Pattern 8: sort (5 questions) ---
    {
        "id": "freebie_36",
        "topic": "Freebies & Welfare",
        "k": "sort",
        "q": "Sort each government expenditure as either a 'Merit / Public Good' or a 'Non-Merit Freebie':",
        "it": [
            ["Subsidized food grains under National Food Security Act (PDS)", 0],
            ["Free distribution of color televisions and mixer-grinders", 1],
            ["Constructing primary healthcare centers and rural schools", 0],
            ["Free electricity up to 300 units for affluent residential consumers", 1],
            ["Wages for manual labor under MGNREGA", 0],
            ["Free gold coins distributed as election marriage incentives", 1]
        ],
        "b": ["Merit / Public Good", "Non-Merit Freebie"],
        "kw": "Expenditure Typology Sorting",
        "e": "Merit goods build human capabilities (PDS, primary health, MGNREGA); non-merit freebies are private consumption inducements (color TVs, free power for wealthy, gold coins).",
        "data": "Clear operational distinction based on positive societal externalities.",
        "ex": "Nutritional security (Merit) vs Consumer electronics (Freebie).",
        "mains": "Core classification tool for evaluating government schemes."
    },
    {
        "id": "freebie_37",
        "topic": "Freebies & Welfare",
        "k": "sort",
        "q": "Sort each argument as supporting the 'Welfare & Equity Perspective' or the 'Fiscal Prudence Perspective':",
        "it": [
            ["Protects the vulnerable bottom 40% from acute inflationary shocks", 0],
            ["Sub-national Debt-to-GSDP ratios approaching 48% trigger fiscal distress", 1],
            ["Unconditional Cash Transfers enhance female autonomy and household nutrition", 0],
            ["Capex multiplier of 2.5x-3.5x is crowded out by consumption subsidies (<0.9x)", 1],
            ["Rural poor have high marginal propensity to consume, stimulating local trade", 0],
            ["Unmetered free agricultural power causes catastrophic groundwater depletion", 1]
        ],
        "b": ["Welfare & Equity Perspective", "Fiscal Prudence Perspective"],
        "kw": "Welfare vs Prudence Debate Alignment",
        "e": "Welfare arguments focus on social security, women's empowerment, and poverty cushions; Fiscal prudence arguments focus on debt ceilings, capex crowding-out, and ecological distortions.",
        "data": "Captures the central tension of India's development economics.",
        "ex": "Balancing Article 38 (social welfare) with Article 293(3) (fiscal solvency).",
        "mains": "Essential dialectical synthesis required for UPSC evaluators."
    },
    {
        "id": "freebie_38",
        "topic": "Freebies & Welfare",
        "k": "sort",
        "q": "Sort each characteristic into the philosophical category from Katha Upanishad: 'Shreya' (Enduring Good) vs 'Preya' (Transient Pleasure):",
        "it": [
            ["Capital investments in state medical colleges and STEM universities", 0],
            ["Distributing cash notes the night before election polling", 1],
            ["Solarizing agricultural irrigation pumps under PM-KUSUM", 0],
            ["Supplying 100% free unmetered grid electricity leading to aquifer collapse", 1],
            ["Building permanent rural road connectivity under PMGSY", 0],
            ["Waiving all commercial utility bills immediately prior to voting day", 1]
        ],
        "b": ["Shreya (Enduring Good)", "Preya (Transient Pleasure)"],
        "kw": "Shreya vs Preya Philosophical Sorting",
        "e": "Shreya represents sustainable, long-term, righteous capital investments; Preya represents short-term, alluring, destructive populist shortcuts.",
        "data": "Katha Upanishad Chapter 1, Section 2.",
        "ex": "PM-KUSUM solar pumps (Shreya) vs unmetered thermal power (Preya).",
        "mains": "Profound philosophical framing for GS-4 Ethics case studies."
    },
    {
        "id": "freebie_39",
        "topic": "Freebies & Welfare",
        "k": "sort",
        "q": "Sort each cash transfer program by its primary target group: 'Women Empowerment' vs 'Farmer Income Support':",
        "it": [
            ["Ladli Behna Yojana (Madhya Pradesh)", 0],
            ["PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)", 1],
            ["Kalaignar Magalir Urimai Thittam (Tamil Nadu)", 0],
            ["Rythu Bandhu / PM-Kisan matching schemes", 1],
            ["Gruha Lakshmi Scheme (Karnataka)", 0],
            ["Krushak Assistance for Livelihood and Income Augmentation (KALIA)", 1]
        ],
        "b": ["Women Empowerment", "Farmer Income Support"],
        "kw": "Direct Cash Transfer Typology",
        "e": "Women transfers: Ladli Behna, Magalir Urimai, Gruha Lakshmi; Farmer transfers: PM-KISAN, Rythu Bandhu, KALIA.",
        "data": "Combined transfers exceed ₹1.5 Lakh Crore annually across Union and States.",
        "ex": "Targeting female bank accounts vs land-owning agrarian records.",
        "mains": "Categorization of contemporary DBT schemes in India."
    },
    {
        "id": "freebie_40",
        "topic": "Freebies & Welfare",
        "k": "sort",
        "q": "Sort each fiscal entity as either an 'On-Budget Direct Liability' or an 'Off-Budget Disguised Liability':",
        "it": [
            ["Salaries of state government school teachers", 0],
            ["State government guarantees issued to loss-making state power DISCOMs", 1],
            ["Interest payments on State Development Loans (SDLs) raised via RBI", 0],
            ["Loans taken by State Infrastructure Development Corporations backed by letters of comfort", 1],
            ["Monthly pensions disbursed from the Consolidated Fund of the State", 0],
            ["Borrowings by special purpose vehicles (SPVs) servicing debt via liquor excise cess", 1]
        ],
        "b": ["On-Budget Direct Liability", "Off-Budget Disguised Liability"],
        "kw": "On-Budget vs Off-Budget Debt Classification",
        "e": "On-budget: Disclosed in annual financial statement (salaries, SDL interest, pensions); Off-budget: Hidden in SPVs, DISCOM guarantees, and special cesses to evade FRBM limits.",
        "data": "CAG and Ministry of Finance now mandate bringing all off-budget borrowing onto official balance sheets.",
        "ex": "KIIFB in Kerala or Andhra Pradesh State Development Corporation bonds.",
        "mains": "Technical public finance mastery for GS-3."
    },

    # --- Pattern 9: year (5 questions) ---
    {
        "id": "freebie_41",
        "topic": "Freebies & Welfare",
        "k": "year",
        "q": "Slide to the year Parliament enacted the landmark Fiscal Responsibility and Budget Management (FRBM) Act to institutionalize fiscal discipline:",
        "min": 1998,
        "max": 2010,
        "a": 2003,
        "tol": 0,
        "kw": "FRBM Act Enactment Year",
        "e": "The FRBM Act was enacted in August 2003 under the Vajpayee government to mandate reductions in fiscal deficits, eliminate revenue deficits, and enhance public debt transparency.",
        "data": "Act No. 39 of 2003; notified with effect from 5 July 2004.",
        "ex": "Setting statutory targets for Union and State fiscal consolidation.",
        "mains": "The foundational statutory milestone for fiscal discipline in India."
    },
    {
        "id": "freebie_42",
        "topic": "Freebies & Welfare",
        "k": "year",
        "q": "Slide to the year the Supreme Court delivered its landmark judgment in S. Subramaniam Balaji v. State of Tamil Nadu concerning election manifesto freebies:",
        "min": 2008,
        "max": 2020,
        "a": 2013,
        "tol": 0,
        "kw": "S. Subramaniam Balaji Judgment Year",
        "e": "The Supreme Court delivered its historic ruling in S. Subramaniam Balaji v. State of Tamil Nadu on 5 July 2013, holding that election manifestos are outside Section 123 of the RPA, 1951.",
        "data": "(2013) 9 SCC 659; directed the Election Commission of India to formulate election manifesto guidelines.",
        "ex": "Ruling on the distribution of color TVs, laptops, and mixers in Tamil Nadu elections.",
        "mains": "Crucial legal milestone cited in every election freebies litigation."
    },
    {
        "id": "freebie_43",
        "topic": "Freebies & Welfare",
        "k": "year",
        "q": "Slide to the year the Central Government officially launched the Pradhan Mantri Jan Dhan Yojana (PMJDY), creating the universal financial account pillar of the JAM Trinity:",
        "min": 2010,
        "max": 2020,
        "a": 2014,
        "tol": 0,
        "kw": "PMJDY Universal Account Launch",
        "e": "PMJDY was launched nationwide on 28 August 2014, opening over 53 Crore zero-balance bank accounts with RuPay debit cards and overdraft facilities, anchoring the DBT revolution.",
        "data": "Over 53 Crore accounts opened, with over 55% owned by women and 67% in rural/semi-urban areas.",
        "ex": "Enabling instant direct electronic cash transfers without bank branches or paperwork.",
        "mains": "The financial inclusion milestone that made modern targeted welfare delivery possible."
    },
    {
        "id": "freebie_44",
        "topic": "Freebies & Welfare",
        "k": "year",
        "q": "Slide to the year the Reserve Bank of India (RBI) published its landmark risk assessment report titled 'State Finances: A Risk Analysis' warning of severe debt stress across 10 vulnerable states:",
        "min": 2018,
        "max": 2026,
        "a": 2022,
        "tol": 0,
        "kw": "RBI State Finances Risk Study",
        "e": "In June 2022, the RBI published a landmark bulletin article titled 'State Finances: A Risk Analysis', diagnosing ballooning debt, unbudgeted subsidies, and DISCOM liabilities across Punjab, Rajasthan, Bihar, Kerala, and West Bengal.",
        "data": "Identified 10 states where debt-to-GSDP ratios were escalating toward unsustainable cliffs.",
        "ex": "Triggered national policy debates on the fiscal sustainability of sub-national guarantees.",
        "mains": "The primary economic trigger reigniting the contemporary 'revdi' debate."
    },
    {
        "id": "freebie_45",
        "topic": "Freebies & Welfare",
        "k": "year",
        "q": "Slide to the year the 16th Finance Commission of India was formally constituted by the President under the chairmanship of Dr. Arvind Panagariya:",
        "min": 2020,
        "max": 2026,
        "a": 2023,
        "tol": 0,
        "kw": "16th Finance Commission Constitution",
        "e": "The 16th Finance Commission was constituted on 31 December 2023 with Dr. Arvind Panagariya (former Vice-Chairman of NITI Aayog) as Chairman, tasked with recommending tax devolution for the 5-year award period 2026–2031.",
        "data": "Notified on 31 December 2023; mandated to submit recommendations by October 2025.",
        "ex": "Evaluating state off-budget borrowings, capital investments, and subsidy rationalization.",
        "mains": "The reigning institutional commission shaping India's federal fiscal trajectory."
    },

    # --- Pattern 11: flip (5 questions) ---
    {
        "id": "freebie_46",
        "topic": "Freebies & Welfare",
        "k": "flip",
        "q": "Draft a model 25-word opening hook for a UPSC Mains GS-3 answer on: 'Revdi Culture vs Social Welfare: The Growing Challenge of Sub-National Fiscal Profligacy'.",
        "r": "While targeted social safety nets fulfill constitutional DPSPs (Articles 38 and 41), unbudgeted electoral freebies weaponize competitive populism, crowd out capital investment, and mortgage inter-generational fiscal solvency. Balancing welfare equity with FRBM discipline is India's urgent federal imperative.",
        "kw": "Freebies Mains Opening Formula",
        "e": "Combines constitutional foundations (Art 38/41), macro-economic critique (capex crowding-out, inter-generational debt), and policy resolution in under 40 words.",
        "data": "Balances social justice with fiscal prudence.",
        "ex": "Instantly establishes an analytical, balanced, and constitutional tone.",
        "mains": "Memorize and reproduce in the first 30 seconds of any GS-2 or GS-3 question on freebies."
    },
    {
        "id": "freebie_47",
        "topic": "Freebies & Welfare",
        "k": "flip",
        "q": "Flip to reveal the 4-box comparison matrix contrasting 'Genuine Welfare / Merit Goods' with 'Populist Freebies':",
        "r": "1. OBJECTIVE: Merit Goods build human capability & public assets; Freebies induce election votes.\n2. EXTERNALITIES: Merit Goods generate high social returns & productivity; Freebies focus on private consumption with near-zero returns.\n3. MULTIPLIER: Capex & merit goods yield 2.5x-3.5x multiplier; Freebies yield < 0.9x.\n4. FINANCING: Merit Goods are budgeted with sustainable revenue; Freebies rely on off-budget debt & fiscal deficits.",
        "kw": "4-Box Welfare vs Freebies Comparison Matrix",
        "e": "Four core evaluation vectors: Objective, Externalities, Multiplier, and Financing. Drawing this table in Mains answers guarantees maximum clarity and marks.",
        "data": "Objective / Externalities / Multiplier / Financing taxonomy.",
        "ex": "Comparing school mid-day meals against election-eve color television distribution.",
        "mains": "The definitive comparative table for GS-2 and GS-3."
    },
    {
        "id": "freebie_48",
        "topic": "Freebies & Welfare",
        "k": "flip",
        "q": "Flip to reveal the 3-point economic argument explaining why 'Unconditional Cash Transfers to Women' are NOT wasteful freebies:",
        "r": "1. High Marginal Propensity to Consume (MPC): Poor female recipients spend transfers immediately on nutrition and children's education, boosting rural demand.\n2. Intra-Household Financial Agency: Direct cash reduces gender vulnerability and gives women decision-making autonomy.\n3. Leak-Free Delivery: Direct Benefit Transfer (DBT) over Jan Dhan accounts eliminates corrupt middleman cuts and administrative leakages.",
        "kw": "Economic Defense of Women UCTs",
        "e": "Provides the 3 economic defenses: Keynesian consumption velocity, feminist welfare economics, and digital public infrastructure efficiency.",
        "data": "MPC ~ 1.0; DBT leak-free savings > ₹38 Lakh Crore.",
        "ex": "Women heads of households in rural Tamil Nadu and MP allocating cash toward milk, vegetables, and school fees.",
        "mains": "Essential counter-argument preventing one-sided anti-poor bias in your answers."
    },
    {
        "id": "freebie_49",
        "topic": "Freebies & Welfare",
        "k": "flip",
        "q": "Flip to reveal the structural solution of 'Mandatory Fiscal Impact Statements in Election Manifestos':",
        "r": "Political parties must be legally mandated by the Election Commission of India (ECI) to submit an audited Fiscal Impact Statement with their manifestos. This statement must quantify: (a) The estimated annual financial cost of each poll promise, (b) The specific revenue sources (tax hikes, borrowing, or spending cuts) intended to fund them, and (c) Compliance with FRBM Act 3% GSDP debt limits.",
        "kw": "Mandatory Fiscal Impact Statements",
        "e": "Replaces vague, impossible election promises with quantified budgetary accountability before voters cast their ballots.",
        "data": "Proposed by ECI in its consultation paper to political parties (October 2022).",
        "ex": "Voters able to see whether a promised ₹2,000 dole will force an increase in electricity tariffs or bus fares.",
        "mains": "High-scoring governance reform proposal for GS-2 Electoral and Administrative reforms."
    },
    {
        "id": "freebie_50",
        "topic": "Freebies & Welfare",
        "k": "flip",
        "q": "Flip to reveal the statesmanlike concluding synthesis for an essay on: 'Fiscal Federalism, Democratic Accountability, and the Politics of Welfare':",
        "r": "A democratic state must remain compassionate to the marginalized without turning reckless with future generations. By institutionalizing statutory boundaries between merit goods and private doles, enforcing off-budget borrowing transparency under Article 293(3), and subjecting manifestos to fiscal costing, India can transition from transactional 'clientelism' to enduring human capability development, truly honoring the constitutional promise of Article 38.",
        "kw": "Statesmanlike Concluding Synthesis",
        "e": "A balanced, constitutional conclusion synthesizing compassion, inter-generational equity, transparency, and Article 38.",
        "data": "Synthesizes compassion, fiscal prudence, and democratic accountability.",
        "ex": "Positions India as a mature constitutional republic balancing economic growth with social inclusion.",
        "mains": "Flawless concluding paragraph for GS-2, GS-3, and UPSC Essay papers."
    }
]

print(f"Freebies questions prepared: {len(freebies_questions)}")
