# Turell and Timothy Tufts profiles; Authoritative IDs and Spouse(s) sections on every profile (2026-11-03).
# Brooks (1855) page numbers are the printed pages of the 1855 edition (scan: archive.org historyoftownofm1855broo);
# Perseus omits page markers after p. 529 in the Register of Families, so the scan pages are used.
PERS_T = lambda doc, ch: f"https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A{doc}%3Achapter%3D{ch}&amp;force=y"
B55 = "Charles Brooks, <em>History of the Town of Medford</em> (1855)"
SCAN = "https://archive.org/details/historyoftownofm1855broo/page/"
BRG = lambda pg: f'{B55}, Register of Families, p. {pg}. <a href="{SCAN}{pg}">Page scan</a> &middot; <a href="{PERS_T("2001.05.0104", 18)}">Text (Perseus)</a>'
BRX = lambda pg, ch: f'{B55}, p. {pg}. <a href="{PERS_T("2001.05.0104", ch)}">Text (Perseus)</a>'
GILL = lambda pg: f'Eliza M. Gill, &ldquo;Turell Tufts and His Family Connections,&rdquo; <em>Medford Historical Register</em>, vol. XVIII (1915), p. {pg}. <a href="{PERS_T("2005.05.0018", 16)}">Text (Perseus)</a>'
BTH = lambda pg: f'{BOOTH}, p. {pg}. <a href="{BOOTH_URL}7">Text (Perseus)</a>'
COBURN = "Frank Warren Coburn, <em>The Battle of April 19, 1775</em> (1912), p. 150"
FREESE = "John W. Freese, <em>Historic Houses and Spots in Cambridge, Massachusetts, and Near-by Towns</em> (1897)"
MHSD = "https://www.masshist.org/digitaladams/archive/doc?id="
PL = lambda s, t: f'<a href="{{P}}profiles/{s}.html">{t}</a>'

