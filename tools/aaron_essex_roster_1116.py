# 2026-11-16 (owner-approved job): Aaron Tufts and the privateer Essex; Essex page; five roster profiles
# (Peter of Winter Hill, Henry Sr., Henry Jr., William killed 1777, Joseph Jr. b. 1755).
# Sources: Wild, Medford in the Revolution (1903), pp. 50, 53, 62; MSS vol. XVI, pp. 135, 137; Tufts Kinsmen Vol. I
# (pages as given in the owner's research table); Papers of John Adams vols. 11-12; William Russell's Mill Prison diary (BPL).
_KV = lambda pg: f'<em>Tufts Kinsmen</em>, Vol. I, p. {pg}'
_WILDIA = '<a href="https://archive.org/details/medfordinrevolut00wild">Internet Archive</a>'
_WD = lambda pg: f'{WILD}, p. {pg}. {_WILDIA}'
_MS = lambda pg: f'{MSS}, p. {pg}. <a href="https://archive.org/details/massachusettssol16mass">Internet Archive</a>'
_PJA11 = '&ldquo;From Job Field and Others, 8 September 1781,&rdquo; editorial note 1, <em>Papers of John Adams</em>, vol. 11. <a href="https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-06-11-02-0356">Massachusetts Historical Society</a>'
_PJA12 = '&ldquo;Thomas Vinton to John Adams, 20 December 1781,&rdquo; <em>Papers of John Adams</em>, vol. 12. <a href="https://founders.archives.gov/documents/Adams/06-12-02-0101">Founders Online</a>'
_TD = '&ldquo;American Privateer ship &lsquo;Essex&rsquo; (1780),&rdquo; <a href="https://threedecks.org/index.php?display_type=show_ship&amp;id=12912">threedecks.org</a> (a secondary database)'
_KIN = '&ldquo;The American prisoners at Kinsale,&rdquo; <em>Journal of the Cork Historical and Archaeological Society</em> (1989). <a href="https://corkhist.ie/wp-content/uploads/jfiles/1989/b1989-004.pdf">PDF</a>'
_RUSSIA = '<a href="https://archive.org/details/diariesofcruisew00russ">Internet Archive</a>'
_RUSS = 'William Russell, <em>Diaries of cruise with privateer from Boston, capture, ordeals in Old Mill Prison at Plymouth, England, attempted escapes, and release</em> (manuscript), Boston Public Library. ' + _RUSSIA
_ESX = '<a href="{P}essex-privateer.html">the privateer <em>Essex</em> and Mill Prison</a>'

IMAGES.update({
 "mill-prison-diary-russell-1781-07-08.jpg": ("Mill Prison diary, 8&ndash;9 July 1781",
   "A page from the diary kept inside Mill Prison, Plymouth, by the American prisoner William Russell. The entries for 8 and 9 July 1781 fall in the same month the crew of the Salem privateer <em>Essex</em> was committed to the prison.",
   "William Russell (manuscript, Boston Public Library); scan by Internet Archive Book Images", "No known copyright restrictions",
   "https://commons.wikimedia.org/wiki/File:Diaries_of_cruise_with_privateer_from_Boston,_capture,_ordeals_in_Old_Mill_Prison_at_Plymouth,_England,_attempted_escapes,_and_release_(manuscript)_(1779)_(14595694290).jpg"),
 "mill-prison-diary-russell-1781-10-01.jpg": ("Mill Prison diary, 1&ndash;2 October 1781",
   "Russell&rsquo;s entries for 1 and 2 October 1781 record a death in the prison hospital and an attempted escape in a coffin, two weeks after the date Wild gives for Aaron Tufts&rsquo;s death there.",
   "William Russell (manuscript, Boston Public Library); scan by Internet Archive Book Images", "No known copyright restrictions",
   "https://commons.wikimedia.org/wiki/File:Diaries_of_cruise_with_privateer_from_Boston,_capture,_ordeals_in_Old_Mill_Prison_at_Plymouth,_England,_attempted_escapes,_and_release_(manuscript)_(1779)_(14779305051).jpg"),
 "hms-roebuck-forcing-hudson-1776.jpg": ("HMS <em>Roebuck</em> with <em>Phoenix</em> and <em>Tartar</em>, Hudson River, 1776",
   "Comparable example only: British warships of the period forcing a passage of the Hudson River, October 1776, after Dominic Serres. No picture of the Salem privateer <em>Essex</em> has been found. <em>Roebuck</em> is shown because some accounts name her as the <em>Essex</em>&rsquo;s captor; the sources cited on this site name the London privateer <em>Queen Charlotte</em>.",
   "Thomas Mitchell, after Dominic Serres", "Public domain",
   "https://commons.wikimedia.org/wiki/File:Forcing_a_Passage_of_the_Hudson.jpg"),
})

