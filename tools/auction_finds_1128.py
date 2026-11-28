# Historic auction and bookseller listings of pre-1910 Tufts papers (28 Nov. 2026).
# Free public lot pages and registers only; unverified details are flagged.
# Hooked from six_profiles_1127.py, so new text enters PROFILES before pages are written.

_CT = "cotton-tufts"
_CTJ = "cotton-tufts-jr"
_FT = "francis-tufts-41-4"
_HT = "horace-tufts"
_QT = "quincy-tufts"
_MB = "mercy-brooks-tufts"
_SW = "susanna-warner-tufts"
_PWH = "peter-tufts-winter-hill"

_CHR1772 = "https://www.christies.com/en/lot/lot-1081160"
_CHR1788 = "https://www.christies.com/en/lot/lot-1632812"
_RR1788 = "https://www.rrauction.com/auctions/lot-detail/34431680608121-john-hancock-two-months-before-hancock-as-architect-of-the-massachusetts-compromise-advocates-that-the-constitution-be-unconditionally-ratified/"
_RR1807_2014 = "https://www.rrauction.com/auctions/lot-detail/332188004285-abigail-adams-the-president-and-mrs-adams-send-an-invitation-to-new-years-dinner/"
_RR1807_2025 = "https://www.rrauction.com/auctions/lot-detail/350848407310001-abigail-adams-third-person-autograph-letter-signed-the-president-and-mrs-adams-ask-the-pleasure-of-mr-and-mrs-tufts-company-to-dinner/"
_WFA = "https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection"
_BRM = "https://bostonraremaps.com/inventory/8th-massachusetts-regiment-returns-1779-1781/"
_HM84015 = "https://www.huntington.org/collections/lib-msshm-84015"
_ABE_HT = "https://www.abebooks.com/first-edition/1848-HANDWRITTEN-LETTER-CAPT-HORACE-TUFTS/30461455113/bd"
_SHIP = "https://archive.org/details/shipregistersofd00hitc"
_ISTG = "https://www.immigrantships.net/v21/1800v21/gambia18350408.html"
_UA_DRAPER = "https://www.universityarchives.com/auction-lot/dr.-cotton-tufts-founder-of-mass.-medical-societ_1204a00a89"
_RR_DRAPER = "http://rr-auctions.blogspot.com/2012/08/rr-autograph-auction-cotton-tufts.html"

_SHIPB = ('A. Frank Hitchings and Stephen Willard Phillips, <em>Ship Registers of the District of Salem and Beverly, 1789&ndash;1900</em> '
          '(Salem: Essex Institute, 1906)')

_HOLDINGS = (
    "<p>These papers have come to light as scattered single documents; no large Tufts family archive has appeared on the open market. "
    "The principal holdings remain institutional, among them the Weymouth Public Libraries&rsquo; "
    f'<a href="{_WFA}">Tufts/Smith/Adams Family Collection</a>, '
    "the Countway Library of Medicine, the Massachusetts Historical Society, the New York Public Library, and the Tufts family papers in university collections.</p>"
)

