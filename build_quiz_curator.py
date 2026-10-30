# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

from prepare_mecca_q import mecca_questions
from prepare_freebies_q import freebies_questions

all_questions = mecca_questions + freebies_questions
print(f"Total questions compiled: {len(all_questions)}")

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
<title>UPSC CAVA Quiz Curator · 100 Questions</title>
<style>
:root {
  --bg: #0f172a;
  --card: #1e293b;
  --card-sub: #334155;
  --line: #475569;
  --ink: #f8fafc;
  --mut: #94a3b8;
  --acc: #38bdf8;
  --selb: #3b82f6;
  --ok: #10b981;
  --okbg: rgba(16, 185, 129, 0.15);
  --okb: #059669;
  --no: #ef4444;
  --nobg: rgba(239, 68, 68, 0.15);
  --nob: #dc2626;
  --purple: #a855f7;
  --amber: #f59e0b;
}

* { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  background: var(--bg);
  color: var(--ink);
  line-height: 1.5;
  padding-bottom: 80px;
}

/* Sticky Top Bar */
.top-bar {
  position: sticky;
  top: 0;
  z-index: 100;
  background: rgba(15, 23, 42, 0.95);
  backdrop-filter: blur(12px);
  border-bottom: 1.5px solid var(--line);
  padding: 12px 20px;
}

.top-row {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 12px;
}

.brand {
  display: flex;
  align-items: center;
  gap: 8px;
}
.brand h1 {
  font-size: 18px;
  font-weight: 800;
  color: #fff;
  letter-spacing: -0.02em;
}
.brand span {
  background: var(--selb);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  padding: 2px 8px;
  border-radius: 99px;
  text-transform: uppercase;
}

.stats-bar {
  display: flex;
  align-items: center;
  gap: 12px;
  background: var(--card);
  padding: 6px 14px;
  border-radius: 99px;
  border: 1px solid var(--line);
  font-size: 13px;
  font-weight: 700;
}
.stat-pill { display: flex; align-items: center; gap: 4px; }
.stat-pill.picked { color: var(--ok); }
.stat-pill.rejected { color: var(--no); }
.stat-pill.pending { color: var(--mut); }

.actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.btn {
  background: var(--card-sub);
  color: #fff;
  border: 1px solid var(--line);
  padding: 7px 14px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.15s ease;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}
