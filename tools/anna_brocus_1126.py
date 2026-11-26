# Anna Tufts (b. 1676), daughter of Capt. Peter Tufts and Elizabeth Lynde;
# married John Brocus at Medford, 24 June 1700.
# Sources: Medford VRs (1907), pp. 146, 192, 307; Wyman, p. 958;
# NEHGR 51 (July 1897), p. 300; MHR XXXIV (Dec. 1931), p. 78.
_AT = "anna-tufts-brocus"
_PT = "peter-tufts-1648"
_S78 = ('Wilson Fiske and Ruth Dame Coolidge, &ldquo;The Old Time Medford Town Meeting,&rdquo; '
  '<em>Medford Historical Register</em> XXXIV, no. 4 (Dec. 1931), p. 78, reprinting the early Medford town records. '
  '<a href="https://archive.org/details/medfordhistorica07medf/page/n289/mode/1up">View the page scan</a>')
_NE = ('Larkin T. Tufts and Edward C. Booth, &ldquo;Tufts Genealogy&mdash;Earlier Generations,&rdquo; '
  '<em>NEHGR</em> 51 (July 1897), p. 300. '
  '<a href="https://books.google.com/books?id=hcgMAAAAYAAJ&amp;pg=PA300">Google Books</a>')
_SEC = ('<section id="marriage-1700"><h2>Marriage to John Brocus, 24 June 1700</h2>'
  + '<p>The early Medford town records, as reprinted in the <em>Medford Historical Register</em> in 1931, give the marriage in its original spelling:</p>'
  + FIG("mhr-xxxiv-brocus-tufts-marriage.jpg", "hfig-flow mi-inline")
  + Q("the 24th day of June 1700. John Brocus &amp; Anna Tufts was maried.", _S78)
  + '<p>The 1907 printed vital records of Medford enter the same marriage under both names, still as Brocus, at pp. 192 and 307 (' + MV(192) + '; ' + MV(307) + '). Wyman, writing in 1879, gives the husband as John Brookhouse (' + WY(958) + '); the 1897 Tufts genealogy gives John Brocas (Brookhouse) (' + _NE + ').</p>'
  + '<p>A 1931 play, &ldquo;The Old Time Medford Town Meeting,&rdquo; brings &ldquo;Mistress Peter Tufts and her daughter, Anna&rdquo; to a neighbor&rsquo;s fireside, Anna with John Brocus, &ldquo;with whom her banns were cried last Sunday.&rdquo; The authors treat Mercy Cotton, ' + PL(_PT, "Capt. Peter Tufts") + '&rsquo;s second wife, as Anna&rsquo;s stepmother. The dialogue is a dramatization; the authors&rsquo; notes and the reprinted town record are the historical sources. The scene is quoted, with the same clipping, on ' + PL(_PT, "Capt. Peter Tufts&rsquo;s profile") + '.</p>'
  + '</section>')
_nf_new(_AT, "Anna Tufts (b. 1676)", "25 February 1676 &ndash; [death date not found]", "Medford, Mass.",
  "1676", "", "Colonial",
  "Daughter of Capt. Peter Tufts (c. 1648&ndash;1721) by Elizabeth Lynde; married John Brocus, 24 June 1700",
  '<p>Anna Tufts was born in Medford on 25 February 1676, a daughter of ' + PL(_PT, "Capt. Peter Tufts") + ' by his first wife, Elizabeth Lynde. The town record of her birth, printed as the earliest now extant in the Medford vital records, reads &ldquo;Anna, d. Goodman, Feb. 25, 1676&rdquo; (' + MV(146) + '). Wyman and the 1897 Tufts genealogy identify this Anna as Capt. Peter&rsquo;s daughter (' + WY(958) + '; ' + _NE + ').</p>'
  + '<p>On 24 June 1700 she married John Brocus at Medford. The 1897 genealogy names two children, Richard, born 20 November 1702, and Ann, born 23 March 1703/4 (' + _NE + ').</p>'
  + _SEC,
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL(_PT, "Capt. Peter Tufts (c. 1648&ndash;1721)") + '. Mother: Elizabeth Lynde (d. 1684), daughter of Ensign Thomas and Elizabeth Lynde of Malden. Stepmother: Mercy Cotton. Grandfather: ' + PL("peter-tufts-1617", "Peter Tufts the immigrant") + '. Half-brother and half-sister (children of Mercy Cotton): ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + '; ' + PL("sarah-tufts-hinckley", "Sarah Tufts Hinckley (1702&ndash;1784)") + '. Children: Richard (b. 20 November 1702) and Ann (b. 23 March 1703/4) (' + WY(958) + '; ' + _NE + ').</p>',
  "<strong>Death:</strong> her date of death has not been found in the Medford vital records or in the compiled accounts cited here. Note: Pending further work.",
  "<ul><li><strong>John Brocus</strong> (also spelled Brocas, and Brookhouse by Wyman). Married 24 June 1700, at Medford (" + _S78 + "; " + MV(192) + "; " + MV(307) + "; " + WY(958) + "; " + _NE + ").</li></ul>",
  [(_PT, "father Capt. Peter Tufts (c. 1648&ndash;1721)", "daughter Anna Tufts (b. 1676)"),
   ("peter-tufts-1617", "grandfather Peter Tufts the immigrant", "granddaughter Anna Tufts (b. 1676)"),
   ("simon-tufts-1700", "half-brother Dr. Simon Tufts (1700&ndash;1747)", "half-sister Anna Tufts (b. 1676)"),
   ("sarah-tufts-hinckley", "half-sister Sarah Tufts Hinckley (1702&ndash;1784)", "half-sister Anna Tufts (b. 1676)")])
# Link Anna from the 1931 town-meeting section already on Capt. Peter's profile.
for _p in PROFILES:
    if _p["slug"] == _PT and "anna-tufts-brocus.html" not in _p.get("bio", ""):
        _p["bio"] = (_p["bio"]
          .replace("her daughter, Anna", "her daughter, " + PL(_AT, "Anna"))
          .replace("the town record of Anna&rsquo;s marriage", "the town record of " + PL(_AT, "Anna Tufts") + "&rsquo;s marriage"))
        break
# Peter's Family Connection already names "Anna (Mrs. John Brocas)"; turn that into a profile link.
for _p in PROFILES:
    if _p["slug"] == _PT and "Anna (Mrs. John Brocas)" in _p.get("family", "") and "anna-tufts-brocus.html" not in _p.get("family", ""):
        _p["family"] = _p["family"].replace("Anna (Mrs. John Brocas)", PL(_AT, "Anna") + " (Mrs. John Brocas)")
        break

_IDSEC_A = IDSEC
def IDSEC(p):
    h = _IDSEC_A(p)
    if p["slug"] == _AT:
        h = h.replace("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
            "<td>Town / vital records</td><td><em>Vital Records of Medford, Massachusetts, to the Year 1850</em> (1907), p. 146 (birth: &ldquo;Anna, d. Goodman, Feb. 25, 1676&rdquo;); pp. 192, 307 (marriage to John Brocus, June 24, 1700).</td>")
        h = h.replace("<td><em>Mass. Soldiers and Sailors</em></td><td>Not yet checked for this page</td>",
            "<td><em>Mass. Soldiers and Sailors</em></td><td>No military entry expected</td>")
    return h

print("anna_brocus_1126 done")
