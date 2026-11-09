"""Post-build pass: adds a grouped "Links and Resources" section to every profile page.
Collects every outside source, scan, map, survey, marker, grave and on-site place/artifact entry
already cited on the page, plus curated links (CUR) for maps, surveys and artifacts tied to the person.
Run automatically at the end of tools/build_pages.py."""
import glob, re, html as _h
from bs4 import BeautifulSoup
from urllib.parse import urlparse

GROUPS = ["Maps, Surveys and Artifacts", "Graves and Memorials", "Markers, Plaques and Places", "Digitized Books and Journals",
          "Archives, Letters and Records", "Biographies and Family Trees", "Related Pages on This Site", "Other Resources"]
GNOTE = {"Biographies and Family Trees": "Secondary and user-contributed sites; not verified here."}
SURV = "places.html#survey-1797"
CUR = {
 "peter-tufts-1774": [
  ("Maps, Surveys and Artifacts", SURV, "Road from Concord to Cambridge, survey by Peter Tufts junior (1797)", "This site&rsquo;s entry for his manuscript survey of the April 19, 1775 road, signed June 14, 1797."),
  ("Maps, Surveys and Artifacts", "places.html#maps", "Plan of Charlestown Peninsula (1818)", "His engraved plan &ldquo;from accurate survey by Peter Tufts Jun<sup>r</sup>. Esq<sup>r</sup>.&rdquo;, shown on Places: Maps, with the 1794 Medford plan that may be his or his father&rsquo;s."),
  ("Maps, Surveys and Artifacts", "https://bostonraremaps.com/inventory/peter-tufts-survey-concord-cambridge-1797/", "Boston Rare Maps, inventory BRM3348", "Dealer description and images of the 1797 survey (privately held; linked, not reproduced)."),
  ("Markers, Plaques and Places", "places.html#powder-house", "The Powder House, Somerville", "He was keeper of the Powder House until 1815 (Booth, p. 22)."),
 ],
 "peter-tufts-jr": [
  ("Maps, Surveys and Artifacts", "places.html#maps", "Plans of Medford (1794) and Charlestown Peninsula (1818)", "Plans signed by a Peter Tufts Jun<sup>r</sup>; the 1818 plan is by his son Peter the surveyor, and the 1794 plan may be his or his son&rsquo;s."),
  ("Maps, Surveys and Artifacts", SURV, "Road from Concord to Cambridge survey (1797)", "Drawn by his son Peter the surveyor, then signing as &ldquo;Peter Tufts junior.&rdquo;"),
  ("Markers, Plaques and Places", "places.html#powder-house", "The Powder House, Somerville", "In 1788 he bought the farm opposite the Powder House (Booth, p. 22)."),
 ],
 "anne-adams-tufts": [
  ("Markers, Plaques and Places", "generations/colonial.html#anne-adams", "The 1909 DAR tablet on her door-stone", "Photographs and transcription of the tablet in Paul Revere Park, Somerville."),
  ("Markers, Plaques and Places", "https://www.hmdb.org/m.asp?m=248718", "HMdb marker 248718: Anne Adams-Tufts", "Historical Marker Database entry with photographs and location."),
  ("Maps, Surveys and Artifacts", "places.html#siege-plan-1776", "Siege of Boston plan (1776)", "Shows the siege lines across the Winter Hill land where she nursed the wounded."),
 ],
 "timothy-tufts": [("Maps, Surveys and Artifacts", "places.html#siege-plan-1776", "Siege of Boston plan (1776)", "Shows the lines across the Charlestown mainland near his Elm Street house."),
                   ("Maps, Surveys and Artifacts", SURV, "Road from Concord to Cambridge survey (1797)", "The road the British marched past his house on April 19, 1775, drawn by his grandnephew.")],
}
for _s in ("william-tufts-1802", "edward-tufts-1806", "george-f-tufts-1825", "alfred-tufts-1829"):
    CUR[_s] = [("Maps, Surveys and Artifacts", "places.html#tufts-subdivisions", "The Tufts subdivisions of South Medford", "This site&rsquo;s entry on the 1854 and 1861 plans labeled &ldquo;W E G F &amp; A Tufts.&rdquo;"),
               ("Markers, Plaques and Places", "https://medfordhistoricalcommission.org/wp-content/uploads/2022/02/area-edward.pdf", "Medford Historical Commission, Edward Street Area (2022)", "Inventory form with the Walling (1855), Beers (1875) and Walker (1889) maps and the subdivision plans.")]
