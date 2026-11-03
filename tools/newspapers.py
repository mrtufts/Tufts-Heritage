# Massachusetts Spy mentions (Digital Commonwealth full-text search, 2026-11-03). OCR quoted with obvious long-s fixes only.
DCS = "https://www.digitalcommonwealth.org/search/commonwealth:"
def SPY(date, iid, pg, col, txt):
    return Q(txt, f'<em>The Massachusetts Spy</em> (Boston), {date}, p. {pg}, col. {col} (column approximate, from OCR position). <a href="{DCS}{iid}">Issue scan (Digital Commonwealth)</a>')
NEWS = f'''<section id="newspapers"><h2>In the Newspapers: <em>The Massachusetts Spy</em></h2>
<p>Isaiah Thomas&rsquo;s <em>Massachusetts Spy</em>, printed in Boston until April 1775, is the paper sometimes called the &ldquo;Boston Spy.&rdquo; A full-text search of its digitized issues finds a Simon Tufts in three kinds of notice. The quotations come from the OCR text, with the long s and obvious misreadings corrected. Each should be checked against the linked scan.</p>
<h3>Instructions to the representative, January 1773</h3>
{SPY("January 7, 1773", "n2971p92q", 3, 1, "To Simon Tufts, Esq.")}<p>The heading above, garbled in the OCR, appears to read &ldquo;Instructions to their Representative.&rdquo; Check the scan.</p>
<p>The notice prints a town&rsquo;s instructions to its representative to back constitutional measures in the House of Representatives to redress the province&rsquo;s grievances, part of the town replies to Boston&rsquo;s Committee of Correspondence.</p>
{UNV("The town and which Simon Tufts. The OCR text shown does not name the town. Medford&rsquo;s Dr. Simon Tufts (1727&ndash;1786), son of the Dr. Simon who died in 1747, is a likely candidate, but this has not been confirmed from the House journals.")}
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
