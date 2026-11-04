# Further profiles (2026-11-04): Anne Adams Tufts's other children (Adams genealogy, 1898)
# and the Edward Street Tufts men (Medford Historical Commission, Edward Street Area form, 2022).
MHC1 = MHC.replace("(2022).", "(2022), continuation sheet 1.")
MHC2 = MHC.replace("(2022).", "(2022), continuation sheet 2.")
ADGP = lambda pg: ADG(pg)
_OCRB = OCR
_ANNE = '<p>Mother: ' + PL("anne-adams-tufts", "Anne Adams Tufts (1729&ndash;1813)") + '. Father: ' + WH + '.</p>'
_KIDS = [("ann-tufts-richardson", "Ann Tufts Richardson (b. 1757)", "b. 1757", "1757", "Ann Tufts, b. Jan. 2, 1757; m. Abel Richardson.", "Abel Richardson"),
 ("elizabeth-tufts-swan", "Elizabeth Tufts Swan (b. 1758)", "b. 1758", "1758", "Elizabeth Tufts, b. Oct. 23, 1758; m. March 2, 1787, Daniel Swan.", "Daniel Swan, married March 2, 1787"),
 ("joseph-tufts-1760", "Joseph Tufts (b. 1760)", "b. 1760", "1760", "Joseph Tufts, b. July 12, 1760; m. Abigail Tufts.", "Abigail Tufts"),
 ("lydia-tufts-gray", "Lydia Tufts Gray (b. 1762)", "b. 1762", "1762", "Lydia Tufts, b. June 10, 1762; m. Rev. Robert Gray of Dover, N. H.", "Rev. Robert Gray of Dover, N.H."),
 ("asa-tufts-1764", "Asa Tufts (1764&ndash;1828)", "1764&ndash;1828", "1764", "Asa Tufts, b. July 2, 1764, d. 24 Oct., 1828.", ""),
 ("thomas-tufts-1766", "Thomas Tufts of Lexington (1766&ndash;1830)", "1766&ndash;1830", "1766", "Thomas Tufts, b. May 18, 1766; m. Nov. 29, 1791, Rebecca Adams, dau. of John and Lucy (Hubbard) Adams of Lincoln, Mass., d, 20 Feb., 1858. He d. 10 June, 1830; res. Lexington, Mass.", ""),
 ("lucy-tufts-osgood", "Lucy Tufts Osgood (b. 1767)", "b. 1767", "1767", "Lucy Tufts, b. Nov. 12, 1767; m. Jacob Osgood.", "Jacob Osgood"),
 ("rebecca-tufts-adams", "Rebecca Tufts Adams (1769&ndash;c. 1848)", "1769&ndash;c. 1848", "1769", "Rebecca Tufts, b. Sept. 20, 1769; m. Nathan Adams, Esq., son of Dea. Joseph and Hannah (Hill) Adams (his 2nd wife).", ""),
 ("sarah-tufts-adams", "Sarah Tufts Adams", "dates pending", "", "Sarah Tufts, b. in Charlestown, Mass.; m. Feb. 25, 1802, Maj. Joseph Adams, son of Dea. Joseph and Martha (Frost) Adams (his 2nd wife).", "")]
