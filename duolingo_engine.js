/**
 * CORTEX DUOLINGO ENGINE - GAMIFIED UPSC LEVEL-WISE LEARNING
 * Sound FX, Visual Winding Path, Hearts/Lives, XP, Tap-to-Order & Match Pairs
 */

function getActiveDuoData() {
  if (typeof window !== 'undefined' && window.ACTIVE_DUO_DATA) return window.ACTIVE_DUO_DATA;
  const isMsme = typeof window !== 'undefined' && (
    window.location.pathname.includes('msme') || 
    window.location.search.includes('msme') || 
    window.location.href.includes('msme')
  );
  if (isMsme && typeof MSME_DATA !== 'undefined') return MSME_DATA;
  if (typeof PUBLIC_EXAM_DATA !== 'undefined') return PUBLIC_EXAM_DATA;
  if (typeof MSME_DATA !== 'undefined') return MSME_DATA;
  return null;
}

class DuoState {
  static getStorageKey() {
    const data = getActiveDuoData();
    return data && data.id ? `cortex_duo_progress_${data.id}` : 'cortex_duo_progress';
  }

  static getProgress() {
    const key = DuoState.getStorageKey();
    const raw = localStorage.getItem(key);
    const data = getActiveDuoData();
    const defaultLvl = (data && data.levels && data.levels[0]) ? data.levels[0].id : "lvl-1";
    let state = null;
    try {
      state = raw ? JSON.parse(raw) : null;
    } catch(e) {
      state = null;
    }
    return {
      xp: (state && state.xp) || 60,
      hearts: 'unlimited', // Unlimited tries - no heart lockout
      completedLevels: (state && state.completedLevels) || [defaultLvl],
      levelStars: (state && state.levelStars) || { [defaultLvl]: 3 },
      streak: (state && state.streak) || 18
    };
  }

  static saveProgress(state) {
    const key = DuoState.getStorageKey();
    state.hearts = 'unlimited';
    localStorage.setItem(key, JSON.stringify(state));
    DuoState.updateHeaderUI();
  }

  static completeLevel(levelId, xpReward, stars = 3) {
    const state = DuoState.getProgress();
    if (!state.completedLevels.includes(levelId)) {
      state.completedLevels.push(levelId);
    }
    state.levelStars = state.levelStars || {};
    state.levelStars[levelId] = Math.max(state.levelStars[levelId] || 0, stars);
    state.xp += xpReward;
    DuoState.saveProgress(state);
  }

  static deductHeart() {
    // Unlimited tries! No penalty or depletion
    return 'unlimited';
  }

  static refillHearts() {
    const state = DuoState.getProgress();
    state.hearts = 'unlimited';
    DuoState.saveProgress(state);
  }

  static updateHeaderUI() {
    const state = DuoState.getProgress();
    const xpEl = document.getElementById('duo-xp-count');
    const heartsEl = document.getElementById('duo-hearts-count');
    const streakEl = document.getElementById('duo-streak-count');
    const lessonHeartsEl = document.getElementById('lesson-hearts-display');

    if (xpEl) xpEl.textContent = state.xp;
    if (heartsEl) heartsEl.innerHTML = '&#8734; Unlimited';
    if (streakEl) streakEl.textContent = state.streak;
    if (lessonHeartsEl) lessonHeartsEl.innerHTML = '&#8734; Unlimited';
  }
}

/* ==========================================================================
   FEEDBACK & LESSON STARS DATA SYSTEM (LOCAL PERSISTENCE & REPORT GENERATOR)
   ========================================================================== */
const CORTEX_FEEDBACK = {
  getQuestionsKey() {
    return 'cortex_question_feedback';
  },

  getCourseKey(topicId) {
    return `cortex_course_feedback_${topicId || 'general'}`;
  },

  getAllQuestionFeedback() {
    try {
      return JSON.parse(localStorage.getItem(this.getQuestionsKey()) || '[]');
    } catch(e) {
      return [];
    }
  },

  saveQuestionFeedback(item) {
    try {
      const list = this.getAllQuestionFeedback();
      const existingIdx = list.findIndex(x => x.id === item.id);
      if (existingIdx >= 0) {
        list[existingIdx] = { ...list[existingIdx], ...item, updatedAt: new Date().toISOString() };
      } else {
        list.push({ ...item, createdAt: new Date().toISOString() });
      }
      localStorage.setItem(this.getQuestionsKey(), JSON.stringify(list));
      return true;
    } catch(e) {
      console.error('Failed to save question feedback', e);
      return false;
    }
  },

  saveCourseFeedback(topicId, rating, comment) {
    try {
      const data = {
        topic: topicId,
        rating: rating,
        comment: comment,
        savedAt: new Date().toISOString()
      };
      localStorage.setItem(this.getCourseKey(topicId), JSON.stringify(data));
      return true;
    } catch(e) {
      return false;
    }
  },

  getCourseFeedback(topicId) {
    try {
      return JSON.parse(localStorage.getItem(this.getCourseKey(topicId)) || 'null');
    } catch(e) {
      return null;
    }
  },

  buildMarkdownReport(topicId, duoData, completedLevels, levelStars, courseRating, userComment) {
    const levels = duoData && duoData.levels ? duoData.levels : [];
    const allQFeedback = this.getAllQuestionFeedback().filter(x => !topicId || x.topic === topicId || x.topic === duoData.id);
    
    let md = `# 🎓 UPSC Cortex Academy - Lesson Stars & Feedback Report\n\n`;
    md += `**Topic**: ${duoData.title || topicId || 'UPSC GS Mains / Prelims'}\n`;
    md += `**Generated**: ${new Date().toLocaleDateString()} ${new Date().toLocaleTimeString()}\n`;
    md += `**Overall Course Rating**: ${'⭐'.repeat(courseRating || 5)} (${courseRating || 5}/5)\n\n`;

    md += `### 🌟 Lesson-Wise Stars Summary\n`;
    md += `| Level | Lesson Title | Stars Earned | Status | Question Notes |\n`;
    md += `| :---: | :--- | :---: | :---: | :---: |\n`;

    let totalStars = 0;
    levels.forEach(lvl => {
      const isDone = completedLevels.includes(lvl.id) || completedLevels.includes(lvl.levelNumber);
      const starsCount = (levelStars && (levelStars[lvl.id] || levelStars[lvl.levelNumber])) || (isDone ? 3 : 0);
      totalStars += starsCount;
      const starsStr = starsCount > 0 ? '⭐'.repeat(starsCount) : '—';
      const statusStr = isDone ? '✓ Completed' : '🔒 In Progress';
      const qNotesCount = allQFeedback.filter(q => q.levelId === lvl.id || q.levelNumber === lvl.levelNumber).length;
      const notesBadge = qNotesCount > 0 ? `📝 ${qNotesCount} note${qNotesCount > 1 ? 's' : ''}` : '—';
      md += `| Level ${lvl.levelNumber} | ${lvl.title} | ${starsStr} | ${statusStr} | ${notesBadge} |\n`;
    });
    md += `\n**Total Stars Earned**: ${totalStars} / ${levels.length * 3} ⭐\n\n`;

    if (allQFeedback.length > 0) {
      md += `### 📝 Question-Specific Feedback (${allQFeedback.length} Logged)\n`;
      allQFeedback.forEach((q, i) => {
        const ratingIcon = q.rating === 'Helpful' ? '👍' : q.rating === 'Clear' ? '💡' : q.rating === 'Confusing' ? '🤔' : '⚠️';
        md += `${i + 1}. **[${q.levelTitle || ('Level ' + q.levelNumber)}] Q${(q.taskIndex || 0) + 1}**: ${ratingIcon} *${q.rating}*\n`;
        md += `   - **Prompt**: "${(q.prompt || '').substring(0, 90)}${q.prompt && q.prompt.length > 90 ? '...' : ''}"\n`;
        if (q.note) md += `   - **User Note**: "${q.note}"\n`;
      });
      md += `\n`;
    }

    md += `### 💬 Overall User Feedback & Suggestions for AI\n`;
    md += `> ${userComment && userComment.trim() ? userComment.trim().replace(/\n/g, '\n> ') : 'No additional text comments provided.'}\n\n`;
    md += `---\n*Generated by Cortex Academy Gamified Engine (Unlimited Tries & Feedback System)*\n`;

    return md;
  }
};

function copyReportToClipboard(text, triggerBtn) {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(text).then(() => {
      showCopyToast(triggerBtn);
    }).catch(() => {
      fallbackCopy(text, triggerBtn);
    });
  } else {
    fallbackCopy(text, triggerBtn);
  }
}

