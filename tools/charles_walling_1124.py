# Daily research run 2026-11-24: Charles Tufts's land on Walling's 1855 map of Medford, and his Walnut Hill farm.
# Sources: "Medford Railroad Stations," MHR XXXIX (March 1936) p. 4 (IA medfordhistorica00me n157);
# "Walnut Tree Hill," MHR XXXIX (June 1936) p. 32 (IA medfordhistorica00me n195).
_CT = "charles-tufts-1781"
_R4 = "https://archive.org/details/medfordhistorica00me/page/n157/mode/1up"
_W32 = "https://archive.org/details/medfordhistorica00me/page/n195/mode/1up"
_RSRC = '&ldquo;Medford Railroad Stations,&rdquo; <em>Medford Historical Register</em> XXXIX (March 1936), p. 4. <a href="' + _R4 + '">View the page scan</a>'
_WSRC = '&ldquo;Walnut Tree Hill,&rdquo; <em>Medford Historical Register</em> XXXIX (June 1936), p. 32. <a href="' + _W32 + '">View the page scan</a>'
_MHRS5 = "Medford Historical Society, <em>Medford Historical Register</em>, via Internet Archive"
IMAGES["mhr-xxxix-walling-1855-charles-tufts.jpg"] = ("Clipping: Tufts land on Walling&rsquo;s 1855 map",
  "Detail of p. 4, <em>Medford Historical Register</em> XXXIX (March 1936), &ldquo;Medford Railroad Stations&rdquo;: owners along the Boston &amp; Lowell Railroad as shown on H. F. Walling&rsquo;s 1855 map of Medford.",
  _MHRS5, "Shown for non-commercial historical use", _R4, "Internet Archive (full page)")
IMAGES["mhr-xxxix-walnut-hill-charles-tufts.jpg"] = ("Clipping: Walnut Hill, part of the farm of Charles Tufts",
  "Detail of p. 32, <em>Medford Historical Register</em> XXXIX (June 1936), &ldquo;Walnut Tree Hill.&rdquo;",
  _MHRS5, "Shown for non-commercial historical use", _W32, "Internet Archive (full page)")
_QR = ("The names of the owners of the land adjoining the railroad from Broadway to the Mystic River are shown. On the westerly side, starting at Broadway, we find all the land between the railroad, the Somerville line and South Street, owned by Charles Tufts with the exception of the Medford portion of the tract presented by Mr. Tufts to Tufts College, and a large plot at the South Street end owned by Joseph Manning. "
  "The land bounded by the railroad, South Street, the Somerville line and the river is about equally divided among Samuel Tufts, Joseph Manning, Timothy Cotting, J. Q. Adams Estate and J. B. Felt. &hellip; Returning to our starting point at Broadway we find the land adjoining the easterly side of the railroad to Harvard Street owned by Charles Tufts and George E. Adams&hellip;")
_QW = ("In the fourth generation from Peter Tufts the first, was Daniel Tufts, a farmer and brickmaker, and a large land-owner in the Somerville of today. Charles Tufts, a son of Daniel, was born July 17, 1787 [sic], and likewise became a farmer and brickmaker. His house was on Washington Street, but he owned also extensive farm lands. "
  "In 1842 he was one of two persons in the new Somerville who paid a tax amounting to over one hundred dollars. Among the lands taxed to him was that part of Walnut Hill lying in Somerville. His holdings extended also into Medford. Walnut Hill at that time was a hill-top pasture, &mdash;a part of the farm of Charles Tufts.")
_SEC = ('<section id="walling-1855-land"><h2>His Land on Walling&rsquo;s 1855 Map and the Walnut Hill Farm</h2>'
  + '<p>A 1936 history of Walnut Hill describes Charles Tufts as a farmer and brickmaker like his father, and one of Somerville&rsquo;s two largest taxpayers in 1842:</p>'
  + FIG("mhr-xxxix-walnut-hill-charles-tufts.jpg", "hfig-flow mi-inline")
  + Q(_QW, _WSRC)
  + '<p>The same year the <em>Register</em> printed a reading of H. F. Walling&rsquo;s map of the Town of Medford (1855), naming the owners of the land beside the Boston &amp; Lowell Railroad. Charles Tufts held nearly the whole western side from Broadway to South Street, apart from the land he had already given to Tufts College:</p>'
  + FIG("mhr-xxxix-walling-1855-charles-tufts.jpg", "hfig-flow mi-inline")
  + Q(_QR, _RSRC)
  + '<p><strong>Tufts association:</strong> farm and pasture land owned by Charles Tufts in Somerville and Medford, including Walnut Hill, the site he gave for Tufts College (' + _WSRC + '; ' + _RSRC + ').</p>'
  + UNV("<strong>Birth year:</strong> the 1936 article prints his birth as July 17, 1787; other sources used on this page give 1781, which is followed here. <strong>Samuel Tufts</strong> on the 1855 map, owner of land between South Street and the Mystic River, is not yet identified with a profile on this site. Walling&rsquo;s 1855 map itself has not yet been viewed for this page. Note: Pending further work.")
  + '</section>')
_up_add(_CT, _SEC, 'id="walling-1855-land"')
if "MAPS_HTML" in globals() and "walling-1855-land" not in MAPS_HTML:
    MAPS_HTML = MAPS_HTML.replace("</ul>", '<li>H. F. Walling, map of the Town of Medford (1855): shows the land of ' + PL(_CT, "Charles Tufts (1781&ndash;1876)") + ' on both sides of the Boston &amp; Lowell Railroad from Broadway to South Street, and land of a Samuel Tufts between South Street and the Mystic (' + _RSRC + '). <a href="{P}profiles/' + _CT + '.html#walling-1855-land">Details on his profile</a>.</li></ul>', 1)
print("charles_walling_1124 done")
