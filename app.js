/**
 * CORTEX ANKI 2.0 - MAIN APPLICATION LOGIC
 * Dashboard Heatmap, Canvas Charting, SRS Engine, and Global Utilities
 */

document.addEventListener('DOMContentLoaded', () => {
  // Update streak counter in navbar
  CortexStorage.updateStreak();

  // If dashboard heatmap element exists, render it
  if (document.getElementById('anki-heatmap')) {
    initDashboard();
  }

  // Setup Global Upload Lecture Modal
  setupUploadModal();
});

/* ==========================================================================
   DASHBOARD INITIALIZATION: HEATMAP & CHARTS
   ========================================================================== */
function initDashboard() {
  renderHeatmap();
  renderRetentionChart();
  renderSRSBreakdownChart();
}

/**
 * Renders an Anki/GitHub style 365-day Activity Heatmap
 */
function renderHeatmap() {
  const container = document.getElementById('anki-heatmap');
  if (!container) return;

  container.innerHTML = '';
  const reviews = CortexStorage.getReviews();
  const tooltip = document.getElementById('heatmap-tooltip') || createTooltip();

  const totalDays = 364; // 52 weeks * 7 days
  const today = new Date();
  
  // Calculate start date (52 weeks ago aligned to Sunday/Monday)
  const startDate = new Date(today);
  startDate.setDate(today.getDate() - totalDays);

  const grid = document.createElement('div');
  grid.className = 'heatmap-grid';

  let currentDate = new Date(startDate);
  
  for (let w = 0; w < 52; w++) {
    const weekCol = document.createElement('div');
    weekCol.className = 'heatmap-week';

    for (let d = 0; d < 7; d++) {
      const dateStr = currentDate.toISOString().split('T')[0];
      const dayData = reviews[dateStr];
      const count = dayData ? dayData.count : 0;

      const cell = document.createElement('div');
      cell.className = `heatmap-cell ${getHeatmapLevel(count)}`;
      cell.dataset.date = dateStr;
      cell.dataset.count = count;

      // Tooltip Events
      cell.addEventListener('mouseenter', (e) => {
        const rect = cell.getBoundingClientRect();
        tooltip.innerHTML = `<strong>${count} cards reviewed</strong> on ${formatDate(dateStr)}`;
        tooltip.style.left = `${rect.left + window.scrollX + rect.width / 2}px`;
        tooltip.style.top = `${rect.top + window.scrollY - 10}px`;
        tooltip.style.display = 'block';
      });

      cell.addEventListener('mouseleave', () => {
        tooltip.style.display = 'none';
      });

      cell.addEventListener('click', () => {
        showToast(`${count} cards reviewed on ${formatDate(dateStr)}`);
      });

      weekCol.appendChild(cell);
      currentDate.setDate(currentDate.getDate() + 1);
    }

    grid.appendChild(weekCol);
  }

  container.appendChild(grid);
}

function getHeatmapLevel(count) {
  if (count === 0) return 'level-0';
  if (count <= 10) return 'level-1';
  if (count <= 25) return 'level-2';
  if (count <= 45) return 'level-3';
  return 'level-4';
}

function createTooltip() {
  const tip = document.createElement('div');
  tip.id = 'heatmap-tooltip';
  document.body.appendChild(tip);
  return tip;
}

function formatDate(isoStr) {
  const d = new Date(isoStr);
  return d.toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' });
}

/**
 * Custom High-Performance Canvas Chart: 14-Day Review Trend
 */
