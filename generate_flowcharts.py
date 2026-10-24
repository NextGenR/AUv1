"""
Generate high-resolution SVG visual flowcharts for the MSME chapter:
1. flowchart_msme_classification.svg
2. flowchart_delayed_payments.svg
3. flowchart_pm_vishwakarma.svg
4. flowchart_dwarfism_vs_mittelstand.svg

Saves to both:
- d:\\Anki_Upgraded\\Raw_questions_CAVA\\Filtered_questions\\
- d:\\Anki_Upgraded\\Filtered_Questions\\
- d:\\Anki_Upgraded\\mobile\\assets\\flowcharts\\
"""

import os

fc1_classification = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 620" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#070a12"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
    <linearGradient id="microGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#059669"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
    <linearGradient id="smallGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb"/>
      <stop offset="100%" stop-color="#3b82f6"/>
    </linearGradient>
    <linearGradient id="medGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="100%" stop-color="#8b5cf6"/>
    </linearGradient>
    <linearGradient id="bannerGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.5"/>
    </filter>
  </defs>

  <!-- Background Canvas -->
  <rect width="900" height="620" rx="28" fill="url(#bgGrad)"/>
  <rect x="2" y="2" width="896" height="616" rx="26" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>

  <!-- Header Section -->
  <g transform="translate(40, 35)">
    <rect x="0" y="0" width="140" height="26" rx="13" fill="rgba(44,117,255,0.2)" stroke="#2c75ff" stroke-width="1.5"/>
    <text x="70" y="17" fill="#60a5fa" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="1">UPSC CAVA • MSME</text>
    <text x="0" y="60" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="26" font-weight="900">MSME Composite Classification Architecture</text>
    <text x="0" y="85" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">Statutory Framework: MSMED Act 2020 Baseline vs. Union Budget 2025-26 Scaling Multipliers</text>
  </g>

  <!-- Highlight Banner: Budget 2025-26 Multipliers -->
  <g transform="translate(40, 145)" filter="url(#shadow)">
    <rect width="820" height="54" rx="16" fill="url(#bannerGrad)"/>
    <text x="25" y="33" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="15" font-weight="900">🚀 BUDGET 2025-26 MULTIPLIERS:</text>
    <text x="280" y="33" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="14" font-weight="700">Investment limits increased by <tspan font-weight="900" text-decoration="underline">2.5 Times</tspan> • Turnover limits increased by <tspan font-weight="900" text-decoration="underline">2.0 Times</tspan></text>
  </g>

  <!-- 3 Classification Cards -->
  <!-- 1. MICRO ENTERPRISE -->
  <g transform="translate(40, 220)" filter="url(#shadow)">
    <rect width="255" height="260" rx="22" fill="#121622" stroke="rgba(16,185,129,0.3)" stroke-width="2"/>
    <rect width="255" height="55" rx="22" fill="url(#microGrad)"/>
    <text x="127" y="34" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="18" font-weight="900" text-anchor="middle">🌱 MICRO</text>
    
    <text x="20" y="85" fill="#6ee7b7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">INVESTMENT CEILING</text>
    <text x="20" y="112" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹2.5 Cr</text>
    <text x="20" y="130" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹1.0 Cr)</text>
    
    <line x1="20" y1="145" x2="235" y2="145" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <text x="20" y="172" fill="#6ee7b7" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">ANNUAL TURNOVER CEILING</text>
    <text x="20" y="199" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹10.0 Cr</text>
    <text x="20" y="217" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹5.0 Cr)</text>

    <rect x="20" y="230" width="215" height="18" rx="9" fill="rgba(16,185,129,0.15)"/>
    <text x="127" y="243" fill="#34d399" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" text-anchor="middle">&gt;95% of all Indian MSMEs</text>
  </g>

  <!-- 2. SMALL ENTERPRISE -->
  <g transform="translate(322, 220)" filter="url(#shadow)">
    <rect width="255" height="260" rx="22" fill="#121622" stroke="rgba(59,130,246,0.3)" stroke-width="2"/>
    <rect width="255" height="55" rx="22" fill="url(#smallGrad)"/>
    <text x="127" y="34" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="18" font-weight="900" text-anchor="middle">⚡ SMALL</text>
    
    <text x="20" y="85" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">INVESTMENT CEILING</text>
    <text x="20" y="112" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹25.0 Cr</text>
    <text x="20" y="130" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹10.0 Cr)</text>
    
    <line x1="20" y1="145" x2="235" y2="145" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <text x="20" y="172" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">ANNUAL TURNOVER CEILING</text>
    <text x="20" y="199" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹100.0 Cr</text>
    <text x="20" y="217" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹50.0 Cr)</text>

    <rect x="20" y="230" width="215" height="18" rx="9" fill="rgba(59,130,246,0.15)"/>
    <text x="127" y="243" fill="#60a5fa" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" text-anchor="middle">Eligible for Section 43B(h)</text>
  </g>

  <!-- 3. MEDIUM ENTERPRISE -->
  <g transform="translate(605, 220)" filter="url(#shadow)">
    <rect width="255" height="260" rx="22" fill="#121622" stroke="rgba(139,92,246,0.3)" stroke-width="2"/>
    <rect width="255" height="55" rx="22" fill="url(#medGrad)"/>
    <text x="127" y="34" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="18" font-weight="900" text-anchor="middle">🏢 MEDIUM</text>
    
    <text x="20" y="85" fill="#c4b5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">INVESTMENT CEILING</text>
    <text x="20" y="112" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹125.0 Cr</text>
    <text x="20" y="130" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹50.0 Cr)</text>
    
    <line x1="20" y1="145" x2="235" y2="145" stroke="rgba(255,255,255,0.08)" stroke-width="1"/>

    <text x="20" y="172" fill="#c4b5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">ANNUAL TURNOVER CEILING</text>
    <text x="20" y="199" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="22" font-weight="900">≤ ₹500.0 Cr</text>
    <text x="20" y="217" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11">(2020 Baseline: ≤ ₹250.0 Cr)</text>

    <rect x="20" y="230" width="215" height="18" rx="9" fill="rgba(139,92,246,0.15)"/>
    <text x="127" y="243" fill="#a78bfa" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="800" text-anchor="middle">Mittelstand Target Group</text>
  </g>

  <!-- Critical Rule Callout Footer -->
  <g transform="translate(40, 500)">
    <rect width="820" height="85" rx="18" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
    <text x="25" y="32" fill="#facc15" font-family="'Outfit', sans-serif" font-size="14" font-weight="900">★ STATUTORY EXCLUSION CLAUSE (MSMED RULES):</text>
    <text x="25" y="55" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">1. <tspan font-weight="800" fill="#38bdf8">Export Turnover of Goods &amp; Services</tspan> is completely excluded when calculating annual turnover for classification!</text>
    <text x="25" y="74" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">2. Investment calculation excludes Land, Buildings, R&amp;D equipment, Pollution Control devices, and Industrial Safety tools.</text>
  </g>
