"""Generates the site's HTML pages with one shared header, nav, and footer.
Run from the repo root: python3 tools/build_pages.py"""
import re
FONTS = '''<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cinzel:wght@500;700&family=EB+Garamond:ital,wght@0,400;0,600;1,400&display=swap">'''
CREST = '<svg class="crest" viewBox="0 0 60 70" aria-hidden="true"><path d="M5 5h50v28c0 18-12 28-25 33C17 61 5 51 5 33z" fill="#6d1a24" stroke="#c9a24a" stroke-width="3"/><path d="M30 5v61M5 30h50" stroke="#c9a24a" stroke-width="2"/></svg>'
DIV = '<svg class="divider" viewBox="0 0 360 40" role="img" aria-label="Heraldic divider: shield with crossed swords"><line x1="0" y1="20" x2="140" y2="20" stroke="#c9a24a" stroke-width="2"/><line x1="220" y1="20" x2="360" y2="20" stroke="#c9a24a" stroke-width="2"/><g stroke="#2e3034" stroke-width="3" stroke-linecap="round"><line x1="150" y1="34" x2="210" y2="4"/><line x1="210" y1="34" x2="150" y2="4"/></g><path d="M168 6h24v14c0 9-6 14-12 17c-6-3-12-8-12-17z" fill="#9b1c2c" stroke="#c9a24a" stroke-width="2"/></svg>'
SOON = '<span class="tag">Coming soon</span>'
# (label, path, coming_soon)
GENS = [("Colonial 1638&ndash;1765", "generations/colonial.html", False),
        ("The Revolution 1765&ndash;1783", "generations/revolution.html", False),
        ("19th Century", "generations/19th-century.html", False),
        ("Modern", "generations/modern.html", False)]
TOP = [("Home", "index.html", False), ("GEN", None, False), ("People", "people.html", False),
       ("Places", "places.html", False), ("Collections", "collections.html", False), ("Sources", "sources.html", False), ("About", "about.html", False)]

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
<meta property="og:site_name" content="Tufts Lineage &amp; Legacy">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
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
{(body + EXTRA(path)).replace("{P}", pre).replace("{DIV}", DIV).replace("{SOON}", SOON)}
</main>
<footer class="chainmail">
  &copy; <span id="year">2026</span> Tufts Lineage &amp; Legacy &middot; <a href="{pre}about.html">About</a>
</footer>
<script src="{pre}config.js"></script>
<script src="{pre}js/main.js"></script>
</body>
</html>
'''
    open(path, "w").write(html)

def soon_section(id_, h, note):
    return f'<section id="{id_}" class="soon"><h2>{h}{{SOON}}</h2><p>{note}</p></section>'

exec(open("tools/images.py").read())
exec(open("tools/content.py").read())