function fallbackCopy(text, triggerBtn) {
  const ta = document.createElement('textarea');
  ta.value = text;
  ta.style.position = 'fixed';
  ta.style.opacity = '0';
  document.body.appendChild(ta);
  ta.select();
  try {
    document.execCommand('copy');
    showCopyToast(triggerBtn);
  } catch(e) {
    alert('Copy failed, please select and copy manually.');
  }
  document.body.removeChild(ta);
}

function showCopyToast(triggerBtn) {
  if (triggerBtn) {
    const orig = triggerBtn.innerHTML;
    triggerBtn.innerHTML = '✓ Copied to Clipboard!';
    triggerBtn.style.background = '#10b981';
    triggerBtn.style.borderColor = '#059669';
    setTimeout(() => {
      triggerBtn.innerHTML = orig;
      triggerBtn.style.background = '';
      triggerBtn.style.borderColor = '';
    }, 2500);
  }
  alert('📋 Feedback report copied to clipboard!\n\nYou can now paste it right into the chat to share your feedback with me.');
}

function downloadFeedbackJson(topicId, duoData, completedLevels, levelStars, courseRating, userComment) {
  const allQ = CORTEX_FEEDBACK.getAllQuestionFeedback().filter(x => !topicId || x.topic === topicId || x.topic === duoData.id);
  const payload = {
    topic: topicId || duoData.id,
    title: duoData.title,
    date: new Date().toISOString(),
    overallRating: courseRating || 5,
    userFeedback: userComment,
    completedLevels: completedLevels,
    levelStars: levelStars,
    questionFeedback: allQ
  };
  const blob = new Blob([JSON.stringify(payload, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `cortex_feedback_${topicId || 'report'}_${Date.now()}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}

// Duolingo Signature Web Audio Sound Synthesizer
class DuoSound {
  static init() {
    try {
      if (!this.ctx) {
        const AudioCtx = window.AudioContext || window.webkitAudioContext;
        if (AudioCtx) this.ctx = new AudioCtx();
      }
    } catch(e) {
      this.ctx = null;
    }
  }

  static playTap() {
    try {
      this.init();
      if (!this.ctx) return;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sine';
      osc.frequency.setValueAtTime(600, this.ctx.currentTime);
      osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.05);
      gain.gain.setValueAtTime(0.08, this.ctx.currentTime);
      gain.gain.linearRampToValueAtTime(0.01, this.ctx.currentTime + 0.05);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start();
      osc.stop(this.ctx.currentTime + 0.05);
    } catch(e) {}
  }

  static playCorrect() {
    try {
      this.init();
      if (!this.ctx) return;
      const t = this.ctx.currentTime;
      // Cheerful ascending arpeggio (C5 -> E5 -> G5 -> C6)
      [523.25, 659.25, 783.99, 1046.50].forEach((freq, i) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, t + i * 0.06);
        gain.gain.setValueAtTime(0.12, t + i * 0.06);
        gain.gain.linearRampToValueAtTime(0.01, t + (i + 1) * 0.06);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t + i * 0.06);
        osc.stop(t + (i + 1) * 0.06);
      });
    } catch(e) {}
  }

  static playWrong() {
    try {
      this.init();
      if (!this.ctx) return;
      const t = this.ctx.currentTime;
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();
      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(180, t);
      osc.frequency.linearRampToValueAtTime(120, t + 0.2);
      gain.gain.setValueAtTime(0.12, t);
      gain.gain.linearRampToValueAtTime(0.01, t + 0.2);
      osc.connect(gain);
      gain.connect(this.ctx.destination);
      osc.start(t);
      osc.stop(t + 0.2);
    } catch(e) {}
  }

  static playFanfare() {
    try {
      this.init();
      if (!this.ctx) return;
      const t = this.ctx.currentTime;
      const notes = [523.25, 659.25, 783.99, 1046.5, 1318.5];
      notes.forEach((freq, idx) => {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq, t + idx * 0.1);
        gain.gain.setValueAtTime(0.15, t + idx * 0.1);
        gain.gain.linearRampToValueAtTime(0.01, t + idx * 0.1 + 0.3);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(t + idx * 0.1);
        osc.stop(t + idx * 0.1 + 0.3);
      });
    } catch(e) {}
  }
}

/* ==========================================================================
   APP INITIALIZATION
   ========================================================================== */
let activeLevel = null;
let currentTaskIndex = 0;
let selectedOption = null;
let matchedPairCount = 0;
let assembledTokens = [];

document.addEventListener('DOMContentLoaded', () => {
  DuoState.updateHeaderUI();
  renderLevelPath();
  setupSheetViewToggle();
  renderForumIASSheet();

  const starsFeedbackBtn = document.getElementById('btn-open-stars-feedback');
  if (starsFeedbackBtn) {
    starsFeedbackBtn.addEventListener('click', () => {
      openStarsFeedbackModal();
    });
  }
});

/* ==========================================================================
   VIEW TOGGLE (DUOLINGO PATH ⟷ FORUMIAS SHEET NOTES)
   ========================================================================== */
function setupSheetViewToggle() {
  const btnPath = document.getElementById('toggle-view-path');
  const btnSheet = document.getElementById('toggle-view-sheet');
  const pathSection = document.getElementById('duo-path-section');
  const sheetSection = document.getElementById('duo-sheet-section');

  if (!btnPath || !btnSheet) return;

  btnPath.addEventListener('click', () => {
    btnPath.classList.add('active');
    btnSheet.classList.remove('active');
    if (pathSection) pathSection.style.display = 'block';
    if (sheetSection) sheetSection.style.display = 'none';
    DuoSound.playTap();
  });

  btnSheet.addEventListener('click', () => {
    btnSheet.classList.add('active');
    btnPath.classList.remove('active');
    if (pathSection) pathSection.style.display = 'none';
    if (sheetSection) sheetSection.style.display = 'block';
    DuoSound.playTap();
  });
}

/* ==========================================================================
   RENDER FORUMIAS CLASSROOM NOTES SHEET (MATCHING PDF FORMAT)
   ========================================================================== */
function renderForumIASSheet() {
  const container = document.getElementById('sheet-notes-target');
  const duoData = getActiveDuoData();
  if (!container || !duoData || !duoData.sheetNotes) return;

  const data = duoData.sheetNotes;
  container.innerHTML = '';

  const sheet = document.createElement('div');
  sheet.className = 'pdf-notes-sheet';

  // 1. Top bar
  sheet.innerHTML = `
    <div class="pdf-sheet-topbar">
      <div><span>Shared Freely By AbxK</span></div>
      <div style="font-weight:700; color:#ef4444;"><span style="background:#ef4444; color:#fff; padding:2px 6px; border-radius:3px; margin-right:4px;">▲</span> Forum<span style="color:#fff;">IAS</span></div>
      <div><span class="code-tag">${data.sheetCode}</span></div>
    </div>

    <div class="pdf-title-container">
      <div class="pdf-title-box">
        <h3>${data.title}</h3>
      </div>
    </div>
    <hr class="pdf-dashed-separator">
  `;

  // 2. Render sections
  data.sections.forEach(sec => {
    if (sec.type === 'PROS_CONS') {
      const grid = document.createElement('div');
      grid.className = 'pdf-pros-cons-grid';

      // Left Column
      const prosCol = document.createElement('div');
      prosCol.className = 'pdf-pros-col';
      prosCol.innerHTML = `<div class="pdf-tag-box">${sec.prosTag}</div>`;
      const prosList = document.createElement('ul');
      prosList.className = 'pdf-bullet-list';
      sec.pros.forEach(b => prosList.appendChild(createDuoBullet(b)));
      prosCol.appendChild(prosList);
      grid.appendChild(prosCol);

      // Right Column
      const consCol = document.createElement('div');
      consCol.className = 'pdf-cons-col';
      consCol.innerHTML = `<div class="pdf-tag-box">${sec.consTag}</div>`;
      const consList = document.createElement('ul');
      consList.className = 'pdf-bullet-list';
      sec.cons.forEach(b => consList.appendChild(createDuoBullet(b)));
      consCol.appendChild(consList);
      grid.appendChild(consCol);

      sheet.appendChild(grid);
      sheet.appendChild(createDuoSeparator());
    } else if (sec.type === 'BOTTOM_GRID') {
      const bottomGrid = document.createElement('div');
      bottomGrid.className = 'pdf-bottom-grid';

      const suggCol = document.createElement('div');
      suggCol.innerHTML = `<div class="pdf-tag-box">${sec.suggestionsTag}</div>`;
      const suggList = document.createElement('ul');
      suggList.className = 'pdf-bullet-list';
      sec.suggestions.forEach(b => suggList.appendChild(createDuoBullet(b)));
      suggCol.appendChild(suggList);
      bottomGrid.appendChild(suggCol);

      const concCol = document.createElement('div');
      concCol.innerHTML = `<div class="pdf-tag-box">${sec.conclusionTag}</div>`;
      const concList = document.createElement('ul');
      concList.className = 'pdf-bullet-list';
      sec.conclusion.forEach(b => concList.appendChild(createDuoBullet(b)));
      concCol.appendChild(concList);
      bottomGrid.appendChild(concCol);

      sheet.appendChild(bottomGrid);
    } else {
      const secDiv = document.createElement('div');
      secDiv.innerHTML = `<div class="pdf-tag-box">${sec.tag}</div>`;
      const list = document.createElement('ul');
      list.className = 'pdf-bullet-list';
      sec.bullets.forEach(b => list.appendChild(createDuoBullet(b)));
      secDiv.appendChild(list);

      sheet.appendChild(secDiv);
      sheet.appendChild(createDuoSeparator());
    }
  });

  // Footer
  const footer = document.createElement('div');
  footer.className = 'pdf-sheet-footer';
  footer.innerHTML = `
    <span>Current Affairs Classes by ForumIAS • Lecture 4</span>
    <span>Page 1 of 1</span>
  `;
  sheet.appendChild(footer);

  container.appendChild(sheet);

  // Click listeners for expandable detail notes
  sheet.querySelectorAll('.pdf-bullet-item.has-detail').forEach(it => {
    it.addEventListener('click', () => it.classList.toggle('expanded'));
  });
}

function createDuoBullet(bullet) {
  const li = document.createElement('li');
  li.className = `pdf-bullet-item ${bullet.detail ? 'has-detail' : ''}`;
  li.innerHTML = `
    <span class="pdf-bullet-arrow">→</span>
    <div class="pdf-bullet-content">
      <div class="pdf-bullet-main">${bullet.text}</div>
      ${bullet.detail ? `<div class="pdf-bullet-detail">${bullet.detail}</div>` : ''}
    </div>
  `;
  return li;
}

function createDuoSeparator() {
  const hr = document.createElement('hr');
  hr.className = 'pdf-dashed-separator';
  return hr;
}

/* ==========================================================================
   RENDER DUOLINGO WINDING PATH / STEPPING STONES
   ========================================================================== */
function renderLevelPath() {
  const container = document.getElementById('duo-path-container');
  if (!container) return;

  const duoData = getActiveDuoData();
  if (!duoData || !duoData.levels) return;

  container.innerHTML = '';
  const progress = DuoState.getProgress();
  let currentUnit = '';

  duoData.levels.forEach((lvl, idx) => {
    // If new unit, render unit header banner
    if (lvl.unit !== currentUnit) {
      currentUnit = lvl.unit;
      const unitBanner = document.createElement('div');
      unitBanner.className = 'duo-unit-banner';
      unitBanner.style.borderLeftColor = lvl.unitColor;
      unitBanner.innerHTML = `
        <div class="unit-meta" style="color:${lvl.unitColor};">${lvl.unit.toUpperCase()}</div>
        <div class="unit-title">${duoData.title || 'Integrity & Structural Reforms'}</div>
      `;
      container.appendChild(unitBanner);
    }

    // Determine status: completed, current, or locked
    const isCompleted = progress.completedLevels.includes(lvl.id);
    const prevCompleted = idx === 0 || progress.completedLevels.includes(duoData.levels[idx - 1].id);
    const isCurrent = !isCompleted && prevCompleted;
    const isLocked = !isCompleted && !isCurrent;

    // Duolingo winding pattern offsets: center -> right -> center -> left -> center
    const offsets = ['offset-center', 'offset-right', 'offset-center', 'offset-left'];
    const offsetClass = offsets[idx % offsets.length];

    const nodeWrap = document.createElement('div');
    nodeWrap.className = `duo-node-wrapper ${offsetClass}`;

    const button = document.createElement('button');
    button.className = `duo-path-node ${isCompleted ? 'completed' : isCurrent ? 'active' : 'locked'}`;
    button.dataset.levelId = lvl.id;
    button.setAttribute('aria-label', `Level ${lvl.levelNumber}: ${lvl.title}`);

    // Crown or Checkmark
    const crownBadge = isCompleted ? '<span class="node-crown">✓</span>' : isCurrent ? '<span class="node-crown">👑</span>' : '<span class="node-crown">🔒</span>';

    button.innerHTML = `
      <div class="node-inner">
        <span class="node-icon">${lvl.badgeIcon}</span>
        ${crownBadge}
      </div>
    `;

    // Tooltip Card below node
    const tooltip = document.createElement('div');
    tooltip.className = 'duo-node-tooltip';
    tooltip.innerHTML = `
      <strong>Level ${lvl.levelNumber}: ${lvl.title}</strong>
      <span>${isCompleted ? '✓ Completed (+20 XP)' : isCurrent ? '▶ Start Lesson (+25 XP)' : '🔒 Locked'}</span>
    `;

    if (!isLocked) {
      button.addEventListener('click', () => {
        DuoSound.playTap();
        startLesson(lvl);
      });
    }

    nodeWrap.appendChild(button);
    nodeWrap.appendChild(tooltip);
    container.appendChild(nodeWrap);
  });
}

/* ==========================================================================
   INTERACTIVE LESSON ARENA & TASK RUNNER
   ========================================================================== */
let sorterAssignments = {};
let clozeAnswers = {};
let activeClozeBlankId = null;

function startLesson(level) {
  activeLevel = level;
  currentTaskIndex = 0;
  selectedOption = null;
  assembledTokens = [];
  matchedPairCount = 0;
  sorterAssignments = {};
  clozeAnswers = {};
  activeClozeBlankId = null;

  const modal = document.getElementById('duo-lesson-modal');
  if (modal) modal.classList.add('active');

  renderCurrentTask();
}

function renderCurrentTask() {
  if (!activeLevel) return;

  const task = activeLevel.tasks[currentTaskIndex];
  if (!task) {
    // Lesson Finished!
    completeLesson();
    return;
  }

  // Update progress bar
  const progressPct = ((currentTaskIndex) / activeLevel.tasks.length) * 100;
  const progressBar = document.getElementById('lesson-progress-fill');
  if (progressBar) progressBar.style.width = `${progressPct}%`;

  // Reset Bottom Action Bar
  const bottomBar = document.getElementById('lesson-bottom-bar');
  const actionBtn = document.getElementById('lesson-action-btn');
  const feedbackMsg = document.getElementById('lesson-feedback-message');
  
  if (bottomBar) bottomBar.className = 'lesson-bottom-bar state-ready';
  if (feedbackMsg) feedbackMsg.innerHTML = '';
  if (actionBtn) {
    actionBtn.textContent = task.type === 'concept' ? 'Continue' : 'Check Answer';
    actionBtn.disabled = task.type === 'concept' ? false : true;
    actionBtn.onclick = handleTaskAction;
  }

  const arena = document.getElementById('lesson-task-arena');
  if (!arena) return;
  arena.innerHTML = '';

  // Render specific task template (Innovative Formats)
  if (task.type === 'concept') {
    renderConceptTask(task, arena, actionBtn);
  } else if (task.type === 'category_sorter') {
    renderCategorySorterTask(task, arena, actionBtn);
  } else if (task.type === 'cloze_chips') {
    renderClozeChipsTask(task, arena, actionBtn);
  } else if (task.type === 'flaw_hunter') {
    renderFlawHunterTask(task, arena, actionBtn);
  } else if (task.type === 'case_judge') {
    renderCaseJudgeTask(task, arena, actionBtn);
  } else if (task.type === 'binary_verdict') {
    renderBinaryVerdictTask(task, arena, actionBtn);
  } else if (task.type === 'match_pairs') {
    renderMatchPairsTask(task, arena, actionBtn);
  } else if (task.type === 'true_false') {
    renderTrueFalseTask(task, arena, actionBtn);
  } else if (task.type === 'mcq') {
    renderMcqTask(task, arena, actionBtn);
  } else if (task.type === 'tap_order') {
    renderTapOrderTask(task, arena, actionBtn);
  }
}

/* --- Task Type 1: Concept Drop --- */
function renderConceptTask(task, arena, actionBtn) {
  const flowchartHtml = task.flowchart ? `
    <div class="duo-flowchart-card" style="margin: 1.25rem 0; border: 1.5px solid rgba(59, 130, 246, 0.35); border-radius: 14px; padding: 0.9rem; background: rgba(15, 23, 42, 0.85); text-align: center;">
      <div style="font-size: 0.78rem; font-weight: 800; color: #38bdf8; text-transform: uppercase; margin-bottom: 0.6rem; display: flex; align-items: center; justify-content: space-between;">
        <span>📊 Visual Flowchart Diagram</span>
        <a href="Filtered_Questions/${task.flowchart}" target="_blank" style="color: #60a5fa; text-decoration: none; font-size: 0.75rem; background: rgba(59,130,246,0.2); padding: 3px 8px; border-radius: 6px;">🔍 Full View ↗</a>
      </div>
      <img src="Filtered_Questions/${task.flowchart}" alt="Flowchart Diagram" style="max-width: 100%; height: auto; max-height: 280px; border-radius: 8px; box-shadow: 0 4px 14px rgba(0,0,0,0.5);" loading="lazy">
    </div>
  ` : '';

  arena.innerHTML = `
    <div class="duo-concept-card">
      <div class="duo-mascot-row">
        <div class="duo-mascot-avatar">🦉</div>
        <div class="duo-speech-bubble">
          <strong>${task.title}</strong>
          <p>${(task.content || '').replace(/\\n/g, '<br>').replace(/\n/g, '<br>')}</p>
        </div>
      </div>
      ${flowchartHtml}
      <div class="duo-takeaway-banner">
        💡 <strong>Key UPSC Takeaway:</strong> ${task.keyTakeaway}
      </div>
    </div>
  `;
  actionBtn.disabled = false;
}

/* --- Task Type 2: Multiple Choice Question --- */
function renderMcqTask(task, arena, actionBtn) {
  selectedOption = null;
  const optionsHtml = task.options.map((opt, i) => `
    <button class="duo-option-btn" data-index="${i}">
      <span class="opt-num">${i + 1}</span>
      <span class="opt-label">${opt}</span>
    </button>
  `).join('');

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-options-grid">${optionsHtml}</div>
  `;

  arena.querySelectorAll('.duo-option-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      DuoSound.playTap();
      arena.querySelectorAll('.duo-option-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedOption = parseInt(btn.dataset.index, 10);
      actionBtn.disabled = false;
    });
  });
}

/* --- Task Type 3: True or False --- */
function renderTrueFalseTask(task, arena, actionBtn) {
  selectedOption = null;
  arena.innerHTML = `
    <div class="duo-question-prompt">
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-tf-grid">
      <button class="duo-tf-btn duo-tf-true" data-val="true">
        <span class="tf-icon">✓</span>
        <span>TRUE</span>
      </button>
      <button class="duo-tf-btn duo-tf-false" data-val="false">
        <span class="tf-icon">✕</span>
        <span>FALSE</span>
      </button>
    </div>
  `;

  arena.querySelectorAll('.duo-tf-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      DuoSound.playTap();
      arena.querySelectorAll('.duo-tf-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedOption = btn.dataset.val === 'true';
      actionBtn.disabled = false;
    });
  });
}

