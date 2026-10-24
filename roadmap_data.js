/**
 * CORTEX VISUAL ROADMAP DATA (ROADMAP.SH STYLE)
 * Structured hierarchy for CAVA Topics:
 * 1. Public Examinations & NTA Governance Overhaul
 * 2. Artificial Intelligence in Judiciary
 * 3. MSME Sector & MSMED Act 2026
 */

const ROADMAP_DATA = {
  "public-exams": {
    id: "public-exams",
    title: "Public Examinations & NTA Governance Overhaul",
    subject: "CAVA Lecture 4",
    syllabus: "GS-2: Governance, Transparency & Statutory Bodies",
    readTime: "15 min visual roadmap",
    sections: [
      {
        id: "trunk-1",
        title: "Constitutional & Moral Canvas",
        subtitle: "The Foundation of Examination Integrity",
        isCore: true,
        branches: [
          {
            id: "pe-b1",
            title: "Upward Social Mobility",
            shortDesc: "Sole objective merit ladder for rural & poor youth to break generational poverty.",
            tag: "Core Value",
            details: `
              <h4>Upward Social Mobility as a Democratic Anchor</h4>
              <p>In developing societies like India, public examinations serve as the single most vital institutional mechanism for <strong>intergenerational upward social mobility</strong>.</p>
              <div class="reading-callout">
                <strong>Socio-Economic Reality:</strong> Unlike private corporate hiring where social capital and elite networking dominate, competitive exams (UPSC, State PSCs, NEET) allow a farmer's or laborer's child to attain sovereign administrative and professional status solely on merit.
              </div>
              <p>When exams are compromised by paper leaks, it is not merely a procedural lapse—it constitutes <em>structural disenfranchisement</em> of the honest underprivileged youth.</p>
            `,
            quotes: ["\"Public employment based on merit is the crown jewel of our egalitarian Republic.\""],
            mainsTip: "Use upward mobility as your sociological anchor in Mains answer introduction."
          },
          {
            id: "pe-b2",
            title: "Chhattisgarh High Court Dictum",
            shortDesc: "Paper leak is more heinous than murder (murders dreams & faith of millions).",
            tag: "Judicial Precedent",
            details: `
              <h4>Chhattisgarh High Court Landmark Observation</h4>
              <p>In an iconic ruling on exam malpractice, the High Court observed:</p>
              <div class="reading-callout reading-callout-warning">
                <strong>The Quotation:</strong> <em>"A question paper leak is more heinous than murder. While murder kills a single individual, a paper leak murders the dreams, trust, aspirations, and future of millions of youth and destroys the nation's faith in meritocracy."</em>
              </div>
              <p><strong>Answer-Writing Utility:</strong> Provides an unforgettable opening hook for any 10-marker or 15-marker question on educational or exam integrity.</p>
            `,
            quotes: ["Chhattisgarh High Court: 'Paper leak is more heinous than murder'"],
            mainsTip: "Direct quote for high-impact intro or conclusion hook."
          },
          {
            id: "pe-b3",
            title: "Concurrent List (42nd CAA 1976)",
            shortDesc: "Entry 25: Shared constitutional obligation of Union & States.",
            tag: "Constitutional Law",
            details: `
              <h4>Constitutional Division of Powers</h4>
              <ul>
                <li><strong>42nd Constitutional Amendment Act (1976):</strong> Shifted 'Education' from the State List to the <strong>Concurrent List (Entry 25)</strong>.</li>
                <li><strong>Dual Accountability:</strong> Both Parliament and State Legislatures possess legislative competence to regulate examination standards and punish unfair means.</li>
                <li><strong>Federal Friction:</strong> State governments often resist central entrance tests (e.g. Tamil Nadu's anti-NEET stance) citing regional disparity in schooling boards.</li>
              </ul>
            `,
            quotes: ["7th Schedule: Concurrent List, Entry 25 - Education, including technical and medical education"],
            mainsTip: "Cite 42nd CAA when discussing cooperative federalism in education."
          },
          {
            id: "pe-b4",
            title: "Articles 14, 16 & 21A Framework",
            shortDesc: "Right to Equality, Equal Opportunity in Public Posts & Right to Education.",
            tag: "Fundamental Rights",
            details: `
              <h4>Fundamental Rights Invalidation by Leaks</h4>
              <ul>
                <li><strong>Article 14 (Equality Before Law):</strong> Arbitrary leaking of papers creates an unconstitutional classification between corrupt cartels and honest aspirants.</li>
                <li><strong>Article 16 (Equal Opportunity):</strong> Direct violation of equal opportunity in state employment.</li>
                <li><strong>Article 21A & DPSP (Art 45, 46):</strong> Directive to promote with special care the educational and economic interests of the weaker sections (SC/ST).</li>
              </ul>
            `,
            quotes: ["Supreme Court: 'Meritocracy without integrity is arbitrary under Article 14.'"],
            mainsTip: "Integrate Articles 14, 16, and 21A into the constitutional dimension."
          }
        ]
      },
      {
        id: "trunk-2",
        title: "The Crisis & NTA Paradox",
        subtitle: "Systemic Institutional Vulnerabilities",
        isCore: true,
        branches: [
          {
            id: "pe-b5",
            title: "The 24-Staff Paradox",
            shortDesc: "NTA conducts exams for 1.5 Cr candidates with only 24 permanent employees.",
            tag: "Institutional Deficit",
            details: `
              <h4>The Anatomy of Institutional Fragility</h4>
              <p>The <strong>National Testing Agency (NTA)</strong> conducts exams for over <strong>1.5 crore candidates annually</strong> across 250+ cycles, yet shockingly operates with a permanent core of only <strong>24 employees</strong>.</p>
              <ul>
                <li><strong>Heavy Outsourcing:</strong> Essential high-security tasks—transport of papers, printing, IT server hosting, invigilation, and center management—are delegated to private third-party contractors.</li>
                <li><strong>Accountability Vacuum:</strong> Private contractual staff lack sovereign civil service vetting or long-term stakes in institutional reputation.</li>
              </ul>
            `,
            quotes: ["24 permanent staff vs 1.5 crore examinees: A structural faultline"],
            mainsTip: "Must-cite statistic in Mains body paragraph on administrative bottlenecks."
          },
          {
            id: "pe-b6",
            title: "₹30-50 Lakh Seat Pricing",
            shortDesc: "EOU Bihar investigation: Organized paper leak mafias charging fortunes per seat.",
            tag: "Crime Economy",
            details: `
              <h4>Commercialization of Paper Leaks</h4>
              <p>Investigations by the <strong>Economic Offenses Unit (EOU) Bihar</strong> and central agencies revealed that paper leak cartels operated like corporate syndicates:</p>
              <ul>
                <li>Leaked answer keys and question papers were sold for <strong>₹30 lakh to ₹50 lakh per candidate</strong>.</li>
                <li>Safe houses and mock testing centers were rented near test locations to drill candidates on leaked answers hours before the test.</li>
                <li>Reveals that paper leaks are not student cheating; they are high-return organized financial crimes.</li>
              </ul>
            `,
            quotes: ["EOU Bihar: Seat leak pricing between ₹30L - ₹50L"],
            mainsTip: "Contrasts commercial syndicates with individual cheating."
          },
          {
            id: "pe-b7",
            title: "Registered Society Status",
            shortDesc: "NTA is merely a registered society under Societies Act 1860, not a statutory body.",
            tag: "Legal Status",
            details: `
              <h4>Absence of Statutory Autonomy</h4>
              <p>NTA was constituted in 2018 as an autonomous society registered under the <em>Societies Registration Act, 1860</em>.</p>
              <ul>
                <li><strong>The Consequence:</strong> It lacks the legislative authority, parliamentary oversight, statutory powers, and regulatory teeth that constitutional/statutory bodies like UPSC or UGC enjoy.</li>
                <li><strong>Reform Need:</strong> Must be reconstituted through an Act of Parliament with permanent civil cadre and strict security clearances.</li>
              </ul>
            `,
            quotes: ["Societies Registration Act 1860 vs Statutory Authority"],
            mainsTip: "Primary structural recommendation: transform NTA via parliamentary statute."
          }
        ]
      },
      {
        id: "trunk-3",
        title: "The Legal Fortress (2024 & 2026 Acts)",
        subtitle: "Criminal Deterrence & Economic Theory of Crime",
        isCore: true,
        branches: [
          {
            id: "pe-b8",
            title: "Student Exemption Safeguard",
            shortDesc: "Bona fide candidates protected from criminal prosecution; syndicates targeted.",
            tag: "Statutory Protection",
            details: `
              <h4>Protecting Honest Aspirants</h4>
              <p>Under the <strong>Public Examinations (Prevention of Unfair Means) Act 2024</strong>:</p>
              <ul>
                <li><strong>No Criminal Harassment of Students:</strong> Candidates appearing for exams are deliberately excluded from the penal provisions of the Act. They remain governed by administrative debarment rules of the testing body.</li>
                <li><strong>Syndicate Focus:</strong> Criminal provisions apply strictly to question printing presses, paper transit managers, corrupt service providers, and organized cheating cartels.</li>
              </ul>
            `,
            quotes: ["Public Examinations Act 2024: Zero criminalization of bona fide examinees"],
            mainsTip: "Critical distinction to highlight in legal analysis."
          },
          {
            id: "pe-b9",
            title: "7-10 Yrs Prison & ₹1 Cr Fine",
            shortDesc: "2026 Amendment heightened penalties with mandatory attachment of property.",
            tag: "Penal Provisions",
            details: `
              <h4>Criminal Escalation</h4>
              <ul>
                <li><strong>Organized Crime:</strong> Minimum 5 to 10 years imprisonment and fine of at least <strong>₹1 Crore</strong>.</li>
                <li><strong>2026 Amendment:</strong> Increased individual facilitation sentences to <strong>7 to 10 years</strong>; offenses made strictly non-bailable, non-compoundable, and cognizable.</li>
                <li><strong>Asset Forfeiture:</strong> Attachment and confiscation of ill-gotten properties belonging to cheating networks.</li>
              </ul>
            `,
            quotes: ["Non-bailable, cognizable, with mandatory asset recovery"],
            mainsTip: "Cite 2026 amendments when discussing deterrence."
          },
          {
            id: "pe-b10",
            title: "Becker's Deterrence Economics",
            shortDesc: "Severe punishment fails without high detection probability & swift conviction.",
            tag: "Economic Theory",
            details: `
              <h4>Gary Becker's Economics of Crime</h4>
              <p>Nobel Laureate Gary Becker's economic model posits:</p>
              <div class="reading-callout">
                <strong>Deterrence Formula:</strong> <em>Expected Penalty = Severity of Punishment × Probability of Detection × Speed of Conviction.</em>
              </div>
              <p>Even if punishment is life imprisonment, if the detection probability is only 5%, syndicates making ₹50 Crore will happily take the gamble. Hence, forensic auditing, digital locks, and Special Fast-Track Courts are far more crucial than just writing harsh laws on paper.</p>
            `,
            quotes: ["Becker: 'Deterrence requires high probability of capture, not just severity.'"],
            mainsTip: "Award-winning theoretical point for GS-2 & GS-4 governance answers."
          }
        ]
      },
      {
        id: "trunk-4",
        title: "K. Radhakrishnan Committee Blueprint",
        subtitle: "The 7 Pillars of Transformation",
        isCore: true,
        branches: [
          {
            id: "pe-b11",
            title: "Statutory NTA Restructuring",
            shortDesc: "Statutory body with permanent IT security, psychometric & logistics cadres.",
            tag: "Panel Pillar 1",
            details: `
              <h4>Pillar 1: Institutional Renaissance</h4>
              <p>The 7-member panel chaired by <strong>Dr. K. Radhakrishnan</strong> (former ISRO Chairman) recommended:</p>
              <ul>
                <li>Pass a dedicated parliamentary Act to grant NTA statutory status.</li>
                <li>Build an in-house permanent professional cadre in place of contractual employees.</li>
                <li>Separate test curation and psychometrics from ground logistics.</li>
              </ul>
            `,
            quotes: ["Dr. K. Radhakrishnan Committee: Professionalize NTA on ISRO standards"],
            mainsTip: "Top recommendation for institutional reform."
          },
          {
            id: "pe-b12",
            title: "Two-Stage Testing (Prelims + Mains)",
            shortDesc: "Screening stage eliminates single-day high-stakes bottleneck.",
            tag: "Panel Pillar 2",
            details: `
              <h4>Pillar 2: Multi-Stage Filtering</h4>
              <ul>
                <li><strong>Problem with Single Day:</strong> Cramming 24 lakh candidates into one 3-hour window once a year creates astronomical pressure and massive leak incentives.</li>
                <li><strong>Two-Stage Model:</strong> Conduct a Stage-1 qualifying screening test, followed by a Stage-2 proctored Mains test for shortlisted candidates, drastically reducing logistical exposure.</li>
              </ul>
            `,
            quotes: ["Shift from monolithic one-shot exams to two-stage filtering"],
            mainsTip: "Solves both logistical strain and leak incentives."
          },
          {
            id: "pe-b13",
            title: "Hybrid Digital Lockboxes",
            shortDesc: "Encrypted transmission 30 mins before test; zero physical storage latency.",
            tag: "Panel Pillar 3",
            details: `
              <h4>Pillar 3: The End of Physical Paper Leaks</h4>
              <p>Traditional papers sit in bank vaults and courier trucks for days. In the <strong>Hybrid Testing Model</strong>:</p>
              <ul>
                <li>Encrypted question data packets transmitted digitally to test centers only <strong>30 minutes before exam time</strong>.</li>
                <li>Decrypted using dual multi-factor keys shared simultaneously with the Center Superintendent.</li>
                <li>Eliminates physical transit and vault storage vulnerabilities completely.</li>
              </ul>
            `,
            quotes: ["Zero storage latency = Zero physical paper leaks"],
            mainsTip: "Key technological solution to cite in Way Forward."
          },
          {
            id: "pe-b14",
            title: "Accredited Government Centers Only",
            shortDesc: "Bar private commercial labs; utilize Kendriya Vidyalayas, Navodayas & Universities.",
            tag: "Panel Pillar 4",
            details: `
              <h4>Pillar 4: Trusted Physical Infrastructure</h4>
              <ul>
                <li>Completely bar unvetted private computer labs and rented private schools.</li>
                <li>Mandate testing exclusively at <strong>Kendriya Vidyalayas (KVs), Jawahar Navodaya Vidyalayas (JNVs), and State/Central Universities</strong> with CCTV integration.</li>
              </ul>
            `,
            quotes: ["Utilize public educational infrastructure for public testing integrity"],
            mainsTip: "Eliminates private cyber cafe hacking nexus."
          }
        ]
      },
      {
        id: "trunk-5",
        title: "Global Benchmarks & Mains Synthesis",
        subtitle: "Comparative Strategy & Answer Framework",
        isCore: true,
        branches: [
          {
            id: "pe-b15",
            title: "China Gaokao vs Western SAT/GRE",
            shortDesc: "Military escort & jammers vs multiple annual attempts & adaptive testing.",
            tag: "Global Models",
            details: `
              <h4>International Testing Comparisons</h4>
              <ul>
                <li><strong>China (Gaokao):</strong> Heavily militarized. Armed police escorts for test papers, drone radio-signal jammers, facial recognition, and up to 7 years imprisonment under criminal code.</li>
                <li><strong>USA / UK (SAT / A-Levels):** Multiple testing dates each year (4-6 windows), computerized adaptive question generation, and school assessment weightage. Eliminates the desperate fear of losing an entire year.</li>
              </ul>
            `,
            quotes: ["India requires technological rigor paired with multi-attempt psychological relief"],
            mainsTip: "Use global examples to earn 1-2 extra marks in comparison."
          },
          {
            id: "pe-b16",
            title: "The Mains Master Conclusion",
            shortDesc: "Covenant of meritocracy; technology as enabler; human trust restored.",
            tag: "Mains Conclusion",
            details: `
              <h4>Final Synthesis for Mains Answer Writing</h4>
              <div class="reading-callout">
                <strong>Concluding Dictum:</strong> <em>"Safeguarding examination integrity is not merely an administrative exercise in logistical efficiency; it is a sacred constitutional covenant that protects the democratic trust, dreams, and upward social mobility of India's youth. Implementing the Radhakrishnan Committee blueprint with statutory autonomy is the sine qua non for restoring faith in meritocracy."</em>
              </div>
            `,
            quotes: ["Examination integrity is the cornerstone of democratic meritocracy"],
            mainsTip: "Ready-to-use concluding paragraph for UPSC GS-2."
          }
        ]
      }
    ]
  },

  "ai-judiciary": {
    id: "ai-judiciary",
    title: "Artificial Intelligence in Judiciary",
    subject: "CAVA Lecture 3",
    syllabus: "GS-2: Structure & Independence of Judiciary | GS-3: Emerging Tech",
    readTime: "12 min visual roadmap",
    sections: [
      {
        id: "ai-trunk-1",
        title: "Introductory Framing & Backlog Reality",
        subtitle: "The Operational Imperative for AI",
        isCore: true,
        branches: [
          {
            id: "ai-b1",
            title: "5 Crore Pending Cases Reality",
            shortDesc: "4.3-4.4 Cr in lower courts, 60L in HCs, >80k in Supreme Court (NJDG).",
            tag: "Backlog Data",
            details: `<h4>5.1 Crore Cases Gridlock</h4><p>NJDG reports over 87% pendency in subordinate district courts. AI is needed to accelerate procedural turnarounds and registry defect detection.</p>`,
            quotes: ["5+ crore pending cases in Indian courts"],
            mainsTip: "Anchor question on judicial speed with NJDG statistics."
          },
          {
            id: "ai-b2",
            title: "21 Judges / Million Paradox",
            shortDesc: "Critically below Law Commission 1987 target of 50/M (USA: 150/M, Europe: 220/M).",
            tag: "Human Resource",
            details: `<h4>Severe Human Capital Deficit</h4><p>India operates with only 21 judges per million citizens, highlighting why technological assistance is an urgent priority.</p>`,
            quotes: ["Law Commission (1987): Target of 50 judges per million population"],
            mainsTip: "Use to justify why assistive AI is unavoidable."
          },
          {
            id: "ai-b3",
            title: "NCLT Fake Precedent Alarm",
            shortDesc: "SC: 'Using AI-hallucinated citations in court is like release of toxic Methyl Isocyanate gas!'",
            tag: "Apex Warning",
            details: `<h4>The Hallucination Precedent</h4><p>Advocates citing fictitious ChatGPT citations prompted the Apex Court to establish zero-tolerance against algorithmic hallucination in court filings.</p>`,
            quotes: ["SC: 'AI hallucinations in court are like toxic Methyl Isocyanate gas'"],
            mainsTip: "Unbeatable introduction hook for AI in Judiciary answers."
          }
        ]
      },
      {
        id: "ai-trunk-2",
        title: "The Supreme Court AI Pyramid",
        subtitle: "Three-Tier Regulatory Framework",
        isCore: true,
        branches: [
          {
            id: "ai-b4",
            title: "Green Tier: Allowed & Encouraged",
            shortDesc: "Case management, cause-list automation, defect checking, OCR digitisation.",
            tag: "Administrative AI",
            details: `<h4>Green Tier: Administrative Velocity</h4><p>Registry tasks, intelligent case listing, docket categorization, and flagging 5-10+ year cases.</p>`,
            quotes: ["Green Tier: Administrative AI without adjudicatory discretion"],
            mainsTip: "Explain administrative dividends here."
          },
          {
            id: "ai-b5",
            title: "Amber Tier: Cautious Research & Translation",
            shortDesc: "SUPACE & SUVAS; strict verification required (risk of 'Leave granted' -> 'छुट्टी स्वीकार है').",
            tag: "Assistive AI",
            details: `<h4>Amber Tier: Assistive Research</h4><p>SUPACE fact summarization and SUVAS translation (Article 39A). Human proofreading is mandatory to prevent translation distortion.</p>`,
            quotes: ["Amber Tier: Cautious research with mandatory human verification"],
            mainsTip: "Illustrate with the 'Leave granted' mistranslation case."
          },
          {
            id: "ai-b6",
            title: "Red Tier: Strictly Prohibited",
            shortDesc: "Automated adjudication, determining guilt & sentencing strictly banned.",
            tag: "Banned Adjudication",
            details: `<h4>Red Tier: Sovereign Decision-Making</h4><p>Core judicial functions demand moral reasoning, remorse evaluation, and human empathy that algorithms cannot possess.</p>`,
            quotes: ["Red Tier: Complete prohibition of algorithmic adjudication"],
            mainsTip: "Core constitutional constraint defending Article 21."
          }
        ]
      },
      {
        id: "ai-trunk-3",
        title: "Constitutional & Ethical Dilemmas",
        subtitle: "Article 21, Natural Justice & Black Box AI",
        isCore: true,
        branches: [
          {
            id: "ai-b7",
            title: "The Black Box Conundrum",
            shortDesc: "Neural opacity conflicts with Natural Justice mandate for 'reasoned speaking orders'.",
            tag: "Natural Justice",
            details: `<h4>Algorithmic Inscrutability</h4><p>Administrative law demands that judges give reasons. A deep learning black-box cannot explain its weights, violating natural justice.</p>`,
            quotes: ["Speaking order doctrine vs Black-Box neural opacity"],
            mainsTip: "Directly relates to administrative law principles."
          },
          {
            id: "ai-b8",
            title: "Re-encoding Historical Bias",
            shortDesc: "COMPAS precedent: Predictive scoring risk penalizing marginalized communities.",
            tag: "Constitutional Bias",
            details: `<h4>Predictive Injustice</h4><p>Training models on historical policing data risks institutionalizing discrimination against marginalized groups under Article 14.</p>`,
            quotes: ["COMPAS US precedent: Algorithmic bias in bail recidivism"],
            mainsTip: "Draw analogy to British Criminal Tribes labeling."
          },
          {
            id: "ai-b9",
            title: "Digital Divide 1.0 vs 2.0",
            shortDesc: "Divide 1.0 (device access) vs Divide 2.0 (literacy, cyber hygiene & digital arrest scams).",
            tag: "Social Justice",
            details: `<h4>The New Digital Chasm</h4><p>Virtual courts risk excluding rural litigants lacking digital literacy and cyber hygiene.</p>`,
            quotes: ["Digital Divide 2.0: Literacy & cyber hygiene disparities"],
            mainsTip: "Highlight why tech adoption must remain inclusive."
          }
        ]
      },
      {
        id: "ai-trunk-4",
        title: "Regulatory Safeguards & Way Forward",
        subtitle: "Human-in-the-Loop Governance",
        isCore: true,
        branches: [
          {
            id: "ai-b10",
            title: "Regulation 43 & Absolute Accountability",
            shortDesc: "Mandatory disclosure when AI used; human lawyers retain 100% liability.",
            tag: "SC Regulations",
            details: `<h4>Regulation 43 of Draft Rules</h4><p>Lawyers must disclose AI use; cannot blame 'ChatGPT error' (Mata v. Avianca precedent).</p>`,
            quotes: ["Regulation 43: Mandatory affirmative disclosure"],
            mainsTip: "Key regulatory provision to cite."
          },
          {
            id: "ai-b11",
            title: "CORE AI & Swadeshi Jurisprudence",
            shortDesc: "SC Center of Research & Excellence on AI; indigenous sovereign models.",
            tag: "Institutional Reform",
            details: `<h4>Technological Sovereignty</h4><p>Building native foundation models trained on Indian statutes preserves data sovereignty under the DPDP Act.</p>`,
            quotes: ["CORE AI at Supreme Court & Swadeshi AI sovereignty"],
            mainsTip: "Key technological recommendation."
          },
          {
            id: "ai-b12",
            title: "The Human Conscience Dictum",
            shortDesc: "'The law is not a mere algorithm; it is the reflection of human conscience.'",
            tag: "Master Conclusion",
            details: `<h4>The Concluding Dictum</h4><p>Technology must augment, not replace, the discernment of the human Bench. The heart of justice remains human.</p>`,
            quotes: ["Supreme Court: 'The law, after all, is not a mere algorithm.'"],
            mainsTip: "Golden conclusion quote."
          }
        ]
      }
    ]
  },
  "msme": {
    id: "msme",
    title: "MSMEs as Catalysts: Growth Engine, Creative Destruction & Budget Reforms",
    subject: "CAVA Lecture 4",
    syllabus: "GS-3: Indian Economy, Industrial Policy & Mobilization of Resources",
    readTime: "18 min visual roadmap",
    sections: [
      {
        id: "msme-trunk-1",
        title: "Macro Bedrock & Employment Footprint",
        subtitle: "The 31.1% Engine of Indian Growth",
        isCore: true,
        branches: [
          {
            id: "msme-b1",
            title: "The 31.1% GDP & 35.4% GVA Bedrock",
            shortDesc: "MSMEs drive 31.1% of national GDP, 35.4% of manufacturing GVA, and 48.6% of merchandise exports.",
            tag: "Macro Pillar",
            details: `
              <h4>The Bedrock of India's Economic Architecture</h4>
              <p>Official data and CAVA Lecture 4 establish that any MSME answer must open with precise macro data:</p>
              <div class="reading-callout">
                <strong>Macro Statistics:</strong>
                <ul>
                  <li><strong>31.1%</strong> of India's Gross Domestic Product (GDP)</li>
                  <li><strong>35.4%</strong> of Manufacturing Gross Value Added (GVA)</li>
                  <li><strong>48.6%</strong> of Total Merchandise Exports</li>
                  <li><strong>Over 11.1 Crore jobs</strong> across 6.33 crore enterprises</li>
                </ul>
              </div>
              <p>MSMEs generate 4x more employment per unit of capital invested compared to large-scale organized manufacturing corporations.</p>
            `,
            quotes: ["\"MSME means data has to be there. No other introduction, whatever be the MSME question!\" - CAVA 4"],
            mainsTip: "Use 31.1% GDP + 48.6% Exports as your opening data hook."
          },
          {
            id: "msme-b2",
            title: "51.2% Rural Social Footprint",
            shortDesc: "Decentralized regional growth preventing distress urban migration; high SC/ST/OBC ownership.",
            tag: "Inclusive Growth",
            details: `
              <h4>Democratization of Employment & Rural Decentralization</h4>
              <p>More than <strong>51.2% of MSMEs are situated in rural hinterlands</strong>, making the sector the foremost driver of decentralized, balanced regional development.</p>
              <div class="reading-callout reading-callout-warning">
                <strong>Social Equity Anchor:</strong> Substantial ownership among SC, ST, and Women entrepreneurs enables direct wealth generation and prevents forced distress migration to congested Tier-1 megacities.
              </div>
            `,
            quotes: ["Over 51% of MSMEs are rural, anchoring decentralized regional growth."],
            mainsTip: "Connect to inclusive growth and distress migration mitigation."
          },
          {
            id: "msme-b3",
            title: "Composite Classification Matrix (2020)",
            shortDesc: "Investment & Turnover dual ceilings (1/5, 10/50, 50/250) with statutory exclusion of exports.",
            tag: "Statutory Matrix",
            details: `
              <h4>Unified Composite Criteria (July 1, 2020)</h4>
              <p>Abolished the legacy manufacturing vs service dichotomy, adopting a dual Investment AND Turnover test:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>Micro:</strong> Investment ≤ ₹1 Cr | Turnover ≤ ₹5 Cr</li>
                  <li><strong>Small:</strong> Investment ≤ ₹10 Cr | Turnover ≤ ₹50 Cr</li>
                  <li><strong>Medium:</strong> Investment ≤ ₹50 Cr | Turnover ≤ ₹250 Cr</li>
                </ul>
                <p><strong>Golden Rule:</strong> Export turnover is statutorily EXCLUDED to incentivize global competitiveness.</p>
              </div>
            `,
            quotes: ["Export turnover is strictly excluded from classification ceilings."],
            mainsTip: "Highlight the 1:5 ratio and export exclusion rule."
          }
        ]
      },
      {
        id: "msme-trunk-2",
        title: "Structural Dilemmas: Dwarfism & Creative Destruction",
        subtitle: "The Missing Middle vs. German Mittelstand",
        isCore: true,
        branches: [
          {
            id: "msme-b4",
            title: "Joseph Schumpeter's Creative Destruction",
            shortDesc: "Market process where dynamic innovators displace obsolete firms, hindered by exit barriers and subsidies.",
            tag: "Core Economic Concept",
            details: `
              <h4>Creative Destruction (Joseph Schumpeter)</h4>
              <p>As emphasized in CAVA Lecture 4, <em>Creative Destruction</em> describes the continuous process of industrial mutation where technologically dynamic innovators displace obsolete, inefficient enterprises.</p>
              <div class="reading-callout reading-callout-warning">
                <strong>The Indian Paradox:</strong> When bankruptcy, labor laws, and insolvency exit barriers prevent unviable firms from closing down, capital and labor remain trapped in unproductive units, blocking creative destruction.
              </div>
            `,
            quotes: ["Joseph Schumpeter: 'Destructing the obsolete to create the innovative new.'"],
            mainsTip: "Anchor analytical questions on exit policy and IBC with Schumpeter's creative destruction."
          },
          {
            id: "msme-b5",
            title: "Dwarfs vs. Infant Enterprises (Eco Survey)",
            shortDesc: "Firms staying small for decades to retain subsidies vs young firms growing exponentially.",
            tag: "Economic Survey Thesis",
            details: `
              <h4>Dwarfs vs Infants (Economic Survey 2018-19)</h4>
              <p>Chief Economic Adviser Krishnamurthy Subramanian highlighted:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>Infant Enterprises:</strong> Young firms that start small but rapidly scale in productivity, employment, and technology.</li>
                  <li><strong>Dwarf Enterprises:</strong> Firms that remain small despite being in business for over 10-20 years!</li>
                </ul>
                <p>Over 99.4% of units remain micro; only 0.08% are medium—creating the infamous 'Missing Middle'.</p>
              </div>
            `,
            quotes: ["Economic Survey: Subsidize infant firms with sunset clauses, not perpetual dwarfs."],
            mainsTip: "Use the dwarfism thesis to critique indefinite size-based reservations."
          },
          {
            id: "msme-b6",
            title: "The German 'Mittelstand' Benchmark",
            shortDesc: "Scale-neutral incentives, dual technical vocational education, and global niche export champions.",
            tag: "Global Best Practice",
            details: `
              <h4>The Mittelstand Blueprint for India</h4>
              <p>Germany's world-leading industrial backbone relies on medium-sized family-owned firms (Mittelstand) characterized by:</p>
              <div class="reading-callout">
                <ul>
                  <li>Scale-neutral regulatory compliance and tax regimes</li>
                  <li>Dual vocational apprenticeship systems linking technical institutes to shop floors</li>
                  <li>Deep niche specialization dominating global B2B export supply chains</li>
                </ul>
              </div>
            `,
            quotes: ["German Mittelstand: Scale-neutral support creates global niche champions."],
            mainsTip: "Propose Mittelstand adoption in Way Forward for GS-3 industrial policy."
          }
        ]
      },
      {
        id: "msme-trunk-3",
        title: "Statutory Fortress: MSMED Act & Section 43B(h)",
        subtitle: "Solving Delayed Payments & Working Capital Asphyxiation",
        isCore: true,
        branches: [
          {
            id: "msme-b7",
            title: "MSMED Act Sections 15 to 19",
            shortDesc: "15-day default, 45-day ceiling, 3x RBI Bank Rate compounding interest, and MSEFC 90-day arbitration.",
            tag: "Statutory Teeth",
            details: `
              <h4>The Delayed Payments Statutory Code</h4>
              <p>Sections 15 to 19 of the MSMED Act, 2006 provide powerful protection for micro and small suppliers:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>Section 15:</strong> Mandatory payment within agreed timeline (max 45 days) or 15 days by default.</li>
                  <li><strong>Section 16:</strong> Penal compound interest with monthly rests at <strong>3x the RBI Bank Rate</strong>.</li>
                  <li><strong>Section 18:</strong> MSEFC conciliation/arbitration within 90 days.</li>
                  <li><strong>Section 19:</strong> Mandatory 75% pre-deposit by buyer before challenging any MSEFC award.</li>
                  <li><strong>Section 23:</strong> Penal interest cannot be claimed as tax-deductible expenditure.</li>
                </ul>
              </div>
            `,
            quotes: ["Section 16 compound penal interest at 3x RBI Bank Rate is non-waivable."],
            mainsTip: "Cite Sections 15, 16, and 19 for any question on MSME liquidity."
          },
          {
            id: "msme-b8",
            title: "Section 43B(h) Income Tax Revolution",
            shortDesc: "Finance Act 2023: Tax deduction disallowed for corporate buyers delaying MSE payment past 45 days.",
            tag: "Tax Law Game Changer",
            details: `
              <h4>Section 43B(h) of Income Tax Act (AY 2024-25)</h4>
              <p>Direct tax deduction is conditioned upon timely payment to Micro and Small suppliers:</p>
              <div class="reading-callout reading-callout-warning">
                <strong>Statutory Mechanism:</strong> If a buyer fails to pay a registered MSE within 45 days, the entire purchase amount is disallowed as a business deduction in that fiscal year, forcing income tax liability!
                <br><br>
                <strong>Nuances:</strong> Applies only to Micro and Small entities (Medium excluded; retail traders excluded unless registered manufacturers).
              </div>
            `,
            quotes: ["Section 43B(h): Transforming delayed payment from civil breach to tax disallowance."],
            mainsTip: "Highlight Section 43B(h) as an effective behavioral nudge."
          }
        ]
      },
      {
        id: "msme-trunk-4",
        title: "Union Budget 2025-26 & Credit Underwriting",
        subtitle: "Dismantling the ₹30 Lakh Crore Credit Deficit",
        isCore: true,
        branches: [
          {
            id: "msme-b9",
            title: "₹100 Cr Manufacturing Term Loan Guarantee",
            shortDesc: "Self-financing guarantee fund providing collateral-free credit cover up to ₹100 Crore for machinery.",
            tag: "Budget 2025 Reform",
            details: `
              <h4>Budget 2025-26 Credit Guarantee Architecture</h4>
              <p>Union Budget 2025-26 directly attacked the physical collateral bottleneck:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>₹100 Cr Guarantee Fund:</strong> Self-financing guarantee providing collateral-free cover for term loans up to ₹100 Cr to purchase machinery and equipment.</li>
                  <li><strong>CGTMSE Doubling:</strong> Normal guarantee cover under CGTMSE doubled from ₹5 Cr to ₹10 Cr.</li>
                  <li><strong>Digital Footprint Underwriting:</strong> PSBs shift from immovable land mortgages to scoring GST returns and TReDS invoices.</li>
                </ul>
              </div>
            `,
            quotes: ["Union Budget 2025-26: Shifting from balance-sheet mortgage to cash-flow underwriting."],
            mainsTip: "Prime data point for Budget 2025-26 economic governance answers."
          },
          {
            id: "msme-b10",
            title: "PM Vishwakarma 5-Pillar Architecture",
            shortDesc: "₹13,000 Cr Central Sector Scheme covering 18 artisan trades with ₹15k toolkits and 5% credit.",
            tag: "Artisan Empowerment",
            details: `
              <h4>PM Vishwakarma Central Sector Scheme</h4>
              <p>Launched on Vishwakarma Jayanti with ₹13,000 Crore outlay for 18 traditional artisan trades:</p>
              <div class="reading-callout">
                <ol>
                  <li>Recognition: PM Vishwakarma Certificate & Digital ID</li>
                  <li>Skill Upgradation: 5-7 days basic (₹500/day stipend) + 15 days advanced</li>
                  <li>Toolkit Grant: ₹15,000 modern e-voucher</li>
                  <li>Credit: Collateral-free ₹1L + ₹2L at 5% concessional interest (8% subvention)</li>
                  <li>Digital Incentives & GeM/ONDC market linkages</li>
                </ol>
              </div>
            `,
            quotes: ["PM Vishwakarma: Preserving guru-shishya parampara with Industry 4.0 market linkages."],
            mainsTip: "Comprehensive case study for rural artisanal industrialization."
          },
          {
            id: "msme-b11",
            title: "TReDS Mandatory Onboarding & Mudra Tarun Plus",
            shortDesc: "Turnover ceiling lowered to ₹500 Cr for buyers; Mudra Tarun ceiling doubled to ₹20 Lakh.",
            tag: "Liquidity Ecosystem",
            details: `
              <h4>Receivables Liquidity & Mudra Expansion</h4>
              <p>Expanding liquidity pipelines for small entrepreneurs:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>TReDS Mandate:</strong> Lowered turnover threshold for mandatory corporate buyer onboarding to ₹500 Crore.</li>
                  <li><strong>Mudra 'Tarun Plus':</strong> Ceiling doubled from ₹10 Lakh to ₹20 Lakh for entrepreneurs with good repayment track records.</li>
                  <li><strong>UAP Platform:</strong> Enabled 1.5+ crore informal micro units to obtain priority sector lending certificates without GSTIN.</li>
                </ul>
              </div>
            `,
            quotes: ["TReDS securitisation turns unpaid bills into immediate working capital."],
            mainsTip: "Cite TReDS and Mudra Tarun Plus for financial inclusion questions."
          }
        ]
      },
      {
        id: "msme-trunk-5",
        title: "Cluster Agglomeration & Viksit Bharat 2047",
        subtitle: "Collective Scale, Cross-Border E-Commerce & Article 39",
        isCore: true,
        branches: [
          {
            id: "msme-b12",
            title: "The Tiruppur Miracle & SFURTI Clusters",
            shortDesc: "Shared effluent infrastructure, common facilities, and $4B knitwear exports.",
            tag: "Cluster Economics",
            details: `
              <h4>Cluster Agglomeration: Converting Weakness into Power</h4>
              <p>Individual micro units cannot afford advanced testing or effluent treatment. Industrial clustering solves this:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>Tiruppur Cluster:</strong> Over $4 Billion knitwear exports achieved through Common Effluent Treatment Plants (CETPs) with Zero Liquid Discharge (ZLD).</li>
                  <li><strong>SFURTI Scheme:</strong> Up to ₹5 Crore assistance to establish Common Facility Centers (CFCs) for traditional khadi, coir, and agro-processing clusters.</li>
                </ul>
              </div>
            `,
            quotes: ["Clusters turn atomized individual weakness into collective industrial power."],
            mainsTip: "Use Tiruppur as your primary cluster agglomeration example."
          },
          {
            id: "msme-b13",
            title: "E-Commerce Export Hubs (ECEH) & ONDC",
            shortDesc: "Public-private bonded export hubs, customs pre-clearance, and unbundled digital e-commerce.",
            tag: "Digital Trade",
            details: `
              <h4>Democratizing Digital Trade & Cross-Border Logistics</h4>
              <p>Breaking intermediary monopolies through open digital public infrastructure:</p>
              <div class="reading-callout">
                <ul>
                  <li><strong>ONDC:</strong> Unbundles e-commerce value chains so local artisans sell to buyers across multiple consumer apps without 30% platform monopolies.</li>
                  <li><strong>E-Commerce Export Hubs (ECEH):</strong> Bonded warehousing, automated regulatory clearances, and return-processing logistics in PPP mode.</li>
                </ul>
              </div>
            `,
            quotes: ["ONDC unbundles the e-commerce stack to liberate artisans from platform rent-seeking."],
            mainsTip: "Cite ONDC and ECEHs for digital economy and export questions."
          },
          {
            id: "msme-b14",
            title: "Viksit Bharat 2047 & Article 39(b)-(c)",
            shortDesc: "\"MSMEs are the crucible where Indian entrepreneurship meets global manufacturing excellence.\"",
            tag: "Master Thesis Hook",
            details: `
              <h4>Constitutional Vision & Concluding Synthesis</h4>
              <p>Under <strong>Directive Principles Articles 39(b) and 39(c)</strong>, the State must distribute material resources to serve the common good and prevent concentration of economic power.</p>
              <div class="reading-callout reading-callout-warning">
                <strong>The Golden Conclusion:</strong>
                <em>"MSMEs are not just a safety valve for surplus agricultural labor; they are the crucible where Indian entrepreneurship meets global manufacturing excellence. Unleashing them from dwarfism is the paramount prerequisite for India's $5 Trillion economy and Viksit Bharat 2047."</em>
              </div>
            `,
            quotes: ["\"MSMEs are the crucible where Indian entrepreneurship meets global manufacturing excellence.\""],
            mainsTip: "Memorize this concluding thesis for GS-3 economy answers."
          }
        ]
      }
    ]
  }
};
