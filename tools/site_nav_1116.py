# Site-wide findability (Nov 16): subjects index, "On this page" jump nav, cross-links.
# Runs last in build_pages.py, after every page is written. Adds navigation only;
# all links are derived from links and names already on the site. No page text is changed.
import pathlib as _sn_pl, posixpath as _sn_pp, re as _sn_re, json as _sn_json, html as _sn_html

def _sn_strip(s):
    s = _sn_re.sub(r'<span class="tag">.*?</span>', '', s)
    s = _sn_re.sub(r"<[^>]+>", "", s)
    return _sn_re.sub(r"\s+", " ", s).strip()

def _sn_slug(s):
    s = _sn_html.unescape(_sn_strip(s)).lower()
    s = _sn_re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s[:60].strip("-") or "section"

def _sn_files():
    root = _sn_pl.Path(".")
    out = []
    for pat in ("*.html", "generations/*.html", "profiles/*.html", "stories/*.html"):
        out += [str(p) for p in sorted(root.glob(pat)) if not p.name.startswith("_")]
    return out

def _sn_main(h):
    a = h.find("<main>"); b = h.rfind("</main>")
    return (a + 6, b) if a >= 0 and b > a else (None, None)

def _sn_ensure_ids(h):
    """Give every h2 in <main> an id (existing h2/section ids are kept). Returns html, [(id,label)]."""
    a, b = _sn_main(h)
    if a is None:
        return h, []
    m = h[a:b]
    used = set(_sn_re.findall(r'\bid="([^"]+)"', h))
    heads = []
    def rep(mo):
        attrs, inner = mo.group(1), mo.group(2)
        label = _sn_strip(inner)
        idm = _sn_re.search(r'\bid="([^"]+)"', attrs)
        if idm:
            heads.append((idm.group(1), label)); return mo.group(0)
        before = m[:mo.start()]
        sm = _sn_re.search(r'<section[^>]*\bid="([^"]+)"[^>]*>\s*$', before)
        if sm:
            heads.append((sm.group(1), label)); return mo.group(0)
        base = _sn_slug(inner); i = base; n = 2
        while i in used:
            i = f"{base}-{n}"; n += 1
        used.add(i); heads.append((i, label))
        return f'<h2{attrs} id="{i}">{inner}</h2>'
    m2 = _sn_re.sub(r"<h2([^>]*)>(.*?)</h2>", rep, m, flags=_sn_re.S)
    return h[:a] + m2 + h[b:], heads

def _sn_title(h):
    t = _sn_re.search(r"<h1>(.*?)</h1>", h, _sn_re.S)
    return _sn_strip(t.group(1)) if t else ""

SN_EVENTS = [("event-louisbourg", "Louisbourg (1745, 1758)", r"Louisbo?urg"),
             ("event-lexington-concord", "Lexington &amp; Concord (1775)", r"Lexington"),
             ("event-bunker-hill", "Bunker Hill (1775)", r"Bunker Hill|Breed&rsquo;s Hill|Breed's Hill"),
             ("event-saratoga", "Saratoga (1777)", r"Saratoga"),
             ("event-bennington", "Bennington (1777)", r"Bennington"),
             ("event-mill-prison", "The Essex privateer &amp; Mill Prison (1781)", r"Mill Prison")]
SN_CAT = {"places.html": "Places", "essex-privateer.html": "Places", "salem-street-burying-ground.html": "Places",
          "harvard.html": "Places", "businesses.html": "Places", "collections.html": "Artifacts &amp; collections",
          "coat-of-arms.html": "Artifacts &amp; collections", "index.html": "Stories &amp; articles",
          "shea-selee-lineage.html": "Genealogy", "sources.html": "Sources"}
def _sn_cat(f):
    if f.startswith("stories/"): return "Stories &amp; articles"
    if f.startswith("generations/"): return "Genealogy"
    return SN_CAT.get(f)
SN_BACKLINK_PAGES = ("places.html", "essex-privateer.html", "salem-street-burying-ground.html", "harvard.html",
                     "businesses.html", "collections.html", "coat-of-arms.html")

