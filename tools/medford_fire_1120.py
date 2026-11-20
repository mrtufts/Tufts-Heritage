# Daily research run 2026-11-20: the Medford fire of November 21, 1850, and the Tufts wheelwright shops on Main Street.
# Sources: "A Medford Disaster of 1850," MHR XLII nos. 3-4 (Sept.-Dec. 1939), pp. 59-62 (reprinting George P. Little,
# The Fireman's Own Book, 1860); Vital Records of Medford to 1850 (1907), pp. 147, 152; Brooks, History of Medford (1855), p. 553;
# Tufts Kinsmen Vol. I pp. 113, 257 (nos. 57-1, 143-4); Vol. II pp. 39, 271 (nos. 190-8, 422-1).
_RT = "richard-tufts-1804"
_ET = "elias-tufts-1787"
_F60 = "https://archive.org/details/medfordhistorica12medf/page/n227/mode/1up"
_F61 = "https://archive.org/details/medfordhistorica12medf/page/n228/mode/1up"
_FSRC = '&ldquo;A Medford Disaster of 1850,&rdquo; <em>Medford Historical Register</em> XLII, nos. 3&ndash;4 (September&ndash;December 1939)'
_FC = lambda pg, u: _FSRC + f', p. {pg}, quoting George P. Little, <em>The Fireman&rsquo;s Own Book</em> (1860). <a href="{u}">View the page scan</a>'
_BR553 = 'Charles Brooks, <em>History of the Town of Medford</em> (1855), p. 553. <a href="https://archive.org/details/historyoftownofm1855broo/page/553/mode/1up">Page scan (Internet Archive)</a>'
_MHRS = "Medford Historical Society, <em>Medford Historical Register</em> XLII (1939), via Internet Archive"
IMAGES["mhr-xlii-fire-1850-richard-tufts-shop-clip.jpg"] = ("Clipping: Richard Tufts&rsquo;s wheelwright shop burned, 1850",
  "Detail of p. 60, <em>Medford Historical Register</em> XLII, nos. 3&ndash;4 (September&ndash;December 1939), &ldquo;A Medford Disaster of 1850&rdquo;: the Misses Tufts&rsquo; dwelling-house and Richard Tufts&rsquo; wheelwright shop on Main Street.",
  _MHRS, "Shown for non-commercial historical use", _F60, "Internet Archive (full page)")
IMAGES["mhr-xlii-fire-1850-elias-tufts-shop-clip.jpg"] = ("Clipping: Elias Tufts&rsquo;s wheelwright shop and house burned, 1850",
  "Detail of p. 61, <em>Medford Historical Register</em> XLII, nos. 3&ndash;4 (September&ndash;December 1939), &ldquo;A Medford Disaster of 1850&rdquo;: Elias Tufts&rsquo; wheelwright shop and dwelling-house, across Main Street.",
  _MHRS, "Shown for non-commercial historical use", _F61, "Internet Archive (full page)")
_Q60 = ("Next to the Gregg estate was Timothy Cutting&rsquo;s house, blacksmith shop, and two stables, which were totally destroyed. Mr. Nathan Barker occupied a part of the dwelling-house. Mr. George Lynne&rsquo;s house, blacksmith shop and stable came next, and were also destroyed. "
  "The Misses Tufts&rsquo; dwelling-house, and Richard Tufts&rsquo; wheelwright shop, on the same side of Main Street, were also totally laid in ashes.")
