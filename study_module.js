/**
 * CORTEX ANKI 2.0 - TOPIC STUDY ENGINE
 * Powers all 6 modules:
 * 1. Interactive Reading with Highlighting & TTS
 * 2. Key Terms & Prelims/Mains Pointers
 * 3. Diagrams & Flowcharts
 * 4. Flashcards (Anki SRS Algorithm & Keyboard Shortcuts)
 * 5. MCQs (Instant Feedback & Explanations)
 * 6. Mains Questions (Timer, Word Counter & Model Answer Reveal)
 */

let currentTopicData = LECTURE_DATA;
let activeCardIndex = 0;
let isFlipped = false;
let currentHighlightColor = 'hl-prelims';
let mainsTimerInterval = null;
let mainsSecondsRemaining = 11 * 60; // 11 mins for 15-marker

document.addEventListener('DOMContentLoaded', () => {
  // Check if a custom uploaded lecture is requested via URL param
  loadRequestedTopic();

  // Initialize navigation tabs
  setupStudyTabs();

  // Initialize individual modules
  initReadingModule();
  initKeyTermsModule();
  initDiagramsModule();
  initFlashcardsModule();
  initMCQsModule();
  initMainsModule();
});

function loadRequestedTopic() {
  const params = new URLSearchParams(window.location.search);
  const customId = params.get('custom');
  if (customId) {
    const customLectures = CortexStorage.getCustomLectures();
    const found = customLectures.find(l => l.id === customId);
    if (found) {
      currentTopicData = {
        ...LECTURE_DATA,
        title: found.title,
        readTime: found.readTime,
        reading: {
          title: found.title,
          sections: found.sections || []
        },
        flashcards: found.flashcards || LECTURE_DATA.flashcards,
        keyTerms: found.keyTerms || LECTURE_DATA.keyTerms
      };
    }
  }

  // Update header text
  const titleEl = document.getElementById('study-topic-title');
  if (titleEl) titleEl.textContent = currentTopicData.title;
}

/* ==========================================================================
   MODULE NAVIGATION TABS
   ========================================================================== */
function setupStudyTabs() {
  const tabBtns = document.querySelectorAll('.study-tab-btn');
  const panes = document.querySelectorAll('.tab-pane');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      panes.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const targetPane = document.getElementById(btn.dataset.target);
      if (targetPane) {
        targetPane.classList.add('active');
        window.scrollTo({ top: 180, behavior: 'smooth' });
      }
    });
  });
}

/* ==========================================================================
   MODULE 1: INTERACTIVE READING & PDF SHEET FORMAT
   ========================================================================== */
