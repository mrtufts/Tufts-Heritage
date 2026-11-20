# Nov 19, 2026: findings from the later group of public-domain town histories, county histories,
# town records, registers and directories. Printed page numbers checked against the page images.
def _IAP(i, n): return f'<a href="https://archive.org/details/{i}/page/n{n - 1}/mode/1up">Internet Archive</a>'
MVY = lambda pg, n: f'Charles Edward Banks, <em>The History of Martha&rsquo;s Vineyard, Dukes County, Massachusetts</em>, vol. 2, <em>Town Annals</em> (1911), {pg}. {_IAP("historyofmarthas00bank", n)}'
PRB = f'<em>Probate Index, Norfolk County, Massachusetts, 1793&ndash;1900</em>, vol. 2 (1910), p. 1090. {_IAP("probateindexnorf02mass", 466)}'
CHM = lambda pg, n: f'Wilson Waters, <em>History of Chelmsford, Massachusetts</em> (1917), {pg}. {_IAP("historyofchelmsf00inwate", n)}'
NOR = lambda pg, n: f'Louis A. Cook, ed., <em>History of Norfolk County, Massachusetts, 1622&ndash;1918</em>, vol. 1 (1918), {pg}. {_IAP("historyofnorfolk01cookl", n)}'
HNG = lambda pg, n: f'<em>History of the Town of Hingham, Massachusetts</em>, vol. 3 (1893), {pg}. {_IAP("historyoftownofh00hing", n)}'
LIT = lambda pg, n: f'<em>Records of Littleton, Massachusetts</em> (1900), {pg}. {_IAP("recordsoflittlet00litt_0", n)}'
R39 = lambda pg, n: f'<em>The Massachusetts Register</em> for 1839, {pg}. {_IAP("massachusettsreg1839bost", n)}'
R44 = lambda pg, n: f'<em>The Massachusetts Register and United States Calendar</em> for 1844, {pg}. {_IAP("massachusettsreg1844unse", n)}'
R55 = lambda pg, n: f'<em>The Massachusetts Register</em> for 1855, {pg}. {_IAP("massachusettsreg1855bost", n)}'
R67 = lambda pg, n: f'<em>The Massachusetts Register</em> for 1867, {pg}. {_IAP("massachusettsreg1867bost", n)}'
R74 = lambda pg, n: f'<em>The Massachusetts Register and Business Directory</em> (1874), {pg}. {_IAP("massachusettsreg1874bost", n)}'
R78 = lambda pg, n: f'<em>The Massachusetts Register and Business Directory</em> (1878), {pg}. {_IAP("massachusettsreg1878bost", n)}'
B16 = lambda vol, pg, i, n: f'<em>The Boston Directory</em> for 1916, vol. {vol}, {pg}. {_IAP(i, n)}'
HMP = lambda pg, n: f'Alfred M. Copeland, ed., <em>&ldquo;Our County and Its People&rdquo;: A History of Hampden County, Massachusetts</em>, vol. 3 (1902), {pg}. {_IAP("ourcountyitspeop03cope", n)}'
WBR = f'Heman Packard DeForest and Edward Craig Bates, <em>The History of Westborough, Massachusetts</em> (1891), p. 451. {_IAP("historyofwestbor01defo", 553)}'
TKV2 = lambda pg, no="": f'<em>Tufts Kinsmen</em>, Vol.&nbsp;II, p. {pg}' + (f', no. {no}' if no else '')

def _lb_img(f, title, cap, src_label, ia, n):
    IMAGES[f] = (title, cap, src_label, "Public domain", f"https://archive.org/details/{ia}/page/n{n - 1}/mode/1up", "Internet Archive (full page)")
    global CREDITS
    if f not in CREDITS:
        CREDITS = CREDITS.replace("</ul></section>", f'<li><a href="{{P}}assets/images/{f}">{title}</a>. {src_label}. Public domain. <a href="https://archive.org/details/{ia}/page/n{n - 1}/mode/1up">Internet Archive page</a></li></ul></section>', 1)
_lb_img("mv-joshua-tufts-1759-p155-clip.jpg", "Clipping: the ministry of Joshua Tufts at Edgartown, 1759&ndash;1760",
  "Detail of p. 155, Banks, <em>History of Martha&rsquo;s Vineyard</em>, vol. 2 (1911): the town&rsquo;s call to the Rev. Joshua Tufts, December 1759, and the committee of July 9, 1760.",
  "Charles Edward Banks, <em>The History of Martha&rsquo;s Vineyard</em>, vol. 2 (1911)", "historyofmarthas00bank", 165)
_lb_img("mv-joshua-tufts-1760-p156-clip.jpg", "Clipping: the Edgartown church&rsquo;s statement on Mr. Tufts, 1760",
  "Detail of p. 156, Banks, <em>History of Martha&rsquo;s Vineyard</em>, vol. 2 (1911): the church committee&rsquo;s report recommending his dismission.",
  "Charles Edward Banks, <em>The History of Martha&rsquo;s Vineyard</em>, vol. 2 (1911)", "historyofmarthas00bank", 166)
_lb_img("hingham-lincoln-funeral-pallbearers-p10-clip.jpg", "Clipping: the pallbearers at Gen. Benjamin Lincoln&rsquo;s funeral, 1810",
  "Detail of p. 10, <em>History of the Town of Hingham</em>, vol. 3 (1893), genealogy of the Lincoln family.",
  "<em>History of the Town of Hingham, Massachusetts</em>, vol. 3 (1893)", "historyoftownofh00hing", 18)
_lb_img("littleton-sarah-tufts-whitcomb-p503-clip.jpg", "Clipping: Sarah Tufts and Jonathan Whitcomb in the Littleton records",
  "Detail of p. 503, <em>Records of Littleton, Massachusetts</em> (1900), Whitcomb family.",
  "<em>Records of Littleton, Massachusetts</em> (1900)", "recordsoflittlet00litt_0", 513)
_lb_img("norfolk-probate-index-tufts-p1090-clip.jpg", "Clipping: the Tufts entries in the Norfolk County probate index",
  "Detail of p. 1090, <em>Probate Index, Norfolk County, Massachusetts, 1793&ndash;1900</em>, vol. 2 (1910): name, year, town, kind of case, and case number.",
  "<em>Probate Index, Norfolk County, Massachusetts, 1793&ndash;1900</em>, vol. 2 (1910)", "probateindexnorf02mass", 466)
_lb_img("mass-register-1867-arctic-soda-apparatus-james-w-tufts-ad.jpg", "Advertisement: James W. Tufts&rsquo;s &ldquo;Arctic&rdquo; soda apparatus, 1867",
  "Detail of p. 769 (Advertising Department), <em>The Massachusetts Register</em> for 1867: &ldquo;Arctic Soda Apparatus &hellip; James W. Tufts, (Patentee and Manufacturer,) 138 Hanover Street, Boston, Mass.&rdquo;",
  "<em>The Massachusetts Register</em> for 1867", "massachusettsreg1867bost", 773)

def _lb_bio(slug, html, mark):
    for _p in PROFILES:
        if _p["slug"] == slug:
            if mark not in _p["bio"]: _p["bio"] = _p["bio"] + html
            return _p
    return None