_Q61 = ("On the opposite side of Main Street, the fire commenced at the bridge with the dwelling-house of Nathan W. White, and swept down Daniel Lawrence&rsquo;s store and dwelling-house, James Hyde&rsquo;s dwelling-house and store, Elias Tufts&rsquo; wheelwright shop and dwelling-house, George E. Willis&rsquo; tinware shop and dwelling-house, Mitchell&rsquo;s barber shop and dwelling-house, Benjamin Parker&rsquo;s dwelling-house and stable, Moses Merrill &amp; Son&rsquo;s paint shop and Hartshorn&rsquo;s harness shop, in the same building, a ten-footer occupied by an Irish family, and three stables &mdash; were all totally destroyed.")
_FIRE_INTRO = ('<p>Late on the night of Thursday, November 21, 1850, fire broke out in the loft of Gregg&rsquo;s stable on the north side of Main Street in Medford, near the bridge over the Mystic. Driven by a fresh northwest wind, it crossed to both sides of the street and burned until about two in the morning, destroying some twenty-five buildings between the bridge and the Medford House hotel, leaving thirty or forty families homeless, and doing about $75,000 in damage. Engine companies came from Boston, Somerville, Charlestown, Chelsea, Malden, Reading, Woburn and Cambridge. A contemporary account, printed in George P. Little&rsquo;s <em>The Fireman&rsquo;s Own Book</em> (1860), was reprinted by the Medford Historical Society in 1939 (' + _FSRC + ', pp. 59&ndash;62).</p>')
_FIRE_SEC = lambda who: ('<section id="fire-1850"><h2>The Main Street Fire of 1850</h2>' + _FIRE_INTRO
  + FIG("mhr-xlii-fire-1850-richard-tufts-shop-clip.jpg", "hfig-flow mi-inline")
  + '<p>Two Tufts wheelwrights had shops in the path of the fire, one on each side of Main Street. On the north side, where the fire began, it took ' + who[0] + ':</p>'
  + Q(_Q60, _FC(60, _F60))
  + FIG("mhr-xlii-fire-1850-elias-tufts-shop-clip.jpg", "hfig-flow mi-inline")
  + '<p>On the south side it took ' + who[1] + ':</p>'
  + Q(_Q61, _FC(61, _F61))
  + '<p>See also <a href="{P}businesses.html#wheelwrights-main-street">Businesses: The Tufts wheelwright shops on Main Street</a>.</p></section>')
_MISSES_UNV = ("<strong>Who the &ldquo;Misses Tufts&rdquo; were</strong> is not stated in the account. Richard Tufts&rsquo;s unmarried sisters Hannah (1801&ndash;1864) and Emily (1806&ndash;1895) were living in Medford in 1850 and are the likeliest candidates, since their house stood on the same side of Main Street as his shop (" + TKV(257, "143-3, 143-5") + "); Elias Tufts&rsquo;s unmarried sister Mercy (1782&ndash;1855) is another possibility (" + TKV2(38, "190-5") + "). Note: Pending further work.")

_nf_new(_RT, "Richard Tufts, Wheelwright (1804&ndash;1885)", "5 March 1804 &ndash; 25 July 1885", "Medford, Mass.", "1804", "1885", "19th Century",
  "Son of Benjamin Tufts Jr. and Hannah (Turner) Tufts; wheelwright of Medford",
  '<p>Richard Tufts was born in Medford on March 5, 1804, a son of Benjamin Tufts Jr. (1761&ndash;1826) and Hannah (Turner) Tufts. The town record reads:</p>'
  + Q("Richard, s. Benj[ami]n [Benjamin Jr., c.r.1. p.r.42.] and Hannah, Mar. 5, 1804.", MV(152))
  + '<p>He became a wheelwright, building and mending the wheels, carts and wagons of a town whose shipyards, brickyards and distillery depended on hauling. His younger brother Watts Turner Tufts (1811&ndash;1841) was also a wheelwright. Richard never married, and he died in Medford on July 25, 1885 (' + TKV(257, "143-4") + ').</p>'
  + _FIRE_SEC(("his shop, next to the house of &ldquo;the Misses Tufts&rdquo;", "the shop and house of " + PL(_ET, "Elias Tufts") + ", another Medford wheelwright of an older generation and a different branch of the family"))
  + '<p>He is not the same man as ' + PL("richard-tufts", "Richard Tufts (b. 1763 or 1765)") + ', son of Lieut. William Tufts.</p>',
  '<p>Born in 1804, he had no Revolutionary service. No military service is recorded for him.</p>',
  '<p>Father: Benjamin Tufts Jr. (1761&ndash;1826), son of ' + PL("benjamin-tufts", "Benjamin Tufts (1731&ndash;1804)") + ' and Esther (Lynde) Tufts. Mother: Hannah (Turner) Tufts (bapt. 1773&ndash;1841), daughter of Watts and Hannah (Tufts) Turner (' + TKV(113, "57-1") + '). Brothers and sisters: Benjamin (1797&ndash;1843), Augustus Turner (1799&ndash;1811), Hannah (1801&ndash;1864), Emily (1806&ndash;1895), Andrew (b. 1808, died in North Carolina), Watts Turner (1811&ndash;1841), wheelwright, Augustus (1813&ndash;1864), carpenter and Civil War soldier, and Edward (1815&ndash;1866), blacksmith of Malden (' + TKV("256&ndash;257") + ').</p>',
  _MISSES_UNV + " <strong>The site of his shop</strong> on Main Street is not more closely located in the account, and whether he rebuilt after the fire is not yet known. Note: Pending further work.",
  "<p>He did not marry (" + TKV(257) + ").</p>",
  [("benjamin-tufts", "grandfather Benjamin Tufts (1731&ndash;1804)", "grandson Richard Tufts, wheelwright (1804&ndash;1885)"),
   ("richard-tufts", "a different man of the same name: Richard Tufts (b. 1763 or 1765)", "a different man of the same name: Richard Tufts, wheelwright (1804&ndash;1885)")])