CUR.setdefault("cotton-tufts", []).append(("Maps, Surveys and Artifacts", "coat-of-arms.html#armories", "The Tufts Coat of Arms: the Norton tankard", "Bolton&rsquo;s <em>American Armory</em> (1927) records the Norton arms on a tankard given by Elizabeth Quincy to her daughter Lucy Tufts, his first wife."))
CUR["alfred-tufts-1829"].insert(0, ("Maps, Surveys and Artifacts", "places.html#tufts-subdivisions", "Subdivision plans surveyed by Alfred Tufts", "MCSRD Plans 7:19 (1854), 9a:9 and plan book 10, plan 17 (1861), described on Places."))
del CUR["alfred-tufts-1829"][1]


for _s,_items in {
 "cotton-tufts": [
  ("Markers, Plaques and Places", "places.html#tufts-library", "Tufts Library, Weymouth", "Founded by his grandchildren Quincy and Susannah."),
  ("Markers, Plaques and Places", "places.html#tufts-corner", "Tufts Corner / Tufts & Whittemore store", "His son Cotton Jr.&rsquo;s store at Weymouth Landing."),
  ("Archives, Letters and Records", "https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection", "Weymouth Tufts/Smith/Adams finding aid", "Municipal finding aid for the family papers."),
  ("Digitized Books and Journals", "https://archive.org/details/mobot31753002119144", "Memoirs of the American Academy of Arts and Sciences, Vol. I (1785)", "First Memoirs volume (Boston: Adams and Nourse, 1785); title page and preface reprint the Academy&rsquo;s act of incorporation."),
  ("Digitized Books and Journals", "https://archive.org/details/jstor-25053737", "A List of the American Academy of Arts and Sciences, 1785", "Printed list naming Hon. Cotton Tufts, Esq; M. D. F. M. S. among the Council."),
  ("Archives, Letters and Records", "https://www.amacad.org/archives/charter", "American Academy charter and charter members", "Academy archives page with the 1780 act and the list of 62 incorporators, including Cotton Tufts."),
 ],
 "cotton-tufts-jr": [
  ("Markers, Plaques and Places", "places.html#tufts-corner", "Tufts Corner", "Tufts &amp; Whittemore store and circulating library."),
  ("Archives, Letters and Records", "https://www.historicnewengland.org/explore/collections-access/gusn/194087/", "Historic New England stock book (1823)", "Tufts &amp; Whittemore inventory."),
 ],
 "quincy-tufts": [("Markers, Plaques and Places", "places.html#tufts-library", "Tufts Library", "Co-founder by bequest (1879).")],
 "susannah-tufts-1797": [("Markers, Plaques and Places", "places.html#tufts-library", "Tufts Library", "Co-founder by bequest (1879).")],
 "mercy-brooks-tufts": [("Archives, Letters and Records", "https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection", "Weymouth finding aid", "Notes her 1799 diary in the family papers.")],
}.items():
    CUR.setdefault(_s, [])
    for it in _items:
        if it not in CUR[_s]:
            CUR[_s].append(it)

import json as _json
BROKEN = {"http://www.battleroad.net/rememberingthefallen/gravesite17.html"}
for _pg, _d in _json.load(open("data/research_links.json")).items():
    BROKEN |= {u for u, e in _d.items() if e.get("broken")}
