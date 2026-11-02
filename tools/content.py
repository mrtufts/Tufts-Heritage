# Site content. Every book citation has an exact quote, its printed page, and a page scan.
import json
IMG = "{P}sources/images/"
def Q(text, cite, scans=(), note=""):
    links = " &middot; ".join(f'<a href="{IMG}{s}">page scan</a>' for s in scans)
    return f'<blockquote>&ldquo;{text}&rdquo;</blockquote>\n<p class="cite">{cite}{(" &middot; " + links) if links else ""}{(" " + note) if note else ""}</p>'
def UNV(text):
    return f'<div class="flag"><h3>&#9873; Unverified</h3><p>{text}</p></div>'
MSS = "<em>Massachusetts Soldiers and Sailors of the Revolutionary War</em>, vol. XVI (1907)"
WILD = "Helen Tilden Wild, <em>Medford in the Revolution</em> (1903)"
WYMAN = "Thomas Bellows Wyman, <em>The Genealogies and Estates of Charlestown</em>, vol. II (1879)"
JONES = "Alvin Lincoln Jones, <em>Under Colonial Roofs</em> (1894)"
TFH = "Jay Franklin Tufts, <em>Tufts Family History 1633&ndash;1963</em> (secondary source)"
CHASE = "Ellen Chase, <em>The Beginnings of the American Revolution</em>, vol. III (1910)"

