# Dr. Cotton Tufts of Weymouth and his descendants: Cotton Jr., Mercy Brooks,
# Quincy and Susannah (Tufts Library founders). Leads traced to primary sources;
# copyrighted talk used only privately as a finding aid (never cited on the site).
WFA = ('Weymouth Public Libraries, <em>Tufts / Smith / Adams Family Collection</em> finding aid '
       '(Collection ID WCT002; prepared C. G. Swank, June 2016). '
       '<a href="https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection">Finding aid (PDF)</a>')
WVR1 = ('<em>Vital Records of Weymouth, Massachusetts, to the Year 1850</em>, vol. I, Births '
        '(Boston: NEHGS, 1910). <a href="https://archive.org/details/vitalrecordsofwe01weym">Book scan</a>')
WVR2 = ('<em>Vital Records of Weymouth, Massachusetts, to the Year 1850</em>, vol. II, Marriages and Deaths '
        '(Boston: NEHGS, 1910). <a href="https://archive.org/details/vitalrecordsofwe02weym">Book scan</a>')
MVR = ('<em>Vital Records of Medford, Massachusetts, to the Year 1850</em> (Boston: NEHGS, 1907). '
       '<a href="https://archive.org/details/vitalrecordsofme00medf_1">Book scan</a>')
NASH = ('Gilbert Nash, <em>Historical Sketch of the Town of Weymouth, Massachusetts, from 1622 to 1884</em> '
        '(Weymouth, 1885). <a href="https://archive.org/details/historicalsketch00nash">Book scan</a>')
HUNT = ('Edmund Soper Hunt, <em>Weymouth Ways and Weymouth People: Reminiscences</em> (Boston, 1907). '
        '<a href="https://archive.org/details/weymouthwaysweym00hunt">Book scan</a>')
LIBH = ('Town of Weymouth, &ldquo;Library History&rdquo; (Tufts Library founding). '
        '<a href="https://www.weymouth.ma.us/2521/Library-History">Town page</a>')
HNE_STOCK = ('Historic New England, Tufts &amp; Whittemore stock book, 1823 '
             '(collections access GUSN 194087). '
             '<a href="https://www.historicnewengland.org/explore/collections-access/gusn/194087/">Catalog record</a>')
OCRN = '<span class="note">(Scanned text; obvious scanning errors corrected.)</span>'

def _cw_replace(slug, **kw):
    for i, p in enumerate(PROFILES):
        if p.get("slug") == slug:
            p = dict(p); p.update(kw); PROFILES[i] = p; return
    raise KeyError(slug)

