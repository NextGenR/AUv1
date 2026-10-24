# 🧠 Cortex Anki 2.0 Pro
### Next-Gen Spaced Repetition, Duolingo Gamified Learning & Roadmap.sh Visual Tree Notes

[![GitHub Pages](https://img.shields.io/badge/Deployment-GitHub%20Pages-success?style=for-the-badge&logo=github)](https://nextgenr.github.io/AUv1/)
[![Syllabus](https://img.shields.io/badge/UPSC-GS--2%20%7C%20GS--3-indigo?style=for-the-badge)](https://nextgenr.github.io/AUv1/)
[![Design](https://img.shields.io/badge/UI-Roadmap.sh%20%2B%20Glassmorphism-facc15?style=for-the-badge)](https://nextgenr.github.io/AUv1/roadmap_notes.html)
[![Mobile](https://img.shields.io/badge/Mobile-100%25%20Responsive-emerald?style=for-the-badge)](https://nextgenr.github.io/AUv1/roadmap_notes.html)

Cortex Anki 2.0 is an advanced cognitive learning and spaced repetition engine tailored for civil services preparation, legal studies, and high-yield value addition. Built with vanilla HTML5, CSS3, and modern JavaScript with zero heavy framework overhead.

---

## 🚀 Live Demo & Pages

- 🗺️ **[Visual Tree Roadmap (`roadmap_notes.html`)](https://nextgenr.github.io/AUv1/roadmap_notes.html)**: Interactive Roadmap.sh-style tree notes with ForumIAS slide-out/bottom-sheet inspector drawer.
- 🎮 **[Duolingo Gamified Path (`public_exam_duo.html`)](https://nextgenr.github.io/AUv1/public_exam_duo.html)**: 10 progressive gamified levels on the Public Examinations (Prevention of Unfair Means) Act & NTA Governance Overhaul.
- ⚡ **[CAVA Subject Hub (`cava.html`)](https://nextgenr.github.io/AUv1/cava.html)**: Topic directory with flashcard decks, flowcharts, and study modules.
- ⚖️ **[AI in the Judiciary Module (`topic_study.html`)](https://nextgenr.github.io/AUv1/topic_study.html)**: 6 comprehensive study modules covering the Supreme Court 3-tier AI pyramid and NCLT precedent.
- 📊 **[Executive Dashboard (`index.html`)](https://nextgenr.github.io/AUv1/index.html)**: Spaced repetition retention metrics, study streaks, and activity heatmaps.

---

## 🌟 Key Features

### 1. 🗺️ Roadmap.sh Visual Tree Architecture
- **Vibrant Yellow Trunk Nodes** (`#ffe600`): Neo-brutalist rounded pill headers along the central vertical blue spine.
- **Dynamic Dotted Bezier Connectors**: Smooth SVG cubic curves connecting trunk concepts to branch cards on desktop.
- **Warm Cream Branch Cards** (`#fef3c7`): Tactile cards with tags, short summaries, and interactive circular checkmarks (`✓`).
- **Milestone Checkpoints**: Floating callout checkpoints between sections summarizing key breakthroughs with one-click deep-dive buttons.
- **Split Multi-Pill Nodes**: Side-by-side grouped pills (e.g., `npm | yarn | pnpm | Bun` style).

### 2. 📋 ForumIAS High-Yield Inspector Drawer
- Slide-out side drawer on desktop and interactive bottom-sheet modal on mobile.
- **Judicial Dicta**: Direct quotes from the Chhattisgarh High Court (*"Paper leak is more heinous than murder"*) and Supreme Court (*"Methyl Isocyanate gas"* warning).
- **Economic Theory of Crime**: Gary Becker's deterrence formula ($\text{Expected Penalty} = \text{Severity} \times \text{Detection Probability} \times \text{Speed}$).
- **Institutional Blueprints**: Dr. K. Radhakrishnan 7-Pillar ISRO-grade testing model (statutory NTA cadre, 2-stage filtering, hybrid digital lockboxes, public test centers only).
- **Text-to-Speech Engine**: Web SpeechSynthesis audio readout with browser synthesizer.

### 3. 🎮 Duolingo-Style Gamified Progression
- 10-level winding road with XP, 5-heart life system, and study streak tracking.
- Interactive question modes:
  - Match-Pairs tiles with flip animations.
  - Tap-to-Order sentence builders.
  - High-yield concept discovery cards.
  - Milestone boss quizzes with immediate feedback.

### 4. 📱 100% Mobile-Friendly Design
- Fully responsive across 320px–1440px viewports.
- The desktop 2-sided roadmap automatically transforms into a clean vertical timeline on mobile with left-pinned spine and touch-friendly cards.
- Bottom sheet drawer with native swipe/drag handle and close controls.

---

## 🛠️ Tech Stack

- **Markup & Layout**: Semantic HTML5 with accessibility attributes (ARIA).
- **Styling**: Vanilla CSS3, Custom Properties, Glassmorphism, Micro-animations, Mobile Media Queries (`style.css`).
- **Logic & Audio**: Vanilla ES6+ JavaScript (`roadmap_engine.js`, `duolingo_engine.js`, `app.js`), Web Audio API sound synthesis.
- **Data Architecture**: Structured JSON/JS datasets (`roadmap_data.js`, `public_exam_data.js`, `lecture_data.js`).

---

## 💻 Local Development

Clone and run locally without installing any npm dependencies:

```bash
git clone https://github.com/NextGenR/AUv1.git
cd AUv1
python -m http.server 8080
```

Open [http://localhost:8080](http://localhost:8080) in your browser.

---

## 📄 License

MIT License © 2026 NextGenR