_D1 = ('<blockquote class="transcription"><strong>Sunday 8th July 1781.</strong> Showers; 75th Regim<sup>t</sup> Mounted Guard. we had 2 Centinals in the Prison all Night and a Lamp burning, this Morn<sup>g</sup> M<sup>r</sup> Isaac Baren [?], &amp; Isaac Hilton released from the Black-hole. We here that Arnold has had a Battle, and lost 500 of his troops &amp; himself taken and was immediately Executed. nothing more remarkable.<br>'
       '<strong>Monday 9th July 1781.</strong> Cloudy Morn<sup>g</sup>. 50th Reg<sup>t</sup> Mounted Guard, they came from Bucklin [?] Down 7 Miles. This afternoon 11 Americans Committed to Prison Part of y<sup>e</sup> Luzarne&rsquo;s Crew. &hellip;</blockquote>'
       '<p class="cite">Transcription from the page shown, ' + _RUSS + '. Bracketed queries mark uncertain readings. The rumour about Benedict Arnold was false.</p>')
_D2 = ('<blockquote class="transcription"><strong>Monday 1st Octob<sup>r</sup> 1781.</strong> Cloudy 50 Regim<sup>t</sup> Mounted Guard Last Night Died in y<sup>e</sup> Hospital John Tillow [?], alias Callis, belong<sup>g</sup> to North Carolina. This Morn<sup>g</sup> Inglis Thomas, left y<sup>e</sup> Hospital and came into our Ward, After being y<sup>e</sup> Nurse 19 Months. Noth<sup>g</sup> Remarkable.<br>'
       '<strong>Tuesday 2<sup>d</sup> Octob<sup>r</sup> 1781.</strong> Fair Weather, 75th Regim<sup>t</sup> Mounted Guard. they came from y<sup>e</sup> Baracks at Dawn. &mdash; This Morn<sup>g</sup> As the Dead Man was to be Caried out for burial M<sup>r</sup> Alexand<sup>r</sup> Tindall intended to remove him &amp; go out in the Coffin, but had not time to Effect it, otherwise he would have made his Escape.</blockquote>'
       '<p class="cite">Transcription from the page shown, ' + _RUSS + '. Bracketed queries mark uncertain readings.</p>')

# ---------- TASK 1: Aaron ----------
_AARON_ADD = ('<section id="essex-story" class="story-brief"><h3>Sailor, Prisoner of War: The Navy and <em>Essex</em> Record</h3>'
  + '<p>The family record adds a second chapter to Aaron&rsquo;s service. <em>Tufts Kinsmen</em> (Vol. I, p. 177, no. 93-4) records that Aaron Tufts was born on 18 December 1761 in Medford, a son of ' + PL("william-tufts-40-2", "William Tufts Jr.") + ' and Susanna (Dix) Tufts, and a member of Tufts Family 93, with a sister Eleanor (93-3) and a brother William (93-5). He never married.</p>'
  + Q("AARON TUFTS, sailor in USN, POW b. 18, Dec. 1761 in Medford, {Middlesex} Mass. [MMCC 1:76 &amp; 2:80] d. 1781 in Plymouth, {Devonshire} England [GAZ 9/18/1781] single. AARON, during the American Revolution, enlisted in the new U. S. Navy for 3 years, return dated Feb. 1778, and enlisted again for 8 months in 1780, at 19, a member of the crew of the ship Essex that was captured by the British. He died in Old Mill Prison in England while a prisoner of war", _KV(177) + ", no. 93-4 (the book cites MMCC 1:76 and 2:80, and GAZ 9/18/1781)")
  + '<p>Helen Tilden Wild, writing in 1903, had already connected the young Medford soldier with that death abroad:</p>'
  + Q("Tufts, Aaron. Enlisted for 3 yrs., return dated Feb., 1778; enlisted for 8 mos., 1780; age 19. Son of William and Susanna; born Dec. 18, 1761. Probably Aaron, who died in Old Mill Prison, England, Sept. 18, 1781.", _WD(50), ["wild-medford-in-revolution-p50.jpg"])
  + FIG("mill-prison-diary-russell-1781-07-08.jpg", "hfig-flow")
  + '<p>The <em>Essex</em> was a Salem privateer of twenty guns commanded by Capt. John Cathcart. She sailed in April 1781 and was taken at sea on 10 June 1781 by the London privateer <em>Queen Charlotte</em>; her crew were committed to Mill Prison at Plymouth in July (' + _PJA11 + '; ' + _PJA12 + '). If Wild&rsquo;s date is right, Aaron died there on 18 September 1781, aged nineteen. The full story of the ship and the prison is on ' + _ESX + '.</p>'
  + UNV("<strong>Army or Navy?</strong> <em>Massachusetts Soldiers and Sailors</em> (vol. XVI, p. 131, quoted above) records an Aaron Tufts of Medford in the Continental Army: Capt. Bancroft&rsquo;s company, Col. Jackson&rsquo;s regiment, for three years from 1777, then a six-months man from July 4 to Dec. 12, 1780. <em>Tufts Kinsmen</em> (Vol. I, p. 177) reads the 1778 three-year return and the 1780 eight-month enlistment as service in the new U.S. Navy, and Wild (p. 50) gives the same enlistments without naming either service. The Army discharge of December 1780 would still allow him to sail on the <em>Essex</em> in April 1781, but no crew list naming him has been seen. <strong>Year aboard:</strong> the family record places him on the <em>Essex</em> in 1780; the voyage on which she was captured began in April 1781. <strong>Captor:</strong> some accounts name HMS <em>Roebuck</em> (1780); the Adams Papers and a prisoner&rsquo;s own letter name the privateer <em>Queen Charlotte</em> (10 June 1781). <strong>Date of death:</strong> 18 September 1781 is Wild&rsquo;s, offered as &ldquo;probably&rdquo;; the family record gives 1781 and cites a gazette of 9/18/1781. Note: Pending further work.")
  + '</section>')