_SIBS = [("peter-tufts-jr", "brother Peter Tufts Jr. (1753&ndash;1832)"), ("john-tufts-1754", "brother John Tufts (b. 1754)")] + [(s, ("sister " if any(w in n for w in ("Ann ", "Elizabeth", "Lydia", "Lucy", "Rebecca", "Sarah")) else "brother ") + n) for s, n, *_ in _KIDS]
_XB = {
 "thomas-tufts-1766": dict(bio_extra=Q("Rebecca, b. in Lincoln, Feb. 28. 1767; m. Nov. 19, 1791, Thomas Tufts, a large farmer of Lexington, Mass., son of Peter, Jr., and Anna (Adams) Tufts, b. May 18, 1766, d. 10 June, 1830. She d. 20 Feb., 1858, age 91 years.", ADGP(978), note=_OCRB)
   + '<p>The same genealogy lists their children: Thomas, born 1792, &ldquo;drowned in fording a river in Kentucky, 1816, age 24&rdquo;; Rebecca, who died at 30; Marshall, Harvard 1827, died 1855; Eveline, who married a Rochester of Ohio; and Lucy Ann, who married Dr. Proctor of Castine, Maine (Adams, p. 1004).</p>',
   sp="<ul><li><strong>Rebecca Adams</strong> (b. Lincoln, Feb. 28, 1767; d. Feb. 20, 1858, aged 91), daughter of John and Lucy (Hubbard) Adams of Lincoln. Married Nov. 1791 (Adams genealogy, pp. 973, 978).</li></ul>",
   unv="<strong>Marriage day:</strong> the Adams genealogy gives Nov. 29, 1791 on p. 973 and Nov. 19, 1791 on p. 978."),
 "rebecca-tufts-adams": dict(bio_extra=Q("m. (2) Dec. 13, 1803, Rebecca Tufts, b. Sept. 20, 1770, d. about 1848. He settled in Medford, Mass.; had [&hellip;] acres where Mystic Park now is", ADGP("971&ndash;72"), note="(Of Nathan Adams, Esq., b. in Menotomy Aug. 9, 1763. Scanned text; the acreage is illegible in the scan text.)")
   + '<p>Their children were Peter Adams, born in Medford Dec. 9, 1804, later of Roxbury, and Louisa, born Oct. 6, 1808, who died in 1810 (Adams, p. 990).</p>',
   sp="<ul><li><strong>Nathan Adams, Esq.</strong> (b. Menotomy, Aug. 9, 1763; d. aged 78), of Medford, as his second wife. Married Dec. 13, 1803 (Adams genealogy, pp. 971&ndash;72).</li></ul>",
   unv="<strong>Birth:</strong> Sept. 20, 1769 (Adams, p. 973) against Sept. 20, 1770 (p. 971&ndash;72). <strong>Death:</strong> &ldquo;about 1848&rdquo;; Note: Pending further work. Nathan Adams&rsquo;s death date and acreage are unclear in the scanned text; Note: Pending further work."),
 "sarah-tufts-adams": dict(bio_extra='<p>Her husband, Maj. Joseph Adams of Menotomy, had married first Lucy Kent of Cambridge in 1770; he settled in Charlestown and died there in December 1834 (Adams, p. 971). Their children, all born in Charlestown, were Sarah Ann (b. Dec. 30, 1803, per the scanned text), who married John C. Magoun on Dec. 30, 1824; Martha (1804&ndash;1855); Rebecca (1806&ndash;1832); Charles (1809&ndash;1890), who died in Somerville; Lucy (1812&ndash;1836); Eliza (b. 1814), who married Roswell Tenney; and Harriet (b. 1816), who married Aaron B. Magoun (Adams, p. 988).</p><p>Through Sarah Ann Magoun she was the grandmother of Helen Magoun Heald, long an officer of the DAR chapter named for Anne Adams Tufts (see her mother&rsquo;s profile).</p>',
   sp="<ul><li><strong>Maj. Joseph Adams</strong> (b. Menotomy, Nov. 29, 1743; d. Charlestown, Dec. 1834), as his second wife. Married Feb. 25, 1802 (Adams genealogy, pp. 971, 973).</li></ul>",
   unv="<strong>Birth and death dates:</strong> not given by Adams. Note: Pending further work. <strong>Sarah Ann&rsquo;s birth:</strong> Adams (p. 988) gives Dec. 30, 1803; the profile of Anne Adams Tufts gives 1802 from a later blog. Note: Pending further work. <strong>Helen Magoun Heald&rsquo;s descent</strong> through Sarah Ann is inferred from her name and the DAR history&rsquo;s &ldquo;great-granddaughter&rdquo;; Note: Pending further work."),
}
for s, n, d, b, q, sp in _KIDS:
    x = _XB.get(s, {})
    first = n.split(" (")[0]
    PROFILES.append(dict(slug=s, name=n, dates=d, town="Winter Hill, Charlestown (now Somerville), Mass.", born=b, died=("1828" if s == "asa-tufts-1764" else "1830" if s == "thomas-tufts-1766" else ""), era="The Revolution", line="Child of Peter and Anne (Adams) Tufts of Winter Hill",
      bio=f'<p>{first} was one of the twelve children of ' + WH + ' and ' + PL("anne-adams-tufts", "Anne Adams Tufts") + ', raised on the family farm on Winter Hill. The Adams family genealogy of 1898 records:</p>' + Q(q, ADGP(973), note=_OCRB) + x.get("bio_extra", ""),
      service='<p>No military or public service has been matched to this person. Note: Pending further work.</p>',
      family=_ANNE, unverified=x.get("unv", "<strong>Death, residence and children:</strong> Note: Pending further work. Only the Adams genealogy entry above has been found so far.")))
    SP[s] = x.get("sp", f"<ul><li><strong>{sp}</strong> (Adams genealogy, p. 973).</li></ul>" if sp else "<p>Note: Pending further work.</p>")
    NEWUNCHK.add(s)
    REL[s] = [("anne-adams-tufts", "mother Anne Adams Tufts"), ("peter-tufts-1697", "grandfather Peter Tufts (1697&ndash;1776)"), ("timothy-tufts", "uncle Timothy Tufts")] + [t for t in _SIBS if t[0] != s]
