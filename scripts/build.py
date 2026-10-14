"""Build the static site: data/ + src/index.template.html -> dist/index.html.

Usage: python scripts/build.py            (needs the `markdown` package)
"""
import html
import json
import pathlib
import re

import markdown

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SITE = json.loads((ROOT / "site.json").read_text())
EXAMS = SITE["exams"]  # display order


def md_to_html(text, base):
    text = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)[^\n]*\n?", "", text)  # linked images
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)                           # images
    text = re.sub(r"^Save or share the card above; the full sheet follows\.\s*$", "", text, flags=re.M)
    h = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    h = re.sub(r'<pre><code class="language-mermaid">(.*?)</code></pre>', r'<pre class="mdiag">\1</pre>', h, flags=re.S)
    h = h.replace("<table>", '<div class="tscroll"><table>').replace("</table>", "</table></div>")

    def link(m):
        u = m.group(1)
        if u.startswith("http"):
            return f'href="{u}" target="_blank" rel="noopener"'
        if u.startswith(("#", "mailto:")):
            return m.group(0)
        return f'href="{base}{u.lstrip("./")}" target="_blank" rel="noopener"'
    return re.sub(r'href="([^"]+)"', link, h)


def split_h2(text):
    """Split markdown at level-2 headings; the level-1 title is dropped."""
    parts, title, cur = [], None, []
    for ln in text.splitlines():
        if ln.startswith("## "):
            if title is not None or "".join(cur).strip():
                parts.append((title, "\n".join(cur)))
            title, cur = ln[3:].strip(), []
        elif ln.startswith("# "):
            continue
        else:
            cur.append(ln)
    parts.append((title, "\n".join(cur)))
    return [(t or "Overview", b) for t, b in parts if b.strip()]


def docs_html(exam):
    index_file = DATA / exam / "docs" / "index.json"
    if not index_file.exists():
        return [], ""
    index = json.loads(index_file.read_text())
    out = []
    for d in index:
        sections = []
        for f in d["files"]:
            text = (DATA / exam / "docs" / f).read_text()
            if d["split"] == "files":
                title = re.search(r"^# (.+)", text, re.M).group(1)
                title = re.sub(r"\s+[—-]\s+Cheat Sheet$", "", title)
                body = re.sub(r"^# .+\n", "", text, count=1).replace("\n## ", "\n### ")
                sections.append((title, md_to_html(body, d["base"])))
            else:
                sections += [(t, md_to_html(b, d["base"])) for t, b in split_h2(text)]
        secs = "".join(f'<section class="dsec" id="{d["id"]}-{i}"><h2 class="dtitle">{html.escape(t)}</h2>{b}</section>'
                       for i, (t, b) in enumerate(sections))
        out.append(f'<article class="doc prose" data-doc="{d["id"]}" hidden>{secs}'
                   f'<p class="docsrc">Source: <a href="{d["src"]}" target="_blank" rel="noopener">{html.escape(d["src"])}</a></p></article>')
    return [{"id": d["id"], "label": d["label"], "src": d["src"]} for d in index], "\n".join(out)


def load_exam(exam):
    d = DATA / exam
    cert = json.loads((d / "exam.json").read_text())
    qs = []
    for bank in [b for b, _ in cert["banks"]] + cert.get("hiddenBanks", []):
        if bank and (d / f"questions-{bank}.json").exists():
            qs += json.loads((d / f"questions-{bank}.json").read_text())
    cert["questions"] = qs
    if (d / "recall.json").exists():
        cert["recall"] = json.loads((d / "recall.json").read_text())
        cert["guide"] = json.loads((d / "guide.json").read_text())
    return cert


def main():
    certs, docs_markup = {}, []
    for exam in EXAMS:
        cert = load_exam(exam)
        docs, markup = docs_html(exam)
        if docs:
            cert["docs"] = docs
            docs_markup.append(markup)
        certs[exam] = cert
    data = {"certs": certs, "repo": SITE.get("repo", ""), "siteUrl": SITE.get("siteUrl", "")}
    page = (ROOT / "src" / "index.template.html").read_text()
    page = page.replace("<!--__DOCS__-->", "\n".join(docs_markup))
    page = page.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False).replace("</", "<\\/"))
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    (out / "index.html").write_text(page)
    (out / ".nojekyll").write_text("")
    total = sum(len(c["questions"]) for c in certs.values())
    print(f"dist/index.html: {len(page) // 1024} KB, {total} questions across {len(certs)} exams")


if __name__ == "__main__":
    main()