PROFILES += [
 dict(slug="turell-tufts", name="Turell Tufts (1770&ndash;1842)", dates="1770&ndash;1842", town="Medford, Mass.", born="1770", died="1842", era="19th Century", line="Son of Dr. Simon Tufts (1727&ndash;1786)",
  bio=Q("Turell , b. 1770; d. June 9, 1842.", BRG(546) + ", among the children of Dr. Simon Tufts, jun., by his second wife, Elizabeth Hall")
   + f'<p>Turell Tufts was the eldest son of the second marriage of {PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)")}. He was named for the Rev. Ebenezer Turell, Medford&rsquo;s second minister, whose portrait he later left to the First Parish. His uncle {PL("cotton-tufts", "Dr. Cotton Tufts")} described him to John Adams in 1798 as a man &ldquo;bred in the Mercantile Line&rdquo; who had been in business at Hartford, Connecticut, and had lost heavily through Georgia land speculation and French depredations. He recommended him as well qualified for a consulship.</p>'
   + Q("Turell Tufts, a Son of my Brother Dr. Tufts decd.", 'Cotton Tufts to John Adams, June 1798, <em>Adams Family Correspondence</em>, vol. 13 (Adams Papers document ADMS-04-13-02-0057). <a href="https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-04-13-02-0057">MHS digital edition</a>')
   + Q("I have made Turell Tufts a Consul at Surinam.", f'John Adams to Abigail Adams, 28 January 1799. <a href="{MHSD}L17990128ja">MHS, Adams Family Papers</a>')
   + '<p>The Adams Papers editors note that Adams nominated him consul to Suriname on 10 January 1799 and that the Senate confirmed him on 14 January. He wrote from Paramaribo as &ldquo;T. Tufts Consul USA&rdquo; to Secretary of State James Madison on 28 January 1808, reporting the embargo of American vessels at Barbados (<em>Papers of James Madison</em>, Secretary of State Series; original in National Archives, RG 59, Consular Despatches, Paramaribo). His younger brother Hall Tufts died at Surinam in 1801 (Brooks, p. 546).</p>'
   + '<p>Back in Medford he became one of the town&rsquo;s leading citizens. When General Lafayette visited, it was Turell Tufts, as chairman of the selectmen, who gave the address of welcome:</p>'
   + Q("the Selectmen of the town met the General and his cortege ; and they thus addressed him, by Turell Tufts, Esq., their Chairman", f'{B55}, p. 141, in the account of Governor Brooks and Lafayette. <a href="{SCAN}141">Page scan (Internet Archive)</a>')
   + Q("Turell Tufts was selectman, 1820&mdash;1825 and 1827-1828. He served the town as its treasurer in 1827. In 1824 he was fence viewer, on the committee to audit the treasurer&rsquo;s books, was chosen moderator in absence of Dudley Hall, who was first chosen, and was representative to the General Court.", GILL(55))
   + '<p>He left Medford several bequests: five hundred dollars for roadside shade trees, five hundred dollars to the Medford Social Library, and communion plate and the portrait of Mr. Turell to the church.</p>'
   + Q("A legacy of five hundred dollars from Turell Tufts , Esq. , was expended, according to his directions, in planting ornamental trees on the roadsides.", BRX("58&ndash;59", 3))
   + Q("Turell Tufts , Esq. , bequeathed to it five hundred dollars, the interest of which must be expended annually for the purchase of valuable books.", BRX(294, 9) + ", on the Medford Social Library")
   + Q("1842, July.--The church received, from the hand of Dudley Hall, a bequest of the late Turell Tufts , Esq. ,--two pieces of plate for the communion-table; and a portrait of the Rev. Mr. Turell , one of the former pastors of this church.", BRX(494, 16))
   + f'<p>He lived in the old family house at Medford Square, &ldquo;successively the home of the elder and younger Drs. Simon, and Turell Tufts, Esq.&rdquo; ({MHR18}, p. 67). See <a href="{{P}}places.html#homesteads">Places</a>.</p>',
  service='<p>No military service. Civil offices: U.S. consul at Paramaribo, Surinam (nominated 10 Jan. 1799); Medford selectman 1820&ndash;25 and 1827&ndash;28, town treasurer 1827, and representative to the General Court in 1824 (Gill, p. 55).</p>',
  family=Q("The children by this union were Turell , born 1770, died 1842, unmarried; Cotton, born 1772, died 1835, was insane for forty-four years; Hall , born 1775, died 1801, at Surinam ; Hepsibah, born 1777; Stephen, born 1779, died young.", GILL(54) + ", on the children of Dr. Simon Tufts, Jr. and Elizabeth Hall")
   + f'<p>Father: {PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)")}. Mother: Elizabeth Hall (born May 15, 1743), daughter of Stephen Hall; she married secondly, on July 12, 1795, Capt. Duncan Ingraham of Concord, and died in 1830 aged 87 (Gill, pp. 54, 56). Grandfather: {PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)")}. Uncle: {PL("cotton-tufts", "Dr. Cotton Tufts")}. Half-brother: {PL("simon-tufts-29-1", "Simon Tufts (1750&ndash;1801)")} (Brooks, p. 546, lists &ldquo;Simon, b. 1750&rdquo; as the first son by Lucy Dudley; Gill, p. 54, says he died at the Cape of Good Hope in 1802).</p>',
  unverified="Gill gives Simon Jr.&rsquo;s death as 1802 at the Cape of Good Hope; the Simon Tufts (1750&ndash;1801) profile uses 1801. The full text of Cotton Tufts&rsquo;s June 1798 letter was quoted from the MHS edition&rsquo;s search extract; the page could not be opened directly from here (server error), so its exact date (the editors refer to a letter of 14 June) is unconfirmed. His burial in the Tufts family tomb, Salem Street Burying Ground, is reported only by a private genealogy website and is not confirmed."),
 dict(slug="timothy-tufts", name="Timothy Tufts (1735&ndash;1805)", dates="1735&ndash;1805", town="Charlestown (now Somerville), Mass.", born="1735", died="1805", era="The Revolution", line="Son of Peter Tufts of Milk Row",
  bio=Q("Timothy, the third son of Peter of Milk Row, who was born in 1735, received from his father a farm on Elm street, at the corner of Willow avenue.", BTH(25))
   + Q("This house was built about a year before the Revolution, and replaced an older one which stood on a knoll by a large elm tree somewhat farther back from the street. Timothy Tufts was a prominent man in public affairs. He was frequently chosen moderator of the town meeting and was a selectman for most of the years between 1780 and 1792. He is always spoken of in the records as Timothy Tufts , Esquire , and his commission as justice of the peace, signed by Governor John Hancock , may be still seen hanging in the sitting-room of the old house.", BTH(25))
   + '<p>On the afternoon of April 19, 1775, Lord Percy&rsquo;s column, falling back from Lexington and Concord, turned off toward Charlestown and passed his door on the road now called Elm Street. The historian of the day&rsquo;s fighting describes what happened there:</p>'
   + Q("Near the corner of Beech Street, and on the easterly side of Elm Street, stood the house of Timothy Tufts. Here Percy halted his army while his two field pieces were dragged up the hill back of the Tufts house and discharged toward his pursuers, with the usual result of his cannonading, - none killed. From out a grove a little way up the road came a scattering fire of American sharpshooters, and in consequence quite a number of Britons were killed. They fell in the road, just in front of the Tufts house, and a tablet there marks where they were buried.", COBURN + ' (quoted from the transcription at <a href="http://www.battleroad.net/rememberingthefallen/gravesite17.html">battleroad.net</a>; page scan not yet checked)')
   + Q("A SHARP FIGHT OCCURRED HERE BETWEEN THE PATRIOTS AND THE BRITISH APRIL 19, 1775. THIS MARKS BRITISH SOLDIERS&rsquo; GRAVES. The house in front of which this tablet stands was built by Timothy Tufts, and was a witness of the &ldquo; sharp fight.&rdquo;", FREESE + ', Somerville section (page not recorded; <a href="https://ldsgenealogy.com/MA/books/Historic-houses-and-spots-in-Cambridge-Massachusetts-and-near-by-towns-part-3.htm">transcription</a>). The tablet survives at Elm Street near Beech Street (<a href="https://www.hmdb.org/m.asp?m=103186">HMdb marker 103186</a>).')
   + f'<p>He served Charlestown&rsquo;s Milk Row school as a committeeman from 1776 (<em>Historic Leaves</em>, vol. 3, pp. 90&ndash;93). See also <a href="{{P}}places.html#homesteads">the Timothy Tufts house on Places</a>.</p>',
  service='<p>Civil: moderator, selectman (most years 1780&ndash;1792) and justice of the peace (Booth, p. 25). No military service record has yet been matched to him in <em>Massachusetts Soldiers and Sailors</em>.</p>',
  family=Q("Timothy married Anne Adams , a niece of the wife of his brothers, Nathan and Peter . They had sons Timothy, Abijah, Isaac, and Joseph.", BTH(25))
   + Q("68 Timothy, b. Jan. 20, 1735.", BRG(545) + ", among the children of Peter Tufts of Milk Row and Lydia Buckman")
   + '<p>Father: Peter Tufts of Milk Row (d. Dec. 5, 1776). Mother: Lydia Buckman (Brooks, p. 545). Brothers include Nathan (b. 1724), who married Mary Adams, and Peter of Winter Hill (b. 1728), who married Anne Adams (see <a href="{P}generations/colonial.html#peter-1728">Peter Tufts of Winter Hill</a>). Peter Tufts of Winter Hill was the father of <a href="{P}profiles/peter-tufts-jr.html">Peter Tufts Jr. (1753&ndash;1832)</a>, Timothy&rsquo;s nephew. Booth (p. 25) says his eldest son Timothy Jr. &ldquo;died in 1802, three years before his father,&rdquo; which places the elder Timothy&rsquo;s death in 1805.</p>',
  unverified="<strong>Which Timothy:</strong> the 1775 house was the elder Timothy&rsquo;s (b. 1735). His son Timothy Jr. (d. 1802) lived on Broadway, and a grandson Timothy owned the Elm Street house in 1897&ndash;1903. <strong>Death year 1805</strong> is worked out from Booth&rsquo;s &ldquo;three years before his father&rdquo;, not from a record. <strong>Build date conflict:</strong> Booth says the house was built &ldquo;about a year before the Revolution&rdquo;; a modern Historypin caption says 1761. <strong>&ldquo;One of the heaviest engagements of the retreat&rdquo;</strong> is not stated in any source seen. Coburn calls the cannon fire harmless and says &ldquo;quite a number of Britons were killed&rdquo;; the tablet calls it a &ldquo;sharp fight.&rdquo; Coburn and Freese are quoted from online transcriptions, not page scans. The house was demolished; Historypin gives 1904."),
]

