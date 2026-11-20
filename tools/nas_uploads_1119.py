# Nov 19, 2026: photographs, postcards, DAR records and books contributed by Shannon Tufts.
# Kinsmen citations use printed page numbers.
_DARU = lambda n: f'https://services.dar.org/public/dar_research/search_adb/?action=full&amp;p_id={n}'
_DARL = lambda n: f'<a href="{_DARU(n)}">DAR Ancestor no. {n}</a>'
_DARGRS = "DAR Genealogical Research System, Revolutionary War grave and marker records"
_HL2 = lambda pg: f'&ldquo;Charlestown Schools in the 18th Century,&rdquo; <em>Historic Leaves</em> (Somerville Historical Society), vol. 2 (1903&ndash;04), p. {pg}. <a href="https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0302%3Apage%3D{pg}">Text (Perseus)</a>'
_WC = lambda pg: f'Samuel Abbot Smith, <em>West Cambridge on the Nineteenth of April, 1775: An Address Delivered in Behalf of the Ladies&rsquo; Soldiers&rsquo; Aid Society</em> (Boston, 1864), {pg}. <a href="https://archive.org/details/westcambridgeon00massgoog">Internet Archive</a>'
_SANF = '<a href="https://web.archive.org/web/20171107113338/http://www.sanfordclan.com/tuftshouse/">Rich Sanford, &ldquo;The Oliver Tufts House: An Unofficial History&rdquo; (2005, archived copy)</a>'
_ST = "Photo by Shannon Tufts"
_STC = "Shannon Tufts collection"

def _up_img(f, title, cap, who, lic, src, lab):
    IMAGES[f] = (title, cap, who, lic, src, lab)
    global CREDITS
    if f not in CREDITS:
        CREDITS = CREDITS.replace("</ul></section>", f'<li><a href="{{P}}assets/images/{f}">{title}</a>. {who}. {lic}. <a href="{src}">{lab}</a></li></ul></section>', 1)
_SELF = lambda f: "{P}assets/images/" + f

_up_img("oliver-tufts-house-sycamore-street-postcard.jpg", "Old Tufts House, Sycamore Street, Somerville",
  "Early twentieth-century colored postcard: &ldquo;Old Tufts House, Sycamore St., Somerville, Mass.&rdquo; The tablet beside the upper window marks the house as the headquarters of Maj. Gen. Charles Lee during the siege of Boston, 1775&ndash;76. This was the farm of John Tufts (1754&ndash;1839) and of his son Oliver Tufts (1801&ndash;1883).",
  _STC, "Postcard, publisher and date not shown on the image", _SELF("oliver-tufts-house-sycamore-street-postcard.jpg"), "Full-size image")
_up_img("timothy-tufts-house-elm-street-1904-postcard.jpg", "Timothy Tufts House, Elm Street, Somerville",
  "Postcard, &ldquo;Copyright, 1904, by G. O. W. Servis.&rdquo; Its printed caption reads: &ldquo;TIMOTHY TUFTS HOUSE, Elm Street. Somerville, Mass. Built 1761. A sharp fight occurred here between the Patriots and the British on the retreat from Concord and Lexington, April 19, 1775. British soldiers were buried here.&rdquo;",
  _STC, "Public domain (published 1904)", _SELF("timothy-tufts-house-elm-street-1904-postcard.jpg"), "Full-size image")
_up_img("dr-simon-tufts-house-medford-photograph.jpg", "The house of Dr. Simon Tufts, Medford, in an early photograph",
  "An original mounted photograph of the house of Dr. Simon Tufts, later of Turell Tufts, at the corner of High and Forest Streets in Medford Square. It shows the same view that the <em>Medford Historical Register</em> later reproduced as a plate. The house was demolished in 1867, so the photograph is older than that.",
  _STC, "Photographer and date unknown", _SELF("dr-simon-tufts-house-medford-photograph.jpg"), "Full-size image")
_up_img("dr-simon-tufts-house-ai-enhanced-shannon-tufts.jpg", "AI-enhanced rendition of the house of Dr. Simon Tufts",
  "AI-enhanced rendition by Shannon Tufts of the photograph at left/above. It is not a historical photograph; see the original for how the house actually looked.",
  "Shannon Tufts (AI-enhanced rendition)", "Modern AI-enhanced artwork, used with the creator&rsquo;s permission",
  _SELF("dr-simon-tufts-house-ai-enhanced-shannon-tufts.jpg"), "Full-size image")
_SIMHOUSE_PAIR = ('<div class="fig-row">'
  + FIG("dr-simon-tufts-house-medford-photograph.jpg")
  + FIG("dr-simon-tufts-house-ai-enhanced-shannon-tufts.jpg")
  + '</div>')
_up_img("peter-tufts-house-cradock-insurance-card.jpg", "&ldquo;The Oldest House in America&rdquo;: an insurance trade card",
  "A nineteenth-century trade card of the Commercial Union Assurance Co. showing the Medford brick house then called the Cradock Mansion, &ldquo;Built 1634.&rdquo; Later research dates the house to about 1677&ndash;1680 and connects it with Peter Tufts rather than Matthew Cradock&rsquo;s agents.",
  _STC, "Publisher&rsquo;s card, nineteenth century", _SELF("peter-tufts-house-cradock-insurance-card.jpg"), "Full-size image")
_up_img("peter-mary-tufts-gravestone-bell-rock-shannon-tufts.jpg", "Gravestone of Peter and Mary Tufts, Bell Rock Cemetery, Malden",
  "The carved slate of Peter Tufts the immigrant and his wife Mary, Bell Rock Cemetery, Malden, with Shannon Tufts. Inscription: &ldquo;Here lyes the body of Peter Tufts aged 83 years died May 13 1700. Also here lyes y<sup>e</sup> body of Mary Tufts his wife aged 75 years died January 1702/3.&rdquo;",
  _ST, "Used with permission", _SELF("peter-mary-tufts-gravestone-bell-rock-shannon-tufts.jpg"), "Full-size image")
_up_img("peter-anne-tufts-gravestones-phipps-street-shannon-tufts.jpg", "Gravestones of Peter and Anne Tufts, Phipps Street Burying Ground, Charlestown",
  "Shannon Tufts between the slates of Peter Tufts of Winter Hill (right: &ldquo;Here lyes buried the body of Mr. Peter Tufts, who departed this life &hellip;&rdquo;) and Anne Adams Tufts (left: &ldquo;In memory of Mrs. Anne Tufts &hellip;&rdquo;). The lower lines of both stones are worn.",
  _ST, "Used with permission", _SELF("peter-anne-tufts-gravestones-phipps-street-shannon-tufts.jpg"), "Full-size image")
_up_img("anne-adams-tufts-doorstone-tablet-shannon-tufts.jpg", "The Anne Adams Tufts doorstone tablet, Somerville",
  "Bronze tablet on the doorstone of her home: &ldquo;To the memory of Anne Adams Tufts, born 1729, died 1813. A heroine of the Revolution who did active patriotic service after the Battle of Bunker Hill. This was the door-stone of her home which stood about 120 feet south-west of this spot. This tablet is placed by the Somerville Chapter of the Daughters of the American Revolution which is honored in bearing her name. 1909.&rdquo;",
  _ST, "Used with permission", _SELF("anne-adams-tufts-doorstone-tablet-shannon-tufts.jpg"), "Full-size image")
_up_img("medford-minutemen-monument-shannon-tufts.jpg", "Medford&rsquo;s monument to its First Company of Minute Men",
  "Shannon Tufts beside the bronze &ldquo;Roster of the First Company of Minute Men who assembled in Medford at the call of Paul Revere and engaged in the Battle of April 19, 1775,&rdquo; erected by the City of Medford on the 150th anniversary (1925). Peter Tufts Jr. and eight other men named Tufts are on the roster.",
  _ST, "Used with permission", _SELF("medford-minutemen-monument-shannon-tufts.jpg"), "Full-size image")