/* --- Task Type 4: Match Pairs --- */
function renderMatchPairsTask(task, arena, actionBtn) {
  matchedPairCount = 0;
  let selectedLeft = null;
  let selectedRight = null;

  // Shuffle right items
  const lefts = task.pairs.map((p, i) => ({ text: p.left, id: i }));
  const rights = [...task.pairs.map((p, i) => ({ text: p.right, id: i }))].sort(() => Math.random() - 0.5);

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <h3>${task.prompt}</h3>
      <p style="font-size:0.85rem; color:var(--text-muted);">Tap a left item, then tap its matching constitutional/policy partner on the right.</p>
    </div>
    <div class="duo-pairs-grid">
      <div class="pairs-col left-col">
        ${lefts.map(l => `<button class="duo-pair-chip" data-side="left" data-id="${l.id}">${l.text}</button>`).join('')}
      </div>
      <div class="pairs-col right-col">
        ${rights.map(r => `<button class="duo-pair-chip" data-side="right" data-id="${r.id}">${r.text}</button>`).join('')}
      </div>
    </div>
  `;

  const chips = arena.querySelectorAll('.duo-pair-chip');
  chips.forEach(chip => {
    chip.addEventListener('click', () => {
      if (chip.classList.contains('matched')) return;
      DuoSound.playTap();

      const side = chip.dataset.side;
      if (side === 'left') {
        chips.forEach(c => c.dataset.side === 'left' && c.classList.remove('selected'));
        chip.classList.add('selected');
        selectedLeft = chip;
      } else {
        chips.forEach(c => c.dataset.side === 'right' && c.classList.remove('selected'));
        chip.classList.add('selected');
        selectedRight = chip;
      }

      // Check match if both selected
      if (selectedLeft && selectedRight) {
        if (selectedLeft.dataset.id === selectedRight.dataset.id) {
          // Correct Match!
          DuoSound.playCorrect();
          selectedLeft.classList.remove('selected');
          selectedRight.classList.remove('selected');
          selectedLeft.classList.add('matched');
          selectedRight.classList.add('matched');
          matchedPairCount++;

          selectedLeft = null;
          selectedRight = null;

          if (matchedPairCount === task.pairs.length) {
            actionBtn.disabled = false;
            actionBtn.textContent = 'Continue';
          }
        } else {
          // Mismatch
          DuoSound.playWrong();
          selectedLeft.classList.add('error');
          selectedRight.classList.add('error');
          setTimeout(() => {
            selectedLeft.classList.remove('selected', 'error');
            selectedRight.classList.remove('selected', 'error');
            selectedLeft = null;
            selectedRight = null;
          }, 350);
        }
      }
    });
  });
}

/* --- Task Type 5: Tap to Order Sentence --- */
function renderTapOrderTask(task, arena, actionBtn) {
  assembledTokens = [];
  const shuffled = [...task.tokens].sort(() => Math.random() - 0.5);

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-rack-container" id="token-rack"></div>
    <div class="duo-token-bank" id="token-bank">
      ${shuffled.map((t, i) => `<button class="duo-token-btn" data-text="${t}" id="tok-${i}">${t}</button>`).join('')}
    </div>
  `;

  const bank = arena.querySelector('#token-bank');
  const rack = arena.querySelector('#token-rack');

  bank.querySelectorAll('.duo-token-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      DuoSound.playTap();
      const text = btn.dataset.text;
      btn.style.visibility = 'hidden';

      // Create token in rack
      const rackToken = document.createElement('button');
      rackToken.className = 'duo-token-btn placed';
      rackToken.textContent = text;
      rackToken.addEventListener('click', () => {
        DuoSound.playTap();
        btn.style.visibility = 'visible';
        rackToken.remove();
        assembledTokens = assembledTokens.filter(t => t !== rackToken);
        actionBtn.disabled = assembledTokens.length === 0;
      });

      rack.appendChild(rackToken);
      assembledTokens.push(rackToken);
      actionBtn.disabled = false;
    });
  });
}