_COTTON_SEC = (
    '<section id="letters-at-auction"><h2>Letters and Papers at Auction</h2>'
    "<p>From time to time a Cotton Tufts letter has come up for sale as a single autograph, far from the institutional collections that hold the bulk of his papers.</p>"
    "<p>On 15 October 1772, writing from Weymouth, he sent a short signed letter that later appeared at Christie&rsquo;s, New York, on 12 June 1996, where it realized $115 "
    f'(<a href="{_CHR1772}">lot page</a>). The catalogue called it an autograph letter signed to his daughter, and printed this extract: '
    "&ldquo;My Dear Mr. Shute brought me a very agreeable present, a line from you - and the Latin, which you have sent me in good season - and am well pleas&rsquo;d with it &amp; with your improvement in writing&hellip; Your affectionate father Cotton Tufts.&rdquo; "
    "The only child recorded of " + PL(_CT, "Dr. Cotton Tufts") + " and " + PL("lucy-quincy-tufts", "Lucy Quincy") + " is their son "
    + PL(_CTJ, "Cotton Tufts (1757&ndash;1833)") + ". The Weymouth family papers hold letters of August 1772 and January 1773 from the doctor to that son, in care of Rev. Mr. Shute "
    f'(<a href="{_WFA}">finding aid</a>, box 1, folders 5 and 7). The catalogue&rsquo;s &ldquo;daughter&rdquo; is therefore likely a misidentification, and the Latin letter of 15 October 1772 is more probably to Cotton Jr. at school.</p>'
    + UNV("The Christie&rsquo;s catalogue of 12 June 1996 describes the letter as written &ldquo;to his daughter.&rdquo; No daughter of Dr. Cotton Tufts is known, and the Shute address in the Weymouth papers points to Cotton Jr., but the original address leaf has not been seen here. A later offering of this same letter at RR Auction in 2008 has been reported; no public RR Auction lot page for a 2008 sale of this item was found. Note: Pending further work.")
    + "<p>On 10 April 1788, John Hancock, writing as Governor of Massachusetts, summoned Dr. Tufts to a committee &ldquo;to enquire into the State of the College,&rdquo; and asked him to attend &ldquo;on Tuesday next 10 oClock at the College.&rdquo; "
    "In Massachusetts in 1788 &ldquo;the College&rdquo; meant Harvard. The letter was sold at Christie&rsquo;s, New York, on 10 December 1999, realizing $10,350 "
    f'(<a href="{_CHR1788}">lot page</a>), and again at RR Auction, sale no. 608, which closed 12 May 2021, for $4,973 '
    f'(<a href="{_RR1788}">lot page</a>). The Christie&rsquo;s catalogue&rsquo;s phrase &ldquo;Boston College&rdquo; is an anachronism: Boston College was not founded until 1863.</p>'
    + UNV("A letter from Dr. Cotton Tufts to Dr. Amos Holbrooke (or Holbrook), dated 13 September 1787, concerning medical association rules, and said to have been offered at RR Auction in 2007 and again in 2011, was not found on a public lot page. A different letter, to Dr. Philip Draper of Dedham, 26 October 1785, declining an invitation to an &ldquo;Association of Physicians&rdquo; and asking how the society had proceeded, has been described on an "
    + f'<a href="{_RR_DRAPER}">RR Auction blog post</a> (with an older bid-tracker link) and was later offered as '
    + f'<a href="{_UA_DRAPER}">University Archives lot 194</a> (6 December 2016, estimate $800&ndash;$1,000; the lot is marked as having passed). That 1785 Draper letter is not the 1787 Holbrooke letter. Note: Pending further work.')
    + _HOLDINGS
    + "</section>"
)

_JR_SEC = (
    '<section id="letters-at-auction"><h2>A New Year&rsquo;s Dinner Invitation, 1807</h2>'
    "<p>On 31 December 1807 Abigail Adams wrote a third-person dinner invitation, addressed in her hand to &ldquo;Mr Cotton Tufts and Lady, Weymouth.&rdquo; The note reads, in the wording printed by RR Auction in 2014: "
    "&ldquo;The president and Mrs Adams ask the pleasure of Mr and Mrs Tufts company to dinner tomorrow 2 oclock, together with Mr Quincy Tufts and Miss Lucy.&rdquo; "
    "The 2014 catalogue identifies the guests as " + PL(_CTJ, "Cotton Tufts (1757&ndash;1833)") + ", his wife "
    + PL(_MB, "Mercy Brooks Tufts") + ", and their two eldest children, "
    + PL(_QT, "Quincy Tufts") + " and Lucy, then aged sixteen and fourteen. That reading fits the family: Quincy was born on 4 July 1791, Lucy later married Thomas Tarbell at Weymouth on 5 May 1813, and the doctor&rsquo;s first wife, "
    + PL("lucy-quincy-tufts", "Lucy Quincy") + ", had died in 1785. The invitation was sold at RR Auction, sale no. 428, which closed 14 May 2014, for $2,027 "
    f'(<a href="{_RR1807_2014}">lot page</a>), and again at sale no. 731, which closed 10 December 2025, for $2,723 '
    f'(<a href="{_RR1807_2025}">lot page</a>).</p>'
    + UNV("The 2025 RR Auction catalogue attributes the invitation to the physician Dr. Cotton Tufts, Abigail&rsquo;s uncle by marriage, rather than to Cotton Jr. and Mercy. The 2014 catalogue, and the family dates, identify the younger household. John Adams is styled &ldquo;the President&rdquo; in the invitation, a courtesy title; he had left office in 1801. Note: Pending further work.")
    + "</section>"
)

