# Profiles for Tufts people named on the site who did not yet have one
# (Shannon, t315, Nov 26, 2026). Facts from the site plus Wyman, Brooks,
# Booth, Medford VRs, Littleton records, and the family record already cited
# on the site. Peter Tufts the surveyor (peter-tufts-1774) already exists.

_BTH24 = BTH(24) if "BTH" in dir() else (
    BOOTH + ', part 2, p. 24. <a href="' + BOOTH_URL + '7">Text (Perseus)</a>')
_BTH22 = BTH(22) if "BTH" in dir() else (
    BOOTH + ', part 2, p. 22. <a href="' + BOOTH_URL + '7">Text (Perseus)</a>')
_BTH23 = BOOTH + ', part 1, pp. 22&ndash;23. <a href="' + BOOTH_URL + '2">Text (Perseus)</a>'
_FSRC = ('&ldquo;A Medford Disaster of 1850,&rdquo; <em>Medford Historical Register</em> '
         'XLII, nos. 3&ndash;4 (September&ndash;December 1939), pp. 59&ndash;62')
_AHSP = ('Arlington Historical Society, portrait catalog no. 1915.7.1B, '
         '<a href="https://arlingtonhistorical.pastperfectonline.com/photo/F8D78A69-41C6-4E05-9734-560754397332">catalog record</a>')
_GAZ1774 = ('<em>Boston Gazette</em>, 17 and 24 October 1774. '
            'The notice is on the <a href="{P}collections.html#mary-tufts-horse">Collections page</a>')

# ---------- already-existing matches (do not create a second page) ----------
# Peter, son of Peter Tufts Jr.: profiles/peter-tufts-1774.html
# Aaron Tufts (1761-1781), son of William Tufts Jr.: profiles/aaron-tufts.html (not Peter Jr's son)

def _mp_link_in(slug, old, new, field="bio"):
    p = _up_get(slug)
    if p and old in p.get(field, "") and new not in p.get(field, ""):
        p[field] = p[field].replace(old, new)

# =====================================================================
# Edmund Tufts (1795-1859), printer
# =====================================================================
_mp_ed = "edmund-tufts-1795"
_nf_new(_mp_ed, "Edmund Tufts, Printer (1795&ndash;1859)", "13 August 1795 &ndash; 28 March 1859",
  "Charlestown, later Somerville, Mass.", "1795", "1859", "19th Century",
  "Son of Joseph Tufts (1760&ndash;1818) and Abigail Tufts; printer of Somerville",
  '<p>Edmund Tufts was born on 13 August 1795, a son of ' + PL("joseph-tufts-1760", "Joseph Tufts") + ' and his first wife, ' + PL("abigail-tufts-1761", "Abigail Tufts") + ', and died on 28 March 1859, aged 59 (' + WY(966) + '). He did not marry (' + WY(966) + ').</p>'
  + '<p>Booth, writing of the Winter Hill homestead, remembered him as the printer of early Somerville:</p>'
  + Q("Edmund was intimately connected with the early history of this town, and his sign on the old house, &lsquo;Edmund Tufts, Printer,&rsquo; is still remembered. For some years he did the printing for the new town of Somerville and its inhabitants, and we find his name on most of the early town reports. He issued a Somerville Directory in 1851, a pamphlet of thirty-two pages.", _BTH24)
  + '<p>The press is also on the <a href="{P}businesses.html#printer">Businesses</a> and <a href="{P}places.html#homesteads">Places</a> pages. Somerville was set off in 1842, in his lifetime.</p>',
  "<p>No military service is recorded for him.</p>",
  '<p>Father: ' + PL("joseph-tufts-1760", "Joseph Tufts (1760&ndash;1818)") + ', deacon, son of ' + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill") + ' and ' + PL("anne-adams-tufts", "Anne Adams Tufts") + '. Mother: ' + PL("abigail-tufts-1761", "Abigail Tufts (1761&ndash;1801)") + '. He was the eighth of eleven children of the first marriage, all living at his mother&rsquo;s death in 1801 (' + WY(966) + ').</p>',
  "",
  "<p>He did not marry (" + WY(966) + ").</p>",
  [("joseph-tufts-1760", "father Joseph Tufts (1760&ndash;1818)", "son Edmund Tufts, printer (1795&ndash;1859)"),
   ("abigail-tufts-1761", "mother Abigail Tufts (1761&ndash;1801)", "son Edmund Tufts, printer (1795&ndash;1859)"),
   ("anne-adams-tufts", "grandmother Anne Adams Tufts", "grandson Edmund Tufts, printer (1795&ndash;1859)")])

# =====================================================================
# Seth Tufts and his son Seth, brickmakers
# =====================================================================
_mp_st = "seth-tufts-brickmaker"
_mp_stj = "seth-tufts-jr-brickmaker"
_nf_new(_mp_st, "Seth Tufts, Brickmaker", "[dates not found] &ndash; [death date not found]",
  "Medford, Mass. (south of the Mystic, near the Middlesex Canal)", "", "", "19th Century",
  "Brickmaker at the &ldquo;Sodom&rdquo; yards; carried on the business with his son Seth",
  '<p>After the brothers Isaac, Jonathan and Ebenezer Tufts had opened brick-yards on the south side of the Mystic, Brooks wrote, the work passed to a later pair:</p>'
  + Q("After these gentlemen came Seth Tufts, who, with his son Seth, carried on the business till recently. These yards were situated near Middlesex Canal and the river, about south-south-east from Rock Hill.", BK(356))
  + '<p>Brooks was writing in 1855, so the two Seths were still remembered as recent occupants of the yards then. The street location, between Summer and George Streets on Brickyard Lane, is given on the <a href="{P}businesses.html#sodom-yards">Businesses page</a>. A Seth Tufts also appears among the Medford fishermen named in the town records (Brooks, p. 385).</p>'
  + UNV("Brooks gives neither dates nor parentage for this Seth, or for his son. Wyman records a Seth, born 1774, son of Isaac Tufts and Martha of Medford (p. 961; Brooks, Register of Families, has the same son born 14 September 1774). That Seth is of the right generation to have run a yard &ldquo;till recently&rdquo; before 1855, but Brooks does not name the brickmaker as Isaac&rsquo;s son, and the identification is not made here. Note: Pending further work."),
  "<p>No military service is recorded for him in the sources cited here.</p>",
  '<p>Son: ' + PL(_mp_stj, "Seth Tufts, his son, brickmaker") + ' (Brooks, p. 356). Parentage otherwise not established.</p>',
  "<strong>Identity:</strong> Brooks names him only as Seth Tufts, successor at the &ldquo;Sodom&rdquo; yards, and his son Seth, without dates. Note: Pending further work.",
  "<p>Not recorded in the sources cited here.</p>",
  [(_mp_stj, "son Seth Tufts, brickmaker", "father Seth Tufts, brickmaker")])
_nf_new(_mp_stj, "Seth Tufts, Brickmaker, the Son", "[dates not found] &ndash; [death date not found]",
  "Medford, Mass. (south of the Mystic, near the Middlesex Canal)", "", "", "19th Century",
  "Brickmaker with his father Seth at the &ldquo;Sodom&rdquo; yards",
  '<p>Brooks, in 1855, says that ' + PL(_mp_st, "Seth Tufts") + ', who succeeded Isaac, Jonathan and Ebenezer Tufts at the yards south of the Mystic, &ldquo;with his son Seth, carried on the business till recently&rdquo; (' + BK(356) + '). The son is not otherwise named in that account, and no dates are given for him.</p>',
  "<p>No military service is recorded for him in the sources cited here.</p>",
  '<p>Father: ' + PL(_mp_st, "Seth Tufts, brickmaker") + ' (Brooks, p. 356).</p>',
  "<strong>Dates and further identity</strong> have not been found. Note: Pending further work.",
  "<p>Not recorded in the sources cited here.</p>",
  [(_mp_st, "father Seth Tufts, brickmaker", "son Seth Tufts, brickmaker")])

