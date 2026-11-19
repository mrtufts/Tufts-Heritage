# Daily research run 2026-11-19: Turell Tufts (1770-1842) in Surinam, his return to Medford, the 1832 agent's letter,
# his portrait at the Medford Historical Society, and the 1839 Medford tax list.
# Sources: Coolidge, MHR XLI no. 4 (Dec. 1938) pp. 62-63; Hervey (ed.), "The Medford Town Report of 1839," MHR XLII no. 1 (Mar. 1939) pp. 1-2;
# Gill, MHR XVIII (1915) p. 56 (portrait on the Society's wall); MHR III, Royall House loan exhibition (portrait shown).
_TT = "turell-tufts"
_TT62 = "https://archive.org/details/medfordhistorica12medf/page/n109/mode/1up"
_TT63 = "https://archive.org/details/medfordhistorica12medf/page/n110/mode/1up"
_TR39 = "https://archive.org/details/medfordhistorica12medf/page/n129/mode/1up"
_CDEC = S3_SRC.replace("no. 3 (September 1938)", "no. 4 (December 1938)")
_HRV = 'Wade S. Hervey, ed., &ldquo;The Medford Town Report of 1839,&rdquo; <em>Medford Historical Register</em> XLII, no. 1 (March 1939), pp. 1&ndash;2'
_ROY = "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2005.05.0002%3Achapter%3D10"
_GILL16 = "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2005.05.0018%3Achapter%3D16"
_MHR = "Medford Historical Society, <em>Medford Historical Register</em>"
IMAGES["mhr-xli-turell-surinam-letter-1808-clip.jpg"] = ("Clipping: Turell Tufts&rsquo;s letter from Surinam, 20 November 1808",
  "Detail of p. 62, <em>Medford Historical Register</em> XLI, no. 4 (December 1938): Turell Tufts to his cousin Dudley Hall, from Surinam, with a postscript on the Embargo.",
  _MHR + " XLI (1938), via Internet Archive", "Shown for non-commercial historical use", _TT62, "Internet Archive (full page)")
IMAGES["mhr-xli-turell-returns-medford-clip.jpg"] = ("Clipping: Turell Tufts leaves Surinam for Medford",
  "Detail of p. 63, <em>Medford Historical Register</em> XLI, no. 4 (December 1938): the agent&rsquo;s letter of 1832 and the Medford Tufts Library.",
  _MHR + " XLI (1938), via Internet Archive", "Shown for non-commercial historical use", _TT63, "Internet Archive (full page)")
IMAGES["mhr-xli-turell-portrait-blue-eyes-clip.jpg"] = ("Clipping: the portrait of Turell Tufts",
  "Detail of p. 63, <em>Medford Historical Register</em> XLI, no. 4 (December 1938): &ldquo;The Historical Society has his portrait.&rdquo;",
  _MHR + " XLI (1938), via Internet Archive", "Shown for non-commercial historical use", _TT63, "Internet Archive (full page)")
IMAGES["mhr-xlii-1839-taxpayers-turell-clip.jpg"] = ("Clipping: Turell Tufts among Medford&rsquo;s leading taxpayers, 1839",
  "Detail of p. 2, <em>Medford Historical Register</em> XLII, no. 1 (March 1939), &ldquo;The Medford Town Report of 1839.&rdquo;",
  _MHR + " XLII (1939), via Internet Archive", "Shown for non-commercial historical use", _TR39, "Internet Archive (full page)")
_LET = ("Surinam 20 Nov. 1808. My dear Cousin, I thank you for your Letter in answer to mine to your mother. Tho&rsquo; it contains subjects for grief and serious reflections, I am gratified in seeing the hand writing &amp; the thoughts of a relation, whose countenance &amp; manners, most probably, I should not now recognise. "
  "The length of time I have been banished as it were from my country, upon reviewing it, makes me think that I am growing old: and I am told that my native Town, and the surrounding country are so much improved that I should as little recollect the Scenes of my youthful life as the countenances of those who now inhabit them. &hellip; "
  "P.S. The Embargo had an immediate effect of making most articles scarce &amp; dear in this Colony. From indirect Sources however, we have been supplied, and tho&rsquo; much groaning &amp; murmuring is made at prices, most things are now to be had and prices are falling. &hellip; When the Embargo is raised it will be hazardous to send cargoes to these Regions, such will be the glut &amp; consequent loss to adventurers. &hellip; Dec 10. 1808. This Vessel has been detained unexpectedly. No American Vessel remains!")
_RET = ("At some time during the following years Turell Tufts evidently abandoned Surinam and returned to Medford. Perhaps he feared the fate of his brother Hall, whose death in Surinam is noted on the tombstone. The business was entrusted to an agent and occasioned much correspondence. "
  "On December 8, 1832, an agent named Nash sent a letter by the brig <em>Sarah Ann</em>, a letter postmarked in Gloucester, December 31, an indication of the length of the passage. There had been a fire and Nash had a chance to settle things up. "
  "We do not know how successful Turell was in business, but on his death, in 1842, he left a fund of $500.00 to the town to be used for the purchase of valuable books for the Medford Social Library. So munificent was the gift regarded that the name was changed from Medford Social Library to Medford Tufts Library, in honor of Turell Tufts. The name, however, was eventually changed, by vote of the town, to Medford Public Library.")