_up_img("malden-revolution-tablet-shannon-tufts.jpg", "Malden&rsquo;s tablet to its soldiers and sailors of the Revolution",
  "&ldquo;To the memory of the soldiers and sailors of the American Revolution who enlisted from Malden,&rdquo; placed by the Malden Chapter, Sons of the American Revolution, and the Deliverance Monroe Chapter, Daughters of the American Revolution. In the fourth column are Adam Tufts, John Tufts, Stephen Tufts and Timothy Tufts. Capt. Benjamin Blaney heads the first column.",
  _ST, "Used with permission", _SELF("malden-revolution-tablet-shannon-tufts.jpg"), "Full-size image")
_up_img("clip-spy-simon-tufts-store-ad.jpg", "Clipping: &ldquo;To be SOLD, by SIMON TUFTS&rdquo;",
  "Advertisement in <em>The Massachusetts Spy</em> (Boston), from the Library of Congress&rsquo;s Chronicling America scans.",
  "<em>The Massachusetts Spy</em>, via Library of Congress, Chronicling America", "Public domain",
  "https://chroniclingamerica.loc.gov/lccn/sn83021193/1770-09-01/ed-1/seq-1/", "Chronicling America")
_BRM = "https://bostonraremaps.com/inventory/peter-tufts-survey-concord-cambridge-1797/"
_up_img("peter-tufts-jr-road-survey-1797-sheet.jpg", "Peter Tufts Jr.&rsquo;s road survey, Concord to Cambridge, 1797",
  "The whole sheet: &ldquo;This Plan Laid down by a Scale of Half-Mile per inch By Peter Tufts junior June 14th 1797,&rdquo; ink and watercolor on two joined sheets, about 9&frac12; by 31 inches.",
  "Boston Rare Maps (dealer&rsquo;s photograph, inventory BRM3348)", "Manuscript of 1797, public domain", _BRM, "Boston Rare Maps listing")
_up_img("peter-tufts-jr-road-survey-1797-compass.jpg", "Detail: the compass rose and the road through Concord",
  "Detail of the 1797 survey, with its ink-and-watercolor compass rose. The dealer notes that East and West are reversed on it.",
  "Boston Rare Maps (dealer&rsquo;s photograph, inventory BRM3348)", "Manuscript of 1797, public domain", _BRM, "Boston Rare Maps listing")

def _up_get(slug):
    for _p in PROFILES:
        if _p["slug"] == slug: return _p
    return None
def _up_add(slug, html, mark, field="bio"):
    _p = _up_get(slug)
    if _p is None: return False
    if mark not in _p.get(field, ""): _p[field] = _p.get(field, "") + html
    return True
def _up_unv(slug, text):
    _p = _up_get(slug)
    if _p is None: return
    u = _p.get("unverified", "")
    if text not in u: _p["unverified"] = (u + " " if u else "") + text
def _dar_sec(slug, html, unv=None, sid="dar-records"):
    body = f'<section id="{sid}"><h2>In the DAR Records</h2>' + html + (UNV(unv) if unv else "") + '</section>'
    _up_add(slug, body, f'id="{sid}"')

# =====================================================================
# 1. The Sycamore Street house: new profile of Oliver Tufts (1801-1883)
# =====================================================================
_OT = "oliver-tufts-1801"
_JOHN_Q = ("John Tufts had come up from his home in Somerville to take his part in the events of the day. He chanced to meet a young woman, Elizabeth Perry by name, wandering in the fields in a state of great anxiety and fear. The young man, though he had never seen her before, gallantly offered his protection, which she thankfully accepted; and, as for the result, it need only be said that her name afterwards became Elizabeth Tufts.")
_nf_new(_OT, "Oliver Tufts (1801&ndash;1883)", "20 October 1801 &ndash; 18 May 1883", "Charlestown, later Somerville (Sycamore Street), Mass.", "1801", "1883", "19th Century",
  "Son of John and Elizabeth (Perry) Tufts; farmer of the Sycamore Street homestead",
  '<p>Oliver Tufts was born in Charlestown, in the part that became Somerville, on October 20, 1801. He was the youngest of the twelve children of ' + PL("john-tufts-53-3", "John Tufts (1754&ndash;1839)") + ' and Elizabeth (Perry) Tufts. He was born on the family farm on what is now Sycamore Street, lived there all his life, and died there of paralysis on May 18, 1883 (' + TKV(238, "130-12") + ').</p>'
  + '<p>He was a farmer and a large landowner. When Somerville was set off from Charlestown in 1842, he became the new town&rsquo;s first assessor. He also served as an overseer of the poor for a number of years and was one of the founders of the Unitarian church on Highland Avenue (' + TKV(238) + '). Edward C. Booth wrote that Oliver farmed the old place until his death in 1883 (' + BOOTH + ', pp. 23&ndash;24. <a href="' + BOOTH_URL + '7">Text (Perseus)</a>).</p>'
  + '<section id="sycamore-street-house"><h2>The House on Sycamore Street</h2>'
  + FIG("oliver-tufts-house-sycamore-street-postcard.jpg", "hfig-flow mi-inline")
  + '<p>The house had been General Charles Lee&rsquo;s headquarters during the siege of Boston, 1775&ndash;76. Peter Tufts of Winter Hill set his son John up on this farm during the Revolution, and it passed from John to Oliver (' + BOOTH + ', p. 23. <a href="' + BOOTH_URL + '7">Text (Perseus)</a>). It stands today at 78 Sycamore Street, moved a short distance from its first site; see <a href="{P}places.html#homesteads">Places: Homesteads</a>.</p>'
  + '<p>An unofficial history of the house, compiled by a resident from the files of the Somerville Historical Society, says it was built between 1714 and 1719 by a Mr. Mattison (or Watson), whose family owned the land until 1778. It says the house first stood on a knoll at what is now the corner of Sycamore and Pembroke Streets, and that Sycamore Street began as its private drive (' + _SANF + ').</p>'
  + '<p>Oliver&rsquo;s only child, Annie Louise Tufts, was born in the house on October 31, 1839. She married Dr. William Kelley Fletcher in 1874 and died in Somerville on October 7, 1917, leaving no children (' + TKV2(158, "302-1") + ').</p></section>'
  + '<section id="april-1775-story"><h2>A Family Story of April 19, 1775</h2>'
  + '<p>Oliver was the source of one of the best-known stories about his parents. In 1864 Samuel Abbot Smith, speaking at West Cambridge (now Arlington), told how John Tufts met Elizabeth Perry on the day of Lexington and Concord, and named &ldquo;Oliver Tufts&rdquo; in a footnote as his authority:</p>'
  + Q(_JOHN_Q, _WC("pp. 50&ndash;51") + '; the footnote on p. 51 reads &ldquo;Oliver Tufts.&rdquo;')
  + '<p>The same story, told later by Ellen Chase, is on ' + PL("john-tufts-1754", "his father&rsquo;s profile") + '.</p></section>',
  '<p>Born after the Revolution; no military service is recorded for him.</p>',
  '<p>Father: ' + PL("john-tufts-53-3", "John Tufts (1754&ndash;1839)") + '. Mother: Elizabeth (Perry) Tufts (1759&ndash;1844). He was the twelfth child; his brothers and sisters included Asa Tufts (1799&ndash;1836), cordwainer, whose widow he married (' + TKV(238) + '). Child: Annie Louise (1839&ndash;1917), wife of Dr. William Kelley Fletcher (' + TKV2(158) + ').</p>',
  '<strong>The house&rsquo;s building date</strong> (1714&ndash;1719) and its builder come from an unofficial modern history, not from a deed or other record. <strong>Visits by Washington</strong> to the house are mentioned in the family record as tradition, not documented here. <strong>The postcard&rsquo;s</strong> publisher and date are not shown on the card. Note: Pending further work.',
  "<ul><li><strong>Dorothy (Danforth) Tufts</strong> (b. July 28, 1797, at Lynn; d. February 7, 1875, at Somerville), daughter of Joshua and Lydia (Sweetser) Danforth and widow of his brother Asa Tufts; married November 21, 1838, at Cambridge, by the Rev. James D. Green (" + TKV(238) + ").</li></ul>",
  [("john-tufts-53-3", "father John Tufts (1754&ndash;1839)", "son Oliver Tufts (1801&ndash;1883)"),
   ("john-tufts-1754", "father John Tufts (b. 1754)", "son Oliver Tufts (1801&ndash;1883)"),
   ("peter-tufts-winter-hill", "grandfather Peter Tufts of Winter Hill", "grandson Oliver Tufts (1801&ndash;1883)"),
   ("anne-adams-tufts", "grandmother Anne Adams Tufts", "grandson Oliver Tufts (1801&ndash;1883)")])