# =====================================================================
# Jonathan Tufts, Mystic fisherman c. 1803
# =====================================================================
_mp_jf = "jonathan-tufts-fisherman"
_nf_new(_mp_jf, "Jonathan Tufts, Mystic Fisherman (fl. 1803)", "flourished about 1803",
  "Medford, Mass.", "", "", "19th Century",
  "Among the earliest holders of the town fishing right on the Mystic River",
  '<p>Brooks, in his chapter on the fishery, names him among the first men who paid the town for the right to fish in the Mystic:</p>'
  + Q("Among the earliest fishermen were John Cutter, Jonathan Tufts, and Benjamin Teel. In 1803, Cutter paid sixty-five dollars, Tufts thirteen dollars, and Teel thirteen dollars, for the right of fishing.", BK(385))
  + '<p>The fishery is described on the <a href="{P}businesses.html#fishing">Businesses page</a>.</p>'
  + UNV("Which Jonathan Tufts this was is not stated. " + PL("jonathan-tufts-36-8", "Jonathan Tufts (1739&ndash;1784)") + " died too early to be the man of 1803. No other identifying date, residence or family connection is given in Brooks. Note: Pending further work."),
  "<p>No military service is recorded for him in the sources cited here.</p>",
  "<p>Not established from the sources cited here.</p>",
  "<strong>Identity:</strong> Brooks names only &ldquo;Jonathan Tufts&rdquo; among the Mystic fishermen of about 1803, without dates or parentage. Note: Pending further work.",
  "<p>Not recorded in the sources cited here.</p>")

# =====================================================================
# Jonathan Tufts (c. 1659-1722), son of the immigrant; likely the tithing man
# =====================================================================
_mp_jt = "jonathan-tufts-1659"
_S44 = ('Wilson Fiske and Ruth Dame Coolidge, &ldquo;The Old Time Medford Town Meeting,&rdquo; '
        '<em>Medford Historical Register</em> XXXIV, no. 4 (December 1931), p. 44')
_nf_new(_mp_jt, "Jonathan Tufts (c. 1659&ndash;1722)", "about 2 May 1659 &ndash; 13 August 1722",
  "Malden and Medford, Mass.", "1659", "1722", "Colonial",
  "Son of Peter Tufts the immigrant; of Malden and Medford",
  '<p>Jonathan Tufts was a son of ' + PL("peter-tufts-1617", "Peter Tufts the immigrant") + ' and Mary (Pierce) Tufts, and a brother of ' + PL("peter-tufts-1648", "Capt. Peter Tufts") + ' and of John Tufts, the father of ' + PL("nathaniel-tufts-1692", "Nathaniel Tufts") + '. Wyman places him in Malden and Medford, and records his death on 13 August 1722, aged 63 years, 3 months and 11 days, with a gravestone at Malden, which would place his birth at about 2 May 1659 (' + WY(961) + ').</p>'
  + '<p>He married Rebecca Wait. Wyman lists nine children: Jonathan (1685&ndash;1688); James; John (b. 1688); Jonathan (b. 6 February 1690); Rebecca (b. 1694, m. John Willis); Samuel (b. 29 April 1697); Persis (b. 1700); Joseph (b. 1704); and Abigail (1707&ndash;1726) (' + WY(961) + ').</p>'
  + '<p>A 1931 account of an early Medford town meeting names a Jonathan Tufts as tithing man, with ' + PL("peter-tufts-1648", "Capt. Peter Tufts") + ' as moderator and selectman (' + _S44 + '). The identification of that officer with this Jonathan, Capt. Peter&rsquo;s brother, is likely, but it is not confirmed in the account. The scene is on ' + PL("peter-tufts-1648", "Capt. Peter Tufts&rsquo;s profile") + '.</p>',
  "<p>No military service is recorded for him in the sources cited here.</p>",
  '<p>Father: ' + PL("peter-tufts-1617", "Peter Tufts the immigrant (1617&ndash;1700)") + '. Mother: Mary Pierce (d. 1702/3). Brothers include ' + PL("peter-tufts-1648", "Capt. Peter Tufts (c. 1648&ndash;1721)") + ' and John Tufts (d. 1728), father of ' + PL("nathaniel-tufts-1692", "Nathaniel Tufts (1692&ndash;1741)") + ' (' + WY(961) + '; ' + WY(963) + ').</p>',
  "<strong>The tithing man</strong> of the early Medford town meeting in the 1931 Register is named only as Jonathan Tufts. That he was this Jonathan, brother of Capt. Peter, is likely from the date and the family, but it is not stated in the source. Note: Pending further work.",
  "<ul><li><strong>Rebecca Wait</strong>. Wyman records the marriage and her husband&rsquo;s death at Malden on 13 August 1722 (" + WY(961) + "). The date of the marriage has not been taken from a vital-record page here.</li></ul>",
  [("peter-tufts-1617", "father Peter Tufts the immigrant", "son Jonathan Tufts (c. 1659&ndash;1722)"),
   ("peter-tufts-1648", "brother Capt. Peter Tufts (c. 1648&ndash;1721)", "brother Jonathan Tufts (c. 1659&ndash;1722)"),
   ("nathaniel-tufts-1692", "nephew Nathaniel Tufts (1692&ndash;1741)", "uncle Jonathan Tufts (c. 1659&ndash;1722)")])

# =====================================================================
# "the Misses Tufts" (1850 Medford fire)
# =====================================================================
_mp_ms = "misses-tufts"
_nf_new(_mp_ms, "The Misses Tufts (fl. 1850)", "living in Medford, 1850",
  "Main Street, Medford, Mass.", "", "", "19th Century",
  "Occupants of the Main Street dwelling-house burned in the Medford fire of 21 November 1850",
  '<p>On the night of 21 November 1850 a fire burned some twenty-five buildings on Main Street in Medford, between the Mystic bridge and the Medford House. Among the buildings lost, the <em>Medford Historical Register</em> later recorded:</p>'
  + Q("The Misses Tufts&rsquo; dwelling-house, and Richard Tufts&rsquo; wheelwright shop, on the same side of Main Street, were also totally laid in ashes.", _FSRC + ', p. 60')
  + '<p>The fire is told on the profiles of ' + PL("richard-tufts-1804", "Richard Tufts, wheelwright") + ' and ' + PL("elias-tufts-1787", "Elias Tufts, wheelwright") + ', and on the <a href="{P}businesses.html">Businesses</a> page. The 1939 account does not give the given names of the &ldquo;Misses Tufts.&rdquo;</p>',
  "<p>No military service is recorded.</p>",
  '<p>The 1939 account does not identify them further. Richard Tufts&rsquo;s unmarried sisters Hannah (1801&ndash;1864) and Emily (1806&ndash;1895) were living in Medford in 1850 and are the likeliest candidates, since their house stood on the same side of Main Street as his shop; Elias Tufts&rsquo;s unmarried sister Mercy (1782&ndash;1855) is another possibility. Those identifications are discussed on ' + PL("richard-tufts-1804", "Richard Tufts&rsquo;s profile") + '.</p>',
  "<strong>Who the &ldquo;Misses Tufts&rdquo; were</strong> is not stated in the 1939 account. The identification with Richard Tufts&rsquo;s sisters Hannah and Emily, or with Elias Tufts&rsquo;s sister Mercy, remains unconfirmed. Note: Pending further work.",
  "<p>None recorded in the account of the fire; they are described as &ldquo;the Misses Tufts.&rdquo;</p>",
  [("richard-tufts-1804", "neighbor Richard Tufts, wheelwright, whose shop stood beside their house", "the Misses Tufts, whose Main Street house burned in 1850"),
   ("elias-tufts-1787", "Elias Tufts, wheelwright, whose shop and house also burned in the 1850 fire", "the Misses Tufts, whose Main Street house burned in 1850")])

