# Daily research run 2026-11-18: Hall Tufts (1775-1801), 4th son of Dr. Simon Tufts; died at Surinam.
# Sources: Brooks, History of Medford (1855), p. 546 (genealogy) and p. 301 (Harvard graduates);
# Coolidge, MHR XLI no. 3 (1938), p. 33 (tomb) and pp. 61-62 (Hall and Turell in the Surinam trade).
_HT = "hall-tufts-1775"
_BRK_IA = "https://archive.org/details/historyoftownofm1855broo/page/546/mode/1up"
_BR546 = 'Charles Brooks, <em>History of the Town of Medford</em> (1855), p. 546. <a href="' + _BRK_IA + '">Page scan (Internet Archive)</a>'
_HT_IA = "https://archive.org/details/medfordhistorica12medf/page/n108/mode/1up"
IMAGES["mhr-xli-hall-turell-surinam-clip.jpg"] = ("Clipping: Hall and Turell Tufts in the Surinam trade",
  "Detail of pp. 61&ndash;62, <em>Medford Historical Register</em> XLI, no. 4 (December 1938), from Coolidge&rsquo;s &ldquo;Simon Tufts the Third, Merchant of India.&rdquo;",
  "Medford Historical Society, <em>Medford Historical Register</em> XLI (1938), via Internet Archive", "Shown for non-commercial historical use", _HT_IA, "Internet Archive (full page)")
_HT_CLIP = ("The letters copied in the Hall collection from Turell Tufts do not present so close a sequence. Hall and Turell Tufts evidently continued the family tradition in overseas business by commerce with Surinam in Dutch Guiana. "
  "Turell wrote a letter from Surinam in 1808 to Mistress Lucy Hall on the death of her husband. Later he had letters, while dwelling in Medford, from solicitors in Surinam. Hall, his older brother, had died there in 1801, and perhaps Turell followed to clear up the business or continue it.")
