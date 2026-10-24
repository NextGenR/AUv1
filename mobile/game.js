/**
 * CORTEX MOBILE GAME ENGINE
 * Native Touch Gestures, Web Audio Sound Effects, Canvas Confetti & Game Physics
 */

(function () {
  'use strict';

  // --- AUDIO SYNTHESIZER (WEB AUDIO API) ---
  const SoundFX = {
    ctx: null,
    init() {
      if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
        this.ctx = new (window.AudioContext || window.webkitAudioContext)();
      }
    },
    playTap() {
      try {
        this.init();
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(600, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(800, this.ctx.currentTime + 0.05);
        gain.gain.setValueAtTime(0.15, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.05);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.06);
      } catch (e) {}
    },
    playCorrect() {
      try {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const notes = [587.33, 880]; // D5, A5
        notes.forEach((freq, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.08);
          gain.gain.setValueAtTime(0.2, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.18);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.2);
        });
      } catch (e) {}
    },
    playError() {
      try {
        this.init();
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(160, this.ctx.currentTime);
        osc.frequency.linearRampToValueAtTime(100, this.ctx.currentTime + 0.2);
        gain.gain.setValueAtTime(0.25, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.2);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.22);
      } catch (e) {}
    },
    playBossHit() {
      try {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'square';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(40, now + 0.25);
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.01, now + 0.25);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start(now);
        osc.stop(now + 0.26);
      } catch (e) {}
    },
    playVictory() {
      try {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const melody = [523.25, 659.25, 783.99, 1046.50]; // C, E, G, High C
        melody.forEach((freq, idx) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + idx * 0.09);
          gain.gain.setValueAtTime(0.25, now + idx * 0.09);
          gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.09 + 0.35);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + idx * 0.09);
          osc.stop(now + idx * 0.09 + 0.38);
        });
      } catch (e) {}
    }
  };

  // --- CONFETTI CANNON ENGINE ---
  const Confetti = {
    canvas: null,
    ctx: null,
    particles: [],
    animId: null,
    init() {
      this.canvas = document.getElementById('game-confetti-canvas');
      if (this.canvas) {
        this.ctx = this.canvas.getContext('2d');
        this.resize();
        window.addEventListener('resize', () => this.resize());
      }
    },
    resize() {
      if (!this.canvas) return;
      this.canvas.width = window.innerWidth;
      this.canvas.height = window.innerHeight;
    },
    launch() {
      if (!this.canvas || !this.ctx) return;
      this.particles = [];
      const colors = ['#10b981', '#3b82f6', '#facc15', '#ec4899', '#8b5cf6', '#f97316'];
      for (let i = 0; i < 90; i++) {
        this.particles.push({
          x: this.canvas.width / 2 + (Math.random() - 0.5) * 80,
          y: this.canvas.height / 2 + (Math.random() - 0.5) * 40,
          vx: (Math.random() - 0.5) * 14,
          vy: (Math.random() - 0.8) * 16,
          size: Math.random() * 8 + 4,
          color: colors[Math.floor(Math.random() * colors.length)],
          rotation: Math.random() * 360,
          rotSpeed: (Math.random() - 0.5) * 10,
          life: 1
        });
      }
      cancelAnimationFrame(this.animId);
      this.animate();
    },
    animate() {
      if (!this.ctx || this.particles.length === 0) return;
      this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      this.particles.forEach((p, index) => {
        p.x += p.vx;
        p.y += p.vy;
        p.vy += 0.4; // gravity
        p.rotation += p.rotSpeed;
        p.life -= 0.015;

        this.ctx.save();
        this.ctx.translate(p.x, p.y);
        this.ctx.rotate((p.rotation * Math.PI) / 180);
        this.ctx.fillStyle = p.color;
        this.ctx.globalAlpha = Math.max(0, p.life);
        this.ctx.fillRect(-p.size / 2, -p.size / 2, p.size, p.size);
        this.ctx.restore();

        if (p.life <= 0) {
          this.particles.splice(index, 1);
        }
      });
      if (this.particles.length > 0) {
        this.animId = requestAnimationFrame(() => this.animate());
      } else {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
      }
    }
  };

  // --- URL PARAMETERS & INITIAL TOPIC ---
  const urlParams = new URLSearchParams(window.location.search);
  const initialTopic = urlParams.get('topic') || localStorage.getItem('cortex_active_topic') || 'msme';

  // --- GAME STATE ---
  const STATE = {
    currentTopic: (typeof GAME_DATA !== 'undefined' && GAME_DATA.topics && GAME_DATA.topics[initialTopic]) ? initialTopic : 'msme',
    hearts: 'unlimited', // Unlimited tries - no heart depletion
    gems: parseInt(localStorage.getItem('cortex_game_gems') || '450', 10),
    coins: parseInt(localStorage.getItem('cortex_game_coins') || '1280', 10),
    streak: parseInt(localStorage.getItem('cortex_game_streak') || '18', 10),
    completedLevels: new Set(JSON.parse(localStorage.getItem(`cortex_game_levels_${initialTopic}`) || '[1]')),
    levelStars: JSON.parse(localStorage.getItem(`cortex_game_stars_${initialTopic}`) || '{"1":3}'),
    activeTab: 'map',
    theme: localStorage.getItem('samsung_ui_theme') || 'samsung-dark',

    // Active Level Session
    activeLevel: null,
    currentQuestionIdx: 0,
    selectedOption: null,
    assembledTokens: [],
    matchedPairsCount: 0,
    activeMatchPick: null,
    bossCurrentHp: 1000,

    // Blitz Session
    blitzTimer: 60,
    blitzInterval: null,
    blitzScore: 0,
    blitzCombo: 1,
    blitzIndex: 0
  };

  function saveState() {
    localStorage.setItem('cortex_game_hearts', 'unlimited');
    localStorage.setItem('cortex_game_gems', STATE.gems);
    localStorage.setItem('cortex_game_coins', STATE.coins);
    localStorage.setItem('cortex_game_streak', STATE.streak);
    localStorage.setItem(`cortex_game_levels_${STATE.currentTopic}`, JSON.stringify(Array.from(STATE.completedLevels)));
    localStorage.setItem(`cortex_game_stars_${STATE.currentTopic}`, JSON.stringify(STATE.levelStars));
    updateHUD();
  }

  // --- DOM ELEMENTS ---
  const DOM = {
    hudStreak: document.getElementById('hud-streak-count'),
    hudGems: document.getElementById('hud-gems-count'),
    hudCoins: document.getElementById('hud-coins-count'),
    hudHearts: document.getElementById('hud-hearts-count'),
    hudHeartsPill: document.getElementById('hud-hearts-pill'),
    themeToggleBtn: document.getElementById('samsung-theme-toggle'),
    themeToggleIcon: document.getElementById('theme-toggle-icon'),
    themeToggleText: document.getElementById('theme-toggle-text'),
    screens: document.querySelectorAll('.game-screen'),
    dockBtns: document.querySelectorAll('.dock-btn'),
    questPath: document.getElementById('quest-path-content'),
    // Topic Switcher Elements
    topicPills: document.querySelectorAll('.topic-pill'),
    topicLevelCounter: document.getElementById('topic-level-counter'),
    btnOpenFlowcharts: document.getElementById('btn-open-flowcharts'),
    // Flowchart Modal Elements
    flowchartModal: document.getElementById('flowchart-modal'),
    flowchartCloseBtn: document.getElementById('flowchart-modal-close'),
    flowchartTabs: document.querySelectorAll('.fc-tab-btn'),
    flowchartImg: document.getElementById('flowchart-active-img'),
    flowchartTitle: document.getElementById('flowchart-modal-title'),
    flowchartDesc: document.getElementById('flowchart-desc-text'),
    flowchartFullscreen: document.getElementById('btn-fc-fullscreen'),
    // Stars & AI Feedback Modal Elements
    btnOpenStarsFeedback: document.getElementById('btn-open-stars-feedback'),
    starsFeedbackModal: document.getElementById('stars-feedback-modal'),
    starsModalCloseBtn: document.getElementById('stars-modal-close-btn'),
    starsModalBody: document.getElementById('stars-modal-body'),
    starsModalTopicTitle: document.getElementById('stars-modal-topic-title'),
    // Play Modal
    playModal: document.getElementById('play-modal'),
    playCloseBtn: document.getElementById('play-close-btn'),
    playProgressBar: document.getElementById('play-progress-bar'),
    bossHpContainer: document.getElementById('boss-hp-container'),
    bossHpFill: document.getElementById('boss-hp-fill'),
    bossHpText: document.getElementById('boss-hp-text'),
    playQuestionBox: document.getElementById('play-question-box'),
    feedbackBanner: document.getElementById('feedback-banner'),
    playActionBtn: document.getElementById('play-action-btn'),
    // Blitz Arena
    blitzScreen: document.getElementById('screen-blitz'),
    blitzTimer: document.getElementById('blitz-timer-display'),
    blitzCombo: document.getElementById('blitz-combo-badge'),
    blitzCardText: document.getElementById('blitz-card-text'),
    btnBlitzTrue: document.getElementById('btn-blitz-true'),
    btnBlitzFalse: document.getElementById('btn-blitz-false'),
    // Leaderboard & Shop
    leaderboardList: document.getElementById('leaderboard-list'),
    shopGrid: document.getElementById('shop-grid')
  };

  // --- SAMSUNG ONE UI THEME CONTROLLER ---
  function applySamsungTheme(theme) {
    STATE.theme = theme;
    localStorage.setItem('samsung_ui_theme', theme);
    localStorage.setItem('cortex_roadmap_dark', theme === 'samsung-dark' ? 'true' : 'false');

    if (theme === 'samsung-light') {
      document.body.classList.remove('samsung-dark');
      document.body.classList.add('samsung-light');
      if (DOM.themeToggleIcon) DOM.themeToggleIcon.textContent = '☀️';
      if (DOM.themeToggleText) DOM.themeToggleText.textContent = 'Light';
      const metaTheme = document.querySelector('meta[name="theme-color"]');
      if (metaTheme) metaTheme.setAttribute('content', '#f2f4f8');
    } else {
      document.body.classList.remove('samsung-light');
      document.body.classList.add('samsung-dark');
      if (DOM.themeToggleIcon) DOM.themeToggleIcon.textContent = '🌙';
      if (DOM.themeToggleText) DOM.themeToggleText.textContent = 'Dark';
      const metaTheme = document.querySelector('meta[name="theme-color"]');
      if (metaTheme) metaTheme.setAttribute('content', '#000000');
    }
  }

  function toggleSamsungTheme() {
    SoundFX.playTap();
    const nextTheme = STATE.theme === 'samsung-dark' ? 'samsung-light' : 'samsung-dark';
    applySamsungTheme(nextTheme);
  }

  // --- UPDATE TOP HUD ---
  function updateHUD() {
    if (DOM.hudStreak) DOM.hudStreak.textContent = STATE.streak;
    if (DOM.hudGems) DOM.hudGems.textContent = STATE.gems;
    if (DOM.hudCoins) DOM.hudCoins.textContent = STATE.coins.toLocaleString();
    if (DOM.hudHearts) DOM.hudHearts.textContent = '♾️ Unlimited';
    if (DOM.hudHeartsPill) {
      DOM.hudHeartsPill.classList.remove('low-hearts');
    }
  }

  // --- SWITCH TABS ---
  function switchTab(tabId) {
    SoundFX.playTap();
    STATE.activeTab = tabId;
    DOM.screens.forEach(s => s.classList.remove('active'));
    DOM.dockBtns.forEach(b => b.classList.remove('active'));

    const targetScreen = document.getElementById(`screen-${tabId}`);
    const targetBtn = document.querySelector(`.dock-btn[data-tab="${tabId}"]`);

    if (targetScreen) targetScreen.classList.add('active');
    if (targetBtn) targetBtn.classList.add('active');

    if (tabId === 'blitz') {
      startBlitzGame();
    } else {
      clearInterval(STATE.blitzInterval);
    }
  }

  // --- TOPIC CONTROLLER (SAMSUNG ONE UI PICKER) ---
  function switchTopic(topicId) {
    if (!GAME_DATA.topics || !GAME_DATA.topics[topicId]) return;
    STATE.currentTopic = topicId;
    localStorage.setItem('cortex_active_topic', topicId);

    // Load topic progress
    const savedLevels = localStorage.getItem(`cortex_game_levels_${topicId}`);
    STATE.completedLevels = new Set(JSON.parse(savedLevels || '[1]'));
    const savedStars = localStorage.getItem(`cortex_game_stars_${topicId}`);
    STATE.levelStars = JSON.parse(savedStars || '{"1":3}');

    // Update Pills
    if (DOM.topicPills) {
      DOM.topicPills.forEach(pill => {
        const isActive = pill.dataset.topic === topicId;
        pill.classList.toggle('active', isActive);
        pill.setAttribute('aria-selected', isActive ? 'true' : 'false');
      });
    }

    // Update counter
    const topicData = GAME_DATA.topics[topicId];
    if (DOM.topicLevelCounter && topicData) {
      DOM.topicLevelCounter.textContent = `${topicData.levels.length} Levels`;
    }

    // Toggle flowcharts strip visibility (show for MSME or topics with flowcharts)
    const fcStrip = document.getElementById('flowchart-quick-strip');
    if (fcStrip) {
      fcStrip.style.display = (topicId === 'msme' || (topicData.flowcharts && topicData.flowcharts.length > 0)) ? 'block' : 'none';
    }

    renderQuestMap();
  }

  // --- FLOWCHART MODAL CONTROLLER ---
  function openFlowchart(fcId = 'fc-classification') {
    if (!DOM.flowchartModal) return;
    DOM.flowchartModal.classList.add('open');
    showFlowchart(fcId);
  }

  function closeFlowchart() {
    if (DOM.flowchartModal) {
      DOM.flowchartModal.classList.remove('open');
    }
  }

  function showFlowchart(fcId) {
    if (!GAME_DATA.flowcharts) return;
    const fc = GAME_DATA.flowcharts[fcId];
    if (!fc) return;

    if (DOM.flowchartImg) DOM.flowchartImg.src = fc.file;
    if (DOM.flowchartTitle) DOM.flowchartTitle.textContent = fc.title;
    if (DOM.flowchartDesc) DOM.flowchartDesc.textContent = fc.desc;
    if (DOM.flowchartFullscreen) DOM.flowchartFullscreen.href = fc.file;

    if (DOM.flowchartTabs) {
      DOM.flowchartTabs.forEach(tab => {
        tab.classList.toggle('active', tab.dataset.fc === fcId);
      });
    }
  }

  // --- RENDER QUEST MAP (TOPIC-AWARE & LEVEL PATH) ---
  function renderQuestMap() {
    if (!DOM.questPath) return;
    DOM.questPath.innerHTML = '';

    const topic = (GAME_DATA.topics && GAME_DATA.topics[STATE.currentTopic]) ? GAME_DATA.topics[STATE.currentTopic] : (GAME_DATA.topics ? GAME_DATA.topics['msme'] : null);
    if (!topic) return;

    // World Banner for Active Topic
    const banner = document.createElement('div');
    banner.className = `world-header-banner topic-${topic.id}`;
    banner.style.borderLeftColor = topic.color;
    banner.innerHTML = `
      <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.4rem;">
        <span class="world-tag" style="color:${topic.color}; border-color:${topic.color};">${topic.badge}</span>
        <span style="font-size:0.75rem; font-weight:800; color:#cbd5e1; background:rgba(255,255,255,0.08); padding:2px 8px; border-radius:999px;">
          ${topic.levels.length} Quests
        </span>
      </div>
      <h2 class="world-title">${topic.icon} ${topic.title}</h2>
      <p class="world-desc">${topic.description}</p>
    `;
    DOM.questPath.appendChild(banner);

    // Levels in Active Topic
    const pathContainer = document.createElement('div');
    pathContainer.className = 'quest-path-container';

    let currentUnit = '';

    topic.levels.forEach((level) => {
      // Unit Divider Banner if unit changes
      if (level.unit && level.unit !== currentUnit) {
        currentUnit = level.unit;
        const unitDiv = document.createElement('div');
        unitDiv.style.cssText = `margin: 1.5rem 0 0.8rem; padding: 0.5rem 0.85rem; background: rgba(255,255,255,0.04); border-left: 3.5px solid ${level.unitColor || topic.color}; border-radius: 0 10px 10px 0; font-size: 0.74rem; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em; color: ${level.unitColor || topic.color};`;
        unitDiv.textContent = currentUnit;
        pathContainer.appendChild(unitDiv);
      }

      const isCompleted = STATE.completedLevels.has(level.id);
      const isUnlocked = isCompleted || STATE.completedLevels.has(level.id - 1) || level.id === 1;
      const isCurrent = !isCompleted && isUnlocked;
      const stars = STATE.levelStars[level.id] || 0;

      const nodeWrapper = document.createElement('div');
      nodeWrapper.className = 'quest-node-wrapper';

      const btn = document.createElement('button');
      btn.className = `quest-node-btn ${level.isBoss ? 'boss' : ''} ${isCurrent ? 'current' : ''} ${!isUnlocked ? 'locked' : ''}`;
      btn.innerHTML = isUnlocked ? (level.isBoss ? '👑' : (level.icon || '⚔️')) : '🔒';
      btn.disabled = !isUnlocked;
      btn.setAttribute('aria-label', `Level ${level.id}: ${level.title}`);

      btn.addEventListener('click', () => {
        if (isUnlocked) {
          startLevel(level);
        }
      });

      const label = document.createElement('div');
      label.className = 'quest-node-label';
      label.textContent = `Lvl ${level.id}: ${level.title}`;

      const starsEl = document.createElement('div');
      starsEl.className = 'quest-node-stars';
      starsEl.textContent = isCompleted ? '⭐'.repeat(stars) : '';

      nodeWrapper.appendChild(btn);
      nodeWrapper.appendChild(label);
      if (isCompleted) nodeWrapper.appendChild(starsEl);

      pathContainer.appendChild(nodeWrapper);
    });

    DOM.questPath.appendChild(pathContainer);
  }

  // --- START LEVEL SESSION ---
  function startLevel(level) {
    // Unlimited tries - no heart depletion or lockout
    SoundFX.playTap();
    STATE.activeLevel = level;
    STATE.currentQuestionIdx = 0;
    STATE.selectedOption = null;
    STATE.bossCurrentHp = level.bossHp || 1000;

    // Boss UI toggle
    if (level.isBoss) {
      DOM.bossHpContainer.classList.add('visible');
      updateBossHp();
    } else {
      DOM.bossHpContainer.classList.remove('visible');
    }

    renderQuestion();
    DOM.playModal.classList.add('open');
  }

  function updateBossHp() {
    if (!STATE.activeLevel || !STATE.activeLevel.isBoss) return;
    const max = STATE.activeLevel.bossHp || 1000;
    const pct = Math.max(0, (STATE.bossCurrentHp / max) * 100);
    DOM.bossHpFill.style.width = `${pct}%`;
    DOM.bossHpText.textContent = `${STATE.activeLevel.bossName}: ${STATE.bossCurrentHp} / ${max} HP`;
  }

  function formatContent(text) {
    if (!text) return '';
    return text
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/\n\n/g, '<div style="margin-bottom:0.75rem;"></div>')
      .replace(/\n/g, '<br>');
  }

  // --- RENDER ACTIVE TASK / QUESTION (SYNCED WITH DESKTOP) ---
  function renderQuestion() {
    const level = STATE.activeLevel;
    if (!level) return;

    const tasks = level.tasks || level.questions;
    const task = tasks[STATE.currentQuestionIdx];

    // Progress bar update
    const progressPct = ((STATE.currentQuestionIdx) / tasks.length) * 100;
    DOM.playProgressBar.style.width = `${progressPct}%`;

    // Reset feedback and action button
    DOM.feedbackBanner.className = 'feedback-banner';
    DOM.feedbackBanner.style.display = 'none';

    STATE.selectedOption = null;
    STATE.assembledTokens = [];
    STATE.matchedPairsCount = 0;
    STATE.activeMatchPick = null;

    DOM.playQuestionBox.innerHTML = '';

    // TYPE 1: CONCEPT CARD (Desktop Verbatim)
    if (task.type === 'concept') {
      DOM.playActionBtn.textContent = 'CONTINUE (+10 XP)';
      DOM.playActionBtn.disabled = false;

      const fcPreview = task.flowchart ? `
        <div class="concept-flowchart-card" id="task-flowchart-preview-btn">
          <div style="font-size:0.75rem; font-weight:800; color:#38bdf8; display:flex; justify-content:space-between; align-items:center; margin-bottom:6px;">
            <span>📊 Architectural Flowchart</span>
            <span style="background:rgba(59,130,246,0.25); color:#93c5fd; padding:2px 8px; border-radius:6px; font-size:0.72rem;">🔍 Tap to Zoom</span>
          </div>
          <img src="assets/flowcharts/${task.flowchart}" alt="Flowchart Diagram" style="width:100%; max-height:160px; object-fit:contain; border-radius:8px; background:rgba(0,0,0,0.4);" loading="lazy">
        </div>
      ` : '';

      const card = document.createElement('div');
      card.style.cssText = 'background: rgba(255,255,255,0.05); border: 1.5px solid rgba(255,255,255,0.12); border-radius: 18px; padding: 1.25rem; display: flex; flex-direction: column; gap: 0.85rem;';
      card.innerHTML = `
        <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:#10b981; letter-spacing:0.05em;">
          💡 CONCEPT DISCOVERY
        </div>
        <h3 style="font-family:'Outfit', sans-serif; font-size:1.35rem; font-weight:900; color:#fff; line-height:1.25;">
          ${task.title}
        </h3>
        <div style="font-size:0.95rem; line-height:1.6; color:#cbd5e1;">
          ${formatContent(task.content)}
        </div>
        ${fcPreview}
        ${task.keyTakeaway ? `
          <div style="background: rgba(16, 185, 129, 0.15); border-left: 4px solid #10b981; border-radius: 0 10px 10px 0; padding: 0.75rem 1rem; font-size:0.86rem; color:#a7f3d0; line-height:1.45;">
            <strong>Key Takeaway:</strong> ${task.keyTakeaway}
          </div>
        ` : ''}
      `;

      if (task.flowchart) {
        const fcBtn = card.querySelector('#task-flowchart-preview-btn');
        if (fcBtn) {
          fcBtn.addEventListener('click', () => {
            SoundFX.playTap();
            let fcKey = 'fc-classification';
            if (task.flowchart.includes('delayed')) fcKey = 'fc-delayed-payments';
            else if (task.flowchart.includes('vishwakarma')) fcKey = 'fc-pm-vishwakarma';
            else if (task.flowchart.includes('dwarfism')) fcKey = 'fc-dwarfism';
            openFlowchart(fcKey);
          });
        }
      }

      DOM.playQuestionBox.appendChild(card);
      return;
    }

    DOM.playActionBtn.textContent = 'CHECK ANSWER';
    DOM.playActionBtn.disabled = true;

    // Prompt Header
    const promptEl = document.createElement('h3');
    promptEl.className = 'question-prompt';
    promptEl.textContent = task.prompt || task.question;
    DOM.playQuestionBox.appendChild(promptEl);

    // TYPE 2: MCQ (Desktop Verbatim)
    if (task.type === 'mcq') {
      const grid = document.createElement('div');
      grid.className = 'options-grid';
      task.options.forEach((opt, idx) => {
        const card = document.createElement('div');
        card.className = 'option-card';
        card.innerHTML = `<span style="color:#6366f1; font-weight:800;">${['A', 'B', 'C', 'D'][idx]}</span> <span>${opt}</span>`;
        card.addEventListener('click', () => {
          SoundFX.playTap();
          grid.querySelectorAll('.option-card').forEach(c => c.classList.remove('selected'));
          card.classList.add('selected');
          STATE.selectedOption = idx;
          DOM.playActionBtn.disabled = false;
        });
        grid.appendChild(card);
      });
      DOM.playQuestionBox.appendChild(grid);
    } 
    // TYPE 3: TRUE / FALSE (Desktop Verbatim)
    else if (task.type === 'true_false' || task.type === 'swipe') {
      const swipeGrid = document.createElement('div');
      swipeGrid.className = 'blitz-controls';
      swipeGrid.style.marginTop = '2rem';

      const btnFalse = document.createElement('button');
      btnFalse.className = 'btn-blitz-false';
      btnFalse.innerHTML = '✕ FALSE';
      btnFalse.onclick = () => {
        SoundFX.playTap();
        btnFalse.style.outline = '3px solid #fff';
        btnTrue.style.outline = 'none';
        STATE.selectedOption = false;
        DOM.playActionBtn.disabled = false;
      };

      const btnTrue = document.createElement('button');
      btnTrue.className = 'btn-blitz-true';
      btnTrue.innerHTML = '✓ TRUE';
      btnTrue.onclick = () => {
        SoundFX.playTap();
        btnTrue.style.outline = '3px solid #fff';
        btnFalse.style.outline = 'none';
        STATE.selectedOption = true;
        DOM.playActionBtn.disabled = false;
      };

      swipeGrid.appendChild(btnFalse);
      swipeGrid.appendChild(btnTrue);
      DOM.playQuestionBox.appendChild(swipeGrid);
    } 
    // TYPE 4: MATCH PAIRS (Desktop Verbatim)
    else if (task.type === 'match_pairs' || task.type === 'match') {
      const matchGrid = document.createElement('div');
      matchGrid.className = 'match-grid';

      const rawPairs = task.pairs.map((p, idx) => ({
        pairId: idx,
        left: p.left || p.term,
        right: p.right || p.def
      }));

      const tiles = [];
      rawPairs.forEach(p => {
        tiles.push({ text: p.left, pairId: p.pairId, side: 'left' });
        tiles.push({ text: p.right, pairId: p.pairId, side: 'right' });
      });
      tiles.sort(() => Math.random() - 0.5);

      tiles.forEach((t) => {
        const tileEl = document.createElement('div');
        tileEl.className = 'match-tile';
        tileEl.textContent = t.text;
        tileEl.addEventListener('click', () => {
          SoundFX.playTap();
          if (tileEl.classList.contains('matched')) return;

          if (!STATE.activeMatchPick) {
            STATE.activeMatchPick = { element: tileEl, data: t };
            tileEl.classList.add('active-pick');
          } else {
            const first = STATE.activeMatchPick;
            if (first.element === tileEl) {
              tileEl.classList.remove('active-pick');
              STATE.activeMatchPick = null;
              return;
            }

            if (first.data.pairId === t.pairId && first.data.side !== t.side) {
              // Correct Pair Match!
              SoundFX.playCorrect();
              first.element.classList.remove('active-pick');
              first.element.classList.add('matched');
              tileEl.classList.add('matched');
              STATE.matchedPairsCount++;
              STATE.activeMatchPick = null;

              if (STATE.matchedPairsCount === rawPairs.length) {
                DOM.playActionBtn.disabled = false;
                DOM.feedbackBanner.className = 'feedback-banner success';
                DOM.feedbackBanner.innerHTML = '<strong>✨ Perfect Match!</strong> All concepts connected successfully.';
                DOM.feedbackBanner.style.display = 'block';
              }
            } else {
              // Mismatch
              SoundFX.playError();
              first.element.classList.remove('active-pick');
              STATE.activeMatchPick = null;
            }
          }
        });
        matchGrid.appendChild(tileEl);
      });

      DOM.playQuestionBox.appendChild(matchGrid);
    } 
    // TYPE 5: TAP TO ORDER (Desktop Verbatim)
    else if (task.type === 'tap_order') {
      const slot = document.createElement('div');
      slot.className = 'tokens-assembly-slot';
      slot.id = 'tokens-assembly-slot';

      const bank = document.createElement('div');
      bank.className = 'tokens-bank';

      const shuffledTokens = [...task.tokens].sort(() => Math.random() - 0.5);
      shuffledTokens.forEach((token, idx) => {
        const tokenBtn = document.createElement('button');
        tokenBtn.className = 'word-token';
        tokenBtn.textContent = token;
        tokenBtn.dataset.idx = idx;

        tokenBtn.addEventListener('click', () => {
          SoundFX.playTap();
          tokenBtn.classList.add('placed');
          STATE.assembledTokens.push({ text: token, element: tokenBtn });

          const placedPill = document.createElement('button');
          placedPill.className = 'word-token';
          placedPill.textContent = token;
          placedPill.onclick = () => {
            SoundFX.playTap();
            tokenBtn.classList.remove('placed');
            STATE.assembledTokens = STATE.assembledTokens.filter(t => t.element !== tokenBtn);
            placedPill.remove();
            DOM.playActionBtn.disabled = STATE.assembledTokens.length !== task.tokens.length;
          };
          slot.appendChild(placedPill);

          if (STATE.assembledTokens.length === task.tokens.length) {
            DOM.playActionBtn.disabled = false;
          }
        });
        bank.appendChild(tokenBtn);
      });

      DOM.playQuestionBox.appendChild(slot);
      DOM.playQuestionBox.appendChild(bank);
    }
  }

  // --- CHECK ANSWER HANDLER ---
  function handleCheckAnswer() {
    const level = STATE.activeLevel;
    const tasks = level.tasks || level.questions;
    const task = tasks[STATE.currentQuestionIdx];

    // If in 'Continue' state, advance to next question
    if (DOM.playActionBtn.textContent.startsWith('CONTINUE')) {
      SoundFX.playTap();
      STATE.currentQuestionIdx++;
      if (STATE.currentQuestionIdx < tasks.length) {
        renderQuestion();
      } else {
        finishLevel();
      }
      return;
    }

    let isCorrect = false;

    if (task.type === 'mcq') {
      isCorrect = STATE.selectedOption === task.correctIndex;
    } else if (task.type === 'true_false' || task.type === 'swipe') {
      isCorrect = STATE.selectedOption === (task.correct !== undefined ? task.correct : task.isTrue);
    } else if (task.type === 'match_pairs' || task.type === 'match') {
      isCorrect = STATE.matchedPairsCount === task.pairs.length;
    } else if (task.type === 'tap_order') {
      const userString = STATE.assembledTokens.map(t => t.text).join(' ').trim();
      const targetString = (task.correctSentence || (task.correctOrder ? task.correctOrder.join(' ') : task.tokens.join(' '))).trim();
      isCorrect = userString === targetString;
    }

    if (isCorrect) {
      SoundFX.playCorrect();
      if (level.isBoss) {
        SoundFX.playBossHit();
        STATE.bossCurrentHp = Math.max(0, STATE.bossCurrentHp - 250);
        updateBossHp();
      }
      DOM.feedbackBanner.className = 'feedback-banner success';
      DOM.feedbackBanner.innerHTML = `
        <div style="font-weight:900; margin-bottom:4px;">✨ BRILLIANT! +25 XP</div>
        <div>${task.explanation || 'Spot on conceptual clarity!'}</div>
      `;
    } else {
      SoundFX.playError();
      // Unlimited tries! No heart loss!
      DOM.feedbackBanner.className = 'feedback-banner error';
      DOM.feedbackBanner.innerHTML = `
        <div style="font-weight:900; margin-bottom:4px; color:#f87171;">💡 NOT QUITE • Unlimited Tries</div>
        <div>${task.explanation || 'Review the core concept carefully!'}</div>
      `;
    }

    renderMobileQuestionFeedback(task, isCorrect, DOM.feedbackBanner);

    DOM.feedbackBanner.style.display = 'block';
    DOM.playActionBtn.textContent = 'CONTINUE';
    DOM.playActionBtn.disabled = false;
  }

  // --- QUESTION FEEDBACK WIDGET (MOBILE) ---
  function renderMobileQuestionFeedback(task, isCorrect, banner) {
    const topicId = STATE.currentTopic || 'msme';
    const levelId = STATE.activeLevel ? STATE.activeLevel.id : 1;
    const qId = `${topicId}_lvl-${levelId}_q${STATE.currentQuestionIdx}`;

    let existing = null;
    try {
      const list = JSON.parse(localStorage.getItem('cortex_question_feedback') || '[]');
      existing = list.find(x => x.id === qId);
    } catch(e) {}

    const fbWrap = document.createElement('div');
    fbWrap.className = 'mobile-q-fb-wrap';
    fbWrap.innerHTML = `
      <div class="mobile-q-fb-title">
        <span>Rate Question:</span>
        <span class="mobile-q-fb-saved" style="color:#10b981; font-weight:800; font-size:0.75rem; ${existing ? 'display:inline;' : 'display:none;'}">✓ Saved (${existing ? existing.rating : ''})</span>
      </div>
      <div class="mobile-q-fb-chips">
        <button type="button" class="mobile-q-fb-chip ${existing && existing.rating === 'Helpful' ? 'selected' : ''}" data-rating="Helpful">👍 Helpful</button>
        <button type="button" class="mobile-q-fb-chip ${existing && existing.rating === 'Clear' ? 'selected' : ''}" data-rating="Clear">💡 Clear</button>
        <button type="button" class="mobile-q-fb-chip ${existing && existing.rating === 'Confusing' ? 'selected' : ''}" data-rating="Confusing">🤔 Confusing</button>
        <button type="button" class="mobile-q-fb-chip ${existing && existing.rating === 'Issue' ? 'selected' : ''}" data-rating="Issue">⚠️ Typo</button>
      </div>
      <div class="mobile-q-fb-input-row">
        <input type="text" class="mobile-q-fb-input" placeholder="Optional note for AI..." value="${existing && existing.note ? existing.note.replace(/"/g, '&quot;') : ''}" maxlength="120" />
        <button type="button" class="mobile-q-fb-btn">Save</button>
      </div>
    `;

    banner.appendChild(fbWrap);

    const chips = fbWrap.querySelectorAll('.mobile-q-fb-chip');
    const input = fbWrap.querySelector('.mobile-q-fb-input');
    const btn = fbWrap.querySelector('.mobile-q-fb-btn');
    const savedTag = fbWrap.querySelector('.mobile-q-fb-saved');

    function save(ratingOverride) {
      const activeChip = fbWrap.querySelector('.mobile-q-fb-chip.selected');
      const rating = ratingOverride || (activeChip ? activeChip.dataset.rating : 'Helpful');
      const note = input ? input.value.trim() : '';

      try {
        const list = JSON.parse(localStorage.getItem('cortex_question_feedback') || '[]');
        const item = {
          id: qId,
          topic: topicId,
          levelId: `lvl-${levelId}`,
          levelNumber: levelId,
          levelTitle: STATE.activeLevel ? STATE.activeLevel.title : '',
          taskIndex: STATE.currentQuestionIdx,
          prompt: task.prompt || task.title || (task.tokens ? task.tokens.join(' ') : 'Question'),
          rating: rating,
          note: note,
          isCorrect: isCorrect,
          timestamp: new Date().toISOString()
        };
        const idx = list.findIndex(x => x.id === qId);
        if (idx >= 0) list[idx] = item;
        else list.push(item);
        localStorage.setItem('cortex_question_feedback', JSON.stringify(list));
        if (savedTag) {
          savedTag.textContent = `✓ Saved (${rating})`;
          savedTag.style.display = 'inline';
        }
      } catch(e) {}
    }

    chips.forEach(chip => {
      chip.addEventListener('click', (e) => {
        e.stopPropagation();
        chips.forEach(c => c.classList.remove('selected'));
        chip.classList.add('selected');
        save(chip.dataset.rating);
      });
    });

    if (btn) {
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        save();
      });
    }

    if (input) {
      input.addEventListener('keydown', (e) => {
        e.stopPropagation();
        if (e.key === 'Enter') save();
      });
    }
  }

  // --- BUILD LESSON STARS & AI FEEDBACK HTML (MOBILE) ---
  function buildMobileLessonStarsHtml(topicId) {
    const topic = GAME_DATA.topics[topicId];
    const levels = (topic && topic.levels) ? topic.levels : [];
    
    let allQ = [];
    try {
      allQ = JSON.parse(localStorage.getItem('cortex_question_feedback') || '[]').filter(x => x.topic === topicId);
    } catch(e) {}

    let existingCourseFb = null;
    try {
      existingCourseFb = JSON.parse(localStorage.getItem(`cortex_course_feedback_${topicId}`) || 'null');
    } catch(e) {}

    const currentRating = (existingCourseFb && existingCourseFb.rating) || 5;
    const currentComment = (existingCourseFb && existingCourseFb.comment) || '';

    let itemsHtml = '';
    let totalStars = 0;
    levels.forEach(lvl => {
      const isDone = STATE.completedLevels.has(lvl.id);
      const stars = STATE.levelStars[lvl.id] || (isDone ? 3 : 0);
      totalStars += stars;
      const starsDisplay = stars > 0 ? '⭐'.repeat(stars) : '<span style="color:#64748b;">—</span>';
      const qNotesCount = allQ.filter(q => q.levelNumber === lvl.id || q.levelId === `lvl-${lvl.id}`).length;
      const notesBadge = qNotesCount > 0 ? `<span style="font-size:0.7rem; color:#38bdf8; background:rgba(56,189,248,0.15); padding:2px 5px; border-radius:4px; margin-left:4px;">📝${qNotesCount}</span>` : '';

      itemsHtml += `
        <div class="mobile-star-item">
          <div class="mobile-star-item-info">
            <span class="mobile-star-num">L${lvl.id}</span>
            <div style="text-align:left;">
              <div class="mobile-star-title">${lvl.title}</div>
              <div style="font-size:0.72rem; color:${isDone ? '#34d399' : '#94a3b8'};">
                ${isDone ? '✓ Mastered' : '🔒 In Progress'}${notesBadge}
              </div>
            </div>
          </div>
          <div class="mobile-star-display">${starsDisplay}</div>
        </div>
      `;
    });

    return `
      <div style="margin-top:0.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.6rem;">
          <h4 style="font-family:'Outfit'; font-size:1rem; font-weight:800; color:#facc15; margin:0;">
            🌟 All Lessons Stars
          </h4>
          <span style="font-size:0.8rem; font-weight:800; color:#38bdf8;">
            ${totalStars} / ${levels.length * 3} ⭐
          </span>
        </div>

        <div class="mobile-stars-list">
          ${itemsHtml}
        </div>

        <!-- AI Feedback Box -->
        <div class="mobile-ai-box" style="margin-top:1rem;">
          <div style="font-size:0.9rem; font-weight:800; color:var(--game-text); text-align:center;">
            💬 Feedback for the AI / Developer
          </div>
          <p style="font-size:0.75rem; color:var(--game-text-dim); text-align:center; margin:0;">
            Rate this topic and share suggestions. Click "Copy for AI" to paste into our conversation!
          </p>

          <div class="mobile-star-picker" id="mobile-star-picker">
            ${[1, 2, 3, 4, 5].map(n => `
              <button type="button" class="mobile-star-btn ${n <= currentRating ? 'active' : ''}" data-val="${n}">⭐</button>
            `).join('')}
          </div>

          <div style="display:flex; flex-wrap:wrap; gap:0.35rem; justify-content:center;">
            <button type="button" class="quick-fb-tag mobile-quick-tag" data-tag="High UPSC Yield">🎯 High Yield</button>
            <button type="button" class="quick-fb-tag mobile-quick-tag" data-tag="Great Explanations">🔍 Explanations</button>
            <button type="button" class="quick-fb-tag mobile-quick-tag" data-tag="Helpful Flowcharts">📊 Flowcharts</button>
            <button type="button" class="quick-fb-tag mobile-quick-tag" data-tag="Good Pacing">⏱️ Pacing</button>
          </div>

          <textarea class="mobile-textarea" id="mobile-feedback-text" rows="3" placeholder="Share your suggestions, question feedback, or next topics...">${currentComment}</textarea>

          <button type="button" class="btn-mobile-copy-ai" id="btn-mobile-copy-report">
            <span>📋</span> Copy Feedback Report for AI
          </button>
        </div>
      </div>
    `;
  }

  function wireMobileFeedbackEvents(container, topicId) {
    if (!container) return;
    const topic = GAME_DATA.topics[topicId];
    let selectedRating = 5;
    try {
      const fb = JSON.parse(localStorage.getItem(`cortex_course_feedback_${topicId}`) || 'null');
      if (fb && fb.rating) selectedRating = fb.rating;
    } catch(e) {}

    const starBtns = container.querySelectorAll('.mobile-star-btn');
    const textarea = container.querySelector('#mobile-feedback-text');
    const copyBtn = container.querySelector('#btn-mobile-copy-report');
    const quickTags = container.querySelectorAll('.mobile-quick-tag');

    function saveFeedback() {
      const comment = textarea ? textarea.value.trim() : '';
      const payload = {
        topic: topicId,
        rating: selectedRating,
        comment: comment,
        savedAt: new Date().toISOString()
      };
      localStorage.setItem(`cortex_course_feedback_${topicId}`, JSON.stringify(payload));
    }

    starBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const val = parseInt(btn.dataset.val, 10);
        selectedRating = val;
        starBtns.forEach(b => {
          const bVal = parseInt(b.dataset.val, 10);
          b.classList.toggle('active', bVal <= val);
        });
        saveFeedback();
      });
    });

    quickTags.forEach(tag => {
      tag.addEventListener('click', () => {
        if (!textarea) return;
        const text = tag.dataset.tag;
        if (textarea.value.includes(text)) return;
        textarea.value = textarea.value ? `${textarea.value}; ${text}` : text;
        saveFeedback();
      });
    });

    if (textarea) {
      textarea.addEventListener('input', saveFeedback);
    }

    if (copyBtn) {
      copyBtn.addEventListener('click', () => {
        saveFeedback();
        const md = generateMobileFeedbackReport(topicId, topic, selectedRating, textarea ? textarea.value : '');
        copyMobileTextToClipboard(md, copyBtn);
      });
    }
  }

  function generateMobileFeedbackReport(topicId, topic, rating, comment) {
    const levels = (topic && topic.levels) ? topic.levels : [];
    let allQ = [];
    try {
      allQ = JSON.parse(localStorage.getItem('cortex_question_feedback') || '[]').filter(x => x.topic === topicId);
    } catch(e) {}

    let md = `# 🎓 UPSC Cortex Mobile - Lesson Stars & Feedback Report\n\n`;
    md += `**Topic**: ${topic ? topic.name : topicId}\n`;
    md += `**Date**: ${new Date().toLocaleDateString()} ${new Date().toLocaleTimeString()}\n`;
    md += `**Overall Course Rating**: ${'⭐'.repeat(rating || 5)} (${rating || 5}/5)\n\n`;

    md += `### 🌟 Lesson-Wise Stars Summary\n`;
    md += `| Level | Title | Stars Earned | Status | Notes |\n`;
    md += `| :---: | :--- | :---: | :---: | :---: |\n`;

    let totalStars = 0;
    levels.forEach(lvl => {
      const isDone = STATE.completedLevels.has(lvl.id);
      const stars = STATE.levelStars[lvl.id] || (isDone ? 3 : 0);
      totalStars += stars;
      const starsDisplay = stars > 0 ? '⭐'.repeat(stars) : '—';
      const statusDisplay = isDone ? '✓ Mastered' : '🔒 In Progress';
      const qNotesCount = allQ.filter(q => q.levelNumber === lvl.id || q.levelId === `lvl-${lvl.id}`).length;
      const notesBadge = qNotesCount > 0 ? `📝 ${qNotesCount}` : '—';
      md += `| Level ${lvl.id} | ${lvl.title} | ${starsDisplay} | ${statusDisplay} | ${notesBadge} |\n`;
    });
    md += `\n**Total Stars Earned**: ${totalStars} / ${levels.length * 3} ⭐\n\n`;

    if (allQ.length > 0) {
      md += `### 📝 Question-Specific Feedback (${allQ.length} Logged)\n`;
      allQ.forEach((q, i) => {
        const ratingIcon = q.rating === 'Helpful' ? '👍' : q.rating === 'Clear' ? '💡' : q.rating === 'Confusing' ? '🤔' : '⚠️';
        md += `${i + 1}. **[${q.levelTitle || ('Level ' + q.levelNumber)}] Q${(q.taskIndex || 0) + 1}**: ${ratingIcon} *${q.rating}*\n`;
        md += `   - **Prompt**: "${(q.prompt || '').substring(0, 80)}..."\n`;
        if (q.note) md += `   - **Note**: "${q.note}"\n`;
      });
      md += `\n`;
    }

    md += `### 💬 User Review & Suggestions for AI\n`;
    md += `> ${comment && comment.trim() ? comment.trim().replace(/\n/g, '\n> ') : 'No additional text comments provided.'}\n\n`;
    md += `---\n*Generated by Cortex Mobile Gamified Engine (Unlimited Tries & Feedback System)*\n`;
    return md;
  }

  function copyMobileTextToClipboard(text, triggerBtn) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(text).then(() => {
        showMobileCopyToast(triggerBtn);
      }).catch(() => {
        fallbackMobileCopy(text, triggerBtn);
      });
    } else {
      fallbackMobileCopy(text, triggerBtn);
    }
  }

  function fallbackMobileCopy(text, triggerBtn) {
    const ta = document.createElement('textarea');
    ta.value = text;
    ta.style.position = 'fixed';
    ta.style.opacity = '0';
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand('copy');
      showMobileCopyToast(triggerBtn);
    } catch(e) {
      alert('Copy failed, please copy manually.');
    }
    document.body.removeChild(ta);
  }

  function showMobileCopyToast(triggerBtn) {
    if (triggerBtn) {
      const orig = triggerBtn.innerHTML;
      triggerBtn.innerHTML = '✓ Copied to Clipboard!';
      triggerBtn.style.background = '#10b981';
      setTimeout(() => {
        triggerBtn.innerHTML = orig;
        triggerBtn.style.background = '';
      }, 2500);
    }
    alert('📋 Feedback report copied to clipboard!\n\nYou can now paste it into the chat to share your feedback with me.');
  }

  function openMobileStarsFeedbackModal() {
    SoundFX.playTap();
    if (!DOM.starsFeedbackModal || !DOM.starsModalBody) return;
    const topic = GAME_DATA.topics[STATE.currentTopic];
    if (DOM.starsModalTopicTitle) {
      DOM.starsModalTopicTitle.textContent = `${topic ? topic.name : 'Topic'} Stars`;
    }
    DOM.starsModalBody.innerHTML = buildMobileLessonStarsHtml(STATE.currentTopic);
    wireMobileFeedbackEvents(DOM.starsModalBody, STATE.currentTopic);
    DOM.starsFeedbackModal.classList.add('open');
  }

  // --- FINISH LEVEL (VICTORY SCREEN WITH LESSON STARS MATRIX) ---
  function finishLevel() {
    const level = STATE.activeLevel;
    SoundFX.playVictory();
    Confetti.launch();

    // Rewards
    STATE.completedLevels.add(level.id);
    STATE.levelStars[level.id] = 3;
    STATE.gems += 20;
    STATE.coins += level.coinsReward || 100;
    saveState();

    DOM.playProgressBar.style.width = '100%';
    const starsHtml = buildMobileLessonStarsHtml(STATE.currentTopic);

    DOM.playQuestionBox.innerHTML = `
      <div style="text-align: center; padding: 1.5rem 0; animation: screenFadeIn 0.4s ease;">
        <div style="font-size: 4rem; margin-bottom: 0.5rem;">🏆</div>
        <h2 style="font-family:'Outfit'; font-size: 1.8rem; font-weight: 900; color: #facc15; margin-bottom: 0.25rem;">
          LEVEL COMPLETE!
        </h2>
        <p style="color: #cbd5e1; font-size: 0.92rem; margin-bottom: 1.25rem;">
          You mastered: <strong>${level.title}</strong>
        </p>

        <div style="display:flex; justify-content:center; gap:1rem; margin-bottom: 1.5rem;">
          <div style="background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:0.8rem 1.2rem;">
            <div style="font-size:1.6rem; color:#facc15;">⭐ ⭐ ⭐</div>
            <div style="font-size:0.75rem; font-weight:800; color:#94a3b8; text-transform:uppercase;">Mastery</div>
          </div>
          <div style="background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:0.8rem 1.2rem;">
            <div style="font-size:1.4rem; font-weight:900; color:#38bdf8;">+${level.xpReward || 50} XP</div>
            <div style="font-size:0.75rem; font-weight:800; color:#94a3b8; text-transform:uppercase;">Reward</div>
          </div>
        </div>

        ${level.badgeUnlock ? `
          <div style="background: linear-gradient(135deg, rgba(234, 179, 8, 0.2), rgba(249, 115, 22, 0.2)); border:1.5px solid #facc15; border-radius:14px; padding:0.85rem; margin-bottom:1.5rem;">
            <div style="font-size:0.75rem; font-weight:900; text-transform:uppercase; color:#facc15;">🎖️ New Title Unlocked!</div>
            <div style="font-size:1.05rem; font-weight:900; color:#fff;">${level.badgeUnlock}</div>
          </div>
        ` : ''}

        <!-- Lesson-Wise Stars & Course Feedback -->
        <div id="finish-stars-container" style="text-align:left;">
          ${starsHtml}
        </div>
      </div>
    `;

    wireMobileFeedbackEvents(document.getElementById('finish-stars-container'), STATE.currentTopic);

    DOM.feedbackBanner.style.display = 'none';
    DOM.playActionBtn.textContent = 'BACK TO QUEST MAP';
    DOM.playActionBtn.onclick = () => {
      DOM.playModal.classList.remove('open');
      renderQuestMap();
      DOM.playActionBtn.onclick = handleCheckAnswer;
    };
  }

  // --- BLITZ RAPID-FIRE ENGINE ---
  function startBlitzGame() {
    STATE.blitzTimer = 60;
    STATE.blitzScore = 0;
    STATE.blitzCombo = 1;
    STATE.blitzIndex = 0;
    updateBlitzUI();

    clearInterval(STATE.blitzInterval);
    STATE.blitzInterval = setInterval(() => {
      STATE.blitzTimer--;
      if (DOM.blitzTimer) DOM.blitzTimer.textContent = STATE.blitzTimer;
      if (STATE.blitzTimer <= 0) {
        endBlitzGame();
      }
    }, 1000);
  }

  function updateBlitzUI() {
    const qList = GAME_DATA.blitzQuestions;
    const curr = qList[STATE.blitzIndex % qList.length];
    if (DOM.blitzCardText) DOM.blitzCardText.textContent = curr.q;
    if (DOM.blitzCombo) DOM.blitzCombo.textContent = `🔥 ${STATE.blitzCombo}X STREAK COMBO`;
    if (DOM.blitzTimer) DOM.blitzTimer.textContent = STATE.blitzTimer;
  }

  function answerBlitz(userChoice) {
    const qList = GAME_DATA.blitzQuestions;
    const curr = qList[STATE.blitzIndex % qList.length];

    if (userChoice === curr.ans) {
      SoundFX.playCorrect();
      STATE.blitzScore += 50 * STATE.blitzCombo;
      STATE.blitzCombo = Math.min(5, STATE.blitzCombo + 1);
    } else {
      SoundFX.playError();
      STATE.blitzCombo = 1;
    }

    STATE.blitzIndex++;
    updateBlitzUI();
  }

  function endBlitzGame() {
    clearInterval(STATE.blitzInterval);
    SoundFX.playVictory();
    Confetti.launch();
    STATE.coins += STATE.blitzScore;
    saveState();

    if (DOM.blitzCardText) {
      DOM.blitzCardText.innerHTML = `
        <div style="font-size:2rem; margin-bottom:0.5rem;">⚡ BLITZ OVER!</div>
        <div style="font-size:1.4rem; color:#facc15; font-weight:900;">Score: ${STATE.blitzScore} Pts</div>
        <div style="font-size:0.9rem; color:#a7f3d0; margin-top:0.5rem;">+${STATE.blitzScore} Coins Earned!</div>
      `;
    }
  }

  // --- RENDER LEADERBOARD ---
  function renderLeaderboard() {
    if (!DOM.leaderboardList) return;
    DOM.leaderboardList.innerHTML = '';

    GAME_DATA.leaderboard.forEach(entry => {
      const row = document.createElement('div');
      row.className = `leader-row ${entry.isUser ? 'is-user' : ''}`;
      row.innerHTML = `
        <div class="leader-rank">${entry.rank === 1 ? '🥇' : entry.rank === 2 ? '🥈' : entry.rank === 3 ? '🥉' : entry.rank}</div>
        <div class="leader-info">
          <span style="font-size:1.4rem;">${entry.avatar}</span>
          <span class="leader-name">${entry.name}</span>
        </div>
        <div class="leader-xp">${entry.score} XP</div>
      `;
      DOM.leaderboardList.appendChild(row);
    });
  }

  // --- RENDER SHOP ---
  function renderShop() {
    if (!DOM.shopGrid) return;
    DOM.shopGrid.innerHTML = '';

    GAME_DATA.shopItems.forEach(item => {
      const card = document.createElement('div');
      card.className = 'shop-card';
      card.innerHTML = `
        <div style="display:flex; align-items:center; gap:0.85rem;">
          <span style="font-size:2.2rem;">${item.icon}</span>
          <div>
            <div style="font-size:0.96rem; font-weight:800; color:#fff;">${item.name}</div>
            <div style="font-size:0.78rem; color:#94a3b8; line-height:1.3;">${item.desc}</div>
          </div>
        </div>
        <button class="shop-item-btn" data-id="${item.id}">
          ${item.currency === 'gems' ? '💎' : '🪙'} ${item.price}
        </button>
      `;

      const btn = card.querySelector('.shop-item-btn');
      btn.addEventListener('click', () => {
        SoundFX.playTap();
        buyShopItem(item);
      });

      DOM.shopGrid.appendChild(card);
    });
  }

  function buyShopItem(item) {
    if (item.currency === 'gems') {
      if (STATE.gems < item.price) {
        alert('💎 Not enough Gems! Complete more levels to earn gems.');
        return;
      }
      STATE.gems -= item.price;
    } else {
      if (STATE.coins < item.price) {
        alert('🪙 Not enough Coins! Play Blitz Mode to earn coins.');
        return;
      }
      STATE.coins -= item.price;
    }

    if (item.id === 'heart-refill') {
      STATE.hearts = 'unlimited';
    }

    SoundFX.playCorrect();
    saveState();
    alert(`🎉 Purchased ${item.name}! Unlimited Tries are Active.`);
  }

  // --- INITIALIZATION ---
  function init() {
    applySamsungTheme(STATE.theme);
    Confetti.init();
    updateHUD();
    renderLeaderboard();
    renderShop();

    // Initialize Active Topic & Quest Map
    switchTopic(STATE.currentTopic);

    // Topic Switcher Event Listeners
    if (DOM.topicPills) {
      DOM.topicPills.forEach(pill => {
        pill.addEventListener('click', () => {
          const topicId = pill.dataset.topic;
          if (topicId) switchTopic(topicId);
        });
      });
    }

    // Stars & AI Feedback Modal Event Listeners
    if (DOM.btnOpenStarsFeedback) {
      DOM.btnOpenStarsFeedback.addEventListener('click', () => {
        openMobileStarsFeedbackModal();
      });
    }

    if (DOM.starsModalCloseBtn) {
      DOM.starsModalCloseBtn.addEventListener('click', () => {
        SoundFX.playTap();
        if (DOM.starsFeedbackModal) DOM.starsFeedbackModal.classList.remove('open');
      });
    }

    if (DOM.starsFeedbackModal) {
      DOM.starsFeedbackModal.addEventListener('click', (e) => {
        if (e.target === DOM.starsFeedbackModal) {
          DOM.starsFeedbackModal.classList.remove('open');
        }
      });
    }

    // Flowchart Modal Event Listeners
    if (DOM.btnOpenFlowcharts) {
      DOM.btnOpenFlowcharts.addEventListener('click', () => {
        SoundFX.playTap();
        openFlowchart('fc-classification');
      });
    }

    if (DOM.flowchartCloseBtn) {
      DOM.flowchartCloseBtn.addEventListener('click', () => {
        SoundFX.playTap();
        closeFlowchart();
      });
    }

    if (DOM.flowchartTabs) {
      DOM.flowchartTabs.forEach(tab => {
        tab.addEventListener('click', () => {
          SoundFX.playTap();
          const fcId = tab.dataset.fc;
          if (fcId) showFlowchart(fcId);
        });
      });
    }

    // Theme Switcher Event
    if (DOM.themeToggleBtn) {
      DOM.themeToggleBtn.addEventListener('click', toggleSamsungTheme);
    }

    // Dock Navigation Events
    DOM.dockBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const tab = btn.dataset.tab;
        if (tab) switchTab(tab);
      });
    });

    // Play Modal Events
    if (DOM.playCloseBtn) {
      DOM.playCloseBtn.addEventListener('click', () => {
        SoundFX.playTap();
        DOM.playModal.classList.remove('open');
      });
    }

    if (DOM.playActionBtn) {
      DOM.playActionBtn.addEventListener('click', handleCheckAnswer);
    }

    // Blitz Buttons
    if (DOM.btnBlitzTrue) {
      DOM.btnBlitzTrue.addEventListener('click', () => answerBlitz(true));
    }
    if (DOM.btnBlitzFalse) {
      DOM.btnBlitzFalse.addEventListener('click', () => answerBlitz(false));
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})();