def _lb_rel(a, b, la, lb):
    _nf_rel(a, b, la, lb)

# =====================================================================
# Rev. Joshua Tufts (1716-1767), Harvard 1736
# =====================================================================
_JS = "joshua-tufts-hc1736"
_nf_new(_JS, "Rev. Joshua Tufts (1716&ndash;1767)", "4 October 1716 &ndash; 12 March 1767", "Newbury, Mass.; Litchfield, N.H.; Edgartown, Martha&rsquo;s Vineyard; Fort Cumberland and Halifax, Nova Scotia", "1716", "1767", "Colonial",
  "Son of Rev. John Tufts of Newbury; Harvard 1736; minister at Edgartown, 1759&ndash;1760",
  '<p>Joshua Tufts was born at Newbury on October 4, 1716, a son of the ' + PL("john-tufts-hc1708", "Rev. John Tufts") + ' and Sarah (Bradstreet) Tufts. A Hollis scholarship paid most of his way through Harvard College, and he graduated in 1736. He preached at Medford in 1738, declined a call from Arundel (now Kennebunkport), Maine, in 1739, and in 1741 settled as pastor at Litchfield, New Hampshire, where he was ordained on December 9 and dismissed in 1744. From 1756 to 1758 he preached in one of the Narragansett townships of Maine (' + TKV("34", "10-2") + ').</p>'
  + '<section id="edgartown"><h2>Minister at Edgartown, 1759&ndash;1760</h2>'
  + FIG("mv-joshua-tufts-1759-p155-clip.jpg", "hfig-flow mi-inline")
  + '<p>Charles Edward Banks&rsquo;s <em>History of Martha&rsquo;s Vineyard</em> tells how the church and town of Edgartown, having failed to secure Zachariah Mayhew of Chilmark, turned to him at the end of 1759:</p>'
  + Q("Another attempt was made to secure the services of a clergyman, and the Rev. Joshua Tufts, Harvard College 1736, who had been settled as pastor at Litchfield, N. H., and Narragansett Township, No. 2, was invited to assume the vacant pastorate in December, 1759. The town voted to purchase a parsonage, and made the usual provisions for his maintenance.", MVY("p. 155", 165))
  + '<p>The town also provided &ldquo;for the Removal of his family and things here.&rdquo; Within months, Banks writes, &ldquo;he was scarcely warmed in his seat before trouble began,&rdquo; and on July 9, 1760, a committee was appointed to discuss with him &ldquo;his asking and taking a dismission,&rdquo; with a sum of money voted him &ldquo;provided he asks and obtains a dismission&rdquo; (' + MVY("pp. 155&ndash;156", 165) + '). The church&rsquo;s report, which it adopted, recommended his release in careful words:</p>'
  + FIG("mv-joshua-tufts-1760-p156-clip.jpg", "hfig-flow mi-inline")
  + Q("That notwithstanding some reports have been spread to the prejudice of the Rev. Mr. Joshua Tufts&rsquo; character since he came to this place by which the affections of some of the people seem to be so far alienated from him that it has been thought convenient by the sd Mr. Tufts and this Church that he be dismissed from his pastoral and ministerial relation thereto: yet we hereby declare we are in full charity with the sd Mr. Tufts and hope that in some other place he may have an opportunity of improving his ministerial talents and of being more extensively useful in promoting the Kingdom &amp; Interests of our Common Lord.", MVY("p. 156", 166))
  + '<p>&ldquo;The exact nature of the disaffection indicated by his involuntary exit is not known,&rdquo; Banks concludes, &ldquo;but it may have been an echo of the troubles of his predecessor,&rdquo; the Rev. John Newman. A note adds that the town then reconsidered the purchase of a parsonage and put part of the money &ldquo;to pay the towns debts,&rdquo; and that Mr. Tufts &ldquo;was later settled at Cumberland, N. S.&rdquo; (' + MVY("p. 156 and note", 166) + ').</p></section>'
  + '<section id="nova-scotia"><h2>Chaplain at Fort Cumberland, Nova Scotia</h2>'
  + '<p>The family record follows him north. After a short stay at Pownalborough (now Wiscasset), Maine, he went to Nova Scotia, preached at Louisbourg and for several months at Halifax, and in September 1761 settled at Cumberland, where he received land and served as chaplain to the British garrison at Fort Cumberland (the former Fort Beaus&eacute;jour). In a letter of September 25, 1761, to his father-in-law, Capt. William Ellery of Cape Ann, he reported that he was &ldquo;employed as Chaplain in the Garrison, and minister to the inhabitants.&rdquo; His wife and children, left at Edgartown, joined him by 1762. The family later moved to Halifax, where he died on March 12, 1767, and his wife six days later; both were buried at St. Paul&rsquo;s Church on April 1, 1767 (' + TKV("34&ndash;35", "10-2") + ').</p></section>'
  + '<p>See also the <a href="{P}harvard.html">Harvard graduates</a> list.</p>',
  '<p>No military service. From 1761 he was chaplain to the British garrison at Fort Cumberland, Nova Scotia (' + TKV("34&ndash;35") + ').</p>',
  '<p>Father: ' + PL("john-tufts-hc1708", "Rev. John Tufts (Harvard 1708)") + ', minister at Newbury. Mother: Sarah (Bradstreet) Tufts. Fourteen children are listed, among them Capt. John Tufts, master mariner; William Ellery Tufts of Nova Scotia; ' + PL("samuel-tufts-28-11", "Capt. Samuel Tufts (1758&ndash;1819)") + ', master mariner; Joshua Bradstreet Tufts (1760&ndash;1835); and Rowland Cotton Tufts, born about 1766 (' + TKV("34, 66&ndash;68", "10-2; family 28") + ').</p>',
  '<strong>Year of death:</strong> Banks says he &ldquo;died in 1766&rdquo; (p. 156, note); the family record gives March 12, 1767, at Halifax. <strong>The Maine township:</strong> Banks says &ldquo;Narragansett Township, No. 2&rdquo;; the family record says Narragansett No. 1 (Buxton). <strong>Date of the Edgartown call:</strong> the family record dates it July 10, 1759, but Banks gives that date for the call to Zachariah Mayhew and places the invitation to Mr. Tufts in December 1759. Note: Pending further work.',
  "<ul><li><strong>Abigail Ellery</strong> (b. January 25, 1725/6, at Gloucester; d. March 18, 1767, at Halifax), daughter of Capt. William and Dorcas (Elwell) Ellery of Gloucester. The marriage is recorded at Gloucester under September 13, 1741 (" + TKV(34) + ").</li></ul>",
  [("john-tufts-hc1708", "father Rev. John Tufts (Harvard 1708)", "son Rev. Joshua Tufts (1716&ndash;1767)"),
   ("samuel-tufts-28-11", "son Capt. Samuel Tufts (1758&ndash;1819)", "father Rev. Joshua Tufts (1716&ndash;1767)")])