# ---------- Spouse(s) ----------
NF = "Not found in the sources checked (Brooks 1855 Register of Families; Wild; Find a Grave data on file; <em>Tufts Kinsmen</em> Vol. I extract)."
SP = {
 "turell-tufts": Q("Turell , born 1770, died 1842, unmarried", GILL(54)) + "<p>Unmarried. Brooks (p. 546) records no marriage.</p>",
 "timothy-tufts": "<ul><li><strong>Anne (Anna) Adams.</strong> Marriage date and place not found.</li></ul>" + Q("38-68 TIMOTHY Tufts m. Anna ----, and had--", BRG(547)) + "<p>Booth (p. 25) gives her surname as Adams, &ldquo;a niece of the wife of his brothers.&rdquo;</p>",
 "simon-tufts-11-1": "<ul><li><strong>Lucy Dudley</strong> (1727&ndash;1768). Married February 23, 1749.</li><li><strong>Elizabeth Hall</strong> (1743&ndash;1830), daughter of Stephen Hall. Married October 5, 1769. As his widow she married Capt. Duncan Ingraham of Concord, July 12, 1795.</li></ul>"
   + Q("D R. Simon Tufts , Jr. (1727-1786) married Lucy Dudley (1727-1768), February 23, 1749.", GILL(54))
   + Q("He m., 2d, Elizabeth Hall, Oct. 5, 1769", BRG(546)) + '<p>Brooks (p. 546) gives Lucy Dudley&rsquo;s death as &ldquo;Nov., 1768, aged 41&rdquo; but no first marriage date. Find a Grave memorial 26903836 gives both marriages (1749, 1769). Place of marriage not found.</p>',
 "simon-tufts-1700": "<ul><li><strong>Abigail Smith</strong> (d. 1790, aged 90). Marriage date and place not found.</li></ul>" + Q("He m. Abigail Smith , who d. 1790, aged 90", BRG(545)),
 "cotton-tufts": "<ul><li><strong>Lucy Quincy</strong> (1729&ndash;1785), first wife.</li><li><strong>Susanna Warner</strong>, second wife.</li></ul><p>Both names from Jay Franklin Tufts, <em>Tufts Family History</em>, p. 37 (see Family Connection); Find a Grave memorial 68293670 names Lucy (Quincy) Tufts. Dates and places of marriage not found.</p>"
   + Q("COTTON Tufts m.---- Smith , sister-in-law of President John Adams", BRG(546)) + UNV("Brooks&rsquo;s &ldquo;m.---- Smith&rdquo; conflicts with the Lucy Quincy of the other sources. Lucy Quincy was a cousin of Abigail (Smith) Adams; Brooks appears to have confused the Smith connection. Brooks is reported here, not followed."),
 "caleb-tufts": "<ul><li><strong>Rebecca Burrows</strong> (1764&ndash;1819). Married 1787 (Wild, p. 50, quoted in Family Connection). Place not stated.</li></ul>",
 "peter-tufts-jr": "<ul><li><strong>Hannah Adams</strong> (d. 1816, aged 60). Married July 22, 1773, at Cambridge (Wyman, vol. II, p. 965, quoted in Family Connection).</li></ul>",
 "joseph-tufts-jr-15-2": "<ul><li><strong>Hannah Cutter</strong> (d. 1779). Married 1754 per Find a Grave; Hannah Cutter per <em>Tufts Kinsmen</em>, Vol. I, p. 119.</li></ul>" + Q("33-61 Joseph Tufts , who d. Dec. 6, 1798, m. Hannah ----, who d. Sept. 21, 1779, aged 45", BRG(546)) + UNV("Brooks gives his death as Dec. 6, 1798; his stone, Find a Grave and Vol. I give 1778. The 1798 looks like a misprint."),
 "samuel-tufts-15-3": "<ul><li><strong>Hannah Tufts</strong> (d. 1795, aged 60). Married April 14, 1757.</li></ul>" + Q("Samuel Tufts , who d. Dec. 31, 1818, m. Hannah Tufts , Apr. 14, 1757, who d. Mar. 13, 1795, aged 60", BRG(546)) + UNV("Brooks files this Samuel under Dr. Simon Tufts&rsquo;s son Samuel (b. 1736). Wild (p. 53), <em>Tufts Kinsmen</em> Vol. I and Find a Grave make him the son of Joseph, b. 1732. The death date and wife agree, so the marriage is taken as his; the parentage in Brooks is not followed."),
 "william-tufts-13-6": "<ul><li><strong>Catherine Wyman</strong> (d. 1749). Find a Grave gives the marriage as 1732.</li><li><strong>Mary Francis.</strong> Married February 8, 1750 (Brooks); Find a Grave gives 1749.</li></ul>" + Q("William Tufts m., 1st, Catherine Wyman , who d. 1749; and had-- &hellip; He m., 2d, Mary Francis , Feb. 8, 1750", BRG(550)) + '<p class="note">1749/1750: a February 1749/50 date in Old Style dating would explain the difference.</p>',
 "william-tufts-40-2": "<ul><li><strong>Susanna</strong> (surname not given).</li></ul>" + Q("290 William Tufts , 4th, m. Susanna----. He died Apr. 27, 1782", BRG(551)) + '<p class="note">Matched by death date (Find a Grave: d. 27 Apr. 1782). Brooks also lists him as no. 257, son of William, b. Mar. 27, 1736.</p>',
 "samuel-tufts-41-2": "<ul><li><strong>Margaret Hodgkins</strong> of Ipswich (d. 1793). Married before 1779 (Wild, p. 53).</li></ul>" + Q("255-267 Samuel Tufts m. Margaret Hodgkins , who d. Aug. 7, 1793. He d. Nov. 29, 1815", BRG(551)),
 "nathan-tufts-jr": "<ul><li><strong>Sarah Trefray.</strong> Married February 22, 1776.</li></ul>" + Q("341 NATHAN Tufts , jun. , m. Sarah Trefray , Feb. 22, 1776", BRG(552)),
 "moses-tufts-40-6": UNV("Possible only: Brooks (p. 552) has &ldquo;324 Moses Tufts m. Phebe Thompson , May 7, 1767&rdquo;, but does not say which Moses. Not attached until confirmed."),
 "hutchinson-tufts": UNV("Possible only: Brooks (p. 547) has &ldquo;39-77 HUTCHINSON Tufts , who d. Aug. 2, 1800, m. Mary Grover&rdquo;. This profile gives no dates to confirm the match."),
 "daniel-tufts": UNV("Possible only: Brooks (p. 548) has &ldquo;65-104 Daniel Tufts m. Abigail Tufts&rdquo;. Several Daniel Tuftses lived in Medford; not attached."),
 "eliphalet-tufts-25-4": "<p>Unmarried (<em>Tufts Kinsmen</em>, Vol. I, p. 137).</p>",
 "nathan-tuffs-35-9": "<p>Unmarried (<em>Tufts Kinsmen</em>, Vol. I, p. 150).</p>",
 "samuel-tufts": "<p>Several men. Spouses are given under each man in Family Connection (e.g. Martha Upham; Margaret Hodgkins; Hannah Tufts).</p>",
 "william-tufts": "<p>Several men; see Family Connection. No spouse is attached to a single man here.</p>",
}

