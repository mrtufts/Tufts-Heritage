# 1766 Newburyport notice by Samuel Tufts (eBay item 237179159588).
# Photographs of a manuscript dated 11 July 1766; which Samuel Tufts wrote it is not established.
_EBAY_1766 = "https://www.ebay.com/itm/237179159588"
_SN_FRONT = "samuel-tufts-newburyport-1766-front.jpg"
_SN_BACK = "samuel-tufts-newburyport-1766-back.jpg"
IMAGES[_SN_FRONT] = (
    "Samuel Tufts&rsquo;s notice to the Newburyport selectmen, 11 July 1766 (front)",
    "Handwritten note on laid paper, about 6&frac14; by 8 inches, in which Samuel Tufts notifies the selectmen of Newburyport that on 7 July 1766 he took into his family Samuel Resnick, aged about eight, son of Isaac Resnick, late of Newbury, deceased. Signed &ldquo;Saml Tufts.&rdquo;",
    "Antique Cottage Collectibles (eBay listing)",
    "Photograph of a 1766 manuscript; used with credit to the listing",
    _EBAY_1766, "eBay listing")
IMAGES[_SN_BACK] = (
    "Samuel Tufts&rsquo;s notice to the Newburyport selectmen, 11 July 1766 (back)",
    "The reverse of the same note, docketed &ldquo;Notification from S Tufts.&rdquo;",
    "Antique Cottage Collectibles (eBay listing)",
    "Photograph of a 1766 manuscript; used with credit to the listing",
    _EBAY_1766, "eBay listing")
# Append credits only; do not rebuild the list (later tools have already set the wording).
_sn_cred = "".join(
    f'<li><a href="{{P}}assets/images/{f}">{IMAGES[f][0]}</a>. {IMAGES[f][2]}. {IMAGES[f][3]}. <a href="{IMAGES[f][4]}">{IMAGES[f][5]} page</a></li>'
    for f in (_SN_FRONT, _SN_BACK))
if _SN_FRONT not in CREDITS:
    CREDITS = CREDITS.replace("</ul></section>", _sn_cred + "</ul></section>", 1)
_SN_CREDIT = f'<a href="{_EBAY_1766}">Photo: eBay listing by Antique Cottage Collectibles</a>'
_SN_FIG = (
    f'<figure class="hfig hfig-pair"><div class="pair-imgs">'
    f'<a href="{{P}}assets/images/{_SN_FRONT}"><img src="{{P}}assets/images/{_SN_FRONT}" alt="Front of a 1766 handwritten notice from Samuel Tufts to the Newburyport selectmen" loading="lazy"></a>'
    f'<a href="{{P}}assets/images/{_SN_BACK}"><img src="{{P}}assets/images/{_SN_BACK}" alt="Back of the 1766 Samuel Tufts notice, docketed Notification from S Tufts" loading="lazy"></a>'
    f'</div><figcaption><strong>Samuel Tufts&rsquo;s notice to the Newburyport selectmen, July 1766.</strong> Front and back of the manuscript, about 6&frac14; by 8 inches, on laid paper.'
    f'<span class="credit">{_SN_CREDIT}</span></figcaption></figure>')
_SN_TRANS = (
    "Gentlemen / This is to Notify you that I / Have this Seventh day of July 1766 taken / "
    "into my family to live with me Saml / Resnick aged about Eight years old &mdash; / "
    "son of Isaac Resnick Late of Newby / Deceasd &mdash; Dated this 11th day of July &mdash; / "
    "1766 &mdash; Saml Tufts / To / The Gentlemen / Select men / for the Town / of Newbury Port")
_SN_SEC = (
    '<section id="newburyport-1766"><h2>A Notice to the Newburyport Selectmen, 1766</h2>'
    + _SN_FIG
    + "<p>A short handwritten note on laid paper, about 6&frac14; by 8 inches, was addressed to the selectmen of Newburyport in July 1766. In it Samuel Tufts tells them that on July 7 he had taken into his family Samuel Resnick, aged about eight, the son of Isaac Resnick, late of Newbury, deceased. The note is dated July 11, 1766, and signed &ldquo;Saml Tufts.&rdquo; The back is docketed &ldquo;Notification from S Tufts.&rdquo;</p>"
    + "<p>The paper reads as a town notice of a child taken into a household, of a kind consistent with colonial Massachusetts poor-law practice, by which a town was informed when a child was received into a family. That reading is offered with caution; the note itself does not name the legal arrangement.</p>"
    + "<p>A later commercial description of the manuscript gave the month as February, but the handwriting reads July, which is followed here.</p>"
    + f'<blockquote class="transcription">{_SN_TRANS}</blockquote>'
    + f'<p class="cite">Transcription from the photographs of the manuscript, with the original line breaks marked by slashes. The photographs are from eBay item 237179159588, listed by Antique Cottage Collectibles; the listing ended November 17, 2026, with no bids. <a href="{_EBAY_1766}">eBay listing</a></p>'
    + UNV("Which Samuel Tufts wrote this notice is not established. No Samuel Tufts of Newburyport is known on this site, and the name is not attached here to any of the men already profiled. Note: Pending further work.")
    + "</section>")
_page_sn1766 = page
def page(path, title, kicker, h1, sub, body, *a, **k):
    if path == "profiles/samuel-tufts.html" and 'id="newburyport-1766"' not in body:
        needle = '<p><a href="{P}people.html">'
        insert = "{DIV}" + _SN_SEC
        body = body.replace(needle, insert + needle, 1) if needle in body else body + insert
    return _page_sn1766(path, title, kicker, h1, sub, body, *a, **k)