# Owner rule (2026-11-04): Tufts genealogy blog links stay only where the post holds firsthand material
# not traced to an authoritative source; each kept fact carries a red Unverified box.
_BP = "https://tuftsgenealogy.blogspot.com/2014/"
BLOG_KEEP = {
 "zachariah-tufts": (_BP + "01/zachariah-tufts-revolutionary-soldier.html", "Blog post transcribing his New Hampshire pension record (Cheshire County, 1818)",
   "Pension record (Cheshire County, N.H., 1818), as transcribed on a family blog: service in 1776 as a private in Capt. Hale&rsquo;s company, Col. John Stark&rsquo;s N.H. regiment, and in 1777&ndash;1779 in Capt. Hale&rsquo;s company of Col. Morgan&rsquo;s riflemen; one pension names the 15th Virginia Regiment. The original pension file has not been seen here."),
 "adam-tufts": (_BP + "02/tufts-military-history-part-two-all.html", "Blog post with an image of a marriage intention for Adam, &ldquo;negro&rdquo; servant of Stephen Tufts of Malden",
   "A marriage intention record (image on a family blog) names Adam as a Negro servant of Stephen Tufts of Malden. The original register and page have not been identified here."),
 "aaron-tufts": (_BP + "02/tufts-military-history-part-two-all.html", "Blog post with an image of his entry in <em>Mariners of the American Revolution</em>",
   "Naval service, from an entry in <em>Mariners of the American Revolution</em> (image on a family blog). The book, edition and page have not been checked here."),
 "ebenezer-tufts-36-7": (_BP + "02/tufts-military-history-part-two-all.html", "Blog post summarizing his pension application",
   "His pension application, as summarized on a family blog, swears to service in Col. Loammi Baldwin&rsquo;s regiment; the blog adds marriages to Hannah Levistone (1781) and Elizabeth Traverse (1802) and residence at Marlborough by 1810. The pension file has not been seen here."),
}
def group(u):
    h = urlparse(u).netloc.lower().replace("www.", ""); p = u.lower()
    if not h:
        if "burying" in p: return "Graves and Memorials"
        if any(k in p for k in ("#maps", "survey", "subdivision", "collections", "siege", "images", "letters", "musket", ".jpg", ".pdf")): return "Maps, Surveys and Artifacts"
        if any(k in p for k in ("places", "businesses", "harvard")): return "Markers, Plaques and Places"
        if "sources" in p: return "Digitized Books and Journals"
        return "Related Pages on This Site"
    if any(k in h for k in ("findagrave", "billiongraves", "interment")): return "Graves and Memorials"
    if any(k in h for k in ("hmdb", "nps.gov", "mass.gov", "historicalcommission", "medfordhistorical")): return "Markers, Plaques and Places"
    if any(k in h for k in ("bostonraremaps", "leventhal", "maps", "commons.wikimedia")): return "Maps, Surveys and Artifacts"
    if any(k in h for k in ("archive.org", "perseus", "books.google", "hathitrust", "gutenberg", "jstor")): return "Digitized Books and Journals"
    if any(k in h for k in ("masshist", "founders.archives", "loc.gov", "dar.org", "newspapers", "archives", "nara", "americanancestors", "harvard.edu")): return "Archives, Letters and Records"
    if any(k in h for k in ("wikipedia", "wikitree", "geni", "familysearch", "ancestry", "blogspot", "wordpress", "tuftsgenealogy")): return "Biographies and Family Trees"
    return "Other Resources"

GENERIC = re.compile(r"^(page scans?|text|text \(perseus\)|perseus|book scan.*|page \(internet archive\)|internet archive.*|online text|article|pdf|mhs|scan|dealer description|link|here|full text|record|transcription|catalog.*|\d[\d\-]*)$", re.I)
def clean(t, n=230):
    t = re.sub(r"\s+", " ", t).strip(" &middot;·,;:(")
    for _ in range(3):
        t = re.sub(r"(\s*(See|see|See the|see the|at|in|Page scans?|page scans?|Text \(Perseus\)|Book scan \(Internet Archive\)|Page \(Internet Archive\))\s*)+$", "", t).strip(" &middot;·,;:(")
    if len(t) > n: t = "&hellip;" + t[-n:].split(" ", 1)[-1]
    return t