/* --- Task Type: Category Sorter / Concept Bucketing --- */
window.handleCategorySelect = function(btn, event, itemIdx, chosenCat) {
  try {
    if (event && event.stopPropagation) {
      event.stopPropagation();
    }
    DuoSound.playTap();

    if (itemIdx === undefined || itemIdx === null || isNaN(itemIdx)) {
      itemIdx = parseInt(btn.getAttribute('data-item') || (btn.dataset && btn.dataset.item), 10);
    }
    if (!chosenCat) {
      chosenCat = btn.getAttribute('data-cat') || (btn.dataset && btn.dataset.cat);
    }
    sorterAssignments[itemIdx] = chosenCat;

    // Highlight selected button & update card style
    const arena = document.getElementById('lesson-task-arena');
    const card = (arena && arena.querySelector(`#sorter-card-${itemIdx}`)) || btn.closest('.duo-sorter-card');
    if (card) {
      card.querySelectorAll('.duo-cat-btn').forEach(b => b.classList.remove('selected'));
      card.classList.add('classified');
    }
    btn.classList.add('selected');

    // Update buckets
    const tasks = (activeLevel && (activeLevel.tasks || activeLevel.questions)) || [];
    const task = tasks[currentTaskIndex];
    if (task) {
      const categories = task.categories || [];
      const items = task.items || [];

      categories.forEach((cat, cIdx) => {
        const bItems = document.getElementById(`bitems-${cIdx}`);
        const bCount = document.getElementById(`bcount-${cIdx}`);
        const assigned = items.filter((_, i) => sorterAssignments[i] === cat);
        if (bCount) bCount.textContent = assigned.length;
        if (bItems) {
          bItems.innerHTML = assigned.map(it => `
            <div class="duo-placed-item">
              <span>${(it.text.split('|')[0] || it.text).substring(0, 36)}...</span>
              <span style="color:#10b981; font-weight:bold;">✓</span>
            </div>
          `).join('');
        }
      });

      const actionBtn = document.getElementById('lesson-action-btn');
      if (actionBtn && Object.keys(sorterAssignments).length === items.length) {
        actionBtn.disabled = false;
        actionBtn.classList.add('ready-pulse');
      }
    }
  } catch(err) {
    console.error("handleCategorySelect error:", err);
  }
};