_QT_SEC = (
    '<section id="letters-at-auction"><h2>Invited to Dinner, 1808</h2>'
    "<p>Abigail Adams&rsquo;s invitation of 31 December 1807, asking &ldquo;Mr and Mrs Tufts&rdquo; of Weymouth to dinner on New Year&rsquo;s Day &ldquo;together with Mr Quincy Tufts and Miss Lucy,&rdquo; names this Quincy, then sixteen, and his sister Lucy. "
    "The note was sold at RR Auction in 2014 and again in 2025; the texts and links are on the page of his father, "
    + PL(_CTJ, "Cotton Tufts (1757&ndash;1833)") + ".</p></section>"
)

_FRANCIS_SEC = (
    '<section id="regimental-returns"><h2>The Regimental Returns, 1779&ndash;1781</h2>'
    "<p>A companion to " + PL(_FT, "Francis Tufts") + "&rsquo;s orderly books is a manuscript volume of weekly returns for the same regiment, the 8th Massachusetts, commanded by Col. Michael Jackson, covering 3 September 1779 to 18 December 1781, while the regiment was on garrison duty at West Point and in the Hudson Valley. "
    "Boston Rare Maps, which offered the book, transcribes its title page as &ldquo;Returns of the 8th Massachusetts Regiment of Foot Commanded by Col Michl Jackson of West Newton. [As?] kept by Adjutant Francis Tufts &amp; Others from Septr. 3rd 1779 to Decr. 18th 1781, with some additions &amp; remarks made since by Gardner Tufts.&rdquo; "
    "The dealer notes that Tufts signed most of the returns dated 3 November 1780 and later, and that many of the earlier entries are also in his hand. Later leaves, added in the nineteenth century, include a short narrative of his service, copies of orders, and family matter. "
    f'The listing is at <a href="{_BRM}">Boston Rare Maps</a>. The Huntington Library purchased the volume from that dealer in February 2021; it is now '
    f'<a href="{_HM84015}">mssHM 84015</a>, in the same library that holds his orderly books (mssHM 719).</p>'
    + UNV("A 2020 sale of this volume at Skinner Auctioneers for $8,125 has been reported, but no public Skinner or Bonhams lot page giving that date, a lot number, or a realized price of $8,125 was found. The identity of Gardner Tufts, who made later additions to the volume, has not been established from a vital record in this pass. Note: Pending further work.")
    + "<p>Like the Cotton Tufts letters that have appeared at auction, this book came on the market as a single manuscript, not as part of a large family archive. It is now with the institutional collection of his orderly books at the Huntington.</p>"
    + "</section>"
)

_PWH_UNV = (
    "<strong>A 1781 Charlestown land document</strong> said to involve Tufts and Adams descendants, to have been signed by Nathaniel Gorham, to concern land near Winter Hill, and to have been offered by University Archives, was not found on a public University Archives lot page, and the Tufts persons named in it have not been identified. Note: Pending further work."
)