# The two John Tufts pages describe the same man.
_nf_rel("john-tufts-53-3", "john-tufts-1754", "the same man: see also John Tufts (b. 1754)", "the same man: see also Cpl. John Tufts (1754&ndash;1839)")
for _j in ("john-tufts-1754", "john-tufts-53-3"):
    _up_add(_j, '<section id="sycamore-street-farm"><h2>The Sycamore Street Farm</h2>' + FIG("oliver-tufts-house-sycamore-street-postcard.jpg", "hfig-flow mi-inline")
      + '<p>The farm his father gave him during the Revolution, with General Lee&rsquo;s headquarters house, stayed in the family through his son ' + PL(_OT, "Oliver Tufts (1801&ndash;1883)") + ', who was born and died there. Samuel Abbot Smith&rsquo;s 1864 address at West Cambridge tells of John&rsquo;s meeting with Elizabeth Perry on April 19, 1775, on Oliver&rsquo;s authority (' + _WC("pp. 50&ndash;51") + ').</p></section>', 'id="sycamore-street-farm"')
_dar_sec("john-tufts-53-3", '<p>The DAR lists him as ' + _DARL("A116799") + ': corporal, Massachusetts, in Capt. Isaac Hall&rsquo;s company; born November 24, 1754, at Cambridge; died September 10, 1839, at Somerville.</p>',
  "The DAR gives his birthplace as Cambridge and his death as September 10, 1839; the family record gives Charlestown (now Somerville) and September 9, 1839 (" + TKV(105, "53-3") + "). Note: Pending further work.")
_dar_sec("john-tufts-1754", '<p>He is ' + _DARL("A116799") + ' in the DAR Ancestor Database (corporal, Capt. Isaac Hall&rsquo;s company; died 1839). See ' + PL("john-tufts-53-3", "Cpl. John Tufts (1754&ndash;1839)") + ', which describes the same man.</p>')
DAR["john-tufts-53-3"] = f'A116799 (<a href="{_DARU("A116799")}">DAR Ancestor Database</a>)'
DAR["john-tufts-1754"] = DAR["john-tufts-53-3"]

# =====================================================================
# 2. Timothy Tufts and the Elm Street house
# =====================================================================
_TIM = _up_get("timothy-tufts")
if _TIM:
    _TIM["bio"] = _TIM["bio"] + ('<section id="elm-street-house"><h2>The House on Elm Street</h2>'
      + FIG("timothy-tufts-house-elm-street-1904-postcard.jpg", "hfig-flow mi-inline")
      + '<p>A postcard copyrighted in 1904 by G. O. W. Servis shows the house standing behind its fence on Elm Street. The family record describes the farm on Milk Row (Elm Street near Willow Avenue), Anne Tufts watching from her bedroom as the column halted to drink at their well on the night of April 18, and the British dead buried in a common grave in the front yard, where a marker in the sidewalk identifies the site (' + TKV(52, "18-4") + ').</p>'
      + '<p>The family record also settles his dates. He was born at Charlestown on January 20, 1734/5, which explains why some lists say 1734 and others 1735. He married Anne Adams, daughter of Dea. Joseph Adams Jr. and Martha (Frost) Adams of Menotomy, at Cambridge on May 7, 1761. He died at Charlestown on February 18, 1805 (' + TKV(52) + ').</p></section>')
    _TIM["unverified"] = _TIM.get("unverified", "").replace("<strong>Death year 1805</strong> is worked out from Booth&rsquo;s &ldquo;three years before his father&rdquo;, not from a record. ", "").replace("a modern Historypin caption says 1761.", "a modern Historypin caption and the 1904 Servis postcard both say 1761, the year of his marriage.")
_dar_sec("timothy-tufts", '<p>The DAR lists him as ' + _DARL("A116816") + ': patriotic service, Massachusetts, &ldquo;Charlestown, loaned money to government&rdquo;; born January 20, 1734, and died February 18, 1805, at Charlestown.</p>')
DAR["timothy-tufts"] = f'A116816 (<a href="{_DARU("A116816")}">DAR Ancestor Database</a>)'

# =====================================================================
# 3. Samuel Tufts of Milk Row (1737-1828)
# =====================================================================
_SM = "samuel-tufts-18-5"
_nf_new(_SM, "Samuel Tufts of Milk Row (1737&ndash;1828)", "24 November 1737 &ndash; 24 October 1828", "Milk Row, Charlestown (now Somerville), Mass.", "1737", "1828", "The Revolution",
  "Son of Peter and Lydia (Bucknam) Tufts; brother of Timothy and of Peter of Winter Hill",
  '<p>Samuel Tufts, farmer, was born at Charlestown on November 24, 1737, a son of ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + ' and Lydia (Bucknam) Tufts. He lived on Milk Row, now Somerville Avenue near Laurel Street. On the night of April 18, 1775, he was still up, casting bullets with his slave in a hut behind the house, when the British column went quietly by. A neighbor, the widow Rand, saw the soldiers and ran across the road to tell him. At first he did not believe her. Then his lantern showed the many footprints in the dirt road, and he rode by a bridle path to Cambridge to spread the alarm (' + TKV("52&ndash;53", "18-5") + '). The story is told on ' + PL("timothy-tufts", "his brother Timothy&rsquo;s profile") + ' from Ellen Chase&rsquo;s account.</p>'
  + '<p>He later served as a private. He headed his household in the 1810 and 1820 censuses and died at Charlestown on October 24, 1828 (' + TKV(53) + ').</p>',
  '<p>The DAR lists him as ' + _DARL("A116814") + ': civil and patriotic service, Massachusetts. He suffered losses to the British in 1775, was town treasurer of Charlestown in 1777&ndash;1778 and 1780, and selectman in 1780. The DAR cites Hunnewell&rsquo;s <em>A Century of Town Life</em> (vol. 9, p. 173) and the Charlestown town records. The DAR grave index gives his service as private in Capt. Isaac Hall&rsquo;s company, Col. Thomas Gardner&rsquo;s regiment, and his burial as the Somerville Cemetery (' + _DARGRS + ').</p>',
  '<p>Father: ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + '. Brothers: ' + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill (1728&ndash;1791)") + ' and ' + PL("timothy-tufts", "Timothy Tufts (1735&ndash;1805)") + '. Children: Samuel, Martha, Lydia, Susanna, Mary, and Elizabeth (' + TKV(52) + ').</p>',
  '<strong>Burial place:</strong> the DAR grave index names the Somerville Cemetery; no stone has been seen. <strong>Which company he served in</strong> is given by the DAR but not by the family record, which says only that he was a private. Note: Pending further work.',
  "<ul><li><strong>Martha Adams</strong> (b. September 25, 1746, at Menotomy; d. August 18, 1811, at Charlestown), daughter of Dea. Joseph Adams Jr. and Martha (Frost) Adams and sister of his brother Timothy&rsquo;s wife; married May 11, 1769, at Menotomy (" + TKV(52) + ").</li></ul>",
  [("peter-tufts-1697", "father Peter Tufts (1697&ndash;1776)", "son Samuel Tufts of Milk Row (1737&ndash;1828)"),
   ("timothy-tufts", "brother Timothy Tufts (1735&ndash;1805)", "brother Samuel Tufts of Milk Row (1737&ndash;1828)"),
   ("peter-tufts-winter-hill", "brother Peter Tufts of Winter Hill", "brother Samuel Tufts of Milk Row (1737&ndash;1828)")], rw="pistol")