function renderCategorySorterTask(task, arena, actionBtn) {
  sorterAssignments = {};
  const categories = task.categories || [];
  const items = task.items || [];

  const bucketsHtml = categories.map((cat, cIdx) => `
    <div class="duo-bucket" data-cat="${cat}" id="bucket-${cIdx}">
      <div class="duo-bucket-title">
        <span>${cat}</span>
        <span class="duo-bucket-count" id="bcount-${cIdx}">0</span>
      </div>
      <div class="duo-bucket-items" id="bitems-${cIdx}"></div>
    </div>
  `).join('');

  const itemsHtml = items.map((it, idx) => `
    <div class="duo-sorter-card" id="sorter-card-${idx}">
      <div class="duo-sorter-card-text">${it.text}</div>
      <div class="duo-cat-buttons">
        ${categories.map(cat => {
          const safeCat = cat.replace(/'/g, "\\'");
          return `<button type="button" class="duo-cat-btn" data-item="${idx}" data-cat="${cat}" onclick="window.handleCategorySelect(this, event, ${idx}, '${safeCat}')">${cat}</button>`;
        }).join('')}
      </div>
    </div>
  `).join('');

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(99,102,241,0.15); border:1px solid rgba(99,102,241,0.3); padding:3px 10px; border-radius:999px; font-size:0.78rem; font-weight:800; color:#818cf8; margin-bottom:0.5rem;">
        <span>📊 CONCEPT BUCKETER</span>
      </div>
      <h3>${task.prompt}</h3>
      <p style="font-size:0.85rem; color:var(--text-muted);">Assign each industrial profile to its correct statutory category:</p>
    </div>
    <div class="duo-sorter-wrap">
      <div class="duo-bucket-grid">${bucketsHtml}</div>
      <div class="duo-sorter-items-pool">${itemsHtml}</div>
    </div>
  `;

  // Attach event listener fallback on arena
  arena.querySelectorAll('.duo-cat-btn').forEach(btn => {
    btn.addEventListener('click', function(e) {
      window.handleCategorySelect(this, e);
    });
  });
}

/* --- Task Type: Cloze Chips / Fill-in-the-Blanks --- */
function renderClozeChipsTask(task, arena, actionBtn) {
  clozeAnswers = {};
  activeClozeBlankId = (task.blanks && task.blanks[0]) ? task.blanks[0].id : 1;

  let templateHtml = task.template || '';
  (task.blanks || []).forEach(b => {
    const slotTag = `{${b.id}}`;
    const slotHtml = `<span class="duo-cloze-slot ${b.id === activeClozeBlankId ? 'active' : ''}" data-blank-id="${b.id}" id="cslot-${b.id}">[ Blank ${b.id} ]</span>`;
    templateHtml = templateHtml.replace(slotTag, slotHtml);
  });

  const shuffledChips = [...(task.chips || [])].sort(() => Math.random() - 0.5);
  const chipsHtml = shuffledChips.map((chip, i) => `
    <button type="button" class="duo-chip-btn" data-chip="${chip}" id="cchip-${i}">${chip}</button>
  `).join('');

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(16,185,129,0.15); border:1px solid rgba(16,185,129,0.3); padding:3px 10px; border-radius:999px; font-size:0.78rem; font-weight:800; color:#34d399; margin-bottom:0.5rem;">
        <span>🧩 CLOZE STATUTORY KEYWORD DROP</span>
      </div>
      <h3>${task.prompt}</h3>
      <p style="font-size:0.85rem; color:var(--text-muted);">Tap a blank, then tap the matching keyword or timeline chip below:</p>
    </div>
    <div class="duo-cloze-wrap">
      <div class="duo-cloze-sentence-box">${templateHtml}</div>
      <div class="duo-cloze-chips-bank">${chipsHtml}</div>
    </div>
  `;

  arena.querySelectorAll('.duo-cloze-slot').forEach(slot => {
    slot.addEventListener('click', () => {
      DuoSound.playTap();
      const bId = parseInt(slot.dataset.blankId, 10);
      if (clozeAnswers[bId]) {
        const val = clozeAnswers[bId];
        delete clozeAnswers[bId];
        slot.textContent = `[ Blank ${bId} ]`;
        slot.classList.remove('filled');
        arena.querySelectorAll('.duo-chip-btn').forEach(btn => {
          if (btn.dataset.chip === val && btn.classList.contains('used')) {
            btn.classList.remove('used');
          }
        });
      }
      activeClozeBlankId = bId;
      arena.querySelectorAll('.duo-cloze-slot').forEach(s => s.classList.remove('active'));
      slot.classList.add('active');
      actionBtn.disabled = Object.keys(clozeAnswers).length !== (task.blanks || []).length;
    });
  });

  arena.querySelectorAll('.duo-chip-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      if (btn.classList.contains('used')) return;
      DuoSound.playTap();
      const chipText = btn.dataset.chip;

      let targetId = activeClozeBlankId;
      if (!targetId || clozeAnswers[targetId]) {
        const nextBlank = (task.blanks || []).find(b => !clozeAnswers[b.id]);
        if (nextBlank) targetId = nextBlank.id;
      }
      if (!targetId) return;

      clozeAnswers[targetId] = chipText;
      btn.classList.add('used');

      const slot = arena.querySelector(`#cslot-${targetId}`);
      if (slot) {
        slot.textContent = chipText;
        slot.classList.remove('active');
        slot.classList.add('filled');
      }

      const nextEmpty = (task.blanks || []).find(b => !clozeAnswers[b.id]);
      if (nextEmpty) {
        activeClozeBlankId = nextEmpty.id;
        const nextSlot = arena.querySelector(`#cslot-${nextEmpty.id}`);
        if (nextSlot) nextSlot.classList.add('active');
      } else {
        activeClozeBlankId = null;
      }

      actionBtn.disabled = Object.keys(clozeAnswers).length !== (task.blanks || []).length;
    });
  });
}

/* --- Task Type: Spot the Impostor / Statutory Flaw Hunter --- */
function renderFlawHunterTask(task, arena, actionBtn) {
  selectedOption = null;
  const cardsHtml = (task.statements || []).map((st, i) => `
    <div class="duo-flaw-card" data-index="${i}">
      <span class="duo-flaw-badge">Statement ${String.fromCharCode(65 + i)}</span>
      <div class="duo-flaw-text">${st.text}</div>
    </div>
  `).join('');

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(239,68,68,0.15); border:1px solid rgba(239,68,68,0.3); padding:3px 10px; border-radius:999px; font-size:0.78rem; font-weight:800; color:#f87171; margin-bottom:0.5rem;">
        <span>🕵️ STATUTORY FLAW HUNTER</span>
      </div>
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-flaw-dossier">${cardsHtml}</div>
  `;

  arena.querySelectorAll('.duo-flaw-card').forEach(card => {
    card.addEventListener('click', () => {
      DuoSound.playTap();
      arena.querySelectorAll('.duo-flaw-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedOption = parseInt(card.dataset.index, 10);
      actionBtn.disabled = false;
    });
  });
}

/* --- Task Type: Case Study Simulation / Mini-Tribunal Judge --- */
function renderCaseJudgeTask(task, arena, actionBtn) {
  selectedOption = null;
  const dossier = task.caseDossier || { title: 'Case Dossier', facts: [] };
  const factsHtml = (dossier.facts || []).map(f => `
    <li class="duo-case-fact-item">
      <span class="duo-case-fact-bullet">§</span>
      <span>${f}</span>
    </li>
  `).join('');

  const optionsHtml = (task.options || []).map((opt, i) => `
    <div class="duo-verdict-card" data-index="${i}">
      <span style="font-size:1.1rem;">⚖️</span>
      <span>${opt.text}</span>
    </div>
  `).join('');

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(245,158,11,0.15); border:1px solid rgba(245,158,11,0.3); padding:3px 10px; border-radius:999px; font-size:0.78rem; font-weight:800; color:#fbbf24; margin-bottom:0.5rem;">
        <span>🏛️ MSEFC ARBITRAL TRIBUNAL</span>
      </div>
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-case-wrap">
      <div class="duo-case-dossier-box">
        <div class="duo-case-header">
          <div class="duo-case-title"><span>📜</span> ${dossier.title}</div>
          <span class="duo-case-tag">Arbitral Record</span>
        </div>
        <ul class="duo-case-facts">${factsHtml}</ul>
      </div>
      <div class="duo-verdict-title">${task.question || 'Determine the Statutory Verdict:'}</div>
      <div class="duo-verdict-grid">${optionsHtml}</div>
    </div>
  `;

  arena.querySelectorAll('.duo-verdict-card').forEach(card => {
    card.addEventListener('click', () => {
      DuoSound.playTap();
      arena.querySelectorAll('.duo-verdict-card').forEach(c => c.classList.remove('selected'));
      card.classList.add('selected');
      selectedOption = parseInt(card.dataset.index, 10);
      actionBtn.disabled = false;
    });
  });
}

