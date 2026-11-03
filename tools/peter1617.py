# Peter Tufts the immigrant (c. 1617-1700): profile, ferry history, Tufts Landing name note (owner request 2026-11-03).
COREY = "Deloraine Pendre Corey, <em>The History of Malden, Massachusetts, 1633&ndash;1785</em> (1899)"
COREY_URL = "https://archive.org/details/historyofmaldenm00corey/page/"
CR = lambda pg, extra="": f'{COREY}, p. {pg}{extra}. <a href="{COREY_URL}{pg}">Page scan (Internet Archive)</a>'
WM = f'&ldquo;Why Mystic?&rdquo;, <em>Medford Historical Register</em>, vol. XXI (1918), p. 54. <a href="{PERS_T("2005.05.0021", 19)}">Text (Perseus)</a>'
WT9 = '<a href="https://www.wikitree.com/wiki/Tufts-9">WikiTree, Peter Tufts Sr (Tufts-9)</a> (secondary, compiled)'
OCRN = '<span class="note">The OCR texts read &ldquo;Maiden&rdquo; for Malden; the word is given here as printed.</span>'
PROFILES += [dict(slug="peter-tufts-1617", name="Peter Tufts the Immigrant (c. 1617&ndash;1700)", dates="c. 1617&ndash;1700", town="Charlestown (Mystic Side) and Malden, Mass.", born="1617", died="1700", era="Colonial", line="Peter Tufts the immigrant",
  bio='<p>Peter Tufts came to Charlestown from England and settled across the Mystic on the Malden side, the &ldquo;Mystic Side&rdquo; of Charlestown. All the Tufts families of Malden, Medford and Charlestown on this site descend from him.</p>'
   + Q("This was the beginning of the Penny Ferry which served the inhabitants of Malden and the upper towns until 1787, when it was superseded by the Malden Bridge.", CR(85, ", on Charlestown&rsquo;s vote of April 2, 1640 that Philip Drinker keep &ldquo;a ferry at the Neck of Land with a sufficient boat&rdquo;") + " " + OCRN)
   + Q("Drinker, who died June 23, 1647, was succeeded a few months before his death by Peter Tufts, who afterwards became a large landholder on Mystic Side and in Malden, and the owner of the Nowell grant. He was assisted by his brother-in-law, William Bridge.", CR(85, ", note 53, citing Frothingham, <em>History of Charlestown</em>, p. 147"))
   + Q("He kept the Ferry between Charlestown and Malden with his brother-in-law, Bridges, in 1646-7", BOOTH + f', part 1, p. 21. <a href="{BOOTH_URL}2">Perseus</a>')
   + Q("these two continued to be the only bridges until the Malden bridge was built at the Penny-ferry in Charlestown .", WM + " " + OCRN)
   + '<p>Corey says the ferry-ways were built on &ldquo;the southerly side&rdquo; of an island in the marsh &ldquo;afterward known as the Ferry Island&rdquo; (p. 85, note 53). The ferry did not stay with Tufts: in 1651 the town voted to let it to John Harris, and soon after it was granted to Philip Knight (same note).</p>'
   + '<p>He became one of the great landholders north of the Mystic. In 1663 he bought the two-hundred-acre Nowell grant from Parnell Nowell, executrix:</p>'
   + Q("The two hundred acres were sold to Peter Tufts in 1663 by Parnell Nowell, as executrix, and with large additions, gained by purchase from the Cradock farm, remained in the family of the purchaser many years.", CR(58))
   + Q("Peter, of Medford, who lived upon a portion of the three hundred and fifty acres of the original Cradock farm, which his father had bought of Richard Russell's estate in 1677.", CR(215, ", note, on his son Capt. Peter Tufts"))
   + Q("Peter Tufts of Mystic Side, who many times during a long life appears in the court records and files, and not always as a desirable neighbor, also complained of them.", CR(330, ", on the 1692 witchcraft complaints against Elizabeth Fosdick and Elizabeth Paine"))
   + '<p>He died at Malden on May 13, 1700, and is buried in Bell Rock Cemetery. His stone reads &ldquo;Here Lyes the Body of Peter Tufts aged 83 years died May 13 1700&rdquo; (Find a Grave memorial <a href="https://www.findagrave.com/memorial/20180511/peter-tufts">20180511</a>). See also <a href="{P}generations/colonial.html#immigrant">Colonial</a> and <a href="{P}businesses.html#ferry">the ferry on Businesses</a>.</p>'
   + CROSSSEC().replace('<section id="penny-ferry"><h2>The Charlestown&ndash;Malden Crossing</h2>', '<section id="penny-ferry"><h2>The Ferry Crossing: Maps and Views</h2>'),
  service='<p>Ferryman at Charlestown Neck from early 1647 (Corey, p. 85, n. 53). Freeman 1665 (Jones, p. 128). Constable and other town service appear in Corey; not yet itemised here.</p>',
  family='<p>Married Mary Pierce (see Spouse). Children named by Brooks (1855, Register of Families) include Capt. Peter Tufts of Medford, Jonathan Tufts of Medford and John Tufts of Malden. Capt. Peter was father of Dr. Simon Tufts (1700&ndash;1747) (Brooks, p. 545).</p>',
  unverified="<strong>Partner&rsquo;s name:</strong> Corey (citing Frothingham) has &ldquo;William Bridge&rdquo;; Booth has &ldquo;Bridges&rdquo;; <em>New England Marriages to 1700</em> (as quoted by WikiTree) has &ldquo;called bro. by William BRIDGES.&rdquo; No source seen names a <strong>Thomas Bridges</strong>, or says he married a sister of Mary Pierce; that claim is not supported. <strong>Russell farm:</strong> Corey says 350 acres, bought of Richard Russell&rsquo;s <em>estate</em> in 1677, after Russell&rsquo;s death in 1676. The &ldquo;300-acre farm from Russell&rsquo;s executors&rdquo; version gives a different acreage. <strong>&ldquo;Tufts Landing&rdquo;</strong> as the name of the ferry landing is not found in Corey, Booth, Brooks, the <em>Register</em> or WikiTree. <strong>Wilby, Norfolk; in Charlestown 1637 &ldquo;on the Malden side&rdquo;; 43 acres by 1638; on Mystic Side by 1647 as one of the earliest and largest landowners:</strong> these appear only in WikiTree&rsquo;s text copied from Wikipedia. WikiTree itself marks the Wilby/Tibenham birthplace &ldquo;[uncertain].&rdquo; Corey confirms only that he became &ldquo;a large landholder on Mystic Side and in Malden.&rdquo; <strong>Birth year</strong> c. 1617 is computed from &ldquo;aged 83&rdquo; on his stone. <strong>Penny Ferry</strong> is Corey&rsquo;s name for the ferry from 1640 onward, not a name recorded in 1647. No BillionGraves memorial page was found for him; only the Bell Rock Cemetery listing.")]
