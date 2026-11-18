# Nov 18, 2026: findings from public-domain town histories, county histories, vital records and
# the Massachusetts Magazine. Items that turn on identity or date questions are not included yet.
def _IA(i): return f'<a href="https://archive.org/details/{i}">Internet Archive</a>'
def _C(auth, title, year, pg, ia, pp="p."):
    return f'{auth}, <em>{title}</em> ({year}), {pp} {pg}. {_IA(ia)}'
ARL = lambda pg, pp="p.": _C("Benjamin and William R. Cutter", "History of the Town of Arlington, Massachusetts", 1880, pg, "historyoftownofa00cut", pp)
MEL = lambda pg, pp="p.": _C("Elbridge Henry Goss", "The History of Melrose, County of Middlesex, Massachusetts", 1902, pg, "historyofmelrose00goss", pp)
LEX = lambda pg, pp="p.": _C("Charles Hudson", "History of the Town of Lexington, Middlesex County, Massachusetts", 1868, pg, "historyoftownofl00huds", pp)
FRO = lambda pg, pp="p.": _C("Richard Frothingham Jr.", "The History of Charlestown, Massachusetts", 1845, pg, "historyofcharles1845frot", pp)
BAR = lambda pg, pp="p.": _C("Josiah Bartlett", "An Historical Sketch of Charlestown, in the County of Middlesex", 1814, pg, "historicalsketch00bart", pp)
SUF = lambda pg, pp="p.": _C("Davis (ed.)", "Professional and Industrial History of Suffolk County, Massachusetts", "1894", pg, "professionalindu02davi_0", pp).replace("<em>Professional and Industrial History of Suffolk County, Massachusetts</em>", "<em>Professional and Industrial History of Suffolk County, Massachusetts</em>, vol. 2")
COL = lambda pg: _C("Mary Caroline Crawford [as published]", "Colonial Massachusetts", 1899, pg, "colonialmassachu00dawe")
MM5 = lambda pg: f'<em>The Massachusetts Magazine</em>, vol. 5 (1912), p. {pg}. {_IA("massachusettsmagv5sale")}'
MM6 = lambda pg: f'<em>The Massachusetts Magazine</em>, vol. 6 (1913), p. {pg}. {_IA("massachusettsmagv6sale")}'
ESX = lambda pg: _C("D. Hamilton Hurd [as published]", "Standard History of Essex County, Massachusetts", 1878, pg, "standardhistoryo00trac")
WES = lambda pg: _C("Daniel S. Lamson", "History of the Town of Weston, Massachusetts, 1630&ndash;1890", 1913, pg, "historyoftownofw00lams")
MX3 = lambda pg: _C("D. Hamilton Hurd", "History of Middlesex County, Massachusetts", "1890", pg, "historyofmiddles00hurd3").replace("Massachusetts</em>", "Massachusetts</em>, vol. 3", 1)
CHV = lambda pg: f'<em>Vital Records of Chelsea, Massachusetts, to the Year 1850</em> (1916), p. {pg}. {_IA("vitalrecordsofch00chels")}'
WYV = lambda pg: f'<em>Vital Records of Weymouth, Massachusetts, to the Year 1850</em>, vol. 1 (1910), p. {pg}. {_IA("vitalrecordsofwe01weym")}'
LYN = lambda pg: _C("Alonzo Lewis and James R. Newhall", "History of Lynn, Essex County, Massachusetts", 1890, pg, "historyoflynness00newh", "pp.")
TRV = lambda pg: f'<em>Two Centuries of Travel in Essex County, Massachusetts</em> (1921), p. {pg}, from the diary of John Adams. {_IA("twocenturiesoftr00dow")}'
DRW = lambda n: f'Benjamin Drew, <em>Burial Hill, Plymouth, Massachusetts: Its Monuments and Gravestones Numbered and Briefly Described</em> (1894), {n}. {_IA("burialhillplymou00drew")}'
DWO = lambda pg: f'Franklin P. Rice, <em>Dictionary of Worcester (Massachusetts) and Its Vicinity</em> (1893), p. {pg}. {_IA("dictionaryofworc1893rice")}'
# Fix author lines where the title page was not read: give the title only.
COL = lambda pg: f'<em>Colonial Massachusetts</em> (1899), p. {pg}. {_IA("colonialmassachu00dawe")}'
ESX = lambda pg: f'<em>Standard History of Essex County, Massachusetts</em> (1878), p. {pg}. {_IA("standardhistoryo00trac")}'
SUF = lambda pg, pp="p.": f'<em>Professional and Industrial History of Suffolk County, Massachusetts</em>, vol. 2 (1894), {pp} {pg}. {_IA("professionalindu02davi_0")}'
MX3 = lambda pg: f'<em>History of Middlesex County, Massachusetts</em>, ed. D. Hamilton Hurd, vol. 3 (1890), p. {pg}. {_IA("historyofmiddles00hurd3")}'
WES = lambda pg: f'<em>History of the Town of Weston, Massachusetts, 1630&ndash;1890</em> (1913), p. {pg}. {_IA("historyoftownofw00lams")}'
LYN = lambda pg: f'<em>History of Lynn, Essex County, Massachusetts</em> (1890), pp. {pg}. {_IA("historyoflynness00newh")}'
MEL = lambda pg, pp="p.": f'Elbridge Henry Goss, <em>The History of Melrose, County of Middlesex, Massachusetts</em> (1902), {pp} {pg}. {_IA("historyofmelrose00goss")}'
OCRN = '<span class="note">(Scanned text; obvious scanning errors corrected.)</span>'

def _nf_add_bio(slug, html):
    for _p in PROFILES:
        if _p["slug"] == slug:
            _p["bio"] = _p["bio"] + html
            return True
    NF_EXTRA.setdefault(f"profiles/{slug}.html", []).append(html)
    return False
NF_EXTRA = {}
def _nf_rel(a, b, la, lb):
    REL.setdefault(a, []); REL.setdefault(b, [])
    if b not in [s for s, _ in REL[a]]: REL[a] = REL[a] + [(b, la)]
    if a not in [s for s, _ in REL[b]]: REL[b] = REL[b] + [(a, lb)]

# ---------- Image: Peter Tufts Jr.'s Plan of Malden, 1795 ----------
_MAL = "plan-of-malden-1795-peter-tufts-jr.jpg"
IMAGES[_MAL] = ("Plan of Malden, surveyed by Peter Tufts Jr., 1795",
  "&ldquo;The Plan of Malden, Contains 8826 Acres including Water and Roads, Survey&rsquo;d AD 1795 By Peter Tufts jun.&rdquo; Reproduced, reduced, in Goss&rsquo;s <em>History of Melrose</em> (1902), facing p. 50, by permission of Deloraine P. Corey. It shows the Malden River, Ell Pond, Spot Pond&rsquo;s neighbourhood, the Reading, Salem, Medford, Charlestown and Chelsea roads, and the town lines with Medford, Stoneham and Chelsea.",
  "Elbridge Henry Goss, <em>The History of Melrose</em> (1902)", "Public domain", "https://archive.org/details/historyofmelrose00goss", "Internet Archive")
if _MAL not in CREDITS:
    CREDITS = CREDITS.replace("</ul></section>", f'<li><a href="{{P}}assets/images/{_MAL}">{IMAGES[_MAL][0]}</a>. {IMAGES[_MAL][2]}. {IMAGES[_MAL][3]}. <a href="{IMAGES[_MAL][4]}">Internet Archive page</a></li></ul></section>', 1)

_nf_add_bio("peter-tufts-1774",
  '{DIV}<section id="plans-1795-1803"><h2>His Plans of Malden (1795) and West Cambridge (1803)</h2>'
  + '<p>In 1794 the General Court ordered every town to have an accurate plan of its bounds taken. Malden&rsquo;s was surveyed in 1795 by &ldquo;Peter Tufts, Jr., of Medford.&rdquo; The Melrose historian Elbridge Goss used it to show which roads then existed in North Malden, now Melrose:</p>'
  + Q("On a plan of Malden, surveyed by Peter Tufts, Jr., of Medford, in 1795, by authority of a resolve passed by the General Court in 1794, the only roads laid down in what was then North Malden, are, the main road as last described, called the &ldquo;Reading Road,&rdquo; now Main Street, and the &ldquo;Stoneham Road&rdquo;", MEL(47) + " " + OCRN)
  + FIG(_MAL, "hfig-flow mi-inline")
  + '<p>Eight years later a &ldquo;plan by Peter Tufts, Jr., dated 1803&rdquo; recorded mill land along the brook in West Cambridge, now Arlington (' + ARL(17) + '). The Arlington register, describing his marriage to Martha Locke, adds a one-line judgment of his work:</p>'
  + Q("&ldquo;Peter Tufts, Jr., Esq.,&rdquo; was an eminent surveyor.", ARL(311))
  + UNV("<strong>Which Peter Tufts Jr. drew the 1795 plan.</strong> In 1803 &ldquo;Peter Tufts, Jr.&rdquo; can only be the surveyor (1774&ndash;1825), and the Arlington register calls him &ldquo;Peter, Jr., of Medford (s. of Peter, 3d).&rdquo; By 1795 his father had already become plain &ldquo;Peter&rdquo; on the death of the elder Peter of Winter Hill in 1791, so the 1795 plan is probably also the surveyor&rsquo;s work, but no source seen states it outright. Note: Pending further work.")
  + '</section>')

