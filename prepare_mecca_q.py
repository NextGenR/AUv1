# -*- coding: utf-8 -*-
"""
Generator for 100 UPSC Current Affairs Questions:
- 50 on MECCA PACT (Trilateral Joint Defence Agreement)
- 50 on FREEBIES vs WELFARE GOODS (Revdi Culture & Fiscal Federalism)
Across the 10 selected testing patterns:
1. mc, 2. tf, 3. multi, 4. flag, 5. riddle, 6. match, 7. order, 8. sort, 9. year, 11. flip
"""

import json

mecca_questions = [
    # --- Pattern 1: mc (5 questions) ---
    {
        "id": "mecca_01",
        "topic": "Mecca Pact",
        "k": "mc",
        "q": "Which three nations signed the Trilateral Joint Defence Agreement in Mecca, altering the West and South Asian security matrix?",
        "o": [
            "Saudi Arabia, UAE, and Pakistan",
            "Saudi Arabia, Pakistan, and Turkey",
            "Turkey, Iran, and Qatar",
            "Saudi Arabia, Egypt, and Pakistan"
        ],
        "a": 1,
        "kw": "Trilateral Signatories",
        "e": "The Trilateral Joint Defence Agreement was signed in Mecca by Saudi Arabia, Pakistan, and Turkey, bringing together Arab financial heft, Pakistani military manpower/nuclear threshold, and Turkish defence-industrial technology.",
        "data": "Signed in Mecca (2024–25); combines KSA's $83B defence budget with Turkey's NATO-standard defence exports and Pakistan's 6.6L army.",
        "ex": "Joint naval and air maneuvers coordinated between Riyadh, Rawalpindi, and Ankara.",
        "mains": "Marks a significant structural departure from traditional Gulf reliance on bilateral Western security umbrellas."
    },
    {
        "id": "mecca_02",
        "topic": "Mecca Pact",
        "k": "mc",
        "q": "What is the primary economic and domestic driver compelling Saudi Arabia to participate in the Mecca Defence Pact?",
        "o": [
            "Replacing OPEC+ oil production quotas",
            "Protecting critical oil infrastructure and Vision 2030 investments from asymmetric drone and missile threats",
            "Deploying Saudi ground troops in Pakistani border regions",
            "Funding Turkey's high-speed rail network"
        ],
        "a": 1,
        "kw": "Vision 2030 Infrastructure Shield",
        "e": "Following devastating drone strikes on Abqaiq-Khurais (2019) and Houthi missile incursions, Saudi Arabia seeks multi-layered air and asymmetric defense to safeguard its gigaprojects (NEOM, Red Sea) and oil export terminals.",
        "data": "Saudi Arabia defense outlay ~$83 Billion; Vision 2030 requires over $1 Trillion in foreign investment requiring an ironclad regional security environment.",
        "ex": "Protecting Aramco facilities and Ras Tanura oil export terminals from regional asymmetric saturation attacks.",
        "mains": "Demonstrates the nexus between economic diversification and sovereign defense architecture in rentier petro-states."
    },
    {
        "id": "mecca_03",
        "topic": "Mecca Pact",
        "k": "mc",
        "q": "Approximately what percentage of India's total crude oil imports is sourced from the Kingdom of Saudi Arabia?",
        "o": [
            "About 5%",
            "About 14%",
            "About 35%",
            "Over 50%"
        ],
        "a": 1,
        "kw": "India-KSA Energy Anchor",
        "e": "Saudi Arabia remains one of India's top 3 crude suppliers, accounting for ~14% of India's crude imports alongside Russia and Iraq.",
        "data": "14% of India's crude imports; Bilateral trade ~$43 Billion (FY 2023-24).",
        "ex": "Long-term crude supply agreements between Saudi Aramco and Indian public sector refiners (IOCL, BPCL).",
        "mains": "Underpins India's vital interest in Persian Gulf stability and sea lane open access."
    },
    {
        "id": "mecca_04",
        "topic": "Mecca Pact",
        "k": "mc",
        "q": "Which proposed transnational connectivity corridor is most vulnerable to geopolitical friction arising from Turkish inclusion in the Mecca Pact?",
        "o": [
            "INSTC (International North-South Transport Corridor)",
            "IMEC (India-Middle East-Europe Economic Corridor)",
            "CPEC (China-Pakistan Economic Corridor)",
            "Kaladan Multi-Modal Transit Transport Project"
        ],
        "a": 1,
        "kw": "IMEC Geopolitical Vulnerability",
        "e": "IMEC links India to Europe via UAE, Saudi Arabia, Jordan, and Israel, deliberately bypassing Turkey. Turkish President Erdogan strongly opposed IMEC, promoting the rival Iraq Development Road instead.",
        "data": "IMEC unveiled at New Delhi G20 Summit (2023); route relies critically on Saudi rail network connecting Al Ghuwaifat to Haifa.",
        "ex": "Turkey pushing the $17 Billion 'Development Road' from Basra to Europe as an explicit counter to IMEC.",
        "mains": "Highlights how minilateral pacts in West Asia can create geo-economic bottlenecks for India's European trade routes."
    },
    {
        "id": "mecca_05",
        "topic": "Mecca Pact",
        "k": "mc",
        "q": "Which prominent Indian strategic affairs scholar highlighted that pan-Islamic defense formations historically fracture due to deep intra-regional national interest divergences?",
        "o": [
            "C. Raja Mohan",
            "Stanly Johny",
            "Brahma Chellaney",
            "Sanjaya Baru"
        ],
        "a": 1,
        "kw": "Expert Critique on Pan-Islamic Alliances",
        "e": "Stanly Johny (The Hindu) has argued that ideological or religious rhetoric in West Asian defense alignments inevitably collapses under the weight of divergent national security threats.",
        "data": "Historical precedent: Baghdad Pact (CENTO) and Islamic Military Counter Terrorism Coalition (IMCTC).",
        "ex": "Saudi Arabia prioritizing containment of Iranian proxies, while Pakistan avoids antagonizing Tehran along its Balochistan border.",
        "mains": "Provides an authoritative scholarly citation for questioning the operational cohesion of the Mecca Pact."
    },

    # --- Pattern 2: tf (5 questions) ---
    {
        "id": "mecca_06",
        "topic": "Mecca Pact",
        "k": "tf",
        "q": "True or False: The Mecca Pact establishes an automatic NATO-style Article 5 collective defense obligation requiring Saudi Arabia to enter a military war if Pakistan is attacked by India.",
        "a": 1,
        "kw": "Non-Automatic Collective Defense",
        "e": "False! The agreement is a consultative and capacity-building framework for joint training, procurement, and intelligence. Saudi Arabia is deeply risk-averse and maintains a resilient strategic partnership with India.",
        "data": "India-KSA bilateral trade ($43B) dwarfs Pakistan-KSA trade (~$4B); Saudi Arabia officially avoids bilateral South Asian conflicts.",
        "ex": "Saudi Arabia maintaining strategic neutrality during the 2019 Balakot airstrikes and Article 370 abrogation.",
        "mains": "Crucial distinction preventing alarmist assessments in UPSC GS-2 IR answers."
    },
    {
        "id": "mecca_07",
        "topic": "Mecca Pact",
        "k": "tf",
        "q": "True or False: Turkey currently possesses the second-largest standing military force by active personnel within the NATO alliance.",
        "a": 0,
        "kw": "Turkey's NATO Military Standing",
        "e": "True! Turkey maintains ~4,25,000 active military personnel, making it NATO's second-largest standing army after the United States.",
        "data": "2nd largest in NATO; Defence industrial exports exceeded $10 Billion in 2023-24 (including Bayraktar TB2 and Akinci UAVs).",
        "ex": "Turkish drone exports to over 30 countries across Africa, Central Asia, and Eastern Europe.",
        "mains": "Underlines Turkey's military-industrial leverage in seeking non-Western defense partnerships."
    },
    {
        "id": "mecca_08",
        "topic": "Mecca Pact",
        "k": "tf",
        "q": "True or False: The Indian expatriate diaspora in Saudi Arabia is currently smaller than the Pakistani expatriate diaspora.",
        "a": 1,
        "kw": "Diaspora Primacy in the Gulf",
        "e": "False! With over 2.6 Million non-resident Indians, the Indian community is the single largest expatriate workforce in the Kingdom of Saudi Arabia.",
        "data": "2.6 Million Indians in KSA sending ~$10 Billion in annual remittances back to India.",
        "ex": "Indian healthcare professionals, engineers, and blue-collar workers anchoring critical sectors of the Saudi economy.",
        "mains": "Constitutes a powerful socio-economic cushion protecting India-Saudi ties from geopolitical disruptions."
    },
    {
        "id": "mecca_09",
        "topic": "Mecca Pact",
        "k": "tf",
        "q": "True or False: The Mecca Pact signatories share a contiguous land border, facilitating seamless overland logistics and armor deployment.",
        "a": 1,
        "kw": "Geographical Non-Contiguity",
        "e": "False! Turkey, Saudi Arabia, and Pakistan are separated by thousands of kilometers of non-allied territory (Iran, Iraq, Syria) and complex maritime chokepoints, creating acute operational logistics hurdles.",
        "data": "Over 3,000 km maritime/air distance separates Ankara, Riyadh, and Islamabad.",
        "ex": "Any land transit between Pakistan and Turkey requires transit through Iran, which views the pact with strategic suspicion.",
        "mains": "Physical geography remains a severe natural barrier to conventional military integration."
    },
    {
        "id": "mecca_10",
        "topic": "Mecca Pact",
        "k": "tf",
        "q": "True or False: 'Security Renting' describes a strategy where financially distressed nations leverage military forces and nuclear deterrence to secure economic bailouts from wealthy monarchies.",
        "a": 0,
        "kw": "Concept of Security Renting",
        "e": "True! Scholars use 'Security Renting' to characterize Pakistan's geopolitical posture: offering military deployments, pilot training, and nuclear deterrence signaling to Gulf monarchies in exchange for financial deposits and concessional fuel.",
        "data": "Pakistan stationed over 20,000 troops in Saudi Arabia during the 1980s under bilateral security accords.",
        "ex": "Saudi Arabia depositing $3 Billion in the State Bank of Pakistan to prevent sovereign debt default.",
        "mains": "Core theoretical lens for dissecting Pakistan's persistent transactional alignments."
    },

    # --- Pattern 3: multi (5 questions) ---
    {
        "id": "mecca_11",
        "topic": "Mecca Pact",
        "k": "multi",
        "q": "Tap all verified strategic concepts and doctrines reflected in the formation of the Mecca Trilateral Pact:",
        "o": [
            "Strategic Hedging away from unilateral reliance on Pax Americana",
            "Security Renting by financially distressed militarized regimes",
            "Security Mirroring in response to shifting regional alignments",
            "Complete military absorption of GCC armies under Turkish unified central command"
        ],
        "a": [0, 1, 2],
        "kw": "Geopolitical Conceptual Frameworks",
        "e": "The pact embodies Strategic Hedging, Security Renting, and Security Mirroring. However, GCC states have NOT ceded military sovereignty to Turkey, maintaining independent command structures.",
        "data": "US security umbrella recalibration in the Middle East post-Afghanistan and Ukraine.",
        "ex": "Gulf states procuring Turkish drones and Chinese air defense while retaining US bases (Al Udeid, NSA Bahrain).",
        "mains": "High-scoring academic conceptualization for GS-2 International Relations essays."
    },
    {
        "id": "mecca_12",
        "topic": "Mecca Pact",
        "k": "multi",
        "q": "Tap all core systemic challenges and internal contradictions undermining the operational effectiveness of the Mecca Pact:",
        "o": [
            "Absence of a shared common adversary among the three signatories",
            "Historic rivalry between Saudi Arabia and Turkey for leadership of the Sunni Islamic world",
            "Turkey's macroeconomic distress and Pakistan's severe financial insolvency",
            "India imposing a total naval blockade on the Red Sea and Persian Gulf"
        ],
        "a": [0, 1, 2],
        "kw": "Inherent Structural Contradictions",
        "e": "The pact suffers from lack of a common enemy, ideological leadership friction (Erdogan's neo-Ottomanism vs House of Saud), and severe economic frailty in Ankara and Islamabad. India has NOT blockaded the Gulf.",
        "data": "Turkish inflation >60% (2024); Pakistan debt-to-GDP >75% with recurring IMF bailouts.",
        "ex": "Saudi-Turkey tensions during the 2017 Qatar blockade and Jamal Khashoggi controversy in Istanbul.",
        "mains": "Exposes why the pact is likely to remain largely symbolic and transactional."
    },
    {
        "id": "mecca_13",
        "topic": "Mecca Pact",
        "k": "multi",
        "q": "Tap all direct strategic security implications of the Mecca Pact for India's foreign policy and defense posture:",
        "o": [
            "Potential transfer of advanced Turkish unmanned aerial systems (UAVs) and electronic warfare to Pakistan",
            "Challenge to India's hard-won strategic de-hyphenation between Gulf capitals and Islamabad",
            "Complications in coordinating maritime connectivity corridors like IMEC",
            "Immediate expulsion of all 2.6 Million Indian expatriates from Saudi Arabia"
        ],
        "a": [0, 1, 2],
        "kw": "Strategic Security Matrix for India",
        "e": "The pact threatens tech proliferation to Pakistan, challenges India's de-hyphenated Gulf diplomacy, and complicates IMEC. Saudi Arabia has zero intention of expelling its vital Indian expatriate workforce.",
        "data": "Pakistan utilizing Turkish Bayraktar TB2 and Akinci combat drones along the Western border.",
        "ex": "Turkish diplomatic interference on the Kashmir issue in UN General Assembly debates.",
        "mains": "Structure of India's external threat evaluation in West Asia."
    },
    {
        "id": "mecca_14",
        "topic": "Mecca Pact",
        "k": "multi",
        "q": "Tap all pillars of India's recommended strategic response ('Gulf Balancing') to counter the Mecca Pact:",
        "o": [
            "Deepening bilateral Comprehensive Strategic Partnerships with UAE, Saudi Arabia, and Oman",
            "Leveraging India's $43B energy and trade footprint alongside its massive diaspora presence",
            "Expanding Indian Navy's Mission-Based Deployments (MBD) across the Western Indian Ocean",
            "Unilaterally snapping diplomatic ties with Riyadh and joining the Tehran military alliance"
        ],
        "a": [0, 1, 2],
        "kw": "India's Counter-Strategy Roadmap",
        "e": "India's optimal strategy is proactive multi-alignment: deepening strategic ties with Riyadh, Abu Dhabi, and Muscat, maintaining naval readiness, and leveraging market size. Severing ties with Saudi Arabia would be diplomatic suicide.",
        "data": "Indian Navy anti-piracy and drone-interception deployments in Gulf of Aden (Operation Sankalp).",
        "ex": "Joint naval exercises 'Al-Mohed Al-Hindi' (India-Saudi) and 'Zayed Talwar' (India-UAE).",
        "mains": "Exemplifies India's policy of Strategic Autonomy and Issue-Based Multi-Alignment."
    },
    {
        "id": "mecca_15",
        "topic": "Mecca Pact",
        "k": "multi",
        "q": "Tap all verified geopolitical actors and institutions whose regional positions are directly impacted by the Mecca Pact:",
        "o": [
            "Islamic Republic of Iran (monitoring Sunni military consolidation along its eastern and western flanks)",
            "Gulf Cooperation Council (GCC) whose traditional multilateral primacy is bypassed",
            "State of Israel (monitoring Turkish military-industrial footprint in the Arabian peninsula)",
            "Mercosur (South American Common Market)"
        ],
        "a": [0, 1, 2],
        "kw": "Regional Stakeholder Ramifications",
        "e": "Iran, the GCC, and Israel are intimately affected by a trilateral Sunni alliance. Mercosur (South America) is completely unrelated.",
        "data": "Iran shares borders with both Pakistan (900 km) and Turkey (500 km); Saudi-Iran detente brokered by China in 2023.",
        "ex": "Iranian Foreign Ministry expressing wariness over foreign military presence altering regional security dynamics.",
        "mains": "Demonstrates the complex multi-polar balance of power in contemporary West Asia."
    },

    # --- Pattern 4: flag (5 questions) ---
    {
        "id": "mecca_16",
        "topic": "Mecca Pact",
        "k": "flag",
        "q": "Spot the red flag: which statement regarding Saudi Arabia's defense spending and capabilities is FACTUALLY INCORRECT?",
        "o": [
            "Saudi Arabia operates with an annual defense budget of approximately $83 Billion",
            "Saudi Arabia has developed fully indigenous fifth-generation stealth fighter jet assembly lines in Riyadh",
            "Saudi Arabia remains one of the largest global importers of advanced Western defense hardware",
            "Saudi Arabia's Vision 2030 targets localizing 50% of its military equipment spending by 2030"
        ],
        "a": 1,
        "kw": "Saudi Defense Industrial Reality",
        "e": "Red Flag! Saudi Arabia does NOT have indigenous 5th-gen fighter manufacturing. It remains heavily reliant on imported US F-15s and European Eurofighter Typhoons, which is why it seeks Turkish drone and naval partnerships.",
        "data": "KSA Defense Budget ~$83B; Localization target 50% under GAMI (General Authority for Military Industries).",
        "ex": "Saudi Arabia purchasing Turkish Baykar Akinci drones in a multi-billion dollar deal to jumpstart local assembly.",
        "mains": "Distinguishes between raw petrodollar purchasing power and genuine domestic technological manufacturing."
    },
    {
        "id": "mecca_17",
        "topic": "Mecca Pact",
        "k": "flag",
        "q": "Spot the red flag: which clause in this assessment of Pakistan's role in the Mecca Pact is FALSE?",
        "o": [
            "Pakistan provides conventional infantry manpower and nuclear deterrence prestige to the grouping",
            "Pakistan has stationed over 6,60,000 active military personnel in its standing armed forces",
            "Pakistan's fragile macro-economy forces it into a position of 'security renting' for Gulf capital",
            "Pakistan has formally ceded sovereign command of its strategic nuclear arsenal to the Saudi Royal Court"
        ],
        "a": 3,
        "kw": "Pakistan Nuclear Command Sovereignty",
        "e": "Red Flag! Pakistan has NEVER surrendered sovereign command of its nuclear arsenal to Saudi Arabia. Pakistan's Strategic Plans Division (SPD) maintains strict sovereign custody over its nuclear warheads.",
        "data": "Pakistan army conventional personnel ~6,60,000; ~170 nuclear warheads under National Command Authority (NCA).",
        "ex": "Despite rumors of 'Saudi nuclear financing', Pakistan has consistently maintained operational nuclear independence.",
        "mains": "Prevents unsubstantiated sensationalism in strategic nuclear assessments."
    },
    {
        "id": "mecca_18",
        "topic": "Mecca Pact",
        "k": "flag",
        "q": "Spot the red flag: which statement regarding India-Saudi Arabia bilateral ties is FALSE?",
        "o": [
            "Bilateral merchandise trade between India and Saudi Arabia reached ~$43 Billion in FY 2023-24",
            "Saudi Arabia officially recognizes Pakistan's claim over Kashmir and has severed all defense ties with New Delhi",
            "The Indian and Saudi navies conduct bilateral naval combat exercises titled 'Al-Mohed Al-Hindi'",
            "Saudi Arabia is home to over 2.6 Million Indian expatriates who contribute vital human capital"
        ],
        "a": 1,
        "kw": "India-KSA Strategic De-Hyphenation",
        "e": "Red Flag! Saudi Arabia has NOT severed ties with India nor endorsed Pakistan's maximalist stance. Riyadh views Kashmir as a bilateral issue, upgraded ties to a Strategic Partnership Council with India, and conducts regular joint naval drills.",
        "data": "Crown Prince Mohammed bin Salman state visit to India (September 2023); Bilateral trade $43 Billion.",
        "ex": "Exercise Al-Mohed Al-Hindi conducted off Jubail, showcasing bilateral maritime cooperation.",
        "mains": "Proof that India's Gulf diplomacy has achieved structural resilience against Pakistani diplomatic lobbying."
    },
    {
        "id": "mecca_19",
        "topic": "Mecca Pact",
        "k": "flag",
        "q": "Spot the red flag: which statement regarding Turkey's foreign policy and defense industry is INCORRECT?",
        "o": [
            "Turkey's defense exports exceeded $10 Billion, driven by armed UAVs and naval corvettes",
            "Turkey strongly endorsed the IMEC corridor as its premier European connectivity conduit",
            "Turkey maintains the 2nd largest standing military force within NATO",
            "Turkish foreign policy blends neo-Ottoman regional ambition with strategic autonomy from the West"
        ],
        "a": 1,
        "kw": "Turkish Opposition to IMEC",
        "e": "Red Flag! Turkey vehemently OPPOSES the IMEC corridor because it bypasses Turkish territory. President Erdogan announced: 'There can be no corridor without Turkey', promoting the rival Iraq-Turkey Development Road.",
        "data": "Turkey excluded from G20 IMEC MoU signed by India, USA, Saudi Arabia, UAE, France, Germany, Italy, and EU.",
        "ex": "Turkey pushing the $17 Billion Grand Faw port and rail link through Iraq to access the Persian Gulf.",
        "mains": "Essential geoeconomic nuance for GS-2 trade and connectivity questions."
    },
    {
        "id": "mecca_20",
        "topic": "Mecca Pact",
        "k": "flag",
        "q": "Spot the red flag: which threat perception assessment among the Mecca Pact members is FLAWED?",
        "o": [
            "Saudi Arabia's primary operational focus is containing Iranian ballistic proxies and securing oil assets",
            "Turkey's primary military focus revolves around Kurdish militants (PKK/YPG) and Eastern Mediterranean gas disputes",
            "Pakistan's entire military doctrine and force posture are centered on countering India",
            "All three nations consider the State of Israel to be their sole, identical existential military adversary"
        ],
        "a": 3,
        "kw": "Radical Threat Divergence",
        "e": "Red Flag! The three nations do NOT share Israel as an identical existential threat. Turkey maintains formal diplomatic relations with Israel; Saudi Arabia was actively pursuing normalization via the Abraham Accords; Pakistan refuses to recognize Israel.",
        "data": "Saudi-Israel normalization talks paused post-Oct 7, but security cooperation against Iranian drones persists.",
        "ex": "Turkey conducts billions in commercial trade with Israel while Pakistan bars trade entirely.",
        "mains": "The single most decisive argument proving why the Mecca Pact cannot operate as an integrated collective alliance."
    },

    # --- Pattern 5: riddle (5 questions) ---
    {
        "id": "mecca_21",
        "topic": "Mecca Pact",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a premier defense-industrial export from Turkey that reshaped modern combat in Nagorno-Karabakh, Libya, and Ukraine.",
            "I offer medium-altitude long-endurance (MALE) reconnaissance and strike capability at a fraction of the cost of US MQ-9 Reapers.",
            "My acquisition by Pakistan and Saudi Arabia forms the technological backbone of the Mecca Trilateral alignment. Who am I?"
        ],
        "o": ["Bayraktar TB2 / Akinci UCAV", "Shaheen-III Ballistic Missile", "Eurofighter Typhoon", "Patriot Missile Battery"],
        "a": 0,
        "kw": "Turkish Drone Diplomacy",
        "e": "Bayraktar TB2 and Akinci UCAVs manufactured by Baykar Technologies! Turkey's drone diplomacy serves as the primary currency for forging strategic defense partnerships across the Middle East, Central Asia, and Africa.",
        "data": "Bayraktar TB2 exported to over 30 countries; signed largest defense contract in Turkish history with Saudi Arabia ($3B+).",
        "ex": "Pakistan deploying Bayraktar TB2 and Akinci drones for ISR and precision strike near the Line of Control.",
        "mains": "Exemplifies the revolution in military affairs (RMA) driven by low-cost, high-attrition autonomous systems."
    },
    {
        "id": "mecca_22",
        "topic": "Mecca Pact",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a proposed 4,800 km multi-modal transit corridor linking South Asia to Europe via the Arabian Peninsula.",
            "I was unveiled at the 2023 New Delhi G20 Summit as a green connectivity corridor countering China's Belt and Road.",
            "My trajectory traverses Saudi Arabia and the UAE, but bypasses Turkey, generating severe friction with Ankara. Who am I?"
        ],
        "o": ["India-Middle East-Europe Economic Corridor (IMEC)", "International North-South Transport Corridor (INSTC)", "Chabahar-Zahedan Railway", "Lapis Lazuli Corridor"],
        "a": 0,
        "kw": "IMEC Strategic Route",
        "e": "The India-Middle East-Europe Economic Corridor (IMEC)! Designed to connect India to Europe via ship-to-rail transit across the UAE, Saudi Arabia, Jordan, and Israel.",
        "data": "Expected to cut transit time between India and Europe by 40% and shipping costs by 30%.",
        "ex": "Connecting JNPT and Mundra ports to Jebel Ali and onward via rail to Haifa.",
        "mains": "The centerpiece of India's West Asian geo-economic strategy, vulnerable to regional conflicts."
    },
    {
        "id": "mecca_23",
        "topic": "Mecca Pact",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am a foreign policy doctrine practiced by India to decouple its ties with conflicting regional rivals.",
            "Through me, India built deep strategic ties with Israel, Saudi Arabia, UAE, and Iran simultaneously without picking sides.",
            "The Mecca Pact threatens to re-link Pakistan to Gulf security, challenging my decades-long success. Who am I?"
        ],
        "o": ["Strategic De-Hyphenation", "Gujral Doctrine", "Panchsheel", "Non-Alignment 2.0"],
        "a": 0,
        "kw": "Strategic De-Hyphenation Doctrine",
        "e": "Strategic De-Hyphenation! Under this doctrine, India treats relationships with rival powers (Israel vs Arab states; Saudi Arabia vs Iran; Gulf vs Pakistan) on their independent bilateral merits.",
        "data": "PM Modi visited Israel in 2017 and Palestine in 2018 in distinct standalone visits, cementing de-hyphenation.",
        "ex": "Simultaneously procuring oil from Saudi Arabia and gas from Qatar while developing Chabahar Port in Iran.",
        "mains": "The foundational triumph of modern Indian diplomacy in West Asia."
    },
    {
        "id": "mecca_24",
        "topic": "Mecca Pact",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am an Indian Navy operational operational deployment philosophy introduced in 2017.",
            "I maintain round-the-clock presence of mission-ready warships at key maritime choke-points across the Indian Ocean.",
            "I secure the Persian Gulf, Gulf of Oman, and Gulf of Aden against piracy, drone strikes, and adversarial naval maneuvers. Who am I?"
        ],
        "o": ["Mission-Based Deployments (MBD)", "Operation Raahat", "Project Seabird", "Indo-Pacific Oceans Initiative (IPOI)"],
        "a": 0,
        "kw": "Mission-Based Naval Deployments (MBD)",
        "e": "Mission-Based Deployments (MBD)! Under MBD, the Indian Navy deploys 12–15 frontline warships 24/7/365 across critical entry/exit points from the Malacca Strait to the Bab-el-Mandeb and Strait of Hormuz.",
        "data": "Operation Sankalp initiated in June 2019 to escort Indian-flagged oil tankers through the Persian Gulf.",
        "ex": "INS Kolkata and INS Visakhapatnam rescuing crew and extinguishing fires on merchant ships struck by Houthi drones.",
        "mains": "Positions India as the 'Preferred Security Partner' and First Responder in the Western Indian Ocean."
    },
    {
        "id": "mecca_25",
        "topic": "Mecca Pact",
        "k": "riddle",
        "q": "Detective: who am I? (Fewer clues, more XP)",
        "c": [
            "I am an ancient theological and political concept revived in modern international relations.",
            "I describe alliances formed on the basis of shared sectarian identity across Sunni Muslim states.",
            "I am invoked in the Mecca Pact to bridge Arab monarchy, Turkish secular-Islamist democracy, and Pakistani military rule. Who am I?"
        ],
        "o": ["Sunni Solidarity", "Pan-Arabism", "Wahhabism", "Baathism"],
        "a": 0,
        "kw": "Sunni Solidarity Alignment",
        "e": "Sunni Solidarity! Invoked as an ideological banner to project Islamic unity, though historically it routinely gives way to realpolitik, secular national interests, and regime survival.",
        "data": "OIC (57 member states) frequently crippled by intra-Sunni rivalries (e.g. Qatar vs Quartet, Turkey vs Egypt).",
        "ex": "Saudi Arabia aligning with Israel against Shia Iran despite ideological differences.",
        "mains": "Demonstrates the tension between religious solidarity rhetoric and hard-nosed geostrategic interest."
    },

    # --- Pattern 6: match (5 questions) ---
    {
        "id": "mecca_26",
        "topic": "Mecca Pact",
        "k": "match",
        "q": "Match each Mecca Pact signatory to its primary national strategic asset contributed to the alliance:",
        "p": [
            ["Saudi Arabia", "Petrodollar financing & critical energy assets"],
            ["Pakistan", "Conventional troop manpower & nuclear threshold"],
            ["Turkey", "Advanced aerospace/UAV industrial base"],
            ["India's Lever", "2.6M diaspora & $43B bilateral trade"]
        ],
        "kw": "Signatory Asset Matrix",
        "e": "Saudi Arabia brings massive fiscal liquidity; Pakistan contributes battle-tested manpower and nuclear capability; Turkey provides indigenous drone/naval defense tech; India counters via economic and diaspora leverage.",
        "data": "KSA ($83B budget) + Pakistan (6.6L troops) + Turkey ($10B defense exports) vs India ($43B trade).",
        "ex": "Pairing Saudi capital with Turkish drone R&D and Pakistani military pilots.",
        "mains": "Core analytical breakdown of the trilateral balance of contributions."
    },
    {
        "id": "mecca_27",
        "topic": "Mecca Pact",
        "k": "match",
        "q": "Match the defense expert or diplomat to their central observation on the Mecca Pact:",
        "p": [
            ["Stanly Johny", "Pan-Islamic groupings fracture under national interest divergence"],
            ["Dr. Swasti Rao", "Turkey uses defense exports to contest regional leadership"],
            ["Lt. Gen. Rahul Singh", "Geographic non-contiguity impairs joint combat synergy"],
            ["Dr. Rayed Krimly", "Saudi partnerships are non-exclusionary and de-escalatory"]
        ],
        "kw": "Expert Analytical Perspectives",
        "e": "Stanly Johny focuses on ideological limits; Swasti Rao highlights Turkish industrial ambition; Rahul Singh diagnoses military logistics gaps; Rayed Krimly provides the official Saudi diplomatic reassurance.",
        "data": "Compiled from MP-IDSA security briefs, The Hindu strategic analyses, and KSA foreign ministry releases.",
        "ex": "Citing Lt. Gen. Rahul Singh on the logistical impossibility of joint rapid armor deployment across 3,000 km.",
        "mains": "Elevates Mains answers from generic commentary to scholarly, attributed analysis."
    },
    {
        "id": "mecca_28",
        "topic": "Mecca Pact",
        "k": "match",
        "q": "Match the international connectivity initiative to its strategic geopolitical alignment:",
        "p": [
            ["IMEC", "India-UAE-Saudi-Jordan-Israel-Europe corridor"],
            ["Iraq Development Road", "Turkey-backed alternative linking Basra to Europe"],
            ["CPEC", "China-Pakistan transit link ending at Gwadar"],
            ["INSTC", "India-Iran-Russia multimodal freight corridor"]
        ],
        "kw": "Corridor Rivalry Geopolitics",
        "e": "IMEC bypasses Turkey; Development Road is Turkey's counter-initiative; CPEC cements Sino-Pak axis; INSTC links India to Eurasia via Iran.",
        "data": "Global trade infrastructure competition involving hundreds of billions of dollars.",
        "ex": "Turkey actively lobbying Gulf capitals to fund the Development Road rail link rather than IMEC.",
        "mains": "Mastery of West Asian connectivity corridors for GS-2 and GS-3."
    },
    {
        "id": "mecca_29",
        "topic": "Mecca Pact",
        "k": "match",
        "q": "Match the strategic concept to its exact international relations definition:",
        "p": [
            ["Strategic Hedging", "Diversifying security ties to avoid superpower dependence"],
            ["Security Renting", "Trading military utility for foreign financial bailouts"],
            ["Strategic De-Hyphenation", "Treating rival states on standalone bilateral merits"],
            ["Mission-Based Deployment", "Continuous naval presence at strategic choke points"]
        ],
        "kw": "IR Concept Definitions",
        "e": "Precision definitions: Hedging prevents over-dependence; Renting trades security for cash; De-hyphenation decouples rivalries; MBD maintains continuous maritime vigil.",
        "data": "Foundational theoretical concepts for UPSC GS-2 International Relations.",
        "ex": "India practicing de-hyphenation between Riyadh and Tehran while deploying MBD in Gulf of Aden.",
        "mains": "Demonstrates mastery of professional geopolitical vocabulary."
    },
    {
        "id": "mecca_30",
        "topic": "Mecca Pact",
        "k": "match",
        "q": "Match each regional nation to its primary security friction with Mecca Pact members:",
        "p": [
            ["Iran", "Suspicious of Sunni military encirclement on borders"],
            ["India", "Concerned over Turkish tech proliferation to Pakistan"],
            ["Greece / Cyprus", "Threatened by expanding Turkish naval power (Mavi Vatan)"],
            ["Israel", "Monitors Turkish Islamist rhetoric and missile transfers"]
        ],
        "kw": "Regional Threat Perceptions",
        "e": "Iran fears Sunni encirclement; India fears tech transfers to Rawalpindi; Greece counters Turkish naval expansion in Eastern Med; Israel monitors Turkish hostility.",
        "data": "Demonstrates how a single trilateral pact triggers ripple effects across 4 distinct geopolitical theaters.",
        "ex": "India, Greece, and UAE deepening trilateral air exercises (Iniochos) to counterbalance Turkey-Pak axis.",
        "mains": "Connects West Asian dynamics with Mediterranean and South Asian security."
    },

    # --- Pattern 7: order (5 questions) ---
    {
        "id": "mecca_31",
        "topic": "Mecca Pact",
        "k": "order",
        "q": "Order the logical sequence of events explaining the genesis of the Mecca Defence Pact:",
        "o": [
            "Perceived US retrenchment & shift from Pax Americana",
            "Heightened drone/missile attacks on Gulf oil infrastructure",
            "Saudi Arabia initiates strategic hedging & defense diversification",
            "Turkey seeks export markets for its expanding UAV defense industry",
            "Signing of the Trilateral Joint Defence Agreement in Mecca"
        ],
        "kw": "Mecca Pact Chronological Causality",
        "e": "US security retreat -> Gulf infrastructure attacks (Abqaiq 2019) -> Saudi hedging -> Turkish defense sales push -> Formalization of Trilateral Agreement in Mecca.",
        "data": "Traces the structural evolution of West Asian defense from 2019 to 2024.",
        "ex": "From US hesitation to retaliate for Abqaiq to Riyadh seeking Turkish Bayraktar drones.",
        "mains": "Provides a flawless chronological narrative for 15-marker GS-2 answers."
    },
    {
        "id": "mecca_32",
        "topic": "Mecca Pact",
        "k": "order",
        "q": "Order the geographic checkpoints of the IMEC corridor from South Asia to Europe:",
        "o": [
            "Indian West Coast Ports (JNPT / Mundra)",
            "UAE Maritime Gateway (Jebel Ali / Fujairah)",
            "Saudi Arabian Trans-Desert Rail Network (Al Ghuwaifat to Al Haditha)",
            "Israeli Mediterranean Port (Haifa)",
            "European Destination Ports (Piraeus / Marseille)"
        ],
        "kw": "IMEC Geographic Transit Route",
        "e": "Mundra/JNPT -> Arabian Sea voyage -> Jebel Ali -> Saudi rail line -> Haifa port -> Mediterranean crossing -> European mainland.",
        "data": "Bypasses both the Suez Canal and Turkish landmass, reducing transit time by 40%.",
        "ex": "Goods moving seamlessly under unified digital TIR carnet from Gujarat to Greece.",
        "mains": "Essential spatial knowledge for map-based and connectivity questions."
    },
    {
        "id": "mecca_33",
        "topic": "Mecca Pact",
        "k": "order",
        "q": "Order India's 5-step diplomatic and security escalation ladder to counter adverse fallout from the Mecca Pact:",
        "o": [
            "Engage Riyadh diplomatically citing $43B trade and energy interdependence",
            "Expand naval Mission-Based Deployments across Gulf of Aden and Arabian Sea",
            "Fast-track indigenous defense production (Aatmanirbharta in counter-drone tech)",
            "Deepen strategic quadrilateral cooperation via I2U2 and Mediterranean partners (Greece/Cyprus)",
            "Consolidate IMEC corridor infrastructure with UAE and European allies"
        ],
        "kw": "India's Escalation Counter-Ladder",
        "e": "Diplomatic engagement -> Naval vigil -> Domestic tech readiness -> Plurilateral balancing (I2U2/Greece) -> Geo-economic corridor consolidation.",
        "data": "Synthesizes diplomatic, military, industrial, and multilateral levers.",
        "ex": "Deploying indigenous counter-drone systems along Western borders while conducting joint naval drills with UAE.",
        "mains": "Structure of a comprehensive policy blueprint in UPSC Mains."
    },
    {
        "id": "mecca_34",
        "topic": "Mecca Pact",
        "k": "order",
        "q": "Order the primary military contributors to the Mecca Pact by the size of their annual defense budget (highest to lowest):",
        "o": [
            "Saudi Arabia (~$83 Billion)",
            "Turkey (~$16–$20 Billion)",
            "Pakistan (~$7–$8 Billion)"
        ],
        "kw": "Defense Budget Hierarchy",
        "e": "Saudi Arabia ($83B) dwarfs Turkey ($16-20B) and Pakistan ($7-8B). Saudi Arabia provides the overwhelming financial capital of the grouping.",
        "data": "KSA spends over 10x Pakistan's defense budget, proving Pakistan is the dependent recipient rather than equal partner.",
        "ex": "Saudi Arabia financing multi-billion dollar procurements of Turkish military hardware.",
        "mains": "Reveals the stark economic asymmetry at the core of the alliance."
    },
    {
        "id": "mecca_35",
        "topic": "Mecca Pact",
        "k": "order",
        "q": "Order the optimal structure for a 15-mark UPSC answer on: 'The Mecca Trilateral Pact and its Strategic Implications for India':",
        "o": [
            "Intro: Context of Mecca Pact + Concept of Strategic Hedging",
            "Driver Matrix: Saudi oil defense, Pak survival, Turkey defense exports",
            "Implications for India: Conflict matrix, IMEC friction, de-hyphenation risk",
            "Counter-Arguments: Saudi risk aversion, threat divergence, resilient India-KSA ties",
            "Way Forward: Gulf Balancing, Naval MBD, I2U2, and Conclusion"
        ],
        "kw": "15-Marker Answer Architecture",
        "e": "Context -> National Drivers -> Threat Evaluation for India -> Ground Reality Checks -> Strategic Recommendations -> Visionary Conclusion.",
        "data": "Standardized topper structure maximizing marks across all 4 evaluation dimensions.",
        "ex": "Balancing threat realism with diplomatic optimism.",
        "mains": "Guarantees a top-percentile score in GS-2 International Relations."
    },

    # --- Pattern 8: sort (5 questions) ---
    {
        "id": "mecca_36",
        "topic": "Mecca Pact",
        "k": "sort",
        "q": "Sort each national attribute into its correct country: Saudi Arabia, Pakistan, or Turkey:",
        "it": [
            ["$83 Billion defense budget", 0],
            ["Second largest standing army in NATO", 2],
            ["Declared nuclear weapon state with 6.6L troops", 1],
            ["Vision 2030 economic transformation", 0],
            ["Manufacturer of Bayraktar and Akinci drones", 2],
            ["Chronic balance of payments crisis and IMF reliance", 1]
        ],
        "b": ["Saudi Arabia", "Pakistan", "Turkey"],
        "kw": "Tri-Nation Capability Matrix",
        "e": "Saudi Arabia = Petrodollar scale & Vision 2030; Pakistan = Nuclear power & economic frailty; Turkey = NATO army & drone manufacturing.",
        "data": "Clear operational division of labor among the three signatories.",
        "ex": "Turkish aerospace tech funded by Saudi oil capital deployed by Pakistani operators.",
        "mains": "Crucial matrix for understanding the complementary components of the pact."
    },
    {
        "id": "mecca_37",
        "topic": "Mecca Pact",
        "k": "sort",
        "q": "Sort each strategic factor as either a 'Pact Unifier' (driving cohesion) or a 'Pact Divider' (causing internal friction):",
        "it": [
            ["Disenchantment with US security guarantees", 0],
            ["Saudi-Turkey contest for leadership of Sunni Islam", 1],
            ["Radically divergent threat perceptions (Iran vs India vs Kurds)", 1],
            ["Desire for autonomous regional defense hedging", 0],
            ["Vast geographic distance and non-contiguous borders", 1],
            ["Complementarity between Saudi cash and Turkish defense tech", 0]
        ],
        "b": ["Pact Unifier", "Pact Divider"],
        "kw": "Centripetal vs Centrifugal Forces",
        "e": "Unifiers: US withdrawal, defense hedging, capital-tech complementarity. Dividers: Ideological leadership contests, divergent foes, geographical separation.",
        "data": "Centrifugal forces far outweigh centripetal cohesion in long-term military alliances.",
        "ex": "Riyadh unwilling to risk its economic ties with India or detente with Iran for Pakistani border disputes.",
        "mains": "Dialectical framework for analyzing international defense treaties."
    },
    {
        "id": "mecca_38",
        "topic": "Mecca Pact",
        "k": "sort",
        "q": "Sort each regional actor into its geopolitical stance toward the Mecca Pact: 'Supportive / Participant' vs 'Suspicious / Opposed':",
        "it": [
            ["Kingdom of Saudi Arabia", 0],
            ["Islamic Republic of Iran", 1],
            ["Republic of Turkey", 0],
            ["State of Israel", 1],
            ["Islamic Republic of Pakistan", 0],
            ["Republic of Cyprus and Greece", 1]
        ],
        "b": ["Supportive / Participant", "Suspicious / Opposed"],
        "kw": "Regional Alignment Polarisation",
        "e": "Participants: KSA, Pakistan, Turkey. Opposed/Suspicious: Iran (fears Sunni encircling), Israel (monitors Turkish weapons), Greece/Cyprus (counters Turkish naval power).",
        "data": "Demonstrates the external balancing reactions triggered by minilateral pacts.",
        "ex": "Greece and UAE conducting joint air maneuvers in response to Turkish regional posturing.",
        "mains": "Essential balance of power mapping for West Asia."
    },
    {
        "id": "mecca_39",
        "topic": "Mecca Pact",
        "k": "sort",
        "q": "Sort these connectivity routes as 'IMEC Aligned' vs 'IMEC Rival / Bypassing':",
        "it": [
            ["Mundra to Jebel Ali maritime leg", 0],
            ["Iraq-Turkey Development Road from Basra to Europe", 1],
            ["Saudi trans-desert rail from Al Ghuwaifat to Al Haditha", 0],
            ["CPEC corridor terminating at Gwadar port", 1],
            ["Haifa port to Piraeus maritime connection", 0],
            ["International North-South Transport Corridor via Bandar Abbas", 1]
        ],
        "b": ["IMEC Aligned", "IMEC Rival / Bypassing"],
        "kw": "Connectivity Architecture Classification",
        "e": "IMEC includes India-UAE-Saudi-Israel-Europe. Rivals/alternatives include Turkish Development Road, CPEC, and INSTC.",
        "data": "Global geoeconomic competition over the shortest multimodal trade routes between Asia and Europe.",
        "ex": "Turkey building alternative logistics nodes to prevent marginalization by IMEC.",
        "mains": "Classifies transit corridors for GS-2 trade and connectivity."
    },
    {
        "id": "mecca_40",
        "topic": "Mecca Pact",
        "k": "sort",
        "q": "Sort each diplomatic lever available to India as an 'Economic/Energy Lever' or a 'Security/Defense Lever':",
        "it": [
            ["$43 Billion annual trade with Saudi Arabia", 0],
            ["Mission-Based Naval Deployments in Gulf of Oman and Bab-el-Mandeb", 1],
            ["14% of crude oil import market sourced from KSA", 0],
            ["Joint naval combat exercise 'Al-Mohed Al-Hindi'", 1],
            ["2.6 Million Indian expatriates sending remittances", 0],
            ["I2U2 security and food corridor collaboration", 1]
        ],
        "b": ["Economic / Energy Lever", "Security / Defense Lever"],
        "kw": "India's Foreign Policy Tool Classification",
        "e": "Economic levers: Trade volume, crude purchases, diaspora remittances. Security levers: Naval deployments, joint exercises, plurilateral frameworks (I2U2).",
        "data": "India balances hard naval power with soft economic and diaspora diplomacy.",
        "ex": "Using crude purchase flexibility to maintain high strategic attention from Gulf monarchs.",
        "mains": "Structure of India's multi-dimensional diplomatic toolkit."
    },

    # --- Pattern 9: year (5 questions) ---
    {
        "id": "mecca_41",
        "topic": "Mecca Pact",
        "k": "year",
        "q": "Slide to the year the historic India-Middle East-Europe Economic Corridor (IMEC) was officially unveiled at the New Delhi G20 Summit:",
        "min": 2018,
        "max": 2026,
        "a": 2023,
        "tol": 0,
        "kw": "IMEC Launch Milestone",
        "e": "IMEC was officially announced in September 2023 on the sidelines of the G20 Leaders' Summit in New Delhi by leaders of India, USA, Saudi Arabia, UAE, France, Germany, Italy, and EU.",
        "data": "MoU signed on 9 September 2023 in New Delhi.",
        "ex": "Prime Minister Modi and Crown Prince Mohammed bin Salman co-chairing the announcement.",
        "mains": "Crucial timeline anchor for contemporary Indian geoeconomics."
    },
    {
        "id": "mecca_42",
        "topic": "Mecca Pact",
        "k": "year",
        "q": "Slide to the year catastrophic drone and cruise missile strikes struck Saudi Aramco's processing facilities at Abqaiq and Khurais, triggering the Kingdom's search for multi-layered air defense hedging:",
        "min": 2015,
        "max": 2025,
        "a": 2019,
        "tol": 0,
        "kw": "Abqaiq-Khurais Drone Attack",
        "e": "On 14 September 2019, coordinated drone and missile strikes hit Aramco facilities at Abqaiq and Khurais, temporarily knocking out 5.7 million barrels per day (50% of Saudi oil output). US failure to launch military retaliation convinced Riyadh to diversify defense alliances.",
        "data": "Knocked out ~5% of global daily oil supply in a single morning.",
        "ex": "Exposed the vulnerability of conventional US Patriot missile batteries against low-flying swarming drones.",
        "mains": "The catalytic turning point marking the breakdown of the 1945 Quincy Pact ('Oil for Security')."
    },
    {
        "id": "mecca_43",
        "topic": "Mecca Pact",
        "k": "year",
        "q": "Slide to the year the Indian Navy formally launched 'Operation Sankalp' to escort Indian-flagged tankers through the Persian Gulf and Gulf of Oman following maritime tanker attacks:",
        "min": 2015,
        "max": 2025,
        "a": 2019,
        "tol": 0,
        "kw": "Operation Sankalp Genesis",
        "e": "Operation Sankalp was launched on 19 June 2019 by the Indian Navy following explosions on tankers in the Gulf of Oman, ensuring continuous warship protection for Indian merchant shipping.",
        "data": "Continuous naval deployment escorting over hundreds of Indian-flagged oil tankers through Hormuz.",
        "ex": "Deploying stealth frigates and P-8I maritime surveillance aircraft out of INS Hansa.",
        "mains": "Concrete proof of India acting as a net maritime security provider."
    },
    {
        "id": "mecca_44",
        "topic": "Mecca Pact",
        "k": "year",
        "q": "Slide to the year China brokered the landmark diplomatic normalization agreement between the Kingdom of Saudi Arabia and the Islamic Republic of Iran:",
        "min": 2018,
        "max": 2026,
        "a": 2023,
        "tol": 0,
        "kw": "Beijing-Brokered Saudi-Iran Normalization",
        "e": "In March 2023, Saudi Arabia and Iran signed a historic normalization pact in Beijing, agreeing to reopen embassies and reactivate security pacts after a 7-year diplomatic freeze.",
        "data": "Signed on 10 March 2023; marked China's emergence as a premier geopolitical mediator in West Asia.",
        "ex": "Riyadh and Tehran exchanging ambassadors and initiating ministerial visits.",
        "mains": "Explains why Saudi Arabia is deeply reluctant to turn the Mecca Pact into an anti-Iran military front."
    },
    {
        "id": "mecca_45",
        "topic": "Mecca Pact",
        "k": "year",
        "q": "Slide to the year the inaugural edition of the bilateral India-Saudi Arabia naval combat exercise 'Al-Mohed Al-Hindi' was conducted off the coast of Al Jubail:",
        "min": 2017,
        "max": 2025,
        "a": 2021,
        "tol": 0,
        "kw": "Exercise Al-Mohed Al-Hindi Inauguration",
        "e": "The maiden edition of Exercise 'Al-Mohed Al-Hindi' took place in August 2021 off Jubail, marking the first-ever joint naval combat exercise between the Indian Navy and the Royal Saudi Naval Forces.",
        "data": "Guided missile destroyer INS Kochi participated; expanded into larger complex multi-domain drills in 2023.",
        "ex": "Tactical drills, helicopter cross-deck landings, and anti-piracy simulations.",
        "mains": "Historic milestone evidencing the tangible security deepening between India and the Gulf monarchies."
    },

    # --- Pattern 11: flip (5 questions) ---
    {
        "id": "mecca_46",
        "topic": "Mecca Pact",
        "k": "flip",
        "q": "Draft a model 25-word opening hook for a UPSC Mains GS-2 answer on: 'The Mecca Trilateral Pact: Emerging Strategic Architecture and Challenges for India'.",
        "r": "Synthesizing Arab petrodollars, Turkish drone technology, and Pakistani manpower, the Mecca Defence Pact marks West Asia's transition toward multi-aligned hedging post-Pax Americana. However, deep structural contradictions and resilient India-Gulf economic anchors mitigate existential threats to New Delhi.",
        "kw": "Mecca Pact Opening Hook Formula",
        "e": "This opening hook combines the 3 national assets (cash, tech, manpower), systemic context (post-Pax Americana hedging), structural reality (divergences), and India's position in under 40 words.",
        "data": "Covers actors, doctrine, limitations, and Indian strategic takeaway.",
        "ex": "Sets an authoritative, non-sensationalist, policy-grade tone from the very first sentence.",
        "mains": "Memorize and adapt for any GS-2 West Asian defense alignment question."
    },
    {
        "id": "mecca_47",
        "topic": "Mecca Pact",
        "k": "flip",
        "q": "Flip to reveal the 4-box conceptual diagram summarizing the 'Internal Contradictions of the Mecca Pact':",
        "r": "1. STRUCTURAL: Absence of common enemy (Iran vs India vs Kurds) & geographical non-contiguity.\n2. IDEOLOGICAL: Saudi-Turkey rivalry for Sunni primacy & divergent civil-military cultures.\n3. FINANCIAL: Turkey's runaway inflation + Pakistan's debt insolvency vs Saudi fiscal load.\n4. REGIONAL: Proxy clashes in Syria/Libya/Yemen & destabilizing the Saudi-Iran detente.",
        "kw": "4-Box Internal Contradictions Diagram",
        "e": "Memorize the 4-box typology: Structural, Ideological, Financial, Regional. Drawing this box in Mains answers guarantees 1.5 to 2 extra marks.",
        "data": "Structural / Ideological / Financial / Regional taxonomy.",
        "ex": "Visual organizer breaking down why pan-Islamic alliances historically fail to achieve NATO-style collective defense.",
        "mains": "Ideal visual template for 10-marker and 15-marker GS-2 answers."
    },
    {
        "id": "mecca_48",
        "topic": "Mecca Pact",
        "k": "flip",
        "q": "Flip to reveal how India can strategically leverage its 'Diaspora and Trade Footprint' to neutralize adverse fallout from the Mecca Pact:",
        "r": "With 2.6 Million Indian expatriates in Saudi Arabia generating critical workforce stability and $43 Billion in bilateral merchandise trade, India is an irreplaceable partner for Saudi Vision 2030. India can leverage its position as one of the world's largest crude consumers to ensure Riyadh maintains strict bilateral neutrality and safeguards Indian maritime corridors.",
        "kw": "Diaspora & Economic Leverage Doctrine",
        "e": "India's real leverage is geo-economic: Saudi Arabia cannot jeopardize its single largest expat workforce or its massive, growing crude buyer for marginal military alignments with Islamabad.",
        "data": "2.6M diaspora; $43B trade; 14% crude oil anchor.",
        "ex": "Bilateral Strategic Partnership Council established at the head-of-government level.",
        "mains": "Demonstrates sophisticated understanding of geo-economics over crude military balance."
    },
    {
        "id": "mecca_49",
        "topic": "Mecca Pact",
        "k": "flip",
        "q": "Flip to reveal the analytical critique explaining why the Mecca Pact is unlikely to alter the conventional military balance along the India-Pakistan border:",
        "r": "1. Non-Transferable Deterrence: Saudi Arabia will not commit forces against India.\n2. Technology Absorption Lag: Turkish drones require complex sensor integration and are vulnerable to India's multi-layered S-400 and MRSAM air defense.\n3. Financial Squeeze: Pakistan lacks foreign exchange to procure Turkish systems at scale without Saudi grants, which are capped by Riyadh's risk aversion.\n4. Strategic Vigil: India's Western Command maintains decisive conventional air and armored superiority.",
        "kw": "Military Balance Reality Check",
        "e": "Addresses four hard military filters: foreign policy reluctance, integrated air defense counters (S-400), economic insolvency, and Indian conventional superiority.",
        "data": "India's defense budget ($74B) is ~10x Pakistan's ($7.5B); S-400 Triumf deployed in Western sector.",
        "ex": "Turkish TB2 drones suffering heavy attrition against integrated air defense systems in Ukraine and Libya.",
        "mains": "Dismantles alarmist military narratives with rigorous operational facts."
    },
    {
        "id": "mecca_50",
        "topic": "Mecca Pact",
        "k": "flip",
        "q": "Flip to reveal the statesmanlike concluding paragraph for an essay on: 'India's Navigating of Changing Geopolitical Currents in West Asia':",
        "r": "West Asia's evolving security architecture demands that India transition from defensive de-hyphenation to proactive, value-additive multi-alignment. By anchoring its partnerships in energy transition, maritime security, digital public infrastructure, and corridor connectivity like IMEC, India can ensure that emerging regional minilaterals complement, rather than compromise, its vital national interests.",
        "kw": "Visionary Concluding Synthesis",
        "e": "A balanced, statesmanlike conclusion emphasizing proactive diplomacy, DPI, maritime security, and strategic autonomy.",
        "data": "Synthesizes energy, security, diaspora, and digital corridors.",
        "ex": "Positions India as a constructive, indispensable anchor of stability in the extended neighborhood.",
        "mains": "Flawless closing for UPSC Mains GS-2 and Essay papers."
    }
]

print(f"Mecca questions prepared: {len(mecca_questions)}")
