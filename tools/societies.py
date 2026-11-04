# Learned societies (Cotton) and the two Drs. Simon (owner requests 2026-11-03).
AAA1 = "https://www.amacad.org/archives/transcriptions/rg7_minutes_vol01pt1.html"
AAAC = "https://www.amacad.org/archives/charter"
MMSP = "https://www.massmed.org/Governance-and-Leadership/MMS-Officers/Past-Presidents-of-the-Massachusetts-Medical-Society/"
CSM = "https://www.colonialsociety.org/node/1202"
CSMC = 'Philip Cash, &ldquo;The Professionalization of Boston Medicine, 1760&ndash;1803,&rdquo; <em>Medicine in Colonial Massachusetts</em> (Colonial Society of Massachusetts, 1980), n. 33. <a href="' + CSM + '">Online text</a>'
CTW = '<a href="https://curiosity.lib.harvard.edu/contagion/feature/cotton-tufts-papers">Harvard Library, <em>Contagion</em>: &ldquo;Cotton Tufts Papers&rdquo;</a>; also <a href="https://researchworks.oclc.org/archivegrid/collection/data/122521209">ArchiveGrid record for B MS c30</a>'
NEJM = '&ldquo;From the Curator&rsquo;s Notebook: Cotton Tufts to Cotton Tufts, 1776,&rdquo; <em>New England Journal of Medicine</em> 260 (March 26, 1959). <a href="https://doi.org/10.1056/nejm195903262601317">DOI</a>'
COTTON_SOC = ('{DIV}<section id="learned-societies"><h2>Learned Societies</h2>'
 '<h3>American Academy of Arts and Sciences, 1780</h3>'
 + Q("Be it therefore Enacted &hellip; that the Honble Samuel Adams Esqr., Honble John Adams Esqr., &hellip; Honble John Hancock Esqr., &hellip; Cotton Tufts Esqr., &hellip; be, and they hereby are formed into, constituted &amp; made a body politic and corporate, by the name of the American Academy of Arts and Sciences", f'Act of incorporation, passed May 3, 1780, as copied into the Academy&rsquo;s Minutes, vol. 1, pp. 1&ndash;2. <a href="{AAA1}">American Academy archives transcription</a>; <a href="{AAAC}">charter and list of the 62 charter members</a>')
 + '<p>He was one of 62 incorporators named in the act. The Academy&rsquo;s own charter page lists him among its charter members.</p>'
 + UNV("The date. The copied minutes say the act passed May 3, 1780; the Academy&rsquo;s charter page says it was granted May 4, 1780.")
 + '<h3>Massachusetts Medical Society: an incorporator, 1781</h3>'
 + Q("Tufts was also an incorporator of the Massachusetts Medical Society in 1781 and served as its fourth president (1787&ndash;1795).", CTW)
 + '<p>The Society was incorporated on November 1, 1781, with thirty-one incorporators (Cash, as below, text at nn. 45&ndash;46).</p>'
 + UNV("The 1781 act itself, with its list of names, has not been seen. Cotton Tufts&rsquo;s place among the incorporators rests on the Countway Library&rsquo;s description.")
 + '<h3>President of the Massachusetts Medical Society, 1787&ndash;1795</h3>'
 + Q("Cotton Tufts, Weymouth, 1787-1795", f'Massachusetts Medical Society, <a href="{MMSP}">Past Presidents of the Massachusetts Medical Society</a>')
 + '<p>On the Society&rsquo;s list he follows Edward Augustus Holyoke (1786&ndash;1787), William Kneeland (1784&ndash;1786) and Holyoke&rsquo;s first term (1782&ndash;1784), which makes him the fourth president.</p>'
 + '<h3>The 1765 plan for a medical society</h3>'
 + Q("The prime mover in the attempt to found a colonywide medical society in 1765 was Dr. Cotton Tufts of Weymouth, later a major force in the early years of the Massachusetts Medical Society.", CSMC)
 + '<p>Cash calls the 1765 effort &ldquo;the abortive attempt&rdquo; (same article, text at n. 33). A 1959 note in the <em>New England Journal of Medicine</em> also says that Cotton planned the first state medical society in 1765 and that the plan fell through (' + NEJM + '; abstract only seen). His older brother, <a href="{P}profiles/simon-tufts-11-1.html">Dr. Simon Tufts (1727&ndash;1786)</a>, was called to the plan&rsquo;s first meeting (see his profile).</p>'
 + UNV("No minutes or letters of the 1765 meeting have been seen. Cotton&rsquo;s letters about it are probably among his Countway papers, which have not been read.")
 + '</section>')
