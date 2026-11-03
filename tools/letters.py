# Letters of the Tufts doctors (owner request B, 2026-11-03). Adams Papers list from the MHS digital edition (correspondent facets).
import json as _jl
DL = _jl.load(open("data/tufts_doctors_letters.json"))
MHSV = "https://www.masshist.org/publications/adams-papers/index.php/view/"
FO = lambda i: "https://founders.archives.gov/documents/Adams/" + i[5:]
def LCITE(r): return f'<em>{r["cite"].split(",")[0]}</em>{r["cite"][len(r["cite"].split(",")[0]):]}. <a href="{MHSV}{r["id"]}">MHS digital edition</a> &middot; <a href="{FO(r["id"])}">Founders Online</a>'
def LROW(r, topic=None):
    w = r["who"].replace("Tufts, Cotton", "Dr. Cotton Tufts").replace("Adams, Abigail", "Abigail Adams").replace("Adams, John", "John Adams")
    return f'<tr><td>{r["date"]}</td><td>{w}</td><td>{topic or r["teaser"]}</td><td class="cite">{LCITE(r)}</td></tr>'
TH = '<table class="data"><thead><tr><th>Date</th><th>Correspondents</th><th>Topic</th><th>Citation</th></tr></thead><tbody>'
QL = {"ADMS-04-01-02-0017": "&ldquo;Ye must permit the little Villains call&rsquo;d the small Pox to have their Feast this Spring.&rdquo;",
      "ADMS-04-02-02-0019": "&ldquo;Yesterday People in Boston were openly inoculated for the Small Pox.&rdquo;",
      "ADMS-04-02-02-0037": "&ldquo;The Small Pox prevailing in our Armies and Country has much retarded the raising Recruits.&rdquo;",
      "ADMS-04-02-02-0050": "Thanks Adams for &ldquo;Dr. Rushs Letter on Inoculation.&rdquo;",
      "ADMS-04-08-02-0087": "&ldquo;my little Boy has got well through the small pox.&rdquo;",
      "ADMS-04-09-02-0014": "Thomas Adams carried to Braintree &ldquo;with the Symptoms of the Measles upon him.&rdquo;",
      "ADMS-04-14-02-0046": "&ldquo;some few Instances of bilious Fevers with us, at present scarce any Complaint of Disease.&rdquo;"}
COT = [r for r in DL if r["kind"] in ("by", "to")]
DIS = [r for r in COT if r["disease"]]
def _d(r):
    import datetime
    try: return datetime.datetime.strptime(r["date"], "%B %d, %Y")
    except Exception: return datetime.datetime(1900, 1, 1)