function initReadingModule() {
  const sheetContainer = document.getElementById('reading-sheet-container');
  const essayContainer = document.getElementById('reading-body-container');
  const tocList = document.getElementById('reading-toc-list');

  // Render PDF Notes Sheet format (Default view)
  if (sheetContainer && currentTopicData.pdfSheetNotes) {
    renderPdfNotesSheet(currentTopicData.pdfSheetNotes, sheetContainer);
  }

  // Render Long-form Essay format (Alternate view)
  if (essayContainer && currentTopicData.reading) {
    renderEssayContent(currentTopicData.reading, essayContainer, tocList);
  }

  // Setup View Mode Switcher
  const btnViewSheet = document.getElementById('btn-view-sheet');
  const btnViewEssay = document.getElementById('btn-view-essay');

  if (btnViewSheet && btnViewEssay) {
    btnViewSheet.addEventListener('click', () => {
      btnViewSheet.classList.add('active');
      btnViewEssay.classList.remove('active');
      if (sheetContainer) sheetContainer.style.display = 'block';
      if (essayContainer) essayContainer.style.display = 'none';
      showToast('Switched to: ForumIAS Sheet Notes format', 'info');
    });

    btnViewEssay.addEventListener('click', () => {
      btnViewEssay.classList.add('active');
      btnViewSheet.classList.remove('active');
      if (sheetContainer) sheetContainer.style.display = 'none';
      if (essayContainer) essayContainer.style.display = 'block';
      showToast('Switched to: Detailed Lecture Guide', 'info');
    });
  }

  // Expand / Collapse All Details in Sheet
  const btnToggleAll = document.getElementById('btn-toggle-all-details');
  let allExpanded = false;
  if (btnToggleAll) {
    btnToggleAll.addEventListener('click', () => {
      allExpanded = !allExpanded;
      const items = document.querySelectorAll('.pdf-bullet-item.has-detail');
      items.forEach(it => {
        if (allExpanded) it.classList.add('expanded');
        else it.classList.remove('expanded');
      });
      btnToggleAll.textContent = allExpanded ? '⇥ Collapse Details' : '↔ Expand Details';
      showToast(allExpanded ? 'Expanded all high-yield notes' : 'Collapsed to summary sheet');
    });
  }

  // Print Sheet
  const btnPrint = document.getElementById('btn-print-sheet');
  if (btnPrint) {
    btnPrint.addEventListener('click', () => {
      window.print();
    });
  }

  // Reading Scroll Progress Indicator
  window.addEventListener('scroll', () => {
    const progressBar = document.getElementById('reading-progress-indicator');
    if (!progressBar) return;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const progress = (window.scrollY / docHeight) * 100;
    progressBar.style.width = `${Math.min(100, Math.max(0, progress))}%`;
  });

  // Text Highlighting Tools
  const hlButtons = document.querySelectorAll('.btn-hl');
  hlButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      hlButtons.forEach(b => b.style.outline = 'none');
      btn.style.outline = '2px solid #fff';
      currentHighlightColor = btn.dataset.hl;
      showToast(`Highlighter set to: ${btn.textContent.trim()}`);
    });
  });

  // Text Selection Highlight Action
  const activeArticleBox = document.getElementById('reading-article-box');
  if (activeArticleBox) {
    activeArticleBox.addEventListener('mouseup', () => {
      const selection = window.getSelection();
      if (selection && selection.toString().trim().length > 2) {
        const selectedText = selection.toString();
        const range = selection.getRangeAt(0);
        const span = document.createElement('span');
        span.className = currentHighlightColor;
        span.textContent = selectedText;
        range.deleteContents();
        range.insertNode(span);
        selection.removeAllRanges();
        showToast('Annotation saved!', 'success');
        SoundFX.playCorrect();
      }
    });
  }

  // Font Size Adjusters
  let currentFontSize = 1.05;
  const btnFontIncrease = document.getElementById('btn-font-increase');
  const btnFontDecrease = document.getElementById('btn-font-decrease');

  if (btnFontIncrease && activeArticleBox) {
    btnFontIncrease.addEventListener('click', () => {
      currentFontSize = Math.min(1.4, currentFontSize + 0.08);
      activeArticleBox.style.fontSize = `${currentFontSize}rem`;
    });
  }
  if (btnFontDecrease && activeArticleBox) {
    btnFontDecrease.addEventListener('click', () => {
      currentFontSize = Math.max(0.9, currentFontSize - 0.08);
      activeArticleBox.style.fontSize = `${currentFontSize}rem`;
    });
  }

  // Text to Speech Read Aloud
  const btnTTS = document.getElementById('btn-read-aloud');
  if (btnTTS) {
    let isSpeaking = false;
    btnTTS.addEventListener('click', () => {
      if ('speechSynthesis' in window) {
        if (isSpeaking) {
          window.speechSynthesis.cancel();
          btnTTS.textContent = '🔊 Read Aloud';
          isSpeaking = false;
        } else {
          const textToRead = "Artificial Intelligence in Judiciary. Context: Supreme Court formulated draft Regulations for use of AI in Courts, 2026. Key debates: Innovation versus Independence, Human Primacy versus Algorithmic Justice, Administrative AI versus Adjudicatory AI, and Imported Tech versus Swadeshi.";
          const utterance = new SpeechSynthesisUtterance(textToRead);
          utterance.rate = 1.0;
          utterance.onend = () => {
            btnTTS.textContent = '🔊 Read Aloud';
            isSpeaking = false;
          };
          window.speechSynthesis.speak(utterance);
          btnTTS.textContent = '⏹️ Stop Reading';
          isSpeaking = true;
          showToast('Narrating sheet overview...');
        }
      } else {
        showToast('Text-to-speech not supported in this browser.', 'warning');
      }
    });
  }
}