# ---------- Peter Tufts the immigrant: 1660 slander case; 1663 Ell Pond sale ----------
_nf_add_bio("peter-tufts-1617",
  '{DIV}<section id="court-1660"><h2>A Household in Court, 1660, and the Ell Pond Farm, 1663</h2>'
  + '<p>The Middlesex court records preserve a glimpse of the immigrant&rsquo;s household. In 1660 James Barrett and William Luddington sued Mary Tufts, Peter&rsquo;s wife, for slander. The quarrel began, Goss explains, when Peter&rsquo;s servant came to them with a complaint:</p>'
  + Q("It appears by the evidence, that Peter Tufts of Malden, had beaten and abused his man Henry Swillaway, who went to Barrett and Luddington and told his tale and cried.", MEL(100) + " " + OCRN)
  + '<p>When the two men gave evidence for Swillaway, Mary said that none spoke against her husband at court &ldquo;but the Skines of the Country, and liars, and them that did not care what they said.&rdquo; The jury found for the plaintiffs, with damages, and ordered her to make a public acknowledgment before the Malden congregation on a Sunday afternoon, beginning: &ldquo;That whereas I Mary Tufts am legally convicted of slandering &amp; wronging James Barrat &amp; William Luddington&rdquo; (Goss, citing Middlesex Court Records, vol. i, p. 200; ' + MEL(100) + ').</p>'
  + '<p>Three years later he parted with land at the heart of what became Melrose:</p>'
  + Q("Peter Tufts, who seems to have been a land speculator, owning large tracts of land in this region, sold, in 1663, to Samuel Howard, then of Charlestown, his farm land, which was situated in what is now the centre of Melrose.", MEL(118) + ", citing Middlesex Deeds, book 3, p. 276 (the farm lay at Ell Pond)")
  + '</section>')

# ---------- Peter Tufts of Winter Hill: Charlestown selectman, 1771-1775 ----------
_nf_add_bio("peter-tufts-winter-hill",
  '{DIV}<section id="selectman-1771"><h2>Charlestown Selectman on the Eve of the Revolution</h2>'
  + '<p>Frothingham&rsquo;s <em>History of Charlestown</em> lists &ldquo;Peter Tufts, Jr.&rdquo; among the town&rsquo;s selectmen in each year from 1771 through 1775 (' + FRO("284&ndash;285, 308", "pp.") + '). In 1774, when the Boston Port Bill closed Boston harbor, Charlestown raised gifts for the relief of Boston, and he served on the town&rsquo;s committee on donations:</p>'
  + Q("The committee on donations consisted of Nathaniel Gorham, Nathaniel Frothingham, Nehemiah Rand, Peter Tufts, Jun., John Stanton, Stephen Miller, James Gardner &hellip;", FRO(310) + " " + OCRN)
  + UNV("<strong>Identity.</strong> Frothingham writes &ldquo;Peter Tufts, Jr.&rdquo; without dates. In the 1770s the elder Peter of Charlestown (1697&ndash;1776) was still living, so &ldquo;Jr.&rdquo; most likely means his son, Peter of Winter Hill (1728&ndash;1791). This is an inference from the dates, not a statement in the source. Note: Pending further work.")
  + '</section>')

# ---------- Thomas Tufts of Lexington ----------
_nf_add_bio("thomas-tufts-1766",
  '{DIV}<section id="lexington-selectman"><h2>Selectman of Lexington</h2>'
  + '<p>Hudson&rsquo;s <em>History of Lexington</em> records that Thomas Tufts served the town as selectman in 1799 and 1800:</p>'
  + Q("Thomas Tufts, b. May 18, 1766, m. Nov. 29, 1791, Rebecca Adams of Lincoln, b. Feb. 28, 1767. He d. June 10, 1830, aged 64. She d. Feb. 20, 1858, aged 91. He was selectman, 1799 and 1800.", LEX(247) + "; the selectmen list on p. 404 gives &ldquo;Thomas Tufts, 1799, 1800.&rdquo;")
  + '<p>The family place gave its name to a landmark on the road to Lincoln: Weston Street ran &ldquo;to Lincoln line, passing near the Tufts Place&rdquo; (' + LEX(444) + ').</p>'
  + '<p>Hudson adds that their son Marshall, born September 26, 1802, graduated from Harvard College in 1827 and studied theology with Dr. Holmes of Cambridge. &ldquo;He wrote and published several small volumes, one of which was, &lsquo;The Shores of Vespucci,&rsquo; a romance&rdquo; (' + LEX(247) + ').</p>'
  + '</section>')

# ---------- Deacon Amos Tufts; Peter Tufts (b. 1753): Charlestown offices, 1813-1814 ----------
_nf_add_bio("amos-tufts-1762",
  '{DIV}<section id="charlestown-1814"><h2>Deacon and Selectman, 1813&ndash;1814</h2>'
  + '<p>Josiah Bartlett&rsquo;s address at the opening of Washington Hall in November 1813, printed the next year, names him among the officers of the church and the town:</p>'
  + Q("The present deacons of the church are James Frothingham, Thomas Miller, and Amos Tufts.", BAR(11))
  + Q("Elected 1814. Selectmen, David Goodwin, John Soley, and Jeremiah Evarts, Esq&rsquo;rs. Deac. Amos Tufts, Messrs. Samuel Payson, Peter Tufts, and Joseph Tufts.", BAR(16) + " " + OCRN)
  + '</section>')