# =====================================================================
# Mary Tufts, stray-horse notice, Medford, Oct 1774
# =====================================================================
_mp_my = "mary-tufts-1774"
_nf_new(_mp_my, "Mary Tufts of Medford (fl. 1774)", "flourished October 1774",
  "Medford, Mass.", "", "", "The Revolution",
  "Advertised a stray or stolen horse from her Medford pasture, October 1774",
  '<p>In October 1774 a Mary Tufts of Medford advertised in the <em>Boston Gazette</em> for a horse gone from her pasture:</p>'
  + Q("TWO DOLLARS REWARD. Strayed or Stolen out of the Pasture of Mary Tufts, in Medford, a large dark bay Horse, about 11 Years old, 15 Hands high &hellip; Whoever will bring said Horse to me the Subscriber, shall have the above Reward, and all necessary Charges paid by MARY TUFTS.",
     '<em>Boston Gazette</em>, 17 October 1774 (repeated 24 October 1774). The full notice is on the <a href="{P}collections.html#mary-tufts-horse">Collections page</a>')
  + '<p>The notice is the only mention of her gathered here. Several women named Mary Tufts lived in and around Medford in those years, and the subscriber is not further identified in the advertisement.</p>',
  "<p>No military service is recorded for her.</p>",
  "<p>Not established. The 1774 notice names only &ldquo;Mary Tufts, in Medford.&rdquo;</p>",
  "<strong>Which Mary Tufts of Medford</strong> placed the notice has not been established. Note: Pending further work.",
  "<p>Not recorded in the notice.</p>")

# =====================================================================
# Sally Tufts (Mrs. Amos Locke)
# =====================================================================
_mp_sa = "sally-tufts-locke"
_nf_new(_mp_sa, "Sally (Tufts) Locke (1789&ndash;1871)", "15 February 1789 &ndash; 12 August 1871",
  "Medford; Charlestown (Somerville); West Cambridge (Arlington), Mass.", "1789", "1871", "19th Century",
  "Daughter of Peter Tufts Jr. and Hannah Adams; wife of Amos Locke; her portrait is at the Arlington Historical Society",
  '<p>Sally Tufts was born in Medford on 15 February 1789, a daughter of ' + PL("peter-tufts-jr", "Peter Tufts Jr.") + ' and Hannah Adams (' + MV(152) + '; ' + TKV(235, "129-8") + '). On 12 October 1813, at West Cambridge (now Arlington), she married Amos Locke, son of Lieut. Samuel Locke Jr. and Margaret (Adams) Locke, and a brother of Martha Locke, the first wife of Sally&rsquo;s brother ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + '. Amos was born at Menotomy on 11 June 1785 and died at West Cambridge on 1 April 1843. They had no children. Sally died at Arlington on 12 August 1871 (' + TKV(235, "129-8") + ').</p>'
  + '<p>The Arlington Historical Society holds a portrait catalogued as &ldquo;Mrs Amos Locke nee Sally Tufts&rdquo; (no. 1915.7.1B). It is noted on the <a href="{P}collections.html">Collections page</a> (' + _AHSP + ').</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + '. Mother: Hannah Adams (d. 1816). Brothers and sisters with profiles on this site include ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', ' + PL("joel-tufts-1781", "Joel Tufts") + ', ' + PL("thomas-tufts-1785", "Thomas Tufts") + ' and ' + PL("aaron-tufts-1793", "Aaron Tufts") + '. Grandparents: ' + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill") + ' and ' + PL("anne-adams-tufts", "Anne Adams Tufts") + '.</p>',
  "<strong>The portrait</strong> is identified from the Society&rsquo;s catalog title; the painting itself has not been reproduced here, and the catalog does not state the artist or the date. Her birth is in the printed Medford vital records; her marriage, her husband&rsquo;s dates, her death at Arlington and that they had no children are from the family record and have not been re-checked against the printed Arlington vital records in this pass. Note: Pending further work.",
  "<ul><li><strong>Amos Locke</strong> (11 June 1785 &ndash; 1 April 1843), son of Lieut. Samuel Locke Jr. and Margaret (Adams) Locke of Menotomy (West Cambridge). Married 12 October 1813, at West Cambridge. No children (" + TKV(235, "129-8") + ").</li></ul>",
  [("peter-tufts-jr", "father Peter Tufts Jr. (1753&ndash;1832)", "daughter Sally (Tufts) Locke (1789&ndash;1871)"),
   ("peter-tufts-1774", "brother Peter Tufts the surveyor (1774&ndash;1825)", "sister Sally (Tufts) Locke (1789&ndash;1871)"),
   ("joel-tufts-1781", "brother Joel Tufts (1781&ndash;1852)", "sister Sally (Tufts) Locke (1789&ndash;1871)"),
   ("thomas-tufts-1785", "brother Thomas Tufts (1785&ndash;1844)", "sister Sally (Tufts) Locke (1789&ndash;1871)"),
   ("aaron-tufts-1793", "brother Aaron Tufts (1793&ndash;1881)", "sister Sally (Tufts) Locke (1789&ndash;1871)"),
   ("anne-adams-tufts", "grandmother Anne Adams Tufts", "granddaughter Sally (Tufts) Locke (1789&ndash;1871)")])

# =====================================================================
# Effie Tufts (musket donation, unconfirmed)
# =====================================================================
_mp_ef = "effie-tufts"
_nf_new(_mp_ef, "Effie Tufts", "dates not found",
  "Not established", "", "", "Modern",
  "Named in some accounts as a donor of Capt. Benjamin Locke&rsquo;s musket; the museum record does not name her",
  '<p>Some accounts state that the musket of Capt. Benjamin Locke of Menotomy (now Arlington), catalog no. 1924.5.1 at the Arlington Historical Society, was &ldquo;donated via Effie Tufts.&rdquo; The museum record instead says the gun was presented in 1924 by the children of Benjamin Delmont Locke and William Henry Locke, and names no Tufts. The notice is on the <a href="{P}collections.html">Collections page</a>.</p>'
  + '<p>The Lockes and the Tufts family did intermarry: ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ' married Martha Locke, and ' + PL("sally-tufts-locke", "Sally Tufts") + ' married Amos Locke. No source found here identifies an Effie Tufts in that connection, or gives her dates.</p>',
  "<p>No military service is recorded.</p>",
  "<p>Not established from the sources cited here.</p>",
  "<strong>The donation:</strong> the museum record of Capt. Benjamin Locke&rsquo;s musket does not name a Tufts donor. Who Effie Tufts was, and whether she had any part in the gift, has not been shown. Note: Pending further work.",
  "<p>Not recorded.</p>",
  [("sally-tufts-locke", "Sally (Tufts) Locke, whose husband was a Locke of the same Menotomy family", "Effie Tufts, named in some accounts of a Locke musket donation")])

# =====================================================================
# Nathaniel Tufts (1692-1741)
# =====================================================================
_mp_nt = "nathaniel-tufts-1692"
_nf_new(_mp_nt, "Nathaniel Tufts (1692&ndash;1741)", "23 February 1692 &ndash; 27 August 1741",
  "Medford and Charlestown (Washington Street near Union Square, now Somerville), Mass.", "1692", "1741", "Colonial",
  "Son of John Tufts of Malden; homestead on Washington Street near Union Square",
  '<p>Nathaniel Tufts was born at Medford on 23 February 1692, a son of John Tufts of Malden (himself a son of ' + PL("peter-tufts-1617", "Peter Tufts the immigrant") + ') and Mary (Putnam) Tufts, and a brother of ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + ' (' + WY(963) + ').</p>'
  + '<p>He married, first, Mary Sprague on 7 April 1715; she died on 15 December 1715, in her 26th year, and was buried at Charlestown. He married, second, Mary Rand on 18 October 1716; she died on 26 December 1764, aged 70, and was buried at Cambridge. Nathaniel died on 27 August 1741, &ldquo;in 53d yr.,&rdquo; with a gravestone (' + WY(963) + '). His children by the second marriage, as Wyman gives them, were Nathaniel (baptized 4 August 1717); William (died 1719, an infant) and William (born 30 June 1721); Mary (born 11 January 1722/3, m. John Morse); David (born 25 February 1724); John (born 13 February 1727); Timothy (born 2 February 1728/9); Persis (born 27 May 1733); and Isaiah (baptized 20 July 1740) (' + WY(963) + ').</p>'
  + '<p>Booth places his homestead on Washington Street near Union Square. By the Revolution the lot had passed to his son William, who died in 1773. A barrack was erected on the homestead lot during the siege of Boston, and Fort No. 3 took its beginning near the same point (' + _BTH23 + '). The homestead is on the <a href="{P}places.html#powder-house">Places page</a>. Wyman&rsquo;s William 33, brother of Nathaniel&rsquo;s eldest surviving son, died on 2 November 1773, aged 53, which fits Booth&rsquo;s William who died in 1773 (' + WY(964) + ').</p>',
  "<p>No military service is recorded for him.</p>",
  '<p>Father: John Tufts of Malden (d. 28 March 1728, aged 63), son of ' + PL("peter-tufts-1617", "Peter Tufts the immigrant") + '. Mother: Mary Putnam. Brother: ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + ', father of ' + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill") + '. Uncle: ' + PL("jonathan-tufts-1659", "Jonathan Tufts (c. 1659&ndash;1722)") + ' (' + WY(963) + ').</p>',
  "<strong>Age at death:</strong> Wyman reports the gravestone as &ldquo;in 53d yr.,&rdquo; which would imply a birth about 1688, four years earlier than the Medford birth of 23 February 1692. The birth record and Booth&rsquo;s dates (1692&ndash;1741) are followed here; the stone&rsquo;s stated age has not been re-read. Note: Pending further work.",
  "<ul><li><strong>Mary Sprague</strong> (d. 15 December 1715, in her 26th year, gravestone at Charlestown). Married 7 April 1715 (" + WY(963) + ").</li>"
  "<li><strong>Mary Rand</strong> (d. 26 December 1764, aged 70, gravestone at Cambridge). Married 18 October 1716. Administration on her estate was granted to her son William on 22 January 1765 (" + WY(963) + ").</li></ul>",
  [("peter-tufts-1617", "grandfather Peter Tufts the immigrant", "grandson Nathaniel Tufts (1692&ndash;1741)"),
   ("peter-tufts-1697", "brother Peter Tufts (1697&ndash;1776)", "brother Nathaniel Tufts (1692&ndash;1741)"),
   ("jonathan-tufts-1659", "uncle Jonathan Tufts (c. 1659&ndash;1722)", "nephew Nathaniel Tufts (1692&ndash;1741)"),
   ("peter-tufts-winter-hill", "nephew Peter Tufts of Winter Hill", "great-uncle Nathaniel Tufts (1692&ndash;1741)")])