def collect(soup, me):
    items, seen = [], set()
    main = soup.find("main")
    for a in main.find_all("a", href=True):
        if a.find_parent("section", id="links-resources"): continue
        u = a["href"]
        if u.startswith("#") or u.startswith("mailto:"): continue
        rel = re.sub(r"^(\.\./)+", "", u)
        if 'tuftsgenealogy.blogspot' in u: continue
        if rel.startswith("profiles/") or rel in ("people.html", "generations/revolution.html#profiles", "index.html", "about.html"): continue
        key = re.sub(r'^https?://(www\.)?', '', rel).rstrip('/')
        if key in seen: continue
        seen.add(key)
        par = a.find_parent(["li", "p", "td", "figcaption", "div"]) or a.parent
        txt = ""
        for el in par.descendants:
            if el is a: break
            if isinstance(el, str): txt += el
        lab = a.get_text(" ", strip=True)
        desc = clean(_h.escape(txt, quote=False))
        if par.name == "td":
            tr = a.find_parent("tr"); th = tr.find("td") if tr else None
            if th and th is not par: desc = _h.escape(th.get_text(" ", strip=True), quote=False)
        if not desc: desc = _h.escape(par.get_text(" ", strip=True)[:200], quote=False)
        items.append((group(rel), u, _h.escape(lab, quote=False), desc))
    return items

def section(items, pre):
    by = {g: [] for g in GROUPS}
    for g, u, lab, d in items: by[g].append((u, lab, d))
    out = ['<section id="links-resources" class="links-resources"><h2>Links and Resources</h2><p>Every source, record, map, survey, marker and artifact tied to this person, gathered in one place. Page numbers are given where a book is cited.</p>']
    for g in GROUPS:
        if not by[g]: continue
        out.append(f'<h3>{g}</h3>' + (f'<p class="note">{GNOTE[g]}</p>' if g in GNOTE else "") + '<ul class="link-list">')
        for u, lab, d in by[g]:
            if u in BROKEN: d = (d + " " if d else "") + '<span class="tag">link not responding (checked 2026-11-04)</span>'
            if GENERIC.match(_h.unescape(lab).strip()) and d:
                out.append(f'<li><span class="link-desc">{d}</span> &middot; <a href="{u}">{lab}</a></li>')
            else:
                out.append(f'<li><a href="{u}">{lab}</a>' + (f' &mdash; <span class="link-desc">{d}</span>' if d and d != lab else "") + '</li>')
        out.append("</ul>")
    out.append("</section>")
    return "".join(out)

def run():
    p = open("places.html").read()
    p = p.replace("<h3>Road from Concord to Cambridge, surveyed by Peter Tufts Jr. (1797)</h3>", '<h3 id="survey-1797">Road from Concord to Cambridge, surveyed by Peter Tufts Jr. (1797)</h3>')
    p = p.replace("<h3>Siege of Boston plan (1776)</h3>", '<h3 id="siege-plan-1776">Siege of Boston plan (1776)</h3>')
    open("places.html", "w").write(p)
    for f in sorted(glob.glob("profiles/*.html")):
        if f.endswith("_template.html"): continue
        s = f[9:-5]; t = open(f).read()
        t = re.sub(r'<svg class="divider"(?:(?!</svg>)[^\n])*</svg><section id="research-links">.*?</section>', "", t, flags=re.S)
        t = re.sub(r'<section id="research-links">.*?</section>', "", t, flags=re.S)
        soup = BeautifulSoup(t, "html.parser")
        cur = ([("Biographies and Family Trees", BLOG_KEEP[s][0], "Family blog post", BLOG_KEEP[s][1])] if s in BLOG_KEEP else []) + [(g, ("" if u.startswith("http") else "../") + u, l, d) for g, u, l, d in CUR.get(s, [])]
        curk = {re.sub(r"^https?://(www\.)?", "", re.sub(r"^(\.\./)+", "", c[1])).rstrip("/") for c in cur}
        items = cur + [i for i in collect(soup, s) if re.sub(r"^https?://(www\.)?", "", re.sub(r"^(\.\./)+", "", i[1])).rstrip("/") not in curk]
        sec = section(items, "../")
        div = re.search(r'<svg class="divider".*?</svg>', t, flags=re.S).group(0)
        if s in BLOG_KEEP: sec = sec.replace("</section>", '<div class="flag"><h3>&#9873; Unverified</h3><p>' + BLOG_KEEP[s][2] + '</p></div></section>', 1)
        t = re.sub(r'<a href="https?://tuftsgenealogy\.blogspot\.com[^"]*">(.*?)</a>', r"\1", t) if s not in BLOG_KEEP else t
        t = t.replace("</main>", div + "\n" + sec + "\n</main>", 1)
        open(f, "w").write(t)
run()