for _p in PROFILES:
    if _p["slug"] == "aaron-tufts" and "essex-story" not in _p["bio"]:
        _p["bio"] = _p["bio"] + _AARON_ADD
        _p["service"] = _p["service"] + '<p>Later service at sea: enlisted for three years (return dated February 1778) and again for eight months in 1780, at age 19; one of the crew of the Salem privateer <em>Essex</em>, captured in 1781; died a prisoner of war in Old Mill Prison, Plymouth, England, in 1781 (' + _KV(177) + ', no. 93-4; ' + _WD(50) + '). See ' + _ESX + '.</p>'
        _p["family"] = _p["family"] + '<p>Parents: ' + PL("william-tufts-40-2", "William Tufts Jr. (1736&ndash;1782)") + ' and Susanna (Dix) Tufts. Grandfather: ' + PL("william-tufts-13-6", "Lieut. William Tufts (1713&ndash;1783)") + '. Tufts Family 93; siblings named in <em>Tufts Kinsmen</em> are Eleanor (93-3) and William (93-5), who do not yet have pages here. Brothers ' + PL("uriah-tufts-1768", "Uriah Tufts (1768&ndash;1837)") + ' and ' + PL("nathan-tufts-jr", "Nathan Tufts Jr.") + ' are listed on this site among William Jr.&rsquo;s sons. Single; no children (' + _KV(177) + ').</p>'
        _p["dates"] = "18 Dec. 1761 &ndash; 1781"; _p["born"] = "1761"; _p["died"] = "1781"
SP["aaron-tufts"] = "<p>None. <em>Tufts Kinsmen</em>, Vol. I, p. 177 (no. 93-4), records him as single.</p>"
_addrel("aaron-tufts", [("william-tufts-40-2", "father William Tufts Jr. (1736&ndash;1782)"), ("william-tufts-13-6", "grandfather Lieut. William Tufts"), ("uriah-tufts-1768", "brother Uriah Tufts (1768&ndash;1837)"), ("nathan-tufts-jr", "brother Nathan Tufts Jr.")])
_addrel("william-tufts-40-2", [("aaron-tufts", "son Aaron Tufts (1761&ndash;1781), died in Mill Prison")])
_addrel("william-tufts-13-6", [("aaron-tufts", "grandson Aaron Tufts (1761&ndash;1781)")])
_addrel("uriah-tufts-1768", [("aaron-tufts", "brother Aaron Tufts (1761&ndash;1781)")])
_addrel("nathan-tufts-jr", [("aaron-tufts", "brother Aaron Tufts (1761&ndash;1781)")])

# ---------- TASK 3: Essex page ----------
ESSEX = ('<section id="about"><p>Aaron Tufts of Medford, a soldier at nineteen, went to sea in the last years of the war and did not come home. This page gathers what the records say about the Salem privateer <em>Essex</em>, her capture in 1781, and Mill Prison at Plymouth, England, where her crew were held.</p>'
  + TA('Crew member and prisoner of war: ' + PL("aaron-tufts", "Aaron Tufts (1761&ndash;1781)") + ', son of ' + PL("william-tufts-40-2", "William Tufts Jr.") + ' of Medford.', _KV(177) + ', no. 93-4')
  + '</section>{DIV}'
  + '<section id="ship"><h2>The Ship</h2>'
  + '<p>The <em>Essex</em> was a privately owned, ship-rigged vessel sailing out of Salem under a privateer&rsquo;s commission, commanded by Capt. John Cathcart. A ship database records her as twenty guns and about 200 tons, acquired in 1780, with 150 men in April 1781 (' + _TD + '). Where and when she was built is not recorded in the sources seen.</p>'
  + FIG("hms-roebuck-forcing-hudson-1776.jpg", "hfig-flow")
  + UNV("<strong>Built 1779?</strong> A construction date of 1779 has been reported, but no builder&rsquo;s or registry record has been seen; the database above gives only the year acquired, 1780. Note: Pending further work.")
  + '</section>{DIV}'
  + '<section id="capture"><h2>Cruise and Capture, 1781</h2>'
  + '<p>Twelve of the crew were young men from Braintree and Milton, neighbours of John Adams. In their first letter to him from prison they wrote that they had left home on 22 April 1781. The editors of the Adams Papers summarise:</p>'
  + Q("All had been captured in June on board the Salem privateer Essex, Capt. John Cathcart, and committed to Mill Prison in July.", _PJA11)
  + '<p>One of them, Thomas Vinton, named the captor in his own hand:</p>'
  + Q("I was taken the 10th of June Last by the Queen Charlotte Priveteer Belonging to London and was Striped of all my Cloaths And Left Nothing only what I had on.", _PJA12)
  + '<p>An Irish study of American prisoners at Kinsale describes an engagement far west of the Fastnet light between the <em>Queen Charlotte</em> and four American privateers, after which the <em>Queen Charlotte</em> brought the <em>Essex</em> and her crew into Kinsale (' + _KIN + '). It places the action in May 1781, a month earlier than Vinton&rsquo;s date.</p>'
  + UNV("<strong>Which captor?</strong> Some accounts say the <em>Essex</em> was captured by HMS <em>Roebuck</em> in 1780. The sources cited here (the Adams Papers, Vinton&rsquo;s letter, the Kinsale study and the ship database) all name the London privateer <em>Queen Charlotte</em> and the year 1781. No record of a capture by <em>Roebuck</em> has been seen. <strong>Date:</strong> 10 June 1781 (Vinton; the database) against May 1781 (the Kinsale study).")
  + '</section>{DIV}'
  + '<section id="mill-prison"><h2>Old Mill Prison, Plymouth</h2>'
  + '<p>Mill Prison stood at Plymouth in Devon and held American seamen taken at sea throughout the war. Prisoners there depended on guards, the prison hospital and whatever money friends could send. The Braintree men wrote to John Adams in Paris for help; the editors count over twenty letters exchanged over the next twelve months, and Job Field, one of the signers, returned home in 1782 (' + _PJA11 + ').</p>'
  + '<p>William Russell, an American prisoner, kept a daily diary inside the prison. Two of its pages from 1781 are shown below with transcriptions.</p>'
  + FIG("mill-prison-diary-russell-1781-07-08.jpg", "hfig-flow") + _D1
  + FIG("mill-prison-diary-russell-1781-10-01.jpg", "hfig-flow") + _D2
  + '</section>{DIV}'
  + '<section id="aaron"><h2>Aaron Tufts&rsquo;s Fate</h2>'
  + '<p>' + PL("aaron-tufts", "Aaron Tufts") + ' was born in Medford on 18 December 1761. He served in the Continental Army from 1777 and again with Medford&rsquo;s six-months men in 1780 (' + _MS(131) + '). The family record then places him among the crew of the <em>Essex</em>:</p>'
  + Q("died in Old Mill Prison in England while a prisoner of war", _KV(177) + ", no. 93-4")
  + Q("Probably Aaron, who died in Old Mill Prison, England, Sept. 18, 1781.", _WD(50), ["wild-medford-in-revolution-p50.jpg"])
  + '<p>He was nineteen. No grave or burial record for him in England has been found.</p>'
  + UNV("Aaron&rsquo;s name has not been seen on a crew list of the <em>Essex</em> or on a Mill Prison register; his place on the ship rests on <em>Tufts Kinsmen</em>, Vol. I, p. 177. Wild (p. 50) says only &ldquo;probably.&rdquo; Note: Pending further work.")
  + '</section>')
