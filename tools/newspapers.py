# Massachusetts Spy mentions (Digital Commonwealth full-text search, 2026-11-03). OCR quoted with obvious long-s fixes only.
DCS = "https://www.digitalcommonwealth.org/search/commonwealth:"
def SPY(date, iid, pg, col, txt):
    return Q(txt, f'<em>The Massachusetts Spy</em> (Boston), {date}, p. {pg}, col. {col} (column approximate, from OCR position). <a href="{DCS}{iid}">Issue scan (Digital Commonwealth)</a>')
NEWS = f'''<section id="newspapers"><h2>In the Newspapers: <em>The Massachusetts Spy</em></h2>
<p>Isaiah Thomas&rsquo;s <em>Massachusetts Spy</em>, printed in Boston until April 1775, is the paper sometimes called the &ldquo;Boston Spy.&rdquo; A full-text search of its digitized issues finds a Simon Tufts in three kinds of notice. The quotations come from the OCR text, with the long s and obvious misreadings corrected. Each should be checked against the linked scan.</p>
<h3>Instructions to the representative, January 1773</h3>
{SPY("January 7, 1773", "n2971p92q", 3, 1, "To Simon Tufts, Esq.")}<p>The heading above, garbled in the OCR, appears to read &ldquo;Instructions to their Representative.&rdquo; Check the scan.</p>
<p>The notice prints a town&rsquo;s instructions to its representative to back constitutional measures in the House of Representatives to redress the province&rsquo;s grievances, part of the town replies to Boston&rsquo;s Committee of Correspondence.</p>
{UNV("The town and which Simon Tufts. The OCR text shown does not name the town. Medford&rsquo;s Dr. Simon Tufts (1727&ndash;1786), son of the Dr. Simon who died in 1747, is a likely candidate. <em>The Boston Gazette</em> of June 1, 1772 lists &ldquo;Medford, Simon Tufts, Esq.&rdquo; among the members returned to the House (see below), which supports Medford, but the town is not named in this notice.")}
<h3>A store near Faneuil Hall, autumn 1774</h3>
{SPY("October 6, 1774", "2v240h051", 1, 2, "To be SOLD, by SIMON TUFTS, At the Store adjoining Mr. Henry Prentiss, near Faneuil-Hall, Choice Jamaica Spirits, West-India and New-England Rum, Loaf and Brown Sugars")}
<p>The same advertisement runs in the issues of <a href="{DCS}v405x071f">October 13</a>, <a href="{DCS}3j336s19f">October 20</a>, <a href="{DCS}nc584c620">October 27</a> and <a href="{DCS}348536069">November 10, 1774</a> (p. 4 in each).</p>
{UNV("Which Simon Tufts kept this Boston store. He may be the <a href='{P}profiles/simon-tufts-29-1.html'>Loyalist Simon Tufts (1750&ndash;1801)</a>, but that is not confirmed.")}
<h3>List of letters, July 1774</h3>
{SPY("July 21, 1774", "0g358508k", 2, 4, "Tufts, Simon")}
<p>The name appears in a list of letters waiting at the post office. Identity Unverified.</p>
</section>'''
SIMON29 = '{DIV}<section id="spy"><h2>In the Newspapers</h2><p>In the autumn of 1774 <em>The Massachusetts Spy</em> carried advertisements for goods &ldquo;To be SOLD, by SIMON TUFTS, At the Store adjoining Mr. Henry Prentiss, near Faneuil-Hall.&rdquo; Whether that merchant is this man is Unverified. See <a href="{P}collections.html#newspapers">Collections</a>.</p></section>'
_EXTRA5 = EXTRA
def EXTRA(path):
    out = _EXTRA5(path)
    if path == "collections.html": out += "{DIV}" + NEWS
    if path == "profiles/simon-tufts-29-1.html": out += SIMON29

    return out

# Boston Gazette mentions (Internet Archive OCR of the Boston Gazette and Country Journal, 385 issues 1768-1776 searched 2026-11-04). Page = scan image order.
IA_G = "https://archive.org/details/per_boston-gazette_the-boston-gazette-and-country-journal_"
def GAZ(date, iid, leaf, pg, txt):
    loc = f"p. {pg} (page from the scan order)" if pg else f"scan image {leaf+1} (page number not confirmed)"
    return Q(txt, f'<em>The Boston-Gazette, and Country Journal</em>, {date}, {loc}. <a href="{IA_G}{iid}/page/n{leaf}">Issue scan (Internet Archive)</a>')
