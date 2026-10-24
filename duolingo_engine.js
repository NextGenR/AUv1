/**
 * CORTEX DUOLINGO ENGINE - GAMIFIED UPSC LEVEL-WISE LEARNING
 * Sound FX, Visual Winding Path, Hearts/Lives, XP, Tap-to-Order & Match Pairs
 */

class DuoState {
  static getProgress() {
    const raw = localStorage.getItem('cortex_duo_progress');
    return raw ? JSON.parse(raw) : {
      xp: 60,
      hearts: 5,
      completedLevels: ["lvl-1"],
      streak: 18
    };
  }

  static saveProgress(state) {
    localStorage.setItem('cortex_duo_progress', JSON.stringify(state));
    DuoState.updateHeaderUI();
  }

  static completeLevel(levelId, xpReward) {
    const state = DuoState.getProgress();
    if (!state.completedLevels.includes(levelId)) {
      state.completedLevels.push(levelId);
    }
    state.xp += xpReward;
    DuoState.saveProgress(state);
  }

  static deductHeart() {
    const state = DuoState.getProgress();
    state.hearts = Math.max(0, state.hearts - 1);
    DuoState.saveProgress(state);
    return state.hearts;
  }

  static refillHearts() {
    const state = DuoState.getProgress();
    state.hearts = 5;
    DuoState.saveProgress(state);
  }

  static updateHeaderUI() {
    const state = DuoState.getProgress();
    const xpEl = document.getElementById('duo-xp-count');
    const heartsEl = document.getElementById('duo-hearts-count');
    const streakEl = document.getElementById('duo-streak-count');

    if (xpEl) xpEl.textContent = state.xp;
    if (heartsEl) heartsEl.textContent = state.hearts;
    if (streakEl) streakEl.textContent = state.streak;
  }
}

// Duolingo Signature Web Audio Sound Synthesizer
class DuoSound {
  static init() {
    if (!this.ctx) {
      const AudioCtx = window.AudioContext || window.webkitAudioContext;
      if (AudioCtx) this.ctx = new AudioCtx();
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
  if (!container || !PUBLIC_EXAM_DATA.sheetNotes) return;

  const data = PUBLIC_EXAM_DATA.sheetNotes;
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

  container.innerHTML = '';
  const progress = DuoState.getProgress();
  let currentUnit = '';

  PUBLIC_EXAM_DATA.levels.forEach((lvl, idx) => {
    // If new unit, render unit header banner
    if (lvl.unit !== currentUnit) {
      currentUnit = lvl.unit;
      const unitBanner = document.createElement('div');
      unitBanner.className = 'duo-unit-banner';
      unitBanner.style.borderLeftColor = lvl.unitColor;
      unitBanner.innerHTML = `
        <div class="unit-meta" style="color:${lvl.unitColor};">${lvl.unit.toUpperCase()}</div>
        <div class="unit-title">Exam Integrity & Institutional Reforms</div>
      `;
      container.appendChild(unitBanner);
    }

    // Determine status: completed, current, or locked
    const isCompleted = progress.completedLevels.includes(lvl.id);
    const prevCompleted = idx === 0 || progress.completedLevels.includes(PUBLIC_EXAM_DATA.levels[idx - 1].id);
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
function startLesson(level) {
  activeLevel = level;
  currentTaskIndex = 0;
  selectedOption = null;
  assembledTokens = [];
  matchedPairCount = 0;

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

  // Render specific task template
  if (task.type === 'concept') {
    renderConceptTask(task, arena, actionBtn);
  } else if (task.type === 'mcq') {
    renderMcqTask(task, arena, actionBtn);
  } else if (task.type === 'true_false') {
    renderTrueFalseTask(task, arena, actionBtn);
  } else if (task.type === 'match_pairs') {
    renderMatchPairsTask(task, arena, actionBtn);
  } else if (task.type === 'tap_order') {
    renderTapOrderTask(task, arena, actionBtn);
  }
}

/* --- Task Type 1: Concept Drop --- */
function renderConceptTask(task, arena, actionBtn) {
  arena.innerHTML = `
    <div class="duo-concept-card">
      <div class="duo-mascot-row">
        <div class="duo-mascot-avatar">🦉</div>
        <div class="duo-speech-bubble">
          <strong>${task.title}</strong>
          <p>${task.content.replace(/\n/g, '<br>')}</p>
        </div>
      </div>
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

  if (task.type === 'mcq') {
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
    const remainingHearts = DuoState.deductHeart();
    bottomBar.className = 'lesson-bottom-bar state-error';
    feedbackMsg.innerHTML = `
      <div style="font-weight:800; font-size:1.15rem; color:#ef4444;">✕ Incorrect • Lost 1 Heart (${remainingHearts} left)</div>
      <div style="font-size:0.88rem; color:#cbd5e1; margin-top:2px;">${explanation}</div>
    `;
    actionBtn.textContent = 'Continue';
  }
}

/* ==========================================================================
   LESSON COMPLETION & REWARD MODAL
   ========================================================================== */
function completeLesson() {
  DuoSound.playFanfare();
  DuoState.completeLevel(activeLevel.id, activeLevel.xpReward);

  const arena = document.getElementById('lesson-task-arena');
  const bottomBar = document.getElementById('lesson-bottom-bar');
  const actionBtn = document.getElementById('lesson-action-btn');
  const feedbackMsg = document.getElementById('lesson-feedback-message');

  if (bottomBar) bottomBar.className = 'lesson-bottom-bar state-ready';
  if (feedbackMsg) feedbackMsg.innerHTML = '';

  arena.innerHTML = `
    <div class="duo-completion-screen">
      <div class="completion-crown">👑</div>
      <h2 style="font-family:var(--font-display); font-size:2rem; color:#fff; margin-bottom:0.5rem;">Lesson Complete!</h2>
      <p style="color:var(--text-muted); margin-bottom:1.5rem;">You mastered Level ${activeLevel.levelNumber}: ${activeLevel.title}</p>

      <div class="duo-rewards-row">
        <div class="duo-reward-card">
          <div style="font-size:1.8rem;">💎</div>
          <div style="font-size:1.4rem; font-weight:800; color:#38bdf8;">+${activeLevel.xpReward} XP</div>
          <div style="font-size:0.75rem; color:var(--text-dim);">Earned Today</div>
        </div>
        <div class="duo-reward-card">
          <div style="font-size:1.8rem;">🔥</div>
          <div style="font-size:1.4rem; font-weight:800; color:#fbbf24;">18 Days</div>
          <div style="font-size:0.75rem; color:var(--text-dim);">Active Streak</div>
        </div>
      </div>
    </div>
  `;

  if (actionBtn) {
    actionBtn.textContent = 'Finish & Return to Path';
    actionBtn.onclick = () => {
      document.getElementById('duo-lesson-modal').classList.remove('active');
      renderLevelPath();
      DuoState.updateHeaderUI();
    };
  }
}