_jt = _nf_get("john-tufts-hc1708")
if _jt and _JS not in _jt["family"]:
    _jt["family"] += '<p>Son: ' + PL(_JS, "Rev. Joshua Tufts (1716&ndash;1767)") + ', born at Newbury, Harvard 1736, minister at Litchfield, N.H., and Edgartown, and chaplain at Fort Cumberland, Nova Scotia. His mother was Sarah (Bradstreet) Tufts (' + TKV(34, "10-2") + ').</p>'
_st = _nf_get("samuel-tufts-28-11")
if _st and "Parents are not named in this entry." in _st["family"]:
    _st["family"] = _st["family"].replace("Parents are not named in this entry.", 'Parents: ' + PL(_JS, "Rev. Joshua Tufts (1716&ndash;1767)") + ' and Abigail (Ellery) Tufts (' + TKV(66, "family 28") + ').')

# =====================================================================
# Dr. Cotton Tufts: Weymouth affairs, Lincoln's funeral, probate
# =====================================================================
_lb_bio("cotton-tufts",
  '{DIV}<section id="weymouth-affairs"><h2>In Weymouth&rsquo;s Public Affairs, 1760&ndash;1775</h2>'
  + '<p>The <em>History of Norfolk County</em> (1918) describes him as &ldquo;a well educated, progressive man&rdquo; who &ldquo;took great interest in local political affairs and general social conditions.&rdquo; On March 10, 1760, the town chose him as its agent to confer with other towns about forming a new county (' + NOR("p. 384", 494) + '). As the quarrel with Parliament deepened, Weymouth turned to him again:</p>'
  + Q("On September 21, 1768, James Humphrey and Dr. Cotton Tufts were appointed agents to meet in Faneuil Hall in Boston the next day, to consult with agents of other towns upon the state of public affairs.", NOR("p. 325", 423))
  + '<p>That meeting was the convention of towns called after Boston&rsquo;s town meeting of September 1768. On March 9, 1775, Weymouth chose a committee of correspondence &ldquo;of which Dr. Cotton Tufts was chairman,&rdquo; to act with the committees of neighboring towns; it first met at Arnold&rsquo;s Tavern at Weymouth Landing. In May 1775, when the town accepted the use of two swivel guns then at Salem, &ldquo;Doctor Tufts agreed to have them brought to Weymouth&rdquo; (' + NOR("p. 325", 423) + ').</p>'
  + UNV("<strong>When he settled in Weymouth.</strong> This page follows the Weymouth Tufts papers in placing the start of his Weymouth practice about 1751. The <em>History of Norfolk County</em> says instead: &ldquo;About 1759 Dr. Cotton Tufts settled in the northern part of the Town of Weymouth&rdquo; (p. 384). Neither date has yet been checked against a contemporary record. Note: Pending further work.")
  + '</section>'
  + '<section id="lincoln-funeral"><h2>Pallbearer for General Lincoln, 1810</h2>'
  + '<p>Gen. Benjamin Lincoln of Hingham, the Revolutionary general who received the British sword at Yorktown, died on May 9, 1810 (' + HNG("p. 9", 17) + '). Among those who bore his pall were two old friends of the Weymouth doctor, John Adams and Richard Cranch:</p>'
  + FIG("hingham-lincoln-funeral-pallbearers-p10-clip.jpg", "hfig-flow mi-inline")
  + Q("His pall was borne by the Hon. John Adams, Hon. R. T. Paine, Hon. Richard Cranch, Hon. Cotton Tufts, his Honor Lieutenant-Governor Cobb and Thomas Melville, Esq.", HNG("p. 10", 18))
  + UNV("The Hingham history writes only &ldquo;Hon. Cotton Tufts.&rdquo; In 1810 the title fits Dr. Cotton Tufts, a former state senator and kinsman of Adams and Cranch, rather than his son Cotton Jr., a merchant; this is an inference. Note: Pending further work.")
  + '</section>'
  + '<section id="probate"><h2>His Estate in the Probate Index</h2>'
  + '<p>The printed index of Norfolk County probate records lists the Tufts estates of Weymouth with their case numbers, the key to the original files at the Norfolk Probate Court. The first entry, a will of 1816, fits Dr. Cotton Tufts, who died in December 1815:</p>'
  + FIG("norfolk-probate-index-tufts-p1090-clip.jpg", "hfig-flow mi-inline")
  + '<p>Transcription (Weymouth entries): Cotton, 1816, Will, no. 18,841. Cotton, 1833, Adm., no. 18,842. Elizabeth, 1858, Will, no. 18,844. Francis, 1866, Will, no. 18,846. Mercy, 1849, Adm., no. 18,848. Mercy, 1858, Adm., no. 18,849. Susan, 1877, Will, no. 18,851 (' + PRB + ').</p>'
  + '<p>The 1833 administration fits his son ' + PL("cotton-tufts-jr", "Cotton Tufts Jr.") + ', the 1849 administration his daughter-in-law ' + PL("mercy-brooks-tufts", "Mercy (Brooks) Tufts") + ', and the 1877 will his granddaughter ' + PL("susannah-tufts-1797", "Susannah (Susan) Tufts") + '. The contents of the files have not been read here.</p>'
  + '</section>', 'id="weymouth-affairs"')

_lb_bio("cotton-tufts-jr",
  '{DIV}<section id="probate-academy"><h2>The Probate Index and the Weymouth and Braintree Academy</h2>'
  + '<p>The Norfolk County probate index lists a Weymouth administration for &ldquo;Cotton&rdquo; Tufts in 1833, case no. 18,842, the year of his death (' + PRB + '; see the <a href="{P}profiles/cotton-tufts.html#probate">clipping on his father&rsquo;s page</a>).</p>'
  + '<p>The <em>History of Norfolk County</em> records that the Weymouth and Braintree Academy, started by citizens of Weymouth Landing late in 1827, &ldquo;was incorporated on February 28, 1828, by Dr. Cotton Tufts, Noah Fifield, Joseph Loud and their associates&rdquo;; Capt. Warren Weston gave the site on the Weymouth and Braintree turnpike (' + NOR("p. 395", 513) + ').</p>'
  + UNV("<strong>Who founded the academy.</strong> Dr. Cotton Tufts died in December 1815, so he cannot have been an incorporator in 1828. The founder was probably his son Cotton Tufts Jr. (1757&ndash;1833), then a leading Weymouth merchant, and the county history&rsquo;s &ldquo;Dr.&rdquo; is probably an error. The act of incorporation has not yet been checked. Note: Pending further work.")
  + '</section>', 'id="probate-academy"')

_lb_bio("mercy-brooks-tufts",
  '{DIV}<section id="probate"><h2>Her Estate in the Probate Index</h2>'
  + '<p>The Norfolk County probate index lists two Weymouth administrations under &ldquo;Mercy&rdquo; Tufts: one in 1849, case no. 18,848, and one in 1858, case no. 18,849 (' + PRB + '; see the <a href="{P}profiles/cotton-tufts.html#probate">clipping</a>). The 1849 entry agrees with her death on May 6, 1849.</p>'
  + UNV("<strong>The 1858 administration</strong> (no. 18,849) may be a later proceeding on her estate or the estate of another Mercy Tufts of Weymouth, possibly her daughter Mercy. The file has not been read. Note: Pending further work.")
  + '</section>', 'id="probate"')