</svg>'''

fc2_delayed_payments = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 640" width="100%" height="100%">
  <defs>
    <linearGradient id="bg2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080c16"/>
      <stop offset="100%" stop-color="#111827"/>
    </linearGradient>
    <linearGradient id="redGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#dc2626"/>
      <stop offset="100%" stop-color="#ef4444"/>
    </linearGradient>
    <linearGradient id="stepGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e293b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="900" height="640" rx="28" fill="url(#bg2)"/>
  <rect x="2" y="2" width="896" height="636" rx="26" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(40, 35)">
    <rect x="0" y="0" width="170" height="26" rx="13" fill="rgba(239,68,68,0.2)" stroke="#ef4444" stroke-width="1.5"/>
    <text x="85" y="17" fill="#fca5a5" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="1">MSMED ACT 2006 • CH. V</text>
    <text x="0" y="62" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="26" font-weight="900">Delayed Payments &amp; Commercial Justice Pipeline</text>
    <text x="0" y="86" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">Sections 15–19, Penal Compound Interest, Section 43B(h) Tax Disallowance &amp; MSEFC Timelines</text>
  </g>

  <!-- Step 1: Supply & Delivery -->
  <g transform="translate(40, 140)">
    <rect width="180" height="150" rx="18" fill="url(#stepGrad)" stroke="rgba(255,255,255,0.12)" stroke-width="1.5"/>
    <rect x="15" y="15" width="40" height="24" rx="6" fill="#3b82f6"/>
    <text x="35" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">SEC 15</text>
    <text x="15" y="65" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="15" font-weight="800">Supply of Goods / Services</text>
    <text x="15" y="90" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• With Agreement: <tspan fill="#facc15" font-weight="800">Max 45 Days</tspan></text>
    <text x="15" y="112" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• No Agreement: <tspan fill="#38bdf8" font-weight="800">15 Days</tspan> (Appointed Day)</text>
    <text x="15" y="132" fill="#ef4444" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700">Non-negotiable deadline</text>
  </g>

  <!-- Arrow 1 -->
  <path d="M 230 215 L 255 215" stroke="#60a5fa" stroke-width="3" fill="none" stroke-linecap="round"/>
  <polygon points="255,210 265,215 255,220" fill="#60a5fa"/>

  <!-- Step 2: Default & Section 16 Penalty -->
  <g transform="translate(275, 140)">
    <rect width="190" height="150" rx="18" fill="url(#stepGrad)" stroke="rgba(239,68,68,0.4)" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="24" rx="6" fill="#ef4444"/>
    <text x="35" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">SEC 16</text>
    <text x="15" y="65" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="15" font-weight="800">Penal Compound Interest</text>
    <text x="15" y="90" fill="#f87171" font-family="'Outfit', sans-serif" font-size="18" font-weight="900">3× RBI Bank Rate</text>
    <text x="15" y="112" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• Compounded monthly</text>
    <text x="15" y="132" fill="#fca5a5" font-family="'Plus Jakarta Sans', sans-serif" font-size="10" font-weight="700">Sec 23: Tax non-deductible</text>
  </g>

  <!-- Arrow 2 -->
  <path d="M 475 215 L 500 215" stroke="#f87171" stroke-width="3" fill="none" stroke-linecap="round"/>
  <polygon points="500,210 510,215 500,220" fill="#f87171"/>

  <!-- Step 3: MSEFC Adjudication (Section 18) -->
  <g transform="translate(520, 140)">
    <rect width="340" height="150" rx="18" fill="url(#stepGrad)" stroke="rgba(245,158,11,0.4)" stroke-width="2"/>
    <rect x="15" y="15" width="40" height="24" rx="6" fill="#f59e0b"/>
    <text x="35" y="32" fill="#000" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">SEC 18</text>
    <text x="65" y="32" fill="#fde68a" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">MSEFC Facilitation Council</text>
    
    <rect x="15" y="55" width="145" height="55" rx="10" fill="rgba(245,158,11,0.15)"/>
    <text x="87" y="75" fill="#facc15" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">1. MEDIATION</text>
    <text x="87" y="95" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Mandatory in 90 Days</text>

    <rect x="175" y="55" width="145" height="55" rx="10" fill="rgba(239,68,68,0.15)"/>
    <text x="247" y="75" fill="#f87171" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">2. ARBITRATION</text>
    <text x="247" y="95" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700" text-anchor="middle">Completion in 30 Days</text>

    <text x="15" y="132" fill="#cbd5e1" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">Filed digitally via <tspan fill="#38bdf8" font-weight="800">MSME Samadhaan</tspan> Portal</text>
  </g>

  <!-- Step 4: Court Appeal & Pre-Deposit (Section 19) -->
  <g transform="translate(40, 320)">
    <rect width="400" height="140" rx="18" fill="url(#stepGrad)" stroke="rgba(168,85,247,0.3)" stroke-width="1.5"/>
    <rect x="15" y="15" width="40" height="24" rx="6" fill="#a855f7"/>
    <text x="35" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">SEC 19</text>
    <text x="65" y="32" fill="#d8b4fe" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">Appeal Barrier (Section 19)</text>
    <text x="15" y="70" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="18" font-weight="900">75% Pre-Deposit Mandate</text>
    <text x="15" y="95" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Buyer MUST deposit 75% of awarded amount with court</text>
    <text x="15" y="115" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Proposed amendment: calibrate to 50% to ease genuine appeals</text>
  </g>

  <!-- Step 5: Income Tax Section 43B(h) Disallowance -->
  <g transform="translate(460, 320)">
    <rect width="400" height="140" rx="18" fill="url(#stepGrad)" stroke="rgba(239,68,68,0.3)" stroke-width="1.5"/>
    <rect x="15" y="15" width="55" height="24" rx="6" fill="#dc2626"/>
    <text x="42" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="11" font-weight="900" text-anchor="middle">IT ACT</text>
    <text x="80" y="32" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">Section 43B(h) Tax Disallowance</text>
    <text x="15" y="70" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="18" font-weight="900">Expense Disallowance if Unpaid</text>
    <text x="15" y="95" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• If overdue beyond 45 days on March 31, deduction denied</text>
    <text x="15" y="115" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12">• Applies ONLY to Micro &amp; Small units (NOT Medium or Traders)</text>
  </g>

  <!-- Warning Banner: Fear of Business Loss -->
  <g transform="translate(40, 485)">
    <rect width="820" height="120" rx="18" fill="rgba(239,68,68,0.1)" stroke="rgba(239,68,68,0.4)" stroke-width="2"/>
    <text x="25" y="34" fill="#ef4444" font-family="'Outfit', sans-serif" font-size="16" font-weight="900">⚠️ THE 'FEAR OF BUSINESS LOSS' MARKET PARADOX:</text>
    <text x="25" y="60" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">• Despite statutory protections, small suppliers hesitate to file on Samadhaan fearing buyers will blacklist them.</text>
    <text x="25" y="80" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">• Large buyers may divert orders to Medium or unregistered firms to evade the rigid 45-day payment constraint.</text>
    <text x="25" y="100" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">★ SOLUTION: Mandatory TReDS Onboarding for all CPSEs &amp; Corporates for non-recourse digital invoice factoring!</text>
  </g>
</svg>'''