GAZSEC = f'''<section id="boston-gazette"><h2>In the Newspapers: <em>The Boston Gazette</em></h2>
<p>Edes and Gill&rsquo;s <em>Boston-Gazette, and Country Journal</em> was the leading Whig paper of Boston. A search of the 385 issues from 1768 to 1776 digitized on the Internet Archive finds the Tufts notices below. The OCR is poor, so each quotation is given in modern spelling and should be checked against the linked scan.</p>
<h3>A Harvard master&rsquo;s degree, July 1770</h3>
{GAZ("July 23, 1770", "1770-07-23_3_798", 0, None, "Masters of Arts &hellip; Simon Tufts")}
<p>His name is in the commencement list of those taking the Master of Arts at Harvard in 1770, three years after the Simon Tufts of the class of 1767. See <a href="{{P}}harvard.html">Harvard College</a>.</p>
{UNV("That this is <a href='{P}profiles/simon-tufts-29-1.html'>Simon Tufts (1750&ndash;1801)</a>. The class of 1767 is the likely link, but the list gives no other detail.")}
<h3>Justice of the peace, September 1770</h3>
{GAZ("September 3, 1770", "1770-09-03_3_804", 0, None, "Simon Tufts, Esq; to be a Justice of the Peace for the County of Middlesex.")}
<p>The line comes from a list of new commissions issued by the governor. It matches the 1770 justiceship given for <a href="{{P}}profiles/simon-tufts-11-1.html">Dr. Simon Tufts (1727&ndash;1786)</a> of Medford.</p>
{UNV("The notice gives no town. Dr. Simon of Medford is the likely man, since the elder Dr. Simon had died in 1747 and his son Simon was then about twenty.")}
<h3>William Tufts Jr. and Louisbourg, June 1771</h3>
{GAZ("June 17, 1771", "1771-06-17_3_845", 2, 3, "Mr. William Tufts, jun. an account of whose Death we mentioned the Third Instant, was the first Person that inlisted in the Massachusetts Service, in the Expedition against Louisbourg in 1745.")}
{UNV("Which William Tufts this was. He is not <a href='{P}profiles/william-tufts-40-2.html'>William Tufts Jr. (1736&ndash;1782)</a>, who was a child in 1745. The death notice of June 3, 1771 has not yet been found in these scans.")}
<h3>Cotton Tufts&rsquo;s mare, November 1771</h3>
{GAZ("November 25, 1771", "1771-11-25_3_868", 3, 4, "Stolen or Stray&rsquo;d &hellip; of October, from the Pasture of Cotton Tufts, Esq; in Weymouth, a black Mare &hellip; Whoever will bring or give information of the said Mare &hellip; shall be handsomely Rewarded, by Mr. John Bishop, of Medford, or Cotton Tufts, of Weymouth.")}
<p>The owner is <a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts</a> of Weymouth.</p>
<h3>Medford&rsquo;s representative, May 1772</h3>
{GAZ("June 1, 1772", "1772-06-01_4_895", 1, 2, "Medford, Simon Tufts, Esq.")}
<p>The entry is in the list of those who &ldquo;were returned to serve as Members of the Honorable House of Representatives&rdquo; when the General Court met at Cambridge in May 1772. This is good evidence that the &ldquo;Simon Tufts, Esq.&rdquo; to whom a town sent its instructions in the <em>Massachusetts Spy</em> of January 7, 1773 (above) was Medford&rsquo;s representative, <a href="{{P}}profiles/simon-tufts-11-1.html">Dr. Simon Tufts</a>.</p>
<h3>Executor of Thomas Seccombe, May 1773</h3>
{GAZ("May 24, 1773", "1773-05-24_4_946", 3, 4, "All Persons who have Demands on, or are indebted to the Estate of Thomas Seccombe, late of Medford, deceased, are desired to apply to Simon Tufts, Esq; an Executor, or to Jonathan Patten, Attorney to Mrs. Rebeccah Seccombe, Executrix of the said Will and Testament of the Deceased, for Settlement.")}
{UNV("That this executor is Dr. Simon Tufts of Medford. It is likely but not stated.")}
<h3>Estate of William Tufts of Charlestown, November 1773</h3>
{GAZ("November 29, 1773", "1773-11-29_4_973", 2, 3, "All Persons having Demands on the Estate of William Tufts, late of Charlestown, in the County of Middlesex, deceased, are desired to lodge their Accounts with the Subscriber; and those who are indebted to said Estate are requested to make immediate Payment to Nehemiah Rand, Administrator.")}
{UNV("Which William Tufts this was, and whether he is the Louisbourg volunteer of 1771 above. He is not Lieut. William Tufts (died 1783) or William Tufts Jr. (died 1782). The administrator&rsquo;s name is read from poor OCR.")}
<h3>Mary Tufts&rsquo;s horse, Medford, October 1774</h3>
{GAZ("October 17, 1774", "1774-10-17_4_1018", 0, 1, "TWO DOLLARS REWARD. Strayed or Stolen out of the Pasture of Mary Tufts, in Medford, a large dark bay Horse, about 11 Years old, 15 Hands high &hellip; Whoever will bring said Horse to me the Subscriber, shall have the above Reward, and all necessary Charges paid by MARY TUFTS.")}
<p>The notice ran again on <a href="{IA_G}1774-10-24_4_1019/page/n3">October 24, 1774</a> (p. 4).</p>
{UNV("Which Mary Tufts of Medford this was. No profile on this site matches yet.")}
<h3>Simon Tufts and the tea, March 1775</h3>
{GAZ("April 3, 1775", "1775-04-03_4_1042", 2, 3, "I have purchas&rsquo;d no Tea since the First of March &hellip; I had no Intention from the Beginning of militating with the Association of the Continental Congress, and declare I will not buy or sell any more of said Article till a general Permission therefor takes place. If by the above imprudent Step I have given any Offence to my Countrymen, am sorry therefor; and hope for a Restoration to their Favour and Confidence. &hellip; 20 March 1775. SIMON TUFTS.")}
<p>Below it, the declaration is sworn before Belcher Noyes, justice of the peace. Buying tea after March 1, 1775 broke the Continental Association&rsquo;s boycott, and this is his public apology. The merchant is probably the Simon Tufts who advertised from a store near Faneuil Hall in the <em>Massachusetts Spy</em> in 1774 (above).</p>
{UNV("Which Simon Tufts this was. He may be the <a href='{P}profiles/simon-tufts-29-1.html'>Loyalist Simon Tufts (1750&ndash;1801)</a>, but that is not confirmed. The place line at the foot is unreadable in the OCR.")}
<h3>Soldiers&rsquo; guns at Samuel Tufts&rsquo;s house, Medford, May 1776</h3>
{GAZ("May 9, 1776", "1776-05-09_4_1094", 3, 4, "A List of guns belonging to the following men, formerly soldiers in Col. John [Stark]&rsquo;s regiment, and left by the subscriber at Mr. Samuel Tufts&rsquo;s house in Medford. The owners may have them again by applying to said Tufts, paying him for his trouble of storage and advertising them.")}
<p>The notice, repeated on <a href="{IA_G}1776-05-16_4_1095/page/n3">May 16, 1776</a> (p. 4), lists guns by number and owner and is signed by a quartermaster.</p>
{UNV("The colonel&rsquo;s surname is garbled in both OCR texts and appears to read Stark; check the scan. Which Samuel Tufts kept the guns is not stated; candidates include <a href='{P}profiles/samuel-tufts-15-3.html'>Samuel Tufts (1732&ndash;1818)</a> and <a href='{P}profiles/samuel-tufts-41-2.html'>Samuel Tufts 2d (41-2)</a>.")}
<p><strong>Tufts association.</strong> Samuel Tufts of Medford was a trusted townsman during the war years. In 1776 the town sent &ldquo;Lieut. Moses Tufts and Samuel Tufts&rdquo; into Hampshire County and elsewhere, armed with £8 bounties, to hire the thirty men Medford owed for the Canada service; the recruits were sent on to Ticonderoga.</p>
<p class="cite">&ldquo;Medford in the War of the Revolution,&rdquo; <em>The Medford Historical Register</em>, vol. II, no. 1 (January 1899), p. 39. <a href="https://archive.org/details/medfordhistoricav1v2medf">Volume scan (Internet Archive)</a></p>
<h3>Crockery left with Samuel Tufts, Medford, 1775</h3>
<blockquote>&ldquo;Taken up in Medford some time after the Battle of Lexington, a basket of crockery ware which the owner may have again by enquiring of Mr. Samuel Tufts of Medford.&rdquo;</blockquote>
<p class="cite">Advertisement in the <em>New-England Chronicle</em>, as reprinted under &ldquo;Medford Incidents&rdquo; (noted by B. F. Fenton), <em>The Medford Historical Register</em>, vol. XIV, no. 2 (April 1911), p. 55. <a href="https://archive.org/details/medfordhistoricv13v16medf">Volume scan (Internet Archive)</a></p>
<p>Like the soldiers&rsquo; guns above, goods lost in the confusion of 1775&ndash;76 were left in Samuel Tufts&rsquo;s keeping. The same Register asked, in January 1911 (vol. XIV, p. 21), &ldquo;Where in 1775 did Mr. Samuel Tufts live?&rdquo;, so his house site was not settled even then.</p>
{UNV("The Register prints the date as &ldquo;September 21&ndash;28, 1773,&rdquo; which cannot be right for an advertisement written after Lexington (April 1775); the original <em>New-England Chronicle</em> issue has not been checked. Which Samuel Tufts this was, and where his house stood, is not yet established.")}
</section>'''
SIMON11_GAZ = '{DIV}<section id="gazette"><h2>In the Newspapers</h2><p><em>The Boston Gazette</em> of September 3, 1770 lists &ldquo;Simon Tufts, Esq; to be a Justice of the Peace for the County of Middlesex,&rdquo; and its issue of June 1, 1772 (p. 2) names &ldquo;Medford, Simon Tufts, Esq.&rdquo; among the members returned to the House of Representatives. In May 1773 a Simon Tufts, Esq. was executor of Thomas Seccombe of Medford (p. 4). See <a href="{P}collections.html#boston-gazette">Collections</a>.</p>' + UNV("None of these notices gives his dates; the match to this Dr. Simon is by elimination.") + '</section>'
GZP = {"profiles/cotton-tufts.html": '<p>In November 1771 <em>The Boston Gazette</em> (p. 4) advertised a black mare stolen or strayed &ldquo;from the Pasture of Cotton Tufts, Esq; in Weymouth.&rdquo;</p>',
       "profiles/simon-tufts-29-1.html": '<p><em>The Boston Gazette</em> lists a Simon Tufts among the Harvard masters of arts in July 1770, and on April 3, 1775 printed a Simon Tufts&rsquo;s sworn apology for buying tea in breach of the Continental Association. Whether either is this man is Unverified.</p>',
       "profiles/samuel-tufts-15-3.html": '<p>In May 1776 <em>The Boston Gazette</em> (p. 4) advertised soldiers&rsquo; guns left &ldquo;at Mr. Samuel Tufts&rsquo;s house in Medford.&rdquo; Which Samuel Tufts this was is Unverified.</p>',
       "profiles/samuel-tufts-41-2.html": '<p>In May 1776 <em>The Boston Gazette</em> (p. 4) advertised soldiers&rsquo; guns left &ldquo;at Mr. Samuel Tufts&rsquo;s house in Medford.&rdquo; Which Samuel Tufts this was is Unverified.</p>'}
_EXTRA_GZ = EXTRA
def EXTRA(path):
    out = _EXTRA_GZ(path)
    if path == "collections.html": out = out.replace("{DIV}" + NEWS, "{DIV}" + NEWS + "{DIV}" + GAZSEC, 1) if NEWS in out else out + "{DIV}" + GAZSEC
    if path == "profiles/simon-tufts-11-1.html": out += SIMON11_GAZ
    if path in GZP: out += '{DIV}<section id="gazette"><h2>In the Newspapers</h2>' + GZP[path] + '<p>See <a href="{P}collections.html#boston-gazette">Collections</a>.</p></section>'
    return out