_nf_new(_ET, "Elias Tufts, Wheelwright (1787&ndash;1868)", "30 January 1787 &ndash; 18 May 1868", "Medford, Mass.", "1787", "1868", "19th Century",
  "Son of James Tufts, potter, and Elizabeth (Hay) Tufts; wheelwright of Medford",
  '<p>Elias Tufts was born in Medford on January 30, 1787, the eighth child of ' + PL("james-tufts-82-3", "James Tufts, the potter") + ', and Elizabeth (Hay) Tufts. The town record reads:</p>'
  + Q("Elias, s. James [James Jr., p.r.42.] and Elizabeth, Jan. 30, 1787.", MV(147))
  + '<p>Brooks gives the same date in his list of this family (' + _BR553 + '). Elias became a wheelwright. He married Abigail (Nabby) Symmes in Medford on May 23, 1813, and they had two sons, Alfred (1818&ndash;1901), wheelwright and ship joiner, and Larkin Turner (1822&ndash;1905), ship joiner, who later compiled Tufts family records. Elias died in Medford on May 18, 1868 (' + TKV2(39, "190-8") + '; ' + TKV2(271, "422-1, 422-2") + '). His son followed him in the trade; the town record of a grandson&rsquo;s birth in 1845 names &ldquo;Alfred, wheelwright&rdquo; as the father (' + MV(147) + ').</p>'
  + _FIRE_SEC(("the shop of " + PL(_RT, "Richard Tufts") + ", a younger wheelwright of another branch of the family, and the house of &ldquo;the Misses Tufts&rdquo;", "his own shop and house"))
  + '<p>He is not the same man as ' + PL("elias-tufts-42-4", "Elias Tufts (b. 1751)") + ', who died at Pembroke, New Hampshire.</p>',
  '<p>No military service is recorded for him.</p>',
  '<p>Father: ' + PL("james-tufts-82-3", "James Tufts, potter (1755&ndash;1810)") + '. Mother: Elizabeth (Hay) Tufts (1753&ndash;1828). Grandfather: ' + PL("james-tufts-jr-36-2", "James Tufts") + '. Brothers and sisters: Mary (Mrs. Benjamin Reed), James Jr. (1777&ndash;1825), Elizabeth (Mrs. Samuel Newhall), Lucretia (Mrs. Reuben Richardson), Mercy (1782&ndash;1855, unmarried), two Sarahs, Frances (Mrs. Luke Richardson Jr.), two Lucys, and Nancy (Mrs. Amasa J. Boynton) (' + TKV2("37&ndash;39") + '). Sons: Alfred and Larkin Turner Tufts (' + TKV2(271) + ').</p>',
  "<strong>Birth date:</strong> the family record gives January 20, 1787, but the printed town record and Brooks both read January 30; the town record is followed here. " + _MISSES_UNV,
  "<ul><li><strong>Abigail (Nabby) Symmes</strong> (1785&ndash;1863), daughter of Capt. John and Elizabeth (Wright) Symmes; married May 23, 1813, at Medford; died at Medford, August 11, 1863 (" + TKV2(39) + ").</li></ul>",
  [("james-tufts-82-3", "father James Tufts, potter (1755&ndash;1810)", "son Elias Tufts, wheelwright (1787&ndash;1868)"),
   ("james-tufts-jr-36-2", "grandfather James Tufts", "grandson Elias Tufts, wheelwright (1787&ndash;1868)"),
   ("elias-tufts-42-4", "a different man of the same name: Elias Tufts (b. 1751)", "a different man of the same name: Elias Tufts, wheelwright (1787&ndash;1868)"),
   (_RT, "fellow Medford wheelwright Richard Tufts (1804&ndash;1885), whose shop burned in the same fire", "fellow Medford wheelwright Elias Tufts (1787&ndash;1868), whose shop burned in the same fire")])