page("essex-privateer.html", "The Privateer Essex and Mill Prison | Tufts Lineage &amp; Legacy", "Places &middot; At Sea and Abroad", "The Privateer <em>Essex</em> and Mill Prison", "Salem, 1781, and Plymouth, England: the last voyage of Aaron Tufts", ESSEX)

# ---------- TASK 4: roster profiles ----------
def _np(slug, name, dates, town, born, died, era, line, bio, service, family, unv):
    PROFILES.append(dict(slug=slug, name=name, dates=dates, town=town, born=born, died=died, era=era, line=line, bio=bio, service=service, family=family, unverified=unv))
    NEWUNCHK.add(slug)

# (a) Peter Tufts of Winter Hill
_WHS = "peter-tufts-winter-hill"
_kids = [(s, l) for s, l in REL.get("anne-adams-tufts", []) if l.startswith(("son ", "daughter "))]
_np(_WHS, "Peter Tufts of Winter Hill (1728&ndash;1791)", "24 April 1728 &ndash; 4 March 1791", "Charlestown (Winter Hill, now Somerville), Mass.", "1728", "1791", "Colonial",
  "Second son of Peter Tufts of Milk Row; farmer of Winter Hill; husband of Anne Adams",
  '<p>Peter Tufts, called &ldquo;of Winter Hill&rdquo; and in Jones &ldquo;of Charlestown,&rdquo; was born on 24 April 1728, the second son of ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + ', &ldquo;Peter of Milk Row,&rdquo; and Lydia Bucknam. Booth writes that he &ldquo;was established on a farm on Winter hill&rdquo; (<em>Historic Leaves</em>, vol. 1, no. 1, pp. 21&ndash;22).</p>'
  + Q("This Peter the third is called &ldquo;of Charlestown,&rdquo; and was born April 24, 1728. He married Anne Adams of Quincy, a relative of President John Adams.", JONES + ", p. 129", ["jones-under-colonial-roofs-p129.jpg"])
  + '<p>On the night the war began, the alarm came to his door:</p>'
  + Q("At the outbreak of the Revolution, Peter Tufts lived at the top of Winter Hill in a little old house, which stood until a few years ago. Here he was soundly sleeping when Paul Revere came thundering up to the door, calling on the people to rouse and arm themselves, for the Regulars were coming.", JONES + ", p. 129", ["jones-under-colonial-roofs-p129.jpg"])
  + FIG("anne-adams-tufts-marker-hmdb.jpg", "hfig-flow")
  + '<p>April 19, 1775 was also his twenty-fifth wedding anniversary. His wife, ' + PL("anne-adams-tufts", "Anne Adams Tufts") + ', nursed the wounded after Bunker Hill; the marker above stands on the door-stone of her home. Wyman records his death:</p>'
  + Q("PETER 37. Son of Peter 36; m. ANN ADAMS [18] April 19, 1750, who d. Feb. 7, 1813, &aelig;. 84, g. s. &hellip; d. March 4, 1791, &aelig;. 63, g. s.", _WY(965), ["wyman-v2-p965.jpg"])
  + '<p>The earlier account of this family is on <a href="{P}generations/colonial.html#peter-1728">The Colonial Era: Peter Tufts of Winter Hill</a>, and the farm on <a href="{P}places.html#winter-hill">Places: Winter Hill</a>.</p>',
  '<p>The family list of Revolutionary service names him &ldquo;Medford Minute Man &ndash; Winter Hill.&rdquo; The printed source that places him in the story of April 19, 1775 is Jones (p. 129), quoted above. The Medford roll of Capt. Isaac Hall&rsquo;s company (' + _MS("137&ndash;138") + ') names &ldquo;Peter, Jr., Medford&rdquo;; this site assigns that entry to his son ' + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + ', whom Wild identifies as the minuteman.</p>',
  '<p>Father: ' + PL("peter-tufts-1697", "Peter Tufts (1697&ndash;1776)") + ', housewright, of Milk Row. Mother: Lydia Bucknam (d. Oct. 31, 1776). Brothers: Nathan (b. 1724) and ' + PL("timothy-tufts", "Timothy Tufts") + ' (' + _WY(964) + '). Wife: ' + PL("anne-adams-tufts", "Anne Adams") + ' (married April 19, 1750). Children on this site: ' + ", ".join(PL(s, l.split(" ", 1)[1]) for s, l in _kids) + '. <em>Tufts Kinsmen</em> (Vol. I, p. 50) lists twelve children: Peter, Peter, John, Anna, Elizabeth, Joseph, Lydia, Asa, Thomas, Lucy, Rebecca and Sarah.</p>',
  "<strong>Service record:</strong> no muster roll naming this Peter (b. 1728) has been matched; the MSS &ldquo;Peter, Jr.&rdquo; entry is placed with his son. The Revolutionary War icon follows the site&rsquo;s rule for this family. <strong>Birth date:</strong> 24 April 1728 (NEHGR; Jones; Wyman) against April 19, 1729 in an Adams genealogy (see Anne&rsquo;s page). <strong>Anne&rsquo;s death:</strong> Feb. 7, 1813 (Wyman) or Feb. 17, 1813 (Jones). WikiTree places the Revere story with his father; the printed sources place it with this Peter. Note: Pending further work.")
