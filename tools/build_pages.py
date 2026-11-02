"""Generates the site's HTML pages with one shared header, nav, and footer.
Run from the repo root: python3 tools/build_pages.py"""
import re
T = open("profiles/_template.html").read() if False else None
FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap">'''
CREST = '<svg class="crest" viewBox="0 0 60 70" aria-hidden="true"><path d="M5 5h50v28c0 18-12 28-25 33C17 61 5 51 5 33z" fill="#6d1a24" stroke="#c9a24a" stroke-width="3"/><path d="M30 5v61M5 30h50" stroke="#c9a24a" stroke-width="2"/></svg>'
DIV = '<svg class="divider" viewBox="0 0 360 40" role="img" aria-label="Heraldic divider: shield with crossed swords"><line x1="0" y1="20" x2="140" y2="20" stroke="#c9a24a" stroke-width="2"/><line x1="220" y1="20" x2="360" y2="20" stroke="#c9a24a" stroke-width="2"/><g stroke="#2e3034" stroke-width="3" stroke-linecap="round"><line x1="150" y1="34" x2="210" y2="4"/><line x1="210" y1="34" x2="150" y2="4"/></g><path d="M168 6h24v14c0 9-6 14-12 17c-6-3-12-8-12-17z" fill="#9b1c2c" stroke="#c9a24a" stroke-width="2"/></svg>'
SOON = '<span class="tag">Coming soon</span>'
# (label, path, coming_soon)
GENS = [("Colonial 1638&ndash;1765", "generations/colonial.html", True),
        ("The Revolution 1765&ndash;1783", "generations/revolution.html", False),
        ("19th Century", "generations/19th-century.html", True),
        ("Modern", "generations/modern.html", True)]
TOP = [("Home", "index.html", False), ("GEN", None, False), ("People", "people.html", True),
       ("Places", "places.html", False), ("Collections", "collections.html", True), ("Sources", "sources.html", False)]

def link(label, path, soon, pre, cur):
    cls = ' class="soon"' if soon else ''
    ac = ' aria-current="page"' if path == cur else ''
    return f'<a href="{pre}{path}"{cls}{ac}>{label}{SOON if soon else ""}</a>'

def nav(pre, cur):
    out = ['<nav aria-label="Main"><ul>']
    for label, path, soon in TOP:
        if label == "GEN":
            sub = "".join(f"<li>{link(l, p, s, pre, cur)}</li>" for l, p, s in GENS)
            out.append(f'<li class="dropdown"><a href="{pre}generations/revolution.html" aria-haspopup="true">Generations &#9662;</a><ul>{sub}</ul></li>')
        else:
            out.append(f"<li>{link(label, path, soon, pre, cur)}</li>")
    out.append("</ul></nav>")
    return "\n".join(out)

def page(path, title, kicker, h1, sub, body, desc="The Tufts family across generations, from colonial New England onward."):
    pre = "../" * path.count("/")
    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
{FONTS}
<link rel="stylesheet" href="{pre}css/style.css">
</head>
<body>
<header class="chainmail">
  {CREST}
  <div class="kicker">{kicker}</div>
  <h1>{h1}</h1>
  <div>{sub}</div>
</header>
{nav(pre, path)}
<main>
{body.replace("{P}", pre).replace("{DIV}", DIV).replace("{SOON}", SOON)}
</main>
<footer class="chainmail">
  &copy; <span id="year">2026</span> Tufts Family Heritage
</footer>
<script src="{pre}config.js"></script>
<script src="{pre}js/main.js"></script>
</body>
</html>
'''
    open(path, "w").write(html)

def soon_section(id_, h, note):
    return f'<section id="{id_}" class="soon"><h2>{h}{{SOON}}</h2><p>{note}</p></section>'

page("index.html", "Tufts Family Heritage", "From Colonial New England Onward", "Tufts Family Heritage", "The Tufts Family Across the Generations", '''
<section id="about">
  <h2>The Tufts Family Across the Generations</h2>
  <p>This site follows the Tufts family through the generations, from colonial New England onward. It covers the people, the family lines that connect them to descendants today, the places they lived and worked, and the letters and artifacts they left behind.</p>
