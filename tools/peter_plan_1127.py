# Daily research run 2026-11-27: Peter Tufts's 1816 road plan (MHR XXXI, Sept. 1928, p. 58) and the 1929 campaign to save the
# Cradock-Tufts house (MHR XXXII, June 1929, p. 32). IA medfordhistorica05medf n81 and n167.
_PS = "peter-tufts-1774"
_PH = "peter-tufts-1648"
_U58 = "https://archive.org/details/medfordhistorica05medf/page/n81/mode/1up"
_U32 = "https://archive.org/details/medfordhistorica05medf/page/n167/mode/1up"
_S58 = '&ldquo;Upper Medford,&rdquo; <em>Medford Historical Register</em> XXXI no. 3 (Sept. 1928), p. 58. <a href="' + _U58 + '">View the page scan</a>'
_S32 = '&ldquo;Notes by the Way,&rdquo; <em>Medford Historical Register</em> XXXII no. 2 (June 1929), p. 32. <a href="' + _U32 + '">View the page scan</a>'
_MH7 = "Medford Historical Society, <em>Medford Historical Register</em>, via Internet Archive"
IMAGES["mhr-xxxi-peter-tufts-plan-1816.jpg"] = ("Clipping: Peter Tufts&rsquo;s plan of 1816", "Detail of p. 58, <em>Medford Historical Register</em> XXXI (Sept. 1928), &ldquo;Upper Medford.&rdquo;", _MH7, "Shown for non-commercial historical use", _U58, "Internet Archive (full page)")
IMAGES["mhr-xxxii-cradock-tufts-campaign.jpg"] = ("Clipping: the campaign to save the Cradock-Tufts house, 1929", "Detail of p. 32, <em>Medford Historical Register</em> XXXII (June 1929), &ldquo;Notes by the Way.&rdquo;", _MH7, "Shown for non-commercial historical use", _U32, "Internet Archive (full page)")
_Q58 = ("Two interesting old plans drawn in 1816 are preserved in the Historical Society&rsquo;s files. One by Peter Tufts (of Medford) shows the various turnpikes and roads, also including the canal and rivers, also the millponds both sides of the Charles, the roads converging at Boston market, i. e. Faneuil hall. At the other end is Burlington meeting-house and Woods&rsquo; tavern. A &ldquo;new intended road&rdquo; is shown leading from the old West Cambridge road at Gardner&rsquo;s across the canal and the Aberjona, across the Brooks&rsquo; farm at Grove street to Elbow corner and the &ldquo;Otis&rdquo; place on old Woburn street. On this all distances are marked in rods and mile marks along the entire course. Wood&rsquo;s tavern is stated as thirteen miles from Charlestown bridges by Medford and Woburn. The (upper) Medford and Charlestown lines are clearly shown. Especially interesting is the outline of the end of the upper pond as compared with the present.")
_Q32 = ("The campaign to save the old Cradock-Tufts house on Riverside avenue, by the Society for the Preservation of New England Antiquities, has been successful. Two special meetings of the Historical Society were held in July to consider a proposal made by the Preservation Society to give the house to our society. After full discussion the society decided that it was not in a position to accept the gift at this time and the disposition of the property is still undecided.")
_SEC1 = ('<section id="road-plan-1816"><h2>A Road Plan of 1816 in the Medford Historical Society</h2>'
  + '<p>In 1928 the <em>Medford Historical Register</em> described two road plans of 1816 kept in the Medford Historical Society&rsquo;s files. The first was drawn by &ldquo;Peter Tufts (of Medford)&rdquo; and traced the turnpikes, the Middlesex Canal and a proposed new road through Upper Medford, measured in rods with mile marks all the way from Charlestown bridges to Wood&rsquo;s tavern in Burlington:</p>'
  + FIG("mhr-xxxi-peter-tufts-plan-1816.jpg", "hfig-flow mi-inline")
  + Q(_Q58, _S58)
  + '<p>The proposed road was never built. A companion plan by James F. Baldwin showed the same route and a second one that became Purchase Street (now North Winthrop Street).</p>'
  + '<p><strong>Tufts association:</strong> a survey plan drawn by Peter Tufts, preserved by the Medford Historical Society (' + _S58 + '). See also <a href="../places.html#maps">Places: Maps</a>.</p>'
  + UNV("The <em>Register</em> names the maker only as &ldquo;Peter Tufts (of Medford).&rdquo; He is placed here as Peter the surveyor, the family&rsquo;s known map-maker, who had moved to Cambridgeport by 1815; his father, " + PL("peter-tufts-jr", "Peter Tufts Jr. (1753&ndash;1832)") + ", of Medford, also signed plans as &ldquo;Peter Tufts jun<sup>r</sup>.&rdquo; Whether the plan is still in the Society&rsquo;s collection, and its present catalog number, are not known. Note: Pending further work.")
  + '</section>')
_up_add(_PS, _SEC1, 'id="road-plan-1816"')
_SEC2 = ('<section id="cradock-tufts-1929"><h2>Saving the Cradock-Tufts House, 1929</h2>'
  + '<p>By the late 1920s the brick house associated with Peter Tufts on Riverside Avenue was in danger. The <em>Register</em> reported in June 1929 that the Society for the Preservation of New England Antiquities (now Historic New England) had saved it, and that the Medford Historical Society had been offered the house:</p>'
  + FIG("mhr-xxxii-cradock-tufts-campaign.jpg", "hfig-flow mi-inline")
  + Q(_Q32, _S32)
  + '<p>The Preservation Society kept the house, and the Medford Historical Society later held meetings there, including the November 1931 reading of &ldquo;Medford and George Washington&rdquo; &ldquo;at the Peter Tufts or Cradock House&rdquo; (<em>Medford Historical Register</em> XXXIV no. 4, Dec. 1931, p. 57. <a href="https://archive.org/details/medfordhistorica07medf/page/n268/mode/1up">View the page scan</a>). See <a href="../places.html">Places</a>.</p>'
  + '<p><strong>Tufts association:</strong> the Peter Tufts (Cradock-Tufts) House, 350 Riverside Avenue, Medford (' + _S32 + ').</p>'
  + '</section>')
_up_add(_PH, _SEC2, 'id="cradock-tufts-1929"')
if "MAPS_HTML" in globals() and "road-plan-1816" not in MAPS_HTML:
    MAPS_HTML = MAPS_HTML.replace("</ul>", '<li>Peter Tufts, plan of the turnpikes, canal and a proposed road through Upper Medford (1816), Medford Historical Society files: described by the <em>Register</em> with distances in rods from Charlestown bridges to Wood&rsquo;s tavern (' + _S58 + '; maker&rsquo;s identity flagged). <a href="{P}profiles/' + _PS + '.html#road-plan-1816">Details on his page</a>.</li></ul>', 1)
print("peter_plan_1127 done")

exec(open("tools/six_profiles_1127.py").read())