/* --- Task Type: Binary Policy Verdict --- */
function renderBinaryVerdictTask(task, arena, actionBtn) {
  selectedOption = null;
  const labels = task.labels || { trueLabel: "VALID / TRUE", falseLabel: "INVALID / FALSE" };

  arena.innerHTML = `
    <div class="duo-question-prompt">
      <div style="display:inline-flex; align-items:center; gap:0.4rem; background:rgba(59,130,246,0.15); border:1px solid rgba(59,130,246,0.3); padding:3px 10px; border-radius:999px; font-size:0.78rem; font-weight:800; color:#60a5fa; margin-bottom:0.5rem;">
        <span>⚖️ STATUTORY POLICY VERDICT</span>
      </div>
      <h3>${task.prompt}</h3>
    </div>
    <div class="duo-binary-wrap">
      <div class="duo-binary-scenario-card">${task.scenario || ''}</div>
      <div style="font-weight:800; font-size:0.95rem; color:#e2e8f0;">${task.verdictQuestion || 'Render your statutory determination:'}</div>
      <div class="duo-binary-btns">
        <button type="button" class="duo-binary-btn btn-true" data-val="true">
          <span style="font-size:1.4rem;">✓</span>
          <span>${labels.trueLabel}</span>
        </button>
        <button type="button" class="duo-binary-btn btn-false" data-val="false">
          <span style="font-size:1.4rem;">✕</span>
          <span>${labels.falseLabel}</span>
        </button>
      </div>
    </div>
  `;

  arena.querySelectorAll('.duo-binary-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      DuoSound.playTap();
      arena.querySelectorAll('.duo-binary-btn').forEach(b => b.classList.remove('selected'));
      btn.classList.add('selected');
      selectedOption = btn.dataset.val === 'true';
      actionBtn.disabled = false;
    });
  });
}

/* ==========================================================================
   TASK EVALUATION & ACTION HANDLER
   ========================================================================== */
function handleTaskAction() {
  const task = activeLevel.tasks[currentTaskIndex];
  const bottomBar = document.getElementById('lesson-bottom-bar');
  const actionBtn = document.getElementById('lesson-action-btn');
  const feedbackMsg = document.getElementById('lesson-feedback-message');

  // If already checked, continue to next task
  if (bottomBar.classList.contains('state-success') || bottomBar.classList.contains('state-error') || task.type === 'concept' || task.type === 'match_pairs') {
    currentTaskIndex++;
    renderCurrentTask();
    return;
  }

  let isCorrect = false;
  let explanation = '';

  if (task.type === 'category_sorter') {
    isCorrect = (task.items || []).every((it, idx) => sorterAssignments[idx] === it.category);
    explanation = task.explanation || 'Review the composite classification thresholds.';
  } else if (task.type === 'cloze_chips') {
    isCorrect = (task.blanks || []).every(b => clozeAnswers[b.id] === b.correct);
    explanation = task.explanation || 'Statutory formula verified.';
  } else if (task.type === 'flaw_hunter') {
    const chosen = (task.statements || [])[selectedOption];
    isCorrect = chosen && chosen.isFlaw === true;
    explanation = chosen ? (chosen.flawReason || task.explanation) : task.explanation;
  } else if (task.type === 'case_judge') {
    const chosen = (task.options || [])[selectedOption];
    isCorrect = chosen && chosen.isVerdict === true;
    explanation = task.explanation;
  } else if (task.type === 'binary_verdict') {
    isCorrect = selectedOption === task.correct;
    explanation = task.explanation;
  } else if (task.type === 'mcq') {
    isCorrect = selectedOption === task.correctIndex;
    explanation = task.explanation;
  } else if (task.type === 'true_false') {
    isCorrect = selectedOption === task.correct;
    explanation = task.explanation;
  } else if (task.type === 'tap_order') {
    const assembledString = assembledTokens.map(t => t.textContent.trim()).join(' ');
    isCorrect = assembledString.toLowerCase() === task.correctSentence.toLowerCase();
    explanation = `Correct sentence: "${task.correctSentence}"`;
  }

  if (isCorrect) {
    DuoSound.playCorrect();
    bottomBar.className = 'lesson-bottom-bar state-success';
    feedbackMsg.innerHTML = `
      <div style="font-weight:800; font-size:1.15rem; color:#10b981;">✓ Nicely done!</div>
      <div style="font-size:0.88rem; color:#cbd5e1; margin-top:2px;">${explanation}</div>
    `;
    actionBtn.textContent = 'Continue';
  } else {
    DuoSound.playWrong();
    // Unlimited tries - no heart loss!
    bottomBar.className = 'lesson-bottom-bar state-error';
    feedbackMsg.innerHTML = `
      <div style="font-weight:800; font-size:1.15rem; color:#ef4444;">✕ Not Quite • Unlimited Tries (Review & Keep Going)</div>
      <div style="font-size:0.88rem; color:#cbd5e1; margin-top:2px;">${explanation}</div>
    `;
    actionBtn.textContent = 'Continue';
  }

  // Interactive Question Feedback Widget
  renderQuestionFeedbackWidget(task, isCorrect, feedbackMsg);
}

/* ==========================================================================
   PER-QUESTION FEEDBACK WIDGET
   ========================================================================== */
function renderQuestionFeedbackWidget(task, isCorrect, container) {
  const data = getActiveDuoData();
  const topicId = data && data.id ? data.id : 'general';
  const qId = `${topicId}_${activeLevel ? activeLevel.id : 'lvl'}_q${currentTaskIndex}`;
  
  const existingList = CORTEX_FEEDBACK.getAllQuestionFeedback();
  const existing = existingList.find(x => x.id === qId);

  const fbWrap = document.createElement('div');
  fbWrap.className = 'duo-q-feedback-box';
  fbWrap.id = 'duo-q-feedback-box';
  fbWrap.innerHTML = `
    <div class="q-fb-header">
      <span class="q-fb-title">Rate this question:</span>
      <span class="q-fb-tag-saved" id="q-fb-tag-saved" style="${existing ? 'display:inline-block;' : 'display:none;'}">✓ Feedback Saved (${existing ? existing.rating : ''})</span>
    </div>
    <div class="q-fb-chips">
      <button type="button" class="q-fb-chip ${existing && existing.rating === 'Helpful' ? 'selected' : ''}" data-rating="Helpful" title="Clear & insightful">👍 Helpful</button>
      <button type="button" class="q-fb-chip ${existing && existing.rating === 'Clear' ? 'selected' : ''}" data-rating="Clear" title="Good clarity & balance">💡 Clear</button>
      <button type="button" class="q-fb-chip ${existing && existing.rating === 'Confusing' ? 'selected' : ''}" data-rating="Confusing" title="Ambiguous or difficult">🤔 Confusing</button>
      <button type="button" class="q-fb-chip ${existing && existing.rating === 'Issue' ? 'selected' : ''}" data-rating="Issue" title="Typo, error or bug">⚠️ Typo / Issue</button>
    </div>
    <div class="q-fb-input-row" id="q-fb-input-row">
      <input type="text" class="q-fb-note-input" id="q-fb-note-input" placeholder="Optional note for AI/developer..." value="${existing && existing.note ? existing.note.replace(/"/g, '&quot;') : ''}" maxlength="150" />
      <button type="button" class="q-fb-note-btn" id="q-fb-note-btn">Save Note</button>
    </div>
  `;

  container.appendChild(fbWrap);

  const chips = fbWrap.querySelectorAll('.q-fb-chip');
  const noteInput = fbWrap.querySelector('#q-fb-note-input');
  const saveBtn = fbWrap.querySelector('#q-fb-note-btn');
  const tagSaved = fbWrap.querySelector('#q-fb-tag-saved');

  function saveCurrent(ratingOverride) {
    const activeChip = fbWrap.querySelector('.q-fb-chip.selected');
    const rating = ratingOverride || (activeChip ? activeChip.dataset.rating : 'Helpful');
    const note = noteInput ? noteInput.value.trim() : '';

    const payload = {
      id: qId,
      topic: topicId,
      levelId: activeLevel ? activeLevel.id : 'lvl',
      levelNumber: activeLevel ? activeLevel.levelNumber : 1,
      levelTitle: activeLevel ? activeLevel.title : '',
      taskIndex: currentTaskIndex,
      prompt: task.prompt || task.title || (task.tokens ? task.tokens.join(' ') : 'Question'),
      rating: rating,
      note: note,
      isCorrect: isCorrect,
      timestamp: new Date().toISOString()
    };

    CORTEX_FEEDBACK.saveQuestionFeedback(payload);
    if (tagSaved) {
      tagSaved.textContent = `✓ Feedback Saved (${rating})`;
      tagSaved.style.display = 'inline-block';
    }
  }

  chips.forEach(chip => {
    chip.addEventListener('click', (e) => {
      e.stopPropagation();
      chips.forEach(c => c.classList.remove('selected'));
      chip.classList.add('selected');
      saveCurrent(chip.dataset.rating);
    });
  });

  if (saveBtn) {
    saveBtn.addEventListener('click', (e) => {
      e.stopPropagation();
      saveCurrent();
    });
  }

  if (noteInput) {
    noteInput.addEventListener('keydown', (e) => {
      e.stopPropagation();
      if (e.key === 'Enter') {
        saveCurrent();
      }
    });
    noteInput.addEventListener('keyup', (e) => e.stopPropagation());
  }
}

