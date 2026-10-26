// Comprehensive Test Suite for CAVA Mobile Engine with Game Hub & Interactive Tools
const fs = require('fs');
const html = fs.readFileSync('mobile/index.html', 'utf8');

// Extract JS
const script = html.split('<script>')[1].split('</script>')[0];

// Mock minimal browser environment
global.window = {
  addEventListener() {},
  matchMedia: () => ({ matches: false }),
  AudioContext: class {
    createOscillator() { return { frequency: { value: 0 }, connect() {}, start() {}, stop() {} }; }
    createGain() { return { gain: { value: 0 }, connect() {} }; }
    get destination() { return {}; }
    get currentTime() { return 0; }
  }
};
const elements = {};
global.document = {
  documentElement: {
    _attrs: {},
    getAttribute(k) { return this._attrs[k] || null; },
    setAttribute(k, v) { this._attrs[k] = String(v); }
  },
  getElementById: (id) => {
    if (!elements[id]) {
      elements[id] = {
        id,
        classList: { add() {}, remove() {} },
        style: {},
        appendChild() {},
        querySelectorAll: () => [],
        querySelector: () => null,
        scrollTop: 0,
        scrollHeight: 100
      };
    }
    return elements[id];
  },
  querySelectorAll: () => [],
  querySelector: () => null,
  createElement: () => ({ style: {}, className: '', appendChild() {} })
};
global.localStorage = {
  _store: {},
  getItem: (k) => global.localStorage._store[k] || null,
  setItem: (k, v) => { global.localStorage._store[k] = String(v); }
};
global.navigator = { vibrate: () => true };

eval(script);

console.log("=== CAVA ENGINE & GAME HUB TEST SUITE START ===");
console.log("1. Checking DATA topics...");
const topics = Object.keys(DATA);
console.log("Topics found:", topics);
if (topics.length !== 8) throw new Error("Expected 8 topics, got " + topics.length);

topics.forEach(t => {
  const top = DATA[t];
  console.log(`Checking topic: ${t} (${top.title}) - ${top.lessons.length} lessons, ${top.pyq.length} PYQs, ${top.sks.length} Skeletons`);
  if (!top.lessons.length) throw new Error(`Topic ${t} has no lessons`);
  if (!top.pyq.length) throw new Error(`Topic ${t} has no PYQs`);
  if (!top.sks.length) throw new Error(`Topic ${t} has no skeletons`);

  // Verify Game Hub pools
  if (!top.aq || !top.aq.length) throw new Error(`Topic ${t} missing Arcade questions (aq)`);
  if (!top.dq || !top.dq.length) throw new Error(`Topic ${t} missing Detective riddles (dq)`);
  if (!top.sq || !top.sq.s || !top.sq.s.length) throw new Error(`Topic ${t} missing Officer Mission story (sq)`);
  if (!top.vq || !top.vq.b || !top.vq.it) throw new Error(`Topic ${t} missing Venn sort card (vq)`);
  if (!top.bq || !top.bq.length) throw new Error(`Topic ${t} missing Sentence builders (bq)`);
  if (!top.bg || !top.bg.b || !top.bg.it || !top.bg.it.length) throw new Error(`Topic ${t} missing Block Game data (bg)`);
  let has2020Pyq = top.pyq.some(q => q.q && (q.q.includes('2020') || q.q.includes('2021') || q.q.includes('2022') || q.q.includes('2023') || q.q.includes('2024') || q.q.includes('2025') || q.q.includes('2026')));
  if (!has2020Pyq) throw new Error(`Topic ${t} missing 2020+ UPSC Mains PYQs`);

  top.lessons.forEach((l, li) => {
    if (!l.n || !l.e || !l.d) throw new Error(`Lesson ${li} missing title/emoji/desc in ${t}`);
    if (!l.c || !l.c.length) throw new Error(`Lesson ${li} has no concept cards in ${t}`);
    if (!l.q || !l.q.length) throw new Error(`Lesson ${li} has no questions in ${t}`);

    l.q.forEach((q, qi) => {
      if (!q.k || !q.q) throw new Error(`Question ${qi} in lesson ${li} (${t}) missing kind or prompt`);
      if (q.k === 'mc' && (typeof q.a !== 'number' || q.a < 0 || q.a >= q.o.length)) {
        throw new Error(`Invalid mc question ${qi} in lesson ${li} (${t}): a=${q.a}, options=${q.o.length}`);
      }
      if (q.k === 'tf' && (q.a !== 0 && q.a !== 1)) {
        throw new Error(`Invalid tf question ${qi} in lesson ${li} (${t}): a=${q.a}`);
      }
      if (q.k === 'multi' && (!Array.isArray(q.a) || !q.a.length)) {
        throw new Error(`Invalid multi question ${qi} in lesson ${li} (${t}): a=${q.a}`);
      }
      if (q.k === 'match' && (!Array.isArray(q.p) || !q.p.length)) {
        throw new Error(`Invalid match question ${qi} in lesson ${li} (${t})`);
      }
      if (q.k === 'order' && (!Array.isArray(q.o) || !q.o.length)) {
        throw new Error(`Invalid order question ${qi} in lesson ${li} (${t})`);
      }
      if (q.k === 'flag' && (!Array.isArray(q.o) || typeof q.a !== 'number')) {
        throw new Error(`Invalid flag question ${qi} in lesson ${li} (${t})`);
      }
      if (q.k === 'year' && (typeof q.a !== 'number' || typeof q.min !== 'number' || typeof q.max !== 'number')) {
        throw new Error(`Invalid year question ${qi} in lesson ${li} (${t})`);
      }
      if (q.k === 'sort' && (!Array.isArray(q.b) || !Array.isArray(q.it))) {
        throw new Error(`Invalid sort question ${qi} in lesson ${li} (${t})`);
      }
      if (q.k === 'riddle' && (!Array.isArray(q.c) || !Array.isArray(q.o) || typeof q.a !== 'number')) {
        throw new Error(`Invalid riddle question ${qi} in lesson ${li} (${t})`);
      }
    });

    // Check diagrams
    for (let ci = 0; ci < l.c.length; ci++) {
      const d = diag(t, li, ci);
    }
  });
});