# =====================================================================
# Abigail Tufts (1761-1801), wife of Joseph Tufts
# =====================================================================
_mp_ab = "abigail-tufts-1761"
_nf_new(_mp_ab, "Abigail Tufts (1761&ndash;1801)", "24 July 1761 &ndash; 9 October 1801",
  "Medford and Charlestown (now Somerville), Mass.", "1761", "1801", "The Revolution",
  "Daughter of James and Tabitha (Binford) Tufts; first wife of Joseph Tufts (1760&ndash;1818)",
  '<p>Abigail Tufts was born on 24 July 1761, a daughter of ' + PL("james-tufts-jr-36-2", "James Tufts") + ' and Tabitha (Binford) Tufts of Medford, and a sister of ' + PL("james-tufts-82-3", "James Tufts, potter") + ' (' + WY(960) + ').</p>'
  + '<p>On 31 March 1783 she married ' + PL("joseph-tufts-1760", "Joseph Tufts") + ', son of ' + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill") + ' and ' + PL("anne-adams-tufts", "Anne Adams Tufts") + '. She died at Medford, in child-bed, on 9 October 1801, aged 40 (39 on her tablet), and was carried to Charlestown (' + WY(966) + '). Joseph later married Hannah Williams, and died on 17 December 1818, aged 58.</p>'
  + '<p>All eleven of their children were by Abigail, and all were living at her death: Joseph (b. 5 October 1783); Abigail (b. 24 March 1785, still single at Somerville in 1866); Lydia (1786&ndash;1808); Bernard (b. 27 August 1788); Asa (b. 25 May 1790); Lucy (b. 6 January 1792); Mary (1793&ndash;1820); ' + PL("edmund-tufts-1795", "Edmund, the printer") + ' (1795&ndash;1859); Mercy (1797&ndash;1820); Harriet (b. 7 April 1799); and Caroline (b. 17 September 1801) (' + WY(966) + ').</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("james-tufts-jr-36-2", "James Tufts") + ' of Medford, who married Tabitha Binford. Brother: ' + PL("james-tufts-82-3", "James Tufts, potter (1755&ndash;1810)") + '. Husband: ' + PL("joseph-tufts-1760", "Joseph Tufts (1760&ndash;1818)") + '. Son: ' + PL("edmund-tufts-1795", "Edmund Tufts, printer (1795&ndash;1859)") + '. Mother-in-law: ' + PL("anne-adams-tufts", "Anne Adams Tufts") + '.</p>',
  "",
  "<ul><li><strong>Joseph Tufts</strong> (12 July 1760 &ndash; 17 December 1818), son of Peter and Anne (Adams) Tufts of Winter Hill. Married 31 March 1783. After Abigail&rsquo;s death he married Hannah Williams, 11 July 1802, at Medford (" + WY(966) + "; Adams genealogy, p. 973).</li></ul>",
  [("joseph-tufts-1760", "husband Joseph Tufts (1760&ndash;1818)", "first wife Abigail Tufts (1761&ndash;1801)"),
   ("james-tufts-jr-36-2", "father James Tufts of Medford", "daughter Abigail Tufts (1761&ndash;1801)"),
   ("james-tufts-82-3", "brother James Tufts, potter (1755&ndash;1810)", "sister Abigail Tufts (1761&ndash;1801)"),
   ("edmund-tufts-1795", "son Edmund Tufts, printer (1795&ndash;1859)", "mother Abigail Tufts (1761&ndash;1801)"),
   ("anne-adams-tufts", "mother-in-law Anne Adams Tufts", "daughter-in-law Abigail Tufts (1761&ndash;1801)")])

# =====================================================================
# Katherine/Catherine (Tufts) Tufts (b. 1734)
# =====================================================================
_mp_ka = "katherine-tufts-1734"
_nf_new(_mp_ka, "Katherine (Tufts) Tufts (b. 1734)", "31 March 1734 &ndash; [death date not found]",
  "Medford, Mass.", "1734", "", "The Revolution",
  "Daughter of Lieut. William Tufts; wife of William Tufts Jr., the Medford mariner; mother of Ebenezer, Eliakim, and William (d. 1777)",
  '<p>Katherine (also Catherine, and Catharine in Wyman) Tufts was born on 31 March 1734, the eldest child of ' + PL("william-tufts-13-6", "Lieut. William Tufts") + ' of Medford by his first wife, Catharine Wyman (' + WY(961) + ').</p>'
  + '<p>On 10 January 1750 she married her cousin William Tufts Jr., a mariner of Medford, son of John Tufts. He died on 25 May 1771, aged 44, &ldquo;left widow and children&rdquo; (<em>Essex Gazette</em>, as cited by Wyman). She married, second, Nathaniel Wyman in 1772, and third, Eben Richardson in 1776 (' + WY(961) + ').</p>'
  + '<p>Among her children by William were ' + PL("ebenezer-tufts-87-4", "Ebenezer Tufts (1761&ndash;1830)") + ', ' + PL("william-tufts-1777", "William Tufts (1762&ndash;1777)") + ', who was killed in the Revolutionary service, and ' + PL("eliakim-tufts-87-6", "Eliakim Tufts (1767&ndash;1825)") + '. Wild records William as &ldquo;Son of William and Catherine (Tufts); born 1762; killed 1777.&rdquo;</p>',
  "<p>No military service is recorded for her. Her son William served and was killed in 1777; Ebenezer was a Revolutionary pensioner.</p>",
  '<p>Father: ' + PL("william-tufts-13-6", "Lieut. William Tufts (1713&ndash;1783)") + '. Mother: Catharine Wyman (d. 20 February 1748/9, aged 32). Husband: William Tufts Jr., mariner, of Medford (d. 25 May 1771, aged 44), son of John Tufts. Children with profiles on this site: ' + PL("ebenezer-tufts-87-4", "Ebenezer") + ', ' + PL("william-tufts-1777", "William (d. 1777)") + ', ' + PL("eliakim-tufts-87-6", "Eliakim") + ' (' + WY(961) + ').</p>',
  "<strong>Death:</strong> the date of Katherine&rsquo;s own death has not been found in Wyman or in the compiled accounts cited on her children&rsquo;s pages. <strong>The number of children</strong> by William is given by Wyman only as &ldquo;6 or 7.&rdquo; Note: Pending further work.",
  "<ul><li><strong>William Tufts Jr.</strong>, mariner, of Medford, son of John Tufts; died 25 May 1771, aged 44. Married 10 January 1750 (" + WY(961) + ").</li>"
  "<li><strong>Nathaniel Wyman</strong>. Married 1772 (" + WY(961) + ").</li>"
  "<li><strong>Eben Richardson</strong>. Married 1776 (" + WY(961) + ").</li></ul>",
  [("william-tufts-13-6", "father Lieut. William Tufts (1713&ndash;1783)", "daughter Katherine (Tufts) Tufts (b. 1734)"),
   ("ebenezer-tufts-87-4", "son Ebenezer Tufts (1761&ndash;1830)", "mother Katherine (Tufts) Tufts (b. 1734)"),
   ("william-tufts-1777", "son William Tufts (1762&ndash;1777)", "mother Katherine (Tufts) Tufts (b. 1734)"),
   ("eliakim-tufts-87-6", "son Eliakim Tufts (1767&ndash;1825)", "mother Katherine (Tufts) Tufts (b. 1734)")])