function renderRetentionChart() {
  const canvas = document.getElementById('chart-retention');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();
  
  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  ctx.scale(dpr, dpr);

  const width = rect.width;
  const height = rect.height;
  const padding = { top: 30, right: 25, bottom: 40, left: 45 };

  // Generate 14-day data points
  const points = [];
  const labels = [];
  const reviews = CortexStorage.getReviews();
  const today = new Date();

  for (let i = 13; i >= 0; i--) {
    const d = new Date(today);
    d.setDate(d.getDate() - i);
    const str = d.toISOString().split('T')[0];
    const val = reviews[str] ? reviews[str].count : Math.floor(Math.random() * 20) + 15;
    points.push(val);
    labels.push(d.toLocaleDateString('en-US', { weekday: 'narrow' }));
  }

  const maxVal = Math.max(...points, 60);
  const chartW = width - padding.left - padding.right;
  const chartH = height - padding.top - padding.bottom;

  // Draw Grid Lines
  ctx.strokeStyle = 'rgba(255, 255, 255, 0.06)';
  ctx.lineWidth = 1;
  for (let i = 0; i <= 4; i++) {
    const y = padding.top + (chartH / 4) * i;
    ctx.beginPath();
    ctx.moveTo(padding.left, y);
    ctx.lineTo(width - padding.right, y);
    ctx.stroke();

    // Axis label
    ctx.fillStyle = '#64748b';
    ctx.font = '11px Plus Jakarta Sans, sans-serif';
    ctx.textAlign = 'right';
    const labelVal = Math.round(maxVal - (maxVal / 4) * i);
    ctx.fillText(labelVal, padding.left - 10, y + 4);
  }

  // Draw Gradient Area & Line
  const stepX = chartW / (points.length - 1);
  const coords = points.map((val, idx) => ({
    x: padding.left + idx * stepX,
    y: padding.top + chartH - (val / maxVal) * chartH
  }));

  // Gradient fill
  const gradient = ctx.createLinearGradient(0, padding.top, 0, height - padding.bottom);
  gradient.addColorStop(0, 'rgba(99, 102, 241, 0.45)');
  gradient.addColorStop(1, 'rgba(99, 102, 241, 0.0)');

  ctx.beginPath();
  ctx.moveTo(coords[0].x, height - padding.bottom);
  coords.forEach(pt => ctx.lineTo(pt.x, pt.y));
  ctx.lineTo(coords[coords.length - 1].x, height - padding.bottom);
  ctx.closePath();
  ctx.fillStyle = gradient;
  ctx.fill();

  // Draw Line
  ctx.beginPath();
  coords.forEach((pt, idx) => {
    if (idx === 0) ctx.moveTo(pt.x, pt.y);
    else {
      // Smooth curve
      const prev = coords[idx - 1];
      const cx = (prev.x + pt.x) / 2;
      ctx.quadraticCurveTo(prev.x, prev.y, cx, (prev.y + pt.y) / 2);
    }
  });
  ctx.lineTo(coords[coords.length - 1].x, coords[coords.length - 1].y);
  ctx.strokeStyle = '#6366f1';
  ctx.lineWidth = 3;
  ctx.stroke();

  // Draw points & X-labels
  coords.forEach((pt, idx) => {
    ctx.beginPath();
    ctx.arc(pt.x, pt.y, 4, 0, Math.PI * 2);
    ctx.fillStyle = '#ffffff';
    ctx.fill();
    ctx.strokeStyle = '#4f46e5';
    ctx.lineWidth = 2;
    ctx.stroke();

    // X Axis Label
    ctx.fillStyle = '#94a3b8';
    ctx.font = '11px Plus Jakarta Sans, sans-serif';
    ctx.textAlign = 'center';
    ctx.fillText(labels[idx], pt.x, height - padding.bottom + 20);
  });
}

/**
 * Custom SRS Breakdown Bar/Distribution Chart
 */
function renderSRSBreakdownChart() {
  const canvas = document.getElementById('chart-srs');
  if (!canvas) return;

  const ctx = canvas.getContext('2d');
  const dpr = window.devicePixelRatio || 1;
  const rect = canvas.getBoundingClientRect();

  canvas.width = rect.width * dpr;
  canvas.height = rect.height * dpr;
  ctx.scale(dpr, dpr);

  const categories = [
    { label: 'New', count: 18, color: '#3b82f6' },
    { label: 'Learning', count: 34, color: '#f59e0b' },
    { label: 'Review Due', count: 42, color: '#ec4899' },
    { label: 'Mastered', count: 126, color: '#10b981' }
  ];

  const total = categories.reduce((sum, c) => sum + c.count, 0);
  const width = rect.width;
  const height = rect.height;

  // Draw horizontal stacked bar
  const barY = 50;
  const barHeight = 28;
  const barWidth = width - 40;
  let currentX = 20;

  // Background track
  ctx.fillStyle = 'rgba(255, 255, 255, 0.05)';
  ctx.beginPath();
  ctx.roundRect(20, barY, barWidth, barHeight, 8);
  ctx.fill();

  categories.forEach((cat, idx) => {
    const segW = (cat.count / total) * barWidth;
    ctx.fillStyle = cat.color;
    ctx.beginPath();
    if (idx === 0) {
      ctx.roundRect(currentX, barY, segW, barHeight, [8, 0, 0, 8]);
    } else if (idx === categories.length - 1) {
      ctx.roundRect(currentX, barY, segW, barHeight, [0, 8, 8, 0]);
    } else {
      ctx.rect(currentX, barY, segW, barHeight);
    }
    ctx.fill();
    currentX += segW;
  });

  // Draw Legend & Stats Below
  const legendY = 120;
  const colW = (width - 40) / 2;

  categories.forEach((cat, idx) => {
    const col = idx % 2;
    const row = Math.floor(idx / 2);
    const x = 25 + col * colW;
    const y = legendY + row * 45;

    // Dot
    ctx.fillStyle = cat.color;
    ctx.beginPath();
    ctx.arc(x, y + 6, 6, 0, Math.PI * 2);
    ctx.fill();

    // Label
    ctx.fillStyle = '#f8fafc';
    ctx.font = '600 13px Plus Jakarta Sans, sans-serif';
    ctx.textAlign = 'left';
    ctx.fillText(cat.label, x + 16, y + 6);

    // Percentage & Count
    const pct = Math.round((cat.count / total) * 100);
    ctx.fillStyle = '#94a3b8';
    ctx.font = '12px Plus Jakarta Sans, sans-serif';
    ctx.fillText(`${cat.count} cards (${pct}%)`, x + 16, y + 24);
  });
}

