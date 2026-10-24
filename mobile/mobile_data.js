/**
 * CORTEX MOBILE GAME DATA
 * Worlds, Levels, Boss Battles, Blitz Rapid-Fire, Shop Items & Quests
 */

const GAME_DATA = {
  worlds: [
    {
      id: "world-1",
      name: "World 1: Public Examinations & NTA Overhaul",
      badge: "CAVA Lecture 4",
      description: "Conquer paper leak deterrence, the 24-staff paradox, and the Radhakrishnan 7 pillars.",
      color: "#10b981",
      levels: [
        {
          id: 1,
          title: "Upward Social Mobility",
          subtitle: "The Moral Anchor of Meritocracy",
          icon: "🌱",
          stars: 0,
          xpReward: 30,
          coinsReward: 50,
          dialogue: "In developing nations like India, competitive exams are the sole merit-based ladder for rural youth to break intergenerational poverty.",
          questions: [
            {
              type: "mcq",
              prompt: "Why are public examinations described as the 'crown jewel' of an egalitarian republic?",
              options: [
                "They favor wealthy candidates with private coaching",
                "They provide intergenerational upward social mobility solely on merit",
                "They are conducted entirely online without human invigilation",
                "They eliminate all administrative costs for the state"
              ],
              correctIndex: 1,
              explanation: "Competitive examinations provide the sole transparent vehicle for the children of marginalized laborers and farmers to attain sovereign administrative status on merit."
            },
            {
              type: "swipe",
              prompt: "Paper leaks merely cause temporary exam delays without harming the socio-economic trust of marginalized youth.",
              isTrue: false,
              explanation: "Paper leaks cause structural disenfranchisement of honest underprivileged youth and destroy faith in democratic meritocracy."
            },
            {
              type: "match",
              prompt: "Match the concept with its democratic implication:",
              pairs: [
                { term: "Upward Mobility", def: "Intergenerational escape from poverty" },
                { term: "Meritocracy", def: "Status earned by ability, not birth" },
                { term: "Paper Leak", def: "Structural disenfranchisement" }
              ]
            }
          ]
        },
        {
          id: 2,
          title: "Chhattisgarh HC Landmark Dictum",
          subtitle: "The Legal & Moral Judgment",
          icon: "⚖️",
          stars: 0,
          xpReward: 35,
          coinsReward: 60,
          dialogue: "The High Court pronounced an unforgettable opening hook for educational integrity in India.",
          questions: [
            {
              type: "mcq",
              prompt: "How did the Chhattisgarh High Court characterize the gravity of question paper leaks?",
              options: [
                "As an administrative misdemeanor punishable by fine only",
                "As more heinous than murder, because it murders the trust and future of millions of youth",
                "As a civil contract dispute between universities and agencies",
                "As an inevitable byproduct of large population demographics"
              ],
              correctIndex: 1,
              explanation: "The High Court stated: 'A paper leak is more heinous than murder. Murder kills an individual, but a paper leak murders the dreams, trust, and future of millions of youth.'"
            },
            {
              type: "tap_order",
              prompt: "Assemble the High Court's quote in correct sequence:",
              tokens: ["Paper", "leak", "is", "more", "heinous", "than", "murder"],
              correctOrder: ["Paper", "leak", "is", "more", "heinous", "than", "murder"],
              explanation: "High-impact hook for UPSC GS-2 Mains answers on governance and ethics."
            }
          ]
        },
        {
          id: 3,
          title: "Constitutional Matrix",
          subtitle: "42nd CAA & Fundamental Rights",
          icon: "📜",
          stars: 0,
          xpReward: 40,
          coinsReward: 70,
          questions: [
            {
              type: "mcq",
              prompt: "Which Constitutional Amendment transferred 'Education' from the State List to the Concurrent List (Entry 25)?",
              options: [
                "44th Amendment Act (1978)",
                "42nd Amendment Act (1976)",
                "86th Amendment Act (2002)",
                "91st Amendment Act (2003)"
              ],
              correctIndex: 1,
              explanation: "The 42nd Amendment shifted Education to Concurrent List Entry 25, creating dual legislative competence between Union and States."
            },
            {
              type: "match",
              prompt: "Match the Article to its testing integrity protection:",
              pairs: [
                { term: "Article 14", def: "Protection against arbitrary discrimination" },
                { term: "Article 16", def: "Equal opportunity in public employment" },
                { term: "Article 21A", def: "Right to quality education" }
              ]
            }
          ]
        },
        {
          id: 4,
          title: "The 24-Staff Paradox & Crime Economy",
          subtitle: "Structural Institutional Fragility",
          icon: "🔍",
          stars: 0,
          xpReward: 45,
          coinsReward: 80,
          questions: [
            {
              type: "mcq",
              prompt: "What is the core institutional vulnerability of the National Testing Agency (NTA)?",
              options: [
                "It has an overstaffed permanent cadre of over 50,000 employees",
                "It conducts tests for 1.5 Crore candidates with only 24 permanent employees, forcing heavy outsourcing",
                "It is a constitutional body established directly under Article 324",
                "It only operates pen-and-paper tests in rural areas"
              ],
              correctIndex: 1,
              explanation: "Operating with only 24 permanent staff forced NTA to outsource critical logistics, IT servers, and centers to third parties with minimal civil service stakes."
            },
            {
              type: "mcq",
              prompt: "According to EOU Bihar investigations, how much were paper leak syndicates charging per leaked seat?",
              options: [
                "₹5,000 to ₹10,000",
                "₹30 Lakh to ₹50 Lakh per candidate",
                "Free of cost on telegram channels",
                "₹1 Lakh to ₹2 Lakh only"
              ],
              correctIndex: 1,
              explanation: "Investigations revealed organized financial syndicates charging ₹30L–₹50L per candidate, renting safe-houses for pre-exam cram sessions."
            }
          ]
        },
        {
          id: 5,
          title: "Gary Becker Deterrence Economics",
          subtitle: "Expected Penalty Formula",
          icon: "📐",
          stars: 0,
          xpReward: 50,
          coinsReward: 90,
          questions: [
            {
              type: "tap_order",
              prompt: "Arrange Gary Becker's Deterrence Economics Equation:",
              tokens: ["Expected", "Penalty", "=", "Severity", "×", "Detection", "Probability", "×", "Conviction", "Speed"],
              correctOrder: ["Expected", "Penalty", "=", "Severity", "×", "Detection", "Probability", "×", "Conviction", "Speed"],
              explanation: "Nobel Laureate Gary Becker proved that severity alone cannot deter syndicates if detection probability remains near zero."
            },
            {
              type: "swipe",
              prompt: "Increasing statutory prison terms alone will completely eliminate paper leaks without improving forensic detection or fast-track conviction speeds.",
              isTrue: false,
              explanation: "If probability of capture is only 5%, syndicates making ₹50 Crore will gamble regardless of maximum prison terms."
            }
          ]
        },
        {
          id: 6,
          title: "The Legal Fortress (2024 & 2026 Acts)",
          subtitle: "Public Examinations Penal Architecture",
          icon: "🛡️",
          stars: 0,
          xpReward: 55,
          coinsReward: 100,
          questions: [
            {
              type: "mcq",
              prompt: "How does the Public Examinations (Prevention of Unfair Means) Act 2024 treat bona fide student examinees?",
              options: [
                "Mandates 10 years imprisonment for any student in the exam hall",
                "Excludes students from penal criminal prosecution; regulates them via institutional debarment",
                "Requires students to post ₹1 Crore bail bonds before writing tests",
                "Cancels the citizenship of any candidate who fails"
              ],
              correctIndex: 1,
              explanation: "The Act explicitly shields bona fide student candidates from criminalization, focusing severe penal provisions on organized cartels."
            },
            {
              type: "mcq",
              prompt: "What are the penalties under the Act for organized paper leak syndicates?",
              options: [
                "1 month simple detention and ₹500 fine",
                "Minimum 5-10 years imprisonment and ₹1 Crore minimum fine with property attachment",
                "Community service for 2 weeks",
                "Verbal warning by the District Magistrate"
              ],
              correctIndex: 1,
              explanation: "Syndicate offenses are cognizable, non-bailable, and non-compoundable, carrying 5–10 years imprisonment, ₹1 Cr minimum fine, and asset forfeiture."
            }
          ]
        },
        {
          id: 7,
          title: "Radhakrishnan Committee: Testing Architecture",
          subtitle: "Two-Stage Filtering & Hybrid Lockboxes",
          icon: "🏛️",
          stars: 0,
          xpReward: 60,
          coinsReward: 110,
          questions: [
            {
              type: "match",
              prompt: "Match Dr. K. Radhakrishnan's reform pillar to its solution:",
              pairs: [
                { term: "Two-Stage Testing", def: "Eliminates single-day 24-lakh high-stakes bottleneck" },
                { term: "Hybrid Lockbox", def: "Zero transit storage latency; 30-min encrypted delivery" },
                { term: "Statutory Cadre", def: "Permanent in-house psychometric and security staff" }
              ]
            },
            {
              type: "swipe",
              prompt: "Dr. K. Radhakrishnan recommended continuing to conduct central exams in unvetted private commercial cyber cafes.",
              isTrue: false,
              explanation: "The panel recommended barring private commercial labs completely and utilizing Kendriya Vidyalayas, JNVs, and public universities."
            }
          ]
        },
        {
          id: 8,
          title: "Global Benchmarks & Mains Synthesis",
          subtitle: "Gaokao vs SAT vs Indian Synthesis",
          icon: "🌐",
          stars: 0,
          xpReward: 65,
          coinsReward: 120,
          questions: [
            {
              type: "mcq",
              prompt: "What characterizes the Chinese Gaokao examination security model?",
              options: [
                "Take-home open book exams with zero invigilation",
                "Militarized police escorts, drone frequency jammers, facial recognition, and criminal code penalties",
                "Conducting tests exclusively via mobile chat apps",
                "Only grading candidates based on athletic performance"
              ],
              correctIndex: 1,
              explanation: "China's Gaokao employs armed police escorts for test papers, radio frequency drone jammers, and criminal penalties up to 7 years imprisonment."
            }
          ]
        },
        {
          id: 9,
          title: "The Covenant of Meritocracy",
          subtitle: "Master Conclusion Synthesis",
          icon: "🎓",
          stars: 0,
          xpReward: 70,
          coinsReward: 130,
          questions: [
            {
              type: "tap_order",
              prompt: "Construct the closing dictum for UPSC Mains answers:",
              tokens: ["Examination", "integrity", "is", "a", "sacred", "constitutional", "covenant", "protecting", "meritocracy"],
              correctOrder: ["Examination", "integrity", "is", "a", "sacred", "constitutional", "covenant", "protecting", "meritocracy"],
              explanation: "Top conclusion hook for UPSC GS-2 Governance answers."
            }
          ]
        },
        {
          id: 10,
          isBoss: true,
          title: "BOSS BATTLE: The Paper Leak Syndicate Chief",
          subtitle: "Defeat the ₹50-Lakh Mafia with Governance Mastery!",
          icon: "👹",
          bossName: "Dreadlord Cartel Master",
          bossHp: 1000,
          stars: 0,
          xpReward: 150,
          coinsReward: 300,
          badgeUnlock: "Meritocracy Defender",
          questions: [
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 1: What is the primary institutional transformation needed to fix NTA's structural weakness?",
              options: [
                "Reconstitute NTA as a statutory body via parliamentary Act with permanent civil cadres",
                "Abolish all national entrance exams forever",
                "Hire more temporary contractual workers without background verification",
                "Move all exams back to state high schools without CCTV"
              ],
              correctIndex: 0,
              damage: 250,
              explanation: "Direct hit! Transforming NTA from a registered society into a statutory authority eliminates the accountability vacuum."
            },
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 2: Which testing model eliminates the vulnerability of physical test papers stored in bank vaults for days?",
              options: [
                "Postal mailing of paper packets 2 weeks in advance",
                "Hybrid digital lockbox with encrypted transmission 30 minutes before the exam",
                "Oral interviews conducted over telephone",
                "Printing papers on open billboards"
              ],
              correctIndex: 1,
              damage: 250,
              explanation: "Critical Strike! Hybrid digital transmission with dual-key decryption 30 minutes before exam time eliminates storage latency leaks."
            },
            {
              type: "swipe",
              prompt: "BOSS CHALLENGE 3: Gary Becker proved that high criminal severity on paper compensates fully for low detection probability.",
              isTrue: false,
              damage: 250,
              explanation: "Massive Damage! Severity is meaningless without high detection probability and swift conviction speed."
            },
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 4: Where should all high-stakes public examinations be physically hosted according to the Radhakrishnan Panel?",
              options: [
                "Unvetted commercial cyber cafes and rented shopping complexes",
                "Exclusively in accredited public infrastructure: Kendriya Vidyalayas, Navodayas & Universities",
                "At private coaching institutes",
                "Candidates' own private homes"
              ],
              correctIndex: 1,
              damage: 250,
              explanation: "FATAL BLOW! The Syndicate Boss is defeated! Public infrastructure restores examination integrity and trust!"
            }
          ]
        }
      ]
    },
    {
      id: "world-2",
      name: "World 2: AI in the Judiciary",
      badge: "CAVA Lecture 3",
      description: "Master Supreme Court regulations, the 3-tier pyramid, algorithmic bias, and Article 21.",
      color: "#6366f1",
      levels: [
        {
          id: 11,
          title: "The 5-Crore Pendency Gridlock",
          subtitle: "Judicial Reality & Need for Tech",
          icon: "📊",
          stars: 0,
          xpReward: 35,
          coinsReward: 60,
          questions: [
            {
              type: "mcq",
              prompt: "According to NJDG data, what is the total case backlog in the Indian judicial system?",
              options: [
                "50,000 cases",
                "Over 5.1 Crore pending cases, with over 87% in subordinate district courts",
                "10 Lakh cases",
                "Under 1,000 cases"
              ],
              correctIndex: 1,
              explanation: "Over 5.1 Crore cases are pending across Supreme Court, High Courts, and subordinate judiciary, driving the push for assistive AI."
            },
            {
              type: "mcq",
              prompt: "What is India's judge-to-population ratio compared to the Law Commission's 1987 target?",
              options: [
                "Current: 21 per million; Target: 50 per million",
                "Current: 500 per million; Target: 100 per million",
                "Current: 100 per million; Target: 20 per million",
                "Current: 5 per million; Target: 10 per million"
              ],
              correctIndex: 0,
              explanation: "India operates with just 21 judges per million citizens, compared to 150/M in the USA and 220/M in parts of Europe."
            }
          ]
        },
        {
          id: 12,
          title: "The Toxic Gas Alarm",
          subtitle: "NCLT Hallucination Precedent",
          icon: "🚨",
          stars: 0,
          xpReward: 40,
          coinsReward: 70,
          questions: [
            {
              type: "mcq",
              prompt: "How did the Supreme Court characterize citing AI-hallucinated fake precedents in court filings?",
              options: [
                "A minor formatting mistake",
                "Comparable to the release of toxic Methyl Isocyanate gas contaminating justice",
                "A creative way to build new common law",
                "A recommended best practice for junior advocates"
              ],
              correctIndex: 1,
              explanation: "The Apex Court warned that citing fictitious LLM-hallucinated case citations poisons the judicial stream like toxic Methyl Isocyanate gas."
            }
          ]
        },
        {
          id: 13,
          title: "The Supreme Court 3-Tier AI Pyramid",
          subtitle: "Green, Amber & Red Tiers",
          icon: "🚦",
          stars: 0,
          xpReward: 50,
          coinsReward: 90,
          questions: [
            {
              type: "match",
              prompt: "Match the Supreme Court Tier to its regulatory status:",
              pairs: [
                { term: "Green Tier", def: "Permitted & encouraged: Registry defect checks & case listing" },
                { term: "Amber Tier", def: "Cautious assistive research with mandatory human checking" },
                { term: "Red Tier", def: "Strictly banned: Automated determination of guilt and sentencing" }
              ]
            },
            {
              type: "swipe",
              prompt: "The Supreme Court permits AI algorithms to automatically deliver final criminal verdicts and determine prison sentences in simple cases.",
              isTrue: false,
              explanation: "Automated adjudication is strictly relegated to the Red Tier—absolutely prohibited under Article 21 and Natural Justice."
            }
          ]
        },
        {
          id: 14,
          isBoss: true,
          title: "BOSS BATTLE: The Black-Box Hallucination Dragon",
          subtitle: "Defend Article 21 and the Speaking Order Doctrine!",
          icon: "🐉",
          bossName: "Algorithmic Black-Box Leviathan",
          bossHp: 1200,
          stars: 0,
          xpReward: 180,
          coinsReward: 350,
          badgeUnlock: "Constitutional Guardian",
          questions: [
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 1: Why does neural 'black-box' opacity violate Administrative Law in India?",
              options: [
                "It violates the Natural Justice mandate for 'reasoned speaking orders'",
                "It uses too much electrical power",
                "It cannot translate Hindi words",
                "It requires internet access"
              ],
              damage: 300,
              correctIndex: 0,
              explanation: "DIRECT HIT! Administrative law mandates reasoned speaking orders so litigants know why decisions were taken; unexplainable weights violate natural justice."
            },
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 2: What historical risk does the COMPAS US bail recidivism precedent demonstrate?",
              options: [
                "AI always charges too much money",
                "Predictive AI re-encodes historical human bias against marginalized communities under Article 14",
                "AI refuses to work during night hours",
                "AI only works in English"
              ],
              damage: 300,
              correctIndex: 1,
              explanation: "CRITICAL HIT! Training AI on historical policing records leads to automated discrimination against marginalized groups."
            },
            {
              type: "mcq",
              prompt: "BOSS CHALLENGE 3: What does Regulation 43 of the Supreme Court Draft AI Rules mandate?",
              options: [
                "Lawyers can blame ChatGPT errors to avoid liability",
                "Mandatory affirmative disclosure of AI use with 100% human advocate liability",
                "All judges must be replaced by neural networks",
                "AI cannot be used for typing documents"
              ],
              damage: 300,
              correctIndex: 1,
              explanation: "SHATTERING BLOW! Regulation 43 imposes absolute accountability on human advocates; AI cannot be blamed."
            },
            {
              type: "tap_order",
              prompt: "BOSS CHALLENGE 4: Complete the golden closing dictum:",
              tokens: ["The", "law", "is", "not", "a", "mere", "algorithm;", "it", "is", "human", "conscience"],
              correctOrder: ["The", "law", "is", "not", "a", "mere", "algorithm;", "it", "is", "human", "conscience"],
              damage: 300,
              explanation: "FINAL VICTORY! The Dragon is vanquished! Justice remains anchored in human conscience and empathy!"
            }
          ]
        }
      ]
    }
  ],

  // 60-Second Rapid-Fire Blitz Questions
  blitzQuestions: [
    { q: "Education was moved to Concurrent List by 42nd CAA 1976.", ans: true },
    { q: "NTA has over 5,000 permanent civil service officers.", ans: false },
    { q: "Under 2024 Act, bona fide student examinees face criminal prison terms.", ans: false },
    { q: "Chhattisgarh HC stated paper leak is more heinous than murder.", ans: true },
    { q: "Gary Becker proved harsh punishment alone eliminates crime without detection.", ans: false },
    { q: "India currently operates with 21 judges per million citizens.", ans: true },
    { q: "Supreme Court Red Tier permits algorithmic determination of criminal guilt.", ans: false },
    { q: "Lawyers are 100% liable for AI hallucinations under Regulation 43.", ans: true },
    { q: "Radhakrishnan Committee recommended hybrid digital lockboxes with 30-min delivery.", ans: true },
    { q: "NTA is established as a statutory authority under the Constitution.", ans: false },
    { q: "Radhakrishnan panel recommended holding exams only in accredited government schools.", ans: true },
    { q: "Speaking order doctrine requires judges to provide explainable reasons.", ans: true },
    { q: "China's Gaokao exam employs armed military escorts and signal jammers.", ans: true },
    { q: "The 2026 Amendment heightened organized crime leak fines to minimum ₹1 Crore.", ans: true },
    { q: "SUVAS is Supreme Court's AI tool for automated judicial verdicts.", ans: false }
  ],

  // In-Game Shop Catalog
  shopItems: [
    {
      id: "heart-refill",
      name: "Full Heart Refill",
      desc: "Instantly restore all 5 Lives to keep playing non-stop.",
      price: 100,
      currency: "gems",
      icon: "❤️",
      type: "refill"
    },
    {
      id: "streak-freeze",
      name: "Streak Shield",
      desc: "Protects your study streak if you miss a day.",
      price: 250,
      currency: "gems",
      icon: "🧊",
      type: "streak"
    },
    {
      id: "time-boost",
      name: "Blitz Time Freezer",
      desc: "Adds +15 seconds to rapid-fire blitz rounds.",
      price: 150,
      currency: "coins",
      icon: "⏱️",
      type: "booster"
    },
    {
      id: "hint-5050",
      name: "50-50 Eliminator",
      desc: "Eliminates 2 wrong options in any tough question.",
      price: 120,
      currency: "coins",
      icon: "💡",
      type: "booster"
    },
    {
      id: "skin-dm",
      name: "District Magistrate Badge",
      desc: "Unlock the golden IAS Collector avatar for your profile.",
      price: 500,
      currency: "gems",
      icon: "🎖️",
      type: "skin"
    },
    {
      id: "skin-judge",
      name: "Supreme Court Gavel Avatar",
      desc: "Unlock the Apex Bench Judiciary avatar.",
      price: 500,
      currency: "gems",
      icon: "⚖️",
      type: "skin"
    }
  ],

  // Competitive Leaderboard
  leaderboard: [
    { rank: 1, name: "Ananya Sharma (AIR 1)", score: 2840, league: "Diamond", avatar: "👩‍💼" },
    { rank: 2, name: "Vikramaditya (IPS Cadet)", score: 2620, league: "Diamond", avatar: "👮‍♂️" },
    { rank: 3, name: "Meera Nair (IAS Trainee)", score: 2490, league: "Diamond", avatar: "🏛️" },
    { rank: 4, name: "You (Aspirant)", score: 620, league: "Gold", avatar: "🧠", isUser: true },
    { rank: 5, name: "Rahul Verma (State PSC)", score: 580, league: "Gold", avatar: "🧑‍💻" },
    { rank: 6, name: "Sneha Patel (UPSC 2026)", score: 540, league: "Gold", avatar: "📖" },
    { rank: 7, name: "Karthik Raja (Prelims Pro)", score: 490, league: "Silver", avatar: "⚡" },
    { rank: 8, name: "Devansh Gupta", score: 410, league: "Silver", avatar: "🎯" }
  ]
};
