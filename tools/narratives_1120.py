# Opening narrative summaries for Revolutionary service profiles.
# Reads data/narratives.json (keyed by profile filename) and inserts a
# <section class="narrative-summary"> at the top of each page's main
# content, after the "On this page" nav when present. Idempotent.
import json as _nv_json, re as _nv_re, os as _nv_os, glob as _nv_glob, pathlib as _nv_pl

_NV_PATH = "data/narratives.json"
_NV_SEC = _nv_re.compile(r"[ \t]*<section class=\"narrative-summary\">.*?</section>\s*", _nv_re.S)
_NV_MAIN_TOP = _nv_re.compile(
    r'(<main>\s*(?:<nav class="toc"[^>]*>.*?</nav>\s*)?)',
    _nv_re.S,
)

def _nv_block(inner):
    inner = inner.strip()
    return (
        '<section class="narrative-summary">\n'
        + inner + "\n"
        + '<p class="narrative-source">Summary drawn from the sources cited on this page.</p>\n'
        + "</section>\n"
    )

def _nv_apply_file(path, inner):
    h = open(path).read()
    if 'http-equiv="refresh"' in h:
        return False
    block = _nv_block(inner)
    h2 = _NV_SEC.sub("", h)
    m = _NV_MAIN_TOP.search(h2)
    if not m:
        return False
    h2 = h2[: m.end()] + block + h2[m.end() :]
    if h2 != h:
        open(path, "w").write(h2)
        return True
    return False

def _nv_remap_john_links():
    """Point leftover john-tufts-1754 links at the merged 53-3 page."""
    n = 0
    paths = (
        _nv_glob.glob("*.html")
        + _nv_glob.glob("profiles/*.html")
        + _nv_glob.glob("generations/*.html")
        + _nv_glob.glob("stories/*.html")
        + _nv_glob.glob("sources/*.html")
    )
    for f in paths:
        if f.endswith("john-tufts-1754.html"):
            continue
        h = open(f).read()
        h2 = h.replace("profiles/john-tufts-1754.html", "profiles/john-tufts-53-3.html")
        if f.startswith("profiles/"):
            h2 = h2.replace('href="john-tufts-1754.html"', 'href="john-tufts-53-3.html"')
        if h2 != h:
            open(f, "w").write(h2)
            n += 1
    pj = "data/people.json"
    if _nv_os.path.exists(pj):
        people = _nv_json.loads(open(pj).read())
        new = [r for r in people if r.get("slug") != "john-tufts-1754"]
        for rec in new:
            if rec.get("profile") == "profiles/john-tufts-1754.html":
                rec["profile"] = "profiles/john-tufts-53-3.html"
        txt = _nv_json.dumps(new, indent=2) + "\n"
        if txt != open(pj).read():
            open(pj, "w").write(txt)
            n += 1
    return n

def NV_apply():
    data = _nv_json.loads(open(_NV_PATH).read())
    updated, skipped = [], []
    for fname, rec in data.items():
        path = fname if fname.startswith("profiles/") else "profiles/" + fname
        if not _nv_os.path.exists(path):
            skipped.append((fname, "file not found"))
            continue
        h = open(path).read()
        if 'http-equiv="refresh"' in h:
            skipped.append((fname, "redirect page"))
            continue
        inner = rec if isinstance(rec, str) else rec.get("html") or rec.get("body") or ""
        if not str(inner).strip():
            skipped.append((fname, "empty narrative"))
            continue
        _nv_apply_file(path, inner)
        updated.append(_nv_pl.Path(path).name)
    remapped = _nv_remap_john_links()
    print(
        "narratives_1120: updated",
        len(updated),
        "; skipped",
        skipped,
        "; link files remapped",
        remapped,
    )

NV_apply()