fc3_pm_vishwakarma = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 620" width="100%" height="100%">
  <defs>
    <linearGradient id="bg3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#080e1a"/>
      <stop offset="100%" stop-color="#1e1b4b"/>
    </linearGradient>
    <linearGradient id="cardG3" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#1e1b4b"/>
      <stop offset="100%" stop-color="#0f172a"/>
    </linearGradient>
  </defs>

  <rect width="900" height="620" rx="28" fill="url(#bg3)"/>
  <rect x="2" y="2" width="896" height="616" rx="26" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(40, 35)">
    <rect x="0" y="0" width="165" height="26" rx="13" fill="rgba(168,85,247,0.2)" stroke="#a855f7" stroke-width="1.5"/>
    <text x="82" y="17" fill="#d8b4fe" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="1">CENTRAL SECTOR SCHEME</text>
    <text x="0" y="62" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="26" font-weight="900">PM Vishwakarma 5-Pillar Artisan Lifecycle</text>
    <text x="0" y="86" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">Launched Sept 17, 2023 • ₹13,000 Cr Outlay • Supporting 18 Traditional Hands-and-Tools Trades</text>
  </g>

  <!-- 5 Horizontal Sequential Step Boxes -->
  <!-- Pillar 1 -->
  <g transform="translate(40, 130)">
    <rect width="150" height="220" rx="16" fill="url(#cardG3)" stroke="rgba(168,85,247,0.3)" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="20" fill="#7c3aed"/>
    <text x="75" y="41" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">1</text>
    <text x="75" y="78" fill="#c4b5fd" font-family="'Outfit', sans-serif" font-size="13" font-weight="800" text-anchor="middle">RECOGNITION</text>
    <text x="12" y="105" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• Biometric CSC Enrolment</text>
    <text x="12" y="135" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• 3-Tier Verification (Gram Panchayat / District / State)</text>
    <text x="12" y="190" fill="#38bdf8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">Certificate &amp; ID</text>
  </g>

  <!-- Pillar 2 -->
  <g transform="translate(205, 130)">
    <rect width="150" height="220" rx="16" fill="url(#cardG3)" stroke="rgba(59,130,246,0.3)" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="20" fill="#2563eb"/>
    <text x="75" y="41" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">2</text>
    <text x="75" y="78" fill="#93c5fd" font-family="'Outfit', sans-serif" font-size="13" font-weight="800" text-anchor="middle">SKILLING</text>
    <text x="12" y="105" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• 5-Day Basic Skill Training</text>
    <text x="12" y="135" fill="#facc15" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="800">• ₹500 / Day</text>
    <text x="12" y="152" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">daily stipend support</text>
    <text x="12" y="190" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">15-day Advanced Opt.</text>
  </g>

  <!-- Pillar 3 -->
  <g transform="translate(370, 130)">
    <rect width="150" height="220" rx="16" fill="url(#cardG3)" stroke="rgba(16,185,129,0.3)" stroke-width="1.5"/>
    <circle cx="75" cy="35" r="20" fill="#059669"/>
    <text x="75" y="41" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">3</text>
    <text x="75" y="78" fill="#6ee7b7" font-family="'Outfit', sans-serif" font-size="13" font-weight="800" text-anchor="middle">TOOLKIT</text>
    <text x="12" y="105" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• Modern Tools Grant</text>
    <text x="12" y="135" fill="#10b981" font-family="'Outfit', sans-serif" font-size="18" font-weight="900">₹15,000</text>
    <text x="12" y="155" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">via e-Voucher</text>
    <text x="12" y="190" fill="#34d399" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">Digital Tool Purchase</text>
  </g>

  <!-- Pillar 4 -->
  <g transform="translate(535, 130)">
    <rect width="165" height="220" rx="16" fill="url(#cardG3)" stroke="rgba(245,158,11,0.3)" stroke-width="1.5"/>
    <circle cx="82" cy="35" r="20" fill="#d97706"/>
    <text x="82" y="41" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">4</text>
    <text x="82" y="78" fill="#fde68a" font-family="'Outfit', sans-serif" font-size="13" font-weight="800" text-anchor="middle">CREDIT SUPPORT</text>
    <text x="12" y="105" fill="#ffffff" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="700">Collateral-Free Loan:</text>
    <text x="12" y="125" fill="#facc15" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">• Tranche 1: Up to ₹1L (18m)</text>
    <text x="12" y="145" fill="#facc15" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">• Tranche 2: Up to ₹2L (30m)</text>
    <text x="12" y="175" fill="#34d399" font-family="'Outfit', sans-serif" font-size="14" font-weight="900">5% Interest Rate</text>
    <text x="12" y="195" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">(8% Govt Subvention)</text>
  </g>

  <!-- Pillar 5 -->
  <g transform="translate(715, 130)">
    <rect width="145" height="220" rx="16" fill="url(#cardG3)" stroke="rgba(236,72,153,0.3)" stroke-width="1.5"/>
    <circle cx="72" cy="35" r="20" fill="#db2777"/>
    <text x="72" y="41" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">5</text>
    <text x="72" y="78" fill="#fbcfe8" font-family="'Outfit', sans-serif" font-size="13" font-weight="800" text-anchor="middle">MARKETING</text>
    <text x="10" y="105" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• Digital Tx: ₹1/tx (max ₹100/mo)</text>
    <text x="10" y="140" fill="#f8fafc" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="600">• Onboarding on GeM &amp; ONDC</text>
    <text x="10" y="190" fill="#f472b6" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800">Quality &amp; Branding</text>
  </g>

  <!-- Achievement Numbers Banner -->
  <g transform="translate(40, 380)">
    <rect width="820" height="200" rx="20" fill="rgba(255,255,255,0.03)" stroke="rgba(255,255,255,0.1)" stroke-width="1.5"/>
    <text x="30" y="35" fill="#facc15" font-family="'Outfit', sans-serif" font-size="16" font-weight="900">★ OFFICIAL SCHEME MILESTONES (PIB FEB 2025):</text>
    
    <g transform="translate(30, 60)">
      <rect width="240" height="110" rx="14" fill="rgba(124,58,237,0.15)" stroke="rgba(124,58,237,0.4)" stroke-width="1.5"/>
      <text x="20" y="35" fill="#c4b5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">TOTAL APPLICATIONS</text>
      <text x="20" y="75" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="28" font-weight="900">2.65 Crore+</text>
      <text x="20" y="95" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">submitted nationwide</text>
    </g>

    <g transform="translate(290, 60)">
      <rect width="240" height="110" rx="14" fill="rgba(16,185,129,0.15)" stroke="rgba(16,185,129,0.4)" stroke-width="1.5"/>
      <text x="20" y="35" fill="#6ee7b7" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">SUCCESSFUL REGISTRATIONS</text>
      <text x="20" y="75" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="28" font-weight="900">27.13 Lakh</text>
      <text x="20" y="95" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">vetted &amp; certified artisans</text>
    </g>

    <g transform="translate(550, 60)">
      <rect width="240" height="110" rx="14" fill="rgba(59,130,246,0.15)" stroke="rgba(59,130,246,0.4)" stroke-width="1.5"/>
      <text x="20" y="35" fill="#93c5fd" font-family="'Plus Jakarta Sans', sans-serif" font-size="12" font-weight="700">TRADITIONAL TRADES</text>
      <text x="20" y="75" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="28" font-weight="900">18 Trades</text>
      <text x="20" y="95" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="10">Carpenters, Potters, Masons, etc.</text>
    </g>
  </g>