/**
 * Renders the exact PDF sheet format:
 * - Red dashed title box
 * - Purple/blue dashed dividers
 * - Green dashed section tags
 * - Vertical dashed divider for PROS & CONS
 * - Clean digital typography (Outfit & Plus Jakarta Sans)
 */
function renderPdfNotesSheet(data, container) {
  container.innerHTML = '';

  const sheet = document.createElement('div');
  sheet.className = 'pdf-notes-sheet';

  // 1. Top bar matching header of the PDF sheet
  const topbar = document.createElement('div');
  topbar.className = 'pdf-sheet-topbar';
  topbar.innerHTML = `
    <div><span>Shared Freely By AbxK</span></div>
    <div style="font-weight:700; color:#ef4444;"><span style="background:#ef4444; color:#fff; padding:2px 6px; border-radius:3px; margin-right:4px;">▲</span> Forum<span style="color:#fff;">IAS</span></div>
    <div><span class="code-tag">${data.sheetCode || 'CA - 260814'}</span></div>
  `;
  sheet.appendChild(topbar);

  // 2. Title Box (Red Dashed Border)
  const titleContainer = document.createElement('div');
  titleContainer.className = 'pdf-title-container';
  titleContainer.innerHTML = `
    <div class="pdf-title-box">
      <h3>${data.title}</h3>
    </div>
  `;
  sheet.appendChild(titleContainer);

  // Purple dashed divider
  sheet.appendChild(createDashedSeparator());

  // 3. Sections
  data.sections.forEach(sec => {
    if (sec.type === 'PROS_CONS') {
      // Side-by-side PROS & CONS with vertical dashed divider
      const grid = document.createElement('div');
      grid.className = 'pdf-pros-cons-grid';

      // Left Column (PROS)
      const prosCol = document.createElement('div');
      prosCol.className = 'pdf-pros-col';
      prosCol.innerHTML = `<div class="pdf-tag-box">${sec.prosTag}</div>`;
      const prosList = document.createElement('ul');
      prosList.className = 'pdf-bullet-list';
      sec.pros.forEach(b => prosList.appendChild(createBulletItem(b)));
      prosCol.appendChild(prosList);
      grid.appendChild(prosCol);

      // Right Column (CONS)
      const consCol = document.createElement('div');
      consCol.className = 'pdf-cons-col';
      consCol.innerHTML = `<div class="pdf-tag-box">${sec.consTag}</div>`;
      const consList = document.createElement('ul');
      consList.className = 'pdf-bullet-list';
      sec.cons.forEach(b => consList.appendChild(createBulletItem(b)));
      consCol.appendChild(consList);
      grid.appendChild(consCol);

      sheet.appendChild(grid);
      sheet.appendChild(createDashedSeparator());
    } else if (sec.type === 'BOTTOM_GRID') {
      // Bottom SUGGESTIONS & CONCLUSION side-by-side
      const bottomGrid = document.createElement('div');
      bottomGrid.className = 'pdf-bottom-grid';

      // Left: SUGGESTIONS
      const suggCol = document.createElement('div');
      suggCol.innerHTML = `<div class="pdf-tag-box">${sec.suggestionsTag}</div>`;
      const suggList = document.createElement('ul');
      suggList.className = 'pdf-bullet-list';
      sec.suggestions.forEach(b => suggList.appendChild(createBulletItem(b)));
      suggCol.appendChild(suggList);
      bottomGrid.appendChild(suggCol);

      // Right: CONCLUSION
      const concCol = document.createElement('div');
      concCol.innerHTML = `<div class="pdf-tag-box">${sec.conclusionTag}</div>`;
      const concList = document.createElement('ul');
      concList.className = 'pdf-bullet-list';
      sec.conclusion.forEach(b => concList.appendChild(createBulletItem(b)));
      concCol.appendChild(concList);
      bottomGrid.appendChild(concCol);

      sheet.appendChild(bottomGrid);
    } else {
      // Standard Section (INTRO, CONTEXT, DEBATES, CHALLENGES, etc.)
      const secDiv = document.createElement('div');
      secDiv.innerHTML = `<div class="pdf-tag-box">${sec.tag}</div>`;

      const bulletList = document.createElement('ul');
      bulletList.className = 'pdf-bullet-list';
      sec.bullets.forEach(b => bulletList.appendChild(createBulletItem(b)));
      secDiv.appendChild(bulletList);

      sheet.appendChild(secDiv);
      sheet.appendChild(createDashedSeparator());
    }
  });

  // 4. Footer matching the PDF sheet
  const footer = document.createElement('div');
  footer.className = 'pdf-sheet-footer';
  footer.innerHTML = `
    <span>Current Affairs Classes by ForumIAS</span>
    <span>Page 1 of 1</span>
  `;
  sheet.appendChild(footer);

  container.appendChild(sheet);

  // Click listeners to toggle item expansion
  sheet.querySelectorAll('.pdf-bullet-item.has-detail').forEach(item => {
    item.addEventListener('click', () => {
      item.classList.toggle('expanded');
    });
  });
}