# ---------------- Profiles ----------------
PROFILES = [
 dict(slug="peter-tufts-jr", name="Peter Tufts Jr.", dates="1753 &ndash; [death year unverified]", town="Medford", born="1753", died="", era="The Revolution", line="Peter Tufts of Winter Hill",
  bio="""<p>Peter Tufts Jr. was born in 1753, the son of Peter and Anne (Adams) Tufts of Winter Hill. On April 19, 1775, the day his parents marked their twenty-fifth wedding anniversary, he marched from Medford with Capt. Isaac Hall's company on the Lexington alarm. Medford later listed his name on its monument to the town's First Company of Minute Men.</p>""",
  service=Q("TUFTS, PETER, Jr., Medford. Private, Capt. Isaac Hall's co., Col. Thomas Gardner's regt., which assembled April 19, 1775; service, 5 days; also, account of money paid by persons to hire men to go to Canada [year not given], examined [p. 137] and allowed by a committee at Medford Oct. 8, 1776; also, account of money paid by persons to hire men who went to New York in Sept., 1776, examined and allowed by a committee at Medford Jan. 13, 1777. [p. 138]", MSS+", pp. 137&ndash;138", ["mss-v16-p137.jpg","mss-v16-p138.jpg"]) +
   Q("TUFTS, PETER, JR. Private, Lexington alarm; loaned money for bounty paid to men enlisting July and Sept., 1776; served guarding troops of convention, 1778.", WILD+", p. 52", ["wild-medford-in-revolution-p52.jpg"]) +
   Q("TUFTS PETER JR.", "Roster of the First Company of Minute Men, monument erected by the City of Medford (1925)", ["medford-1925-monument.jpg"], ""),
  family=Q("Son of Peter and Anne (Adams) of Winter Hill; born 1753; married Hannah Adams; died 1836.", WILD+", p. 52", ["wild-medford-in-revolution-p52.jpg"]) +
   Q("PETER 38. Son of Peter 37; m. HANNAH ADAMS [19] July 22, 1773, at Camb., who d. 1816, &aelig;. 60 (tablet with Bernard).", WYMAN+", p. 965", ["wyman-v2-p965.jpg"]) +
   Q("ii. Peter, Jan. 9, 1753.", WYMAN+", p. 965 (issue of Peter 37)", ["wyman-v2-p965.jpg"]),
  unverified="Death year. Wild (p. 52) prints &ldquo;died 1836.&rdquo; Secondhand web sources for DAR ancestor A116812 give 1832. Wyman gives no death date. A separate MSS entry, &ldquo;TUFTS, PETER. Private, Capt. Benjamin Blaney's co., Col. Eleazer Brooks's regt. of guards; joined Jan. 23, 1778&rdquo; (p. 137), gives no town, so it is not attached to him here. <em>Tufts Kinsmen</em> Vol. II gives no death date for Peter5 (generation 5 is in Vol. I). Vol. I and DAR records have not been seen."),
 dict(slug="cotton-tufts", name="Dr. Cotton Tufts", dates="[birth year not in sources seen] &ndash; 1815", town="Medford; Weymouth", born="", died="1815", era="The Revolution", line="Dr. Simon Tufts",
  bio="""<p>Dr. Cotton Tufts was born in Medford, the son of Dr. Simon Tufts. He practiced medicine in Weymouth until his death in 1815. A family history records his ties to the Adams family: John Adams noted dining with him in 1796. The same history credits him with service as a state senator and as a delegate to the convention that adopted the Constitution. These points come from a 20th-century secondary source and are quoted as written.</p>""",
  service=Q("Dr. Cotton Tufts besides practicing medicine in Weymouth was a State Senator for many years; also a delegate to the convention which adopted the constitution of the United States; Always an ardent Federalist.", TFH+", p. 35", ["tufts-family-history-p35.jpg"]) +
   '<p class="note">No entry for Cotton Tufts appears among the Tufts entries in '+MSS+', pp. 131&ndash;140.</p>',
  family=Q("Dr. Tufts was Dr. Cotton Tufts, born in Medford, the son of Dr. Simon Tufts, first Physician of Medford, and probably also of Massachusetts. Dr. Cotton Tufts started his medical practice in Weymouth and remained there until his death in 1815. His first wife was Lucy Quincy; he later married Susanna Warner.", TFH+", p. 37 (printed page number per archive.org page map; not legible on the scan)", ["tufts-family-history-p37.jpg"]) +
   Q("July 17, 1796, yesterday Dr. Tufts and family, also Mr. Otis, (presumably a friend of both families) dined with me.", TFH+", p. 37, quoting John Adams's diary", ["tufts-family-history-p37.jpg"]),
  unverified="Birth year, Harvard class, and the claims of state senate and ratifying-convention service come only from the secondary source above. Not yet checked against primary records. The same page lists &ldquo;Cotton, Jr. (Esq), (1791-1872)&rdquo; with dates identical to &ldquo;Quincy (1791-1872)&rdquo;, an apparent error in the source (p. 35)."),
 dict(slug="zachariah-tufts", name="Zachariah Tufts", dates="[dates not in sources seen]", town="Woburn", born="", died="", era="The Revolution", line="Undetermined",
  bio="""<p>Two entries under the name Zachariah Tufts of Woburn appear in <em>Massachusetts Soldiers and Sailors</em>. The first follows a private in Capt. John Wood's company through 1775, in camp at Medford and Cambridge. The second is a 1780 descriptive list of a man aged 21, engaged for Woburn for three years.</p>""",
  service=Q("TUFTS, ZACHARIAH, Woburn. List of men belonging to Capt. John Wood's co. who took the oath in Middlesex Co. May 27, 1775, required by Congress to be taken by the Mass. army; also, Capt. Wood's (5th) co., Col. Samuel Gerrish's regt.; order for advance pay, signed by said Tufts and others, dated Cambridge, June 1, 1775; also, Private, Capt. Wood's co., Lieut. Col. Loammi Baldwin's (late Col. Gerrish's) 38th (also given 37th) regt.; muster roll dated Aug. 1, 1775; enlisted May 5, 1775; service, 88 days; &hellip;", MSS+", p. 140", ["mss-v16-p140.jpg"]) +
   Q("TUFTS, ZACHARIAH. Descriptive list of men raised in Middlesex Co., agreeable to resolve of Dec. 2, 1780, as returned by Joseph Hosmer, Superintendent for said county; age, 21 yrs.; stature, 5 ft. 9 in.; complexion, light; hair, light; eyes, blue; occupation, laborer (also given farmer); engaged for town of Woburn; engaged April 1, 1781; term, 3 years.", MSS+", p. 140", ["mss-v16-p140.jpg"]),
  family="<p>No family connection has been found in the sources seen.</p>",
  unverified="Whether the two Woburn entries are the same man. A man aged 21 in 1780&ndash;81 would have been about 15 in 1775. They are shown together only because the name and town match."),
 dict(slug="william-tufts", name="William Tufts (several men)", dates="See entries", town="Bedford; Medford; others not given", born="", died="", era="The Revolution", line="Undetermined",
  bio="""<p>Several different men named William Tufts served in the Revolution. This page lists each record separately. It does not merge them, because the records do not show which entries belong to the same man.</p>""",
  service=Q("TUFTES, WILLIAM. Private, Capt. Samuel Ward's co., Col. Solomon Lovell's regt.; service, 5 days, subsequent to March 10, 1776. Roll sworn to in Suffolk Co.", MSS+", p. 131 (spelled Tuftes)", ["mss-v16-p131.jpg"]) +
   Q("TUFTS, WILLIAM, Bedford. List of men mustered by Nathaniel Barber, Muster Master for Suffolk Co., dated Boston, April 13, 1777; Capt. Pettengill's co., Col. Wesson's regt.; reported received State bounty.", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   Q("TUFTS, WILLIAM, Medford. Private, Capt. Stephen Dana's co., Col. McIntosh's (McIntosh's) regt.; arrived at camp March 19 [1778]; discharged April 5 [1778]; service, 18 days, at the Lines at Boston.", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   Q("TUFTS, WILLIAM. 2d Lieutenant, Capt. Ezekiel Knowlton's co.; list of officers chosen to command three companies drafted from [Brig.] Jonathan Warner's brigade to serve at and about Boston, as returned by said Warner to Maj. Gen. Warren, July 27, 1776.", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   Q("TUFTS, WILLIAM. Private, Capt. Nathan Sergant's co. of guards; entered service Feb. 3, 1779; discharged May 3, 1779; service, 3 mos.; company raised for service under Maj. Gen. Gates at and about Boston.", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   Q("TUFTS, WILLIAM. Private, Capt. Stephen Frost's co., Col. Cyprian How's regt.; entered service July 31, 1780, 3 days preceding march; discharged Nov. 1, 1780; service 3 mos. 2 days (also given 96 days), at Rhode Island, including travel (60 miles) home; regiment raised for 3 months.", MSS+", p. 140", ["mss-v16-p140.jpg"]) +
   Q("TUFTS, WILLIAM, Jr. Account of money paid by persons to hire men to go to Canada [year not given], examined and allowed by a committee at Medford Oct. 8, 1776.", MSS+", p. 140", ["mss-v16-p140.jpg"]),
  family=Q("TUFTS, WILLIAM. Served at lines at Boston, 1776; in Col. Wesson's Regt., 1777. Son of William and Catherine (Tufts); born 1762; killed 1777.", WILD+", p. 53", ["wild-medford-in-revolution-p53.jpg"]) +
   Q("TUFTS, WILLIAM, 4TH. Joined army at Clavarack, 1779, for 3 mos.; signature on original receipt for bounty in archives.", WILD+", p. 53", ["wild-medford-in-revolution-p53.jpg"]),
  unverified="Which MSS entries match Wild's William (b. 1762, killed 1777) or William 4th. Wild's &ldquo;Col. Wesson's Regt., 1777&rdquo; resembles the MSS Bedford entry, but MSS gives the town as Bedford, so they are not linked here."),
 dict(slug="samuel-tufts", name="Samuel Tufts (several men)", dates="See entries", town="Medford; Brookline; others not given", born="", died="", era="The Revolution", line="Undetermined",
  bio="""<p>Many records name a Samuel Tufts, most of them from Medford. Medford itself told its Samuels apart as Samuel, Samuel Jr., and Samuel 3d. Each record appears separately below. Matches with Wild's biographical notes are given only where the details agree closely.</p>""",
  service=Q("TUFTS, SAMUEL, Brookline. Petition dated Camp at Hull, Sept. 17, 1776, signed by said Tufts and others belonging to battalion stationed at Hull, asking for increase and payment of wages; also, Private, Capt. William Warner's co., Col. Josiah Whitney's regt.; service from May 19, 1776, 4 days preceding march, to Nov. 1, 1776, 5 mos. 13 days; &hellip;", MSS+", p. 138", ["mss-v16-p138.jpg"]) +
   Q("TUFTS, SAMUEL, Medford. Private, Capt. Isaac Hall's co., Col. Thomas Gardner's regt., which assembled April 19, 1775; service, 5 days.", MSS+", p. 138", ["mss-v16-p138.jpg"]) +
   Q("TUFTS, SAMUEL (also given SAMUEL, Jr.), Medford. &hellip; Private, Capt. Walton's co.; enlisted Dec. 9, 1776; discharged Dec. 21, 1776; company detached for service at Noddle's Island; also, receipt dated Medford, signed by Joseph Tufts, for wages due his son, said Samuel Tufts, for service at Noddle's Island in Dec., 1776.", MSS+", p. 138", ["mss-v16-p138.jpg"]) +
   Q("TUFTS, SAMUEL, Medford. List of men raised for the 6 months service &hellip; pay roll for 6 months men raised by the town of Medford for service in the Continental Army during 1780; marched to camp July 4, 1780; discharged Dec. 20, 1780; service, 5 mos. 28 days, including travel (220 miles) home.", MSS+", p. 138", ["mss-v16-p138.jpg"]) +
   Q("TUFTS, SAMUEL, Medford (also given Boston). List of men raised to serve in the Continental Army from 1st Middlesex Co. regt., as returned by Lieut. Stephen Hall; residence, Medford; engaged for town of Medford; joined Capt. King's co., Col. Marshall's regt.; term, 3 years; &hellip;", MSS+", p. 138", ["mss-v16-p138.jpg"]) +
   Q("TUFTS, SAMUEL, Jr. Private, Capt. Isaac Hall's co.; service, 4 days; company marched from Medford by order of Gen. Washington at the time of taking Dorchester Heights in March, 1776; &hellip;", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   Q("TUFTS, SAMUEL, 3d, Medford. Private, Capt. Isaac Hall's co., Col. Thomas Gardner's regt., which assembled April 19, 1775; service, 5 days.", MSS+", p. 139", ["mss-v16-p139.jpg"]) +
   '<p class="note">MSS p. 139 also lists a Samuel Tufts in Capt. Benjamin Blaney&rsquo;s co. of guards (1778), in Capt. Nathan Sargeant&rsquo;s co. &ldquo;stationed at Winter Hill&rdquo; (1778&ndash;79), and in Capt. John Metcalf&rsquo;s co. (1783, &ldquo;[See Samuel Twist.]&rdquo;). <a href="'+IMG+'mss-v16-p139.jpg">Page scan</a></p>',
  family=Q("TUFTS, SAMUEL. Private, Walton's Co. at Noddle's Island, 1776; wages paid to his father, Joseph Tufts. Born 1759 or 1760; his mother's name was Hannah; married Martha Upham; died in Westford, 1818 or 1819; occupation, dyer.", WILD+", p. 52 (matches the MSS Noddle's Island entry: father Joseph Tufts)", ["wild-medford-in-revolution-p52.jpg"]) +
   Q("TUFTS, SAMUEL. Enlisted, 1780, for 6 mos.; age 19. Son of Samuel and Hannah (Tufts); born April, 1761; taxed 1781.", WILD+", p. 52", ["wild-medford-in-revolution-p52.jpg"]) +
   Q("TUFTS, SAMUEL, 3D. Private, Lexington alarm; paid money for bounty to men going to N. Y. (Called Jr., 1776.) Born 1752; son of William and Mary (Francis); married Margaret Hodgkins of Ipswich before 1779; died Nov. 20, 1815; gravestone in Salem Street Cemetery.", WILD+", p. 53", ["wild-medford-in-revolution-p53.jpg"]) +
   Q("TUFTS, SAMUEL. Private, Lexington alarm, loaned money to pay bounty July, 1776 (archives). Committee of safety, 1779 (town records). Son of Joseph and Lydia (Francis); born Aug. 16, 1732; married Hannah Tufts; died 1818; aged 86; gravestone, Salem Street Cemetery.", WILD+", p. 52", ["wild-medford-in-revolution-p52.jpg"]),
  unverified="Which Medford Samuel is which across sources. Wild p. 53 says Samuel 3d was &ldquo;Called Jr., 1776,&rdquo; so the MSS &ldquo;Samuel, Jr.&rdquo; and &ldquo;Samuel (also given Samuel, Jr.)&rdquo; entries could belong to different men. They are not merged."),
 dict(slug="barnabas-tufts", name="Barnabas Tufts", dates="[dates not in sources seen]", town="Gloucester", born="", died="", era="The Revolution", line="Undetermined",
  bio="<p>Barnabas Tufts of Gloucester served as a drummer in Col. Wigglesworth's regiment. He was paid travel allowance for the 360-mile journey home from Albany.</p>",
  service=Q("TUFTS, BARNABAS, Gloucester. Drummer, Capt. Nicholas Blasdel's co., Col. Wigglesworth's regt.; pay abstract for travel allowance, etc., from Albany home; 360 miles travel allowed said Tufts; warrant allowed in Council Jan. 21, 1777.", MSS+", p. 131", ["mss-v16-p131.jpg"]),
  family="<p>No family connection has been found in the sources seen.</p>",
  unverified="Birth, death, and parentage are not in the sources seen."),
 dict(slug="caleb-tufts", name="Caleb Tufts", dates="1762 &ndash; 1852 (per Wild; identity with MSS entry unconfirmed)", town="Medford; later Mystic, Conn.", born="1762", died="1852", era="The Revolution", line="Undetermined",
  bio="<p>A Caleb Tufts credited to Medford enlisted in December 1776 to guard stores at and about Boston, and served again in a company of guards in 1779. Wild's Medford list includes a Caleb Tufts born in 1762 who later settled in Mystic, Connecticut.</p>",
  service=Q("TUFTS, CALEB. Private, Capt. Caleb Brooks's co., Col. Dike's regt.; muster roll for Dec., 1776&ndash;Feb., 1777; credited to town of Medford; enlisted Dec. 14, 1776; service guarding stores at and about Boston; regiment raised to serve until March 1, 1777; also, Capt. Nathan Sergant's co. of guards; entered service Feb. 3, 1779; discharged May 7, 1779; service, 3 mos. 3 days; company raised for service under Maj. Gen. Gates at and about Boston.", MSS+", p. 132", ["mss-v16-p132.jpg"]),
  family=Q("TUFTS, CALEB. Served 3 mos., 1776. Taxed in Medford, 1785; son of Samuel and Hannah (Tufts); born Sept. 5, 1762; married, 1787, Rebecca Burrows; settled in Mystic, Conn.; died in Mystic, 1852; occupation, brick-layer and farmer.", WILD+", p. 50", ["wild-medford-in-revolution-p50.jpg"]),
  unverified="That Wild's Caleb (b. 1762) is the man in the MSS entry. Both are tied to Medford, but Wild's &ldquo;3 mos., 1776&rdquo; does not exactly match the MSS dates."),
]


TK = "<em>Tufts Kinsmen</em>, Vol. II"
KIN = {
 "peter-tufts-jr": f"""<p>Vol. II, which covers generations 7 and 8, places Peter Tufts Jr. as <strong>Peter5</strong> in the line &ldquo;from Peter5, Peter4, Peter3, John2, Peter1.&rdquo; It also records the families of four of his sons: Peter6 and Martha (Locke) Tufts, Joel6 and Sarah (Butterfield) Tufts, Thomas6 and Sarah (Barrows) Tufts, and Aaron6 and Mehitable (Pearson) Tufts. All are cross-referenced to Vol. I family 129 (children 129-2, 129-4, 129-6, 129-10). <span class="cite">({TK}, pp. 145, 149, 150, 151)</span></p>
<p>His grandson Peter7 is listed as &ldquo;PETER7 TUFTS, 3rd, leather manufacturer,&rdquo; born 3 Sep. 1798 in Charlestown. <span class="cite">({TK}, p. 145)</span></p>
<p class="note">Identity match: strong. The line and his son Peter6&rsquo;s marriage to Martha Locke agree with Wyman, p. 965. Vol. II does not give Peter5&rsquo;s own birth or death dates; those are in Vol. I, which has not been seen.</p>""",
 "caleb-tufts": f"""<p>Vol. II records the family of Ezekiel6 and Ann C. (Williams) Tufts (Vol. I ref. 111-1), &ldquo;from Caleb5, Samuel4, Joseph3, Jonathan2, Peter1.&rdquo; Their children were born in Groton, New London County, Connecticut, near Mystic. <span class="cite">({TK}, p. 115)</span></p>
<p class="note">Identity match: strong for Wild&rsquo;s Caleb (son of Samuel; settled in Mystic, Conn.). It is still only a <strong>possible match</strong> for the MSS Caleb credited to Medford.</p>""",
 "barnabas-tufts": f"""<p>Vol. II records the family of Richard6 and Rhoda (Goss) Tufts (Vol. I ref. 90-6), &ldquo;from Barnabas5, John4, James3, Jonathan2, Peter1.&rdquo; Their children were born in &ldquo;Gloucester [Rockport]&rdquo; from 1812. <span class="cite">({TK}, p. 77)</span></p>
<p class="note"><strong>Possible match</strong> to the MSS Barnabas Tufts of Gloucester. The town agrees, but Vol. II gives no service record or dates for Barnabas5.</p>""",
 "william-tufts": f"""<p>Vol. II records the family of Nathan6 and Sarah (Trefrey) Tufts (Vol. I ref. 93-1), &ldquo;from William5, William4, James3, Jonathan2, Peter1.&rdquo; Their children were born in Medford, starting with Sarah7, born 9 Apr. 1780. <span class="cite">({TK}, p. 83)</span> Wild (p. 52) names Nathan Jr. of Medford as the son of William and Susanna, married to Sarah Trefrey.</p>
<p class="note"><strong>Possible match</strong> only: William5 lived in Medford, but Vol. II does not say which, if any, of the MSS William entries is his.</p>""",
 "samuel-tufts": f"""<p>Vol. II traces several separate Samuel5 lines. These include &ldquo;Samuel5, William4, James3, Jonathan2, Peter1&rdquo; (p. 96), &ldquo;Samuel5, Joseph4, Joseph3, Jonathan2, Peter1&rdquo; (pp. 107&ndash;111), and &ldquo;Samuel5, Samuel4, Joseph3, Jonathan2, Peter1&rdquo; (p. 114). <span class="cite">({TK})</span></p>
<p class="note"><strong>Possible matches</strong> only. Wild&rsquo;s Samuel 3d was the son of William, his Samuel b. 1732 the son of Joseph, and his Samuel b. 1761 the son of Samuel. These fit the three lines above in parentage, but Vol. II gives no service or dates for any Samuel5. None is attached to a specific MSS entry.</p>""",
}

def profile(p):
    body = f'''<section id="biography"><h2>Biography</h2>{p["bio"]}</section>
{{DIV}}
<section id="service"><h2>Service Record</h2><p><strong>Town:</strong> {p["town"]} &middot; <strong>Dates:</strong> {p["dates"]}</p>{p["service"]}</section>
{{DIV}}
<section id="family"><h2>Family Connection</h2>{p["family"]}</section>
{('<section id="kinsmen"><h2>From <em>Tufts Kinsmen</em></h2>' + KIN[p["slug"]] + '</section>') if p["slug"] in KIN else ''}
<section id="unverified">{UNV(p["unverified"])}</section>
<p><a href="{{P}}people.html">&larr; All people</a> &middot; <a href="{{P}}generations/revolution.html#profiles">The Revolution</a></p>'''
    page(f'profiles/{p["slug"]}.html', f'{p["name"]} | Tufts Family Heritage', "The Revolution &middot; Profile", p["name"], f'{p["dates"]} &middot; {p["town"]}', body)
for p in PROFILES: profile(p)
json.dump([dict(name=p["name"], slug=p["slug"], born=p["born"], died=p["died"], era=p["era"], line=p["line"], town=p["town"], profile=f'profiles/{p["slug"]}.html') for p in PROFILES]
          + [dict(name="Charles Tufts", slug="charles-tufts", born="", died="1876", era="19th Century", line="Undetermined", town="Somerville", profile="generations/19th-century.html#charles-tufts"),
             dict(name="Albert C. Tufts", slug="albert-c-tufts", born="", died="", era="19th Century", line="Undetermined", town="Sacramento, Calif.", profile="generations/19th-century.html#albert-c-tufts"),
             dict(name="Peter Tufts of Winter Hill", slug="peter-tufts-winter-hill", born="1728", died="1791", era="Colonial", line="Peter Tufts of Winter Hill", town="Charlestown (Winter Hill)", profile="generations/colonial.html#peter-1728"),
             dict(name="Anne Adams Tufts", slug="anne-adams-tufts", born="1729", died="1813", era="Colonial", line="Peter Tufts of Winter Hill", town="Charlestown (Winter Hill)", profile="generations/colonial.html#anne-adams"),
             dict(name="Peter Tufts (the immigrant)", slug="peter-tufts-immigrant", born="1617", died="1700", era="Colonial", line="Peter Tufts the immigrant", town="Charlestown / Malden", profile="generations/colonial.html#immigrant")],
          open("data/people.json", "w"), indent=2)

PROF_LIST = "<ul>" + "".join(f'<li><a href="{{P}}profiles/{p["slug"]}.html">{p["name"]}</a> ({p["town"]})</li>' for p in PROFILES) + "</ul>"

page("index.html", "Tufts Family Heritage", "From Colonial New England Onward", "Tufts Family Heritage", "The Tufts Family Across the Generations", '''
<section id="about">
  <h2>The Tufts Family Across the Generations</h2>
  <p>This site follows the Tufts family through the generations, from colonial New England onward. It covers the people, the family lines that connect them to descendants today, the places they lived and worked, and the letters and artifacts they left behind. Every statement is tied to a quoted source and a page scan, and anything not yet proven is marked Unverified.</p>
</section>
<nav class="timeline" aria-label="Timeline">
  <a href="generations/colonial.html"><strong>Colonial</strong>1638&ndash;1765</a>
  <a href="generations/revolution.html"><strong>The Revolution</strong>1765&ndash;1783</a>
  <a href="generations/19th-century.html"><strong>19th Century</strong></a>
  <a href="generations/modern.html"><strong>Modern</strong></a>
</nav>
{DIV}
<section id="featured">
  <h2>Featured Stories</h2>
  <div class="cards">
    <a class="card" href="places.html#winter-hill"><h3>Winter Hill, April 19, 1775</h3><p>&ldquo;Here he was soundly sleeping when Paul Revere came thundering up to the door.&rdquo; Jones, <em>Under Colonial Roofs</em>, p. 129.</p></a>
    <a class="card" href="profiles/peter-tufts-jr.html"><h3>Peter Tufts Jr. of Medford</h3><p>Minute man on the Lexington alarm, Capt. Isaac Hall's company. <em>Mass. Soldiers and Sailors</em>, vol. XVI, p. 137.</p></a>
    <a class="card" href="generations/19th-century.html#charles-tufts"><h3>Charles Tufts and Walnut Hill</h3><p>&ldquo;I will put a light on it.&rdquo; The land that became Tufts College. <em>Tufts Family History</em>, p. 139.</p></a>
    <a class="card" href="generations/colonial.html#anne-adams"><h3>Anne Adams Tufts</h3><p>Nursing the wounded after Bunker Hill, as told in a 1909 newspaper account.</p></a>
  </div>
</section>
{DIV}
<section>
  <h2>Our Standard</h2>
  <p>Every account here is drawn from primary and documented sources. Each book citation shows a page scan or an exact quote with its printed page number. Where a detail cannot yet be verified, we say so. See <a href="sources.html">Sources</a>.</p>
</section>''')

page("generations/colonial.html", "Colonial 1638–1765 | Tufts Family Heritage", "Generations", "Colonial Era", "1638&ndash;1765", f'''
<section id="immigrant"><h2>Peter Tufts the Immigrant</h2>
<p>The Tufts families of Malden, Medford, and Charlestown descend from a Peter Tufts who came from England about 1638.</p>
{Q("Peter Tufts was a descendant in the fourth generation of another Peter who came over from England about 1638. He was the ancestor of the numerous families of the name in Malden, Medford, and Somerville. &hellip; He was born in 1617, probably at or near Malden, England; &hellip; He was made a freeman in 1665. His wife's name was Mary. She died in 1703, aged seventy-five. Peter died in 1700. They had nine children, of whom the third son was John, born in 1665.", JONES+", p. 128", ["jones-under-colonial-roofs-p128.jpg"])}
{UNV("Jones's statement that the immigrant was born &ldquo;probably at or near Malden, England&rdquo; is his own hedge. The English origin is not confirmed by a primary record here.")}
</section>
{{DIV}}
<section id="peter-1728"><h2>Peter Tufts of Winter Hill (1728&ndash;1791)</h2>
{Q("This Peter the third is called &ldquo;of Charlestown,&rdquo; and was born April 24, 1728. He married Anne Adams of Quincy, a relative of President John Adams.", JONES+", p. 129", ["jones-under-colonial-roofs-p129.jpg"])}
{Q("PETER 37. Son of Peter 36; m. ANN ADAMS [18] April 19, 1750, who d. Feb. 7, 1813, &aelig;. 84, g. s. &hellip; d. March 4, 1791, &aelig;. 63, g. s.", WYMAN+", p. 965", ["wyman-v2-p965.jpg"])}
{Q("PETER 36. Son of John 28; housewright; m. LYDIA BUCKNAM, who d. Oct. 31, 1776, in 72d yr., g. s.; d. Dec. 5, 1776, in 80th yr., g. s. Issue.&mdash;i. Nathan, b. May 14, 1724. ii. Peter, April 24, 1728.", WYMAN+", p. 964 (his parents)", ["wyman-v2-p964.jpg"])}
</section>
<section id="anne-adams"><h2>Anne Adams Tufts</h2>
{Q("She was born July 8, 1729, and died February 17, 1813.", JONES+", p. 129", ["jones-under-colonial-roofs-p129.jpg"])}
{Q("Anne Adams Tufts rendered notable service to her country during the Revolutionary War. After the battle of Bunker Hill, she assisted in binding up the wounds of many soldiers who were brought to her house, and later, when part of Burgoyne's army was encamped on Winter Hill, she went to camp and nursed all night the dying wife of one of the prisoners.", TFH+", p. 28, quoting the <em>Boston Journal</em>, June 22, 1909", ["tufts-family-history-p28.jpg"])}
{UNV("Anne's death date: Wyman (p. 965) gives Feb. 7, 1813, and Jones (p. 129) gives February 17, 1813. Her father: Jones says &ldquo;Anne Adams of Quincy&rdquo;, and the family history (p. 28) says &ldquo;the daughter of Joseph Adams of Cambridge&rdquo;. Her nursing service is known only from a 1909 newspaper account quoted in a secondary source.")}
</section>
{{DIV}}
<section><h2>The Winter Hill Farm</h2><p>See <a href="{{P}}places.html#winter-hill">Places: Winter Hill</a>.</p></section>''')

page("generations/revolution.html", "The Revolution 1765–1783 | Tufts Family Heritage", "Generations", "The Revolution", "1765&ndash;1783", f'''
<div class="banner">1776 &ndash; 2026 &middot; The 250th Anniversary of American Independence</div>
<section><h2>The Revolution</h2>
<p>On April 19, 1775, Medford's minute men marched on the alarm. Isaac, John, Daniel, Ebenezer, Jonathan, James, Peter Jr., and several Samuels of the Tufts family served in Capt. Isaac Hall's company (MSS vol. XVI, pp. 132–139). Over the following eight years, men named Tufts from Medford, Woburn, Gloucester, Chelsea, Malden, Cambridge, Brookline, and other towns appear on the rolls.</p>
{Q("The 19th of April, as it chanced, was the silver wedding anniversary of Peter and Anne Tufts, who lived at Winter Hill. Paul Revere's alarm took Peter to the front, his son John, a lad of eighteen, being charged to stay behind and take care of things.", CHASE+", p. 99", ["chase-v3-p99-fullpage.jpg"])}
</section>
{{DIV}}
<section id="profiles"><h2>Revolutionary Profiles</h2>{PROF_LIST}
<p class="note">The Tufts entries in <em>Massachusetts Soldiers and Sailors</em>, vol. XVI, fill pp. 131&ndash;140. Every page is linked here so that men not yet profiled can be read in the original: <a href="{IMG}mss-v16-p131.jpg">131</a> &middot; <a href="{IMG}mss-v16-p132.jpg">132</a> &middot; <a href="{IMG}mss-v16-p133.jpg">133</a> &middot; <a href="{IMG}mss-v16-p134.jpg">134</a> &middot; <a href="{IMG}mss-v16-p135.jpg">135</a> &middot; <a href="{IMG}mss-v16-p136.jpg">136</a> &middot; <a href="{IMG}mss-v16-p137.jpg">137</a> &middot; <a href="{IMG}mss-v16-p138.jpg">138</a> &middot; <a href="{IMG}mss-v16-p139.jpg">139</a> &middot; <a href="{IMG}mss-v16-p140.jpg">140</a>.</p>
</section>
<section id="medford-roster"><h2>The Medford Minute Men Roster</h2>
<blockquote>&ldquo;ROSTER OF THE FIRST COMPANY OF MINUTE MEN WHO ASSEMBLED IN MEDFORD AT THE CALL OF PAUL REVERE AND ENGAGED IN THE BATTLE OF APRIL 19, 1775&rdquo;</blockquote>
<p>The monument, erected by the City of Medford in 1925, lists Tufts Daniel, Tufts Ebenezer, Tufts James Jr., Tufts John Corporal, Tufts Jonathan, Tufts Isaac Sergeant, Tufts Peter Jr., Tufts Samuel, and Tufts Samuel 3d. <a href="{IMG}medford-1925-monument.jpg">View photograph</a></p>
</section>
<p>Related: <a href="{{P}}places.html#winter-hill">Winter Hill</a> &middot; <a href="{{P}}places.html#medford-charlestown">Medford &amp; Charlestown</a></p>''')

page("generations/19th-century.html", "19th Century | Tufts Family Heritage", "Generations", "19th Century", "", f'''
<section id="charles-tufts"><h2>Charles Tufts and Walnut Hill</h2>
<p>Charles Tufts of Somerville gave the hilltop land on which Tufts College was built.</p>
{Q("As early as 1841, Charles Tufts conceived the idea that an Universalist College was needed, and that his Walnut Hill was the appropiate site for it. &hellip; when previously asked by a friend what he intended to do with the wind-swept height, Mr. Tufts replied; &ldquo;I will put a light on it&rdquo;, &mdash;a remark which has become one of the traditions of Tufts University. &hellip; A charter for the new College was issued April 15, 1852, and on July 23, 1853 the corner stone for Ballou Hall, the first building, was laid; and in 1854 was opened to students.", TFH+", p. 139", ["tufts-family-history-p139.jpg"])}
{Q("Mr. Charles Tufts, whose name is better known to the people than almost any other, whose generous acts endeared him to many he had benefacted, is no more. &hellip; He believed in doing good to the greatest number, and hence his noble gift to Tufts College, of the beautiful tract of land upon which the buildings are now located.", TFH+", p. 143, quoting the <em>Somerville Journal</em>, December 30, 1876", ["tufts-family-history-p143.jpg"])}
{UNV("Charles Tufts's birth and death dates and his parentage are not quoted here. The obituary says only &ldquo;nearly ninety-six&rdquo;. These need a primary record such as a gravestone, vital record, or probate file.")}
</section>
{{DIV}}
<section id="weymouth"><h2>The Weymouth Line and Tufts Library</h2>
{Q("The year 1879 was a memorable one for the town of Weymouth. Early that year, through the generosity of Quincy and his sister Miss Susanna Tufts, they gave to the town, by will, a fund for the establishment of a library for the benefit of its citizens.", TFH+", p. 35", ["tufts-family-history-p35.jpg"])}
<p>See also <a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts</a>.</p>
</section>
{{DIV}}
<section id="albert-c-tufts"><h2>Albert C. Tufts of Sacramento</h2>
<p><span class="tag">Research in progress</span></p>
<h3>Sacramento city directories (primary)</h3>
<ul>
<li>1869: no entry found.</li>
<li>1870: &ldquo;Tufts A. C., clerk, with Justin Gates &amp; Bro.&rdquo;</li>
<li>1874: &ldquo;Tufts A. C., apothecary, with J. L. Polhemus, res 282 J&rdquo;</li>
<li>1875: &ldquo;Tufts A. C., apothecary, with Justin Gates &amp; Bro.&rdquo;</li>
<li>1879&ndash;80 and 1880&ndash;81: druggist, SE corner of 10th &amp; J (&ldquo;Tufts A C, druggist, se cor 10th&rdquo;)</li>
<li>1884&ndash;85: &ldquo;TUFTS A C, druggist, SE cor J and Tenth, res 1605&rdquo; [H]</li>
<li>1888&ndash;89: &ldquo;Tufts A C, druggist 1000 J&rdquo;</li>
<li>1894: &ldquo;TUFTS ALBERT C, druggist, 1000 J, r 1605 H&rdquo;</li>
<li>1896: &ldquo;TUFTS ALBERT C., Druggist 1000 J. Telephone 379&rdquo;</li>
<li>1897: &ldquo;Tufts Edith Miss, r 1605 H.&rdquo; (Jessie M. also at 1605 H)</li>
<li>1898: &ldquo;Tufts Albert C, r 1104 I&rdquo;; &ldquo;Tufts Edith Miss, r 1104 I&rdquo;</li>
<li>1899: &ldquo;Tufts A C Mrs, r 1104 I&rdquo;; &ldquo;Tufts Jessie Miss, emp State Print[ing Office]&rdquo;. Albert is not listed.</li>
<li>1902: &ldquo;Tufts Edith Miss, teacher Union Prim School, r 817 18th&rdquo;</li>
</ul>
<p class="note">Quoted from the OCR text of each directory. Printed page numbers have not yet been captured.</p>
<h3>Secondary sources (labeled as such)</h3>
<ul>
<li>Marriage to Eva N. Carriger, c. December 1877, per the title of a Newspapers.com clipping citing <em>The Pacific Bee</em>, Sacramento, Dec. 22, 1877, p. 8. The clipping text has not been seen.</li>
<li>Albert, Edith, Mrs. Eva Nelson Tufts, and Jessie May Tufts listed at St. Paul's Episcopal Church (Sacramento Historic Churches Index, 1852&ndash;1910).</li>
<li>Edith Tufts Shaw, b. 7 Oct. 1878, Sacramento (SSA-derived index).</li>
<li>1884&ndash;85 business directory: proprietor of Meadows' Magic Liniment and Tufts' Yerbine Cough Balsam.</li>
<li>Tufts &amp; Spieker, California Trade Mark No. 404, Yerba Santa Cough Balsam, 1877 (collector blog).</li>
</ul>
{UNV("Albert's absence from the 1899 directory suggests, by inference only, that he died about 1898&ndash;99. No death record has been found. Also unverified: his birthplace, death, burial, any link to the Massachusetts Tufts family, Masonic office, and any bottle-collection accession. The trademark's location (10th &amp; K) conflicts with the directories (10th &amp; J).")}
</section>''')

page("generations/modern.html", "Modern | Tufts Family Heritage", "Generations", "Modern", "", f'''
<section id="tka"><h2>The Tufts Kinsmen Association</h2>
<p>A family association, separate from this site, has carried on Tufts genealogical research since the 1970s. According to its own public website:</p>
<blockquote>&ldquo;The Tufts Kinsmen Association was founded in 1975 by Herbert Freeman Adams (1924-2003) as a way to support his on-going Tufts Kinsmen Project.&rdquo;</blockquote>
<blockquote>&ldquo;members of the Tufts Kinsmen Association who had worked with Herb continued his work and published Tufts Kinsmen, Volumes I and II, in 2010 and 2013.&rdquo;</blockquote>
<p class="cite">Tufts Kinsmen Association, &ldquo;Kinsmen History,&rdquo; <a href="https://tuftskinsmenassociation.org/kinsmen-history/">tuftskinsmenassociation.org/kinsmen-history</a> (accessed Nov. 2, 2026).</p>
<blockquote>&ldquo;Today, we are a small group of Tufts descendants who meet annually and enjoy sharing our family history through the book, Tufts Kinsmen (2010).&rdquo;</blockquote>
<p class="cite">Tufts Kinsmen Association, &ldquo;Mission,&rdquo; <a href="https://tuftskinsmenassociation.org/mission/">tuftskinsmenassociation.org/mission</a> (accessed Nov. 2, 2026).</p>
<p>Its reunion page invites descendants to a September reunion focused on &ldquo;people and events in Medford, greater Boston, and New England.&rdquo; <span class="cite">(<a href="https://tuftskinsmenassociation.org/events-reunion/">Events &amp; Reunion</a>, accessed Nov. 2, 2026)</span></p>
</section>
<section id="newsletter-1979" class="soon"><h2>The 1979 Newsletter<span class="tag">Awaiting material from owner</span></h2><p>A recreation of the 1979 newsletter will be added once the owner supplies it.</p></section>''')

page("people.html", "People | Tufts Family Heritage", "A&ndash;Z Index", "People", "Searchable index of family members", '''
<section>
  <h2>People A&ndash;Z</h2>
  <div class="filters">
    <label>Search <input id="q" type="search" placeholder="Name"></label>
    <label>Era <select id="era"><option value="">All eras</option></select></label>
    <label>Line <select id="line"><option value="">All lines</option></select></label>
  </div>
  <div id="people-list"><p class="note">Loading&hellip;</p></div>
  <p class="note">&ldquo;Several men&rdquo; pages group records that share a name. Different men are never merged.</p>
</section>''')

page("places.html", "Places | Tufts Family Heritage", "Places", "Places", "Where the family lived and worked", f'''
<section id="winter-hill"><h2>Winter Hill</h2>
{Q("At the outbreak of the Revolution, Peter Tufts lived at the top of Winter Hill in a little old house, which stood until a few years ago. Here he was soundly sleeping when Paul Revere came thundering up to the door, calling on the people to rouse and arm themselves, for the Regulars were coming.", JONES+", p. 129", ["jones-under-colonial-roofs-p129.jpg"])}
{Q("The tablet rests upon the historic door stone of the Anne Adams Tufts homestead and was recently presented to the chapter.", TFH+", p. 28, quoting the <em>Boston Journal</em>, June 22, 1909, on the tablet unveiled in Paul Revere Park, Winter Hill, Somerville", ["tufts-family-history-p28.jpg"])}
</section>
{{DIV}}
<section id="medford-charlestown"><h2>Medford &amp; Charlestown</h2>
{Q("Lived in house occupied at one time by his cousin Daniel, opposite Powder House; through his influence his homestead lot was set off to Charlestown in 1811.", WILD+", p. 52 (Peter Tufts Jr.)", ["wild-medford-in-revolution-p52.jpg"])}
{Q("lived near Powder House, Somerville; land where his house stood set off from Medford to Charlestown, 1811.", WILD+", p. 50 (Daniel Tufts)", ["wild-medford-in-revolution-p50.jpg"])}
</section>
{{DIV}}
<section id="later-homes"><h2>Later Homes</h2>
<ul><li>Weymouth, Mass.: Dr. Cotton Tufts and the Tufts Library (<a href="{{P}}generations/19th-century.html#weymouth">19th Century</a>)</li>
<li>Walnut Hill, Somerville and Medford: Charles Tufts's gift for Tufts College (<a href="{{P}}generations/19th-century.html#charles-tufts">19th Century</a>)</li>
<li>Mystic, Conn.: Caleb Tufts, per Wild p. 50 (<a href="{{P}}profiles/caleb-tufts.html">profile</a>)</li>
<li>Sacramento, Calif.: Albert C. Tufts, druggist (<a href="{{P}}generations/19th-century.html#albert-c-tufts">19th Century</a>)</li></ul>
</section>''')

page("collections.html", "Collections | Tufts Family Heritage", "Collections", "Collections", "Letters, artifacts, and photographs", f'''
<section id="photographs"><h2>Photographs</h2>
<div class="cards"><a class="card" href="{IMG}medford-1925-monument.jpg"><img src="{IMG}medford-1925-monument.jpg" alt="Medford 1925 Minute Men monument" loading="lazy"><h3>Medford Minute Men Monument (1925)</h3><p>Roster of the First Company of Minute Men, April 19, 1775, including nine men named Tufts.</p></a></div>
<p>All page scans: <a href="{{P}}sources.html#scans">Sources: Page Scans</a>.</p>
</section>
{{DIV}}
<section id="artifacts"><h2>Artifacts</h2>
{Q("One heirloom of the family, a tankard (now belonging to the First Congregational Society of Quincy, Mass.), made by John Edwards, was the gift of Elizabeth Quincy to her daughter, Lucy (Quincy) Tufts, who married Dr. Cotton Tufts in 1755.", TFH+", p. 35", ["tufts-family-history-p35.jpg"])}
{UNV("The tankard's present location is reported from 1963. No photograph is held.")}
<p class="soon">Family artifacts <span class="tag">Awaiting material from owner</span></p>
</section>
{{DIV}}
<section id="letters" class="soon"><h2>Letters<span class="tag">Awaiting material from owner</span></h2><p>Transcribed family letters, with images of the originals, will be added as the owner supplies them.</p></section>''')

page("sources.html", "Sources | Tufts Family Heritage", "Sources", "Sources", "Bibliography, page scans, and research notes", f'''
<section id="bibliography"><h2>Bibliography</h2>
<ul>
<li>{MSS}, pp. 131&ndash;140 (all Tufts entries). <a href="https://archive.org/details/massachusettssol16mass">archive.org</a></li>
<li>{WYMAN}, pp. 964&ndash;965. <a href="https://archive.org/details/genealogiesestat02wyma">archive.org</a></li>
<li>{JONES}, pp. 128&ndash;129. <a href="https://archive.org/details/undercolonialroo00jone">archive.org</a></li>
<li>{WILD}, pp. 50, 52, 53. <a href="https://archive.org/details/medfordinrevolut00wild">archive.org</a></li>
<li>{CHASE}, p. 99. <a href="https://archive.org/details/beginningsofamer03chas">archive.org</a></li>
<li>{TFH}, pp. 28, 35, 37, 139, 143. <a href="https://archive.org/details/tuftsfamilyhisto00tuft_0">archive.org</a></li>
<li>Sacramento city directories, 1869&ndash;1902 (Albert C. Tufts).</li>
<li>City of Medford, Minute Men monument (1925), photograph.</li>
<li>Herbert Freeman Adams, comp., <em>Tufts Kinsmen</em>, Vol. II (Tufts Kinsmen Association, 2012; &copy; 2003), pp. 77, 83, 96, 107&ndash;115, 145&ndash;151. Private copy; cited with short quotes only, no scans. Vol. I <strong>not seen</strong>.</li>
<li>DAR records. <strong>Not seen; missing images.</strong></li>
</ul></section>
{{DIV}}
<section id="scans"><h2>Page Scans</h2><div id="scan-list" class="cards"></div></section>
{{DIV}}
<section id="notes"><h2>Research Notes</h2>
{UNV("Peter Tufts Jr.'s death year: 1836 (Wild p. 52) or 1832 (secondhand DAR listing).")}
{UNV("Anne Adams Tufts's death date (Feb. 7 or Feb. 17, 1813) and her father (Quincy or Cambridge).")}
{UNV("The <em>Tufts Kinsmen</em> p. 50 claim is known only secondhand. It is probably in Vol. I, which has not been seen.")}
<p>Full quote table: <a href="sources/README.md">sources/README.md</a></p>
</section>''')
