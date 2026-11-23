# Letters of the Tufts doctors (owner request B, 2026-11-03). Adams Papers list from the MHS digital edition (correspondent facets).
import json as _jl
DL = _jl.load(open("data/tufts_doctors_letters.json"))
MHSV = "https://www.masshist.org/publications/adams-papers/index.php/view/"
FO = lambda i: "https://founders.archives.gov/documents/Adams/" + i[5:]
def LCITE(r): return f'<em>{r["cite"].split(",")[0]}</em>{r["cite"][len(r["cite"].split(",")[0]):]}. <a href="{MHSV}{r["id"]}">MHS digital edition</a> &middot; <a href="{FO(r["id"])}">Founders Online</a>'
AUDIO_ID = "ADMS-04-08-02-0087"
AUDIO_ANCHOR = "letter-1787-11-06"
AUDIO_FILE = "assets/audio/abigail-adams-to-cotton-tufts-1787-11-06.mp3"
AUDIO_DOWNLOAD = "abigail-adams-to-cotton-tufts-1787-11-06.mp3"
_AUDIO_ANCHORED = []

def LETTER_TRANSCRIPT_HTML():
    # Recipient's copy as printed in Adams Family Correspondence, vol. 8, pp. 201-203.
    # Editorial footnote markers and annotations are omitted; print page breaks are omitted.
    return (
        '<details class="letter-transcript">'
        '<summary>Read the letter</summary>'
        '<div class="letter-text">'
        '<p class="letter-dateline">London Nov<sup>br</sup> 6<sup>th</sup> 1787&mdash;</p>'
        '<p class="letter-salute">Dear Sir</p>'
        '<p>Last week Captains Folger &amp; Callihan arrived by whom we received all your Letters &amp; Bills. the Bills were imediatly accepted, &amp; will be paid when due. I feel under great obligations to you my dear sir, for all your kind care, &amp; attention to our affairs. I am glad to find the buisness closed with mr Borland, and at a price which I think must be reasonable judging by what was formerly given for it, for I do not recollect how many acres of Land there are belonging to it. I know there is a wood lot containing 25 acres, &amp; an other Lot of four, besides the Six which were sold to deacon Webb.&mdash; with regard to the repairs painting both without &amp; within I should be glad to have compleated as soon as possible in the Spring, as the Smell is always pernicious to me. the east lower room to be painted what is calld a French Grey and as the furniture is red, a paper conformable, will look best. the Chamber over it will have Green furniture, and may be in the same manner, made uniform by a paper Green &amp; white. the mahogany room, I know not what to say about it, making the two windows into the Garden will dispell much of the Gloom, &amp; if it is not much abused &amp; injured, had it not better remain as it is? can there be a Closset contrived in the Room when the windows are made, I could wish to have one, to make a uniform appearence, must there not be windows in the Chamber above, in the east Room. I think there are two clossets by the side of the Chimney. what would be the expence of taking them away &amp; making arches in the Room of them? Iron Backs to the Chimneys &amp; Brass Locks upon the Doors of the two best rooms &amp; Chambers are all the particular directions I think of at present with regard to the other part of the House I shall leave it wholy to your judgment to make such repairs as you deem necessary and consistant with economy. as to any aditional building we cannot at present afford any. in some future day perhaps we may think of making the House Square by adding a Library, which mr A will really want, but at present, some chamber must be a substitute. The Frame set up by mr T. you do not mention. it is best to let it remain in its present state untill we return. in the painting you will be so good as to employ a person who properly understands the Buisness. I mention this, because I once Sufferd &amp; was obliged to have a room 3 times painted when one would have answerd&mdash;</p>'
        '<p>Mr Adams has written to you respecting our Farm, &amp; mr Pratt. it has become so poor &amp; misirable, that we must take some measures for making it better that we may be able to get our Bread from it. indeed I think I should enjoy better Health, to come Home &amp; make butter &amp; Cheese, raise poultry &amp; look after my Garden, than by the inactive Life I am compelld to lead here. it will require my strickest attention to oconomy to be able to live &amp; compleat the Education of our children, but this does not terify me. I can conform to Whatever is necessary, with regard to the pocket expences of Charles &amp; Tommy&mdash;you know sir, that on the one hand, we would not wish to have them too Spairingly Supplied, nor on the other permit them so much, as to lead them into Idleness &amp; dissapation. if any thing of the kind appears you will check your Hand. Mrs Cranch knows what her son expended, and I do not see why mine Should require more. I shall write to them both, &amp; exort them to prudence in their expences. I would venture Sir one hundred pounds more in the purchase of paper. I am fully of your mind with respect to Land and whatever purchases we may make in future, I could wish it might be better than what we already own&mdash;</p>'
        '<p>it is mr A&rsquo;s intention to retire to Braintree as a private man, nor need any one fear that he will become a competitor with them for offices. he has always dealt too openly &amp; candedly with his Countrymen to be popular, &amp; whatever they may assert with regard to his principals, he says they may be assured that he will never conceal a Sentiment of his Heart, however unpopular it may be, which he considers for the interest of His Countrymen to know &amp; consider, altho he should forfeit by it the highest offices in the united states. he was never yet the partizan of any Country, nor will he ever become a Tool to any party, if fourteen years unremitted attention to the Service of his Country has not convinced them that he is their unshaken Friend, it would be in vain to attempt a conviction at this day. The English Review which you mention &amp; which I see several of the states have carefully reprinted, was written by that Honour to his Country Silas Dean, who lives here as his appearence indicates, in real want &amp; Horrour, and is Said to be a half crown Gazzet writer. I have only room to add that the Form of Government by the late Convention is esteemed here as a sublime work. they add that it is so good that they are perswaided the Americans will not accept it, it may admitt of some amendments but it is certainly a great Federal Structure. I shall write to all my Friends by Folger. my little Boy has got well through the small pox. adieu yours / &amp;c &amp;c</p>'
        '<p class="letter-signed">A A&mdash;</p>'
        '</div>'
        f'<p class="cite">Transcription from <em>Adams Family Correspondence</em>, vol. 8, pp. 201&ndash;203. <a href="{FO(AUDIO_ID)}">Founders Online</a> &middot; <a href="{MHSV}{AUDIO_ID}">MHS digital edition</a></p>'
        '</details>'
    )

