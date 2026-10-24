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
            text: "Joseph Schumpeter's 'Creative Destruction' vs Capital Locking",
            detail: "Healthy economies thrive through continuous innovation where dynamic firms displace obsolete enterprises. Rigid exit barriers and distortionary subsidies lock capital and labor in unproductive dwarf units, choking creative destruction."
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

  // 2. DUOLINGO LEVEL-WISE LEARNING ROADMAP (10 Progressive Levels - 100% Innovative Formats)
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
          type: "cloze_chips",
          prompt: "Snap the verified macroeconomic benchmarks into the official policy assessment:",
          template: "India's MSME sector powers {1} of Gross Domestic Product (GDP), generates {2} of Manufacturing Gross Value Added (GVA), and drives {3} of total merchandise exports while sustaining {4} livelihoods nationwide.",
          blanks: [
            { id: 1, correct: "31.1%" },
            { id: 2, correct: "35.4%" },
            { id: 3, correct: "48.6%" },
            { id: 4, correct: "11.1 Crore" }
          ],
          chips: ["31.1%", "35.4%", "48.6%", "11.1 Crore", "18.5%", "24.2%", "5.2 Crore", "62.4%"],
          explanation: "Official Ministry of MSME & CAVA data: MSMEs account for 31.1% of GDP, 35.4% of manufacturing GVA, 48.6% of merchandise exports, and over 11.1 Crore jobs."
        },
        {
          type: "match_pairs",
          prompt: "Connect each Macro Pillar with its Concrete National Impact:",
          pairs: [
            { left: "31.1% of National GDP", right: "Nearly 1/3rd contribution to India's total economic output" },
            { left: "35.4% Manufacturing GVA", right: "Dominant engine of value-added industrial output" },
            { left: "48.6% Merchandise Exports", right: "Crucial foreign exchange earner in textiles, brass & engineering" },
            { left: "51.2% Rural Footprint", right: "Mitigates distress urbanization through decentralized livelihoods" }
          ]
        },
        {
          type: "binary_verdict",
          prompt: "Evaluate this macroeconomic policy claim against official MSME census data:",
          scenario: "\"Because modern manufacturing requires high-density urban infrastructure, over 70% of Indian MSME enterprises are concentrated in Tier-1 metropolitan cities, rendering them ineffective at mitigating rural distress migration.\"",
          verdictQuestion: "Is this geographic concentration assertion factually and analytically VALID?",
          labels: { trueLabel: "FACT / VALID", falseLabel: "MYTH / INVALID" },
          correct: false,
          explanation: "MYTH / INVALID! Over 51.2% of MSMEs in India are situated in rural hinterlands. They serve as the foremost vehicle of inclusive decentralized industrialization and prevent distress rural-to-urban migration."
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
      description: "Master the July 1, 2020 composite criteria: Investment + Turnover thresholds, 1:5 ratio, and export turnover exclusion.",
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
          type: "category_sorter",
          prompt: "Classify each industrial enterprise profile into its exact statutory tier under the 2020 Composite Criteria:",
          categories: ["Micro Enterprise", "Small Enterprise", "Medium Enterprise"],
          items: [
            { text: "Unit Alpha: Plant ₹80 Lakh | Annual Turnover ₹4.2 Crore", category: "Micro Enterprise" },
            { text: "Unit Beta: Plant ₹8 Crore | Annual Turnover ₹42 Crore", category: "Small Enterprise" },
            { text: "Unit Gamma: Plant ₹25 Crore | Annual Turnover ₹180 Crore", category: "Medium Enterprise" },
            { text: "Unit Delta: Plant ₹90 Lakh | Annual Turnover ₹8.5 Crore", category: "Small Enterprise" }
          ],
          explanation: "Composite criteria requires satisfying BOTH conditions (1/5, 10/50, 50/250). Unit Delta has investment under ₹1 Cr, but because its turnover (₹8.5 Cr) breaches the ₹5 Cr micro ceiling, it is classified as a Small Enterprise."
        },
        {
          type: "flaw_hunter",
          prompt: "Three of these statutory provisions regarding MSME classification are genuine. Spot the SINGLE FLAWED provision:",
          statements: [
            { text: "The composite classification criteria applies uniformly across both manufacturing and service enterprises without sectoral distinction.", isFlaw: false },
            { text: "For all three tiers (Micro, Small, Medium), the turnover threshold is exactly 5 times the investment ceiling.", isFlaw: false },
            { text: "Export turnover of goods and services is fully included when computing whether an enterprise breaches the turnover ceiling.", isFlaw: true, flawReason: "STATUTORY FLAW IDENTIFIED! Under Notification S.O. 2119(E), export turnover of goods or services is COMPLETELY EXCLUDED from the calculation of turnover to incentivize global competitiveness." },
            { text: "Exceeding either the investment ceiling OR the turnover ceiling pushes the enterprise into the higher category.", isFlaw: false }
          ],
          explanation: "Export turnover is statutorily excluded to prevent penalizing enterprises that expand into international export markets."
        },
        {
          type: "binary_verdict",
          prompt: "Review the Tax Inspector's statutory determination under the 2020 composite rules:",
          scenario: "M/s Sahyadri Precision Tools has an Investment in Plant of ₹8 Crore, Domestic Turnover of ₹45 Crore, and Export Turnover of ₹30 Crore (Gross Turnover = ₹75 Crore). The Tax Inspector reclassifies it as 'Medium' because total turnover exceeds ₹50 Crore.",
          verdictQuestion: "Is the Tax Inspector's reclassification as 'Medium' legally valid?",
          labels: { trueLabel: "UPHELD / VALID", falseLabel: "REVERSED / ILLEGAL" },
          correct: false,
          explanation: "REVERSED / ILLEGAL! Export turnover (₹30 Cr) is statutorily excluded. Qualifying turnover is strictly ₹45 Cr (≤ ₹50 Cr limit) and investment is ₹8 Cr (≤ ₹10 Cr limit). The enterprise remains firmly classified as a SMALL Enterprise."
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
          content: "Chief Economic Adviser Krishnamurthy Subramanian and CAVA Lecture 4 highlight a fundamental flaw in Indian industrial policy:\n\n• **Infants:** Young firms that start small but rapidly scale up in productivity, employment, and technology.\n• **Dwarfs:** Firms that remain small despite being in business for over 10-20 years!\n• **Creative Destruction (Joseph Schumpeter):** Dynamic economies thrive when innovative firms displace obsolete units. In India, rigid exit barriers and distortionary subsidies trap capital in unproductive dwarf units, choking creative destruction.\n\n**Why do firms stay small?** Historically, policy offered subsidies based on *size* rather than *age*, creating a 'regulatory cliff' where growing meant losing priority sector credit, tax exemptions, and labor inspection immunities.\n\nOver 99.4% of India's MSMEs are Micro units; only 0.52% are Small and 0.08% are Medium—a stark 'Missing Middle'.",
          keyTakeaway: "Policy must incentivize infant firms with sunset clauses rather than permanently subsidizing perpetual dwarf enterprises."
        },
        {
          type: "category_sorter",
          prompt: "Assign each industrial dynamic to Infant Enterprises vs Dwarf Enterprises (Economic Survey 2018-19):",
          categories: ["Infant Enterprises (Sunset Subsidies)", "Dwarf Enterprises (Pathological Stagnation)"],
          items: [
            { text: "Young firms (< 10 yrs) that start small and experience rapid productivity & headcount growth", category: "Infant Enterprises (Sunset Subsidies)" },
            { text: "Enterprises operating for 10-20+ years that intentionally suppress scale to retain small-size subsidies", category: "Dwarf Enterprises (Pathological Stagnation)" },
            { text: "Nurtured through age-based support frameworks equipped with mandatory sunset clauses", category: "Infant Enterprises (Sunset Subsidies)" },
            { text: "Trap valuable capital and labor in unproductive low-wage units, choking creative destruction", category: "Dwarf Enterprises (Pathological Stagnation)" }
          ],
          explanation: "Smallness is natural and healthy for young infants, but pathological for aged dwarfs that intentionally suppress expansion to evade labor laws and retain size-based fiscal protections."
        },
        {
          type: "match_pairs",
          prompt: "Connect each Industrial Structure Concept with its Core Analytical Definition:",
          pairs: [
            { left: "Creative Destruction", right: "Schumpeterian innovation where dynamic firms displace obsolete enterprises" },
            { left: "Missing Middle", right: "Bimodal distribution: 99.4% tiny micro units vs few large conglomerates" },
            { left: "German Mittelstand", right: "High-productivity, scale-neutral mid-sized export champions" },
            { left: "Regulatory Cliff", right: "Disincentive to expand due to sudden loss of priority subsidies & labor exemptions" }
          ]
        },
        {
          type: "flaw_hunter",
          prompt: "Identify the economically FLAWED statement regarding India's missing middle and industrial policy:",
          statements: [
            { text: "Over 99.4% of India's MSMEs are classified as Micro units, while Medium enterprises account for less than 0.1% of the total.", isFlaw: false },
            { text: "Dwarf enterprises dominate Indian manufacturing because micro-units achieve significantly higher labor productivity and innovation than mid-sized firms.", isFlaw: true, flawReason: "ECONOMIC FLAW IDENTIFIED! Empirical data proves medium and large firms generate dramatically higher labor productivity, wages, and export competitiveness. Dwarfism persists due to perverse regulatory incentives to stay small, not superior efficiency." },
            { text: "Sun-setting size-based reservations and transitioning to age-based support encourages infant firms to scale into mature corporations.", isFlaw: false },
            { text: "In Germany, the Mittelstand forms the resilient backbone of industrial manufacturing, vocational training, and global niche exports.", isFlaw: false }
          ],
          explanation: "Dwarf enterprises suffer from significantly lower labor productivity than scaled firms. Their numerical preponderance is an artifact of regulatory distortions."
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
          type: "cloze_chips",
          prompt: "Snap the exact statutory numbers and terms into the MSMED Act legal framework:",
          template: "Under Section 15, the agreed credit period cannot exceed {1} (or {2} if no agreement exists). Section 16 mandates penal compound interest at {3} with monthly rests. Under Section 19, an appellant must pre-deposit {4} of the award before challenging an MSEFC decree.",
          blanks: [
            { id: 1, correct: "45 days" },
            { id: 2, correct: "15 days" },
            { id: 3, correct: "3x RBI Bank Rate" },
            { id: 4, correct: "75% of decreed amount" }
          ],
          chips: ["45 days", "15 days", "3x RBI Bank Rate", "75% of decreed amount", "60 days", "30 days", "2x Repo Rate", "50% pre-deposit"],
          explanation: "Section 15 mandates payment within 45 days (agreed) or 15 days (default). Section 16 imposes compound penal interest at 3x RBI Bank Rate. Section 19 requires 75% pre-deposit for appeals."
        },
        {
          type: "case_judge",
          prompt: "Act as the Presiding Arbitrator on the Micro and Small Enterprises Facilitation Council (MSEFC):",
          caseDossier: {
            title: "M/s Vapi Precision (Micro) vs Apex Heavy CPSE (Delayed Supply Claim)",
            facts: [
              "Vapi Precision supplied precision hydraulic valves worth ₹40 Lakh to Apex Heavy CPSE on Oct 1.",
              "No formal written credit agreement was executed between the parties.",
              "Apex Heavy CPSE released the principal payment on Day 85, citing internal CPSE audit delays.",
              "Apex Heavy argues that corporate audit procedures and commercial goodwill waive any penal interest liability."
            ]
          },
          question: "Render the statutory arbitral decree under Sections 15 & 16 of the MSMED Act:",
          options: [
            { text: "Dismiss claim: Lack of written agreement and CPSE audit protocol permits commercial extension up to 90 days without penalty.", isVerdict: false },
            { text: "Decree mandatory compound penal interest at 3 times RBI Bank Rate with monthly rests from Day 16 to Day 85, as Section 16 cannot be waived by private consent.", isVerdict: true },
            { text: "Order simple interest at standard SBI savings rate of 4% per annum starting from Day 46 onwards.", isVerdict: false }
          ],
          explanation: "In the absence of a written agreement, Section 15 mandates payment within 15 days. Section 16 penal interest is mandatory by operation of law and cannot be waived by internal audit delays or mutual goodwill."
        },
        {
          type: "match_pairs",
          prompt: "Match each MSMED Act Section with its Statutory Legal Mandate:",
          pairs: [
            { left: "Section 15 MSMED", right: "Mandatory payment ceiling of 45 days (agreed) or 15 days (default)" },
            { left: "Section 16 MSMED", right: "Mandatory compound penal interest at 3x RBI Bank Rate with monthly rests" },
            { left: "Section 18 MSMED", right: "MSEFC conciliation and arbitral decree mandated within 90 days" },
            { left: "Section 23 MSMED", right: "Explicit disallowance of penal interest as a deductible business expense" }
          ]
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
          type: "category_sorter",
          prompt: "Assign each commercial supplier based on whether delayed payments trigger Section 43B(h) tax disallowances:",
          categories: ["Covered under 43B(h) (Disallowance Triggered)", "Excluded from 43B(h) (No Tax Penalty)"],
          items: [
            { text: "Udyam-registered Micro Precision Machining Unit", category: "Covered under 43B(h) (Disallowance Triggered)" },
            { text: "Udyam-registered Small IT Architecture & Coding Consultancy", category: "Covered under 43B(h) (Disallowance Triggered)" },
            { text: "Medium-scale Auto Component Enterprise (Turnover ₹140 Cr)", category: "Excluded from 43B(h) (No Tax Penalty)" },
            { text: "Wholesale Hardware Distributor (Registered under Retail/Wholesale NIC code)", category: "Excluded from 43B(h) (No Tax Penalty)" }
          ],
          explanation: "Section 43B(h) strictly covers Micro and Small manufacturing/service enterprises. Medium enterprises and pure wholesale/retail traders are explicitly excluded from 43B(h) tax protection."
        },
        {
          type: "flaw_hunter",
          prompt: "Spot the legal FLAW among these Section 43B(h) corporate tax compliance statements:",
          statements: [
            { text: "Section 43B(h) was introduced via Finance Act 2023 to link income tax deduction disallowances with MSMED Act payment timelines.", isFlaw: false },
            { text: "If a buyer fails to pay within the 45-day window, the business expense is permanently forfeited and can NEVER be claimed as a tax deduction in any future assessment year.", isFlaw: true, flawReason: "TAX LAW FLAW DETECTED! Section 43B(h) does not permanently forfeit the deduction. It disallows the expense in the year of delay, but RESTORES the deduction in the subsequent financial year in which actual payment is cleared." },
            { text: "Section 43B(h) protection applies only when the vendor is formally registered on the Udyam portal as a Micro or Small enterprise.", isFlaw: false },
            { text: "Medium enterprises are outside the statutory ambit of Section 43B(h) disallowance rules.", isFlaw: false }
          ],
          explanation: "Section 43B(h) defers the deduction to the financial year of actual payment; it does not permanently extinguish the business expense."
        },
        {
          type: "binary_verdict",
          prompt: "As the Income Tax Assessing Officer, evaluate this corporate deduction claim under Section 43B(h):",
          scenario: "Corporate Buyer X purchased ₹1 Crore raw materials from an Udyam Micro supplier on February 10, 2024 (45-day limit expired March 26). Payment was cleared on May 15, 2024 (before the corporate tax return filing deadline). The CFO claims the deduction for FY 2023-24 under the general Section 43B proviso.",
          verdictQuestion: "Can the corporate buyer claim this tax deduction in FY 2023-24?",
          labels: { trueLabel: "CLAIM ALLOWED", falseLabel: "CLAIM DISALLOWED" },
          correct: false,
          explanation: "CLAIM DISALLOWED! Unlike other clauses of Section 43B (like provident fund or tax dues), clause (h) explicitly excludes the relaxation of paying before the return filing date. Because payment was made after March 31 and beyond the Section 15 timeline, the deduction is disallowed for FY 2023-24 and can only be claimed in FY 2024-25."
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
          type: "cloze_chips",
          prompt: "Snap the structural parameters into the PM Vishwakarma scheme matrix:",
          template: "PM Vishwakarma covers {1} across India with a total central outlay of {2}. Artisans receive an e-voucher of {3} for modern toolkits, and collateral-free enterprise credit at an effective interest rate of {4} (with 8% government interest subvention).",
          blanks: [
            { id: 1, correct: "18 traditional trades" },
            { id: 2, correct: "₹13,000 Crore" },
            { id: 3, correct: "₹15,000" },
            { id: 4, correct: "5% interest" }
          ],
          chips: ["18 traditional trades", "₹13,000 Crore", "₹15,000", "5% interest", "24 trades", "₹5,000 Crore", "₹25,000", "8% interest"],
          explanation: "PM Vishwakarma: 18 trades, ₹13,000 Cr outlay, ₹15,000 toolkit e-voucher, Tranche 1 (₹1L) & Tranche 2 (₹2L) at 5% interest with 8% subvention."
        },
        {
          type: "match_pairs",
          prompt: "Match each Vishwakarma Architecture Pillar with its Concrete Deliverable:",
          pairs: [
            { left: "Pillar 1: Formal Recognition", right: "PM Vishwakarma Certificate & Digital ID Card" },
            { left: "Pillar 2: Skill Upgradation", right: "5-7 days basic training (₹500/day stipend) + 15 days advanced" },
            { left: "Pillar 3: Toolkit Grant", right: "₹15,000 electronic e-RUPI voucher for precision equipment" },
            { left: "Pillar 4: Credit Support", right: "Collateral-free loans (₹1L + ₹2L) at concessional 5% interest" }
          ]
        },
        {
          type: "flaw_hunter",
          prompt: "Spot the FLAWED provision regarding artisan and informal enterprise credit:",
          statements: [
            { text: "Artisans must pledge physical ancestral property or agricultural land as collateral to access the first ₹1 Lakh tranche under PM Vishwakarma.", isFlaw: true, flawReason: "POLICY FLAW IDENTIFIED! PM Vishwakarma loans are 100% COLLATERAL-FREE enterprise credit, backed entirely by a central credit guarantee fund." },
            { text: "The Udyam Assist Platform (UAP) enables informal micro enterprises without GSTIN to secure priority sector lending certificates.", isFlaw: false },
            { text: "PM Vishwakarma provides end-to-end integration with e-commerce platforms like GeM and ONDC for artisan products.", isFlaw: false },
            { text: "The central government provides an 8% interest subvention to partner commercial banks to enable the 5% concessional loan rate.", isFlaw: false }
          ],
          explanation: "PM Vishwakarma loans are fully collateral-free to ensure underprivileged artisans without land titles can access institutional finance."
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
          type: "category_sorter",
          prompt: "Classify each underwriting practice into Legacy Mortgage Underwriting vs Budget 2025 Digital Underwriting:",
          categories: ["Legacy Mortgage Underwriting", "Budget 2025 Digital Underwriting"],
          items: [
            { text: "Mandatory demand for physical land deeds and residential property mortgages", category: "Legacy Mortgage Underwriting" },
            { text: "Credit assessment via automated algorithms analyzing GST filings, e-way bills & bank cash flows", category: "Budget 2025 Digital Underwriting" },
            { text: "Dynamic invoice factoring and discounting executed over TReDS digital exchanges", category: "Budget 2025 Digital Underwriting" },
            { text: "Rigid reliance on historical audited balance sheets excluding asset-light tech startups", category: "Legacy Mortgage Underwriting" }
          ],
          explanation: "Budget 2025-26 pivoted Indian public sector banks from collateral/asset-based lending to digital cash-flow and transaction footprint underwriting."
        },
        {
          type: "cloze_chips",
          prompt: "Snap the verified Budget 2025-26 figures into the financial reforms policy brief:",
          template: "Budget 2025 launched a self-financing guarantee fund providing cover up to {1} for machinery term loans, doubled the CGTMSE normal credit cover to {2}, enhanced the Mudra Tarun Plus loan ceiling to {3}, and lowered mandatory TReDS buyer onboarding to {4}.",
          blanks: [
            { id: 1, correct: "₹100 Crore" },
            { id: 2, correct: "₹10 Crore" },
            { id: 3, correct: "₹20 Lakh" },
            { id: 4, correct: "₹500 Crore turnover" }
          ],
          chips: ["₹100 Crore", "₹10 Crore", "₹20 Lakh", "₹500 Crore turnover", "₹50 Crore", "₹5 Crore", "₹15 Lakh", "₹250 Crore turnover"],
          explanation: "Budget 2025-26: ₹100 Cr machinery fund, ₹10 Cr CGTMSE cover, ₹20 Lakh Mudra Tarun Plus, and ₹500 Cr TReDS threshold."
        },
        {
          type: "match_pairs",
          prompt: "Match each Budget 2025-26 MSME Initiative with its Strategic Policy Feature:",
          pairs: [
            { left: "₹100 Cr Machinery Fund", right: "Self-financing guarantee for term loans without land mortgage" },
            { left: "CGTMSE Normal Cover", right: "Credit guarantee cover doubled from ₹5 Crore to ₹10 Crore" },
            { left: "Mudra Tarun Plus", right: "Loan ceiling enhanced from ₹10 Lakh to ₹20 Lakh" },
            { left: "Customised Credit Card", right: "₹5 Lakh credit limit for Udyam-registered micro units" }
          ]
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
          type: "cloze_chips",
          prompt: "Snap the statutory procurement percentages and criteria into the legal text:",
          template: "Under the Public Procurement Policy, Central Ministries and CPSEs must procure {1} of their annual requirement from MSEs, with earmarked sub-targets of {2} for SC/ST-owned units and {3} for Women-owned units. Participating MSEs within the {4} band can match L1 prices.",
          blanks: [
            { id: 1, correct: "25% minimum" },
            { id: 2, correct: "4% quota" },
            { id: 3, correct: "3% quota" },
            { id: 4, correct: "L1 + 15%" }
          ],
          chips: ["25% minimum", "4% quota", "3% quota", "L1 + 15%", "20% minimum", "5% quota", "2% quota", "L1 + 25%"],
          explanation: "Procurement mandates 25% overall, 4% SC/ST, 3% Women, and price preference within the L1 + 15% band."
        },
        {
          type: "flaw_hunter",
          prompt: "Identify the INCORRECT or FLAWED statement regarding MSE public procurement rights:",
          statements: [
            { text: "Udyam-registered Micro and Small enterprises are legally exempt from paying tender document fees.", isFlaw: false },
            { text: "MSEs must deposit an Earnest Money Deposit (EMD) of at least 10% of contract value to participate in CPSE public tenders.", isFlaw: true, flawReason: "PROCUREMENT FLAW DETECTED! Udyam-registered MSEs are 100% EXEMPT from paying Earnest Money Deposit (EMD) / Bid Security in government and CPSE tenders, eliminating working capital blockages." },
            { text: "Over 358 items are exclusively reserved for procurement solely from the micro and small sector.", isFlaw: false },
            { text: "The Government e-Marketplace (GeM) provides direct digital access without intermediaries.", isFlaw: false }
          ],
          explanation: "MSEs enjoy 100% statutory exemption from tender document fees and Earnest Money Deposits (EMD)."
        },
        {
          type: "match_pairs",
          prompt: "Match each Procurement Policy Provision with its Concrete Statutory Protection:",
          pairs: [
            { left: "25% Annual Procurement Quota", right: "Guaranteed domestic market exceeding ₹50,000 Crore annually" },
            { left: "EMD & Tender Fee Waiver", right: "Eliminates prohibitive capital lock-in for small bidders" },
            { left: "L1 + 15% Price Preference", right: "Right to match lowest conglomerate bidder for 25% of tender quantity" },
            { left: "GeM Digital Portal", right: "Direct, transparent public procurement without intermediary cartels" }
          ]
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
          type: "category_sorter",
          prompt: "Classify each industrial intervention into Physical Infrastructure Cluster vs Cross-Border Digital Architecture:",
          categories: ["Physical Infrastructure Cluster", "Cross-Border & Digital Trade"],
          items: [
            { text: "Tiruppur Zero Liquid Discharge (ZLD) Common Effluent Treatment Plants", category: "Physical Infrastructure Cluster" },
            { text: "SFURTI Common Facility Centers (CFCs) with shared artisan machinery and quality testing", category: "Physical Infrastructure Cluster" },
            { text: "E-Commerce Export Hubs (ECEH) with bonded warehousing & customs pre-clearance", category: "Cross-Border & Digital Trade" },
            { text: "ONDC Open Network unbundling logistics, payment gateways, and buyer discovery", category: "Cross-Border & Digital Trade" }
          ],
          explanation: "Physical clusters aggregate shared heavy equipment; digital architectures eliminate platform commission monopolies and cross-border customs bottlenecks."
        },
        {
          type: "match_pairs",
          prompt: "Connect each Cluster & Export Initiative with its Strategic Function:",
          pairs: [
            { left: "Tiruppur Cluster Model", right: "Generates $4B+ knitwear exports through shared common processing infrastructure" },
            { left: "SFURTI Scheme", right: "Up to ₹5 Cr financial grant for Common Facility Centers in traditional craft clusters" },
            { left: "ECEH Architecture", right: "Public-private bonded export staging hubs for expedited customs clearance" },
            { left: "RAMP Program", right: "World Bank assisted initiative for state-level MSME capacity and green transition" }
          ]
        },
        {
          type: "binary_verdict",
          prompt: "Review the administrative officer's decision regarding this SFURTI cluster grant application:",
          scenario: "A rural bamboo and brass artisan cooperative in Moradabad seeks to establish a ₹4.5 Crore Common Facility Center with CNC laser cutting machinery and shared testing labs under the SFURTI scheme. The local administrative officer rejects the proposal claiming: 'SFURTI assistance is strictly capped at ₹50 Lakh per cluster and cannot fund heavy machinery.'",
          verdictQuestion: "Is the administrative officer's rejection and ₹50 Lakh ceiling statutorily accurate?",
          labels: { trueLabel: "REJECTION UPHELD", falseLabel: "REJECTION ERRONEOUS" },
          correct: false,
          explanation: "REJECTION ERRONEOUS! Under SFURTI (Fund for Regeneration of Traditional Industries), financial assistance of up to ₹5 Crore is provided for Major Clusters (and up to ₹2.5 Crore for Regular Clusters) specifically to set up Common Facility Centers with modern high-value machinery."
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
          type: "case_judge",
          prompt: "BOSS CHALLENGE 1: Deliver judgment in this landmark export classification appeal:",
          caseDossier: {
            title: "Dispute: Precision Engineering Ltd vs State Directorate of Industries",
            facts: [
              "Enterprise invested ₹9 Crore in advanced precision CNC machinery.",
              "Achieved Domestic Turnover of ₹45 Crore and Export Turnover of ₹35 Crore (Gross Turnover = ₹80 Crore).",
              "Directorate of Industries issued an order reclassifying the unit as 'Medium', stripping it of priority procurement status.",
              "Enterprise appeals to the High Court under Article 226 citing S.O. 2119(E)."
            ]
          },
          question: "As the High Court Bench, deliver the binding statutory verdict:",
          options: [
            { text: "Dismiss Appeal: Gross turnover of ₹80 Crore exceeds the ₹50 Crore Small ceiling; export exemptions are purely discretionary.", isVerdict: false },
            { text: "Allow Appeal with Costs: Export turnover is statutorily excluded by notification; qualifying turnover is strictly ₹45 Crore and investment is ₹9 Crore, keeping the unit legally Small.", isVerdict: true },
            { text: "Remand to Directorate: Direct the enterprise to deposit 50% of foreign export earnings in an escrow account.", isVerdict: false }
          ],
          explanation: "CRITICAL HIT ON BOSS! Under MSMED Notification S.O. 2119(E), turnover in exports of goods or services is strictly excluded from classification. Qualifying turnover is ₹45 Cr (≤ ₹50 Cr limit) and investment is ₹9 Cr (≤ ₹10 Cr limit), preserving its Small Enterprise status."
        },
        {
          type: "case_judge",
          prompt: "BOSS CHALLENGE 2: Identify the landmark institutional committee behind India's credit transformation:",
          caseDossier: {
            title: "Expert Committee Review on MSME Financial Architecture",
            facts: [
              "Constituted by the Reserve Bank of India in 2019 to address the systemic ₹30 Lakh Crore credit gap.",
              "Recommended the creation of a ₹10,000 Crore Fund of Funds (SRI Fund) for equity infusion.",
              "Pioneered mandatory TReDS onboarding for corporate buyers and transitioning from collateral to digital cash-flow lending."
            ]
          },
          question: "Name the landmark expert committee responsible for this reform blueprint:",
          options: [
            { text: "U.K. Sinha Committee on MSMEs (RBI, 2019)", isVerdict: true },
            { text: "Bimal Jalan Committee on Economic Capital Framework", isVerdict: false },
            { text: "Nachiket Mor Committee on Comprehensive Financial Services", isVerdict: false },
            { text: "Urjit Patel Committee on Monetary Policy Framework", isVerdict: false }
          ],
          explanation: "SUPER EFFECTIVE HIT! The U.K. Sinha Committee on MSMEs (RBI, 2019) formulated the landmark roadmap for the Self-Reliant India (SRI) Fund, TReDS expansion, and cash-flow underwriting."
        },
        {
          type: "flaw_hunter",
          prompt: "BOSS CHALLENGE 3: Spot the FATALLY FLAWED economic proposition regarding MSMEs and Viksit Bharat 2047:",
          statements: [
            { text: "MSMEs generate 31.1% of India's GDP and 48.6% of merchandise exports, serving as the crucible for inclusive economic growth.", isFlaw: false },
            { text: "Under Section 16 of the MSMED Act, delayed payments attract mandatory compound interest at 3x the RBI Bank Rate.", isFlaw: false },
            { text: "To eliminate the 'Missing Middle', India must indefinitely maintain size-based subsidies so that micro enterprises face zero incentive to ever scale up into mid-sized or large corporations.", isFlaw: true, flawReason: "FATAL FLAW IDENTIFIED! Indefinitely maintaining size-based subsidies is the EXACT cause of 'Dwarfism' and the 'Missing Middle'. Economic Survey 2018-19 recommends transitioning to AGE-BASED incentives with strict sunset clauses, allowing dynamic firms to scale into German-style Mittelstand champions without falling off a regulatory cliff." },
            { text: "Budget 2025-26 introduced a ₹100 Crore guarantee fund for machinery and equipment term loans without physical land mortgages.", isFlaw: false }
          ],
          explanation: "BOSS OVERLORD WEAKENED! Indefinite size subsidies trap capital in unproductive dwarf units. Scaled growth requires sunset clauses and age-based incentives."
        },
        {
          type: "match_pairs",
          prompt: "BOSS FINISHER: Link the Constitutional & Policy Pillars to India's MSME Transformation:",
          pairs: [
            { left: "Article 39(b) & (c)", right: "Preventing corporate monopoly and distributing industrial resources" },
            { left: "German Mittelstand", right: "Transforming dwarf firms into globally competitive niche champions" },
            { left: "TReDS & Factoring", right: "Liquidity architecture turning receivables into instant working capital" },
            { left: "Viksit Bharat 2047", right: "MSMEs driving 50% of GDP and inclusive regional industrialization" }
          ]
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