# ---------- Expand Dr. Cotton Tufts ----------
_cw_replace(
 "cotton-tufts",
 name="Dr. Cotton Tufts (1732&ndash;1815)",
 dates="1732&ndash;1815",
 town="Medford; Weymouth, Mass.",
 born="1732", died="1815",
 era="The Revolution",
 line="Dr. Simon Tufts",
 bio=FIG("cotton-tufts-greenleaf-1804.jpg")
  + '<p>' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + ', Medford&rsquo;s first physician, and Abigail (Smith) Tufts raised Cotton in Medford. He took his bachelor&rsquo;s degree at Harvard in 1749 and later received an honorary M.D.:</p>'
  + Q("Dr. Cotton Tufts, born 1732, brother of the above, graduated at Harvard College 1749; studied medicine with his brother; settled in Weymouth", 'Charles Brooks, <em>History of the Town of Medford</em> (1855), p. 306')
  + '<p>The Quinquennial Catalogue lists him A.B. 1749, A.M., and honorary M.D. 1785 (class of 1749). His brother ' + PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)") + ' trained him. By about 1751 he had opened a practice in Weymouth that lasted the rest of his life.</p>'
  + '<h3>Physician</h3>'
  + '<p>The Weymouth Tufts family papers summarize the start of that practice and the sore-throat (diphtheria) epidemic that made his name:</p>'
  + Q("Tufts gained recognition in 1751 when he introduced a new therapy for diphtheria, or &ldquo;putrid sore throat,&rdquo; which was prevalent and often fatal at the time. Harvard awarded him an honorary M.D. in 1785.", WFA, note=OCRN)
  + Q("As a practitioner of medicine he was faithful, considerate, courteous, kind and sympathetic. &hellip; He was one of the original members of the Massachusetts Medical Society, was chosen vice-president and in due course of time became president, which office he held from 1787 to 1793", NASH + ", pp. 191&ndash;192 (physician sketch)", note=OCRN)
  + '<p>He is also named among the sixty-two incorporators of the American Academy of Arts and Sciences (act of May 3, 1780). See his Learned Societies section.</p>'
  + '<h3>Town and Revolution</h3>'
  + '<p>In 1765 the town adopted instructions against the Stamp Act. Nash prints those instructions in Appendix E and credits them to James Humphrey, Esq.; later writers also associate Dr. Tufts with Weymouth&rsquo;s Stamp Act stance. The Weymouth finding aid states:</p>'
  + Q("In 1765 Dr. Tufts wrote instructions to representatives of the town of Weymouth against the Stamp Act. He served as a justice of the peace for Suffolk County, and from 1781&ndash;1792, was a member of the Massachusetts state senate. In 1788 Tufts was a Federalist delegate to the Massachusetts state convention that ratified the Constitution.", WFA, note=OCRN)
  + Q("A committee of correspondence for Weymouth &hellip; had been chosen on the 9th of March, consisting of Dr. Tufts, Major Lovell, Major Vining, Capt. Asa White and Mr. Josiah Colson. This committee met in Arnold&rsquo;s Tavern, at Weymouth Landing &hellip; organized by choice of Dr. Tufts as chairman", NASH + ", pp. 59&ndash;60", note=OCRN)
  + Q("The town also accepted the offer of Mr. Polley for the use of two swivel guns then at Salem, and voted their thanks to Dr. Tufts for his offer to transport them to Weymouth.", NASH + ", p. 60", note=OCRN)
  + Q("Dr. Cotton Tufts was chosen a delegate to the Convention", NASH + ", p. 74 (ratifying convention; see also finding aid)", note=OCRN)
  + '<h3>Deacon and Adams trustee</h3>'
  + Q("For more than forty years he was deacon of the Old North Church in Weymouth.", NASH + ", p. 191", note=OCRN)
  + Q("Of particular note is that he was entrusted with sole care of John and Abigail Adams&rsquo; private affairs during their time abroad between 1780 and 1788, and again handled the local affairs for the couple during Adams&rsquo; presidency.", WFA, note=OCRN)
  + '<p>Lucy Quincy, his first wife, was a sister of Elizabeth Quincy Smith, mother of Abigail Adams, so Dr. Tufts was Abigail&rsquo;s uncle by marriage. The Adams Papers hold 188 letters by or to him. See <a href="{P}collections.html#adams-letters">Collections: Adams correspondence</a> and his Letters section.</p>'
  + '<h3>Marriage, son and death</h3>'
  + Q("TUFTS, Cotton, Dr., and Mrs. Lucy Quincey of Brantree, Dec. 2, 1755.", WVR2 + ", marriages", note=OCRN)
  + Q("Cotton, s. Dr. Cotton and Lucy, Aug. 4, 1757.", WVR1 + ", births", note=OCRN)
  + Q("Lucy, w. Hon. Cotton Esq., Oct. 30, 1785. [[dup. Lucy Quincy, w. Cotton, M. D.] a. 56, G.R.14.]", WVR2 + ", deaths", note=OCRN)
  + '<p>He married second ' + PL("susanna-warner-tufts", "Susanna Warner") + ' of Gloucester on October 22, 1789 (see her profile). He died at Weymouth on December 8, 1815:</p>'
  + Q("Cotton Esq., Hon., Dec. 8, 1815, a. 84. [old age with a severe cold, C.R.I.] [Cotton, M. D., A. A. S., M. M. S. [h. Lucy Quincy], G.R.14.]", WVR2 + ", deaths", note=OCRN)
  + '<p>His only son, ' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + ', became a Weymouth merchant. Grandchildren ' + PL("quincy-tufts", "Quincy") + ' and ' + PL("susannah-tufts-1797", "Susannah") + ' later founded the Tufts Library.</p>',
 service=Q("Dr. Cotton Tufts besides practicing medicine in Weymouth was a State Senator for many years; also a delegate to the convention which adopted the constitution of the United States; Always an ardent Federalist.", TFH+", p. 35", ["tufts-family-history-p35.jpg"])
  + Q("from 1781&ndash;1792, was a member of the Massachusetts state senate. In 1788 Tufts was a Federalist delegate to the Massachusetts state convention that ratified the Constitution.", WFA)
  + Q("Cotton Tufts, Weymouth, 1787-1795", 'Massachusetts Medical Society, <a href="https://www.massmed.org/About/MMS-Leadership/History/Past-Presidents-of-the-Massachusetts-Medical-Society/">Past Presidents</a> (fourth president)')
  + '<p class="note">No military service entry appears for him among the Tufts names in ' + MSS + ', pp. 131&ndash;140; his Revolutionary work was civil (committee of correspondence, town offices, senate).</p>',
 family='<p>Father: ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + '. Mother: Abigail Smith. Brother: ' + PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)") + '. First wife: Lucy Quincy (1729&ndash;1785), daughter of Col. John Quincy of Braintree; married Dec. 2, 1755 (Weymouth VR, vol. II). Second wife: ' + PL("susanna-warner-tufts", "Susanna Warner Tufts") + '. Only child of the first marriage: ' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + ' (Weymouth VR, vol. I, births). No children of the second marriage have been found.</p>',
 unverified="<strong>Exact birth date:</strong> Brooks and the Adams Papers editors give 1732; Find a Grave prints May 30, 1732; Nash (p. 190) prints May 31, 1731; the Weymouth death record&rsquo;s age 84 on Dec. 8, 1815 also points near 1731. No Medford printed birth line for him was found in the volume checked. <strong>Stamp Act instructions of 1765:</strong> the finding aid says he wrote them; Nash prints the town&rsquo;s instructions in Appendix E under James Humphrey&rsquo;s name. Both are reported. <strong>Bequests of $10,000 to Harvard, Amherst, Atkinson Academy, Massachusetts General Hospital and a Weymouth free library:</strong> summarized in the finding aid only; the will text has not been read here. <strong>Schooner and sloop ownership</strong> belongs to his son the merchant, not to the doctor.")