SN_FLAGGED = {"profiles/simon-tufts-11-1.html", "profiles/simon-tufts-1700.html", "profiles/cotton-tufts.html",
              "profiles/joseph-tufts-1755.html", "profiles/joseph-tufts-43-1.html", "profiles/henry-tufts-25-1.html",
              "profiles/henry-tufts-1716.html", "profiles/henry-tufts-1748.html", "profiles/nathan-tufts-15-7.html",
              "profiles/nathan-tufts-cordwainer.html", "profiles/william-tufts-1777.html", "businesses.html",
              "collections.html", "places.html", "generations/modern.html"}

def SN_finalize():
    files = _sn_files()
    people = _sn_json.load(open("data/people.json"))
    pname = {r["slug"]: r["name"] for r in people}
    H, HEADS = {}, {}
    for f in files:
        H[f], HEADS[f] = _sn_ensure_ids(open(f).read())
    for f in files:
        if f.startswith("profiles/"):
            pname.setdefault(f[9:-5], _sn_title(H[f]))
    # Link graph: which non-profile pages link to which profile, and from which section.
    inbound, outlinks, events = {}, {}, {}
    for f in files:
        a, b = _sn_main(H[f])
        if a is None: continue
        m = H[f][a:b]
        txt = _sn_strip(m)
        events[f] = [e for e in SN_EVENTS if _sn_re.search(e[2], txt)]
        if f.startswith("profiles/") or f in ("people.html", "subjects.html"): continue
        for mo in _sn_re.finditer(r'href="([^"#?]+\.html)(?:#[^"]*)?"', m):
            tgt = _sn_pp.normpath(_sn_pp.join(_sn_pp.dirname(f), mo.group(1)))
            if not tgt.startswith("profiles/") or tgt == f or not _sn_pl.Path(tgt).exists(): continue
            slug = tgt[9:-5]
            ids = _sn_re.findall(r'\bid="([^"]+)"', m[:mo.start()])
            sec = ids[-1] if ids else ""
            lab = dict(HEADS[f]).get(sec, "")
            inbound.setdefault(slug, {}).setdefault((f, sec), lab)
            outlinks.setdefault(f, [])
            if slug not in outlinks[f]: outlinks[f].append(slug)
    # Section lists for the subjects page.
    def secs(f, pat=None):
        return [(f, i, l) for i, l in HEADS.get(f, []) if pat is None or _sn_re.search(pat, l, _sn_re.I)]
    nonprof = [f for f in files if not f.startswith("profiles/") and f != "subjects.html"]
    def li_page(f, i, l):
        return f'<li><a href="{{P}}{f}#{i}">{l}</a> <span class="subj-src">&middot; {_sn_title(H[f])}</span></li>'
    def li_file(f, note=""):
        return f'<li><a href="{{P}}{f}">{_sn_title(H[f])}</a>{note}</li>'
    def li_person(s):
        return f'<li><a href="{{P}}profiles/{s}.html">{pname.get(s, s)}</a></li>'
    rw = [r for r in people if r.get("rw") and _sn_pl.Path(f"profiles/{r['slug']}.html").exists()]
    rw.sort(key=lambda r: (r.get("born") or "9999", r["name"]))
    letters = [x for f in nonprof for x in secs(f, r"letter|diar|document|will\b|deed|manuscript|journal|petition")]
    artifacts = secs("collections.html") + [x for f in nonprof if f != "collections.html" for x in secs(f, r"artifact|pitcher|needlework|sampler|portrait|musket|powder horn|heirloom")]
    articles = [x for f in nonprof for x in secs(f, r"newspaper|article|clipping|gazette|magazine|featured")]
    places = secs("places.html")
    by_era = {}
    for r in people:
        if _sn_pl.Path(f"profiles/{r['slug']}.html").exists():
            by_era.setdefault(r.get("era") or "Other", []).append(r)
    listed = {r["slug"] for r in people}
    extra = sorted(s for s in pname if s not in listed and _sn_pl.Path(f"profiles/{s}.html").exists())
    def ul(items): return '<ul class="subj-list">' + "".join(items) + "</ul>"
    body = ['<p>Every page on the site, grouped by subject. This index is rebuilt from the site&rsquo;s own pages and people data each time the site is updated.</p>']
    body.append('<section id="soldiers"><h2>Revolutionary War Soldiers &amp; Sailors</h2><p>Family members with recorded Revolutionary War service, oldest first.</p>'
                + ul(f'<li><a href="{{P}}profiles/{r["slug"]}.html">{r["name"]}</a> <span class="subj-src">&middot; {r.get("town","")}{(" &middot; " + str(r["born"])) if r.get("born") else ""}</span></li>' for r in rw) + "</section>")
    ev = []
    for eid, elab, pat in SN_EVENTS:
        ps = [f for f in files if eid in [e[0] for e in events.get(f, [])] and f != "subjects.html"]
        if not ps: continue
        pro = [f for f in ps if f.startswith("profiles/")]; oth = [f for f in ps if not f.startswith("profiles/")]
        ev.append(f'<h3 id="{eid}">{elab}</h3><p class="subj-src">Pages that name this event:</p>' + ul([li_file(f) for f in oth] + [li_person(f[9:-5]) for f in pro]))
    body.append('<section id="events"><h2>Battles &amp; Events</h2>' + "".join(ev) + "</section>")
    pl = [li_file(f) for f in ("places.html", "essex-privateer.html", "salem-street-burying-ground.html", "harvard.html", "businesses.html") if f in H]
    body.append('<section id="places"><h2>Places</h2>' + ul(pl) + '<h3>Places page sections</h3>' + ul(li_page(*x) for x in places) + "</section>")
    body.append('<section id="artifacts"><h2>Artifacts &amp; Collections</h2>' + ul([li_file(f) for f in ("collections.html", "artifacts.html", "coat-of-arms.html") if f in H] + [li_page(*x) for x in artifacts]) + "</section>")
    body.append('<section id="letters"><h2>Family Letters &amp; Documents</h2>' + ul(li_page(*x) for x in letters) + "</section>")
    gen = [li_file(f) for f in files if f.startswith("generations/")] + [li_file(f) for f in ("people.html", "shea-selee-lineage.html") if f in H]
    eras = "".join(f'<h3 id="era-{_sn_slug(e)}">{e}</h3>' + ul(li_person(r["slug"]) for r in sorted(rs, key=lambda r: r["name"])) for e, rs in by_era.items())
    if extra: eras += '<h3 id="era-other-profiles">Other profiles</h3>' + ul(li_person(s) for s in extra)
    body.append('<section id="genealogy"><h2>Genealogy &amp; Generations</h2>' + ul(gen) + '<h3>All profiles by era</h3>' + eras + "</section>")
    body.append('<section id="stories"><h2>Stories &amp; Articles</h2>' + ul([li_file(f) for f in files if f.startswith("stories/")] + [li_page(*x) for x in articles]) + "</section>")
    body.append('<section id="sources"><h2>Sources</h2>' + ul([li_file("sources.html")] + [li_page(*x) for x in secs("sources.html")]) + "</section>")
    page("subjects.html", "Subjects | Tufts Lineage &amp; Legacy", "Explore", "Browse by Subject", "Soldiers, places, artifacts, letters, generations and stories", "\n".join(body))
    files.append("subjects.html") if "subjects.html" not in files else None
    H["subjects.html"], HEADS["subjects.html"] = _sn_ensure_ids(open("subjects.html").read())
    stats = {"toc": 0, "related": 0, "people_on_page": 0}
    for f in files:
        h = H[f]; pre = "../" * f.count("/")
        a, b = _sn_main(h)
        if a is None: continue
        add = ""
        if f.startswith("profiles/"):
            slug = f[9:-5]; groups = {}
            for (src, sec), lab in sorted(inbound.get(slug, {}).items()):
                cat = _sn_cat(src)
                if not cat: continue
                t = _sn_title(H[src]); href = f"{pre}{src}" + (f"#{sec}" if sec else "")
                groups.setdefault(cat, []).append(f'<li><a href="{href}">{t}{(" &mdash; " + lab) if lab and lab != t else ""}</a></li>')
            evs = [f'<li><a href="{pre}subjects.html#{e[0]}">{e[1]}</a></li>' for e in events.get(f, [])]
            if any(e[0] == "event-mill-prison" for e in events.get(f, [])) and not any(s == "essex-privateer.html" for s, _ in inbound.get(slug, {})):
                evs.append(f'<li><a href="{pre}essex-privateer.html">The Privateer Essex and Mill Prison</a></li>')
            if groups or evs:
                parts = [f"<h3>{c}</h3><ul>{''.join(dict.fromkeys(v))}</ul>" for c, v in groups.items()]
                if evs: parts.append(f"<h3>Battles &amp; events named on this page</h3><ul>{''.join(evs)}</ul>")
                add = (f'<section id="related" class="sn-related"><h2>Related Places &amp; Articles</h2><p>Other pages on this site that mention {pname.get(slug, "this person")}.</p>'
                       + "".join(parts) + f'<p><a href="{pre}subjects.html">Browse all subjects</a></p></section>')
                stats["related"] += 1
        elif (f in SN_BACKLINK_PAGES or f.startswith("stories/")) and outlinks.get(f):
            items = sorted(outlinks[f], key=lambda s: pname.get(s, s))
            add = ('<section id="people-on-this-page" class="sn-related"><h2>People on This Page</h2><ul class="subj-list">'
                   + "".join(f'<li><a href="{pre}profiles/{s}.html">{pname.get(s, s)}</a></li>' for s in items) + "</ul></section>")
            stats["people_on_page"] += 1
        if f == "index.html":
            k = h.find("</section>", h.find('<section id="featured">'))
            if k > 0:
                k += len("</section>")
                block = (f'\n<section id="browse-by-subject" class="sn-browse"><h2>Browse by Subject</h2><ul class="subj-grid">'
                         + "".join(f'<li><a href="subjects.html#{i}">{l}</a></li>' for i, l in [("soldiers", "Revolutionary Soldiers"), ("events", "Battles &amp; Events"), ("places", "Places"), ("artifacts", "Artifacts &amp; Collections"), ("letters", "Family Letters &amp; Documents"), ("genealogy", "Genealogy &amp; Generations"), ("stories", "Stories &amp; Articles"), ("sources", "Sources")])
                         + "</ul></section>")
                h = h[:k] + block + h[k:]
        if add:
            b = h.rfind("</main>"); h = h[:b] + add + "\n" + h[b:]
        h, heads = _sn_ensure_ids(h)
        if len(heads) >= 3:
            toc = ('<nav class="toc" aria-label="On this page"><details open><summary>On this page</summary><ol>'
                   + '<li><a href="#top">Top</a></li>' + "".join(f'<li><a href="#{i}">{l}</a></li>' for i, l in heads) + "</ol></details></nav>\n")
            a = h.find("<main>") + 6
            h = h[:a] + "\n" + toc + h[a:]
            b = h.rfind("</main>")
            h = h[:b] + '<p class="to-top"><a href="#top">Back to top &uarr;</a></p>\n' + h[b:]
            stats["toc"] += 1
        h = h.replace('<header class="chainmail">', '<header class="chainmail" id="top">', 1) if 'id="top"' not in h else h
        h = _sn_re.sub(r'(<img\b[^>]*?\balt=")([^"]*<[^"]*)(")', lambda mo: mo.group(1) + _sn_strip(mo.group(2)) + mo.group(3), h)
        if f in SN_FLAGGED or (f.startswith("profiles/") and not _sn_re.search(r"<img(?![^>]*rw-icon)", h[h.find("<main>"):])):
            if 'class="review-flag"' not in h:
                h = _sn_re.sub(r"(<header[^>]*>.*?</h1>)", r'\1<span class="review-flag" title="Flagged for review" aria-hidden="true"></span>', h, count=1, flags=_sn_re.S)
            stats["flagged"] = stats.get("flagged", 0) + 1
        h = RW_apply(h, pre, f)
        open(f, "w").write(h)
    print("site_nav:", stats, "pages:", len(files))
    return stats
SN_finalize()