_lb_bio("susannah-tufts-1797",
  '{DIV}<section id="norfolk-records"><h2>&ldquo;Susan&rdquo; in the County Records</h2>'
  + '<p>The county records call her Susan. The <em>History of Norfolk County</em> (1918) credits the library to Dr. Cotton Tufts&rsquo;s grandchildren, &ldquo;Quincy and Susan Tufts&rdquo; (' + NOR("p. 384", 494) + '), and describes its endowment:</p>'
  + Q("The Tufts Library was founded in 1879, when Quincy Tufts and his sister, Susan Tufts, left a fund of some twenty thousand dollars to be applied by the town &ldquo;to instructive lectures, the reading room and the general expenses of a free public library.&rdquo;", NOR("p. 418", 540))
  + '<p>Part of the gift was two buildings at the corner of Washington and Commercial Streets, one of which served as the library and reading room until October 1892, when a new building went up on the site (' + NOR("p. 418", 540) + '). The Norfolk probate index lists her will: &ldquo;Susan,&rdquo; Weymouth, 1877, Will, case no. 18,851 (' + PRB + '; see the <a href="{P}profiles/cotton-tufts.html#probate">clipping</a>).</p>'
  + '<p class="note">Susan, Susanna and Susannah are forms of the same name, and these records refer to her.</p>'
  + '</section>', 'id="norfolk-records"')
_lb_bio("quincy-tufts",
  '{DIV}<section id="norfolk-history"><h2>The Library in the County History</h2>'
  + '<p>The <em>History of Norfolk County</em> (1918) names Quincy Tufts and his sister Susan as founders of the Tufts Library in 1879, leaving &ldquo;a fund of some twenty thousand dollars&rdquo; and two buildings at Washington and Commercial Streets (' + NOR("pp. 384, 418", 540) + '). See ' + PL("susannah-tufts-1797", "Susannah Tufts") + '.</p></section>', 'id="norfolk-history"')

# =====================================================================
# Samuel Tufts Jr., Middlesex Canal incorporator (several men page)
# =====================================================================
_lb_bio("samuel-tufts",
  '{DIV}<section id="middlesex-canal-1793"><h2>An Incorporator of the Middlesex Canal, 1793</h2>'
  + '<p>The Middlesex Canal, which linked the Merrimack River at Chelmsford with the Medford River and Boston, received its charter from the General Court, &ldquo;signed by Governor Hancock on the 22d of June, 1793&rdquo; (' + CHM("p. 503", 601) + '). The act named the first proprietors:</p>'
  + Q("Be it therefore enacted, by the Senate and House of Representatives in General Court assembled, that the said James Sullivan, Oliver Prescott, Jas. Winthrop, Loammi Baldwin, Benjamin Hall, Jonathan Porter, Andrew Hall, Ebenezer Hall, Samuel Tufts, Jr., Aaron Brown, Willis Hall, Samuel Swan, Jr., and Ebenezer Hall, Jr., their associates and successors, are hereby incorporated and shall be a corporation forever, under the name of The Proprietors of the Middlesex Canal", CHM("p. 506", 604))
  + '<p>Several of the names, the Halls, Jonathan Porter and Samuel Swan Jr., belong to Medford families, and the canal crossed the Brooks estate at Medford on its way to the Charlestown mill-pond (' + CHM("p. 506", 604) + ').</p>'
  + UNV("<strong>Which Samuel Tufts Jr.</strong> The act gives no town or dates. He was probably of Medford, like several of his fellow incorporators, but which of the Medford Samuels listed on this page he was has not been established. Note: Pending further work.")
  + '</section>', 'id="middlesex-canal-1793"')

# =====================================================================
# Sarah (Tufts) Whitcomb of Littleton; Mary (Tufts) Edes
# =====================================================================
_SW = "sarah-tufts-whitcomb-1718"
_nf_new(_SW, "Sarah (Tufts) Whitcomb (1718&ndash;1801)", "30 August 1718 &ndash; 20 February 1801", "Malden, Mass.; Littleton, Mass.; died at Shelburne Falls, Mass.", "1718", "1801", "Colonial",
  "Daughter of Peter Tufts; wife of Jonathan Whitcomb of Littleton",
  '<p>Sarah Tufts was born on August 30, 1718. Her first husband, Thomas Backus of Canterbury, Connecticut, whom she married in 1740 at Haddam, Connecticut, died about a year later (' + TKV(28, "7-4") + '). About 1747 she married Jonathan Whitcomb of Littleton, and the Littleton town records preserve the family:</p>'
  + FIG("littleton-sarah-tufts-whitcomb-p503-clip.jpg", "hfig-flow mi-inline")
  + Q("Jonathan m. about 1747 Sarah, b. Aug. 30 1718, dau. Peter Tufts of Charlestown, and 1745 took a deed of the house and 3 acres of land known as the residence of the late Peter Whitcomb. (Jonathan&rsquo;s d. on pp. 152, 365.) Sarah d. at Shelburne Falls at the residence of her dau. Martha.", LIT("p. 503", 513))
  + '<p>Jonathan Whitcomb was a Littleton selectman from 1777 to 1782 and died in 1790 (' + TKV(28) + '). Their children were Sarah, who married Josiah Willis Seaver and lived at Moretown, Vermont; Martha, who married Jonas Rice in 1776 and lived at Shelburne; Jonathan; Peter; Lydia; and Dinah, who married Simeon Fiske of Shelburne in 1784 (' + LIT("p. 504", 514) + ').</p>'
  + '<section id="peter-whitcomb-1775"><h2>Her Son Peter at Bunker Hill</h2>'
  + '<p>Her son Peter Whitcomb, born at Littleton on December 24, 1756 (' + TKV(28) + '), &ldquo;d. June 17 1775, killed at Battle of Bunker Hill&rdquo; (' + LIT("p. 504", 514) + '). The family record adds that he had walked from Littleton to Charlestown that day to visit his Tufts relations and was struck by a stray bullet (' + TKV(51) + ').</p></section>'
  + '<section id="tufts-whitcomb"><h2>The Name Carried On</h2>'
  + '<p>The family kept her maiden name in use. Her grandson Tufts Whitcomb, &ldquo;fourth son of Jonathan Whitcomb and Sarah his Wife,&rdquo; was born November 22, 1795, and died September 29, 1799 (' + LIT("p. 383", 393) + '), and the church record of burials notes &ldquo;Tufts Whitcomb Son of Jonathan Whitcomb &amp; Wife Aged about four years&rdquo; (' + LIT("p. 346", 356) + '). That Jonathan was her son, who married Sarah Baker (' + LIT("p. 504", 514) + ').</p></section>',
  '<p>No service record applies to her. Her son Peter Whitcomb was killed at Bunker Hill on June 17, 1775 (' + LIT("p. 504", 514) + ').</p>',
  '<p>Father: Peter Tufts. The family record identifies him as Peter Tufts Jr. (1678&ndash;1756), son of ' + PL("peter-tufts-1648", "Capt. Peter Tufts (c. 1648&ndash;1721)") + ' and Elizabeth (Lynde) Tufts, who married Deborah Lawrence of Reading in 1708 and later moved to Ashford (now Eastford), Connecticut (' + TKV("16, 28", "2-3; 7-4") + '). Children: Sarah, Martha, Jonathan, Peter (1756&ndash;1775), Lydia and Dinah Whitcomb (' + LIT("p. 504", 514) + ').</p>',
  '<strong>Her father.</strong> The Littleton records call him &ldquo;Peter Tufts of Charlestown&rdquo;; the family record makes him Peter Tufts Jr. (1678&ndash;1756) and gives her birthplace as Malden. The two have not been reconciled from a contemporary record, and her father has no profile here yet. Note: Pending further work.',
  "<ul><li><strong>Thomas Backus</strong> (b. 1713 at Canterbury, Conn.; d. about 1741), son of Timothy and Sarah (Post) Backus; married 1740 at Haddam, Conn. No children (" + TKV(28) + ").</li>"
  + "<li><strong>Jonathan Whitcomb</strong> (1717&ndash;1790), lieutenant and farmer of Littleton, son of Jonathan and Deliverance (Nutting) Whitcomb; married about 1747 (" + LIT("p. 503", 513) + "; " + TKV(28) + ").</li></ul>",
  [("peter-tufts-1648", "granddaughter Sarah (Tufts) Whitcomb (1718&ndash;1801)", "grandfather Capt. Peter Tufts (c. 1648&ndash;1721)")])