# =====================================================================
# Rowland Cotton Tufts (1763-1768)
# =====================================================================
_mp_rc = "rowland-cotton-tufts"
_nf_new(_mp_rc, "Rowland Cotton Tufts (1763&ndash;1768)", "1 March 1763 &ndash; 10 June 1768",
  "Fort Cumberland and Halifax, Nova Scotia", "1763", "1768", "Colonial",
  "Son of Rev. Joshua Tufts; died in childhood at Halifax",
  '<p>Rowland Cotton Tufts was a son of ' + PL("joshua-tufts-hc1736", "Rev. Joshua Tufts") + ' and Abigail (Ellery) Tufts. The family record gives his birth as 1 March 1763, at Fort Cumberland, Nova Scotia (now Fort Beauséjour), and his death as 10 June 1768, at Halifax, a child (' + TKV(69, "28-13") + '). He is named with his brothers and sisters on his father&rsquo;s profile. The given names recall the Cotton family, from which several New England Tuftses also descend.</p>',
  "<p>No military service is recorded; he died in childhood.</p>",
  '<p>Father: ' + PL("joshua-tufts-hc1736", "Rev. Joshua Tufts (1716&ndash;1767)") + '. Mother: Abigail (Ellery) Tufts. Brothers with profiles on this site include ' + PL("samuel-tufts-28-11", "Capt. Samuel Tufts (1758&ndash;1819)") + '.</p>',
  "<strong>Dates:</strong> his birth and death are taken from the family record (Vol. I, p. 69, no. 28-13) and have not been re-checked against a Halifax or Fort Cumberland register in this pass. An earlier note on his father&rsquo;s page gave the birth as about 1766. Note: Pending further work.",
  "<p>He died in childhood; no marriage is recorded.</p>",
  [("joshua-tufts-hc1736", "father Rev. Joshua Tufts (1716&ndash;1767)", "son Rowland Cotton Tufts (1763&ndash;1768)"),
   ("samuel-tufts-28-11", "brother Capt. Samuel Tufts (1758&ndash;1819)", "brother Rowland Cotton Tufts (1763&ndash;1768)")])

# =====================================================================
# Annie Louise Tufts (1839-1917)
# =====================================================================
_mp_al = "annie-louise-tufts"
_nf_new(_mp_al, "Annie Louise (Tufts) Fletcher (1839&ndash;1917)", "31 October 1839 &ndash; 7 October 1917",
  "Charlestown, later Somerville (Sycamore Street), Mass.", "1839", "1917", "19th Century",
  "Only child of Oliver Tufts; born in the Sycamore Street house; wife of Dr. William Kelley Fletcher",
  '<p>Annie Louise Tufts was the only child of ' + PL("oliver-tufts-1801", "Oliver Tufts") + '. She was born in the family house on Sycamore Street, Charlestown (later Somerville), on 31 October 1839. She married Dr. William Kelley Fletcher in 1874 and died in Somerville on 7 October 1917, leaving no children (' + TKV2(158, "302-1") + '). The house is described on her father&rsquo;s profile and on the <a href="{P}places.html">Places</a> page.</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("oliver-tufts-1801", "Oliver Tufts (1801&ndash;1883)") + '. Grandfather: ' + PL("john-tufts-53-3", "John Tufts (1754&ndash;1839)") + '. She was her father&rsquo;s only child, and she left no children.</p>',
  "<strong>Dates:</strong> her birth, marriage, death and that she left no children are from the family record (Vol. II, p. 158, no. 302-1), as already cited on her father&rsquo;s profile, and have not been re-checked against a Somerville vital record in this pass. Note: Pending further work.",
  "<ul><li><strong>Dr. William Kelley Fletcher</strong>. Married 1874 (" + TKV2(158, "302-1") + ").</li></ul>",
  [("oliver-tufts-1801", "father Oliver Tufts (1801&ndash;1883)", "daughter Annie Louise (Tufts) Fletcher (1839&ndash;1917)"),
   ("john-tufts-53-3", "grandfather John Tufts (1754&ndash;1839)", "granddaughter Annie Louise (Tufts) Fletcher (1839&ndash;1917)")])

# =====================================================================
# Edith Tufts Shaw and Jessie May Tufts
# =====================================================================
_mp_es = "edith-tufts-shaw"
_mp_jm = "jessie-may-tufts"
_nf_new(_mp_es, "Edith (Tufts) Shaw (b. 1878)", "7 October 1878 &ndash; [death date not found]",
  "Sacramento, Calif.", "1878", "", "19th Century",
  "Daughter of Albert C. Tufts, the Sacramento druggist; later Edith Tufts Shaw",
  '<p>Edith Tufts was a daughter of ' + PL("albert-c-tufts", "Albert C. Tufts") + ', the Sacramento druggist. A Social Security-derived index gives her birth as 7 October 1878, at Sacramento, under the married name Edith Tufts Shaw. Sacramento city directories place &ldquo;Tufts Edith Miss&rdquo; at the family addresses in the late 1890s, and in 1902 list her as a teacher at the Union Primary School, residing at 817 18th Street. She is named with her father, Mrs. Eva Nelson Tufts, and her sister ' + PL("jessie-may-tufts", "Jessie May Tufts") + ' in the historic-churches index of St. Paul&rsquo;s Episcopal Church, Sacramento (1852&ndash;1910). The directory record is gathered on her father&rsquo;s profile and on the <a href="{P}generations/19th-century.html#albert-c-tufts">19th Century</a> page.</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("albert-c-tufts", "Albert C. Tufts") + '. Sister: ' + PL("jessie-may-tufts", "Jessie May Tufts") + '. The family&rsquo;s tie to the Massachusetts Tufts lines has not been established.</p>',
  "<strong>Death date and husband&rsquo;s name</strong> (beyond the married surname Shaw in a Social Security-derived index) have not been found. The birth date is from that index, not from a Sacramento vital-record page seen here. Note: Pending further work.",
  "<p>Married name Shaw, from a Social Security-derived index; the husband&rsquo;s full name and the date of the marriage have not been found.</p>",
  [("albert-c-tufts", "father Albert C. Tufts", "daughter Edith (Tufts) Shaw (b. 1878)"),
   ("jessie-may-tufts", "sister Jessie May Tufts", "sister Edith (Tufts) Shaw (b. 1878)")])
_nf_new(_mp_jm, "Jessie May Tufts", "dates not found (living in Sacramento, 1890s)",
  "Sacramento, Calif.", "", "", "19th Century",
  "Daughter of Albert C. Tufts, the Sacramento druggist",
  '<p>Jessie May Tufts was a daughter of ' + PL("albert-c-tufts", "Albert C. Tufts") + '. Sacramento city directories list her with her sister ' + PL("edith-tufts-shaw", "Edith") + ' at 1605 H Street in 1897, and in 1899 as &ldquo;Tufts Jessie Miss, emp State Print[ing Office],&rdquo; after Albert himself has dropped from the directory. She is named with Albert, Edith, and Mrs. Eva Nelson Tufts in the historic-churches index of St. Paul&rsquo;s Episcopal Church, Sacramento (1852&ndash;1910). The directory record is gathered on her father&rsquo;s profile.</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("albert-c-tufts", "Albert C. Tufts") + '. Sister: ' + PL("edith-tufts-shaw", "Edith (Tufts) Shaw") + '. The family&rsquo;s tie to the Massachusetts Tufts lines has not been established.</p>',
  "<strong>Birth and death dates</strong> have not been found. The directories give no age. Note: Pending further work.",
  "<p>Not recorded in the directories cited here; she appears as &ldquo;Tufts Jessie Miss.&rdquo;</p>",
  [("albert-c-tufts", "father Albert C. Tufts", "daughter Jessie May Tufts"),
   ("edith-tufts-shaw", "sister Edith (Tufts) Shaw (b. 1878)", "sister Jessie May Tufts")])