# ---- Capt. Horace Tufts (new short profile) ----
_nf_new(
    _HT,
    "Capt. Horace Tufts (b. about 1796&ndash;97)",
    "[b. about 1796&ndash;97] &ndash; [death not found]",
    "Salem and Beverly, Mass.; at sea",
    "1797",
    "",
    "19th Century",
    "Shipmaster in the Salem and Beverly registers; parentage not established",
    "<p>Horace Tufts was a shipmaster in the Salem and Beverly customs district in the mid-nineteenth century. On 8 April 1835 he arrived at New York from St. Jago (Santiago), Cape Verde, on the brig <em>Gambia</em>, listed as a mariner, age 38, one of several &ldquo;distressed seamen&rdquo; put on board by the American consul "
    f'(National Archives microfilm M237, reel 26, list 144; <a href="{_ISTG}">transcript of the manifest</a>). That age points to a birth about 1796 or 1797.</p>'
    + "<p>The printed Salem and Beverly ship registers name him as master of the brig <em>Ruby</em>, 126 tons, built at Sedgwick, Maine, in 1839, registered 5 August 1847, with owners Edward D. Kimball and John Bertram ("
    + _SHIPB + f', p. 161. <a href="{_SHIP}/page/161/mode/1up">Internet Archive</a>). '
    "They also name him as master of the bark <em>Lady Suffolk</em>, 199 tons, registered 17 October 1860, William Calley owner ("
    + _SHIPB + f', p. 103. <a href="{_SHIP}/page/103/mode/1up">Internet Archive</a>).</p>'
    + '<section id="letters-at-auction"><h2>Letter from the Brig <em>Tam O&rsquo;Shanter</em>, 1848</h2>'
    + "<p>A bookseller, R &amp; A Petrilla of Roosevelt, New Jersey, has listed a 1&frac12;-page autograph letter signed by Horace Tufts, written at Matacong (Matakong, Guinea) on 15 December 1848 and addressed to Edward D. Kimball, the Salem merchant who appears as an owner of both the <em>Ruby</em> and the brig <em>Tam O&rsquo;Shanter</em>. "
    "The listing quotes him as writing, in part, that he is &ldquo;very sorry to inform you that the Tam O Shanter is in such a very bad condition that I am afraid she will not be fit to come home unless there is a great deal of money laid out,&rdquo; that he had &ldquo;been up the Coast in her and disposed of part of her Cargo and the Remnant of Ruby Powder,&rdquo; and that he had left his sick second mate at Sierra Leone to come home in the brig <em>Ohio</em>, his chief mate having also been sick. He asked Kimball to pay the second mate on his return and promised to &ldquo;do all in my power to forward the voyage.&rdquo; "
    f'The listing is at <a href="{_ABE_HT}">AbeBooks</a> (asked $252 at the time it was checked).</p>'
    + "<p>The same registers describe the brig <em>Tam O&rsquo;Shanter</em>, 123 tons, built at Essex in 1833, as registered 18 March 1848 with Edward D. Kimball as owner and Collins Ingalls as master ("
    + _SHIPB + f', p. 181. <a href="{_SHIP}/page/181/mode/1up">Internet Archive</a>). '
    "Horace Tufts is not named as master on that register entry; the December 1848 letter is the evidence that he was then in command of the vessel off the West African coast.</p></section>",
    "<p>No Revolutionary or military service is recorded or expected for him.</p>",
    "<p>Parentage, wife, and children have not been established from a vital record in this pass. The Salem and Beverly ship registers and the 1835 passenger list identify him only as a master and mariner.</p>",
    "<strong>Parentage and family connection.</strong> No birth, marriage, or death line for this Horace Tufts was confirmed in the Salem vital records searched in this pass, and he has not been attached to a Medford or Charlestown family already on this site. The age 38 on the 1835 manifest is the only evidence used here for a birth about 1796&ndash;97. "
    "<strong>The <em>Tam O&rsquo;Shanter</em>.</strong> The March 1848 Salem register names Collins Ingalls, not Horace Tufts, as master; the letter of 15 December 1848 is known from the bookseller&rsquo;s extract, not from the original sheet. "
    "<strong>The bookseller&rsquo;s further claims</strong> that he was employed in the triangle trade, that he &ldquo;plied some of the most notorious slave-trading ports,&rdquo; and that he later sued the English government over an accusation of slave trading, are the seller&rsquo;s commentary and are not in the quoted letter. Note: Pending further work.",
    "<p>No marriage has been confirmed from a vital record in this pass. Note: Pending further work.</p>",
)

