# -*- coding: utf-8 -*-
"""
Full Generator for CAVA Mobile Learning App
Coded exactly following the architecture, UX, styling, and mechanics of
Citizen’s Charter_ Learn from Scratch (1).html.
Includes:
- Game Hub (Arcade, Lightning Round, Boss Battle, Detective, Officer Mission, Daily Challenge, Concept Lab - NO duel)
- Interactive Question Tools (Spot the red flag, Timeline year slider, Card sorting, Detective riddles, Sentence builders)
- Multi-topic CAVA integration across MSME, Public Exams, AI Judiciary, Citizen's Charter, and Right to Information.
"""

import json
from scratch_builder import TOPICS

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Cortex CAVA: Learn from Scratch</title>
<link rel="manifest" href="manifest.json">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#14a273">
<link rel="icon" type="image/png" sizes="192x192" href="icons/icon-192.png">
<link rel="icon" type="image/png" sizes="32x32" href="icons/favicon-32.png">
<link rel="apple-touch-icon" href="icons/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--bg:#f4f6f8;--card:#ffffff;--card-sub:#f8fafc;--ink:#111827;--mut:#64748b;--line:#e2e8f0;--acc:#f59e0b;--accd:#d97706;--ok:#16a34a;--okbg:#dcfce7;--no:#dc2626;--nobg:#fee2e2;--sel:#eff6ff;--selb:#2563eb;--chip:#f1f5f9;--hl-bg:rgba(254,215,64,0.36);--hl-line:rgba(245,158,11,0.65);box-sizing:border-box;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}
@media(prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#000000;--card:#141519;--card-sub:#1c1d24;--ink:#f6f7f9;--mut:#94a3b8;--line:#262833;--acc:#f59e0b;--accd:#d97706;--ok:#22c55e;--okbg:#062e1a;--no:#ef4444;--nobg:#381216;--sel:#1e293b;--selb:#3b82f6;--chip:#1c1d24;--hl-bg:rgba(245,158,11,0.26);--hl-line:rgba(245,158,11,0.7)}}
:root[data-theme="dark"]{--bg:#000000;--card:#141519;--card-sub:#1c1d24;--ink:#f6f7f9;--mut:#94a3b8;--line:#262833;--acc:#f59e0b;--accd:#d97706;--ok:#22c55e;--okbg:#062e1a;--no:#ef4444;--nobg:#381216;--sel:#1e293b;--selb:#3b82f6;--chip:#1c1d24;--hl-bg:rgba(245,158,11,0.26);--hl-line:rgba(245,158,11,0.7)}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
html,body{height:100%;margin:0}
body{background:var(--bg);color:var(--ink);font-family:"SamsungOne","Samsung One","Plus Jakarta Sans","Inter",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif;font-weight:500;font-size:16.5px;line-height:1.45;letter-spacing:-0.015em;-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;text-rendering:optimizeLegibility;display:flex;justify-content:center}
h1,h2,h3{letter-spacing:-0.025em;font-weight:800}
#app{width:100%;max-width:480px;height:100%;display:flex;flex-direction:column;position:relative;overflow:hidden}
.top{display:flex;gap:12px;justify-content:flex-end;padding:12px 18px 6px;font-weight:800;align-items:center}
.install-pill{background:#2563eb;color:#fff;border:0;border-bottom:3px solid #1d4ed8;border-radius:999px;padding:4px 12px;font:inherit;font-size:13.5px;font-weight:800;cursor:pointer;display:inline-flex;align-items:center;gap:4px}
.install-pill:active{transform:translateY(1px);border-bottom-width:2px}
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.65);display:flex;align-items:flex-end;justify-content:center;z-index:1000;animation:pop .2s ease-out}
.modal-sheet{background:var(--card);border-top-left-radius:24px;border-top-right-radius:24px;width:100%;max-width:480px;padding:24px 20px calc(24px + env(safe-area-inset-bottom,0px));box-shadow:0 -8px 30px rgba(0,0,0,.3)}
.modal-sheet h2{font-size:22px;margin:0 0 6px;font-weight:800}
.modal-sheet p{color:var(--mut);font-size:15px;line-height:1.4;margin:0 0 16px}
.modal-steps{display:flex;flex-direction:column;gap:10px;margin-bottom:20px}
.modal-step{display:flex;gap:12px;align-items:center;background:var(--bg);border:1.5px solid var(--line);border-radius:14px;padding:10px 14px;font-size:15px;font-weight:700}
.modal-step span.num{width:26px;height:26px;background:var(--acc);color:#2a1a00;border-radius:50%;display:grid;place-items:center;font-size:14px;font-weight:800;flex:none}
.topics{display:flex;gap:8px;overflow-x:auto;padding:6px 18px 12px;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.topics::-webkit-scrollbar{display:none}
.topic-btn{background:var(--card);border:2px solid var(--line);border-bottom-width:4px;border-radius:999px;padding:6px 14px;font:inherit;font-size:14px;font-weight:800;color:var(--mut);cursor:pointer;white-space:nowrap;flex:none}
.topic-btn:active{transform:translateY(2px);border-bottom-width:2px}
.topic-btn.active{background:var(--acc);color:#2a1a00;border-color:var(--accd)}
.home{flex:1;overflow-y:auto;padding:0 18px 24px}
h1{font-size:26px;line-height:1.15;margin:4px 0 4px;font-weight:800}
.sub{color:var(--mut);margin:0 0 16px;font-size:15px;line-height:1.35}
.path{display:flex;flex-direction:column;gap:14px}
.lesson{background:var(--card);border:2px solid var(--line);border-bottom-width:5px;border-radius:18px;padding:14px 16px;display:flex;gap:14px;align-items:center;text-align:left;font:inherit;color:inherit;width:100%;cursor:pointer}
.lesson:active{transform:translateY(2px);border-bottom-width:3px}
.lesson.lock{opacity:.5}
.badge{width:56px;height:56px;border-radius:50%;background:var(--acc);display:grid;place-items:center;font-size:26px;border-bottom:5px solid var(--accd);flex:none}
.lesson.done .badge{background:var(--ok);border-color:#0d7753;color:#fff}
.lesson b{font-size:18px;font-weight:800;display:block}
.lesson small{color:var(--mut);font-size:13.5px}
.qhead{display:flex;align-items:center;gap:12px;padding:12px 16px}
.x{background:none;border:0;font-size:26px;color:var(--mut);cursor:pointer;padding:0 4px;font-family:inherit}
.bar{flex:1;height:14px;background:var(--line);border-radius:9px;overflow:hidden}
.bar i{display:block;height:100%;width:0;background:var(--ok);border-radius:9px;transition:width .35s}
.hearts{font-weight:800;color:var(--no)}
.body{flex:1;overflow-y:auto;padding:8px 18px 190px}
.kind{color:var(--accd);font-weight:800;font-size:15px;margin:0 0 4px}
.q{font-size:21px;line-height:1.25;font-weight:800;margin:0 0 14px}
.fact{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:6px 16px;margin-bottom:14px}
.fact p{margin:10px 0;line-height:1.35}
.chips{display:flex;flex-wrap:wrap;gap:8px}
.chip{background:var(--chip);border-radius:20px;padding:3px 12px;font-weight:700;font-size:14.5px}
.note{margin:14px 0 0;color:var(--mut);font-size:15px}
.opt{display:block;width:100%;text-align:left;background:var(--card);border:2px solid var(--line);border-bottom-width:5px;border-radius:14px;padding:12px 14px;margin-bottom:10px;font:inherit;color:inherit;cursor:pointer}
.opt.sel{background:var(--sel);border-color:var(--selb)}
.opt.gone{opacity:.25;pointer-events:none}
.opt.bad{animation:sh .35s;border-color:var(--no);background:var(--nobg)}
.opt:disabled{cursor:default}
.opt.fl{display:inline-block;width:auto;margin:4px 6px 4px 0}
@keyframes sh{25%{transform:translateX(-6px)}75%{transform:translateX(6px)}}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.cols .opt{font-size:14.5px;margin:0 0 10px;padding:10px}
.slots{min-height:64px;border-bottom:2px solid var(--line);display:flex;flex-direction:column;gap:8px;margin-bottom:16px;padding-bottom:10px}
.slots.w{flex-direction:row;flex-wrap:wrap}
.slots .opt{margin:0;padding:9px 12px;font-size:15.5px}
.ph{color:var(--mut);padding:8px 2px}
.flip{background:var(--card);border:2px dashed var(--selb);border-radius:16px;padding:18px;min-height:130px;cursor:pointer;font-size:17.5px;line-height:1.4}
.flip em{color:var(--mut);font-style:normal}
input[type="range"]{accent-color:var(--acc);margin:16px 0;height:8px;cursor:pointer}
.foot{position:absolute;left:0;right:0;bottom:0;padding:14px 18px calc(18px + env(safe-area-inset-bottom,0px));border-top:2px solid var(--line);background:var(--bg)}
.foot.ok{background:var(--okbg);border-color:transparent}.foot.no{background:var(--nobg);border-color:transparent}
.foot h3{margin:0 0 4px;font-size:21px;font-weight:800}
.foot.ok h3{color:var(--ok)}.foot.no h3{color:var(--no)}
.foot p{margin:0 0 12px;font-size:15.5px;line-height:1.3}
.btn{display:block;width:100%;border:0;border-bottom:5px solid var(--accd);background:var(--acc);color:#2a1a00;font:inherit;font-weight:800;font-size:18px;border-radius:14px;padding:11px;cursor:pointer}
.btn:active{transform:translateY(2px);border-bottom-width:3px}
.btn:disabled{background:var(--line);border-color:var(--mut);color:var(--mut);cursor:default}
.foot.ok .btn{background:var(--ok);border-color:#0d7753;color:#fff}.foot.no .btn{background:var(--no);border-color:#a82a2f;color:#fff}
.two{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.end{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;padding:24px;gap:6px}
.end .big{font-size:76px;line-height:1}
.stats{display:flex;gap:12px;margin:16px 0 28px}
.stat{border:2px solid var(--line);border-radius:14px;padding:10px 18px;background:var(--card);font-weight:800}
.stat small{display:block;color:var(--mut);font-weight:500}
.end .btn{max-width:320px}
.goal{display:flex;gap:14px;align-items:center;background:var(--card);border:2px solid var(--line);border-radius:18px;padding:10px 16px;margin-bottom:12px}
.goal small{display:block;color:var(--mut)}
.home .two{margin-bottom:16px}
.mb{background:var(--card);border:2px solid var(--line);border-bottom-width:5px;border-radius:16px;padding:10px;font:inherit;color:inherit;font-weight:800;cursor:pointer;text-align:center}
.mb:active{transform:translateY(2px);border-bottom-width:3px}
.mb small{display:block;color:var(--mut);font-weight:500}
.dg{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:8px;margin-top:6px}
.tmr{font-weight:800;color:var(--accd);margin:12px 0 0;text-align:center}
.skn{font-size:84px;font-weight:800;text-align:center;line-height:1;margin:18px 0 14px;color:var(--accd)}
.skt .sub{text-align:center;margin-top:14px}
.cf{position:absolute;top:-20px;width:10px;height:14px;border-radius:2px;pointer-events:none;animation:fall 2.2s ease-in forwards}
@keyframes fall{to{transform:translateY(105vh) rotate(720deg)}}
.hero{display:flex;gap:14px;align-items:center;background:linear-gradient(135deg,var(--h),color-mix(in srgb,var(--h) 55%,#000));color:#fff;border-radius:20px;padding:16px;margin-bottom:14px;border-bottom:5px solid color-mix(in srgb,var(--h) 60%,#000)}
.hero .ico{font-size:44px;background:rgba(255,255,255,.2);border-radius:16px;width:68px;height:68px;display:grid;place-items:center;flex:none}
.hero small{opacity:.9;font-weight:700}
.hero h2{margin:0;font-size:23px;line-height:1.15;font-weight:800}
.tile{display:flex;gap:10px;background:var(--card);border:2px solid var(--line);border-left:6px solid var(--h);border-radius:14px;padding:4px 14px 4px 12px;margin-bottom:10px}
.tile p{margin:8px 0;line-height:1.4}
.tile .dot{color:var(--h);margin-top:9px;flex:none}
b,strong,.tile b,.fact b,p b{font-weight:700;color:inherit;background:var(--hl-bg);padding:1.5px 6px;margin:0 1.5px;border-radius:6px;-webkit-box-decoration-break:clone;box-decoration-break:clone;display:inline;box-shadow:inset 0 -2.5px 0 0 var(--hl-line)}
.pop{animation:pop .35s ease-out}
@keyframes pop{from{opacity:0;transform:translateY(14px) scale(.97)}to{opacity:1;transform:none}}
.kw{font-weight:800;margin:16px 0 8px;color:var(--mut)}
.chips .chip{background:var(--h);color:#fff;animation:pop .4s ease-out}
.bub{display:flex;gap:10px;align-items:flex-start;margin-top:14px}
.bub span{font-size:34px}
.bub p{margin:0;background:var(--card);border:2px solid var(--line);border-radius:16px 16px 16px 4px;padding:8px 12px;font-size:15px}
button:focus-visible{outline:3px solid var(--selb);outline-offset:2px}
@media(prefers-reduced-motion:reduce){*{animation:none!important;transition:none!important}}
.blk-arena{display:flex;flex-direction:column;flex:1;min-height:360px;position:relative;justify-content:space-between;padding:10px 0}
.blk-track{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;position:relative;min-height:190px;background:var(--card-sub);border:2px dashed var(--line);border-radius:20px;padding:16px;margin-bottom:12px;overflow:hidden}
.blk-card{background:var(--card);border:2.5px solid var(--selb);border-radius:18px;padding:16px 18px;width:100%;max-width:380px;text-align:center;box-shadow:0 8px 24px rgba(0,0,0,.12);animation:blkDrop 6s linear forwards}
@keyframes blkDrop{0%{transform:translateY(-10px);opacity:.95}100%{transform:translateY(10px);opacity:1}}
.blk-card.catch{transform:scale(0.85);opacity:0;transition:all .25s ease-in}
.blk-term{font-size:19px;font-weight:800;color:var(--ink);margin:0 0 6px;line-height:1.25}
.blk-sub{font-size:13px;color:var(--mut);font-weight:600;margin:0 0 10px}
.blk-timer{height:6px;width:100%;background:var(--line);border-radius:6px;overflow:hidden}
.blk-timer i{display:block;height:100%;background:var(--acc);transition:width .2s linear}
.blk-targets{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px}
.blk-bin{background:var(--card);border:2px solid var(--line);border-bottom-width:5px;border-radius:16px;padding:12px 6px;font:inherit;cursor:pointer;display:flex;flex-direction:column;align-items:center;text-align:center;gap:4px;transition:all .15s}
.blk-bin:active{transform:translateY(2px);border-bottom-width:3px}
.blk-bin.b0{border-color:rgba(239,68,68,.35)}.blk-bin.b0 .b-ico{color:#ef4444}
.blk-bin.b1{border-color:rgba(34,197,94,.35)}.blk-bin.b1 .b-ico{color:#16a34a}
.blk-bin.b2{border-color:rgba(59,130,246,.35)}.blk-bin.b2 .b-ico{color:#2563eb}
.blk-bin.b-ok{border-color:var(--ok)!important;background:var(--okbg)!important}
.blk-bin.b-no{border-color:var(--no)!important;background:var(--nobg)!important;animation:sh .35s}
.blk-bin b{font-size:13.5px;font-weight:800;line-height:1.15;color:var(--ink)}
.blk-bin small{font-size:11px;color:var(--mut);font-weight:700}
.blk-toast{background:var(--card);border:2px solid var(--line);border-radius:14px;padding:10px 14px;font-size:14px;line-height:1.35;margin-top:10px;animation:pop .25s ease-out}
.blk-toast.ok{border-color:var(--ok);background:var(--okbg)}
.blk-toast.no{border-color:var(--no);background:var(--nobg)}
</style></head><body><div id="app"></div>
<script>
var DATA = %TOPICS_JSON%;

var CUR_TOPIC = "msme";
try {
  var ut = new URLSearchParams(window.location.search).get("topic");
  if (ut && DATA[ut]) CUR_TOPIC = ut;
} catch(e) {}
var S = {xp:0, streak:0, done:{}, kw:[], weak:[], dd:''};
var app = document.getElementById("app"), R = {}, IV;

try {
  var s = JSON.parse(localStorage.getItem("cortex_cava_state") || "null");
  if(s) S = s;
} catch(e) {}
if(S.theme && document.documentElement) try { document.documentElement.setAttribute('data-theme', S.theme); } catch(e) {}

function save(){
  try {
    localStorage.setItem("cortex_cava_state", JSON.stringify(S));
  } catch(e) {}
}

S.kw = S.kw || [];
S.weak = S.weak || [];

function today(){ return new Date().toDateString(); }
function addXp(x){
  var t = today();
  if(S.dd !== t){
    var y = new Date(Date.now() - 864e5).toDateString();
    S.streak = S.dd === y ? (S.streak || 0) + 1 : 1;
    S.dd = t;
    S.dx = 0;
  }
  S.dx = (S.dx || 0) + x;
  S.xp = (S.xp || 0) + x;
  save();
}

function curStreak(){
  var y = new Date(Date.now() - 864e5).toDateString();
  return S.dd === today() || S.dd === y ? (S.streak || 0) : 0;
}

function unlock(c){
  c.k.forEach(function(k){
    if(!S.kw.some(function(x){ return x.k === k && x.topic === CUR_TOPIC && x.i === R.i; })) {
      S.kw.push({k: k, topic: CUR_TOPIC, i: R.i});
    }
  });
  save();
}

function owlSay(){
  if(R.ok) return R.cb >= 3 ? 'On fire! ' + R.cb + ' in a row' : ['Spot on!', 'Hoot-standing!', 'Nailed it!', 'Wise choice!'][Math.floor(Math.random()*4)];
  return ['Not quite', 'Almost, hoot again', 'Good try, learn from it'][Math.floor(Math.random()*3)];
}

function beep(ok){
  if(S.mute) return;
  try {
    var a = beep.c || (beep.c = new (window.AudioContext || window.webkitAudioContext)());
    var o = a.createOscillator(), g = a.createGain();
    o.frequency.value = ok ? 660 : 220;
    g.gain.value = 0.05;
    o.connect(g);
    g.connect(a.destination);
    o.start();
    o.stop(a.currentTime + 0.12);
  } catch(e) {}
}

function confetti(){
  var c = ['#e8a317','#14a273','#3d79e8','#d23a40','#7442d6'];
  for(var i = 0; i < 46; i++){
    var s = document.createElement('i');
    s.className = 'cf';
    s.style.cssText = 'left:' + Math.random()*100 + '%;background:' + c[i%5] + ';animation-delay:' + Math.random()*0.6 + 's;animation-duration:' + (1.8 + Math.random()*1.2) + 's';
    app.appendChild(s);
  }
  setTimeout(function(){
    document.querySelectorAll('.cf').forEach(function(e){ e.remove(); });
  }, 3500);
}

function goalCard(){
  var x = S.dd === today() ? (S.dx || 0) : 0, p = Math.min(1, x/50), w = (S.weak || []).filter(function(k){ return k.indexOf(CUR_TOPIC+':') === 0; }).length;
  var kwCount = (S.kw || []).filter(function(k){ return k.topic === CUR_TOPIC; }).length;
  var top = DATA[CUR_TOPIC];
  return '<div class="goal">' +
    '<svg width="64" height="64" viewBox="0 0 64 64" aria-hidden="true">' +
      '<circle cx="32" cy="32" r="26" fill="none" stroke="var(--line)" stroke-width="8"/>' +
      '<circle cx="32" cy="32" r="26" fill="none" stroke="var(--ok)" stroke-width="8" stroke-linecap="round" stroke-dasharray="' + (163.4*p) + ' 163.4" transform="rotate(-90 32 32)"/>' +
    '</svg>' +
    '<div><b>Daily goal</b><small>' + x + ' / 50 XP' + (x >= 50 ? ' · done! 🎉' : '') + '</small></div>' +
  '</div>' +
  '<div class="two">' +
    '<button class="mb" id="vt">🔑 Keyword vault<small>' + kwCount + ' unlocked</small></button>' +
    '<button class="mb" id="wk"' + (w ? '' : ' disabled style="opacity:.5"') + '>🎯 Weak spots<small>' + (w ? w + ' to review' : 'none yet') + '</small></button>' +
  '</div>' +
  '<button class="mb" id="pq" style="width:100%;margin-bottom:12px">📝 PYQ-style practice<small>' + top.pyq.length + ' timed answer drills</small></button>' +
  '<button class="mb" id="sk" style="width:100%;margin-bottom:12px">⏱ 45-second skeleton drill<small>' + top.sks.length + ' timed topics</small></button>' +
  '<button class="mb" id="ac" style="width:100%;margin-bottom:16px">🎮 Game hub<small>arcade, lightning, boss, detective, story, lab</small></button>';
}

function vault(){
  var top = DATA[CUR_TOPIC];
  var h = '<div class="qhead"><button class="x" id="bk" aria-label="Back">←</button><b style="font-size:20px">🔑 ' + top.title + ' Keywords</b></div><div class="body" style="padding-bottom:30px">';
  var ks = (S.kw || []).filter(function(x){ return x.topic === CUR_TOPIC; });
  if(!ks.length) h += '<p class="sub">Complete study cards in this topic to unlock high-yield keywords here.</p>';
  top.lessons.forEach(function(l, i){
    var lks = ks.filter(function(x){ return x.i === i; });
    if(!lks.length) return;
    h += '<p class="kw">' + l.e + ' ' + esc(l.n) + '</p><div class="chips" style="--h:' + top.hue[i % top.hue.length] + '">';
    lks.forEach(function(x){ h += '<span class="chip">' + esc(x.k) + '</span>'; });
    h += '</div>';
  });
  app.innerHTML = h + '</div>';
  document.getElementById('bk').onclick = home;
}

function startReview(){
  var top = DATA[CUR_TOPIC];
  var wks = (S.weak || []).filter(function(k){ return k.indexOf(CUR_TOPIC+':') === 0; }).slice(0, 8);
  var q = wks.map(function(k){
    var parts = k.split(':');
    var lIdx = +parts[1], qIdx = +parts[2];
    return { q: top.lessons[lIdx].q[qIdx], key: k };
  });
  R = { i: 0, ci: 99, queue: q, total: q.length, solved: 0, hearts: 5, mist: 0, xp: 0, review: 1 };
  next();
}

function finRev(win){
  if(R.daily && win && S.dc !== today()){
    S.dc = today();
    addXp(15);
  }
  if(win) addXp(R.xp);
  app.innerHTML = '<div class="end"><div class="big">' + (win ? '🎯' : '💔') + '</div>' +
    '<h1>' + (win ? (R.daily ? 'Daily challenge done!' : R.lab ? 'Lab complete!' : R.boss ? 'Boss defeated!' : R.lt ? 'Lightning round done!' : R.det ? 'Case closed!' : R.sto ? 'Mission complete!' : R.arc ? 'Arcade cleared!' : R.pyq ? 'PYQ drill completed!' : 'Weak spots reviewed!') : 'Out of hearts') + '</h1>' +
    '<p class="sub">' + (win ? '+' + R.xp + ' XP. ' + (R.daily ? 'Daily bonus claimed.' : R.lab ? 'Core concepts locked in.' : R.boss ? 'Mastery unlocked.' : R.lt ? 'Rapid reflexes proven.' : R.det ? 'Clues deciphered.' : R.sto ? 'Governance mission accomplished.' : R.arc ? 'Arcade cleared.' : R.pyq ? 'PYQ drill finished.' : 'Weak spots cleared.') : 'Try again after re-reading the study cards.') + '</p>' +
    '<button class="btn" id="a">Back to lessons</button></div>';
  document.getElementById('a').onclick = home;
  if(win) confetti();
}

function pyTimer(){
  clearInterval(IV);
  var s = 60;
  function t(){
    var e = document.getElementById('tm');
    if(!e){ clearInterval(IV); return; }
    e.textContent = '⏱ ' + s + 's · outline your answer in your head';
    if(s-- <= 0){ clearInterval(IV); R.rev = true; inner(); foot(); }
  }
  t();
  IV = setInterval(t, 1000);
}

function startPyq(){
  var top = DATA[CUR_TOPIC];
  var q = top.pyq.map(function(x){ return { q: x }; });
  R = { i: 0, ci: 99, queue: q, total: q.length, solved: 0, hearts: 99, mist: 0, xp: 0, review: 1, pyq: 1 };
  next();
}

var STEPS = [['Intro Definition', 10], ['Data / Article / Case', 5], ['3 Pros / 3 Cons', 15], ['Committee / Scheme', 5], ['1 Diagram Idea', 5]];
var SK = {};

function skPick(){
  var top = DATA[CUR_TOPIC];
  var h = '<div class="qhead"><button class="x" id="bk" aria-label="Back">←</button><b style="font-size:20px">⏱ 45-second skeleton</b></div><div class="body"><p class="sub">Pick a topic. Five rapid timed steps: say each one aloud before time runs out, then check the model answer.</p>';
  top.sks.forEach(function(s, i){
    h += '<button class="mb" style="width:100%;margin-bottom:10px;text-align:left" data-k="' + i + '">' + esc(s.t) + '<small>about 45 seconds · 5 steps</small></button>';
  });
  app.innerHTML = h + '</div>';
  document.getElementById('bk').onclick = home;
  app.querySelectorAll('[data-k]').forEach(function(b){
    b.onclick = function(){ skStart(+b.dataset.k); };
  });
}

function skStart(k){ SK = { k: k, n: 0, ok: 0 }; skStep(); }
function skStep(){
  clearInterval(IV);
  var st = STEPS[SK.n];
  SK.rev = false;
  SK.left = st[1];
  skDraw();
  IV = setInterval(function(){
    var e = document.getElementById('tm');
    if(!e){ clearInterval(IV); return; }
    SK.left--;
    if(SK.left <= 0){ skReveal(); return; }
    e.textContent = SK.left;
    document.getElementById('tb').style.width = (SK.left / st[1] * 100) + '%';
  }, 1000);
}
function skReveal(){ clearInterval(IV); SK.rev = true; skDraw(); }
function skDraw(){
  var top = DATA[CUR_TOPIC];
  var st = STEPS[SK.n], s = top.sks[SK.k];
  var h = '<div class="qhead"><button class="x" id="quit" aria-label="Quit">✕</button><div class="bar"><i style="width:' + (SK.n/5*100) + '%"></i></div></div><div class="body" style="--h:#d9570c"><p class="kind">' + esc(s.t) + ' · step ' + (SK.n+1) + ' of 5</p><p class="q">' + esc(st[0]) + '</p>';
  if(!SK.rev) h += '<div class="skt"><div id="tm" class="skn">' + SK.left + '</div><div class="bar"><i id="tb" style="width:' + (SK.left/st[1]*100) + '%;background:var(--acc);transition:width 1s linear"></i></div><p class="sub">Say it aloud now. You have ' + st[1] + ' seconds.</p></div>';
  else h += '<div class="tile"><span class="dot">✦</span><p>' + esc(s.s[SK.n]) + '</p></div>';
  h += '</div><div class="foot">' + (SK.rev ? '<div class="two"><button class="btn" id="mi" style="background:var(--no);border-color:#a82a2f;color:#fff">Missed it</button><button class="btn" id="go">Got it</button></div>' : '<button class="btn" id="rv">Reveal answer</button>') + '</div>';
  app.innerHTML = h;
  document.getElementById('quit').onclick = function(){ clearInterval(IV); home(); };
  if(SK.rev){
    document.getElementById('go').onclick = function(){ SK.ok++; skNext(); };
    document.getElementById('mi').onclick = skNext;
  } else {
    document.getElementById('rv').onclick = skReveal;
  }
}
function skNext(){ SK.n++; if(SK.n >= 5) return skEnd(); skStep(); }
function skEnd(){
  var x = SK.ok * 6; addXp(x);
  app.innerHTML = '<div class="end"><div class="big">' + (SK.ok >= 4 ? '🏆' : '⏱') + '</div><h1>' + SK.ok + ' of 5 steps nailed</h1><p class="sub">+' + x + ' XP. ' + (SK.ok >= 4 ? 'Your skeleton is exam-ready.' : 'Run it again to lock weak steps.') + '</p><button class="btn" id="a">Back to lessons</button><button class="btn" id="b" style="margin-top:10px;background:var(--card);color:var(--ink);border-color:var(--line)">Try another topic</button></div>';
  document.getElementById('a').onclick = home;
  document.getElementById('b').onclick = skPick;
  if(SK.ok >= 4) confetti();
}

function hub(){
  var G = [
    ['🎮 Arcade', 'red flags, year slider, card sorting', startArc],
    ['🧱 Block Drop', 'sort falling key terms into solution, challenge, model blocks', startBlocks],
    ['⚡ Lightning round', '8 questions, 10 seconds each', startLt],
    ['👹 Boss battle', '10 questions, one heart only', startBoss],
    ['🕵️ Detective', 'guess from fewer clues', startDet],
    ['🎭 Officer mission', 'branching story, your choices matter', startStory],
    ['📅 Daily challenge', S.dc === today() ? '✅ done today' : '5 new questions, +15 bonus XP', startDaily],
    ['🧪 Concept lab', 'Venn sorting and build-the-sentence', startLab]
  ];
  var top = DATA[CUR_TOPIC];
  var h = '<div class="qhead"><button class="x" id="bk" aria-label="Back">←</button><b style="font-size:20px">🎮 ' + esc(top.title.split('&')[0].trim()) + ' Game Hub</b></div><div class="body">';
  G.forEach(function(g, i){
    h += '<button class="mb" style="width:100%;margin-bottom:10px;text-align:left" data-g="' + i + '">' + g[0] + '<small>' + g[1] + '</small></button>';
  });
  app.innerHTML = h + '</div>';
  document.getElementById('bk').onclick = home;
  app.querySelectorAll('[data-g]').forEach(function(b){
    b.onclick = function(){ G[+b.dataset.g][2](); };
  });
}

function go(q, o){
  R = Object.assign({
    i: 0,
    ci: 99,
    queue: q.map(function(x){ return { q: x }; }),
    total: q.length,
    solved: 0,
    hearts: 5,
    mist: 0,
    xp: 0,
    review: 1
  }, o);
  next();
}

function pool(ks){
  var p = [];
  var top = DATA[CUR_TOPIC];
  top.lessons.forEach(function(l){
    l.q.forEach(function(q){
      if(ks.indexOf(q.k) > -1) p.push(q);
    });
  });
  return sh(p);
}

function startLt(){ go(pool(['mc', 'tf', 'flag']).slice(0, 8), { lt: 1 }); }
function startBoss(){ go(pool(['mc', 'tf', 'multi', 'order', 'flag', 'sort', 'year']).slice(0, 10), { boss: 1, hearts: 1 }); }
function startDet(){ var top = DATA[CUR_TOPIC]; go(top.dq || [], { det: 1 }); }
function startStory(){ var top = DATA[CUR_TOPIC]; go(top.sq ? [top.sq] : [], { sto: 1 }); }
function startLab(){ var top = DATA[CUR_TOPIC]; go((top.vq ? [top.vq] : []).concat(top.bq || []), { lab: 1 }); }
function startArc(){ var top = DATA[CUR_TOPIC]; go(top.aq || [], { arc: 1 }); }

var BLK = {};

function startBlocks(){
  var top = DATA[CUR_TOPIC];
  if (!top.bg || !top.bg.it || !top.bg.it.length) return alert('No block game data for this topic');
  var deck = sh(top.bg.it);
  BLK = {
    deck: deck,
    idx: 0,
    buckets: top.bg.b,
    counts: [0, 0, 0],
    score: 0,
    combo: 1,
    maxCombo: 1,
    hearts: 3,
    mistakes: 0,
    timer: null,
    left: 8,
    paused: false
  };
  blkStep();
}

function blkStep(){
  clearInterval(BLK.timer);
  if (BLK.hearts <= 0 || BLK.idx >= BLK.deck.length) {
    return blkEnd();
  }
  BLK.left = 8;
  BLK.paused = false;
  blkDraw();
  BLK.timer = setInterval(function(){
    var e = document.getElementById('b-sec');
    var bar = document.getElementById('b-tb');
    if (!e || BLK.paused) return;
    BLK.left--;
    e.textContent = BLK.left + 's';
    if (bar) bar.style.width = (BLK.left / 8 * 100) + '%';
    if (BLK.left <= 0) {
      clearInterval(BLK.timer);
      dropBlock(-1);
    }
  }, 1000);
}

function blkDraw(feedback){
  var item = BLK.deck[BLK.idx];
  var bks = BLK.buckets;
  var icons = ['🔴', '🟢', '🔵'];
  var h = '<div class="qhead">' +
    '<button class="x" id="b-quit" aria-label="Quit">✕</button>' +
    '<span style="font-weight:800;color:var(--accd);flex:1;text-align:center">🔥 x' + BLK.combo + ' Combo</span>' +
    '<span style="font-weight:800;color:var(--no)">❤️ ' + BLK.hearts + '</span>' +
  '</div>' +
  '<div class="body" style="padding-bottom:12px">' +
    '<p class="kind" style="text-align:center">Term ' + (BLK.idx + 1) + ' of ' + BLK.deck.length + ' · ' + BLK.score + ' XP</p>' +
    '<div class="blk-arena">' +
      '<div class="blk-track">' +
        '<div class="blk-card" id="b-card">' +
          '<div class="blk-term">' + esc(item[0]) + '</div>' +
          '<div class="blk-sub">Sort into lower blocks below:</div>' +
          '<div class="blk-timer"><i id="b-tb" style="width:' + (BLK.left / 8 * 100) + '%"></i></div>' +
        '</div>' +
        '<div id="b-sec" style="font-size:12.5px;color:var(--mut);font-weight:700;margin-top:6px">' + BLK.left + 's</div>' +
        (feedback || '') +
      '</div>' +
      '<div class="blk-targets">';

  bks.forEach(function(b, i){
    h += '<button class="blk-bin b' + i + '" data-b="' + i + '"' + (BLK.paused ? ' disabled' : '') + '>' +
      '<span class="b-ico" style="font-size:22px">' + icons[i] + '</span>' +
      '<b>' + esc(b) + '</b>' +
      '<small>' + (BLK.counts[i] || 0) + ' sorted</small>' +
    '</button>';
  });

  h += '</div></div></div>';
  app.innerHTML = h;

  document.getElementById('b-quit').onclick = function(){
    clearInterval(BLK.timer);
    hub();
  };

  app.querySelectorAll('[data-b]').forEach(function(btn){
    btn.onclick = function(){
      if (BLK.paused) return;
      dropBlock(+btn.dataset.b);
    };
  });
}

function dropBlock(binIdx){
  clearInterval(BLK.timer);
  BLK.paused = true;
  var item = BLK.deck[BLK.idx];
  var correctIdx = item[1];
  var isOk = binIdx === correctIdx;

  if (isOk) {
    BLK.counts[binIdx] = (BLK.counts[binIdx] || 0) + 1;
    var gain = 10 * BLK.combo;
    BLK.score += gain;
    BLK.combo++;
    if (BLK.combo > BLK.maxCombo) BLK.maxCombo = BLK.combo;
    beep(true);
    var card = document.getElementById('b-card');
    if (card) card.classList.add('catch');
    var btn = app.querySelector('[data-b="' + binIdx + '"]');
    if (btn) btn.classList.add('b-ok');
    var fb = '<div class="blk-toast ok"><b>✓ Correct! +' + gain + ' XP</b> (🔥 x' + BLK.combo + ' combo)<br><small>' + esc(item[2]) + '</small></div>';
    setTimeout(function(){
      BLK.idx++;
      blkStep();
    }, 850);
  } else {
    BLK.hearts--;
    BLK.mistakes++;
    BLK.combo = 1;
    beep(false);
    var btnBad = app.querySelector('[data-b="' + binIdx + '"]');
    if (btnBad) btnBad.classList.add('b-no');
    var btnCorrect = app.querySelector('[data-b="' + correctIdx + '"]');
    if (btnCorrect) btnCorrect.classList.add('b-ok');
    var reason = binIdx === -1 ? '⏱ Out of time!' : '✕ Not quite!';
    var fb = '<div class="blk-toast no"><b>' + reason + '</b><br>Belongs in <b>' + esc(BLK.buckets[correctIdx]) + '</b>.<br><small>' + esc(item[2]) + '</small></div>' +
      '<button class="btn" id="b-next" style="margin-top:10px;padding:8px 16px;font-size:15px">Next Term →</button>';
    blkDraw(fb);
    var nxt = document.getElementById('b-next');
    if (nxt) nxt.onclick = function(){
      BLK.idx++;
      blkStep();
    };
  }
}

function blkEnd(){
  clearInterval(BLK.timer);
  var win = BLK.hearts > 0;
  var total = BLK.deck.length;
  var solved = total - BLK.mistakes;
  var pct = Math.max(0, Math.round(solved / total * 100));
  addXp(BLK.score);

  var h = '<div class="end">' +
    '<div class="big">' + (win ? '🧱' : '💔') + '</div>' +
    '<h1>' + (win ? 'Block Drop Cleared!' : 'Out of Hearts') + '</h1>' +
    '<p class="sub">' + (win ? 'Mastered key terms and conceptual classifications.' : 'Keep drilling to lock in your term reflexes.') + '</p>' +
    '<div class="stats">' +
      '<div class="stat">+' + BLK.score + '<small>XP Earned</small></div>' +
      '<div class="stat">' + pct + '%<small>Accuracy</small></div>' +
      '<div class="stat">🔥 x' + BLK.maxCombo + '<small>Max Combo</small></div>' +
    '</div>' +
    '<button class="btn" id="b-again">Play Again</button>' +
    '<button class="btn" id="b-hub" style="margin-top:10px;background:var(--card);color:var(--ink);border-color:var(--line)">Back to Game Hub</button>' +
  '</div>';

  app.innerHTML = h;
  document.getElementById('b-again').onclick = startBlocks;
  document.getElementById('b-hub').onclick = hub;
  if (win && pct >= 70) confetti();
}

function startDaily(){
  var s = 0, d = today();
  for(var i = 0; i < d.length; i++) s = (s * 31 + d.charCodeAt(i)) % 2147483647;
  var p = [];
  var top = DATA[CUR_TOPIC];
  top.lessons.forEach(function(l){
    l.q.forEach(function(q){
      if(['mc', 'tf', 'multi', 'flag', 'year'].indexOf(q.k) > -1) p.push(q);
    });
  });
  var out = [];
  while(out.length < 5 && p.length){
    s = (s * 48271) % 2147483647;
    out.push(p.splice(s % p.length, 1)[0]);
  }
  go(out, { daily: 1 });
}

function ltTimer(){
  clearInterval(IV);
  var s = 10;
  function t(){
    var k = document.querySelector('.kind');
    if(!k || R.ok !== null){ clearInterval(IV); return; }
    k.textContent = '⚡ Lightning · ' + s + 's';
    if(s-- <= 0){
      clearInterval(IV);
      R.ok = false;
      R.sel = [];
      R.msg = 'Too slow! ' + (R.q.e || '');
      finish();
    }
  }
  t();
  IV = setInterval(t, 1000);
}

function sh(a){
  a = a.slice();
  for(var i = a.length - 1; i > 0; i--){
    var j = Math.floor(Math.random() * (i + 1));
    var t = a[i]; a[i] = a[j]; a[j] = t;
  }
  return a;
}
function esc(t){ return String(t).replace(/&/g,"&amp;").replace(/</g,"&lt;"); }

function tx(x,y,t,fs,f){
  var l = t.split('|');
  return `<text x='${x}' text-anchor='middle' font-size='${fs||13}' font-weight='700' fill='${f||'var(--ink)'}'>` +
    l.map(function(s,i){ return `<tspan x='${x}' y='${y + i*15 - (l.length-1)*7}'>${s}</tspan>`; }).join('') + '</text>';
}
function bx(x,y,w,h,t,f){
  return `<rect x='${x}' y='${y}' width='${w}' height='${h}' rx='10' fill='${f||'var(--card)'}' stroke='var(--h)' stroke-width='2'/>` +
    tx(x+w/2, y+h/2+5, t, 12, f ? '#fff' : 0);
}
function ar(a,b,c,d){
  return `<line x1='${a}' y1='${b}' x2='${c}' y2='${d}' stroke='var(--h)' stroke-width='2.5' marker-end='url(#ar)'/>`;
}

function diag(topic, i, c){
  var k = topic + ':' + i + ':' + c, H = 150, s = '';
  // MSME Diagrams
  if(k === 'msme:0:0'){
    H = 175;
    s = bx(10, 20, 68, 110, '31.1%|GDP', 'var(--h)') +
        bx(85, 10, 68, 120, '35.4%|Mfg GVA', 'var(--h)') +
        bx(160, 5, 68, 125, '48.6%|Exports', 'var(--h)') +
        bx(235, 30, 75, 100, '11.1 Cr|Jobs', 'var(--h)') +
        tx(160, 160, 'Macro Economic Pillars of India', 12, 'var(--mut)');
  }
  else if(k === 'msme:1:1'){
    H = 180;
    s = bx(10, 15, 95, 45, 'Micro|₹1 Cr / ₹5 Cr') +
        ar(105, 37, 135, 37) +
        bx(135, 15, 95, 45, 'Small|₹10 Cr / ₹50 Cr') +
        ar(182, 60, 182, 85) +
        bx(110, 85, 140, 45, 'Medium|₹50 Cr / ₹250 Cr', 'var(--h)') +
        `<path d='M 10 150 Q 160 170 310 150' fill='none' stroke='var(--ok)' stroke-width='2' stroke-dasharray='4'/>` +
        tx(160, 165, 'Export Turnover Excluded from Threshold', 11, 'var(--ok)');
  }
  else if(k === 'msme:2:0'){
    H = 170;
    s = `<polygon points='30,20 290,20 160,140' fill='none' stroke='var(--h)' stroke-width='2.5'/>` +
        tx(160, 45, '99.4% Micro Dwarfs', 14, 'var(--no)') +
        tx(160, 75, '0.52% Small', 12) +
        tx(160, 105, '0.08% Medium', 11) +
        tx(160, 158, 'The Dwarfism Inverted Pyramid', 12, 'var(--mut)');
  }
  else if(k === 'msme:3:1'){
    H = 160;
    s = bx(10, 15, 80, 40, 'Supply|Done') +
        ar(90, 35, 115, 35) +
        bx(115, 15, 90, 40, 'Max 45 Days|Sec 15') +
        ar(205, 35, 230, 35) +
        bx(230, 15, 80, 40, 'Default!','var(--no)') +
        ar(270, 55, 270, 85) +
        bx(30, 85, 260, 45, '3x Bank Rate Compounding & Sec 43B(h) Tax Disallowance','var(--h)');
  }
  else if(k === 'msme:4:1'){
    H = 160;
    s = bx(10, 15, 90, 40, 'GST Data') +
        bx(115, 15, 90, 40, 'TReDS Bill') +
        bx(220, 15, 90, 40, 'Acc. Aggr.') +
        ar(55, 55, 130, 85) + ar(160, 55, 160, 85) + ar(265, 55, 190, 85) +
        bx(40, 85, 240, 45, 'Digital Cash-Flow Underwriting', 'var(--h)');
  }
  else if(k === 'msme:5:1'){
    H = 175;
    s = bx(80, 10, 160, 35, 'PM Vishwakarma (₹13k Cr)', 'var(--h)') +
        ar(110, 45, 45, 80) + ar(160, 45, 160, 80) + ar(210, 45, 275, 80) +
        bx(10, 80, 80, 45, '18 Artisan|Trades') +
        bx(115, 80, 90, 45, '₹15k Toolkit|Grant') +
        bx(230, 80, 80, 45, '₹3L Credit|@ 5%') +
        tx(160, 155, 'Holistic 5-Pillar Artisan Architecture', 12, 'var(--mut)');
  }
  // Public Exams Diagrams
  else if(k === 'exams:0:1'){
    H = 150;
    s = bx(10, 15, 85, 45, 'Breach at|Press / Lab') +
        ar(95, 37, 120, 37) +
        bx(120, 15, 85, 45, '₹30-50L|Per Seat') +
        ar(205, 37, 230, 37) +
        bx(230, 15, 80, 45, 'Merit|Compromised', 'var(--no)') +
        tx(160, 110, 'HC: "Paper leak is more heinous than murder"', 12, 'var(--no)');
  }
  else if(k === 'exams:1:1'){
    H = 170;
    s = bx(10, 100, 140, 45, 'Individual Cheater|3-5 Yrs + ₹10L') +
        ar(150, 122, 170, 72) +
        bx(170, 50, 140, 45, 'Organized Syndicate|5-10 Yrs + ₹1 Cr Min', 'var(--no)') +
        ar(240, 50, 240, 20) +
        bx(170, 5, 140, 35, 'Asset Attachment', 'var(--h)');
  }
  else if(k === 'exams:2:1'){
    H = 160;
    s = bx(10, 20, 95, 45, 'Multi-Stage|Exams') +
        bx(112, 20, 95, 45, 'Hybrid CBT|OMR Mode') +
        bx(214, 20, 95, 45, '100% Govt|Centers (KVs)', 'var(--h)') +
        ar(57, 65, 130, 95) + ar(160, 65, 160, 95) + ar(262, 65, 190, 95) +
        bx(40, 95, 240, 40, 'Radhakrishnan Reform Architecture');
  }
  // Judiciary Diagrams
  else if(k === 'judiciary:0:0'){
    H = 170;
    s = `<polygon points='30,135 290,135 160,20' fill='none' stroke='var(--h)' stroke-width='2.5'/>` +
        tx(160, 55, 'SC: 80,000', 12) +
        tx(160, 85, 'High Courts: 60 Lakh', 12) +
        tx(160, 115, 'District Courts: 4.4 Crore', 13, 'var(--no)') +
        tx(160, 155, 'National Judicial Data Grid: >5 Cr Backlog', 12, 'var(--mut)');
  }
  else if(k === 'judiciary:1:1'){
    H = 160;
    s = bx(15, 30, 130, 70, 'Assistive AI|Translation (SUVAS)|Cause-lists|Document Search') +
        `<line x1='160' y1='10' x2='160' y2='130' stroke='var(--no)' stroke-width='3' stroke-dasharray='6'/>` +
        bx(175, 30, 130, 70, 'Human Judge|Constitutional Morality|Empathy & Conscience|Final Adjudication', 'var(--h)') +
        tx(160, 145, 'Supreme Court Draft AI Boundary Line', 12, 'var(--h)');
  }
  else if(k === 'judiciary:2:0'){
    H = 150;
    s = bx(10, 15, 90, 40, 'SUPACE|Research') +
        bx(115, 15, 90, 40, 'SUVAS|Translate') +
        bx(220, 15, 90, 40, 'FASTER|Bail Orders') +
        ar(55, 55, 130, 85) + ar(160, 55, 160, 85) + ar(265, 55, 190, 85) +
        bx(50, 85, 220, 45, 'e-Courts Phase III (₹7,210 Cr)', 'var(--h)');
  }
  // Citizen's Charter Diagrams
  else if(k === 'charter:0:1'){
    H = 250;
    s = `<line x1='60' y1='20' x2='60' y2='230' stroke='var(--h)' stroke-width='3'/>`;
    [['1991','UK Charter launched'],['1997','India: CMs’ Action Plan'],['2006','Sevottam framework'],['2009','2nd ARC 12th Report'],['2011','Bill (lapsed 2014)']].forEach(function(e,j){
      var y = 25 + j*50;
      s += `<circle cx='60' cy='${y}' r='8' fill='var(--h)'/>` + tx(26, y+5, e[0], 13, 'var(--h)') + tx(205, y+5, e[1]);
    });
  }
  else if(k === 'charter:1:2'){
    H = 145;
    s = bx(20,10,120,44,'Consult') + bx(180,10,120,44,'Set standards') + bx(180,90,120,44,'Publish') + bx(20,90,120,44,'Review & revise') +
        ar(140,32,178,32) + ar(240,54,240,88) + ar(180,112,142,112) + ar(80,88,80,56);
  }
  else if(k === 'charter:2:1'){
    H = 195;
    s = `<g stroke='var(--h)' stroke-width='2'><line x1='160' y1='95' x2='75' y2='48'/><line x1='160' y1='95' x2='245' y2='48'/><line x1='160' y1='95' x2='160' y2='150'/></g>` +
        bx(10,8,130,40,'1 Citizen’s|Charter') + bx(180,8,130,40,'2 Grievance|Redress') + bx(90,150,140,40,'3 Service Delivery|Capability') +
        `<circle cx='160' cy='95' r='32' fill='var(--h)'/>` + tx(160,100,'Sevottam',13,'#fff');
  }
  else if(k === 'charter:3:1'){
    H = 170;
    s = bx(10,110,95,50,'Charter|promise') + bx(112,65,95,50,'Bill 2011|lapsed') + bx(214,20,95,50,'RTS Acts|guarantee','var(--h)') +
        ar(105,135,150,117) + ar(207,90,250,72);
  }
  else if(k === 'charter:5:0'){
    H = 160;
    [['Top-down|design','Co-create|with citizens'],['Citizens|unaware','Local language|+ apps'],['No penalty','Statutory|backing']].forEach(function(p,j){
      var y = 8 + j*50;
      s += bx(10, y, 125, 40, p[0]) + ar(137, y+20, 183, y+20) + bx(185, y, 125, 40, p[1]);
    });
  }
  // RTI Diagrams
  else if(k === 'rti:0:0'){
    H = 260;
    s = `<line x1='60' y1='20' x2='60' y2='240' stroke='var(--h)' stroke-width='3'/>`;
    [['1975','Raj Narain (Art 19(1)(a))'],['1990s','MKSS Jan Sunwais (Rajasthan)'],['1997','Tamil Nadu: First State Law'],['2005','RTI Act 2005 Enacted'],['2024','ADR: Electoral Bonds Struck Down']].forEach(function(e,j){
      var y = 25 + j*50;
      s += `<circle cx='60' cy='${y}' r='8' fill='var(--h)'/>` + tx(26, y+5, e[0], 12, 'var(--h)') + tx(205, y+5, e[1], 12);
    });
  }
  else if(k === 'rti:1:2'){
    H = 175;
    s = bx(10, 15, 80, 45, 'Citizen|Request') +
        ar(90, 37, 120, 37) +
        bx(120, 5, 95, 35, '30 Days|Standard', 'var(--h)') +
        bx(120, 50, 95, 35, '48 Hours|Life & Liberty', 'var(--no)') +
        ar(215, 37, 240, 37) +
        bx(240, 15, 75, 45, '1st / 2nd|Appeal') +
        tx(160, 130, 'Fee Waived for BPL & Free if Delayed', 11, 'var(--ok)');
  }
  else if(k === 'rti:2:0'){
    H = 165;
    s = bx(15, 30, 130, 60, 'Section 8(1)|Categorical|Exemptions') +
        `<line x1='160' y1='10' x2='160' y2='120' stroke='var(--ok)' stroke-width='3' stroke-dasharray='4'/>` +
        bx(175, 30, 130, 60, 'Section 8(2)|Public Interest|Override!', 'var(--h)') +
        ar(175, 60, 145, 60) +
        tx(160, 140, 'Public Interest Trumps Secrecy Provisos', 12, 'var(--ok)');
  }
  else if(k === 'rti:3:2'){
    H = 160;
    s = bx(10, 15, 140, 45, 'Subhash Agarwal (2019)|CJI Office under RTI') +
        bx(170, 15, 140, 45, 'ADR v. UOI (2024)|Electoral Bonds Struck', 'var(--h)') +
        ar(80, 60, 160, 95) + ar(240, 60, 160, 95) +
        bx(30, 95, 260, 40, 'Voters Right to Know under Art 19(1)(a)');
  }
  else if(k === 'rti:5:0'){
    H = 185;
    s = `<circle cx='160' cy='90' r='34' fill='var(--h)'/>` + tx(160, 95, '2nd ARC|Blueprint', 12, '#fff') +
        `<g stroke='var(--h)' stroke-width='2'><line x1='160' y1='90' x2='75' y2='35'/><line x1='160' y1='90' x2='245' y2='35'/><line x1='160' y1='90' x2='160' y2='155'/></g>` +
        bx(10, 15, 125, 40, 'National Coordination|Committee (NCC)') +
        bx(185, 15, 125, 40, '50% Non-Civil|Service Members') +
        bx(80, 145, 160, 35, 'Independent Public Records');
  }

  if(!s) return '';
  return `<p class='kw'>📊 Picture it</p><div class='dg'><svg viewBox='0 0 320 ${H}' width='100%' role='img' aria-label='Diagram'><defs><marker id='ar' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0L8,4L0,8z' fill='var(--h)'/></marker></defs>${s}</svg></div>`;
}

function home(){
  var top = DATA[CUR_TOPIC];
  var topicsHtml = '<div class="topics">';
  Object.keys(DATA).forEach(function(k){
    var t = DATA[k];
    topicsHtml += '<button class="topic-btn' + (k === CUR_TOPIC ? ' active' : '') + '" data-t="' + k + '">' + t.badge + ' ' + esc(t.title.split('&')[0].trim()) + '</button>';
  });
  topicsHtml += '</div>';

  var isInstalled = isStandalone();
  var installBtn = isInstalled ? '' : '<button class="install-pill" id="btn-install" aria-label="Install App on Chrome">📲 Install</button>';
  var docEl = document.documentElement;
  var isDark = docEl && (docEl.getAttribute("data-theme") === "dark" || (!docEl.getAttribute("data-theme") && window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches));
  var themeBtn = '<button class="x" id="theme-btn" aria-label="Toggle Night Mode" style="font-size:18px">' + (isDark ? '☀️' : '🌙') + '</button>';

  var h = '<div class="top">' +
    themeBtn +
    installBtn +
    '<button class="x" id="mt" aria-label="Sound">' + (S.mute ? '🔇' : '🔊') + '</button>' +
    '<span>🔥 ' + curStreak() + '</span>' +
    '<span>⚡ ' + (S.xp || 0) + ' XP</span>' +
  '</div>' +
  topicsHtml +
  '<div class="home">' +
    '<h1>' + top.title + '</h1>' +
    '<p class="sub">' + esc(top.sub) + '</p>' +
    goalCard() +
    '<div class="path">';

  top.lessons.forEach(function(l, i){
    var d = (S.done[CUR_TOPIC] || {})[i];
    h += '<button class="lesson' + (d ? ' done' : '') + '" data-i="' + i + '">' +
      '<span class="badge">' + (d ? '✓' : l.e) + '</span>' +
      '<span><b>' + esc(l.n) + '</b><small>' + esc(l.d) + (d ? ' · best ' + d + '%' : '') + '</small></span>' +
    '</button>';
  });

  app.innerHTML = h + '</div></div>';

  var tb = document.getElementById('theme-btn');
  if (tb) tb.onclick = function(){
    var cur = document.documentElement ? document.documentElement.getAttribute('data-theme') : null;
    var sysDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    var next = (cur === 'dark' || (!cur && sysDark)) ? 'light' : 'dark';
    if (document.documentElement) document.documentElement.setAttribute('data-theme', next);
    S.theme = next;
    save();
    home();
  };

  var ib = document.getElementById('btn-install');
  if (ib) ib.onclick = triggerInstall;

  app.querySelectorAll('.topic-btn').forEach(function(b){
    b.onclick = function(){
      CUR_TOPIC = b.dataset.t;
      home();
    };
  });

  app.querySelectorAll('.lesson').forEach(function(b){
    b.onclick = function(){ start(+b.dataset.i); };
  });

  var v = document.getElementById('vt'), w = document.getElementById('wk');
  if(v) v.onclick = vault;
  if(w) w.onclick = startReview;
  var pq = document.getElementById('pq'); if(pq) pq.onclick = startPyq;
  var sk = document.getElementById('sk'); if(sk) sk.onclick = skPick;
  var ac = document.getElementById('ac'); if(ac) ac.onclick = hub;
  document.getElementById('mt').onclick = function(){ S.mute = !S.mute; save(); home(); };
}

function start(i){
  var top = DATA[CUR_TOPIC];
  var l = top.lessons[i];
  R = {
    i: i,
    ci: 0,
    queue: l.q.map(function(q, n){ return { q: q, key: CUR_TOPIC + ':' + i + ':' + n }; }),
    total: l.c.length + l.q.length,
    solved: 0,
    hearts: 5,
    mist: 0,
    xp: 0
  };
  next();
}

function next(){
  var top = DATA[CUR_TOPIC];
  var l = top.lessons[R.i];
  if(l && R.ci < l.c.length) return card();
  if(R.hearts <= 0) return fin(false);
  if(!R.queue.length) return fin(true);
  R.cur = R.queue.shift();
  clearInterval(IV);
  R.sel = [];
  R.ok = null;
  R.q = R.cur.q;
  var q = R.q;
  if(q.o) R.ord = sh(q.o.map(function(_, i){ return i; }));
  if(q.k === "tf") R.ord = [0, 1];
  if(q.k === "match"){
    R.L = sh(q.p.map(function(_, i){ return i; }));
    R.Rr = sh(q.p.map(function(_, i){ return i; }));
    R.m = [];
    R.pick = null;
    R.err = false;
  }
  if(q.k === "flip") R.rev = false;
  if(q.k === "flag") R.ord = q.o.map(function(_, i){ return i; });
  if(q.k === "sort"){ R.si = 0; R.err = false; R.it = sh(q.it); }
  if(q.k === "story"){ R.so = 0; R.pk = null; R.err = false; }
  if(q.k === "riddle") R.cl = 1;
  if(q.k === "year") R.sel = [Math.round((q.min + q.max) / 2)];
  draw();
}

function head(){
  return '<div class="qhead">' +
    '<button class="x" id="quit" aria-label="Quit lesson">✕</button>' +
    '<div class="bar"><i style="width:' + Math.round(R.solved/R.total*100) + '%"></i></div>' +
    (R.pyq ? '' : '<span class="hearts">❤ ' + R.hearts + '</span>') +
  '</div>';
}

function quit(){
  document.getElementById("quit").onclick = function(){
    if(confirm("Quit this lesson? Progress will be lost.")) {
      clearInterval(IV);
      home();
    }
  };
}

function card(){ R.sh = 1; cardDraw(); }

function cardDraw(){
  var top = DATA[CUR_TOPIC];
  var l = top.lessons[R.i];
  var c = l.c[R.ci], n = c.b.length, all = R.sh >= n, tot = l.c.length;
  var hue = top.hue[R.i % top.hue.length];
  var ico = top.ico[R.i % top.ico.length][R.ci % 3] || l.e;

  var h = head() + '<div class="body" style="--h:' + hue + '">' +
    '<div class="hero"><span class="ico">' + ico + '</span><div><small>' + esc(l.n) + ' · card ' + (R.ci+1) + ' of ' + tot + '</small><h2>' + esc(c.t) + '</h2></div></div>';

  for(var i = 0; i < R.sh; i++){
    h += '<div class="tile' + (i === R.sh-1 && i > 0 ? ' pop' : '') + '"><span class="dot">✦</span><p>' + c.b[i] + '</p></div>';
  }

  if(all){
    unlock(c);
    h += diag(CUR_TOPIC, R.i, R.ci);
    h += '<p class="kw">🔑 Keywords unlocked</p><div class="chips">';
    c.k.forEach(function(k){ h += '<span class="chip">' + esc(k) + '</span>'; });
    h += '</div>';
    if(c.n) h += '<div class="bub"><span>🦉</span><p>' + esc(c.n) + '</p></div>';
  }

  h += '</div><div class="foot"><button class="btn" id="go">' + (all ? 'Got it' : 'Continue (' + R.sh + '/' + n + ')') + '</button></div>';
  app.innerHTML = h;
  quit();
  document.getElementById("go").onclick = function(){
    if(!all){
      R.sh++;
      cardDraw();
      var b = document.querySelector(".body");
      if(b) b.scrollTop = b.scrollHeight;
    } else {
      R.solved++;
      R.ci++;
      next();
    }
  };
}

var KIND = {
  riddle: "Detective: who am I?",
  story: "Officer mission",
  flag: "Spot the red flag",
  year: "Slide to the year",
  sort: "Sort the cards",
  tf: "True or false",
  mc: "Pick one",
  multi: "Select all that apply",
  order: "Put in order",
  match: "Match the pairs",
  flip: "Flip the card"
};

function draw(){
  var q = R.q;
  app.innerHTML = head() + '<div class="body"><p class="kind">' + (KIND[q.k] || '') + '</p><p class="q">' + esc(q.q) + '</p><div id="in"></div></div><div class="foot" id="foot"></div>';
  quit();
  inner();
  foot();
  if(R.lt) ltTimer();
}

function inner(){
  var q = R.q, el = document.getElementById("in"), h = "";
  if(q.k === "mc" || q.k === "riddle" || q.k === "flag" || q.k === "tf" || q.k === "multi"){
    var lab = q.k === "tf" ? ["True", "False"] : q.o;
    if(q.k === "riddle"){
      h = '<div class="fact">';
      for(var c = 0; c < R.cl; c++) h += '<p>🔎 ' + esc(q.c[c]) + '</p>';
      h += '</div>';
      if(R.cl < q.c.length && R.ok === null) {
        h += '<button class="mb" id="nc" style="width:100%;margin-bottom:12px">💡 Next clue (−3 XP)</button>';
      }
    }
    R.ord.forEach(function(i){
      h += '<button class="opt' + (q.k === "flag" ? ' fl' : '') + (R.sel.indexOf(i) > -1 ? ' sel' : '') + '" data-i="' + i + '"' + (R.ok !== null ? ' disabled' : '') + '>' + esc(lab[i]) + '</button>';
    });
    el.innerHTML = h;
    var nc = document.getElementById("nc");
    if(nc) nc.onclick = function(){ R.cl++; R.xp = Math.max(0, R.xp - 3); inner(); };
    el.querySelectorAll(".opt").forEach(function(b){
      b.onclick = function(){
        var i = +b.dataset.i;
        if(q.k === "multi"){
          var p = R.sel.indexOf(i);
          p > -1 ? R.sel.splice(p, 1) : R.sel.push(i);
        } else {
          R.sel = [i];
        }
        inner(); foot();
        if(R.lt && q.k !== "multi"){
          clearInterval(IV);
          R.ok = R.sel[0] === q.a;
          R.msg = undefined;
          finish();
        }
      };
    });
  } else if(q.k === "order"){
    h = '<div class="slots' + (q.inl ? ' w' : '') + '">' + (R.sel.length ? '' : '<span class="ph">Tap the items below in order</span>');
    R.sel.forEach(function(i){
      h += '<button class="opt' + (q.inl ? ' fl' : '') + '" data-r="' + i + '"' + (R.ok !== null ? ' disabled' : '') + '>' + esc(q.o[i]) + '</button>';
    });
    h += '</div>';
    R.ord.forEach(function(i){
      if(R.sel.indexOf(i) < 0) h += '<button class="opt' + (q.inl ? ' fl' : '') + '" data-a="' + i + '"' + (R.ok !== null ? ' disabled' : '') + '>' + esc(q.o[i]) + '</button>';
    });
    el.innerHTML = h;
    el.querySelectorAll("[data-a]").forEach(function(b){
      b.onclick = function(){ R.sel.push(+b.dataset.a); inner(); foot(); };
    });
    el.querySelectorAll("[data-r]").forEach(function(b){
      b.onclick = function(){ R.sel.splice(R.sel.indexOf(+b.dataset.r), 1); inner(); foot(); };
    });
  } else if(q.k === "match"){
    h = '<div class="cols"><div>';
    R.L.forEach(function(i){
      h += '<button class="opt' + (R.pick === i ? ' sel' : '') + (R.m.indexOf(i) > -1 ? ' gone' : '') + '" data-l="' + i + '">' + esc(q.p[i][0]) + '</button>';
    });
    h += '</div><div>';
    R.Rr.forEach(function(i){
      h += '<button class="opt' + (R.m.indexOf(i) > -1 ? ' gone' : '') + '" data-r="' + i + '">' + esc(q.p[i][1]) + '</button>';
    });
    el.innerHTML = h + '</div></div>';
    el.querySelectorAll("[data-l]").forEach(function(b){
      b.onclick = function(){ R.pick = +b.dataset.l; inner(); };
    });
    el.querySelectorAll("[data-r]").forEach(function(b){
      b.onclick = function(){
        if(R.pick === null) return;
        if(R.pick === +b.dataset.r){
          R.m.push(R.pick);
          R.pick = null;
          if(R.m.length === q.p.length){
            R.ok = !R.err;
            finish();
            return;
          }
          inner();
        } else {
          R.err = true;
          R.pick = null;
          inner();
          var bb = el.querySelector('[data-r="' + b.dataset.r + '"]');
          if(bb) bb.classList.add("bad");
        }
      };
    });
  } else if(q.k === "year"){
    var yv = R.sel.length ? R.sel[0] : Math.round((q.min + q.max) / 2);
    el.innerHTML = '<div class="skn" id="yv">' + (R.sel.length ? yv : '?') + '</div><input type="range" id="yr" min="' + q.min + '" max="' + q.max + '" value="' + yv + '" style="width:100%" aria-label="Year"' + (R.ok !== null ? ' disabled' : '') + '>';
    var yr = document.getElementById('yr');
    yr.onchange = yr.oninput = function(){
      R.sel = [+yr.value];
      document.getElementById('yv').textContent = yr.value;
      foot();
    };
  } else if(q.k === "sort"){
    var it = R.it[R.si];
    if(!it){ el.innerHTML = '<p class="sub" style="text-align:center">All sorted!</p>'; return; }
    h = '<p class="ph" style="text-align:center">' + (R.si + 1) + ' of ' + R.it.length + '</p><div class="flip" style="text-align:center;font-weight:800;font-size:22px;display:grid;place-items:center;cursor:default">' + esc(it[0]) + '</div><div class="cols" style="margin-top:16px">';
    q.b.forEach(function(b, j){
      h += '<button class="opt" style="text-align:center;font-weight:800" data-b="' + j + '">' + esc(b) + '</button>';
    });
    el.innerHTML = h + '</div>';
    el.querySelectorAll('[data-b]').forEach(function(b){
      b.onclick = function(){
        if(+b.dataset.b === it[1]){
          R.si++;
          if(R.si >= R.it.length){
            R.ok = !R.err;
            finish();
            return;
          }
          inner();
        } else {
          R.err = true;
          b.classList.add('bad');
        }
      };
    });
  } else if(q.k === "story"){
    var sc = q.s[R.so];
    if(!sc){ el.innerHTML = '<p class="sub" style="text-align:center">Mission complete!</p>'; return; }
    h = '<div class="fact"><p>' + esc(sc.t) + '</p></div>';
    if(R.pk === null){
      sc.o.forEach(function(o, j){
        h += '<button class="opt" data-s="' + j + '">' + esc(o[0]) + '</button>';
      });
    } else {
      var oo = sc.o[R.pk];
      h += '<div class="tile" style="border-left-color:var(--' + (oo[1] ? 'ok' : 'no') + ')"><span class="dot">' + (oo[1] ? '✅' : '⚠️') + '</span><p>' + esc(oo[2]) + '</p></div><button class="btn" id="sn">' + (R.so + 1 >= q.s.length ? 'Finish mission' : 'Next scene') + '</button>';
    }
    el.innerHTML = h;
    el.querySelectorAll('[data-s]').forEach(function(b){
      b.onclick = function(){
        R.pk = +b.dataset.s;
        if(!sc.o[R.pk][1]) R.err = true;
        inner();
      };
    });
    var sn = document.getElementById('sn');
    if(sn) sn.onclick = function(){
      R.pk = null;
      R.so++;
      if(R.so >= q.s.length){
        R.ok = !R.err;
        finish();
      } else {
        inner();
      }
    };
  } else if(q.k === "flip"){
    el.innerHTML = '<div class="flip" id="fl">' + (R.rev ? esc(q.r) : '<em>Think of your answer, then tap to reveal.</em>') + '</div>' + (R.pyq && !R.rev ? '<p class="tmr" id="tm"></p>' : '');
    document.getElementById("fl").onclick = function(){
      clearInterval(IV);
      R.rev = true;
      inner();
      foot();
    };
    if(R.pyq && !R.rev) pyTimer();
  }
}

function foot(){
  var f = document.getElementById("foot"), q = R.q;
  f.className = "foot";
  if(R.ok !== null){
    f.className = "foot " + (R.ok ? "ok" : "no");
    f.innerHTML = '<h3>🦉 ' + owlSay() + '</h3><p>' + esc(R.msg !== undefined ? R.msg : (q.e || "")) + '</p><button class="btn" id="go">Continue</button>';
    document.getElementById("go").onclick = done;
    return;
  }
  if(q.k === "flip"){
    f.innerHTML = R.rev ? '<div class="two"><button class="btn" id="miss" style="background:var(--no);border-color:#a82a2f;color:#fff">Missed it</button><button class="btn" id="got">Got it</button></div>' : '<button class="btn" disabled>Reveal first</button>';
    if(R.rev){
      document.getElementById("got").onclick = function(){ R.ok = true; R.msg = ""; finish(); };
      document.getElementById("miss").onclick = function(){ R.ok = false; R.msg = "We’ll bring it back in a moment."; finish(); };
    }
    return;
  }
  if(q.k === "match" || q.k === "sort" || q.k === "story"){
    f.innerHTML = '<button class="btn" disabled>' + (q.k === "story" ? "Make your choices" : q.k === "sort" ? "Sort every card" : "Match all pairs") + '</button>';
    return;
  }
  var ready = q.k === "order" ? R.sel.length === q.o.length : R.sel.length > 0;
  f.innerHTML = '<button class="btn" id="chk"' + (ready ? '' : ' disabled') + '>Check</button>';
  document.getElementById("chk").onclick = function(){
    var ok;
    if(q.k === "order") ok = R.sel.every(function(v, i){ return v === i; });
    else if(q.k === "multi") ok = R.sel.length === q.a.length && q.a.every(function(v){ return R.sel.indexOf(v) > -1; });
    else if(q.k === "year") ok = Math.abs(R.sel[0] - q.a) <= (q.tol || 0);
    else ok = R.sel[0] === q.a;
    R.ok = ok;
    R.msg = undefined;
    finish();
  };
}

function finish(){
  if(R.ok){ R.xp += 10; R.cb = (R.cb || 0) + 1; }
  else { R.hearts--; R.mist++; R.cb = 0; }
  beep(R.ok);
  try { navigator.vibrate && navigator.vibrate(R.ok ? 15 : [40, 30, 40]); } catch(e) {}
  inner(); foot();
}

function done(){
  var k = R.cur.key, i;
  if(R.ok){
    R.solved++;
    if(k && !R.cur.again){
      i = S.weak.indexOf(k);
      if(i > -1) S.weak.splice(i, 1);
    }
  } else {
    if(k && S.weak.indexOf(k) < 0) S.weak.push(k);
    if(!R.cur.again){
      R.queue.push({ q: R.cur.q, again: true, key: k });
    } else {
      R.solved++;
    }
  }
  save(); next();
}

function fin(win){
  if(R.review) return finRev(win);
  var top = DATA[CUR_TOPIC];
  var l = top.lessons[R.i];
  var nq = l.q.length, pct = Math.max(0, Math.round((nq - R.mist)/nq * 100));
  if(win){
    addXp(R.xp);
    S.done[CUR_TOPIC] = S.done[CUR_TOPIC] || {};
    if(!S.done[CUR_TOPIC][R.i] || S.done[CUR_TOPIC][R.i] < pct) S.done[CUR_TOPIC][R.i] = pct;
    save();
  }
  app.innerHTML = '<div class="end"><div class="big">' + (win ? '🏆' : '💔') + '</div><h1>' + (win ? 'Lesson complete!' : 'Out of hearts') + '</h1><p class="sub">' + (win ? l.n + ' cleared.' : 'Re-read the cards and try again.') + '</p>' +
    (win ? '<div class="stats"><div class="stat">+' + R.xp + '<small>XP</small></div><div class="stat">' + pct + '%<small>Accuracy</small></div><div class="stat">' + R.hearts + '<small>Hearts left</small></div></div>' : '<div style="height:24px"></div>') +
    '<button class="btn" id="a">' + (win ? 'Back to lessons' : 'Try again') + '</button></div>';
  document.getElementById("a").onclick = function(){ win ? home() : start(R.i); };
  if(win) confetti();
}

var deferredInstallPrompt = null;

if ('serviceWorker' in navigator) {
  window.addEventListener('load', function() {
    navigator.serviceWorker.register('sw.js').then(function(reg) {
      console.log('[PWA] Service Worker registered with scope:', reg.scope);
    }).catch(function(err) {
      console.warn('[PWA] Service Worker registration failed:', err);
    });
  });
}

window.addEventListener('beforeinstallprompt', function(e) {
  e.preventDefault();
  deferredInstallPrompt = e;
  var b = document.getElementById('btn-install');
  if (b) b.style.display = 'inline-flex';
});

window.addEventListener('appinstalled', function() {
  deferredInstallPrompt = null;
  var b = document.getElementById('btn-install');
  if (b) b.style.display = 'none';
  confetti();
});

function isStandalone() {
  try {
    return (window.matchMedia && window.matchMedia('(display-mode: standalone)').matches) || (window.navigator && window.navigator.standalone === true);
  } catch(e) {
    return false;
  }
}

function triggerInstall() {
  if (deferredInstallPrompt) {
    deferredInstallPrompt.prompt();
    deferredInstallPrompt.userChoice.then(function(choice) {
      if (choice.outcome === 'accepted') {
        var b = document.getElementById('btn-install');
        if (b) b.style.display = 'none';
      }
      deferredInstallPrompt = null;
    });
  } else {
    showInstallModal();
  }
}

function showInstallModal() {
  var isIOS = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
  var old = document.getElementById('install-modal');
  if (old) old.remove();

  var m = document.createElement('div');
  m.id = 'install-modal';
  m.className = 'modal-overlay';
  m.innerHTML = '<div class="modal-sheet">' +
    '<h2>📲 Install on Chrome / Mobile</h2>' +
    '<p>Install this app on your device for 1-tap home screen access, ultra-smooth offline drills, and a clean full-screen learning window.</p>' +
    '<div class="modal-steps">' +
      (isIOS ?
        '<div class="modal-step"><span class="num">1</span><span>Tap the <b>Share button</b> (⎋) at the bottom</span></div>' +
        '<div class="modal-step"><span class="num">2</span><span>Scroll down & tap <b>"Add to Home Screen"</b></span></div>' +
        '<div class="modal-step"><span class="num">3</span><span>Tap <b>Add</b> in the top right</span></div>'
      :
        '<div class="modal-step"><span class="num">1</span><span>Tap the <b>three dots menu (⋮)</b> in Chrome</span></div>' +
        '<div class="modal-step"><span class="num">2</span><span>Tap <b>"Install app"</b> or <b>"Add to Home screen"</b></span></div>' +
        '<div class="modal-step"><span class="num">3</span><span>Confirm <b>Install</b></span></div>'
      ) +
    '</div>' +
    '<button class="btn" id="modal-close">Got it</button>' +
  '</div>';
  document.body.appendChild(m);
  document.getElementById('modal-close').onclick = function() { m.remove(); };
  m.onclick = function(e) { if (e.target === m) m.remove(); };
}

home();
</script></body></html>
"""

def generate():
    topics_json_str = json.dumps(TOPICS, ensure_ascii=False)
    rendered_html = HTML_TEMPLATE.replace("%TOPICS_JSON%", topics_json_str)

    # 1. Write to mobile/index.html
    mobile_index_path = r"d:\Anki_Upgraded\mobile\index.html"
    with open(mobile_index_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated mobile index at {mobile_index_path} ({len(rendered_html)} bytes)")

    # 2. Write to root CAVA_Learn_from_Scratch.html
    root_cava_path = r"d:\Anki_Upgraded\CAVA_Learn_from_Scratch.html"
    with open(root_cava_path, "w", encoding="utf-8") as f:
        f.write(rendered_html)
    print(f"Generated root CAVA file at {root_cava_path} ({len(rendered_html)} bytes)")

    # 3. Write to root Citizen’s Charter_ Learn from Scratch.html
    root_charter_path = r"d:\Anki_Upgraded\Citizen’s Charter_ Learn from Scratch.html"
    charter_html = rendered_html.replace('var CUR_TOPIC = "msme";', 'var CUR_TOPIC = "charter";')
    with open(root_charter_path, "w", encoding="utf-8") as f:
        f.write(charter_html)
    print(f"Generated Citizen's Charter file at {root_charter_path} ({len(charter_html)} bytes)")

if __name__ == "__main__":
    generate()