function createBulletItem(bullet) {
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

function createDashedSeparator() {
  const hr = document.createElement('hr');
  hr.className = 'pdf-dashed-separator';
  return hr;
}

function renderEssayContent(readingData, container, tocList) {
  container.innerHTML = '';
  if (tocList) tocList.innerHTML = '';

  readingData.sections.forEach(sec => {
    const secDiv = document.createElement('section');
    secDiv.id = sec.id;
    secDiv.innerHTML = `
      <h2>${sec.heading}</h2>
      ${sec.content}
    `;
    container.appendChild(secDiv);

    if (tocList) {
      const li = document.createElement('li');
      li.innerHTML = `<a href="#${sec.id}">${sec.heading}</a>`;
      tocList.appendChild(li);
    }
  });
}

/* ==========================================================================
   MODULE 2: KEY TERMS & PRELIMS / MAINS POINTERS
   ========================================================================== */
function initKeyTermsModule() {
  const termsContainer = document.getElementById('key-terms-container');
  const prelimsList = document.getElementById('prelims-pointers-list');
  const mainsGrid = document.getElementById('mains-pointers-grid');

  // Key Terms
  if (termsContainer && currentTopicData.keyTerms) {
    termsContainer.innerHTML = '';
    currentTopicData.keyTerms.forEach(item => {
      const card = document.createElement('div');
      card.className = 'pointer-card';
      card.innerHTML = `
        <div class="pointer-header">
          <span class="pointer-title">${item.term}</span>
          <span class="badge badge-primary">${item.category}</span>
        </div>
        <div style="font-size:0.85rem; color:#818cf8; font-weight:600; margin-bottom:0.4rem;">${item.fullForm}</div>
        <p style="font-size:0.92rem; color:var(--text-muted); line-height:1.6;">${item.desc}</p>
      `;
      termsContainer.appendChild(card);
    });
  }

  // Prelims Pointers
  if (prelimsList && currentTopicData.prelimsPointers) {
    prelimsList.innerHTML = '';
    currentTopicData.prelimsPointers.forEach(pt => {
      const li = document.createElement('li');
      li.style.marginBottom = '0.9rem';
      li.style.lineHeight = '1.6';
      li.innerHTML = `<strong>🎯</strong> ${pt}`;
      prelimsList.appendChild(li);
    });
  }

  // Mains Dimensions
  if (mainsGrid && currentTopicData.mainsPointers) {
    mainsGrid.innerHTML = '';
    currentTopicData.mainsPointers.forEach(m => {
      const col = document.createElement('div');
      col.className = 'pointer-card';
      col.innerHTML = `
        <div style="font-family:var(--font-display); font-size:1.1rem; font-weight:700; color:#38bdf8; margin-bottom:0.5rem;">
          ${m.dimension}
        </div>
        <p style="font-size:0.92rem; color:#cbd5e1; line-height:1.6;">${m.content}</p>
      `;
      mainsGrid.appendChild(col);
    });
  }
}

/* ==========================================================================
   MODULE 3: DIAGRAMS & FLOWCHARTS
   ========================================================================== */
function initDiagramsModule() {
  const flowContainer = document.getElementById('flowchart-steps-container');
  if (!flowContainer || !currentTopicData.diagrams || !currentTopicData.diagrams[0]) return;

  const diagram = currentTopicData.diagrams[0];
  flowContainer.innerHTML = '';

  diagram.steps.forEach((step, idx) => {
    const stepBox = document.createElement('div');
    stepBox.className = 'flow-step-box';
    stepBox.innerHTML = `
      <div class="flow-step-num">${step.num}</div>
      <div class="flow-step-content">
        <h4>${step.title}</h4>
        <p>${step.detail}</p>
      </div>
    `;
    flowContainer.appendChild(stepBox);

    // Arrow except after last item
    if (idx < diagram.steps.length - 1) {
      const arrow = document.createElement('div');
      arrow.className = 'flow-arrow-down';
      arrow.innerHTML = '↓';
      flowContainer.appendChild(arrow);
    }
  });
}

/* ==========================================================================
   MODULE 4: FLASHCARDS (ANKI SPACED REPETITION ENGINE)
   ========================================================================== */
function initFlashcardsModule() {
  const cards = currentTopicData.flashcards;
  if (!cards || cards.length === 0) return;

  activeCardIndex = 0;
  isFlipped = false;
  renderActiveFlashcard();

  const flipper = document.getElementById('card-flipper');
  const cardPerspective = document.getElementById('card-perspective');

  if (cardPerspective) {
    cardPerspective.addEventListener('click', toggleCardFlip);
  }

  // Keyboard Shortcuts: Space to flip, 1-4 for SRS grading
  window.addEventListener('keydown', (e) => {
    // Only trigger if flashcards tab is active
    const tabFlashcards = document.getElementById('pane-flashcards');
    if (!tabFlashcards || !tabFlashcards.classList.contains('active')) return;

    if (e.code === 'Space') {
      e.preventDefault();
      toggleCardFlip();
    } else if (isFlipped) {
      if (e.key === '1') rateSRS(1);
      else if (e.key === '2') rateSRS(2);
      else if (e.key === '3') rateSRS(3);
      else if (e.key === '4') rateSRS(4);
    }
  });

  // SRS Button Listeners
  document.querySelectorAll('.btn-srs').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const rating = parseInt(btn.dataset.rating, 10);
      rateSRS(rating);
    });
  });
}