_lb_bio("peter-tufts-1617",
  '{DIV}<section id="mary-edes"><h2>His Daughter Mary Edes</h2>'
  + '<p>The <em>Records of Littleton</em> (1900) note under the Edes family: &ldquo;John Edes m. Mary, b. 1658, dau. Peter Tufts&rdquo; (' + LIT("p. 458", 468) + '). This agrees with &ldquo;Mary Eades,&rdquo; one of the daughters named in the immigrant&rsquo;s will.</p></section>', 'id="mary-edes"')

# =====================================================================
# Eliakim Tufts (1767-1825) of Groton and Littleton
# =====================================================================
_EL = "eliakim-tufts-87-6"
_nf_new(_EL, "Eliakim Tufts (1767&ndash;1825)", "4 September 1767 &ndash; 19 February 1825", "Medford; Billerica; Groton; Littleton, Mass.", "1767", "1825", "The Revolution",
  "Son of William and Katherine (Tufts) Tufts; Revolutionary soldier from Billerica; died at Littleton",
  '<p>Eliakim Tufts was born in Medford on September 4, 1767, a son of William and Katherine (Tufts) Tufts. He married Sarah Ross at Billerica on May 8, 1788 (' + TKV(165, "87-6") + '). Their children were born at Groton from the 1790s to about 1804 (' + TKV2("73&ndash;75") + '), and the family later lived at Littleton.</p>'
  + '<section id="littleton"><h2>The Family at Littleton</h2>'
  + '<p>Within four years the Littleton town clerk entered four deaths in the family on a single page:</p>'
  + Q("Eliakim Ross Tufts. Son of Eliakim Tufts. &amp; Sarah his wife Died April 17. 1821. Sarah Tufts, wife of Eliakim Tufts. Died July 1st 1822. Ebenezer Tufts, Son of Said Eliakim Died December 31th 1823 The above said Eliakim Tufts. Died February 19th 1825.", LIT("p. 205", 215))
  + '<p>Between those losses he remarried. The town&rsquo;s intentions of marriage record &ldquo;Mr Eliakim Tufts of Littleton, and Mrs Merriam Raymond of Amhurst State of Newhampshire, July 6 1823&rdquo; (' + LIT("p. 281", 291) + '). She was Miriam (Leonard) Raymond, widow of the Hon. David Raymond; the family record has the marriage at New Durham, New Hampshire, in July 1823, and her death at Amherst, New Hampshire, on December 29, 1838 (' + TKV(165) + '). A few weeks after his death, the intention of &ldquo;Leonard Porter of Carlisle and Daranda Tufts of Littleton, May 1st 1825&rdquo; was entered (' + LIT("p. 282", 292) + '). She was his daughter Dorinda.</p></section>',
  '<p>The family record notes that his name appears on a list of Billerica soldiers who served three years in the Continental Army during the Revolution (' + TKV(165, "87-6") + ', citing a D.A.R. list). No muster roll naming him has yet been seen here.</p>',
  '<p>Parents: William Tufts and Katherine (Tufts) Tufts (' + TKV(163) + '). Children (thirteen are listed): Sarah, Catherine, William, Catherine, Eliakim (bapt. 1797, died young), Mary (b. 1798, m. Benjamin Brown), Lucy (b. 1800, m. Brooks Bowman), Eliakim Ross (1801&ndash;1821), the twins Levi and Achsah (b. 1804), Dorinda, George, and Ebenezer (d. 1823) (' + TKV(165) + '; ' + TKV2("74&ndash;75") + ').</p>',
  '<strong>Revolutionary service</strong> rests on a list cited in the family record; the original roll has not been seen. <strong>His second wife&rsquo;s name</strong> is written &ldquo;Merriam&rdquo; in the Littleton record and Miriam in the family record. Note: Pending further work.',
  "<ul><li><strong>Sarah Ross</strong> (b. January 21, 1765, at Billerica; d. July 1, 1822, at Littleton), daughter of John and Mary (Dunckle) Ross; married May 8, 1788, at Billerica (" + TKV(165) + "; " + LIT("p. 205", 215) + ").</li>"
  + "<li><strong>Miriam (Leonard) Raymond</strong> (b. 1765; d. December 29, 1838, at Amherst, N.H.), widow of the Hon. David Raymond; intention recorded at Littleton, July 6, 1823 (" + LIT("p. 281", 291) + "; " + TKV(165) + ").</li></ul>",
  rw="musket")