# ---------- New profiles ----------
PROFILES.append(dict(
 slug="cotton-tufts-jr", name="Cotton Tufts (1757&ndash;1833)", dates="1757&ndash;1833",
 town="Weymouth, Mass.", born="1757", died="1833", era="The Revolution",
 line="Son of Dr. Cotton Tufts",
 bio='<p>Cotton Tufts, only child of ' + PL("cotton-tufts", "Dr. Cotton Tufts") + ' and Lucy Quincy, was born in Weymouth:</p>'
  + Q("Cotton, s. Dr. Cotton and Lucy, Aug. 4, 1757.", WVR1 + ", births", note=OCRN)
  + '<p>The Adams Papers editors and the Harvard Quinquennial Catalogue place him in the Harvard class of 1777. Letters from his father to &ldquo;Cotton Tufts Jr. student at Harvard&rdquo; from 1774 to 1777 survive in the Weymouth Tufts family papers (' + WFA + ').</p>'
  + '<h3>Merchant of Tufts Corner</h3>'
  + Q("His son Cotton Tufts (1757&ndash;1833) had a business/store with James Whittemore where the original Tufts Library building was built.", WFA, note=OCRN)
  + Q("Now we come to the store occupied for years by Tufts and Whittemore. Here they kept a general store with the post office and our first circulating library, &mdash; the building then occupying the site of Tufts Library building in 1906.", HUNT + ", p. 23", note=OCRN)
  + '<p>Historic New England holds the firm&rsquo;s 1823 stock book and other account books (1818&ndash;1833), listing yard goods, notions, hardware, tools and books (' + HNE_STOCK + '). See <a href="{P}places.html#tufts-corner">Places: Tufts Corner</a>.</p>'
  + '<h3>Marriage and children</h3>'
  + Q("Cotton Jr. and Mercy Brooks of Medford, int. Feb. 2, 1788.", WVR2 + ", marriages", note=OCRN)
  + Q("Mercy and Cotton Tufts Jr. of Weymouth, Mar. 6, 1788.", MVR + ", marriages", note=OCRN)
  + '<p>His wife ' + PL("mercy-brooks-tufts", "Mercy Brooks") + ' was his first cousin once the Medford and Weymouth lines are traced through the Brooks and Tufts families; the finding aid simply records the marriage and their four surviving children:</p>'
  + Q("They had four children: Quincy (1791&ndash;1872), Lucy (1793&ndash;1856) who married Thomas Tarbell, Susannah (1797&ndash;1877), and Mercy (1800&ndash;1858).", WFA, note=OCRN)
  + Q("Quincy, s. Cotton Jr. [dup. omits Jr.] [Jr., c.r.i.] and Mercy, July 4, 1791. &hellip; Lucy, d. Cotton and Mercy, Sept. 13, 1793. &hellip; Susanna [dup. Susannah], d. Cotton and Mercy, Jan. 19, 1797. &hellip; Mercy, d. Cotton and Mercy, Nov. 19, 1800.", WVR1 + ", births", note=OCRN)
  + '<h3>Death</h3>'
  + Q("Cotton Esq., Mar. 4, 1833, a. 76. [[h. Mercy (Brooks)] G.R.14.]", WVR2 + ", deaths", note=OCRN)
  + '<p>G.R.14 is the North Weymouth Cemetery. His homestead at 246 Commercial Street is listed by the town as the Cotton Tufts Jr. Homestead (see Places).</p>',
 service='<p>Civilian merchant and postmaster at Weymouth Landing (Hunt, p. 23; finding aid). Harvard class of 1777 (Quinquennial Catalogue; Adams Papers editors). No entry under his name was checked in detail in ' + MSS + ' for this pass.</p>',
 family='<p>Father: ' + PL("cotton-tufts", "Dr. Cotton Tufts (1732&ndash;1815)") + '. Mother: Lucy Quincy (d. 1785). Wife: ' + PL("mercy-brooks-tufts", "Mercy Brooks (1763&ndash;1849)") + '. Children: ' + PL("quincy-tufts", "Quincy") + '; Lucy (m. Thomas Tarbell, May 5, 1813, Weymouth VR vol. II); ' + PL("susannah-tufts-1797", "Susannah") + '; Mercy (1800&ndash;1858). Grandfather: ' + PL("simon-tufts-1700", "Dr. Simon Tufts") + '.</p>',
 unverified="<strong>&ldquo;First cousin&rdquo; marriage:</strong> commonly stated; the Medford marriage of Mercy Tufts to Thomas Brooks Jr. (Dec. 29, 1762) makes Mercy Brooks a Tufts granddaughter, but the exact cousin degree is not worked here. <strong>Part owner of a schooner and a sloop:</strong> from secondary genealogy only; not in the sources quoted above. <strong>Postmaster:</strong> Hunt says the store held the post office; appointment papers not seen."))