SP["peter-tufts-1617"] = ("<ul><li><strong>Mary Pierce</strong> (c. 1628&ndash;1703), daughter of Thomas Pierce. Married at Charlestown, about October 1647 (WikiTree) or &ldquo;by 1648&rdquo; (<em>New England Marriages to 1700</em>, as quoted by WikiTree).</li></ul>"
   + "<p>Their joint stone in Bell Rock Cemetery adds: &ldquo;Also here lyes buried ye body of Mary Tufts his wife aged 75 years died January 1702/3&rdquo; (Find a Grave 20180511). Jones (p. 128) gives only &ldquo;His wife&rsquo;s name was Mary. She died in 1703, aged seventy-five.&rdquo;</p>"
   + UNV("Her surname Pierce and her father Thomas come from WikiTree and the marriage compilations; none of the printed sources quoted here names her family. The marriage date differs between WikiTree&rsquo;s data (Oct. 1647) and its text (1648)."))
FAGOK["peter-tufts-1617"] = "20180511/peter-tufts"
BREG["peter-tufts-1617"] = ("1 (head of the Tufts register)", 545)
_IDS0 = IDSEC
def IDSEC(p):
    h = _IDS0(p)
    if p["slug"] == "peter-tufts-1617":
        h = h.replace("WikiTree API refused requests on 3 Nov. 2026: rate limit)", "WikiTree API refused requests on 3 Nov. 2026)").replace(
            '<tr><td>WikiTree ID</td><td>Not yet checked (WikiTree API refused requests on 3 Nov. 2026)</td></tr>',
            '<tr><td>WikiTree ID</td><td><a href="https://www.wikitree.com/wiki/Tufts-9">Tufts-9</a>. Confirmed: death 13 May 1700, Malden; wife Mary Pierce. WikiTree comments flag Tufts-225 and Tufts-57 as probable duplicates.</td></tr>'
            '<tr><td>BillionGraves</td><td>Checked, not found (only the Bell Rock Cemetery page, no memorial for him)</td></tr>'
            '<tr><td>Middlesex probate</td><td>Case 22994 (will dated 1 Mar. 1693), as cited by WikiTree; not seen</td></tr>')
    return h
