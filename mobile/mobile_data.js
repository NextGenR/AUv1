/**
 * CORTEX MOBILE GAME DATA
 * Unified repository synchronizer: uses the EXACT SAME questions as the desktop webpage version
 * (MSME_DATA from msme_data.js, PUBLIC_EXAM_DATA from public_exam_data.js, and LECTURE_DATA from lecture_data.js)
 */

(function () {
  'use strict';

  // 1. TOPIC: MSME Reforms & Catalysts (10 Levels from MSME_DATA)
  function buildMsmeLevels() {
    if (typeof MSME_DATA !== 'undefined' && MSME_DATA.levels) {
      return MSME_DATA.levels.map((lvl) => ({
        id: lvl.levelNumber,
        rawId: lvl.id,
        topic: 'msme',
        title: lvl.title,
        subtitle: lvl.description,
        icon: lvl.badgeIcon,
        unit: lvl.unit,
        unitColor: lvl.unitColor,
        xpReward: lvl.xpReward,
        coinsReward: lvl.xpReward * 3,
        isBoss: lvl.levelNumber === 10,
        bossName: lvl.levelNumber === 10 ? "Regulatory Cliff & Syndicate Overlord" : null,
        bossHp: 1000,
        tasks: lvl.tasks
      }));
    }
    return [];
  }

  // 2. TOPIC: Public Examinations & NTA Reforms (10 Levels from PUBLIC_EXAM_DATA)
  function buildPublicExamLevels() {
    if (typeof PUBLIC_EXAM_DATA !== 'undefined' && PUBLIC_EXAM_DATA.levels) {
      return PUBLIC_EXAM_DATA.levels.map((lvl) => ({
        id: lvl.levelNumber,
        rawId: lvl.id,
        topic: 'public-exams',
        title: lvl.title,
        subtitle: lvl.description,
        icon: lvl.badgeIcon,
        unit: lvl.unit,
        unitColor: lvl.unitColor,
        xpReward: lvl.xpReward,
        coinsReward: lvl.xpReward * 3,
        isBoss: lvl.levelNumber === 10,
        bossName: lvl.levelNumber === 10 ? "Dreadlord Cartel Master" : null,
        bossHp: 1000,
        tasks: lvl.tasks
      }));
    }
    return [];
  }

  // 3. TOPIC: AI in the Judiciary (4 Levels from LECTURE_DATA)
  function buildAiJudiciaryLevels() {
    const mcqs = (typeof LECTURE_DATA !== 'undefined' && LECTURE_DATA.mcqs) ? LECTURE_DATA.mcqs : [];
    return [
      {
        id: 1,
        rawId: 'ai-1',
        topic: 'ai-judiciary',
        title: "5.1 Crore Pendency & Judge Ratio",
        subtitle: "Human Capital Deficit & NJDG Data",
        icon: "📊",
        unit: "Unit 1: Judicial Crisis & AI Capabilities",
        unitColor: "#6366f1",
        xpReward: 30,
        coinsReward: 90,
        tasks: [
          {
            type: "concept",
            title: "5.1 Crore Cases Gridlock",
            content: "NJDG reports over **5.1 Crore cases** pending in Indian courts, with over 87% in subordinate district courts. India has just **21 judges per million citizens** against the Law Commission (1987) target of 50/million.",
            keyTakeaway: "Assistive AI is needed to solve clerical bottlenecks, not to replace judicial conscience."
          },
          mcqs[1] || {
            type: "mcq",
            prompt: "In the context of the Indian judiciary's human resource constraints, consider:\n1. India currently has approximately 21 judges per million population.\n2. The Law Commission in 1987 recommended at least 50 judges per million.\n3. Over 80% of India's 5 crore pending cases are in subordinate district courts.\n\nWhich of the statements given above are correct?",
            options: ["1 and 2 only", "2 and 3 only", "1 and 3 only", "1, 2 and 3"],
            correctIndex: 3,
            explanation: "All three statements are correct: India has 21 judges/M (target 50/M) and district courts account for over 87% of pendency."
          }
        ]
      },
      {
        id: 2,
        rawId: 'ai-2',
        topic: 'ai-judiciary',
        title: "Supreme Court 3-Tier AI Pyramid",
        subtitle: "Green, Amber & Red Tiers",
        icon: "🚦",
        unit: "Unit 1: Judicial Crisis & AI Capabilities",
        unitColor: "#6366f1",
        xpReward: 35,
        coinsReward: 100,
        tasks: [
          {
            type: "concept",
            title: "The AI Regulatory Pyramid",
            content: "• **Green Tier:** Case scheduling, defect checking, and registry automation.\n• **Amber Tier:** Legal research and multilingual translation (SUVAS/SUPACE with mandatory human proofreading).\n• **Red Tier:** Automated determination of guilt and criminal sentencing (**Strictly Banned**).",
            keyTakeaway: "Red Tier strictly bans algorithmic adjudication under Article 21."
          },
          mcqs[0] || {
            type: "mcq",
            prompt: "According to the Supreme Court's draft guidelines on Artificial Intelligence, which of the following falls under the 'Red Tier' (Strictly Prohibited)?",
            options: [
              "Automated cause-list scheduling and case categorization",
              "Machine-assisted translation of judgments via SUVAS",
              "Automated judicial adjudication and determining criminal sentences",
              "Pre-trial evidentiary fact extraction using SUPACE"
            ],
            correctIndex: 2,
            explanation: "Under the Supreme Court's AI Pyramid, automated adjudication and sentencing are strictly prohibited under the Red Tier."
          }
        ]
      },
      {
        id: 3,
        rawId: 'ai-3',
        topic: 'ai-judiciary',
        title: "Judicial Hallucinations & Precedent",
        subtitle: "The Toxic Gas Warning & Mata v. Avianca",
        icon: "⚖️",
        unit: "Unit 2: Ethical Hazards & Legal Guardrails",
        unitColor: "#ec4899",
        xpReward: 40,
        coinsReward: 120,
        tasks: [
          {
            type: "concept",
            title: "The Toxic Gas Alarm",
            content: "In the NCLT matter, lawyers submitted fictitious ChatGPT-hallucinated citations. The Supreme Court observed:\n\n*\"Using AI-hallucinated citations in court is like the release of toxic Methyl Isocyanate gas!\"*",
            keyTakeaway: "Zero-tolerance for AI legal hallucinations."
          },
          mcqs[2] || {
            type: "mcq",
            prompt: "In the famous international precedent 'Mata v. Avianca', cited extensively in Indian judicial ethics debates, what issue was adjudicated?",
            options: [
              "Use of algorithmic facial recognition in public protests",
              "Sanctioning an attorney for submitting fictitious, ChatGPT-hallucinated case precedents",
              "Data sovereignty of personal health records in cloud storage",
              "Banning autonomous lethal weapons systems"
            ],
            correctIndex: 1,
            explanation: "Attorneys were sanctioned for submitting fake, non-existent ChatGPT citations, establishing absolute human advocate liability."
          }
        ]
      },
      {
        id: 4,
        rawId: 'ai-4',
        topic: 'ai-judiciary',
        isBoss: true,
        title: "BOSS: Regulation 43 & Conscience Dictum",
        subtitle: "Defend Article 21 and the Speaking Order Doctrine!",
        icon: "👑",
        unit: "Unit 2: Ethical Hazards & Legal Guardrails",
        unitColor: "#ec4899",
        bossName: "Algorithmic Black-Box Leviathan",
        bossHp: 1200,
        xpReward: 60,
        coinsReward: 250,
        tasks: [
          {
            type: "concept",
            title: "Regulation 43 & Absolute Accountability",
            content: "Regulation 43 establishes the mandatory disclosure requirement: legal counsels must affirmatively disclose whenever AI tools were utilized. Lawyers cannot blame 'ChatGPT error'.",
            keyTakeaway: "The law, after all, is not a mere algorithm; it is the reflection of human conscience."
          },
          mcqs[3] || {
            type: "mcq",
            prompt: "Under the proposed Supreme Court regulatory framework, 'Regulation 43' specifically deals with:",
            options: [
              "Mandatory deployment of ePOS devices in court registries",
              "Compulsory disclosure by legal counsels whenever AI tools were utilized in preparing court filings",
              "Allocation of ₹7,210 crore under e-Courts Phase III",
              "Live-streaming procedures for Constitution Bench hearings"
            ],
            correctIndex: 1,
            explanation: "Regulation 43 mandates proactive affirmative disclosure of AI usage in court filings."
          },
          {
            type: "tap_order",
            prompt: "Assemble the Supreme Court's golden closing dictum on AI:",
            tokens: ["The law, after all,", "is not a mere algorithm.", "It is the reflection", "of human conscience."],
            correctSentence: "The law, after all, is not a mere algorithm. It is the reflection of human conscience."
          }
        ]
      }
    ];
  }

  // Visual Flowcharts Repository for Mobile Viewer
  const flowcharts = {
    'fc-classification': {
      id: 'fc-classification',
      title: 'Composite Classification & Multipliers',
      file: 'assets/flowcharts/flowchart_msme_classification.svg',
      desc: 'Visual breakdown of Investment & Turnover ceilings (Micro ₹1Cr/₹5Cr, Small ₹10Cr/₹50Cr, Medium ₹50Cr/₹250Cr), 1:5 ratio, 2.5x multiplier, and export turnover exclusion.'
    },
    'fc-delayed-payments': {
      id: 'fc-delayed-payments',
      title: 'Delayed Payments & Section 43B(h)',
      file: 'assets/flowcharts/flowchart_delayed_payments.svg',
      desc: 'MSMED Act Sections 15-19: 15/45-day deadline, Section 16 compound interest at 3x RBI Bank Rate, MSEFC 90-day arbitration, 75% court pre-deposit, and Section 43B(h) tax disallowance.'
    },
    'fc-pm-vishwakarma': {
      id: 'fc-pm-vishwakarma',
      title: 'PM Vishwakarma 5-Pillar Architecture',
      file: 'assets/flowcharts/flowchart_pm_vishwakarma.svg',
      desc: '₹13,000 Cr Central Sector outlay, 18 traditional artisan trades, ₹15k precision toolkit, and ₹1L + ₹2L collateral-free enterprise credit at 5% concessional interest with 8% subvention.'
    },
    'fc-dwarfism': {
      id: 'fc-dwarfism',
      title: 'Dwarfism & Missing Middle vs. Mittelstand',
      file: 'assets/flowcharts/flowchart_dwarfism_vs_mittelstand.svg',
      desc: 'Economic Survey 2018-19: Inverted pyramid of 99.4% micro units vs German Mittelstand high-productivity model, and scale-neutral policy pathways.'
    }
  };

  // The 3 Playable Topics
  const topics = {
    'msme': {
      id: 'msme',
      title: 'MSME Reforms & Catalysts',
      badge: 'CAVA GS-3 (Desktop Synced)',
      description: '10 levels: Composite Criteria, Delayed Payments, 43B(h), PM Vishwakarma & Budget 2025.',
      color: '#3b82f6',
      icon: '🏭',
      flowcharts: ['fc-classification', 'fc-delayed-payments', 'fc-pm-vishwakarma', 'fc-dwarfism'],
      get levels() { return buildMsmeLevels(); }
    },
    'public-exams': {
      id: 'public-exams',
      title: 'Public Examinations & NTA Overhaul',
      badge: 'CAVA Lecture 4 (Desktop Synced)',
      description: '10 levels: Unfair Means Act 2024, Radhakrishnan Committee & NTA 24-staff paradox.',
      color: '#10b981',
      icon: '🏛️',
      flowcharts: [],
      get levels() { return buildPublicExamLevels(); }
    },
    'ai-judiciary': {
      id: 'ai-judiciary',
      title: 'AI in the Judiciary',
      badge: 'CAVA Lecture 3 (Desktop Synced)',
      description: '4 levels: Supreme Court 3-Tier AI Pyramid, Regulation 43 & Conscience Dictum.',
      color: '#6366f1',
      icon: '⚖️',
      flowcharts: [],
      get levels() { return buildAiJudiciaryLevels(); }
    }
  };

  // Backward compatible worlds builder
  function buildWorlds() {
    return [
      {
        id: "world-msme",
        topicId: "msme",
        name: "World 1: MSMEs as Catalysts",
        badge: "CAVA GS-3 (Desktop Synced)",
        description: "10 progressive levels: Composite Criteria, Delayed Payments, 43B(h), PM Vishwakarma & Budget 2025.",
        color: "#3b82f6",
        levels: buildMsmeLevels()
      },
      {
        id: "world-1",
        topicId: "public-exams",
        name: "World 2: Public Examinations & NTA Reforms",
        badge: "CAVA Lecture 4 (Desktop Synced)",
        description: "10 progressive levels directly synced with the desktop Duolingo learning model.",
        color: "#10b981",
        levels: buildPublicExamLevels()
      },
      {
        id: "world-2",
        topicId: "ai-judiciary",
        name: "World 3: AI in the Judiciary",
        badge: "CAVA Lecture 3 (Desktop Synced)",
        description: "Supreme Court Draft Regulations, 3-Tier AI Pyramid, and Regulation 43.",
        color: "#6366f1",
        levels: buildAiJudiciaryLevels()
      }
    ];
  }

  // Rapid-fire blitz statements (Comprehensive MSME + Public Exams + AI Judiciary)
  const blitzQuestions = [
    // MSME
    { q: "MSMEs contribute approximately 31.1% of India's GDP and 48.6% of merchandise exports.", ans: true },
    { q: "Export turnover is included when calculating the turnover limit under the 2020 MSME composite criteria.", ans: false },
    { q: "Section 16 of MSMED Act prescribes compound interest at 3 times the RBI Bank Rate for delayed payments.", ans: true },
    { q: "Section 43B(h) of the Income Tax Act applies equally to Micro, Small, and Medium enterprises.", ans: false },
    { q: "PM Vishwakarma provides collateral-free enterprise loans up to ₹3 Lakh at a subsidized 5% interest rate.", ans: true },
    { q: "In the 2020 composite criteria, the Turnover ceiling is exactly 5 times the Investment ceiling across all tiers.", ans: true },
    { q: "Under Budget 2025-26, the credit guarantee cover for MSME manufacturing machinery was set at up to ₹100 Crore.", ans: true },
    { q: "Over 99% of all MSMEs in India are classified as Medium enterprises.", ans: false },
    { q: "Section 19 of MSMED Act requires a defaulting buyer to pre-deposit 75% of the decreed amount before appealing in court.", ans: true },
    { q: "The Udyam Assist Platform (UAP) enables informal micro enterprises lacking GSTIN to access priority sector lending.", ans: true },
    { q: "Mudra loan ceiling under the Tarun Plus category was doubled from ₹10 Lakh to ₹20 Lakh in Budget 2025-26.", ans: true },

    // Public Exams
    { q: "Education was moved to Concurrent List (Entry 25) by 42nd CAA 1976.", ans: true },
    { q: "NTA conducts exams for 1.5 Crore students with only 24 permanent employees.", ans: true },
    { q: "Under the 2024 Act, candidates appearing for exams face mandatory 5 years in prison.", ans: false },
    { q: "The Chhattisgarh High Court observed that a paper leak is more heinous than murder.", ans: true },
    { q: "Gary Becker proved that severe punishment alone deters crime even with near-zero detection.", ans: false },
    { q: "Radhakrishnan Committee recommended hybrid digital lockboxes with 30-min transmission.", ans: true },
    { q: "NTA was established as a statutory constitutional body under Article 324.", ans: false },
    { q: "The 2026 Amendment heightened organized paper leak fines to a minimum of ₹1 Crore.", ans: true },

    // AI Judiciary
    { q: "India currently has approximately 21 judges per million population (target is 50).", ans: true },
    { q: "Supreme Court Red Tier permits automated algorithmic determination of criminal guilt.", ans: false },
    { q: "Regulation 43 mandates compulsory disclosure whenever AI tools are used in court filings.", ans: true },
    { q: "Speaking order doctrine requires judges to provide explainable written reasoning.", ans: true },
    { q: "SUVAS is an automated adjudicatory algorithm that delivers final Supreme Court verdicts.", ans: false }
  ];

  const shopItems = [
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
      id: "skin-msme",
      name: "Viksit Bharat Industrialist Badge",
      desc: "Unlock the MSME Catalyst Champion avatar.",
      price: 500,
      currency: "gems",
      icon: "🏭",
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
  ];

  const leaderboard = [
    { rank: 1, name: "Ananya Sharma (AIR 1)", score: 2840, league: "Diamond", avatar: "👩‍💼" },
    { rank: 2, name: "Vikramaditya (IPS Cadet)", score: 2620, league: "Diamond", avatar: "👮‍♂️" },
    { rank: 3, name: "Meera Nair (IAS Trainee)", score: 2490, league: "Diamond", avatar: "🏛️" },
    { rank: 4, name: "You (Aspirant)", score: 620, league: "Gold", avatar: "🧠", isUser: true },
    { rank: 5, name: "Rahul Verma (State PSC)", score: 580, league: "Gold", avatar: "🧑‍💻" },
    { rank: 6, name: "Sneha Patel (UPSC 2026)", score: 540, league: "Gold", avatar: "📖" },
    { rank: 7, name: "Karthik Raja (Prelims Pro)", score: 490, league: "Silver", avatar: "⚡" },
    { rank: 8, name: "Devansh Gupta", score: 410, league: "Silver", avatar: "🎯" }
  ];

  window.GAME_DATA = {
    topics,
    flowcharts,
    get worlds() {
      return buildWorlds();
    },
    blitzQuestions,
    shopItems,
    leaderboard
  };
})();
