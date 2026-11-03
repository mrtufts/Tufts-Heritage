# Harvard ties (owner request A, 2026-11-03).
PU = lambda doc, ch: f"https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A{doc}%3Achapter%3D{ch}&amp;force=y"
BRK9 = PU("2001.05.0104", 9)
BRP = lambda pg: f'Charles Brooks, <em>History of the Town of Medford</em> (1855), p. {pg}. <a href="{BRK9}">Text (Perseus)</a>'
SIB_IDX = "https://archive.org/details/sibley.index"
QQ = "https://archive.org/details/quinquennialcat00univgoog"
QQC = lambda yr: f'<em>Quinquennial Catalogue of the Officers and Graduates of Harvard University, 1636&ndash;1915</em> (1915), class of {yr}. <a href="{QQ}">Internet Archive</a>'
def SIB(vol, pp): return f'Clifford K. Shipton, <em>Sibley&rsquo;s Harvard Graduates</em>, vol. {vol}, pp. {pp} (sketch location from Andrew W. Pollock&rsquo;s <a href="{SIB_IDX}">Index of Graduates</a>; sketch text not seen)'
PROFILES += [dict(slug="simon-tufts-1700", name="Dr. Simon Tufts (1700&ndash;1747)", dates="1700&ndash;1747", town="Medford, Mass.", born="1700", died="1747", era="Colonial", line="Son of Capt. Peter Tufts",
  bio=Q("Dr. Simon Tufts, son of Peter, born in Medford, Jan. 31, 1700, died here, Jan. 31, 1747. He graduated at Harvard College in 1724.", BRP("302&ndash;303"))
   + '<p>Brooks says he was called &ldquo;the first physician of Medford,&rdquo; and that the town records call him doctor in May 1724. His obituary, which Brooks reprints, says he &ldquo;took his degrees at Harvard College in the years 1724 and 1727&rdquo; and was the youngest son of Captain Peter Tufts by his second wife, a daughter of the Rev. Seaborn Cotton. His sons <a href="{P}profiles/simon-tufts-11-1.html">Dr. Simon Tufts (1727&ndash;1786)</a> and <a href="{P}profiles/cotton-tufts.html">Dr. Cotton Tufts (1732&ndash;1815)</a> both became physicians. See <a href="{P}harvard.html">Harvard</a> and <a href="{P}places.html#homesteads">the Drs. Simon Tufts house</a>.</p>',
  service='<p>Justice of the peace from 1733 (obituary quoted by Brooks, p. 303). His service was medical and civil; he died before the Revolution.</p>',
  family='<p>Son of Capt. Peter Tufts and his second wife, Mercy Cotton (Brooks, p. 303). Father of the two doctors Simon and Cotton.</p>',
  unverified="Not to be confused with his son Dr. Simon Tufts (1727&ndash;1786). Brooks says his house was built in 1725, and the <em>Medford Historical Register</em> (vol. XVIII, p. 67) says it was demolished in 1867. Sibley sketch not yet read.")]