function toggleCardFlip() {
  const flipper = document.getElementById('card-flipper');
  const srsControls = document.getElementById('srs-controls-wrapper');
  if (!flipper) return;

  isFlipped = !isFlipped;
  SoundFX.playFlip();

  if (isFlipped) {
    flipper.classList.add('flipped');
    if (srsControls) srsControls.style.opacity = '1';
  } else {
    flipper.classList.remove('flipped');
    if (srsControls) srsControls.style.opacity = '0.5';
  }
}

function renderActiveFlashcard() {
  const cards = currentTopicData.flashcards;
  const currentCard = cards[activeCardIndex];
  if (!currentCard) return;

  isFlipped = false;
  const flipper = document.getElementById('card-flipper');
  if (flipper) flipper.classList.remove('flipped');

  const srsControls = document.getElementById('srs-controls-wrapper');
  if (srsControls) srsControls.style.opacity = '0.5';

  // Front Content
  document.getElementById('card-category-front').textContent = currentCard.category || 'Constitutional Law';
  document.getElementById('card-prompt-front').textContent = currentCard.front;

  // Back Content
  document.getElementById('card-category-back').textContent = currentCard.topic || 'Exam High-Yield';
  document.getElementById('card-answer-back').innerHTML = currentCard.back.replace(/\n/g, '<br>');

  // Card Counter / Progress
  const counterEl = document.getElementById('srs-card-counter');
  if (counterEl) counterEl.textContent = `Card ${activeCardIndex + 1} of ${cards.length}`;

  const progressEl = document.getElementById('srs-progress-bar');
  if (progressEl) {
    const pct = ((activeCardIndex + 1) / cards.length) * 100;
    progressEl.style.width = `${pct}%`;
  }
}