_POR = "Turell returned from Surinam to live and die in Medford. The Historical Society has his portrait, a shrewd, kindly face, with clear blue eyes."
_TAX = "&hellip; Dudley Hall &hellip; the Medford Distillery, Turell Tufts, Peter Brooks, and the Osgood sisters. As these taxes were for more than one hundred dollars and up to over five hundred, as in the case of Thatcher Magoun &hellip;"
_TT_ADD = ('<section id="surinam-years"><h2>The Surinam Years and the Return to Medford</h2>'
  + FIG("mhr-xli-turell-surinam-letter-1808-clip.jpg", "hfig-flow mi-inline")
  + '<p>Turell Tufts spent long years at Surinam, the Dutch colony on the north coast of South America where his brother ' + PL("hall-tufts-1775", "Hall Tufts") + ' had died in 1801. A letter he wrote from there in November 1808 to his kinsman Dudley Hall, whom he addresses as &ldquo;Cousin&rdquo; and whose mother had written to him, was copied into the Hall family papers of the Medford Historical Society and printed by Ruth Dame Coolidge in 1938. He wrote of feeling &ldquo;banished&rdquo; from home and longing to see Medford again, and he added a merchant&rsquo;s postscript on the Embargo of 1807, which had cut off American shipping to the colony:</p>'
  + Q(_LET, _CDEC + ', p. 62. <a href="' + _TT62 + '">View the page scan</a>')
  + FIG("mhr-xli-turell-returns-medford-clip.jpg", "hfig-flow mi-inline")
  + '<p>He later gave up living in Surinam and came home, leaving the business to an agent. Coolidge found a letter from that agent, a man named Nash, dated December 8, 1832, reporting a fire. She also connects Turell&rsquo;s $500 bequest to the Medford Social Library with the library&rsquo;s renaming in his honor:</p>'
  + Q(_RET, _CDEC + ', p. 63. <a href="' + _TT63 + '">View the page scan</a>')
  + '<p>Three years before his death, the printed town report of 1839 still listed him among Medford&rsquo;s larger taxpayers, those assessed more than one hundred dollars, alongside Dudley Hall and the Medford Distillery:</p>'
  + FIG("mhr-xlii-1839-taxpayers-turell-clip.jpg", "hfig-flow mi-inline")
  + Q(_TAX, _HRV + '. <a href="' + _TR39 + '">View the page scan</a>')
  + '<p>His own amount is not given in the Register&rsquo;s summary. Note: Pending further work.</p>'
  + '</section>'
  + '<section id="turell-tufts-portrait"><h2>His Portrait</h2>'
  + FIG("mhr-xli-turell-portrait-blue-eyes-clip.jpg", "hfig-flow mi-inline")
  + '<p>A portrait of Turell Tufts belonged to the Medford Historical Society. It was shown at the Society&rsquo;s Royall House loan exhibition (<a href="' + _ROY + '"><em>Medford Historical Register</em> III, &ldquo;The Royall House Loan Exhibition,&rdquo; text on Perseus</a>), and Eliza M. Gill wrote in 1915 that it hung on the Society&rsquo;s library wall, the gift of Dudley C. Hall (<a href="' + _GILL16 + '"><em>Medford Historical Register</em> XVIII, text on Perseus</a>). Coolidge described it in 1938:</p>'
  + Q(_POR, _CDEC + ', p. 63. <a href="' + _TT63 + '">View the page scan</a>')
  + '<p>See also <a href="{P}collections.html#turell-tufts-portrait">Collections: Portrait of Turell Tufts</a>.</p>'
  + UNV("The painter, date and present whereabouts of the portrait are not stated in these sources, and no published photograph of it has been found. Note: Pending further work.")
  + '</section>')
for _p in PROFILES:
    if _p["slug"] == _TT and 'id="surinam-years"' not in _p["bio"]:
        _p["bio"] = _p["bio"] + _TT_ADD
for _p in PROFILES:
    if _p["slug"] == "hall-tufts-1775" and "surinam-years" not in _p["bio"]:
        _p["bio"] = _p["bio"] + '<p>Turell&rsquo;s own letter from Surinam in 1808, his return to Medford, and the agent who later managed the business there are described on <a href="{P}profiles/turell-tufts.html#surinam-years">his profile</a>.</p>'
NF_EXTRA.setdefault("collections.html", []).append(
  '{DIV}<section id="turell-tufts-portrait"><h2>Portrait of Turell Tufts</h2>'
  + FIG("mhr-xli-turell-portrait-blue-eyes-clip.jpg", "hfig-flow mi-inline")
  + '<p><strong>Tufts association:</strong> a portrait of ' + PL(_TT, "Turell Tufts (1770&ndash;1842)") + ', merchant in the Surinam trade, Medford selectman and benefactor of the Medford Social Library, son of ' + PL("simon-tufts-11-1", "Dr. Simon Tufts") + '. It was lent to the Royall House loan exhibition, given to the Medford Historical Society by Dudley C. Hall, and hung on the Society&rsquo;s library wall in 1915 (<a href="' + _GILL16 + '">MHR XVIII, Perseus</a>; <a href="' + _ROY + '">MHR III, Perseus</a>).</p>'
  + Q(_POR, _CDEC + ', p. 63. <a href="' + _TT63 + '">View the page scan</a>')
  + UNV("Painter, date, and present location not confirmed; no image of the portrait has been found online. Note: Pending further work.")
  + '</section>')