SP[_WHS] = '<ul><li>' + PL("anne-adams-tufts", "Anne (Adams) Tufts") + ' (1729&ndash;1813). Married April 19, 1750; she died Feb. 7, 1813, aged 84 (' + _WY(965) + '); Jones gives February 17, 1813 (p. 129).</li></ul>'
REL[_WHS] = [("peter-tufts-1697", "father Peter Tufts (1697&ndash;1776)"), ("anne-adams-tufts", "wife Anne Adams Tufts"), ("timothy-tufts", "brother Timothy Tufts")] + _kids
for _s, _l in [("peter-tufts-1697", "son Peter Tufts of Winter Hill"), ("anne-adams-tufts", "husband Peter Tufts of Winter Hill"), ("timothy-tufts", "brother Peter Tufts of Winter Hill")] + [(s, "father Peter Tufts of Winter Hill") for s, _ in _kids]:
    _addrel(_s, [(_WHS, _l)])

# (b) Henry Tufts Sr. and (c) Henry Tufts Jr.
_HS, _HJ = "henry-tufts-1716", "henry-tufts-1748"
_HCONF = ("<strong>Possible conflation:</strong> this site&rsquo;s earlier page " + PL("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)") + " carries the family number 25-1 and the date &ldquo;abt. 1735.&rdquo; In <em>Tufts Kinsmen</em> as summarised here, 25-1 is Henry Jr., born 24 June 1748, the memoirist, while the Boston tailoring apprenticeship and the move to Newmarket belong to his father, Henry Sr. (8-4), born 1716. The two men appear to be blended on that page. Both are kept separate here and the older page is left as it stands. ")
_np(_HS, "Henry Tufts Sr. (1716&ndash;1780)", "24 Sept. 1716 &ndash; 1780", "Medford, Mass.; Newmarket and Lee, N.H.", "1716", "1780", "The Revolution",
  "Medford-born tailor who settled at Lee, N.H.; father of Henry Tufts the memoirist",
  '<p>Henry Tufts was born in Medford on 24 September 1716, a son of Thomas Tufts and Mary (Lynde) Tufts. The family record says he was briefly apprenticed in physic to his uncle, ' + PL("simon-tufts-1700", "Dr. Simon Tufts") + ', before turning to tailoring in Boston. He moved to New Hampshire, married Mary Wedgwood at Newmarket in 1742, and later farmed at Lee, where he died in 1780 (' + _KV(104) + ', no. 8-4).</p>'
  + Q("HENRY TUFTS, tailor b. 24, Sep. 1716 in Medford, {Middlesex} Mass. [MVR2 148] d. 1780 in Lee, {Strafford} N. H. m 1742 in Newmarket, {Rockingham} N. H. to MARY WEDGWOOD dau of John and Elizabeth (Mather) Wedgwood b. 1722 in Newmarket, {Rockingham} N. H. d. 1782 in Lee, {Strafford} N. H. had 1) Henry, 2) Jonathan, 3) Thomas, 4) Eliphalet, 5) Molly, 6) John", _KV(104) + ", no. 8-4")
  + '<p>His eldest son was ' + PL(_HJ, "Henry Tufts Jr. (1748&ndash;1831)") + ', whose memoir of 1807 made the family name notorious in New England.</p>',
  '<p>Patriotic service: signed the Association Test at Lee, New Hampshire, in 1776, at about fifty-nine (' + _KV(104) + ', no. 8-4). Henry Jr.&rsquo;s entry adds that father and son signed together (' + _KV("62&ndash;63") + ').</p>',
  '<p>Parents: Thomas Tufts and Mary (Lynde) Tufts. Uncle: ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + ' (per the family record). Wife: Mary Wedgwood. Children (Tufts Family 25): ' + PL(_HJ, "Henry") + ', Jonathan, ' + PL("thomas-tufts-25-3", "Thomas") + ', Eliphalet, Molly and John.</p>',
  _HCONF + "<strong>Uncle Simon:</strong> the family record calls Dr. Simon Tufts his uncle; this has not been checked against Medford records. <strong>Page:</strong> the 8-4 entry is cited as printed p. 104 in the research table used; the page has not been seen. <strong>Thomas:</strong> the link to Thomas Tufts of Lee (25-3, 1757&ndash;1834) follows the family numbering. Note: Pending further work.")