PROFILES.append(dict(
 slug="mercy-brooks-tufts", name="Mercy Brooks Tufts (1763&ndash;1849)", dates="1763&ndash;1849",
 town="Medford; Weymouth, Mass.", born="1763", died="1849", era="The Revolution",
 line="Wife of Cotton Tufts (1757&ndash;1833)",
 bio='<p>Mercy Brooks was born in Medford:</p>'
  + Q("Mercy, d. Thomas [Thomas Jr., c.r.i.] and Mercy Jr., Sept. 3, 1763.", MVR + ", births (under Brooks)", note=OCRN)
  + '<p>Her mother was Mercy (Tufts) Brooks; the Medford marriage record of Dec. 29, 1762, names Mercy Tufts and Thomas Brooks Jr. (' + MVR + ', marriages). She married ' + PL("cotton-tufts-jr", "Cotton Tufts Jr.") + ' of Weymouth in 1788 (intentions at Weymouth, Feb. 2; marriage at Medford, Mar. 6).</p>'
  + '<p>The Weymouth collection holds her diary for the year 1799 (' + WFA + ', Series II). She raised four children who lived to adulthood, including the library founders ' + PL("quincy-tufts", "Quincy") + ' and ' + PL("susannah-tufts-1797", "Susannah") + '.</p>'
  + Q("Mercy, b. Medford, wid. Cotton, d. Tho[ma]s Brooks and Mercy, old age, May 6, 1849, a. 85 y. 7 m. 4 d. [a. 86, G.R.14.]", WVR2 + ", deaths", note=OCRN),
 service='<p>Civilian. No public office found in the sources checked.</p>',
 family='<p>Father: Thomas Brooks Jr. of Medford. Mother: Mercy (Tufts) Brooks (Medford VR). Husband: ' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + '. Father-in-law: ' + PL("cotton-tufts", "Dr. Cotton Tufts") + '. Children: Quincy, Lucy (Tarbell), Susannah and Mercy (Weymouth VR, vol. I).</p>',
 unverified="<strong>Diary contents:</strong> the 1799 diary is noted in the finding aid as not yet transcribed for this site. <strong>Exact place of burial plot:</strong> G.R.14 (North Weymouth Cemetery) is cited in the death record; the stone has not been photographed here."))

