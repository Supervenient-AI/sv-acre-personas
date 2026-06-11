#!/usr/bin/env python3
"""Build a self-contained HTML viewer for the ACRE persona library.

Scans the `personas/` tree for persona documents and their `individuals/`
folders, plus the framework and target-universe docs, and bakes the raw
markdown into a single `tool/index.html` styled to the Supervenient brand &
design system (docs/design/). The markdown is embedded inline (not fetched),
so the result works by simply double-clicking the file — no local server.

Usage:
    python3 tool/build.py

Re-run whenever you add or edit personas or individuals.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = ROOT / "personas"
ABOUT_FILE = ROOT / "about-acre-personas.md"
UNIVERSE_FILE = ROOT / "ACRE-target-universe.md"
OUTPUT = ROOT / "tool" / "index.html"


def persona_number(text: str) -> float:
    """Sort key: the 'N' in '# ACRE Persona N — ...', else infinity."""
    m = re.search(r"ACRE Persona\s+(\d+)", text)
    return int(m.group(1)) if m else float("inf")


def first_heading(text: str) -> str | None:
    for line in text.splitlines():
        m = re.match(r"^#\s+(.*)", line.strip())
        if m:
            return m.group(1).strip()
    return None


def subtitle_heading(text: str) -> str | None:
    """The '### ...' line that follows the title in persona docs."""
    for line in text.splitlines():
        m = re.match(r"^###\s+(.*)", line.strip())
        if m:
            return m.group(1).strip()
    return None


def individual_subtitle(text: str) -> str | None:
    """First bold line in an individual doc: '**Role · age · place**'."""
    for line in text.splitlines():
        m = re.match(r"^\*\*(.+?)\*\*\s*$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def collect_documents() -> list[dict]:
    docs: list[dict] = []

    for path, sub in ((ABOUT_FILE, "The framework"), (UNIVERSE_FILE, "Candidate audiences")):
        if path.exists():
            text = path.read_text(encoding="utf-8")
            docs.append(
                {
                    "id": path.name,
                    "group": "Framework",
                    "name": first_heading(text) or path.stem,
                    "subtitle": subtitle_heading(text) or sub,
                    "markdown": text,
                    "children": [],
                }
            )

    # personas/<status>/<slug>/acre-persona.md with individuals/*.md as children
    persona_paths = sorted(
        PERSONAS_DIR.glob("*/*/acre-persona.md"),
        key=lambda p: (persona_number(p.read_text(encoding="utf-8")), str(p)),
    )
    for md_path in persona_paths:
        rel = md_path.relative_to(PERSONAS_DIR)
        status, slug = rel.parts[0], rel.parts[1]
        text = md_path.read_text(encoding="utf-8")
        children = []
        for ind_path in sorted((md_path.parent / "individuals").glob("*.md")):
            ind_text = ind_path.read_text(encoding="utf-8")
            children.append(
                {
                    "id": str(ind_path.relative_to(PERSONAS_DIR)),
                    "name": first_heading(ind_text) or ind_path.stem,
                    "subtitle": individual_subtitle(ind_text) or "Individual",
                    "markdown": ind_text,
                }
            )
        docs.append(
            {
                "id": str(rel),
                "group": status.replace("-", " ").title(),
                "name": first_heading(text) or slug,
                "subtitle": subtitle_heading(text) or slug,
                "markdown": text,
                "children": children,
            }
        )

    return docs


def build_html(docs: list[dict]) -> str:
    n_personas = sum(1 for d in docs if d["group"] != "Framework")
    n_individuals = sum(len(d["children"]) for d in docs)
    data_json = json.dumps(docs, ensure_ascii=False)
    return (
        TEMPLATE.replace("/*__DATA__*/", data_json)
        .replace("__N_PERSONAS__", str(n_personas))
        .replace("__N_INDIVIDUALS__", str(n_individuals))
    )


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>ACRE Personas · Supervenient</title>
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Lexend:wght@300;400;500&display=swap" rel="stylesheet" />
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
  /* ── Supervenient design tokens (docs/design, v0.5) ───────────────── */
  :root {
    --canvas: #FFFFFF;
    --depth: #0E2841;
    --ink: #0E2841;
    --n50: #F6F8FA; --n100: #ECEFF3; --n200: #DCE2E9;
    --n400: #9AA5B3; --n600: #5B6675; --n900: #0E2841;
    --sky: #93DAF7; --peach: #F3AC89; --mint: #A1E9AB; --lilac: #EAA4E0;
    --sky-a: #1668B0; --peach-a: #B45A30; --mint-a: #1E7A3E; --lilac-a: #9A4D8E;
    --info-surf: #E6F3FC;
    --r-sm: 6px; --r-md: 10px; --r-lg: 16px; --r-xl: 24px;
    --e1: 0 1px 3px rgba(14,40,65,0.10), 0 1px 2px rgba(14,40,65,0.06);
    --e2: 0 4px 12px rgba(14,40,65,0.08);
    --e3: 0 12px 40px rgba(14,40,65,0.12);
    --ease: cubic-bezier(0.2, 0, 0, 1);
    --sidebar-w: 320px;
    --toc-w: 230px;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; }
  body {
    font-family: "Lexend", -apple-system, "Segoe UI", sans-serif;
    font-weight: 400;
    font-size: 16px;
    line-height: 1.55;
    color: var(--ink);
    background: var(--n50);
  }
  :focus-visible { outline: 2px solid var(--sky-a); outline-offset: 2px; border-radius: var(--r-sm); }

  .app { display: grid; grid-template-columns: var(--sidebar-w) 1fr; height: 100vh; }

  /* ── Sidebar ──────────────────────────────────────────────────────── */
  .sidebar {
    background: var(--canvas);
    border-right: 1px solid var(--n200);
    overflow-y: auto;
    display: flex;
    flex-direction: column;
  }
  .brand {
    padding: 24px 24px 16px;
    border-bottom: 1px solid var(--n200);
    position: sticky; top: 0; background: var(--canvas); z-index: 2;
  }
  .brand-row { display: flex; align-items: center; gap: 12px; }
  .orb {
    width: 36px; height: 36px; border-radius: 999px; flex: none;
    background: var(--depth);
    position: relative; overflow: hidden;
    box-shadow: var(--e1);
  }
  .orb::before, .orb::after {
    content: ""; position: absolute; inset: 0; border-radius: 999px;
    mix-blend-mode: screen;
  }
  .orb::before {
    background:
      radial-gradient(60% 60% at 30% 35%, var(--sky) 0%, transparent 70%),
      radial-gradient(55% 55% at 72% 30%, var(--peach) 0%, transparent 70%);
    opacity: .9;
  }
  .orb::after {
    background:
      radial-gradient(55% 55% at 35% 75%, var(--lilac) 0%, transparent 70%),
      radial-gradient(50% 50% at 70% 70%, var(--mint) 0%, transparent 70%),
      radial-gradient(38% 38% at 50% 50%, rgba(255,255,255,.85) 0%, transparent 72%);
    opacity: .85;
  }
  .brand h1 { font-size: 17px; font-weight: 500; letter-spacing: -0.025em; margin: 0; }
  .brand .word { color: var(--ink); }
  .brand p { margin: 2px 0 0; color: var(--n600); font-size: 12.5px; }
  .brand .stats { margin-top: 10px; color: var(--n600); font-size: 12px; }
  .search {
    margin-top: 12px;
  }
  .search input {
    width: 100%; padding: 8px 12px;
    font: inherit; font-size: 14px; color: var(--ink);
    background: var(--n50);
    border: 1px solid var(--n200); border-radius: var(--r-md);
  }
  .search input::placeholder { color: var(--n400); }

  nav#nav { padding: 8px 0 48px; }
  .nav-group > .label {
    padding: 16px 24px 6px;
    font-size: 11.5px; font-weight: 500;
    letter-spacing: .08em; text-transform: uppercase;
    color: var(--n600);
  }
  .nav-item {
    display: block; width: 100%; text-align: left;
    padding: 9px 24px 9px 21px;
    border: none; background: none; cursor: pointer;
    font: inherit; color: var(--ink);
    border-left: 3px solid transparent;
    transition: background 160ms var(--ease);
  }
  .nav-item:hover { background: var(--n50); }
  .nav-item.active { background: var(--info-surf); border-left-color: var(--sky-a); }
  .nav-item .title { font-size: 13.5px; font-weight: 500; letter-spacing: -0.01em; }
  .nav-item .sub { font-size: 11.5px; color: var(--n600); margin-top: 1px; }
  .nav-item .count {
    display: inline-block; margin-left: 6px;
    font-size: 10.5px; color: var(--sky-a);
    background: var(--info-surf); border-radius: 999px; padding: 0 7px;
  }
  .nav-children { overflow: hidden; }
  .nav-child {
    display: block; width: 100%; text-align: left;
    padding: 6px 24px 6px 44px;
    border: none; background: none; cursor: pointer;
    font: inherit; font-size: 12.5px; color: var(--n600);
    border-left: 3px solid transparent;
    position: relative;
  }
  .nav-child::before {
    content: ""; position: absolute; left: 31px; top: 0; bottom: 0;
    width: 1px; background: var(--n200);
  }
  .nav-child:hover { background: var(--n50); color: var(--ink); }
  .nav-child.active { background: var(--info-surf); color: var(--sky-a); border-left-color: var(--sky-a); }
  .nav-item, .nav-child { -webkit-tap-highlight-color: transparent; }
  .hidden { display: none !important; }

  /* ── Main ─────────────────────────────────────────────────────────── */
  .main { overflow-y: auto; }
  .layout {
    display: grid; grid-template-columns: minmax(0, 760px) var(--toc-w);
    gap: 40px; max-width: 1100px; margin: 0 auto; padding: 32px 48px 120px;
  }
  .content { min-width: 0; }

  /* Hero: the additive layer on a deep ground (design system §6–7) */
  .hero {
    position: relative; overflow: hidden;
    background: var(--depth);
    border-radius: var(--r-lg);
    padding: 36px 36px 32px;
    margin-bottom: 28px;
    box-shadow: var(--e2);
  }
  .hero::before, .hero::after {
    content: ""; position: absolute; inset: -20%;
    mix-blend-mode: screen; pointer-events: none;
  }
  .hero::before {
    background:
      radial-gradient(45% 70% at 85% 10%, var(--sky) 0%, transparent 60%),
      radial-gradient(40% 65% at 10% 90%, var(--lilac) 0%, transparent 60%);
    opacity: .5;
  }
  .hero::after {
    background:
      radial-gradient(35% 55% at 70% 90%, var(--mint) 0%, transparent 60%),
      radial-gradient(30% 50% at 25% 0%, var(--peach) 0%, transparent 60%);
    opacity: .4;
  }
  .hero .crumb {
    position: relative; z-index: 1;
    font-size: 12px; letter-spacing: .08em; text-transform: uppercase;
    color: rgba(255,255,255,.66); margin-bottom: 10px;
  }
  .hero h1 {
    position: relative; z-index: 1;
    margin: 0; color: #fff;
    font-size: 27px; line-height: 1.2; font-weight: 500; letter-spacing: -0.025em;
  }
  .hero .sub {
    position: relative; z-index: 1;
    margin: 8px 0 0; color: #B9C4D2; font-size: 15px; line-height: 1.5;
  }
  .hero .belongs {
    position: relative; z-index: 1;
    margin-top: 14px;
  }
  .hero .belongs button {
    font: inherit; font-size: 12.5px; color: var(--depth);
    background: rgba(255,255,255,.92);
    border: none; border-radius: 999px; padding: 4px 12px; cursor: pointer;
  }

  /* ── Markdown body (Lexend scale, design system §9) ──────────────── */
  .doc-body { background: var(--canvas); border: 1px solid var(--n200); border-radius: var(--r-lg); padding: 40px 44px; box-shadow: var(--e1); }
  .doc-body > :first-child { margin-top: 0; }
  .doc-body h1 { font-size: 24px; font-weight: 500; letter-spacing: -0.025em; line-height: 1.2; margin: 0 0 4px; }
  .doc-body h2 { font-size: 21px; font-weight: 500; letter-spacing: -0.02em; line-height: 1.25; margin: 40px 0 12px; padding-bottom: 8px; border-bottom: 1px solid var(--n200); }
  .doc-body h3 { font-size: 17px; font-weight: 500; letter-spacing: -0.01em; margin: 28px 0 8px; }
  .doc-body p { margin: 12px 0; }
  .doc-body strong { font-weight: 500; }
  .doc-body blockquote {
    margin: 18px 0; padding: 14px 20px;
    background: var(--info-surf);
    border-left: 3px solid var(--sky-a);
    border-radius: 0 var(--r-md) var(--r-md) 0;
    color: var(--ink);
  }
  .doc-body blockquote p { margin: 6px 0; }
  .doc-body code {
    background: var(--n100); padding: 1px 6px; border-radius: var(--r-sm);
    font-size: 13.5px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  }
  .doc-body pre { background: var(--n50); border: 1px solid var(--n200); border-radius: var(--r-md); padding: 14px 16px; overflow-x: auto; }
  .doc-body hr { border: none; border-top: 1px solid var(--n200); margin: 32px 0; }
  .doc-body ul, .doc-body ol { padding-left: 24px; }
  .doc-body li { margin: 5px 0; }
  .doc-body table {
    border-collapse: collapse; width: 100%; margin: 16px 0;
    font-size: 14px; display: block; overflow-x: auto;
  }
  .doc-body th, .doc-body td { border: 1px solid var(--n200); padding: 9px 12px; text-align: left; vertical-align: top; }
  .doc-body th { background: var(--n50); font-weight: 500; }
  .doc-body a { color: var(--sky-a); text-decoration: none; }
  .doc-body a:hover { text-decoration: underline; }
  .doc-body em { color: inherit; }
  .doc-body :target { scroll-margin-top: 24px; }
  .anchor { color: var(--n400); text-decoration: none; opacity: 0; margin-left: 8px; font-weight: 400; }
  .doc-body h2:hover .anchor, .doc-body h3:hover .anchor { opacity: 1; }

  /* Individuals gallery at the foot of a persona */
  .people { margin-top: 28px; }
  .people .label { font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--n600); margin: 0 0 12px 4px; }
  .people-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 12px; }
  .person-card {
    text-align: left; font: inherit; cursor: pointer;
    background: var(--canvas); border: 1px solid var(--n200); border-radius: var(--r-md);
    padding: 14px 16px; box-shadow: var(--e1);
    transition: box-shadow 160ms var(--ease), transform 160ms var(--ease);
    position: relative; overflow: hidden;
  }
  .person-card::before {
    content: ""; position: absolute; left: 0; top: 0; bottom: 0; width: 3px;
    background: linear-gradient(180deg, var(--sky), var(--lilac));
    opacity: .85;
  }
  .person-card:hover { box-shadow: var(--e2); transform: translateY(-1px); }
  .person-card .pname { font-weight: 500; font-size: 14px; letter-spacing: -0.01em; }
  .person-card .prole { font-size: 12px; color: var(--n600); margin-top: 3px; }

  /* ── TOC ──────────────────────────────────────────────────────────── */
  .toc { position: sticky; top: 32px; align-self: start; font-size: 13px; max-height: calc(100vh - 64px); overflow-y: auto; }
  .toc .label { font-size: 11.5px; text-transform: uppercase; letter-spacing: .08em; color: var(--n600); margin-bottom: 10px; }
  .toc a { display: block; color: var(--n600); text-decoration: none; padding: 4px 0 4px 12px; border-left: 2px solid var(--n200); transition: color 160ms var(--ease); }
  .toc a:hover { color: var(--ink); }
  .toc a.h3 { padding-left: 26px; font-size: 12px; }
  .toc a.active { color: var(--sky-a); border-left-color: var(--sky-a); }

  .offline { display: none; background: #FCF3E1; color: #8A5A00; padding: 12px 16px; border-radius: var(--r-md); margin-bottom: 20px; font-size: 13.5px; }

  @media (max-width: 1020px) {
    .app { grid-template-columns: 1fr; }
    .sidebar { position: static; height: auto; max-height: 45vh; }
    .layout { grid-template-columns: 1fr; padding: 20px; }
    .toc { display: none; }
    .doc-body { padding: 24px 20px; }
  }
  @media (prefers-reduced-motion: reduce) {
    * { transition: none !important; }
  }
</style>
</head>
<body>
<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <div class="brand-row">
        <div class="orb" aria-hidden="true"></div>
        <div>
          <h1><span class="word">Supervenient</span></h1>
          <p>ACRE personas — Account · Constellation · Role · Edge</p>
        </div>
      </div>
      <div class="stats">__N_PERSONAS__ constellations · __N_INDIVIDUALS__ individuals</div>
      <div class="search"><input id="search" type="search" placeholder="Find a persona or person…" aria-label="Search personas" /></div>
    </div>
    <nav id="nav" aria-label="Persona library"></nav>
  </aside>
  <main class="main">
    <div class="layout">
      <div class="content">
        <div class="offline" id="offline">We couldn't load the markdown renderer (no internet?) — showing raw text.</div>
        <div class="hero" id="hero">
          <div class="crumb" id="hero-crumb"></div>
          <h1 id="hero-title"></h1>
          <p class="sub" id="hero-sub"></p>
          <div class="belongs" id="hero-belongs"></div>
        </div>
        <div class="doc-body" id="doc"></div>
        <div class="people" id="people"></div>
      </div>
      <nav class="toc" id="toc" aria-label="On this page"></nav>
    </div>
  </main>
</div>

<script>
const DOCS = /*__DATA__*/;

/* Flatten: every doc and child addressable by id; children know their parent. */
const FLAT = {};
DOCS.forEach(d => {
  FLAT[d.id] = { ...d, parent: null };
  (d.children || []).forEach(c => { FLAT[c.id] = { ...c, group: d.group, parent: d.id, children: [] }; });
});

function renderMarkdown(md) {
  if (window.marked) return marked.parse(md, { gfm: true, breaks: false });
  document.getElementById("offline").style.display = "block";
  const pre = document.createElement("pre");
  pre.textContent = md;
  return pre.outerHTML;
}

function stripTitle(md) {
  // The hero shows the H1 + first H3 subtitle, so remove them from the body.
  const lines = md.split("\n");
  const out = [];
  let removedH1 = false, removedSub = false;
  for (const line of lines) {
    if (!removedH1 && /^#\s/.test(line)) { removedH1 = true; continue; }
    if (removedH1 && !removedSub) {
      if (/^###\s/.test(line)) { removedSub = true; continue; }
      if (/^\s*$/.test(line)) continue;          // blank between title lines
      if (/^\*\*.+\*\*\s*$/.test(line)) continue; // individual's bold strapline
      removedSub = true;
    }
    out.push(line);
  }
  return out.join("\n").replace(/^\s*(---\s*\n)+/, "");
}

function buildNav(filter) {
  const nav = document.getElementById("nav");
  const q = (filter || "").trim().toLowerCase();
  const groups = {};
  DOCS.forEach(d => { (groups[d.group] = groups[d.group] || []).push(d); });
  nav.innerHTML = "";
  Object.keys(groups).forEach(group => {
    const g = document.createElement("div");
    g.className = "nav-group";
    const label = document.createElement("div");
    label.className = "label";
    label.textContent = group;
    g.appendChild(label);
    let groupHasVisible = false;

    groups[group].forEach(d => {
      const selfMatch = !q || (d.name + " " + d.subtitle).toLowerCase().includes(q);
      const kids = (d.children || []).filter(c => !q || (c.name + " " + c.subtitle).toLowerCase().includes(q));
      if (q && !selfMatch && kids.length === 0) return;
      groupHasVisible = true;

      const item = document.createElement("button");
      item.className = "nav-item";
      item.dataset.id = d.id;
      const count = (d.children || []).length;
      item.innerHTML =
        '<span class="title">' + esc(d.name) + (count ? '<span class="count">' + count + "</span>" : "") + "</span>" +
        '<div class="sub">' + esc(d.subtitle) + "</div>";
      item.onclick = () => selectDoc(d.id);
      g.appendChild(item);

      const kidsWrap = document.createElement("div");
      kidsWrap.className = "nav-children";
      kidsWrap.dataset.parent = d.id;
      const showKids = q ? kids : (d.children || []);
      showKids.forEach(c => {
        const cb = document.createElement("button");
        cb.className = "nav-child";
        cb.dataset.id = c.id;
        cb.textContent = c.name;
        cb.title = c.subtitle;
        cb.onclick = () => selectDoc(c.id);
        kidsWrap.appendChild(cb);
      });
      // Collapsed unless searching or this persona (or one of its people) is active.
      if (!q) kidsWrap.classList.add("hidden");
      g.appendChild(kidsWrap);
    });

    if (groupHasVisible) nav.appendChild(g);
  });
  syncNavActive();
}

function esc(s) {
  return String(s).replace(/[&<>"']/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));
}

function slugify(s) {
  return s.toLowerCase().replace(/[^\w]+/g, "-").replace(/^-+|-+$/g, "");
}

let CURRENT = null;

function syncNavActive() {
  const doc = CURRENT && FLAT[CURRENT];
  const openParent = doc ? (doc.parent || doc.id) : null;
  document.querySelectorAll(".nav-item").forEach(n => {
    n.classList.toggle("active", !!doc && n.dataset.id === doc.id);
  });
  document.querySelectorAll(".nav-child").forEach(n => {
    n.classList.toggle("active", !!doc && n.dataset.id === doc.id);
  });
  document.querySelectorAll(".nav-children").forEach(w => {
    const searching = document.getElementById("search").value.trim() !== "";
    if (searching) return;
    w.classList.toggle("hidden", w.dataset.parent !== openParent);
  });
}

function selectDoc(id) {
  const doc = FLAT[id] || FLAT[DOCS[0].id];
  CURRENT = doc.id;

  // Hero
  const isChild = !!doc.parent;
  document.getElementById("hero-crumb").textContent =
    isChild ? "Individual · " + (FLAT[doc.parent] ? FLAT[doc.parent].name : "") : doc.group;
  document.getElementById("hero-title").textContent = doc.name;
  document.getElementById("hero-sub").textContent = doc.subtitle || "";
  const belongs = document.getElementById("hero-belongs");
  belongs.innerHTML = "";
  if (isChild && FLAT[doc.parent]) {
    const b = document.createElement("button");
    b.textContent = "← Back to constellation";
    b.onclick = () => selectDoc(doc.parent);
    belongs.appendChild(b);
  }

  // Body
  document.getElementById("doc").innerHTML = renderMarkdown(stripTitle(doc.markdown));

  // Individuals gallery
  const people = document.getElementById("people");
  people.innerHTML = "";
  if ((doc.children || []).length) {
    const label = document.createElement("p");
    label.className = "label";
    label.textContent = "The individuals in this constellation";
    people.appendChild(label);
    const grid = document.createElement("div");
    grid.className = "people-grid";
    doc.children.forEach(c => {
      const card = document.createElement("button");
      card.className = "person-card";
      card.innerHTML = '<div class="pname">' + esc(c.name) + '</div><div class="prole">' + esc(c.subtitle) + "</div>";
      card.onclick = () => selectDoc(c.id);
      grid.appendChild(card);
    });
    people.appendChild(grid);
  }

  // TOC
  const target = document.getElementById("doc");
  const toc = document.getElementById("toc");
  const heads = target.querySelectorAll("h2, h3");
  if (heads.length) {
    let tocHtml = '<div class="label">On this page</div>';
    const seen = {};
    heads.forEach(h => {
      let base = slugify(h.textContent) || "section";
      seen[base] = (seen[base] || 0) + 1;
      const hid = seen[base] > 1 ? base + "-" + seen[base] : base;
      h.id = hid;
      h.insertAdjacentHTML("beforeend", '<a class="anchor" href="#' + hid + '">#</a>');
      tocHtml += '<a class="' + h.tagName.toLowerCase() + '" href="#' + hid + '" data-target="' + hid + '">' + esc(h.firstChild.textContent) + "</a>";
    });
    toc.innerHTML = tocHtml;
    toc.style.display = "block";
    wireTocLinks();
  } else {
    toc.innerHTML = "";
    toc.style.display = "none";
  }

  syncNavActive();
  history.replaceState(null, "", "#" + encodeURIComponent(doc.id));
  document.querySelector(".main").scrollTo(0, 0);
}

function wireTocLinks() {
  document.querySelectorAll(".toc a[data-target]").forEach(a => {
    a.onclick = e => {
      e.preventDefault();
      const el = document.getElementById(a.dataset.target);
      if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    };
  });
}

document.querySelector(".main").addEventListener("scroll", () => {
  const heads = [...document.querySelectorAll("#doc h2, #doc h3")];
  let current = null;
  for (const h of heads) {
    if (h.getBoundingClientRect().top < 120) current = h.id; else break;
  }
  document.querySelectorAll(".toc a[data-target]").forEach(a =>
    a.classList.toggle("active", a.dataset.target === current));
});

document.getElementById("search").addEventListener("input", e => buildNav(e.target.value));

buildNav("");
const initial = decodeURIComponent((location.hash || "").slice(1));
selectDoc(FLAT[initial] ? initial : DOCS[0].id);
</script>
</body>
</html>
"""


def main() -> None:
    docs = collect_documents()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_html(docs), encoding="utf-8")
    n_children = sum(len(d["children"]) for d in docs)
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(docs)} document(s) and {n_children} individual(s):")
    for d in docs:
        kids = f" (+{len(d['children'])} individuals)" if d["children"] else ""
        print(f"  - [{d['group']}] {d['name']}{kids}")


if __name__ == "__main__":
    main()
