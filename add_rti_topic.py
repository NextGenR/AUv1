# -*- coding: utf-8 -*-
"""
Helper script to inject the complete RTI topic into scratch_builder.py
"""

RTI_TOPIC = {
    "id": "rti",
    "title": "Right to Information (RTI) & Governance",
    "badge": "🔑",
    "sub": "Master constitutional genesis (Art 19(1)(a)), statutory architecture, Section 8 exemptions, landmark case laws, and 2nd ARC reforms.",
    "hue": ["#0b8a9a", "#2f63d6", "#7442d6", "#b8760a", "#d23a40", "#0f8a62", "#d9570c"],
    "ico": [["🔑", "📜", "⚖️"], ["🏢", "⏱️", "📋"], ["🔒", "🛡️", "📝"], ["🏛️", "⚖️", "🗳️"], ["🚧", "⚠️", "⏳"], ["✅", "🏛️", "📊"], ["🎯", "🗺️", "🏆"]],
    "lessons": [
        {
            "n": "Constitutional Roots & Evolution",
            "e": "🧭",
            "d": "From Raj Narain (1975) & MKSS to 2005 Act",
            "c": [
                {
                    "t": "Constitutional Genesis: Article 19(1)(a)",
                    "b": [
                        "The Right to Information is rooted in <b>Article 19(1)(a) (Freedom of Speech and Expression)</b>, reinforced by <b>Article 14 (anti-arbitrariness)</b> and <b>Article 21 (dignity)</b>.",
                        "Landmark ruling: In <b>State of Uttar Pradesh v. Raj Narain (1975)</b>, the Supreme Court held that in a democracy where all agents of the public must be responsible for their conduct, citizens have a right to know every public act.",
                        "Shifts governance from the colonial culture of secrecy (*Official Secrets Act, 1923*) to participatory democracy."
                    ],
                    "k": ["Article 19(1)(a)", "Raj Narain (1975)", "Culture of Secrecy vs Openness"],
                    "n": "Without information, citizens cannot cast an informed vote or meaningfully exercise free speech."
                },
                {
                    "t": "Grassroots Struggle: The MKSS Movement",
                    "b": [
                        "In the 1990s, the <b>Mazdoor Kisan Shakti Sangathan (MKSS)</b> led by Aruna Roy in rural Rajasthan spearheaded the RTI movement.",
                        "Historic demand: <b>'Hamara Paisa, Hamara Hisab'</b> (Our Money, Our Accounts). Organized *Jan Sunwais* (public hearings) to audit muster rolls and expose fake vouchers in drought relief.",
                        "Proved that RTI is not an elite intellectual pursuit, but an indispensable weapon of survival for the poor."
                    ],
                    "k": ["MKSS Rajasthan", "Jan Sunwai (Social Audit)", "Hamara Paisa Hamara Hisab"],
                    "n": "A classic example of a grassroots civil society movement transforming into a statutory reality."
                },
                {
                    "t": "Legislative Evolution (1997–2005)",
                    "b": [
                        "<b>1997:</b> Tamil Nadu became the first state in India to pass an RTI law, followed by Goa, Delhi, and Karnataka.",
                        "<b>2002:</b> The central <i>Freedom of Information Act, 2002</i> was passed, but was toothless, lacked independent appellate bodies, and was never notified.",
                        "<b>2005:</b> Enactment of the comprehensive <b>Right to Information Act, 2005</b>, with the <b>DoPT (Dept. of Personnel & Training)</b> as the nodal department."
                    ],
                    "k": ["Tamil Nadu (1997 First State)", "Freedom of Information Act 2002", "RTI Act 2005", "DoPT Nodal Body"],
                    "n": "The 2005 Act provided enforceable mechanisms, penalty provisions, and independent oversight commissions."
                }
            ],
            "q": [
                {
                    "k": "mc",
                    "q": "In which landmark 1975 case did the Supreme Court first recognize the Right to Information under Article 19(1)(a)?",
                    "o": ["Kesavananda Bharati v. State of Kerala", "State of Uttar Pradesh v. Raj Narain", "Maneka Gandhi v. Union of India", "Minerva Mills v. Union of India"],
                    "a": 1,
                    "e": "In State of UP v. Raj Narain (1975), Justice Mathew ruled that citizens have a right to know every public act done by their functionaries."
                },
                {
                    "k": "mc",
                    "q": "Which grassroots movement in Rajasthan popularized the demand for public records through 'Jan Sunwais'?",
                    "o": ["Chipko Movement", "Mazdoor Kisan Shakti Sangathan (MKSS)", "Narmada Bachao Andolan", "Bhoodan Movement"],
                    "a": 1,
                    "e": "MKSS, founded by Aruna Roy, Nikhil Dey, and Shankar Singh, championed rural transparency through Jan Sunwais."
                },
                {
                    "k": "mc",
                    "q": "Which state was the first in India to enact an RTI law in 1997?",
                    "o": ["Maharashtra", "Tamil Nadu", "Kerala", "Rajasthan"],
                    "a": 1,
                    "e": "Tamil Nadu enacted India's first state-level Right to Information Act in 1997."
                },
                {
                    "k": "order",
                    "q": "Arrange the milestones in India's transparency movement in chronological order.",
                    "o": [
                        "SC recognizes RTI in Raj Narain case (1975)",
                        "MKSS grassroots Jan Sunwais in Rajasthan (1990s)",
                        "Tamil Nadu enacts first state RTI law (1997)",
                        "Passage of the Right to Information Act (2005)"
                    ],
                    "e": "1975 (Raj Narain) → 1990s (MKSS) → 1997 (Tamil Nadu) → 2005 (RTI Act)."
                }
            ]
        },
        {
            "n": "Core Architecture & Timelines",
            "e": "🏛️",
            "d": "Public authorities, PIOs & Section 7 deadlines",
            "c": [
                {
                    "t": "Universal Scope: Public Authority (Section 2(h))",
                    "b": [
                        "Defines 'Public Authority' as any body established by the <b>Constitution, Parliament, State Legislature, or government notification</b>.",
                        "Critically includes entities <b>owned, controlled, or substantially financed</b> directly or indirectly by government funds.",
                        "Covers non-government organizations (NGOs) receiving substantial state funding."
                    ],
                    "k": ["Section 2(h)", "Substantially Financed", "Public Authority Scope"],
                    "n": "Broad definition ensures public funds cannot hide behind corporate or non-profit veils."
                },
                {
                    "t": "Proactive Transparency (Section 4)",
                    "b": [
                        "Mandates all public authorities to <b>suo motu publish details</b> of their organization, functions, powers, officers' salaries, and subsidy schemes.",
                        "Requires digitized records for easy public access and regular updating.",
                        "Philosophy: Sunshine by default — minimize the necessity for citizens to file formal applications."
                    ],
                    "k": ["Section 4 Suo Motu Disclosure", "Digitized Records", "Proactive Sunshine"],
                    "n": "If Section 4 is fully implemented, over 70% of routine RTI applications become unnecessary."
                },
                {
                    "t": "Strict Statutory Deadlines (Section 7)",
                    "b": [
                        "<b>General Request:</b> Must be answered within <b>30 days</b> (or 35 days if submitted via Assistant PIO).",
                        "<b>Life or Liberty:</b> If the requested information concerns the life or liberty of an individual, it must be provided within <b>48 HOURS</b>!",
                        "<b>Fees:</b> Nominal fee for general citizens; <b>100% free for Below Poverty Line (BPL) applicants</b>. If response is delayed beyond 30 days, information must be given free to everyone."
                    ],
                    "k": ["30-Day Standard Limit", "48-Hour Life & Liberty Rule", "BPL Fee Waiver", "Free if Delayed"],
                    "n": "The 48-hour life-or-liberty rule is vital for undertrials, police encounters, and emergency medical access."
                }
            ],
            "q": [
                {
                    "k": "mc",
                    "q": "Within what statutory timeframe must information concerning 'life or liberty' be supplied under Section 7(1)?",
                    "o": ["24 hours", "48 hours", "7 days", "15 days"],
                    "a": 1,
                    "e": "Section 7(1) mandates a strict 48-hour turnaround if information concerns an individual's life or liberty."
                },
                {
                    "k": "tf",
                    "q": "Citizens living Below the Poverty Line (BPL) must pay double the fee to prioritize their applications.",
                    "a": 1,
                    "e": "False. Section 7(5) explicitly waives all application and copying fees for BPL citizens."
                },
                {
                    "k": "multi",
                    "q": "Tap all entities falling under the definition of 'public authority' under Section 2(h).",
                    "o": ["Constitutional bodies like Election Commission", "Statutory corporations established by Parliament", "NGOs substantially financed by the government", "Wholly private clubs with zero government funding"],
                    "a": [0, 1, 2],
                    "e": "Bodies created by Constitution, statute, or substantially financed by govt qualify. Wholly private clubs with no govt funds do not."
                },
                {
                    "k": "match",
                    "q": "Match the statutory section to its core mandate.",
                    "p": [
                        ["Section 2(h)", "Definition of Public Authority"],
                        ["Section 4", "Suo motu proactive transparency"],
                        ["Section 5", "Designation of PIOs & APIOs"],
                        ["Section 7", "30-day / 48-hour deadlines & fees"]
                    ],
                    "e": "Memorize Sections 2(h), 4, 7, 8, and 20 for GS-2 answers!"
                }
            ]
        },
        {
            "n": "Exemptions & Recent Amendments",
            "e": "⚖️",
            "d": "Section 8, 2019 Tenure & DPDP Act 2023",
            "c": [
                {
                    "t": "Section 8 Exemptions & Public Interest Override",
                    "b": [
                        "Section 8(1) carves out limited exceptions: national security, foreign relations, cabinet papers, commercial confidence, and personal privacy.",
                        "<b>The Golden Rule — Section 8(2) Public Interest Override:</b> A public authority may allow access to exempt information if <b>public interest in disclosure outweighs the harm to protected interests</b>!",
                        "Parliamentary Parity Proviso: <i>Information which cannot be denied to Parliament or a State Legislature shall not be denied to any citizen.</i>"
                    ],
                    "k": ["Section 8(1) Exemptions", "Section 8(2) Public Interest Override", "Parliamentary Parity"],
                    "n": "Section 8(2) establishes that public welfare always trumps bureaucratic secrecy."
                },
                {
                    "t": "RTI (Amendment) Act, 2019",
                    "b": [
                        "Removed the fixed <b>5-year statutory tenure</b> for Central and State Information Commissioners.",
                        "Removed statutory salary parity linking CIC to Chief Election Commissioner.",
                        "Tenure, salaries, and service conditions are now <b>determined by rules prescribed by the Central Government</b>.",
                        "Critique: Stirs concerns regarding the perceived independence and institutional autonomy of the commissions."
                    ],
                    "k": ["2019 Amendment", "Removal of Fixed 5-Year Tenure", "Executive Rule-Making"],
                    "n": "A frequent UPSC Mains topic on the dilution of independent statutory watchdogs."
                },
                {
                    "t": "DPDP Act, 2023 [Section 44(3)]",
                    "b": [
                        "The Digital Personal Data Protection Act, 2023 substituted Section 8(1)(j) of the RTI Act with an exemption for <b>'information which relates to personal information'</b>.",
                        "Deleted earlier provisos that allowed disclosure if information had a nexus to public activity or if it could not be denied to Parliament.",
                        "However, the overarching <b>Section 8(2) Public Interest Override remains fully alive</b> in the statute!"
                    ],
                    "k": ["DPDP Act 2023 Sec 44(3)", "Section 8(1)(j) Substitution", "Personal Information Exemption"],
                    "n": "Balances the constitutional Right to Information with the Right to Privacy (Puttaswamy 2017)."
                }
            ],
            "q": [
                {
                    "k": "mc",
                    "q": "What extraordinary power does Section 8(2) of the RTI Act bestow upon authorities?",
                    "o": ["To delete controversial government files", "To override exemptions if public interest outweighs harm", "To cancel citizen applications without reasons", "To arrest citizens for asking sensitive questions"],
                    "a": 1,
                    "e": "Section 8(2) allows disclosure of exempt records if the public interest in disclosure outweighs the harm."
                },
                {
                    "k": "tf",
                    "q": "The RTI (Amendment) Act, 2019 strengthened the statutory autonomy of Information Commissioners by granting them constitutional status.",
                    "a": 1,
                    "e": "False. It removed fixed 5-year tenures and salary parity, placing terms under executive discretion."
                },
                {
                    "k": "mc",
                    "q": "What significant modification did the DPDP Act, 2023 introduce to Section 8(1)(j) of the RTI Act?",
                    "o": ["Abolished the RTI Act completely", "Substituted Section 8(1)(j) with a blanket exemption for personal information", "Made all government databases public", "Banned journalists from filing RTIs"],
                    "a": 1,
                    "e": "Section 44(3) of DPDP Act substituted Section 8(1)(j) to broaden exemptions for personal information."
                },
                {
                    "k": "multi",
                    "q": "Tap true statements regarding exemptions under the RTI Act.",
                    "o": ["Section 8(2) public interest override continues to exist after DPDP Act 2023", "Information that cannot be denied to Parliament cannot be denied to citizens", "Any officer can invent new exemptions not listed in Section 8", "Cabinet papers must be disclosed after decisions are made and completed"],
                    "a": [0, 1, 3],
                    "e": "Section 8(2) still overrides, parliamentary parity stands, and completed cabinet decisions become disclosable."
                }
            ]
        },
        {
            "n": "Landmark Case Laws",
            "e": "📜",
            "d": "Aditya Bandopadhyay to Electoral Bonds (2024)",
            "c": [
                {
                    "t": "Answer Books & ACRs: Exams and Service Records",
                    "b": [
                        "<b>CBSE v. Aditya Bandopadhyay (2011):</b> The Supreme Court held that evaluated answer scripts are 'information' accessible under RTI. The examiner–examinee relationship is not an exempt fiduciary shield.",
                        "<b>Girish Ramchandra Deshpande v. CIC (2013):</b> Annual Confidential Reports (ACRs), service records, and disciplinary proceedings constitute personal information under Section 8(1)(j) unless larger public interest justifies disclosure."
                    ],
                    "k": ["Aditya Bandopadhyay (2011)", "Answer Books Disclosable", "Girish Deshpande (2013)"],
                    "n": "Balances student transparency against the privacy of public servants' personnel records."
                },
                {
                    "t": "Financial Transparency & Institutions",
                    "b": [
                        "<b>Thalappalam Coop Bank v. State of Kerala (2013):</b> Cooperative societies are not automatically public authorities under Section 2(h); they must satisfy the test of substantial state financing or control.",
                        "<b>RBI v. Jayantilal N. Mistry (2016):</b> SC rejected the Reserve Bank of India's blanket claim of fiduciary confidentiality, ordering disclosure of inspection reports of defaulting banks in the public interest."
                    ],
                    "k": ["Thalappalam Coop Bank (2013)", "RBI v. Jayantilal Mistry (2016)", "Fiduciary Shield Rejected"],
                    "n": "Reaffirms that economic regulators cannot shield systemic financial defaulters behind secrecy."
                },
                {
                    "t": "CJI Office & Electoral Bonds (2019 & 2024)",
                    "b": [
                        "<b>CPIO, Supreme Court v. Subhash Chandra Agarwal (2019):</b> A 5-judge Constitution Bench held that the <b>Office of the Chief Justice of India (CJI) is a public authority</b> under RTI, balancing judicial independence with transparency via proportionality.",
                        "<b>ADR v. Union of India (2024):</b> Constitution Bench unanimously struck down the Electoral Bonds Scheme, holding that voters' right to know political party funding is an integral fundamental right under Article 19(1)(a)."
                    ],
                    "k": ["CJI Office under RTI (2019)", "Subhash Chandra Agarwal", "ADR Electoral Bonds (2024)", "Voters' Right to Know"],
                    "n": "The 2024 Electoral Bonds judgment is the strongest constitutional reaffirmation of RTI in decades."
                }
            ],
            "q": [
                {
                    "k": "match",
                    "q": "Match the landmark case to its historic legal doctrine.",
                    "p": [
                        ["Aditya Bandopadhyay (2011)", "Exam answer scripts accessible under RTI"],
                        ["RBI v. Jayantilal Mistry (2016)", "Rejected blanket fiduciary shield for bank inspection reports"],
                        ["Subhash Chandra Agarwal (2019)", "Office of the CJI is a public authority under RTI"],
                        ["ADR v. Union of India (2024)", "Struck down Electoral Bonds under Art 19(1)(a)"]
                    ],
                    "e": "These four cases represent the bedrock of judicial interpretation of the RTI Act."
                },
                {
                    "k": "mc",
                    "q": "In which case did the Supreme Court hold that cooperative societies are not automatically public authorities unless substantially financed by the state?",
                    "o": ["ADR Case", "Thalappalam Coop Bank v. State of Kerala", "Raj Narain Case", "Jayantilal Mistry Case"],
                    "a": 1,
                    "e": "In Thalappalam (2013), SC clarified that cooperative societies need substantial govt control or funds to fall under Sec 2(h)."
                },
                {
                    "k": "tf",
                    "q": "In Subhash Chandra Agarwal (2019), the Supreme Court ruled that judicial independence completely excludes the higher judiciary from the RTI Act.",
                    "a": 1,
                    "e": "False. The Constitution Bench held that the CJI's office IS a public authority under RTI, harmonized via proportionality."
                }
            ]
        },
        {
            "n": "Systemic Challenges & Whistleblower Peril",
            "e": "🚧",
            "d": "Vacancies, threats, the 4% penalty & Official Secrets",
            "c": [
                {
                    "t": "Danger to RTI Users & Whistleblowers",
                    "b": [
                        "Citizens and activists using RTI to expose sand mafia, tender rigging, or panchayat scams face physical assault, harassment, and murder.",
                        "Over 100+ RTI activists have been murdered across India over the past two decades.",
                        "The <b>Whistleblowers Protection Act, 2014</b> has languished without operationalized rules, leaving information seekers vulnerable."
                    ],
                    "k": ["Whistleblower Murders", "Whistleblowers Protection Act 2014", "Safety Crisis"],
                    "n": "When seeking public information carries a death sentence, democracy is mortally wounded."
                },
                {
                    "t": "Appellate Backlogs & Vacancy Paralysis",
                    "b": [
                        "Over <b>3 to 4 lakh appeals</b> remain pending across the Central Information Commission (CIC) and State Information Commissions (SICs).",
                        "Governments delay appointments, leaving several state commissions completely headless or functioning with skeletal staff.",
                        "Waiting times for a second appeal stretch from 2 to 5 years, converting 'Right to Information' into 'Right to Wait'."
                    ],
                    "k": ["Commission Vacancies", "Right to Wait", "Multi-Year Pendency"],
                    "n": "Delayed justice in transparency turns statutory promises into paper tigers."
                },
                {
                    "t": "The 4% Penalty Paradox & Colonial Secrecy",
                    "b": [
                        "Section 20 allows commissions to levy fines of ₹250/day up to ₹25,000 on recalcitrant PIOs.",
                        "Empirical data: Between 2015 and 2023, <b>penalties were imposed in barely ~4% of cases</b> where violations were found!",
                        "Bureaucrats weaponize minor formatting errors or claim 'state secret' under the lingering mindset of the <b>Official Secrets Act, 1923</b>."
                    ],
                    "k": ["Section 20 Penalty Under-Use (4%)", "Official Secrets Act 1923 Mindset", "Unfair Rejections"],
                    "n": "Without fear of personal financial penalties, PIOs have zero incentive to answer on time."
                }
            ],
            "q": [
                {
                    "k": "mc",
                    "q": "Between 2015 and 2023, approximately what percentage of defaulting officers faced Section 20 financial penalties?",
                    "o": ["Over 50%", "About 25%", "Barely ~4%", "Exactly 0%"],
                    "a": 2,
                    "e": "Transparency studies reveal that penalties are imposed in only ~4% of eligible violation cases, nullifying deterrence."
                },
                {
                    "k": "tf",
                    "q": "The Whistleblowers Protection Act, 2014 has established dedicated local safe-houses and comprehensive rules in all states.",
                    "a": 1,
                    "e": "False. The Act has not been fully operationalized through comprehensive notified rules."
                },
                {
                    "k": "multi",
                    "q": "Tap genuine systemic challenges crippling the RTI Act.",
                    "o": ["Chronic vacancies and backlog in Information Commissions", "Lack of physical safety for grassroots whistleblowers", "Low rate of penalty imposition under Section 20", "Too many officers being sent to jail"],
                    "a": [0, 1, 2],
                    "e": "Vacancies, activist murders, and lack of penalties cripple implementation. Officers are almost never jailed."
                }
            ]
        },
        {
            "n": "2nd ARC & The Way Forward",
            "e": "✅",
            "d": "National Coordination Committee & systemic fixes",
            "c": [
                {
                    "t": "2nd ARC Blueprint: 1st Report",
                    "b": [
                        "The 2nd Administrative Reforms Commission (ARC) dedicated its 1st Report to <b>'Right to Information: Master Key to Good Governance'</b>.",
                        "Recommended establishing a <b>National Coordination Committee (NCC)</b> under the Chief Information Commissioner to monitor portal performance and impact.",
                        "Stressed that at least <b>half (50%) of Information Commissioners</b> should be drawn from non-civil services backgrounds (law, media, academia, civil society)."
                    ],
                    "k": ["2nd ARC 1st Report", "Master Key to Good Governance", "National Coordination Committee", "50% Non-Civil Services"],
                    "n": "Breaking the bureaucratic monopoly over Information Commissions restores public trust."
                },
                {
                    "t": "Statutory Protection Chapter for Seekers",
                    "b": [
                        "Urgent need to amend the RTI Act to incorporate a dedicated chapter: <b>'Protection of those seeking information under the RTI Act'</b>.",
                        "Mandate police protection and fast-track prosecution when an information seeker reports intimidation or filing an RTI on sensitive land/mining issues.",
                        "Must work hand-in-hand with fully operationalized rules under the Whistleblowers Protection Act."
                    ],
                    "k": ["Dedicated Protection Chapter", "Whistleblower Safeguards", "Fast-track Prosecution"],
                    "n": "State must guarantee life and liberty to those who dare to shine light on corruption."
                },
                {
                    "t": "Independent Public Records Offices & Tech",
                    "b": [
                        "2nd ARC recommended setting up independent <b>Public Records Offices</b> at Central and State levels to overhaul archiving and indexing.",
                        "<b>Standardize procedures:</b> Eliminate archaic payment methods (like compulsory demand drafts); unify application fee structures nationwide.",
                        "Continuous capacity building and rigorous sensitization for PIOs on the constitutional sanctity of transparency."
                    ],
                    "k": ["Public Records Offices", "Standardized Fee Structure", "E-Filing & Digital Tracking"],
                    "n": "Good governance cannot function without modern, indexed, searchable public records."
                }
            ],
            "q": [
                {
                    "k": "mc",
                    "q": "What body did the 2nd ARC recommend setting up under the Chief Information Commissioner to evaluate RTI impact?",
                    "o": ["Central Vigilance Commission", "National Coordination Committee (NCC)", "National Transparency Tribunal", "Public Grievance Council"],
                    "a": 1,
                    "e": "The 2nd ARC recommended an NCC under the Chief Information Commissioner to monitor RTI nationwide."
                },
                {
                    "k": "mc",
                    "q": "What proportion of Information Commissioners should be drawn from non-civil service backgrounds according to the 2nd ARC?",
                    "o": ["10%", "25%", "At least 50%", "100%"],
                    "a": 2,
                    "e": "The 2nd ARC recommended at least 50% non-civil service commissioners to avoid bureaucratic insularity."
                },
                {
                    "k": "multi",
                    "q": "Tap the core reform measures recommended by the 2nd ARC for RTI.",
                    "o": ["Establish independent Public Records Offices", "Incorporate statutory protection chapter for information seekers", "Standardize fee structures and eliminate demand draft hurdles", "Repeal the RTI Act and replace with Official Secrets Act"],
                    "a": [0, 1, 2],
                    "e": "Public Records Offices, protection chapter, and standardized digital access are 2nd ARC cornerstones."
                },
                {
                    "k": "match",
                    "q": "Match the proposed reform to its governance outcome.",
                    "p": [
                        ["National Coordination Committee", "Central monitoring of portal & Act impact"],
                        ["50% Non-Civil Service Commissioners", "Prevents bureaucratic bias and insularity"],
                        ["Public Records Offices", "Modern cataloging and suo motu disclosure"],
                        ["Statutory Protection Chapter", "Shields whistleblowers from physical violence"]
                    ],
                    "e": "Strategic solutions to cite in Mains GS-2 answers."
                }
            ]
        },
        {
            "n": "Mains Answer Mastery Toolkit",
            "e": "🎯",
            "d": "Keywords, 5-point skeleton & model intro",
            "c": [
                {
                    "t": "High-Yield Keywords to Drop",
                    "b": [
                        "<b>Constitutional Anchors:</b> Article 19(1)(a), Raj Narain (1975), Sunshine legislation, Culture of secrecy vs openness.",
                        "<b>Statutory Architecture:</b> Section 2(h) Public Authority, Section 4 Suo Motu, Section 7 Life & Liberty (48h), Section 8(2) Public Interest Override, Section 20 Penalty.",
                        "<b>Landmark Jurisprudence:</b> Subhash Chandra Agarwal (CJI office), Jayantilal Mistry (RBI), ADR (Electoral Bonds 2024).",
                        "<b>2nd ARC Recommendations:</b> 1st Report ('Master Key to Good Governance'), National Coordination Committee, 50% non-civil service commissioners, Public Records Offices."
                    ],
                    "k": ["Use 4 to 5 per Mains answer!"],
                    "n": "Examiners award top marks for precise statutory section citations and landmark jurisprudence."
                },
                {
                    "t": "Mains 5-Stage Answer Skeleton",
                    "b": [
                        "<b>1. Intro:</b> Article 19(1)(a) + Raj Narain (1975) + MKSS grassroots Jan Sunwais.",
                        "<b>2. Statutory Pillars:</b> Sections 2(h), 4, 7 (48h/30d), and the Section 8(2) public interest override.",
                        "<b>3. Landmark Case Laws:</b> CJI under RTI (Subhash Chandra Agarwal) & ADR Electoral Bonds (2024).",
                        "<b>4. Structural Bottlenecks:</b> 2019 tenure amendment, DPDP Act 2023 Sec 44(3), 4% penalty rate, whistleblower murders.",
                        "<b>5. Way Forward & Conclusion:</b> 2nd ARC blueprint (NCC, 50% non-IAS, Public Records Offices, Whistleblower chapter); master key to participatory democracy."
                    ],
                    "k": ["Intro → Statutory Pillars → Case Laws → Bottlenecks → 2nd ARC Conclusion"],
                    "n": "A comprehensive, high-scoring structure for any 10-marker or 15-marker RTI question."
                }
            ],
            "q": [
                {
                    "k": "order",
                    "q": "Order the optimal Mains answer structure for a Right to Information question.",
                    "o": [
                        "Intro: Article 19(1)(a), Raj Narain (1975) & MKSS struggle",
                        "Statutory Canvas: Sections 2(h), 4, 7 & Sec 8(2) override",
                        "Landmark Jurisprudence: Subhash Chandra Agarwal & ADR (2024)",
                        "Contemporary Challenges: Vacancies, 4% penalty & whistleblower peril",
                        "Way Forward: 2nd ARC National Coordination Committee & Protection"
                    ],
                    "e": "Constitutional Roots → Statutory Design → Jurisprudence → Bottlenecks → 2nd ARC Solutions."
                },
                {
                    "k": "mc",
                    "q": "Best one-line concluding sentence for an answer on RTI?",
                    "o": [
                        "The RTI Act should be repealed because citizens ask too many questions.",
                        "Right to Information is the master key to participatory democracy, transforming citizens from passive recipients of governance into vigilant custodians of constitutional accountability.",
                        "Official secrecy must be restored to accelerate bureaucratic file movement.",
                        "Information Commissions should be abolished to save public funds."
                    ],
                    "a": 1,
                    "e": "A balanced, inspiring constitutional conclusion directly echoing the 2nd ARC."
                },
                {
                    "k": "flip",
                    "q": "Write a 2-line intro for 'Right to Information: Cornerstone of Democratic Governance'.",
                    "r": "Recognized in State of UP v. Raj Narain (1975) as an integral part of Article 19(1)(a) and birthed by grassroots struggle (MKSS), the RTI Act, 2005 dismantled the colonial culture of secrecy. By institutionalizing transparency and citizen participation, it serves as the master key to democratic accountability."
                }
            ]
        }
    ],
    "pyq": [
        {
            "k": "flip",
            "q": "PYQ-style: 'Right to Information is not merely a statutory right but a fundamental constitutional entitlement.' Trace its evolution and evaluate its efficacy in dismantling bureaucratic secrecy. (150 words)",
            "r": "Intro: SC in Raj Narain (1975) recognized RTI within Article 19(1)(a); grassroots struggle by MKSS in Rajasthan (Jan Sunwais) led to the RTI Act, 2005. Efficacy in Promoting Openness: 1. Sections 2(h), 4 & 7 established enforceable transparency, life/liberty 48-hr mandate, and BPL fee waivers. 2. Section 8(2) provided a golden 'public interest override'. 3. SC expanded scope: CJI office under RTI (Subhash Chandra Agarwal 2019) and struck down Electoral Bonds (ADR 2024). Persistent Impediments: 1. Official Secrets Act 1923 culture persists; 4% penalty rate under Sec 20. 2. Murders of whistleblowers without operationalized Whistleblowers Act. 3. 2019 tenure dilution & DPDP Act 2023 Sec 44(3). Conclude: Adopt 2nd ARC recommendations (NCC, 50% non-bureaucrat commissioners) to preserve transparency as the master key to democracy."
        },
        {
            "k": "flip",
            "q": "PYQ-style: The office of the Chief Justice of India was brought under the RTI Act in Subhash Chandra Agarwal (2019). How did the Supreme Court reconcile transparency with judicial independence? (150 words)",
            "r": "Context: Constitution Bench affirmed that the CJI's office is a public authority under Section 2(h). Reconciliation Doctrine: 1. Transparency vs Independence: Held that transparency does not undermine judicial independence; it fortifies public faith in judicial probity. 2. Proportionality & Balance: Disclosure must be weighed against personal privacy under Section 8(1)(j) using the proportionality test. 3. Fiduciary Filter: Deliberations of the Collegium and medical records are shielded unless larger public interest demands disclosure. Significance: Established that no constitutional office is an island of absolute secrecy, setting a benchmark for open governance while safeguarding institutional integrity."
        },
        {
            "k": "flip",
            "q": "PYQ-style: Examine the safety risks faced by RTI activists and suggest measures to protect information seekers drawing from 2nd ARC recommendations. (150 words)",
            "r": "Context: Over 100+ RTI activists have been murdered for exposing sand, mining, and welfare corruption. Structural Vulnerability: 1. Asymmetry of power between rural citizens and corrupt local syndicates. 2. Whistleblowers Protection Act 2014 remains non-operationalized without notified rules. 2nd ARC Measures: 1. Statutory Protection Chapter: Amend RTI Act to include a dedicated chapter for mandatory state protection of threatened applicants. 2. Fast-track investigation: Mandate high-level time-bound police probes into attacks on activists. 3. Suo motu disclosure of queried info: If an activist is threatened or killed, the requested information should be immediately placed in the public domain to eliminate the murderer's motive. Conclude: Protecting the information seeker is prerequisite to protecting the right itself."
        }
    ],
    "sks": [
        {
            "t": "Right to Information Act, 2005",
            "s": [
                "RTI is rooted in Article 19(1)(a) as held in Raj Narain (1975); catalyzed by MKSS Jan Sunwais in Rajasthan.",
                "Sections 2(h) Public Authority, Sec 4 Suo Motu, Sec 7 (30 days / 48h life & liberty), Sec 8(2) override.",
                "Pros: citizen empowerment, exposed major scams, BPL fee waiver. Cons: 4% penalty rate, backlog, activist deaths.",
                "2nd ARC 1st Report ('Master Key to Good Governance'), National Coordination Committee, DoPT.",
                "Ladder: Colonial Secrecy (OSA 1923) → Raj Narain (1975) → MKSS → RTI Act 2005 → Sunshine Democracy."
            ]
        },
        {
            "t": "RTI vs Right to Privacy & DPDP Act",
            "s": [
                "Tension between Article 19(1)(a) (Transparency) and Article 21 Right to Privacy (Puttaswamy 2017).",
                "Section 8(1)(j) amended via DPDP Act 2023 Sec 44(3) to exempt personal information; Sec 8(2) override retained.",
                "Pros: protects citizen data. Cons: public authorities weaponize privacy to shield corrupt public officials.",
                "Girish Deshpande (2013), Subhash Chandra Agarwal (2019 CJI Office proportionality), 2nd ARC.",
                "Balance Scale: Right to Know (Art 19(1)(a)) on left vs Right to Privacy (Art 21) on right; public interest weighs center."
            ]
        },
        {
            "t": "2nd ARC Reforms on RTI",
            "s": [
                "2nd ARC dedicated its 1st Report, 'Right to Information: Master Key to Good Governance'.",
                "National Coordination Committee (NCC) under Chief Information Commissioner to monitor implementation.",
                "Pros: checks bureaucratic insularity, unifies portals. Cons: recommendations remain largely un-implemented.",
                "50% Non-Civil Service Commissioners; Independent Public Records Offices; Protection Chapter for seekers.",
                "Wheel: Chief Information Commissioner at center surrounded by NCC, Public Records Office, 50% Non-IAS, and Protection."
            ]
        }
    ]
}

def inject():
    with open("scratch_builder.py", "r", encoding="utf-8") as f:
        content = f.read()

    # Check if rti is already in scratch_builder
    if '"rti":' in content:
        print("RTI topic already exists in scratch_builder.py")
        return

    # Find the last closing bracket of TOPICS
    target = 'print("Topics defined successfully. Total topics:", len(TOPICS))'
    import pprint
    # Dump formatted
    import json
    rti_code = '    "rti": ' + json.dumps(RTI_TOPIC, ensure_ascii=False, indent=8) + ',\n}\n'
    
    # Replace the end of TOPICS: '    }\n}\n'
    idx = content.rfind('    }\n}')
    if idx == -1:
        idx = content.rfind('    }\n}\r\n')
    
    new_content = content[:idx] + '    },\n' + rti_code + '\n' + target + '\n'
    with open("scratch_builder.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Injected RTI topic into scratch_builder.py successfully!")

if __name__ == "__main__":
    inject()