DAR[_SM] = f'A116814 (<a href="{_DARU("A116814")}">DAR Ancestor Database</a>)'

# =====================================================================
# 4. Malden: John (1739-1799), Stephen Jr. (1749-1832), Capt. Timothy (1756-1810)
# =====================================================================
_MALFIG = FIG("malden-revolution-tablet-shannon-tufts.jpg", "hfig-flow mi-inline")
_JM = "john-tufts-19-5"; _SJ = "stephen-tufts-21-1"; _TM = "timothy-tufts-21-4"
_nf_new(_JM, "John Tufts of Malden (1739&ndash;1799)", "15 March 1738/9 &ndash; 23 March 1799", "Medford and Malden, Mass.", "1739", "1799", "The Revolution",
  "Son of Benjamin and Mary (Hutchinson) Tufts; soldier from Malden",
  '<p>John Tufts was born in Medford on March 15, 1738/9, a son of Benjamin and Mary (Hutchinson) Tufts, and lived in Malden. In June 1776 he went with Capt. Benjamin Blaney&rsquo;s company on the expedition to Point Shirley, now Winthrop. He was head of a household in the 1790 census and died at Malden on March 23, 1799 (' + TKV(55, "19-5") + ').</p>'
  + '<section id="malden-tablet"><h2>On Malden&rsquo;s Revolutionary Tablet</h2>' + _MALFIG
  + '<p>A John Tufts is named on Malden&rsquo;s bronze tablet to the soldiers and sailors who enlisted from the town, along with Adam, Stephen and Timothy Tufts. Capt. Benjamin Blaney heads its list.</p></section>',
  '<p>The DAR lists him as ' + _DARL("A116803") + ': private, Massachusetts, in Capt. Benjamin Blaney&rsquo;s company; born March 15, 1739, at Medford; died February 23, 1799, at Malden. The family record adds the Point Shirley expedition of June 1776 (' + TKV(55) + ').</p>',
  '<p>Parents: Benjamin and Mary (Hutchinson) Tufts. A brother, Benjamin, is probably the ' + PL("benjamin-tufts", "Benjamin Tufts") + ' of Medford on this site. Children by his first wife: John, Asa, and Josiah. By his second: Elias and Peter (' + TKV(55) + ').</p>',
  '<strong>Date of death:</strong> the family record gives March 23, 1799, and the DAR gives February 23, 1799. <strong>Which John Tufts</strong> is on the Malden tablet is not stated there; his son John Jr. (1764&ndash;1845), also of Malden, is another candidate. Note: Pending further work.',
  "<ul><li><strong>Rebecca Hawkes</strong> (1746&ndash;1769), daughter of John and Hannah (Priest) Hawkes of Lynn; married April 28, 1763, at Lynn.</li><li><strong>Lois Taylor</strong> (1748&ndash;1834), daughter of Ebenezer and Mary (Gowing) Taylor of Reading; married June 15, 1773, at Reading (" + TKV(55) + ").</li></ul>",
  [("benjamin-tufts", "probable brother Benjamin Tufts", "probable brother John Tufts of Malden (1739&ndash;1799)")], rw="pistol")
DAR[_JM] = f'A116803 (<a href="{_DARU("A116803")}">DAR Ancestor Database</a>)'
_nf_new(_SJ, "Stephen Tufts Jr., Miller, of Malden (1749&ndash;1832)", "28 March 1749 &ndash; 12 March 1832", "Malden, Mass.", "1749", "1832", "The Revolution",
  "Son of Stephen and Katherine (Taylor) Tufts; miller on Spot Pond Brook",
  '<p>Stephen Tufts Jr. was born at Malden on March 28, 1749, the eldest son of Stephen Tufts, schoolmaster, and Katherine (Taylor) Tufts. He owned the mill privileges on Spot Pond Brook and lived in the old Tufts house on the bank of the Malden River. He died at Malden on March 12, 1832 (' + TKV(58, "21-1") + ').</p>'
  + '<p>He turned out as a private at the Lexington alarm in 1775 and served in Col. Thomas Gardner&rsquo;s regiment. The family record also passes on a tradition. Stephen was known as a marksman, and on the day of Bunker Hill he is said to have rowed down the river, hidden his boat in the bushes on the Charlestown shore behind the British lines, and fired into the flank of the advancing Regulars (' + TKV(58) + ').</p>'
  + '<section id="malden-tablet"><h2>On Malden&rsquo;s Revolutionary Tablet</h2>' + _MALFIG
  + '<p>A Stephen Tufts is named on Malden&rsquo;s tablet to the town&rsquo;s soldiers and sailors. The DAR also records a Revolutionary grave marker for a Stephen Tufts at Bell Rock Cemetery, Malden, placed by the Mystic Side Chapter (' + _DARGRS + ').</p></section>',
  '<p>Private at the Lexington alarm, 1775; Col. Thomas Gardner&rsquo;s regiment (' + TKV(58) + ').</p>',
  '<p>Parents: Stephen Tufts (1711&ndash;1785), schoolmaster, and Katherine (Taylor) Tufts. Brother: ' + PL(_TM, "Capt. Timothy Tufts (1756&ndash;1810)") + '. Children: Stephen, John, Stephen, Hannah, Rebecca, Nancy, Simon, Sarah, Mary, and Joseph W. (' + TKV(58) + ').</p>',
  '<strong>Bunker Hill:</strong> his shooting from the Charlestown shore is family tradition, with no muster roll or other record. <strong>Which Stephen</strong> the Malden tablet and the Bell Rock marker honor is not stated; his father, the schoolmaster (d. 1785), is buried at Malden too. Note: Pending further work.',
  "<ul><li><strong>Hannah Farrington</strong> (1754&ndash;1820), daughter of John and Hannah (Hawkes) Farrington; married June 10, 1773, at Malden (" + TKV(58) + ").</li></ul>",
  [(_TM, "brother Capt. Timothy Tufts (1756&ndash;1810)", "brother Stephen Tufts Jr. (1749&ndash;1832)"),
   (_JM, "cousin John Tufts of Malden (1739&ndash;1799)", "cousin Stephen Tufts Jr. (1749&ndash;1832)"),
   ("peter-tufts-1617", "great-grandfather Peter Tufts the immigrant", "great-grandson Stephen Tufts Jr. of Malden (1749&ndash;1832)")], rw="pistol")