def LETTER_AUDIO_HTML(with_id=False):
    id_attr = f' id="{AUDIO_ANCHOR}"' if with_id else ""
    return (
        f'<div class="letter-audio"{id_attr}>'
        f'<p class="letter-audio-label">Listen to a reading of this letter</p>'
        f'<audio controls preload="none">'
        f'<source src="{{P}}{AUDIO_FILE}" type="audio/mpeg">'
        f'</audio>'
        f'<p class="letter-audio-fallback"><a href="{{P}}{AUDIO_FILE}" download="{AUDIO_DOWNLOAD}">Download the reading (MP3)</a></p>'
        + LETTER_TRANSCRIPT_HTML() +
        f'</div>'
    )

def LROW(r, topic=None):
    w = r["who"].replace("Tufts, Cotton", "Dr. Cotton Tufts").replace("Adams, Abigail", "Abigail Adams").replace("Adams, John", "John Adams")
    audio = ""
    id_attr = ""
    if r["id"] == AUDIO_ID:
        if not _AUDIO_ANCHORED:
            _AUDIO_ANCHORED.append(True)
            id_attr = f' id="{AUDIO_ANCHOR}"'
        audio = LETTER_AUDIO_HTML(with_id=False)
    row = f'<tr{id_attr}><td>{r["date"]}</td><td>{w}</td><td>{topic or r["teaser"]}</td><td class="cite">{LCITE(r)}</td></tr>'
    if audio:
        row += f'<tr class="letter-full"><td colspan="4">{audio}</td></tr>'
    return row