PROFILES.append(dict(slug=_HT, name="Hall Tufts (1775&ndash;1801)", dates="1775&ndash;19 July 1801", town="Medford, Mass.; died at Surinam", born="1775", died="1801", era="Early Republic",
  line="Fourth son of Dr. Simon Tufts (1727&ndash;1786) and Elizabeth (Hall) Tufts; Harvard 1794; merchant in the Surinam trade",
  bio=('<p>Hall Tufts was born in Medford in 1775, a son of ' + PL("simon-tufts-11-1", "Dr. Simon Tufts") + ' by his second wife, Elizabeth Hall, whom the doctor married on October 5, 1769. His first name was his mother&rsquo;s family name. Brooks lists him among the doctor&rsquo;s children and records that he died at Surinam on July 19, 1801.</p>'
    + Q("87 Hall, &bdquo; 1775 ; d. at Surinam, July 19, 1801.", _BR546)
    + '<p>Brooks also names Hall Tufts among Medford&rsquo;s graduates of Harvard College, in the class of 1794 (Brooks, p. 301). The family tomb gives him the degree &ldquo;A. M.&rdquo;</p>'
    + FIG("mhr-xli-hall-turell-surinam-clip.jpg", "hfig-flow mi-inline")
    + '<p>Like his half-brother ' + PL("simon-tufts-29-1", "Simon Tufts, the &ldquo;Merchant of India&rdquo;") + ', Hall went abroad in trade. Ruth Dame Coolidge, working from the Hall family papers of the Medford Historical Society, found that he and his brother ' + PL("turell-tufts", "Turell Tufts") + ' carried on business with Surinam, the Dutch colony on the north coast of South America, and that Turell may have gone out there after Hall&rsquo;s death to settle or continue the business:</p>'
    + Q(_HT_CLIP, S3_SRC.replace("no. 3 (September 1938)", "no. 4 (December 1938)") + ', pp. 61&ndash;62. <a href="' + _HT_IA + '">View the page scan</a>')
    + '<p>Turell Tufts was later named United States consul at Surinam (see his profile). Hall died there at twenty-six, and he is remembered on the family tomb in the Salem Street burying ground in Medford:</p>'
    + FIG("mhr-xli-simon-tufts-family-tomb-clip.jpg", "hfig-flow mi-inline")
    + Q("Hall Tufts A. M. 4th son at Surinam, 19 July 1801 Aged 26 y&rsquo;s.", S3_SRC + ', p. 33. <a href="' + S3_IA + '">View the page scan</a>')
    + '<p>The house he grew up in is shown on the page of ' + PL("simon-tufts-29-1", "his half-brother Simon") + ' and on <a href="{P}places.html#homesteads">Places: Homesteads</a>.</p>'),
  service='<p>Born in 1775, he was a child during the Revolution. No military or civil service is recorded for him.</p>',
  family=('<p>Father: ' + PL("simon-tufts-11-1", "Dr. Simon Tufts (1727&ndash;1786)") + '. Mother: Elizabeth (Hall) Tufts, who died August 30, 1830, aged 87. Grandfather: ' + PL("simon-tufts-1700", "Dr. Simon Tufts (1700&ndash;1747)") + '. Half-brother: ' + PL("simon-tufts-29-1", "Simon Tufts (1750&ndash;1801/2)") + '; half-sisters Lucy (Mrs. Benjamin Hall, Jr.) and Catharine. Full siblings, per Brooks: ' + PL("turell-tufts", "Turell (1770&ndash;1842)") + ', Cotton (1772&ndash;1835), Hepzibah (born 1777, married Benjamin Hall), and Stephen (born 1779) (' + _BR546 + ').</p>'),
  unverified=('<strong>Birth order:</strong> Coolidge calls Hall Turell&rsquo;s &ldquo;older brother,&rdquo; but Brooks gives Turell&rsquo;s birth as 1770 and Hall&rsquo;s as 1775, and the tomb calls Hall the fourth son, which fits Brooks. Brooks is followed here. <strong>Exact birth date</strong> and <strong>place of burial</strong> (at Surinam or brought home) are not recorded in these sources. <strong>Harvard degree:</strong> the class year 1794 is from Brooks&rsquo;s list; it has not yet been checked against the Harvard <em>Quinquennial Catalogue</em>. Note: Pending further work.')))
SP[_HT] = "<p>No marriage is recorded for him by Brooks or Coolidge.</p>"
NEWUNCHK.add(_HT)
REL[_HT] = [("simon-tufts-11-1", "father Dr. Simon Tufts (1727&ndash;1786)"), ("simon-tufts-1700", "grandfather Dr. Simon Tufts (1700&ndash;1747)"), ("simon-tufts-29-1", "half-brother Simon Tufts (1750&ndash;1801/2)"), ("turell-tufts", "brother Turell Tufts (1770&ndash;1842)")]
for _s, _r in [("simon-tufts-11-1", [(_HT, "son Hall Tufts (1775&ndash;1801)")]), ("simon-tufts-1700", [(_HT, "grandson Hall Tufts (1775&ndash;1801)")]),
               ("simon-tufts-29-1", [(_HT, "half-brother Hall Tufts (1775&ndash;1801)")]), ("turell-tufts", [(_HT, "brother Hall Tufts (1775&ndash;1801)")])]:
    REL.setdefault(_s, []); REL[_s] = REL[_s] + _r
for _p in PROFILES:
    if _p["slug"] == "turell-tufts" and "mhr-xli-hall-turell-surinam-clip" not in _p["bio"]:
        _p["bio"] = _p["bio"] + FIG("mhr-xli-hall-turell-surinam-clip.jpg", "hfig-flow mi-inline") + '<p>Coolidge, working from the Hall family papers, found that Turell and his brother ' + PL(_HT, "Hall Tufts") + ' carried on trade with Surinam; Hall died there on July 19, 1801, and Turell wrote from Surinam in 1808 to Lucy Hall on the death of her husband.' + S3_C("no. 4, pp. 61&ndash;62") + '</p>'