DIS.sort(key=_d); COT.sort(key=_d)
DOCTORS = f'''<section id="doctors-letters"><h2>Letters of the Tufts Doctors</h2>
<p>Three Tufts physicians are easy to confuse. In this section each letter is assigned to one of them by name and dates:</p>
<ul><li><a href="{{P}}profiles/simon-tufts-1700.html">Dr. Simon Tufts the elder (1700&ndash;1747)</a>, Medford&rsquo;s first physician;</li>
<li><a href="{{P}}profiles/simon-tufts-11-1.html">Dr. Simon Tufts the younger (1727&ndash;1786)</a>, his eldest son, of Medford;</li>
<li><a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts (1732&ndash;1815)</a>, the younger son, of Weymouth.</li></ul>
<h3>Dr. Cotton Tufts: letters on smallpox, fevers and other diseases</h3>
<p>The Adams Papers digital edition of the Massachusetts Historical Society lists 188 letters by or to Cotton Tufts: 90 written by him and 98 written to him. These {len(DIS)} touch on disease in the letter text. Topics were read from each letter; a quotation is given where one is short.</p>
{TH}{"".join(LROW(r, r["disease"].capitalize() + ((". " + QL[r["id"]]) if r["id"] in QL else "")) for r in DIS)}</tbody></table>
{UNV("None of the 188 Adams letters is on throat distemper (diphtheria). Cotton Tufts&rsquo;s own medical papers at the Countway Library include &ldquo;a treatise on distemper,&rdquo; and the Countway&rsquo;s exhibit says he &ldquo;introduced a popular treatment for diphtheria early in his career&rdquo; (see the manuscript collections below). Those papers have not been read item by item.")}
<details><summary>All 188 Adams Papers letters by or to Dr. Cotton Tufts</summary>{TH}{"".join(LROW(r) for r in COT)}</tbody></table><p class="cite">Topics in this list are the opening words shown by the MHS digital edition. Founders Online links follow the same document numbers.</p></details>
<h3>Dr. Simon Tufts the younger (1727&ndash;1786): letters with Col. Isaac Royall</h3>
<p>No letter by or to either Dr. Simon appears in the Adams Papers. The surviving references are to the younger Simon&rsquo;s letters with the Loyalist Isaac Royall, for whom he acted as agent:</p>
{TH}
<tr><td>May 1775</td><td>Isaac Royall (Halifax) to Dr. Simon Tufts</td><td>Asks him to become his agent; Brooks says the doctor &ldquo;declined, but afterwards accepted.&rdquo;</td><td class="cite">{BRP(173).replace(BRK9, PU("2001.05.0104", 5))}</td></tr>
<tr><td>March 12, 1776</td><td>Isaac Royall (Halifax) to Dr. Simon Tufts</td><td>Directions to sell enslaved people of the Royall household; Brooks quotes the letter.</td><td class="cite">Brooks, p. 173. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
<tr><td>August 1777</td><td>Isaac Royall (Kensington, England) to Dr. Simon Tufts</td><td>Mentioned only (&ldquo;Dr. Tufts had a letter from him&rdquo;).</td><td class="cite">Brooks, pp. 173&ndash;174. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
<tr><td>October 22 [1778?]</td><td>Dr. Simon Tufts to Isaac Royall</td><td>Reports that the Medford committee had taken the estate out of his hands; known from Royall&rsquo;s reply.</td><td class="cite"><em>Medford Historical Register</em>, vol. XI, p. 17 (&ldquo;A recently discovered Letter written by Colonel Isaac Royall in 1779&rdquo;). <a href="{PU("2005.05.0011", 3)}">Perseus</a></td></tr>
<tr><td>1779</td><td>Isaac Royall to [his friends in Medford]</td><td>&ldquo;Some time past I receiv&rsquo;d a Letter from my Attorney Dr Simon Tufts at Medford dated October 22&rdquo;; says he has written back to &ldquo;Doct. Tufts.&rdquo;</td><td class="cite"><em>Medford Historical Register</em>, vol. XI, p. 17. <a href="{PU("2005.05.0011", 3)}">Perseus</a></td></tr>
<tr><td>April 12, 1779</td><td>Isaac Royall (Kensington) to Dr. Simon Tufts</td><td>&ldquo;I doubt not you, and Mr. Hall, and the rest of my friends, will do all in your power to procure me liberty from the General Court to return home&rdquo;</td><td class="cite">Brooks, p. 175. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
</tbody></table>
{UNV("Whether Royall&rsquo;s letter of August 22, 1779 (Brooks, p. 175) was also addressed to Dr. Tufts. Brooks says only &ldquo;in another letter.&rdquo; The originals&rsquo; whereabouts are not stated.")}
<h3>Dr. Simon Tufts the elder (1700&ndash;1747)</h3>
<p>No letter by or to the elder Dr. Simon has yet been found in print. His obituary of February 5, 1747, printed &ldquo;in the public papers,&rdquo; is quoted by Brooks (pp. 303&ndash;304).</p>
<h3>Simon Tufts, the doctor&rsquo;s son (not a physician)</h3>
<p>The <em>Medford Historical Register</em> prints &ldquo;Extracts from letters written by Simon Tufts Son of Dr. Simon Tufts&rdquo; (vol. VI, p. 96, &ldquo;A Package of old letters&rdquo;. <a href="{PU("2005.05.0006", 6)}">Perseus</a>), and a letter he wrote from Cape Town on March 20, 1801, to his brother-in-law Benjamin Hall Jr. (vol. XVI, p. 30. <a href="{PU("2005.05.0016", 5)}">Perseus</a>). He is not either doctor.</p>
<h3>Manuscript collections (not yet read item by item)</h3><ul>
<li><strong>Cotton Tufts papers, 1751&ndash;1805</strong>, B MS c30, Countway Library of Medicine, Harvard: correspondence &ldquo;with his older brother, Simon Tufts (1726/7&ndash;1786), and other physicians, regarding medical matters, and the founding of a medical society,&rdquo; with manuscripts on vaccine, inoculation and the 1772&ndash;73 measles. <a href="https://researchworks.oclc.org/archivegrid/collection/data/122521209">ArchiveGrid</a> &middot; <a href="https://curiosity.lib.harvard.edu/contagion/feature/cotton-tufts-papers">Harvard <em>Contagion</em> exhibit</a></li>
<li><strong>Simon Tufts, correspondence, 1751&ndash;1778</strong>, New England Historic Genealogical Society; which Simon is not stated. <a href="https://snaccooperative.org/view/6284266">SNAC record for Cotton Tufts</a></li>
<li><strong>Cotton Tufts diaries, 1748&ndash;1794</strong> (interleaved almanacs), Massachusetts Historical Society. <a href="https://snaccooperative.org/vocab_administrator/resources/7140379">SNAC description</a></li>
<li>Abigail Adams to Cotton Tufts, 2 March 1788 (original, MHS). <a href="https://www.masshist.org/database/2154">MHS Collections Online</a></li>
<li>Also listed by SNAC: John Adams to &ldquo;Dr. Tufts,&rdquo; Nov. 18, 1797 (Morgan Library); Caleb Gannett to Cotton Tufts, Apr. 20, 1781 (Duke Medical Center Archives); John Avery to Cotton Tufts, Apr. 9, 1790 (Harvard University Archives).</li></ul>
{UNV("The Massachusetts Medical Society&rsquo;s own archives have not been searched. The NEHGS and Countway letters between the two brothers are the most likely source of letters on smallpox and throat distemper by Dr. Simon the younger.")}
</section>'''
_EXTRA7 = EXTRA
def EXTRA(path):
    out = _EXTRA7(path)
    if path == "collections.html": out = out.replace('<section id="muskets">', DOCTORS + "{DIV}" + '<section id="muskets">', 1) if '<section id="muskets">' in out else out + "{DIV}" + DOCTORS
    if path == "profiles/cotton-tufts.html": out += '{DIV}<section id="doctor-letters"><h2>His Letters</h2><p>The Adams Papers hold 188 letters by or to Dr. Cotton Tufts, ' + str(len(DIS)) + ' of them touching on smallpox inoculation, fevers, dysentery or measles. Examples: to John Adams, July 5, 1776: &ldquo;Yesterday People in Boston were openly inoculated for the Small Pox&rdquo; (<a href="' + MHSV + 'ADMS-04-02-02-0019">MHS</a>). His Countway papers hold letters with his brother Dr. Simon. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p></section>'
    if path == "profiles/simon-tufts-11-1.html": out += '{DIV}<section id="doctor-letters"><h2>His Letters</h2><p>Letters between this Dr. Simon (1727&ndash;1786) and the Loyalist Isaac Royall, 1775&ndash;1779, are quoted by Brooks (pp. 173&ndash;179) and the <em>Medford Historical Register</em> (vol. XI, p. 17). His letters with his brother Cotton are in the Countway Library. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p>' + UNV("Cause of death. This page&rsquo;s source says a fall from his horse, and Brooks (p. 306) says a fall brought on bleeding of the lungs. Mary Cranch wrote to Abigail Adams on September 28, 1786 that &ldquo;Doctor Simon Tufts is just gone in a consumtion&rdquo; (<a href=\"" + MHSV + "ADMS-04-07-02-0131\">MHS</a>), and Medford&rsquo;s church record gives consumption.") + '</section>'
    if path == "profiles/simon-tufts-1700.html": out += '{DIV}<section id="doctor-letters"><h2>Letters</h2><p>No letter by or to this Dr. Simon has yet been found. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p></section>'
    return out