_addrel("anne-adams-tufts", [(s, ("daughter " if "Tufts " in n and any(w in n for w in ("Ann ", "Elizabeth", "Lydia", "Lucy", "Rebecca", "Sarah")) else "son ") + n) for s, n, *_ in _KIDS])
for _s in ("peter-tufts-jr", "john-tufts-1754"):
    _addrel(_s, [t for t in _SIBS if t[0] not in ("peter-tufts-jr", "john-tufts-1754")])
_addrel("timothy-tufts", [(s, "nephew/niece " + n) for s, n, *_ in _KIDS])
_addrel("peter-tufts-1697", [(s, "grandchild " + n) for s, n, *_ in _KIDS])
_addrel("peter-tufts-1774", [("thomas-tufts-1766", "uncle Thomas Tufts of Lexington"), ("rebecca-tufts-adams", "aunt Rebecca Tufts Adams"), ("sarah-tufts-adams", "aunt Sarah Tufts Adams")])

# ---- Edward Street men ----
_ES = '<p>In the 1850s and 1860s they laid out the Tufts subdivisions of South Medford (Winter Hill), labeled on the 1875 Beers atlas &ldquo;W E G F &amp; A Tufts.&rdquo; See <a href="{P}places.html#tufts-subdivisions">Places: The Tufts Subdivisions of South Medford</a>.</p>'
_ESQ = Q("labeled &ldquo;W E G F &amp; A Tufts,&rdquo; William, Edward, George F, and Alfred Tufts. William (1802-1862) and Edward (1806-1875) were the two youngest of Amos&rsquo;s seven sons. William Tufts lived in Charlestown and was a clerk and later secretary of an insurance company; Edward Tufts was also a clerk and lived in Lowell. George and Alfred were sons of Joseph Frothingham Tufts (1790-1854) the oldest of Amos&rsquo;s sons. George F Tufts (1825-1920) was a civil engineer and later a bank president; Alfred Tufts (1829-1882) was a clerk, an engineer, and a bank teller.", MHC1)
_NAT = Q("This real estate Nathan Tufts bequeathed to the sons of his two brothers Daniel and Amos, and it appears that it was the sons of Amos (1762-1839) who took charge of the land in this vicinity known as Dexter Farm.", MHC1)
_ESM = [("william-tufts-1802", "William Tufts (1802&ndash;1862)", "1802&ndash;1862", "1802", "1862", "Charlestown, Mass.", "Son of Amos Tufts (1762&ndash;1839)",
   '<p>William Tufts was one of the seven sons of Amos Tufts (1762&ndash;1839) of Charlestown, a son of Nathan and Mary (Adams) Tufts. With his brother Edward and his nephews George F. and Alfred, he took charge of the Medford land left to Amos&rsquo;s sons by their uncle Nathan Tufts (1764&ndash;1839), the Charlestown butcher and tanner.</p>', "uncle"),
  ("edward-tufts-1806", "Edward Tufts (1806&ndash;1875)", "1806&ndash;1875", "1806", "1875", "Lowell, Mass.", "Son of Amos Tufts (1762&ndash;1839)",
   '<p>Edward Tufts, the youngest of Amos Tufts&rsquo;s seven sons, was a clerk who lived in Lowell. With his brother William and his nephews George F. and Alfred, he held the old Dexter Farm lands in South Medford left by his uncle Nathan Tufts (1764&ndash;1839). Edward Street in Medford&rsquo;s Winter Hill neighborhood is one of the streets &ldquo;named for members of the Tufts family&rdquo; (Medford Historical Commission); which Edward it honors is not stated.</p>', "uncle"),
  ("george-f-tufts-1825", "George F. Tufts (1825&ndash;1920)", "1825&ndash;1920", "1825", "1920", "Charlestown and Medford, Mass.", "Grandson of Amos Tufts (1762&ndash;1839)",
   '<p>George F. Tufts, a son of Joseph Frothingham Tufts (1790&ndash;1854), the eldest son of Amos, was a civil engineer and later a bank president. After the 1858 and 1861 divisions, &ldquo;Alfred, Edward and William&rsquo;s heirs sold many of their lots to George&rdquo; (' + MHC2 + ').</p>' + Q("George Tufts then reorganized a portion of section #5 in 1880, adding additional streets to the section between Dexter, Edward, Henry, and Albion streets to increase the density of the area", MHC2) + '<p>In March 1886 he sold the four lots that became Edward Street&rsquo;s row of six end houses, two to Abby B. Costelow and two to Augustus F. Dickson, for $1,035 each (' + MHC2 + ').</p>', "nephew"),
  ("alfred-tufts-1829", "Alfred Tufts (1829&ndash;1882)", "1829&ndash;1882", "1829", "1882", "Charlestown and Medford, Mass.", "Grandson of Amos Tufts (1762&ndash;1839)",
   '<p>Alfred Tufts, a younger son of Joseph Frothingham Tufts (1790&ndash;1854), was a clerk, an engineer and a bank teller. He was the surveyor of the family&rsquo;s recorded subdivision plans: &ldquo;Alfred was surveyor for the recorded plans&rdquo; (' + MHC1 + '). Alfred Street in the westernmost section (no. 2, 1854) appears in the same subdivision (MCSRD Plans 7:19).</p>', "nephew")]