SP[_HS] = "<ul><li><strong>Mary (Wedgwood) Tufts</strong>, daughter of John and Elizabeth (Mather) Wedgwood; born 1722 at Newmarket, N.H.; married 1742 at Newmarket; died 1782 at Lee, N.H. (" + _KV(104) + ", no. 8-4).</li></ul>"

_np(_HJ, "Henry Tufts Jr. (1748&ndash;1831)", "24 June 1748 &ndash; 31 Jan. 1831", "Newmarket and Lee, N.H.; Limerick, Me.", "1748", "1831", "The Revolution",
  "Soldier, wanderer and &ldquo;Indian doctor&rdquo;; author of the 1807 memoir",
  '<p>Henry Tufts Jr. was born at Newmarket, New Hampshire, on 24 June 1748, the eldest son of ' + PL(_HS, "Henry Tufts Sr.") + ' and Mary (Wedgwood) Tufts. <em>Tufts Kinsmen</em> calls him, without softening, a &ldquo;vagabond, deserting soldier AR, Indian doctor.&rdquo; In 1770 he married Lydia Bickford at Durham, and they made a home beyond Newmarket Plains toward Lee Hook. He died at Limerick, Maine, on 31 January 1831 (' + _KV("62&ndash;63") + ', no. 25-1).</p>'
  + FIG("henry-tufts-narrative-1807.jpg", "hfig-flow")
  + '<p>His life of crime, imprisonment, escape and doctoring among the Saint Francis Indians is told in his own memoir and summarised on ' + PL("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)") + '.</p>',
  Q("During the Revolutionary War he signed the Association Test of Loyalty, along with his father, and in 1775 enlisted in the Company of Captain Clark for two months detailed to repair for the vicinity of Portsmouth, N. H. He enlisted again for two months with Captain Dembo and was stationed on Winter Hill, Charlestown [Somerville] during the siege of Boston. His third enlistment with Captain True was at Salisbury, Mass. Mar. 26, 1781 when they marched to Andover, Mass. and then to Castee and thence to West Point, N.Y. It is said he served as far from home as Virginia.", _KV("62&ndash;63") + ", no. 25-1")
  + '<p>The Massachusetts record confirms the third enlistment:</p>'
  + Q("Tufts, Henry. Return of men raised in Essex Co. for Continental service, agreeable to resolve of Dec. 2, 1780; engaged for town of Salisbury; engaged March 26, 1781; term, 3 years.", _MS(135), ["mss-v16-p135.jpg"]),
  '<p>Parents: ' + PL(_HS, "Henry Tufts Sr. (1716&ndash;1780)") + ' and Mary (Wedgwood) Tufts. Brothers named in his letters: ' + PL("thomas-tufts-25-3", "Thomas") + ' and Eliphalet. Wife: Lydia Bickford. Children (Tufts Family 70): Simeon, Thomas, Deborah, Hannah, Nancy A. and Catherine (' + _KV("62&ndash;63") + ').</p>',
  _HCONF + "<strong>Birth year:</strong> 1748 (family record) against &ldquo;abt. 1735&rdquo; on the older page. <strong>Captain &ldquo;Dembo&rdquo;</strong> and &ldquo;Castee&rdquo; (probably the Castle, Boston Harbor) are given as printed in the family record. The New Hampshire enlistments have not been checked against New Hampshire rolls. Note: Pending further work.")