# ---------- Authoritative IDs ----------
PKEYS = set("simon peter jonathan john joseph james william nathan turell samuel benjamin timothy isaac daniel francis charles ebenezer asa aaron hutchinson moses cotton".split())
FAGOK = {k.split("/")[1].replace(".html", ""): v[0] for k, v in FG_PAGES.items() if v[0]}
FAGOK["simon-tufts-1700"] = "26903835/simon-tufts"
FAGQ = {"grimes-tufts-40-8": "Uncertain: two duplicate memorials, 250967026 and 198523618", "nathan-tufts-15-7": "Uncertain: probable 26891997, not accepted",
        "samuel-tufts-28-11": "Uncertain: 29337459 (Westford), likely not him", "simon-tufts-29-1": "Uncertain: 26903840", "william-tuffs-35-8": "Uncertain: 21091070",
        "francis-tufts-20-1": "Uncertain: 78802812 (from a search summary only)"}
FAGNO = set("isaac-tufts-36-10 john-tufts-53-3 moses-tufts-40-6 andrew-tufts-43-3 samuel-tufts-44-3 nathan-tuffs-35-9 barnabas-tufts henry-tufts-25-1 eliphalet-tufts-25-4 zachariah-tufts".split())
BREG = {"simon-tufts-1700": ("2-23", 545), "simon-tufts-11-1": ("23-52", 546), "cotton-tufts": ("23-55", 546), "turell-tufts": ("85 (52-85)", 546), "timothy-tufts": ("68 / 38-68", "545, 547"),
        "samuel-tufts-15-3": ("62; family 23-56 (see Spouse note)", "545&ndash;546"), "joseph-tufts-jr-15-2": ("61 / 33-61", "545&ndash;546"), "caleb-tufts": ("94", 546),
        "peter-tufts-jr": ("107 (66-107)", 547), "william-tufts-13-6": ("2-255", 550), "william-tufts-40-2": ("257; 290", "550&ndash;551"), "george-tufts-40-7": ("258", 550),
        "grimes-tufts-40-8": ("259", 550), "samuel-tufts-41-2": ("261 / 255-267", "550&ndash;551"), "david-tufts-41-7": ("265", 550), "moses-tufts-40-6": ("266a (possible)", 550),
        "nathan-tufts-jr": ("341 (same as 291)", "551&ndash;552")}
