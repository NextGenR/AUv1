# -*- coding: utf-8 -*-
"""
Updater script to inject the Governance Hub (5 Themes) and Theme 2 Cluster 1 Interactive Flow
directly into generate_cava_app.py, then rebuild mobile/index.html.
"""

import re
import sys

def main():
    with open("generate_cava_app.py", "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Add extra CSS for Governance mobile cards and drills
    css_insert = """
/* Governance Mobile Master Styles */
.gov-box{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:14px;margin-bottom:12px}
.gov-pyq-box{background:var(--card-sub);border:2px dashed var(--selb);border-radius:14px;padding:12px 14px;margin-bottom:12px}
.gov-demand{background:rgba(245,158,11,0.08);border:2px solid rgba(245,158,11,0.35);border-radius:14px;padding:12px 14px;margin-bottom:12px;font-size:14.5px;line-height:1.4}
.gov-demand b{background:var(--hl-bg);color:var(--ink)}
.gov-quote{background:var(--card-sub);border:2px solid var(--line);border-left:5px solid var(--selb);border-radius:14px;padding:12px 14px;margin-bottom:12px;font-size:15px;line-height:1.4}
.gov-triad-card{background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:10px}
.gov-tag{display:inline-block;font-size:11px;font-weight:800;text-transform:uppercase;padding:2px 7px;border-radius:6px;margin-bottom:4px}
.gov-tag.struct{background:rgba(37,99,235,0.18);color:#60a5fa}
.gov-tag.cult{background:rgba(245,158,11,0.18);color:#fbbf24}
.gov-tag.imp{background:rgba(239,68,68,0.18);color:#f87171}
.flag-seg{display:inline-block;padding:4px 8px;margin:3px 2px;border-radius:8px;border:1.5px solid var(--line);background:var(--card);cursor:pointer;font-weight:700;font-size:14px}
.flag-seg.ok{border-color:var(--ok);background:var(--okbg);color:var(--ok)}
.flag-seg.bad{border-color:var(--no);background:var(--nobg);color:var(--no)}
.gov-sort-box{background:var(--card-sub);border:2px dashed var(--line);border-radius:14px;padding:12px;text-align:center;min-height:55px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14.5px;margin-bottom:10px}
.gov-fb{display:none;border-radius:12px;padding:10px 12px;margin-top:10px;font-size:13.5px;line-height:1.35}
.gov-fb.ok{display:block;background:var(--okbg);border:1.5px solid var(--ok);color:var(--ok)}
.gov-fb.no{display:block;background:var(--nobg);border:1.5px solid var(--no);color:var(--no)}
"""

    if ".gov-box{" not in content:
        content = content.replace("</style></head><body><div id=\"app\"></div>", css_insert + "\n</style></head><body><div id=\"app\"></div>")

    # 2. Update SYLLABUS.gs2.domains.governance with the 5 Official Themes
    old_gov_regex = r"governance:\s*\{\s*name:\s*[\"']Governance[\"'],\s*ico:\s*[\"'](?:⚖️|🏛️)[\"'],\s*themes:\s*\[[\s\S]*?\]\s*\}"
    new_gov_block = """governance: {
        name: "Governance",
        ico: "🏛️",
        themes: [
          { id: "gov_theme_1", title: "1. Transparency, Accountability & E-Gov", years: "2018, 2023", desc: "Important aspects of governance, transparency and accountability, e-governance applications, models, citizens charters & institutional measures.", topic: "charter" },
          { id: "gov_theme_2", title: "2. Role of Civil Services in a Democracy 🎯", years: "2016, 2017, 2020, 2024, 2026", desc: "Colonial legacy, generalist vs specialist, democratic ethos, institutional quality & reforms (3 Core Clusters Mapped)", isTheme2: true },
          { id: "gov_theme_3", title: "3. Development Processes & Industry (NGOs/SHGs)", years: "2015, 2021, 2023", desc: "Role of NGOs, SHGs, various groups and associations, donors, charities, institutional and other stakeholders.", isTheme3: true },
          { id: "gov_theme_4", title: "4. Government Policies & Interventions", years: "2017, 2019, 2024", desc: "Government policies and interventions for development in various sectors and issues arising out of their design and implementation.", isTheme4: true },
          { id: "gov_theme_5", title: "5. Pressure Groups & Quasi-Judicial Bodies", years: "2016, 2019, 2023", desc: "Pressure groups and formal/informal associations and their role in the Polity (or statutory, regulatory & quasi-judicial bodies).", isTheme5: true }
        ]
      }"""

    content = re.sub(old_gov_regex, new_gov_block, content, count=1)

    # 3. Add Theme 2 Modal & Interactive Flow JavaScript functions (using curly apostrophes ’)
    gov_js_block = """
function showTheme2Modal(){
  var m = document.createElement('div');
  m.className = 'modal-overlay';
  var h = '<div class="modal-sheet" style="max-height:85vh;overflow-y:auto">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
      '<span class="theme-tag" style="background:#2563eb;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:800">Theme 2 · 5 PYQs Clustered</span>' +
      '<button class="x" id="modal-x" style="font-size:22px">×</button>' +
    '</div>' +
    '<h2 style="font-size:20px;margin:4px 0 6px">Role of Civil Services in a Democracy</h2>' +
    '<p style="font-size:13.5px;color:var(--mut);margin:0 0 12px">These 5 PYQs are clubbed into 3 core thematic clusters covering Structure, Ethos & Institutional Quality:</p>' +
    
    '<!-- Cluster 1 -->' +
    '<div style="background:rgba(37,99,235,0.08);border:2px solid #2563eb;border-radius:14px;padding:12px;margin-bottom:10px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">' +
        '<b style="color:var(--ink);font-size:15px">Cluster 1: Structure & Colonial Legacy</b>' +
        '<span style="background:var(--okbg);color:var(--ok);font-size:11px;font-weight:800;padding:2px 6px;border-radius:4px">Ready</span>' +
      '</div>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin-bottom:4px">Target PYQs: 2016 (Q14) & 2026 (Q8)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0 0 10px;line-height:1.35">Weberian hierarchy, silos, 3Cs fear, red-tapism vs development; Northcote-Trevelyan generalist premise vs modern knowledge economy.</p>' +
      '<button class="btn" id="btn-play-cluster1" style="background:#2563eb;border-color:#1d4ed8;color:#fff;font-size:15px;padding:8px">🚀 Learn this Chapter →</button>' +
    '</div>' +

    '<!-- Cluster 2 -->' +
    '<div style="background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:10px">' +
      '<b style="color:var(--ink);font-size:14.5px">Cluster 2: Democratic Ethos & Public Trust</b>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin:2px 0 4px">Target PYQs: 2017 (Part A) & 2024 (Q8)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0;line-height:1.35">Neutrality, anonymity, committed bureaucracy, Hota Committee & Sevottam model.</p>' +
    '</div>' +

    '<!-- Cluster 3 -->' +
    '<div style="background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:14px">' +
      '<b style="color:var(--ink);font-size:14.5px">Cluster 3: Institutional Quality & Reforms</b>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin:2px 0 4px">Target PYQs: 2017 (Part B) & 2020 (Q7)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0;line-height:1.35">Mission Karmayogi (FRAC), 360-degree APAR, Baswan & Surinder Nath recommendations.</p>' +
    '</div>' +

    '<button class="btn" id="modal-close-btn" style="background:var(--line);color:var(--ink);border-color:var(--mut);font-size:15px;padding:8px">Close</button>' +
  '</div>';

  m.innerHTML = h;
  document.body.appendChild(m);
  var cb = document.getElementById('modal-close-btn'), cx = document.getElementById('modal-x'), cp = document.getElementById('btn-play-cluster1');
  if (cb) cb.onclick = function(){ m.remove(); };
  if (cx) cx.onclick = function(){ m.remove(); };
  if (cp) cp.onclick = function(){ m.remove(); startGovCluster1(); };
  m.onclick = function(e){ if (e.target === m) m.remove(); };
}

var GSTEP = 0;
var GTOTAL = 17;
var GXP = 0;

function startGovCluster1(){
  GSTEP = 0;
  GXP = 0;
  drawGovScreen();
}

function drawGovScreen(){
  var pct = Math.round((GSTEP / (GTOTAL - 1)) * 100);
  var headHtml = '<div class="qhead">' +
    '<button class="x" id="gov-quit" aria-label="Quit">✕</button>' +
    '<div class="bar"><i style="width:' + pct + '%;background:linear-gradient(90deg,#2563eb,#10b981)"></i></div>' +
    '<span style="font-size:12.5px;font-weight:800;color:var(--accd);white-space:nowrap">' + (GSTEP+1) + '/' + GTOTAL + '</span>' +
  '</div>';

  var bodyHtml = '';
  var footHtml = '';

  if (GSTEP === 0) {
    // PYQ 1
    bodyHtml = '<div class="body">' +
      '<p class="kind">TARGET PYQ 1 OF 2 · 2016 (Q14)</p>' +
      '<div class="gov-pyq-box">' +
        '<small style="font-weight:800;color:var(--selb)">UPSC MAINS 2016 | 12.5M | 200 WORDS</small>' +
        '<p style="font-size:18px;font-weight:800;margin:6px 0 0;line-height:1.3;color:var(--ink)">“Traditional bureaucratic structure and culture have hampered the process of socio-economic development in India.” Comment.</p>' +
      '</div>' +
      '<div class="gov-demand">' +
        '<b style="color:var(--accd)">🎯 Demand of the Question:</b>' +
        '<p style="margin:6px 0 0">1. Split into <b>Structural</b> (steep Weberian pyramid, 6-8 file noting layers, ministerial silos, centralized command) vs <b>Cultural</b> bottlenecks (red-tape, “Mai-Baap” paternalism, 3Cs fear).<br>2. Explicitly link to <b>Socio-Economic Development</b> (capex lapse, project delays, local body starvation).<br>3. Provide balanced comment & structural remedies.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to PYQ 2 →</button></div>';
  } else if (GSTEP === 1) {
    // PYQ 2
    bodyHtml = '<div class="body">' +
      '<p class="kind">TARGET PYQ 2 OF 2 · 2026 (Q8)</p>' +
      '<div class="gov-pyq-box">' +
        '<small style="font-weight:800;color:var(--selb)">UPSC MAINS 2026 | 10M | 150 WORDS</small>' +
        '<p style="font-size:18px;font-weight:800;margin:6px 0 0;line-height:1.3;color:var(--ink)">“Analyse the advantages and limitations of the generalist structure of the Indian Civil Services in contemporary governance.”</p>' +
      '</div>' +
      '<div class="gov-demand">' +
        '<b style="color:var(--accd)">🎯 Demand of the Question:</b>' +
        '<p style="margin:6px 0 0">1. Unpack Northcote-Trevelyan all-rounder generalist model.<br>2. <b>Advantages:</b> Grassroots SDM/DM reality, holistic integration without tunnel vision, crisis leadership, federal glue.<br>3. <b>Limitations:</b> Domain asymmetry in AI, semiconductor, WTO; 18-month amnesia; demoralizing technical services.<br>4. <b>Way Forward:</b> Mid-career specialization & lateral entry.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to Thematic Clubbing →</button></div>';
  } else if (GSTEP === 2) {
    // Clubbing
    bodyHtml = '<div class="body">' +
      '<p class="kind">THEMATIC SYNTHESIS</p>' +
      '<p class="q">Why These 2 PYQs Club Together</p>' +
      '<div class="gov-box">' +
        '<p style="margin:0 0 10px;font-size:15px">Both questions test the identical core administrative tension:</p>' +
        '<div style="background:rgba(37,99,235,0.12);padding:10px;border-radius:12px;font-weight:700;font-size:14.5px;color:var(--ink);margin-bottom:10px">' +
          'A 19th-Century Colonial Regulatory Apparatus (Steel Frame)<br>' +
          '<span style="color:#60a5fa">VERSUS</span><br>' +
          'A 21st-Century Dynamic Knowledge Economy & Welfare State.' +
        '</div>' +
        '<p style="margin:0;font-size:13.5px;color:var(--mut)">Mastering this cluster gives you plug-and-play intro hooks, structural-cultural matrices, Fulton & ARC citations, and the Bamboo Frame conclusion.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Start Learning: Introductions →</button></div>';
  } else if (GSTEP === 3) {
    // Hist Intro
    bodyHtml = '<div class="body">' +
      '<p class="kind">READY-TO-USE INTRO (PART 1 OF 2)</p>' +
      '<p class="q">1. Historical / Evolution Angle</p>' +
      '<div class="gov-quote">' +
        '“Rooted in the <b>Macaulay Committee (1854)</b> and Weberian legal-rational model, Indian bureaucracy was originally designed as a regulatory <b>“Steel Frame”</b> for law-and-order maintenance and revenue extraction, rather than as a dynamic instrument of post-independence socio-economic transformation.”' +
      '</div>' +
      '<div class="gov-box">' +
        '<b>🏛️ Macaulay Committee (1854):</b> Elite merit exam for colonial order.<br><br>' +
        '<b>⚖️ Weberian Rationalism:</b> Steep hierarchy & impersonal rules.<br><br>' +
        '<b>💰 Extractive DNA:</b> Revenue siphoning repurposed for socialist welfare.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to Contemporary Intro →</button></div>';
  } else if (GSTEP === 4) {
    // Contemp Intro
    bodyHtml = '<div class="body">' +
      '<p class="kind">READY-TO-USE INTRO (PART 2 OF 2)</p>' +
      '<p class="q">2. Contemporary / Generalist Angle</p>' +
      '<div class="gov-quote" style="border-left-color:var(--acc)">' +
        '“As India transitions from a basic welfare regulator to a complex knowledge economy managing <b>AI regulation</b>, <b>semiconductor supply chains</b>, and <b>climate finance</b>, the 19th-century <b>Northcote-Trevelyan model of the “all-rounder generalist”</b> faces a severe structural stress test.”' +
      '</div>' +
      '<div class="gov-box">' +
        '<b>📜 Northcote-Trevelyan (1854):</b> Liberal arts generalists managing any ministry.<br><br>' +
        '<b>🔬 Modern Frontiers:</b> High-tech governance requires deep domain mastery.<br><br>' +
        '<b>⚡ Stress Test:</b> 18-month rotations create dependency on Big Four consultants.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Proceed to Dimension A →</button></div>';
  } else if (GSTEP === 5) {
    // Dimension A
    bodyHtml = '<div class="body">' +
      '<p class="kind">DIMENSION A (2016 CORE)</p>' +
      '<p class="q">Structure, Culture & Impact Triads</p>' +
      
      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Rigid Weberian Hierarchy</b>: 6-8 file noting layers.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>Rule over Outcome</b>: Red-Tapism procedural obsession.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Delayed Projects</b>: Cost overruns & capex lapsing.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Departmental Silos</b>: Fragmented ministries.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>Turf Consciousness</b>: Refusal to share data.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Policy Incoherence</b>: Water split across 4 ministries.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Centralized Command</b>: Secretariat monopoly.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>“Mai-Baap” Paternalism</b>: Citizens as charity cases.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Local Disempowerment</b>: Starving Panchayats of 3Fs.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>No Inaction Penalty</b>: APAR ignores omission.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>3Cs Fear (CBI, CVC, CAG)</b>: Defensive status-quoism.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Policy Paralysis</b>: Bold PPP & innovation stifled.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Proceed to Dimension B →</button></div>';
  } else if (GSTEP === 6) {
    // Dimension B
    bodyHtml = '<div class="body">' +
      '<p class="kind">DIMENSION B (2026 CORE)</p>' +
      '<p class="q">Generalist Advantages vs Limitations</p>' +

      '<div class="gov-box" style="border-color:rgba(16,185,129,0.4)">' +
        '<b style="color:var(--ok);font-size:16px">🛡️ 5 Enduring Advantages:</b>' +
        '<ol style="margin:8px 0 0;padding-left:18px;font-size:13.5px;line-height:1.45">' +
          '<li><b>Grassroots Exposure:</b> SDM/DM reality grounds policy.</li>' +
          '<li><b>Holistic Integration:</b> Cures narrow specialist “tunnel vision”.</li>' +
          '<li><b>Crisis Agility:</b> Rapid multi-agency command in disasters.</li>' +
          '<li><b>Federal Glue:</b> Sardar Patel’s All-India Services unity.</li>' +
          '<li><b>Political Buffer:</b> Translates technical jargon for Ministers.</li>' +
        '</ol>' +
      '</div>' +

      '<div class="gov-box" style="border-color:rgba(239,68,68,0.4)">' +
        '<b style="color:var(--no);font-size:16px">⚠️ 4 Modern Limitations:</b>' +
        '<ol style="margin:8px 0 0;padding-left:18px;font-size:13.5px;line-height:1.45">' +
          '<li><b>Domain Asymmetry:</b> Out of depth in AI, WTO, carbon markets.</li>' +
          '<li><b>Rotational Amnesia:</b> 18-month musical chairs destroy memory.</li>' +
          '<li><b>Specialist Demotivation:</b> IRS, scientists blocked from top posts.</li>' +
          '<li><b>Flawed Drafting:</b> Faulty tenders & retrospective tax controversies.</li>' +
        '</ol>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Start Practice Quizzes →</button></div>';
  } else if (GSTEP === 7) {
    // Detailed Practice Quizzes
    bodyHtml = '<div class="body">' +
      '<p class="kind">CHECKPOINT DRILL</p>' +
      '<p class="q">Lock-in Macaulay, Triads & Keyterms</p>' +

      '<!-- Q1 -->' +
      '<div class="gov-box" id="dq1">' +
        '<b>1. Macaulay Committee (1854) primary intent?</b>' +
        '<button class="opt" data-q="1" data-a="0" style="margin-top:8px">Grassroots social empowerment</button>' +
        '<button class="opt" data-q="1" data-a="1">Colonial regulatory Steel Frame for revenue & order</button>' +
        '<div class="gov-fb" id="dfb1"></div>' +
      '</div>' +

      '<!-- Q2 -->' +
      '<div class="gov-box" id="dq2">' +
        '<b>2. Tap the Red Flag:</b><br>' +
        '<div style="margin:8px 0">' +
          '<span class="flag-seg" data-s="0">Bureaucratic fear of 3Cs comprises</span> ' +
          '<span class="flag-seg" data-s="1">the CBI, the CVC,</span> ' +
          '<span class="flag-seg" data-s="2">and NITI Aayog.</span>' +
        '</div>' +
        '<div class="gov-fb" id="dfb2"></div>' +
      '</div>' +

      '<!-- Q3 -->' +
      '<div class="gov-box" id="dq3">' +
        '<b>3. Sort “Mai-Baap Paternalism”:</b>' +
        '<div class="gov-sort-box">Treating citizens as passive charity recipients</div>' +
        '<div class="two">' +
          '<button class="opt" data-s="struct">Structural</button>' +
          '<button class="opt" data-s="cult">Cultural</button>' +
        '</div>' +
        '<div class="gov-fb" id="dfb3"></div>' +
      '</div>' +

      '<!-- Q4 -->' +
      '<div class="gov-box" id="dq4">' +
        '<b>4. Sort “Preventing Specialist Tunnel Vision”:</b>' +
        '<div class="two" style="margin-top:8px">' +
          '<button class="opt" data-g="adv">Generalist Advantage</button>' +
          '<button class="opt" data-g="lim">Generalist Limitation</button>' +
        '</div>' +
        '<div class="gov-fb" id="dfb4"></div>' +
      '</div>' +

      '<!-- Q5 -->' +
      '<div class="gov-box" id="dq5">' +
        '<b>5. Inaction caused by fear of audits is termed:</b>' +
        '<button class="opt" data-q="5" data-a="1" style="margin-top:8px">Policy Paralysis</button>' +
        '<button class="opt" data-q="5" data-a="0">Domain Specialization</button>' +
        '<div class="gov-fb" id="dfb5"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Complete Drills to Proceed →</button></div>';
  } else if (GSTEP === 8) {
    // Value Addition 1 - Fulton
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 1 OF 4 · GLOBAL PRECEDENT</p>' +
      '<p class="q">Fulton Committee (UK, 1968)</p>' +
      '<div class="gov-quote">' +
        'The Fulton Committee famously diagnosed that the civil service was crippled by the <b>“Cult of the Amateur”</b>—the flawed assumption that men trained in general arts could manage modern industrial and technological governance.' +
      '</div>' +
      '<div class="gov-box" id="mq8">' +
        '<b>Which phrase was coined by Fulton Committee?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">“Cult of the Amateur”</button>' +
        '<button class="opt" data-a="0">“Steel Frame”</button>' +
        '<div class="gov-fb" id="mfb8"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 9) {
    // Value Addition 2 - 1st ARC
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 2 OF 4 · 1966 ROADMAP</p>' +
      '<p class="q">1st ARC (1966) — 8 Functional Areas</p>' +
      '<div class="gov-quote">' +
        'The First ARC recommended classifying civil service posts into <b>8 functional areas</b> (Economic, Social, Agriculture, Financial, etc.) for mid-career domain specialization.' +
      '</div>' +
      '<div class="gov-box" id="mq9">' +
        '<b>How many functional areas did 1st ARC recommend?</b>' +
        '<button class="opt" data-a="0" style="margin-top:8px">3 macro cadres</button>' +
        '<button class="opt" data-a="1">8 functional areas</button>' +
        '<div class="gov-fb" id="mfb9"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 10) {
    // Value Addition 3 - Surinder Nath
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 3 OF 4 · DOMAIN MAPPING</p>' +
      '<p class="q">Surinder Nath Committee (2003)</p>' +
      '<div class="gov-quote">' +
        'Recommended assigning officers to <b>11 specific domain clusters</b> based on proven aptitude and field performance to eliminate erratic rotational transfers.' +
      '</div>' +
      '<div class="gov-box" id="mq10">' +
        '<b>Surinder Nath Committee proposed how many domain clusters?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">11 domain clusters</button>' +
        '<button class="opt" data-a="0">28 state cadres</button>' +
        '<div class="gov-fb" id="mfb10"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 11) {
    // Value Addition 4 - 2nd ARC
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 4 OF 4 · MASTER REPORTS</p>' +
      '<p class="q">2nd ARC 10th & 13th Reports</p>' +
      '<div class="gov-quote">' +
        '<b>10th Report:</b> Mandatory domain specialization after <b>13 years</b> of service + open senior competition.<br><br>' +
        '<b>13th Report:</b> Replace steep pyramids with <b>flatter, mission-mode</b> executive structures.' +
      '</div>' +
      '<div class="gov-box" id="mq11">' +
        '<b>Mandatory specialization year per 2nd ARC 10th Report?</b>' +
        '<button class="opt" data-a="0" style="margin-top:8px">3 years (probation)</button>' +
        '<button class="opt" data-a="1">13 years of service</button>' +
        '<div class="gov-fb" id="mfb11"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 12) {
    // Examples - Titans
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (1 OF 3)</p>' +
      '<p class="q">Technocrat Titans in Governance</p>' +
      '<div class="gov-box">' +
        '🥛 <b>Dr. Verghese Kurien:</b> Operation Flood (AMUL)<br>' +
        '🌾 <b>Dr. M.S. Swaminathan:</b> Green Revolution<br>' +
        '🚇 <b>E. Sreedharan:</b> Konkan Railway & Delhi Metro<br>' +
        '🆔 <b>Nandan Nilekani:</b> UIDAI (Aadhaar)<br>' +
        '🚽 <b>Parameswaran Iyer:</b> Swachh Bharat Mission (Grameen)' +
      '</div>' +
      '<div class="gov-box" id="mq12">' +
        '<b>Who led UIDAI to build Aadhaar identity infrastructure?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Nandan Nilekani</button>' +
        '<button class="opt" data-a="0">E. Sreedharan</button>' +
        '<div class="gov-fb" id="mfb12"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 13) {
    // Examples - ADP
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (2 OF 3)</p>' +
      '<p class="q">Generalist-Specialist Synergy: ADP</p>' +
      '<div class="gov-quote">' +
        'NITI Aayog’s <b>Aspirational Districts Programme (ADP)</b> proved the golden mean: Generalist District Collectors coordinate field delivery, empowered by domain fellows and real-time data dashboards (<b>Champions of Change</b>).' +
      '</div>' +
      '<div class="gov-box" id="mq13">' +
        '<b>The ADP model proves that:</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Generalists + Specialists achieve peak synergy together</button>' +
        '<button class="opt" data-a="0">District Collectors should be replaced entirely</button>' +
        '<div class="gov-fb" id="mfb13"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 14) {
    // Lateral Entry 2024 Nuance
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (3 OF 3)</p>' +
      '<p class="q">Lateral Entry Dilemma (2024 Update)</p>' +
      '<div class="gov-quote" style="border-left-color:var(--no)">' +
        'August 2024 UPSC withdrawal of 45 lateral posts highlights that technical induction cannot bypass constitutional social justice (<b>Article 16(4)</b>). India needs an <b>institutionalized UPSC framework</b> with clear reservation rosters, not ad-hoc hiring.' +
      '</div>' +
      '<div class="gov-box" id="mq14">' +
        '<b>Reason for the August 2024 UPSC lateral withdrawal?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Constitutional reservation compliance concerns</button>' +
        '<button class="opt" data-a="0">Shortage of government desks</button>' +
        '<div class="gov-fb" id="mfb14"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 15) {
    // Way Forward & Conclusion
    bodyHtml = '<div class="body">' +
      '<p class="kind">WAY FORWARD & CONCLUSION</p>' +
      '<p class="q">Steel Frame to Bamboo Frame</p>' +
      '<div class="gov-box">' +
        '🎯 <b>Role-Based HR:</b> Mission Karmayogi (FRAC competencies).<br><br>' +
        '🌟 <b>Generalist-Plus:</b> 10-12 yrs district exposure, then domain specialization.<br><br>' +
        '⚖️ <b>Permanent Lateral Framework:</b> UPSC-led with reservation compliance.<br><br>' +
        '✂️ <b>Desk Officer De-layering:</b> Max 3 decision tiers.' +
      '</div>' +
      '<div class="gov-quote" style="border-left-color:var(--ok)">' +
        '“Contemporary governance demands evolving from a colonial “Steel Frame” into a collaborative <b>“Bamboo Frame”</b>—flexible, specialized at the apex, yet deeply rooted in grassroots realities—to achieve Viksit Bharat by 2047.”' +
      '</div>' +
      '<div class="gov-box" id="mq15">' +
        '<b>The “Bamboo Frame” signifies:</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Flexibility & apex specialization rooted in grassroots field reality</button>' +
        '<button class="opt" data-a="0">Complete privatization of civil services</button>' +
        '<div class="gov-fb" id="mfb15"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Final Quiz →</button></div>';
  } else if (GSTEP === 16) {
    // Celebration
    confetti();
    addXp(180);
    bodyHtml = '<div class="body" style="text-align:center;padding-top:20px">' +
      '<div style="font-size:64px;line-height:1">🏆</div>' +
      '<h1 style="font-size:24px;margin:10px 0 6px">Cluster 1 Mastered!</h1>' +
      '<p style="color:var(--mut);font-size:14px;margin:0 0 16px">You conquered both 2016 (Q14) & 2026 (Q8), Macaulay, Fulton, 1st & 2nd ARC, and the Bamboo Frame synthesis.</p>' +
      '<div class="two" style="margin-bottom:16px">' +
        '<div class="stat">+180 XP<small>Knowledge Earned</small></div>' +
        '<div class="stat" style="color:var(--ok)">100%<small>Retention Rate</small></div>' +
      '</div>' +
      '<button class="btn" id="gov-finish" style="background:#2563eb;color:#fff;border-color:#1d4ed8">Return to Governance Themes</button>' +
    '</div>';
    footHtml = '';
  }

  app.innerHTML = headHtml + bodyHtml + footHtml;

  var qb = document.getElementById('gov-quit');
  if (qb) qb.onclick = function(){ home(); };

  var nb = document.getElementById('gov-next');
  if (nb && GSTEP < 7) {
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  // Interactive Handlers for Step 7 (Checkpoint)
  if (GSTEP === 7) {
    var p7 = { q1: false, q2: false, q3: false, q4: false, q5: false };
    function chk7(){
      if (p7.q1 && p7.q2 && p7.q3 && p7.q4 && p7.q5) {
        nb.disabled = false;
        nb.style.opacity = '1';
        nb.style.background = 'var(--ok)';
        nb.textContent = 'All Passed! Continue to Value Additions →';
        beep(true);
      }
    }
    app.querySelectorAll('#dq1 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb1');
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Correct! Extractive & law-and-order steel frame.';
          p7.q1 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Incorrect. It was designed for imperial order.';
        }
        chk7();
      };
    });
    app.querySelectorAll('.flag-seg').forEach(function(s){
      s.onclick = function(){
        var fb = document.getElementById('dfb2');
        if (s.dataset.s === '2') {
          s.className = 'flag-seg bad'; fb.className = 'gov-fb ok';
          fb.textContent = 'Red Flag Spotted! 3Cs are CBI, CVC, and CAG, not NITI Aayog!';
          p7.q2 = true;
        } else {
          s.className = 'flag-seg ok'; fb.className = 'gov-fb no';
          fb.textContent = 'That segment is true. Spot which agency is wrong.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq3 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb3');
        if (b.dataset.s === 'cult') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Spot on! Mindset/cultural bottleneck.';
          p7.q3 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Paternalism is an entrenched mindset/culture.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq4 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb4');
        if (b.dataset.g === 'adv') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Exactly! Core generalist advantage.';
          p7.q4 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Preventing tunnel vision is an advantage.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq5 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb5');
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Correct! Policy Paralysis from 3Cs fear.';
          p7.q5 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Inaction from audit fear is Policy Paralysis.';
        }
        chk7();
      };
    });
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  // Micro Quizzes Handlers for Steps 8-15
  if (GSTEP >= 8 && GSTEP <= 15) {
    var boxId = '#mq' + GSTEP;
    var fbId = 'mfb' + GSTEP;
    app.querySelectorAll(boxId + ' .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById(fbId);
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Spot on! Nailed it.';
          nb.disabled = false;
          nb.style.opacity = '1';
          nb.style.background = 'var(--acc)';
          nb.textContent = 'Continue →';
          beep(true);
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Not quite, look at the concept card above.';
          beep(false);
        }
      };
    });
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  if (GSTEP === 16) {
    var fb = document.getElementById('gov-finish');
    if (fb) fb.onclick = function(){ home(); };
  }
}
"""

    # Clean previous injection if any and insert
    clean_pos = content.find("function showTheme2Modal()")
    if clean_pos != -1:
        end_clean = content.find("function showThemeSheet(themeId){", clean_pos)
        content = content[:clean_pos] + content[end_clean:]

    content = content.replace("function showThemeSheet(themeId){", gov_js_block + "\nfunction showThemeSheet(themeId){")
    print("Injected showTheme2Modal & startGovCluster1 with curly apostrophes.")

    # 4. In home() theme-item click handler: add check for gov_theme_2
    old_theme_click = """    item.onclick = function(){
      var topId = item.dataset.top;
      var thId = item.dataset.th;
      if (topId && DATA[topId]) {
        CUR_TOPIC = topId;
        home();
      } else {
        showThemeSheet(thId);
      }
    };"""

    new_theme_click = """    item.onclick = function(){
      var topId = item.dataset.top;
      var thId = item.dataset.th;
      if (thId === 'gov_theme_2' || thId === 'cs_structure') {
        showTheme2Modal();
      } else if (topId && DATA[topId]) {
        CUR_TOPIC = topId;
        home();
      } else {
        showThemeSheet(thId);
      }
    };"""

    if old_theme_click in content:
        content = content.replace(old_theme_click, new_theme_click)
        print("Updated theme-item click handler to trigger showTheme2Modal.")

    # 5. In home() quick topic pills: add 🏛️ Governance pill
    old_topics_code = """  Object.keys(DATA).forEach(function(k){
    var t = DATA[k];
    topicsHtml += '<button class="topic-btn' + (k === CUR_TOPIC ? ' active' : '') + '" data-t="' + k + '">' + t.badge + ' ' + esc(t.title.split('&')[0].trim()) + '</button>';
  });"""

    new_topics_code = """  topicsHtml += '<button class="topic-btn' + (S.domain === 'governance' ? ' active' : '') + '" id="pill-gov">🏛️ Governance (5 Themes)</button>';
  Object.keys(DATA).forEach(function(k){
    var t = DATA[k];
    topicsHtml += '<button class="topic-btn' + (k === CUR_TOPIC && S.domain !== 'governance' ? ' active' : '') + '" data-t="' + k + '">' + t.badge + ' ' + esc(t.title.split('&')[0].trim()) + '</button>';
  });"""

    if "pill-gov" not in content:
        content = content.replace(old_topics_code, new_topics_code)
        print("Added quick Governance topic pill.")

    # In home() click handlers: attach click to pill-gov
    old_pill_attach = """  app.querySelectorAll('.topic-btn').forEach(function(b){"""
    new_pill_attach = """  var pGov = document.getElementById('pill-gov');
  if (pGov) pGov.onclick = function(){ S.paper = 'gs2'; S.domain = 'governance'; save(); home(); };
  app.querySelectorAll('.topic-btn').forEach(function(b){"""

    if "pill-gov" in content and "pGov.onclick" not in content:
        content = content.replace(old_pill_attach, new_pill_attach)
        print("Attached click handler to pill-gov.")

    with open("generate_cava_app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated generate_cava_app.py.")

if __name__ == "__main__":
    main()