H = [("Thomas Tufts", "1701", "", SIB("V", "122&ndash;124"), "The Quinquennial Catalogue (1915) lists a Thomas Tufts, A.M., under 1700; the Sibley index gives A.B. 1701. Identity and family not yet established."),
 ("Jonathan Tufts", "attended, left 1707", "", SIB("V", "403"), "Recorded in Sibley as a non-graduate (ex-1707). Identity not established."),
 ("Rev. John Tufts", "1708", "", SIB("V", "457&ndash;461"), "Minister at Newbury, called by Brooks the &ldquo;townsman and relative&rdquo; of the elder Dr. Simon (Brooks, p. 303). No profile yet."),
 ("Dr. Simon Tufts (1700&ndash;1747)", "1724", "simon-tufts-1700", SIB("VII", "444&ndash;446"), "Medford&rsquo;s first physician; A.M. as well (obituary: &ldquo;degrees &hellip; 1724 and 1727&rdquo;)."),
 ("Thomas Tufts Jr.", "1732", "", SIB("IX", "228&ndash;229"), 'Born in Medford in 1712; the first master in Medford&rsquo;s first schoolhouse (<em>Medford Historical Register</em>, vol. II, pp. 11, 13. <a href="' + PU("2005.05.0003", 1) + '">Perseus</a>).'),
 ("Joshua Tufts", "1736", "", SIB("X", "82&ndash;84"), "Listed by Brooks among Medford&rsquo;s Harvard graduates (p. 301). Identity not established."),
 ("Dr. Simon Tufts (1727&ndash;1786)", "1744", "simon-tufts-11-1", SIB("XI", "478&ndash;481"), "Brooks: born Jan. 16, 1727, &ldquo;graduated at Harvard College in 1744&rdquo; (p. 305)."),
 ("Dr. Cotton Tufts (1732&ndash;1815)", "1749", "cotton-tufts", SIB("XII", "493&ndash;500"), "A.B. 1749, A.M.; honorary M.D. 1785 (Quinquennial Catalogue, class of 1749)."),
 ("Simon Tufts (son of Dr. Simon)", "1767", "", SIB("XVI", "540&ndash;542"), 'Probably the Simon Tufts, A.M., eldest son of Dr. Simon and Lucy (Dudley) Tufts, who died in 1802 at the Cape of Good Hope (Medford vital records). Whether he is the <a href="{P}profiles/simon-tufts-29-1.html">Loyalist Simon Tufts (1750&ndash;1801)</a> on this site is Unverified.'),
 ("Cotton Tufts Jr. (1757&ndash;1833)", "1777", "", QQC("1777"), "Son of Dr. Cotton Tufts; the Adams Papers editors give &ldquo;Harvard 1777&rdquo; (Adams Family Correspondence, vol. 1, Abigail Smith to Cotton Tufts, 2 April 1764, note 6)."),
 ("Abijah Tufts", "1790", "", QQC("1790"), "Identity not established."),
 ("Hall Tufts", "1794", "", 'Brooks, p. 301 (Medford graduates list)', "Listed by Brooks among Medford&rsquo;s Harvard graduates. Identity not established."),
 ("Joseph Tufts", "1807", "", QQC("1807"), "Identity not established."),
]
ROWS = "".join(f'<tr><td>{(f"<a href=\"{{P}}profiles/{s}.html\">{n}</a>") if s else n}</td><td>{y}</td><td>{note}</td><td class="cite">{c}</td></tr>' for n, y, s, c, note in H)
HARV = f'''<section id="about"><p>Harvard College in Cambridge educated three generations of Medford Tufts physicians and a string of ministers and schoolmasters. This page gathers every Tufts tie to Harvard found so far in the printed records: degrees, offices and honors. Class years come from Sibley&rsquo;s <em>Harvard Graduates</em> (through the class of 1771) and the <em>Quinquennial Catalogue</em> of 1915.</p>
{TA('Tufts graduates of Harvard College from 1701, among them Medford&rsquo;s first physician, <a href="{P}profiles/simon-tufts-1700.html">Dr. Simon Tufts</a> (class of 1724), his son <a href="{P}profiles/simon-tufts-11-1.html">Dr. Simon Tufts</a> (1744) and <a href="{P}profiles/cotton-tufts.html">Dr. Cotton Tufts</a> (1749), who received an honorary M.D. in 1785.', "Brooks, pp. 302&ndash;306; Quinquennial Catalogue (1915), classes of 1724, 1744, 1749")}</section>{{DIV}}
<section id="graduates"><h2>Tufts Graduates and Students</h2>
<table class="data"><thead><tr><th>Name</th><th>Class</th><th>Notes</th><th>Source</th></tr></thead><tbody>{ROWS}</tbody></table>
{UNV("Sibley sketch texts (vols. V&ndash;XVI) have not been read for this page; only their volume and page locations are cited, from the Pollock index. Each identity marked &ldquo;not established&rdquo; still needs a family placement. The Quinquennial Catalogue lists a Thomas Tufts under 1700, while the Sibley index gives 1701.")}
</section>{{DIV}}
<section id="physicians"><h2>Three Doctors, Two Simons</h2>
{Q("He was born Jan. 16, 1727, and graduated at Harvard College in 1744.", BRP(305))}
{Q("Dr. Cotton Tufts, born 1732, brother of the above, graduated at Harvard College 1749; studied medicine with his brother; settled in Weymouth", BRP(306))}
<p>The elder Simon trained his eldest son. The son, in turn, trained his younger brother Cotton and, later, John Brooks, the future governor (Brooks, pp. 305&ndash;307). The Countway Library&rsquo;s description of Cotton&rsquo;s papers gives his degrees as &ldquo;A.B., 1749, honorary M.D., 1785, Harvard College.&rdquo; <a href="https://researchworks.oclc.org/archivegrid/collection/data/122521209">ArchiveGrid record</a>.</p>
{UNV("Cotton Tufts&rsquo;s birth year. Brooks (p. 306) and the Adams Papers editors give 1732; <em>Historic Leaves</em>, vol. 3, p. 18, gives May 3, 1734.")}
</section>{{DIV}}
<section id="offices"><h2>Offices, Honors and Gifts</h2><ul>
<li><strong>Honorary M.D., 1785:</strong> Dr. Cotton Tufts (Quinquennial Catalogue, class of 1749).</li>
<li><strong>Harvard and the Medical Society:</strong> Brooks writes that among the members of the Massachusetts Medical Society &ldquo;Dr. Tufts&rsquo;s name stands the second, in the order of time, on the college catalogue&rdquo; (p. 306), meaning the younger Dr. Simon.</li>
<li><strong>Gifts:</strong> No gift or bequest to Harvard by a colonial Tufts has yet been found.</li>
<li><strong>Not Harvard:</strong> No Harvard degree has been found for <a href="{{P}}profiles/francis-tufts-20-1.html">Rev. Francis Tufts</a> (1744&ndash;1833), the Freewill Baptist minister, in the Sibley index or the 1915 catalogue. The only Francis Tufts there is an LL.B. of 1851. Tufts College in Medford (1852) is a separate institution.</li>
</ul>{UNV("Harvard University Archives records (faculty records, quarter-bill and steward&rsquo;s books) have not been searched. Offices held at Harvard by any Tufts are unconfirmed.")}</section>'''
page("harvard.html", "Harvard | Tufts Lineage &amp; Legacy", "Places &middot; Cambridge", "Harvard College", "Tufts graduates, offices and honors, 1701&ndash;1807", HARV)
_EXTRA6 = EXTRA
HV = {"simon-tufts-11-1": ("Class of 1744", SIB("XI", "478&ndash;481"), "Brooks, p. 305: born Jan. 16, 1727; &ldquo;graduated at Harvard College in 1744.&rdquo; He was not the elder Dr. Simon (1700&ndash;1747), class of 1724."),
      "cotton-tufts": ("Class of 1749; honorary M.D. 1785", SIB("XII", "493&ndash;500"), "Brooks, p. 306: &ldquo;graduated at Harvard College 1749.&rdquo; Quinquennial Catalogue (1915): A.M.; M.D. (Hon.) 1785."),
      "simon-tufts-1700": ("Class of 1724", SIB("VII", "444&ndash;446"), "Brooks, p. 303: &ldquo;He graduated at Harvard College in 1724.&rdquo;"),
      "simon-tufts-29-1": ("Possibly class of 1767", SIB("XVI", "540&ndash;542"), "A Simon Tufts graduated in 1767. Whether he is this man is Unverified.")}
def EXTRA(path):
    out = _EXTRA6(path)
    s = path[9:-5] if path.startswith("profiles/") else ""
    if s in HV:
        h, c, t = HV[s]; out += '{DIV}<section id="harvard"><h2>Harvard: ' + h + '</h2><p>' + t + ' <span class="cite">(' + c + ')</span> See <a href="{P}harvard.html">Harvard College</a>.</p></section>'
    if path == "places.html": out = '{DIV}<section id="harvard"><h2>Harvard College, Cambridge</h2><p>Thirteen Tufts graduates or students from 1701 to 1807, among them three family physicians. See <a href="{P}harvard.html">Harvard College</a>.</p></section>' + out
    return out