# =====================================================================
# James W. Tufts, soda-fountain maker, and Leonard Tufts
# =====================================================================
_JW = "james-w-tufts-1835"; _LT = "leonard-tufts-1870"
_nf_new(_JW, "James W. Tufts (1835&ndash;1902), Soda-Fountain Maker", "11 February 1835 &ndash; 2 February 1902", "Charlestown (now Somerville); Medford; Boston, Mass.; Pinehurst, N.C.", "1835", "1902", "19th Century",
  "Son of Leonard and Hepzibah (Fosdick) Tufts; apothecary and maker of the &ldquo;Arctic&rdquo; soda apparatus",
  '<p>James Walker Tufts was born in Charlestown, in the part that became Somerville, on February 11, 1835, a son of Leonard Tufts, a blacksmith, and Hepzibah (Fosdick) Tufts. He was named for the Rev. James Walker, who had married his parents (' + TKV(237, "130-6") + '; ' + TKV2(157, "300-4") + '). The family record describes him as an apothecary, a soda-fountain manufacturer and silversmith, and the founder of Pinehurst, North Carolina (' + TKV2(157) + ').</p>'
  + '<section id="arctic-soda"><h2>Apothecary and the &ldquo;Arctic&rdquo; Soda Apparatus</h2>'
  + '<p>The state business directories trace a James W. Tufts from the drug counter to the soda-fountain trade. In 1867 he is listed among the apothecaries of Medford (' + R67("p. 115", 125) + '), and in Boston under &ldquo;Soda and Beer Apparatus&rdquo;: &ldquo;Tufts James W. 138 Hanover (see adv. page 769)&rdquo; (' + R67("p. 526", 538) + '). The advertisement, indexed as &ldquo;Arctic soda-apparatus&rdquo; (' + R67("p. 589", 601) + '), promised soda drawn ice-cold &ldquo;without labor&rdquo;:</p>'
  + FIG("mass-register-1867-arctic-soda-apparatus-james-w-tufts-ad.jpg", "hfig-flow mi-inline")
  + Q("Arctic Soda Apparatus. The immense demand for this Apparatus proves it to be entirely successful as a means of increasing the Soda trade, and drawing ICE COLD SODA without labor. James W. Tufts, (Patentee and Manufacturer,) 138 Hanover Street, Boston, Mass.", R67("p. 769", 773))
  + '<p>By 1874 the business had moved to Bowker Street: &ldquo;Tufts James W. 33 Bowker,&rdquo; under &ldquo;Soda, Ale, and Beer Apparatus&rdquo; (' + R74("p. 221", 235) + '), while the Medford apothecary shop appears as &ldquo;Tufts James W. &amp; Co.&rdquo; (' + R74("p. 245", 257) + '). In 1878 he is at &ldquo;33 to 39 Bowker&rdquo; (' + R78("p. 258", 238) + '), and he lent his name to an advertisement for the <em>Boston Journal of Commerce</em>: &ldquo;I have found the &lsquo;Boston Journal of Commerce&rsquo; an excellent medium for the advertisement of my goods,&rdquo; signed &ldquo;James W. Tufts. Soda Water Apparatus Manufacturer, Boston, Mass.&rdquo; (' + R78("p. 837", 795) + ').</p>'
  + '<p>The family record adds that he founded a plated silverware business in Boston in 1875, which made fountain ware and table pieces until 1915, and that he built a Colonial Revival house at 72 Powder House Road, Medford, in the 1890s (' + TKV2(157) + ').</p>'
  + '<p>In 1916 the Boston directory lists &ldquo;Leonard vice pres 282 Congress&rdquo; among the Tufts entries (' + B16(2, "p. 1955", "bostonmassachus1916v2samp", 427) + '). The same directory gives 282&ndash;288 Congress Street as the address of the American Soda Fountain Company (' + B16(1, "p. 188", "bostonmassachuse1916112samp", 190) + '). See ' + PL(_LT, "Leonard Tufts (1870&ndash;1945)") + '.</p>'
  + '<p>His earlier career, as an apothecary in Somerville and Medford, and the later merger of his firm into the American Soda Fountain Company, are described on <a href="{P}businesses.html#james-w-tufts">Businesses: James W. Tufts, apothecary and soda-fountain maker</a>.</p></section>',
  '<p>No military service is recorded for him.</p>',
  '<p>Father: Leonard Tufts (1788&ndash;1851), blacksmith, of Charlestown and Somerville. Mother: Hepzibah (Fosdick) Tufts (1795&ndash;1864) (' + TKV(237, "130-6") + '). Children: Mary Gertrude; ' + PL(_LT, "George Leonard (Leonard) Tufts (1870&ndash;1945)") + '; James Walker (1872&ndash;1875); and Bessie (1875) (' + TKV2("157, 400&ndash;401") + ').</p>',
  '<strong>Identity.</strong> The directories say only &ldquo;James W. Tufts&rdquo;; the match with James Walker Tufts of the family record rests on the name, the Medford apothecary listing and the soda-fountain trade. That he founded Pinehurst is stated in the family record and in the NCpedia account cited on the Businesses page, not in these directories. Note: Pending further work.',
  "<ul><li><strong>Mary Emma Clough</strong> (b. June 1, 1845, at Alton, Ill.; d. December 5, 1922, at Medford), daughter of Samuel Francis and Martha Louisa (Ayer) Clough; married October 30, 1862, at Medford (" + TKV2(157) + ").</li></ul>",
  [(_LT, "son Leonard Tufts (1870&ndash;1945)", "father James W. Tufts (1835&ndash;1902)")])
_nf_new(_LT, "Leonard Tufts (1870&ndash;1945)", "30 June 1870 &ndash; 19 February 1945", "Medford; Boston, Mass.; Pinehurst, N.C.", "1870", "1945", "19th Century",
  "Son of James W. Tufts, the soda-fountain maker; resort operator",
  '<p>George Leonard Tufts, who went by Leonard, was born in Medford on June 30, 1870, a son of ' + PL(_JW, "James W. Tufts") + ' and Mary Emma (Clough) Tufts. The family record calls him a resort operator and records his death at Pinehurst, North Carolina, on February 19, 1945 (' + TKV2("401&ndash;402", "575-2") + ').</p>'
  + '<p>The Boston directory for 1916 lists a Leonard Tufts as vice president at 282 Congress Street, with his home out of town:</p>'
  + Q("Leonard vice pres 282 Congress h at Meredith [N H]", B16(2, "p. 1955, under Tufts", "bostonmassachus1916v2samp", 427))
  + '<p>The same directory lists the American Soda Fountain Company at 282&ndash;288 Congress Street (' + B16(1, "p. 188", "bostonmassachuse1916112samp", 190) + ').</p>',
  '<p>No military service is recorded for him.</p>',
  '<p>Father: ' + PL(_JW, "James W. Tufts (1835&ndash;1902)") + '. Mother: Mary Emma (Clough) Tufts. Children: Richard S., Esther, Albert S., and James W. (' + TKV2(402) + ').</p>',
  '<strong>Identity.</strong> The 1916 directory gives no full name or dates, and does not name the company at 282 Congress Street in his entry; that this vice president is the Leonard Tufts of the family record, and an officer of the American Soda Fountain Company, is inferred from the address. Note: Pending further work.',
  "<ul><li><strong>Gertrude Ware Sise</strong> (b. June 21, 1870, at Boston; d. June 14, 1940, at Pinehurst), daughter of Albert Fleetford and Edith (Ware) Sise of Medford; married June 14, 1895, at Medford (" + TKV2("401&ndash;402") + ").</li></ul>")