TH = '<table class="data"><thead><tr><th>Date</th><th>Correspondents</th><th>Topic</th><th>Citation</th></tr></thead><tbody>'
QL = {"ADMS-04-01-02-0017": "&ldquo;Ye must permit the little Villains call&rsquo;d the small Pox to have their Feast this Spring.&rdquo;",
      "ADMS-04-02-02-0019": "&ldquo;Yesterday People in Boston were openly inoculated for the Small Pox.&rdquo;",
      "ADMS-04-02-02-0037": "&ldquo;The Small Pox prevailing in our Armies and Country has much retarded the raising Recruits.&rdquo;",
      "ADMS-04-02-02-0050": "Thanks Adams for &ldquo;Dr. Rushs Letter on Inoculation.&rdquo;",
      "ADMS-04-08-02-0087": "&ldquo;my little Boy has got well through the small pox.&rdquo;",
      "ADMS-04-09-02-0014": "Thomas Adams carried to Braintree &ldquo;with the Symptoms of the Measles upon him.&rdquo;",
      "ADMS-04-14-02-0046": "&ldquo;some few Instances of bilious Fevers with us, at present scarce any Complaint of Disease.&rdquo;"}
COT = [r for r in DL if r["kind"] in ("by", "to")]
DIS = [r for r in COT if r["disease"]]
def _d(r):
    import datetime
    try: return datetime.datetime.strptime(r["date"], "%B %d, %Y")
    except Exception: return datetime.datetime(1900, 1, 1)