_nf_add_bio("peter-tufts-jr",
  '{DIV}<section id="charlestown-1814"><h2>Charlestown Selectman, 1814</h2>'
  + '<p>Bartlett&rsquo;s <em>Historical Sketch of Charlestown</em> lists a &ldquo;Peter Tufts&rdquo; among the selectmen elected in 1814, with ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + ' and a Joseph Tufts (' + BAR(16) + '). This agrees with his service as a Charlestown selectman from 1806 to 1817 given elsewhere on this page.</p></section>')

# ---------- Dr. Simon Tufts (1727-1786): John Adams's visits, 1766 ----------
_nf_add_bio("simon-tufts-11-1",
  '{DIV}<section id="adams-1766"><h2>John Adams at Dr. Tufts&rsquo;s, 1766</h2>'
  + '<p>John Adams, riding between Braintree and Salem, twice stopped at the doctor&rsquo;s house in Medford in 1766. His diary entry for Tuesday, August 12:</p>'
  + Q("Set out with my wife for Salem; dined at Boston; drank tea at Dr. Simeon Tuft&rsquo;s at Medford; lodged at Mr. Bishop&rsquo;s.", TRV(87))
  + '<p>In a later entry he wrote, &ldquo;We dined &hellip; at Dr. Tuft&rsquo;s in Medford&rdquo; (' + TRV(90) + '). The elder Dr. Simon Tufts had died in 1747, so the host was this Dr. Simon, brother of Adams&rsquo;s friend and kinsman by marriage ' + PL("cotton-tufts", "Dr. Cotton Tufts") + '.</p></section>')

# ---------- Banks ----------
_nf_add_bio("nathan-tufts-1764",
  '{DIV}<section id="bunker-hill-bank"><h2>Director of the Bunker Hill Bank, 1825&ndash;1830</h2>'
  + '<p>The Bunker Hill Bank of Charlestown elected its first board of directors on July 27, 1825, and Nathan Tufts was one of them (' + SUF(271) + '). The bank&rsquo;s list of past and present directors gives his term as July 27, 1825, to 1830 (' + SUF(273) + '). See also <a href="{P}businesses.html#banks">Banks and savings institutions</a>.</p></section>')
_nf_add_bio("gilbert-tufts-1778",
  '{DIV}<section id="bunker-hill-bank"><h2>Director of the Bunker Hill Bank, 1831&ndash;1848</h2>'
  + '<p>Gilbert Tufts followed his uncle ' + PL("nathan-tufts-1764", "Nathan Tufts") + ' onto the board of the Bunker Hill Bank in Charlestown. The bank&rsquo;s list of directors shows him elected in 1831 and retiring in 1848 (' + SUF(273) + '). See also <a href="{P}businesses.html#banks">Banks and savings institutions</a>.</p></section>')
_nf_add_bio("joseph-f-tufts-1790",
  '{DIV}<section id="warren-treasurer"><h2>Treasurer of the Warren Institution for Savings</h2>'
  + '<p>The Suffolk County history gives the years of his treasurership: Henry L. Jacques &ldquo;was succeeded by Joseph F. Tufts, who held the office in 1851, &rsquo;52, &rsquo;53 and &rsquo;54&rdquo; (' + SUF(412) + '). The same page records that &ldquo;In 1865 George F. Tufts was elected treasurer, and he still occupies that position&rdquo; in 1894.</p>'
  + UNV("That the George F. Tufts elected treasurer in 1865 is this man&rsquo;s son " + PL("george-f-tufts-1825", "George F. Tufts") + " fits Sawyer&rsquo;s remark that the treasurer of his day was Joseph F. Tufts&rsquo;s son, but neither source joins the two statements. Note: Pending further work.")
  + '</section>')
_nf_add_bio("george-f-tufts-1825",
  '{DIV}<section id="warren-treasurer"><h2>The Warren Institution for Savings</h2>'
  + '<p>A George F. Tufts held office in the Warren Institution for Savings of Charlestown: secretary for one year, 1864&ndash;65, and then treasurer from 1865, &ldquo;and he still occupies that position&rdquo; in 1894 (' + SUF(412) + '). His father ' + PL("joseph-f-tufts-1790", "Joseph F. Tufts") + ' had been treasurer from 1851 to 1854.</p>'
  + UNV("The Suffolk history does not give this George F. Tufts&rsquo;s dates or parents; the match with Joseph F. Tufts&rsquo;s son rests on Sawyer&rsquo;s remark that the treasurer was his son. Note: Pending further work.")
  + '</section>')

# ---------- Andrew Tufts and the Worcester tanyard ----------
_nf_add_bio("andrew-tufts-43-3",
  '{DIV}<section id="worcester-tanyard"><h2>The Worcester Tanyard, 1800</h2>'
  + Q("In 1789, Palmer and Daniel Goulding owned the Tanyard in Worcester. In 1800 it was in the hands of Andrew Tufts, and later owners were Samuel Johnson, Thomas Stearns, Asa Wilder &amp; Co., Nymphas Pratt and Ebenezer H. Bowen.", DWO(57) + " " + OCRN)
  + UNV("The <em>Dictionary</em> gives no further detail about this Andrew Tufts. That he is the Andrew Tufts of this page, who died at Worcester, is likely but not stated. Note: Pending further work.")
  + '</section>')

# ---------- Dr. Cotton Tufts's diaries ----------
_nf_add_bio("cotton-tufts",
  '{DIV}<section id="diaries"><h2>His Diaries</h2>'
  + '<p>Dr. Tufts kept diaries. When the Weymouth vital records were compiled for publication in 1910, the editors drew entries from them and noted where they then were:</p>'
  + Q("P.R.19. &mdash; private record, from diaries of Dr. Cotton Tufts, now in the possession of Hon. Charles Francis Adams of South Lincoln", WYV(7))
  + '<p>Records marked &ldquo;P.R.19&rdquo; in the Weymouth volumes come from these diaries.</p></section>')

# ---------- Timothy Tufts: marriage date ----------
_tm = '<p>The Arlington register supplies the date of the marriage: Anna, daughter of Deacon Joseph Adams of Menotomy, born December 14, 1740, &ldquo;m. Timothy Tufts of Medford 7 (19) May, 1761 (d. 8 Oct. 1825)&rdquo; (' + ARL(185) + '). The two dates are the Old Style and New Style forms of the same day.</p>'
SP["timothy-tufts"] = SP.get("timothy-tufts", "") + _tm

# ---------- Lieut. Francis Tufts: orderly book, 1782 ----------
_OB = ('<p>A manuscript list in <em>The Massachusetts Magazine</em> records an &ldquo;Orderly book of Lieut. and Adjutant Francis Tufts, 8th Mass. regt. Jan. 10&ndash;Apr. 8, 1782&rdquo; (' + MM5(13) + '). An orderly book was the daily register of a regiment&rsquo;s general and regimental orders, kept by its adjutant.</p>')
_nf_add_bio("francis-tufts-41-4", '{DIV}<section id="orderly-book"><h2>His Orderly Book, 1782</h2>' + _OB
  + UNV("The list gives no dates for Francis Tufts. That he is the Francis Tufts of this page, who rose to adjutant in Col. Jackson&rsquo;s regiment (the 8th Massachusetts), is likely but not stated. Where the orderly book is held today has not been traced. Note: Pending further work.") + '</section>')

# ---------- Adam Tufts: Col. Ebenezer Francis; Chelsea record of 1749 ----------
_nf_add_bio("adam-tufts",
  '{DIV}<section id="francis-tufts-mother"><h2>Colonel Francis&rsquo;s Tufts Mother</h2>'
  + '<p>The colonel of Adam Tufts&rsquo;s 1777 regiment was himself of Tufts descent on his mother&rsquo;s side:</p>'
  + Q("Captain Ebenezer Francis of Beverly was the son of Ebenezer and Rachel (Tufts) Francis, and was born in Medford, December 22, 1743.", MM6(158))
  + '<p>See ' + PL("rachel-tufts-francis", "Rachel (Tufts) Francis") + '.</p></section>'
  + '{DIV}<section id="chelsea-1749"><h2>A Chelsea Record of 1749</h2>'
  + '<p>The Chelsea vital records include a marriage intention of two servants in 1749:</p>'
  + Q("Adam, servant to Stephen Tufts of Malden, and Priscilla, servant to Samuel Floyd, int. Nov. 29, 1749.", CHV(440) + ', printed among the marriages of persons with surnames not given')
  + UNV("Whether this Adam is the Adam Tufts of this page is not established; no source seen connects them. In Massachusetts records of the 1740s, &ldquo;servant&rdquo; was often used for an enslaved person, and the next entry on the same page records &ldquo;Bathsheba, slave to Capt. Watts.&rdquo; The record does not state Adam&rsquo;s status. Note: Pending further work.")
  + '</section>')

# ---------- New profile: Rachel (Tufts) Francis ----------
_RF = "rachel-tufts-francis"
PROFILES.append(dict(slug=_RF, name="Rachel (Tufts) Francis", dates="[dates not in sources seen]", town="Medford, Mass.", born="", died="", era="Colonial",
  line="Mother of Col. Ebenezer Francis (1743&ndash;1777), killed at Hubbardton",
  bio=('<p>Rachel Tufts married Ebenezer Francis, and their son Ebenezer was born in Medford on December 22, 1743. <em>The Massachusetts Magazine</em> traced the son&rsquo;s career: he lived in Medford until he came of age and then moved to Beverly; he marched as a lieutenant on the Lexington alarm, became a captain in Col. John Mansfield&rsquo;s regiment, was commissioned colonel on July 28, 1776, and on January 1, 1777, became colonel of the 11th Regiment of the Massachusetts Line. He marched to Ticonderoga and was killed at Hubbardton on Monday, July 7, 1777. His regiment included ' + PL("adam-tufts", "Adam Tufts") + '.</p>'
    + Q("Captain Ebenezer Francis of Beverly was the son of Ebenezer and Rachel (Tufts) Francis, and was born in Medford, December 22, 1743.", MM6(158))
    + '<p>The same sketch, drawing on Usher&rsquo;s <em>History of Medford</em> (pp. 179&ndash;180), tells how officers of Burgoyne&rsquo;s army, quartered near Medford as prisoners, met the colonel&rsquo;s widowed mother. Several told her they had seen her son after he was dead, and one of them, Captain Ferguson, gave back to her the colonel&rsquo;s watch, which he had bought from a drum-boy. &ldquo;Her profound gratitude and great grief deeply impressed them all&rdquo; (' + MM6(158) + ').</p>'),
  service='<p>No service record applies to her. Her son&rsquo;s service is summarised above.</p>',
  family='<p>Husband: Ebenezer Francis, who had died by 1777 (the sketch calls her &ldquo;widowed&rdquo;). Son: Col. Ebenezer Francis (1743&ndash;1777) of Beverly (' + MM6(158) + '). Her own parents are not named in the source.</p>',
  unverified='<strong>Her parents and her dates of birth, marriage and death</strong> are not given in the source seen. The meeting with the British officers is told at second hand from Usher&rsquo;s <em>History of Medford</em>, which has not yet been read for this page. Note: Pending further work.'))
SP[_RF] = "<ul><li><strong>Ebenezer Francis</strong>, father of Col. Ebenezer Francis. Marriage date not found.</li></ul>"
NEWUNCHK.add(_RF)
_nf_rel(_RF, "adam-tufts", "Adam Tufts, who served in her son&rsquo;s regiment", "Rachel (Tufts) Francis, mother of his colonel")

# ---------- New profile: John Tufts, tavern keeper and mill owner of West Cambridge ----------
_JT = "john-tufts-1776"
PROFILES.append(dict(slug=_JT, name="John Tufts of West Cambridge (1776&ndash;1817)", dates="11 July 1776&ndash;15 or 16 August 1817", town="Medford; West Cambridge (now Arlington), Mass.", born="1776", died="1817", era="19th Century",
  line="Son of Jonathan and Elizabeth (Holden) Tufts; tavern keeper and owner of the &ldquo;Tufts mills&rdquo; in West Cambridge",
  bio=('<p>John Tufts was born in Medford on July 11, 1776, a son of ' + PL("jonathan-tufts-36-8", "Jonathan Tufts") + ' and Elizabeth (Holden) Tufts (<em>Tufts Kinsmen</em>, Vol.&nbsp;I, p. 161, no. 85-7). He kept a tavern in West Cambridge, the town that is now Arlington, and for nine years owned a wool factory on the brook there. The tavern stood near the old Baptist meeting-house. The Arlington history notes that the old Cutler&rsquo;s Tavern was &ldquo;afterward Tufts&rsquo;s Tavern,&rdquo; and was still standing in 1880 (' + ARL(212) + ').</p>'
    + '<p>In 1804, when West Cambridge built a new meeting-house, the old one was sold at auction in parts: &ldquo;the tower to John Tufts, for $115&rdquo; (' + ARL(110) + '). The town also chose him clerk of the market (' + ARL(121) + ').</p>'
    + '<p>In 1808 he bought the wool-factory of Abner Stearns:</p>'
    + Q("In 1805 Abner Stearns, of Billerica, bought land here of Ephraim Cooke, victualler, which Stearns, in 1808, sold to John Tufts, with a wool-factory thereon and machinery &hellip; Tufts sold these premises to Ezra Trull, of Boston, in 1817, with a mill thereon, and a raceway through land of heirs of Edward Blackington.", ARL(18) + " " + OCRN)
    + '<p>The works kept his name long after he sold them. A lane &ldquo;led to the mills formerly known as the &lsquo;Tufts mills,&rsquo;&rdquo; which burned about 1831; when Trull sold the site that year the deed described it as the place &ldquo;where the mills formerly known by the name of the Tufts mills stood, previous to the fire which destroyed said mills&rdquo; (' + ARL(18) + '). See <a href="{P}businesses.html#tufts-mills-west-cambridge">The Tufts Mills, West Cambridge</a>.</p>'
    + '<p>His tavern was the centre of the town&rsquo;s celebrations. The Fourth of July in 1808 was kept &ldquo;with a procession, military escort, and an oration in Mr. Fiske&rsquo;s Church, closing with a dinner in an orchard in the rear of Tufts&rsquo;s tavern&rdquo; (' + ARL(121) + '). In 1811 a great sham fight between volunteer companies was staged near the old Baptist meeting-house, &ldquo;just above Tufts&rsquo;s tavern&rdquo;; the attacking colonel held his infantry &ldquo;in an orchard in the rear of Tufts&rsquo;s tavern&rdquo; and then marched his artillery &ldquo;through Tufts&rsquo;s yard and orchards&rdquo; (' + ARL(133) + ').</p>'),
  service='<p>Born in July 1776, he was an infant during the Revolution. No military service is recorded for him in the sources used here.</p>',
  family=('<p>Father: ' + PL("jonathan-tufts-36-8", "Jonathan Tufts") + '; mother: Elizabeth (Holden) Tufts. The Arlington register records that &ldquo;Jonathan Tufts of Medford m. Elizabeth Holden 24 Jan. 1764&rdquo; (' + ARL(311) + '). The register lists John&rsquo;s children, baptized in West Cambridge: Rebecca Cutler; Eliza (bap. 1802, m. Abner Peirce 1826); Elmira (bap. 1804); Caroline (bap. 1806, d. 1808); John (bap. 1808, d. 1837), who as &ldquo;John Tufts, 2d&rdquo; married Lucy Ann Locke in 1833; Caroline (bap. 1810); and Harris or Harrison (bap. 1812, d. 1827). <em>Tufts Kinsmen</em> also names a son James C. (Vol.&nbsp;I, p. 161).</p>'
    + Q("John the father (tavern keeper) d. 16 Aug. 1817, a. 41. His wid. m. James Russell of Chas. 13 July, 1833, W. Camb.", ARL(311))),
  unverified='<strong>Day of death:</strong> the Arlington register gives August 16, 1817, aged 41; <em>Tufts Kinsmen</em> (Vol.&nbsp;I, p. 161) gives August 15, 1817. Note: Pending further work.'))
SP[_JT] = "<ul><li><strong>Rebecca Cutler</strong> (1779&ndash;1862), daughter of William and Rebecca Cutler; married December 13, 1798 (" + ARL(311) + "; <em>Tufts Kinsmen</em>, Vol.&nbsp;I, p. 161). As his widow she married James Russell of Charlestown on July 13, 1833.</li></ul>"
NEWUNCHK.add(_JT)
_nf_rel(_JT, "jonathan-tufts-36-8", "father Jonathan Tufts", "son John Tufts of West Cambridge (1776&ndash;1817), tavern keeper")

# ---------- New profile: Rev. John Tufts of Newbury ----------
_RJ = "john-tufts-hc1708"
PROFILES.append(dict(slug=_RJ, name="Rev. John Tufts (Harvard 1708)", dates="[dates not in sources cited]; ordained c. 1714", town="Medford; minister of the Second Parish of Newbury (now West Newbury), Mass.", born="", died="", era="Colonial",
  line="Son of Capt. Peter Tufts (c. 1648&ndash;1721); minister and author of an early singing-book",
  bio=('<p>John Tufts was born in Medford, a son of ' + PL("peter-tufts-1648", "Capt. Peter Tufts") + ', and graduated from Harvard College in 1708. He became minister of the parish in the western part of Newbury, now West Newbury, and is remembered as the author of one of the first singing-books printed in the colonies.</p>'
    + Q("A year previous to Mr. Belcher&rsquo;s death, John Tufts was ordained. He was born in Medford, graduated at Harvard in 1708. He preached twenty-four years, when he was dismissed by a council called on complaint of some disaffected women of the parish. Mr. Tufts was the author of the first singing-book used in the colony, previous to the publication of which many churches had but two or three tunes, and less than a dozen in all, York, Windsor, and Martyrs, being the best known.", ESX(423) + " " + OCRN)
    + '<p>He was in demand as a preacher beyond his own parish. At the ordination of the Rev. Mr. Bradstreet over the new parish at Squam (Annisquam), &ldquo;The sermon at the ordination was preached by Rev. John Tufts, of Newbury, and was published&rdquo; (' + ESX(138) + ').</p>'
    + '<p>See also his brother ' + PL("thomas-tufts-hc1701", "Rev. Thomas Tufts") + ' and the <a href="{P}harvard.html">Harvard graduates</a> list.</p>'),
  service='<p>No military service is recorded for him.</p>',
  family=('<p>Father: ' + PL("peter-tufts-1648", "Capt. Peter Tufts (c. 1648&ndash;1721)") + ', whose sons who lived included the Rev. Thomas Tufts (Harvard 1701), the Rev. John Tufts of Newbury (Harvard 1708), and ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + ' (NEHGR 51, pp. 302&ndash;303, as cited on his father&rsquo;s page).</p>'),
  unverified='<strong>Dates of birth and death, marriage,</strong> and the <strong>exact years of the ministry</strong> are not given in the source quoted; &ldquo;a year previous to Mr. Belcher&rsquo;s death&rdquo; (Belcher died in 1715) places the ordination about 1714, and &ldquo;twenty-four years&rdquo; the dismissal about 1738. <strong>Title of the singing-book</strong> is not named in the source. Note: Pending further work.'))
SP[_RJ] = "<p>No marriage is recorded in the sources cited here.</p>"
NEWUNCHK.add(_RJ)

# ---------- New profile: Rev. Thomas Tufts (Harvard 1701) ----------
_RT = "thomas-tufts-hc1701"
PROFILES.append(dict(slug=_RT, name="Rev. Thomas Tufts (Harvard 1701)", dates="[dates not in sources cited]", town="Medford; candidate for the ministry at Weston and Malden, Mass.", born="", died="", era="Colonial",
  line="Son of Capt. Peter Tufts (c. 1648&ndash;1721); Harvard 1701; ministerial candidate",
  bio=('<p>Thomas Tufts, a son of ' + PL("peter-tufts-1648", "Capt. Peter Tufts") + ' and a Harvard graduate of 1701, was sought by two towns as their minister.</p>'
    + '<p>Weston, then the western precinct of Watertown, chose him in 1707:</p>'
    + Q("July 16, 1707, they chose Mr. Thomas Tufts, but he declined the call in September.", WES(6))
    + '<p>He was next drawn into Malden&rsquo;s long contest over a successor to the Rev. Michael Wigglesworth. Both he and another candidate appeared in Malden at the same time, each wishing to preach, and the matter went to the General Court, which ordered:</p>'
    + Q("The Court do unanimously agree and conclude as followeth: That Mr. Thomas Tufts is a suitable person, qualified as aforesaid for the work of the ministry in that town of Malden, and see cause to settle him there in that work", MX3(491) + ", quoting the Malden <em>Bi-Centennial Book</em>, pp. 158&ndash;159. " + OCRN)
    + '<p>The Court ordered the town to pay him &pound;70 a year during his service there, and &ldquo;Mr. Tufts entered on his ministry in compliance with the order which the Court had issued&rdquo; (' + MX3(464) + '). A committee of the church then petitioned the Court to suspend its order; the petition was granted, and the Rev. David Parsons was ordained at Malden early in 1709 (' + MX3(464) + ').</p>'
    + '<p>See also his brother ' + PL(_RJ, "Rev. John Tufts") + '.</p>'),
  service='<p>No military service is recorded for him.</p>',
  family=('<p>Father: ' + PL("peter-tufts-1648", "Capt. Peter Tufts (c. 1648&ndash;1721)") + ' (NEHGR 51, pp. 302&ndash;303, as cited on his father&rsquo;s page). Brothers included ' + PL(_RJ, "Rev. John Tufts") + ' and ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + '.</p>'),
  unverified='<strong>Dates of birth and death</strong>, and <strong>how long he preached at Malden</strong> before the Court suspended its order, are not given in the passages quoted. Note: Pending further work.'))
SP[_RT] = "<p>No marriage is recorded in the sources cited here.</p>"
NEWUNCHK.add(_RT)
for _a, _b in [(_RJ, _RT)]:
    _nf_rel(_a, _b, "brother Rev. Thomas Tufts (Harvard 1701)", "brother Rev. John Tufts (Harvard 1708)")
for _s, _l in [(_RJ, "son Rev. John Tufts (Harvard 1708)"), (_RT, "son Rev. Thomas Tufts (Harvard 1701)")]:
    _nf_rel("peter-tufts-1648", _s, _l, "father Capt. Peter Tufts (c. 1648&ndash;1721)")
    _nf_rel("simon-tufts-1700", _s, _l.replace("son ", "brother "), "brother Dr. Simon Tufts (1700&ndash;1747)")

# ---------- New profiles: Jonathan Tufts of Plymouth and his son William Drew Tufts ----------
_JP = "jonathan-tufts-plymouth"; _WD = "william-drew-tufts-1791"
PROFILES.append(dict(slug=_JP, name="Jonathan Tufts of Plymouth (c. 1747&ndash;1821)", dates="c. 1747&ndash;19 January 1821", town="Plymouth, Mass.", born="1747", died="1821", era="Early Republic",
  line="Buried on Burial Hill, Plymouth, with his two wives",
  bio=('<p>Jonathan Tufts lived in Plymouth, where he and both of his wives lie on Burial Hill, the old hilltop burying ground above the town. Benjamin Drew, who numbered and copied every stone on the hill in 1894, recorded three Tufts slate stones together:</p>'
    + Q("In memory of Mr Jonathan Tufts, who died January 19, 1821, aged 74 years.", DRW("p. 28, No. 305"))
    + Q("Here lies buried the body of Mrs Elizabeth Tufts wife of Mr Jonathan Tufts, who departed this Life Jany 12th 1786 Aged 39 years.", DRW("p. 28, No. 306"))
    + Q("In memory of Mrs. Priscilla Tufts, wife of Mr. Jonathan Tufts, who died August 20, 1820, aged 55 years.", DRW("p. 28, No. 304"))
    + '<p>His son ' + PL(_WD, "William Drew Tufts") + ' died at the Island of Cuba in 1811.</p>'),
  service='<p>Born about 1747, he was of age to serve in the Revolution, but no service record has yet been matched to him.</p>',
  family='<p>Wives: Elizabeth (died 1786) and Priscilla (died 1820). Son by Priscilla: ' + PL(_WD, "William Drew Tufts (1791&ndash;1811)") + '.</p>',
  unverified='<strong>Parents and birthplace</strong> are not given on the stones, and no tie to the Medford Tufts family has been found. <strong>Birth year</strong> is computed from his age at death. <strong>Priscilla&rsquo;s maiden name</strong> is not given; the son&rsquo;s middle name Drew may point to it. Note: Pending further work.'))
SP[_JP] = "<ul><li><strong>Elizabeth</strong>, died January 12, 1786, aged 39 (Drew, p. 28, No. 306).</li><li><strong>Priscilla</strong>, died August 20, 1820, aged 55 (Drew, p. 28, No. 304).</li></ul>"
PROFILES.append(dict(slug=_WD, name="William Drew Tufts (1791&ndash;1811)", dates="9 November 1791&ndash;29 March 1811", town="Plymouth, Mass.; died at Cuba", born="1791", died="1811", era="Early Republic",
  line="Son of Jonathan and Priscilla Tufts of Plymouth",
  bio=('<p>William Drew Tufts, son of ' + PL(_JP, "Jonathan Tufts") + ' and his second wife Priscilla, was born in Plymouth on November 9, 1791, and died at nineteen on the Island of Cuba. His stone on Burial Hill reads:</p>'
    + Q("In memory of William Drew Tufts Son of Jona &amp; Priscilla Tufts, Born Nov. 9 1791 Died at the Island of Cuba March 29 1811 aged Nineteen years. Green as the bay tree, ever green, With its new foliage on, The young, the healthful have I seen, I pass&rsquo;d, and they were gone.", DRW("p. 27, No. 302") + "; the same inscription is printed in the <em>Handbook of Old Burial Hill</em> (1902). " + _IA("handbookofoldbur00perki"))),
  service='<p>Born in 1791; no military service.</p>',
  family='<p>Father: ' + PL(_JP, "Jonathan Tufts (c. 1747&ndash;1821)") + '. Mother: Priscilla Tufts (died 1820, aged 55).</p>',
  unverified='<strong>Why he was at Cuba</strong>, and whether he is buried there or on Burial Hill, is not stated; the stone may be a memorial. Note: Pending further work.'))
SP[_WD] = "<p>Died unmarried at nineteen.</p>"
NEWUNCHK |= {_JP, _WD}
_nf_rel(_JP, _WD, "son William Drew Tufts (1791&ndash;1811)", "father Jonathan Tufts of Plymouth")

# ---------- New profile: Deacon Richard Tufts of Lynn ----------
_RL = "richard-tufts-lynn"
PROFILES.append(dict(slug=_RL, name="Deacon Richard Tufts of Lynn", dates="[dates not in source]", town="Lynn, Mass.", born="", died="", era="19th Century",
  line="Son of David Tufts, a Revolutionary corporal; deacon of the First Church of Lynn; father of Gardiner Tufts",
  bio=('<p>The 1890 <em>History of Lynn</em> gives a short sketch of Deacon Richard Tufts. He was born in Lynn, the son of a Revolutionary soldier:</p>'
    + Q("Deacon Tufts was born in Lynn, and was a son of David Tufts, a corporal in the army of the Revolution, who, after the war was ended, took up the peaceful and multifarious employments of farmer, trader, and common carrier, all in a limited way. He owned and occupied a house that stood on the south-east corner of Federal street and Western avenue.", LYN("212&ndash;213") + " " + OCRN)
    + '<p>As a young man the deacon became known for his zeal in the temperance cause, and for many years he held the office of deacon in the First Church of Lynn, holding firmly to its Calvinist faith. The sketch closes with his son:</p>'
    + Q("His son, Gardiner Tufts, was prominent in the civil war, for his efficient services in Washington and elsewhere in behalf of the Massachusetts soldiery. And since the close of the war he has acceptably filled several important public positions", LYN("212&ndash;213"))),
  service='<p>No military service is recorded for him. His father, David Tufts, was a corporal in the Revolutionary army (Lewis and Newhall, p. 212).</p>',
  family='<p>Father: David Tufts, Revolutionary corporal, later farmer, trader and carrier of Lynn. Son: Gardiner Tufts, prominent in Massachusetts soldiers&rsquo; relief during the Civil War.</p>',
  unverified='<strong>Dates</strong> for Deacon Richard, his father David and his son Gardiner are not given in the sketch. <strong>Which David Tufts</strong>: no tie has been made to any David Tufts profiled on this site. This Richard is a different man from the ' + PL("richard-tufts", "Richard Tufts (b. 1763 or 1765)") + ' of Medford records unless shown otherwise. Note: Pending further work.'))
SP[_RL] = "<p>His wife is not named in the source.</p>"
NEWUNCHK.add(_RL)

# ---------- Page sections: Businesses (mills, banks), Places (Powder House, maps), Collections ----------
_P0 = "{P}"
NF_EXTRA.setdefault("businesses.html", []).append(
  '{DIV}<section id="tufts-mills-west-cambridge"><h2>The Tufts Mills, West Cambridge (1808&ndash;1831)</h2>'
  + '<p>In 1808 ' + PL(_JT, "John Tufts") + ', tavern keeper of West Cambridge (now Arlington), bought Abner Stearns&rsquo;s wool-factory and its machinery on the brook. He sold the premises, &ldquo;with a mill thereon,&rdquo; to Ezra Trull of Boston in 1817, the year he died. The works were long remembered as the &ldquo;Tufts mills&rdquo; and burned about 1831.</p>'
  + Q("A lane or road led to the mills formerly known as the &ldquo;Tufts mills.&rdquo; The mills were destroyed by fire about 1831.", ARL(18))
  + '</section>'
  + '{DIV}<section id="banks"><h2>Banks and Savings Institutions</h2>'
  + '<p><strong>Manufacturers&rsquo; and Mechanics&rsquo; Bank, Boston (1814).</strong> The list of original stockholders of this bank, later the Tremont National Bank, includes &ldquo;Nathan Tufts &hellip; 100&rdquo; and &ldquo;Dr. Aaron Tufts &hellip; 120&rdquo; (' + SUF(246) + ').</p>'
  + '<p><strong>Bunker Hill Bank, Charlestown (1825).</strong> ' + PL("nathan-tufts-1764", "Nathan Tufts") + ' sat on the first board of directors, elected July 27, 1825, and served until 1830. His nephew ' + PL("gilbert-tufts-1778", "Gilbert Tufts") + ' was a director from 1831 to 1848, and a Nathan Tufts, jr., from 1862 (' + SUF("271, 273", "pp.") + ').</p>'
  + '<p><strong>Warren Institution for Savings, Charlestown.</strong> Nathan A. Tufts was its president from 1850 to 1855. ' + PL("joseph-f-tufts-1790", "Joseph F. Tufts") + ' was treasurer in 1851&ndash;1854, and George F. Tufts was secretary in 1864&ndash;65 and treasurer from 1865 into the 1890s (' + SUF(412) + ').</p>'
  + UNV("Which Nathan Tufts and which Dr. Aaron Tufts subscribed to the Manufacturers&rsquo; and Mechanics&rsquo; Bank in 1814, which Nathan Tufts, jr., sat on the Bunker Hill board from 1862, and who Nathan A. Tufts was, are not stated in the source. Note: Pending further work.")
  + '</section>')

NF_EXTRA.setdefault("collections.html", []).append(
  '{DIV}<section id="orderly-book-1782"><h2>Orderly Book of Lieut. Francis Tufts, 1782</h2>' + _OB
  + '<p>See ' + PL("francis-tufts-41-4", "Lieut. Francis Tufts") + '.</p>'
  + UNV("The present location of the orderly book has not been traced, and the identification with the Francis Tufts profiled here is likely but not stated. Note: Pending further work.") + '</section>')

NF_EXTRA.setdefault("places.html", []).append(
  '{DIV}<section id="plan-of-malden-1795"><h2>Plan of Malden, 1795</h2>'
  + '<p>The earliest surviving survey of the whole town of Malden, which then included present-day Melrose and Everett, was drawn in 1795 by Peter Tufts Jr. of Medford under a 1794 order of the General Court. It shows the Malden River, the mill at its head, Ell Pond, the Reading, Salem, Medford, Charlestown and Chelsea roads, and a handful of named houses. See ' + PL("peter-tufts-1774", "Peter Tufts the Surveyor") + '.</p>'
  + FIG(_MAL, "hfig-flow mi-inline") + '</section>')

def _nf_sec_end(h, sid):
    i = h.find(f'<section id="{sid}"')
    if i < 0: return -1
    import re as _re
    d = 0
    for m in _re.finditer(r"</?section\b[^>]*>", h[i:]):
        d += -1 if m.group(0).startswith("</") else 1
        if d == 0: return i + m.end()
    return -1
_PH_ADD = ('<div class="nf-powder"><p>A third account, in <em>Colonial Massachusetts</em> (1899), names a different buyer:</p>'
  + Q("The government sold the property to Nathan Tufts, and the place was known from that time as the Tufts Farm, but it also retained the name of Old Powder House Farm.", COL(115))
  + UNV("Sources differ on who bought the Powder House property from the Commonwealth: &ldquo;a Peter Tufts&rdquo; in 1818 in the account above, and Nathan Tufts in <em>Colonial Massachusetts</em>, which gives no year. Both may be right if the property passed from one to the other. Note: Pending further work.") + '</div>')

_page_nf1118 = page
def page(path, title, kicker, h1, sub, body, *a, **k):
    if path == "places.html" and "nf-powder" not in body:
        j = _nf_sec_end(body, "powder-house")
        if j > 0:
            body = body[:j - len("</section>")] + _PH_ADD + body[j - len("</section>"):]
        else:
            NF_EXTRA.setdefault("places.html", []).append('{DIV}<section id="powder-house-buyer"><h2>The Powder House: Who Bought It</h2>' + _PH_ADD + '</section>')
    return _page_nf1118(path, title, kicker, h1, sub, body, *a, **k)
_EXTRA_nf1118 = EXTRA
def EXTRA(path):
    out = _EXTRA_nf1118(path)
    if path == "places.html" and "nf-powder" not in out and 'id="powder-house"' in out:
        j = _nf_sec_end(out, "powder-house")
        if j > 0:
            out = out[:j - len("</section>")] + _PH_ADD + out[j - len("</section>"):]
            NF_EXTRA["places.html"] = [x for x in NF_EXTRA.get("places.html", []) if "powder-house-buyer" not in x]
    for _h in NF_EXTRA.get(path, []):
        if _h not in out: out += _h
    return out

# =====================================================================
# Part 2: answers checked against Tufts Kinsmen Vol. I (printed pages).
# =====================================================================
TKV = lambda pg, no="": f'<em>Tufts Kinsmen</em>, Vol.&nbsp;I, p. {pg}' + (f', no. {no}' if no else '')
BED = lambda pg: f'Abram English Brown, <em>History of the Town of Bedford</em> (1891), p. {pg}. {_IA("historyoftownofb00brow")}'
MM7 = lambda pg: f'<em>The Massachusetts Magazine</em>, vol. 7 (1914), p. {pg}. {_IA("massachusettsmag07newy")}'
WWN = lambda pg: f'<em>Worcester County, Mass., Warnings, 1737&ndash;1788</em> (1899), p. {pg}. {_IA("worcestercountym00blak")}'
NHL = lambda pg: f'Henry M. Brooks and others, <em>The Newhall Family of Lynn, Massachusetts</em> (1882), p. {pg}. {_IA("newhallfamilyofl01wate")}'
NHL = lambda pg: f'<em>The Newhall Family of Lynn, Massachusetts</em> (1882), p. {pg}. {_IA("newhallfamilyofl01wate")}'
def _nf_get(slug):
    for _p in PROFILES:
        if _p["slug"] == slug: return _p
    return None

# ---- Dr. Simon Tufts (11-1): dates ----
_s = _nf_get("simon-tufts-11-1")
if _s:
    _s.update(name="Dr. Simon Tufts (1727&ndash;1786)", dates="16 January 1726/7 &ndash; 31 December 1786", born="1727", died="1786")
    _s["bio"] = _s["bio"] + '<p>He was born in Medford on January 16, 1726/7, the eldest child of ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + ' and Abigail (Smith) Tufts, graduated from Harvard College in 1744, read medicine with his father and took over his practice at his father&rsquo;s death, and died in Medford on December 31, 1786 (' + TKV(36, "11-1") + ').</p>'

# ---- William Tufts (d. 1777) ----
_w = _nf_get("william-tufts-1777")
if _w:
    _w.update(dates="24 August 1762 &ndash; 1777", born="1762")
    for _k in ("bio", "family"):
        _w[_k] = _w[_k].replace("William Tufts Jr. (1727&ndash;1782)", "William Tufts Jr. (1727&ndash;1771)")
    _w["bio"] = _w["bio"] + ('<p>The family record gives his birth as August 24, 1762, in Medford, and says he was a private killed at the Battle of Bennington in August 1777. His nephew Nathaniel Trask applied for a pension on behalf of his heirs in 1829 (' + TKV(165, "87-5") + '). His father, the Louisbourg volunteer of 1745, died in 1771; his mother Katherine then married Nathaniel Wyman in 1772 and Ebenezer Richardson in 1776 (' + TKV(81, "37-1") + ').</p>'
        + '<p>The town history of Bedford lists a William Tufts among the &ldquo;Men from Bedford who served for three years or the war. Called in 1777&rdquo; (' + BED(67) + '), and the family record itself cites that page for him.</p>')
    _w["unverified"] = ("<strong>Day and place of death:</strong> the family record gives August 19, 1777, at Bennington; Wild says only &ldquo;killed 1777,&rdquo; and no muster or casualty roll recording his death has yet been seen. "
        "<strong>Bedford:</strong> that the Bedford three-year man of 1777 and the Bedford entry in Col. Wesson&rsquo;s regiment are this Medford-born William is supported by the family record but not by an enlistment paper. "
        "<strong>Earlier birth year:</strong> a family list on another site gives about 1755; Wild and the family record both give 1762, which is followed here. Note: Pending further work.")

# ---- Thomas Tufts of Lexington: son drowned 1817 ----
_nf_add_bio("thomas-tufts-1766",
  '<p class="note"><strong>Son Thomas&rsquo;s death:</strong> Hudson records that the son Thomas, born December 16, 1792, &ldquo;was drowned in Ky., Oct. 8, 1817&rdquo; (' + LEX(247) + '), and the family record agrees: he drowned fording the Licking River, Kentucky, on October 8, 1817, after serving as a private in the War of 1812 (' + TKV(243, "133-1") + '). The year 1817 is followed on this site; the Adams genealogy quoted above gives 1816.</p>')

# ---- Grimes Tufts (40-8): officer sketch; death year ----
_nf_add_bio("grimes-tufts-40-8",
  '{DIV}<section id="officer-1775"><h2>Officer in Mansfield&rsquo;s Regiment, 1775</h2>'
  + '<p><em>The Massachusetts Magazine</em>, in its series on the officers of Col. John Mansfield&rsquo;s regiment, gives Grimes Tufts a sketch of his own:</p>'
  + Q("SECOND LIEUTENANT GRIMES TUFTS of Lynn served as Sergeant in Captain Ezra Newhall&rsquo;s (Lynn) Company of Minute Men which marched on the Lexington alarm of April 19, 1775. April 24, 1775 he was engaged as Ensign in Captain Ezra Newhall&rsquo;s Company, Colonel John Mansfield&rsquo;s Regiment.", MM7(44))
  + '<p>Another list of the company&rsquo;s officers calls him Second Lieutenant, and Col. William Henshaw&rsquo;s orderly book gives him the same rank in Capt. Asa Prince&rsquo;s company. &ldquo;He served through the year&rdquo; (' + MM7(44) + '). He is also named among the regiment&rsquo;s subalterns in the magazine&rsquo;s list for Mansfield&rsquo;s regiment (' + MM6(149) + ').</p>'
  + UNV("<strong>Year of death:</strong> the magazine says &ldquo;He died December 23, 1805.&rdquo; <em>Tufts Kinsmen</em> gives December 23, 1808, at Lynn, citing the Lynn vital records (Vol.&nbsp;I, p. 86). This site follows 1808. Note: Pending further work.")
  + '</section>')

# ---- Lieut. William Tufts (13-6): Lancaster warning, 1767 ----
_nf_add_bio("william-tufts-13-6",
  '{DIV}<section id="lancaster-1767"><h2>In Lancaster, 1767</h2>'
  + '<p>For some years the family lived in Lancaster, in Worcester County. When the Lancaster selectmen &ldquo;warned out&rdquo; newcomers on January 6, 1767, a routine step that relieved a town of liability for their support, they listed the whole household as having come from Medford:</p>'
  + Q("Tuffs, William, w. Mary, ch. Aaron, Moses, George, Grimes, Mary, Samuel, Lucy. Also William Jr., w. Susanna, ch. Susanna, Nathan, servant Benj. Paine, from Medford.", WWN(33))
  + '<p>The children named include ' + PL("moses-tufts-40-6", "Moses") + ', ' + PL("george-tufts-40-7", "George") + ', ' + PL("grimes-tufts-40-8", "Grimes") + ' and ' + PL("samuel-tufts-41-2", "Samuel") + '; &ldquo;William Jr., w. Susanna&rdquo; is ' + PL("william-tufts-40-2", "William Tufts Jr. (1736&ndash;1782)") + ' and his wife Susanna (Dix). His son ' + PL("francis-tufts-41-4", "Francis") + ' had been born at Lancaster in 1756.</p>'
  + '</section>')

# ---- Nathan Tufts, cordwainer (18-1) ----
_nf_add_bio("nathan-tufts-cordwainer",
  '{DIV}<section id="dates"><h2>Birth, Marriage and Death</h2>'
  + '<p>The family record gives his birth as May 14, 1724, at Charlestown (now Somerville), and his death as December 21, 1771, at Medford; his widow Mary married Richard Clark of Watertown in 1777 (' + TKV(50, "18-1") + '). The Arlington register adds the marriage: &ldquo;Nathan of Chas., bro. of Peter (1), m. Mary Adams of Camb. 6 June 1751&rdquo; (' + ARL(310) + '). He is a different man from ' + PL("nathan-tufts-15-7", "Nathan Tufts (1741&ndash;1784)") + ', who was nine years old at that marriage.</p>'
  + UNV("<strong>Year of marriage:</strong> the Arlington register and Wyman give June 6, 1751; <em>Tufts Kinsmen</em> gives June 6, 1750 (Vol.&nbsp;I, p. 50). Note: Pending further work.")
  + '</section>')
_nf_rel("nathan-tufts-cordwainer", "nathan-tufts-15-7", "a different man: Nathan Tufts (1741&ndash;1784)", "a different man: Nathan Tufts, cordwainer (1724&ndash;1771)")

# ---- Peter Tufts (b. 1753, 53-2): Woburn birth ----
_pj = _nf_get("peter-tufts-jr")
if _pj:
    _pj.update(dates="9 January 1753 &ndash; 4 November 1832 (Wild: 1836)")
    _pj["bio"] = _pj["bio"] + ('{DIV}<section id="woburn-birth"><h2>Born at Woburn</h2>'
      + '<p>The Arlington genealogical register records his birth from the Woburn records: &ldquo;Peter, 3d, of Chas., s. of Peter (1), b. Woburn 9 Jan. 1753&rdquo; (' + ARL(310) + '). The family record agrees, placing his birth at Woburn (now Burlington) and his death at Charlestown on November 4, 1832; he married Hannah Adams at Menotomy on February 22, 1773 (' + TKV(104, "53-2") + '). An older brother, also Peter, born at Woburn in 1751, died in 1752.</p>'
      + '<p>His sons included ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', Joel, Thomas, Elias and Aaron (' + TKV(105) + '); ' + PL(_JT, "John Tufts of West Cambridge") + ' was a cousin&rsquo;s son, not his.</p></section>')

# ---- Joseph Tufts Jr. (b. 1755) = 43-1: merge ----
_jj = _nf_get("joseph-tufts-1755")
if _jj:
    _jj.update(name="Joseph Tufts Jr. (1755&ndash;1840)", dates="17 February 1755 &ndash; 10 March 1840", died="1840", town="Medford; later Danvers, Mass.")
    _jj["bio"] = _jj["bio"] + ('{DIV}<section id="danvers"><h2>Later Life in Danvers</h2>'
      + '<p>The family record identifies him as no. 43-1, the eldest son of ' + PL("joseph-tufts-jr-15-2", "Capt. Joseph Tufts") + ' and Hannah (Cutter) Tufts. It records that he was a private in the Revolution and lent bounty money in 1776, married his cousin Esther Dickson at Menotomy on December 23, 1779, was head of a household in Danvers in the 1820 census, and died at Danvers on March 10, 1840 (' + TKV("90&ndash;91", "43-1") + '). The Arlington register confirms the marriage: &ldquo;Joseph Tufts of Medford m. Esther Dickson 23 Dec. 1779&rdquo; (' + ARL(312) + ').</p>'
      + '<p>Their children were Joseph, Esther, Rebecca, Lucy, Cotton, Anna, and Frederick A. (' + TKV(91) + '). His brother ' + PL("andrew-tufts-43-3", "Andrew Tufts") + ' settled at Worcester.</p></section>')
    _jj["unverified"] = re.sub(r"<strong>Possibly the same man as</strong>.*?(?=<strong>|Note: Pending|$)", "", _jj["unverified"], flags=re.S) or "Note: Pending further work."
SP["joseph-tufts-1755"] = "<ul><li><strong>Esther Dickson</strong> (1757&ndash;1848), daughter of Walter and Anne (Cutter) Dickson; married December 23, 1779, at Menotomy (" + ARL(312) + "; " + TKV(91) + ").</li></ul>"

# ---- Henry Tufts Jr. (1748) absorbs 25-1; tailoring to Henry Sr. (1716) ----
_hj = _nf_get("henry-tufts-1748"); _hs = _nf_get("henry-tufts-1716")
if _hs:
    _hs["bio"] = _hs["bio"] + ('{DIV}<section id="tailor"><h2>Tailor of Fleet Street; Newmarket and Lee</h2>'
      + '<p>After his apprenticeship to a Boston tailor he set up as a tailor on Fleet Street in the North End, then followed his brother Thomas to Newmarket, New Hampshire. On November 18, 1765, he was among the petitioners for dividing Durham and forming the parish of Lee. He signed the Association Test of loyalty and served as a private in the Revolution (' + TKV("31&ndash;32", "8-4") + ').</p>'
      + '<p>His son ' + PL("henry-tufts-1748", "Henry Tufts Jr.") + ' signed the Association Test with him.</p></section>')
if _hs:
    _hs["unverified"] = re.sub(r"<strong>Page:</strong>.*?(?=<strong>|Note: Pending|$)", "", _hs["unverified"], flags=re.S)
    _hs["unverified"] = re.sub(r"<strong>Possible conflation:</strong>.*?(?=<strong>|Note: Pending|$)", "", _hs["unverified"], flags=re.S)
    if "Note: Pending" not in _hs["unverified"]: _hs["unverified"] += " Note: Pending further work."
if _hj:
    _hj["bio"] = _hj["bio"].replace(" and summarised on " + PL("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)"), ", summarised below").replace(" and summarised on " + PL("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)").replace(RW_icon("henry-tufts-25-1"), ""), ", summarised below")
    _hj["service"] = _hj["service"].replace(" and summarised on " + PL("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)"), ", summarised below")
    _hj["bio"] = _hj["bio"] + ('{DIV}<section id="family-record"><h2>From the Family Record</h2>'
      + '<p>The family record numbers him 25-1, the eldest son of ' + PL("henry-tufts-1716", "Henry Tufts Sr.") + ': born at Newmarket on June 24, 1748; married Lydia Bickford at Durham in 1770; died at Limerick, Maine, on January 31, 1831. He signed the Association Test &ldquo;along with his father&rdquo; (' + TKV("62&ndash;63", "25-1") + '). It also covers his conviction in 1793, the commuting of his sentence to imprisonment at Castle Island in Boston Harbor, his years among the Saint Francis Indians learning doctoring from Molly Ockit, and the town of Limerick&rsquo;s payments to him for doctoring its poor (pp. 63&ndash;64). It dates his memoir to Dover, N.H., printed by Samuel Bragg Jr., 1807 (p. 64).</p></section>')
    _hj["unverified"] = re.sub(r"<strong>Possible conflation:</strong>.*?(?=<strong>|Note: Pending|$)", "", _hj["unverified"], flags=re.S)
    if "Note: Pending" not in _hj["unverified"]: _hj["unverified"] += " Note: Pending further work."
# Remove the merged pages from the profile list; they become redirects.
NF_REDIRECTS = {"profiles/henry-tufts-25-1.html": "henry-tufts-1748.html", "profiles/joseph-tufts-43-1.html": "joseph-tufts-1755.html"}
_NF_GONE = {"henry-tufts-25-1": "henry-tufts-1748", "joseph-tufts-43-1": "joseph-tufts-1755"}
PROFILES[:] = [p for p in PROFILES if p["slug"] not in _NF_GONE]
for _k in list(REL.keys()):
    if _k in _NF_GONE: del REL[_k]; continue
    _seen = set(); _new = []
    for _s2, _l in REL[_k]:
        if _s2 in _NF_GONE: continue
        if _s2 not in _seen: _seen.add(_s2); _new.append((_s2, _l))
    REL[_k] = _new
for _g in _NF_GONE:
    RW_SERVICE.pop(_g, None)
try:
    if "profiles/henry-tufts-25-1.html" in PAGE_FIGS:
        PAGE_FIGS.setdefault("profiles/henry-tufts-1748.html", []); PAGE_FIGS["profiles/henry-tufts-1748.html"] += [x for x in PAGE_FIGS.pop("profiles/henry-tufts-25-1.html") if x not in PAGE_FIGS["profiles/henry-tufts-1748.html"]]
except NameError:
    pass

# ---- Names formerly under research: Ichabod, Elias, Frederick, James (1755) ----
AUDIT = ""
def _nf_new(slug, name, dates, town, born, died, era, line, bio, service, family, unv, sp, rels=(), rw=None):
    PROFILES.append(dict(slug=slug, name=name, dates=dates, town=town, born=born, died=died, era=era, line=line, bio=bio, service=service, family=family, unverified=unv))
    SP[slug] = sp; NEWUNCHK.add(slug)
    for _o, _la, _lb in rels: _nf_rel(slug, _o, _la, _lb)
    if rw: RW_SERVICE[slug] = rw
_nf_new("ichabod-tufts-37-3", "Ichabod Tufts (1731&ndash;1775?)", "16 May 1731 &ndash; 17 June 1775?", "Medford, Mass.", "1731", "1775", "The Revolution",
  "Son of John and Sarah (Peirce) Tufts; by tradition killed at Bunker Hill",
  '<p>Ichabod Tufts was born in Medford on May 16, 1731, a son of John and Sarah (Peirce) Tufts, and married Rebecca Francis there on May 17, 1753 (' + TKV(82, "37-3") + '). Nothing is known of him after 1775. Family tradition holds that he was killed in the confusion of the Battle of Bunker Hill on June 17, 1775; no record of his death has been found (' + TKV("51, 82") + ').</p>'
  + '<p>His widow married Aaron Blanchard Jr. on November 14, 1776.</p>',
  '<p>No muster roll, casualty list or pension record naming him has been found. He does not appear among the Tufts entries of <em>Massachusetts Soldiers and Sailors</em>, vol. XVI, pp. 130&ndash;140.</p>',
  '<p>Parents: John Tufts and Sarah (Peirce) Tufts. Brother: William Tufts Jr. (1727&ndash;1771), father of ' + PL("william-tufts-1777", "William Tufts (1762&ndash;1777)") + '. Children: John (1754&ndash;1805), a ship blacksmith of Newburyport; Samuel (1758&ndash;1808); and Rebecca (1760&ndash;1821), who married John Blanchard (' + TKV("167&ndash;168") + ').</p>',
  '<strong>Death at Bunker Hill</strong> is a family tradition. The family record itself says only that he was &ldquo;probably&rdquo; killed there and that no record of his death has been found. Note: Pending further work.',
  "<ul><li><strong>Rebecca Francis</strong> (bapt. 1733&ndash;1817), daughter of Samuel and Mary (Nurse) Francis; married May 17, 1753, at Medford. She married second Aaron Blanchard Jr., November 14, 1776 (" + TKV(82) + ").</li></ul>",
  [("william-tufts-1777", "nephew William Tufts (1762&ndash;1777)", "uncle Ichabod Tufts (1731&ndash;1775?)")])
_nf_new("elias-tufts-42-4", "Elias Tufts (b. 1751)", "13 July 1751 &ndash; [death date not found]", "Charlestown; Watertown, Mass.; Pembroke, N.H.", "1751", "", "The Revolution",
  "Son of Jonathan and Sarah (Thompson) Tufts; of Watertown in 1774; died at Pembroke, N.H.",
  '<p>Elias Tufts was born in Charlestown (now Somerville) on July 13, 1751, a son of Jonathan and Sarah (Thompson) Tufts. He was of Watertown in 1774, when he married Sarah (Sally) Fillebrown there on February 14. Their daughter Sally was born at Newtown (Pembroke), New Hampshire, in July 1774 and died in 1784. Elias died at Pembroke; the date is not recorded (' + TKV(90, "42-4") + ').</p>',
  '<p>No Revolutionary service is recorded for him in the family record or in the Tufts entries of <em>Massachusetts Soldiers and Sailors</em>, vol. XVI.</p>',
  '<p>Parents: Jonathan Tufts and Sarah (Thompson) Tufts. Child: Sally (1774&ndash;1784) (' + TKV(192) + ').</p>',
  '<strong>Service in the 15th Massachusetts</strong>, reported in some accounts, has not been found in any source seen. <strong>Date of death</strong> is not recorded. Note: Pending further work.',
  "<ul><li><strong>Sarah (Sally) Fillebrown</strong> (b. 1752), daughter of Edward and Susanna (Peirce) Fillebrown; married February 14, 1774, at Watertown; died at Pembroke, N.H. (" + TKV(90) + ").</li></ul>")
_nf_new("frederick-tufts-9-7", "Sergt. Frederick Tufts (bapt. 1731)", "baptized 27 June 1731 &ndash; [death not found]", "Boston; Mystic (West Medford), Mass.", "1731", "", "The Revolution",
  "Son of Thomas and Emma (Phipps) Tufts; sergeant from Mystic in the Revolution",
  '<p>Frederick Tufts was baptized in Boston on June 27, 1731, a son of Thomas and Emma (Phipps) Tufts. The family record says he served as a sergeant from Mystic (West Medford) in the Revolutionary War, and that he apparently died in the service or never came home; no later record of him has been found. He did not marry (' + TKV(34, "9-7") + ').</p>',
  '<p>Sergeant from Mystic (West Medford) in the Revolutionary War, per the family record (' + TKV(34) + '). No muster roll naming him has yet been found.</p>',
  '<p>Parents: Thomas Tufts and Emma (Phipps) Tufts. Single.</p>',
  '<strong>Service:</strong> the family record places his service as a sergeant in the Revolutionary War, not in the colonial militia as some accounts say, and no muster roll naming him has yet been found. <strong>Death</strong> is not recorded. Note: Pending further work.',
  "<p>He did not marry (" + TKV(34) + ").</p>", rw="pistol")
_nf_new("james-tufts-82-3", "James Tufts, Potter (1755&ndash;1810)", "24 May 1755 &ndash; 10 November 1810", "Medford, Mass.", "1755", "1810", "The Revolution",
  "Son of James and Tabitha (Binford) Tufts; potter of Medford",
  '<p>James Tufts, potter, was born in Medford on May 24, 1755, a son of ' + PL("james-tufts-jr-36-2", "James Tufts") + ' and Tabitha (Binford) Tufts, and died in Medford on November 10, 1810. He married Elizabeth Hay at Waltham on March 23, 1775, and they had twelve children (' + TKV(150, "82-3") + '). See also the family&rsquo;s <a href="{P}businesses.html#pottery">pottery</a>.</p>',
  '<p>No Revolutionary service is stated for him in the family record.</p>',
  '<p>Father: ' + PL("james-tufts-jr-36-2", "James Tufts") + '. Mother: Tabitha (Binford) Tufts. Sister: Elizabeth, wife of ' + PL("nathan-tufts-15-7", "Nathan Tufts (1741&ndash;1784)") + '. Children: Mary, James, Elizabeth, Lucretia, Mercy, Sarah, Sarah, Elias, Frances, Lucy, Lucy, and Nancy (' + TKV(150) + ').</p>',
  '<strong>Service:</strong> some accounts treat him as a supporter of the Revolutionary cause; no record of service or support has been found. Note: Pending further work.',
  "<ul><li><strong>Elizabeth Hay</strong> (1753&ndash;1828), daughter of James and Elizabeth (Hall) Hay; married March 23, 1775, at Waltham (" + TKV(150) + ").</li></ul>",
  [("james-tufts-jr-36-2", "father James Tufts", "son James Tufts, potter (1755&ndash;1810)"), ("nathan-tufts-15-7", "brother-in-law Nathan Tufts (1741&ndash;1784)", "brother-in-law James Tufts, potter (1755&ndash;1810)")])

# ---- Dr. Samuel Tufts (11-5) of Newburyport ----
_DS = "samuel-tufts-11-5"
_nf_new(_DS, "Dr. Samuel Tufts of Newburyport (1735&ndash;1799)", "7 January 1734/5 &ndash; 20 September 1799", "Medford; Newbury and Newburyport, Mass.", "1735", "1799", "The Revolution",
  "Son of Dr. Simon Tufts (1700&ndash;1747); physician, druggist and merchant of Newburyport",
  '<p>Samuel Tufts was born in Medford on January 7, 1734/5, a son of ' + PL("simon-tufts-1700", "Dr. Simon Tufts") + ' and Abigail (Smith) Tufts and a younger brother of ' + PL("simon-tufts-11-1", "Dr. Simon Tufts") + ' and ' + PL("cotton-tufts", "Dr. Cotton Tufts") + '. Like them he became a physician; he was also a druggist and merchant. He settled in Newbury, married Sarah Moody there on November 8, 1762, and was chosen a clerk of the market in 1764. He was one of the petitioners to set off Newburyport as a town, served as one of its selectmen from 1777 to 1783, and died at Newburyport on September 20, 1799 (' + TKV("38&ndash;39", "11-5") + ').</p>'
  + '<p>Early in 1762 a Samuel Tufts was acting in Newbury family business. When Capt. Joseph Newhall of Newbury died intestate, &ldquo;guardianship of his son Samuel Newhall (above fourteen years of age) was granted 23 Jan., 1762, to Samuel Tufts&rdquo; (' + NHL(179) + '). The widow, Mercy (Bradshaw) Newhall, was a daughter of John and Mercy (Tufts) Bradshaw of Medford and so Dr. Samuel&rsquo;s first cousin.</p>'
  + '<p>A notice of July 1766 to the selectmen of Newburyport, signed &ldquo;Saml Tufts,&rdquo; is shown on <a href="{P}profiles/samuel-tufts.html#newburyport-1766">Samuel Tufts (several men)</a>.</p>'
  + '<p>The family record notes that the Tufts arms appear on his bookplate (' + TKV("xxx") + '); see <a href="{P}coat-of-arms.html">Coat of Arms</a>.</p>',
  '<p>In 1777 he served in the commissary of Capt. Newell&rsquo;s company (' + TKV(39) + ').</p>',
  '<p>Father: ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + '. Mother: Abigail (Smith) Tufts. Brothers: ' + PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)") + ', ' + PL("cotton-tufts", "Dr. Cotton Tufts (1732&ndash;1815)") + '. Children, born at Newburyport from 1763: Sarah, Samuel, Dorothy, Simon, Sarah, and Polly (' + TKV(38) + ').</p>',
  '<strong>The 1762 guardianship and the 1766 notice</strong> name only &ldquo;Samuel Tufts.&rdquo; Dr. Samuel is the only Samuel Tufts known to have been living in Newbury then, and he was a cousin of the Newhall widow, so both are attributed to him here as likely, not proven. <strong>Newburyport</strong> was set off from Newbury in 1764, so a 1766 notice to its selectmen fits his residence. Note: Pending further work.',
  "<ul><li><strong>Sarah Moody</strong>, married November 8, 1762, at Newbury (" + TKV(38) + ").</li></ul>",
  [("simon-tufts-1700", "father Dr. Simon Tufts (1700&ndash;1747)", "son Dr. Samuel Tufts of Newburyport (1735&ndash;1799)"),
   ("simon-tufts-11-1", "brother Dr. Simon Tufts (1727&ndash;1786)", "brother Dr. Samuel Tufts of Newburyport (1735&ndash;1799)"),
   ("cotton-tufts", "brother Dr. Cotton Tufts (1732&ndash;1815)", "brother Dr. Samuel Tufts of Newburyport (1735&ndash;1799)"),
   ("samuel-tufts", "Samuel Tufts (several men), including the 1766 Newburyport notice", "Dr. Samuel Tufts of Newburyport (1735&ndash;1799), the likely writer of the 1766 notice")], rw="pistol")
_SN_SEC = _SN_SEC.replace(
  UNV("Which Samuel Tufts wrote this notice is not established. No Samuel Tufts of Newburyport is known on this site, and the name is not attached here to any of the men already profiled. Note: Pending further work."),
  '<p>The writer was most likely ' + PL(_DS, "Dr. Samuel Tufts (1735&ndash;1799)") + ', physician and merchant, who married at Newbury in 1762, lived in Newburyport, and later served as one of its selectmen. In January 1762 a Samuel Tufts was also appointed guardian of a Newbury boy, Samuel Newhall, whose mother was Dr. Samuel&rsquo;s first cousin (' + NHL(179) + ').</p>'
  + UNV("The note is signed only &ldquo;Saml Tufts,&rdquo; and no source states that Dr. Samuel wrote it; the attribution rests on his residence, his public role in Newburyport, and the family connection. Note: Pending further work."))

# ---- Redirect pages for merged profiles (written after the build) ----
def NF_write_redirects():
    for _src, _dst in NF_REDIRECTS.items():
        open(_src, "w").write(f'<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>Moved | Tufts Lineage &amp; Legacy</title><link rel="canonical" href="{_dst}"><meta http-equiv="refresh" content="0; url={_dst}"><meta name="robots" content="noindex"></head><body><p>This page has moved to <a href="{_dst}">{_dst}</a>.</p></body></html>\n')
# Remove last build's redirect stubs so the post-processing passes see only full pages; they are rewritten at the end.
import os as _nf_os
for _nfsrc in NF_REDIRECTS:
    if _nf_os.path.exists(_nfsrc) and "http-equiv=\"refresh\"" in open(_nfsrc).read():
        _nf_os.remove(_nfsrc)
# Businesses page was already written earlier in the build; rewrite it with the new sections, as earlier runs did.
if "BIZ_HTML" in globals():
    BIZ_HTML = BIZ_HTML + "".join(NF_EXTRA.pop("businesses.html", []))
    page("businesses.html", "Businesses | Tufts Lineage &amp; Legacy", "Places", "Businesses", "The trades of the Tufts family, colonial era to the 19th century", BIZ_HTML)