/* ==========================================================================
   LESSON COMPLETION & LESSON-WISE STARS MATRIX WITH AI FEEDBACK
   ========================================================================== */
function completeLesson() {
  DuoSound.playFanfare();
  DuoState.completeLevel(activeLevel.id, activeLevel.xpReward, 3);

  const arena = document.getElementById('lesson-task-arena');
  const bottomBar = document.getElementById('lesson-bottom-bar');
  const actionBtn = document.getElementById('lesson-action-btn');
  const feedbackMsg = document.getElementById('lesson-feedback-message');

  if (bottomBar) bottomBar.className = 'lesson-bottom-bar state-ready';
  if (feedbackMsg) feedbackMsg.innerHTML = '';

  const data = getActiveDuoData();
  const state = DuoState.getProgress();
  const topicId = data && data.id ? data.id : 'general';
  const existingFeedback = CORTEX_FEEDBACK.getCourseFeedback(topicId);
  const currentRating = existingFeedback ? existingFeedback.rating : 5;
  const currentComment = existingFeedback ? existingFeedback.comment : '';

  // Lesson-Wise Stars Table for all 10 levels
  let starsTableHtml = `
    <div class="duo-stars-matrix-wrap">
      <div class="duo-stars-matrix-header">
        <h3 style="font-family:var(--font-display); font-size:1.25rem; color:#facc15; display:flex; align-items:center; gap:0.5rem; justify-content:center;">
          <span>🌟</span> Lesson-Wise Stars & Mastery Matrix
        </h3>
        <p style="font-size:0.84rem; color:var(--text-muted); margin-top:0.25rem; text-align:center;">
          Review your stars across all ${data.levels ? data.levels.length : 10} lessons
        </p>
      </div>

      <div class="duo-stars-table-scroll">
        <table class="duo-stars-table">
          <thead>
            <tr>
              <th>Level</th>
              <th>Lesson Title</th>
              <th>Stars</th>
              <th>Status</th>
              <th>Question Notes</th>
            </tr>
          </thead>
          <tbody>
  `;

  const allQFeedback = CORTEX_FEEDBACK.getAllQuestionFeedback().filter(x => !topicId || x.topic === topicId || x.topic === data.id);

  let totalStars = 0;
  (data.levels || []).forEach(lvl => {
    const isDone = state.completedLevels.includes(lvl.id);
    const starsCount = (state.levelStars && state.levelStars[lvl.id]) || (isDone ? 3 : 0);
    totalStars += starsCount;
    const starsDisplay = starsCount > 0 ? '⭐'.repeat(starsCount) : '<span style="color:#64748b;">—</span>';
    const statusBadge = isDone 
      ? '<span class="status-badge done">✓ Mastered</span>' 
      : '<span class="status-badge pending">In Progress</span>';
    const qCount = allQFeedback.filter(q => q.levelId === lvl.id || q.levelNumber === lvl.levelNumber).length;
    const notesBadge = qCount > 0 
      ? `<span class="notes-count-badge">📝 ${qCount} note${qCount > 1 ? 's' : ''}</span>` 
      : '<span style="color:#64748b;">—</span>';

    starsTableHtml += `
      <tr class="${lvl.id === activeLevel.id ? 'highlight-current' : ''}">
        <td><strong>L${lvl.levelNumber}</strong></td>
        <td style="text-align:left;">${lvl.title}</td>
        <td class="star-cell">${starsDisplay}</td>
        <td>${statusBadge}</td>
        <td>${notesBadge}</td>
      </tr>
    `;
  });

  starsTableHtml += `
          </tbody>
        </table>
      </div>
      <div style="font-size:0.85rem; font-weight:800; color:#38bdf8; text-align:right; margin-top:0.5rem;">
        Total Stars Earned: ${totalStars} / ${(data.levels ? data.levels.length : 10) * 3} ⭐
      </div>
    </div>
  `;

  arena.innerHTML = `
    <div class="duo-completion-screen">
      <div class="completion-crown">👑</div>
      <h2 style="font-family:var(--font-display); font-size:2rem; color:#fff; margin-bottom:0.25rem;">Lesson Complete!</h2>
      <p style="color:var(--text-muted); margin-bottom:1.25rem;">You mastered Level ${activeLevel.levelNumber}: ${activeLevel.title}</p>

      <div class="duo-rewards-row" style="margin-bottom:1.5rem;">
        <div class="duo-reward-card">
          <div style="font-size:1.6rem;">💎</div>
          <div style="font-size:1.3rem; font-weight:800; color:#38bdf8;">+${activeLevel.xpReward} XP</div>
          <div style="font-size:0.75rem; color:var(--text-dim);">Earned Today</div>
        </div>
        <div class="duo-reward-card">
          <div style="font-size:1.6rem;">⭐</div>
          <div style="font-size:1.3rem; font-weight:800; color:#facc15;">3 / 3 Stars</div>
          <div style="font-size:0.75rem; color:var(--text-dim);">Mastery Rating</div>
        </div>
        <div class="duo-reward-card">
          <div style="font-size:1.6rem;">🔥</div>
          <div style="font-size:1.3rem; font-weight:800; color:#fbbf24;">18 Days</div>
          <div style="font-size:0.75rem; color:var(--text-dim);">Active Streak</div>
        </div>
      </div>

      ${starsTableHtml}

      <!-- Course & AI Feedback Form -->
      <div class="duo-ai-feedback-box" id="duo-ai-feedback-box">
        <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.4rem; display:flex; align-items:center; gap:0.4rem; justify-content:center;">
          <span>💬</span> Send Feedback to the AI / Developer
        </h4>
        <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.8rem; text-align:center;">
          Rate this course and write suggestions. Click "Copy Feedback Report" to paste directly into our chat!
        </p>

        <div class="course-star-rating-row" style="justify-content:center;">
          <span style="font-size:0.82rem; font-weight:700; color:#cbd5e1;">Course Rating:</span>
          <div class="rating-stars" id="course-rating-stars">
            ${[1, 2, 3, 4, 5].map(num => `
              <button type="button" class="star-btn ${num <= currentRating ? 'active' : ''}" data-val="${num}">⭐</button>
            `).join('')}
          </div>
        </div>

        <div class="course-quick-tags" style="margin:0.5rem 0; justify-content:center;">
          <span style="font-size:0.75rem; color:#94a3b8; margin-right:4px;">Quick tags:</span>
          <button type="button" class="quick-fb-tag" data-tag="High UPSC Yield">🎯 High Yield</button>
          <button type="button" class="quick-fb-tag" data-tag="Great Explanations">🔍 Great Explanations</button>
          <button type="button" class="quick-fb-tag" data-tag="Helpful Flowcharts">📊 Helpful Flowcharts</button>
          <button type="button" class="quick-fb-tag" data-tag="Well Balanced Pacing">⏱️ Good Pacing</button>
          <button type="button" class="quick-fb-tag" data-tag="Add More Mains PYQs">📝 More PYQs</button>
        </div>

        <textarea class="course-feedback-textarea" id="course-feedback-input" rows="3" placeholder="What did you think of the explanations, notes, and question difficulty? Tell me what to polish or add...">${currentComment}</textarea>

        <div class="feedback-export-btn-group">
          <button type="button" class="btn-copy-ai-feedback" id="btn-copy-ai-feedback">
            <span>📋</span> Copy Feedback Report for AI
          </button>
          <button type="button" class="btn-download-json-feedback" id="btn-download-json-feedback">
            <span>💾</span> Download JSON
          </button>
        </div>
      </div>
    </div>
  `;

  // Bind interactive handlers
  wireFeedbackBoxEvents(topicId, data, state);

  if (actionBtn) {
    actionBtn.textContent = 'Finish & Return to Path';
    actionBtn.onclick = () => {
      document.getElementById('duo-lesson-modal').classList.remove('active');
      renderLevelPath();
      DuoState.updateHeaderUI();
    };
  }
}

