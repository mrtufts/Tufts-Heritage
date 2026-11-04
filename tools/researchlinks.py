# Further research links per person/page (data/research_links.json). No attribution to any outside index.
import json as _j
from urllib.parse import urlparse as _up
RL = _j.load(open("data/research_links.json"))
def _src(u):
    h = _up(u).netloc.lower().replace("www.", "")
    return {"ia600505.us.archive.org": "Internet Archive", "archive.org": "Internet Archive", "findagrave.com": "Find a Grave", "en.wikipedia.org": "Wikipedia",
            "founders.archives.gov": "Founders Online (National Archives)", "masshist.org": "Massachusetts Historical Society", "familysearch.org": "FamilySearch",
            "tuftsgenealogy.blogspot.com": "Tufts Genealogy blog", "wikitree.com": "WikiTree", "hmdb.org": "HMdb"}.get(h, h)
def RLSEC(path):
    d = RL.get(path)
    if not d: return ""
    li = []; _seen = set()
    for u, e in d.items():
        _k = re.sub(r'^https?://(www\.)?', '', u).rstrip('/')
        if _k in _seen: continue
        _seen.add(_k)
        if 'tuftsgenealogy.blogspot' in u: continue  # owner rule 2026-11-04: blog links only where firsthand and untraced (see links_resources.py BLOG_KEEP)
        lab = " / ".join(e["labels"][:3]) or _src(u)
        br = ' <span class="tag">link reported broken (checked 2026-11-03)</span>' if e["broken"] else ""
        nt = f' <em>{e["note"]}</em>' if e["note"] else ""
        li.append(f'<li><a href="{u}">{lab}</a> ({_src(u)}){br}{nt}</li>')
    return '{DIV}<section id="research-links"><h2>Further Research Links</h2><p>Outside resources for further research. Secondary and user-contributed sites (blogs, family trees, memorial sites, Wikipedia) are not verified here.</p><ul>' + "".join(li) + "</ul></section>"
_EXTRA4 = EXTRA
def EXTRA(path):
    return _EXTRA4(path) + RLSEC(path)