PROFILES.append(dict(
 slug="quincy-tufts", name="Quincy Tufts (1791&ndash;1872)", dates="1791&ndash;1872",
 town="Weymouth; Boston, Mass.", born="1791", died="1872", era="19th Century",
 line="Grandson of Dr. Cotton Tufts",
 bio='<p>Quincy Tufts, son of ' + PL("cotton-tufts-jr", "Cotton Tufts") + ' and ' + PL("mercy-brooks-tufts", "Mercy Brooks") + ', was born in Weymouth on Independence Day, 1791:</p>'
  + Q("Quincy, s. Cotton Jr. [dup. omits Jr.] [Jr., c.r.i.] and Mercy, July 4, 1791.", WVR1 + ", births", note=OCRN)
  + '<h3>Boston merchant</h3>'
  + Q("Mr. Tufts, a bachelor, kept a store on Washington street in Boston, for many years. This was located nearly opposite the Old South Church and was one of the best known stores of Boston, where he carried such a variety of dry goods that one could match his buttons, braids, silks, bandana handkerchiefs, etc. Mr. Tufts saved all his wrapping paper, assorted it, and whenever a customer bought an article he carefully selected a piece of just the size for wrapping. He never wasted anything but time. At the close of life he left his fortune, &mdash; some twenty thousand dollars, &mdash; to found the Tufts Library in his native town.", HUNT + ", pp. 26&ndash;27", note=OCRN)
  + Q("Quincy Tufts kept a store on Washington St. in Boston which carried dry goods. He left his fortune ($20k) to Tufts Library. He and his sister Susannah were the founders and benefactors of the Tufts Library.", WFA, note=OCRN)
  + '<h3>Tufts Library</h3>'
  + Q("The Tufts Library was founded in 1879, when the Town of Weymouth received bequests of money and land from Quincy Tufts and his sister Susannah, grandchildren of Weymouth physician, Dr. Cotton Tufts, for the establishment of a public library. Part of the bequest included two wooden buildings at the corner of Washington and Commercial Streets in Weymouth Landing.", LIBH)
  + '<p>He never married. See <a href="{P}places.html#tufts-library">Places: Tufts Library</a>.</p>',
 service='<p>Civilian dry-goods merchant. No military record sought for this nineteenth-century profile.</p>',
 family='<p>Father: ' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + '. Mother: ' + PL("mercy-brooks-tufts", "Mercy Brooks Tufts") + '. Sister and co-founder: ' + PL("susannah-tufts-1797", "Susannah Tufts (1797&ndash;1877)") + '. Sisters Lucy (Tarbell) and Mercy. Grandfather: ' + PL("cotton-tufts", "Dr. Cotton Tufts") + '. Unmarried; no children (Hunt; finding aid).</p>',
 unverified="<strong>Death date 1872:</strong> from the Weymouth finding aid and town library history; not in the 1850 Weymouth printed vital records (he died after that cutoff). Burial place and exact day not yet confirmed from a primary death record. <strong>$20,000 figure:</strong> Hunt and the finding aid agree on the amount left for the library; the probate file has not been read here."))