_nf_new(_TM, "Capt. Timothy Tufts, Master Mariner (1756&ndash;1810)", "15 April 1756 &ndash; April 1810", "Malden, Mass.; Baltimore, Md.", "1756", "1810", "The Revolution",
  "Son of Stephen and Katherine (Taylor) Tufts; corporal from Malden; later a Baltimore sea captain",
  '<p>Timothy Tufts was born at Malden on April 15, 1756, a son of Stephen and Katherine (Taylor) Tufts. He served as a corporal in the Revolution: he answered the Lexington alarm with Capt. Benjamin Blaney, went on the Point Shirley expedition in June 1776, and on September 26, 1776, was drafted and marched as third corporal under Col. Brooks for Horse Neck (' + TKV("58&ndash;59", "21-4") + ').</p>'
  + '<p>After the war he moved to Baltimore and followed the sea as a master mariner. He married a widow, Elizabeth (Margeon) Aveneaux, at Paris on November 6, 1796. In 1809 he was master of the ship <em>Elizabeth</em>, in port at Santiago de Cuba. He died at Baltimore in April 1810 (' + TKV(59) + ').</p>'
  + '<section id="malden-tablet"><h2>On Malden&rsquo;s Revolutionary Tablet</h2>' + _MALFIG
  + '<p>A Timothy Tufts is named on Malden&rsquo;s tablet to the soldiers and sailors who enlisted from the town.</p></section>',
  '<p>Corporal: the Lexington alarm with Capt. Benjamin Blaney; Point Shirley, June 1776; Horse Neck, September 1776 (' + TKV(59) + ').</p>',
  '<p>Parents: Stephen and Katherine (Taylor) Tufts. Brother: ' + PL(_SJ, "Stephen Tufts Jr. (1749&ndash;1832)") + '. Child: William (' + TKV(59) + ').</p>',
  '<strong>Which Timothy</strong> the Malden tablet names is not stated there; this Timothy, born at Malden and serving under Capt. Blaney, is the likeliest. Note: Pending further work.',
  "<ul><li><strong>Elizabeth (Margeon) Aveneaux</strong> (b. November 6, 1769, at London; d. June 22, 1812, at Baltimore), daughter of Pierre and Eleanor (Meyer) Margeon of Paris, and widow of Pierre Aveneaux; married November 6, 1796, at Paris (" + TKV(59) + ").</li></ul>",
  [], rw="pistol")
_up_add("adam-tufts", '<section id="malden-tablet"><h2>On Malden&rsquo;s Revolutionary Tablet</h2>' + _MALFIG
  + '<p>Adam Tufts heads the four men of the name on Malden&rsquo;s bronze tablet to the soldiers and sailors who enlisted from the town. The others are ' + PL(_JM, "John") + ', ' + PL(_SJ, "Stephen") + ' and ' + PL(_TM, "Timothy") + '.</p></section>', 'id="malden-tablet"')
for _o, _l in [(_JM, "John Tufts of Malden"), (_SJ, "Stephen Tufts Jr. of Malden"), (_TM, "Capt. Timothy Tufts of Malden")]:
    _nf_rel("adam-tufts", _o, f"also on the Malden tablet: {_l}", "also on the Malden tablet: Adam Tufts")

# =====================================================================
# 5. Ebenezer Tufts (1761-1830), brother of Eliakim
# =====================================================================
_EB = "ebenezer-tufts-87-4"
_nf_new(_EB, "Ebenezer Tufts (1761&ndash;1830)", "19 April 1761 &ndash; 27 November 1830", "Medford; Billerica, Mass.; Marlborough and Roxbury, N.H.", "1761", "1830", "The Revolution",
  "Son of William and Katherine (Tufts) Tufts; Revolutionary pensioner; farmer in New Hampshire",
  '<p>Ebenezer Tufts, farmer, was born in Medford on April 19, 1761, a son of William and Katherine (Tufts) Tufts and an older brother of ' + PL("eliakim-tufts-87-6", "Eliakim Tufts") + '. He married Hannah Livingston at Billerica in 1781, and the family later moved to Cheshire County, New Hampshire. Hannah died at Marlborough in 1802, and he died at Roxbury, New Hampshire, on November 27, 1830 (' + TKV(164, "87-4") + ').</p>',
  '<p>The DAR lists him as ' + _DARL("A116789") + ': private, Massachusetts, in Capt. John Wood&rsquo;s company, Col. Loammi Baldwin&rsquo;s regiment, with a Revolutionary pension (file &ldquo;S&rdquo;); born April 19, 1761, at Medford; died November 27, 1830, at Roxbury, N.H.</p>',
  '<p>Parents: William and Katherine (Tufts) Tufts. Brother: ' + PL("eliakim-tufts-87-6", "Eliakim Tufts (1767&ndash;1825)") + '. Children by Hannah: Hannah, Catherine, William, Ebenezer, Betsey, Eliakim, Lydia, Catherine, and Phebe. By Elizabeth: Abigail and Eliakim (' + TKV(164) + ').</p>',
  '<strong>Service details</strong> beyond the DAR summary have not been checked in <em>Massachusetts Soldiers and Sailors</em> or the pension file. Note: Pending further work.',
  "<ul><li><strong>Hannah Livingston</strong> (1760&ndash;1802), daughter of Thomas and Phebe (Stone) Livingston of Billerica; married April 27, 1781, at Billerica.</li><li><strong>Elizabeth (Betsey) Travis</strong> (b. 1765, Holliston), daughter of John and Anna (Maxwell) Travis; married November 25, 1802, in Sullivan County, N.H.; living in 1820 at Detroit with her stepdaughter Phebe (Tufts) Scales (" + TKV(164) + ").</li></ul>",
  [("eliakim-tufts-87-6", "brother Eliakim Tufts (1767&ndash;1825)", "brother Ebenezer Tufts (1761&ndash;1830)")], rw="pistol")
DAR[_EB] = f'A116789 (<a href="{_DARU("A116789")}">DAR Ancestor Database</a>)'

# =====================================================================
# 6. DAR numbers and grave records for existing profiles
# =====================================================================
def _dar_id(slug, n, note=""):
    DAR[slug] = f'{n} (<a href="{_DARU(n)}">DAR Ancestor Database</a>)' + note
for _s, _n in [("anne-adams-tufts", "A116782"), ("david-tufts-41-7", "A116788"), ("eliakim-tufts-87-6", "A116790"), ("francis-tufts-20-1", "A116791"),
               ("francis-tufts-41-4", "A116795"), ("henry-tufts-1716", "A216175"), ("james-tufts-82-3", "A116797"), ("jonathan-tufts-36-8", "A116806"),
               ("joseph-tufts-1755", "A116810"), ("joseph-tufts-jr-15-2", "A116807"), ("peter-tufts-jr", "A116812"), ("peter-tufts-winter-hill", "A116811"),
               ("peter-tufts-1697", "A116809"), ("william-tufts-40-2", "A116819"), ("benjamin-tufts", "A116786")]:
    _dar_id(_s, _n)
DAR["benjamin-tufts"] += " (probable identification; see the DAR section)"
DAR["william-tuffs-35-8"] = f'Possibly A116818 (<a href="{_DARU("A116818")}">DAR Ancestor Database</a>); the DAR marks that record as under correction'

_dar_sec("anne-adams-tufts", FIG("anne-adams-tufts-doorstone-tablet-shannon-tufts.jpg", "hfig-flow mi-inline")
  + '<p>The DAR lists her as ' + _DARL("A116782") + ', born July 8, 1729, at Lexington, and died February 7, 1813, at Medford, with the notice that future applicants must prove correct service. Its marker index records the doorstone tablet shown here, placed in 1909 at Winter Hill by the chapter named for her and presented to the city. Its grave index places her in the Old Phipps Burying Ground, Charlestown, and gives her service as taking eight wounded soldiers from the Battle of Bunker Hill into her home and caring for them and others (' + _DARGRS + ').</p>'
  + FIG("peter-anne-tufts-gravestones-phipps-street-shannon-tufts.jpg", "hfig-flow mi-inline"),
  "<strong>Birth and death:</strong> the DAR ancestor record gives Lexington and Medford, and its grave index gives a death date of February 13, 1813. Find a Grave gives Cambridge and Charlestown, February 7, 1813. Note: Pending further work.")
