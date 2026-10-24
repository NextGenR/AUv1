/**
 * CORTEX DUOLINGO LEARNING MODEL - MSME SECTOR & POLICY REFORMS
 * Topic: Micro, Small and Medium Enterprises (MSME) as Catalysts for Inclusive Growth
 * Sourced directly from ForumIAS Current Affairs Notes, Visual Mindmap, and Union Budget 2025-26
 */

const MSME_DATA = {
  id: "msme-catalysts",
  title: "MSMEs as Catalysts: Growth Engine, Statutory Architecture & Budget Reforms",
  syllabusTags: [
    "GS-3: Indian Economy & Mobilization of Resources",
    "GS-3: Industrial Policy, Manufacturing GVA & Employment",
    "CAVA Lecture: MSME Reforms"
  ],
  stats: {
    totalLevels: 10,
    totalXP: 320,
    estimatedMinutes: 30
  },

  // Flowchart Visual Artifact References
  flowcharts: [
    {
      id: "fc-classification",
      title: "Composite Classification Matrix & Multipliers",
      filename: "flowchart_msme_classification.svg",
      path: "Filtered_Questions/flowchart_msme_classification.svg",
      mobilePath: "assets/flowcharts/flowchart_msme_classification.svg",
      caption: "Composite Investment & Turnover ceilings (1/5, 10/50, 50/250) & 2.5x Multiplier"
    },
    {
      id: "fc-delayed-payments",
      title: "Delayed Payments & Section 43B(h) Workflow",
      filename: "flowchart_delayed_payments.svg",
      path: "Filtered_Questions/flowchart_delayed_payments.svg",
      mobilePath: "assets/flowcharts/flowchart_delayed_payments.svg",
      caption: "MSMED Act Sections 15-19, 3x Bank Rate Compounding & Section 43B(h) Tax Deduction"
    },
    {
      id: "fc-pm-vishwakarma",
      title: "PM Vishwakarma 5-Pillar Architecture",
      filename: "flowchart_pm_vishwakarma.svg",
      path: "Filtered_Questions/flowchart_pm_vishwakarma.svg",
      mobilePath: "assets/flowcharts/flowchart_pm_vishwakarma.svg",
      caption: "₹13,000 Cr outlay, 18 artisan trades, ₹15k toolkit, and ₹1L + ₹2L collateral-free credit @ 5%"
    },
    {
      id: "fc-dwarfism",
      title: "Dwarfism & Missing Middle vs. German Mittelstand",
      filename: "flowchart_dwarfism_vs_mittelstand.svg",
      path: "Filtered_Questions/flowchart_dwarfism_vs_mittelstand.svg",
      mobilePath: "assets/flowcharts/flowchart_dwarfism_vs_mittelstand.svg",
      caption: "Inverted pyramid of 99.4% micro units vs. German Mittelstand scale-neutral model"
    }
  ],

  // 1. FORUMIAS SHEET NOTES FORMAT (Exact PDF Replica)
  sheetNotes: {
    sheetCode: "CA - 260818",
    title: "MSMEs AS CATALYSTS: ECONOMIC ARCHITECTURE & REFORMS",
    sections: [
      {
        tag: "INTRO & MACRO BENCHMARK",
        bullets: [
          {
            text: "The Bedrock of India's Economic Architecture",
            detail: "MSMEs contribute 31.1% to India's GDP, 35.4% to Manufacturing Gross Value Added (GVA), and 48.6% to Total Merchandise Exports."
          },
          {
            text: "Democratization of Employment: 11.1 Crore Livelihoods",
            detail: "Over 6.33 crore MSME units nationwide; second largest employer in India after agriculture with low capital cost per job created."
          },
          {
            text: "Inclusive Social Footprint",
            detail: "More than 51% of MSMEs are situated in rural areas; substantial ownership by SC/ST/OBC entrepreneurs driving equitable regional growth."
          }
        ]
      },
      {
        tag: "CONTEXT & POLICY IMPERATIVE",
        bullets: [
          {
            text: "Transition from Regulatory Protectionism to Global Competitiveness",
            detail: "Shift from legacy 2006 bifurcated criteria to 2020 composite investment-turnover standards, augmented by Budget 2025-26 credit underwriting reforms."
          },
          {
            text: "Urgent Need to Dismantle the 'Missing Middle' & Dwarfism",
            detail: "Perverse incentives historically prompted firms to intentionally suppress scale to retain small-enterprise fiscal exemptions."
          }
        ]
      },
      {
        tag: "CONSTITUTIONAL & STATUTORY CANVAS",
        bullets: [
          {
            text: "Article 39(b) & 39(c) (Directive Principles of State Policy)",
            detail: "Distribution of material resources of the community to serve common good; preventing concentration of wealth in large corporate monopolies."
          },
          {
            text: "Article 19(1)(g) & Article 301",
            detail: "Right to practice any profession, trade, or business freely across India; supported by non-discriminatory public procurement policies."
          },
          {
            text: "Micro, Small and Medium Enterprises Development (MSMED) Act, 2006",
            detail: "Statutory framework for classification, Delayed Payments arbitration (Sec 15-19), and National Board for MSMEs."
          }
        ]
      },
      {
        type: "PROS_CONS",
        prosTag: "STRUCTURAL STRENGTHS & CATALYTIC POWER",
        consTag: "SYSTEMIC BOTTLENECKS & STRUCTURAL CHALLENGES",
        pros: [
          {
            text: "High Labor Intensity & Low Capital Barrier",
            detail: "Generates 4x more employment per unit of capital invested compared to large-scale organized manufacturing corporations."
          },
          {
            text: "Decentralized Regional Industrialization",
            detail: "Reduces rural-to-urban distress migration by developing localized value-chains in Tier-2/Tier-3 cities and rural clusters."
          },
          {
            text: "Industrial Agility & Supply Chain Resilience",
            detail: "Serves as essential ancillary feeder base for automotive, defense, electronics, aerospace, and pharmaceutical giants."
          },
          {
            text: "Export Dynamo",
            detail: "Supplies almost half of India's merchandise exports across textiles, engineering goods, leather, gems, and brassware."
          }
        ],
        cons: [
          {
            text: "The Dwarfism Paradox & 'Missing Middle'",
            detail: "Over 99.4% of units remain micro; firms stay small not because they are young, but because growing triggers a 'regulatory cliff'."
          },
          {
            text: "The ₹30 Lakh Crore Credit Gap",
            detail: "UK Sinha Committee estimated severe credit deficit; traditional banks demand physical immovable collateral rather than cash-flow data."
          },
          {
            text: "Delayed Payments & Working Capital Asphyxiation",
            detail: "Large buyers, private corporations, and CPSEs routinely delay payments well beyond 45 days, causing insolvency."
          },
          {
            text: "Technological & Green Transition Deficit",
            detail: "Low adoption of Industry 4.0 automation, AI-driven inventory management, and carbon compliance (e.g. EU CBAM tax hurdles)."
          }
        ]
      },
      {
        tag: "BUDGET 2025-26 & INSTITUTIONAL INITIATIVES",
        bullets: [
          {
            text: "Credit Guarantee Scheme for MSMEs in Manufacturing (Budget 2025)",
            detail: "Self-financing guarantee fund providing collateral-free credit cover up to ₹100 Crore per enterprise for machinery & equipment purchase."
          },
          {
            text: "New Digital Assessment Model for Credit",
            detail: "Public sector banks shifting from immovable collateral to scoring digital footprints, GST returns, and TReDS invoices."
          },
          {
            text: "Mandatory TReDS Onboarding & Mudra Ceiling Doubling",
            detail: "Turnover threshold for mandatory onboarding of buyers onto TReDS reduced to ₹500 Cr; Mudra 'Tarun Plus' ceiling doubled to ₹20 Lakh."
          },
          {
            text: "PM Vishwakarma Central Sector Scheme (₹13,000 Crore)",
            detail: "Full lifecycle support across 18 traditional artisan trades: PM Vishwakarma Certificate, ₹15k toolkit, and ₹1L + ₹2L loans at 5% interest."
          }
        ]
      },
      {
        type: "BOTTOM_GRID",
        suggestionsTag: "WAY FORWARD & POLICY ROADMAP",
        conclusionTag: "CONCLUDING STRATEGIC SYNTHESIS",
        suggestions: [
          {
            text: "Adopt the German 'Mittelstand' Model",
            detail: "Support medium enterprises with scale-neutral incentives, dual technical vocational training, and patient bank capital."
          },
          {
            text: "Strict Enforcement of Section 43B(h) & MSEFC Councils",
            detail: "Disallow tax deductions for buyers failing to pay within 45 days, and enforce the 75% pre-deposit rule under Section 19."
          },
          {
            text: "Establish E-Commerce Export Hubs (ECEH)",
            detail: "Facilitate single-window export clearance, warehousing, and testing for MSMEs to access cross-border digital consumers."
          },
          {
            text: "Cluster Agglomeration & SFURTI Expansion",
            detail: "Scale plug-and-play industrial parks and shared effluent treatment infrastructure (e.g. Tiruppur model)."
          }
        ],
        conclusion: [
          {
            text: "The Engine of Viksit Bharat 2047",
            detail: "\"MSMEs are not just a safety valve for surplus agricultural labor; they are the crucible where Indian entrepreneurship meets global manufacturing excellence. Unleashing them from dwarfism is the paramount prerequisite for India's $5 Trillion economy and Viksit Bharat.\""
          }
        ]
      }
    ]
  },

  // 2. DUOLINGO LEVEL-WISE LEARNING ROADMAP (10 Progressive Levels)
  levels: [
    {
      id: "msme-lvl-1",
      unit: "Unit 1: Macro Architecture & Structural Significance",
      unitColor: "#3b82f6", // Royal Blue
      levelNumber: 1,
      title: "The 31.1% Engine & Macro Pillars",
      badgeIcon: "🏭",
      xpReward: 25,
      description: "Master the macro statistics, GDP/GVA share, exports, and employment footprint of India's MSME sector.",
      tasks: [
        {
          type: "concept",
          title: "The Giant in Plain Sight",
          mascotMood: "excited",
          flowchart: "flowchart_msme_classification.svg",
          content: "India's MSME sector is the second largest employer after agriculture, sustaining **over 11.1 Crore jobs** across **6.33 Crore enterprises**.\n\n• **31.1%** of India's Gross Domestic Product (GDP)\n• **35.4%** of Manufacturing Gross Value Added (GVA)\n• **48.6%** of Total Merchandise Exports\n• **51.2%** located in rural hinterlands, bridging the urban-rural divide.",
          keyTakeaway: "MSMEs produce nearly 1/3rd of India's GDP and half of merchandise exports with exceptionally low capital per job."
        },
        {
          type: "mcq",
          prompt: "According to official data and ForumIAS notes, what is the exact share of the MSME sector in India's Gross Domestic Product (GDP)?",
          options: [
            "18.5 per cent",
            "24.2 per cent",
            "31.1 per cent",
            "42.8 per cent"
          ],
          correctIndex: 2,
          explanation: "MSMEs account for 31.1% of India's GDP, 35.4% of manufacturing GVA, and 48.6% of merchandise exports."
        },
        {
          type: "true_false",
          prompt: "True or False: June 27 is observed globally as International MSME Day, and globally MSMEs account for approximately 90% of all businesses and over 50% of employment.",
          correct: true,
          explanation: "Correct! UN designated June 27 as International MSME Day to recognize their fundamental economic role worldwide."
        },
        {
          type: "tap_order",
          prompt: "Assemble the core macroeconomic statistic regarding MSME exports:",
          tokens: ["MSMEs contribute", "nearly 48.6%", "of India's", "total merchandise", "exports."],
          correctSentence: "MSMEs contribute nearly 48.6% of India's total merchandise exports."
        }
      ]
    },

    {
      id: "msme-lvl-2",
      unit: "Unit 1: Macro Architecture & Structural Significance",
      unitColor: "#3b82f6",
      levelNumber: 2,
      title: "Composite Classification Matrix",
      badgeIcon: "📐",
      xpReward: 30,
      description: "Master the July 1, 2020 composite criteria: Investment + Turnover thresholds, 1:5 ratio, and the 2.5x turnover multiplier.",
      tasks: [
        {
          type: "concept",
          title: "The Unified Composite Criteria (2020)",
          mascotMood: "teaching",
          flowchart: "flowchart_msme_classification.svg",
          content: "Effective **July 1, 2020**, India abolished the distinction between manufacturing and service enterprises, adopting a dual **Investment AND Turnover** composite criteria:\n\n• **Micro:** Investment ≤ ₹1 Cr | Turnover ≤ ₹5 Cr (1:5 ratio)\n• **Small:** Investment ≤ ₹10 Cr | Turnover ≤ ₹50 Cr (1:5 ratio)\n• **Medium:** Investment ≤ ₹50 Cr | Turnover ≤ ₹250 Cr (1:5 ratio)\n\n**Key Rule:** Export turnover is completely EXCLUDED when calculating the turnover limit to encourage globalization!",
          keyTakeaway: "Exceeding either the Investment OR the Turnover ceiling immediately elevates the enterprise to the next higher category."
        },
        {
          type: "match_pairs",
          prompt: "Match the MSME Category with its official Investment & Turnover Ceilings:",
          pairs: [
            { left: "Micro Enterprise", right: "Investment ≤ ₹1 Cr & Turnover ≤ ₹5 Cr" },
            { left: "Small Enterprise", right: "Investment ≤ ₹10 Cr & Turnover ≤ ₹50 Cr" },
            { left: "Medium Enterprise", right: "Investment ≤ ₹50 Cr & Turnover ≤ ₹250 Cr" },
            { left: "Export Turnover", right: "Completely excluded from classification ceilings" }
          ]
        },
        {
          type: "mcq",
          prompt: "Under the composite criteria, what is the mathematical multiplier between the Investment ceiling and Turnover ceiling across Micro, Small, and Medium categories?",
          options: [
            "Turnover ceiling is exactly 2 times Investment ceiling across all tiers",
            "Turnover ceiling is exactly 5 times Investment ceiling across all tiers",
            "Turnover ceiling is 10 times Investment ceiling for Micro and 2 times for Medium",
            "Turnover ceiling is completely unrelated to Investment ceiling"
          ],
          correctIndex: 1,
          explanation: "In all three categories, Turnover is exactly 5 times the Investment ceiling: ₹1Cr:₹5Cr (5x), ₹10Cr:₹50Cr (5x), and ₹50Cr:₹250Cr (5x)."
        },
        {
          type: "true_false",
          prompt: "True or False: If a firm has an Investment in Plant & Machinery of ₹8 Crore and an annual Turnover of ₹55 Crore, it remains classified as a Small enterprise.",
          correct: false,
          explanation: "False! The composite criteria requires satisfying BOTH conditions. Because turnover (₹55 Cr) exceeds the Small threshold of ₹50 Cr, it is pushed into the Medium category."
        }
      ]
    },

    {
      id: "msme-lvl-3",
      unit: "Unit 2: Structural Challenges & Economic Concepts",
      unitColor: "#f59e0b", // Amber
      levelNumber: 3,
      title: "Dwarfism & The Missing Middle",
      badgeIcon: "📉",
      xpReward: 30,
      description: "Explore the inverted pyramid, the Economic Survey 2018-19 thesis on dwarfism, and contrast with the German Mittelstand.",
      tasks: [
        {
          type: "concept",
          title: "Dwarfs vs. Infants (Economic Survey 2018-19)",
          mascotMood: "concerned",
          flowchart: "flowchart_dwarfism_vs_mittelstand.svg",
          content: "Chief Economic Adviser Krishnamurthy Subramanian highlighted a fundamental flaw in Indian industrial policy:\n\n• **Infants:** Young firms that start small but rapidly scale up in productivity, employment, and technology.\n• **Dwarfs:** Firms that remain small despite being in business for over 10-20 years!\n\n**Why do firms stay small?** Historically, policy offered subsidies based on *size* rather than *age*, creating a 'regulatory cliff' where growing meant losing priority sector credit, tax exemptions, and labor inspection immunities.",
          keyTakeaway: "Over 99.4% of India's MSMEs are Micro units; only 0.52% are Small and 0.08% are Medium—a stark 'Missing Middle'."
        },
        {
          type: "mcq",
          prompt: "According to the Economic Survey 2018-19, what distinguishes 'dwarf' enterprises from 'infant' enterprises in India?",
          options: [
            "Dwarfs operate in agriculture while infants operate in manufacturing",
            "Dwarfs are enterprises that stay small throughout their multi-decade existence, whereas infants start small and rapidly scale",
            "Dwarfs have foreign institutional ownership while infants are purely domestic",
            "Dwarfs are fully registered on Udyam while infants operate in the informal unorganized sector"
          ],
          correctIndex: 1,
          explanation: "Infants are young firms with high growth potential, whereas dwarfs stay small for decades intentionally to exploit small-enterprise regulatory loopholes."
        },
        {
          type: "match_pairs",
          prompt: "Match the Industrial Structure Concept with its Definitional Attribute:",
          pairs: [
            { left: "Missing Middle", right: "Severe deficit of medium-sized enterprises (0.08%)" },
            { left: "German Mittelstand", right: "High-productivity, globally competitive niche leaders" },
            { left: "Regulatory Cliff", right: "Disincentive to expand due to loss of size-based subsidies" },
            { left: "Zombie Enterprise", right: "Insolvent firm surviving only on subsidized bank rollover" }
          ]
        },
        {
          type: "tap_order",
          prompt: "Assemble the structural recommendation from Economic Survey 2018-19:",
          tokens: ["Incentivize infant firms", "with sunset clauses", "rather than protecting", "perpetual dwarf enterprises."],
          correctSentence: "Incentivize infant firms with sunset clauses rather than protecting perpetual dwarf enterprises."
        }
      ]
    },

    {
      id: "msme-lvl-4",
      unit: "Unit 2: Structural Challenges & Economic Concepts",
      unitColor: "#f59e0b",
      levelNumber: 4,
      title: "Statutory Fortress: MSMED Act 2006",
      badgeIcon: "📜",
      xpReward: 35,
      description: "Master Sections 15 to 19 of the MSMED Act: 15-day default, 45-day ceiling, 3x Bank Rate compounding, and MSEFC arbitrations.",
      tasks: [
        {
          type: "concept",
          title: "The Delayed Payments Fortress (Sections 15-19)",
          mascotMood: "teaching",
          flowchart: "flowchart_delayed_payments.svg",
          content: "The MSMED Act 2006 contains stringent legal teeth to protect suppliers from delayed cash flows:\n\n• **Section 15:** Buyer MUST pay within the agreed period, which CANNOT exceed **45 days**. If no agreement exists, payment is due within **15 days**.\n• **Section 16:** Failure to pay attracts mandatory compound interest with monthly rests at **3 times the RBI Bank Rate**!\n• **Section 18:** Dispute referred to Micro and Small Enterprises Facilitation Council (MSEFC), which must conclude conciliation/arbitration within **90 days**.\n• **Section 19:** Buyer cannot appeal any MSEFC award in court without pre-depositing **75% of the decreed amount**!",
          keyTakeaway: "Section 16 penal interest is mandatory by law and cannot be waived even by private mutual agreement."
        },
        {
          type: "mcq",
          prompt: "Under Section 16 of the MSMED Act 2006, what is the statutory rate of penal interest payable by a defaulting buyer to a Micro or Small enterprise?",
          options: [
            "Simple interest at the prevailing SBI Prime Lending Rate",
            "Compound interest with monthly rests at 3 times the Bank Rate notified by the RBI",
            "Flat 18 per cent per annum simple interest",
            "Discretionary interest decided mutually by the parties"
          ],
          correctIndex: 1,
          explanation: "Section 16 prescribes compound interest with monthly rests at three times the RBI Bank Rate, creating severe financial deterrence against delayed payments."
        },
        {
          type: "true_false",
          prompt: "True or False: Under Section 19 of the MSMED Act, an appellant challenging an MSEFC decree in a civil court must deposit at least 75% of the awarded amount as a mandatory pre-condition.",
          correct: true,
          explanation: "Correct! Section 19 prevents large corporate buyers from using protracted litigation to starve small suppliers of funds."
        },
        {
          type: "tap_order",
          prompt: "Assemble the statutory payment timeline under Section 15 of MSMED Act:",
          tokens: ["Payment cannot exceed", "45 days by agreement", "or 15 days", "if no agreement exists."],
          correctSentence: "Payment cannot exceed 45 days by agreement or 15 days if no agreement exists."
        }
      ]
    },

    {
      id: "msme-lvl-5",
      unit: "Unit 3: Legal & Financial Game Changers",
      unitColor: "#10b981", // Emerald
      levelNumber: 5,
      title: "Section 43B(h) & Payment Revolution",
      badgeIcon: "⚖️",
      xpReward: 35,
      description: "Understand the Finance Act 2023 amendment to Section 43B of the Income Tax Act and its real-world economic impact.",
      tasks: [
        {
          type: "concept",
          title: "The Section 43B(h) Tax Shockwave",
          mascotMood: "excited",
          flowchart: "flowchart_delayed_payments.svg",
          content: "Inserted via Finance Act 2023 (effective AY 2024-25), **Section 43B(h)** of the Income Tax Act linked tax deductions directly to the MSMED Act:\n\n• Any sum payable by a buyer to a **Micro or Small enterprise** beyond the Section 15 time limit (15 or 45 days) is **DISALLOWED as a business expenditure** in that financial year!\n• The deduction is allowed ONLY in the subsequent year when actual payment is made.\n• **Critical Nuance:** It applies strictly to Micro and Small enterprises—**Medium enterprises are EXCLUDED**!\n• **Wholesalers/Traders:** Do not qualify for 43B(h) protection unless registered as manufacturers/service providers.",
          keyTakeaway: "Section 43B(h) transformed delayed payment from a contractual breach into a direct income tax penalty."
        },
        {
          type: "mcq",
          prompt: "Consider the following statements regarding Section 43B(h) of the Income Tax Act, 1961:\n1. It disallows tax deductions for expenditure incurred on purchases from Micro and Small enterprises if payments are delayed beyond the MSMED Act Section 15 timeline.\n2. The provision applies equally to transactions with Medium enterprises.\n3. The disallowed expenditure can be claimed as a deduction in the subsequent financial year when actual payment is completed.\nWhich of the statements given above are correct?",
          options: [
            "1 and 2 only",
            "1 and 3 only",
            "2 and 3 only",
            "1, 2 and 3"
          ],
          correctIndex: 1,
          explanation: "Statements 1 and 3 are correct. Statement 2 is incorrect because Section 43B(h) explicitly excludes Medium enterprises and applies solely to Micro and Small entities."
        },
        {
          type: "true_false",
          prompt: "True or False: A corporate buyer who purchases goods from an unregistered informal enterprise without an Udyam certificate faces automatic tax disallowance under Section 43B(h).",
          correct: false,
          explanation: "False! Section 43B(h) applies only when the supplier is formally registered as a Micro or Small enterprise on the Udyam portal."
        },
        {
          type: "tap_order",
          prompt: "Assemble the core operation of Section 43B(h):",
          tokens: ["Delayed payments to MSMEs", "are disallowed as deductions", "and taxed as income", "in that fiscal year."],
          correctSentence: "Delayed payments to MSMEs are disallowed as deductions and taxed as income in that fiscal year."
        }
      ]
    },

    {
      id: "msme-lvl-6",
      unit: "Unit 3: Legal & Financial Game Changers",
      unitColor: "#10b981",
      levelNumber: 6,
      title: "PM Vishwakarma & Traditional Artisans",
      badgeIcon: "🔨",
      xpReward: 30,
      description: "Master the 5-pillar architecture of PM Vishwakarma: 18 traditional trades, ₹15,000 toolkits, and subsidized 5% enterprise credit.",
      tasks: [
        {
          type: "concept",
          title: "PM Vishwakarma: Guru-Shishya Parampara",
          mascotMood: "happy",
          flowchart: "flowchart_pm_vishwakarma.svg",
          content: "Launched on Vishwakarma Jayanti (Sept 17, 2023) with a **₹13,000 Crore** fully Central Sector outlay:\n\n• **Target:** Traditional artisans and craftspeople working with hands and tools across **18 designated trades** (carpenter, blacksmith, potter, cobbler, weaver, etc.).\n• **5-Pillar Architecture:**\n  1. Recognition: PM Vishwakarma Certificate & Digital ID\n  2. Skill Upgradation: 5-7 days basic training (₹500/day stipend) + 15 days advanced\n  3. Toolkit Incentive: ₹15,000 e-voucher for modern precision tools\n  4. Credit Support: Collateral-free loans of ₹1 Lakh (Tranche 1) + ₹2 Lakh (Tranche 2) at **5% concessional interest** (8% subvention paid by GoI)\n  5. Digital Transaction Incentives & Market Linkages (GeM & ONDC integration).",
          keyTakeaway: "PM Vishwakarma integrates centuries-old informal artisan trades into the formal financial and e-commerce ecosystem."
        },
        {
          type: "mcq",
          prompt: "Which of the following is NOT one of the benefits provided under the PM Vishwakarma Scheme?",
          options: [
            "Concessional collateral-free enterprise credit up to ₹3 Lakh in two tranches at 5 per cent interest",
            "Toolkit incentive of ₹15,000 through electronic vouchers",
            "Unconditional direct cash transfer of ₹50,000 per month for life",
            "Skill verification, basic training with ₹500 daily stipend, and advanced training"
          ],
          correctIndex: 2,
          explanation: "PM Vishwakarma does not provide monthly lifetime pensions or unconditional cash transfers. It provides skill training, ₹15k toolkits, and subsidized credit."
        },
        {
          type: "match_pairs",
          prompt: "Match the PM Vishwakarma Component with its Statutory Detail:",
          pairs: [
            { left: "Financial Outlay", right: "₹13,000 Crore (100% Central Sector Scheme)" },
            { left: "Artisan Trades Covered", right: "18 traditional trades across rural and urban India" },
            { left: "Concessional Loan Rate", right: "5% interest (Government provides 8% subvention)" },
            { left: "Modern Toolkit Incentive", right: "₹15,000 via e-RUPI / electronic voucher" }
          ]
        },
        {
          type: "true_false",
          prompt: "True or False: The Udyam Assist Platform (UAP) was launched to enable informal micro enterprises lacking GST registration to obtain priority sector lending certificates.",
          correct: true,
          explanation: "Correct! UAP brought over 1.5 crore informal micro enterprises into formal priority sector lending without requiring mandatory GSTIN."
        }
      ]
    },

    {
      id: "msme-lvl-7",
      unit: "Unit 4: Future Reforms & Institutional Ecosystem",
      unitColor: "#6366f1", // Indigo
      levelNumber: 7,
      title: "Union Budget 2025-26 & Credit Underwriting",
      badgeIcon: "🏦",
      xpReward: 35,
      description: "Explore the self-financing guarantee fund up to ₹100 Cr, digital footprint underwriting, TReDS mandates, and Mudra Tarun Plus.",
      tasks: [
        {
          type: "concept",
          title: "The Credit Underwriting Revolution (Budget 2025-26)",
          mascotMood: "excited",
          content: "Union Budget 2025-26 introduced pathbreaking credit reforms to break the ₹30 Lakh Crore credit deficit:\n\n• **₹100 Crore Credit Guarantee Cover:** A self-financing guarantee fund providing collateral-free credit cover up to ₹100 Crore for term loans to acquire machinery and equipment.\n• **Collateral-Free Digital Scoring:** Public sector banks will assess loan eligibility using **digital footprints** (GST filings, UPI transactions, bank flows) rather than insisting on physical immovable land collateral!\n• **TReDS Expansion:** Lowered mandatory onboarding threshold for buyers to **₹500 Crore** turnover, and mandated all CPSEs to onboard.\n• **Mudra Loan Expansion:** Ceiling under Mudra 'Tarun Plus' category doubled from **₹10 Lakh to ₹20 Lakh** for entrepreneurs who successfully repaid previous loans.",
          keyTakeaway: "Moving from balance-sheet lending to cash-flow based digital underwriting unlocks bank credit for asset-light enterprises."
        },
        {
          type: "mcq",
          prompt: "As announced in the Union Budget 2025-26, what major reform was introduced in the credit assessment mechanism for MSMEs by Public Sector Banks?",
          options: [
            "Mandating 100% gold mortgaging for all manufacturing loans",
            "Shifting from physical immovable collateral to scoring digital footprints and transaction data",
            "Restricting all bank lending exclusively to public sector undertakings",
            "Abolishing the requirement of any credit evaluation for loans under ₹50 Crore"
          ],
          correctIndex: 1,
          explanation: "Public sector banks have developed in-house digital scoring models that analyze GST, electricity bills, and banking flows, eliminating the requirement for physical land mortgages."
        },
        {
          type: "true_false",
          prompt: "True or False: Under Union Budget 2025-26, the loan ceiling under the Pradhan Mantri Mudra Yojana (Tarun category) was doubled from ₹10 Lakh to ₹20 Lakh.",
          correct: true,
          explanation: "Correct! The 'Tarun Plus' category now offers up to ₹20 Lakh for entrepreneurs who have previously availed and successfully repaid Tarun loans."
        },
        {
          type: "tap_order",
          prompt: "Assemble the key Budget 2025-26 manufacturing guarantee reform:",
          tokens: ["Guarantee cover up to ₹100 Cr", "for purchasing machinery", "without third-party collateral", "or land mortgage."],
          correctSentence: "Guarantee cover up to ₹100 Cr for purchasing machinery without third-party collateral or land mortgage."
        }
      ]
    },

    {
      id: "msme-lvl-8",
      unit: "Unit 4: Future Reforms & Institutional Ecosystem",
      unitColor: "#6366f1",
      levelNumber: 8,
      title: "Public Procurement & GeM Mandate",
      badgeIcon: "🛒",
      xpReward: 30,
      description: "Master the 25% annual procurement mandate, sub-targets for SC/ST and Women, and GeM portal non-discriminatory access.",
      tasks: [
        {
          type: "concept",
          title: "Public Procurement Policy (2012 & 2018 Amendments)",
          mascotMood: "teaching",
          content: "Every Central Ministry, Department, and Central Public Sector Enterprise (CPSE) is mandated by law to fulfill specific procurement quotas:\n\n• **25% Mandatory Annual Procurement:** Minimum 25% of all goods and services procured must be sourced from MSEs.\n• **4% Sub-Target:** Earmarked specifically for MSEs owned by **SC/ST entrepreneurs**.\n• **3% Sub-Target:** Earmarked specifically for MSEs owned by **Women entrepreneurs**.\n• **358 Items Reserved:** Exclusively reserved for manufacture and procurement from the micro and small sector.\n• **GeM (Government e-Marketplace):** Level-playing digital field eliminating cartel intermediaries.",
          keyTakeaway: "Public procurement guarantees an assured ₹50,000+ Crore annual domestic market for small entrepreneurs."
        },
        {
          type: "mcq",
          prompt: "Under the Public Procurement Policy for Micro and Small Enterprises, what are the mandatory overall procurement percentage and the specific sub-quota for women entrepreneurs?",
          options: [
            "20% overall and 1% for women entrepreneurs",
            "25% overall and 3% for women entrepreneurs",
            "30% overall and 5% for women entrepreneurs",
            "15% overall and 2% for women entrepreneurs"
          ],
          correctIndex: 1,
          explanation: "The statutory policy mandates 25% annual procurement from MSEs, with 4% earmarked for SC/ST and 3% earmarked for Women entrepreneurs."
        },
        {
          type: "match_pairs",
          prompt: "Match the Procurement Policy Component with its Statutory Mandate:",
          pairs: [
            { left: "Overall MSE Procurement", right: "25% mandatory annual value from Central CPSEs" },
            { left: "SC/ST Entrepreneur Quota", right: "4% earmarked sub-target" },
            { left: "Women Entrepreneur Quota", right: "3% earmarked sub-target" },
            { left: "Tender Fee & EMD", right: "100% exemption for Udyam-registered MSEs" }
          ]
        },
        {
          type: "true_false",
          prompt: "True or False: Udyam-registered Micro and Small enterprises are legally exempt from paying tender document fees and Earnest Money Deposits (EMD) when bidding for government contracts.",
          correct: true,
          explanation: "Correct! This removes working capital bottlenecks and allows small firms to compete freely with large conglomerates."
        }
      ]
    },

    {
      id: "msme-lvl-9",
      unit: "Unit 5: Cluster Agglomeration & Industrial Case Studies",
      unitColor: "#8b5cf6", // Purple
      levelNumber: 9,
      title: "Cluster Agglomeration & Export Hubs",
      badgeIcon: "🌐",
      xpReward: 35,
      description: "Examine Tiruppur's knitwear miracle, SFURTI cluster regeneration, E-Commerce Export Hubs (ECEH), and ONDC.",
      tasks: [
        {
          type: "concept",
          title: "The Tiruppur Miracle & Agglomeration Economics",
          mascotMood: "excited",
          flowchart: "flowchart_dwarfism_vs_mittelstand.svg",
          content: "Why are industrial clusters the holy grail of MSME competitiveness?\n\n• **Tiruppur Knitwear Cluster:** Generates **over $4 Billion in exports**; over 90% of units are MSMEs. They achieved global scale through **shared infrastructure** (Common Effluent Treatment Plants with Zero Liquid Discharge) and division of specialized labor.\n• **SFURTI Scheme:** Fund for Regeneration of Traditional Industries—modernizes artisan clusters with Common Facility Centers (CFCs) and design labs.\n• **E-Commerce Export Hubs (ECEH):** Budget 2024-26 initiative enabling cross-border logistics, customs pre-clearance, and bonded warehousing for MSME artisans.\n• **ONDC:** Democratizes digital e-commerce, freeing small kiranas and artisans from Amazon/Flipkart 30% commission monopolies.",
          keyTakeaway: "Clusters convert individual atomized weakness into collective industrial power through shared capital."
        },
        {
          type: "mcq",
          prompt: "In the context of MSME export facilitation and digital inclusion, how does the Open Network for Digital Commerce (ONDC) empower small merchants?",
          options: [
            "By offering 100% subsidized air freight for export consignments",
            "By unbundling the e-commerce value chain so buyers and sellers interact without being locked into proprietary single-platform monopolies",
            "By replacing all national currencies with central bank cryptocurrency",
            "By prohibiting large corporate brands from selling goods online"
          ],
          correctIndex: 1,
          explanation: "ONDC uses open network protocols (like UPI for payments) to allow small sellers on any catalog application to be discovered by buyers on any consumer app without 30% platform monopolies."
        },
        {
          type: "tap_order",
          prompt: "Assemble the strategic advantage of industrial cluster agglomeration:",
          tokens: ["Shared common infrastructure", "lowers capital barriers", "and boosts global", "export competitiveness."],
          correctSentence: "Shared common infrastructure lowers capital barriers and boosts global export competitiveness."
        },
        {
          type: "true_false",
          prompt: "True or False: Under the SFURTI scheme, the Government provides financial assistance up to ₹5 Crore to establish Common Facility Centers (CFCs) for traditional khadi, coir, and bamboo artisan clusters.",
          correct: true,
          explanation: "Correct! SFURTI funds shared machinery, quality testing labs, and training centers that individual artisans could never afford independently."
        }
      ]
    },

    {
      id: "msme-lvl-10",
      unit: "Unit 5: Cluster Agglomeration & Industrial Case Studies",
      unitColor: "#8b5cf6",
      levelNumber: 10,
      title: "BOSS BATTLE: The Regulatory Cliff & Overlord",
      badgeIcon: "👑",
      xpReward: 60,
      description: "DEFEND ARTICLE 39 & UNLEASH VIKSIT BHARAT! Defeat the Regulatory Cliff and Delayed Payment Syndicate in an epic 1000 HP battle!",
      tasks: [
        {
          type: "concept",
          title: "The Ultimate Gauntlet: Defeating Dwarfism",
          mascotMood: "teaching",
          flowchart: "flowchart_dwarfism_vs_mittelstand.svg",
          content: "You have arrived at the final frontier of India's economic transformation. The **Regulatory Cliff & Syndicate Overlord (1000 HP)** thrives on:\n\n1. Keeping 99% of firms trapped as micro entities\n2. Choking working capital with delayed payments past 45 days\n3. Demanding physical land collateral that young entrepreneurs lack\n\nDeploy your mastery of **Sections 15-19**, **Section 43B(h)**, **PM Vishwakarma**, and **Budget 2025-26** to conquer this boss!",
          keyTakeaway: "Unshackling MSMEs creates the high-productivity Mittelstand required for a $5 Trillion economy."
        },
        {
          type: "mcq",
          prompt: "BOSS CHALLENGE 1: A manufacturing firm in Pune has an investment in machinery of ₹9 Crore, domestic turnover of ₹45 Crore, and export turnover of ₹35 Crore. Under the MSMED 2020 classification criteria, what is its exact statutory status?",
          options: [
            "Medium Enterprise because total turnover is ₹80 Crore (exceeds ₹50 Cr)",
            "Small Enterprise because export turnover is excluded, leaving net qualifying turnover at ₹45 Crore (≤ ₹50 Cr)",
            "Micro Enterprise because net investment after depreciation is below ₹1 Crore",
            "Disqualified from MSME status due to exceeding foreign trade limits"
          ],
          correctIndex: 1,
          explanation: "CRITICAL HIT! Export turnover is strictly excluded from classification. Net qualifying turnover is ₹45 Cr (≤ ₹50 Cr) and investment is ₹9 Cr (≤ ₹10 Cr), making it firmly a Small Enterprise!"
        },
        {
          type: "match_pairs",
          prompt: "BOSS CHALLENGE 2: Connect the Statutory & Institutional Mechanisms with their Strategic Missions:",
          pairs: [
            { left: "Section 16 MSMED Act", right: "Compound interest at 3x RBI Bank Rate for delayed payments" },
            { left: "Section 43B(h) IT Act", right: "Disallowance of buyer tax deductions if payment exceeds 45 days" },
            { left: "Budget 2025 Guarantee", right: "₹100 Cr collateral-free cover for machinery acquisition" },
            { left: "PM Vishwakarma", right: "Full lifecycle support across 18 artisan trades with 5% loans" }
          ]
        },
        {
          type: "mcq",
          prompt: "BOSS CHALLENGE 3: Which committee appointed by the Ministry of MSME recommended removing size-based concessions and transitioning towards scale-neutral support to eradicate dwarfism?",
          options: [
            "Justice B.N. Srikrishna Committee",
            "Dr. K.P. Krishnan Committee on Regulatory Simplification",
            "Kelkar Committee on PPP Models",
            "Justice A.K. Rajan Committee"
          ],
          correctIndex: 1,
          explanation: "SUPER EFFECTIVE! The Dr. K.P. Krishnan Committee recommended replacing arbitrary size cliffs with sunset clauses and scale-neutral compliance."
        },
        {
          type: "tap_order",
          prompt: "BOSS FINISHER: Assemble the golden concluding thesis on India's MSME revolution:",
          tokens: ["MSMEs are the crucible", "where Indian entrepreneurship", "meets global competitiveness", "to power Viksit Bharat 2047."],
          correctSentence: "MSMEs are the crucible where Indian entrepreneurship meets global competitiveness to power Viksit Bharat 2047."
        }
      ]
    }
  ]
};

// Export to Global Scope for Web & Mobile
if (typeof window !== 'undefined') {
  window.MSME_DATA = MSME_DATA;
}
if (typeof module !== 'undefined' && module.exports) {
  module.exports = MSME_DATA;
}