# =====================================================================
# Daranda / Dorinda Tufts of Littleton, 1825
# =====================================================================
_mp_da = "daranda-tufts"
_nf_new(_mp_da, "Dorinda (&ldquo;Daranda&rdquo;) Tufts (fl. 1825)", "flourished 1825",
  "Littleton, Mass.", "", "", "19th Century",
  "Daughter of Eliakim Tufts of Littleton; marriage intention to Leonard Porter of Carlisle, 1 May 1825",
  '<p>A few weeks after the death of ' + PL("eliakim-tufts-87-6", "Eliakim Tufts") + ' of Littleton (19 February 1825), the town recorded the intention of marriage of &ldquo;Leonard Porter of Carlisle and Daranda Tufts of Littleton, May 1st 1825&rdquo; (' + LIT("p. 282", 292) + '). The entry is quoted on Eliakim&rsquo;s profile, which identifies her as his daughter Dorinda.</p>',
  "<p>No military service is recorded for her.</p>",
  '<p>Father: ' + PL("eliakim-tufts-87-6", "Eliakim Tufts (1767&ndash;1825)") + ' of Medford, Billerica, Groton and Littleton. The compiled list of Eliakim&rsquo;s children on his profile includes a daughter in this generation; the Littleton intention is the contemporary record of her name and residence in 1825.</p>',
  "<strong>Birth, death and the marriage itself</strong> (beyond the 1 May 1825 intention) have not been taken from a vital record in this pass. The spelling Daranda is the town clerk&rsquo;s; Dorinda is the form used in the compiled account of her father&rsquo;s family. Note: Pending further work.",
  "<ul><li><strong>Leonard Porter</strong> of Carlisle. Intention of marriage recorded at Littleton, 1 May 1825 (" + LIT("p. 282", 292) + "). Whether the marriage took place, and his dates, have not been confirmed here.</li></ul>",
  [("eliakim-tufts-87-6", "father Eliakim Tufts (1767&ndash;1825)", "daughter Dorinda (&ldquo;Daranda&rdquo;) Tufts")])

# =====================================================================
# Peter Jr's sons Joel, Thomas, Aaron (Peter the surveyor already exists)
# =====================================================================
_mp_jo = "joel-tufts-1781"
_mp_th = "thomas-tufts-1785"
_mp_aa = "aaron-tufts-1793"
_nf_new(_mp_jo, "Joel Tufts (1781&ndash;1852)", "22 December 1781 &ndash; 4 May 1852",
  "Medford and Charlestown (Somerville), Mass.; later Peterborough, N.H.", "1781", "1852", "19th Century",
  "Son of Peter Tufts Jr. and Hannah Adams",
  '<p>Joel Tufts was a son of ' + PL("peter-tufts-jr", "Peter Tufts Jr.") + ' and Hannah Adams. The family record gives his birth as 22 December 1781, at Medford, and his death as 4 May 1852, at Peterborough, New Hampshire (' + TKV(234, "129-4") + '). Booth, writing of the eleven children of Peter and Hannah, says that Peter (the surveyor) and Joel stayed in Somerville, while Thomas and Aaron settled in New York State (' + _BTH22 + ').</p>'
  + '<p>He married, first, on 13 January 1805 at Menotomy (now Arlington), Sarah Butterfield, daughter of William and Deborah (Locke) Butterfield; she died at West Cambridge on 14 November 1821. Their children, as the family record lists them, were Joel, Amanda, Sarah, Rebecca and Hannah. He married, second, on 23 October 1828 at Peterborough, Rebecca Brackett; they had no children (' + TKV(234, "129-4") + ').</p>'
  + UNV("Wyman&rsquo;s list of the children of Peter 38 (p. 965) names Peter, Hannah, Anna, Thomas, Rebecca, Sally, Aaron, Eliza and Lucretia, but not Joel. Booth and the family record both include him. Booth&rsquo;s statement that Joel stayed in Somerville describes his earlier residence; the family record places his death at Peterborough. Note: Pending further work."),
  "<p>No military service is recorded for him in the sources cited here.</p>",
  '<p>Father: ' + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + '. Mother: Hannah Adams (d. 1816). Brothers and sisters with profiles on this site: ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', ' + PL("thomas-tufts-1785", "Thomas") + ', ' + PL("aaron-tufts-1793", "Aaron") + ', ' + PL("sally-tufts-locke", "Sally (Tufts) Locke") + '.</p>',
  "<strong>Dates</strong> of birth, marriage and death are from the family record (Vol. I, p. 234, no. 129-4) and have not been re-checked against a Medford or Peterborough vital-record page in this pass. Wyman omits him from the children of Peter 38. Note: Pending further work.",
  "<ul><li><strong>Sarah Butterfield</strong> (7 March 1784 &ndash; 14 November 1821), daughter of William and Deborah (Locke) Butterfield. Married 13 January 1805, at Menotomy (" + TKV(234) + ").</li>"
  "<li><strong>Rebecca Brackett</strong> (6 July 1801 &ndash; 4 July 1880), daughter of Josiah and Mary (Stuart) Brackett. Married 23 October 1828, at Peterborough, N.H. No children. She later married Norton Hunt, 14 March 1861 (" + TKV(234) + ").</li></ul>",
  [("peter-tufts-jr", "father Peter Tufts Jr. (1753&ndash;1832)", "son Joel Tufts (1781&ndash;1852)"),
   ("peter-tufts-1774", "brother Peter Tufts the surveyor (1774&ndash;1825)", "brother Joel Tufts (1781&ndash;1852)"),
   ("thomas-tufts-1785", "brother Thomas Tufts (1785&ndash;1844)", "brother Joel Tufts (1781&ndash;1852)"),
   ("aaron-tufts-1793", "brother Aaron Tufts (1793&ndash;1881)", "brother Joel Tufts (1781&ndash;1852)"),
   ("sally-tufts-locke", "sister Sally (Tufts) Locke (1789&ndash;1871)", "brother Joel Tufts (1781&ndash;1852)")])