SP[_HJ] = "<ul><li><strong>Lydia (Bickford) Tufts</strong>, of Bloody Point, Kittery, daughter of Joseph and Margery Bickford; born 1741 at Newington, N.H. (baptized May 9, 1742); married 1770 at Durham, N.H.; died August 1834 at Limerick, Me. (" + _KV("62&ndash;63") + ", no. 25-1).</li></ul>"
REL[_HS] = [(_HJ, "son Henry Tufts Jr. (1748&ndash;1831)"), ("thomas-tufts-25-3", "son Thomas Tufts of Lee (family no. 25-3)"), ("simon-tufts-1700", "uncle Dr. Simon Tufts (per the family record)"), ("henry-tufts-25-1", "see also Henry Tufts (of Lee, N.H.), the older page")]
REL[_HJ] = [(_HS, "father Henry Tufts Sr. (1716&ndash;1780)"), ("thomas-tufts-25-3", "brother Thomas Tufts of Lee"), ("henry-tufts-25-1", "same family number (25-1): the older page")]
_addrel("henry-tufts-25-1", [(_HJ, "Henry Tufts Jr. (1748&ndash;1831), same family number 25-1"), (_HS, "Henry Tufts Sr. (1716&ndash;1780)")])
_addrel("thomas-tufts-25-3", [(_HS, "father Henry Tufts Sr. (family no. 8-4)"), (_HJ, "brother Henry Tufts Jr.")])
_addrel("simon-tufts-1700", [(_HS, "nephew Henry Tufts Sr. (per the family record)")])

# (d) William Tufts, killed 1777
_WK = "william-tufts-1777"
_np(_WK, "William Tufts (d. 1777)", "c. 1755 or 1762 &ndash; 1777", "Medford, Mass.", "", "1777", "The Revolution",
  "Son of William and Catherine (Tufts) Tufts; killed in service, 1777",
  '<p>Among the many Medford Williams, one did not survive the war. Helen Tilden Wild lists him with the town&rsquo;s soldiers:</p>'
  + Q("TUFTS, WILLIAM. Served at lines at Boston, 1776; in Col. Wesson's Regt., 1777. Son of William and Catherine (Tufts); born 1762; killed 1777.", WILD + ", p. 53", ["wild-medford-in-revolution-p53.jpg"])
  + '<p>His father was William Tufts Jr. (1727&ndash;1782), who as a youth of eighteen had been first into the Island Battery at Louisbourg in 1745 and who loaned money for Medford&rsquo;s bounties in July 1776 (' + _WD("62&ndash;63") + '). The family list of Revolutionary service remembers the son as a soldier killed at Bennington in 1777.</p>'
  + '<p>His record is among the entries on <a href="{P}profiles/william-tufts.html">William Tufts (several men)</a>, which keeps the Massachusetts entries for every William separate.</p>',
  '<p>Wild (p. 53): service at the lines at Boston in 1776 and in Col. Wesson&rsquo;s regiment in 1777; killed 1777. <em>Massachusetts Soldiers and Sailors</em> (vol. XVI, p. 139) has a William Tufts of Bedford mustered in Capt. Pettengill&rsquo;s company, Col. Wesson&rsquo;s regiment, April 13, 1777; whether that is this man is not established.</p>',
  '<p>Father: William Tufts Jr. (1727&ndash;1782), son of John and Sarah Tufts; mother: Catherine Tufts, who married second a Wyman and third a Richardson (' + _WD("62&ndash;63") + '). Neither parent has a page here yet. Single so far as known.</p>',
  "<strong>Birth year:</strong> Wild gives 1762; the family list gives about 1755. A boy born in 1762 would have been fourteen at the Boston lines in 1776. <strong>Bennington:</strong> the place of death comes from the family list and a family genealogy blog; Wild says only &ldquo;killed 1777,&rdquo; and no record of his death at Bennington has been seen. Col. Wesson&rsquo;s regiment served with the northern army in 1777, but it is not recorded at Bennington itself (16 August 1777). <strong>Siblings</strong> named in the blog (Zachariah, Ebenezer, Eliakim) are not confirmed here. Note: Pending further work.")
SP[_WK] = "<p>None recorded. He died young, in 1777.</p>"
REL[_WK] = [("william-tufts", "William Tufts (several men): all Massachusetts entries for the name")]
_addrel("william-tufts", [(_WK, "William Tufts (d. 1777), son of William and Catherine")])

# (e) Joseph Tufts Jr. (b. 1755)
_JJ = "joseph-tufts-1755"
_np(_JJ, "Joseph Tufts Jr. (b. 1755)", "17 Feb. 1755 &ndash; [death not found]", "Medford, Mass.", "1755", "", "The Revolution",
  "Son of Capt. Joseph and Hannah (Cutter) Tufts; loaned money for Medford&rsquo;s 1776 bounties",
  '<p>Joseph Tufts Jr. was born on 17 February 1755, the son of ' + PL("joseph-tufts-jr-15-2", "Capt. Joseph Tufts") + ' and Hannah (Cutter) Tufts of Medford. At twenty-one he helped pay the bounties that sent Medford men to Canada in the summer of 1776:</p>'
  + Q("Tufts, Joseph, Jr. Loaned money for bounty, July, 1776. Born Feb. 17, 1755; son of Joseph and Hannah; taxed in Medford, 1775 to 1794.", _WD(62), ["wild-medford-in-revolution-p62.jpg"])
  + Q("Tufts, Joseph, Jr. Account of money paid by persons to hire men to go to Canada [year not given], examined and allowed by a committee at Medford Oct. 8, 1776.", _MS(137), ["mss-v16-p137.jpg"])
  + '<p>His father, on the same page of Wild, served on Medford&rsquo;s committees of correspondence and safety and died in December 1778. Joseph Jr. was taxed in Medford until 1794.</p>',
  '<p>Patriotic service: loaned money for the Medford bounty of July 1776 (Wild, p. 62); account allowed by the Medford committee, Oct. 8, 1776 (MSS, vol. XVI, p. 137).</p>',
  '<p>Father: ' + PL("joseph-tufts-jr-15-2", "Capt. Joseph Tufts Jr. (1730/1&ndash;1778)") + '. Mother: Hannah (Cutter) Tufts. The family record names his siblings as Samuel 3rd, Ammi Ruhamah, Walter, Cotton, Hannah and ' + PL("andrew-tufts-43-3", "Andrew Tufts") + ' (' + _KV(91) + ', no. 43-3, as summarised in the family research table).</p>',
  "<strong>Possibly the same man as</strong> " + PL("joseph-tufts-43-1", "Joseph Tufts (of Danvers)") + ", family no. 43-1, the first number in his parents&rsquo; Family 43, who is also recorded as helping pay the bounties of 1776. The two pages are kept apart until a record links them. <strong>Death, marriage and later residence</strong> are not yet found. Note: Pending further work.")