_up_add(_CT, _COTTON_SEC, 'id="letters-at-auction"')
_up_add(_CTJ, _JR_SEC, 'id="letters-at-auction"')
_up_add(_QT, _QT_SEC, 'id="letters-at-auction"')
_up_add(_FT, _FRANCIS_SEC, 'id="regimental-returns"')
_up_unv(_PWH, _PWH_UNV)

# Brief pointers from Mercy (named in the 1807 invitation) and from the 19th-century generation page.
_up_add(
    _MB,
    "<p>She is named, with her husband and their children Quincy and Lucy, as a guest in Abigail Adams&rsquo;s dinner invitation of 31 December 1807. The letter and its later sales are described on "
    + PL(_CTJ, "Cotton Tufts (1757&ndash;1833)")
    + "&rsquo;s page.</p>",
    "dinner invitation of 31 December 1807",
)

_AF_EXTRA = EXTRA
def EXTRA(path):
    out = _AF_EXTRA(path)
    if path == "generations/19th-century.html":
        _sec = (
            '{DIV}<section id="horace-tufts-note"><h2>A Salem Shipmaster</h2><p>'
            + PL(_HT, "Capt. Horace Tufts")
            + ", a mid-nineteenth-century master in the Salem and Beverly registers, wrote from the West African coast in 1848 about the brig <em>Tam O&rsquo;Shanter</em>. "
            "His parentage in the larger Tufts family has not been established.</p></section>"
        )
        if 'id="horace-tufts-note"' not in out:
            out += _sec
    if path == "collections.html":
        _sec = (
            '{DIV}<section id="regimental-returns"><h2>Francis Tufts&rsquo;s Regimental Returns, 1779&ndash;1781</h2><p>A volume of weekly returns of the 8th Massachusetts Regiment, kept by Adjutant '
            + PL(_FT, "Francis Tufts")
            + " and others from 1779 to 1781, is now at the Huntington Library (mssHM 84015), purchased in February 2021 from Boston Rare Maps. "
            "It stands with his orderly books in the same library. Details are on his profile.</p></section>"
        )
        if 'id="regimental-returns"' not in out:
            if '<section id="francis-tufts-orderly-book">' in out:
                out = out.replace(
                    '<section id="francis-tufts-orderly-book">',
                    _sec + "{DIV}" + '<section id="francis-tufts-orderly-book">',
                    1,
                )
            else:
                out += _sec
    if path == "sources.html":
        _li = (
            "<li>Regimental returns of the 8th Massachusetts Regiment, 3 September 1779&ndash;18 December 1781, kept by Adjutant Francis Tufts and others, with later additions by Gardner Tufts. "
            f'The Huntington Library, mssHM 84015; purchased from Boston Rare Maps, February 2021. <a href="{_HM84015}">Huntington catalogue</a> &middot; '
            f'<a href="{_BRM}">Boston Rare Maps listing</a>.</li>'
        )
        if "mssHM 84015" not in out:
            out = out.replace("</ul></section>", _li + "\n</ul></section>", 1)
    return out

exec(open("tools/artifacts_1128c.py").read())
exec(open("tools/artifacts_1128b.py").read())
_ar_gallery()
print("auction_finds_1128 done")
