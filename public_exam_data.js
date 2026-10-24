/**
 * CORTEX DUOLINGO LEARNING MODEL - PUBLIC EXAMINATIONS
 * Topic: Public Examinations (Prevention of Unfair Means) Act, NTA Reforms & Exam Integrity
 * Sourced directly from CAVA Lecture 4 Audio Transcript
 */

const PUBLIC_EXAM_DATA = {
  id: "public-examinations",
  title: "Public Examinations & NTA Governance Reforms",
  syllabusTags: ["GS-2: Governance & Statutory Bodies", "GS-2: Social Justice & Education", "CAVA Lecture 4"],
  stats: {
    totalLevels: 10,
    totalXP: 250,
    estimatedMinutes: 25
  },

  // 1. FORUMIAS SHEET NOTES FORMAT (From Lecture 4 Transcript)
  sheetNotes: {
    sheetCode: "CA - 260815",
    title: "PUBLIC EXAMINATIONS & NTA REFORMS",
    sections: [
      {
        tag: "INTRO",
        bullets: [
          {
            text: "Public exams are the primary engine for upward social mobility in India",
            detail: "Enables rural, underprivileged youth to break generational poverty through merit-based recruitment."
          },
          {
            text: "Chhattisgarh High Court Dictum: 'Paper leak is more heinous than murder'",
            detail: "Murder kills one person; a paper leak murders the dreams, trust, and future of millions of youth."
          },
          {
            text: "Scale of Crisis: Over 250+ exams conducted by NTA since 2018; multiple high-stakes breaches (NEET-UG, UGC-NET)",
            detail: "Organized paper leak syndicates charging between ₹30 lakh to ₹50 lakh per leaked seat (EOU Bihar findings)."
          }
        ]
      },
      {
        tag: "CONTEXT",
        bullets: [
          {
            text: "Enactment of Public Examinations (Prevention of Unfair Means) Act 2024 & 2026 Amendments",
            detail: "Legislative intervention to create deterrent criminal penalties for paper leak syndicates."
          },
          {
            text: "Formation of High-Level 7-Member K. Radhakrishnan Committee",
            detail: "Constituted by Union Education Ministry to recommend structural reforms in NTA, digital security, and testing methods."
          }
        ]
      },
      {
        tag: "CONSTITUTIONAL CANVAS",
        bullets: [
          {
            text: "42nd Amendment Act (1976): Education in Concurrent List (Entry 25)",
            detail: "Both Center and States share constitutional obligations to maintain examination standards."
          },
          {
            text: "Article 14 & 16: Equality of Opportunity in Public Employment",
            detail: "Compromised exams violate meritocracy and substantive equality guaranteed to honest aspirants."
          },
          {
            text: "Article 21A & DPSP (Art 45, 46): Protection of weaker sections' educational interests",
            detail: "Paper leaks disproportionately exclude students unable to afford ₹30-50L leaked question papers."
          }
        ]
      },
      {
        type: "PROS_CONS",
        prosTag: "2024 & 2026 ACT STRENGTHS",
        consTag: "SYSTEMIC DEFICITS & CRITICISM",
        pros: [
          {
            text: "Severe Criminal Deterrence",
            detail: "7 to 10 years imprisonment for organized syndicates and minimum ₹1 crore fine with property attachment."
          },
          {
            text: "Student Immunity",
            detail: "Bona fide candidates protected from criminalization; focus exclusively on commercial cheating syndicates."
          },
          {
            text: "Special Fast-Track Courts",
            detail: "Time-bound trials to ensure high conviction rates and swift punishment."
          },
          {
            text: "Non-Bailable & Cognizable",
            detail: "Empowers police and central agencies (CBI) to arrest without warrant and seize illicit assets."
          }
        ],
        cons: [
          {
            text: "Ex-Post Deterrence Fallacy",
            detail: "Harsher punishment fails without high detection probability (Becker's Economics of Crime)."
          },
          {
            text: "NTA 24-Staff Paradox",
            detail: "NTA operates with only 24 permanent employees; heavy reliance on unverified private contractors."
          },
          {
            text: "Single-Day High-Stakes Pressure",
            detail: "One-shot annual exams create intense leak incentives and severe adolescent mental health distress."
          },
          {
            text: "Coaching Center Nexus",
            detail: "Justice A.K. Rajan Committee: Centralized high-stakes exams foster an exploitative ₹30,000 Cr coaching industry."
          }
        ]
      },
      {
        tag: "RADHAKRISHNAN COMMITTEE RECOMMENDATIONS",
        bullets: [
          {
            text: "Statutory Autonomy for NTA",
            detail: "Transform NTA from a registered society into a statutory body with permanent cadre and parliamentary oversight."
          },
          {
            text: "Two-Stage Multi-Attempt Testing",
            detail: "Shift from single-day high-stakes exams to Screening Prelims + Proctored Mains, with multiple testing sessions."
          },
          {
            text: "Hybrid Exam Delivery & Digital Lockers",
            detail: "Encrypted digital question transmission just minutes before exam; answers recorded at accredited government institutions."
          },
          {
            text: "Accredited Government Centers Only",
            detail: "Bar private commercial cyber centers; utilize only Kendriya Vidyalayas, Navodayas, and State universities."
          }
        ]
      },
      {
        tag: "GLOBAL BEST PRACTICES",
        bullets: [
          {
            text: "China (Gaokao Model)",
            detail: "Military armed escort for exam papers, facial recognition drone patrols, radio-wave jammers, and 7-year penal sentences."
          },
          {
            text: "UK & US Testing (SAT / A-Levels)",
            detail: "Continuous school assessment weighting, multiple annual attempts, and randomized adaptive item banks."
          }
        ]
      },
      {
        type: "BOTTOM_GRID",
        suggestionsTag: "WAY FORWARD",
        conclusionTag: "CONCLUSION",
        suggestions: [
          {
            text: "Full Radhakrishnan Implementation",
            detail: "Statutory NTA, hybrid digital lockboxes, and accredited government exam centers."
          },
          {
            text: "Dynamic Algorithmic Question Banks",
            detail: "No single printed paper to leak; algorithm synthesizes questions dynamically."
          }
        ],
        conclusion: [
          {
            text: "Restoring Meritocracy",
            detail: "\"Safeguarding public examinations is not merely an administrative duty, but a sacred covenant protecting the constitutional trust of millions of youth.\""
          }
        ]
      }
    ]
  },

  // 2. DUOLINGO LEVEL-WISE LEARNING ROADMAP
  levels: [
    {
      id: "lvl-1",
      unit: "Unit 1: The Crisis & Constitutional Canvas",
      unitColor: "#10b981", // Emerald
      levelNumber: 1,
      title: "The Paper Leak Epidemic",
      badgeIcon: "🚨",
      xpReward: 20,
      description: "Understand the scale of the examination crisis and its impact on social mobility.",
      tasks: [
        {
          type: "concept",
          title: "The Crisis of Faith",
          mascotMood: "concerned",
          content: "Over **250+ national examinations** have been conducted by the National Testing Agency (NTA) since 2018. However, recent paper leaks (NEET-UG, UGC-NET) revealed organized syndicates selling seats for **₹30 to ₹50 lakh**, destroying public faith in meritocracy.",
          keyTakeaway: "Paper leaks are not isolated incidents—they represent commercialized organized crime syndicates."
        },
        {
          type: "true_false",
          prompt: "True or False: According to investigation findings (EOU Bihar), leaked seats in high-stakes examinations were sold for up to ₹30-50 Lakhs.",
          correct: true,
          explanation: "Correct! The Economic Offenses Unit (EOU) documented that criminal cartels charged ₹30-50 lakh per student."
        },
        {
          type: "mcq",
          prompt: "What makes public examinations indispensable to India's democratic ethos?",
          options: [
            "They are the primary vehicle for upward social mobility for rural and underprivileged youth",
            "They eliminate the need for primary school funding",
            "They replace all university semester examinations",
            "They restrict employment to urban candidates"
          ],
          correctIndex: 0,
          explanation: "Public examinations offer the sole objective ladder for millions of hardworking rural youth to escape generational poverty."
        }
      ]
    },

    {
      id: "lvl-2",
      unit: "Unit 1: The Crisis & Constitutional Canvas",
      unitColor: "#10b981",
      levelNumber: 2,
      title: "Constitutional Mandate & Judicial Dictum",
      badgeIcon: "⚖️",
      xpReward: 25,
      description: "Explore Article 14, 16, 21A, Concurrent List Entry 25, and the landmark High Court observation.",
      tasks: [
        {
          type: "concept",
          title: "Heinous Than Murder",
          mascotMood: "teaching",
          content: "The **Chhattisgarh High Court** delivered an iconic observation for UPSC Mains:\n\n*\"A question paper leak is more heinous than murder. While murder kills a single individual, a paper leak murders the dreams, trust, and future of millions of youth.\"*",
          keyTakeaway: "Use this exact quote in your Mains introduction on examination integrity!"
        },
        {
          type: "match_pairs",
          prompt: "Match the Constitutional Provision with its Educational Dimension:",
          pairs: [
            { left: "42nd Amendment (1976)", right: "Education moved to Concurrent List (Entry 25)" },
            { left: "Article 14 & 16", right: "Substantive Equality & Public Employment Merit" },
            { left: "Article 21A", right: "Fundamental Right to Free & Compulsory Education" },
            { left: "DPSP Article 46", right: "Promoting educational interests of SC/ST" }
          ]
        },
        {
          type: "tap_order",
          prompt: "Assemble the iconic High Court dictum in the correct order:",
          tokens: ["A question", "paper leak", "is more heinous", "than", "murder."],
          correctSentence: "A question paper leak is more heinous than murder."
        }
      ]
    },

    {
      id: "lvl-3",
      unit: "Unit 2: The Legal Fortress",
      unitColor: "#6366f1", // Indigo
      levelNumber: 3,
      title: "Public Examinations Act 2024",
      badgeIcon: "📜",
      xpReward: 25,
      description: "Master the statutory features, target scope, and criminal penalties under the 2024 Act.",
      tasks: [
        {
          type: "concept",
          title: "Targeting the Syndicates, Not Students",
          mascotMood: "happy",
          content: "A vital distinction in the **Public Examinations (Prevention of Unfair Means) Act 2024**:\n\n• **Bona fide students are NOT criminalized** under this Act; they remain subject to institutional administrative debarment.\n• The Act targets **organized criminal syndicates, corrupt testing vendors, and question printing mafias** with non-bailable, cognizable offenses.",
          keyTakeaway: "The 2024 Act protects honest students while hunting organized crime syndicates."
        },
        {
          type: "mcq",
          prompt: "Under the Public Examinations Act 2024, what is the statutory penalty for organized paper leak syndicates?",
          options: [
            "A minor administrative fine of ₹50,000",
            "5 to 10 years imprisonment and a minimum fine of ₹1 Crore",
            "Simple warning with 30 days community service",
            "1 year probation with no asset attachment"
          ],
          correctIndex: 1,
          explanation: "The 2024 Act imposes 5-10 years imprisonment and minimum ₹1 crore fine, along with property attachment of guilty institutions."
        },
        {
          type: "true_false",
          prompt: "True or False: Under the 2024 Act, candidates appearing for examinations face mandatory 5 years in prison if found copying.",
          correct: false,
          explanation: "False! Candidates are deliberately excluded from criminal prosecution under this law to prevent harassment. It targets the organizers and syndicates."
        }
      ]
    },

    {
      id: "lvl-4",
      unit: "Unit 2: The Legal Fortress",
      unitColor: "#6366f1",
      levelNumber: 4,
      title: "2026 Amendments & Deterrence Economics",
      badgeIcon: "🛡️",
      xpReward: 30,
      description: "Analyze the 2026 criminal escalation and Gary Becker's Economics of Crime.",
      tasks: [
        {
          type: "concept",
          title: "The Deterrence Paradox",
          mascotMood: "thinking",
          content: "The 2026 Amendment heightened sentences to **7 to 10 years** even for individual facilitators.\n\nHowever, **Becker's Economics of Crime** teaches us that *harsher punishment alone does not deter crime if the probability of detection is low*.\n\nIf the chance of getting caught is 5%, cartels will still risk it for ₹50 Crore illicit gains!",
          keyTakeaway: "Deterrence = Severity of Punishment × Probability of Detection × Speed of Conviction."
        },
        {
          type: "match_pairs",
          prompt: "Connect the Analytical Pillars of Deterrence:",
          pairs: [
            { left: "Ex-Post Deterrence", right: "Lengthy Prison Sentences (7-10 Years)" },
            { left: "Probability of Detection", right: "Digital Forensic Audits & CCTV Surveillance" },
            { left: "Speed of Conviction", right: "Special Designated Fast-Track Courts" },
            { left: "Asset Recovery", right: "Attachment of Illicit Properties & Bank Accounts" }
          ]
        },
        {
          type: "mcq",
          prompt: "Why did the 2026 Amendment create Special Designated Courts?",
          options: [
            "To expedite trials and solve the problem of low conviction rates",
            "To conduct the NEET examination inside courtrooms",
            "To replace the Supreme Court e-Committee",
            "To allow students to file civil suits for free"
          ],
          correctIndex: 0,
          explanation: "Swift conviction ensures that deterrence is immediate, rather than waiting decades in procedural trial delays."
        }
      ]
    },

    {
      id: "lvl-5",
      unit: "Unit 3: Structural Bottlenecks & NTA",
      unitColor: "#06b6d4", // Cyan
      levelNumber: 5,
      title: "The NTA 24-Staff Paradox",
      badgeIcon: "🏢",
      xpReward: 30,
      description: "Examine the institutional design failure: a registered society with only 24 permanent staff.",
      tasks: [
        {
          type: "concept",
          title: "The Anatomy of Vulnerability",
          mascotMood: "surprised",
          content: "Consider this staggering data point for UPSC Mains:\n\n• **National Testing Agency (NTA)** was established in 2018 as a **registered society** under the Societies Registration Act (NOT a statutory body created by Parliament).\n• Despite conducting exams for **1.5+ crore candidates** across 250+ test cycles, NTA operates with only **24 permanent staff members**!\n• The rest of the pipeline—invigilation, IT servers, center hiring, paper transport—is outsourced to third-party contractual vendors.",
          keyTakeaway: "Heavy reliance on unvetted private contractors creates structural leak vectors."
        },
        {
          type: "mcq",
          prompt: "What is the legal status of the National Testing Agency (NTA)?",
          options: [
            "Constitutional body under Article 324",
            "Statutory body established by an Act of Parliament",
            "Registered society under the Societies Registration Act 1860",
            "Public sector undertaking under Ministry of Finance"
          ],
          correctIndex: 2,
          explanation: "NTA is merely a registered society, meaning it lacks statutory autonomy and rigorous parliamentary accountability."
        },
        {
          type: "match_pairs",
          prompt: "Match the Vulnerability with its Manifestation:",
          pairs: [
            { left: "24 Permanent Staff", right: "Over-dependence on private contractual agencies" },
            { left: "Registered Society Status", right: "Absence of direct parliamentary oversight" },
            { left: "Private Cyber Centers", right: "Vulnerable to remote desktop hacking & leaks" },
            { left: "Single-day NEET Format", right: "Concentrated high-stakes illicit incentives" }
          ]
        }
      ]
    },

    {
      id: "lvl-6",
      unit: "Unit 3: Structural Bottlenecks & NTA",
      unitColor: "#06b6d4",
      levelNumber: 6,
      title: "Coaching Nexus & Mental Health Toll",
      badgeIcon: "🧠",
      xpReward: 30,
      description: "Explore the Justice A.K. Rajan findings and the adolescent mental health crisis.",
      tasks: [
        {
          type: "concept",
          title: "The ₹30,000 Crore Coaching Monopoly",
          mascotMood: "thinking",
          content: "The **Justice A.K. Rajan Committee (Tamil Nadu)** observed that centralized high-stakes entrance exams:\n\n1. Disproportionately favor candidates with access to expensive multi-year coaching in hubs like Kota.\n2. Disadvantage rural, first-generation, and State Board vernacular students.\n3. Turn adolescent education into a rote-memorization 'survival test', inducing severe mental health trauma and student suicides.",
          keyTakeaway: "Centralization without equity fuels predatory coaching cartels."
        },
        {
          type: "true_false",
          prompt: "True or False: The Justice A.K. Rajan Committee argued that centralized entrance exams bridge the rural-urban divide in higher education.",
          correct: false,
          explanation: "False! The Committee found that it widened the gap by heavily favoring affluent urban students who can afford private coaching."
        },
        {
          type: "mcq",
          prompt: "What psychological consequence arises from one-shot annual high-stakes examinations?",
          options: [
            "Severe adolescent stress, anxiety, and desperation to cheat due to loss of an entire year",
            "Improved leisure time for students",
            "Complete elimination of exam pressure",
            "Equalization of student outcomes"
          ],
          correctIndex: 0,
          explanation: "When an entire student's future hangs on a single 3-hour window once a year, the pressure fuels desperation, illegal practices, and suicide crises."
        }
      ]
    },

    {
      id: "lvl-7",
      unit: "Unit 4: The Radhakrishnan Overhaul",
      unitColor: "#f59e0b", // Amber
      levelNumber: 7,
      title: "K. Radhakrishnan Committee: 7 Pillars",
      badgeIcon: "🌟",
      xpReward: 35,
      description: "Master the recommendations of the high-level panel chaired by Dr. K. Radhakrishnan.",
      tasks: [
        {
          type: "concept",
          title: "The Blueprint for Total Reform",
          mascotMood: "celebrating",
          content: "The **K. Radhakrishnan Committee** (former ISRO Chairman) submitted a comprehensive reform blueprint:\n\n1. **Statutory Restructuring:** Enact an Act of Parliament to make NTA a permanent, statutory body.\n2. **Professional Permanent Cadre:** Eliminate outsourced contractual staff; hire permanent IT security and psychometric experts.\n3. **Demarcation of Functions:** Separate test design from logistics administration.\n4. **End-to-End Digital Custody:** Encrypted question pipelines with digital forensic watermarks.",
          keyTakeaway: "Transform NTA into an ISRO-grade high-integrity testing institution."
        },
        {
          type: "match_pairs",
          prompt: "Connect the Radhakrishnan Pillar with its Operational Mechanism:",
          pairs: [
            { left: "Statutory NTA", right: "Legislative oversight & permanent civil cadre" },
            { left: "Two-Stage Testing", right: "Screening Prelims + Proctored Mains filter" },
            { left: "Government Centers Only", right: "Barring private commercial computer labs" },
            { left: "Dynamic Question Banks", right: "Algorithmic assembly preventing leaks" }
          ]
        },
        {
          type: "mcq",
          prompt: "Who chaired the high-level committee appointed by the government to overhaul NTA?",
          options: [
            "Dr. K. Radhakrishnan (Former ISRO Chairman)",
            "Prof. Ashok Gulati",
            "Dr. Shanta Kumar",
            "Justice Manepalli Narayana Rao Venkatachaliah"
          ],
          correctIndex: 0,
          explanation: "Dr. K. Radhakrishnan, distinguished scientist and former ISRO Chairman, chaired the 7-member reform panel."
        }
      ]
    },

    {
      id: "lvl-8",
      unit: "Unit 4: The Radhakrishnan Overhaul",
      unitColor: "#f59e0b",
      levelNumber: 8,
      title: "Hybrid Testing & Digital Lockers",
      badgeIcon: "🔐",
      xpReward: 35,
      description: "Explore the hybrid examination delivery model and digital locker encryption.",
      tasks: [
        {
          type: "concept",
          title: "How Hybrid Testing Eliminates Leaks",
          mascotMood: "teaching",
          content: "In traditional exams, printed papers sit in bank vaults and trucks for days, creating leak opportunities.\n\n**The Hybrid Solution:**\n• Questions are transmitted in **military-grade encrypted packets** to government exam centers only **30 minutes before the exam**.\n• Papers are decrypted via multi-factor digital keys and printed in-house or displayed on secure computer terminals.\n• Candidates mark answers on OMR sheets or tamper-proof terminals.",
          keyTakeaway: "Zero physical storage latency = Zero pre-exam paper leaks!"
        },
        {
          type: "true_false",
          prompt: "True or False: In a hybrid testing model, printed question papers are transported via trucks 5 days in advance.",
          correct: false,
          explanation: "False! Hybrid testing transmits questions digitally and securely just minutes before the test, eliminating physical transit leaks."
        },
        {
          type: "mcq",
          prompt: "Which institutions does the Radhakrishnan panel recommend using exclusively as exam test centers?",
          options: [
            "Private unverified cyber cafes and gaming hubs",
            "Kendriya Vidyalayas, Navodaya Vidyalayas, and Government Universities",
            "Commercial shopping mall basements",
            "Private tuition coaching center buildings"
          ],
          correctIndex: 1,
          explanation: "Government institutions provide state-controlled perimeter security, vetted staff, and public accountability."
        }
      ]
    },

    {
      id: "lvl-9",
      unit: "Unit 5: Global Models & Mains Arena",
      unitColor: "#ec4899", // Pink
      levelNumber: 9,
      title: "Global Benchmarks: Gaokao vs SAT",
      badgeIcon: "🌍",
      xpReward: 40,
      description: "Compare China's high-surveillance Gaokao with Western continuous assessment models.",
      tasks: [
        {
          type: "concept",
          title: "China's Gaokao vs Western SAT/GRE",
          mascotMood: "thinking",
          content: "• **China (Gaokao):** The world's most militarized exam. Uses military escorts, anti-drone jammers, biometric face scanners, and 7-year prison terms. Strict deterrence, but creates immense psychological trauma.\n\n• **USA/UK (SAT/A-Levels):** Multiple test attempts per year, holistic continuous school assessment weighting, and adaptive computerized testing where no two students get the identical paper.",
          keyTakeaway: "India must combine technological rigor with multi-attempt psychological relief."
        },
        {
          type: "match_pairs",
          prompt: "Match the Country Model with its Security Strategy:",
          pairs: [
            { left: "China (Gaokao)", right: "Military escorts, radio jammers & 7-yr penal term" },
            { left: "USA (SAT / GRE)", right: "Multiple annual testing windows & adaptive items" },
            { left: "UK (A-Levels)", right: "Weightage to continuous school-based assessments" },
            { left: "India (Reform Vision)", right: "Hybrid digital locks + Statutory NTA governance" }
          ]
        },
        {
          type: "mcq",
          prompt: "What advantage does offering multiple annual attempts (like SAT/GRE) have over a single-day exam?",
          options: [
            "It eliminates the all-or-nothing desperation that fuels paper leaks and student suicides",
            "It increases paper leak profits",
            "It requires zero question banks",
            "It permanently abolishes all universities"
          ],
          correctIndex: 0,
          explanation: "When students have another attempt in 3 months, the catastrophic fear of losing an entire year disappears, drastically reducing leak demand."
        }
      ]
    },

    {
      id: "lvl-10",
      unit: "Unit 5: Global Models & Mains Arena",
      unitColor: "#ec4899",
      levelNumber: 10,
      title: "The Mains Answer Boss Challenge",
      badgeIcon: "👑",
      xpReward: 50,
      description: "Synthesize the 15-marker Mains answer framework: Quotes, Dimensions & Way Forward.",
      tasks: [
        {
          type: "concept",
          title: "UPSC Mains Master Synthesis",
          mascotMood: "celebrating",
          content: "You've conquered the entire Public Examinations curriculum!\n\n**Mains Framework Checklist:**\n• **Intro Hook:** Chhattisgarh High Court quote (*\"More heinous than murder...\"*) + 42nd Amendment (Entry 25).\n• **Crisis Data:** 24 NTA permanent staff, ₹30-50L seat leak pricing, 250+ exams.\n• **Deterrence Analysis:** 2024 & 2026 Acts (7-10 years, ₹1 Cr) vs Becker's Economics of Crime.\n• **Recommendations:** K. Radhakrishnan 7 pillars + Hybrid digital transmission.\n• **Conclusion:** Safeguarding the meritocratic soul of Indian democracy.",
          keyTakeaway: "A complete, high-scoring answer synthesizes data, law, court dictums, and committee reforms!"
        },
        {
          type: "tap_order",
          prompt: "Order the 4 Structural Pillars of a 15-Marker Answer on Exam Integrity:",
          tokens: ["Constitutional Hook & High Court Dictum", "Anatomy of Crisis (NTA 24-Staff Paradox)", "Critical Review of 2024/26 Act", "Radhakrishnan Committee Way Forward"],
          correctSentence: "Constitutional Hook & High Court Dictum Anatomy of Crisis (NTA 24-Staff Paradox) Critical Review of 2024/26 Act Radhakrishnan Committee Way Forward"
        },
        {
          type: "mcq",
          prompt: "In a Mains conclusion on Public Examination reforms, which overarching principle should you emphasize?",
          options: [
            "Examination integrity is the cornerstone of constitutional faith and upward social mobility",
            "All competitive exams should be replaced with lottery systems",
            "Testing agencies should be entirely privatized without government regulation",
            "Penalties should be reduced to encourage cheating syndicates"
          ],
          correctIndex: 0,
          explanation: "Perfect! Meritocracy is a constitutional promise; restoring examination credibility protects the democratic aspirations of India's youth."
        }
      ]
    }
  ]
};
