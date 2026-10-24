/**
 * CORTEX VISUAL ROADMAP ENGINE (ROADMAP.SH STYLE)
 * Dynamic SVG Connectors, Touch Bottom-Sheet Drawer, Sound Effects & ForumIAS Synthesis
 */

(function () {
  'use strict';

  // --- AUDIO SYNTHESIZER (WEB AUDIO API) ---
  const AudioEngine = {
    ctx: null,
    init() {
      if (!this.ctx && (window.AudioContext || window.webkitAudioContext)) {
        this.ctx = new (window.AudioContext || window.webkitAudioContext)();
      }
    },
    playPop() {
      try {
        this.init();
        if (!this.ctx) return;
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(480, this.ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(880, this.ctx.currentTime + 0.08);
        gain.gain.setValueAtTime(0.2, this.ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.01, this.ctx.currentTime + 0.08);
        osc.connect(gain);
        gain.connect(this.ctx.destination);
        osc.start();
        osc.stop(this.ctx.currentTime + 0.09);
      } catch (e) {
        // audio context silent catch
      }
    },
    playComplete() {
      try {
        this.init();
        if (!this.ctx) return;
        const now = this.ctx.currentTime;
        const freqs = [523.25, 659.25, 783.99, 1046.50]; // C Major arpeggio
        freqs.forEach((freq, i) => {
          const osc = this.ctx.createOscillator();
          const gain = this.ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(freq, now + i * 0.07);
          gain.gain.setValueAtTime(0.25, now + i * 0.07);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.07 + 0.25);
          osc.connect(gain);
          gain.connect(this.ctx.destination);
          osc.start(now + i * 0.07);
          osc.stop(now + i * 0.07 + 0.28);
        });
      } catch (e) {}
    }
  };

  // --- STATE MANAGEMENT ---
  const STATE = {
    currentTopicId: 'public-exams',
    mastered: new Set(JSON.parse(localStorage.getItem('cortex_roadmap_mastered') || '[]')),
    activeBranchId: null,
    searchQuery: '',
    isDarkMode: localStorage.getItem('cortex_roadmap_dark') === 'true'
  };

  // Save mastered nodes to localStorage
  function saveMastered() {
    localStorage.setItem('cortex_roadmap_mastered', JSON.stringify(Array.from(STATE.mastered)));
    updateProgressBar();
  }

  // --- DOM REFERENCES ---
  const DOM = {
    body: document.body,
    topicBtns: document.querySelectorAll('.topic-toggle-btn'),
    statsPill: document.getElementById('roadmap-stats-text'),
    progressFill: document.getElementById('roadmap-progress-fill'),
    searchInput: document.getElementById('roadmap-search-input'),
    themeToggleBtn: document.getElementById('btn-theme-toggle'),
    roadmapTree: document.getElementById('roadmap-tree-canvas'),
    svgOverlay: document.getElementById('roadmap-svg-overlay'),
    drawerOverlay: document.getElementById('roadmap-drawer-overlay'),
    drawer: document.getElementById('roadmap-drawer'),
    drawerClose: document.getElementById('roadmap-drawer-close'),
    drawerContent: document.getElementById('roadmap-drawer-body'),
    drawerTitle: document.getElementById('drawer-node-title'),
    drawerTag: document.getElementById('drawer-node-tag'),
    drawerMasterBtn: document.getElementById('drawer-btn-master'),
    drawerAudioBtn: document.getElementById('drawer-btn-audio'),
    drawerPrevBtn: document.getElementById('drawer-btn-prev'),
    drawerNextBtn: document.getElementById('drawer-btn-next')
  };

  // --- MILESTONES DEFINITION ---
  const MILESTONES = {
    'public-exams': [
      {
        afterSectionIndex: 1,
        title: '🎯 Milestone 1: The Crisis Diagnostic Check',
        text: 'You have mastered the Constitutional Canvas and the 24-Staff Paradox. Understand that NTA is merely a registered society under the 1860 Act without statutory autonomy.',
        actionText: '📖 Review EOU Bihar Findings',
        targetBranchId: 'pe-b6'
      },
      {
        afterSectionIndex: 2,
        title: '⚖️ Milestone 2: Deterrence Economics Check',
        text: 'You grasp Becker’s Deterrence Formula: Expected Penalty = Severity × Probability of Detection × Speed. Harsh penal laws fail if syndicates face near-zero detection probability.',
        actionText: '🔍 Inspect 2026 Penal Fortress',
        targetBranchId: 'pe-b10'
      },
      {
        afterSectionIndex: 3,
        title: '🏛️ Milestone 3: The Radhakrishnan 7-Pillars',
        text: 'From two-stage testing to hybrid digital lockboxes and government-only test centers (KVs/JNVs)—this is your go-to blueprint for any GS-2 governance question.',
        actionText: '✨ View Pillar Recommendations',
        targetBranchId: 'pe-b11'
      }
    ],
    'ai-judiciary': [
      {
        afterSectionIndex: 0,
        title: '🚨 Milestone 1: The Methyl Isocyanate Warning',
        text: 'NCLT fake ChatGPT citations led the Supreme Court to mandate zero-tolerance for algorithmic hallucination. Anchor every answer with this landmark warning.',
        actionText: '⚖️ Review NCLT Alarm',
        targetBranchId: 'ai-b3'
      },
      {
        afterSectionIndex: 1,
        title: '🚦 Milestone 2: Supreme Court 3-Tier AI Pyramid',
        text: 'Master the Green Tier (administrative speed), Amber Tier (cautious translation with mandatory human checking), and Red Tier (strictly banned adjudication).',
        actionText: '📊 Review AI Pyramid Tiers',
        targetBranchId: 'ai-b6'
      }
    ],
    'msme': [
      {
        afterSectionIndex: 1,
        title: '🏭 Milestone 1: The Creative Destruction & Dwarfism Diagnostic',
        text: 'You have mastered the 31.1% GDP macro bedrock and Joseph Schumpeter\'s Creative Destruction. Indefinite size-based reservations foster pathological dwarfism rather than scaling up infants.',
        actionText: '🔍 Inspect Missing Middle',
        targetBranchId: 'msme-b5'
      },
      {
        afterSectionIndex: 2,
        title: '⚖️ Milestone 2: The Statutory Fortress & Section 43B(h)',
        text: 'Section 16 penal interest (3x Bank Rate) and Section 43B(h) tax disallowance form the dual legal teeth safeguarding small supplier liquidity.',
        actionText: '📜 Review Section 43B(h)',
        targetBranchId: 'msme-b8'
      },
      {
        afterSectionIndex: 3,
        title: '🏦 Milestone 3: The Budget 2025 Underwriting Revolution',
        text: 'Shifting from immovable land mortgages to scoring digital footprints (GST/TReDS) unlocks bank credit for asset-light innovators.',
        actionText: '✨ View Budget Reforms',
        targetBranchId: 'msme-b9'
      }
    ]
  };

  // Split-pill groups for Roadmap.sh aesthetics (like npm | yarn | pnpm | Bun)
  const SPLIT_PILLS = {
    'pe-b3': [
      { name: '42nd CAA 1976', id: 'pe-b3-1' },
      { name: 'Entry 25 Concurrent List', id: 'pe-b3-2' },
      { name: 'Dual Competence', id: 'pe-b3-3' }
    ],
    'pe-b9': [
      { name: '7-10 Yrs Prison', id: 'pe-b9-1' },
      { name: '₹1 Cr Minimum Fine', id: 'pe-b9-2' },
      { name: 'Asset Forfeiture', id: 'pe-b9-3' }
    ],
    'ai-b4': [
      { name: 'Cause-List AI', id: 'ai-b4-1' },
      { name: 'Registry Defect Check', id: 'ai-b4-2' },
      { name: 'Docket Grouping', id: 'ai-b4-3' }
    ],
    'msme-b3': [
      { name: 'Micro: ≤ ₹1Cr / ₹5Cr', id: 'msme-b3-1' },
      { name: 'Small: ≤ ₹10Cr / ₹50Cr', id: 'msme-b3-2' },
      { name: 'Medium: ≤ ₹50Cr / ₹250Cr', id: 'msme-b3-3' },
      { name: 'Exports Excluded', id: 'msme-b3-4' }
    ]
  };

  // --- RENDER ROADMAP TREE ---
  function renderRoadmap() {
    const topic = ROADMAP_DATA[STATE.currentTopicId];
    if (!topic || !DOM.roadmapTree) return;

    // Reset tree canvas
    DOM.roadmapTree.innerHTML = '';

    const milestones = MILESTONES[STATE.currentTopicId] || [];

    topic.sections.forEach((section, sIndex) => {
      // Create Section Block
      const sectionEl = document.createElement('div');
      sectionEl.className = 'roadmap-section-block';
      sectionEl.id = `section-${section.id}`;

      // Trunk Node (Yellow Pill)
      const trunkEl = document.createElement('div');
      trunkEl.className = 'roadmap-trunk-node';
      trunkEl.id = `trunk-${section.id}`;
      trunkEl.innerHTML = `
        <span class="roadmap-trunk-title">${section.title}</span>
        <span class="roadmap-trunk-subtitle">${section.subtitle}</span>
      `;
      trunkEl.addEventListener('click', () => {
        // Open first branch of section
        if (section.branches && section.branches.length > 0) {
          openDrawer(section.branches[0].id);
        }
      });
      sectionEl.appendChild(trunkEl);

      // Branches Wrapper
      if (section.branches && section.branches.length > 0) {
        const branchesWrapper = document.createElement('div');
        branchesWrapper.className = 'roadmap-branches-wrapper';

        const leftCol = document.createElement('div');
        leftCol.className = 'roadmap-branch-column left';

        const rightCol = document.createElement('div');
        rightCol.className = 'roadmap-branch-column right';

        section.branches.forEach((branch, bIndex) => {
          const isMastered = STATE.mastered.has(branch.id);
          const branchCard = document.createElement('div');
          branchCard.className = `roadmap-branch-card ${isMastered ? 'mastered' : ''}`;
          branchCard.id = `branch-${branch.id}`;
          branchCard.dataset.branchId = branch.id;

          // Check badge class
          const badgeCheckedClass = isMastered ? 'checked' : '';
          const badgeAltColor = (bIndex % 2 === 1) ? 'alt-green' : '';

          branchCard.innerHTML = `
            <div class="roadmap-branch-info">
              <span class="roadmap-branch-tag">${branch.tag || 'Concept'}</span>
              <span class="roadmap-branch-title">${branch.title}</span>
            </div>
            <button class="roadmap-check-badge ${badgeCheckedClass} ${badgeAltColor}" title="Toggle Mastery" data-check-id="${branch.id}" aria-label="Mark ${branch.title} as mastered">
              ✓
            </button>
          `;

          // Card Click: Open Drawer
          branchCard.addEventListener('click', (e) => {
            // If click was on check button, don't open drawer
            if (e.target.closest('.roadmap-check-badge')) {
              e.stopPropagation();
              toggleMastery(branch.id);
              return;
            }
            openDrawer(branch.id);
          });

          // Append to Left or Right Column
          if (bIndex % 2 === 0) {
            leftCol.appendChild(branchCard);
          } else {
            rightCol.appendChild(branchCard);
          }

          // If branch has split pills
          if (SPLIT_PILLS[branch.id]) {
            const splitGroup = document.createElement('div');
            splitGroup.className = 'roadmap-split-container';
            SPLIT_PILLS[branch.id].forEach(pill => {
              const pillEl = document.createElement('div');
              pillEl.className = 'roadmap-split-pill';
              pillEl.innerHTML = `<span>✓</span><span>${pill.name}</span>`;
              pillEl.addEventListener('click', (e) => {
                e.stopPropagation();
                openDrawer(branch.id);
              });
              splitGroup.appendChild(pillEl);
            });
            if (bIndex % 2 === 0) {
              leftCol.appendChild(splitGroup);
            } else {
              rightCol.appendChild(splitGroup);
            }
          }
        });

        branchesWrapper.appendChild(leftCol);
        branchesWrapper.appendChild(rightCol);
        sectionEl.appendChild(branchesWrapper);
      }

      DOM.roadmapTree.appendChild(sectionEl);

      // Check if there's a milestone to render after this section
      const milestone = milestones.find(m => m.afterSectionIndex === sIndex);
      if (milestone) {
        const milestoneEl = document.createElement('div');
        milestoneEl.className = 'roadmap-milestone-card';
        milestoneEl.innerHTML = `
          <div style="font-weight: 800; font-size: 0.95rem; margin-bottom: 0.35rem; color: #1e293b;">${milestone.title}</div>
          <div class="roadmap-milestone-text">${milestone.text}</div>
          <button class="roadmap-milestone-btn" data-target="${milestone.targetBranchId}">
            ${milestone.actionText}
          </button>
        `;
        const milestoneBtn = milestoneEl.querySelector('.roadmap-milestone-btn');
        if (milestoneBtn) {
          milestoneBtn.addEventListener('click', () => {
            openDrawer(milestone.targetBranchId);
          });
        }
        DOM.roadmapTree.appendChild(milestoneEl);
      }
    });

    // Update Progress and Lines
    updateProgressBar();
    scheduleRenderLines();
  }

  // --- CONNECTING DOTTED SVG LINES ---
  function renderSvgLines() {
    if (!DOM.svgOverlay) return;

    // Clear existing SVG paths
    DOM.svgOverlay.innerHTML = '';

    // Only render curved SVG lines on screens > 768px (Mobile uses streamlined CSS timeline)
    if (window.innerWidth <= 768) return;

    const containerRect = DOM.roadmapTree.getBoundingClientRect();
    const topic = ROADMAP_DATA[STATE.currentTopicId];
    if (!topic) return;

    topic.sections.forEach(section => {
      const trunkEl = document.getElementById(`trunk-${section.id}`);
      if (!trunkEl) return;

      const trunkRect = trunkEl.getBoundingClientRect();
      const trunkCenterX = trunkRect.left + trunkRect.width / 2 - containerRect.left;
      const trunkBottomY = trunkRect.bottom - containerRect.top;

      if (!section.branches) return;

      section.branches.forEach((branch, index) => {
        const cardEl = document.getElementById(`branch-${branch.id}`);
        if (!cardEl) return;

        const cardRect = cardEl.getBoundingClientRect();
        const isLeft = index % 2 === 0;

        // Target point on the branch card (right edge if on left, left edge if on right)
        const targetX = isLeft
          ? (cardRect.right - containerRect.left)
          : (cardRect.left - containerRect.left);
        const targetY = cardRect.top + cardRect.height / 2 - containerRect.top;

        // Start point from trunk side
        const startX = isLeft
          ? (trunkRect.left - containerRect.left)
          : (trunkRect.right - containerRect.left);
        const startY = trunkRect.top + trunkRect.height / 2 - containerRect.top;

        // Draw smooth cubic bezier
        const dx = targetX - startX;
        const cp1x = startX + dx * 0.45;
        const cp1y = startY;
        const cp2x = startX + dx * 0.55;
        const cp2y = targetY;

        const path = document.createElementNS('http://www.w3.org/2000/svg', 'path');
        path.setAttribute('d', `M ${startX} ${startY} C ${cp1x} ${cp1y}, ${cp2x} ${cp2y}, ${targetX} ${targetY}`);
        path.setAttribute('class', 'roadmap-svg-path');
        DOM.svgOverlay.appendChild(path);
      });
    });
  }

  let lineDebounceTimer = null;
  function scheduleRenderLines() {
    clearTimeout(lineDebounceTimer);
    lineDebounceTimer = setTimeout(renderSvgLines, 60);
  }

  // --- TOGGLE MASTERY (CHECKMARK) ---
  function toggleMastery(branchId) {
    if (STATE.mastered.has(branchId)) {
      STATE.mastered.delete(branchId);
    } else {
      STATE.mastered.add(branchId);
      AudioEngine.playPop();
    }
    saveMastered();

    // Update Card UI
    const card = document.getElementById(`branch-${branchId}`);
    if (card) {
      const badge = card.querySelector('.roadmap-check-badge');
      if (STATE.mastered.has(branchId)) {
        card.classList.add('mastered');
        if (badge) badge.classList.add('checked');
      } else {
        card.classList.remove('mastered');
        if (badge) badge.classList.remove('checked');
      }
    }

    // Update Drawer Button if open
    if (STATE.activeBranchId === branchId) {
      updateDrawerMasterBtn(branchId);
    }
  }

  // --- UPDATE PROGRESS BAR ---
  function updateProgressBar() {
    const topic = ROADMAP_DATA[STATE.currentTopicId];
    if (!topic) return;

    let total = 0;
    let masteredCount = 0;

    topic.sections.forEach(s => {
      if (s.branches) {
        s.branches.forEach(b => {
          total++;
          if (STATE.mastered.has(b.id)) masteredCount++;
        });
      }
    });

    const percent = total > 0 ? Math.round((masteredCount / total) * 100) : 0;

    if (DOM.statsPill) {
      DOM.statsPill.textContent = `${masteredCount} / ${total} Mastered (${percent}%)`;
    }
    if (DOM.progressFill) {
      DOM.progressFill.style.width = `${percent}%`;
    }

    if (percent === 100 && total > 0) {
      AudioEngine.playComplete();
    }
  }

  // --- FORUM IAS INSPECTOR DRAWER ---
  function findBranch(branchId) {
    const topic = ROADMAP_DATA[STATE.currentTopicId];
    if (!topic) return null;
    for (let s of topic.sections) {
      if (s.branches) {
        const found = s.branches.find(b => b.id === branchId);
        if (found) return found;
      }
    }
    return null;
  }

  function getAllBranchIds() {
    const topic = ROADMAP_DATA[STATE.currentTopicId];
    if (!topic) return [];
    const ids = [];
    topic.sections.forEach(s => {
      if (s.branches) {
        s.branches.forEach(b => ids.push(b.id));
      }
    });
    return ids;
  }

  function openDrawer(branchId) {
    const branch = findBranch(branchId);
    if (!branch) return;

    STATE.activeBranchId = branchId;

    // Highlight selected card
    document.querySelectorAll('.roadmap-branch-card').forEach(c => c.classList.remove('active-selected'));
    const selectedCard = document.getElementById(`branch-${branchId}`);
    if (selectedCard) selectedCard.classList.add('active-selected');

    // Header info
    if (DOM.drawerTitle) DOM.drawerTitle.textContent = branch.title;
    if (DOM.drawerTag) DOM.drawerTag.textContent = branch.tag || 'High-Yield Concept';

    updateDrawerMasterBtn(branchId);

    // Build ForumIAS style body
    let html = '';

    // 1. Landmark Quote / Case Law (if available)
    if (branch.quotes && branch.quotes.length > 0) {
      html += `
        <div class="forum-callout-quote">
          <div style="font-size:0.75rem; text-transform:uppercase; font-weight:800; letter-spacing:0.06em; margin-bottom:4px; color:#b45309;">
            💬 Landmark Quote / Judicial Dictum
          </div>
          ${branch.quotes.join('<br>')}
        </div>
      `;
    }

    // 2. High-Yield Key Points / Details
    html += `
      <div class="forum-key-points">
        ${branch.details || `<p>${branch.shortDesc}</p>`}
      </div>
    `;

    // 3. UPSC Mains Answer-Writing Utility Tip
    if (branch.mainsTip) {
      html += `
        <div class="forum-mains-card">
          <h5>✍️ Mains Answer-Writing Hook</h5>
          <p style="font-size:0.9rem; line-height:1.5; margin:0;">${branch.mainsTip}</p>
        </div>
      `;
    }

    // 4. Prelims High-Alert Trap
    html += `
      <div style="background: rgba(99, 102, 241, 0.08); border: 1.5px solid rgba(99, 102, 241, 0.25); border-radius: 8px; padding: 0.9rem 1.1rem;">
        <div style="font-size:0.75rem; font-weight:800; text-transform:uppercase; color:#6366f1; margin-bottom:4px;">
          ⚡ Prelims Alert: Statutory vs Regulatory Nuance
        </div>
        <p style="font-size:0.86rem; color:#475569; margin:0; line-height:1.45;">
          Remember: Under the 2024 Act, candidates are <em>not</em> prosecuted criminally. Penalties apply strictly to syndicates, paper setters, and service providers.
        </p>
      </div>
    `;

    if (DOM.drawerContent) {
      DOM.drawerContent.innerHTML = html;
      DOM.drawerContent.scrollTop = 0;
    }

    // Prev / Next Navigation state
    const allIds = getAllBranchIds();
    const currIndex = allIds.indexOf(branchId);
    if (DOM.drawerPrevBtn) {
      DOM.drawerPrevBtn.disabled = currIndex <= 0;
      DOM.drawerPrevBtn.onclick = () => {
        if (currIndex > 0) openDrawer(allIds[currIndex - 1]);
      };
    }
    if (DOM.drawerNextBtn) {
      DOM.drawerNextBtn.disabled = currIndex >= allIds.length - 1;
      DOM.drawerNextBtn.onclick = () => {
        if (currIndex < allIds.length - 1) openDrawer(allIds[currIndex + 1]);
      };
    }

    // Open drawer
    if (DOM.drawerOverlay) DOM.drawerOverlay.classList.add('open');
    if (DOM.drawer) DOM.drawer.classList.add('open');
  }

  function closeDrawer() {
    if (DOM.drawerOverlay) DOM.drawerOverlay.classList.remove('open');
    if (DOM.drawer) DOM.drawer.classList.remove('open');
    document.querySelectorAll('.roadmap-branch-card').forEach(c => c.classList.remove('active-selected'));
    STATE.activeBranchId = null;
    // Stop any ongoing speech synthesis
    if ('speechSynthesis' in window) {
      window.speechSynthesis.cancel();
    }
  }

  function updateDrawerMasterBtn(branchId) {
    if (!DOM.drawerMasterBtn) return;
    const isMastered = STATE.mastered.has(branchId);
    if (isMastered) {
      DOM.drawerMasterBtn.style.background = '#10b981';
      DOM.drawerMasterBtn.style.borderColor = '#059669';
      DOM.drawerMasterBtn.style.color = '#ffffff';
      DOM.drawerMasterBtn.innerHTML = '✓ Mastered';
    } else {
      DOM.drawerMasterBtn.style.background = '#e2e8f0';
      DOM.drawerMasterBtn.style.borderColor = '#cbd5e1';
      DOM.drawerMasterBtn.style.color = '#1e293b';
      DOM.drawerMasterBtn.innerHTML = 'Mark Mastered';
    }
  }

  // --- AUDIO READOUT (SPEECH SYNTHESIS) ---
  function readBranchContent(branchId) {
    if (!('speechSynthesis' in window)) {
      alert('Text-to-speech is not supported by your browser.');
      return;
    }
    window.speechSynthesis.cancel();

    const branch = findBranch(branchId);
    if (!branch) return;

    let textToRead = `${branch.title}. `;
    if (branch.quotes && branch.quotes.length > 0) {
      textToRead += `Landmark Quote: ${branch.quotes[0]}. `;
    }
    textToRead += branch.shortDesc || '';
    if (branch.mainsTip) {
      textToRead += ` Mains Tip: ${branch.mainsTip}`;
    }

    const utterance = new SpeechSynthesisUtterance(textToRead);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    utterance.lang = 'en-US';

    // Toggle button visual state
    if (DOM.drawerAudioBtn) {
      DOM.drawerAudioBtn.innerHTML = '🔊 Speaking...';
      utterance.onend = () => {
        DOM.drawerAudioBtn.innerHTML = '🔊 Read Aloud';
      };
      utterance.onerror = () => {
        DOM.drawerAudioBtn.innerHTML = '🔊 Read Aloud';
      };
    }

    window.speechSynthesis.speak(utterance);
  }

  // --- SEARCH FILTER ---
  function handleSearch(query) {
    STATE.searchQuery = query.toLowerCase().trim();
    const cards = document.querySelectorAll('.roadmap-branch-card');
    const sections = document.querySelectorAll('.roadmap-section-block');

    if (!STATE.searchQuery) {
      cards.forEach(c => {
        c.style.display = 'flex';
        c.style.opacity = '1';
      });
      sections.forEach(s => s.style.display = 'flex');
      scheduleRenderLines();
      return;
    }

    sections.forEach(section => {
      let sectionHasMatch = false;
      const sectionCards = section.querySelectorAll('.roadmap-branch-card');
      sectionCards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(STATE.searchQuery)) {
          card.style.display = 'flex';
          card.style.opacity = '1';
          sectionHasMatch = true;
        } else {
          card.style.display = 'none';
        }
      });

      // Also check trunk title
      const trunk = section.querySelector('.roadmap-trunk-node');
      if (trunk && trunk.textContent.toLowerCase().includes(STATE.searchQuery)) {
        sectionHasMatch = true;
      }

      section.style.display = sectionHasMatch ? 'flex' : 'none';
    });

    scheduleRenderLines();
  }

  // --- SAMSUNG ONE UI THEME INTEGRATION ---
  function applyTheme() {
    const saved = localStorage.getItem('samsung_ui_theme');
    STATE.isDarkMode = saved ? saved === 'samsung-dark' : (localStorage.getItem('cortex_roadmap_dark') !== 'false');

    if (STATE.isDarkMode) {
      document.body.classList.remove('samsung-light', 'light-theme');
      document.body.classList.add('dark-theme', 'samsung-dark');
      if (DOM.themeToggleBtn) {
        const icon = DOM.themeToggleBtn.querySelector('#theme-btn-icon');
        const text = DOM.themeToggleBtn.querySelector('#theme-btn-text');
        if (icon) icon.textContent = '🌙';
        if (text) text.textContent = 'Dark UI';
      }
    } else {
      document.body.classList.remove('dark-theme', 'samsung-dark');
      document.body.classList.add('samsung-light', 'light-theme');
      if (DOM.themeToggleBtn) {
        const icon = DOM.themeToggleBtn.querySelector('#theme-btn-icon');
        const text = DOM.themeToggleBtn.querySelector('#theme-btn-text');
        if (icon) icon.textContent = '☀️';
        if (text) text.textContent = 'Light UI';
      }
    }
    scheduleRenderLines();
  }

  // Subscribe to external theme updates
  window.addEventListener('samsungThemeChanged', () => {
    applyTheme();
  });

  // --- SETUP EVENT LISTENERS ---
  function initEvents() {
    // Topic Selector Toggles
    DOM.topicBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        const topicId = btn.dataset.topic;
        if (topicId && topicId !== STATE.currentTopicId) {
          DOM.topicBtns.forEach(b => b.classList.remove('active'));
          btn.classList.add('active');
          STATE.currentTopicId = topicId;
          renderRoadmap();
        }
      });
    });

    // Search Input
    if (DOM.searchInput) {
      DOM.searchInput.addEventListener('input', (e) => {
        handleSearch(e.target.value);
      });
    }

    // Theme Toggle
    if (DOM.themeToggleBtn) {
      DOM.themeToggleBtn.addEventListener('click', () => {
        if (window.SamsungTheme) {
          window.SamsungTheme.toggle();
        } else {
          STATE.isDarkMode = !STATE.isDarkMode;
          localStorage.setItem('samsung_ui_theme', STATE.isDarkMode ? 'samsung-dark' : 'samsung-light');
          applyTheme();
        }
      });
    }

    // Drawer Close Buttons & Overlay Click
    if (DOM.drawerClose) {
      DOM.drawerClose.addEventListener('click', closeDrawer);
    }
    if (DOM.drawerOverlay) {
      DOM.drawerOverlay.addEventListener('click', closeDrawer);
    }

    // Escape Key to close drawer
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && DOM.drawer && DOM.drawer.classList.contains('open')) {
        closeDrawer();
      }
    });

    // Drawer Master Toggle Button
    if (DOM.drawerMasterBtn) {
      DOM.drawerMasterBtn.addEventListener('click', () => {
        if (STATE.activeBranchId) {
          toggleMastery(STATE.activeBranchId);
        }
      });
    }

    // Drawer Audio Read Aloud Button
    if (DOM.drawerAudioBtn) {
      DOM.drawerAudioBtn.addEventListener('click', () => {
        if (STATE.activeBranchId) {
          readBranchContent(STATE.activeBranchId);
        }
      });
    }

    // Window Resize / Orientation Change: Recalculate SVG
    window.addEventListener('resize', scheduleRenderLines);
  }

  // --- INITIALIZATION ---
  function init() {
    applyTheme();
    initEvents();

    // Check URL parameters for topic
    const urlParams = new URLSearchParams(window.location.search);
    const paramTopic = urlParams.get('topic');
    if (paramTopic && ROADMAP_DATA[paramTopic]) {
      STATE.currentTopicId = paramTopic;
      DOM.topicBtns.forEach(b => {
        b.classList.toggle('active', b.dataset.topic === paramTopic);
      });
    }

    renderRoadmap();

    // Check URL parameter for open node
    const paramNode = urlParams.get('node');
    if (paramNode) {
      setTimeout(() => openDrawer(paramNode), 300);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  // Export engine methods for window access if needed
  window.RoadmapEngine = {
    openDrawer,
    closeDrawer,
    toggleMastery,
    switchTopic: (topicId) => {
      STATE.currentTopicId = topicId;
      DOM.topicBtns.forEach(b => b.classList.toggle('active', b.dataset.topic === topicId));
      renderRoadmap();
    }
  };

})();
