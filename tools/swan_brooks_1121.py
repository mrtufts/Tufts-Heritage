# Daily research run 2026-11-21: Margaret "Peggy" Tufts Swan and her "Peggy Tufts on it" china (MHR XLIII, 1940, pp. 26-28),
# and Nathan Tufts's sale of the "Tufts farm" to Peter Chardon Brooks (MHR XLII no. 2, June 1939, pp. 36-37).
# Sources: "Captain Samuel Swan, 3rd, of Medford," MHR XLIII (June-Dec. 1940) pp. 25-28 (IA medfordhistorica12medf n310-n311);
# "The Brooks Family of Medford," MHR XLII no. 2 (June 1939) pp. 36-37 (n185, n188); Brooks, History of Medford (1855), p. 551.
_MS = "margaret-tufts-swan-1779"
_S27 = "https://archive.org/details/medfordhistorica12medf/page/n310/mode/1up"
_B36 = "https://archive.org/details/medfordhistorica12medf/page/n185/mode/1up"
_B37 = "https://archive.org/details/medfordhistorica12medf/page/n188/mode/1up"
_SSRC = '&ldquo;Captain Samuel Swan, 3rd, of Medford,&rdquo; <em>Medford Historical Register</em> XLIII (June&ndash;December 1940), p. 27. <a href="' + _S27 + '">View the page scan</a>'
_BSRC = lambda pg, u: '&ldquo;The Brooks Family of Medford,&rdquo; <em>Medford Historical Register</em> XLII, no. 2 (June 1939), p. ' + pg + '. <a href="' + u + '">View the page scan</a>'
_BRK = 'Charles Brooks, <em>History of the Town of Medford</em> (1855), p. 551. <a href="https://archive.org/details/historyoftownofm1855broo/page/551/mode/1up">Page scan (Internet Archive)</a>'
_MHRS3 = "Medford Historical Society, <em>Medford Historical Register</em>, via Internet Archive"
IMAGES["mhr-xliii-peggy-tufts-china.jpg"] = ("Clipping: &ldquo;Peggy Tufts on it&rdquo;",
  "Detail of p. 27, <em>Medford Historical Register</em> XLIII (1940), &ldquo;Captain Samuel Swan, 3rd, of Medford&rdquo;: Peggy Tufts&rsquo;s marriage and the story of her china.",
  _MHRS3, "Shown for non-commercial historical use", _S27, "Internet Archive (full page)")
IMAGES["mhr-xlii-brooks-tufts-farm-36.jpg"] = ("Clipping: the &ldquo;Tufts farm&rdquo; bought of Nathan Tufts",
  "Detail of p. 36, <em>Medford Historical Register</em> XLII, no. 2 (June 1939), &ldquo;The Brooks Family of Medford.&rdquo;",
  _MHRS3, "Shown for non-commercial historical use", _B36, "Internet Archive (full page)")
IMAGES["mhr-xlii-brooks-tufts-farm-37.jpg"] = ("Clipping: the bounds of the &ldquo;Tufts farm&rdquo;",
  "Detail of p. 37, <em>Medford Historical Register</em> XLII, no. 2 (June 1939): the farm lay south of High Street to the Mystic River and Harvard Avenue.",
  _MHRS3, "Shown for non-commercial historical use", _B37, "Internet Archive (full page)")
_QP = ("The Captain married Peggy (Margaret) Tufts in 1809. Their children were: Benjamin L., who married Sarah Brinkerhoff; Samuel, who married Lucretia Staniels; James, who married Matilda Loring; Margaret, who married William Eveleth, and Hannah L., who married George Francis. "
  "There is a family tradition that when the Captain was courting Peggy, he said: &ldquo;Peggy, my dear, when I come back from this trip I want to give you, as a personal wedding gift, something that you would like. Will you please tell me what you wish?&rdquo; To which Peggy replied: &ldquo;Sam, I can think of nothing better than a set of china for my bedroom.&rdquo; "
  "The Captain asked Peggy what she would like to have put on the china, and her answer was: &ldquo;Oh, put Peggy Tufts on it!&rdquo; When he arrived in the Orient, the Captain gave his directions to one of the china dealers. The literal Chinaman did as he was told to do and, in substantiation of this, one of our treasured possessions is a carafe, on the bottom of which are the words: &ldquo;Peggy Tufts on it.&rdquo;")