SP[_JJ] = "<p>Not found in the sources checked (Wild, p. 62; MSS vol. XVI, p. 137). Note: Pending further work.</p>"
REL[_JJ] = [("joseph-tufts-jr-15-2", "father Capt. Joseph Tufts"), ("andrew-tufts-43-3", "brother Andrew Tufts"), ("joseph-tufts-43-1", "possibly the same man: Joseph Tufts (of Danvers)")]
_addrel("joseph-tufts-jr-15-2", [(_JJ, "son Joseph Tufts Jr. (b. 1755)")])
_addrel("andrew-tufts-43-3", [(_JJ, "brother Joseph Tufts Jr. (b. 1755)")])
_addrel("joseph-tufts-43-1", [(_JJ, "possibly the same man: Joseph Tufts Jr. (b. 1755)")])

# RW icons for the new profiles (musket = extensive; pistol = limited service or support)
# RW icon entries are in data/rw_service.json

# ---------- links from existing pages (insert/append only) ----------
_EXTRA_AER = EXTRA
def EXTRA(path):
    out = _EXTRA_AER(path)
    if path == "places.html":
        out = '{DIV}<section id="essex-mill-prison"><h2>At Sea and Abroad: The Privateer <em>Essex</em> and Mill Prison</h2><p>Aaron Tufts of Medford died a prisoner of war in Old Mill Prison, Plymouth, England, in 1781, after the capture of the Salem privateer <em>Essex</em>. See <a href="{P}essex-privateer.html">The Privateer Essex and Mill Prison</a>.</p></section>' + out
    if path == "collections.html":
        out += '{DIV}<section id="mill-prison-diary"><h2>A Mill Prison Diary, 1781</h2><p>Pages from William Russell&rsquo;s diary kept inside Mill Prison, where Aaron Tufts died, are shown with transcriptions on <a href="{P}essex-privateer.html#mill-prison">The Privateer Essex and Mill Prison</a>.</p></section>'
    if path == "profiles/william-tufts.html":
        out += '{DIV}<section id="william-1777"><h2>Profile: William Tufts (d. 1777)</h2><p>Wild&rsquo;s William, son of William and Catherine (Tufts), killed in 1777, now has his own page: ' + PL(_WK, "William Tufts (d. 1777)") + '.</p></section>'
    if path == "profiles/henry-tufts-25-1.html":
        out += '{DIV}<section id="henry-sr-jr"><h2>Henry Tufts Sr. and Jr.</h2><p>See also ' + PL(_HS, "Henry Tufts Sr. (1716&ndash;1780)") + ' and ' + PL(_HJ, "Henry Tufts Jr. (1748&ndash;1831)") + ', drafted from the family record, which gives family number 25-1 to Henry Jr., born 1748.</p></section>'
    if path == "profiles/joseph-tufts-43-1.html":
        out += '{DIV}<section id="joseph-1755"><h2>Joseph Tufts Jr. (b. 1755)</h2><p>Wild records a Joseph Tufts Jr., born Feb. 17, 1755, son of Joseph and Hannah, who loaned bounty money in July 1776 (p. 62). He may be this man; see ' + PL(_JJ, "Joseph Tufts Jr. (b. 1755)") + '.</p></section>'
    if path == "profiles/anne-adams-tufts.html":
        out += '{DIV}<section id="husband-profile"><h2>Her Husband</h2><p>Full profile: ' + PL(_WHS, "Peter Tufts of Winter Hill (1728&ndash;1791)") + '.</p></section>'
    return out
_page_aer = page
def page(path, title, kicker, h1, sub, body, *a, **k):
    if path == "generations/colonial.html" and 'id="peter-1728"' in body and "peter-tufts-winter-hill.html" not in body:
        _i = body.find('id="peter-1728"'); _j = body.find("</h2>", _i)
        if _j > -1:
            body = body[:_j + 5] + '<p class="note">Full profile: <a href="{P}profiles/peter-tufts-winter-hill.html">Peter Tufts of Winter Hill (1728&ndash;1791)</a>.</p>' + body[_j + 5:]
    return _page_aer(path, title, kicker, h1, sub, body, *a, **k)

exec(open("tools/simon3_mhr_1117.py").read())