_dar_sec("peter-tufts-winter-hill", FIG("peter-anne-tufts-gravestones-phipps-street-shannon-tufts.jpg", "hfig-flow mi-inline")
  + '<p>The DAR lists him as ' + _DARL("A116811") + ' (&ldquo;Peter Tufts Jr.&rdquo;): civil and patriotic service, Massachusetts. He suffered losses at the burning of Charlestown and was a selectman in 1776. The record gives his baptism as April 28, 1728, at Cambridge, and his death as March 4, 1791.</p>'
  + '<p>His slate and his wife&rsquo;s stand side by side in the Phipps Street Burying Ground, Charlestown (photograph above).</p>',
  "<strong>Place of death:</strong> the DAR record says Medford; Find a Grave places his death at Charlestown. Note: Pending further work.")
_dar_sec("peter-tufts-1697", '<p>The DAR lists him as ' + _DARL("A116809") + ' (&ldquo;Peter Tufts Sr.&rdquo;), born May 10, 1697, and died December 5, 1776, both at Charlestown. No service is stated, and the DAR notes that future applicants must prove correct service.</p>')
_dar_sec("peter-tufts-jr", FIG("medford-minutemen-monument-shannon-tufts.jpg", "hfig-flow mi-inline")
  + '<p>The DAR lists him as ' + _DARL("A116812") + ' (&ldquo;Peter Tufts III&rdquo;): private, Massachusetts; born January 9, 1753, and died November 4, 1833, at Medford. Its grave index gives his service as the Lexington alarm in Capt. Isaac Hall&rsquo;s company, Col. Thomas Gardner&rsquo;s regiment (' + _DARGRS + ').</p>',
  "<strong>Death year:</strong> the DAR ancestor record and grave index give 1833; the family record gives November 4, 1832, and Wild gives 1836. <strong>Burial place:</strong> the DAR grave index gives an &ldquo;Old Burying Ground&rdquo; at Lexington, which has not been confirmed. Note: Pending further work.")
_dar_sec("henry-tufts-1716", '<p>The DAR lists him as ' + _DARL("A216175") + ': patriotic service, New Hampshire, for signing the Association Test at Lee in 1776. It cites Stackpole and Thompson, <em>History of the Town of Durham, New Hampshire</em>, vol. 1, pp. 125 and 127. The record gives his birth as September 24, 1716, at Medford.</p>',
  "<strong>Death:</strong> the DAR gives about 1782 at Lee; the family record gives 1780 (" + TKV(31, "8-4") + "). Note: Pending further work.")
_dar_sec("james-tufts-82-3", '<p>The DAR lists him as ' + _DARL("A116797") + ': corporal, also private, Massachusetts; born May 24, 1755, and died November 10, 1810, at Medford. Those dates match the family record exactly (' + TKV(150, "82-3") + ').</p>',
  "<strong>Service:</strong> the DAR accepts service as corporal and private, but the record seen gives no company or source, and no muster roll naming him has been found here. Note: Pending further work.")
_JP = _up_get("james-tufts-82-3")
if _JP:
    _JP["service"] = '<p>The DAR credits him with Revolutionary service as a corporal, also as a private (' + _DARL("A116797") + '). The family record states no service.</p>'
    _JP["unverified"] = "<strong>Service:</strong> the DAR&rsquo;s summary gives no company or regiment, and no muster roll naming him has yet been found. Note: Pending further work."
    RW_SERVICE["james-tufts-82-3"] = "pistol"
_dar_sec("jonathan-tufts-36-8", '<p>The DAR lists him as ' + _DARL("A116806") + ', private, Massachusetts, born February 25, 1739, and died September 26, 1784, at Medford. Its grave index places him in Medford&rsquo;s old (Salem Street) burying ground. It gives his service as private in Capt. Isaac Hall&rsquo;s company, Col. Thomas Gardner&rsquo;s regiment, on April 19, 1775, with service at Dorchester Heights in March 1776. The Sarah Bradlee Fulton Chapter marked his grave in May 1897 (' + _DARGRS + ').</p>')
_dar_sec("joseph-tufts-1755", '<p>The DAR lists him as ' + _DARL("A116810") + ' (&ldquo;Joseph Tufts Jr.&rdquo;): patriotic service, Massachusetts, &ldquo;loaned money during the Revolution&rdquo;; born February 17, 1755, at Medford.</p>',
  "<strong>Death:</strong> the DAR gives &ldquo;about 1794, probably Danvers.&rdquo; The family record gives March 10, 1840, at Danvers (" + TKV("90&ndash;91", "43-1") + "), and Wild says he was taxed in Medford until 1794, which may be the source of the DAR&rsquo;s date. Note: Pending further work.")
_dar_sec("joseph-tufts-jr-15-2", '<p>The DAR lists him as ' + _DARL("A116807") + ' (&ldquo;Joseph Tufts Sr.&rdquo;): civil and patriotic service, Massachusetts. He lent money for bounties and served as surveyor of highways in 1776, and he was a member of the Committee of Safety and a grand juror in 1778. The DAR cites <em>Massachusetts Soldiers and Sailors</em>, vol. XVI, p. 136, and the Medford town records, vol. 3 (1735&ndash;1781), pp. 214&ndash;215 and 235&ndash;237. Born February 21, 1731, and died December 6, 1778, at Medford.</p>')
_dar_sec("david-tufts-41-7", '<p>The DAR lists him as ' + _DARL("A116788") + ': corporal, also private in Capt. Drew&rsquo;s company, Col. Sproat&rsquo;s regiment, Massachusetts, with a Revolutionary pension; born June 17, 1763, at Medford; died July 6, 1823, at Lynn. Its grave index places him in the Western Burial Ground, Lynn, as corporal in Col. Sproat&rsquo;s 2nd Massachusetts Regiment (' + _DARGRS + ').</p>')
_dar_sec("eliakim-tufts-87-6", '<p>The DAR lists him as ' + _DARL("A116790") + ': private, Massachusetts, &ldquo;from Billerica&rdquo;; born September 14, 1767, at Medford.</p><p>See also his brother ' + PL(_EB, "Ebenezer Tufts (1761&ndash;1830)") + '.</p>',
  "<strong>Dates:</strong> the DAR gives birth on September 14 and death &ldquo;after 1810, probably Groton&rdquo;; the family record gives September 4, 1767, and the Littleton town record his death there on February 19, 1825. Note: Pending further work.")