REL["peter-tufts-1617"] = [("simon-tufts-1700", "grandson Dr. Simon Tufts (1700&ndash;1747), through Capt. Peter"), ("timothy-tufts", "great-grandson Timothy Tufts, through John of Malden and Peter of Milk Row"), ("turell-tufts", "great-great-great-grandson Turell Tufts")]
REL["simon-tufts-1700"] = [("peter-tufts-1617", "grandfather Peter Tufts the immigrant")] + REL["simon-tufts-1700"]
REL["timothy-tufts"] = [("peter-tufts-1617", "great-grandfather Peter Tufts the immigrant")] + REL["timothy-tufts"]
REL["turell-tufts"] = REL["turell-tufts"] + [("peter-tufts-1617", "ancestor Peter Tufts the immigrant (Gill, p. 54: &ldquo;fifth in the line of descent from Peter Tufts of Malden&rdquo;)")]
TL_TA = TA("Peter Tufts the immigrant succeeded Philip Drinker as ferryman at Charlestown Neck in early 1647. This was the ferry later called the Penny Ferry, superseded in 1787 by Malden Bridge, on the line of today&rsquo;s Alford Street Bridge. The name &ldquo;Tufts Landing&rdquo; is not found in any source checked.", "Corey, p. 85 and n. 53; <em>Medford Historical Register</em>, vol. XXI, p. 54")
NAME_NOTE = '<aside id="name-note" class="note" style="border:1px dashed #c9a24a;padding:.6em 1em;margin:1em 0"><strong>A possible new name.</strong> The owner is considering renaming this site from <em>Tufts Heritage</em> to <em>Tufts Landing</em>, after Peter Tufts&rsquo;s ferry landing on the Mystic (see <a href="{P}profiles/peter-tufts-1617.html">Peter Tufts the Immigrant</a>). Nothing has been decided, and the site&rsquo;s name and address are unchanged.</aside>'
_EXTRA_P = EXTRA
def EXTRA(path):
    out = _EXTRA_P(path)
    if path == "generations/colonial.html":
        out = out.replace("{DIV}" + CROSSSEC(), "{DIV}" + '<section id="penny-ferry"><h2>The Charlestown&ndash;Malden Crossing</h2><p>The ferry history, with the 1775&ndash;77 maps and the Alford Street Bridge views, is on <a href="{P}profiles/peter-tufts-1617.html#penny-ferry">Peter Tufts the Immigrant</a>.</p>' + TL_TA + '</section>', 1)
        out += '{DIV}<p>Profile: <a href="{P}profiles/peter-tufts-1617.html">Peter Tufts the Immigrant (c. 1617&ndash;1700)</a>.</p>'
    if path == "places.html":
        out = out.replace('<section id="penny-ferry"><h2>The Charlestown&ndash;Malden Crossing</h2>', '<section id="penny-ferry"><h2>Penny Ferry / &ldquo;Tufts Landing&rdquo;: the Charlestown&ndash;Malden Crossing</h2>' + TL_TA + '<p>Profile: <a href="{P}profiles/peter-tufts-1617.html">Peter Tufts the Immigrant</a>.</p>', 1)
    return out