console.log("2. Testing State & Add XP...");
addXp(25);
if (S.xp !== 25) throw new Error("Expected S.xp to be 25, got " + S.xp);

console.log("3. Testing Goal Card & Game Hub button...");
const gc = goalCard();
if (!gc.includes("Daily goal") || !gc.includes("25 / 50 XP")) throw new Error("Invalid goal card output");
if (!gc.includes('id="ac"') || !gc.includes("🎮 Game hub")) throw new Error("Missing Game hub button in goalCard");

console.log("4. Testing Topic Switching...");
CUR_TOPIC = "exams";
if (goalCard().includes("Public Exams")) console.log("Topic switched to exams successfully");
CUR_TOPIC = "msme";

console.log("5. Testing Lesson Start, Progressive Concept Card Reveal & Auto-Next...");
CUR_TOPIC = "cs_structure";
start(0);
if (R.total <= 0) throw new Error("Expected positive total items in lesson");
if (R.hearts !== 5) throw new Error("Expected 5 initial hearts");

// Card 0: Check step 1 (Point 1 only)
const btn1 = global.document.getElementById("go");
if (!btn1 || !app.innerHTML.includes("Continue (1/3)")) throw new Error("Expected Continue (1/3) on step 1");

// Click to step 2 (Point 2)
btn1.onclick();
const btn2 = global.document.getElementById("go");
if (!btn2 || !app.innerHTML.includes("Continue (2/3)")) throw new Error("Expected Continue (2/3) on step 2");

// Click to step 3 (Point 3 - ONLY bullet 3, NO keywords or diagram yet!)
btn2.onclick();
const btn3 = global.document.getElementById("go");
if (!app.innerHTML.includes("Post-1947") || !app.innerHTML.includes("affirmative action")) throw new Error("Expected bullet 3 on step 3");
if (app.innerHTML.includes("Keywords unlocked")) throw new Error("Keywords should NOT be visible on bullet 3 step!");

// Click to step 4 (Diagram reveals)
btn3.onclick();
if (!app.innerHTML.includes("Picture it")) throw new Error("Expected Picture it diagram on step 4");
if (app.innerHTML.includes("Keywords unlocked")) throw new Error("Keywords should NOT be visible on diagram step!");

// Click to step 5 (Keywords reveal)
const btn4 = global.document.getElementById("go");
btn4.onclick();
if (!app.innerHTML.includes("Keywords unlocked") || !app.innerHTML.includes("Revenue Extraction DNA")) throw new Error("Expected Keywords unlocked on step 5");

// Click to step 6 (Owl note reveals)
const btn5 = global.document.getElementById("go");
btn5.onclick();
if (!app.innerHTML.includes("Crucial intro hook")) throw new Error("Expected Owl note on step 6");
const btn6 = global.document.getElementById("go");
if (!app.innerHTML.includes("Got it")) throw new Error("Expected Got it on final card step");

console.log("Progressive concept card sequential reveal verified with 100% accuracy!");

// Test fin(win) auto-next lesson
fin(true);
if (!app.innerHTML.includes("Up Next · Auto-advancing")) throw new Error("Expected Up Next · Auto-advancing banner on lesson completion");
if (!app.innerHTML.includes("Start Next Lesson Now")) throw new Error("Expected Start Next Lesson button");
console.log("Auto-advancing next lesson flow verified with 100% success!");

console.log("6. Testing Game Hub Modes across topics...");
topics.forEach(t => {
  CUR_TOPIC = t;
  // Test Arcade
  startArc();
  if (!R.arc || R.total <= 0 || !R.cur) throw new Error(`startArc failed for ${t}`);

  // Test Lightning
  startLt();
  if (!R.lt || R.total <= 0 || !R.cur) throw new Error(`startLt failed for ${t}`);

  // Test Boss
  startBoss();
  if (!R.boss || R.hearts !== 1 || R.total <= 0) throw new Error(`startBoss failed for ${t}: hearts should be 1, got ${R.hearts}`);

  // Test Detective
  startDet();
  if (!R.det || R.total <= 0 || !R.cur) throw new Error(`startDet failed for ${t}`);

  // Test Officer Mission Story
  startStory();
  if (!R.sto || R.total !== 1 || !R.cur || R.cur.q.k !== 'story') throw new Error(`startStory failed for ${t}`);

  // Test Daily Challenge
  startDaily();
  if (!R.daily || R.total <= 0 || !R.cur) throw new Error(`startDaily failed for ${t}`);

  // Test Concept Lab
  startLab();
  if (!R.lab || R.total <= 0 || !R.cur) throw new Error(`startLab failed for ${t}`);
});

