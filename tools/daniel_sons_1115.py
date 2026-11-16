# Daily research run 2026-11-15 (evening): profiles for Daniel the brick-maker's sons
# Gilbert (1778-1850), Daniel Jr. (1776-1868), and Nathan 2d (1786-1872).
# Sources: Wyman, Genealogies and Estates of Charlestown, vol. 2, p. 968;
# Sawyer, Old Charlestown, pp. 39, 87, 162-164, 166. (_WY and _SW2 from daniel_brick_1115.py)

_GT = "gilbert-tufts-1778"
_DJ = "daniel-tufts-jr-1776"
_N2 = "nathan-tufts-2d-1786"

PROFILES.append(dict(slug=_DJ, name="Daniel Tufts Jr. (1776&ndash;1868)", dates="31 December 1776&ndash;21 September 1868", town="Charlestown, Mass.", born="1776", died="1868", era="19th Century",
  line="Eldest son of Daniel Tufts, brick-maker; tanner; Charlestown legislator, 1830, 1832 and 1833",
  bio=('<p>' + PL(_DJ, "Daniel Tufts Jr.") + ' was the eldest son of ' + PL("daniel-tufts", "Daniel Tufts, the Charlestown brick-maker") + ' and Abigail Tufts. Wyman records his birth as December 31, 1776, his marriage to Martha Bradshaw on December 26, 1809, and his death on September 21, 1868, in his ninety-second year (' + _WY(968) + ').</p>'
    + Q("Daniel, junior, and Gilbert were tanners. Their tanneries and residences were within the peninsula. Daniel was a member of the Legislature from Charlestown in 1830, &rsquo;32, and &rsquo;33. He did considerable business for many years, but in advanced life he became very timid or over-cautious and so fell behind the times.", _SW2(163))
    + Q("He had a stock of sole-leather in the vats of his tannery on Main Street which remained there unsold for years. When a purchaser was ready to meet the price he had been asking, it was always time to advance, and he didn&rsquo;t live long enough to receive an offer he could accept. A kiln of bricks made for and belonging to him remained unsold until, in the accumulation of dust upon it, a willow-tree took root and grew up to its full size, an object for curious observation and remark.", _SW2(163))
    + '<p>Wyman names four children: Charles, who died October 16, 1815, aged seven months and seven days; Daniel, who died October 20, 1815, aged nine days, with a gravestone in the &ldquo;new ground&rdquo;; Martha, who married Thatcher Magoun of Medford; and Abby, who married James C. Neilson, M.D., and who died October 5, 1871, aged fifty-one years, one month and fifteen days, with the funeral from 193 Main Street (' + _WY(968) + '). Sawyer gives his age at death as ninety-two (pp. 163&ndash;164).</p>'),
  service='<p>Born in 1776, he was too young for Revolutionary service. He represented Charlestown in the Massachusetts House in 1830, 1832 and 1833 (Sawyer, p. 163).</p>',
  family=('<p>Father: ' + PL("daniel-tufts", "Daniel Tufts (1753&ndash;1839), brick-maker") + '. Mother: Abigail Tufts (Wyman, p. 968). Brothers: ' + PL(_GT, "Gilbert Tufts (1778&ndash;1850)") + ', ' + PL("charles-tufts-1781", "Charles Tufts (1781&ndash;1876)") + ' and ' + PL(_N2, "Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)") + '. Grandfather: ' + PL("nathan-tufts-cordwainer", "Nathan Tufts, cordwainer") + '. Uncles: ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + ' and ' + PL("nathan-tufts-1764", "Nathan Tufts of Charlestown") + '. Wife: Martha Bradshaw, married December 26, 1809. Children as named by Wyman, p. 968: Charles (d. 1815), Daniel (d. 1815), Martha (m. Thatcher Magoun of Medford), and Abby (m. James C. Neilson, M.D.; d. 1871).</p>'),
  unverified='<strong>Places of birth, marriage and burial</strong> are not given by Wyman or Sawyer, beyond the note of a gravestone in the &ldquo;new ground&rdquo; for the infant son Daniel. <strong>The willow-tree kiln</strong> is reported by Sawyer as a local recollection; no independent contemporary notice has been cited here. Note: Pending further work.'))
SP[_DJ] = "<ul><li><strong>Martha (Bradshaw) Tufts.</strong> Married December 26, 1809 (Wyman, vol. 2, p. 968). Her dates and parentage are not given there.</li></ul>"

PROFILES.append(dict(slug=_GT, name="Gilbert Tufts (1778&ndash;1850)", dates="27 April 1778&ndash;7 July 1850", town="Charlestown, Mass.", born="1778", died="1850", era="19th Century",
  line="Son of Daniel Tufts, brick-maker; tanner, of Nathan Tufts &amp; Co.; father of Hon. Arthur W. Tufts",
  bio=('<p>Gilbert Tufts, second son of ' + PL("daniel-tufts", "Daniel Tufts, the Charlestown brick-maker") + ' and Abigail Tufts, was a tanner on the Charlestown peninsula. Wyman records his birth as April 27, 1778, and his marriage to Mary Chickering on December 26, 1810 (' + _WY(968) + ').</p>'
    + Q("Gilbert Tufts was an able and successful business man. I have referred to him in a former article.", _SW2(163))
    + Q("Next below this estate was that of Gilbert Tufts, the father of Honorable Arthur W. Tufts, who, a few years ago, removed from this, his native place, to Boston Highlands, where he has become somewhat distinguished. Gilbert Tufts was of the firm of Nathan Tufts &amp; Co., extensive tanners, who must be mentioned hereafter in a notice of the business of the town. Mr. Tufts sold this estate to Charles Forster, and removed into a new house on Washington Street.", _SW2(39))
    + '<p>The earlier notice is Sawyer&rsquo;s account of the estates below the Abbott house on Cordis Street. Later he records that the Rev. Henry Jackson, on leaving for Hartford, sold his house on Washington Street, nearest Union Street, to Gilbert Tufts:</p>'
    + Q("On his removal to Hartford he sold his house on Washington Street to Gilbert Tufts, who removed here from Cordis Street and died July 7, 1850.", _SW2(87))
    + '<p>His cousin ' + PL("joseph-f-tufts-1790", "Joseph F. Tufts") + ', eldest son of ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + ', &ldquo;carried on an extensive business as a partner with Gilbert Tufts in a tannery on Main Street, near the Neck&rdquo; (' + _SW2(166) + '). Wyman notes a lot purchased of Amos Carleton in 1816 (p. 968). Children named there are Abby, who married Frederick Williams; Gilbert; Caroline, who married Dr. J. E. Bartlett and died in 1851; Sarah Scholfield; and Arthur Webster (p. 968). Mary (Chickering) Tufts died June 24, 1863, as given on a tablet (p. 968).</p>'
    + '<p>Wyman records his death as July 7, 1850, on a granite monument, and as the 9th in the record (p. 968). Sawyer follows the monument and gives his age as seventy-two (pp. 87, 163&ndash;164).</p>'),
  service='<p>Born in 1778, he was too young for Revolutionary service. No civil office is recorded for him in the sources used here.</p>',
  family=('<p>Father: ' + PL("daniel-tufts", "Daniel Tufts (1753&ndash;1839), brick-maker") + '. Mother: Abigail Tufts (Wyman, p. 968). Brothers: ' + PL(_DJ, "Daniel Tufts Jr. (1776&ndash;1868)") + ', ' + PL("charles-tufts-1781", "Charles Tufts (1781&ndash;1876)") + ' and ' + PL(_N2, "Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)") + '. Grandfather: ' + PL("nathan-tufts-cordwainer", "Nathan Tufts, cordwainer") + '. Uncles: ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + ' and ' + PL("nathan-tufts-1764", "Nathan Tufts of Charlestown") + '. Wife: Mary Chickering, married December 26, 1810; died June 24, 1863. Children as named by Wyman, p. 968: Abby (m. Frederick Williams), Gilbert, Caroline (m. Dr. J. E. Bartlett; d. 1851), Sarah Scholfield, and Arthur Webster, the Honorable Arthur W. Tufts of Sawyer, p. 39.</p>'),
  unverified='<strong>Date of death:</strong> the granite monument and Sawyer give July 7, 1850; Wyman also cites a record of the 9th. Not resolved. <strong>Which Nathan</strong> gave his name to the firm Nathan Tufts &amp; Co. is not stated; the likely partner is his uncle ' + PL("nathan-tufts-1764", "Nathan Tufts of Charlestown (c. 1764&ndash;1835)") + ', the well-known tanner, but this is not confirmed. Note: Pending further work.'))
SP[_GT] = "<ul><li><strong>Mary (Chickering) Tufts</strong> (Wyman&rsquo;s Chickering [4]). Married December 26, 1810; died June 24, 1863, as given on a tablet (Wyman, vol. 2, p. 968).</li></ul>"

PROFILES.append(dict(slug=_N2, name="Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)", dates="10 March 1786&ndash;1 August 1872", town="Charlestown and Somerville, Mass.", born="1786", died="1872", era="19th Century",
  line="Youngest son of Daniel Tufts, brick-maker; brick-maker and farmer, Cambridge Street, Somerville",
  bio=('<p>Nathan Tufts, styled &ldquo;2d&rdquo; by Wyman, was the youngest son of ' + PL("daniel-tufts", "Daniel Tufts, the Charlestown brick-maker") + ' and Abigail Tufts. Wyman records his birth as March 10, 1786, his marriage to Sally Miller on February 21, 1811, and his death on August 1, 1872, aged eighty-six, with the funeral on Monday the 5th (' + _WY(968) + ').</p>'
    + Q("Nathan Tufts was a brick-maker and farmer living outside the Neck, just beyond the Lowell Railroad bridge which crosses Cambridge Street in Somerville. He was at one time a tanner. He was a correct and thrifty business man, a member of the Harvard Unitarian Society, and was constant in his attendance at that church.", _SW2(163))
    + Q("He was the father of the late Nathan Tufts, the grain-dealer whose place of business was on Warren Avenue, and who was accidentally killed by being crushed between a vessel and a belay-post on his wharf, October 20, 1887. Mr. Tufts, senior, like all his family, lived to a ripe old age, his death occurring August 1, 1872, when he was eighty-six years old.", _SW2(163))
    + '<p>Wyman lists his children: Sarah Elizabeth (b. November 22, 1811, m. Andrew B. Kidder); Mary Tapley (b. October 1, 1813, d. 1833); Martha (b. November 1, 1815); Nathan (b. January 8, 1818, grain-dealer, m. Mary J. Fitz)&mdash;the son Sawyer names above; Marcellus (b. April 12, 1820, d. 1822); Hannah Johnson (b. October 28, 1822, m. first Dr. Chauncey Booth, &ldquo;who has made genealogical investigations,&rdquo; and second Benjamin F. Allen); Daniel (b. May 6, 1825, d. 1825); and Francis (b. October 13, 1827, Harvard College 1849, LL.B. 1851) (' + _WY(968) + '). Sally Miller was admitted to the Second (Unitarian) Church on November 1, 1835 (p. 968). Wyman also notes purchases of the Rand lot from John Harris&rsquo;s administrators in 1815, land from S. Ireland&rsquo;s guardian in 1818, a partition in 1817, and a purchase from John Tapley in 1819 (p. 968).</p>'
    + '<p>See also the later firm Nathan Tufts &amp; Sons, grain dealers on Warren Avenue, distinguished on the <a href="{P}businesses.html#nathan-tufts-tide-mill">Tide mill of Nathan Tufts</a> entry from his uncle ' + PL("nathan-tufts-1764", "Nathan Tufts of Charlestown (c. 1764&ndash;1835)") + '.</p>'),
  service='<p>Born in 1786, he was too young for Revolutionary service. No civil office is recorded for him in the sources used here, beyond membership in the Harvard Unitarian Society (Sawyer, p. 163).</p>',
  family=('<p>Father: ' + PL("daniel-tufts", "Daniel Tufts (1753&ndash;1839), brick-maker") + '. Mother: Abigail Tufts (Wyman, p. 968). Brothers: ' + PL(_DJ, "Daniel Tufts Jr. (1776&ndash;1868)") + ', ' + PL(_GT, "Gilbert Tufts (1778&ndash;1850)") + ' and ' + PL("charles-tufts-1781", "Charles Tufts (1781&ndash;1876)") + '. Grandfather: ' + PL("nathan-tufts-cordwainer", "Nathan Tufts, cordwainer") + '. Uncles: ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + ' and ' + PL("nathan-tufts-1764", "Nathan Tufts of Charlestown") + '. Wife: Sally Miller, married February 21, 1811. Children as named by Wyman, p. 968, including Nathan (b. 1818), the Warren Avenue grain dealer who died October 20, 1887 (Sawyer, p. 163), and Francis (Harvard 1849).</p>'),
  unverified='<strong>Occupation:</strong> Wyman (p. 968) styles him a grain-dealer, the occupation Sawyer (p. 163) assigns to his son Nathan (1818&ndash;1887). Sawyer&rsquo;s account of the father as a brick-maker and farmer, and at one time a tanner, is followed in the narrative above; whether the father also dealt in grain is not settled. <strong>Place of burial</strong> is not given by Wyman or Sawyer. Note: Pending further work.'))
SP[_N2] = "<ul><li><strong>Sally (Miller) Tufts.</strong> Married February 21, 1811; admitted to the Second (Unitarian) Church, November 1, 1835 (Wyman, vol. 2, p. 968). Her dates and parentage are not given there.</li></ul>"

for _s in (_DJ, _GT, _N2):
    NEWUNCHK.add(_s)

# Wyman pp. 967-968 settled that this Daniel is the cordwainer's son; drop the old "not established" relative link.
REL["daniel-tufts"] = [x for x in REL.get("daniel-tufts", []) if "not established" not in x[1]]
if not any(x[0] == "nathan-tufts-cordwainer" for x in REL["daniel-tufts"]):
    REL["daniel-tufts"].insert(0, ("nathan-tufts-cordwainer", "father Nathan Tufts, cordwainer"))

# Reciprocal family links
REL[_DJ] = [("daniel-tufts", "father Daniel Tufts, brick-maker"), (_GT, "brother Gilbert Tufts (1778&ndash;1850)"), ("charles-tufts-1781", "brother Charles Tufts (1781&ndash;1876)"), (_N2, "brother Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)"), ("nathan-tufts-cordwainer", "grandfather Nathan Tufts, cordwainer"), ("amos-tufts-1762", "uncle Deacon Amos Tufts"), ("nathan-tufts-1764", "uncle Nathan Tufts of Charlestown")]
REL[_GT] = [("daniel-tufts", "father Daniel Tufts, brick-maker"), (_DJ, "brother Daniel Tufts Jr. (1776&ndash;1868)"), ("charles-tufts-1781", "brother Charles Tufts (1781&ndash;1876)"), (_N2, "brother Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)"), ("nathan-tufts-cordwainer", "grandfather Nathan Tufts, cordwainer"), ("amos-tufts-1762", "uncle Deacon Amos Tufts"), ("nathan-tufts-1764", "uncle Nathan Tufts of Charlestown")]
REL[_N2] = [("daniel-tufts", "father Daniel Tufts, brick-maker"), (_DJ, "brother Daniel Tufts Jr. (1776&ndash;1868)"), (_GT, "brother Gilbert Tufts (1778&ndash;1850)"), ("charles-tufts-1781", "brother Charles Tufts (1781&ndash;1876)"), ("nathan-tufts-cordwainer", "grandfather Nathan Tufts, cordwainer"), ("amos-tufts-1762", "uncle Deacon Amos Tufts"), ("nathan-tufts-1764", "uncle Nathan Tufts of Charlestown")]
for _s, _r in [
    ("daniel-tufts", [(_DJ, "son Daniel Tufts Jr. (1776&ndash;1868), tanner"), (_GT, "son Gilbert Tufts (1778&ndash;1850), tanner"), (_N2, "son Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872), brick-maker")]),
    ("charles-tufts-1781", [(_DJ, "brother Daniel Tufts Jr. (1776&ndash;1868)"), (_GT, "brother Gilbert Tufts (1778&ndash;1850)"), (_N2, "brother Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)")]),
    ("nathan-tufts-cordwainer", [(_DJ, "grandson Daniel Tufts Jr."), (_GT, "grandson Gilbert Tufts"), (_N2, "grandson Nathan Tufts &ldquo;2d&rdquo;")]),
    ("amos-tufts-1762", [(_DJ, "nephew Daniel Tufts Jr."), (_GT, "nephew Gilbert Tufts"), (_N2, "nephew Nathan Tufts &ldquo;2d&rdquo;")]),
    ("nathan-tufts-1764", [(_DJ, "nephew Daniel Tufts Jr."), (_GT, "nephew Gilbert Tufts"), (_N2, "nephew Nathan Tufts &ldquo;2d&rdquo;")]),
]:
    REL.setdefault(_s, []); REL[_s] = REL[_s] + _r

# Confirm Abigail Tufts as Daniel's wife (Wyman p. 968); earlier Brooks match was only possible.
SP["daniel-tufts"] = ("<ul><li><strong>Abigail Tufts</strong> (Wyman&rsquo;s Tufts [69]). Named as his wife in Wyman, vol. 2, p. 968; date and place of marriage are not given there.</li></ul>")

# Businesses: Main Street tanneries and Nathan 2d's Somerville brick-yard
_SONS_BIZ = (
  BIZ("charlestown-main-st-tanneries", "Tanneries on Main Street, Charlestown",
    PR(_DJ, "Daniel Tufts Jr.") + " and " + PR(_GT, "Gilbert Tufts"),
    "Tanning (sole-leather); Gilbert also of Nathan Tufts &amp; Co.",
    "Charlestown peninsula: Daniel Jr.&rsquo;s tannery on Main Street; Gilbert and Joseph F. Tufts&rsquo;s tannery on Main Street near the Neck; Gilbert&rsquo;s houses on Cordis and Washington Streets",
    "Early nineteenth century; Gilbert died 1850; Daniel Jr. died 1868",
    Q("Daniel, junior, and Gilbert were tanners. Their tanneries and residences were within the peninsula.", _SW2(163))
    + '<p>' + PR(_DJ, "Daniel Tufts Jr.") + ' kept sole-leather in the vats of his Main Street tannery unsold for years, and a kiln of his bricks stood so long that a willow tree grew to full size upon it (Sawyer, p. 163). ' + PR(_GT, "Gilbert Tufts") + ' was of the firm of Nathan Tufts &amp; Co., extensive tanners; he lived first on Cordis Street and later in a house on Washington Street bought of the Rev. Henry Jackson, and died there on July 7, 1850 (Sawyer, pp. 39, 87). ' + PR("joseph-f-tufts-1790", "Joseph F. Tufts") + ', eldest son of ' + PR("amos-tufts-1762", "Deacon Amos Tufts") + ', was later his partner in a tannery on Main Street near the Neck (Sawyer, p. 166).</p>'
    + UNV("Which Nathan gave his name to Nathan Tufts &amp; Co. is not stated. The likely partner is " + PR("nathan-tufts-1764", "Nathan Tufts of Charlestown (c. 1764&ndash;1835)") + ", the well-known tanner, but this is not confirmed. Note: Pending further work."))
  + BIZ("nathan-2d-cambridge-st", "Nathan Tufts &ldquo;2d,&rdquo; brick-maker, Cambridge Street, Somerville",
    PR(_N2, "Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)"),
    "Brickmaking and farming; at one time tanning",
    "Outside Charlestown Neck, just beyond the Lowell Railroad bridge on Cambridge Street, Somerville",
    "Nineteenth century; he died August 1, 1872",
    Q("Nathan Tufts was a brick-maker and farmer living outside the Neck, just beyond the Lowell Railroad bridge which crosses Cambridge Street in Somerville. He was at one time a tanner.", _SW2(163))
    + '<p>He was a son of ' + PR("daniel-tufts", "Daniel Tufts, the brick-maker") + ' and a brother of ' + PR("charles-tufts-1781", "Charles Tufts") + '. His son Nathan, a grain dealer on Warren Avenue, was killed on his wharf on October 20, 1887 (Sawyer, p. 163). See his ' + PR(_N2, "profile") + '.</p>'
    + UNV("Wyman (p. 968) styles this Nathan a grain-dealer, the occupation Sawyer assigns to the son. Whether the father also dealt in grain is not settled. Note: Pending further work."))
)
if "BIZ_HTML" in globals():
    BIZ_HTML = BIZ_HTML + "{DIV}" + _SONS_BIZ
    page("businesses.html", "Businesses | Tufts Lineage &amp; Legacy", "Places", "Businesses", "The trades of the Tufts family, colonial era to the 19th century", BIZ_HTML)

# Confirm Daniel the brick-maker's sons on his and Charles's pages; drop the superseded "not established" note from the 2026-11-13 run.
_EXTRA_SONS = EXTRA
def EXTRA(path):
    out = _EXTRA_SONS(path)
    if path == "profiles/daniel-tufts.html":
        out = out.replace(
            '{DIV}<p>Sawyer (<em>Old Charlestown</em>, p. 162) names a Daniel Tufts, brick-maker and farmer living outside Charlestown Neck and a legislator in 1811&ndash;12, as a son of ' + PL("nathan-tufts-cordwainer", "Nathan Tufts, cordwainer") + '. Whether he is this Daniel is not established. Note: Pending further work.</p>',
            '')
        out += ('{DIV}<section id="sons"><h2>Sons</h2><p>His four sons now have profiles: '
          + PL(_DJ, "Daniel Tufts Jr. (1776&ndash;1868)") + ', the Main Street tanner and Charlestown legislator; '
          + PL(_GT, "Gilbert Tufts (1778&ndash;1850)") + ', tanner, of Nathan Tufts &amp; Co.; '
          + PL("charles-tufts-1781", "Charles Tufts (1781&ndash;1876)") + ', donor of Walnut Hill; and '
          + PL(_N2, "Nathan Tufts &ldquo;2d&rdquo; (1786&ndash;1872)") + ', brick-maker and farmer on Cambridge Street in Somerville (Wyman, p. 968; Sawyer, pp. 162&ndash;164).</p></section>')
    if path == "generations/19th-century.html":
        out += ('{DIV}<section id="daniel-sons"><h2>The sons of Daniel Tufts, brick-maker</h2><p>'
          + PL(_DJ, "Daniel Tufts Jr.") + ' and ' + PL(_GT, "Gilbert Tufts") + ' were tanners on the Charlestown peninsula; '
          + PL(_N2, "Nathan Tufts &ldquo;2d&rdquo;") + ' was a brick-maker and farmer just beyond the Lowell Railroad bridge on Cambridge Street, Somerville; and '
          + PL("charles-tufts-1781", "Charles Tufts") + ' gave Walnut Hill to Tufts College (Sawyer, pp. 163&ndash;164; Wyman, p. 968).</p></section>')
    if path == "profiles/amos-tufts-1762.html":
        out += ('{DIV}<p>Joseph F. Tufts, the deacon&rsquo;s eldest son, was later a partner of his cousin ' + PL(_GT, "Gilbert Tufts") + ' in a tannery on Main Street near the Neck (Sawyer, p. 166).</p>')
    return out
exec(open("tools/joseph_f_1116.py").read())