SIM_ELDER = ('{DIV}<section id="offices"><h2>Justice, Physician to the College, Death and Burial</h2>'
 + Q("He was honored with three commissions,&mdash;one for the peace, in the year 1733; another for a special justice, in 1741; and a third for justice of the quorum, 1743", BRP(303) + ", quoting his obituary of Feb. 5, 1747")
 + Q("He was often called to visit the sick at Harvard College; and, though not rich himself, never demanded fees except from rich students.", BRP(303))
 + Q("On the 31st of January, died here, of a convulsive asthma, and this day was decently buried, Simon Tufts, Esq., having just completed his forty-seventh year.", BRP(303) + ", quoting the obituary dated &ldquo;Medford, Feb. 5, 1747&rdquo;")
 + '<p>The Medford vital records give his death as Jan. 31, 1746/7, &ldquo;a. 47 &lsquo;to a day&rsquo;&rdquo;; he was born Jan. 31, 1700 (Brooks, p. 302). He died on his 47th birthday.</p>'
 + '<p><strong>Burial:</strong> Salem Street Burying Ground, Medford, plot 35. <a href="https://www.findagrave.com/memorial/26903835/simon-tufts">Find a Grave memorial 26903835</a> (user-contributed). The same plot holds his son <a href="{P}profiles/simon-tufts-11-1.html">Dr. Simon Tufts (1727&ndash;1786)</a>, <a href="https://www.findagrave.com/memorial/26903836/simon-fms-tufts">memorial 26903836</a>.</p>'
 + UNV("The name &ldquo;Tufts Family Tomb&rdquo; for plot 35 comes from a private genealogy site, not from a cemetery record. The Brooks obituary says he died &ldquo;of a convulsive asthma&rdquo;; no other record of the cause has been seen. The Sibley sketch (vol. VII, pp. 444&ndash;446) and Wyman&rsquo;s <em>Genealogies and Estates of Charlestown</em> have not been checked.")
 + '</section>')
SIM_YOUNGER = ('{DIV}<section id="medical-society"><h2>Medical Societies: 1765 and the Massachusetts Medical Society</h2>'
 '<p>This section concerns Dr. Simon Tufts the younger (1727&ndash;1786), not his father, Dr. Simon Tufts (1700&ndash;1747).</p>'
 '<h3>The 1765 meeting</h3>'
 + Q("he was one of the first in the State who felt the need of a medical society; and he was called to the first meeting for consummating the plan, which meeting took place on the third Monday in March, 1765, at Gardner&rsquo;s tavern, on Boston Neck.", BRP(306))
 + '<p>The plan itself is credited to his younger brother. Philip Cash calls <a href="{P}profiles/cotton-tufts.html">Dr. Cotton Tufts</a> of Weymouth &ldquo;the prime mover&rdquo; of the 1765 attempt, which failed (' + CSMC + '). So Simon is recorded as a participant called to the meeting, and Cotton as its organizer.</p>'
 '<h3>Fellow of the Massachusetts Medical Society, 1782</h3>'
 '<p>Medford&rsquo;s vital records cite his gravestone as &ldquo;Simon Tufts Esq., F. M. S.,&rdquo; that is, Fellow of the Medical Society, and his Find a Grave memorial is headed &ldquo;Dr Simon F.M.S. Tufts Esq.&rdquo; (<a href="https://www.findagrave.com/memorial/26903836/simon-fms-tufts">memorial 26903836</a>). The fellowship date of 1782 comes from <em>Tufts Kinsmen</em>, Vol. I, p. 110.</p>'
 + UNV("The 1782 date of his fellowship has not been confirmed from the Society&rsquo;s own records.")
 + '</section>')
_EXTRA9 = EXTRA
def EXTRA(path):
    out = _EXTRA9(path)
    if path == "profiles/cotton-tufts.html": out = COTTON_SOC + out
    if path == "profiles/simon-tufts-1700.html": out = SIM_ELDER + out
    if path == "profiles/simon-tufts-11-1.html": out = SIM_YOUNGER + out
    return out