DAR = {"peter-tufts-jr": "A116812 (secondhand, as cited in <em>Tufts Kinsmen</em> Vol. I; not yet checked in the DAR GRS)"}
ADAMS = {"turell-tufts": f'ADMS-04-13-02-0057; L17990128ja (<a href="{MHSD}L17990128ja">MHS</a>)', "simon-tufts-11-1": "ADMS-01-01-02-0010-0007-0001 and others (see Collections)",
         "cotton-tufts": "188 letters in the Adams Papers digital edition (see Collections)", "simon-tufts-29-1": "ADMS-06-18-02-0162 (editors&rsquo; identification)"}
NC = "Not yet checked"
def IDSEC(p):
    s = p["slug"]; m = re.search(r'-(\d+-\d+)$', s)
    first = re.sub(r'^(Dr\.|Rev\.|Capt\.|Lieut\.|Sgt\.|Cpl\.) ', '', re.sub(r'<[^>]+>|&[a-z]+;', '', p["name"])).split()[0].lower()
    rows = []
    if s == "turell-tufts": per = f'<code>auth=tufts,turell</code>, a key used only for him (Brooks, chs. 3, 5, 7, 8, 9, 16; <a href="{PERS_T("2005.05.0018", 16)}">MHR vol. XVIII</a>). Confirmed.'
    elif first in PKEYS: per = f'<code>auth=tufts,{first}</code>. This is a name-level key shared by every {first.title()} Tufts in Perseus, not a personal ID. Use it with the passages cited on this page.'
    else: per = "Checked, not found (no <code>auth=tufts,…</code> key for this name in Brooks, the <em>Medford Historical Register</em> or <em>Historic Leaves</em>)."
    rows.append(("Perseus person index (auth=)", per))
    if s in FAGOK: rows.append(("Find a Grave memorial", f'<a href="{FG}{FAGOK[s]}">{FAGOK[s].split("/")[0]}</a>' + (" (shown on his son&rsquo;s memorial as father; not opened)" if s == "simon-tufts-1700" else " (dates and family checked)")))
    elif s in FAGQ: rows.append(("Find a Grave memorial", FAGQ[s] + ". Flagged; not used."))
    elif s in FAGNO: rows.append(("Find a Grave memorial", "Checked, not found"))
    else: rows.append(("Find a Grave memorial", NC + " (Find a Grave blocks automated searches from this machine)"))
    rows.append(("Brooks, <em>History of Medford</em> (1855) register no.", f"No. {BREG[s][0]}, p. {BREG[s][1]}" if s in BREG else "Checked, no entry confidently matched"))
    if m: rows.append(("<em>Tufts Kinsmen</em>, Vol. I family no.", m.group(1)))
    mss = sorted(set(re.findall(r'Revolutionary War</em>, vol\. ([XVI]+)[^,]*, pp?\. ([0-9&ndash;]+)', p.get("bio", "") + p.get("service", "") + p.get("family", ""))))
    rows.append(("<em>Mass. Soldiers and Sailors</em>", "; ".join(f"vol. {v}, p. {g}" for v, g in mss) if mss else ("No military entry expected (civil career)" if s in ("turell-tufts", "simon-tufts-1700") else NC + " for this page")))
    rows.append(("DAR ancestor no.", DAR.get(s, NC + " (the DAR GRS needs a browser session)")))
    if s in ADAMS: rows.append(("Adams Papers document IDs", ADAMS[s]))
    rows += [("FamilySearch ID", NC + " (FamilySearch is blocked from this machine; owner to check)"), ("Geni profile", NC + " (Geni requires sign-in)"),
             ("WikiTree ID", NC + " (WikiTree API refused requests on 3 Nov. 2026: rate limit)"), ("Town / vital records", "Medford VRs not yet checked by volume and page" if s not in BREG else "Brooks&rsquo;s register (above) is drawn from Medford town and church records; printed VR volume and page not yet checked")]
    return '<section id="ids"><h2>Authoritative IDs / Index Numbers</h2><table class="ids"><thead><tr><th>Source</th><th>ID / status</th></tr></thead><tbody>' + "".join(f"<tr><td>{a}</td><td>{b}</td></tr>" for a, b in rows) + '</tbody></table><p class="note">Only IDs confirmed against dates and family are given as matches. &ldquo;Not yet checked&rdquo; means the source has not been searched; &ldquo;Checked, not found&rdquo; means it was searched without a match.</p></section>'