_dar_sec("francis-tufts-20-1", '<p>The DAR lists him as ' + _DARL("A116791") + ': private, Massachusetts, under Capts. Brackett and Plummer and Col. North, pension S3834; born July 21, 1744, near Boston; died October 2, 1833, in Warren County, Ohio. Its grave index places him in the Mainville Cemetery, Ohio. That agrees with the National Register nomination&rsquo;s statement that he died at Maineville. The index describes him as a lieutenant who enlisted in 1775 in the Lincoln County, Massachusetts (now Maine), militia, and names Sarah Blunt as his first wife (' + _DARGRS + ').</p>')
_dar_sec("francis-tufts-41-4", '<p>The DAR lists him as ' + _DARL("A116795") + ': lieutenant, also sergeant, ensign and adjutant, Massachusetts; born May 9, 1756, at Medford; died August 20, 1823, at Boston. Its grave index places him in the Granary Burying Ground. It sums up his service: private in Capt. Isaac Hall&rsquo;s company; sergeant in Capt. Bancroft&rsquo;s company, Col. Jackson&rsquo;s regiment, at Dorchester and Ticonderoga; then ensign, lieutenant and adjutant in Col. Jackson&rsquo;s 8th Regiment until July 18, 1781. It names his wife as Hannah Greenleaf (' + _DARGRS + ').</p>')
_dar_sec("william-tufts-40-2", '<p>The DAR lists him as ' + _DARL("A116819") + ': private, Massachusetts, in Capt. Stephen Dana&rsquo;s company, Col. McIntosh&rsquo;s regiment, 1778, citing <em>Massachusetts Soldiers and Sailors</em>, vol. XVI, p. 139; born March 27, 1736, and died April 27, 1782, at Medford.</p>')
_dar_sec("william-tuffs-35-8", '<p>The DAR grave index records a William Tufts in the Bonneyville Cemetery, east of Bristol, Elkhart County, Indiana, born September 20, 1740, and died September 19, 1848. It gives his service as enlisting from Mystic in April 1775 for three months in Col. Gill&rsquo;s regiment; enlisting again in May 1776 in Capt. Cornelius Sanford&rsquo;s company; and serving three months in Capt. Samuel Tucker&rsquo;s company, including the Battle of Rhode Island. His pension claim is S.32026. A marker placed by the William Tuffs Chapter stands on the lawn of the Elkhart municipal building, dedicated July 4, 1932 (' + _DARGRS + ').</p>',
  "<strong>Birth year:</strong> the grave index gives 1740; his own affidavit, as reported in the family record, gives 1750 (" + TKV(77, "35-8") + "). <strong>DAR ancestor number:</strong> " + _DARL("A116818") + " (born about 1752 at Mystic; soldier under Capt. Sanford and Col. Gansevoort, and sailor under Col. Arnold; died after 1832 in Geauga County, Ohio) shares the Sanford service. But the DAR marks that record as under correction, so it is not attached to him here. Note: Pending further work.")
_dar_sec("benjamin-tufts", '<p>The family record and the DAR both describe a Benjamin Tufts of Medford, born November 15, 1731, and died there July 14, 1804, a son of Benjamin and Mary (Hutchinson) Tufts. He married first Esther Lynde, in 1760, and second Lydia Francis, in 1779 (' + TKV(53, "19-1") + '). The DAR lists him as ' + _DARL("A116786") + ' (&ldquo;Benjamin Tufts Sr.&rdquo;), with patriotic service, &ldquo;paid account.&rdquo; That fits the 1776 payments toward Medford&rsquo;s soldiers described above. The Sarah Bradlee Fulton Chapter marked a Revolutionary grave for a Benjamin Tufts in the Salem Street burying ground in May 1897 (' + _DARGRS + ').</p>',
  "<strong>Identification:</strong> this profile is built on service records that do not give the soldier&rsquo;s age or parents. The 1731&ndash;1804 Benjamin is the most likely match, but another Benjamin Tufts (1761&ndash;1826) also lived in Medford. Note: Pending further work.")
_nf_rel("benjamin-tufts", _JM, "probable brother John Tufts of Malden (1739&ndash;1799)", "probable brother Benjamin Tufts")
for _s, _w in [("ebenezer-tufts-36-7", "Ebenezer"), ("james-tufts-jr-36-2", "James Jr.")]:
    _dar_sec(_s, f'<p>The Sarah Bradlee Fulton Chapter, DAR, placed a Revolutionary War grave marker for {"an" if _w.startswith("E") else "a"} {_w} Tufts in the Salem Street burying ground, Medford, in May 1897 (' + _DARGRS + ').</p>',
      f"<strong>Which {_w} Tufts</strong> the 1897 marker honors is not stated in the index. Note: Pending further work.")
_GR = _up_get("grimes-tufts-40-8")
if _GR:
    _dar_sec("grimes-tufts-40-8", '<p>The DAR grave index places him in the Western Burying Ground, West Lynn, under a special marble stone for minutemen. It gives his service as sergeant, &ldquo;lieutenant on stone,&rdquo; in Capt. Ezra Newhall&rsquo;s company in 1775, and also as ensign (' + _DARGRS + ').</p>',
      "<strong>Death date:</strong> the DAR grave index gives December 23, 1805, which differs from the year shown at the top of this page. Note: Pending further work.")

# =====================================================================
# 7. Owner photographs at the graves
# =====================================================================
_up_add("peter-tufts-1617", '<section id="gravestone-photo"><h2>His Gravestone at Bell Rock</h2>' + FIG("peter-mary-tufts-gravestone-bell-rock-shannon-tufts.jpg", "hfig-flow mi-inline")
  + '<p>Peter and his wife Mary share one carved slate in Bell Rock Cemetery, Malden. Its inscription reads: &ldquo;Here lyes the body of Peter Tufts aged 83 years died May 13 1700. Also here lyes y<sup>e</sup> body of Mary Tufts his wife aged 75 years died January 1702/3.&rdquo;</p></section>', 'id="gravestone-photo"')

# =====================================================================
# 8. Rev. Thomas Tufts (Harvard 1701): dates, schoolmaster, family
# =====================================================================
_RTp = _up_get("thomas-tufts-hc1701")
if _RTp:
    _RTp.update(dates="31 March 1683 &ndash; 26 December 1733", born="1683", died="1733")
    _RTp["bio"] = _RTp["bio"] + ('<section id="schoolmaster"><h2>Schoolmaster at Haverhill and Charlestown</h2>'
      + '<p>Before his calls to the ministry, Thomas Tufts kept school. In 1702 he took the school at Haverhill, then exposed to Indian raids, for &pound;34 a year, until it was suspended in September 1703 (' + TKV(17, "2-5") + '). Charlestown then engaged him:</p>'
      + Q("January 21 following, this committee &ldquo;made return that they had agreed with Mr. Thomas Tufts to keep sd school for one year to perfect Children in Reading &amp; to Learn them to write &amp; Cipher, and to Teach them Gramer, for &pound;40 per annum, &amp; to begin his work the last day of June.&rdquo;", _HL2(61))
      + '<p>The same writer notes that &ldquo;he was the son of Peter Tufts, Jr., (styled &lsquo;Capt. Peter&rsquo;),&rdquo; that he was born in Medford on March 31, 1683, and that he died on December 26, 1733 (' + _HL2(61) + '). The family record gives the same dates and adds that he died at Medford (' + TKV(16, "2-5") + ').</p></section>')
    _RTp["family"] = _RTp["family"] + ('<p>Sons with profiles on this site: ' + PL("henry-tufts-1716", "Henry Tufts (1716&ndash;1780)") + ', by his first wife, and ' + PL("frederick-tufts-9-7", "Sergt. Frederick Tufts (bapt. 1731)") + ', by his second (' + TKV("16&ndash;17") + ').</p>')
    _RTp["unverified"] = "<strong>The Charlestown school:</strong> <em>Historic Leaves</em> dates the agreement to January 1703/4, and the family record dates his Charlestown engagement to 1706. <strong>How long he preached at Malden</strong> before the Court suspended its order is not given in the passages quoted. Note: Pending further work."
    SP["thomas-tufts-hc1701"] = ("<ul><li><strong>Mary Lynde</strong> (b. September 3, 1680, at Charlestown; d. September 3, 1718, at Medford), his cousin, daughter of Thomas Lynde Jr. and Mary (Anderson) Lynde; married 1709 at Charlestown. Children: Mary, Thomas, Peter, and Henry.</li>"
      + "<li><strong>Emma Phipps</strong> (b. October 4, 1694, at Charlestown; buried February 14, 1737/8, at Boston), daughter of Samuel Phipps, register of deeds, and Katherine (Brackenbury) Phipps; married January 29, 1718/19, at Charlestown. Children: Katherine, Samuel, Simon, Solomon, Nancy, David, and Frederick (" + TKV("16&ndash;17", "2-5") + ").</li></ul>")
