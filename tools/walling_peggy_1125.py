# Daily research run 2026-11-25: H. F. Walling's 1855 map of Medford viewed (Tufts College, Charles Tufts, S. Tufts lands),
# and the "Peggy Tufts on it" carafe added to Collections.
# Map: Leventhal Map & Education Center, BPL, via Digital Commonwealth, ark:/50959/x059c900f (no known restrictions).
_WARK = "https://ark.digitalcommonwealth.org/ark:/50959/x059c900f"
_WCIT = 'H. F. Walling, <em>Map of the Town of Medford, Middlesex County, Mass., Surveyed by Order of the Town</em> (Boston, 1855), engraved by A. Kollner. Norman B. Leventhal Map &amp; Education Center, Boston Public Library, call no. G3764.M53 1855 .W3. <a href="' + _WARK + '">View the full map</a>'
IMAGES["walling-1855-medford-tufts.jpg"] = ("Walling&rsquo;s 1855 map of Medford: Tufts College and the Tufts lands",
  "Detail of the southern part of Medford on H. F. Walling&rsquo;s 1855 town map: Tufts College on Walnut Hill at the Somerville line, with the names C. Tufts, Chas. Tufts and Charles Tufts on the land around it and along the Boston &amp; Lowell Railroad, S. Tufts near South Street, and further Tufts lots toward Broadway and the Mystic.",
  "Norman B. Leventhal Map &amp; Education Center, Boston Public Library, via Digital Commonwealth", "No known copyright restrictions", _WARK, "Digital Commonwealth (full map)")
_WSEC = ('<section id="walling-1855-map"><h2>On the Map: Walling&rsquo;s Medford, 1855</h2>'
  + FIG("walling-1855-medford-tufts.jpg", "hfig-flow mi-inline")
  + '<p>The town map itself bears out the 1936 reading. In the southern corner of Medford, where the town met Somerville, Walling drew the new Tufts College on the crown of Walnut Hill. The surrounding slopes are lettered with Charles Tufts&rsquo;s name in three forms, &ldquo;C. Tufts,&rdquo; &ldquo;Chas. Tufts&rdquo; and &ldquo;Charles Tufts,&rdquo; running down to College Station on the Boston &amp; Lowell Railroad and along the Somerville line. Across the tracks the land toward Harvard and Main Streets belongs largely to George E. Adams, while lots marked simply &ldquo;Tufts&rdquo; lie near Broadway and Craigie Road. North of the hill, beside the lands of Joseph Manning and Timothy Cotting near South Street, is a small lot marked &ldquo;S. Tufts&rdquo; (' + _WCIT + ').</p>'
  + '<p><strong>Tufts association:</strong> land of Charles Tufts around the Tufts College site, and other Tufts holdings, named on the 1855 town survey (' + _WCIT + ').</p>'
  + UNV("Which Tufts owned the lots marked only &ldquo;Tufts&rdquo; near Broadway and Craigie Road, and the identity of &ldquo;S. Tufts,&rdquo; are not stated on the map. Note: Pending further work.")
  + '</section>')
_up_add(_CT, _WSEC, 'id="walling-1855-map"')
_old = "Walling&rsquo;s 1855 map itself has not yet been viewed for this page. "
for _p in PROFILES:
    for _k, _v in list(_p.items()):
        if isinstance(_v, str) and _old in _v:
            _p[_k] = _v.replace(_old, "")
if "MAPS_HTML" in globals() and "walling-1855-map" not in MAPS_HTML:
    MAPS_HTML = MAPS_HTML.replace("</ul>", '<li>H. F. Walling, <em>Map of the Town of Medford</em> (1855), the town survey itself: Tufts College on Walnut Hill and the lands of ' + PL(_CT, "Charles Tufts (1781&ndash;1876)") + ' around it, with an &ldquo;S. Tufts&rdquo; lot near South Street (' + _WCIT + '). <a href="{P}profiles/' + _CT + '.html#walling-1855-map">Map detail on his profile</a>.</li></ul>', 1)

# Collections: the "Peggy Tufts on it" carafe (MHR XLIII, 1940, p. 27)
_PMS = "margaret-tufts-swan-1779"
_P27 = "https://archive.org/details/medfordhistorica12medf/page/n310/mode/1up"
_PCIT = '&ldquo;Captain Samuel Swan, 3rd, of Medford,&rdquo; <em>Medford Historical Register</em> XLIII (1940), p. 27. <a href="' + _P27 + '">View the page scan</a>'
NF_EXTRA.setdefault("collections.html", []).append(
  '{DIV}<section id="peggy-tufts-carafe"><h2>The &ldquo;Peggy Tufts on it&rdquo; Carafe</h2>'
  + FIG("mhr-xliii-peggy-tufts-china.jpg", "hfig-flow mi-inline")
  + '<p>When Capt. Samuel Swan of Medford was courting Margaret &ldquo;Peggy&rdquo; Tufts, he offered to bring her a wedding gift from the Orient. She asked for a set of bedroom china and, when he asked what should be put on it, answered, &ldquo;Oh, put Peggy Tufts on it!&rdquo; The china dealer took her literally. In 1940 the Captain&rsquo;s descendants wrote that &ldquo;one of our treasured possessions is a carafe, on the bottom of which are the words: &lsquo;Peggy Tufts on it&rsquo;&rdquo; (' + _PCIT + '). The couple married in 1809.</p>'
  + '<p><strong>Tufts association:</strong> China export ware made for Margaret (Tufts) Swan, daughter of Samuel Tufts 2nd of Medford. See ' + PL(_PMS, "Margaret &ldquo;Peggy&rdquo; (Tufts) Swan") + '.</p>'
  + UNV("The carafe&rsquo;s present location is not known, and no photograph of it has been found. Note: Pending further work.") + '</section>')
_up_add(_PMS, '<p>The carafe from her china is described on the <a href="{P}collections.html#peggy-tufts-carafe">Collections page</a>.</p>', 'collections.html#peggy-tufts-carafe')
print("walling_peggy_1125 done")