PROFILES.append(dict(
 slug="susannah-tufts-1797", name="Susannah Tufts (1797&ndash;1877)", dates="1797&ndash;1877",
 town="Weymouth, Mass.", born="1797", died="1877", era="19th Century",
 line="Granddaughter of Dr. Cotton Tufts",
 bio='<p>Susannah (also recorded Susan / Susanna) Tufts was the daughter of ' + PL("cotton-tufts-jr", "Cotton Tufts") + ' and ' + PL("mercy-brooks-tufts", "Mercy Brooks") + ':</p>'
  + Q("Susanna [dup. Susannah], d. Cotton and Mercy, Jan. 19, 1797. [Susanna, d. Cotton Jr. and Mercy, c.r.i.] [Susannah, G.R.14.]", WVR1 + ", births", note=OCRN)
  + Q("The house now occupied by Major Eliot Pierce was, at the time of which I am writing, the home of the Tufts family, Mr. Quincy Tufts and his sisters Susan and Mercy.", HUNT + ", p. 26", note=OCRN)
  + '<p>With her brother ' + PL("quincy-tufts", "Quincy") + ' she gave money, land and buildings that became the Tufts Library:</p>'
  + Q("The Tufts Library was founded in 1879, when the Town of Weymouth received bequests of money and land from Quincy Tufts and his sister Susannah, grandchildren of Weymouth physician, Dr. Cotton Tufts, for the establishment of a public library.", LIBH)
  + Q("He and his sister Susannah were the founders and benefactors of the Tufts Library.", WFA)
  + '<p>She did not marry. After her death and Quincy&rsquo;s, the town sold remaining Tufts estate lands in Weymouth, Braintree and Quincy (1877 booklet in the family papers).</p>',
 service='<p>Civilian. Co-founder, by bequest, of the Tufts Library (town library history; finding aid).</p>',
 family='<p>Father: ' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + '. Mother: ' + PL("mercy-brooks-tufts", "Mercy Brooks Tufts") + '. Brother: ' + PL("quincy-tufts", "Quincy Tufts") + '. Sisters Lucy (Tarbell) and Mercy. Grandfather: ' + PL("cotton-tufts", "Dr. Cotton Tufts") + '. Unmarried; no children.</p>',
 unverified="<strong>Death date 1877:</strong> from the finding aid and library history; not in the 1850 Weymouth printed VRs. Day and burial not yet confirmed from a primary death record. <strong>Spelling:</strong> birth record uses Susanna / Susannah; Hunt writes Susan; the town library page uses Susannah."))

# Spouses
SP["cotton-tufts"] = ('<ul><li><strong>Lucy Quincy</strong> (1729&ndash;1785) of Braintree (now Quincy). Married Dec. 2, 1755 (<em>Vital Records of Weymouth</em>, vol. II). Died Oct. 30, 1785 (same, deaths; G.R.14).</li>'
  + '<li><strong>' + PL("susanna-warner-tufts", "Susanna Warner") + '</strong> of Gloucester, second wife. Married Oct. 22, 1789 (Gloucester VR, vol. II; Weymouth VR, vol. II).</li></ul>')
