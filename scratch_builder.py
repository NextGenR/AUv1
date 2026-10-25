# -*- coding: utf-8 -*-
"""
Builder script for CAVA Learn from Scratch Mobile Application.
Adopts the exact design, UX architecture, interaction model, and visual tokens of
Citizen's Charter_ Learn from Scratch.html for all CAVA topics:
- MSME Reforms
- Public Examinations & Exam Integrity
- AI in Judiciary
- Citizen's Charter & Service Delivery
"""

import json
import os

TOPICS = {
    "msme": {
        "id": "msme",
        "title": "MSME Reforms & Economic Catalysts",
        "badge": "🏭",
        "sub": "Master India's 31.1% GDP growth engine, 2020 classification, delayed payments, and Budget 2025 reforms.",
        "hue": ["#0f8a62", "#2f63d6", "#7442d6", "#b8760a", "#d23a40", "#0b8a9a", "#d9570c"],
        "ico": [["🏭", "📊", "🎯"], ["📐", "⚙️", "🌍"], ["📉", "🏢", "🇩🇪"], ["⏳", "📜", "⚖️"], ["💳", "📱", "🏦"], ["🚀", "🔨", "📦"], ["🎯", "🗺️", "🏆"]],
        "lessons": [
            {
                "n": "Macro Pillars & Economic Footprint",
                "e": "🏭",
                "d": "GDP, GVA, exports and 11.1 Cr livelihoods",
                "c": [
                    {
                        "t": "The Giant in Plain Sight",
                        "b": [
                            "India's MSME sector is the second largest employer after agriculture, sustaining <b>over 11.1 Crore jobs</b> across <b>6.33 Crore enterprises</b>.",
                            "Macro footprint: <b>31.1% of India's GDP</b>, <b>35.4% of Manufacturing GVA</b>, and <b>48.6% of Total Merchandise Exports</b>.",
                            "Over <b>51.2% of MSMEs are in rural areas</b>, promoting equitable regional growth and reducing distress migration."
                        ],
                        "k": ["31.1% GDP Share", "48.6% Merchandise Exports", "11.1 Crore Jobs", "Rural Democratization"],
                        "n": "Low capital investment per job created makes MSMEs vital for India's demographic dividend."
                    },
                    {
                        "t": "Constitutional & Policy Canvas",
                        "b": [
                            "Rooted in <b>Directive Principles: Article 39(b) and 39(c)</b> to prevent concentration of wealth and ensure equitable resource distribution.",
                            "Key pillar for realizing a <b>$5 Trillion economy</b> and achieving the vision of <b>Viksit Bharat 2047</b>.",
                            "High representation of vulnerable social groups: significant ownership by SC, ST, and women entrepreneurs."
                        ],
                        "k": ["Article 39(b) & 39(c)", "Inclusive Growth", "Viksit Bharat 2047"],
                        "n": "Exam angle: GS-3 (Mobilization of Resources, Employment, Industrial Policy)."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What proportion of India's total merchandise exports is contributed by MSMEs?",
                        "o": ["About 15%", "About 25%", "About 48.6%", "Over 75%"],
                        "a": 2,
                        "e": "MSMEs account for ~48.6% of India's total merchandise exports across textiles, engineering, and leather."
                    },
                    {
                        "k": "tf",
                        "q": "More than 50% of MSME units in India are located in rural areas.",
                        "a": 0,
                        "e": "True. 51.2% of MSMEs are based in rural India, serving as a vital engine for decentralized growth."
                    },
                    {
                        "k": "multi",
                        "q": "Tap all verified macroeconomic benchmarks of India's MSME sector.",
                        "o": ["31.1% of India's GDP", "35.4% of Manufacturing GVA", "11.1 Crore jobs sustained", "90% of central corporate tax"],
                        "a": [0, 1, 2],
                        "e": "31.1% GDP, 35.4% Manufacturing GVA, and 11.1 Cr jobs are verified government benchmarks."
                    },
                    {
                        "k": "match",
                        "q": "Match the macroeconomic metric to its official benchmark.",
                        "p": [
                            ["GDP Contribution", "31.1% of GDP"],
                            ["Manufacturing GVA", "35.4% share"],
                            ["Merchandise Exports", "48.6% of total"],
                            ["Employment Footprint", "11.1 Crore jobs"]
                        ],
                        "e": "Memorize these four data points for your GS-3 introduction paragraphs!"
                    }
                ]
            },
            {
                "n": "2020 Composite Classification",
                "e": "📐",
                "d": "Investment, turnover and export carve-out",
                "c": [
                    {
                        "t": "The 2020 Paradigm Shift",
                        "b": [
                            "Under the <b>Atmanirbhar Bharat package (July 2020)</b>, the government scrapped the old 2006 bifurcation between manufacturing and service units.",
                            "Introduced a <b>composite criteria</b> combining both <b>Plant & Machinery Investment</b> and <b>Annual Turnover</b>.",
                            "Both conditions must be satisfied. Crossing either limit moves the enterprise into the higher bracket."
                        ],
                        "k": ["Composite Criteria", "Unified Classification", "Atmanirbhar Bharat"],
                        "n": "Replaced the archaic 2006 manufacturing vs services equipment division."
                    },
                    {
                        "t": "The 1/5, 10/50, 50/250 Rule",
                        "b": [
                            "<b>Micro:</b> Investment up to <b>₹1 Crore</b> AND Turnover up to <b>₹5 Crore</b> (1:5 ratio).",
                            "<b>Small:</b> Investment up to <b>₹10 Crore</b> AND Turnover up to <b>₹50 Crore</b> (10:50 ratio).",
                            "<b>Medium:</b> Investment up to <b>₹50 Crore</b> AND Turnover up to <b>₹250 Crore</b> (50:250 ratio).",
                            "Notice the constant <b>5x turnover multiplier</b> across all three tiers!"
                        ],
                        "k": ["Micro (1 Cr / 5 Cr)", "Small (10 Cr / 50 Cr)", "Medium (50 Cr / 250 Cr)", "5x Multiplier"],
                        "n": "Easy mnemonic: 1 -> 10 -> 50 for Investment, multiply by 5 for Turnover!"
                    },
                    {
                        "t": "Export Turnover Exclusion",
                        "b": [
                            "A landmark reform: <b>Export turnover is completely EXCLUDED</b> from calculating the turnover ceiling!",
                            "Why? To prevent growing firms from fearing that exporting more will cost them their MSME priority sector status.",
                            "An enterprise can export ₹500 Cr and still remain a 'Small' enterprise as long as domestic turnover is under ₹50 Cr."
                        ],
                        "k": ["Export Carve-out", "Global Scale", "Incentive Compatibility"],
                        "n": "Removes the export penalty and directly supports Atmanirbhar Bharat export competitiveness."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What are the ceiling limits for a 'Small' enterprise under the 2020 classification?",
                        "o": ["Inv ₹1 Cr / TO ₹5 Cr", "Inv ₹10 Cr / TO ₹50 Cr", "Inv ₹50 Cr / TO ₹250 Cr", "Inv ₹25 Cr / TO ₹100 Cr"],
                        "a": 1,
                        "e": "Small enterprise: Investment up to ₹10 Crore AND Turnover up to ₹50 Crore."
                    },
                    {
                        "k": "tf",
                        "q": "Export turnover is included when determining whether an enterprise crosses the MSME turnover threshold.",
                        "a": 1,
                        "e": "False. Export turnover is explicitly excluded to encourage MSMEs to export aggressively without losing benefits."
                    },
                    {
                        "k": "order",
                        "q": "Arrange the 2020 MSME tiers in ascending order of investment ceilings.",
                        "o": ["Micro (₹1 Crore)", "Small (₹10 Crore)", "Medium (₹50 Crore)"],
                        "e": "Micro (₹1 Cr) → Small (₹10 Cr) → Medium (₹50 Cr)."
                    },
                    {
                        "k": "match",
                        "q": "Match the MSME tier to its maximum investment limit.",
                        "p": [
                            ["Micro Enterprise", "Up to ₹1 Crore"],
                            ["Small Enterprise", "Up to ₹10 Crore"],
                            ["Medium Enterprise", "Up to ₹50 Crore"],
                            ["Turnover Multiplier", "5x Investment"]
                        ],
                        "e": "Clean 1:5, 10:50, 50:250 mathematical formula."
                    }
                ]
            },
            {
                "n": "The Dwarfism Paradox",
                "e": "📉",
                "d": "Why Indian firms stay micro vs German Mittelstand",
                "c": [
                    {
                        "t": "The Missing Middle & Dwarfism",
                        "b": [
                            "Economic Survey highlights a severe structural deformity: <b>over 99.4% of enterprises in India remain Micro</b>!",
                            "Only <b>0.52% are Small</b>, and an infinitesimal <b>0.08% are Medium</b>.",
                            "Instead of an upright pyramid or healthy cylinder, India has an <b>inverted mushroom</b>: vast dwarfs and giant conglomerates, with a missing middle."
                        ],
                        "k": ["Dwarfism Paradox", "Missing Middle", "99.4% Micro Share"],
                        "n": "Economic Survey distinguishes between 'infants' (young firms that grow) and 'dwarfs' (old firms that deliberately stay small)."
                    },
                    {
                        "t": "The Regulatory Cliff",
                        "b": [
                            "Why don't Indian firms grow? Because crossing the micro threshold triggers a <b>regulatory cliff</b>.",
                            "Firms fear losing priority sector lending, tax breaks, and flexible labor compliance exemptions.",
                            "Capital and labor become locked in low-productivity dwarf units, preventing <b>Schumpeterian 'Creative Destruction'</b>."
                        ],
                        "k": ["Regulatory Cliff", "Perverse Incentives", "Creative Destruction"],
                        "n": "Subsidies tied to remaining small perversely incentivize staying small."
                    },
                    {
                        "t": "The German 'Mittelstand' Benchmark",
                        "b": [
                            "Germany's economic miracle rests on its <b>Mittelstand</b>: highly innovative, agile medium-sized manufacturing champions.",
                            "Features: <b>Scale-neutral incentives</b> (subsidies don't vanish upon growth), <b>dual vocational training</b>, and long-term bank capital.",
                            "India must transition from protecting dwarfs to empowering Mittelstand-style global scale."
                        ],
                        "k": ["German Mittelstand", "Scale-Neutrality", "Hidden Champions"],
                        "n": "A classic international case study to quote in your GS-3 conclusion."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What percentage of enterprises in India's MSME sector are micro units?",
                        "o": ["Around 50%", "Around 75%", "Over 99.4%", "Exactly 33%"],
                        "a": 2,
                        "e": "Over 99.4% of all MSMEs in India are micro enterprises, showcasing extreme dwarfism."
                    },
                    {
                        "k": "tf",
                        "q": "Economic Survey describes 'dwarfs' as young startup firms that need temporary policy protection to grow.",
                        "a": 1,
                        "e": "False. Young firms are 'infants'. 'Dwarfs' are older firms that intentionally stay small to exploit policy exemptions."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the core root causes of MSME dwarfism in India.",
                        "o": ["Regulatory cliff upon scaling up", "Loss of priority sector lending and fiscal exemptions", "Excessive supply of equity capital", "Distortionary size-based incentives"],
                        "a": [0, 1, 3],
                        "e": "Size-based incentives, regulatory cliffs, and fear of losing exemptions trap firms in dwarfism."
                    },
                    {
                        "k": "match",
                        "q": "Match the economic concept to its definition.",
                        "p": [
                            ["Dwarfism", "Older firms deliberately remaining small"],
                            ["Missing Middle", "Scarcity of medium-sized enterprises"],
                            ["Mittelstand", "German scale-neutral medium firm model"],
                            ["Creative Destruction", "Dynamic firms replacing obsolete ones"]
                        ],
                        "e": "Crucial terminology for GS-3 industrial policy answers."
                    }
                ]
            },
            {
                "n": "Delayed Payments & Section 43B(h)",
                "e": "⏳",
                "d": "MSMED Act Sections 15-19 & statutory teeth",
                "c": [
                    {
                        "t": "Working Capital Asphyxiation",
                        "b": [
                            "Delayed payments from large corporate buyers and CPSEs are the #1 cause of MSME mortality.",
                            "Small suppliers have weak bargaining power and are forced to accept payment delays of 120-180 days.",
                            "This triggers severe liquidity crunches, inability to service bank debt, and insolvency."
                        ],
                        "k": ["Delayed Payments", "Working Capital Crisis", "Bargaining Asymmetry"],
                        "n": "MSMEs are often profitable on paper but bankrupt in cash flow."
                    },
                    {
                        "t": "MSMED Act Statutory Mandate (Sections 15-19)",
                        "b": [
                            "<b>Section 15:</b> Buyer must pay within agreed period (maximum <b>45 days</b>; or 15 days if no agreement in writing).",
                            "<b>Section 16:</b> Defaulting buyer must pay <b>compound interest with monthly rests at 3 TIMES the RBI Bank Rate</b>!",
                            "<b>Section 18 & 19:</b> Micro & Small Enterprise Facilitation Councils (MSEFC). If buyer appeals, they must pre-deposit <b>75% of the award amount</b>!"
                        ],
                        "k": ["45-day Maximum Window", "3x RBI Bank Rate Compound Interest", "MSEFC", "75% Pre-deposit"],
                        "n": "The 75% pre-deposit under Section 19 prevents big buyers from tying small vendors in endless litigation."
                    },
                    {
                        "t": "Section 43B(h) Income Tax Act Tooth",
                        "b": [
                            "Introduced in <b>Finance Act 2023</b> to enforce real payment discipline on buyers.",
                            "Rule: A buyer can only claim tax deduction for purchases from MSMEs in the year the payment is <b>actually made</b>!",
                            "If payment is delayed beyond the 45-day window, the deduction is disallowed that financial year, sharply raising the buyer's income tax bill."
                        ],
                        "k": ["Section 43B(h)", "Tax Disallowance", "Payment Discipline"],
                        "n": "Provides a direct financial penalty that forces corporate CFOs to pay MSMEs on time."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What is the maximum payment credit period permitted under Section 15 of MSMED Act when agreed in writing?",
                        "o": ["15 days", "30 days", "45 days", "90 days"],
                        "a": 2,
                        "e": "Section 15 stipulates that the agreed credit period cannot exceed 45 days under any circumstances."
                    },
                    {
                        "k": "mc",
                        "q": "What penal interest rate applies to delayed payments under Section 16 of the MSMED Act?",
                        "o": ["Bank Rate + 2%", "Simple interest at 10%", "3 times the RBI Bank Rate (compound interest)", "No interest penalty"],
                        "a": 2,
                        "e": "Defaulting buyers must pay compound interest with monthly rests at 3 times the RBI Bank Rate."
                    },
                    {
                        "k": "tf",
                        "q": "Under Section 43B(h), buyers can still claim tax deductions for delayed payments if they provide an affidavit.",
                        "a": 1,
                        "e": "False. Deductions are strictly disallowed for that financial year unless payment was made within the statutory 45-day limit."
                    },
                    {
                        "k": "order",
                        "q": "Put the delayed payments enforcement process in sequence.",
                        "o": ["Supply of goods/services completed", "45-day maximum statutory window expires", "Filing application on MSME Samadhaan portal", "MSEFC arbitral award with 3x bank rate interest", "Buyer mandatory 75% pre-deposit for appeal"],
                        "e": "Supply → 45 days expire → Samadhaan filing → MSEFC award → 75% pre-deposit."
                    }
                ]
            },
            {
                "n": "Credit Gap & Financing Innovations",
                "e": "💳",
                "d": "UK Sinha Committee, TReDS & cash-flow lending",
                "c": [
                    {
                        "t": "The ₹30 Lakh Crore Credit Chasm",
                        "b": [
                            "The <b>UK Sinha Committee (RBI, 2019)</b> estimated an unmet credit gap of over <b>₹30 Lakh Crore</b> in the MSME sector.",
                            "Over 85% of MSMEs lack access to formal bank loans due to an absence of immovable physical collateral (real estate/land).",
                            "Traditional banking relies on asset-based mortgages rather than business cash-flows."
                        ],
                        "k": ["UK Sinha Committee", "₹30 Lakh Crore Deficit", "Collateral Trap"],
                        "n": "Without formal credit, MSMEs are forced into predatory informal borrowing at 30-40% interest."
                    },
                    {
                        "t": "Shift to Digital Cash-Flow Underwriting",
                        "b": [
                            "Public sector banks are pivoting from physical collateral to <b>digital footprint underwriting</b>.",
                            "Assessing creditworthiness through <b>GST invoices</b>, bank statements via <b>Account Aggregators</b>, and UPI merchant turnover.",
                            "Enables algorithm-driven collateral-free credit sanctioning in minutes rather than weeks."
                        ],
                        "k": ["Cash-flow Lending", "Account Aggregator", "Digital Footprint"],
                        "n": "Turns transaction data into an economic asset for the borrower."
                    },
                    {
                        "t": "TReDS: Invoice Factoring Platform",
                        "b": [
                            "<b>Trade Receivables Discounting System (TReDS)</b>: an RBI-regulated institutional mechanism for electronic factoring.",
                            "MSMEs upload accepted invoices; multiple banks and NBFCs bid to discount them without recourse.",
                            "Budget 2024-25 lowered the mandatory buyer onboarding turnover threshold to <b>₹500 Crore</b> to force CPSEs and corporates onto the platform."
                        ],
                        "k": ["TReDS", "Factoring without Recourse", "₹500 Cr Mandate"],
                        "n": "Converts locked accounts receivable into instant liquid working capital."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which RBI-appointed committee authored the comprehensive blueprint on MSME credit and structural reforms?",
                        "o": ["Nachiket Mor Committee", "UK Sinha Committee", "Bimal Jalan Committee", "Urjit Patel Committee"],
                        "a": 1,
                        "e": "The UK Sinha Committee (2019) recommended the overhaul of MSME credit, TReDS expansion, and cash-flow underwriting."
                    },
                    {
                        "k": "tf",
                        "q": "TReDS is an RBI-regulated electronic platform that enables MSMEs to discount their trade invoices through competitive financier bidding.",
                        "a": 0,
                        "e": "True. TReDS allows MSMEs to auction unpaid corporate invoices to financiers for upfront cash without recourse."
                    },
                    {
                        "k": "multi",
                        "q": "Tap all instruments facilitating digital cash-flow based MSME credit.",
                        "o": ["Account Aggregator framework", "GST invoice data analytics", "TReDS factoring platform", "Physical land registry mortgage"],
                        "a": [0, 1, 2],
                        "e": "Account Aggregator, GST returns, and TReDS enable cash-flow lending, replacing physical mortgages."
                    },
                    {
                        "k": "match",
                        "q": "Match the financing tool to its key mechanism.",
                        "p": [
                            ["UK Sinha Committee", "₹30 Lakh Crore credit gap analysis"],
                            ["TReDS Platform", "Invoice discounting without recourse"],
                            ["Account Aggregator", "Consent-based digital financial data sharing"],
                            ["Cash-Flow Lending", "Credit based on GST transactions, not land"]
                        ],
                        "e": "Core pillars of the digital credit revolution for MSMEs."
                    }
                ]
            },
            {
                "n": "Budget 2025-26 & Flagship Schemes",
                "e": "🚀",
                "d": "Credit guarantee, PM Vishwakarma & E-Commerce Hubs",
                "c": [
                    {
                        "t": "New Credit Guarantee Scheme (Budget 2025)",
                        "b": [
                            "A self-financing guarantee fund providing <b>collateral-free credit cover up to ₹100 Crore</b> per MSME for machinery & equipment purchase.",
                            "Focuses specifically on manufacturing scale-up and technological upgradation.",
                            "Borrowers pay an annual guarantee fee based on the diminishing loan balance."
                        ],
                        "k": ["₹100 Cr Guarantee Fund", "Machinery Purchase", "Self-financing"],
                        "n": "Solves the capex financing roadblock for ambitious small enterprises."
                    },
                    {
                        "t": "PM Vishwakarma Scheme (₹13,000 Crore)",
                        "b": [
                            "Central Sector Scheme offering end-to-end holistic lifecycle support for <b>18 traditional artisan trades</b> (carpenters, blacksmiths, potters, etc.).",
                            "Five pillars: <b>PM Vishwakarma Certificate & ID</b>, <b>Skill training with ₹500/day stipend</b>, <b>₹15,000 modern toolkit incentive</b>.",
                            "Collateral-free enterprise credit up to <b>₹3 Lakh</b> (₹1L tranche 1 + ₹2L tranche 2) at a concessional interest rate of <b>5%</b>!"
                        ],
                        "k": ["PM Vishwakarma", "18 Traditional Trades", "₹15,000 Toolkit", "5% Subsidized Loans"],
                        "n": "Protects traditional artisanal heritage while linking them to modern value chains."
                    },
                    {
                        "t": "E-Commerce Export Hubs (ECEH) & Mudra Expansion",
                        "b": [
                            "<b>E-Commerce Export Hubs (ECEH):</b> Public-private partnership zones providing single-window regulatory, customs, and testing clearances for cross-border e-commerce.",
                            "<b>Mudra 'Tarun Plus':</b> Loan ceiling doubled from ₹10 Lakh to <b>₹20 Lakh</b> for entrepreneurs who have successfully repaid prior Tarun loans.",
                            "<b>TReDS expansion:</b> Lowering buyer mandate to ₹500 Cr adds 22 CPSEs and 7,000+ private companies."
                        ],
                        "k": ["E-Commerce Export Hubs", "Mudra Tarun Plus (₹20 Lakh)", "Cross-border Trade"],
                        "n": "Empowers grassroots MSMEs to sell directly to consumers across the globe via digital marketplaces."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What is the maximum credit cover provided under the Budget 2025 Credit Guarantee Scheme for machinery purchase?",
                        "o": ["₹10 Crore", "₹25 Crore", "₹50 Crore", "₹100 Crore"],
                        "a": 3,
                        "e": "Budget 2024-25 introduced a guarantee fund facilitating collateral-free term loans up to ₹100 Crore."
                    },
                    {
                        "k": "mc",
                        "q": "How many traditional artisan trades are supported under the PM Vishwakarma Scheme?",
                        "o": ["10 trades", "12 trades", "18 trades", "25 trades"],
                        "a": 2,
                        "e": "The scheme covers 18 traditional family-based trades including carpenters, blacksmiths, goldsmiths, and sculptors."
                    },
                    {
                        "k": "tf",
                        "q": "The Mudra 'Tarun Plus' ceiling was doubled to ₹20 Lakh in the Union Budget.",
                        "a": 0,
                        "e": "True. The limit was raised to ₹20 Lakh for entrepreneurs who have successfully repaid earlier Tarun loans."
                    },
                    {
                        "k": "multi",
                        "q": "Tap all key pillars of the PM Vishwakarma Scheme.",
                        "o": ["PM Vishwakarma Certificate & ID card", "₹15,000 grant for modern toolkits", "Collateral-free credit up to ₹3 Lakh at 5% interest", "Mandatory nationalization of private workshops"],
                        "a": [0, 1, 2],
                        "e": "Certification, toolkit grant of ₹15,000, and subsidized loans at 5% form the scheme's core."
                    }
                ]
            },
            {
                "n": "Mains Answer Mastery Toolkit",
                "e": "🎯",
                "d": "Keywords, 5-point skeleton & conclusion",
                "c": [
                    {
                        "t": "High-Yield Keywords to Drop",
                        "b": [
                            "<b>Macro & Structure:</b> 31.1% GDP, 48.6% merchandise exports, 11.1 crore livelihoods, rural democratization.",
                            "<b>Diagnostic Terminology:</b> Dwarfism paradox, regulatory cliff, missing middle, Schumpeterian creative destruction, working capital asphyxiation.",
                            "<b>Policy & Reform Solutions:</b> German Mittelstand model, scale-neutral incentives, Section 43B(h) statutory discipline, TReDS invoice factoring, E-Commerce Export Hubs (ECEH)."
                        ],
                        "k": ["Use 4 to 5 per Mains answer!"],
                        "n": "Examiners scan for specific diagnostic vocabulary rather than generic essays."
                    },
                    {
                        "t": "Mains 5-Stage Answer Skeleton",
                        "b": [
                            "<b>1. Introduction:</b> Macro triad (31.1% GDP, 35.4% GVA, 48.6% exports) + Article 39(b)/(c) constitutional link.",
                            "<b>2. Structural Significance:</b> Low capital cost per job, rural balance, export dynamo.",
                            "<b>3. Core Bottlenecks:</b> Dwarfism (99.4% micro), ₹30L Cr credit gap (UK Sinha), delayed payments.",
                            "<b>4. Recent Policy Push:</b> 2020 composite criteria, Budget 2025 ₹100 Cr guarantee, Sec 43B(h), PM Vishwakarma.",
                            "<b>5. Way Forward & Conclusion:</b> Transition from dwarfs to German Mittelstand; engine for $5T economy and Viksit Bharat 2047."
                        ],
                        "k": ["Intro → Significance → Bottlenecks → Policy → Mittelstand Conclusion"],
                        "n": "Structure your answers with subheadings, data, and visual flowcharts for top marks."
                    }
                ],
                "q": [
                    {
                        "k": "order",
                        "q": "Order the optimal Mains answer structure for an MSME question.",
                        "o": [
                            "Intro: 31.1% GDP, 48.6% exports, 11.1 Cr jobs",
                            "Structural Significance & Employment Democratization",
                            "Core Bottlenecks: Dwarfism, Credit Gap, Delayed Payments",
                            "Government Initiatives: Sec 43B(h), Budget 2025, Vishwakarma",
                            "Conclusion: German Mittelstand for Viksit Bharat 2047"
                        ],
                        "e": "Macro Data → Significance → Crisis/Bottlenecks → Policy Interventions → Global Benchmark Conclusion."
                    },
                    {
                        "k": "mc",
                        "q": "Which international manufacturing model is widely recommended for India to overcome the 'missing middle'?",
                        "o": ["South Korean Chaebols", "German Mittelstand", "American Wall Street", "Japanese Keiretsu monopolies"],
                        "a": 1,
                        "e": "The German Mittelstand model is praised for its scale-neutral policies, vocational training, and resilient medium enterprises."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the indispensable Mains keywords for MSME answers.",
                        "o": ["Dwarfism paradox", "Section 43B(h)", "German Mittelstand", "Agrarian collectivization"],
                        "a": [0, 1, 2],
                        "e": "Dwarfism, Section 43B(h), and Mittelstand are top-scoring keywords."
                    },
                    {
                        "k": "flip",
                        "q": "Draft a 2-line intro for 'MSMEs: From Regulatory Dwarfs to Viksit Bharat Engines'.",
                        "r": "Sustaining 31.1% of India's GDP, 48.6% of merchandise exports, and over 11.1 crore livelihoods, MSMEs constitute the bedrock of India's economic architecture. Transitioning them from protected dwarfs into globally competitive, Mittelstand-style champions is the paramount prerequisite for a $5 Trillion economy."
                    }
                ]
            }
        ],
        "pyq": [
            {
                "k": "flip",
                "q": "PYQ-style: Examine the structural reasons behind the 'missing middle' and dwarfism in India's MSME sector. Suggest policy measures drawing from international best practices. (150 words)",
                "r": "Intro: MSMEs drive 31.1% GDP and 11.1 Cr jobs, yet 99.4% remain micro units (inverted mushroom structure). Causes of Dwarfism: 1. Regulatory cliff (growth triggers loss of priority credit and tax exemptions). 2. Labor rigidities and compliance burden. 3. ₹30L Cr credit deficit (UK Sinha). Fixes: 1. Adopt German Mittelstand model with scale-neutral incentives. 2. Enforce Sec 43B(h) against delayed payments. 3. Expand TReDS factoring and E-Commerce Export Hubs. Conclude: Foster creative destruction to build global champions for Viksit Bharat 2047."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Delayed payments are the single biggest cause of working capital distress for MSMEs. How far do MSMED Act and Section 43B(h) address this issue? (150 words)",
                "r": "Context: Small suppliers face 90-180 day payment delays, asphyxiating liquidity. Statutory Architecture: 1. MSMED Act Sec 15 (max 45-day window) & Sec 16 (compound interest at 3x RBI Bank Rate). 2. Sec 19 requires 75% pre-deposit on appeals. 3. Section 43B(h) (Budget 2023): disallows tax deductions to buyers unless payments are actually cleared within 45 days. Gaps: Unequal bargaining power; suppliers fear de-listing if they drag corporate clients to MSEFC. Way Forward: Auto-reporting of overdue invoices on GST portal and mandatory TReDS onboarding for all ₹500 Cr+ buyers."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Discuss how digital cash-flow lending and Budget 2025-26 initiatives can bridge the MSME credit gap. (250 words)",
                "r": "Intro: UK Sinha Committee pegged MSME credit deficit at ₹30 Lakh Crore due to traditional asset-collateral requirements. Shift to Cash-flow Lending: 1. Account Aggregators & GST data enable transaction-based risk profiling. 2. TReDS platform allows competitive invoice discounting without recourse. Budget 2025 Interventions: 1. ₹100 Crore collateral-free Credit Guarantee Scheme for machinery & equipment purchase. 2. Mudra Tarun Plus ceiling doubled to ₹20 Lakh. 3. PM Vishwakarma (₹13,000 Cr) providing ₹15k toolkits and collateral-free credit at 5% to 18 artisan trades. Conclude: Democratizing credit access shifts capital from speculative real estate to productive manufacturing."
            }
        ],
        "sks": [
            {
                "t": "MSME Macro Significance",
                "s": [
                    "MSMEs are the economic bedrock: 31.1% GDP, 35.4% Manufacturing GVA, 48.6% exports, 11.1 Cr jobs.",
                    "Articles 39(b) & 39(c) DPSP; 2020 composite criteria (1/5, 10/50, 50/250) with export exclusion.",
                    "Pros: high employment elasticity, 51.2% rural balance. Cons: 99.4% micro dwarfs, ₹30L Cr credit gap.",
                    "UK Sinha Committee, Budget 2025 ₹100 Cr guarantee, Section 43B(h), PM Vishwakarma.",
                    "Pyramid: Inverted mushroom (99.4% micro) → Transition to German Mittelstand cylinder."
                ]
            },
            {
                "t": "Delayed Payments & Section 43B(h)",
                "s": [
                    "Delayed payments lock working capital and cause insolvency despite on-paper profitability.",
                    "MSMED Act Sec 15 (45-day cap), Sec 16 (3x RBI Bank Rate compound interest), Sec 19 (75% pre-deposit).",
                    "Pros: stringent penal framework. Cons: weak bargaining power, buyers threaten cancellation.",
                    "Section 43B(h) tax disallowance, MSME Samadhaan portal, TReDS invoice discounting.",
                    "Flowchart: Supply goods → 45-day deadline → Sec 43B(h) tax penalty / MSEFC arbitral award."
                ]
            },
            {
                "t": "Overcoming MSME Dwarfism",
                "s": [
                    "Dwarfism: over 99.4% of Indian firms remain micro, suppressing productivity and R&D investment.",
                    "Economic Survey 'Infants vs Dwarfs' distinction; Schumpeter's Creative Destruction.",
                    "Pros of scale: global export competitiveness, higher wages. Cons of dwarfism: locked capital, low tech.",
                    "German Mittelstand model: scale-neutral incentives, dual technical vocational training, ECEH hubs.",
                    "Ladder: Micro (₹1 Cr/₹5 Cr) → Small (₹10 Cr/₹50 Cr) → Medium (₹50 Cr/₹250 Cr) → Mittelstand."
                ]
            }
        ]
    },

    "exams": {
        "id": "exams",
        "title": "Public Exams Act & Exam Integrity",
        "badge": "🏛️",
        "sub": "Master the 2024/2026 Act, K. Radhakrishnan Committee reforms, NTA restructuring, and exam security.",
        "hue": ["#2f63d6", "#7442d6", "#0f8a62", "#d23a40", "#b8760a", "#0b8a9a"],
        "ico": [["🏛️", "⚖️", "📜"], ["🔒", "👮", "⛓️"], ["🔍", "📋", "🏫"], ["⚙️", "🏢", "💻"], ["📜", "⚖️", "🎯"], ["🏆", "🗺️", "🧭"]],
        "lessons": [
            {
                "n": "Engine of Mobility & The Crisis",
                "e": "🏛️",
                "d": "Social mobility, paper leak syndicates & judicial alarm",
                "c": [
                    {
                        "t": "The Ladder of Hope",
                        "b": [
                            "In India, competitive public examinations are the <b>primary vehicle for upward social mobility</b>.",
                            "They allow underprivileged, rural, and first-generation learners to transcend generational poverty on sheer merit.",
                            "When an examination is compromised, meritocracy is murdered, destroying public faith in the republic."
                        ],
                        "k": ["Social Mobility", "Meritocracy", "Public Trust"],
                        "n": "Chhattisgarh High Court dictum: 'A paper leak is more heinous than murder; murder takes one life, but a paper leak kills the dreams of millions.'"
                    },
                    {
                        "t": "The Organized Crime Syndicate",
                        "b": [
                            "Paper leaks have evolved from localized cheating into <b>trans-state organized criminal syndicates</b>.",
                            "Operating with corporate sophistication: charging <b>₹30 Lakh to ₹50 Lakh per leaked paper</b>.",
                            "Modus operandi: breaching printing presses, hacking commercial private computer labs, and deploying expert 'solvers'."
                        ],
                        "k": ["Organized Syndicates", "Commercialized Cheating", "Institutional Breach"],
                        "n": "Economic incentives: multi-crore illicit profits with historically low prosecution and bail loopholes."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which High Court observed that 'a paper leak is more heinous than murder'?",
                        "o": ["Allahabad High Court", "Chhattisgarh High Court", "Delhi High Court", "Bombay High Court"],
                        "a": 1,
                        "e": "The Chhattisgarh High Court highlighted the profound moral and generational damage wrought by examination leaks."
                    },
                    {
                        "k": "tf",
                        "q": "Modern paper leaks in India are primarily minor, isolated classroom offenses rather than organized interstate operations.",
                        "a": 1,
                        "e": "False. Investigations (e.g. EOU Bihar, CBI) reveal multi-state organized crime syndicates charging ₹30-50L per candidate."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the societal impacts of compromised public recruitment exams.",
                        "o": ["Erosion of faith in meritocratic governance", "Disproportionate harm to underprivileged rural aspirants", "Economic loss of candidate years and savings", "Automatic acceleration of government appointments"],
                        "a": [0, 1, 2],
                        "e": "Compromised exams destroy meritocracy, waste precious years of youth, and hit marginalized families hardest."
                    }
                ]
            },
            {
                "n": "Public Examinations Act 2024",
                "e": "⚖️",
                "d": "Statutory architecture, penalties & candidate immunity",
                "c": [
                    {
                        "t": "The Statutory Shield",
                        "b": [
                            "Enacted as the <b>Public Examinations (Prevention of Unfair Means) Act, 2024</b>.",
                            "Applies across central testing bodies: <b>UPSC, SSC, NTA, RRB, and IBPS</b>.",
                            "Defines 15 specific corrupt practices: question leaking, unauthorized paper possession, tampering with computer networks, and fake websites."
                        ],
                        "k": ["Public Examinations Act 2024", "Central Agencies Covered", "15 Corrupt Practices"],
                        "n": "A dedicated central law to create overwhelming criminal deterrence."
                    },
                    {
                        "t": "Two-Tiered Penal Architecture",
                        "b": [
                            "<b>Individual Cheater/Service Provider:</b> Imprisonment of <b>3 to 5 years</b> and fine up to <b>₹10 Lakh</b>.",
                            "<b>Organized Crime Syndicate:</b> Rigorous imprisonment of <b>5 to 10 years</b> and minimum fine of <b>₹1 Crore</b>!",
                            "Defaulting institutions face <b>attachment of property</b> and recovery of total examination costs."
                        ],
                        "k": ["3-5 Years (Individual)", "5-10 Years & ₹1 Cr Fine (Syndicate)", "Asset Attachment"],
                        "n": "All offenses are Cognizable, Non-Bailable, and Non-Compoundable."
                    },
                    {
                        "t": "Bona Fide Candidate Immunity",
                        "b": [
                            "A critical safeguard: <b>honest candidates are NOT criminalized</b> under this Act!",
                            "Students caught cheating remain subject to administrative examination bylaws (debarment), but are shielded from draconian anti-gang criminal charges.",
                            "Focus is squarely on prosecuting the criminal supply-side: syndicates, corrupt officials, and coaching mafia."
                        ],
                        "k": ["Candidate Immunity", "Supply-side Prosecution", "Targeting Kingpins"],
                        "n": "Prevents harassment of vulnerable young students by law enforcement."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What is the minimum fine prescribed for organized paper leak syndicates under the 2024 Act?",
                        "o": ["₹10 Lakh", "₹25 Lakh", "₹50 Lakh", "₹1 Crore"],
                        "a": 3,
                        "e": "Section 10(2) mandates a minimum fine of ₹1 Crore alongside 5 to 10 years imprisonment for organized syndicates."
                    },
                    {
                        "k": "tf",
                        "q": "Bona fide student aspirants caught copying are sentenced to mandatory 5-year prison terms under the 2024 Act.",
                        "a": 1,
                        "e": "False. Candidates are explicitly protected from the criminal provisions of the Act, which target organized syndicates."
                    },
                    {
                        "k": "match",
                        "q": "Match the entity to its statutory penal consequence.",
                        "p": [
                            ["Individual Cheating", "3 to 5 years prison + ₹10L fine"],
                            ["Organized Syndicate", "5 to 10 years prison + min ₹1 Cr fine"],
                            ["Compromised Agency", "Asset attachment & cost recovery"],
                            ["Bona Fide Candidate", "Immune from criminal prosecution under Act"]
                        ],
                        "e": "Clear graduated liability framework."
                    }
                ]
            },
            {
                "n": "Radhakrishnan Committee Reforms",
                "e": "🔍",
                "d": "7-member high-level panel on NTA overhaul",
                "c": [
                    {
                        "t": "The Mandate for Overhaul",
                        "b": [
                            "Constituted under former ISRO chief <b>Dr. K. Radhakrishnan (7-member high-level committee)</b>.",
                            "Formed in response to widespread public outcry over NEET-UG and UGC-NET paper leaks and integrity failures.",
                            "Tasked with recommending structural reforms in NTA, digital security, and examination standard operating procedures."
                        ],
                        "k": ["K. Radhakrishnan Committee", "7-Member Panel", "NTA Overhaul"],
                        "n": "Applies ISRO-grade mission security principles to competitive examination administration."
                    },
                    {
                        "t": "Core Structural Recommendations",
                        "b": [
                            "<b>1. Multi-Stage Testing:</b> Introduce two tiers (Screening Prelims + Mains) for mega-exams to filter candidates safely.",
                            "<b>2. Hybrid Testing Format:</b> Question papers transmitted digitally in encrypted form at the last minute; answers marked on physical OMR or verified terminals.",
                            "<b>3. 100% Government Test Centers:</b> End reliance on dubious private engineering college labs. Conduct exams exclusively in <b>Kendriya Vidyalayas, Navodaya Vidyalayas, IITs, and NITs</b>."
                        ],
                        "k": ["Multi-Stage Exams", "Hybrid Digital Mode", "Government Test Centers"],
                        "n": "Eliminates vulnerable supply chains where physical paper packages travel by road days in advance."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Who chaired the 7-member high-level committee appointed to reform the National Testing Agency (NTA)?",
                        "o": ["K. Kasturirangan", "Dr. K. Radhakrishnan", "Prof. Yash Pal", "Dr. Anil Kakodkar"],
                        "a": 1,
                        "e": "Former ISRO Chairman Dr. K. Radhakrishnan headed the 7-member committee on exam reforms."
                    },
                    {
                        "k": "multi",
                        "q": "Tap key recommendations proposed by the K. Radhakrishnan Committee.",
                        "o": ["Multi-stage screening for mega examinations", "Hybrid encrypted digital question transmission", "Restricting test centers exclusively to verified government institutions", "Complete abolition of all competitive entrance exams"],
                        "a": [0, 1, 2],
                        "e": "Multi-stage testing, hybrid transmission, and using only public institutions (KVs, IITs, NITs) were recommended."
                    },
                    {
                        "k": "tf",
                        "q": "The Radhakrishnan Committee recommended expanding outsourcing of exam center management to unverified private IT institutes.",
                        "a": 1,
                        "e": "False. It strongly recommended eliminating private testing centers in favor of trusted government institutions."
                    }
                ]
            },
            {
                "n": "NTA Deficits & Economics of Crime",
                "e": "⚙️",
                "d": "The 24-staff paradox & Gary Becker's model",
                "c": [
                    {
                        "t": "The NTA 24-Staff Paradox",
                        "b": [
                            "The National Testing Agency (NTA) conducts exams for <b>over 1.3 Crore students annually</b>.",
                            "Yet it operates with a permanent core cadre of <b>barely 24 regular officers</b>!",
                            "Result: massive, dangerous reliance on contractual staffing, outsourced private vendors, and third-party IT labs."
                        ],
                        "k": ["24-Staff Paradox", "Vendor Capture", "Contractual Outsourcing"],
                        "n": "An agency conducting the world's largest high-stakes exams cannot run on a skeleton contractual staff."
                    },
                    {
                        "t": "Gary Becker's Economics of Crime",
                        "b": [
                            "Nobel Laureate Gary Becker proved: <i>Criminal deterrence = Severity of Punishment x Probability of Detection</i>.",
                            "Merely prescribing 10-year prison terms fails if the <b>probability of detection is near zero</b>.",
                            "Real deterrence requires unhackable cyber-audits, biometrics, live CCTV feeds with AI gaze tracking, and sting operations."
                        ],
                        "k": ["Gary Becker's Crime Model", "Probability of Detection", "CCTV & Biometric Integrity"],
                        "n": "A high-scoring theoretical framework to cite in your GS-2 & GS-4 governance answers."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What core administrative anomaly cripples the National Testing Agency's internal capacity?",
                        "o": ["Lack of internet connectivity", "Operating with barely 24 permanent staff members", "Having too many testing centers", "Over-regulation by state governments"],
                        "a": 1,
                        "e": "NTA's reliance on only ~24 permanent officers forces excessive outsourcing to vulnerable third-party contractors."
                    },
                    {
                        "k": "tf",
                        "q": "According to Gary Becker's Economics of Crime, doubling the prison sentence guarantees crime prevention even if detection probability is low.",
                        "a": 1,
                        "e": "False. Severity without high detection probability provides zero deterrent effect."
                    },
                    {
                        "k": "match",
                        "q": "Match the institutional bottleneck to its strategic solution.",
                        "p": [
                            ["24-Staff Paradox", "Create dedicated permanent NTA cadre"],
                            ["Private Lab Compromise", "Shift to KVs, IITs and NITs"],
                            ["Physical Paper Transit Breach", "Hybrid encrypted digital transmission"],
                            ["Low Detection Probability", "Continuous AI-proctoring and forensic audits"]
                        ],
                        "e": "Pair problem with structural administrative remedy."
                    }
                ]
            },
            {
                "n": "Constitutional & Ethical Canvas",
                "e": "📜",
                "d": "Articles 14, 16, 21A & Concurrent List Entry 25",
                "c": [
                    {
                        "t": "Constitutional Violations",
                        "b": [
                            "<b>Article 14 & 16:</b> Equality of opportunity in public employment is violated when wealthy candidates buy leaked question papers.",
                            "<b>Article 21A:</b> Right to education is rendered hollow if admission into medical and higher education institutions is auctioned to the highest bidder.",
                            "<b>Concurrent List Entry 25:</b> Both Parliament and State Legislatures share constitutional responsibility over education."
                        ],
                        "k": ["Article 14 & 16", "Article 21A", "Concurrent List Entry 25"],
                        "n": "Links paper leaks directly to violations of fundamental constitutional guarantees."
                    },
                    {
                        "t": "GS-4 Ethical & Moral Dimension",
                        "b": [
                            "Paper leaks breed profound <b>cynicism and moral disillusionment</b> in the nation's youth.",
                            "Aspirants internalize that integrity and hard work are futile, and corruption is the only viable path to success.",
                            "Restoring exam integrity is therefore a foundational moral duty for preserving democratic citizenship."
                        ],
                        "k": ["Crisis of Conscience", "Moral Cynicism", "Probity in Governance"],
                        "n": "A potent theme for GS-4 Ethics questions on public service values and trust."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which Constitutional Entry establishes education as a shared responsibility between Center and States?",
                        "o": ["Union List Entry 10", "Concurrent List Entry 25", "State List Entry 14", "Residuary Powers"],
                        "a": 1,
                        "e": "Entry 25 of the Concurrent List (introduced via 42nd Amendment, 1976) covers education."
                    },
                    {
                        "k": "tf",
                        "q": "Paper leaks violate Article 16 of the Indian Constitution.",
                        "a": 0,
                        "e": "True. Article 16 guarantees equality of opportunity in matters of public employment."
                    },
                    {
                        "k": "multi",
                        "q": "Tap all constitutional articles directly impacted by examination corruption.",
                        "o": ["Article 14 (Equality before law)", "Article 16 (Equal opportunity in public employment)", "Article 21 (Right to dignified life)", "Article 356 (President's Rule)"],
                        "a": [0, 1, 2],
                        "e": "Articles 14, 16, and 21 are directly undermined when merit is subverted."
                    }
                ]
            },
            {
                "n": "Mains Answer Mastery Toolkit",
                "e": "🎯",
                "d": "Keywords, 5-point skeleton & conclusion",
                "c": [
                    {
                        "t": "Keywords to Drop in Mains",
                        "b": [
                            "<b>Judicial Dictum:</b> 'More heinous than murder' (Chhattisgarh HC).",
                            "<b>Statutory Architecture:</b> Public Examinations Act 2024, ₹1 Crore minimum fine, asset attachment, candidate immunity.",
                            "<b>Committees & Models:</b> K. Radhakrishnan 7-member Committee, Gary Becker's Economics of Crime, 24-staff paradox, hybrid testing."
                        ],
                        "k": ["Use 4 to 5 per Mains answer!"],
                        "n": "Guarantees top marks in GS-2 Governance and GS-4 Ethics papers."
                    },
                    {
                        "t": "Mains Answer Blueprint",
                        "b": [
                            "<b>Intro:</b> Social mobility ladder + Chhattisgarh HC dictum.",
                            "<b>Constitutional Breach:</b> Articles 14, 16, 21A, Concurrent List Entry 25.",
                            "<b>Root Causes:</b> Trans-state syndicates (₹30-50L), NTA 24-staff paradox, low detection probability (Becker).",
                            "<b>Reform Measures:</b> Radhakrishnan Committee: multi-stage testing, hybrid mode, 100% government centers.",
                            "<b>Conclusion:</b> Restoring faith in the meritocratic social contract as a cornerstone of Viksit Bharat."
                        ],
                        "k": ["Intro → Constitution → Bottlenecks → Radhakrishnan Reforms → Meritocracy Conclusion"],
                        "n": "Clear, logical flow from crisis to constitutional values and concrete technical solutions."
                    }
                ],
                "q": [
                    {
                        "k": "order",
                        "q": "Order the optimal Mains answer structure for exam integrity.",
                        "o": [
                            "Intro: Social mobility ladder & Chhattisgarh HC dictum",
                            "Constitutional Violations: Articles 14, 16, 21A",
                            "Root Bottlenecks: 24-staff paradox & private vendor capture",
                            "Remedial Architecture: Radhakrishnan Committee & 2024 Act",
                            "Conclusion: Preserving meritocracy in the social contract"
                        ],
                        "e": "Social Context → Constitutional Breach → Bottlenecks → Reform Blueprint → Conclusion."
                    },
                    {
                        "k": "mc",
                        "q": "Best concluding thought for an answer on public examination reforms?",
                        "o": [
                            "Abolish all examinations and select candidates by lottery.",
                            "Restoring uncompromised exam integrity is not merely administrative; it is preserving the constitutional promise of meritocracy and hope for millions of youth.",
                            "Private vendors should be given total control of all examinations.",
                            "Punishment alone will solve all problems automatically."
                        ],
                        "a": 1,
                        "e": "A balanced, inspiring constitutional conclusion."
                    },
                    {
                        "k": "flip",
                        "q": "Write a 2-line intro for 'Integrity of Public Examinations in India'.",
                        "r": "Public competitive examinations are the primary engine of upward social mobility for India's youth. When paper leaks subvert this meritocratic ladder, they violate Articles 14 and 16, murdering the aspirations of millions as highlighted by the Chhattisgarh High Court."
                    }
                ]
            }
        ],
        "pyq": [
            {
                "k": "flip",
                "q": "PYQ-style: 'A paper leak is more heinous than murder.' In light of recent examination controversies, critically examine the provisions of the Public Examinations Act, 2024. (150 words)",
                "r": "Intro: Cite Chhattisgarh HC dictum. Exams are the vehicle for upward mobility; leaks murder meritocracy. Act Provisions: 1. Coverage: UPSC, SSC, NTA, RRB, IBPS. 2. Severe penal deterrence: 3-5 yrs for individuals; 5-10 yrs and minimum ₹1 Cr fine for organized syndicates with asset attachment. 3. Candidate immunity: bona fide students shielded from criminal charges. Critique & Gaps: 1. Gary Becker's Economics of Crime shows severity fails without high detection probability. 2. NTA's 24-staff paradox forces outsourcing to private labs. Conclude: Statutory teeth must be paired with Radhakrishnan Committee's hybrid testing and government-run exam centers to restore youth faith."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Discuss the structural recommendations of the K. Radhakrishnan Committee to revamp the National Testing Agency (NTA). (150 words)",
                "r": "Context: 7-member high-level panel under former ISRO chief Dr. K. Radhakrishnan setup post-NEET crisis. Key Reforms: 1. Multi-Stage Testing: Screening Prelims + Mains for mega-exams to reduce single-window risks. 2. Hybrid Delivery: Question paper transmitted digitally in encrypted packets minutes before; answer on physical OMR/proctored terminals. 3. 100% Government Centers: Test exclusively in KVs, Navodayas, IITs, NITs, ending shady private lab contracts. 4. Institutional Overhaul: Expand NTA's 24-member permanent cadre into an autonomous professional testing service. Conclude: Transforming NTA from a contractual coordinating body into an ISRO-grade secure testing institution."
            }
        ],
        "sks": [
            {
                "t": "Public Exams Act 2024",
                "s": [
                    "Public examinations are the primary ladder for upward mobility; leaks subvert Articles 14 and 16.",
                    "Public Examinations Act 2024; covers UPSC, SSC, NTA, RRB; 15 corrupt practices defined.",
                    "Pros: 5-10 yrs prison & ₹1 Cr min fine for syndicates, candidate immunity. Cons: Becker's crime model.",
                    "K. Radhakrishnan 7-member Committee, Central Bureau of Investigation (CBI), EOU Bihar.",
                    "Penal Ladder: Individual (3-5y) → Syndicate (5-10y + ₹1 Cr) → Agency (Asset attachment)."
                ]
            },
            {
                "t": "Radhakrishnan Committee Reforms",
                "s": [
                    "High-level 7-member panel under former ISRO chief Dr. K. Radhakrishnan to overhaul NTA.",
                    "Multi-stage testing (Screening + Mains) + Hybrid digital encrypted paper transmission.",
                    "Pros: eliminates physical paper transit breaches, curbs center hacking. Cons: digital infrastructure gap.",
                    "100% Government Test Centers (KVs, IITs, NITs); end the 24-staff paradox with permanent cadre.",
                    "Funnel: Stage 1 Screening → Stage 2 Hybrid Proctored Test at Government Centers."
                ]
            }
        ]
    },

    "judiciary": {
        "id": "judiciary",
        "title": "AI in Judiciary & Legal Tech",
        "badge": "⚖️",
        "sub": "Master the 5 Crore case backlog, draft AI guidelines 2026, NCLT hallucination crisis, and ethical boundaries.",
        "hue": ["#7442d6", "#2f63d6", "#0f8a62", "#d9570c", "#b8760a", "#0b8a9a"],
        "ico": [["⚖️", "📊", "🏛️"], ["⚠️", "🤖", "📜"], ["💻", "🌐", "⚡"], ["🛡️", "👁️", "⚖️"], ["📉", "👨‍⚖️", "⏳"], ["🎯", "🗺️", "🏆"]],
        "lessons": [
            {
                "n": "The 5 Crore Backlog & Assistive AI",
                "e": "⚖️",
                "d": "National Judicial Data Grid & the assistive boundary",
                "c": [
                    {
                        "t": "The Backlog Mountain",
                        "b": [
                            "India's judicial system is burdened with <b>over 5 Crore pending cases</b> according to the <i>National Judicial Data Grid (NJDG)</i>.",
                            "Over 4.4 Crore cases are trapped in subordinate district courts alone.",
                            "Consequence: 'Justice delayed is justice denied' — undertrials languishing for years, and commercial contract enforcement crippled."
                        ],
                        "k": ["5 Crore Backlog", "NJDG Data", "4.4 Cr District Court Cases"],
                        "n": "Economic Survey highlights that judicial delay reduces GDP growth by 1.5% to 2% annually."
                    },
                    {
                        "t": "The Assistive Boundary: Clerk, Not Judge",
                        "b": [
                            "AI offers unprecedented power to automate <b>cause-list management, case categorization, and legal document translation</b>.",
                            "<b>Fundamental Principle:</b> AI must only serve as an <b>assistive tool / judicial assistant</b>, NEVER as the adjudicator!",
                            "Adjudication demands human empathy, constitutional morality, and contextual equity — qualities no LLM possesses."
                        ],
                        "k": ["Assistive AI", "Human in the Loop", "Constitutional Morality"],
                        "n": "Machines can process logic, but only human judges can administer justice with conscience."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What is the approximate total judicial case pendency in India according to the National Judicial Data Grid?",
                        "o": ["1 Crore cases", "2.5 Crore cases", "Over 5 Crore cases", "Over 10 Crore cases"],
                        "a": 2,
                        "e": "NJDG records over 5 Crore pending cases across Supreme Court, High Courts, and Subordinate Courts."
                    },
                    {
                        "k": "tf",
                        "q": "The Supreme Court has endorsed replacing human judges with autonomous AI sentencing algorithms in criminal courts.",
                        "a": 1,
                        "e": "False. The Supreme Court strictly maintains that AI can only be an assistive tool; human adjudication is non-negotiable."
                    },
                    {
                        "k": "multi",
                        "q": "Tap legitimate assistive applications of AI in court administration.",
                        "o": ["Automated vernacular translation of judgments", "Intelligent case clustering and categorization", "Cause-list scheduling and backlog analytics", "Autonomous delivery of death penalty verdicts"],
                        "a": [0, 1, 2],
                        "e": "Translation, categorization, and scheduling are ideal assistive tasks. Adjudication remains human."
                    }
                ]
            },
            {
                "n": "Draft Guidelines 2026 & Hallucinations",
                "e": "⚠️",
                "d": "SC draft regulations & the NCLT 'Methyl Isocyanate' warning",
                "c": [
                    {
                        "t": "The NCLT Hallucination Shock",
                        "b": [
                            "In a prominent case before the National Company Law Tribunal (NCLT), lawyers submitted <b>fake legal precedents hallucinated by ChatGPT</b>!",
                            "Generative LLMs produce convincing citations of non-existent court judgments when queried for supporting case law.",
                            "The Supreme Court reacted sharply, warning that <i>'submitting AI-hallucinated case law in court is like the release of toxic Methyl Isocyanate gas!'</i>"
                        ],
                        "k": ["AI Hallucination", "NCLT Precedent Shock", "Methyl Isocyanate Warning"],
                        "n": "Submitting fabricated precedents damages the foundational integrity of the common-law doctrine of precedent (stare decisis)."
                    },
                    {
                        "t": "Supreme Court Draft Regulations 2026",
                        "b": [
                            "Issued to govern the ethical deployment of Artificial Intelligence across all Indian courts.",
                            "<b>Key Mandates:</b> Mandatory disclosure whenever AI is used in drafting pleadings; total prohibition on AI in final adjudication.",
                            "Strict verification requirement: Advocates bear personal disciplinary responsibility for verifying every citation against official law reporters."
                        ],
                        "k": ["Draft AI Guidelines 2026", "Mandatory Disclosure", "Advocate Responsibility"],
                        "n": "Establishes institutional guardrails to prevent algorithmic poisoning of court records."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "To what toxic substance did the Supreme Court compare the submission of AI-hallucinated case precedents in court?",
                        "o": ["Carbon Monoxide", "Sulphur Dioxide", "Methyl Isocyanate (Bhopal gas)", "Chlorine Gas"],
                        "a": 2,
                        "e": "The Supreme Court warned that citing unverified AI hallucinations pollutes the judicial stream like toxic Methyl Isocyanate."
                    },
                    {
                        "k": "tf",
                        "q": "Under the SC Draft AI Guidelines, advocates must disclose if AI was utilized and personally verify all cited legal precedents.",
                        "a": 0,
                        "e": "True. Personal verification by advocates is mandatory to eliminate hallucinated case submissions."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the risks posed by unverified Generative AI usage in legal proceedings.",
                        "o": ["Fabrication of non-existent case precedents", "Hallucination of statutory sections", "Erosion of stare decisis (doctrine of precedent)", "100% guarantee of winning the lawsuit"],
                        "a": [0, 1, 2],
                        "e": "Hallucinations threaten legal certainty and the doctrine of binding precedent."
                    }
                ]
            },
            {
                "n": "Key Technological Initiatives",
                "e": "💻",
                "d": "SUPACE, SUVAS, FASTER & e-Courts Phase III",
                "c": [
                    {
                        "t": "The Assistive Digital Suite",
                        "b": [
                            "<b>SUPACE (Supreme Court Portal for Assistance in Court's Efficiency):</b> AI tool designed to read case files, extract facts, and assist judges with legal research.",
                            "<b>SUVAS (Supreme Court Vidhik Anuvaad Software):</b> AI-powered translation tool translating English Supreme Court judgments into regional Indian languages (Hindi, Tamil, Bengali, etc.).",
                            "<b>FASTER (Fast and Secured Transmission of Electronic Records):</b> Secure digital delivery of bail orders to prison authorities to prevent unlawful detention."
                        ],
                        "k": ["SUPACE (Research)", "SUVAS (Translation)", "FASTER (Bail Delivery)"],
                        "n": "SUVAS democratizes justice by making apex court rulings accessible in vernacular tongues."
                    },
                    {
                        "t": "e-Courts Phase III (₹7,210 Crore Outlay)",
                        "b": [
                            "Approved with an outlay of <b>₹7,210 Crore</b> under the e-Committee of the Supreme Court.",
                            "Focus: Transition from digitized paper courts to a <b>digital-native, cloud-first platform</b> with intelligent judicial analytics.",
                            "Features: Paperless digital courts, digital case management, virtual hearings, and open judicial data APIs."
                        ],
                        "k": ["e-Courts Phase III", "₹7,210 Cr Outlay", "Cloud-First Architecture"],
                        "n": "Lays the physical and digital rails necessary for ethical AI integration."
                    }
                ],
                "q": [
                    {
                        "k": "match",
                        "q": "Match the judicial tech initiative to its primary objective.",
                        "p": [
                            ["SUPACE", "AI legal research & document parsing"],
                            ["SUVAS", "Translating verdicts into regional languages"],
                            ["FASTER", "Instant secure digital transmission of bail orders"],
                            ["e-Courts Phase III", "₹7,210 Cr digital-native cloud infrastructure"]
                        ],
                        "e": "A classic match question for Prelims and high-yield data for Mains."
                    },
                    {
                        "k": "mc",
                        "q": "Which AI tool was specifically built by the Supreme Court to translate judgments into vernacular languages?",
                        "o": ["SUPACE", "SUVAS", "FASTER", "Bhashini"],
                        "a": 1,
                        "e": "SUVAS (Supreme Court Vidhik Anuvaad Software) handles regional language judicial translations."
                    },
                    {
                        "k": "tf",
                        "q": "FASTER was introduced to ensure that prisoners granted bail are not kept incarcerated due to physical paper transit delays.",
                        "a": 0,
                        "e": "True. FASTER transmits electronic signed bail orders directly to jail authorities instantly."
                    }
                ]
            },
            {
                "n": "Constitutional Challenges & Algorithmic Bias",
                "e": "🛡️",
                "d": "Article 21, the Black Box problem & Open Justice",
                "c": [
                    {
                        "t": "Article 21 & The Right to a Fair Trial",
                        "b": [
                            "<b>Article 21:</b> Guarantees a fair, transparent, and reasoned trial by an impartial human judge.",
                            "<b>The Black Box Problem:</b> Deep neural networks cannot explain <i>why</i> an algorithmic score was assigned (e.g. COMPAS recidivism algorithm in the US).",
                            "A defendant has a fundamental constitutional right to know the exact reasoning behind an adverse finding."
                        ],
                        "k": ["Article 21 Fair Trial", "Black Box Problem", "Reasoned Decision"],
                        "n": "Justice must not only be done, but must be seen to be reasoned and explainable."
                    },
                    {
                        "t": "Algorithmic Bias & The Digital Divide",
                        "b": [
                            "AI trained on historical arrest and conviction data risks <b>perpetuating caste, gender, and minority biases</b>.",
                            "<b>Digital Divide:</b> Wealthy corporate litigants can deploy elite commercial legal AI, while indigent undertrials lack basic legal aid.",
                            "Risk of creating a two-tiered justice system if high-tech tools are not democratized."
                        ],
                        "k": ["Historical Training Bias", "Digital Asymmetry", "Legal Aid Gap"],
                        "n": "Garbage-in, garbage-out: Biased historical legal data produces biased algorithmic predictions."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which constitutional provision guarantees the right to a fair trial and a reasoned judicial decision?",
                        "o": ["Article 12", "Article 21", "Article 25", "Article 324"],
                        "a": 1,
                        "e": "Article 21 encompasses the right to a fair, speedy, and reasoned trial."
                    },
                    {
                        "k": "tf",
                        "q": "Because AI algorithms use mathematics, they are inherently immune to historical caste, racial, or socio-economic prejudices.",
                        "a": 1,
                        "e": "False. AI models trained on historical data frequently encode, amplify, and automate historical human prejudices."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the primary constitutional objections against autonomous algorithmic sentencing.",
                        "o": ["Violation of Article 21 reasoned adjudication", "Opacity of black-box neural networks", "Perpetuation of historical demographic bias", "Algorithms running out of memory"],
                        "a": [0, 1, 2],
                        "e": "Article 21, black-box opacity, and training bias are substantive constitutional challenges."
                    }
                ]
            },
            {
                "n": "Structural Bottlenecks & The Judge Deficit",
                "e": "📉",
                "d": "Judge-population ratio & Case Clearance Rate",
                "c": [
                    {
                        "t": "The Severe Judge Deficit",
                        "b": [
                            "India has approximately <b>21 judges per million people</b>.",
                            "Compare this to the <b>Law Commission's target of 50 judges per million</b>, and 100+ in developed nations (e.g. US ~107).",
                            "AI can assist workflow, but cannot cure the structural vacancy crisis in subordinate and high courts."
                        ],
                        "k": ["21 Judges per Million", "Law Commission 50 Target", "Structural Vacancy"],
                        "n": "Technology cannot substitute for an adequate number of constitutionally appointed judges."
                    },
                    {
                        "t": "Case Clearance Rate (CCR)",
                        "b": [
                            "<b>Case Clearance Rate (CCR):</b> Ratio of cases disposed to cases instituted within a year.",
                            "Economic Survey demonstrates that when CCR drops below 100%, the backlog mountain grows automatically.",
                            "AI's true value lies in accelerating mundane document processing to push the CCR comfortably above 100%."
                        ],
                        "k": ["Case Clearance Rate (CCR)", "Disposal Ratio", "Administrative Velocity"],
                        "n": "A high-impact quantitative metric to include in your GS-2 answers."
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "What is India's current judge-to-population ratio compared to the Law Commission's benchmark?",
                        "o": ["10 per million (vs 20)", "21 per million (vs 50)", "50 per million (vs 100)", "75 per million (vs 150)"],
                        "a": 1,
                        "e": "India has ~21 judges per million citizens, far below the Law Commission's recommended target of 50."
                    },
                    {
                        "k": "tf",
                        "q": "If an economy's Case Clearance Rate (CCR) is below 100%, total judicial case pendency will inevitably rise.",
                        "a": 0,
                        "e": "True. CCR below 100% means more cases are being filed than are being resolved, swelling the backlog."
                    },
                    {
                        "k": "match",
                        "q": "Match the judicial governance metric to its meaning.",
                        "p": [
                            ["Judge-Population Ratio", "21 judges per million citizens in India"],
                            ["Law Commission Target", "50 judges per million benchmark"],
                            ["Case Clearance Rate", "Ratio of disposed cases to instituted cases"],
                            ["e-Courts Outlay", "₹7,210 Crore under Phase III"]
                        ],
                        "e": "Essential statistics for GS-2 Judiciary questions."
                    }
                ]
            },
            {
                "n": "Mains Answer Mastery Toolkit",
                "e": "🎯",
                "d": "Keywords, answer skeleton & ethical conclusion",
                "c": [
                    {
                        "t": "Keywords to Drop in Mains",
                        "b": [
                            "<b>Status & Scale:</b> 5 Crore backlog, NJDG data, 21 judges per million, Case Clearance Rate (CCR).",
                            "<b>Immediate Context:</b> SC Draft AI Regulations 2026, NCLT fake precedent crisis, Methyl Isocyanate warning.",
                            "<b>Tech Initiatives:</b> SUPACE, SUVAS, FASTER, e-Courts Phase III (₹7,210 Cr).",
                            "<b>Constitutional & Ethics:</b> Article 21, black-box opacity, algorithmic bias, human empathy in adjudication."
                        ],
                        "k": ["Use 4 to 5 per Mains answer!"],
                        "n": "Positions your answer in the top 5% of all candidates."
                    },
                    {
                        "t": "Mains 5-Stage Blueprint",
                        "b": [
                            "<b>Intro:</b> 5 Crore backlog (NJDG) + Assistive AI potential.",
                            "<b>The Line in the Sand:</b> Assistive tool (clerk/researcher) vs Adjudicator (conscience/empathy).",
                            "<b>Risks:</b> NCLT ChatGPT hallucination crisis + Article 21 black-box bias.",
                            "<b>Institutional Initiatives:</b> SUPACE, SUVAS, FASTER, e-Courts Phase III, SC Draft Guidelines 2026.",
                            "<b>Conclusion:</b> Technology as a force multiplier for human judges, not a replacement for judicial conscience."
                        ],
                        "k": ["Intro → The Boundary → Risks → Policy → Ethical Conscience Conclusion"],
                        "n": "A balanced, forward-looking constitutional synthesis."
                    }
                ],
                "q": [
                    {
                        "k": "order",
                        "q": "Order the optimal Mains answer structure for AI in the Judiciary.",
                        "o": [
                            "Intro: 5 Crore backlog & NJDG crisis",
                            "The Assistive Boundary: AI as clerk, not judge",
                            "Risks: Hallucination crisis & Article 21 black-box opacity",
                            "Policy Landscape: SUPACE, SUVAS, e-Courts Phase III",
                            "Conclusion: Preserving human empathy and judicial conscience"
                        ],
                        "e": "Scale → Boundary → Risks → Policy → Constitutional Conclusion."
                    },
                    {
                        "k": "mc",
                        "q": "Best concluding sentence for an answer on AI in the Judiciary?",
                        "o": [
                            "Human judges should be replaced with neural networks by 2030.",
                            "Artificial Intelligence can be a powerful clerk to accelerate judicial velocity, but justice demands the empathy, ethics, and constitutional conscience that only human judges possess.",
                            "No technology should ever be allowed in Indian courts.",
                            "Everything is working perfectly and no reforms are required."
                        ],
                        "a": 1,
                        "e": "Balanced, keyword-rich, and constitutionally anchored."
                    },
                    {
                        "k": "flip",
                        "q": "Write a 2-line intro for 'AI in the Indian Judiciary: Potential and Perils'.",
                        "r": "Confronting a monumental backlog of over 5 Crore pending cases on the NJDG, Artificial Intelligence offers transformative tools to accelerate case processing. However, as cautioned by the Supreme Court, AI must serve strictly as an assistive clerk, never usurping the moral conscience and constitutional empathy required in human adjudication."
                    }
                ]
            }
        ],
        "pyq": [
            {
                "k": "flip",
                "q": "PYQ-style: Artificial intelligence can assist judicial efficiency but cannot replace judicial conscience. Comment in light of recent Supreme Court directives. (150 words)",
                "r": "Intro: India's 5 Crore backlog (NJDG) requires technological force multipliers. Assistive Promise: 1. SUPACE parses document facts and research. 2. SUVAS translates judgments into regional languages. 3. Automated cause-lists elevate Case Clearance Rate (CCR). Perils & SC Alarm: 1. NCLT hallucination crisis where LLMs fabricated case precedents (SC warned it is like 'toxic Methyl Isocyanate gas'). 2. Article 21 demands reasoned adjudication, violated by black-box algorithms. Draft AI Guidelines 2026: Mandate disclosure of AI use and require advocates to verify citations. Conclude: AI as clerk, never as judge; efficiency must serve justice, not supersede empathy."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Examine the constitutional and ethical concerns associated with deploying AI algorithms in the Indian judicial system with special reference to Article 21. (150 words)",
                "r": "Context: e-Courts Phase III (₹7,210 Cr) integrates advanced analytics. Constitutional Concerns: 1. Article 21: Right to a fair and reasoned trial requires explainability; deep learning models suffer from the 'Black Box' problem. 2. Algorithmic Bias: Models trained on historical policing/conviction data encode and automate systemic socio-economic and demographic biases. 3. Equality of Arms: Wealthy litigants deploy proprietary legal AI, widening disparity against indigent undertrials. Ethical Dimension: Adjudication requires mercy, moral reasoning, and constitutional morality—traits exclusive to human consciousness. Way Forward: Implement strict algorithmic audits, open APIs, and maintain human-in-the-loop oversight."
            }
        ],
        "sks": [
            {
                "t": "AI in Judiciary: Assistive vs Adjudicative",
                "s": [
                    "India's judicial crisis: over 5 Crore pending cases (NJDG); severe judge deficit (21 per million).",
                    "SC Draft AI Guidelines 2026; boundary: AI as assistive research clerk, never as adjudicator.",
                    "Pros: speed, translation (SUVAS), cause-lists. Cons: hallucinated precedents, black-box bias.",
                    "SUPACE, SUVAS, FASTER, e-Courts Phase III (₹7,210 Cr outlay).",
                    "Diagram: Boundary Line — Assistive Tasks (AI) vs Moral Adjudication (Human Judge)."
                ]
            },
            {
                "t": "Constitutional Safeguards & Article 21",
                "s": [
                    "Article 21 guarantees fair, reasoned trial; threatened by opaque black-box algorithms.",
                    "NCLT hallucination crisis: lawyers citing fake ChatGPT cases (SC 'Methyl Isocyanate' warning).",
                    "Pros of regulation: algorithmic accountability, advocate liability. Cons of unregulated AI: polluted precedents.",
                    "SC e-Committee, Law Commission reports, open judicial data APIs.",
                    "Balance: Algorithmic Efficiency on the left, Constitutional Conscience on the right."
                ]
            }
        ]
    },

    "charter": {
        "id": "charter",
        "title": "Citizen’s Charter & Service Delivery",
        "badge": "📜",
        "sub": "Learn it from zero: read the idea, then prove it. Principles, Sevottam, Right to Services Acts, and 2nd ARC.",
        "hue": ["#0f8a62", "#2f63d6", "#7442d6", "#b8760a", "#d23a40", "#0b8a9a", "#d9570c"],
        "ico": [["📜", "🌍", "🎯"], ["🧱", "📋", "🛠️"], ["🏛️", "⭐", "📊"], ["🐯", "📃", "⚖️"], ["📐", "📢", "🔒"], ["🔧", "📱", "🏆"], ["🗝️", "🗺️", "🧭"]],
        "lessons": [
            {
                "n": "The Big Idea",
                "e": "🧭",
                "d": "What it is, where it began",
                "c": [
                    {
                        "t": "A public promise",
                        "b": [
                            "A Citizen’s Charter is a written promise by a government body: <b>what services it offers</b>, the <b>standards and timelines</b> it commits to, and <b>how to complain</b> if it fails.",
                            "Think of it as a menu with a delivery guarantee, published for citizens."
                        ],
                        "k": ["Service-delivery commitment", "Social contract"],
                        "n": "It is a statement of intent, not a law."
                    },
                    {
                        "t": "Where it started",
                        "b": [
                            "The idea began in the <b>UK in 1991</b> under PM John Major. Public services were to treat users like valued customers.",
                            "In India it gained momentum after the <b>1997 Conference of Chief Ministers</b>, which adopted an Action Plan for an effective and responsive administration.",
                            "The <b>DARPG</b> (Dept. of Administrative Reforms and Public Grievances) is the nodal agency."
                        ],
                        "k": ["New Public Management", "DARPG", "Citizen-centric governance"]
                    },
                    {
                        "t": "Why it matters",
                        "b": [
                            "It shifts government from <b>rule-bound</b> to <b>citizen-centric</b>, and turns vague duty into a measurable promise.",
                            "Exam angle: GS-2 (governance, transparency, accountability) and GS-4 (responsiveness, public service values)."
                        ],
                        "k": ["Accountability", "Responsiveness"]
                    }
                ],
                "q": [
                    {
                        "k": "tf",
                        "q": "A Citizen’s Charter is legally enforceable in a court of law.",
                        "a": 1,
                        "e": "False. It is a voluntary commitment. Enforceability needs a statute, such as a Right to Services Act."
                    },
                    {
                        "k": "mc",
                        "q": "In which country did the Citizen’s Charter idea originate (1991)?",
                        "o": ["United States", "United Kingdom", "France", "Japan"],
                        "a": 1,
                        "e": "UK, under PM John Major."
                    },
                    {
                        "k": "mc",
                        "q": "Which body is the nodal agency for Citizen’s Charters in India?",
                        "o": ["NITI Aayog", "Election Commission", "DARPG", "Finance Commission"],
                        "a": 2,
                        "e": "DARPG in the Ministry of Personnel coordinates charters and grievance redress."
                    },
                    {
                        "k": "mc",
                        "q": "Which phrase best captures the philosophy behind charters?",
                        "o": ["Citizen-centric governance", "Maximising revenue", "Centralised secrecy", "Colonial paternalism"],
                        "a": 0,
                        "e": "Governance designed around the user of the service."
                    }
                ]
            },
            {
                "n": "Anatomy of a Charter",
                "e": "🧩",
                "d": "Principles and contents",
                "c": [
                    {
                        "t": "Six guiding principles",
                        "b": [
                            "Indian notes list six pillars: <b>Quality, Choice, Standards, Value, Accountability, Transparency</b>.",
                            "Quality: better service. Choice: options where possible. Standards: clear, measurable norms. Value: for taxpayers’ money. Accountability: someone answerable. Transparency: open rules."
                        ],
                        "k": ["Quality", "Standards", "Accountability", "Transparency"]
                    },
                    {
                        "t": "What goes inside",
                        "b": [
                            "<b>Vision and mission</b> of the organisation.",
                            "<b>List of services</b> and who is eligible.",
                            "<b>Standards and time limits</b> for each service.",
                            "<b>Grievance redress</b> process and officer details.",
                            "<b>What citizens should do</b> (expectations from the public)."
                        ],
                        "k": ["Service standards", "Time limits", "Grievance redress"]
                    },
                    {
                        "t": "How to build a good one",
                        "b": [
                            "<b>Consult</b> citizens and staff, then <b>set realistic standards</b>.",
                            "<b>Publish</b> widely, in local languages and online.",
                            "<b>Monitor and review</b> regularly, then revise."
                        ],
                        "k": ["Consultation", "Periodic review"]
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which of these is NOT one of the six pillars?",
                        "o": ["Quality", "Standards", "Secrecy", "Transparency"],
                        "a": 2,
                        "e": "Secrecy is the opposite of the charter spirit."
                    },
                    {
                        "k": "multi",
                        "q": "Tap everything a good charter contains.",
                        "o": ["Service standards and time limits", "Grievance redress process", "Vision and mission", "Officers’ personal salary details"],
                        "a": [0, 1, 2],
                        "e": "Salaries are not part of a service promise."
                    },
                    {
                        "k": "order",
                        "q": "Put the charter-building steps in order.",
                        "o": ["Consult citizens and staff", "Set realistic standards", "Publish widely", "Monitor and review"],
                        "e": "Consult → Standards → Publish → Review."
                    },
                    {
                        "k": "match",
                        "q": "Match the pillar to its meaning.",
                        "p": [
                            ["Standards", "Clear, measurable norms"],
                            ["Choice", "Options where possible"],
                            ["Value", "For taxpayers’ money"],
                            ["Transparency", "Open rules and procedures"]
                        ],
                        "e": "Use these one-liners to explain pillars in Mains."
                    }
                ]
            },
            {
                "n": "Committees & Models",
                "e": "🏛️",
                "d": "2nd ARC, Sevottam, feedback tools",
                "c": [
                    {
                        "t": "2nd ARC: the big report",
                        "b": [
                            "The <b>2nd Administrative Reforms Commission</b> studied charters in its 12th Report, <b>“Citizen Centric Administration: The Heart of Governance”</b> (2009).",
                            "It stressed that charters must be made in consultation with citizens, carry realistic standards, and be reviewed periodically, or they become paper exercises."
                        ],
                        "k": ["2nd ARC", "Citizen Centric Administration"]
                    },
                    {
                        "t": "Sevottam model",
                        "b": [
                            "<b>Sevottam</b> = Seva (service) + Uttam (excellent). DARPG developed it around 2006 as a quality framework for service delivery.",
                            "Three modules: <b>1. Citizen’s Charter</b>, <b>2. Public Grievance Redress</b>, <b>3. Service Delivery Capability</b>.",
                            "Organisations are assessed against it, like a report card."
                        ],
                        "k": ["Sevottam", "Service Delivery Capability", "Self-assessment"]
                    },
                    {
                        "t": "Feedback tools",
                        "b": [
                            "<b>CPGRAMS</b>: the central online portal to lodge and track grievances.",
                            "<b>Citizen Report Cards</b>: surveys where users rate services. Pioneered by the Public Affairs Centre, Bangalore.",
                            "Both close the loop between promise and performance."
                        ],
                        "k": ["CPGRAMS", "Citizen Report Card"]
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which 2nd ARC report is the key source on citizen-centric governance?",
                        "o": ["1st: Right to Information", "12th: Citizen Centric Administration", "4th: Ethics in Governance only", "15th: Local Governance only"],
                        "a": 1,
                        "e": "12th Report: Citizen Centric Administration, The Heart of Governance."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the 3 modules of Sevottam.",
                        "o": ["Citizen’s Charter", "Public Grievance Redress", "Service Delivery Capability", "Revenue Maximisation"],
                        "a": [0, 1, 2],
                        "e": "Charter, grievance redress and delivery capability."
                    },
                    {
                        "k": "match",
                        "q": "Match tool to purpose.",
                        "p": [
                            ["Sevottam", "Service excellence framework"],
                            ["CPGRAMS", "Online grievance portal"],
                            ["Report Card", "Citizen feedback survey"],
                            ["2nd ARC 12th Report", "Citizen Centric Administration"]
                        ],
                        "e": "Four keywords you can name-drop confidently."
                    },
                    {
                        "k": "tf",
                        "q": "“Sevottam” combines the words Seva and Uttam.",
                        "a": 0,
                        "e": "True: service of the highest quality."
                    }
                ]
            },
            {
                "n": "Legal Backing",
                "e": "⚖️",
                "d": "From promise to guarantee",
                "c": [
                    {
                        "t": "The weakness of a promise",
                        "b": [
                            "A charter has <b>no penalty</b> and <b>no legal remedy</b>. An officer who ignores it usually faces nothing.",
                            "This is why critics call charters ‘paper tigers’."
                        ],
                        "k": ["Non-justiciable", "Paper tiger"]
                    },
                    {
                        "t": "The 2011 Bill",
                        "b": [
                            "The <b>Citizens Charter Bill, 2011</b> (Right of Citizens for Time Bound Delivery of Goods and Services and Redressal of their Grievances) was introduced in Lok Sabha.",
                            "It proposed mandatory charters, grievance officers and penalties. It <b>lapsed</b> when the Lok Sabha was dissolved in 2014."
                        ],
                        "k": ["Statutory backing", "Lapsed Bill"]
                    },
                    {
                        "t": "Right to Services Acts",
                        "b": [
                            "States moved first. <b>Madhya Pradesh Lok Sewa Guarantee Act, 2010</b> was the first. Bihar (2011), Rajasthan, Delhi, Karnataka (Sakala) and others followed.",
                            "Typical features: <b>notified services, fixed deadlines, penalty on the officer, appeal</b>."
                        ],
                        "k": ["Right to Services", "Lok Sewa Guarantee", "Sakala"]
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "Which state enacted the first Right to Services law (2010)?",
                        "o": ["Bihar", "Madhya Pradesh", "Kerala", "Gujarat"],
                        "a": 1,
                        "e": "Madhya Pradesh Lok Sewa Guarantee Act, 2010."
                    },
                    {
                        "k": "mc",
                        "q": "What does a Right to Services Act add over a plain charter?",
                        "o": ["More posters", "Legal deadlines and penalties", "A new logo", "Fewer services"],
                        "a": 1,
                        "e": "Statutory deadlines, penalties and appeals make it enforceable."
                    },
                    {
                        "k": "tf",
                        "q": "The Citizens Charter Bill, 2011 became an Act in 2012.",
                        "a": 1,
                        "e": "False. It lapsed in 2014."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the usual features of a Right to Services Act.",
                        "o": ["Fixed time limits", "Penalty on defaulting officers", "First and second appeal", "Ban on online services"],
                        "a": [0, 1, 2],
                        "e": "Time limits, penalties and appeals."
                    }
                ]
            },
            {
                "n": "Challenges",
                "e": "🚧",
                "d": "Why charters underperform",
                "c": [
                    {
                        "t": "Design problems",
                        "b": [
                            "Made <b>top-down</b> without consulting users.",
                            "Standards are <b>vague</b> (‘as early as possible’) or unrealistic.",
                            "Seldom <b>updated</b>, so they go out of date."
                        ],
                        "k": ["Top-down", "Vague standards", "Ritual compliance"]
                    },
                    {
                        "t": "Awareness and access",
                        "b": [
                            "Citizens often <b>don’t know</b> a charter exists.",
                            "Not in <b>local languages</b>; poor reach for illiterate or digitally excluded people.",
                            "Information is displayed but not explained."
                        ],
                        "k": ["Awareness gap", "Digital divide"]
                    },
                    {
                        "t": "Enforcement and culture",
                        "b": [
                            "<b>No penalty</b> for breach, and weak grievance follow-up.",
                            "Staff lack <b>training and ownership</b>; the charter is seen as extra paperwork.",
                            "Different departments, different formats: no <b>uniform monitoring</b>."
                        ],
                        "k": ["Weak enforcement", "Accountability deficit", "Bureaucratic culture"]
                    }
                ],
                "q": [
                    {
                        "k": "mc",
                        "q": "“Charters are drafted without consulting citizens.” Which challenge?",
                        "o": ["Design problem", "Awareness problem", "Funding problem"],
                        "a": 0,
                        "e": "Top-down design is a design problem."
                    },
                    {
                        "k": "multi",
                        "q": "Tap all genuine challenges.",
                        "o": ["No penalty for breach", "Poor awareness among citizens", "Too many citizens read charters", "Standards are vague or outdated"],
                        "a": [0, 1, 3],
                        "e": "Low readership, not high, is the problem."
                    },
                    {
                        "k": "match",
                        "q": "Match challenge to root cause.",
                        "p": [
                            ["Paper tiger", "No legal penalty"],
                            ["Awareness gap", "Not in local language"],
                            ["Ritual compliance", "Seen as paperwork"],
                            ["Vague standards", "No SMART timelines"]
                        ],
                        "e": "Pair cause and effect in your answers."
                    },
                    {
                        "k": "mc",
                        "q": "Which is the deepest structural reason charters fail?",
                        "o": ["Lack of enforceable accountability", "Too much colour printing", "Too many websites"],
                        "a": 0,
                        "e": "Without consequences, a promise stays a slogan."
                    }
                ]
            },
            {
                "n": "Solutions & Best Practice",
                "e": "✅",
                "d": "What works, here and abroad",
                "c": [
                    {
                        "t": "Fixing the gaps",
                        "b": [
                            "<b>Co-create</b> with citizens and frontline staff.",
                            "Use <b>SMART standards</b> and service level agreements.",
                            "Give <b>statutory backing</b> through Right to Services laws.",
                            "<b>Third-party audits</b>, social audits and report cards.",
                            "<b>Train and reward</b> staff; link to performance appraisal."
                        ],
                        "k": ["SLA", "Social audit", "Statutory backing"]
                    },
                    {
                        "t": "Technology",
                        "b": [
                            "Online service portals with <b>tracking and auto-escalation</b> (for example Karnataka’s Sakala).",
                            "<b>CPGRAMS</b> for grievances; mobile alerts at each stage.",
                            "Digital delivery cuts discretion and delay."
                        ],
                        "k": ["E-governance", "Auto-escalation"]
                    },
                    {
                        "t": "Best practices",
                        "b": [
                            "<b>UK Charter Mark</b>: an award for organisations that excel at service standards.",
                            "<b>Madhya Pradesh Lok Sewa Guarantee</b>: statutory time-bound service with penalties.",
                            "<b>Citizen Report Cards</b> (Bangalore): evidence-based public feedback."
                        ],
                        "k": ["Charter Mark", "Lok Sewa Guarantee", "Report Card"]
                    }
                ],
                "q": [
                    {
                        "k": "multi",
                        "q": "Tap the effective solutions.",
                        "o": ["Co-create charters with citizens", "Statutory backing with penalties", "Hide the charter from the public", "Third-party and social audits"],
                        "a": [0, 1, 3],
                        "e": "Transparency and consequences drive results."
                    },
                    {
                        "k": "mc",
                        "q": "The UK Charter Mark is best described as:",
                        "o": ["A tax", "An award for excellent service standards", "A court", "A police force"],
                        "a": 1,
                        "e": "A recognition scheme that rewards good service."
                    },
                    {
                        "k": "match",
                        "q": "Match practice to place.",
                        "p": [
                            ["Charter Mark", "United Kingdom"],
                            ["Lok Sewa Guarantee", "Madhya Pradesh"],
                            ["Sakala", "Karnataka"],
                            ["Report Cards", "Bangalore (PAC)"]
                        ],
                        "e": "One domestic and one global example is enough for Mains."
                    },
                    {
                        "k": "mc",
                        "q": "What does ‘SMART standard’ mean in a charter?",
                        "o": ["Specific, measurable and time-bound", "Short, mild, and tentative", "Silent and recorded", "Subjective and flexible"],
                        "a": 0,
                        "e": "Clear, measurable, time-bound commitments."
                    }
                ]
            },
            {
                "n": "Mains Toolkit",
                "e": "🎯",
                "d": "Keywords, intro, conclusion",
                "c": [
                    {
                        "t": "Keywords to drop",
                        "b": [
                            "<b>Citizen-centric governance</b>, <b>service-delivery guarantee</b>, <b>New Public Management</b>.",
                            "<b>Sevottam</b>, <b>2nd ARC 12th Report</b>, <b>CPGRAMS</b>, <b>Lok Sewa Guarantee</b>.",
                            "<b>Paper tiger</b>, <b>ritual compliance</b>, <b>accountability deficit</b>."
                        ],
                        "k": ["Use 4 to 5 per answer"]
                    },
                    {
                        "t": "Answer skeleton",
                        "b": [
                            "<b>Intro:</b> define the charter; UK 1991 to India 1997.",
                            "<b>Body:</b> principles, models (Sevottam), 2nd ARC.",
                            "<b>Challenges:</b> design, awareness, enforcement.",
                            "<b>Way forward:</b> statutory backing, tech, audits.",
                            "<b>Conclusion:</b> from promise to guarantee."
                        ],
                        "k": ["Intro → Body → Challenges → Way forward → Conclusion"]
                    },
                    {
                        "t": "Ethics link (GS-4)",
                        "b": [
                            "Charters embody <b>accountability, responsiveness, empathy</b> and <b>public service orientation</b>.",
                            "A conscientious officer treats the charter as a personal duty, not a poster."
                        ],
                        "k": ["Public service values", "Probity"]
                    }
                ],
                "q": [
                    {
                        "k": "order",
                        "q": "Order the Mains answer skeleton.",
                        "o": ["Intro: define and origin", "Body: principles, Sevottam, 2nd ARC", "Challenges", "Way forward", "Conclusion"],
                        "e": "Define → Explain → Critique → Fix → Conclude."
                    },
                    {
                        "k": "mc",
                        "q": "Best one-line conclusion for a charter answer?",
                        "o": [
                            "Charters are useless.",
                            "Moving from a promise on paper to a guarantee in practice makes governance truly citizen-centric.",
                            "Everything is fine.",
                            "No more reform is needed."
                        ],
                        "a": 1,
                        "e": "Balanced, forward-looking and keyword-rich."
                    },
                    {
                        "k": "multi",
                        "q": "Tap the Mains keywords for this topic.",
                        "o": ["Sevottam", "CPGRAMS", "Citizen-centric governance", "Dynastic politics"],
                        "a": [0, 1, 2],
                        "e": "The fourth is unrelated."
                    },
                    {
                        "k": "flip",
                        "q": "Write a 2-line intro for ‘Citizen’s Charters have remained paper tigers’.",
                        "r": "Citizen’s Charters, born in the UK in 1991 and adopted in India after 1997, promise time-bound, transparent services. Yet without statutory backing or penalties, most remain declarations of intent rather than guarantees."
                    }
                ]
            }
        ],
        "pyq": [
            {
                "k": "flip",
                "q": "PYQ-style: Citizen’s Charters have not delivered the desired results. Examine the reasons and suggest measures. (150 words)",
                "r": "Intro: time-bound service promise (UK 1991, India 1997). Why they fell short: top-down design, vague standards, low awareness, no penalty (paper tiger). Fixes: co-create with SMART standards, Right to Services laws (MP Lok Sewa Guarantee), CPGRAMS, report cards, Sevottam audit. Conclude: from promise to guarantee."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Discuss the role of Sevottam in improving public service delivery.",
                "r": "Seva + Uttam, DARPG framework (~2006). Three modules: Citizen’s Charter, Grievance Redress, Service Delivery Capability. Benefit: a common yardstick and self-assessment. Limits: voluntary, uneven uptake. Link: 2nd ARC 12th Report. Way forward: independent audit and statutory backing."
            },
            {
                "k": "flip",
                "q": "PYQ-style: How far do Right to Services Acts address the limits of Citizen’s Charters?",
                "r": "Gains: statutory deadlines, penalty on officers, appeals (MP 2010 first, then Bihar, Rajasthan, Delhi, Karnataka Sakala). Gaps: only notified services, weak penalty use, low awareness, uneven states. The 2011 Central Bill lapsed in 2014. Way forward: wider coverage, digital tracking, social audits."
            },
            {
                "k": "flip",
                "q": "PYQ-style: What role can technology play in making Citizen’s Charters effective?",
                "r": "Online portals with tracking and auto-escalation (Sakala), CPGRAMS for grievances, SMS alerts, dashboards for monitoring, less discretion and delay. Caution: digital divide, so keep assisted and local-language channels. Conclude: tech enforces the promise only with accountability."
            },
            {
                "k": "flip",
                "q": "GS-4 case: A citizen has waited months for a service your charter promises in 15 days. What do you do?",
                "r": "Act: fast-track the case, find the cause of delay, apologise and inform the citizen, fix the process, fix responsibility, and record the lesson. Values: empathy, accountability, integrity, public service orientation. Report systemic gaps upward."
            },
            {
                "k": "flip",
                "q": "PYQ-style: Citizen-centric administration is the heart of good governance. Comment with reference to the 2nd ARC.",
                "r": "2nd ARC 12th Report: Citizen Centric Administration. Key ideas: consultation, realistic standards, review, grievance redress, service guarantees. Tools: Charter, Sevottam, CPGRAMS, report cards. Challenge: enforcement. Conclude: governance judged by citizen experience."
            }
        ],
        "sks": [
            {
                "t": "Citizen’s Charter",
                "s": [
                    "A Citizen’s Charter is a public promise of services, standards, timelines and redress (UK 1991, India 1997).",
                    "2nd ARC 12th Report on citizen-centric administration; MP Lok Sewa Guarantee Act, 2010.",
                    "Pros: transparency, accountability, empowered citizens. Cons: no legal force, vague standards, low awareness.",
                    "Sevottam (DARPG), 2nd ARC 12th Report, CPGRAMS.",
                    "Ladder: Charter (promise) → Bill 2011 (lapsed) → Right to Services Acts (guarantee)."
                ]
            },
            {
                "t": "Right to Services Acts",
                "s": [
                    "Statutes guaranteeing notified public services within fixed deadlines, with penalty and appeal. MP Lok Sewa Guarantee Act, 2010 was first.",
                    "MP 2010; Bihar 2011; Karnataka Sakala with online tracking.",
                    "Pros: enforceable deadlines, penalty on defaulters, appeals. Cons: only notified services, weak penalty use, low awareness.",
                    "Citizens Charter Bill 2011 (lapsed 2014); 2nd ARC 12th Report; CPGRAMS.",
                    "Ladder: Charter (promise) → Bill 2011 (lapsed) → RTS Acts (guarantee)."
                ]
            },
            {
                "t": "Sevottam model",
                "s": [
                    "Sevottam (Seva + Uttam) is the DARPG quality framework for public service delivery, with three modules.",
                    "Assessment against the framework shows gaps and gives an improvement roadmap.",
                    "Pros: common yardstick, links charter with grievance redress, builds capacity. Cons: voluntary, self-assessment, uneven uptake.",
                    "DARPG, 2nd ARC 12th Report, CPGRAMS.",
                    "Wheel: Sevottam at the centre with Citizen’s Charter, Grievance Redress and Service Delivery Capability around it."
                ]
            }
        ]
    }
}

print("Topics defined successfully. Total topics:", len(TOPICS))
