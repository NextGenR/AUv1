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

  // --- GAME STATE ---
  const STATE = {
    hearts: parseInt(localStorage.getItem('cortex_game_hearts') || '5', 10),
    gems: parseInt(localStorage.getItem('cortex_game_gems') || '450', 10),
    coins: parseInt(localStorage.getItem('cortex_game_coins') || '1280', 10),
    streak: parseInt(localStorage.getItem('cortex_game_streak') || '18', 10),
    completedLevels: new Set(JSON.parse(localStorage.getItem('cortex_game_levels') || '[1]')),
    levelStars: JSON.parse(localStorage.getItem('cortex_game_stars') || '{"1":3}'),
    activeTab: 'map',

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
    localStorage.setItem('cortex_game_hearts', STATE.hearts);
    localStorage.setItem('cortex_game_gems', STATE.gems);
    localStorage.setItem('cortex_game_coins', STATE.coins);
    localStorage.setItem('cortex_game_streak', STATE.streak);
    localStorage.setItem('cortex_game_levels', JSON.stringify(Array.from(STATE.completedLevels)));
    localStorage.setItem('cortex_game_stars', JSON.stringify(STATE.levelStars));
    updateHUD();
  }

  // --- DOM ELEMENTS ---
  const DOM = {
    hudStreak: document.getElementById('hud-streak-count'),
    hudGems: document.getElementById('hud-gems-count'),
    hudCoins: document.getElementById('hud-coins-count'),
    hudHearts: document.getElementById('hud-hearts-count'),
    hudHeartsPill: document.getElementById('hud-hearts-pill'),
    screens: document.querySelectorAll('.game-screen'),
    dockBtns: document.querySelectorAll('.dock-btn'),
    questPath: document.getElementById('quest-path-content'),
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

  // --- UPDATE TOP HUD ---
  function updateHUD() {
    if (DOM.hudStreak) DOM.hudStreak.textContent = STATE.streak;
    if (DOM.hudGems) DOM.hudGems.textContent = STATE.gems;
    if (DOM.hudCoins) DOM.hudCoins.textContent = STATE.coins.toLocaleString();
    if (DOM.hudHearts) DOM.hudHearts.textContent = `${STATE.hearts}/5`;
    if (DOM.hudHeartsPill) {
      DOM.hudHeartsPill.classList.toggle('low-hearts', STATE.hearts <= 1);
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

  // --- RENDER QUEST MAP ---
  function renderQuestMap() {
    if (!DOM.questPath) return;
    DOM.questPath.innerHTML = '';

    GAME_DATA.worlds.forEach((world, wIdx) => {
      // World Banner
      const banner = document.createElement('div');
      banner.className = `world-header-banner ${wIdx === 1 ? 'world-2' : ''}`;
      banner.innerHTML = `
        <span class="world-tag">${world.badge}</span>
        <h2 class="world-title">${world.name}</h2>
        <p class="world-desc">${world.description}</p>
      `;
      DOM.questPath.appendChild(banner);

      // Levels in World
      const pathContainer = document.createElement('div');
      pathContainer.className = 'quest-path-container';

      world.levels.forEach((level) => {
        const isCompleted = STATE.completedLevels.has(level.id);
        const isUnlocked = isCompleted || STATE.completedLevels.has(level.id - 1) || level.id === 1;
        const isCurrent = !isCompleted && isUnlocked;
        const stars = STATE.levelStars[level.id] || 0;

        const nodeWrapper = document.createElement('div');
        nodeWrapper.className = 'quest-node-wrapper';

        const btn = document.createElement('button');
        btn.className = `quest-node-btn ${level.isBoss ? 'boss' : ''} ${isCurrent ? 'current' : ''} ${!isUnlocked ? 'locked' : ''}`;
        btn.innerHTML = isUnlocked ? (level.isBoss ? '👑' : level.icon) : '🔒';
        btn.disabled = !isUnlocked;

        btn.addEventListener('click', () => {
          if (isUnlocked) {
            startLevel(level);
          }
        });

        const label = document.createElement('div');
        label.className = 'quest-node-label';
        label.textContent = level.title;

        const starsEl = document.createElement('div');
        starsEl.className = 'quest-node-stars';
        starsEl.textContent = isCompleted ? '⭐'.repeat(stars) : '';

        nodeWrapper.appendChild(btn);
        nodeWrapper.appendChild(label);
        if (isCompleted) nodeWrapper.appendChild(starsEl);

        pathContainer.appendChild(nodeWrapper);
      });

      DOM.questPath.appendChild(pathContainer);
    });
  }

  // --- START LEVEL SESSION ---
  function startLevel(level) {
    if (STATE.hearts <= 0) {
      alert('❤️ Out of Lives! Refill hearts in the Shop to keep playing.');
      switchTab('shop');
      return;
    }

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

  // --- RENDER ACTIVE QUESTION ---
  function renderQuestion() {
    const level = STATE.activeLevel;
    if (!level) return;

    const questions = level.questions;
    const q = questions[STATE.currentQuestionIdx];

    // Progress bar update
    const progressPct = ((STATE.currentQuestionIdx) / questions.length) * 100;
    DOM.playProgressBar.style.width = `${progressPct}%`;

    // Reset feedback and action button
    DOM.feedbackBanner.className = 'feedback-banner';
    DOM.feedbackBanner.style.display = 'none';
    DOM.playActionBtn.textContent = 'CHECK ANSWER';
    DOM.playActionBtn.disabled = true;

    STATE.selectedOption = null;
    STATE.assembledTokens = [];
    STATE.matchedPairsCount = 0;
    STATE.activeMatchPick = null;

    DOM.playQuestionBox.innerHTML = '';

    // Prompt Header
    const promptEl = document.createElement('h3');
    promptEl.className = 'question-prompt';
    promptEl.textContent = q.prompt;
    DOM.playQuestionBox.appendChild(promptEl);

    // Render by Question Type
    if (q.type === 'mcq') {
      const grid = document.createElement('div');
      grid.className = 'options-grid';
      q.options.forEach((opt, idx) => {
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
    } else if (q.type === 'swipe') {
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
    } else if (q.type === 'match') {
      const matchGrid = document.createElement('div');
      matchGrid.className = 'match-grid';

      // Flatten and shuffle pairs
      const tiles = [];
      q.pairs.forEach((p, idx) => {
        tiles.push({ text: p.term, pairId: idx, side: 'term' });
        tiles.push({ text: p.def, pairId: idx, side: 'def' });
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

              if (STATE.matchedPairsCount === q.pairs.length) {
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
    } else if (q.type === 'tap_order') {
      const slot = document.createElement('div');
      slot.className = 'tokens-assembly-slot';
      slot.id = 'tokens-assembly-slot';

      const bank = document.createElement('div');
      bank.className = 'tokens-bank';

      const shuffledTokens = [...q.tokens].sort(() => Math.random() - 0.5);
      shuffledTokens.forEach((token, idx) => {
        const tokenBtn = document.createElement('button');
        tokenBtn.className = 'word-token';
        tokenBtn.textContent = token;
        tokenBtn.dataset.idx = idx;

        tokenBtn.addEventListener('click', () => {
          SoundFX.playTap();
          tokenBtn.classList.add('placed');
          STATE.assembledTokens.push({ text: token, element: tokenBtn });

          // Render into slot
          const placedPill = document.createElement('button');
          placedPill.className = 'word-token';
          placedPill.textContent = token;
          placedPill.onclick = () => {
            SoundFX.playTap();
            tokenBtn.classList.remove('placed');
            STATE.assembledTokens = STATE.assembledTokens.filter(t => t.element !== tokenBtn);
            placedPill.remove();
            DOM.playActionBtn.disabled = STATE.assembledTokens.length !== q.tokens.length;
          };
          slot.appendChild(placedPill);

          if (STATE.assembledTokens.length === q.tokens.length) {
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
    const q = level.questions[STATE.currentQuestionIdx];

    // If already in 'Continue' state, advance to next question
    if (DOM.playActionBtn.textContent === 'CONTINUE') {
      SoundFX.playTap();
      STATE.currentQuestionIdx++;
      if (STATE.currentQuestionIdx < level.questions.length) {
        renderQuestion();
      } else {
        finishLevel();
      }
      return;
    }

    let isCorrect = false;

    if (q.type === 'mcq') {
      isCorrect = STATE.selectedOption === q.correctIndex;
    } else if (q.type === 'swipe') {
      isCorrect = STATE.selectedOption === q.isTrue;
    } else if (q.type === 'match') {
      isCorrect = STATE.matchedPairsCount === q.pairs.length;
    } else if (q.type === 'tap_order') {
      const userString = STATE.assembledTokens.map(t => t.text).join(' ');
      const correctString = q.correctOrder.join(' ');
      isCorrect = userString === correctString;
    }

    if (isCorrect) {
      SoundFX.playCorrect();
      if (level.isBoss && q.damage) {
        SoundFX.playBossHit();
        STATE.bossCurrentHp = Math.max(0, STATE.bossCurrentHp - q.damage);
        updateBossHp();
      }
      DOM.feedbackBanner.className = 'feedback-banner success';
      DOM.feedbackBanner.innerHTML = `
        <div style="font-weight:900; margin-bottom:4px;">✨ BRILLIANT! +25 XP</div>
        <div>${q.explanation || 'Spot on conceptual clarity!'}</div>
      `;
    } else {
      SoundFX.playError();
      STATE.hearts = Math.max(0, STATE.hearts - 1);
      saveState();
      DOM.feedbackBanner.className = 'feedback-banner error';
      DOM.feedbackBanner.innerHTML = `
        <div style="font-weight:900; margin-bottom:4px;">💔 INCORRECT (-1 Heart)</div>
        <div>${q.explanation || 'Review the core concept carefully!'}</div>
      `;
    }

    DOM.feedbackBanner.style.display = 'block';
    DOM.playActionBtn.textContent = 'CONTINUE';
    DOM.playActionBtn.disabled = false;
  }

  // --- FINISH LEVEL (VICTORY SCREEN) ---
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
    DOM.playQuestionBox.innerHTML = `
      <div style="text-align: center; padding: 2rem 0; animation: screenFadeIn 0.4s ease;">
        <div style="font-size: 5rem; margin-bottom: 1rem;">🏆</div>
        <h2 style="font-family:'Outfit'; font-size: 2rem; font-weight: 900; color: #facc15; margin-bottom: 0.5rem;">
          LEVEL COMPLETE!
        </h2>
        <p style="color: #cbd5e1; font-size: 1rem; margin-bottom: 1.5rem;">
          You mastered: <strong>${level.title}</strong>
        </p>

        <div style="display:flex; justify-content:center; gap:1.25rem; margin-bottom: 2rem;">
          <div style="background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:1rem 1.5rem;">
            <div style="font-size:1.8rem; color:#facc15;">⭐ ⭐ ⭐</div>
            <div style="font-size:0.78rem; font-weight:800; color:#94a3b8; text-transform:uppercase;">Mastery</div>
          </div>
          <div style="background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:14px; padding:1rem 1.5rem;">
            <div style="font-size:1.5rem; font-weight:900; color:#38bdf8;">+${level.xpReward || 50} XP</div>
            <div style="font-size:0.78rem; font-weight:800; color:#94a3b8; text-transform:uppercase;">Reward</div>
          </div>
        </div>

        ${level.badgeUnlock ? `
          <div style="background: linear-gradient(135deg, rgba(234, 179, 8, 0.2), rgba(249, 115, 22, 0.2)); border:1.5px solid #facc15; border-radius:14px; padding:1rem; margin-bottom:1.5rem;">
            <div style="font-size:0.8rem; font-weight:900; text-transform:uppercase; color:#facc15;">🎖️ New Title Unlocked!</div>
            <div style="font-size:1.15rem; font-weight:900; color:#fff;">${level.badgeUnlock}</div>
          </div>
        ` : ''}
      </div>
    `;

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
      STATE.hearts = 5;
    }

    SoundFX.playCorrect();
    saveState();
    alert(`🎉 Purchased ${item.name}!`);
  }

  // --- INITIALIZATION ---
  function init() {
    Confetti.init();
    updateHUD();
    renderQuestMap();
    renderLeaderboard();
    renderShop();

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