SP["cotton-tufts-jr"] = '<ul><li>' + PL("mercy-brooks-tufts", "Mercy Brooks") + ' (b. Medford, Sept. 3, 1763; d. Weymouth, May 6, 1849). Intentions Feb. 2, 1788 (Weymouth); married Mar. 6, 1788 (Medford).</li></ul>'
SP["mercy-brooks-tufts"] = '<ul><li>' + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + '. Married Mar. 6, 1788 (Medford VR).</li></ul>'
SP["quincy-tufts"] = '<p>Unmarried (Hunt, pp. 26&ndash;27; Weymouth finding aid).</p>'
SP["susannah-tufts-1797"] = '<p>Unmarried (town library history; Weymouth finding aid).</p>'

NEWUNCHK |= {"cotton-tufts-jr", "mercy-brooks-tufts", "quincy-tufts", "susannah-tufts-1797"}
# Restore cotton-tufts to checked where we have IDs (already in BREG/FAGOK)
NEWUNCHK.discard("cotton-tufts")

REL["cotton-tufts-jr"] = [("cotton-tufts", "father Dr. Cotton Tufts"), ("mercy-brooks-tufts", "wife Mercy Brooks"),
 ("quincy-tufts", "son Quincy Tufts"), ("susannah-tufts-1797", "daughter Susannah Tufts"),
 ("simon-tufts-1700", "grandfather Dr. Simon Tufts"), ("susanna-warner-tufts", "stepmother Susanna Warner Tufts")]
REL["mercy-brooks-tufts"] = [("cotton-tufts-jr", "husband Cotton Tufts"), ("cotton-tufts", "father-in-law Dr. Cotton Tufts"),
 ("quincy-tufts", "son Quincy"), ("susannah-tufts-1797", "daughter Susannah")]
REL["quincy-tufts"] = [("cotton-tufts-jr", "father"), ("mercy-brooks-tufts", "mother"), ("susannah-tufts-1797", "sister Susannah"),
 ("cotton-tufts", "grandfather Dr. Cotton Tufts")]
REL["susannah-tufts-1797"] = [("cotton-tufts-jr", "father"), ("mercy-brooks-tufts", "mother"), ("quincy-tufts", "brother Quincy"),
 ("cotton-tufts", "grandfather Dr. Cotton Tufts")]
_addrel("cotton-tufts", [("cotton-tufts-jr", "son Cotton Tufts (1757&ndash;1833)"), ("quincy-tufts", "grandson Quincy Tufts"),
 ("susannah-tufts-1797", "granddaughter Susannah Tufts"), ("mercy-brooks-tufts", "daughter-in-law Mercy Brooks")])
_addrel("susanna-warner-tufts", [("cotton-tufts-jr", "stepson Cotton Tufts (1757&ndash;1833)")])
_addrel("simon-tufts-1700", [("cotton-tufts-jr", "grandson Cotton Tufts (1757&ndash;1833)")])
_addrel("simon-tufts-11-1", [("cotton-tufts-jr", "nephew Cotton Tufts (1757&ndash;1833)")])