def SPSEC(p):
    return '<section id="spouses"><h2>Spouse(s)</h2>' + SP.get(p["slug"], "<p>" + NF + "</p>") + '</section>'
_profile0 = profile
def profile(p):
    p = dict(p); p["unverified"] = p["unverified"]
    p["family"] = p["family"] + "</section>{DIV}" + SPSEC(p).replace("</section>", "") 
    _profile0(p)
    f = f'profiles/{p["slug"]}.html'; h = open(f).read()
    h = re.sub(r'<a href="\.\./profiles/' + p["slug"] + r'\.html">(.*?)</a>', r'\1', h)
    h = h.replace('<section id="unverified">', IDSEC(p) + '\n<section id="unverified">', 1)
    open(f, "w").write(h)
# Perseus hits: link Timothy and Turell
PERS[:] = [(d, t.replace("Timothy Tufts and Samuel", "<a href='{P}profiles/timothy-tufts.html'>Timothy Tufts</a> and Samuel"), c) for d, t, c in PERS]
PERS += [("1824", "<a href='{P}profiles/turell-tufts.html'>Turell Tufts</a>, chairman of the selectmen, welcomed Lafayette to Medford.", f'{BR}, p. 141. <a href="{SCAN}141">Page scan</a>'),
         ("1770&ndash;1842", "Gill&rsquo;s sketch of <a href='{P}profiles/turell-tufts.html'>Turell Tufts</a>, &ldquo;unmarried,&rdquo; selectman, treasurer and representative.", PH_(MR("XVIII"), "54&ndash;56", "2005.05.0018", 16))]
