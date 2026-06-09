#!/usr/bin/env python3
"""Build a self-contained HTML viewer for all ACRE personas.

Scans the `personas/` tree for `*.md` files and bakes their raw markdown into a
single `tool/index.html`. The markdown is embedded inline (not fetched), so the
result works by simply double-clicking the file — no local server needed.

Usage:
    python3 tool/build.py

Re-run whenever you add or edit personas.
"""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PERSONAS_DIR = ROOT / "personas"
ABOUT_FILE = ROOT / "about-acre-personas.md"
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


def collect_documents() -> list[dict]:
    docs: list[dict] = []

    # Intro / framework doc first, if present.
    if ABOUT_FILE.exists():
        text = ABOUT_FILE.read_text(encoding="utf-8")
        docs.append(
            {
                "id": "about",
                "group": "About",
                "name": first_heading(text) or "About ACRE Personas",
                "subtitle": "The framework",
                "markdown": text,
            }
        )

    # Each persona markdown file, grouped by its top-level status folder.
    # Sort by persona number where present, then by path.
    persona_paths = sorted(
        PERSONAS_DIR.rglob("*.md"),
        key=lambda p: (persona_number(p.read_text(encoding="utf-8")), str(p)),
    )
    for md_path in persona_paths:
        rel = md_path.relative_to(PERSONAS_DIR)
        parts = rel.parts
        # personas/<status>/<name>/<file>.md  -> group=status, name=<name>
        group = parts[0] if len(parts) > 1 else "personas"
        slug = parts[-2] if len(parts) > 1 else md_path.stem
        text = md_path.read_text(encoding="utf-8")
        docs.append(
            {
                "id": "/".join(parts),
                "group": group.replace("-", " ").title(),
                "name": first_heading(text) or slug,
                "subtitle": str(rel.parent),
                "markdown": text,
            }
        )

    return docs


def build_html(docs: list[dict]) -> str:
    data_json = json.dumps(docs, ensure_ascii=False)
    return TEMPLATE.replace("/*__DATA__*/", data_json)


TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>ACRE Personas</title>
<script src="https://cdn.jsdelivr.net/npm/marked@12/marked.min.js"></script>
<style>
  :root {
    --bg: #f7f6f3;
    --panel: #ffffff;
    --ink: #1f2328;
    --muted: #6b7280;
    --line: #e6e3dd;
    --accent: #7c4dff;
    --accent-soft: #efe9ff;
    --sidebar-w: 300px;
    --toc-w: 240px;
  }
  * { box-sizing: border-box; }
  html, body { margin: 0; height: 100%; }
  body {
    font: 15px/1.6 -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--ink);
    background: var(--bg);
  }
  .app { display: grid; grid-template-columns: var(--sidebar-w) 1fr; height: 100vh; }

  /* Sidebar */
  .sidebar {
    border-right: 1px solid var(--line);
    background: var(--panel);
    overflow-y: auto;
    padding: 20px 0;
  }
  .brand { padding: 0 20px 16px; }
  .brand h1 { font-size: 16px; margin: 0; letter-spacing: .3px; }
  .brand p { margin: 4px 0 0; color: var(--muted); font-size: 12px; }
  .nav-group { margin-top: 14px; }
  .nav-group > .label {
    padding: 6px 20px;
    font-size: 11px;
    text-transform: uppercase;
    letter-spacing: .8px;
    color: var(--muted);
  }
  .nav-item {
    display: block;
    padding: 8px 20px;
    cursor: pointer;
    border-left: 3px solid transparent;
    color: var(--ink);
  }
  .nav-item:hover { background: #faf9f6; }
  .nav-item.active { background: var(--accent-soft); border-left-color: var(--accent); }
  .nav-item .title { font-weight: 600; font-size: 13.5px; }
  .nav-item .sub { font-size: 11.5px; color: var(--muted); margin-top: 2px; }

  /* Main */
  .main { overflow-y: auto; }
  .layout { display: grid; grid-template-columns: 1fr var(--toc-w); gap: 32px; max-width: 1200px; margin: 0 auto; padding: 40px 48px 120px; }
  .content { min-width: 0; }
  .toc { position: sticky; top: 40px; align-self: start; font-size: 13px; }
  .toc .label { font-size: 11px; text-transform: uppercase; letter-spacing: .8px; color: var(--muted); margin-bottom: 10px; }
  .toc a { display: block; color: var(--muted); text-decoration: none; padding: 4px 0; border-left: 2px solid var(--line); padding-left: 12px; }
  .toc a:hover { color: var(--ink); }
  .toc a.h3 { padding-left: 26px; font-size: 12.5px; }
  .toc a.active { color: var(--accent); border-left-color: var(--accent); }

  /* Markdown styling */
  .content h1 { font-size: 28px; line-height: 1.25; margin: 0 0 4px; }
  .content h2 { font-size: 21px; margin: 38px 0 12px; padding-bottom: 6px; border-bottom: 1px solid var(--line); }
  .content h3 { font-size: 17px; margin: 26px 0 8px; }
  .content p { margin: 12px 0; }
  .content blockquote { margin: 16px 0; padding: 8px 18px; border-left: 4px solid var(--accent); background: var(--accent-soft); color: #3a3550; border-radius: 0 6px 6px 0; }
  .content blockquote p { margin: 6px 0; }
  .content code { background: #f0eee9; padding: 1px 6px; border-radius: 4px; font-size: 13px; font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; }
  .content hr { border: none; border-top: 1px solid var(--line); margin: 32px 0; }
  .content ul, .content ol { padding-left: 22px; }
  .content li { margin: 4px 0; }
  .content table { border-collapse: collapse; width: 100%; margin: 16px 0; font-size: 13.5px; display: block; overflow-x: auto; }
  .content th, .content td { border: 1px solid var(--line); padding: 8px 12px; text-align: left; vertical-align: top; }
  .content th { background: #faf9f6; font-weight: 600; }
  .content tr:nth-child(even) td { background: #fcfbf9; }
  .content a { color: var(--accent); }
  .content :target { scroll-margin-top: 24px; }

  .anchor { color: var(--muted); text-decoration: none; opacity: 0; margin-left: 8px; font-weight: normal; }
  .content h2:hover .anchor, .content h3:hover .anchor { opacity: 1; }

  .offline { display: none; background: #fff3cd; color: #664d03; padding: 12px 16px; border-radius: 8px; margin-bottom: 20px; font-size: 13px; }

  @media (max-width: 1000px) {
    .app { grid-template-columns: 1fr; }
    .sidebar { position: static; height: auto; max-height: 40vh; }
    .layout { grid-template-columns: 1fr; padding: 24px; }
    .toc { display: none; }
  }
</style>
</head>
<body>
<div class="app">
  <aside class="sidebar">
    <div class="brand">
      <h1>ACRE Personas</h1>
      <p>Account · Constellation · Role · Edge</p>
    </div>
    <nav id="nav"></nav>
  </aside>
  <main class="main">
    <div class="layout">
      <div class="content">
        <div class="offline" id="offline">
          Couldn't load the markdown renderer (no internet?). Showing raw text.
        </div>
        <div id="doc"></div>
      </div>
      <nav class="toc" id="toc"></nav>
    </div>
  </main>
</div>

<script>
const DOCS = /*__DATA__*/;

function slugify(s) {
  return s.toLowerCase().replace(/[^\w]+/g, "-").replace(/^-+|-+$/g, "");
}

function renderMarkdown(md) {
  if (window.marked) {
    return marked.parse(md, { gfm: true, breaks: false });
  }
  document.getElementById("offline").style.display = "block";
  const pre = document.createElement("pre");
  pre.textContent = md;
  return pre.outerHTML;
}

function buildNav() {
  const nav = document.getElementById("nav");
  const groups = {};
  DOCS.forEach((d, i) => {
    (groups[d.group] = groups[d.group] || []).push({ ...d, index: i });
  });
  nav.innerHTML = "";
  Object.keys(groups).forEach(group => {
    const g = document.createElement("div");
    g.className = "nav-group";
    g.innerHTML = `<div class="label">${group}</div>`;
    groups[group].forEach(d => {
      const item = document.createElement("a");
      item.className = "nav-item";
      item.dataset.id = d.id;
      item.innerHTML = `<div class="title">${d.name}</div><div class="sub">${d.subtitle}</div>`;
      item.onclick = (e) => { e.preventDefault(); selectDoc(d.id); };
      g.appendChild(item);
    });
    nav.appendChild(g);
  });
}

function selectDoc(id) {
  const doc = DOCS.find(d => d.id === id) || DOCS[0];
  document.querySelectorAll(".nav-item").forEach(n =>
    n.classList.toggle("active", n.dataset.id === doc.id));

  const target = document.getElementById("doc");
  target.innerHTML = renderMarkdown(doc.markdown);

  // Give headings ids + anchors, and build the table of contents.
  const toc = document.getElementById("toc");
  const heads = target.querySelectorAll("h2, h3");
  if (heads.length) {
    let tocHtml = '<div class="label">On this page</div>';
    const seen = {};
    heads.forEach(h => {
      let base = slugify(h.textContent) || "section";
      seen[base] = (seen[base] || 0) + 1;
      const hid = seen[base] > 1 ? `${base}-${seen[base]}` : base;
      h.id = hid;
      h.insertAdjacentHTML("beforeend", `<a class="anchor" href="#${hid}">#</a>`);
      tocHtml += `<a class="${h.tagName.toLowerCase()}" href="#${hid}" data-target="${hid}">${h.firstChild.textContent}</a>`;
    });
    toc.innerHTML = tocHtml;
    toc.style.display = "block";
    wireTocLinks();
  } else {
    toc.innerHTML = "";
    toc.style.display = "none";
  }

  history.replaceState(null, "", "#" + encodeURIComponent(doc.id));
  document.querySelector(".main").scrollTo(0, 0);
}

function wireTocLinks() {
  document.querySelectorAll(".toc a[data-target]").forEach(a => {
    a.onclick = (e) => {
      e.preventDefault();
      const el = document.getElementById(a.dataset.target);
      if (el) el.scrollIntoView({ behavior: "smooth", block: "start" });
    };
  });
}

// Highlight the current section in the TOC while scrolling.
document.querySelector(".main").addEventListener("scroll", () => {
  const heads = [...document.querySelectorAll("#doc h2, #doc h3")];
  let current = null;
  for (const h of heads) {
    if (h.getBoundingClientRect().top < 120) current = h.id; else break;
  }
  document.querySelectorAll(".toc a[data-target]").forEach(a =>
    a.classList.toggle("active", a.dataset.target === current));
});

buildNav();
const initial = decodeURIComponent((location.hash || "").slice(1));
selectDoc(DOCS.find(d => d.id === initial) ? initial : (DOCS[0] && DOCS[0].id));
</script>
</body>
</html>
"""


def main() -> None:
    docs = collect_documents()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(build_html(docs), encoding="utf-8")
    print(f"Wrote {OUTPUT.relative_to(ROOT)} with {len(docs)} document(s):")
    for d in docs:
        print(f"  - [{d['group']}] {d['name']}")


if __name__ == "__main__":
    main()