_nf_new(_mp_th, "Thomas Tufts (1785&ndash;1844)", "22 March 1785 &ndash; 23 January 1844",
  "Medford, Mass.; later Utica and LeRoy, N.Y.", "1785", "1844", "19th Century",
  "Son of Peter Tufts Jr.; settled in New York State; land agent",
  '<p>Thomas Tufts was a son of ' + PL("peter-tufts-jr", "Peter Tufts Jr.") + ' and Hannah Adams. The family record gives his birth as 22 March 1785, at Medford, and his death as 23 January 1844, at Utica, New York (' + TKV("234&ndash;235", "129-6") + '; ' + MV(153) + '). Booth says that, of Peter and Hannah&rsquo;s sons, Thomas and Aaron settled in New York State (' + _BTH22 + '). Wyman names Thomas among the children of Peter 38, without dates (' + WY(965) + ').</p>'
  + '<p>The family record calls him a land agent, and names his wife as Sarah Barrows, with a marriage at Greenwich, Massachusetts, and children Sarah A., Andrew C., Caroline, Lucretia and Thomas B. (' + TKV("234&ndash;235", "129-6") + ').</p>',
  '<p>The family record states that during the War of 1812 he served New York as an ensign and paymaster of a light-infantry company (' + TKV(235) + '). No muster roll has been seen in this pass.</p>',
  '<p>Father: ' + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + '. Mother: Hannah Adams (d. 1816). Brothers and sisters with profiles on this site: ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', ' + PL("joel-tufts-1781", "Joel") + ', ' + PL("aaron-tufts-1793", "Aaron") + ', ' + PL("sally-tufts-locke", "Sally (Tufts) Locke") + '.</p>',
  "<strong>The year of his marriage</strong> to Sarah Barrows has not been confirmed from a vital record (a compiled entry gives a year that is clearly impossible). <strong>War of 1812 service</strong> is from the family record only; no muster roll has been seen. Note: Pending further work.",
  "<ul><li><strong>Sarah Barrows</strong>, daughter of Daniel and Lydia (Tuttle) Barrows, of a marriage at Greenwich, Massachusetts. The family record gives her dates as 27 March 1785 (Mansfield, Conn.) &ndash; 15 November 1857 (LeRoy, N.Y.) (" + TKV("234&ndash;235") + "). The year of the marriage has not been confirmed.</li></ul>",
  [("peter-tufts-jr", "father Peter Tufts Jr. (1753&ndash;1832)", "son Thomas Tufts (1785&ndash;1844)"),
   ("peter-tufts-1774", "brother Peter Tufts the surveyor (1774&ndash;1825)", "brother Thomas Tufts (1785&ndash;1844)"),
   ("joel-tufts-1781", "brother Joel Tufts (1781&ndash;1852)", "brother Thomas Tufts (1785&ndash;1844)"),
   ("aaron-tufts-1793", "brother Aaron Tufts (1793&ndash;1881)", "brother Thomas Tufts (1785&ndash;1844)"),
   ("sally-tufts-locke", "sister Sally (Tufts) Locke (1789&ndash;1871)", "brother Thomas Tufts (1785&ndash;1844)")])
_nf_new(_mp_aa, "Aaron Tufts (1793&ndash;1881)", "5 November 1793 &ndash; 8 May 1881",
  "Medford, Mass.; later Pavilion, Genesee County, N.Y.", "1793", "1881", "19th Century",
  "Son of Peter Tufts Jr.; farmer who settled in New York State",
  '<p>Aaron Tufts was a son of ' + PL("peter-tufts-jr", "Peter Tufts Jr.") + ' and Hannah Adams. The family record gives his birth as 5 November 1793, at Medford, and his death as 8 May 1881, at Pavilion, Genesee County, New York, and calls him a farmer (' + TKV(235, "129-10") + '; ' + MV(145) + '). Booth says that Thomas and Aaron settled in New York State (' + _BTH22 + '). Wyman names Aaron among the children of Peter 38, without dates (' + WY(965) + '). He is not the earlier ' + PL("aaron-tufts", "Aaron Tufts (1761&ndash;1781)") + ', who died a prisoner at Mill Prison.</p>'
  + '<p>He married, first, on 21 September 1817 at Bethany, New York, Mehitable Pearson, who died at Pavilion on 7 April 1831; they had six children. He married, second, in March 1833 at Covington, New York, Keziah (Townsend) Perry, a widow; they had no children (' + TKV(235, "129-10") + ').</p>',
  '<p>The family record states that he served New York as a soldier in the War of 1812 (' + TKV(236) + '). No muster roll has been seen in this pass.</p>',
  '<p>Father: ' + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + '. Mother: Hannah Adams (d. 1816). Brothers and sisters with profiles on this site: ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', ' + PL("joel-tufts-1781", "Joel") + ', ' + PL("thomas-tufts-1785", "Thomas") + ', ' + PL("sally-tufts-locke", "Sally (Tufts) Locke") + '.</p>',
  "<strong>Dates</strong> of birth, marriage and death are from the family record (Vol. I, pp. 235&ndash;236, no. 129-10); the Medford birth is also in the printed vital records. <strong>War of 1812 service</strong> is from the family record only; no muster roll has been seen. Note: Pending further work.",
  "<ul><li><strong>Mehitable Pearson</strong> (19 December 1794 &ndash; 7 April 1831), daughter of William Ely and Mehitable (Reeves) Pearson. Married 21 September 1817, at Bethany, N.Y. Six children (" + TKV(235) + ").</li>"
  "<li><strong>Keziah (Townsend) Perry</strong> (1799 &ndash; 18 October 1876), widow. Married March 1833, at Covington, N.Y. No children (" + TKV(235) + ").</li></ul>",
  [("peter-tufts-jr", "father Peter Tufts Jr. (1753&ndash;1832)", "son Aaron Tufts (1793&ndash;1881)"),
   ("peter-tufts-1774", "brother Peter Tufts the surveyor (1774&ndash;1825)", "brother Aaron Tufts (1793&ndash;1881)"),
   ("joel-tufts-1781", "brother Joel Tufts (1781&ndash;1852)", "brother Aaron Tufts (1793&ndash;1881)"),
   ("thomas-tufts-1785", "brother Thomas Tufts (1785&ndash;1844)", "brother Aaron Tufts (1793&ndash;1881)"),
   ("sally-tufts-locke", "sister Sally (Tufts) Locke (1789&ndash;1871)", "brother Aaron Tufts (1793&ndash;1881)"),
   ("aaron-tufts", "Aaron Tufts (1761&ndash;1781) of Medford, a different man", "Aaron Tufts (1793&ndash;1881), son of Peter Tufts Jr., a different man")])

# ---------- Reciprocal wording on existing profiles ----------
_mp_link_in("joseph-tufts-1760", "Abigail Tufts (Adams genealogy, p. 973)",
            PL(_mp_ab, "Abigail Tufts (1761&ndash;1801)") + " (Wyman, p. 966; Adams genealogy, p. 973)", "family")
if "joseph-tufts-1760" in SP and "abigail-tufts-1761.html" not in SP["joseph-tufts-1760"]:
    _js = SP["joseph-tufts-1760"]
    _js = _js.replace("<strong>Abigail Tufts</strong> (Adams genealogy, p. 973).",
                      "<strong>" + PL(_mp_ab, "Abigail Tufts (1761&ndash;1801)") + "</strong> (Wyman, p. 966; Adams genealogy, p. 973).")
    _js = _js.replace("Abigail Tufts (Adams genealogy, p. 973).",
                      PL(_mp_ab, "Abigail Tufts (1761&ndash;1801)") + " (Wyman, p. 966; Adams genealogy, p. 973).")
    SP["joseph-tufts-1760"] = _js
_mp_link_in("oliver-tufts-1801", "Annie Louise Tufts", PL(_mp_al, "Annie Louise Tufts"), "bio")
_mp_link_in("oliver-tufts-1801", "Annie Louise (1839&ndash;1917)", PL(_mp_al, "Annie Louise (1839&ndash;1917)"), "family")
_mp_link_in("joshua-tufts-hc1736", "Rowland Cotton Tufts, born about 1766",
            PL(_mp_rc, "Rowland Cotton Tufts (1763&ndash;1768)"), "family")
_mp_link_in("eliakim-tufts-87-6", "Daranda Tufts of Littleton",
            PL(_mp_da, "Daranda Tufts of Littleton"), "bio")
_mp_link_in("eliakim-tufts-87-6", "She was his daughter Dorinda.",
            "She was his daughter " + PL(_mp_da, "Dorinda") + ".", "bio")
_mp_link_in("eliakim-tufts-87-6", "Parents: William Tufts and Katherine (Tufts) Tufts",
            "Parents: William Tufts and " + PL(_mp_ka, "Katherine (Tufts) Tufts"), "family")
_mp_link_in("ebenezer-tufts-87-4", "William and Katherine (Tufts) Tufts",
            "William and " + PL(_mp_ka, "Katherine (Tufts) Tufts"), "bio")
_mp_link_in("ebenezer-tufts-87-4", "Parents: William and Katherine (Tufts) Tufts",
            "Parents: William and " + PL(_mp_ka, "Katherine (Tufts) Tufts"), "family")
_mp_link_in("william-tufts-1777", "William and Catherine (Tufts) Tufts",
            "William and " + PL(_mp_ka, "Catherine (Tufts) Tufts"), "bio")
_mp_link_in("william-tufts-1777", "Son of William and Catherine (Tufts) Tufts",
            "Son of William and " + PL(_mp_ka, "Catherine (Tufts) Tufts"), "line")