_rp = open("tools/researchpass.py").read(); exec(_rp[_rp.index("RP = ("):_rp.index("_EXTRA8 = EXTRA")])
# ---------- Relatives with their own profiles (matched by identity, not by name) ----------
W1 = [("william-tufts-40-2", "brother William Jr. (1736&ndash;1782; mother Catherine Wyman)"), ("george-tufts-40-7", "brother George (1747&ndash;1796; mother Catherine Wyman)"), ("grimes-tufts-40-8", "brother Grimes (1748&ndash;1808; mother Catherine Wyman)"),
      ("samuel-tufts-41-2", "brother Samuel 2nd (1752&ndash;1815; mother Mary Francis)"), ("david-tufts-41-7", "brother David (1763&ndash;1823; mother Mary Francis)"), ("moses-tufts-40-6", "brother Moses (possible; Brooks no. 266a)")]
def _sib(me, father=("william-tufts-13-6", "father Lieut. William Tufts (1713&ndash;1783)")):
    return [father] + [x for x in W1 if x[0] != me]
REL = {
 "simon-tufts-1700": [("simon-tufts-11-1", "son Dr. Simon Tufts (1727&ndash;1786)"), ("cotton-tufts", "son Dr. Cotton Tufts (1732&ndash;1815)"), ("turell-tufts", "grandson Turell Tufts"), ("simon-tufts-29-1", "grandson Simon Tufts (1750&ndash;1801)")],
 "simon-tufts-11-1": [("simon-tufts-1700", "father Dr. Simon Tufts (1700&ndash;1747)"), ("cotton-tufts", "brother Dr. Cotton Tufts"), ("simon-tufts-29-1", "son Simon Tufts (1750&ndash;1801), by Lucy Dudley"), ("turell-tufts", "son Turell Tufts (1770&ndash;1842), by Elizabeth Hall")],
 "cotton-tufts": [("simon-tufts-1700", "father Dr. Simon Tufts (1700&ndash;1747)"), ("simon-tufts-11-1", "brother Dr. Simon Tufts (1727&ndash;1786)"), ("turell-tufts", "nephew Turell Tufts"), ("simon-tufts-29-1", "nephew Simon Tufts (1750&ndash;1801)")],
 "simon-tufts-29-1": [("simon-tufts-11-1", "father Dr. Simon Tufts (1727&ndash;1786)"), ("simon-tufts-1700", "grandfather Dr. Simon Tufts (1700&ndash;1747)"), ("cotton-tufts", "uncle Dr. Cotton Tufts"), ("turell-tufts", "half-brother Turell Tufts")],
 "turell-tufts": [("simon-tufts-11-1", "father"), ("simon-tufts-1700", "grandfather"), ("cotton-tufts", "uncle"), ("simon-tufts-29-1", "half-brother Simon")],
 "timothy-tufts": [("peter-tufts-jr", "nephew Peter Tufts Jr. (1753&ndash;1832)")],
 "peter-tufts-jr": [("timothy-tufts", "uncle Timothy Tufts (1735&ndash;1805)")],
 "samuel-tufts-15-3": [("joseph-tufts-jr-15-2", "brother Capt. Joseph Tufts Jr. (1731&ndash;1778)"), ("caleb-tufts", "son Caleb Tufts (1762&ndash;1852)")],
 "joseph-tufts-jr-15-2": [("samuel-tufts-15-3", "brother Samuel Tufts (1732&ndash;1818)"), ("caleb-tufts", "nephew Caleb Tufts")],
 "caleb-tufts": [("samuel-tufts-15-3", "father Samuel Tufts (1732&ndash;1818)"), ("joseph-tufts-jr-15-2", "uncle Capt. Joseph Tufts Jr.")],
 "william-tufts-13-6": [(s, l.replace("brother ", "son ")) for s, l in W1],
 "william-tufts-40-2": _sib("william-tufts-40-2") + [("nathan-tufts-jr", "son Nathan Tufts Jr.")],
 "george-tufts-40-7": _sib("george-tufts-40-7"), "grimes-tufts-40-8": _sib("grimes-tufts-40-8"), "samuel-tufts-41-2": _sib("samuel-tufts-41-2"),
 "david-tufts-41-7": _sib("david-tufts-41-7"), "moses-tufts-40-6": _sib("moses-tufts-40-6"),
 "nathan-tufts-jr": [("william-tufts-40-2", "father William Tufts Jr. (1736&ndash;1782), &ldquo;William Tufts, 4th&rdquo; in Brooks"), ("william-tufts-13-6", "grandfather Lieut. William Tufts")],
}
RELNOTE = {**{k: " Brothers are listed with their mothers as Brooks gives them (p. 550); sons of different mothers are half-brothers." for k in ("william-tufts-40-2","george-tufts-40-7","grimes-tufts-40-8","samuel-tufts-41-2","david-tufts-41-7","moses-tufts-40-6")},"william-tufts-13-6": " Sons by Catherine Wyman: William, George, Grimes (Brooks, p. 550). By Mary Francis: Samuel and David. Moses (no. 266a) is listed without a mother.",
           "nathan-tufts-jr": " Brooks, p. 552, says no. 341 is the &ldquo;Same as No. 291,&rdquo; the son of no. 290, William 4th.",
           "caleb-tufts": " Brooks, p. 546, lists &ldquo;94 Caleb, b. Sept. 1, 1762&rdquo; among Samuel and Hannah&rsquo;s children."}
_profile1 = profile
def profile(p):
    r = REL.get(p["slug"])
    if r:
        p = dict(p); p["family"] = p["family"] + '<p class="relatives"><strong>Relatives with profiles on this site:</strong> ' + "; ".join(PL(s, l) for s, l in r) + "." + RELNOTE.get(p["slug"], "") + "</p>"
    _profile1(p)
