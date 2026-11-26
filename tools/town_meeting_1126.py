# Daily research run 2026-11-26: "The Old Time Medford Town Meeting" (MHR XXXIV, 1931): Peter Tufts as moderator and selectman,
# the Peter Tufts (Cradock) house household, Mercy (Cotton) Tufts, and the 1700 marriage of Anna Tufts and John Brocus.
_PT = "peter-tufts-1648"
_ID = "medfordhistorica07medf"
def _u(n): return "https://archive.org/details/" + _ID + "/page/n" + str(n) + "/mode/1up"
_ART = '&ldquo;The Old Time Medford Town Meeting,&rdquo; by Wilson Fiske and Ruth Dame Coolidge, <em>Medford Historical Register</em> XXXIV'
_S44 = _ART + ' no. 3 (Sept. 1931), p. 44. <a href="' + _u(251) + '">View the page scan</a>'
_S69 = _ART + ' no. 4 (Dec. 1931), p. 69. <a href="' + _u(280) + '">View the page scan</a>'
_S71 = _ART + ' no. 4 (Dec. 1931), p. 71. <a href="' + _u(282) + '">View the page scan</a>'
_S78 = _ART + ' no. 4 (Dec. 1931), p. 78, reprinting the early Medford town records. <a href="' + _u(289) + '">View the page scan</a>'
_MH = "Medford Historical Society, <em>Medford Historical Register</em>, via Internet Archive"
IMAGES["mhr-xxxiv-town-meeting-officers.jpg"] = ("Clipping: Peter Tufts, moderator and selectman", "Detail of p. 44, <em>Medford Historical Register</em> XXXIV (Sept. 1931).", _MH, "Shown for non-commercial historical use", _u(251), "Internet Archive (full page)")
IMAGES["mhr-xxxiv-peter-tufts-house-residents.jpg"] = ("Clipping: residents of the Peter Tufts house", "Footnote, p. 69, <em>Medford Historical Register</em> XXXIV (Dec. 1931).", _MH, "Shown for non-commercial historical use", _u(280), "Internet Archive (full page)")
IMAGES["mhr-xxxiv-mercy-cotton-tufts.jpg"] = ("Clipping: Mercy (Cotton) Tufts", "Footnote, p. 71, <em>Medford Historical Register</em> XXXIV (Dec. 1931).", _MH, "Shown for non-commercial historical use", _u(282), "Internet Archive (full page)")
IMAGES["mhr-xxxiv-brocus-tufts-marriage.jpg"] = ("Clipping: John Brocus and Anna Tufts married, 1700", "Early Medford records as reprinted in <em>Medford Historical Register</em> XXXIV (Dec. 1931).", _MH, "Shown for non-commercial historical use", _u(289), "Internet Archive (full page)")
_SEC = ('<section id="town-meeting-1931"><h2>Moderator of the Town Meeting, and a 1931 Portrait of His Household</h2>'
  + '<p>In 1930&ndash;31 the First Parish of Medford staged &ldquo;The Old Time Medford Town Meeting,&rdquo; a play set in the town&rsquo;s first meeting-house and printed with the authors&rsquo; notes in the <em>Medford Historical Register</em>. The authors drew the town officers from the town records, and Peter Tufts stands at the head of them:</p>'
  + FIG("mhr-xxxiv-town-meeting-officers.jpg", "hfig-flow mi-inline")
  + Q("Peter Tufts was moderator at this meeting. Stephen Willis was town clerk&hellip; The selectmen were Peter Tufts, John Francis and Nathan Wade; the tithing man was Jonathan Tufts; Nathaniel Hall was surveyor of highways; and John Francis and Ebeneezer Brooks were fence-viewers.", _S44)
  + '<p>Its third scene, by Ruth Dame Coolidge, brings &ldquo;Mistress Peter Tufts and her daughter, Anna&rdquo; to a neighbor&rsquo;s fireside, Anna with John Brocus, &ldquo;with whom her banns were cried last Sunday.&rdquo; The authors footnote the family as living in the house now known as the Peter Tufts House:</p>'
  + FIG("mhr-xxxiv-peter-tufts-house-residents.jpg", "hfig-flow mi-inline")
  + Q("Residents of the Cradock or Peter Tufts house at this time. Peter Tufts was representative to the General Court.", _S69)
  + '<p>The &ldquo;Mistress Tufts&rdquo; of the scene is his second wife, Mercy Cotton, Anna&rsquo;s stepmother, whose descent from the poet Anne Bradstreet the play notes:</p>'
  + FIG("mhr-xxxiv-mercy-cotton-tufts.jpg", "hfig-flow mi-inline")
  + Q("Mercy Tufts was daughter of Rev. Seaborn Cotton by his wife Dorothy Bradstreet, daughter of Gov. Simon Bradstreet by his wife Ann Dudley, the poetess.", _S71)
  + '<p>The printed play closes the scene with the town record of Anna&rsquo;s marriage:</p>'
  + FIG("mhr-xxxiv-brocus-tufts-marriage.jpg", "hfig-flow mi-inline")
  + Q("the 24th day of June 1700. John Brocus &amp; Anna Tufts was maried.", _S78)
  + '<p><strong>Tufts association:</strong> Peter Tufts as moderator and selectman of Medford, and the household of the Peter Tufts (Cradock) House about 1700 (' + _S44 + '; ' + _S69 + '). See also <a href="../places.html">Places</a>.</p>'
  + UNV("The dialogue of the play is a 1931 dramatization, not a historical record; only the authors&rsquo; notes and the reprinted town records are cited here as fact. The exact year of the meeting depicted is not stated in the passages used here. Which <strong>Jonathan Tufts</strong> served as tithing man (likely Peter&rsquo;s brother Jonathan) is not confirmed. Mercy&rsquo;s &ldquo;eight children&rdquo; is the play&rsquo;s line, not a record. Note: Pending further work.")
  + '</section>')
_up_add(_PT, _SEC, 'id="town-meeting-1931"')
print("town_meeting_1126 done")