_nf_new(_MS, "Margaret &ldquo;Peggy&rdquo; (Tufts) Swan (b. 1779)", "1779 &ndash; date not yet found", "Medford, Mass.", "1779", "", "19th Century",
  "Daughter of Samuel Tufts 2nd and Margaret (Hodgkins) Tufts; wife of Capt. Samuel Swan of Medford",
  '<p>Margaret Tufts, called Peggy, was born in 1779, the daughter of ' + PL("samuel-tufts-41-2", "Samuel Tufts 2nd (1752&ndash;1815)") + ' and Margaret (Hodgkins) Tufts. Brooks lists her in his register of Medford families: &ldquo;Margaret, b. 1779; m. Samuel Swan, jun.&rdquo; (' + _BRK + ').</p>'
  + '<p>Her husband was a Medford sea captain in the African and East India trade. In 1940 the Medford Historical Society printed a family account of him, contributed by his descendants, which tells how Peggy came by a set of china bearing her own name:</p>'
  + FIG("mhr-xliii-peggy-tufts-china.jpg", "hfig-flow mi-inline")
  + Q(_QP, _SSRC)
  + '<p>The carafe was then kept by the Captain&rsquo;s descendants, the Yardley family of East Orange, New Jersey; its present location is not known. The same account says Captain Swan was &ldquo;supposed to have been lost at sea the early part of 1823. Vessel and company never heard from,&rdquo; and that his widow kept a light burning and the door unlocked every night in the old Swan home west of the First Parish Church, where George Washington is said to have stopped (p. 28). Their granddaughter, Mrs. Charles Burleigh Yardley, was born Margaret Tufts Swan.</p>',
  '<p>No military service is recorded for her. Her father, Samuel Tufts 2nd, was of the Revolutionary generation.</p>',
  '<p>Father: ' + PL("samuel-tufts-41-2", "Samuel Tufts 2nd (1752&ndash;1815)") + '. Mother: Margaret (Hodgkins) Tufts (d. 7 August 1793). Brother: Samuel (1784&ndash;1821) (' + _BRK + '). Children: Benjamin L., Samuel, James, Margaret (Mrs. William Eveleth) and Hannah L. (Mrs. George Francis) Swan (' + _SSRC + ').</p>',
  "<strong>Husband&rsquo;s name:</strong> Brooks calls him Samuel Swan, jun.; the 1940 account calls him Captain Samuel Swan, 3rd. They appear to be the same man, but this is Unverified. <strong>The china:</strong> the story is a family tradition; the carafe is not known to survive in a public collection. <strong>Her death date</strong> has not yet been found. Note: Pending further work.",
  "<ul><li><strong>Capt. Samuel Swan</strong> (&ldquo;jun.&rdquo; in Brooks, &ldquo;3rd&rdquo; in the 1940 account), Medford sea captain; married 1809; lost at sea, early 1823 (" + _SSRC + ").</li></ul>",
  [("samuel-tufts-41-2", "father Samuel Tufts 2nd (1752&ndash;1815)", "daughter Margaret &ldquo;Peggy&rdquo; (Tufts) Swan (b. 1779)")])
_QF36 = "&hellip;also a large tract of land lying east of the railroad called the &ldquo;Clewly&rdquo; land, which he bought from the heirs of John Clewly of Halifax. He also bought of Nathan Tufts the &ldquo;Tufts farm,&rdquo; so called,"
_QF37 = "lying south of High Street, including all the land between that street and the Mystic River and Harvard Avenue, and somewhat more lying south of the latter. This property was intersected by the Middlesex Canal, the land of which forms Boston Avenue."
_FARM = ('<section id="tufts-farm-brooks"><h2>The &ldquo;Tufts Farm&rdquo; Sold to Peter Chardon Brooks</h2>'
  + '<p>A 1939 history of the Brooks family records that Peter Chardon Brooks (1767&ndash;1849), the Boston merchant whose Medford estate on Grove and High Streets was one of the handsomest near Boston, enlarged it by buying the &ldquo;Tufts farm&rdquo; from a Nathan Tufts:</p>'
  + FIG("mhr-xlii-brooks-tufts-farm-36.jpg", "hfig-flow mi-inline")
  + Q(_QF36, _BSRC("36", _B36))
  + FIG("mhr-xlii-brooks-tufts-farm-37.jpg", "hfig-flow mi-inline")
  + Q(_QF37, _BSRC("37", _B37))
  + UNV("The account does not say which Nathan Tufts sold the farm or in what year. Nathan Tufts the cordwainer, who farmed chiefly in Medford, and his son Nathan Tufts of Charlestown (c. 1764&ndash;1835) are the likeliest candidates. A Middlesex deed search for a Nathan Tufts to Peter C. Brooks conveyance would settle it. Note: Pending further work.")
  + '</section>')
for _s in ("nathan-tufts-1764", "nathan-tufts-cordwainer"):
    _up_add(_s, _FARM, 'id="tufts-farm-brooks"')
_up_add("samuel-tufts-41-2", '<p>Daughter: ' + PL(_MS, "Margaret &ldquo;Peggy&rdquo; (Tufts) Swan (b. 1779)") + ', wife of Capt. Samuel Swan, whose &ldquo;Peggy Tufts on it&rdquo; china is told on her page.</p>', _MS, "family")
print("swan_brooks_1121 done; profiles", len(PROFILES))
