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
.gs-explorer{padding:2px 18px 8px;display:flex;flex-direction:column;gap:8px}
.paper-row{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.paper-row::-webkit-scrollbar{display:none}
.paper-btn{background:var(--card);border:2px solid var(--line);border-bottom-width:4px;border-radius:12px;padding:6px 12px;font:inherit;font-size:13px;font-weight:800;color:var(--mut);cursor:pointer;flex:none;transition:all .15s}
.paper-btn:active{transform:translateY(2px);border-bottom-width:2px}
.paper-btn.active{background:#2563eb;color:#fff;border-color:#1d4ed8;box-shadow:0 4px 12px rgba(37,99,235,0.25)}
.domain-row{display:flex;gap:6px;overflow-x:auto;scrollbar-width:none;-webkit-overflow-scrolling:touch}
.domain-row::-webkit-scrollbar{display:none}
.domain-btn{background:var(--card-sub);border:1.5px solid var(--line);border-radius:999px;padding:5px 12px;font:inherit;font-size:12.5px;font-weight:700;color:var(--ink);cursor:pointer;flex:none;transition:all .15s}
.domain-btn:active{transform:translateY(1px)}
.domain-btn.active{background:var(--acc);color:#2a1a00;border-color:var(--accd);box-shadow:0 2px 8px rgba(245,158,11,0.25)}
.theme-card-box{background:var(--card);border:2px solid var(--line);border-radius:16px;overflow:hidden;margin-bottom:14px;box-shadow:0 4px 16px rgba(0,0,0,0.03)}
.theme-item{display:flex;justify-content:space-between;align-items:center;padding:12px 14px;border-bottom:1px solid var(--line);cursor:pointer;text-align:left;transition:background .15s}
.theme-item:last-child{border-bottom:0}
.theme-item:hover{background:var(--sel)}
.theme-item.active{background:var(--sel);border-left:4px solid #2563eb}
.theme-left{display:flex;flex-direction:column;gap:2px;flex:1;min-width:0;padding-right:8px}
.theme-title{font-size:15px;font-weight:800;color:var(--ink);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.theme-desc{font-size:11.5px;color:var(--mut);line-height:1.25;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}
.theme-years{font-size:13.5px;font-weight:800;color:var(--ink);letter-spacing:-0.01em;white-space:nowrap;flex:none}
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

/* Governance Mobile Master Styles */
.gov-box{background:var(--card);border:2px solid var(--line);border-radius:16px;padding:14px;margin-bottom:12px}
.gov-pyq-box{background:var(--card-sub);border:2px dashed var(--selb);border-radius:14px;padding:12px 14px;margin-bottom:12px}
.gov-demand{background:rgba(245,158,11,0.08);border:2px solid rgba(245,158,11,0.35);border-radius:14px;padding:12px 14px;margin-bottom:12px;font-size:14.5px;line-height:1.4}
.gov-demand b{background:var(--hl-bg);color:var(--ink)}
.gov-quote{background:var(--card-sub);border:2px solid var(--line);border-left:5px solid var(--selb);border-radius:14px;padding:12px 14px;margin-bottom:12px;font-size:15px;line-height:1.4}
.gov-triad-card{background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:10px}
.gov-tag{display:inline-block;font-size:11px;font-weight:800;text-transform:uppercase;padding:2px 7px;border-radius:6px;margin-bottom:4px}
.gov-tag.struct{background:rgba(37,99,235,0.18);color:#60a5fa}
.gov-tag.cult{background:rgba(245,158,11,0.18);color:#fbbf24}
.gov-tag.imp{background:rgba(239,68,68,0.18);color:#f87171}
.flag-seg{display:inline-block;padding:4px 8px;margin:3px 2px;border-radius:8px;border:1.5px solid var(--line);background:var(--card);cursor:pointer;font-weight:700;font-size:14px}
.flag-seg.ok{border-color:var(--ok);background:var(--okbg);color:var(--ok)}
.flag-seg.bad{border-color:var(--no);background:var(--nobg);color:var(--no)}
.gov-sort-box{background:var(--card-sub);border:2px dashed var(--line);border-radius:14px;padding:12px;text-align:center;min-height:55px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:14.5px;margin-bottom:10px}
.gov-fb{display:none;border-radius:12px;padding:10px 12px;margin-top:10px;font-size:13.5px;line-height:1.35}
.gov-fb.ok{display:block;background:var(--okbg);border:1.5px solid var(--ok);color:var(--ok)}
.gov-fb.no{display:block;background:var(--nobg);border:1.5px solid var(--no);color:var(--no)}

</style></head><body><div id="app"></div>
<script>
var DATA = %TOPICS_JSON%;

var CUR_TOPIC = "cs_structure";
try {
  var ut = new URLSearchParams(window.location.search).get("topic");
  if (ut && DATA[ut]) CUR_TOPIC = ut;
} catch(e) {}
var S = {xp:0, streak:0, done:{}, kw:[], weak:[], dd:'', paper:'gs2', domain:'governance'};
var app = document.getElementById("app"), R = {}, IV;

var SYLLABUS = {
  gs1: {
    name: "GS 1",
    label: "Heritage, Geography & Society",
    domains: {
      history: {
        name: "History & Art",
        ico: "🏺",
        themes: [
          { id: "art", title: "1. Ancient & Medieval Architecture", years: "2018, 2022", desc: "Temple architecture, Indo-Islamic forms & rock-cut caves" },
          { id: "modern", title: "2. Modern Freedom Struggle", years: "2019, 2023", desc: "Tribal uprisings, Gandhian mass movements & revolutionary nationalists" }
        ]
      },
      geography: {
        name: "Geography",
        ico: "🌋",
        themes: [
          { id: "clim", title: "1. Monsoon Dynamics & Climatology", years: "2020, 2024", desc: "El Nino, Indian Ocean Dipole & Western Disturbances" },
          { id: "res", title: "2. Critical Mineral & Energy Resources", years: "2021, 2023", desc: "Lithium reserves, rare earths & renewable geography" }
        ]
      },
      society: {
        name: "Society",
        ico: "👥",
        themes: [
          { id: "women", title: "1. Women's Empowerment & Demographic Shifts", years: "2020, 2024", desc: "Care economy, declining fertility rates & silver economy" },
          { id: "secular", title: "2. Communalism, Regionalism & Secularism", years: "2019, 2023", desc: "Linguistic reorganization, cultural pluralism & urban integration" }
        ]
      }
    }
  },
  gs2: {
    name: "GS 2",
    label: "Governance, Constitution, Polity & IR",
    domains: {
      governance: {
        name: "Governance",
        ico: "🏛️",
        themes: [
          { id: "gov_theme_1", title: "1. Transparency, Accountability & E-Gov", years: "2018, 2023", desc: "Important aspects of governance, transparency and accountability, e-governance applications, models, citizens charters & institutional measures.", topic: "charter" },
          { id: "gov_theme_2", title: "2. Role of Civil Services in a Democracy 🎯", years: "2016, 2017, 2020, 2024, 2026", desc: "Colonial legacy, generalist vs specialist, democratic ethos, institutional quality & reforms (3 Core Clusters Mapped)", isTheme2: true },
          { id: "gov_theme_3", title: "3. Development Processes & Industry (NGOs/SHGs)", years: "2015, 2021, 2023", desc: "Role of NGOs, SHGs, various groups and associations, donors, charities, institutional and other stakeholders.", isTheme3: true },
          { id: "gov_theme_4", title: "4. Government Policies & Interventions", years: "2017, 2019, 2024", desc: "Government policies and interventions for development in various sectors and issues arising out of their design and implementation.", isTheme4: true },
          { id: "gov_theme_5", title: "5. Pressure Groups & Quasi-Judicial Bodies", years: "2016, 2019, 2023", desc: "Pressure groups and formal/informal associations and their role in the Polity (or statutory, regulatory & quasi-judicial bodies).", isTheme5: true }
        ]
      },
      polity: {
        name: "Polity",
        ico: "🏛️",
        themes: [
          { id: "judiciary", title: "1. AI in Judiciary & Judicial Reforms", years: "2023, 2025", desc: "e-Courts Phase III, SUPACE, Constitutional morality vs algorithms", topic: "judiciary" },
          { id: "federalism", title: "2. Federal Dynamics & Inter-State Water", years: "2020, 2024", desc: "Article 262, Finance Commission transfers & Governor's discretionary powers" },
          { id: "elections", title: "3. Electoral Reforms & Political Finance", years: "2021, 2024", desc: "Electoral bonds ADR judgment, ECI independence & Model Code" }
        ]
      },
      justice: {
        name: "Social Justice",
        ico: "🤝",
        themes: [
          { id: "dbt", title: "1. Tech-Enabled Welfare Delivery (DBT, JAM)", years: "2013, 2014, 2022", desc: "JAM Trinity, Inclusion vs Exclusion errors, ABPS & Women cash transfers", topic: "dbt" },
          { id: "health_edu", title: "2. Public Health & Primary Education", years: "2020, 2023", desc: "Ayushman Bharat, out-of-pocket expenditure & Foundational Literacy" },
          { id: "vulnerable", title: "3. Vulnerable Sections & Social Security", years: "2021, 2024", desc: "Senior citizens, Transgender welfare & Forest Rights Act compliance" }
        ]
      },
      ir: {
        name: "IR",
        ico: "🌐",
        themes: [
          { id: "neighborhood", title: "1. Neighborhood First & Indian Ocean Region", years: "2022, 2024", desc: "SAGAR doctrine, Colombo Security Conclave & border connectivity" },
          { id: "multilateral", title: "2. Global South & Strategic Autonomy", years: "2023, 2025", desc: "G20 legacy, Quad, BRICS expansion & reformed multilateralism" }
        ]
      }
    }
  },
  gs3: {
    name: "GS 3",
    label: "Economy, Agriculture, Tech, Environment & Security",
    domains: {
      economy: {
        name: "Economy",
        ico: "📈",
        themes: [
          { id: "msme", title: "1. MSME Reforms & Economic Catalysts", years: "2020, 2023", desc: "31.1% GDP growth engine, 2020 definition, Section 43B(h), TReDS", topic: "msme" },
          { id: "infra", title: "2. Infrastructure Delivery & PM Gati-Shakti", years: "2013, 2019, 2022", desc: "NPG 3-tier GIS platform, NMP 2.0 asset recycling, SASCI & ULIP", topic: "infra" },
          { id: "agriculture", title: "3. Agri Supply Chains & Post-Harvest Losses", years: "2021, 2024", desc: "e-NAM, Quick Commerce, Cold chain infrastructure & FPOs" }
        ]
      },
      tech_sec: {
        name: "Tech & Security",
        ico: "⚡",
        themes: [
          { id: "frontier_tech", title: "1. Frontier Tech & Semiconductor Mission", years: "2023, 2024", desc: "AI governance, India Semiconductor Mission & Quantum computing" },
          { id: "climate_action", title: "2. Climate Mitigation & Green Hydrogen", years: "2022, 2024", desc: "Panchamrit, Carbon Border Adjustment Mechanism (CBAM) & COP targets" },
          { id: "internal_sec", title: "3. Cybersecurity & Border Management", years: "2020, 2023", desc: "Smart border fencing, Drone warfare & critical infrastructure defense" }
        ]
      }
    }
  },
  gs4: {
    name: "GS 4",
    label: "Ethics, Integrity, Aptitude & Probity",
    domains: {
      ethics: {
        name: "Ethics & Probity",
        ico: "⚖️",
        themes: [
          { id: "civil_values", title: "1. Foundational Values for Civil Services", years: "2019, 2022", desc: "Integrity, impartiality, objectivity, dedication & empathy for weaker sections" },
          { id: "probity", title: "2. Probity in Governance & Anti-Corruption", years: "2020, 2024", desc: "Lokpal, CVC, Whistleblowers protection & Conflict of Interest code" },
          { id: "case_dilemmas", title: "3. Ethical Dilemmas & Applied Case Studies", years: "2021, 2024", desc: "Balancing rules with compassion, public protest crisis & whistleblowing" }
        ]
      }
    }
  }
};




function showTheme2Modal(){
  var m = document.createElement('div');
  m.className = 'modal-overlay';
  var h = '<div class="modal-sheet" style="max-height:85vh;overflow-y:auto">' +
    '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
      '<span class="theme-tag" style="background:#2563eb;color:#fff;padding:3px 10px;border-radius:999px;font-size:12px;font-weight:800">Theme 2 · 5 PYQs Clustered</span>' +
      '<button class="x" id="modal-x" style="font-size:22px">×</button>' +
    '</div>' +
    '<h2 style="font-size:20px;margin:4px 0 6px">Role of Civil Services in a Democracy</h2>' +
    '<p style="font-size:13.5px;color:var(--mut);margin:0 0 12px">These 5 PYQs are clubbed into 3 core thematic clusters covering Structure, Ethos & Institutional Quality:</p>' +
    
    '<!-- Cluster 1 -->' +
    '<div style="background:rgba(37,99,235,0.08);border:2px solid #2563eb;border-radius:14px;padding:12px;margin-bottom:10px">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">' +
        '<b style="color:var(--ink);font-size:15px">Cluster 1: Structure & Colonial Legacy</b>' +
        '<span style="background:var(--okbg);color:var(--ok);font-size:11px;font-weight:800;padding:2px 6px;border-radius:4px">Ready</span>' +
      '</div>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin-bottom:4px">Target PYQs: 2016 (Q14) & 2026 (Q8)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0 0 10px;line-height:1.35">Weberian hierarchy, silos, 3Cs fear, red-tapism vs development; Northcote-Trevelyan generalist premise vs modern knowledge economy.</p>' +
      '<button class="btn" id="btn-play-cluster1" style="background:#2563eb;border-color:#1d4ed8;color:#fff;font-size:15px;padding:8px">🚀 Learn this Chapter →</button>' +
    '</div>' +

    '<!-- Cluster 2 -->' +
    '<div style="background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:10px">' +
      '<b style="color:var(--ink);font-size:14.5px">Cluster 2: Democratic Ethos & Public Trust</b>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin:2px 0 4px">Target PYQs: 2017 (Part A) & 2024 (Q8)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0;line-height:1.35">Neutrality, anonymity, committed bureaucracy, Hota Committee & Sevottam model.</p>' +
    '</div>' +

    '<!-- Cluster 3 -->' +
    '<div style="background:var(--card-sub);border:1.5px solid var(--line);border-radius:14px;padding:12px;margin-bottom:14px">' +
      '<b style="color:var(--ink);font-size:14.5px">Cluster 3: Institutional Quality & Reforms</b>' +
      '<div style="font-size:12px;color:var(--accd);font-weight:700;margin:2px 0 4px">Target PYQs: 2017 (Part B) & 2020 (Q7)</div>' +
      '<p style="font-size:12.5px;color:var(--mut);margin:0;line-height:1.35">Mission Karmayogi (FRAC), 360-degree APAR, Baswan & Surinder Nath recommendations.</p>' +
    '</div>' +

    '<button class="btn" id="modal-close-btn" style="background:var(--line);color:var(--ink);border-color:var(--mut);font-size:15px;padding:8px">Close</button>' +
  '</div>';

  m.innerHTML = h;
  document.body.appendChild(m);
  var cb = document.getElementById('modal-close-btn'), cx = document.getElementById('modal-x'), cp = document.getElementById('btn-play-cluster1');
  if (cb) cb.onclick = function(){ m.remove(); };
  if (cx) cx.onclick = function(){ m.remove(); };
  if (cp) cp.onclick = function(){ m.remove(); startGovCluster1(); };
  m.onclick = function(e){ if (e.target === m) m.remove(); };
}

var GSTEP = 0;
var GTOTAL = 17;
var GXP = 0;

function startGovCluster1(){
  GSTEP = 0;
  GXP = 0;
  drawGovScreen();
}

function drawGovScreen(){
  var pct = Math.round((GSTEP / (GTOTAL - 1)) * 100);
  var headHtml = '<div class="qhead">' +
    '<button class="x" id="gov-quit" aria-label="Quit">✕</button>' +
    '<div class="bar"><i style="width:' + pct + '%;background:linear-gradient(90deg,#2563eb,#10b981)"></i></div>' +
    '<span style="font-size:12.5px;font-weight:800;color:var(--accd);white-space:nowrap">' + (GSTEP+1) + '/' + GTOTAL + '</span>' +
  '</div>';

  var bodyHtml = '';
  var footHtml = '';

  if (GSTEP === 0) {
    // PYQ 1
    bodyHtml = '<div class="body">' +
      '<p class="kind">TARGET PYQ 1 OF 2 · 2016 (Q14)</p>' +
      '<div class="gov-pyq-box">' +
        '<small style="font-weight:800;color:var(--selb)">UPSC MAINS 2016 | 12.5M | 200 WORDS</small>' +
        '<p style="font-size:18px;font-weight:800;margin:6px 0 0;line-height:1.3;color:var(--ink)">“Traditional bureaucratic structure and culture have hampered the process of socio-economic development in India.” Comment.</p>' +
      '</div>' +
      '<div class="gov-demand">' +
        '<b style="color:var(--accd)">🎯 Demand of the Question:</b>' +
        '<p style="margin:6px 0 0">1. Split into <b>Structural</b> (steep Weberian pyramid, 6-8 file noting layers, ministerial silos, centralized command) vs <b>Cultural</b> bottlenecks (red-tape, “Mai-Baap” paternalism, 3Cs fear).<br>2. Explicitly link to <b>Socio-Economic Development</b> (capex lapse, project delays, local body starvation).<br>3. Provide balanced comment & structural remedies.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to PYQ 2 →</button></div>';
  } else if (GSTEP === 1) {
    // PYQ 2
    bodyHtml = '<div class="body">' +
      '<p class="kind">TARGET PYQ 2 OF 2 · 2026 (Q8)</p>' +
      '<div class="gov-pyq-box">' +
        '<small style="font-weight:800;color:var(--selb)">UPSC MAINS 2026 | 10M | 150 WORDS</small>' +
        '<p style="font-size:18px;font-weight:800;margin:6px 0 0;line-height:1.3;color:var(--ink)">“Analyse the advantages and limitations of the generalist structure of the Indian Civil Services in contemporary governance.”</p>' +
      '</div>' +
      '<div class="gov-demand">' +
        '<b style="color:var(--accd)">🎯 Demand of the Question:</b>' +
        '<p style="margin:6px 0 0">1. Unpack Northcote-Trevelyan all-rounder generalist model.<br>2. <b>Advantages:</b> Grassroots SDM/DM reality, holistic integration without tunnel vision, crisis leadership, federal glue.<br>3. <b>Limitations:</b> Domain asymmetry in AI, semiconductor, WTO; 18-month amnesia; demoralizing technical services.<br>4. <b>Way Forward:</b> Mid-career specialization & lateral entry.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to Thematic Clubbing →</button></div>';
  } else if (GSTEP === 2) {
    // Clubbing
    bodyHtml = '<div class="body">' +
      '<p class="kind">THEMATIC SYNTHESIS</p>' +
      '<p class="q">Why These 2 PYQs Club Together</p>' +
      '<div class="gov-box">' +
        '<p style="margin:0 0 10px;font-size:15px">Both questions test the identical core administrative tension:</p>' +
        '<div style="background:rgba(37,99,235,0.12);padding:10px;border-radius:12px;font-weight:700;font-size:14.5px;color:var(--ink);margin-bottom:10px">' +
          'A 19th-Century Colonial Regulatory Apparatus (Steel Frame)<br>' +
          '<span style="color:#60a5fa">VERSUS</span><br>' +
          'A 21st-Century Dynamic Knowledge Economy & Welfare State.' +
        '</div>' +
        '<p style="margin:0;font-size:13.5px;color:var(--mut)">Mastering this cluster gives you plug-and-play intro hooks, structural-cultural matrices, Fulton & ARC citations, and the Bamboo Frame conclusion.</p>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Start Learning: Introductions →</button></div>';
  } else if (GSTEP === 3) {
    // Hist Intro
    bodyHtml = '<div class="body">' +
      '<p class="kind">READY-TO-USE INTRO (PART 1 OF 2)</p>' +
      '<p class="q">1. Historical / Evolution Angle</p>' +
      '<div class="gov-quote">' +
        '“Rooted in the <b>Macaulay Committee (1854)</b> and Weberian legal-rational model, Indian bureaucracy was originally designed as a regulatory <b>“Steel Frame”</b> for law-and-order maintenance and revenue extraction, rather than as a dynamic instrument of post-independence socio-economic transformation.”' +
      '</div>' +
      '<div class="gov-box">' +
        '<b>🏛️ Macaulay Committee (1854):</b> Elite merit exam for colonial order.<br><br>' +
        '<b>⚖️ Weberian Rationalism:</b> Steep hierarchy & impersonal rules.<br><br>' +
        '<b>💰 Extractive DNA:</b> Revenue siphoning repurposed for socialist welfare.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Continue to Contemporary Intro →</button></div>';
  } else if (GSTEP === 4) {
    // Contemp Intro
    bodyHtml = '<div class="body">' +
      '<p class="kind">READY-TO-USE INTRO (PART 2 OF 2)</p>' +
      '<p class="q">2. Contemporary / Generalist Angle</p>' +
      '<div class="gov-quote" style="border-left-color:var(--acc)">' +
        '“As India transitions from a basic welfare regulator to a complex knowledge economy managing <b>AI regulation</b>, <b>semiconductor supply chains</b>, and <b>climate finance</b>, the 19th-century <b>Northcote-Trevelyan model of the “all-rounder generalist”</b> faces a severe structural stress test.”' +
      '</div>' +
      '<div class="gov-box">' +
        '<b>📜 Northcote-Trevelyan (1854):</b> Liberal arts generalists managing any ministry.<br><br>' +
        '<b>🔬 Modern Frontiers:</b> High-tech governance requires deep domain mastery.<br><br>' +
        '<b>⚡ Stress Test:</b> 18-month rotations create dependency on Big Four consultants.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Proceed to Dimension A →</button></div>';
  } else if (GSTEP === 5) {
    // Dimension A
    bodyHtml = '<div class="body">' +
      '<p class="kind">DIMENSION A (2016 CORE)</p>' +
      '<p class="q">Structure, Culture & Impact Triads</p>' +
      
      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Rigid Weberian Hierarchy</b>: 6-8 file noting layers.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>Rule over Outcome</b>: Red-Tapism procedural obsession.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Delayed Projects</b>: Cost overruns & capex lapsing.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Departmental Silos</b>: Fragmented ministries.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>Turf Consciousness</b>: Refusal to share data.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Policy Incoherence</b>: Water split across 4 ministries.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>Centralized Command</b>: Secretariat monopoly.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>“Mai-Baap” Paternalism</b>: Citizens as charity cases.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Local Disempowerment</b>: Starving Panchayats of 3Fs.' +
      '</div>' +

      '<div class="gov-triad-card">' +
        '<span class="gov-tag struct">Structural</span> <b>No Inaction Penalty</b>: APAR ignores omission.<br>' +
        '<span class="gov-tag cult">Cultural</span> <b>3Cs Fear (CBI, CVC, CAG)</b>: Defensive status-quoism.<br>' +
        '<span class="gov-tag imp">Impact</span> <b>Policy Paralysis</b>: Bold PPP & innovation stifled.' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Proceed to Dimension B →</button></div>';
  } else if (GSTEP === 6) {
    // Dimension B
    bodyHtml = '<div class="body">' +
      '<p class="kind">DIMENSION B (2026 CORE)</p>' +
      '<p class="q">Generalist Advantages vs Limitations</p>' +

      '<div class="gov-box" style="border-color:rgba(16,185,129,0.4)">' +
        '<b style="color:var(--ok);font-size:16px">🛡️ 5 Enduring Advantages:</b>' +
        '<ol style="margin:8px 0 0;padding-left:18px;font-size:13.5px;line-height:1.45">' +
          '<li><b>Grassroots Exposure:</b> SDM/DM reality grounds policy.</li>' +
          '<li><b>Holistic Integration:</b> Cures narrow specialist “tunnel vision”.</li>' +
          '<li><b>Crisis Agility:</b> Rapid multi-agency command in disasters.</li>' +
          '<li><b>Federal Glue:</b> Sardar Patel’s All-India Services unity.</li>' +
          '<li><b>Political Buffer:</b> Translates technical jargon for Ministers.</li>' +
        '</ol>' +
      '</div>' +

      '<div class="gov-box" style="border-color:rgba(239,68,68,0.4)">' +
        '<b style="color:var(--no);font-size:16px">⚠️ 4 Modern Limitations:</b>' +
        '<ol style="margin:8px 0 0;padding-left:18px;font-size:13.5px;line-height:1.45">' +
          '<li><b>Domain Asymmetry:</b> Out of depth in AI, WTO, carbon markets.</li>' +
          '<li><b>Rotational Amnesia:</b> 18-month musical chairs destroy memory.</li>' +
          '<li><b>Specialist Demotivation:</b> IRS, scientists blocked from top posts.</li>' +
          '<li><b>Flawed Drafting:</b> Faulty tenders & retrospective tax controversies.</li>' +
        '</ol>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next">Start Practice Quizzes →</button></div>';
  } else if (GSTEP === 7) {
    // Detailed Practice Quizzes
    bodyHtml = '<div class="body">' +
      '<p class="kind">CHECKPOINT DRILL</p>' +
      '<p class="q">Lock-in Macaulay, Triads & Keyterms</p>' +

      '<!-- Q1 -->' +
      '<div class="gov-box" id="dq1">' +
        '<b>1. Macaulay Committee (1854) primary intent?</b>' +
        '<button class="opt" data-q="1" data-a="0" style="margin-top:8px">Grassroots social empowerment</button>' +
        '<button class="opt" data-q="1" data-a="1">Colonial regulatory Steel Frame for revenue & order</button>' +
        '<div class="gov-fb" id="dfb1"></div>' +
      '</div>' +

      '<!-- Q2 -->' +
      '<div class="gov-box" id="dq2">' +
        '<b>2. Tap the Red Flag:</b><br>' +
        '<div style="margin:8px 0">' +
          '<span class="flag-seg" data-s="0">Bureaucratic fear of 3Cs comprises</span> ' +
          '<span class="flag-seg" data-s="1">the CBI, the CVC,</span> ' +
          '<span class="flag-seg" data-s="2">and NITI Aayog.</span>' +
        '</div>' +
        '<div class="gov-fb" id="dfb2"></div>' +
      '</div>' +

      '<!-- Q3 -->' +
      '<div class="gov-box" id="dq3">' +
        '<b>3. Sort “Mai-Baap Paternalism”:</b>' +
        '<div class="gov-sort-box">Treating citizens as passive charity recipients</div>' +
        '<div class="two">' +
          '<button class="opt" data-s="struct">Structural</button>' +
          '<button class="opt" data-s="cult">Cultural</button>' +
        '</div>' +
        '<div class="gov-fb" id="dfb3"></div>' +
      '</div>' +

      '<!-- Q4 -->' +
      '<div class="gov-box" id="dq4">' +
        '<b>4. Sort “Preventing Specialist Tunnel Vision”:</b>' +
        '<div class="two" style="margin-top:8px">' +
          '<button class="opt" data-g="adv">Generalist Advantage</button>' +
          '<button class="opt" data-g="lim">Generalist Limitation</button>' +
        '</div>' +
        '<div class="gov-fb" id="dfb4"></div>' +
      '</div>' +

      '<!-- Q5 -->' +
      '<div class="gov-box" id="dq5">' +
        '<b>5. Inaction caused by fear of audits is termed:</b>' +
        '<button class="opt" data-q="5" data-a="1" style="margin-top:8px">Policy Paralysis</button>' +
        '<button class="opt" data-q="5" data-a="0">Domain Specialization</button>' +
        '<div class="gov-fb" id="dfb5"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Complete Drills to Proceed →</button></div>';
  } else if (GSTEP === 8) {
    // Value Addition 1 - Fulton
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 1 OF 4 · GLOBAL PRECEDENT</p>' +
      '<p class="q">Fulton Committee (UK, 1968)</p>' +
      '<div class="gov-quote">' +
        'The Fulton Committee famously diagnosed that the civil service was crippled by the <b>“Cult of the Amateur”</b>—the flawed assumption that men trained in general arts could manage modern industrial and technological governance.' +
      '</div>' +
      '<div class="gov-box" id="mq8">' +
        '<b>Which phrase was coined by Fulton Committee?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">“Cult of the Amateur”</button>' +
        '<button class="opt" data-a="0">“Steel Frame”</button>' +
        '<div class="gov-fb" id="mfb8"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 9) {
    // Value Addition 2 - 1st ARC
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 2 OF 4 · 1966 ROADMAP</p>' +
      '<p class="q">1st ARC (1966) — 8 Functional Areas</p>' +
      '<div class="gov-quote">' +
        'The First ARC recommended classifying civil service posts into <b>8 functional areas</b> (Economic, Social, Agriculture, Financial, etc.) for mid-career domain specialization.' +
      '</div>' +
      '<div class="gov-box" id="mq9">' +
        '<b>How many functional areas did 1st ARC recommend?</b>' +
        '<button class="opt" data-a="0" style="margin-top:8px">3 macro cadres</button>' +
        '<button class="opt" data-a="1">8 functional areas</button>' +
        '<div class="gov-fb" id="mfb9"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 10) {
    // Value Addition 3 - Surinder Nath
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 3 OF 4 · DOMAIN MAPPING</p>' +
      '<p class="q">Surinder Nath Committee (2003)</p>' +
      '<div class="gov-quote">' +
        'Recommended assigning officers to <b>11 specific domain clusters</b> based on proven aptitude and field performance to eliminate erratic rotational transfers.' +
      '</div>' +
      '<div class="gov-box" id="mq10">' +
        '<b>Surinder Nath Committee proposed how many domain clusters?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">11 domain clusters</button>' +
        '<button class="opt" data-a="0">28 state cadres</button>' +
        '<div class="gov-fb" id="mfb10"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 11) {
    // Value Addition 4 - 2nd ARC
    bodyHtml = '<div class="body">' +
      '<p class="kind">VALUE ADDITION 4 OF 4 · MASTER REPORTS</p>' +
      '<p class="q">2nd ARC 10th & 13th Reports</p>' +
      '<div class="gov-quote">' +
        '<b>10th Report:</b> Mandatory domain specialization after <b>13 years</b> of service + open senior competition.<br><br>' +
        '<b>13th Report:</b> Replace steep pyramids with <b>flatter, mission-mode</b> executive structures.' +
      '</div>' +
      '<div class="gov-box" id="mq11">' +
        '<b>Mandatory specialization year per 2nd ARC 10th Report?</b>' +
        '<button class="opt" data-a="0" style="margin-top:8px">3 years (probation)</button>' +
        '<button class="opt" data-a="1">13 years of service</button>' +
        '<div class="gov-fb" id="mfb11"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 12) {
    // Examples - Titans
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (1 OF 3)</p>' +
      '<p class="q">Technocrat Titans in Governance</p>' +
      '<div class="gov-box">' +
        '🥛 <b>Dr. Verghese Kurien:</b> Operation Flood (AMUL)<br>' +
        '🌾 <b>Dr. M.S. Swaminathan:</b> Green Revolution<br>' +
        '🚇 <b>E. Sreedharan:</b> Konkan Railway & Delhi Metro<br>' +
        '🆔 <b>Nandan Nilekani:</b> UIDAI (Aadhaar)<br>' +
        '🚽 <b>Parameswaran Iyer:</b> Swachh Bharat Mission (Grameen)' +
      '</div>' +
      '<div class="gov-box" id="mq12">' +
        '<b>Who led UIDAI to build Aadhaar identity infrastructure?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Nandan Nilekani</button>' +
        '<button class="opt" data-a="0">E. Sreedharan</button>' +
        '<div class="gov-fb" id="mfb12"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 13) {
    // Examples - ADP
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (2 OF 3)</p>' +
      '<p class="q">Generalist-Specialist Synergy: ADP</p>' +
      '<div class="gov-quote">' +
        'NITI Aayog’s <b>Aspirational Districts Programme (ADP)</b> proved the golden mean: Generalist District Collectors coordinate field delivery, empowered by domain fellows and real-time data dashboards (<b>Champions of Change</b>).' +
      '</div>' +
      '<div class="gov-box" id="mq13">' +
        '<b>The ADP model proves that:</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Generalists + Specialists achieve peak synergy together</button>' +
        '<button class="opt" data-a="0">District Collectors should be replaced entirely</button>' +
        '<div class="gov-fb" id="mfb13"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 14) {
    // Lateral Entry 2024 Nuance
    bodyHtml = '<div class="body">' +
      '<p class="kind">EXAMPLES & CASE STUDIES (3 OF 3)</p>' +
      '<p class="q">Lateral Entry Dilemma (2024 Update)</p>' +
      '<div class="gov-quote" style="border-left-color:var(--no)">' +
        'August 2024 UPSC withdrawal of 45 lateral posts highlights that technical induction cannot bypass constitutional social justice (<b>Article 16(4)</b>). India needs an <b>institutionalized UPSC framework</b> with clear reservation rosters, not ad-hoc hiring.' +
      '</div>' +
      '<div class="gov-box" id="mq14">' +
        '<b>Reason for the August 2024 UPSC lateral withdrawal?</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Constitutional reservation compliance concerns</button>' +
        '<button class="opt" data-a="0">Shortage of government desks</button>' +
        '<div class="gov-fb" id="mfb14"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Quiz to Proceed →</button></div>';
  } else if (GSTEP === 15) {
    // Way Forward & Conclusion
    bodyHtml = '<div class="body">' +
      '<p class="kind">WAY FORWARD & CONCLUSION</p>' +
      '<p class="q">Steel Frame to Bamboo Frame</p>' +
      '<div class="gov-box">' +
        '🎯 <b>Role-Based HR:</b> Mission Karmayogi (FRAC competencies).<br><br>' +
        '🌟 <b>Generalist-Plus:</b> 10-12 yrs district exposure, then domain specialization.<br><br>' +
        '⚖️ <b>Permanent Lateral Framework:</b> UPSC-led with reservation compliance.<br><br>' +
        '✂️ <b>Desk Officer De-layering:</b> Max 3 decision tiers.' +
      '</div>' +
      '<div class="gov-quote" style="border-left-color:var(--ok)">' +
        '“Contemporary governance demands evolving from a colonial “Steel Frame” into a collaborative <b>“Bamboo Frame”</b>—flexible, specialized at the apex, yet deeply rooted in grassroots realities—to achieve Viksit Bharat by 2047.”' +
      '</div>' +
      '<div class="gov-box" id="mq15">' +
        '<b>The “Bamboo Frame” signifies:</b>' +
        '<button class="opt" data-a="1" style="margin-top:8px">Flexibility & apex specialization rooted in grassroots field reality</button>' +
        '<button class="opt" data-a="0">Complete privatization of civil services</button>' +
        '<div class="gov-fb" id="mfb15"></div>' +
      '</div>' +
    '</div>';
    footHtml = '<div class="foot"><button class="btn" id="gov-next" disabled style="opacity:.6">Answer Final Quiz →</button></div>';
  } else if (GSTEP === 16) {
    // Celebration
    confetti();
    addXp(180);
    bodyHtml = '<div class="body" style="text-align:center;padding-top:20px">' +
      '<div style="font-size:64px;line-height:1">🏆</div>' +
      '<h1 style="font-size:24px;margin:10px 0 6px">Cluster 1 Mastered!</h1>' +
      '<p style="color:var(--mut);font-size:14px;margin:0 0 16px">You conquered both 2016 (Q14) & 2026 (Q8), Macaulay, Fulton, 1st & 2nd ARC, and the Bamboo Frame synthesis.</p>' +
      '<div class="two" style="margin-bottom:16px">' +
        '<div class="stat">+180 XP<small>Knowledge Earned</small></div>' +
        '<div class="stat" style="color:var(--ok)">100%<small>Retention Rate</small></div>' +
      '</div>' +
      '<button class="btn" id="gov-finish" style="background:#2563eb;color:#fff;border-color:#1d4ed8">Return to Governance Themes</button>' +
    '</div>';
    footHtml = '';
  }

  app.innerHTML = headHtml + bodyHtml + footHtml;

  var qb = document.getElementById('gov-quit');
  if (qb) qb.onclick = function(){ home(); };

  var nb = document.getElementById('gov-next');
  if (nb && GSTEP < 7) {
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  // Interactive Handlers for Step 7 (Checkpoint)
  if (GSTEP === 7) {
    var p7 = { q1: false, q2: false, q3: false, q4: false, q5: false };
    function chk7(){
      if (p7.q1 && p7.q2 && p7.q3 && p7.q4 && p7.q5) {
        nb.disabled = false;
        nb.style.opacity = '1';
        nb.style.background = 'var(--ok)';
        nb.textContent = 'All Passed! Continue to Value Additions →';
        beep(true);
      }
    }
    app.querySelectorAll('#dq1 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb1');
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Correct! Extractive & law-and-order steel frame.';
          p7.q1 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Incorrect. It was designed for imperial order.';
        }
        chk7();
      };
    });
    app.querySelectorAll('.flag-seg').forEach(function(s){
      s.onclick = function(){
        var fb = document.getElementById('dfb2');
        if (s.dataset.s === '2') {
          s.className = 'flag-seg bad'; fb.className = 'gov-fb ok';
          fb.textContent = 'Red Flag Spotted! 3Cs are CBI, CVC, and CAG, not NITI Aayog!';
          p7.q2 = true;
        } else {
          s.className = 'flag-seg ok'; fb.className = 'gov-fb no';
          fb.textContent = 'That segment is true. Spot which agency is wrong.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq3 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb3');
        if (b.dataset.s === 'cult') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Spot on! Mindset/cultural bottleneck.';
          p7.q3 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Paternalism is an entrenched mindset/culture.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq4 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb4');
        if (b.dataset.g === 'adv') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Exactly! Core generalist advantage.';
          p7.q4 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Preventing tunnel vision is an advantage.';
        }
        chk7();
      };
    });
    app.querySelectorAll('#dq5 .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById('dfb5');
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Correct! Policy Paralysis from 3Cs fear.';
          p7.q5 = true;
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Inaction from audit fear is Policy Paralysis.';
        }
        chk7();
      };
    });
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  // Micro Quizzes Handlers for Steps 8-15
  if (GSTEP >= 8 && GSTEP <= 15) {
    var boxId = '#mq' + GSTEP;
    var fbId = 'mfb' + GSTEP;
    app.querySelectorAll(boxId + ' .opt').forEach(function(b){
      b.onclick = function(){
        var fb = document.getElementById(fbId);
        if (b.dataset.a === '1') {
          b.className = 'opt sel'; fb.className = 'gov-fb ok';
          fb.textContent = 'Spot on! Nailed it.';
          nb.disabled = false;
          nb.style.opacity = '1';
          nb.style.background = 'var(--acc)';
          nb.textContent = 'Continue →';
          beep(true);
        } else {
          b.className = 'opt bad'; fb.className = 'gov-fb no';
          fb.textContent = 'Not quite, look at the concept card above.';
          beep(false);
        }
      };
    });
    nb.onclick = function(){ GSTEP++; drawGovScreen(); };
  }

  if (GSTEP === 16) {
    var fb = document.getElementById('gov-finish');
    if (fb) fb.onclick = function(){ home(); };
  }
}

function showThemeSheet(themeId){
  var m = document.createElement('div');
  m.className = 'modal-overlay';
  var h = '';
  if (themeId === 'cs_ethos') {
    h = '<div class="modal-sheet">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<span class="theme-tag">UPSC Mains: 2017 (Part A), 2024</span>' +
        '<button class="x" id="modal-x" style="font-size:22px">×</button>' +
      '</div>' +
      '<h2>2. Ethos, Neutrality & Trust in Civil Services</h2>' +
      '<p><b>Core Dilemma:</b> The Weberian doctrine demands political impartiality, anonymity, and institutional permanence, yet contemporary governance faces the risk of a "committed bureaucracy" and politicization of transfers.</p>' +
      '<div class="modal-steps">' +
        '<div class="modal-step"><span class="num">1</span><div><b>Target PYQ 2017:</b> Civil services were designed to achieve neutrality & effectiveness, which seems to have been compromised in recent times. (10M)</div></div>' +
        '<div class="modal-step"><span class="num">2</span><div><b>Target PYQ 2024:</b> Erosion of public trust in administrative discretion and the demand for civil service functional autonomy. (10M)</div></div>' +
        '<div class="modal-step"><span class="num">3</span><div><b>P.C. Hota Committee:</b> Statutory Civil Services Boards with fixed 2-year tenures to insulate officers from arbitrary punitive transfers.</div></div>' +
        '<div class="modal-step"><span class="num">4</span><div><b>Post-Retirement Cooling-Off:</b> Mandatory 2-year cooling-off period before commercial or political appointments to prevent conflict of interest.</div></div>' +
        '<div class="modal-step"><span class="num">5</span><div><b>2nd ARC (4th Report):</b> Enact a Public Service Bill defining statutory civil service values, objectivity, and ethical codes.</div></div>' +
      '</div>' +
      '<button class="btn" id="modal-close-btn" style="background:#2563eb;color:#fff">Got it • Return to Dashboard</button>' +
    '</div>';
  } else if (themeId === 'cs_reforms') {
    h = '<div class="modal-sheet">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<span class="theme-tag">UPSC Mains: 2017 (Part B), 2020</span>' +
        '<button class="x" id="modal-x" style="font-size:22px">×</button>' +
      '</div>' +
      '<h2>3. Institutional Reforms for Viksit Bharat</h2>' +
      '<p><b>Core Dilemma:</b> Industrial-era vertical pyramids cannot deliver 21st-century digital governance; India needs agile, competency-driven, and mission-mode administration.</p>' +
      '<div class="modal-steps">' +
        '<div class="modal-step"><span class="num">1</span><div><b>Target PYQ 2020:</b> Institutional reforms imperative to make Indian Civil Services future-ready for Viksit Bharat. Discuss Mission Karmayogi. (10M)</div></div>' +
        '<div class="modal-step"><span class="num">2</span><div><b>Mission Karmayogi (NPCSCB):</b> Shift from Rule-based compliance to Role-based competencies using the FRAC architecture and iGOT platform.</div></div>' +
        '<div class="modal-step"><span class="num">3</span><div><b>Lateral Entry Framework:</b> Institutionalized UPSC-led recruitment with strict constitutional reservation quotas for social justice.</div></div>' +
        '<div class="modal-step"><span class="num">4</span><div><b>Desk Officer System:</b> Capping Secretariat file-noting hierarchies to maximum three tiers to eliminate red-tapism.</div></div>' +
        '<div class="modal-step"><span class="num">5</span><div><b>3Cs Safe-Harbor Protection:</b> Statutory protection for bona-fide risk taking, ending policy paralysis caused by retrospective CBI/CAG fear.</div></div>' +
      '</div>' +
      '<button class="btn" id="modal-close-btn" style="background:#2563eb;color:#fff">Got it • Return to Dashboard</button>' +
    '</div>';
  } else {
    h = '<div class="modal-sheet">' +
      '<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">' +
        '<span class="theme-tag">UPSC Mains Topic</span>' +
        '<button class="x" id="modal-x" style="font-size:22px">×</button>' +
      '</div>' +
      '<h2>' + esc(themeId) + '</h2>' +
      '<p>Detailed syllabus module and PYQ analysis for this theme are mapped under the respective GS Paper.</p>' +
      '<button class="btn" id="modal-close-btn">Close</button>' +
    '</div>';
  }
  m.innerHTML = h;
  document.body.appendChild(m);
  var cb = document.getElementById('modal-close-btn'), cx = document.getElementById('modal-x');
  if (cb) cb.onclick = function(){ m.remove(); };
  if (cx) cx.onclick = function(){ m.remove(); };
  m.onclick = function(e){ if (e.target === m) m.remove(); };
}
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
  
  var top = DATA[CUR_TOPIC];
  var nextL = 0;
  if (top && top.lessons) {
    top.lessons.forEach(function(l, idx){
      if (!(S.done[CUR_TOPIC]||{})[idx] && nextL === 0) nextL = idx;
    });
  }

  var autoTimer = null;
  var nextLessonObj = (top && top.lessons && top.lessons[nextL]) ? top.lessons[nextL] : null;

  var h = '<div class="end"><div class="big">' + (win ? '🎯' : '💔') + '</div>' +
    '<h1>' + (win ? (R.daily ? 'Daily challenge done!' : R.lab ? 'Lab complete!' : R.boss ? 'Boss defeated!' : R.lt ? 'Lightning round done!' : R.det ? 'Case closed!' : R.sto ? 'Mission complete!' : R.arc ? 'Arcade cleared!' : R.pyq ? 'PYQ drill completed!' : 'Weak spots reviewed!') : 'Out of hearts') + '</h1>' +
    '<p class="sub">' + (win ? '+' + R.xp + ' XP earned!' : 'Try again after re-reading the study cards.') + '</p>';

  if (win && nextLessonObj) {
    h += '<div style="background:var(--card);border:2px solid var(--ok);border-radius:14px;padding:12px 16px;margin:10px 0 16px;max-width:340px;width:100%">' +
      '<div style="font-size:12px;font-weight:700;color:var(--ok);text-transform:uppercase;letter-spacing:0.04em">Practice Complete · Next Lesson</div>' +
      '<div style="font-size:16px;font-weight:800;color:var(--ink);margin:4px 0 2px">' + esc(nextLessonObj.e) + ' ' + esc(nextLessonObj.n) + '</div>' +
      '<div style="font-size:13px;color:var(--mut)">Auto-starting in <b id="rev-cnt">3</b>s...</div>' +
    '</div>' +
    '<button class="btn" id="btn-next-l" style="max-width:320px;margin-bottom:8px;background:var(--ok);border-color:#0d7753;color:#fff">Start Next Lesson Now →</button>' +
    '<button class="btn" id="a" style="max-width:320px;background:var(--card);border:2px solid var(--line);border-bottom-width:4px;color:var(--ink)">Back to Lessons</button>';
  } else {
    h += '<button class="btn" id="a" style="max-width:320px">Back to Lessons</button>';
  }
  h += '</div>';

  app.innerHTML = h;

  if (win && nextLessonObj) {
    var sec = 3;
    autoTimer = setInterval(function(){
      sec--;
      var cnt = document.getElementById('rev-cnt');
      if (cnt) cnt.textContent = sec;
      if (sec <= 0) {
        clearInterval(autoTimer);
        start(nextL);
      }
    }, 1000);
    var bn = document.getElementById('btn-next-l');
    if (bn) bn.onclick = function(){ clearInterval(autoTimer); start(nextL); };
  }

  document.getElementById('a').onclick = function(){
    if (autoTimer) clearInterval(autoTimer);
    home();
  };
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
  // Infrastructure Delivery Diagrams
  else if(k === 'infra:0:0'){
    H = 175;
    s = bx(10, 15, 95, 45, 'Delhi-Meerut|Road Ready') +
        ar(105, 37, 130, 37) +
        bx(130, 15, 80, 45, '11 Months|Idle Wait', 'var(--no)') +
        ar(210, 37, 235, 37) +
        bx(235, 15, 75, 45, 'Railway|ROB Delay') +
        ar(170, 60, 170, 90) +
        bx(25, 90, 270, 45, 'Gati-Shakti NPG: 3-Tier Synchronized GIS', 'var(--h)') +
        tx(160, 155, 'Overcoming Uncoordinated Silos', 12, 'var(--mut)');
  }
  else if(k === 'infra:1:1'){
    H = 170;
    s = bx(15, 20, 130, 50, 'Past Baseline|13 - 14% of GDP', 'var(--no)') +
        `<path d='M 145 45 Q 160 15 175 45' fill='none' stroke='var(--h)' stroke-width='2.5' marker-end='url(#ar)'/>` +
        bx(175, 20, 130, 50, 'NCAER Rebasing|7.97% of GDP', 'var(--ok)') +
        ar(160, 75, 160, 95) +
        bx(35, 95, 250, 45, 'ULIP + National Logistics Policy|<10% & Top 25 LPI by 2030', 'var(--h)');
  }
  else if(k === 'infra:2:0'){
    H = 165;
    s = bx(10, 15, 90, 42, 'Brownfield|Assets') +
        ar(100, 36, 125, 36) +
        bx(125, 15, 95, 42, 'NMP 1.0 (90%)|₹5.4L Cr Leased', 'var(--h)') +
        ar(220, 36, 245, 36) +
        bx(245, 15, 65, 42, 'Capital|Recycled') +
        ar(172, 57, 172, 85) +
        bx(20, 85, 280, 45, 'NMP 2.0 (FY26-30): ₹16.72L Cr Potential (₹5.8L Cr Pvt)');
  }
  else if(k === 'infra:3:0'){
    H = 175;
    s = bx(15, 20, 130, 45, 'Centre: SASCI|50-Yr 0% Loan (₹2L Cr)', 'var(--h)') +
        ar(145, 42, 175, 42) +
        bx(175, 20, 130, 45, 'State Capex Lag|27% Spent Apr-Aug', 'var(--no)') +
        ar(160, 68, 160, 95) +
        bx(30, 95, 260, 45, 'Cooperative Federalism: 25% CSS Flexi-Fund', 'var(--ok)') +
        tx(160, 160, 'Balancing National Priorities with State Fiscal Space', 11, 'var(--mut)');
  }
  // Tech-Enabled Welfare Delivery (DBT & JAM) Diagrams
  else if(k === 'dbt:0:0'){
    H = 165;
    s = bx(10, 15, 90, 45, 'Jan Dhan|59 Cr Accounts') +
        ar(100, 37, 120, 37) +
        bx(120, 15, 80, 45, 'Aadhaar|Digital ID') +
        ar(200, 37, 220, 37) +
        bx(220, 15, 90, 45, 'Mobile Rail|DBT Bharat') +
        ar(160, 60, 160, 85) +
        bx(30, 85, 260, 45, '₹3.48L Cr Cumulative Savings (53% PDS Reform)', 'var(--h)');
  }
  else if(k === 'dbt:1:1'){
    H = 175;
    s = bx(15, 20, 130, 55, 'Inclusion Error|Ghost / Leakage Cut|₹1.85L Cr PDS Saved', 'var(--ok)') +
        `<line x1='160' y1='10' x2='160' y2='130' stroke='var(--h)' stroke-width='3' stroke-dasharray='4'/>` +
        bx(175, 20, 130, 55, 'Exclusion Error|Biometric Denial|5.48 Cr Deletions', 'var(--no)') +
        ar(80, 75, 120, 105) + ar(240, 75, 200, 105) +
        bx(40, 105, 240, 40, 'Mandatory Offline Fallbacks (Puttaswamy)', 'var(--h)');
  }
  else if(k === 'dbt:2:0'){
    H = 165;
    s = bx(10, 15, 85, 45, 'Aadhaar|Number') +
        ar(95, 37, 115, 37) +
        bx(115, 15, 90, 45, 'NPCI Mapper|Bank Seeding', 'var(--h)') +
        ar(205, 37, 225, 37) +
        bx(225, 15, 85, 45, 'ABPS Rail|Payment') +
        ar(160, 60, 160, 85) +
        bx(25, 85, 270, 45, 'Seeding != Authentication: Name Mismatch Hazard', 'var(--no)');
  }
  else if(k === 'dbt:3:1'){
    H = 170;
    s = bx(10, 15, 140, 45, 'Cash: Ladli Behna|₹18.6k Cr / 6.4% Rec.') +
        bx(170, 15, 140, 45, 'Kind: NFSA PDS|Price Shock Safety', 'var(--h)') +
        ar(80, 60, 160, 95) + ar(240, 60, 160, 95) +
        bx(20, 95, 280, 45, 'Fiscal Safeguard: RBI Capex Floor + Sunset Clauses', 'var(--ok)');
  }
  // Civil Services Structure, Culture & Generalist vs Specialist Diagrams
  else if(k === 'cs_structure:0:0'){
    H = 175;
    s = bx(10, 15, 95, 45, '1854: Macaulay|Revenue & Order', 'var(--no)') +
        ar(105, 37, 130, 37) +
        bx(130, 15, 80, 45, 'Post-1947|Welfare DNA') +
        ar(210, 37, 235, 37) +
        bx(235, 15, 75, 45, '2026: AI &|Knowledge', 'var(--h)') +
        ar(170, 60, 170, 90) +
        bx(25, 90, 270, 45, 'From Colonial "Steel Frame" to "Bamboo Frame"', 'var(--ok)') +
        tx(160, 155, 'Evolution of Civil Services Mandate', 12, 'var(--mut)');
  }
  else if(k === 'cs_structure:1:0'){
    H = 175;
    s = bx(10, 15, 140, 50, 'Structural: 8-Tier Hierarchy|Water Split (4 Ministries)', 'var(--h)') +
        bx(170, 15, 140, 50, 'Cultural: Red-Tape & Mai-Baap|3Cs Fear Policy Paralysis', 'var(--no)') +
        ar(80, 65, 160, 95) + ar(240, 65, 160, 95) +
        bx(30, 95, 260, 45, 'Result: Cost Overruns & Denied Citizen Rights', 'var(--no)') +
        tx(160, 160, 'Core Bottlenecks (2016 Q14 Matrix)', 11, 'var(--mut)');
  }
  else if(k === 'cs_structure:2:1'){
    H = 175;
    s = bx(10, 15, 75, 35, 'Police') + bx(90, 15, 70, 35, 'Health') + bx(165, 15, 70, 35, 'PWD') + bx(240, 15, 70, 35, 'Revenue') +
        ar(47, 50, 120, 85) + ar(125, 50, 140, 85) + ar(200, 50, 180, 85) + ar(275, 50, 200, 85) +
        bx(35, 85, 250, 45, 'Generalist District Magistrate|Cross-Sectoral Integrator & Disaster Commander', 'var(--h)') +
        tx(160, 155, 'Breaking Specialist Tunnel Vision', 12, 'var(--mut)');
  }
  else if(k === 'cs_structure:3:1'){
    H = 165;
    s = bx(10, 15, 95, 45, '18-Mo Transfers|Textiles → Space') +
        ar(105, 37, 130, 37) +
        bx(130, 15, 80, 45, 'Memory Loss|Domain Deficit', 'var(--no)') +
        ar(210, 37, 235, 37) +
        bx(235, 15, 75, 45, 'Big Four|Consultants', 'var(--h)') +
        ar(170, 60, 170, 90) +
        bx(30, 90, 260, 45, 'The "Hollow State" & Policy Capture Risk', 'var(--no)');
  }
  else if(k === 'cs_structure:4:0'){
    H = 180;
    s = bx(10, 15, 95, 38, 'Dr. Kurien|Op Flood') +
        bx(112, 15, 95, 38, 'Sreedharan|Metro Rail') +
        bx(214, 15, 95, 38, 'Nilekani|UIDAI / Tech') +
        ar(57, 53, 130, 85) + ar(160, 53, 160, 85) + ar(262, 53, 190, 85) +
        bx(40, 85, 240, 42, 'Specialist Delivery Breakthroughs', 'var(--h)') +
        tx(160, 155, 'Swachh Bharat: P. Iyer Lateral Leadership', 12, 'var(--mut)');
  }
  else if(k === 'cs_structure:5:0'){
    H = 250;
    s = `<line x1='60' y1='20' x2='60' y2='230' stroke='var(--h)' stroke-width='3'/>`;
    [['1968','Fulton: Cult of the amateur'],['1966','1st ARC: 8 Functional areas'],['2003','Surinder Nath: 11 Domain clusters'],['2009','2nd ARC: 13-Year domain rule'],['2020','Mission Karmayogi: FRAC role HR']].forEach(function(e,j){
      var y = 25 + j*48;
      s += `<circle cx='60' cy='${y}' r='8' fill='var(--h)'/>` + tx(26, y+5, e[0], 12, 'var(--h)') + tx(195, y+5, e[1], 12);
    });
  }
  else if(k === 'cs_structure:6:0'){
    H = 180;
    s = bx(15, 20, 130, 60, 'Colonial "Steel Frame"|Rigid, Procedural|Top-Heavy, Risk-Averse', 'var(--no)') +
        ar(145, 50, 175, 50) +
        bx(175, 20, 130, 60, 'Collaborative "Bamboo Frame"|Deep Grassroots Roots|Apex Domain Mastery', 'var(--ok)') +
        ar(160, 80, 160, 105) +
        bx(30, 105, 260, 45, 'Viksit Bharat 2047: Synergistic Administration', 'var(--h)') +
        tx(160, 165, 'Flexible, Resilient & Specialized', 11, 'var(--mut)');
  }

  if(!s) return '';
  return `<p class='kw'>📊 Picture it</p><div class='dg'><svg viewBox='0 0 320 ${H}' width='100%' role='img' aria-label='Diagram'><defs><marker id='ar' markerWidth='8' markerHeight='8' refX='6' refY='4' orient='auto'><path d='M0,0L8,4L0,8z' fill='var(--h)'/></marker></defs>${s}</svg></div>`;
}

function home(){
  S.paper = S.paper || 'gs2';
  var curPaperObj = SYLLABUS[S.paper] || SYLLABUS.gs2;
  var domainKeys = Object.keys(curPaperObj.domains);
  if (!curPaperObj.domains[S.domain]) S.domain = domainKeys[0];
  var curDomainObj = curPaperObj.domains[S.domain];

  var top = DATA[CUR_TOPIC] || DATA["cs_structure"];

  // 1. Paper Selector Tabs
  var papersHtml = '<div class="paper-row">';
  Object.keys(SYLLABUS).forEach(function(pk){
    var p = SYLLABUS[pk];
    papersHtml += '<button class="paper-btn' + (pk === S.paper ? ' active' : '') + '" data-p="' + pk + '">' + esc(p.name) + '</button>';
  });
  papersHtml += '</div>';

  // 2. Domain Selector Tabs
  var domainsHtml = '<div class="domain-row">';
  domainKeys.forEach(function(dk){
    var d = curPaperObj.domains[dk];
    domainsHtml += '<button class="domain-btn' + (dk === S.domain ? ' active' : '') + '" data-d="' + dk + '">' + d.ico + ' ' + esc(d.name) + '</button>';
  });
  domainsHtml += '</div>';

  // 3. Domain Themes Card List (matches the uploaded image)
  var themesHtml = '<div class="theme-card-box">';
  curDomainObj.themes.forEach(function(th){
    var isActive = (th.topic && th.topic === CUR_TOPIC);
    themesHtml += '<div class="theme-item' + (isActive ? ' active' : '') + '" data-th="' + th.id + '"' + (th.topic ? ' data-top="' + th.topic + '"' : '') + '>' +
      '<div class="theme-left">' +
        '<div class="theme-title">' + esc(th.title) + '</div>' +
        '<div class="theme-desc">' + esc(th.desc) + '</div>' +
      '</div>' +
      '<div class="theme-years">' + esc(th.years) + '</div>' +
    '</div>';
  });
  themesHtml += '</div>';

  // 4. Quick Topic Pills
  var topicsHtml = '<div class="topics">';
  topicsHtml += '<button class="topic-btn' + (S.domain === 'governance' ? ' active' : '') + '" id="pill-gov">🏛️ Governance (5 Themes)</button>';
  Object.keys(DATA).forEach(function(k){
    var t = DATA[k];
    topicsHtml += '<button class="topic-btn' + (k === CUR_TOPIC && S.domain !== 'governance' ? ' active' : '') + '" data-t="' + k + '">' + t.badge + ' ' + esc(t.title.split('&')[0].trim()) + '</button>';
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
  '<div class="gs-explorer">' +
    papersHtml +
    domainsHtml +
  '</div>' +
  '<div class="home">' +
    themesHtml +
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

  h += '</div><div style="margin-top:20px"><small style="color:var(--mut);font-weight:700">Browse all CAVA modules:</small></div>' + topicsHtml + '</div>';

  app.innerHTML = h;

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

  // Paper Selector clicks
  app.querySelectorAll('.paper-btn').forEach(function(btn){
    btn.onclick = function(){
      S.paper = btn.dataset.p;
      var dkeys = Object.keys(SYLLABUS[S.paper].domains);
      S.domain = dkeys[0];
      save();
      home();
    };
  });

  // Domain Selector clicks
  app.querySelectorAll('.domain-btn').forEach(function(btn){
    btn.onclick = function(){
      S.domain = btn.dataset.d;
      save();
      home();
    };
  });

  // Theme Item clicks
  app.querySelectorAll('.theme-item').forEach(function(item){
    item.onclick = function(){
      var topId = item.dataset.top;
      var thId = item.dataset.th;
      if (thId === 'gov_theme_2' || thId === 'cs_structure') {
        showTheme2Modal();
      } else if (topId && DATA[topId]) {
        CUR_TOPIC = topId;
        home();
      } else {
        showThemeSheet(thId);
      }
    };
  });

  var pGov = document.getElementById('pill-gov');
  if (pGov) pGov.onclick = function(){ S.paper = 'gs2'; S.domain = 'governance'; save(); home(); };
  app.querySelectorAll('.topic-btn').forEach(function(b){
    b.onclick = function(){
      CUR_TOPIC = b.dataset.t;
      // Auto-set matching paper & domain if known
      if (CUR_TOPIC === 'cs_structure' || CUR_TOPIC === 'charter' || CUR_TOPIC === 'rti' || CUR_TOPIC === 'exams') {
        S.paper = 'gs2'; S.domain = 'governance';
      } else if (CUR_TOPIC === 'judiciary') {
        S.paper = 'gs2'; S.domain = 'polity';
      } else if (CUR_TOPIC === 'dbt') {
        S.paper = 'gs2'; S.domain = 'justice';
      } else if (CUR_TOPIC === 'msme' || CUR_TOPIC === 'infra') {
        S.paper = 'gs3'; S.domain = 'economy';
      }
      save();
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
  var c = l.c[R.ci];
  var n = c.b.length; // number of bullet points (e.g. 3)
  var tot = l.c.length;
  var hue = top.hue[R.i % top.hue.length];
  var ico = top.ico[R.i % top.ico.length][R.ci % 3] || l.e;

  // Check extra sequential steps available after bullet n
  var diagramHtml = diag(CUR_TOPIC, R.i, R.ci);
  var hasDiag = !!diagramHtml;
  var hasKw = !!(c.k && c.k.length);
  var hasOwl = !!c.n;

  var extraSteps = [];
  if (hasDiag) extraSteps.push('diag');
  if (hasKw) extraSteps.push('kw');
  if (hasOwl) extraSteps.push('owl');

  var maxStage = extraSteps.length;
  var totalCardSteps = n + maxStage;
  var currentStep = R.sh;

  var h = head() + '<div class="body" style="--h:' + hue + '">' +
    '<div class="hero"><span class="ico">' + ico + '</span><div><small>' + esc(l.n) + ' · card ' + (R.ci+1) + ' of ' + tot + '</small><h2>' + esc(c.t) + '</h2></div></div>';

  // 1. Show bullet points up to currentStep (capped at n)
  var bulletsToShow = Math.min(currentStep, n);
  for(var i = 0; i < bulletsToShow; i++){
    h += '<div class="tile' + (i === bulletsToShow - 1 && i > 0 ? ' pop' : '') + '"><span class="dot">✦</span><p>' + c.b[i] + '</p></div>';
  }

  // 2. Reveal post-bullet items sequentially ONLY when currentStep advances past n
  var postStep = currentStep - n;
  if (postStep > 0) {
    for (var s = 0; s < postStep && s < extraSteps.length; s++) {
      var stepType = extraSteps[s];
      var isLatest = (s === postStep - 1);
      if (stepType === 'diag') {
        h += '<div class="' + (isLatest ? 'pop' : '') + '">' + diagramHtml + '</div>';
      } else if (stepType === 'kw') {
        unlock(c);
        h += '<p class="kw' + (isLatest ? ' pop' : '') + '">🔑 Keywords unlocked</p><div class="chips' + (isLatest ? ' pop' : '') + '">';
        c.k.forEach(function(k){ h += '<span class="chip">' + esc(k) + '</span>'; });
        h += '</div>';
      } else if (stepType === 'owl') {
        h += '<div class="bub' + (isLatest ? ' pop' : '') + '"><span>🦉</span><p>' + esc(c.n) + '</p></div>';
      }
    }
  }

  // 3. Button label
  var isFinal = (currentStep >= totalCardSteps);
  var btnText = 'Continue';
  if (currentStep < n) {
    btnText = 'Continue (' + currentStep + '/' + n + ')';
  } else if (isFinal) {
    btnText = (R.ci === tot - 1) ? 'Got it · Start Questions →' : 'Got it · Next Card →';
  } else {
    var nextStepType = extraSteps[postStep];
    if (nextStepType === 'diag') btnText = 'Continue → Picture it';
    else if (nextStepType === 'kw') btnText = 'Continue → Keywords';
    else if (nextStepType === 'owl') btnText = 'Continue → Note';
    else btnText = 'Continue';
  }

  h += '</div><div class="foot"><button class="btn" id="go">' + btnText + '</button></div>';
  app.innerHTML = h;
  quit();

  document.getElementById("go").onclick = function(){
    if (!isFinal) {
      R.sh++;
      cardDraw();
      var b = document.querySelector(".body");
      if (b) {
        setTimeout(function(){
          b.scrollTo({ top: b.scrollHeight, behavior: 'smooth' });
        }, 40);
      }
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

  var nextIdx = R.i + 1;
  var hasNext = (nextIdx < top.lessons.length);
  var nextLessonObj = hasNext ? top.lessons[nextIdx] : null;
  var autoTimer = null;

  var h = '<div class="end"><div class="big">' + (win ? '🏆' : '💔') + '</div>' +
    '<h1>' + (win ? 'Lesson complete!' : 'Out of hearts') + '</h1>' +
    '<p class="sub">' + (win ? esc(l.n) + ' cleared.' : 'Re-read the cards and try again.') + '</p>' +
    (win ? '<div class="stats"><div class="stat">+' + R.xp + '<small>XP</small></div><div class="stat">' + pct + '%<small>Accuracy</small></div><div class="stat">' + R.hearts + '<small>Hearts left</small></div></div>' : '<div style="height:24px"></div>');

  if (win && hasNext && nextLessonObj) {
    h += '<div style="background:var(--card);border:2px solid var(--ok);border-radius:14px;padding:12px 16px;margin:10px 0 16px;max-width:340px;width:100%">' +
      '<div style="font-size:12px;font-weight:700;color:var(--ok);text-transform:uppercase;letter-spacing:0.04em">Up Next · Auto-advancing</div>' +
      '<div style="font-size:16px;font-weight:800;color:var(--ink);margin:4px 0 2px">' + esc(nextLessonObj.e) + ' ' + esc(nextLessonObj.n) + '</div>' +
      '<div style="font-size:13px;color:var(--mut)">Starting in <b id="sec-cnt">3</b>s...</div>' +
    '</div>' +
    '<button class="btn" id="btn-next" style="max-width:320px;margin-bottom:8px;background:var(--ok);border-color:#0d7753;color:#fff">Start Next Lesson Now →</button>' +
    '<button class="btn" id="a" style="max-width:320px;background:var(--card);border:2px solid var(--line);border-bottom-width:4px;color:var(--ink)">Back to Lessons</button>';
  } else if (win) {
    h += '<div style="background:var(--card);border:2px solid var(--acc);border-radius:14px;padding:12px 16px;margin:10px 0 16px;max-width:340px;width:100%">' +
      '<div style="font-size:12px;font-weight:700;color:var(--accd);text-transform:uppercase;letter-spacing:0.04em">👑 All Lessons Cleared!</div>' +
      '<div style="font-size:16px;font-weight:800;color:var(--ink);margin:4px 0 2px">Topic Mastered!</div>' +
    '</div>' +
    '<button class="btn" id="a" style="max-width:320px">Back to Dashboard</button>';
  } else {
    h += '<button class="btn" id="btn-retry" style="max-width:320px;margin-bottom:8px">Try again</button>' +
      '<button class="btn" id="a" style="max-width:320px;background:var(--card);border:2px solid var(--line);border-bottom-width:4px;color:var(--ink)">Back to Lessons</button>';
  }

  h += '</div>';
  app.innerHTML = h;

  if (win && hasNext && nextLessonObj) {
    var sec = 3;
    autoTimer = setInterval(function(){
      sec--;
      var cnt = document.getElementById('sec-cnt');
      if (cnt) cnt.textContent = sec;
      if (sec <= 0) {
        clearInterval(autoTimer);
        start(nextIdx);
      }
    }, 1000);
    var bn = document.getElementById('btn-next');
    if (bn) bn.onclick = function(){ clearInterval(autoTimer); start(nextIdx); };
  }

  var btnRetry = document.getElementById('btn-retry');
  if (btnRetry) btnRetry.onclick = function(){ start(R.i); };

  document.getElementById("a").onclick = function(){
    if (autoTimer) clearInterval(autoTimer);
    home();
  };

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
    charter_html = rendered_html.replace('var CUR_TOPIC = "cs_structure";', 'var CUR_TOPIC = "charter";')
    with open(root_charter_path, "w", encoding="utf-8") as f:
        f.write(charter_html)
    print(f"Generated Citizen's Charter file at {root_charter_path} ({len(charter_html)} bytes)")

if __name__ == "__main__":
    generate()