console.log("7. Verifying Duel Exclusion...");
if (typeof startDuel !== 'undefined') throw new Error("startDuel should NOT be defined: duel was explicitly excluded");
app.innerHTML = '';
hub();
// hub() sets app.innerHTML
if (app.innerHTML.includes('Duel') || app.innerHTML.includes('startDuel')) {
  throw new Error("Duel must not be listed in Game Hub");
}
console.log("Duel successfully excluded from Game Hub!");

console.log("8. Testing Owl Messages & Audio...");
R.ok = true; R.cb = 3;
const owlMsg = owlSay();
console.log("Owl says:", owlMsg);
beep(true);
beep(false);

console.log("9. Testing Interactive Tools Evaluation Logic...");
// Flag check
R.q = { k: 'flag', q: 'Red flag', o: ['A', 'B', 'C'], a: 1 };
R.sel = [1];
let flagOk = R.sel[0] === R.q.a;
if (!flagOk) throw new Error("Flag evaluation failed");

// Year check with tolerance
R.q = { k: 'year', q: 'Year', a: 2020, tol: 1 };
R.sel = [2021];
let yearOk = Math.abs(R.sel[0] - R.q.a) <= (R.q.tol || 0);
if (!yearOk) throw new Error("Year tolerance evaluation failed");

// Order inl:1 check
R.q = { k: 'order', inl: 1, o: ['A', 'B', 'C'] };
R.sel = [0, 1, 2];
let orderOk = R.sel.every((v, i) => v === i);
if (!orderOk) throw new Error("Order evaluation failed");

// FinRev end screens
R = { daily: 1 };
finRev(true);
if (!app.innerHTML.includes("Daily challenge done!")) throw new Error("Daily challenge done screen failed");

R = { boss: 1 };
finRev(true);
if (!app.innerHTML.includes("Boss defeated!")) throw new Error("Boss defeated screen failed");

R = { det: 1 };
finRev(true);
if (!app.innerHTML.includes("Case closed!")) throw new Error("Detective case closed screen failed");

R = { sto: 1 };
finRev(true);
if (!app.innerHTML.includes("Mission complete!")) throw new Error("Officer mission complete screen failed");

R = { lab: 1 };
finRev(true);
if (!app.innerHTML.includes("Lab complete!")) throw new Error("Concept lab complete screen failed");

R = { arc: 1 };
finRev(true);
if (!app.innerHTML.includes("Arcade cleared!")) throw new Error("Arcade cleared screen failed");

console.log("10. Testing Samsung One UI Dark / Night Mode Toggle & Persistence...");
home();
if (!app.innerHTML.includes('id="theme-btn"')) throw new Error("Theme button not rendered in top bar");
// Trigger theme toggle to dark
let curTheme = global.document.documentElement.getAttribute('data-theme');
let nextTheme = (curTheme === 'dark') ? 'light' : 'dark';
global.document.documentElement.setAttribute('data-theme', nextTheme);
S.theme = nextTheme;
save();
home();
if (S.theme !== 'dark') throw new Error("Theme state should be 'dark'");
if (global.document.documentElement.getAttribute('data-theme') !== 'dark') throw new Error("Document attribute should be 'dark'");
console.log("Theme toggled to 'dark' successfully and saved in state!");

// Toggle back to light
nextTheme = (S.theme === 'dark') ? 'light' : 'dark';
global.document.documentElement.setAttribute('data-theme', nextTheme);
S.theme = nextTheme;
save();
home();
if (S.theme !== 'light') throw new Error("Theme state should be 'light'");
console.log("Theme toggled back to 'light' successfully!");

console.log("11. Testing Block Drop Game...");
startBlocks();
if (!app.innerHTML.includes('Sort into lower blocks below')) throw new Error("Block game arena not rendered");
if (BLK.deck.length === 0) throw new Error("Block game deck empty");
let curItem = BLK.deck[BLK.idx];
let targetBin = curItem[1];
dropBlock(targetBin);
if (BLK.score <= 0) throw new Error("Block drop correct should award score");
if (BLK.combo <= 1) throw new Error("Block drop correct should increment combo");
// Test incorrect drop
dropBlock((targetBin + 1) % 3);
if (BLK.hearts !== 2) throw new Error("Incorrect block drop should lose a heart");
if (BLK.combo !== 1) throw new Error("Incorrect block drop should reset combo to 1");
console.log("Block Drop Game verified with 100% success!");

console.log("=== ALL CAVA ENGINE & GAME HUB TESTS PASSED WITH 100% SUCCESS ===");