.btn:hover { background: var(--line); }
.btn-primary {
  background: var(--selb);
  border-color: #2563eb;
}
.btn-primary:hover { background: #2563eb; }
.btn-success {
  background: var(--ok);
  border-color: var(--okb);
}
.btn-success:hover { background: var(--okb); }
.btn-danger {
  background: rgba(239, 68, 68, 0.2);
  color: var(--no);
  border-color: rgba(239, 68, 68, 0.4);
}
.btn-danger:hover { background: var(--no); color: #fff; }

/* Filter Bar */
.filter-row {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-top: 10px;
  overflow-x: auto;
  padding-bottom: 2px;
}
.filter-pill {
  background: var(--card);
  border: 1px solid var(--line);
  color: var(--mut);
  padding: 4px 12px;
  border-radius: 99px;
  font-size: 12px;
  font-weight: 700;
  cursor: pointer;
  white-space: nowrap;
}
.filter-pill:hover { color: var(--ink); border-color: var(--mut); }
.filter-pill.active {
  background: var(--selb);
  color: #fff;
  border-color: var(--selb);
}

/* Main Container */
.container {
  max-width: 900px;
  margin: 20px auto;
  padding: 0 16px;
  display: flex;
  flex-direction: column;
  gap: 20px;
}

/* Question Card */
.q-card {
  background: var(--card);
  border: 2px solid var(--line);
  border-radius: 16px;
  padding: 20px;
  transition: all 0.2s ease;
  position: relative;
}
.q-card.status-picked {
  border-color: var(--ok);
  background: rgba(16, 185, 129, 0.05);
  box-shadow: 0 0 0 1px var(--ok);
}
.q-card.status-rejected {
  border-color: rgba(239, 68, 68, 0.4);
  opacity: 0.55;
  background: rgba(239, 68, 68, 0.03);
}

.card-top {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 12px;
}
.card-left {
  display: flex;
  align-items: center;
  gap: 8px;
  flex-wrap: wrap;
}
.q-num {
  font-size: 14px;
  font-weight: 800;
  color: var(--mut);
}
.topic-tag {
  font-size: 11.5px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 6px;
  text-transform: uppercase;
  letter-spacing: 0.03em;
}
.topic-mecca { background: rgba(59, 130, 246, 0.15); color: #60a5fa; border: 1px solid rgba(59, 130, 246, 0.3); }
.topic-freebie { background: rgba(16, 185, 129, 0.15); color: #34d399; border: 1px solid rgba(16, 185, 129, 0.3); }

.kind-tag {
  font-size: 11.5px;
  font-weight: 800;
  padding: 3px 9px;
  border-radius: 6px;
  background: var(--card-sub);
  color: var(--ink);
  border: 1px solid var(--line);
}

.badge-status {
  font-size: 12px;
  font-weight: 800;
  padding: 3px 10px;
  border-radius: 99px;
  display: none;
}
.q-card.status-picked .badge-status.picked { display: inline-block; background: var(--okbg); color: var(--ok); border: 1px solid var(--ok); }
.q-card.status-rejected .badge-status.rejected { display: inline-block; background: var(--nobg); color: var(--no); border: 1px solid var(--no); }

.q-text {
  font-size: 16px;
  font-weight: 700;
  line-height: 1.45;
  margin-bottom: 14px;
  color: #fff;
}

/* Interactive Preview Components */
.interactive-box {
  background: var(--card-sub);
  border-radius: 10px;
  padding: 12px 14px;
  margin-bottom: 14px;
  font-size: 13.5px;
}
.opt-list { display: flex; flex-direction: column; gap: 6px; }
.opt-item {
  padding: 8px 12px;
  border-radius: 6px;
  background: var(--card);
  border: 1px solid var(--line);
  display: flex;
  align-items: center;
  gap: 8px;
}
.opt-item.correct {
  border-color: var(--ok);
  background: var(--okbg);
  font-weight: 700;
  color: #34d399;
}
.opt-bullet {
  font-size: 12px;
  font-weight: 800;
  color: var(--mut);
}
.opt-item.correct .opt-bullet { color: var(--ok); }

.clue-list { display: flex; flex-direction: column; gap: 6px; }
.clue-item {
  background: var(--card);
  border-left: 3px solid var(--acc);
  padding: 6px 10px;
  border-radius: 4px;
  font-size: 13px;
}

.match-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 8px;
}
.match-pair {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 6px;
  padding: 8px;
  font-size: 12.5px;
}
.match-pair b { color: var(--acc); display: block; margin-bottom: 2px; }

.order-seq {
  display: flex;
  flex-direction: column;
  gap: 5px;
}
.order-step {
  display: flex;
  align-items: center;
  gap: 8px;
  background: var(--card);
  padding: 6px 10px;
  border-radius: 6px;
  font-size: 13px;
}
.order-num {
  width: 22px;
  height: 22px;
  border-radius: 50%;
  background: var(--selb);
  color: #fff;
  font-size: 11px;
  font-weight: 800;
  display: grid;
  place-items: center;
}

.sort-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 8px;
}
.sort-bucket {
  background: var(--card);
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 8px;
}
.sort-title {
  font-size: 11px;
  font-weight: 800;
  text-transform: uppercase;
  color: var(--amber);
  margin-bottom: 4px;
  border-bottom: 1px solid var(--line);
  padding-bottom: 3px;
}
.sort-item { font-size: 12px; margin-bottom: 3px; }

.year-slider-box {
  display: flex;
  align-items: center;
  gap: 12px;
}
.year-badge {
  background: var(--amber);
  color: #000;
  font-size: 16px;
  font-weight: 800;
  padding: 4px 12px;
  border-radius: 6px;
}

.flip-box {
  background: var(--card);
  border: 1.5px dashed var(--purple);
  border-radius: 8px;
  padding: 12px;
  color: #e9d5ff;
  font-size: 13.5px;
  line-height: 1.5;
}
.flip-box em { color: var(--mut); font-size: 11.5px; display: block; margin-bottom: 4px; text-transform: uppercase; font-weight: 800; }

/* Debrief Box */
.debrief-box {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid var(--line);
  border-left: 3px solid var(--selb);
  border-radius: 8px;
  padding: 12px 14px;
  margin-top: 12px;
  font-size: 13px;
  line-height: 1.45;
}
.debrief-rule {
  font-size: 13.5px;
  font-weight: 800;
  color: #60a5fa;
  margin-bottom: 6px;
}
.debrief-expl {
  color: var(--ink);
  margin-bottom: 8px;
}
.debrief-detail {
  display: grid;
  grid-template-columns: 1fr;
  gap: 4px;
  font-size: 12px;
  color: var(--mut);
  border-top: 1px dashed var(--line);
  padding-top: 6px;
}
.debrief-detail span b { color: var(--ink); }

/* Decision Toolbar */
.decision-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  margin-top: 16px;
  padding-top: 12px;
  border-top: 1px solid var(--line);
}
.decision-group {
  display: flex;
  align-items: center;
  gap: 8px;
}
.btn-pick {
  background: var(--okbg);
  border: 1.5px solid var(--ok);
  color: var(--ok);
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}
.btn-pick:hover, .q-card.status-picked .btn-pick {
  background: var(--ok);
  color: #fff;
}

.btn-reject {
  background: var(--nobg);
  border: 1.5px solid var(--no);
  color: var(--no);
  padding: 8px 16px;
  border-radius: 8px;
  font-size: 13px;
  font-weight: 800;
  cursor: pointer;
  transition: all 0.15s ease;
  display: flex;
  align-items: center;
  gap: 6px;
}
.btn-reject:hover, .q-card.status-rejected .btn-reject {
  background: var(--no);
  color: #fff;
}

.modal {
  display: none;
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  z-index: 200;
  align-items: center;
  justify-content: center;
  padding: 20px;
}
.modal.open { display: flex; }
.modal-content {
  background: var(--card);
  border: 1.5px solid var(--line);
  border-radius: 16px;
  max-width: 600px;
  width: 100%;
  max-height: 80vh;
  display: flex;
  flex-direction: column;
  padding: 20px;
}
.modal-content h2 { font-size: 18px; margin-bottom: 12px; }
.modal-content textarea {
  flex: 1;
  min-height: 300px;
  background: var(--bg);
  color: #fff;
  border: 1px solid var(--line);
  border-radius: 8px;
  padding: 12px;
  font-family: monospace;
  font-size: 12px;
  resize: vertical;
  margin-bottom: 12px;
}
.modal-actions {
  display: flex;
  justify-content: flex-end;
  gap: 8px;
}
</style>
</head>
<body>

<div class="top-bar">
  <div class="top-row">
    <div class="brand">
      <h1>UPSC CAVA Quiz Curator</h1>
      <span>100 Pool</span>
    </div>
    <div class="stats-bar">
      <div class="stat-pill picked">✅ <span id="cnt-picked">0</span> Picked</div>
      <div class="stat-pill rejected">❌ <span id="cnt-rejected">0</span> Skipped</div>
      <div class="stat-pill pending">⏳ <span id="cnt-pending">100</span> Pending</div>
    </div>
    <div class="actions">
      <button class="btn btn-success" id="btn-export">📥 Export Picked (JSON)</button>
      <button class="btn btn-primary" id="btn-copy">📋 Copy Summary</button>
      <button class="btn btn-danger" id="btn-reset">Reset</button>
    </div>
  </div>
  <div class="filter-row">
    <button class="filter-pill active" data-filter="all">All Questions (100)</button>
    <button class="filter-pill" data-filter="mecca">🇸🇦 Mecca Pact (50)</button>
    <button class="filter-pill" data-filter="freebie">📜 Freebies & Welfare (50)</button>
    <button class="filter-pill" data-filter="picked">Picked Only</button>
    <button class="filter-pill" data-filter="pending">Pending Only</button>
  </div>
</div>

<div class="container" id="cards-container">
  <!-- Question cards will be dynamically injected here -->
</div>

<!-- Modal for Export -->
<div class="modal" id="export-modal">
  <div class="modal-content">
    <h2 id="modal-title">Export Picked Questions</h2>
    <textarea id="export-text" readonly></textarea>
    <div class="modal-actions">
      <button class="btn" id="modal-copy-btn">Copy to Clipboard</button>
      <button class="btn btn-primary" id="modal-close-btn">Close</button>
    </div>
  </div>
</div>

<script>
var QUESTIONS = %QUESTIONS_JSON%;
var STORAGE_KEY = "cava_quiz_curator_decisions_v1";
var decisions = {};

try {
  var saved = localStorage.getItem(STORAGE_KEY);
  if (saved) decisions = JSON.parse(saved);
} catch(e) {}

var curFilter = "all";

function getTopicKey(topic) {
  return topic.toLowerCase().indexOf("mecca") > -1 ? "mecca" : "freebie";
}

function renderCards() {
  var container = document.getElementById("cards-container");
  var html = "";
  var pickedCount = 0;
  var rejectedCount = 0;

  QUESTIONS.forEach(function(q, idx) {
    var st = decisions[q.id] || "pending";
    if (st === "picked") pickedCount++;
    if (st === "rejected") rejectedCount++;

    var topKey = getTopicKey(q.topic);
    var matchesFilter = true;
    if (curFilter === "mecca" && topKey !== "mecca") matchesFilter = false;
    if (curFilter === "freebie" && topKey !== "freebie") matchesFilter = false;
    if (curFilter === "picked" && st !== "picked") matchesFilter = false;
    if (curFilter === "pending" && st !== "pending") matchesFilter = false;

    if (!matchesFilter) return;

    var previewHtml = "";
    if (q.k === "mc" || q.k === "tf" || q.k === "flag") {
      var opts = (q.k === "tf") ? ["True", "False"] : q.o;
      previewHtml = '<div class="interactive-box"><div class="opt-list">';
      opts.forEach(function(optText, oIdx) {
        var isCorrect = (oIdx === q.a);
        previewHtml += '<div class="opt-item' + (isCorrect ? ' correct' : '') + '">' +
          '<span class="opt-bullet">' + (isCorrect ? '✅' : '○') + '</span>' +
          '<span>' + escapeHtml(optText) + '</span>' +
        '</div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "multi") {
      previewHtml = '<div class="interactive-box"><div class="opt-list">';
      q.o.forEach(function(optText, oIdx) {
        var isCorrect = (q.a.indexOf(oIdx) > -1);
        previewHtml += '<div class="opt-item' + (isCorrect ? ' correct' : '') + '">' +
          '<span class="opt-bullet">' + (isCorrect ? '☑' : '☐') + '</span>' +
          '<span>' + escapeHtml(optText) + '</span>' +
        '</div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "riddle") {
      previewHtml = '<div class="interactive-box"><div class="clue-list">';
      q.c.forEach(function(clue, cIdx) {
        previewHtml += '<div class="clue-item">🔎 <b>Clue ' + (cIdx+1) + ':</b> ' + escapeHtml(clue) + '</div>';
      });
      previewHtml += '</div><div class="opt-list" style="margin-top:8px">';
      q.o.forEach(function(optText, oIdx) {
        var isCorrect = (oIdx === q.a);
        previewHtml += '<div class="opt-item' + (isCorrect ? ' correct' : '') + '">' +
          '<span class="opt-bullet">' + (isCorrect ? '👑' : '○') + '</span>' +
          '<span>' + escapeHtml(optText) + '</span>' +
        '</div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "match") {
      previewHtml = '<div class="interactive-box"><div class="match-grid">';
      q.p.forEach(function(pair) {
        previewHtml += '<div class="match-pair"><b>' + escapeHtml(pair[0]) + '</b><span>' + escapeHtml(pair[1]) + '</span></div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "order") {
      previewHtml = '<div class="interactive-box"><div class="order-seq">';
      q.o.forEach(function(step, sIdx) {
        previewHtml += '<div class="order-step"><span class="order-num">' + (sIdx+1) + '</span><span>' + escapeHtml(step) + '</span></div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "sort") {
      previewHtml = '<div class="interactive-box"><div class="sort-grid">';
      q.b.forEach(function(bucketName, bIdx) {
        previewHtml += '<div class="sort-bucket"><div class="sort-title">📂 ' + escapeHtml(bucketName) + '</div>';
        q.it.forEach(function(item) {
          if (item[1] === bIdx) {
            previewHtml += '<div class="sort-item">✦ ' + escapeHtml(item[0]) + '</div>';
          }
        });
        previewHtml += '</div>';
      });
      previewHtml += '</div></div>';
    } else if (q.k === "year") {
      previewHtml = '<div class="interactive-box"><div class="year-slider-box">' +
        '<span style="font-size:12px;color:var(--mut)">Range: ' + q.min + ' — ' + q.max + '</span>' +
        '<span class="year-badge">🎯 Target Year: ' + q.a + '</span>' +
      '</div></div>';
    } else if (q.k === "flip") {
      previewHtml = '<div class="interactive-box"><div class="flip-box">' +
        '<em>Model Answer / Recall Response:</em>' +
        escapeHtml(q.r).replace(/\\n/g, '<br>') +
      '</div></div>';
    }

    var debriefHtml = '<div class="debrief-box">' +
      '<div class="debrief-rule">🔑 ' + escapeHtml(q.kw || "") + '</div>' +
      '<div class="debrief-expl">' + escapeHtml(q.e || "") + '</div>' +
      '<div class="debrief-detail">' +
        (q.data ? '<span><b>📊 Data:</b> ' + escapeHtml(q.data) + '</span>' : '') +
        (q.ex ? '<span><b>⚡ Case:</b> ' + escapeHtml(q.ex) + '</span>' : '') +
        (q.mains ? '<span><b>🏛️ Mains Hook:</b> ' + escapeHtml(q.mains) + '</span>' : '') +
      '</div>' +
    '</div>';

    html += '<div class="q-card status-' + st + '" id="card-' + q.id + '">' +
      '<div class="card-top">' +
        '<div class="card-left">' +
          '<span class="q-num">#' + (idx+1) + '</span>' +
          '<span class="topic-tag topic-' + topKey + '">' + (topKey === "mecca" ? '🇸🇦 Mecca Pact' : '📜 Freebies') + '</span>' +
          '<span class="kind-tag">' + q.k.toUpperCase() + '</span>' +
        '</div>' +
        '<div>' +
          '<span class="badge-status picked">Picked ✅</span>' +
          '<span class="badge-status rejected">Skipped ❌</span>' +
        '</div>' +
      '</div>' +
      '<div class="q-text">' + escapeHtml(q.q) + '</div>' +
      previewHtml +
      debriefHtml +
      '<div class="decision-bar">' +
        '<div class="decision-group">' +
          '<button class="btn-pick" data-qid="' + q.id + '" data-act="picked">💚 Pick This Question</button>' +
          '<button class="btn-reject" data-qid="' + q.id + '" data-act="rejected">❌ Skip / Reject</button>' +
        '</div>' +
        '<div>' +
          (st !== "pending" ? '<button class="btn" style="font-size:11px" data-qid="' + q.id + '" data-act="pending">Clear</button>' : '') +
        '</div>' +
      '</div>' +
    '</div>';
  });

  container.innerHTML = html;

  // Update counts
  document.getElementById("cnt-picked").textContent = pickedCount;
  document.getElementById("cnt-rejected").textContent = rejectedCount;
  document.getElementById("cnt-pending").textContent = (QUESTIONS.length - pickedCount - rejectedCount);
}

function setDecision(qId, status) {
  if (status === "pending") {
    delete decisions[qId];
  } else {
    decisions[qId] = status;
  }
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(decisions));
  } catch(e) {}
  renderCards();
}

function escapeHtml(str) {
  if (!str) return "";
  return str.toString()
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

// Event Delegation for Decision Buttons
document.getElementById("cards-container").addEventListener("click", function(e) {
  var btn = e.target.closest("button[data-act]");
  if (btn) {
    var act = btn.getAttribute("data-act");
    var qId = btn.getAttribute("data-qid");
    setDecision(qId, act);
  }
});

// Filter Buttons
document.querySelectorAll(".filter-pill").forEach(function(pill) {
  pill.onclick = function() {
    document.querySelectorAll(".filter-pill").forEach(function(p) { p.classList.remove("active"); });
    pill.classList.add("active");
    curFilter = pill.getAttribute("data-filter");
    renderCards();
  };
});

// Export Modal
var exportModal = document.getElementById("export-modal");
var exportText = document.getElementById("export-text");

document.getElementById("btn-export").onclick = function() {
  var pickedList = QUESTIONS.filter(function(q) { return decisions[q.id] === "picked"; });
  if (pickedList.length === 0) {
    alert("You haven't picked any questions yet! Tap '💚 Pick This Question' on questions you like.");
    return;
  }
  document.getElementById("modal-title").textContent = "Exporting " + pickedList.length + " Picked Questions (JSON)";
  exportText.value = JSON.stringify(pickedList, null, 2);
  exportModal.classList.add("open");
};

document.getElementById("btn-copy").onclick = function() {
  var pickedList = QUESTIONS.filter(function(q) { return decisions[q.id] === "picked"; });
  if (pickedList.length === 0) {
    alert("No questions picked yet!");
    return;
  }
  var summary = "SELECTED QUESTIONS (" + pickedList.length + " Total):\\n\\n";
  pickedList.forEach(function(q, i) {
    summary += (i+1) + ". [" + q.topic + "] (" + q.k.toUpperCase() + ") " + q.q + "\\n";
    summary += "   Key: " + q.kw + "\\n\\n";
  });
  navigator.clipboard.writeText(summary).then(function() {
    alert("Copied summary of " + pickedList.length + " picked questions to clipboard!");
  }).catch(function() {
    exportText.value = summary;
    exportModal.classList.add("open");
  });
};

document.getElementById("btn-reset").onclick = function() {
  if (confirm("Reset all selections? This will clear your picked and skipped tags.")) {
    decisions = {};
    try { localStorage.removeItem(STORAGE_KEY); } catch(e) {}
    renderCards();
  }
};

document.getElementById("modal-copy-btn").onclick = function() {
  exportText.select();
  document.execCommand("copy");
  alert("Copied to clipboard!");
};

document.getElementById("modal-close-btn").onclick = function() {
  exportModal.classList.remove("open");
};
exportModal.onclick = function(e) {
  if (e.target === exportModal) exportModal.classList.remove("open");
};

// Initialize
renderCards();
</script>
</body>
</html>
"""

questions_json_str = json.dumps(all_questions, ensure_ascii=False)
final_html = HTML_TEMPLATE.replace("%QUESTIONS_JSON%", questions_json_str)

output_path = r"d:\Anki_Upgraded\quiz_curator.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print(f"Generated quiz_curator.html at {output_path} ({len(final_html)} bytes)")