/* ==========================================================================
   UPLOAD LECTURE MODAL & INGESTION ENGINE
   Allows the user to paste lectures or upload lecture files anytime!
   ========================================================================== */
function setupUploadModal() {
  const openBtns = document.querySelectorAll('.btn-open-upload');
  const modal = document.getElementById('upload-modal');
  const closeBtn = document.getElementById('close-upload-modal');
  const cancelBtn = document.getElementById('cancel-upload');
  const form = document.getElementById('upload-lecture-form');

  if (!modal) return;

  openBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      modal.classList.add('active');
    });
  });

  const closeModal = () => modal.classList.remove('active');

  if (closeBtn) closeBtn.addEventListener('click', closeModal);
  if (cancelBtn) cancelBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  // Handle File Drag / Selection
  const fileInput = document.getElementById('lecture-file-input');
  if (fileInput) {
    fileInput.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (file) {
        const reader = new FileReader();
        reader.onload = (event) => {
          const textarea = document.getElementById('lecture-raw-text');
          if (textarea) textarea.value = event.target.result;
          showToast(`Loaded "${file.name}" into text area!`, 'success');
        };
        reader.readAsText(file);
      }
    });
  }

  // Handle Form Submission
  if (form) {
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const title = document.getElementById('lecture-title-input').value.trim() || 'Custom Lecture Topic';
      const subject = document.getElementById('lecture-subject-select').value || 'cava';
      const rawText = document.getElementById('lecture-raw-text').value.trim();

      if (!rawText) {
        showToast('Please paste or write your lecture content first.', 'warning');
        return;
      }

      // Auto-structure the uploaded lecture
      const parsedTopic = parseUserLecture(title, subject, rawText);
      CortexStorage.saveCustomLecture(parsedTopic);

      showToast(`Lecture "${title}" ingested successfully!`, 'success');
      closeModal();

      // If user is on cava or subjects page, redirect or reload to see the new topic
      setTimeout(() => {
        window.location.href = `topic_study.html?custom=${encodeURIComponent(parsedTopic.id)}`;
      }, 700);
    });
  }
}

/**
 * Intelligent client-side lecture parser that extracts key sections,
 * terms, and flashcard templates from raw text.
 */
function parseUserLecture(title, subject, rawText) {
  const id = 'custom-' + Date.now();
  const paragraphs = rawText.split('\n\n').filter(p => p.trim().length > 0);
  
  // Extract simple flashcards from definitions or key sentences
  const flashcards = [];
  const keyTerms = [];

  paragraphs.forEach((p, idx) => {
    const trimmed = p.trim();
    if (trimmed.includes(':') && trimmed.length < 250) {
      const parts = trimmed.split(':');
      const term = parts[0].replace(/^[0-9\.\-\*\#\s]+/, '').trim();
      const def = parts.slice(1).join(':').trim();
      if (term.length > 2 && term.length < 40) {
        keyTerms.push({
          term: term,
          fullForm: 'Core Concept',
          category: 'Key Note',
          desc: def
        });
        flashcards.push({
          id: `card-${id}-${idx}`,
          topic: term,
          category: 'Concept Review',
          front: `Explain the concept and significance of: ${term}`,
          back: def,
          interval: 1,
          easeFactor: 2.5,
          repetitions: 0,
          dueDate: new Date().toISOString().split('T')[0]
        });
      }
    }
  });

  // Default fallback flashcards if none auto-detected
  if (flashcards.length === 0) {
    flashcards.push({
      id: `card-${id}-1`,
      topic: title,
      category: 'Overview',
      front: `What are the central themes discussed in ${title}?`,
      back: paragraphs.slice(0, 2).join('\n\n') || 'Comprehensive study note.',
      interval: 1,
      easeFactor: 2.5,
      repetitions: 0,
      dueDate: new Date().toISOString().split('T')[0]
    });
  }

  return {
    id: id,
    subjectId: subject,
    title: title,
    rawText: rawText,
    syllabusTags: [subject.toUpperCase(), "Uploaded Lecture"],
    readTime: `${Math.max(5, Math.ceil(rawText.split(' ').length / 150))} min read`,
    lastUpdated: "Just Now",
    flashcards: flashcards,
    keyTerms: keyTerms,
    sections: paragraphs.map((p, i) => ({
      id: `sec-${i}`,
      heading: `Section ${i + 1}`,
      content: `<p>${p.replace(/\n/g, '<br>')}</p>`
    }))
  };
}
