# Custom "page not found" page for GitHub Pages (served at any URL depth,
# so asset/nav paths are made root-relative, never a hardcoded domain).
import re as _re_nf
page("404.html", "Page Not Found", "Tufts Lineage &amp; Legacy", "Page Not Found",
     "The page you were looking for could not be found.",
     '<section id="not-found"><p>The address may be mistyped, or the page may have moved as the site has grown. '
     'Please try one of these:</p><ul>'
     '<li><a href="{P}index.html">Home page</a></li>'
     '<li><a href="{P}subjects.html">Browse by subject</a></li>'
     '<li><a href="{P}people.html">All people</a></li>'
     '<li><a href="{P}places.html">Places</a></li>'
     '<li><a href="{P}collections.html">Collections</a></li></ul></section>')
_nf = open("404.html").read()
_nf = _re_nf.sub(r'(href|src)="(?!https?:|/|#|mailto:)([^"]+)"', r'\1="/\2"', _nf)
open("404.html", "w").write(_nf)