</section>
<nav class="timeline" aria-label="Timeline">
  <a href="generations/colonial.html" class="soon"><strong>Colonial</strong>1638&ndash;1765{SOON}</a>
  <a href="generations/revolution.html"><strong>The Revolution</strong>1765&ndash;1783</a>
  <a href="generations/19th-century.html" class="soon"><strong>19th Century</strong>{SOON}</a>
  <a href="generations/modern.html" class="soon"><strong>Modern</strong>{SOON}</a>
</nav>
{DIV}
<section id="featured">
  <h2>Featured Stories</h2>
  <div class="cards">
    <a class="card" href="places.html#winter-hill"><h3>Winter Hill, April 19, 1775</h3><p>"Here he was soundly sleeping when Paul Revere came thundering up to the door." Jones, <em>Under Colonial Roofs</em>, p. 129.</p></a>
    <a class="card" href="generations/revolution.html#medford-roster"><h3>The Medford Minute Men Roster</h3><p>The 1925 City of Medford monument lists "TUFTS PETER JR." among the First Company of Minute Men.</p></a>
    <div class="card soon"><h3>Soldier Profiles{SOON}</h3><p>Planned: one profile per Tufts soldier, each checked against its sources.</p></div>
  </div>
</section>
{DIV}
<section>
  <h2>Our Standard</h2>
  <p>Every account here is drawn from primary and documented sources. Each book citation shows a page scan or an exact quote with its printed page number. Where a detail cannot yet be verified, we say so. See <a href="sources.html">Sources</a>.</p>
</section>''')

page("generations/colonial.html", "Colonial 1638–1765 | Tufts Family Heritage", "Generations", "Colonial Era", "1638&ndash;1765",
     soon_section("colonial", "Colonial Era", "Planned: the first Tufts generations in New England, drawn from town records and genealogies.") +
     '\n<p>Related: <a href="{P}places.html#medford-charlestown">Medford &amp; Charlestown</a></p>')
page("generations/revolution.html", "The Revolution 1765–1783 | Tufts Family Heritage", "Generations", "The Revolution", "1765&ndash;1783", '''
<div class="banner">1776 &ndash; 2026 &middot; The 250th Anniversary of American Independence</div>
<section>
  <h2>The Revolution</h2>
  <p>This chapter documents members of the Tufts family who served in the Revolution, drawing on records such as <em>Massachusetts Soldiers and Sailors of the Revolutionary War</em>.</p>
</section>
<section id="medford-roster">
  <h2>The Medford Minute Men Roster</h2>
  <blockquote>"ROSTER OF THE FIRST COMPANY OF MINUTE MEN WHO ASSEMBLED IN MEDFORD AT THE CALL OF PAUL REVERE AND ENGAGED IN THE BATTLE OF APRIL 19, 1775" &hellip; "TUFTS PETER JR."</blockquote>
  <p>Monument erected by the City of Medford, 1925. <a href="{P}sources/images/medford-1925-monument.jpg">View photograph</a></p>
</section>
{DIV}
<section id="profiles" class="soon">
  <h2>Revolutionary Profiles{SOON}</h2>
  <p>Planned: one profile per Tufts soldier, listed in <a href="{P}people.html">People</a> as each is checked against its sources.</p>