DIS.sort(key=_d); COT.sort(key=_d)
DOCTORS = f'''<section id="doctors-letters"><h2>Letters of the Tufts Doctors</h2>
<p>Three Tufts physicians are easy to confuse. In this section each letter is assigned to one of them by name and dates:</p>
<ul><li><a href="{{P}}profiles/simon-tufts-1700.html">Dr. Simon Tufts the elder (1700&ndash;1747)</a>, Medford&rsquo;s first physician;</li>
<li><a href="{{P}}profiles/simon-tufts-11-1.html">Dr. Simon Tufts the younger (1727&ndash;1786)</a>, his eldest son, of Medford;</li>
<li><a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts (1732&ndash;1815)</a>, the younger son, of Weymouth.</li></ul>
<h3>Dr. Cotton Tufts: letters on smallpox, fevers and other diseases</h3>
<p>The Adams Papers digital edition of the Massachusetts Historical Society lists 188 letters by or to Cotton Tufts: 90 written by him and 98 written to him. These {len(DIS)} touch on disease in the letter text. Topics were read from each letter; a quotation is given where one is short.</p>
{TH}{"".join(LROW(r, r["disease"].capitalize() + ((". " + QL[r["id"]]) if r["id"] in QL else "")) for r in DIS)}</tbody></table>
{UNV("None of the 188 Adams letters is on throat distemper (diphtheria). Cotton Tufts&rsquo;s own medical papers at the Countway Library include &ldquo;a treatise on distemper,&rdquo; and the Countway&rsquo;s exhibit says he &ldquo;introduced a popular treatment for diphtheria early in his career&rdquo; (see the manuscript collections below). Those papers have not been read item by item.")}
<details><summary>All 188 Adams Papers letters by or to Dr. Cotton Tufts</summary>{TH}{"".join(LROW(r) for r in COT)}</tbody></table><p class="cite">Topics in this list are the opening words shown by the MHS digital edition. Founders Online links follow the same document numbers.</p></details>
<h3>Dr. Simon Tufts the younger (1727&ndash;1786): letters with Col. Isaac Royall</h3>
<p>No letter by or to either Dr. Simon appears in the Adams Papers. The surviving references are to the younger Simon&rsquo;s letters with the Loyalist Isaac Royall, for whom he acted as agent:</p>
{TH}
<tr><td>May 1775</td><td>Isaac Royall (Halifax) to Dr. Simon Tufts</td><td>Asks him to become his agent; Brooks says the doctor &ldquo;declined, but afterwards accepted.&rdquo;</td><td class="cite">{BRP(173).replace(BRK9, PU("2001.05.0104", 5))}</td></tr>
<tr><td>March 12, 1776</td><td>Isaac Royall (Halifax) to Dr. Simon Tufts</td><td>Directions to sell enslaved people of the Royall household; Brooks quotes the letter.</td><td class="cite">Brooks, p. 173. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
<tr><td>August 1777</td><td>Isaac Royall (Kensington, England) to Dr. Simon Tufts</td><td>Mentioned only (&ldquo;Dr. Tufts had a letter from him&rdquo;).</td><td class="cite">Brooks, pp. 173&ndash;174. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
<tr><td>October 22 [1778?]</td><td>Dr. Simon Tufts to Isaac Royall</td><td>Reports that the Medford committee had taken the estate out of his hands; known from Royall&rsquo;s reply.</td><td class="cite"><em>Medford Historical Register</em>, vol. XI, p. 17 (&ldquo;A recently discovered Letter written by Colonel Isaac Royall in 1779&rdquo;). <a href="{PU("2005.05.0011", 3)}">Perseus</a></td></tr>
<tr><td>1779</td><td>Isaac Royall to [his friends in Medford]</td><td>&ldquo;Some time past I receiv&rsquo;d a Letter from my Attorney Dr Simon Tufts at Medford dated October 22&rdquo;; says he has written back to &ldquo;Doct. Tufts.&rdquo;</td><td class="cite"><em>Medford Historical Register</em>, vol. XI, p. 17. <a href="{PU("2005.05.0011", 3)}">Perseus</a></td></tr>
<tr><td>April 12, 1779</td><td>Isaac Royall (Kensington) to Dr. Simon Tufts</td><td>&ldquo;I doubt not you, and Mr. Hall, and the rest of my friends, will do all in your power to procure me liberty from the General Court to return home&rdquo;</td><td class="cite">Brooks, p. 175. <a href="{PU("2001.05.0104", 5)}">Perseus</a></td></tr>
</tbody></table>
{UNV("Whether Royall&rsquo;s letter of August 22, 1779 (Brooks, p. 175) was also addressed to Dr. Tufts. Brooks says only &ldquo;in another letter.&rdquo; The originals&rsquo; whereabouts are not stated.")}
<h3>Dr. Simon Tufts the elder (1700&ndash;1747)</h3>
<p>No letter by or to the elder Dr. Simon has yet been found in print. His obituary of February 5, 1747, printed &ldquo;in the public papers,&rdquo; is quoted by Brooks (pp. 303&ndash;304).</p>
<h3>Simon Tufts, the doctor&rsquo;s son (not a physician)</h3>
<p>The <em>Medford Historical Register</em> prints &ldquo;Extracts from letters written by Simon Tufts Son of Dr. Simon Tufts&rdquo; (vol. VI, p. 96, &ldquo;A Package of old letters&rdquo;. <a href="{PU("2005.05.0006", 6)}">Perseus</a>), and a letter he wrote from Cape Town on March 20, 1801, to his brother-in-law Benjamin Hall Jr. (vol. XVI, p. 30. <a href="{PU("2005.05.0016", 5)}">Perseus</a>). He is not either doctor.</p>
<h3>Manuscript collections (not yet read item by item)</h3><ul>
<li><strong>Cotton Tufts papers, 1751&ndash;1805</strong>, B MS c30, Countway Library of Medicine, Harvard: correspondence &ldquo;with his older brother, Simon Tufts (1726/7&ndash;1786), and other physicians, regarding medical matters, and the founding of a medical society,&rdquo; with manuscripts on vaccine, inoculation and the 1772&ndash;73 measles. <a href="https://researchworks.oclc.org/archivegrid/collection/data/122521209">ArchiveGrid</a> &middot; <a href="https://curiosity.lib.harvard.edu/contagion/feature/cotton-tufts-papers">Harvard <em>Contagion</em> exhibit</a></li>
<li><strong>Simon Tufts, correspondence, 1751&ndash;1778</strong>, New England Historic Genealogical Society; which Simon is not stated. <a href="https://snaccooperative.org/view/6284266">SNAC record for Cotton Tufts</a></li>
<li><strong>Cotton Tufts diaries, 1748&ndash;1794</strong> (interleaved almanacs), Massachusetts Historical Society. <a href="https://snaccooperative.org/vocab_administrator/resources/7140379">SNAC description</a></li>
<li>Abigail Adams to Cotton Tufts, 2 March 1788 (original, MHS). <a href="https://www.masshist.org/database/2154">MHS Collections Online</a></li>
<li>Also listed by SNAC: John Adams to &ldquo;Dr. Tufts,&rdquo; Nov. 18, 1797 (Morgan Library); Caleb Gannett to Cotton Tufts, Apr. 20, 1781 (Duke Medical Center Archives); John Avery to Cotton Tufts, Apr. 9, 1790 (Harvard University Archives).</li></ul>
{UNV("The Massachusetts Medical Society&rsquo;s own archives have not been searched. The NEHGS and Countway letters between the two brothers are the most likely source of letters on smallpox and throat distemper by Dr. Simon the younger.")}
</section>'''
_EXTRA7 = EXTRA
def EXTRA(path):
    out = _EXTRA7(path)
    if path == "collections.html": out = out.replace('<section id="muskets">', DOCTORS + "{DIV}" + '<section id="muskets">', 1) if '<section id="muskets">' in out else out + "{DIV}" + DOCTORS
    if path == "profiles/cotton-tufts.html": out += '{DIV}<section id="doctor-letters"><h2>His Letters</h2><p>The Adams Papers hold 188 letters by or to Dr. Cotton Tufts, ' + str(len(DIS)) + ' of them touching on smallpox inoculation, fevers, dysentery or measles. Examples: to John Adams, July 5, 1776: &ldquo;Yesterday People in Boston were openly inoculated for the Small Pox&rdquo; (<a href="' + MHSV + 'ADMS-04-02-02-0019">MHS</a>). His Countway papers hold letters with his brother Dr. Simon. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p><p class="cite">Abigail Adams to Dr. Cotton Tufts, November 6, 1787. <em>Adams Family Correspondence</em>, vol. 8, pp. 201&ndash;203. <a href="{P}collections.html#' + AUDIO_ANCHOR + '">Listed under Letters of the Tufts Doctors</a></p>' + LETTER_AUDIO_HTML(with_id=True) + '</section>'
    if path == "profiles/simon-tufts-11-1.html": out += '{DIV}<section id="doctor-letters"><h2>His Letters</h2><p>Letters between this Dr. Simon (1727&ndash;1786) and the Loyalist Isaac Royall, 1775&ndash;1779, are quoted by Brooks (pp. 173&ndash;179) and the <em>Medford Historical Register</em> (vol. XI, p. 17). His letters with his brother Cotton are in the Countway Library. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p>' + UNV("Cause of death. This page&rsquo;s source says a fall from his horse, and Brooks (p. 306) says a fall brought on bleeding of the lungs. Mary Cranch wrote to Abigail Adams on September 28, 1786 that &ldquo;Doctor Simon Tufts is just gone in a consumtion&rdquo; (<a href=\"" + MHSV + "ADMS-04-07-02-0131\">MHS</a>), and Medford&rsquo;s church record gives consumption.") + '</section>'
    if path == "profiles/simon-tufts-1700.html": out += '{DIV}<section id="doctor-letters"><h2>Letters</h2><p>No letter by or to this Dr. Simon has yet been found. See <a href="{P}collections.html#doctors-letters">Letters of the Tufts Doctors</a>.</p></section>'
    return out