/**
 * SuperMemo SM-2 Spaced Repetition Algorithm Implementation
 */
function rateSRS(rating) {
  const cards = currentTopicData.flashcards;
  const currentCard = cards[activeCardIndex];
  if (!currentCard) return;

  // Sound feedback
  if (rating >= 3) SoundFX.playCorrect();
  else SoundFX.playWrong();

  // SM-2 calculation
  if (rating < 3) {
    currentCard.repetitions = 0;
    currentCard.interval = 1;
  } else {
    if (currentCard.repetitions === 0) currentCard.interval = 1;
    else if (currentCard.repetitions === 1) currentCard.interval = 6;
    else currentCard.interval = Math.round(currentCard.interval * currentCard.easeFactor);

    currentCard.repetitions += 1;
  }

  // Update ease factor (min 1.3)
  currentCard.easeFactor = Math.max(1.3, currentCard.easeFactor + (0.1 - (5 - rating) * (0.08 + (5 - rating) * 0.02)));

  // Save to persistent storage
  CortexStorage.saveReview(currentCard.id, rating);

  const ratingsLabel = ['Again', 'Hard', 'Good', 'Easy'][rating - 1];
  showToast(`Rated ${ratingsLabel} • Next review in ${currentCard.interval}d`, 'success');

  // Next Card
  setTimeout(() => {
    activeCardIndex = (activeCardIndex + 1) % cards.length;
    renderActiveFlashcard();
  }, 220);
}

/* ==========================================================================
   MODULE 5: MCQs (PRELIMS EXAM SIMULATOR)
   ========================================================================== */