# =====================================================================
# Nathan A. Tufts (1799-1873) and the Charlestown institutions
# =====================================================================
_NA = "nathan-adams-tufts-1799"
_nf_new(_NA, "Nathan A. Tufts (1799&ndash;1873)", "16 January 1799 &ndash; 20 November 1873", "Charlestown, Mass.", "1799", "1873", "19th Century",
  "Son of Deacon Amos Tufts; merchant and bank director of Charlestown",
  '<p>Nathan Tufts, known as Nathan Adams Tufts, was born in Charlestown on January 16, 1799, a son of ' + PL("amos-tufts-1762", "Deacon Amos Tufts") + '. The family record describes him as a merchant and bank director. He married Mary Ann Lamson of Charlestown at Keene, New Hampshire, on September 11, 1822, and died in Charlestown on November 20, 1873 (' + TKV(231, "128-7") + ').</p>'
  + '<section id="warren-institution"><h2>President of the Warren Institution for Savings</h2>'
  + '<p>The <em>Massachusetts Register</em> for 1855 lists the officers of the Warren Institution for Savings, Charlestown: &ldquo;Nathan A. Tufts, Pres.&rdquo; (' + R55("p. 151", 161) + '). The Suffolk County history gives his presidency as 1850 to 1855 (' + SUF(412) + '). His brother ' + PL("joseph-f-tufts-1790", "Joseph F. Tufts") + ' was its treasurer from 1851 to 1854, and his nephew ' + PL("george-f-tufts-1825", "George F. Tufts") + ' later held the same office. In the same year the city government of Charlestown included &ldquo;N. A. Tufts&rdquo; on the school committee for Ward 1, and an Amos Tufts on the common council (' + R55("p. 253", 263) + '). See also <a href="{P}businesses.html#banks">Banks and savings institutions</a>.</p></section>',
  '<p>No military service is recorded for him.</p>',
  '<p>Father: ' + PL("amos-tufts-1762", "Deacon Amos Tufts (c. 1762&ndash;1839)") + '. Brothers included ' + PL("joseph-f-tufts-1790", "Joseph F. Tufts") + ', ' + PL("william-tufts-1802", "William Tufts") + ' and ' + PL("edward-tufts-1806", "Edward Tufts") + '. Children: William Lamson (1824), Nathan Adams (1825&ndash;1826), Hannah Lamson (1828&ndash;1906), who married Nathan P. B. Curtiss, and Henry Adams Tufts (1831&ndash;1884), a merchant of New York (' + TKV(231) + '; ' + TKV2("142&ndash;143") + ').</p>',
  '<strong>Identity.</strong> The register and the Suffolk history write &ldquo;Nathan A. Tufts&rdquo; without dates; the match with Amos Tufts&rsquo;s son Nathan Adams Tufts rests on the name, the Charlestown residence and the family record&rsquo;s &ldquo;bank director.&rdquo; Note: Pending further work.',
  "<ul><li><strong>Mary Ann Lamson</strong> (b. December 17, 1801, at Keene, N.H.; d. January 1, 1878, at Boston), daughter of William and Margery (Russell) Lamson of Charlestown; married September 11, 1822, at Keene (" + TKV(231) + ").</li></ul>",
  [("amos-tufts-1762", "father Deacon Amos Tufts", "son Nathan A. Tufts (1799&ndash;1873)"),
   ("joseph-f-tufts-1790", "brother Joseph F. Tufts", "brother Nathan A. Tufts (1799&ndash;1873)"),
   ("william-tufts-1802", "brother William Tufts", "brother Nathan A. Tufts (1799&ndash;1873)"),
   ("edward-tufts-1806", "brother Edward Tufts", "brother Nathan A. Tufts (1799&ndash;1873)"),
   ("george-f-tufts-1825", "nephew George F. Tufts", "uncle Nathan A. Tufts (1799&ndash;1873)")])
_am = _nf_get("amos-tufts-1762")
if _am and _NA not in _am["family"]:
    _am["family"] = _am["family"].replace("Children on this site: ", "Children on this site: " + PL(_NA, "Nathan A. Tufts (1799&ndash;1873)") + ", ", 1)

# =====================================================================
# William Tufts (1802-1862): State House clerk and insurance secretary
# =====================================================================
_lb_bio("william-tufts-1802",
  '{DIV}<section id="state-house"><h2>Chief Clerk at the State House and Insurance Secretary</h2>'
  + '<p>The family record calls William Tufts an insurance broker and notes that he was secretary of the Massachusetts Mutual Insurance Company and lived on Washington Street (' + TKV(232, "128-9") + '). The annual <em>Massachusetts Register</em> shows a William Tufts holding that post for at least sixteen years, and also serving in the office of the Secretary of the Commonwealth:</p>'
  + '<ul><li><strong>1839:</strong> under the Secretary of the Commonwealth, John P. Bigelow, &ldquo;Chief Clerk, William Tufts&rdquo; (' + R39("p. 32", 50) + '); a justice of the peace in Boston (' + R39("p. 44", 62) + '); and &ldquo;Secretary, William Tufts&rdquo; of the Massachusetts Mutual Fire Insurance Company, 17 State Street (' + R39("p. 243", 227) + ').</li>'
  + '<li><strong>1844:</strong> &ldquo;Chief Clerk, Wm. Tufts,&rdquo; under Secretary John G. Palfrey (' + R44("&ldquo;Civil Government of Massachusetts&rdquo;", 48) + '); a Suffolk justice of the peace (' + R44("p. 43", 59) + '); and secretary of the Massachusetts Mutual Fire Insurance Company, now at 31 State Street (' + R44("p. 244", 260) + ').</li>'
  + '<li><strong>1855:</strong> &ldquo;First Clerk Secretary of State&rsquo;s Office. William Tufts, Salary, $1,300&rdquo; (' + R55("p. 10", 20) + '), and secretary of the insurance company at 31 State Street (' + R55("p. 154", 164) + ').</li></ul>'
  + UNV("The family record names this William as the insurance company&rsquo;s secretary but does not mention the State House clerkship. That the chief clerk is the same man rests on the same name appearing in both offices, year after year, in the same register. Note: Pending further work.")
  + '</section>', 'id="state-house"')
SP["william-tufts-1802"] = "<ul><li><strong>Eliza Brooks Kendall</strong> (b. July 9, 1809, at Charlestown; d. August 9, 1899, at Brookline), daughter of Col. Loammi and Nancy Lovering (Roberts) Kendall; married November 14, 1827, at Charlestown. Children: William C., Helen E., and Emma K. (" + TKV(232, "128-9") + ").</li></ul>"

# =====================================================================
# Edward Tufts (1806-1875) and Mrs. Edward Tufts of Chelmsford
# =====================================================================
_lb_bio("edward-tufts-1806",
  '{DIV}<section id="chelmsford"><h2>Lowell and Chelmsford</h2>'
  + '<p>The family record describes Edward Tufts as a clerk and paymaster in Lowell and gives his death at Chelmsford on March 26, 1875 (' + TKV(232, "128-11") + '). Less than a year later, the Central Congregational Church of Chelmsford was organized in his widow&rsquo;s house:</p>'
  + Q("On February 12, at the residence of Mrs. Edward Tufts, the organization was effected and articles of Faith and Covenant adopted.", CHM("p. 714", 838))
  + '<p>The meeting was held in 1876, and &ldquo;Mrs. Tufts&rdquo; is named again among those present (' + CHM("p. 714", 838) + ').</p>'
  + UNV("The church history does not give Mrs. Edward Tufts&rsquo;s first name. That she was Edward&rsquo;s widow, Rebecca, is inferred from his death at Chelmsford the year before. Note: Pending further work.")
  + '</section>', 'id="chelmsford"')