# Albert's daughters: link names in bio if present as plain text
for _fld in ("bio", "family"):
    _mp_link_in("albert-c-tufts", "Edith Tufts Shaw", PL(_mp_es, "Edith Tufts Shaw"), _fld)
    _mp_link_in("albert-c-tufts", "Jessie May Tufts", PL(_mp_jm, "Jessie May Tufts"), _fld)
_mp_link_in("james-tufts-82-3", "Father: " + PL("james-tufts-jr-36-2", "James Tufts") + ".",
            "Father: " + PL("james-tufts-jr-36-2", "James Tufts") + ". Sister: " + PL(_mp_ab, "Abigail Tufts (1761&ndash;1801)") + ", wife of " + PL("joseph-tufts-1760", "Joseph Tufts") + ".",
            "family")
# Peter Jr.: append a short children note if not already listing Joel as a link
_pjr = _up_get("peter-tufts-jr")
if _pjr and "joel-tufts-1781.html" not in _pjr.get("bio", ""):
    _pjr["bio"] = _pjr.get("bio", "") + (
        '<p>His children included ' + PL("peter-tufts-1774", "Peter Tufts the surveyor") + ', '
        + PL(_mp_jo, "Joel") + ', ' + PL(_mp_th, "Thomas") + ' and ' + PL(_mp_aa, "Aaron") + ', and his daughter '
        + PL(_mp_sa, "Sally") + ', who married Amos Locke (Booth, p. 22; ' + WY(965) + '; '
        + TKV("105, 232&ndash;236") + ').</p>')

# ---------- Linkify businesses / places / collections ----------
def _mp_linkify(html):
    if not html or "edmund-tufts-1795.html" in html and "nathaniel-tufts-1692.html" in html:
        # still apply remaining replacements one by one
        pass
    pairs = [
        ('son of Joseph Tufts (1760&ndash;1819)',
         'son of ' + PL("joseph-tufts-1760", "Joseph Tufts (1760&ndash;1818)") + ', father of ' + PL(_mp_ed, "Edmund Tufts, printer")),
        ('Edmund Tufts, Printer',
         PL(_mp_ed, "Edmund Tufts, Printer")),
        ('his son Edmund later hung the sign',
         'his son ' + PL(_mp_ed, "Edmund") + ' later hung the sign'),
        ('The printer was her grandson Edmund Tufts',
         'The printer was her grandson ' + PL(_mp_ed, "Edmund Tufts")),
        ('later Seth Tufts and his son Seth',
         'later ' + PL(_mp_st, "Seth Tufts") + ' and his son ' + PL(_mp_stj, "Seth")),
        ('came Seth Tufts, who, with his son Seth,',
         'came ' + PL(_mp_st, "Seth Tufts") + ', who, with his son ' + PL(_mp_stj, "Seth") + ','),
        ('John Cutter, Jonathan Tufts, and Benjamin Teel',
         'John Cutter, ' + PL(_mp_jf, "Jonathan Tufts") + ', and Benjamin Teel'),
        ('Which Jonathan, Isaac, Charles, Simon and Seth Tufts these were.',
         'Which Jonathan, Isaac, Charles, Simon and Seth Tufts these were. A profile of the 1803 fisherman is at ' + PL(_mp_jf, "Jonathan Tufts, Mystic fisherman") + '.'),
        ('the house of &ldquo;the Misses Tufts&rdquo;',
         'the house of ' + PL(_mp_ms, "&ldquo;the Misses Tufts&rdquo;")),
        ('the Misses Tufts&rsquo; dwelling-house',
         PL(_mp_ms, "The Misses Tufts") + '&rsquo; dwelling-house'),
        ('homestead of Nathaniel Tufts (1692&ndash;1741)',
         'homestead of ' + PL(_mp_nt, "Nathaniel Tufts (1692&ndash;1741)")),
        ('Pasture of Mary Tufts, in Medford',
         'Pasture of ' + PL(_mp_my, "Mary Tufts") + ', in Medford'),
        ('Which Mary Tufts of Medford this was. No profile on this site matches yet.',
         'Which Mary Tufts of Medford this was. A short profile is at ' + PL(_mp_my, "Mary Tufts of Medford (fl. 1774)") + '.'),
        ('Mrs Amos Locke nee Sally Tufts',
         'Mrs Amos Locke nee ' + PL(_mp_sa, "Sally Tufts")),
        ('donated via Effie Tufts.',
         'donated via ' + PL(_mp_ef, "Effie Tufts") + '.'),
        ('the tithing man was Jonathan Tufts',
         'the tithing man was ' + PL(_mp_jt, "Jonathan Tufts")),
        ('Which <strong>Jonathan Tufts</strong> served as tithing man (likely Peter&rsquo;s brother Jonathan) is not confirmed.',
         'Which <strong>Jonathan Tufts</strong> served as tithing man is not confirmed; the likely identification with Peter&rsquo;s brother ' + PL(_mp_jt, "Jonathan Tufts (c. 1659&ndash;1722)") + ' is discussed on his profile.'),
    ]
    for old, new in pairs:
        if old in html and ("profiles/" not in new or new.split("profiles/")[-1].split(".html")[0] not in html[max(0, html.find(old)-80):html.find(old)+len(old)+80] if "profiles/" in new else True):
            # avoid double-wrapping if the exact new string is already there beside old
            if new not in html:
                html = html.replace(old, new)
    return html

if "BIZ_HTML" in globals():
    BIZ_HTML = _mp_linkify(BIZ_HTML)
    page("businesses.html", "Businesses | Tufts Lineage &amp; Legacy", "Places", "Businesses",
         "The trades of the Tufts family, colonial era to the 19th century", BIZ_HTML)
if "MAPS_HTML" in globals():
    MAPS_HTML = _mp_linkify(MAPS_HTML)
for _vn in ("NEWS", "GAZSEC", "MUSKETS"):
    if _vn in globals():
        globals()[_vn] = _mp_linkify(globals()[_vn])
_mp_extra = EXTRA
def EXTRA(path):
    return _mp_linkify(_mp_extra(path))

_mp_page = page
def page(path, *args, **kwargs):
    if path in ("collections.html", "places.html", "businesses.html") and len(args) >= 5:
        args = list(args)
        args[4] = _mp_linkify(args[4])
        args = tuple(args)
    return _mp_page(path, *args, **kwargs)

# ---------- IDSEC: fill Town/vital records for the better-documented new pages ----------
_IDSEC_M = IDSEC
def IDSEC(p):
    h = _IDSEC_M(p)
    s = p["slug"]
    fixes = {
        _mp_ed: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Wyman, vol. II, p. 966: born 13 August 1795; died 28 March 1859, aged 59, son of Joseph 44 and Abigail.</td>"),
        _mp_ab: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Wyman, vol. II, p. 960 (birth, 24 July 1761, daughter of James 10); p. 966 (marriage, 31 March 1783; death at Medford, 9 October 1801, aged 40).</td>"),
        _mp_nt: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Wyman, vol. II, p. 963: born at Medford 23 February 1692; died 27 August 1741. Marriages and children are on the same page.</td>"),
        _mp_sa: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td><em>Vital Records of Medford, Massachusetts, to the Year 1850</em> (1907), p. 152 (birth, 15 February 1789). Marriage and death as cited from the family record on this page.</td>"),
        _mp_ka: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Wyman, vol. II, p. 961: born 31 March 1734; married William Tufts Jr., 10 January 1750.</td>"),
        _mp_jt: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Wyman, vol. II, p. 961: death 13 August 1722, aged 63 years, 3 months, 11 days, gravestone at Malden; children listed there.</td>"),
        _mp_al: ("<td>Town / vital records</td><td>Medford VRs not yet checked by volume and page</td>",
              "<td>Town / vital records</td><td>Somerville vital records not yet checked by volume and page; dates as cited from the family record on this page and on her father&rsquo;s profile.</td>"),
    }
    if s in fixes:
        a, b = fixes[s]
        h = h.replace(a, b)
        h = h.replace("<td><em>Mass. Soldiers and Sailors</em></td><td>Not yet checked for this page</td>",
                      "<td><em>Mass. Soldiers and Sailors</em></td><td>No military entry expected</td>")
    return h

print("missing_profiles_1126 done")

exec(open("tools/francis_orderly_1127.py").read())