function initMCQsModule() {
  const container = document.getElementById('mcq-questions-container');
  if (!container || !currentTopicData.mcqs) return;

  container.innerHTML = '';
  let correctCount = 0;
  let answeredCount = 0;

  currentTopicData.mcqs.forEach((mcq, qIdx) => {
    const qCard = document.createElement('div');
    qCard.className = 'mcq-question-card';
    qCard.id = `mcq-card-${qIdx}`;

    // Options HTML
    let optionsHtml = '';
    const letters = ['A', 'B', 'C', 'D'];
    mcq.options.forEach((opt, optIdx) => {
      optionsHtml += `
        <div class="mcq-option-item" data-qidx="${qIdx}" data-optidx="${optIdx}">
          <div class="mcq-opt-marker">${letters[optIdx]}</div>
          <div style="flex:1;">${opt}</div>
        </div>
      `;
    });

    qCard.innerHTML = `
      <div class="mcq-meta">
        <span style="font-weight:700; color:var(--primary-light);">Question ${qIdx + 1} of ${currentTopicData.mcqs.length}</span>
        <span class="badge badge-primary">Prelims Paper-1 Pattern</span>
      </div>
      <div class="mcq-statement">${mcq.question.replace(/\n/g, '<br>')}</div>
      <div class="mcq-options-list">
        ${optionsHtml}
      </div>
      <div class="mcq-explanation" id="mcq-exp-${qIdx}">
        <div style="font-weight:700; color:#34d399; margin-bottom:0.35rem;">✓ Detailed Explanation:</div>
        <div>${mcq.explanation}</div>
      </div>
    `;

    container.appendChild(qCard);
  });

  // Click listeners for options
  container.addEventListener('click', (e) => {
    const optionEl = e.target.closest('.mcq-option-item');
    if (!optionEl) return;

    const qIdx = parseInt(optionEl.dataset.qidx, 10);
    const optIdx = parseInt(optionEl.dataset.optidx, 10);
    const mcq = currentTopicData.mcqs[qIdx];
    const parentList = optionEl.parentElement;

    // Check if already answered
    if (parentList.dataset.answered) return;
    parentList.dataset.answered = 'true';
    answeredCount++;

    const isCorrect = optIdx === mcq.correctIndex;
    if (isCorrect) {
      optionEl.classList.add('correct');
      SoundFX.playCorrect();
      correctCount++;
    } else {
      optionEl.classList.add('incorrect');
      SoundFX.playWrong();
      // Highlight correct option
      const correctOptionEl = parentList.querySelectorAll('.mcq-option-item')[mcq.correctIndex];
      if (correctOptionEl) correctOptionEl.classList.add('correct');
    }

    // Reveal explanation
    const expEl = document.getElementById(`mcq-exp-${qIdx}`);
    if (expEl) expEl.style.display = 'block';

    // Update scoreboard
    const scoreEl = document.getElementById('mcq-scoreboard');
    if (scoreEl) {
      const accuracy = Math.round((correctCount / answeredCount) * 100);
      scoreEl.textContent = `Score: ${correctCount}/${answeredCount} (${accuracy}% Accuracy)`;
    }
  });

  // Reset Quiz
  const btnReset = document.getElementById('btn-reset-mcqs');
  if (btnReset) {
    btnReset.addEventListener('click', () => {
      initMCQsModule();
      showToast('MCQ Quiz reset!');
    });
  }
}

/* ==========================================================================
   MODULE 6: MAINS QUESTIONS & ANSWER WRITING
   ========================================================================== */