</section>
<p>Related: <a href="{P}places.html#winter-hill">Winter Hill</a> &middot; <a href="{P}places.html#medford-charlestown">Medford &amp; Charlestown</a></p>''')
page("generations/19th-century.html", "19th Century | Tufts Family Heritage", "Generations", "19th Century", "Coming soon",
     soon_section("nineteenth", "19th Century", "Planned: Tufts family lines through the 1800s.") +
     '\n<p>Related: <a href="{P}places.html#later-homes">Later Homes</a></p>')
page("generations/modern.html", "Modern | Tufts Family Heritage", "Generations", "Modern", "Coming soon",
     soon_section("modern", "Modern", "Planned: 20th-century and present-day generations.") +
     '\n<p>Related: <a href="{P}places.html#later-homes">Later Homes</a></p>')

page("people.html", "People | Tufts Family Heritage", "A&ndash;Z Index", "People", "Searchable index of family members", '''
<section>
  <h2>People A&ndash;Z</h2>
  <div class="filters">
    <label>Search <input id="q" type="search" placeholder="Name"></label>
    <label>Era <select id="era"><option value="">All eras</option></select></label>
    <label>Line <select id="line"><option value="">All lines</option></select></label>
  </div>
  <div id="people-list"><p class="note">Loading&hellip;</p></div>
</section>''')

page("places.html", "Places | Tufts Family Heritage", "Places", "Places", "Where the family lived and worked", '''
<section id="winter-hill">
  <h2>Winter Hill</h2>
  <blockquote>"At the outbreak of the Revolution, Peter Tufts lived at the top of Winter Hill in a little old house, which stood until a few years ago. Here he was soundly sleeping when Paul Revere came thundering up to the door, calling on the people to rouse and arm themselves, for the Regulars were coming."</blockquote>
  <p>Alvin Lincoln Jones, <em>Under Colonial Roofs</em> (1894), p. 129. <a href="sources/images/jones-under-colonial-roofs-p129.jpg">Page scan</a></p>
</section>
{DIV}
''' + soon_section("medford-charlestown", "Medford &amp; Charlestown", "Planned: family homes and land in Medford and Charlestown, from town records and Wyman's <em>Genealogies and Estates of Charlestown</em>.") + "\n" +
     soon_section("later-homes", "Later Homes", "Planned: where later generations settled."))

page("collections.html", "Collections | Tufts Family Heritage", "Collections", "Collections", "Letters, artifacts, and photographs",
     soon_section("letters", "Letters", "Planned: transcribed family letters with images of the originals.") + "\n" +
     soon_section("artifacts", "Artifacts", "Planned: family objects with provenance notes.") + "\n" +
     soon_section("photographs", "Photographs", "Planned: family and place photographs with sources."))

page("sources.html", "Sources | Tufts Family Heritage", "Sources", "Sources", "Bibliography, page scans, and research notes", '''
<section id="bibliography">
  <h2>Bibliography</h2>
  <ul>
    <li><em>Massachusetts Soldiers and Sailors of the Revolutionary War</em>, vol. XVI (1907), pp. 137&ndash;138.</li>
    <li>Thomas Bellows Wyman, <em>The Genealogies and Estates of Charlestown</em>, vol. II (1879), pp. 964&ndash;965.</li>
    <li>Alvin Lincoln Jones, <em>Under Colonial Roofs</em> (1894), pp. 128&ndash;129.</li>
    <li>Helen Tilden Wild, <em>Medford in the Revolution</em> (1903), p. 52.</li>
    <li>Ellen Chase, <em>The Beginnings of the American Revolution</em>, vol. III (1910), p. 99.</li>
    <li>City of Medford, Minute Men monument (1925).</li>
    <li><em>Tufts Kinsmen</em>, Vols. I and II. <strong>Missing images</strong>, still needed.</li>
    <li>DAR records. <strong>Missing images</strong>, still needed.</li>
  </ul>
</section>
{DIV}
<section id="scans">
  <h2>Page Scans</h2>
  <div id="scan-list" class="cards"></div>
</section>
{DIV}
<section id="notes">
  <h2>Research Notes</h2>
  <ul>
    <li><strong>Unverified:</strong> the death year of Peter Tufts Jr. (b. 1753). Wild, p. 52, prints "died 1836". Secondhand web sources for DAR ancestor A116812 give 1832.</li>
    <li><strong>Unverified:</strong> the <em>Tufts Kinsmen</em> p. 50 claim, known only secondhand.</li>
  </ul>
  <p>Full quote table: <a href="sources/README.md">sources/README.md</a></p>
</section>''')