for s, n, d, b, dd, town, line, bio, kind in _ESM:
    PROFILES.append(dict(slug=s, name=n, dates=d, town=town, born=b, died=dd, era="19th Century", line=line,
      bio=bio + _ESQ + _NAT + _ES, service='<p>Civil and business life only, as above. No military service has been matched. Note: Pending further work.</p>',
      family=('<p>Father: Amos Tufts (1762&ndash;1839), son of Nathan and Mary (Adams) Tufts of Charlestown (Adams genealogy, p. 974). Uncle: Nathan Tufts (1764&ndash;1839). Brother: Joseph Frothingham Tufts (1790&ndash;1854).</p>' if kind == "uncle" else '<p>Father: Joseph Frothingham Tufts (1790&ndash;1854), eldest son of Amos Tufts (1762&ndash;1839). Great-uncle: Nathan Tufts (1764&ndash;1839).</p>'),
      unverified="<strong>Exact birth and death dates, burial and wife:</strong> Note: Pending further work. The Medford Historical Commission form gives years only and cites family trees on Ancestry.com among its sources." + (" <strong>Alfred Street:</strong> named for a family member, but not stated to be for him." if s == "alfred-tufts-1829" else "")))
    SP[s] = "<p>Note: Pending further work.</p>"
    NEWUNCHK.add(s)
_EM = ["william-tufts-1802", "edward-tufts-1806", "george-f-tufts-1825", "alfred-tufts-1829"]
REL["george-f-tufts-1825"] = [("alfred-tufts-1829", "brother Alfred Tufts"), ("william-tufts-1802", "uncle William Tufts"), ("edward-tufts-1806", "uncle Edward Tufts")]
REL["alfred-tufts-1829"] = [("george-f-tufts-1825", "brother George F. Tufts"), ("william-tufts-1802", "uncle William Tufts"), ("edward-tufts-1806", "uncle Edward Tufts")]
_L1104 = {"William (1802&ndash;1862)": "william-tufts-1802", "Edward (1806&ndash;1875)": "edward-tufts-1806", "George F. Tufts (1825&ndash;1920)": "george-f-tufts-1825", "Alfred Tufts (1829&ndash;1882)": "alfred-tufts-1829"}
_EXTRA_PB = EXTRA
def EXTRA(path):
    out = _EXTRA_PB(path)
    if path == "places.html":
        for t, s in _L1104.items():
            out = out.replace(t, f'<a href="{{P}}profiles/{s}.html">{t}</a>', 1)
    return out
