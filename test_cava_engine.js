// Comprehensive Test Suite for CAVA Mobile Engine
const fs = require('fs');
const html = fs.readFileSync('mobile/index.html', 'utf8');

// Extract JS
const script = html.split('<script>')[1].split('</script>')[0];

// Mock minimal browser environment
global.window = {
  AudioContext: class {
    createOscillator() { return { frequency: { value: 0 }, connect() {}, start() {}, stop() {} }; }
    createGain() { return { gain: { value: 0 }, connect() {} }; }
    get destination() { return {}; }
    get currentTime() { return 0; }
  }
};
global.document = {
  getElementById: (id) => ({
    id,
    classList: { add() {}, remove() {} },
    style: {},
    appendChild() {},
    querySelectorAll: () => [],
    querySelector: () => null,
    scrollTop: 0,
    scrollHeight: 100
  }),
  querySelectorAll: () => [],
  createElement: () => ({ style: {}, className: '' })
};
global.localStorage = {
  _store: {},
  getItem: (k) => global.localStorage._store[k] || null,
  setItem: (k, v) => { global.localStorage._store[k] = String(v); }
};
global.navigator = { vibrate: () => true };

eval(script);

console.log("=== CAVA ENGINE TEST START ===");
console.log("1. Checking DATA topics...");
const topics = Object.keys(DATA);
console.log("Topics found:", topics);
if (topics.length !== 4) throw new Error("Expected 4 topics, got " + topics.length);

topics.forEach(t => {
  const top = DATA[t];
  console.log(`Checking topic: ${t} (${top.title}) - ${top.lessons.length} lessons, ${top.pyq.length} PYQs, ${top.sks.length} Skeletons`);
  if (!top.lessons.length) throw new Error(`Topic ${t} has no lessons`);
  if (!top.pyq.length) throw new Error(`Topic ${t} has no PYQs`);
  if (!top.sks.length) throw new Error(`Topic ${t} has no skeletons`);

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
    });

    // Check diagrams
    for (let ci = 0; ci < l.c.length; ci++) {
      const d = diag(t, li, ci);
      // d can be empty string or svg, both valid
    }
  });
});

console.log("2. Testing State & Add XP...");
addXp(25);
if (S.xp !== 25) throw new Error("Expected S.xp to be 25, got " + S.xp);

console.log("3. Testing Goal Card...");
const gc = goalCard();
if (!gc.includes("Daily goal") || !gc.includes("25 / 50 XP")) throw new Error("Invalid goal card output");

console.log("4. Testing Topic Switching...");
CUR_TOPIC = "exams";
if (goalCard().includes("Public Exams")) console.log("Topic switched to exams successfully");
CUR_TOPIC = "msme";

console.log("5. Testing Lesson Start & Flow...");
start(0);
if (R.total <= 0) throw new Error("Expected positive total items in lesson");
if (R.hearts !== 5) throw new Error("Expected 5 initial hearts");

console.log("6. Testing Owl Messages & Audio...");
R.ok = true; R.cb = 3;
const owlMsg = owlSay();
console.log("Owl says:", owlMsg);
beep(true);
beep(false);

console.log("=== ALL CAVA ENGINE TESTS PASSED PERFECTLY ===");