</svg>'''

fc4_dwarfism = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bg4" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0a0a0f"/>
      <stop offset="100%" stop-color="#161824"/>
    </linearGradient>
  </defs>

  <rect width="900" height="600" rx="28" fill="url(#bg4)"/>
  <rect x="2" y="2" width="896" height="596" rx="26" fill="none" stroke="rgba(255,255,255,0.08)" stroke-width="2"/>

  <!-- Header -->
  <g transform="translate(40, 35)">
    <rect x="0" y="0" width="180" height="26" rx="13" fill="rgba(245,158,11,0.2)" stroke="#f59e0b" stroke-width="1.5"/>
    <text x="90" y="17" fill="#fde68a" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" font-weight="800" text-anchor="middle" letter-spacing="1">ECONOMIC PARADIGMS</text>
    <text x="0" y="62" fill="#ffffff" font-family="'Outfit', sans-serif" font-size="26" font-weight="900">Indian Dwarfism Trap vs. German Mittelstand</text>
    <text x="0" y="86" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="13" font-weight="600">The Anatomy of the Missing Middle &amp; How Mid-Sized Champions Drive National Productivity</text>
  </g>

  <!-- Left Card: The Indian Dwarfism Trap -->
  <g transform="translate(40, 130)">
    <rect width="390" height="420" rx="22" fill="#111420" stroke="rgba(239,68,68,0.3)" stroke-width="2"/>
    <rect width="390" height="50" rx="22" fill="#dc2626"/>
    <text x="195" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">❌ THE INDIAN DWARFISM TRAP</text>

    <g transform="translate(25, 75)">
      <text x="0" y="0" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">1. Pathological Smallness</text>
      <text x="0" y="20" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Firms remain older than 10-20 years but employ &lt;10 workers deliberately to evade labor and factory laws.</text>

      <text x="0" y="70" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">2. The Bimodal 'Missing Middle'</text>
      <text x="0" y="90" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Over 95% micro-enterprises and a few massive corporations; acute lack of 100-500 employee competitive firms.</text>

      <text x="0" y="140" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">3. Hsieh &amp; Klenow (2009) TFP Penalty</text>
      <text x="0" y="160" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Capital and labor misallocation reduces Indian aggregate manufacturing productivity by <tspan fill="#ef4444" font-weight="800">40% to 60%</tspan>.</text>

      <text x="0" y="210" fill="#fca5a5" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">4. Survivalist vs. Transformational</text>
      <text x="0" y="230" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Tiny units operate for subsistence survival rather than investing in automation, R&amp;D, or export scaling.</text>

      <rect x="-10" y="270" width="360" height="50" rx="12" fill="rgba(239,68,68,0.15)"/>
      <text x="170" y="292" fill="#ef4444" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">RESULT: STAGNANT PRODUCTIVITY</text>
      <text x="170" y="308" fill="#fca5a5" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">Inability to absorb agricultural surplus labor</text>
    </g>
  </g>

  <!-- Right Card: The German Mittelstand Transformation -->
  <g transform="translate(470, 130)">
    <rect width="390" height="420" rx="22" fill="#111420" stroke="rgba(16,185,129,0.3)" stroke-width="2"/>
    <rect width="390" height="50" rx="22" fill="#059669"/>
    <text x="195" y="32" fill="#fff" font-family="'Outfit', sans-serif" font-size="16" font-weight="900" text-anchor="middle">✓ THE MITTELSTAND TRANSFORMATION</text>

    <g transform="translate(25, 75)">
      <text x="0" y="0" fill="#6ee7b7" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">1. Global 'Hidden Champions'</text>
      <text x="0" y="20" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Mid-sized (100–500 workers) specialized firms that dominate global market shares in precision B2B niches.</text>

      <text x="0" y="70" fill="#6ee7b7" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">2. Dual Vocational Apprenticeships</text>
      <text x="0" y="90" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Firms invest heavily in training technical apprentices, solving the skill deficit and creating high-wage jobs.</text>

      <text x="0" y="140" fill="#6ee7b7" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">3. Generational Patient Capital</text>
      <text x="0" y="160" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Family ownership and equity funds (like SRI Fund) prioritize long-term R&amp;D over short-term quarterly debt.</text>

      <text x="0" y="210" fill="#6ee7b7" font-family="'Outfit', sans-serif" font-size="14" font-weight="800">4. High Value-Added Output (55% GDP)</text>
      <text x="0" y="230" fill="#94a3b8" font-family="'Plus Jakarta Sans', sans-serif" font-size="11.5">Contributes 55% of German output, providing the resilient anchor against external global supply shocks.</text>

      <rect x="-10" y="270" width="360" height="50" rx="12" fill="rgba(16,185,129,0.15)"/>
      <text x="170" y="292" fill="#10b981" font-family="'Outfit', sans-serif" font-size="12" font-weight="900" text-anchor="middle">GOAL: VIKSIT BHARAT CHAMPIONS</text>
      <text x="170" y="308" fill="#a7f3d0" font-family="'Plus Jakarta Sans', sans-serif" font-size="11" text-anchor="middle">Transitioning from survivalism to global tech lead</text>
    </g>
  </g>
</svg>'''

files = [
    ("flowchart_msme_classification.svg", fc1_classification),
    ("flowchart_delayed_payments.svg", fc2_delayed_payments),
    ("flowchart_pm_vishwakarma.svg", fc3_pm_vishwakarma),
    ("flowchart_dwarfism_vs_mittelstand.svg", fc4_dwarfism)
]

target_dirs = [
    r"d:\Anki_Upgraded\Raw_questions_CAVA\Filtered_questions",
    r"d:\Anki_Upgraded\Filtered_Questions",
    r"d:\Anki_Upgraded\mobile\assets\flowcharts"
]

for d in target_dirs:
    os.makedirs(d, exist_ok=True)
    for fname, content in files:
        fpath = os.path.join(d, fname)
        with open(fpath, "w", encoding="utf-8") as out:
            out.write(content)
        print(f"Wrote: {fpath}")

print("All flowcharts generated successfully!")
