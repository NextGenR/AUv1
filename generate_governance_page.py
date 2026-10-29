# -*- coding: utf-8 -*-
"""
Generator for governance.html
Builds the comprehensive, interactive Governance Hub and Cluster 1 Deep Learning Module
for UPSC GS-2.
"""

import os
import json

PAGE_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <title>Governance (GS Paper 2) | Cortex Anki 2.0</title>
  <link rel="manifest" href="manifest.json">
  <link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
  <link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
  <link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
  <meta name="mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Cortex Governance">
  <meta name="theme-color" content="#2563eb">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&family=Outfit:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <style>
    :root {
      --gov-primary: #2563eb;
      --gov-primary-dark: #1d4ed8;
      --gov-accent: #f59e0b;
      --gov-accent-dark: #d97706;
      --gov-teal: #0d9488;
      --gov-purple: #7c3aed;
      --gov-rose: #e11d48;
      --gov-card-border: rgba(37, 99, 235, 0.25);
      --card-bg: rgba(18, 24, 40, 0.85);
      --card-sub: rgba(30, 41, 59, 0.7);
      --line: rgba(255, 255, 255, 0.12);
      --ink: #f8fafc;
      --mut: #94a3b8;
      --hl-bg: rgba(254, 215, 64, 0.32);
      --hl-line: rgba(245, 158, 11, 0.65);
      --ok: #10b981;
      --okbg: rgba(16, 185, 129, 0.18);
      --no: #ef4444;
      --nobg: rgba(239, 68, 68, 0.18);
      --sel: rgba(37, 99, 235, 0.18);
      --selb: #3b82f6;
    }
    
    [data-theme="light"], :root:not([data-theme="dark"]) body.light-mode {
      --card-bg: #ffffff;
      --card-sub: #f8fafc;
      --line: #e2e8f0;
      --ink: #0f172a;
      --mut: #64748b;
      --hl-bg: rgba(254, 215, 64, 0.4);
      --hl-line: rgba(245, 158, 11, 0.7);
      --okbg: #dcfce7;
      --nobg: #fee2e2;
      --sel: #eff6ff;
      --selb: #2563eb;
    }

    body {
      background-color: var(--bg-dark, #07090e);
      color: var(--ink);
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, sans-serif;
      margin: 0;
      padding: 0;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    .gov-wrapper {
      max-width: 1050px;
      margin: 0 auto;
      padding: 1.25rem 1.25rem 3rem;
      width: 100%;
      box-sizing: border-box;
    }

    /* Banners & Cards */
    .gov-hero-banner {
      background: linear-gradient(135deg, rgba(37, 99, 235, 0.22) 0%, rgba(124, 58, 237, 0.2) 100%);
      border: 2px solid var(--gov-card-border);
      border-radius: 20px;
      padding: 1.5rem 1.75rem;
      margin-bottom: 1.75rem;
      position: relative;
      overflow: hidden;
      box-shadow: 0 10px 30px rgba(0,0,0,0.25);
    }

    .gov-hero-banner::after {
      content: "🏛️";
      position: absolute;
      right: 1.5rem;
      bottom: -0.8rem;
      font-size: 6rem;
      opacity: 0.12;
      pointer-events: none;
    }

    .theme-tab-row {
      display: flex;
      gap: 0.6rem;
      overflow-x: auto;
      padding-bottom: 0.6rem;
      margin-bottom: 1.5rem;
      scrollbar-width: thin;
    }

    .theme-tab-btn {
      background: var(--card-bg);
      border: 2px solid var(--line);
      border-bottom-width: 4px;
      border-radius: 12px;
      padding: 0.65rem 1.1rem;
      color: var(--mut);
      font-weight: 700;
      font-size: 0.92rem;
      cursor: pointer;
      white-space: nowrap;
      transition: all 0.2s ease;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .theme-tab-btn:hover {
      border-color: var(--gov-primary);
      color: var(--ink);
    }

    .theme-tab-btn.active {
      background: linear-gradient(135deg, #2563eb, #1d4ed8);
      color: #fff;
      border-color: #1e40af;
      box-shadow: 0 4px 15px rgba(37, 99, 235, 0.35);
      border-bottom-width: 4px;
    }

    .theme-card-container {
      background: var(--card-bg);
      border: 2px solid var(--line);
      border-radius: 18px;
      padding: 1.5rem;
      margin-bottom: 2rem;
      box-shadow: 0 8px 24px rgba(0,0,0,0.15);
    }

    .cluster-card {
      background: var(--card-sub);
      border: 2px solid var(--line);
      border-left: 6px solid var(--gov-primary);
      border-radius: 14px;
      padding: 1.25rem 1.4rem;
      margin-bottom: 1.25rem;
      transition: all 0.2s ease;
    }

    .cluster-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    .cluster-card.active-cluster {
      border-color: rgba(37, 99, 235, 0.6);
      border-left: 6px solid var(--gov-primary);
      background: rgba(37, 99, 235, 0.08);
    }

    /* Learning Mode Flow Elements */
    .learn-container {
      display: none;
      background: var(--card-bg);
      border: 2px solid var(--line);
      border-radius: 20px;
      padding: 1.75rem;
      margin-bottom: 2rem;
      box-shadow: 0 12px 35px rgba(0,0,0,0.25);
      position: relative;
    }

    .step-bar-wrap {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.25rem;
    }

    .step-bar {
      flex: 1;
      height: 10px;
      background: var(--line);
      border-radius: 6px;
      overflow: hidden;
    }

    .step-bar-fill {
      height: 100%;
      background: linear-gradient(90deg, #2563eb, #10b981);
      width: 0%;
      transition: width 0.35s ease;
    }

    .step-counter-pill {
      font-size: 0.82rem;
      font-weight: 800;
      color: var(--gov-accent);
      background: rgba(245, 158, 11, 0.15);
      padding: 3px 10px;
      border-radius: 20px;
      white-space: nowrap;
    }

    /* Interactive 3D Buttons */
    .btn-3d {
      background: var(--gov-primary);
      color: #fff;
      border: 0;
      border-bottom: 5px solid var(--gov-primary-dark);
      border-radius: 14px;
      padding: 0.75rem 1.5rem;
      font: inherit;
      font-weight: 800;
      font-size: 1.05rem;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.5rem;
      transition: transform 0.1s, border-bottom-width 0.1s, background-color 0.15s;
    }

    .btn-3d:active {
      transform: translateY(2px);
      border-bottom-width: 3px;
    }

    .btn-3d-amber {
      background: var(--gov-accent);
      border-bottom-color: var(--gov-accent-dark);
      color: #1e1b4b;
    }

    .btn-3d-emerald {
      background: var(--ok);
      border-bottom-color: #059669;
      color: #ffffff;
    }

    .btn-3d-secondary {
      background: var(--card-sub);
      border: 2px solid var(--line);
      border-bottom-width: 4px;
      color: var(--ink);
    }

    /* Content Cards */
    .pyq-box {
      background: rgba(37, 99, 235, 0.08);
      border: 2px dashed rgba(37, 99, 235, 0.4);
      border-radius: 14px;
      padding: 1.25rem 1.4rem;
      margin: 1rem 0 1.25rem;
    }

    .demand-box {
      background: rgba(245, 158, 11, 0.08);
      border: 2px solid rgba(245, 158, 11, 0.35);
      border-radius: 14px;
      padding: 1.25rem 1.4rem;
      margin-bottom: 1.5rem;
    }

    .triad-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 1rem;
      margin: 1.25rem 0;
    }

    .triad-card {
      background: var(--card-sub);
      border: 2px solid var(--line);
      border-radius: 14px;
      padding: 1.1rem;
      position: relative;
    }

    .triad-tag {
      display: inline-block;
      font-size: 0.75rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.05em;
      padding: 2px 8px;
      border-radius: 6px;
      margin-bottom: 0.4rem;
    }

    .tag-struct { background: rgba(37, 99, 235, 0.2); color: #60a5fa; }
    .tag-cult { background: rgba(245, 158, 11, 0.2); color: #fbbf24; }
    .tag-imp { background: rgba(239, 68, 68, 0.2); color: #f87171; }

    /* Highlights */
    b, strong {
      background: var(--hl-bg);
      padding: 1.5px 5px;
      border-radius: 4px;
      color: inherit;
      box-shadow: inset 0 -2.5px 0 0 var(--hl-line);
    }

    /* Practice Quiz Cards */
    .quiz-card {
      background: var(--card-sub);
      border: 2px solid var(--line);
      border-radius: 16px;
      padding: 1.25rem 1.4rem;
      margin-bottom: 1.25rem;
    }

    .quiz-opt {
      display: block;
      width: 100%;
      text-align: left;
      background: var(--card-bg);
      border: 2px solid var(--line);
      border-bottom-width: 4px;
      border-radius: 12px;
      padding: 0.85rem 1.1rem;
      margin-bottom: 0.65rem;
      font: inherit;
      color: inherit;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }

    .quiz-opt:hover {
      border-color: var(--selb);
      background: var(--sel);
    }

    .quiz-opt.selected {
      background: var(--sel);
      border-color: var(--selb);
    }

    .quiz-opt.correct {
      background: var(--okbg) !important;
      border-color: var(--ok) !important;
      color: var(--ink);
    }

    .quiz-opt.incorrect {
      background: var(--nobg) !important;
      border-color: var(--no) !important;
      animation: shake 0.35s;
    }

    @keyframes shake {
      25% { transform: translateX(-6px); }
      75% { transform: translateX(6px); }
    }

    .feedback-banner {
      display: none;
      border-radius: 12px;
      padding: 1rem 1.2rem;
      margin-top: 1rem;
      font-size: 0.95rem;
      line-height: 1.4;
      animation: pop 0.25s ease-out;
    }

    .feedback-banner.correct {
      display: block;
      background: var(--okbg);
      border: 2px solid var(--ok);
      color: #10b981;
    }

    .feedback-banner.incorrect {
      display: block;
      background: var(--nobg);
      border: 2px solid var(--no);
      color: #ef4444;
    }

    /* Red Flag Question */
    .flag-segment {
      display: inline-block;
      padding: 4px 8px;
      margin: 3px 2px;
      border-radius: 8px;
      border: 2px solid transparent;
      background: rgba(255, 255, 255, 0.05);
      cursor: pointer;
      font-weight: 700;
      transition: all 0.15s;
    }

    .flag-segment:hover {
      border-color: var(--gov-accent);
      background: rgba(245, 158, 11, 0.15);
    }

    .flag-segment.flag-bad {
      border-color: var(--no);
      background: var(--nobg);
      color: var(--no);
    }

    .flag-segment.flag-ok {
      border-color: var(--ok);
      background: var(--okbg);
      color: var(--ok);
    }

    /* Sort Arena */
    .sort-arena {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin: 1.25rem 0;
    }

    .sort-card-holder {
      background: rgba(37, 99, 235, 0.1);
      border: 2px dashed rgba(37, 99, 235, 0.35);
      border-radius: 14px;
      padding: 1.25rem;
      text-align: center;
      min-height: 80px;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      font-weight: 700;
    }

    .sort-bins-row {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 0.75rem;
    }

    .sort-bin-btn {
      background: var(--card-sub);
      border: 2px solid var(--line);
      border-bottom-width: 4px;
      border-radius: 12px;
      padding: 0.85rem 0.5rem;
      text-align: center;
      font-weight: 800;
      font-size: 0.9rem;
      cursor: pointer;
      color: var(--ink);
      transition: all 0.15s;
    }

    .sort-bin-btn:hover {
      border-color: var(--gov-primary);
      transform: translateY(-2px);
    }

    .sort-bin-btn:active {
      transform: translateY(2px);
      border-bottom-width: 2px;
    }

    /* Match Pair items */
    .match-row {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }

    @keyframes pop {
      0% { opacity: 0; transform: translateY(8px) scale(0.98); }
      100% { opacity: 1; transform: translateY(0) scale(1); }
    }

    .confetti-canvas {
      position: fixed;
      top: 0;
      left: 0;
      width: 100vw;
      height: 100vh;
      pointer-events: none;
      z-index: 9999;
    }

    .celebrate-card {
      text-align: center;
      padding: 2.5rem 1.5rem;
    }

    .celebrate-icon {
      font-size: 4rem;
      margin-bottom: 1rem;
      animation: pop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    }
  </style>
</head>
<body>

  <!-- Main Navigation Bar -->
  <nav class="navbar" id="main-nav">
    <a href="index.html" class="nav-brand" id="brand-logo">
      <div class="brand-icon">🧠</div>
      <div class="brand-text">
        <h1>CORTEX ANKI <span class="brand-badge">2.0 Pro</span></h1>
      </div>
    </a>

    <ul class="nav-links">
      <li><a href="index.html" class="nav-link" id="nav-dashboard">📊 Dashboard</a></li>
      <li><a href="subjects.html" class="nav-link" id="nav-subjects">📚 Subjects</a></li>
      <li><a href="governance.html" class="nav-link active" id="nav-governance" style="color:#60a5fa; font-weight:800;">🏛️ Governance</a></li>
      <li><a href="cava.html" class="nav-link" id="nav-cava">⚡ CAVA Hub</a></li>
      <li><a href="roadmap_notes.html" class="nav-link" id="nav-roadmap" style="color:#ffe600; font-weight:700;">🗺️ Visual Roadmap</a></li>
      <li><a href="msme_duo.html" class="nav-link" id="nav-duo-msme">🏭 MSME Duolingo</a></li>
      <li><a href="public_exam_duo.html" class="nav-link" id="nav-duo-exam">🎮 Public Exams</a></li>
      <li><a href="topic_study.html" class="nav-link" id="nav-study">🎯 AI in Judiciary</a></li>
    </ul>

    <div class="nav-actions">
      <button class="btn btn-sm btn-secondary" id="theme-toggle-btn" style="font-weight:700; border-radius:999px;">
        🌓 Theme
      </button>
      <div class="streak-pill">
        <span class="streak-flame">🔥</span>
        <span class="streak-number">18</span> Days
      </div>
      <a href="mobile/index.html" class="btn btn-sm" style="background:#10b981; color:#fff; font-weight:800; border-radius:999px; text-decoration:none;">
        📱 Mobile
      </a>
    </div>
  </nav>

  <!-- Page Container -->
  <main class="page-container">
    <div class="gov-wrapper">
      
      <!-- Breadcrumbs -->
      <nav class="breadcrumbs" aria-label="Breadcrumb" style="margin-bottom:1rem;">
        <a href="index.html">Dashboard</a>
        <span class="separator">/</span>
        <a href="subjects.html">Subjects</a>
        <span class="separator">/</span>
        <span class="current">Governance (GS Paper 2)</span>
      </nav>

      <!-- Governance Hero Banner -->
      <header class="gov-hero-banner" id="gov-main-header">
        <div style="display:flex; align-items:center; gap:0.6rem; margin-bottom:0.4rem; flex-wrap:wrap;">
          <span class="subject-tag tag-gs2" style="background:#2563eb; color:#fff; font-weight:800; padding:3px 10px; border-radius:8px;">GS Paper 2 Core</span>
          <span class="badge badge-success">5 Syllabus Themes</span>
          <span class="badge badge-primary">Cluster Architecture Active</span>
        </div>
        <h2 style="font-size:2rem; margin:0.4rem 0 0.5rem; font-weight:800;">Governance & Civil Services Repository</h2>
        <p style="color:var(--mut); margin:0; font-size:1.02rem; line-height:1.45; max-width:820px;">
          Complete thematic deconstruction of the official UPSC GS-2 Governance syllabus. Dive into high-yield PYQ clusters, structural vs cultural analysis, committee recommendations, and interactive retrieval practice.
        </p>
      </header>

      <!-- 5 Syllabus Themes Tabs -->
      <div style="margin-bottom:0.6rem; display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:0.5rem;">
        <h3 style="margin:0; font-size:1.15rem; font-weight:800; display:flex; align-items:center; gap:0.5rem;">
          <span>📑</span> Official UPSC Syllabus Themes (5 Themes)
        </h3>
        <span style="font-size:0.85rem; color:var(--mut);">Select a theme to explore</span>
      </div>

      <div class="theme-tab-row" id="theme-tabs-nav">
        <button class="theme-tab-btn" data-theme-id="theme-1">
          <span>1.</span> Transparency & Accountability
        </button>
        <button class="theme-tab-btn active" data-theme-id="theme-2">
          <span>2.</span> Role of Civil Services 🎯
        </button>
        <button class="theme-tab-btn" data-theme-id="theme-3">
          <span>3.</span> Development Industry (NGOs/SHGs)
        </button>
        <button class="theme-tab-btn" data-theme-id="theme-4">
          <span>4.</span> Government Policies & Interventions
        </button>
        <button class="theme-tab-btn" data-theme-id="theme-5">
          <span>5.</span> Pressure Groups & Quasi-Judicial Bodies
        </button>
      </div>

      <!-- THEME CONTENT CONTAINER -->
      <section class="theme-card-container" id="theme-details-area">
        <!-- Rendered dynamically by JavaScript -->
      </section>

      <!-- INTERACTIVE MASTER LEARNING CONTAINER -->
      <section class="learn-container" id="learn-interactive-module">
        <!-- Step Header & Progress -->
        <div class="step-bar-wrap">
          <button class="btn btn-sm btn-secondary" id="btn-quit-learning" style="padding:4px 10px; border-radius:8px; font-weight:700;">
            ✕ Back to Themes
          </button>
          <div class="step-bar">
            <div class="step-bar-fill" id="learn-progress-fill"></div>
          </div>
          <span class="step-counter-pill" id="learn-step-pill">Step 1 of 15</span>
        </div>

        <!-- Dynamic Learning Screen Area -->
        <div id="learn-screen-content"></div>
      </section>

    </div>
  </main>

  <canvas class="confetti-canvas" id="confetti-canvas"></canvas>

  <script>
    // --- GOVERNANCE DATA DEFINITION ---
    const THEMES = [
      {
        id: "theme-1",
        num: 1,
        title: "Important aspects of governance, transparency and accountability",
        fullTitle: "Important aspects of governance, transparency and accountability, e-governance—applications, models, successes, limitations, and potential; citizens charters, transparency & accountability and institutional and other measures.",
        badge: "Theme 1",
        ico: "🔍",
        desc: "Covers the bedrock pillars of modern public administration: e-governance architectures, DARPG Sevottam model, Right to Information (RTI) jurisprudence, Citizen's Charters, social audits, and institutional watchdogs (CVC, Lokpal, CAG).",
        clustersCount: 3,
        pyqsCount: 14,
        clusters: [
          {
            title: "Citizen's Charters & Sevottam Model",
            pyqs: "2018 (Q10), 2023 (Q9)",
            desc: "Service delivery commitments, 6 principles, 2nd ARC 12th report, and why charters failed without statutory teeth.",
            ready: true,
            link: "Citizen’s Charter_ Learn from Scratch (1).html"
          },
          {
            title: "E-Governance: Promise vs Last-Mile Exclusion",
            pyqs: "2016 (Q15), 2020 (Q8), 2022 (Q7)",
            desc: "Digital delivery, JAM trinity, biometric authentication hurdles, and digital divide vs citizen empowerment.",
            ready: false
          },
          {
            title: "Transparency, RTI & Institutional Watchdogs",
            pyqs: "2019 (Q12), 2020 (Q9), 2024 (Q7)",
            desc: "Article 19(1)(a) sunshine laws, Section 8 exemptions, DPDP Act interface, CVC and Lokpal efficacy.",
            ready: false
          }
        ]
      },
      {
        id: "theme-2",
        num: 2,
        title: "Role of civil services in a democracy",
        fullTitle: "Role of civil services in a democracy.",
        badge: "Theme 2 • Active Master Module",
        ico: "🏛️",
        desc: "In-depth analysis of the permanent executive: Macaulay colonial legacy, Weberian steel frame, generalist vs specialist debate, bureaucratic politicization, institutional quality, and Mission Karmayogi.",
        clustersCount: 3,
        pyqsCount: 5,
        clusters: [
          {
            id: "cluster-1",
            title: "Cluster 1: Structural Design & Colonial Legacy (Structure vs. Development)",
            pyqs: [
              { year: "2016", qnum: "Q14", marks: "12.5 Marks", words: "200 Words", text: "“Traditional bureaucratic structure and culture have hampered the process of socio-economic development in India.” Comment." },
              { year: "2026", qnum: "Q8", marks: "10 Marks", words: "150 Words", text: "Analyse the advantages and limitations of the generalist structure of the Indian Civil Services in contemporary governance." }
            ],
            whyClubbed: "Both questions test how India's Weberian and Macaulay-era bureaucratic structure—characterized by generalist dominance, rigid hierarchy, departmental silos, and status-quoist culture—struggles to deliver modern socio-economic development and technical governance (e.g. AI regulation, climate finance, trade negotiations).",
            status: "ready",
            actionText: "Learn this Chapter →"
          },
          {
            id: "cluster-2",
            title: "Cluster 2: Democratic Ethos, Values & Public Trust (Neutrality & Integrity)",
            pyqs: [
              { year: "2017", qnum: "Q18 (Part A)", marks: "15 Marks", words: "250 Words", text: "Initially Civil Services in India were designed to achieve the goals of neutrality and effectiveness, which seems to be lacking in the present context..." },
              { year: "2024", qnum: "Q8", marks: "10 Marks", words: "150 Words", text: "The Doctrine of Democratic Governance makes it necessary that the public perception of the integrity and commitment of civil servants becomes absolutely positive. Discuss." }
            ],
            whyClubbed: "Both questions focus on the erosion of foundational civil service values (political neutrality, impartiality, anonymity, integrity, and commitment to constitutional morality) and how this erosion damages public trust and democratic legitimacy.",
            status: "preview",
            actionText: "Preview Thematic Blueprint"
          },
          {
            id: "cluster-3",
            title: "Cluster 3: Institutional Quality & Comprehensive Reforms (Capacity & Outcomes)",
            pyqs: [
              { year: "2017", qnum: "Q18 (Part B)", marks: "15 Marks", words: "250 Words", text: "...Do you agree with the view that drastic reforms are required in Civil Services? Comment." },
              { year: "2020", qnum: "Q7", marks: "10 Marks", words: "150 Words", text: "“Institutional quality is a crucial driver of economic performance.” In this context, suggest reforms in Civil Service for strengthening democracy." }
            ],
            whyClubbed: "Both questions link administrative effectiveness and institutional capacity directly to national outcomes (economic performance, ease of doing business, and democratic stability) and demand a comprehensive reform roadmap.",
            status: "preview",
            actionText: "Preview Thematic Blueprint"
          }
        ]
      },
      {
        id: "theme-3",
        num: 3,
        title: "Development processes and the development industry",
        fullTitle: "Development processes and the development industry—the role of NGOs, SHGs, various groups and associations, donors, charities, institutional and other stakeholders.",
        badge: "Theme 3",
        ico: "🤝",
        desc: "Explores the non-state developmental architecture: Self Help Groups (SHG-Bank Linkage, DAY-NRLM), voluntary organizations, FCRA regulatory amendments, donor dynamics, and participatory community development.",
        clustersCount: 2,
        pyqsCount: 9,
        clusters: [
          {
            title: "SHGs & Women's Micro-Enterprise Ecosystem",
            pyqs: "2015 (Q13), 2021 (Q10), 2023 (Q8)",
            desc: "Social capital creation, Kudumbashree/Mission Shakti models, financial inclusion, and graduation to nano-enterprises.",
            ready: false
          },
          {
            title: "NGOs, FCRA Regulations & Civil Society Space",
            pyqs: "2016 (Q13), 2020 (Q10), 2022 (Q8)",
            desc: "Bridging welfare gaps vs national security oversight; FCRA 2020 amendment debate and donor compliance.",
            ready: false
          }
        ]
      },
      {
        id: "theme-4",
        num: 4,
        title: "Government policies and interventions for development",
        fullTitle: "Government policies and interventions for development in various sectors and issues arising out of their design and implementation.",
        badge: "Theme 4",
        ico: "📋",
        desc: "Examines state intervention across health, education, skill development, urban infrastructure, and agriculture—analyzing structural flaws in scheme design, federal fiscal friction, and implementation bottlenecks.",
        clustersCount: 3,
        pyqsCount: 16,
        clusters: [
          {
            title: "Policy Formulation & Design Deficits",
            pyqs: "2017 (Q7), 2019 (Q8), 2023 (Q7)",
            desc: "Top-down schematic rigidity vs localized contextual realities; outcome budgeting vs expenditure tracking.",
            ready: false
          },
          {
            title: "Implementation Bottlenecks & Centrally Sponsored Schemes",
            pyqs: "2018 (Q8), 2021 (Q7), 2024 (Q9)",
            desc: "Single Nodal Agency (SNA) reforms, delayed state matching grants, and SNA-SPARSH digital tracking.",
            ready: false
          }
        ]
      },
      {
        id: "theme-5",
        num: 5,
        title: "Pressure groups and formal/informal associations",
        fullTitle: "Pressure groups and formal/informal associations and their role in the Polity (alternatively grouped with Statutory, regulatory and various quasi-judicial bodies).",
        badge: "Theme 5",
        ico: "⚖️",
        desc: "Focuses on interest articulation in democratic polity: farmer unions, trade bodies (CII, FICCI), environmental lobbies, social movements, and regulatory commissions (CCI, TRAI, NGT).",
        clustersCount: 2,
        pyqsCount: 8,
        clusters: [
          {
            title: "Pressure Groups & Policy Negotiation",
            pyqs: "2014 (Q12), 2017 (Q10), 2022 (Q9)",
            desc: "Agrarian mobilization, corporate lobbying, environmental public hearings, and democratic policy input.",
            ready: false
          },
          {
            title: "Statutory & Quasi-Judicial Watchdogs",
            pyqs: "2016 (Q12), 2019 (Q9), 2023 (Q10)",
            desc: "Functional autonomy, appointment transparency, executive encroachment, and tribunalization issues.",
            ready: false
          }
        ]
      }
    ];

    // --- STATE MANAGEMENT ---
    let activeThemeId = "theme-2";
    let currentStep = 0;
    let userXp = 0;

    // --- DOM REFERENCES ---
    const themeTabsNav = document.getElementById("theme-tabs-nav");
    const themeDetailsArea = document.getElementById("theme-details-area");
    const learnModule = document.getElementById("learn-interactive-module");
    const learnScreenContent = document.getElementById("learn-screen-content");
    const learnProgressFill = document.getElementById("learn-progress-fill");
    const learnStepPill = document.getElementById("learn-step-pill");
    const btnQuitLearning = document.getElementById("btn-quit-learning");
    const themeToggleBtn = document.getElementById("theme-toggle-btn");

    // --- THEME TOGGLE (DARK / LIGHT) ---
    themeToggleBtn.addEventListener("click", () => {
      document.body.classList.toggle("light-mode");
      const isLight = document.body.classList.contains("light-mode");
      themeToggleBtn.textContent = isLight ? "☀️ Light" : "🌙 Dark";
    });

    // --- RENDER THEME TABS & CONTENT ---
    function renderThemeTabs() {
      themeTabsNav.querySelectorAll(".theme-tab-btn").forEach(btn => {
        btn.classList.toggle("active", btn.dataset.themeId === activeThemeId);
      });
      renderThemeContent(activeThemeId);
    }

    themeTabsNav.addEventListener("click", (e) => {
      const btn = e.target.closest(".theme-tab-btn");
      if (!btn) return;
      activeThemeId = btn.dataset.themeId;
      renderThemeTabs();
    });

    function renderThemeContent(themeId) {
      const theme = THEMES.find(t => t.id === themeId);
      if (!theme) return;

      let html = `
        <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:1rem; flex-wrap:wrap; gap:0.5rem;">
          <div>
            <span style="font-size:0.8rem; font-weight:800; background:rgba(37,99,235,0.18); color:#60a5fa; padding:3px 10px; border-radius:999px;">
              ${theme.badge}
            </span>
            <h3 style="font-size:1.45rem; margin:0.4rem 0 0.3rem; font-weight:800; color:var(--ink);">
              ${theme.ico} ${theme.fullTitle}
            </h3>
            <p style="color:var(--mut); font-size:0.95rem; margin:0; line-height:1.45; max-width:850px;">
              ${theme.desc}
            </p>
          </div>
          <div style="display:flex; gap:0.6rem; align-items:center;">
            <span class="badge badge-primary">${theme.clustersCount} Thematic Clusters</span>
            <span class="badge badge-success">${theme.pyqsCount} PYQs Mapped</span>
          </div>
        </div>
      `;

      if (theme.id === "theme-2") {
        html += `
          <div style="background:rgba(37,99,235,0.06); border:1.5px solid rgba(37,99,235,0.25); border-radius:14px; padding:1rem 1.25rem; margin-bottom:1.5rem;">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.4rem;">
              <span style="font-size:1.2rem;">🎯</span>
              <strong style="color:var(--ink); font-size:1.05rem;">The 5 PYQs of Theme 2 are clubbed into 3 Core Thematic Clusters:</strong>
            </div>
            <p style="color:var(--mut); font-size:0.9rem; margin:0; line-height:1.4;">
              Although UPSC changes phrasing each year, questions consistently revolve around three dimensions: <strong>Structure</strong>, <strong>Ethos & Neutrality</strong>, and <strong>Comprehensive Institutional Reforms</strong>.
            </p>
          </div>

          <div class="clusters-list">
        `;

        theme.clusters.forEach(cluster => {
          const isCluster1 = cluster.id === "cluster-1";
          html += `
            <div class="cluster-card ${isCluster1 ? 'active-cluster' : ''}" id="card-${cluster.id}">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.75rem; flex-wrap:wrap; gap:0.5rem;">
                <div>
                  <div style="display:flex; align-items:center; gap:0.5rem;">
                    <h4 style="font-size:1.25rem; margin:0; font-weight:800; color:var(--ink);">
                      ${cluster.title}
                    </h4>
                    ${isCluster1 ? '<span class="badge badge-success">Active & Ready</span>' : '<span class="badge" style="background:rgba(255,255,255,0.1); color:var(--mut);">Blueprint</span>'}
                  </div>
                  <div style="color:var(--gov-accent); font-weight:700; font-size:0.88rem; margin-top:0.25rem;">
                    Target PYQs: ${cluster.pyqs.map(p => p.year + ' (' + p.qnum + ')').join(', ')}
                  </div>
                </div>
                <div>
                  ${isCluster1 
                    ? `<button class="btn-3d btn-3d-amber" id="btn-start-cluster-1" style="font-size:0.95rem; padding:0.6rem 1.2rem;">
                         🚀 ${cluster.actionText}
                       </button>`
                    : `<button class="btn-3d btn-3d-secondary" onclick="alert('Cluster 2 & 3 thematic notes are integrated in the master repository. Focus on Cluster 1 now!')" style="font-size:0.85rem; padding:0.5rem 1rem;">
                         ${cluster.actionText}
                       </button>`
                  }
                </div>
              </div>

              <!-- Question excerpts -->
              <div style="display:flex; flex-direction:column; gap:0.5rem; margin-bottom:0.75rem;">
                ${cluster.pyqs.map(p => `
                  <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:10px; padding:0.65rem 0.9rem; font-size:0.9rem; line-height:1.35;">
                    <span style="font-weight:800; color:#60a5fa;">${p.year} (${p.qnum} | ${p.marks} | ${p.words}):</span>
                    <span style="color:var(--ink);"> ${p.text}</span>
                  </div>
                `).join('')}
              </div>

              <div style="font-size:0.88rem; color:var(--mut); line-height:1.4;">
                <strong style="color:var(--ink);">Why they club together:</strong> ${cluster.whyClubbed}
              </div>
            </div>
          `;
        });

        html += `</div>`;
      } else {
        // Other Themes
        html += `<div class="clusters-list">`;
        theme.clusters.forEach(c => {
          html += `
            <div class="cluster-card">
              <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:0.5rem;">
                <div>
                  <h4 style="font-size:1.15rem; margin:0; font-weight:800; color:var(--ink);">${c.title}</h4>
                  <div style="color:var(--gov-accent); font-size:0.85rem; font-weight:700;">PYQs: ${c.pyqs}</div>
                </div>
                ${c.link 
                  ? `<a href="${c.link}" class="btn-3d btn-3d-emerald" style="font-size:0.82rem; padding:0.4rem 0.9rem; text-decoration:none;">Open Module →</a>`
                  : `<span class="badge" style="background:rgba(255,255,255,0.08); color:var(--mut);">Scheduled</span>`
                }
              </div>
              <p style="margin:0; font-size:0.88rem; color:var(--mut); line-height:1.4;">${c.desc}</p>
            </div>
          `;
        });
        html += `</div>`;
      }

      themeDetailsArea.innerHTML = html;

      // Attach event listener to Start Cluster 1 button
      const btnCluster1 = document.getElementById("btn-start-cluster-1");
      if (btnCluster1) {
        btnCluster1.addEventListener("click", () => {
          startClusterLearning();
        });
      }
    }

    // --- MASTER INTERACTIVE LEARNING MODULE (CLUSTER 1) ---
    // Total steps:
    // 0: PYQ 1 (2016 Q14) + Demand
    // 1: PYQ 2 (2026 Q8) + Demand
    // 2: Thematic Convergence & Clubbing Rationale
    // 3: Historical / Evolution Angle Intro
    // 4: Contemporary / Generalist Angle Intro
    // 5: Dimension A: Structure, Culture & Impact
    // 6: Dimension B: Advantages & Limitations
    // 7: Checkpoint Quiz Round 1 (Macaulay, Trevelyan, Structure-Culture-Impact & Keyterms)
    // 8: Value Addition 1: Fulton Committee (1968) + Micro-Quiz
    // 9: Value Addition 2: 1st ARC (1966) + Micro-Quiz
    // 10: Value Addition 3: Surinder Nath Committee (2003) + Micro-Quiz
    // 11: Value Addition 4: 2nd ARC 10th & 13th Reports + Micro-Quiz
    // 12: Real-World Examples: Technocrat Titans + Match Quiz
    // 13: Real-World Example: Aspirational Districts Programme (Synergy) + Micro-Quiz
    // 14: Real-World Nuance: Lateral Entry Dilemma (2024 UPSC Withdrawal) + Micro-Quiz
    // 15: Way Forward, Ready-to-Use Conclusion & Final Mastery Synthesis
    // 16: Mastery Milestone Celebration Screen

    const TOTAL_STEPS = 16;

    function startClusterLearning() {
      currentStep = 0;
      themeDetailsArea.style.display = "none";
      document.getElementById("gov-main-header").style.display = "none";
      learnModule.style.display = "block";
      window.scrollTo({ top: 0, behavior: 'smooth' });
      renderStep();
    }

    btnQuitLearning.addEventListener("click", () => {
      if (confirm("Are you sure you want to exit Cluster 1 learning mode?")) {
        learnModule.style.display = "none";
        themeDetailsArea.style.display = "block";
        document.getElementById("gov-main-header").style.display = "block";
        window.scrollTo({ top: 0, behavior: 'smooth' });
      }
    });

    function updateProgress(stepNum) {
      const pct = Math.round((stepNum / TOTAL_STEPS) * 100);
      learnProgressFill.style.width = pct + "%";
      learnStepPill.textContent = `Step ${stepNum + 1} of ${TOTAL_STEPS + 1}`;
    }

    function renderStep() {
      updateProgress(currentStep);

      switch (currentStep) {
        case 0:
          renderStep0_PYQ1();
          break;
        case 1:
          renderStep1_PYQ2();
          break;
        case 2:
          renderStep2_Clubbing();
          break;
        case 3:
          renderStep3_HistIntro();
          break;
        case 4:
          renderStep4_ContempIntro();
          break;
        case 5:
          renderStep5_DimensionA();
          break;
        case 6:
          renderStep6_DimensionB();
          break;
        case 7:
          renderStep7_CheckpointQuiz();
          break;
        case 8:
          renderStep8_Fulton();
          break;
        case 9:
          renderStep9_ARC1();
          break;
        case 10:
          renderStep10_SurinderNath();
          break;
        case 11:
          renderStep11_ARC2();
          break;
        case 12:
          renderStep12_Titans();
          break;
        case 13:
          renderStep13_ADP();
          break;
        case 14:
          renderStep14_LateralEntry();
          break;
        case 15:
          renderStep15_WayForward();
          break;
        case 16:
          renderStep16_Celebration();
          break;
      }
    }

    // --- STEP 0: PYQ 1 (2016 Q14) ---
    function renderStep0_PYQ1() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Target PYQ 1 of 2
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">2016 (Q14)</span>
          </div>

          <h2 style="font-size:1.55rem; font-weight:800; margin:0 0 1rem; color:var(--ink);">
            Demystifying the Target Questions
          </h2>

          <div class="pyq-box">
            <div style="font-size:0.85rem; font-weight:800; color:#60a5fa; margin-bottom:0.4rem;">
              UPSC MAINS 2016 | GS PAPER 2 (Q14 | 12.5 MARKS | 200 WORDS)
            </div>
            <div style="font-size:1.35rem; font-weight:800; line-height:1.35; color:var(--ink);">
              “Traditional bureaucratic structure and culture have hampered the process of socio-economic development in India.” Comment.
            </div>
          </div>

          <div class="demand-box">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.6rem;">
              <span style="font-size:1.2rem;">🎯</span>
              <strong style="color:var(--gov-accent); font-size:1.05rem;">Core Demand of the Question:</strong>
            </div>
            <ul style="margin:0; padding-left:1.3rem; color:var(--ink); line-height:1.5; font-size:0.96rem;">
              <li><strong>Deconstruct Two Distinct Components:</strong> You must explicitly separate <b>Structural Bottlenecks</b> (rigid Weberian pyramid, 6-8 file noting tiers, ministerial silos, centralized command) from <b>Cultural Bottlenecks</b> (rule-orientation over outcome-orientation, "Mai-Baap" paternalism, status-quoism, and fear of 3Cs—CBI, CVC, CAG).</li>
              <li><strong>Link Directly to Socio-Economic Development:</strong> Explain how these bottlenecks derail capital expenditure, inflate project timelines, starve Panchayats of the 3Fs, and deny last-mile rights to marginalized citizens.</li>
              <li><strong>Directive ("Comment"):</strong> While validating the critique, provide a balanced counter-perspective (bureaucracy as the national stabilizer during crises) and lay out structural remedies (Mission Karmayogi, de-layering).</li>
            </ul>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step">
              Continue to PYQ 2 →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 1: PYQ 2 (2026 Q8) ---
    function renderStep1_PYQ2() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Target PYQ 2 of 2
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">2026 (Q8)</span>
          </div>

          <h2 style="font-size:1.55rem; font-weight:800; margin:0 0 1rem; color:var(--ink);">
            Demystifying the Target Questions
          </h2>

          <div class="pyq-box">
            <div style="font-size:0.85rem; font-weight:800; color:#60a5fa; margin-bottom:0.4rem;">
              UPSC MAINS 2026 | GS PAPER 2 (Q8 | 10 MARKS | 150 WORDS)
            </div>
            <div style="font-size:1.35rem; font-weight:800; line-height:1.35; color:var(--ink);">
              “Analyse the advantages and limitations of the generalist structure of the Indian Civil Services in contemporary governance.”
            </div>
          </div>

          <div class="demand-box">
            <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.6rem;">
              <span style="font-size:1.2rem;">🎯</span>
              <strong style="color:var(--gov-accent); font-size:1.05rem;">Core Demand of the Question:</strong>
            </div>
            <ul style="margin:0; padding-left:1.3rem; color:var(--ink); line-height:1.5; font-size:0.96rem;">
              <li><strong>The Macaulay / Northcote-Trevelyan Legacy:</strong> Critically assess the 19th-century premise that a liberal-arts "all-rounder" can steer any government ministry.</li>
              <li><strong>Advantages (Why it Still Matters):</strong> Highlight grassroots district immersion (SDM/DM), holistic inter-departmental integration without specialist "tunnel vision", crisis & disaster command agility, and All-India federal glue.</li>
              <li><strong>Limitations in 21st-Century Governance:</strong> Expose severe domain asymmetry in complex domains (AI regulation, semiconductor supply chains, WTO dispute settlement, carbon markets), frequent 18-month rotations causing institutional amnesia, and demotivation of technical services.</li>
              <li><strong>Balanced Way Forward:</strong> Propose the "Generalist-Plus" model (mid-career domain specialization after 10-12 years) and institutionalized lateral entry.</li>
            </ul>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step">
              Continue to Thematic Clubbing →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 2: CLUBBING RATIONALE ---
    function renderStep2_Clubbing() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <span style="font-weight:800; color:var(--gov-teal); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
            Thematic Synthesis
          </span>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0.3rem 0 1rem; color:var(--ink);">
            Why These 2 PYQs Club Together into Cluster 1
          </h2>

          <div style="background:var(--card-sub); border:2px solid var(--line); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              Although UPSC framed the prompt differently in 2016 and 2026, both questions test the exact same foundational tension:
            </p>
            <div style="display:flex; align-items:center; gap:0.75rem; background:rgba(37,99,235,0.12); padding:1rem; border-radius:12px; margin-bottom:1rem;">
              <span style="font-size:2rem;">⚖️</span>
              <div style="font-size:1.02rem; font-weight:700;">
                A 19th-Century Colonial Regulatory Apparatus (Steel Frame) <br>
                <span style="color:#60a5fa;">VERSUS</span> <br>
                A 21st-Century Dynamic Knowledge Economy & Developmental Welfare State.
              </div>
            </div>
            <p style="margin:0; font-size:0.95rem; color:var(--mut);">
              By mastering this single cluster, you prepare ready-to-deploy blueprints for introductions, structural-cultural matrices, committee citations (Fulton, 1st ARC, Surinder Nath, 2nd ARC), and the Mission Karmayogi Bamboo Frame conclusion.
            </p>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d btn-3d-amber" id="btn-next-step">
              Start Learning: Introductions →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 3: HISTORICAL / EVOLUTION INTRO ---
    function renderStep3_HistIntro() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Introduction Part 1 of 2
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">Best for 2016 Q14</span>
          </div>

          <h2 style="font-size:1.55rem; font-weight:800; margin:0 0 1rem; color:var(--ink);">
            1. Historical / Evolution Angle Introduction
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(37,99,235,0.4); border-left:6px solid #2563eb; border-radius:14px; padding:1.35rem 1.5rem; margin-bottom:1.5rem;">
            <div style="font-size:0.82rem; font-weight:800; color:#60a5fa; text-transform:uppercase; margin-bottom:0.4rem;">
              Ready-to-Use High-Scoring Intro:
            </div>
            <blockquote style="margin:0; font-size:1.12rem; font-weight:600; line-height:1.5; color:var(--ink); font-style:normal;">
              “Rooted in the <b>Macaulay Committee (1854)</b> and Weberian legal-rational model, Indian bureaucracy was originally designed as a regulatory <b>'Steel Frame'</b> for law-and-order maintenance and revenue extraction, rather than as a dynamic instrument of post-independence socio-economic transformation.”
            </blockquote>
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:var(--gov-accent);">🏛️ Macaulay Committee 1854:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">Established competitive merit exam for an elite regulatory administrative cadre.</p>
            </div>
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#60a5fa;">⚙️ Weberian Legal-Rationalism:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">Strict hierarchy, impersonal file procedures, rule adherence prioritizing process over speed.</p>
            </div>
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#f87171;">💰 Extractive DNA:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">Created to siphon colonial tax revenue, later awkwardly repurposed to deliver socialist welfare.</p>
            </div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step">
              Continue to Contemporary Intro →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 4: CONTEMPORARY / GENERALIST INTRO ---
    function renderStep4_ContempIntro() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Introduction Part 2 of 2
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">Best for 2026 Q8</span>
          </div>

          <h2 style="font-size:1.55rem; font-weight:800; margin:0 0 1rem; color:var(--ink);">
            2. Contemporary / Generalist Angle Introduction
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(245,158,11,0.4); border-left:6px solid var(--gov-accent); border-radius:14px; padding:1.35rem 1.5rem; margin-bottom:1.5rem;">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); text-transform:uppercase; margin-bottom:0.4rem;">
              Ready-to-Use High-Scoring Intro:
            </div>
            <blockquote style="margin:0; font-size:1.12rem; font-weight:600; line-height:1.5; color:var(--ink); font-style:normal;">
              “As India transitions from a basic welfare regulator to a complex knowledge economy managing <b>AI regulation</b>, <b>semiconductor supply chains</b>, and <b>climate finance</b>, the 19th-century <b>Northcote-Trevelyan model of the 'all-rounder generalist'</b> faces a severe structural stress test.”
            </blockquote>
          </div>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(220px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:var(--gov-accent);">📜 Northcote-Trevelyan (1854):</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">Premise that gentlemen with general liberal arts training can intuitively supervise any ministry.</p>
            </div>
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#60a5fa;">🔬 Modern Knowledge Economy:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">WTO disputes, carbon border taxes (CBAM), and algorithmic governance demand deep technical domain mastery.</p>
            </div>
            <div style="background:var(--card-bg); border:1px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#10b981;">⚡ Structural Stress Test:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.4rem 0 0;">Generalist rotation every 18 months leaves secretaries dependent on private consulting firms (Big Four).</p>
            </div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d btn-3d-amber" id="btn-next-step">
              Proceed to Dimension A: Structure, Culture & Impact →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 5: DIMENSION A (STRUCTURE, CULTURE & IMPACT) ---
    function renderStep5_DimensionA() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
            Core Dimension A (2016 Q14 Core)
          </span>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0.3rem 0 0.5rem; color:var(--ink);">
            Why Traditional Structure & Culture Hamper Development
          </h2>
          <p style="color:var(--mut); font-size:0.95rem; margin-bottom:1.5rem;">
            Notice how every <b>Structural Bottleneck</b> pairs with a toxic <b>Cultural Bottleneck</b> to create a catastrophic <b>Developmental Impact</b>:
          </p>

          <div class="triad-grid">
            <!-- Triad 1 -->
            <div class="triad-card" style="border-top:4px solid #2563eb;">
              <div style="font-size:0.8rem; font-weight:800; color:#60a5fa; margin-bottom:0.4rem;">BOTTLENECK 1: HIERARCHY & RED TAPE</div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-struct">Structural</span>
                <strong style="display:block; margin-top:2px;">Rigid Weberian Hierarchy:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Steep pyramid with 6 to 8 layers of file noting (Section Officer to Secretary).</span>
              </div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-cult">Cultural</span>
                <strong style="display:block; margin-top:2px;">Rule over Outcome:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Obsession with procedural compliance (<b>Red-Tapism</b>) rather than timely citizen delivery.</span>
              </div>
              <div>
                <span class="triad-tag tag-imp">Impact on Development</span>
                <strong style="display:block; margin-top:2px; color:#f87171;">Delayed Infrastructure & Welfare:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Severe cost/time overruns; public capital expenditure lapses at year-end.</span>
              </div>
            </div>

            <!-- Triad 2 -->
            <div class="triad-card" style="border-top:4px solid var(--gov-purple);">
              <div style="font-size:0.8rem; font-weight:800; color:#a78bfa; margin-bottom:0.4rem;">BOTTLENECK 2: SILOS & TURF</div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-struct">Structural</span>
                <strong style="display:block; margin-top:2px;">Departmental Silos:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Artificial splitting of interconnected developmental sectors into siloed ministries.</span>
              </div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-cult">Cultural</span>
                <strong style="display:block; margin-top:2px;">Turf Consciousness:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Jealously guarding administrative jurisdiction; refusal to share data or coordinate.</span>
              </div>
              <div>
                <span class="triad-tag tag-imp">Impact on Development</span>
                <strong style="display:block; margin-top:2px; color:#f87171;">Policy Incoherence:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">E.g., Water governance fragmented across Jal Shakti, Agriculture, Environment, and Rural Development.</span>
              </div>
            </div>

            <!-- Triad 3 -->
            <div class="triad-card" style="border-top:4px solid var(--gov-accent);">
              <div style="font-size:0.8rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.4rem;">BOTTLENECK 3: CENTRALIZATION & PATERNALISM</div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-struct">Structural</span>
                <strong style="display:block; margin-top:2px;">Centralized Command:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Financial and administrative sanctioning power concentrated in the Secretariat.</span>
              </div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-cult">Cultural</span>
                <strong style="display:block; margin-top:2px;">'Mai-Baap' Paternalism:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Viewing citizens as passive charity beneficiaries rather than sovereign rights-holders.</span>
              </div>
              <div>
                <span class="triad-tag tag-imp">Impact on Development</span>
                <strong style="display:block; margin-top:2px; color:#f87171;">Starving Local Bodies:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Subverts 73rd/74th Amendments by withholding 3Fs (Funds, Functions, Functionaries) from Panchayats.</span>
              </div>
            </div>

            <!-- Triad 4 -->
            <div class="triad-card" style="border-top:4px solid var(--gov-rose);">
              <div style="font-size:0.8rem; font-weight:800; color:#fb7185; margin-bottom:0.4rem;">BOTTLENECK 4: RISK AVERSION & PARALYSIS</div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-struct">Structural</span>
                <strong style="display:block; margin-top:2px;">Lack of Inaction Accountability:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Routine APAR penalizes errors of commission, but ignores colossal errors of omission.</span>
              </div>
              <div style="margin-bottom:0.5rem;">
                <span class="triad-tag tag-cult">Cultural</span>
                <strong style="display:block; margin-top:2px;">Status-Quoism & 3Cs Fear:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Entrenched fear of <b>CBI, CVC, CAG</b> leading to defensive decision-making.</span>
              </div>
              <div>
                <span class="triad-tag tag-imp">Impact on Development</span>
                <strong style="display:block; margin-top:2px; color:#f87171;">Stifled Public Innovation:</strong>
                <span style="font-size:0.88rem; color:var(--mut);">Bureaucratic paralysis; officers avoid bold PPP projects, quick procurement, or developmental risks.</span>
              </div>
            </div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d btn-3d-amber" id="btn-next-step">
              Proceed to Dimension B: Generalist Advantages & Limitations →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 6: DIMENSION B (ADVANTAGES & LIMITATIONS) ---
    function renderStep6_DimensionB() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
            Core Dimension B (2026 Q8 Core)
          </span>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0.3rem 0 0.5rem; color:var(--ink);">
            The Generalist Structure: Advantages vs. Limitations
          </h2>
          <p style="color:var(--mut); font-size:0.95rem; margin-bottom:1.5rem;">
            A balanced evaluation of the Northcote-Trevelyan all-rounder paradigm in contemporary Indian governance:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(320px, 1fr)); gap:1.25rem; margin-bottom:1.5rem;">
            
            <!-- ADVANTAGES -->
            <div style="background:rgba(16,185,129,0.06); border:2px solid rgba(16,185,129,0.3); border-radius:16px; padding:1.25rem;">
              <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
                <span style="font-size:1.3rem;">🛡️</span>
                <h3 style="font-size:1.2rem; margin:0; font-weight:800; color:#34d399;">
                  5 Enduring Advantages (Why it Still Matters)
                </h3>
              </div>
              <ol style="margin:0; padding-left:1.2rem; color:var(--ink); font-size:0.92rem; line-height:1.5;">
                <li style="margin-bottom:0.6rem;">
                  <strong>Grassroots Field Exposure:</strong> Early postings as SDM and District Collector expose officers to rural distress, caste fractures, and delivery realities—bringing ground truth to Secretariat policy.
                </li>
                <li style="margin-bottom:0.6rem;">
                  <strong>Holistic Inter-Departmental Coordination:</strong> Acts as a neutral integrator across line departments (Health, PWD, Police, Agriculture), curing narrow specialist <b>“tunnel vision”</b>.
                </li>
                <li style="margin-bottom:0.6rem;">
                  <strong>Crisis & Disaster Agility:</strong> Command agility in multi-agency emergencies (COVID-19 lockdowns, Cyclone Dana evacuations, law-and-order flare-ups).
                </li>
                <li style="margin-bottom:0.6rem;">
                  <strong>Federal Glue & National Unity:</strong> All-India Services (IAS/IPS) maintain uniform administrative vocabulary and national outlook (<b>Sardar Patel's "Steel Frame"</b>).
                </li>
                <li>
                  <strong>Buffer for Political Executive:</strong> Translates technical jargon into politically viable, constitutionally sound policy choices for Ministers.
                </li>
              </ol>
            </div>

            <!-- LIMITATIONS -->
            <div style="background:rgba(239,68,68,0.06); border:2px solid rgba(239,68,68,0.3); border-radius:16px; padding:1.25rem;">
              <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
                <span style="font-size:1.3rem;">⚠️</span>
                <h3 style="font-size:1.2rem; margin:0; font-weight:800; color:#f87171;">
                  4 Critical Limitations in Contemporary Era
                </h3>
              </div>
              <ol style="margin:0; padding-left:1.2rem; color:var(--ink); font-size:0.92rem; line-height:1.5;">
                <li style="margin-bottom:0.6rem;">
                  <strong>Domain Asymmetry in Tech Frontiers:</strong> Modern policymaking in FinTech, WTO disputes, carbon markets, and AI requires deep domain mastery that rapid rotations cannot provide.
                </li>
                <li style="margin-bottom:0.6rem;">
                  <strong>Erosion of Institutional Memory:</strong> Frequent musical-chair transfers (every 18 months) leave officers dependent on lower clerks or private consultants (Big Four).
                </li>
                <li style="margin-bottom:0.6rem;">
                  <strong>Demotivation of Domain Specialists:</strong> Monopoly of top posts (Joint Secretary and above) by generalists breeds resentment among technical services (IRS, IA&AS, engineers, scientists).
                </li>
                <li>
                  <strong>Flawed Regulatory Drafting:</strong> Inadequate technical grasp leads to poorly designed laws, contentious retrospective taxes, and flawed technical tenders.
                </li>
              </ol>
            </div>

          </div>

          <div style="text-align:right;">
            <button class="btn-3d btn-3d-amber" id="btn-next-step">
              Start Checkpoint Practice Quizzes →
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-next-step").onclick = () => {
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 7: CHECKPOINT QUIZ ROUND 1 ---
    function renderStep7_CheckpointQuiz() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Interactive Retrieval Checkpoint
            </span>
            <span class="badge badge-success">+50 XP Drill</span>
          </div>
          <h2 style="font-size:1.55rem; font-weight:800; margin:0 0 0.5rem; color:var(--ink);">
            Test Your Mastery: Macaulay, Dimensions & Keyterms
          </h2>
          <p style="color:var(--mut); font-size:0.92rem; margin-bottom:1.25rem;">
            Answer the interactive prompts below to lock these concepts into long-term memory:
          </p>

          <!-- QUIZ 1: MACAULAY COMMITTEE -->
          <div class="quiz-card" id="q1-box">
            <div style="font-size:0.82rem; font-weight:800; color:#60a5fa; margin-bottom:0.3rem;">QUESTION 1 OF 5 (CORE PURPOSE)</div>
            <div style="font-size:1.05rem; font-weight:700; color:var(--ink); margin-bottom:0.75rem;">
              What was the primary constitutional purpose of the Indian Civil Service as created by the Macaulay Committee (1854)?
            </div>
            <button class="quiz-opt" data-q="1" data-ans="0">Democratic participatory planning and grassroots social empowerment</button>
            <button class="quiz-opt" data-q="1" data-ans="1">A colonial 'Steel Frame' for law-and-order maintenance and revenue extraction</button>
            <button class="quiz-opt" data-q="1" data-ans="2">Managing industrial public sector undertakings and infrastructure projects</button>
            <div class="feedback-banner" id="fb-q1"></div>
          </div>

          <!-- QUIZ 2: RED FLAG (THE 3Cs) -->
          <div class="quiz-card" id="q2-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">QUESTION 2 OF 5 (TAP THE RED FLAG)</div>
            <div style="font-size:1.05rem; font-weight:700; color:var(--ink); margin-bottom:0.75rem;">
              Tap the one FALSE segment in this statement:
            </div>
            <div style="background:var(--card-bg); padding:1rem; border-radius:12px; border:1px solid var(--line); font-size:1.05rem; line-height:1.6;">
              <span class="flag-segment" data-seg="0">Status-quoism in civil services is driven by fear of the 3Cs,</span>
              <span class="flag-segment" data-seg="1">which strictly comprise the CBI, the CVC,</span>
              <span class="flag-segment" data-seg="2">and NITI Aayog.</span>
            </div>
            <div class="feedback-banner" id="fb-q2"></div>
          </div>

          <!-- QUIZ 3: SORTING STRUCTURAL VS CULTURAL -->
          <div class="quiz-card" id="q3-box">
            <div style="font-size:0.82rem; font-weight:800; color:#a78bfa; margin-bottom:0.3rem;">QUESTION 3 OF 5 (SORT THE BOTTLENECK)</div>
            <div style="font-size:1.05rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              Sort this item into its correct category:
            </div>
            <div class="sort-card-holder" id="sort-term-display">
              "Viewing citizens as passive charity recipients ('Mai-Baap' attitude)"
            </div>
            <div class="sort-bins-row" style="margin-top:1rem;">
              <button class="sort-bin-btn" data-bin="struct">🏛️ Structural</button>
              <button class="sort-bin-btn" data-bin="cult">🎭 Cultural</button>
              <button class="sort-bin-btn" data-bin="imp">💥 Impact</button>
            </div>
            <div class="feedback-banner" id="fb-q3"></div>
          </div>

          <!-- QUIZ 4: GENERALIST ADVANTAGE VS LIMITATION -->
          <div class="quiz-card" id="q4-box">
            <div style="font-size:0.82rem; font-weight:800; color:#34d399; margin-bottom:0.3rem;">QUESTION 4 OF 5 (ADVANTAGE VS LIMITATION)</div>
            <div style="font-size:1.05rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              Sort this trait:
            </div>
            <div class="sort-card-holder" id="sort-gen-display">
              "Prevents narrow specialist 'tunnel vision' across conflicting line departments"
            </div>
            <div class="sort-bins-row" style="margin-top:1rem;">
              <button class="sort-bin-btn" data-bin="adv">🛡️ Generalist Advantage</button>
              <button class="sort-bin-btn" data-bin="lim">⚠️ Generalist Limitation</button>
            </div>
            <div class="feedback-banner" id="fb-q4"></div>
          </div>

          <!-- QUIZ 5: KEYTERMS MATCH -->
          <div class="quiz-card" id="q5-box">
            <div style="font-size:0.82rem; font-weight:800; color:#f472b6; margin-bottom:0.3rem;">QUESTION 5 OF 5 (KEYTERMS CONCEPT)</div>
            <div style="font-size:1.05rem; font-weight:700; color:var(--ink); margin-bottom:0.75rem;">
              Which term describes civil servants taking no bold initiatives due to fear that bona fide commercial risk will trigger corruption probes?
            </div>
            <button class="quiz-opt" data-q="5" data-ans="0">Policy Paralysis (Status-Quoism)</button>
            <button class="quiz-opt" data-q="5" data-ans="1">Lateral Induction</button>
            <button class="quiz-opt" data-q="5" data-ans="2">Domain Specialization</button>
            <div class="feedback-banner" id="fb-q5"></div>
          </div>

          <div style="text-align:right; margin-top:1.5rem;">
            <button class="btn-3d btn-3d-amber" id="btn-next-step" disabled style="opacity:0.6;">
              Pass All Drills to Continue →
            </button>
          </div>
        </div>
      `;

      // Handlers for Quizzes
      let passed = { q1: false, q2: false, q3: false, q4: false, q5: false };

      function checkAllPassed() {
        if (passed.q1 && passed.q2 && passed.q3 && passed.q4 && passed.q5) {
          const btn = document.getElementById("btn-next-step");
          btn.disabled = false;
          btn.style.opacity = "1";
          btn.classList.add("btn-3d-emerald");
          btn.textContent = "All Passed! Continue to High-Scoring Value Additions →";
        }
      }

      // Q1 Handlers
      document.querySelectorAll('#q1-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-q1');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Correct!</strong> Macaulay (1854) designed the ICS as an extractive & regulatory Steel Frame, not a developmental welfare engine.";
            passed.q1 = true;
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Post-independence welfare was superimposed onto an extractive colonial administrative frame.";
          }
          checkAllPassed();
        };
      });

      // Q2 Handlers (Red Flag)
      document.querySelectorAll('.flag-segment').forEach(seg => {
        seg.onclick = () => {
          const fb = document.getElementById('fb-q2');
          if (seg.dataset.seg === "2") {
            seg.classList.add('flag-bad');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Red Flag Spotted!</strong> The 3Cs are the <b>CBI</b>, <b>CVC</b>, and <b>CAG</b> (Comptroller & Auditor General), NOT NITI Aayog!";
            passed.q2 = true;
          } else {
            seg.classList.add('flag-ok');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Try again!</strong> That segment is accurate. Spot which watchdog is falsely named.";
          }
          checkAllPassed();
        };
      });

      // Q3 Handlers (Sorting)
      document.querySelectorAll('#q3-box .sort-bin-btn').forEach(btn => {
        btn.onclick = () => {
          const fb = document.getElementById('fb-q3');
          if (btn.dataset.bin === "cult") {
            btn.style.background = "var(--okbg)";
            btn.style.borderColor = "var(--ok)";
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Spot on!</strong> 'Mai-Baap' paternalism is an entrenched <b>cultural bottleneck</b> where citizens are treated as charity recipients rather than sovereign rights-holders.";
            passed.q3 = true;
          } else {
            btn.style.background = "var(--nobg)";
            btn.style.borderColor = "var(--no)";
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Not quite.</strong> Structural relates to organizational layout (hierarchies/silos); viewing citizens paternalistically is a mindset/cultural defect.";
          }
          checkAllPassed();
        };
      });

      // Q4 Handlers
      document.querySelectorAll('#q4-box .sort-bin-btn').forEach(btn => {
        btn.onclick = () => {
          const fb = document.getElementById('fb-q4');
          if (btn.dataset.bin === "adv") {
            btn.style.background = "var(--okbg)";
            btn.style.borderColor = "var(--ok)";
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Exactly!</strong> Preventing narrow specialist 'tunnel vision' is a premier <b>advantage</b> of the generalist coordinator.";
            passed.q4 = true;
          } else {
            btn.style.background = "var(--nobg)";
            btn.style.borderColor = "var(--no)";
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> This is a core advantage that justifies retaining generalists at district and state coordination levels.";
          }
          checkAllPassed();
        };
      });

      // Q5 Handlers
      document.querySelectorAll('#q5-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-q5');
          if (opt.dataset.ans === "0") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Correct!</strong> <b>Policy Paralysis</b> occurs when defensive civil servants delay or avoid decisions due to fear of retrospective audits.";
            passed.q5 = true;
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Fear of the 3Cs driving inaction is defined as Policy Paralysis.";
          }
          checkAllPassed();
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 50;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 8: VALUE ADDITION 1 - FULTON COMMITTEE ---
    function renderStep8_Fulton() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              High-Scoring Value Addition 1 of 4
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">Global Precedent</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            The Fulton Committee (UK, 1968): “The Cult of the Amateur”
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(37,99,235,0.3); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              The British Civil Service, which originally birthed the Northcote-Trevelyan generalist all-rounder model, conducted a ruthless soul-searching inquiry via the <b>Fulton Committee in 1968</b>.
            </p>
            <div style="background:rgba(37,99,235,0.1); border-left:5px solid #2563eb; padding:1rem 1.25rem; border-radius:10px; margin-bottom:1rem;">
              <strong style="color:#60a5fa; font-size:1.05rem;">The Landmark Finding:</strong>
              <p style="margin:0.4rem 0 0; color:var(--ink); font-size:1.02rem;">
                The Fulton Report famously criticized the civil service for being gripped by the <b>“Cult of the Amateur”</b>—the deeply flawed assumption that men trained in classics or liberal arts could manage scientific, industrial, economic, and technical state policies without domain expertise.
              </p>
            </div>
            <p style="margin:0; font-size:0.92rem; color:var(--mut);">
              <strong>Mains Application (2026 Q8):</strong> Cite Fulton to argue that the crisis of generalist obsolescence is not unique to India, but a structural inevitability of the 19th-century colonial personnel design.
            </p>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="va1-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              Which committee coined the immortal critique "Cult of the Amateur" against generalist dominance?
            </div>
            <button class="quiz-opt" data-ans="0">Fulton Committee (UK, 1968)</button>
            <button class="quiz-opt" data-ans="1">Macaulay Committee (1854)</button>
            <button class="quiz-opt" data-ans="2">Sarkaria Commission (1988)</button>
            <div class="feedback-banner" id="fb-va1"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#va1-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-va1');
          if (opt.dataset.ans === "0") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Bingo!</strong> The Fulton Committee (UK, 1968) denounced the generalist administrative monopoly as the 'cult of the amateur'.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to 1st ARC (1966) →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Review the text above—it is the Fulton Committee (1968).";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 9: VALUE ADDITION 2 - 1ST ARC ---
    function renderStep9_ARC1() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              High-Scoring Value Addition 2 of 4
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">1st ARC Roadmap</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            1st ARC (1966): 8 Functional Areas for Specialization
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(16,185,129,0.3); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              Chaired initially by Morarji Desai and later K. Hanumanthaiah, the <b>First Administrative Reforms Commission (1966)</b> warned that the complex task of national development could not be run by pure generalists.
            </p>
            <div style="background:rgba(16,185,129,0.1); border-left:5px solid #10b981; padding:1rem 1.25rem; border-radius:10px; margin-bottom:1rem;">
              <strong style="color:#34d399; font-size:1.05rem;">The 1st ARC Recommendation:</strong>
              <p style="margin:0.4rem 0 0; color:var(--ink); font-size:1.02rem;">
                Civil service positions should be classified into <b>8 functional areas</b> (Economic Administration, Industrial Administration, Agriculture, Social Development, Personnel, Financial, Defense/Security, and General Administration) so officers develop mid-career specialized competence.
              </p>
            </div>
            <p style="margin:0; font-size:0.92rem; color:var(--mut);">
              <strong>Mains Application:</strong> Demonstrates that mid-career domain specialization has been recommended since the 1960s, proving that modern reform is long overdue.
            </p>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="va2-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              The 1st ARC (1966) recommended grouping civil service posts into how many functional areas?
            </div>
            <button class="quiz-opt" data-ans="0">3 broad tiers</button>
            <button class="quiz-opt" data-ans="1">8 functional areas</button>
            <button class="quiz-opt" data-ans="2">18 ministerial cadres</button>
            <div class="feedback-banner" id="fb-va2"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#va2-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-va2');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Accurate!</strong> 1st ARC (1966) recommended grouping posts into <b>8 functional areas</b>.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to Surinder Nath Committee (2003) →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Remember the number 8 (8 functional areas).";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 10: VALUE ADDITION 3 - SURINDER NATH COMMITTEE ---
    function renderStep10_SurinderNath() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              High-Scoring Value Addition 3 of 4
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">Domain Mapping</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            Surinder Nath Committee (2003): 11 Domain Clusters
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(245,158,11,0.3); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              Set up by the Government of India in 2003 to examine civil service career management, the <b>Surinder Nath Committee</b> tackled the chaotic rotational transfer system.
            </p>
            <div style="background:rgba(245,158,11,0.1); border-left:5px solid var(--gov-accent); padding:1rem 1.25rem; border-radius:10px; margin-bottom:1rem;">
              <strong style="color:var(--gov-accent); font-size:1.05rem;">The 11 Domain Clusters Proposal:</strong>
              <p style="margin:0.4rem 0 0; color:var(--ink); font-size:1.02rem;">
                Proposed assigning every civil servant to <b>11 specific domain clusters</b> (Agriculture, Energy, Finance, Health, Social Welfare, Industry, Infrastructure, etc.) based on proven academic aptitude and early field record, ending random transfers.
              </p>
            </div>
            <p style="margin:0; font-size:0.92rem; color:var(--mut);">
              <strong>Mains Application:</strong> Essential value addition to quote when answering how to transition from generalist anarchy to structured domain expertise.
            </p>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="va3-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              How many domain clusters did the Surinder Nath Committee (2003) recommend?
            </div>
            <button class="quiz-opt" data-ans="0">5 macro ministries</button>
            <button class="quiz-opt" data-ans="1">11 specific domain clusters</button>
            <button class="quiz-opt" data-ans="2">28 state cadres</button>
            <div class="feedback-banner" id="fb-va3"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#va3-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-va3');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Superb!</strong> Surinder Nath Committee (2003) recommended <b>11 domain clusters</b>.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to 2nd ARC (10th & 13th Reports) →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Surinder Nath proposed 11 domain clusters.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 11: VALUE ADDITION 4 - 2ND ARC ---
    function renderStep11_ARC2() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              High-Scoring Value Addition 4 of 4
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">2nd ARC Master Reports</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            2nd ARC: 10th & 13th Reports on Personnel & Structures
          </h2>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(300px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <!-- 10th Report -->
            <div style="background:var(--card-sub); border:2px solid var(--line); border-left:5px solid #2563eb; border-radius:14px; padding:1.2rem;">
              <span class="badge" style="background:#2563eb; color:#fff; margin-bottom:0.4rem;">10th Report: Refurbishing Personnel</span>
              <strong style="display:block; font-size:1.05rem; margin-bottom:0.4rem;">Domain Specialization after 13 Years:</strong>
              <p style="font-size:0.92rem; color:var(--mut); line-height:1.45; margin:0 0 0.5rem;">
                Mandated that after <b>13 years of service</b>, officers must be assigned to specialized domains.
              </p>
              <p style="font-size:0.92rem; color:var(--ink); line-height:1.45; margin:0;">
                Also recommended throwing open all Senior Management (SAG/HAG) posts to open competition between IAS, Central Services, and outside domain talent.
              </p>
            </div>

            <!-- 13th Report -->
            <div style="background:var(--card-sub); border:2px solid var(--line); border-left:5px solid #10b981; border-radius:14px; padding:1.2rem;">
              <span class="badge" style="background:#10b981; color:#fff; margin-bottom:0.4rem;">13th Report: Organizational Structure</span>
              <strong style="display:block; font-size:1.05rem; margin-bottom:0.4rem;">Flatter, Mission-Mode Structures:</strong>
              <p style="font-size:0.92rem; color:var(--mut); line-height:1.45; margin:0 0 0.5rem;">
                Replace steep 6-to-8 tier Weberian hierarchies with <b>flatter, mission-mode executive agencies</b>.
              </p>
              <p style="font-size:0.92rem; color:var(--ink); line-height:1.45; margin:0;">
                Abolish archaic file movement by empowering Desk Officers with direct decision-making sanctions.
              </p>
            </div>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="va4-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              According to the 2nd ARC 10th Report, after how many years of service should domain specialization become mandatory?
            </div>
            <button class="quiz-opt" data-ans="0">3 years (right after probation)</button>
            <button class="quiz-opt" data-ans="1">13 years of service</button>
            <button class="quiz-opt" data-ans="2">25 years (at Additional Secretary rank)</button>
            <div class="feedback-banner" id="fb-va4"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#va4-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-va4');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Spot on!</strong> The 2nd ARC 10th Report recommended domain assignment after <b>13 years</b> of service.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to Technocrat Titans Examples →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> The exact 2nd ARC benchmark is 13 years.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 12: REAL-WORLD EXAMPLES - TECHNOCRAT TITANS ---
    function renderStep12_Titans() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Real-World Examples & Case Studies (1 of 3)
            </span>
            <span class="badge" style="background:#2563eb; color:#fff;">Technocrat Titans</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            The Power of Domain Mastery: 5 Iconic Technocrats
          </h2>
          <p style="color:var(--mut); font-size:0.95rem; margin-bottom:1.25rem;">
            Whenever Indian governance entrusted complex sectors to specialized domain leaders, transformational revolutions were born:
          </p>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <div style="font-size:1.5rem; margin-bottom:0.25rem;">🥛</div>
              <strong style="color:var(--ink); font-size:1.02rem;">Dr. Verghese Kurien:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Dairy engineer who spearheaded <b>Operation Flood (White Revolution)</b> and built the AMUL cooperative, turning milk-deficit India into the world's #1 milk producer.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <div style="font-size:1.5rem; margin-bottom:0.25rem;">🌾</div>
              <strong style="color:var(--ink); font-size:1.02rem;">Dr. M.S. Swaminathan:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Agricultural geneticist whose scientific leadership in the <b>Green Revolution</b> rescued India from humiliating "ship-to-mouth" PL-480 famine dependency.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <div style="font-size:1.5rem; margin-bottom:0.25rem;">🚇</div>
              <strong style="color:var(--ink); font-size:1.02rem;">E. Sreedharan ("Metro Man"):</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Civil engineer granted complete autonomous executive authority to deliver <b>Konkan Railway</b> and <b>Delhi Metro</b> ahead of schedule and within budget.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <div style="font-size:1.5rem; margin-bottom:0.25rem;">🆔</div>
              <strong style="color:var(--ink); font-size:1.02rem;">Nandan Nilekani (UIDAI):</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Corporate technocrat inducted laterally with Cabinet rank to architect <b>Aadhaar</b>, the digital identity foundation for 1.4 billion citizens.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <div style="font-size:1.5rem; margin-bottom:0.25rem;">🚽</div>
              <strong style="color:var(--ink); font-size:1.02rem;">Parameswaran Iyer (SBM):</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Water and sanitation specialist inducted laterally as Secretary to lead the behavior-change juggernaut of <b>Swachh Bharat Mission (Grameen)</b>.
              </p>
            </div>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="titans-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              Which corporate technocrat was brought in laterally with Cabinet status to architect India's Aadhaar digital identity infrastructure?
            </div>
            <button class="quiz-opt" data-ans="0">Dr. M.S. Swaminathan</button>
            <button class="quiz-opt" data-ans="1">Nandan Nilekani</button>
            <button class="quiz-opt" data-ans="2">E. Sreedharan</button>
            <div class="feedback-banner" id="fb-titans"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#titans-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-titans');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Correct!</strong> Nandan Nilekani was inducted laterally to lead UIDAI and scale Aadhaar.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to Synergy Example (ADP) →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Nandan Nilekani led UIDAI.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 13: REAL-WORLD EXAMPLE - ADP (SYNERGY) ---
    function renderStep13_ADP() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Real-World Examples & Case Studies (2 of 3)
            </span>
            <span class="badge" style="background:#10b981; color:#fff;">Synergy Masterclass</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            Generalist-Specialist Synergy: Aspirational Districts Programme (ADP)
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(16,185,129,0.3); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              The false dichotomy of <em>“Generalist vs. Specialist”</em> was brilliantly resolved by NITI Aayog's <b>Aspirational Districts Programme (ADP)</b> covering India's 112 most backward districts.
            </p>
            <div style="background:rgba(16,185,129,0.1); border-left:5px solid #10b981; padding:1rem 1.25rem; border-radius:10px; margin-bottom:1rem;">
              <strong style="color:#34d399; font-size:1.05rem;">The Collaborative Architecture:</strong>
              <ul style="margin:0.4rem 0 0; padding-left:1.2rem; color:var(--ink); font-size:0.98rem;">
                <li><strong>Generalist District Collectors:</strong> Act as sovereign coordinators, cutting across line departments, mobilizing local machinery, and resolving administrative friction.</li>
                <li><strong>Domain Specialists & Fellows:</strong> Piramal/Tata fellows, data scientists, and health experts embed inside the Collectorate to operate real-time data dashboards (<b>Champions of Change</b>).</li>
              </ul>
            </div>
            <p style="margin:0; font-size:0.92rem; color:var(--mut);">
              <strong>Mains Conclusion Asset:</strong> ADP proves that the solution is not to eliminate generalist collectors, but to empower them with specialist technical cells!
            </p>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="adp-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              What does the Aspirational Districts Programme (ADP) model demonstrate about administrative reform?
            </div>
            <button class="quiz-opt" data-ans="0">Generalists and domain specialists achieve peak outcomes when paired synergistically</button>
            <button class="quiz-opt" data-ans="1">The office of District Collector should be abolished immediately</button>
            <button class="quiz-opt" data-ans="2">Domain specialists should never be allowed inside district administration</button>
            <div class="feedback-banner" id="fb-adp"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#adp-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-adp');
          if (opt.dataset.ans === "0") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Spot on!</strong> ADP proves generalists + domain specialists form a powerhouse synergy.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to Lateral Entry Dilemma (2024 Update) →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Option A captures the core takeaway.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 14: LATERAL ENTRY DILEMMA (2024-2025 UPDATE) ---
    function renderStep14_LateralEntry() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Real-World Examples & Case Studies (3 of 3)
            </span>
            <span class="badge" style="background:#e11d48; color:#fff;">2024-2025 Current Update</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            The Lateral Entry Dilemma (August 2024 UPSC Withdrawal)
          </h2>

          <div style="background:var(--card-sub); border:2px solid rgba(225,29,72,0.3); border-radius:16px; padding:1.4rem; margin-bottom:1.5rem; line-height:1.55;">
            <p style="margin:0 0 1rem; font-size:1.05rem;">
              In August 2024, UPSC advertised 45 lateral entry posts at Joint Secretary, Director, and Deputy Secretary levels across ministries, but the advertisement was swiftly <b>withdrawn</b> following national debate over constitutional reservations (Article 16(4)).
            </p>
            <div style="background:rgba(225,29,72,0.1); border-left:5px solid #e11d48; padding:1rem 1.25rem; border-radius:10px; margin-bottom:1rem;">
              <strong style="color:#fb7185; font-size:1.05rem;">Crucial Mains Analytical Takeaway:</strong>
              <p style="margin:0.4rem 0 0; color:var(--ink); font-size:1.02rem;">
                While the state urgently requires outside domain expertise in specialized fields, lateral entry cannot bypass social justice. The solution is an <b>institutionalized, transparent, UPSC-led permanent framework</b> with clear reservation rosters, not ad-hoc contractual hiring.
              </p>
            </div>
            <p style="margin:0; font-size:0.92rem; color:var(--mut);">
              <strong>Examiner-Impression Tip:</strong> Mentioning the August 2024 withdrawal demonstrates that your answer is thoroughly updated with the latest constitutional realities.
            </p>
          </div>

          <!-- Micro Quiz -->
          <div class="quiz-card" id="lateral-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">INSTANT RETRIEVAL QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              What was the core constitutional issue that prompted the withdrawal of the August 2024 lateral entry advertisement?
            </div>
            <button class="quiz-opt" data-ans="0">Lack of office space in Central Secretariat</button>
            <button class="quiz-opt" data-ans="1">Concerns regarding constitutional reservation compliance (Article 16(4))</button>
            <button class="quiz-opt" data-ans="2">Lateral candidates failing basic English typing tests</button>
            <div class="feedback-banner" id="fb-lateral"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Continue →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#lateral-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-lateral');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Accurate!</strong> The withdrawal was prompted by concerns regarding social justice and reservation compliance.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-amber");
            btn.textContent = "Continue to Way Forward & Conclusion →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> The constitutional issue centered on reservation quotas.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 15;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 15: WAY FORWARD & CONCLUSION ---
    function renderStep15_WayForward() {
      learnScreenContent.innerHTML = `
        <div style="animation:pop 0.3s ease-out;">
          <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.5rem;">
            <span style="font-weight:800; color:var(--gov-accent); font-size:0.85rem; letter-spacing:0.05em; text-transform:uppercase;">
              Way Forward & Mains Conclusion
            </span>
            <span class="badge badge-success">High-Scoring Template</span>
          </div>
          <h2 style="font-size:1.6rem; font-weight:800; margin:0 0 0.8rem; color:var(--ink);">
            4-Pillar Way Forward & The “Bamboo Frame” Conclusion
          </h2>

          <div style="display:grid; grid-template-columns:repeat(auto-fit, minmax(260px, 1fr)); gap:1rem; margin-bottom:1.5rem;">
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:var(--gov-accent); font-size:1.02rem;">1. Role-Based HR (Mission Karmayogi):</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Implement <b>FRAC (Framework of Roles, Activities, and Competencies)</b> to assign postings based on proven skills rather than seniority alone.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#60a5fa; font-size:1.02rem;">2. "Generalist-Plus" Specialization:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Retain unified generalist entry and district field immersion for the first <b>10–12 years</b>, followed by mandatory assignment into 2–3 core domain tracks.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#34d399; font-size:1.02rem;">3. Institutionalized Lateral Entry:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Establish a permanent, transparent UPSC-led framework that harmonizes specialist induction with constitutional reservation mandates.
              </p>
            </div>
            <div style="background:var(--card-sub); border:1.5px solid var(--line); border-radius:12px; padding:1rem;">
              <strong style="color:#fb7185; font-size:1.02rem;">4. De-layering the Secretariat:</strong>
              <p style="font-size:0.88rem; color:var(--mut); margin:0.3rem 0 0; line-height:1.4;">
                Expand the <b>Desk Officer System</b> to collapse 6–8 file-noting tiers into a maximum of 3 decision levels.
              </p>
            </div>
          </div>

          <!-- Ready to Use Conclusion -->
          <div style="background:linear-gradient(135deg, rgba(37,99,235,0.18), rgba(16,185,129,0.18)); border:2px solid rgba(37,99,235,0.4); border-radius:16px; padding:1.4rem 1.6rem; margin-bottom:1.5rem;">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); text-transform:uppercase; margin-bottom:0.4rem;">
              Ready-to-Use Concluding Punchline:
            </div>
            <blockquote style="margin:0; font-size:1.15rem; font-weight:700; line-height:1.5; color:var(--ink); font-style:italic;">
              “Contemporary governance does not require choosing between the generalist and the specialist in a zero-sum binary; rather, it demands evolving from a colonial 'Steel Frame' into a collaborative <b>'Bamboo Frame'</b>—flexible, specialized at the apex, yet deeply rooted in grassroots realities—to achieve Viksit Bharat by 2047.”
            </blockquote>
          </div>

          <!-- Final Micro Quiz -->
          <div class="quiz-card" id="wf-box">
            <div style="font-size:0.82rem; font-weight:800; color:var(--gov-accent); margin-bottom:0.3rem;">FINAL MASTERY SYNTHESIS QUIZ</div>
            <div style="font-size:1.02rem; font-weight:700; color:var(--ink); margin-bottom:0.6rem;">
              What does evolving from a "Steel Frame" to a "Bamboo Frame" symbolize in Indian administrative reforms?
            </div>
            <button class="quiz-opt" data-ans="0">Replacing all civil servants with private contractors</button>
            <button class="quiz-opt" data-ans="1">A flexible administration specialized at the apex yet deeply anchored in grassroots field reality</button>
            <button class="quiz-opt" data-ans="2">Abolishing competitive entrance examinations</button>
            <div class="feedback-banner" id="fb-wf"></div>
          </div>

          <div style="text-align:right;">
            <button class="btn-3d" id="btn-next-step" disabled style="opacity:0.6;">
              Answer Quiz to Complete Chapter →
            </button>
          </div>
        </div>
      `;

      document.querySelectorAll('#wf-box .quiz-opt').forEach(opt => {
        opt.onclick = () => {
          const fb = document.getElementById('fb-wf');
          if (opt.dataset.ans === "1") {
            opt.classList.add('correct');
            fb.className = "feedback-banner correct";
            fb.innerHTML = "<strong>Flawless!</strong> The Bamboo Frame metaphor captures flexibility, specialized apex leadership, and grassroots resilience.";
            const btn = document.getElementById("btn-next-step");
            btn.disabled = false;
            btn.style.opacity = "1";
            btn.classList.add("btn-3d-emerald");
            btn.textContent = "🏆 Claim Chapter 1 Mastery Certificate →";
          } else {
            opt.classList.add('incorrect');
            fb.className = "feedback-banner incorrect";
            fb.innerHTML = "<strong>Incorrect.</strong> Bamboo Frame represents flexibility, domain expertise, and grassroots anchoring.";
          }
        };
      });

      document.getElementById("btn-next-step").onclick = () => {
        userXp += 50;
        currentStep++;
        renderStep();
      };
    }

    // --- STEP 16: CELEBRATION & COMPLETION SCREEN ---
    function renderStep16_Celebration() {
      triggerConfetti();

      learnScreenContent.innerHTML = `
        <div class="celebrate-card" style="animation:pop 0.4s ease-out;">
          <div class="celebrate-icon">🏆</div>
          <span style="font-size:0.85rem; font-weight:800; background:rgba(16,185,129,0.2); color:#34d399; padding:4px 14px; border-radius:999px;">
            CLUSTER 1 MASTERED
          </span>
          <h1 style="font-size:2.2rem; font-weight:800; margin:0.6rem 0 0.3rem; color:var(--ink);">
            Congratulations! You've Nailed Cluster 1
          </h1>
          <p style="color:var(--mut); font-size:1.05rem; margin:0 auto 1.5rem; max-width:650px; line-height:1.5;">
            You have mastered the complete thematic blueprint covering <strong>2016 (Q14)</strong>, <strong>2026 (Q8)</strong>, Macaulay legacy, Weberian hierarchy, Fulton "cult of the amateur", 1st ARC, Surinder Nath, 2nd ARC, technocrat titans, and the Bamboo Frame conclusion!
          </p>

          <div style="display:flex; justify-content:center; gap:1.25rem; margin-bottom:2rem; flex-wrap:wrap;">
            <div style="background:var(--card-sub); border:2px solid var(--line); border-radius:14px; padding:1rem 1.5rem; min-width:140px;">
              <div style="font-size:1.8rem; font-weight:800; color:var(--gov-accent);">+${userXp} XP</div>
              <div style="font-size:0.82rem; color:var(--mut); font-weight:700;">Knowledge Earned</div>
            </div>
            <div style="background:var(--card-sub); border:2px solid var(--line); border-radius:14px; padding:1rem 1.5rem; min-width:140px;">
              <div style="font-size:1.8rem; font-weight:800; color:#34d399;">100%</div>
              <div style="font-size:0.82rem; color:var(--mut); font-weight:700;">Cluster Retention</div>
            </div>
            <div style="background:var(--card-sub); border:2px solid var(--line); border-radius:14px; padding:1rem 1.5rem; min-width:140px;">
              <div style="font-size:1.8rem; font-weight:800; color:#60a5fa;">2 PYQs</div>
              <div style="font-size:0.82rem; color:var(--mut); font-weight:700;">Full Answers Skeletons</div>
            </div>
          </div>

          <div style="display:flex; justify-content:center; gap:1rem; flex-wrap:wrap;">
            <button class="btn-3d btn-3d-amber" id="btn-back-to-themes" style="font-size:1rem; padding:0.75rem 1.5rem;">
              🏛️ Return to Governance Hub
            </button>
            <button class="btn-3d btn-3d-secondary" id="btn-restart-cluster" style="font-size:1rem; padding:0.75rem 1.5rem;">
              🔄 Review Cluster from Start
            </button>
          </div>
        </div>
      `;

      document.getElementById("btn-back-to-themes").onclick = () => {
        learnModule.style.display = "none";
        themeDetailsArea.style.display = "block";
        document.getElementById("gov-main-header").style.display = "block";
        window.scrollTo({ top: 0, behavior: 'smooth' });
      };

      document.getElementById("btn-restart-cluster").onclick = () => {
        startClusterLearning();
      };
    }

    // --- SIMPLE CANVAS CONFETTI ---
    function triggerConfetti() {
      const canvas = document.getElementById("confetti-canvas");
      const ctx = canvas.getContext("2d");
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;

      const particles = [];
      const colors = ["#2563eb", "#f59e0b", "#10b981", "#7c3aed", "#e11d48", "#38bdf8"];

      for (let i = 0; i < 90; i++) {
        particles.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height - canvas.height,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          vx: Math.random() * 4 - 2,
          vy: Math.random() * 4 + 3,
          rot: Math.random() * 360,
          dRot: Math.random() * 6 - 3
        });
      }

      let frames = 0;
      function renderConfetti() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        particles.forEach(p => {
          p.x += p.vx;
          p.y += p.vy;
          p.rot += p.dRot;
          ctx.save();
          ctx.translate(p.x, p.y);
          ctx.rotate((p.rot * Math.PI) / 180);
          ctx.fillStyle = p.color;
          ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
          ctx.restore();
        });

        frames++;
        if (frames < 180) {
          requestAnimationFrame(renderConfetti);
        } else {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
        }
      }
      renderConfetti();
    }

    // --- INITIALIZE ON PAGE LOAD ---
    renderThemeTabs();
  </script>
</body>
</html>
"""

def main():
    target_path = os.path.join(os.path.dirname(__file__), "governance.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(PAGE_CONTENT)
    print(f"Successfully generated governance.html (Size: {len(PAGE_CONTENT)} bytes)")

if __name__ == "__main__":
    main()