function initMainsModule() {
  const mains = currentTopicData.mains && currentTopicData.mains[0];
  if (!mains) return;

  const promptEl = document.getElementById('mains-question-prompt');
  if (promptEl) promptEl.textContent = mains.question;

  const textarea = document.getElementById('mains-answer-text');
  const wordCountEl = document.getElementById('mains-word-count');
  const timerEl = document.getElementById('mains-timer-display');
  const btnToggleTimer = document.getElementById('btn-toggle-timer');
  const btnRevealModel = document.getElementById('btn-reveal-model');
  const modelBox = document.getElementById('mains-model-content');

  // Restore cached draft from localStorage
  const draftKey = `mains_draft_${currentTopicData.id}`;
  if (textarea) {
    textarea.value = localStorage.getItem(draftKey) || '';
    updateWordCount();

    textarea.addEventListener('input', () => {
      updateWordCount();
      localStorage.setItem(draftKey, textarea.value);
    });
  }

  function updateWordCount() {
    if (!textarea || !wordCountEl) return;
    const text = textarea.value.trim();
    const words = text ? text.split(/\s+/).length : 0;
    wordCountEl.textContent = `${words} / 250 Words`;
    if (words > 250) wordCountEl.style.color = '#ef4444';
    else wordCountEl.style.color = 'var(--text-muted)';
  }

  // Mains Countdown Timer
  let timerRunning = false;
  if (btnToggleTimer) {
    btnToggleTimer.addEventListener('click', () => {
      if (timerRunning) {
        clearInterval(mainsTimerInterval);
        btnToggleTimer.textContent = '▶ Start Timer';
        timerRunning = false;
      } else {
        timerRunning = true;
        btnToggleTimer.textContent = '⏸ Pause Timer';
        mainsTimerInterval = setInterval(() => {
          if (mainsSecondsRemaining > 0) {
            mainsSecondsRemaining--;
            const mins = Math.floor(mainsSecondsRemaining / 60);
            const secs = mainsSecondsRemaining % 60;
            if (timerEl) {
              timerEl.textContent = `${String(mins).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            }
          } else {
            clearInterval(mainsTimerInterval);
            showToast('Time is up for this 15-marker question!', 'warning');
            SoundFX.playWrong();
          }
        }, 1000);
      }
    });
  }

  // Model Answer & Rubric Breakdown Reveal
  if (btnRevealModel && modelBox) {
    btnRevealModel.addEventListener('click', () => {
      if (modelBox.style.display === 'block') {
        modelBox.style.display = 'none';
        btnRevealModel.textContent = '👁️ Reveal Model Answer & Evaluation Rubric';
      } else {
        modelBox.style.display = 'block';
        btnRevealModel.textContent = '🙈 Hide Model Answer';
        SoundFX.playCorrect();
        renderModelAnswer(mains.modelAnswer);
      }
    });
  }
}

function renderModelAnswer(model) {
  const container = document.getElementById('mains-model-content');
  if (!container || !model) return;

  let bodyHtml = '';
  model.bodySections.forEach(sec => {
    bodyHtml += `
      <div style="margin-bottom:1.25rem;">
        <h5 style="color:#38bdf8; font-size:1.05rem; margin-bottom:0.35rem;">${sec.title}</h5>
        <ul style="padding-left:1.5rem; line-height:1.7;">
          ${sec.points.map(pt => `<li>${pt}</li>`).join('')}
        </ul>
      </div>
    `;
  });

  container.innerHTML = `
    <h4 style="font-family:var(--font-display); font-size:1.3rem; color:#fff; margin-bottom:1rem; border-bottom:1px solid rgba(255,255,255,0.1); padding-bottom:0.5rem;">
      UPSC Model Answer Framework (15 Marks / 250 Words)
    </h4>

    <div class="reading-callout" style="margin-bottom:1.5rem;">
      <strong style="color:#818cf8;">Introduction Strategy (30-40 words):</strong>
      <p style="margin-top:0.3rem;">${model.intro}</p>
    </div>

    ${bodyHtml}

    <div class="reading-callout reading-callout-warning" style="margin-top:1.5rem;">
      <strong style="color:#fbbf24;">Conclusion Hook:</strong>
      <p style="margin-top:0.3rem;">${model.conclusion}</p>
    </div>

    <div style="margin-top:2rem; padding:1.25rem; background:rgba(255,255,255,0.03); border-radius:var(--radius-sm); border:1px solid rgba(255,255,255,0.08);">
      <h5 style="color:#fff; font-size:1rem; margin-bottom:0.75rem;">Self-Evaluation Rubric Checklist:</h5>
      <label style="display:block; margin-bottom:0.5rem; cursor:pointer;"><input type="checkbox"> Structured with crisp Intro, Dimensions & Way Forward</label>
      <label style="display:block; margin-bottom:0.5rem; cursor:pointer;"><input type="checkbox"> Cited key initiatives (SUPACE, SUVAS, FASTER, e-Courts Phase III)</label>
      <label style="display:block; margin-bottom:0.5rem; cursor:pointer;"><input type="checkbox"> Addressed Article 21, Article 14, and Natural Justice Black-Box</label>
      <label style="display:block; cursor:pointer;"><input type="checkbox"> Concluded with balanced Human-in-the-Loop governance</label>
    </div>
  `;
}