_nf_rel("thomas-tufts-hc1701", "henry-tufts-1716", "son Henry Tufts (1716&ndash;1780)", "father Rev. Thomas Tufts (Harvard 1701)")
_nf_rel("thomas-tufts-hc1701", "frederick-tufts-9-7", "son Sergt. Frederick Tufts", "father Rev. Thomas Tufts (Harvard 1701)")

# =====================================================================
# 9. Dr. Simon Tufts's house; Whittemore in 1864; Simon Tufts the merchant
# =====================================================================
_SIMHOUSE = ('<section id="house-photograph"><h2>The House in an Early Photograph</h2>' + _SIMHOUSE_PAIR
  + '<p>An original photograph of the house at High and Forest Streets has come down in the family. It shows the same view later printed in the <em>Medford Historical Register</em>, and it must date from before the house was pulled down in 1867. See <a href="{P}places.html#homesteads">Places: Homesteads</a>.</p></section>')
for _s in ("simon-tufts-11-1", "turell-tufts"):
    _up_add(_s, _SIMHOUSE, 'id="house-photograph"')
_up_add("simon-tufts-11-1", '<section id="whittemore-1864"><h2>Samuel Whittemore, as Told in 1864</h2><p>Samuel Abbot Smith&rsquo;s address at West Cambridge in 1864 gives an early account of the doctor&rsquo;s best-known case. Whittemore, eighty years old, was shot in the head, beaten, bayoneted and left for dead on April 19, 1775:</p>'
  + Q("our people, finding that there was some life left in him, carried him to Cooper&rsquo;s tavern, where the surgeon, Dr. Tufts of Medford, said that it was useless to dress his wounds, for he could not live. He dressed the wounds however, and the old hero lived eighteen years after this, dying in 1793 at the age of 98.", _WC("pp. 43&ndash;44"))
  + '<p>Smith does not give the doctor&rsquo;s first name; Dr. Simon Tufts was then Medford&rsquo;s physician.</p></section>', 'id="whittemore-1864"')
_up_add("simon-tufts-29-1", '<section id="store-advertisement"><h2>&ldquo;Choice Jamaica Spirits &hellip; but no Tea&rdquo;</h2>' + FIG("clip-spy-simon-tufts-store-ad.jpg", "hfig-flow mi-inline")
  + '<p>A Simon Tufts kept a store in Boston beside Henry Prentiss&rsquo;s, near Faneuil Hall, and advertised in <em>The Massachusetts Spy</em>:</p>'
  + '<p class="transcription"><em>Transcription:</em> To be SOLD, by SIMON TUFTS, At the Store adjoining Mr. Henry Prentiss, near Faneuil-Hall, CHOICE Jamaica Spirits, West-India and New-England Rum, Loaf and Brown Sugars, some cheap of an ordinary Quality, Raisins in fine Order, Lisbon and Malaga Wines per Quarter Cask, Frontineac ditto, in Cases; Flask Oil, Pepper, Spices, Green Coffee, Chocolate, &amp;c. but no Tea. Cash for Flax-Seed, and No-seed, or the refuse Seed remaining after the cleansing of Flax Seed, for the Purpose of making Linseed Oil.</p>'
  + '<p>&ldquo;But no Tea&rdquo; was the merchants&rsquo; pledge of the non-importation years. It is worth noting because this Simon Tufts was later charged with selling tea.</p>'
  + UNV("<strong>Issue and identity:</strong> the clipping&rsquo;s issue date is not printed on the cropped image. The same wording appears in the issue of October 6, 1774. Whether the advertiser is this Simon Tufts, rather than another of the name, is not confirmed. Note: Pending further work.")
  + '</section>', 'id="store-advertisement"')

# =====================================================================
# 10. Peter Tufts the surveyor: the 1797 road survey reproduced
# =====================================================================
_PS = _up_get("peter-tufts-1774")
if _PS:
    _PS["bio"] = _PS["bio"].replace(" The sheet has been sold and is not reproduced here.", " The sheet has since been sold; the dealer&rsquo;s photographs are shown below.")
    if 'id="road-survey-1797"' not in _PS["bio"]:
        _PS["bio"] += ('<section id="road-survey-1797"><h2>The Road from Concord to Cambridge, 1797</h2>' + FIG("peter-tufts-jr-road-survey-1797-sheet.jpg", "hfig-flow mi-inline") + FIG("peter-tufts-jr-road-survey-1797-compass.jpg", "hfig-flow mi-inline")
          + '<p>The survey follows the road the British marched on April 19, 1775, from Concord meeting house through Lexington and Menotomy to Cambridge and the West Boston Bridge, with distances marked each mile. Beneath it is &ldquo;The Old Road taken from a old Plan Drawn by Mr Osburn,&rdquo; by way of Waltham (<a href="' + _BRM + '">Boston Rare Maps, BRM3348</a>). A later plan of the same road by Peter Tufts, dated December 4, 1801, is in the Lincoln Town Archives (<a href="https://lincolntownarchives.omeka.net/items/show/52">Lincoln Town Archives</a>).</p></section>')

# =====================================================================
# 11. Places page: house pictures in the Homesteads section
# =====================================================================
_PL_INS = {
 "<h3>Peter and Oliver Tufts House, Somerville (78 Sycamore Street)</h3>": FIG("oliver-tufts-house-sycamore-street-postcard.jpg", "hfig-flow mi-inline")
   + '<p>Oliver Tufts (1801&ndash;1883), John&rsquo;s son, was born and died in the house; see ' + PL(_OT, "his profile") + '. An unofficial history of the house dates it to 1714&ndash;1719 (' + _SANF + ').</p>'
   + UNV("The 1714&ndash;1719 building date comes from an unofficial modern history, not from a deed. Note: Pending further work."),
 "<h3>Timothy Tufts house, Elm Street, Somerville</h3>": FIG("timothy-tufts-house-elm-street-1904-postcard.jpg", "hfig-flow mi-inline"),
 "<h3>The Drs. Simon Tufts house, Medford Square</h3>": _SIMHOUSE_PAIR,
 "<h3>Peter Tufts House, Medford (350 Riverside Avenue)</h3>": FIG("peter-tufts-house-cradock-insurance-card.jpg", "hfig-flow mi-inline"),
 "<h3>Peter Tufts of Winter Hill homestead</h3>": FIG("anne-adams-tufts-doorstone-tablet-shannon-tufts.jpg", "hfig-flow mi-inline"),
 "<h3>Peter Tufts the immigrant, Malden</h3>": FIG("peter-mary-tufts-gravestone-bell-rock-shannon-tufts.jpg", "hfig-flow mi-inline"),
}
_page_up1119 = page
def page(path, title, kicker, h1, sub, body, *a, **k):
    if path == "places.html":
        for _h, _f in _PL_INS.items():
            if _h in body and _f not in body:
                body = body.replace(_h, _h + _f, 1)
    return _page_up1119(path, title, kicker, h1, sub, body, *a, **k)
print("nas_uploads_1119: profiles", len(PROFILES))
_EXTRA_up1119 = EXTRA
def EXTRA(path):
    out = _EXTRA_up1119(path)
    if path == "places.html":
        for _h, _f in _PL_INS.items():
            if _h in out and _f not in out:
                out = out.replace(_h, _h + _f, 1)
    return out