/* ==========================================================================
   INTERACTIVE FEEDBACK WIRING & MODAL ENGINE
   ========================================================================== */
function wireFeedbackBoxEvents(topicId, duoData, state) {
  const container = document.getElementById('duo-ai-feedback-box');
  if (!container) return;

  let selectedRating = 5;
  const existing = CORTEX_FEEDBACK.getCourseFeedback(topicId);
  if (existing && existing.rating) selectedRating = existing.rating;

  const starBtns = container.querySelectorAll('.star-btn');
  const commentInput = container.querySelector('#course-feedback-input');
  const copyBtn = container.querySelector('#btn-copy-ai-feedback');
  const downloadBtn = container.querySelector('#btn-download-json-feedback');
  const quickTags = container.querySelectorAll('.quick-fb-tag');

  starBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const val = parseInt(btn.dataset.val, 10);
      selectedRating = val;
      starBtns.forEach(b => {
        const bVal = parseInt(b.dataset.val, 10);
        b.classList.toggle('active', bVal <= val);
      });
      CORTEX_FEEDBACK.saveCourseFeedback(topicId, selectedRating, commentInput ? commentInput.value : '');
    });
  });

  quickTags.forEach(tag => {
    tag.addEventListener('click', () => {
      if (!commentInput) return;
      const text = tag.dataset.tag;
      if (commentInput.value.includes(text)) return;
      commentInput.value = commentInput.value ? `${commentInput.value}; ${text}` : text;
      CORTEX_FEEDBACK.saveCourseFeedback(topicId, selectedRating, commentInput.value);
    });
  });

  if (commentInput) {
    commentInput.addEventListener('input', () => {
      CORTEX_FEEDBACK.saveCourseFeedback(topicId, selectedRating, commentInput.value);
    });
  }

  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      const comment = commentInput ? commentInput.value : '';
      CORTEX_FEEDBACK.saveCourseFeedback(topicId, selectedRating, comment);
      const md = CORTEX_FEEDBACK.buildMarkdownReport(topicId, duoData, state.completedLevels, state.levelStars, selectedRating, comment);
      copyReportToClipboard(md, copyBtn);
    });
  }

  if (downloadBtn) {
    downloadBtn.addEventListener('click', () => {
      const comment = commentInput ? commentInput.value : '';
      CORTEX_FEEDBACK.saveCourseFeedback(topicId, selectedRating, comment);
      downloadFeedbackJson(topicId, duoData, state.completedLevels, state.levelStars, selectedRating, comment);
    });
  }
}

function openStarsFeedbackModal() {
  const data = getActiveDuoData();
  const state = DuoState.getProgress();
  const topicId = data && data.id ? data.id : 'general';

  let modal = document.getElementById('duo-stars-modal');
  if (!modal) {
    modal = document.createElement('div');
    modal.className = 'duo-stars-modal-overlay';
    modal.id = 'duo-stars-modal';
    document.body.appendChild(modal);
  }

  const existingFeedback = CORTEX_FEEDBACK.getCourseFeedback(topicId);
  const currentRating = existingFeedback ? existingFeedback.rating : 5;
  const currentComment = existingFeedback ? existingFeedback.comment : '';
  const allQFeedback = CORTEX_FEEDBACK.getAllQuestionFeedback().filter(x => !topicId || x.topic === topicId || x.topic === data.id);

  let rowsHtml = '';
  let totalStars = 0;
  (data.levels || []).forEach(lvl => {
    const isDone = state.completedLevels.includes(lvl.id);
    const starsCount = (state.levelStars && state.levelStars[lvl.id]) || (isDone ? 3 : 0);
    totalStars += starsCount;
    const starsDisplay = starsCount > 0 ? '⭐'.repeat(starsCount) : '<span style="color:#64748b;">—</span>';
    const statusBadge = isDone 
      ? '<span class="status-badge done">✓ Mastered</span>' 
      : '<span class="status-badge pending">In Progress</span>';
    const qCount = allQFeedback.filter(q => q.levelId === lvl.id || q.levelNumber === lvl.levelNumber).length;
    const notesBadge = qCount > 0 
      ? `<span class="notes-count-badge">📝 ${qCount} note${qCount > 1 ? 's' : ''}</span>` 
      : '<span style="color:#64748b;">—</span>';

    rowsHtml += `
      <tr>
        <td><strong>L${lvl.levelNumber}</strong></td>
        <td style="text-align:left;">${lvl.title}</td>
        <td class="star-cell">${starsDisplay}</td>
        <td>${statusBadge}</td>
        <td>${notesBadge}</td>
      </tr>
    `;
  });

  modal.innerHTML = `
    <div class="duo-stars-modal-dialog">
      <div class="duo-stars-modal-header">
        <div>
          <h3 style="font-family:var(--font-display); font-size:1.4rem; color:#fff; display:flex; align-items:center; gap:0.5rem;">
            <span>🌟</span> Lesson-Wise Stars & Course Feedback
          </h3>
          <p style="font-size:0.82rem; color:var(--text-muted); margin-top:2px;">
            ${data.title || 'UPSC Master Course'} • ${data.levels ? data.levels.length : 10} Interactive Lessons
          </p>
        </div>
        <button class="duo-stars-modal-close" onclick="document.getElementById('duo-stars-modal').classList.remove('active')">&times;</button>
      </div>

      <div class="duo-stars-modal-body">
        <div class="duo-stars-table-scroll">
          <table class="duo-stars-table">
            <thead>
              <tr>
                <th>Level</th>
                <th>Lesson Title</th>
                <th>Stars</th>
                <th>Status</th>
                <th>Notes</th>
              </tr>
            </thead>
            <tbody>${rowsHtml}</tbody>
          </table>
        </div>
        <div style="font-size:0.85rem; font-weight:800; color:#38bdf8; text-align:right; margin: 0.5rem 0 1rem 0;">
          Total Stars Earned: ${totalStars} / ${(data.levels ? data.levels.length : 10) * 3} ⭐
        </div>

        <!-- AI Feedback Section -->
        <div class="duo-ai-feedback-box" id="duo-ai-feedback-box">
          <h4 style="color:#fff; font-size:1.05rem; margin-bottom:0.4rem; display:flex; align-items:center; gap:0.4rem;">
            <span>💬</span> Send Feedback to the AI / Pair Programmer
          </h4>
          <p style="font-size:0.8rem; color:var(--text-muted); margin-bottom:0.8rem;">
            Write your thoughts or click "Copy Feedback Report" to paste directly into our chat!
          </p>

          <div class="course-star-rating-row">
            <span style="font-size:0.82rem; font-weight:700; color:#cbd5e1;">Your Course Rating:</span>
            <div class="rating-stars" id="course-rating-stars">
              ${[1, 2, 3, 4, 5].map(num => `
                <button type="button" class="star-btn ${num <= currentRating ? 'active' : ''}" data-val="${num}">⭐</button>
              `).join('')}
            </div>
          </div>

          <div class="course-quick-tags" style="margin:0.5rem 0;">
            <span style="font-size:0.75rem; color:#94a3b8; margin-right:4px;">Quick tags:</span>
            <button type="button" class="quick-fb-tag" data-tag="High UPSC Yield">🎯 High Yield</button>
            <button type="button" class="quick-fb-tag" data-tag="Great Explanations">🔍 Great Explanations</button>
            <button type="button" class="quick-fb-tag" data-tag="Helpful Flowcharts">📊 Helpful Flowcharts</button>
            <button type="button" class="quick-fb-tag" data-tag="Well Balanced Pacing">⏱️ Good Pacing</button>
            <button type="button" class="quick-fb-tag" data-tag="Add More Mains PYQs">📝 More PYQs</button>
          </div>

          <textarea class="course-feedback-textarea" id="course-feedback-input" rows="3" placeholder="What did you think of the explanations, notes, and question difficulty? Tell me what to polish or add...">${currentComment}</textarea>

          <div class="feedback-export-btn-group">
            <button type="button" class="btn-copy-ai-feedback" id="btn-copy-ai-feedback">
              <span>📋</span> Copy Feedback Report for AI
            </button>
            <button type="button" class="btn-download-json-feedback" id="btn-download-json-feedback">
              <span>💾</span> Download JSON
            </button>
          </div>
        </div>
      </div>
    </div>
  `;

  modal.classList.add('active');
  wireFeedbackBoxEvents(topicId, data, state);
}

window.openStarsFeedbackModal = openStarsFeedbackModal;