# Places + generation page extras
CW_PLACES = f'''<section id="tufts-corner"><h2>Tufts Corner (Washington Square), Weymouth Landing</h2>
{TA("Store of Cotton Tufts (1757&ndash;1833) and James Whittemore; later the first seat of the Tufts Library.", WFA + "; " + HUNT + ", p. 23")}
{Q("Now we come to the store occupied for years by Tufts and Whittemore. Here they kept a general store with the post office and our first circulating library, &mdash; the building then occupying the site of Tufts Library building in 1906.", HUNT + ", p. 23", note=OCRN)}
{Q("His son Cotton Tufts (1757&ndash;1833) had a business/store with James Whittemore where the original Tufts Library building was built.", WFA)}
<p>Hunt elsewhere calls the spot &ldquo;Tufts&rsquo; corner (now Washington Square)&rdquo; ({HUNT}, reminiscences of the turnpike). Historic New England holds the firm&rsquo;s stock and account books ({HNE_STOCK}). See {PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)")} and <a href="{{P}}places.html#tufts-library">Tufts Library</a>.</p>
{UNV("Exact street numbering of the 1820s storefront and the chain of later merchants (White, Ellis, and others) are from Hunt&rsquo;s memory and secondary notes; deeds not yet read.")}
</section>
{{DIV}}
<section id="tufts-library"><h2>Tufts Library, Weymouth</h2>
{TA("Public library founded by bequests of Quincy Tufts (1791&ndash;1872) and Susannah Tufts (1797&ndash;1877), grandchildren of Dr. Cotton Tufts.", LIBH + "; " + WFA)}
{Q("The Tufts Library was founded in 1879, when the Town of Weymouth received bequests of money and land from Quincy Tufts and his sister Susannah, grandchildren of Weymouth physician, Dr. Cotton Tufts, for the establishment of a public library. Part of the bequest included two wooden buildings at the corner of Washington and Commercial Streets in Weymouth Landing. The lower floor of these buildings was set up as the library.", LIBH)}
{Q("On January 1, 1880, with Miss Caroline A. Blanchard as the first librarian, the Tufts Library opened its doors to the public. The library had over 2,300 volumes, and within a year, it had almost as many borrowers as books.", LIBH)}
<p>A purpose-built brick library on the Tufts land opened October 6, 1892; a later main library at Weston Park opened in 1965 (same town history). Profiles: {PL("quincy-tufts", "Quincy Tufts")}, {PL("susannah-tufts-1797", "Susannah Tufts")}, {PL("cotton-tufts", "Dr. Cotton Tufts")}.</p>
{UNV("Portrait paintings of Quincy and Susannah that once hung in the 1892 reading room are reported in secondary accounts; their present location and copyright status are not confirmed, so they are not reproduced here.")}
</section>'''

_EXTRA_CW = EXTRA
def EXTRA(path):
    out = _EXTRA_CW(path)
    if path == "places.html":
        out = "{DIV}" + CW_PLACES + out
        # Link homestead blurb to new profile (string already in MAPS_HTML baked earlier - patch via note)
        out += ('{DIV}<section id="cotton-jr-homestead-note"><h2>Cotton Tufts Jr. Homestead</h2>'
                '<p>See also <a href="{P}profiles/cotton-tufts-jr.html">Cotton Tufts (1757&ndash;1833)</a> and <a href="{P}places.html#tufts-corner">Tufts Corner</a>. '
                'The homestead entry under Homesteads (246 Commercial Street) remains above.</p></section>')
    if path == "generations/19th-century.html":
        out += ('{DIV}<section id="weymouth-profiles"><h2>Weymouth profiles</h2><p>Expanded pages: '
                + PL("cotton-tufts", "Dr. Cotton Tufts") + ', '
                + PL("cotton-tufts-jr", "Cotton Tufts (1757&ndash;1833)") + ', '
                + PL("mercy-brooks-tufts", "Mercy Brooks Tufts") + ', '
                + PL("quincy-tufts", "Quincy Tufts") + ', '
                + PL("susannah-tufts-1797", "Susannah Tufts (1797&ndash;1877)")
                + '. Places: <a href="{P}places.html#tufts-corner">Tufts Corner</a> &middot; <a href="{P}places.html#tufts-library">Tufts Library</a>.</p></section>')
    if path == "profiles/cotton-tufts-jr.html":
        out += ('{DIV}<section id="store"><h2>Tufts &amp; Whittemore</h2><p>See <a href="{P}places.html#tufts-corner">Places: Tufts Corner</a>.</p></section>')
    if path == "profiles/quincy-tufts.html" or path == "profiles/susannah-tufts-1797.html":
        out += ('{DIV}<section id="library"><h2>Tufts Library</h2><p>See <a href="{P}places.html#tufts-library">Places: Tufts Library</a>.</p></section>')
    return out