_p = _up_get("james-tufts-82-3")
if _p and _ET not in _p["family"]:
    _p["family"] = _p["family"].replace("Sarah, Elias, Frances", "Sarah, " + PL(_ET, "Elias") + ", Frances", 1)
_p = _up_get("richard-tufts")
if _p and _RT not in _p["bio"]:
    _p["bio"] = _p["bio"] + '<p>He is not the Richard Tufts whose wheelwright shop burned in the Medford fire of 1850; that was ' + PL(_RT, "Richard Tufts (1804&ndash;1885)") + ', son of Benjamin Tufts Jr.</p>'
_p = _up_get("elias-tufts-42-4")
if _p and _ET not in _p["bio"]:
    _p["bio"] = _p["bio"] + '<p>He is not the Medford wheelwright ' + PL(_ET, "Elias Tufts (1787&ndash;1868)") + ', son of James Tufts the potter.</p>'
_p = _up_get("benjamin-tufts")
if _p and _RT not in _p["family"]:
    _p["family"] = _p["family"] + '<p>Grandson: ' + PL(_RT, "Richard Tufts, wheelwright (1804&ndash;1885)") + ', son of Benjamin Tufts Jr. (' + TKV(257, "143-4") + ').</p>'

_WHEEL_BIZ = BIZ("wheelwrights-main-street", "The Tufts Wheelwright Shops on Main Street, Medford",
  PR(_ET, "Elias Tufts (1787&ndash;1868)") + "; " + PR(_RT, "Richard Tufts (1804&ndash;1885)"), "Wheelwrights", "Main Street, Medford, between the Mystic bridge and the Medford House", "Burned November 21, 1850",
  '<p><strong>Tufts association.</strong> Two Medford wheelwrights of the family kept shops on Main Street, near the Mystic bridge: Elias Tufts, son of James Tufts the potter, whose shop and dwelling-house stood on one side of the street, and Richard Tufts, son of Benjamin Tufts Jr., whose shop stood on the other, beside the house of &ldquo;the Misses Tufts.&rdquo; Both were destroyed in the fire of the night of November 21, 1850, which burned some twenty-five buildings between the bridge and the Medford House (' + _FSRC + ', pp. 59&ndash;62). The family record calls both men wheelwrights, as well as Richard&rsquo;s brother Watts Turner Tufts (1811&ndash;1841) and Elias&rsquo;s son Alfred (1818&ndash;1901) (' + TKV(257) + '; ' + TKV2(39) + '; ' + TKV2(271) + ').</p>'
  + FIG("mhr-xlii-fire-1850-richard-tufts-shop-clip.jpg", "hfig-flow mi-inline")
  + Q(_Q60, _FC(60, _F60))
  + FIG("mhr-xlii-fire-1850-elias-tufts-shop-clip.jpg", "hfig-flow mi-inline")
  + Q(_Q61, _FC(61, _F61))
  + UNV("The account does not give the exact sites of the two shops along the street, how long either had stood, or whether either was rebuilt. " + _MISSES_UNV))
if "BIZ_HTML" in globals() and 'id="wheelwrights-main-street"' not in BIZ_HTML:
    _k = BIZ_HTML.find('<section id="not-found">')
    BIZ_HTML = (BIZ_HTML[:_k] + _WHEEL_BIZ + BIZ_HTML[_k:]) if _k != -1 else (BIZ_HTML + "{DIV}" + _WHEEL_BIZ)
    page("businesses.html", "Businesses | Tufts Lineage &amp; Legacy", "Places", "Businesses", "The trades of the Tufts family, colonial era to the 19th century", BIZ_HTML)
print("medford_fire_1120: profiles", len(PROFILES))
exec(open("tools/john_merge_1120.py").read())