SP["edward-tufts-1806"] = "<ul><li><strong>Rebecca Sprague McClure</strong> (b. May 23, 1807, at Wiscasset, Maine), daughter of John McClure, Esq., and Hannah (Danforth) McClure; married September 20, 1827, at Merrimack, N.H. (" + TKV(232, "128-11") + ").</li></ul>"

# =====================================================================
# Rev. James Tufts of Monson (1812-1901)
# =====================================================================
_JM = "james-tufts-monson-1812"
_nf_new(_JM, "Rev. James Tufts of Monson (1812&ndash;1901)", "3 November 1812 &ndash; 29 March 1901", "Wardsborough, Vt.; Monson, Mass.", "1812", "1901", "19th Century",
  "Son of James and Submit F. (Hayden) Tufts; teacher, principal of Monson Academy",
  '<p>James Browning Tufts, who used only the name James Tufts, was born at Wardsborough, Vermont, on November 3, 1812, a son of James and Submit F. (Hayden) Tufts. A clergyman and teacher, he spent most of his life at Monson, Massachusetts, where he died on March 29, 1901. The family record notes that he was the tutor of the poet Eugene Field (' + TKV2(30, "182-4") + ').</p>'
  + '<section id="monson-academy"><h2>Monson Academy and the Town&rsquo;s Schools</h2>'
  + '<p>In 1855 the <em>Massachusetts Register</em> lists &ldquo;Monson Academy, Monson. Incorporated 1804. James Tufts, A. M., Principal and Teacher of the Classical Department&rdquo; (' + R55("p. 195", 205) + '). The Hampden County history names him among the academy&rsquo;s most prominent teachers, with Richard S. Storrs Jr. and the Rev. Charles Hammond (' + HMP("p. 290", 314) + '), and credits him with a long campaign for the public schools:</p>'
  + Q("Rev. James Tufts took up the work where Mr. Hammond laid it down, and for over forty years he labored untiringly for the improvement of the school system. His last efforts were towards forming a superintendency district.", HMP("p. 287", 311))
  + '<p>He also taught privately. William Trowbridge Forbes of Westborough, born in 1850, &ldquo;completed his preparation for college at the classical school of the Allens at West Newton and at the private school of Rev. James Tufts, of Monson,&rdquo; before entering Amherst College (' + WBR + '). In March 1877 he was one of the townsmen who began the movement for a free public library in Monson (' + HMP("p. 295", 319) + ').</p></section>',
  '<p>No military service is recorded for him.</p>',
  '<p>Parents: James Tufts and Submit F. (Hayden) Tufts of Wardsborough, Vermont. Children: James Frederick (1860, died in infancy) and James Hayden Tufts (1862&ndash;1942), born at Monson, philosopher and educator (' + TKV2("30, 260", "182-4; 407-2") + '). A &ldquo;James H. Tufts, Ph. D., Chicago&rdquo; was a trustee of Monson Academy in 1902 (' + HMP("p. 291", 315) + ').</p>',
  '<strong>The 1902 trustee</strong> James H. Tufts of Chicago is probably his son James Hayden Tufts; the Hampden history does not say so. <strong>His ordination and churches</strong> are not given in the sources seen. Note: Pending further work.',
  "<ul><li><strong>Mary Elizabeth Warren</strong> (b. August 9, 1823, at Wardsborough, Vt.; d. November 1, 1910, at Monson), daughter of Dr. John Parker and Lucy Maynard (Wheelock) Warren; married March 21, 1855, at Brooklyn, N.Y. (" + TKV2(30) + ").</li></ul>")

# =====================================================================
# Businesses page: banks (Nathan A.), Tufts Mill listings, soda apparatus
# =====================================================================
if "BIZ_HTML" in globals():
    _old = "Nathan A. Tufts was its president from 1850 to 1855."
    if _old in BIZ_HTML:
        BIZ_HTML = BIZ_HTML.replace(_old, PL(_NA, "Nathan A. Tufts") + " was its president from 1850 to 1855, and the <em>Massachusetts Register</em> for 1855 still lists &ldquo;Nathan A. Tufts, Pres.&rdquo; (" + R55("p. 151", 161) + ").", 1)
        BIZ_HTML = BIZ_HTML.replace("and who Nathan A. Tufts was, are not stated in the source.", "are not stated in the source. Nathan A. Tufts is identified here as Nathan Adams Tufts (1799&ndash;1873), son of Deacon Amos Tufts, from the family record.", 1)
    def _lb_ins(h, sid, add, mark):
        if mark in h: return h
        j = _nf_sec_end(h, sid)
        if j < 0: return h + "{DIV}" + add
        k = j - len("</section>")
        return h[:k] + add + h[k:]
    BIZ_HTML = _lb_ins(BIZ_HTML, "nathan-tufts-tide-mill",
          '<div id="tufts-mill-listings"><h3>N. Tufts &amp; Son, Tufts Mill, in the 1870s Directories</h3>'
          + '<p>The mill was still working under the family name in the 1870s. The 1874 business directory lists among Boston&rsquo;s flour and grain dealers &ldquo;Tufts N. &amp; Son, 46 Warren av. and rear 553 Main, Charlestown&rdquo; (' + R74("p. 155", 169) + '). In 1878 the firm appears under grist mills: &ldquo;Tufts N. &amp; Son, Tufts Mill, r. 553 Main, Charlestown&rdquo; (' + R78("p. 203", 183) + '), with its Warren Avenue store again under flour and grain (' + R78("p. 198", 178) + ').</p>'
          + UNV("Which Nathan Tufts and which son ran the firm in the 1870s is not stated in the directories. Note: Pending further work.")
          + '</div>', 'id="tufts-mill-listings"')
    BIZ_HTML = _lb_ins(BIZ_HTML, "james-w-tufts",
          '<div id="arctic-directories"><h3>In the State Directories, 1867&ndash;1878</h3>'
          + FIG("mass-register-1867-arctic-soda-apparatus-james-w-tufts-ad.jpg", "hfig-flow mi-inline")
          + '<p>The <em>Massachusetts Register</em> for 1867 lists him among the apothecaries of Medford (' + R67("p. 115", 125) + ') and under &ldquo;Soda and Beer Apparatus&rdquo; in Boston at 138 Hanover Street (' + R67("p. 526", 538) + '), with the advertisement shown here: &ldquo;The immense demand for this Apparatus proves it to be entirely successful as a means of increasing the Soda trade, and drawing ICE COLD SODA without labor&rdquo; (' + R67("p. 769", 773) + '). By 1874 the works were at 33 Bowker Street (' + R74("p. 221", 235) + '), and in 1878 at &ldquo;33 to 39 Bowker&rdquo; (' + R78("p. 258", 238) + '). See ' + PL(_JW, "James W. Tufts (1835&ndash;1902)") + '.</p></div>', 'id="arctic-directories"')
    page("businesses.html", "Businesses | Tufts Lineage &amp; Legacy", "Places", "Businesses", "The trades of the Tufts family, colonial era to the 19th century", BIZ_HTML)
print("late_books_1119: profiles", len(PROFILES))
exec(open("tools/nas_uploads_1119.py").read())
