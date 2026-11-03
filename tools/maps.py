# Maps and homesteads (standing research duty, first pass 2026-11-03). Findings log kept outside the repo.
DC = "https://www.digitalcommonwealth.org/search/commonwealth:"
BOOTH = "Edward C. Booth, &ldquo;The Tufts Family in Somerville,&rdquo; <em>Historic Leaves</em> (Somerville Historical Society), vol. 1 (1902&ndash;03)"
BOOTH_URL = "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2001.05.0309%3Achapter%3D"
MHR18 = "&ldquo;The Tufts Family Residences,&rdquo; <em>Medford Historical Register</em>, vol. XVIII (1915)"
MHR18_URL = "https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A2005.05.0018%3Achapter%3D18"
IMAGES.update({
 "map-medford-1794-peter-tufts.jpg": ("A Plan of the Town of Medford, surveyed 1794 by Peter Tufts Jun<sup>r</sup>", "Manuscript town plan made under the Resolve of 1794 for the state map, showing the Mystic River, the roads, the meeting house, and the bounds with Charlestown, Malden, Stoneham and Woburn. It is signed &ldquo;Peter Tufts jun<sup>r</sup>&rdquo; and states 5,631 acres. Massachusetts Archives, Town Plans 1794 series, vol. 1, p. 16, register no. 1191.", "Peter Tufts Jr. (surveyor); Massachusetts Archives", "No known copyright restrictions", DC+"2227ng58z", "Digital Commonwealth item"),
 "map-charlestown-1818-peter-tufts.jpg": ("Plan of Charlestown Peninsula, &ldquo;from accurate survey by Peter Tufts Jun<sup>r</sup>. Esq<sup>r</sup>.&rdquo; (1818)", "Engraved plan (Boston: Annin &amp; Smith), scale about 400 feet to the inch, showing Bunker and Breed&rsquo;s Hills, the Navy Yard, the State Prison, wharves, lots and landowners&rsquo; names. Norman B. Leventhal Map &amp; Education Center, Boston Public Library, call no. G3764.B6:2C38 1818 .T8x.", "Peter Tufts Jr. (surveyor); Annin &amp; Smith, engravers", "No known copyright restrictions", DC+"cj82m224p", "Digital Commonwealth item"),
})
CREDITS = '<section id="image-credits"><h2>Image Credits</h2><p>Illustrations are public domain or openly licensed, except photographs from The Historical Marker Database (HMdb.org), which are used noncommercially with the attribution its terms require. Each is stored on this site and linked to its source page, which carries the full terms. CC BY-SA images may be reused under the same license.</p><ul>' + "".join(
    f'<li><a href="{{P}}assets/images/{f}">{t}</a>. {who}. {lic}. <a href="{src}">{(v[5]+" page") if len(v)>5 else "Wikimedia Commons file page"}</a></li>' for f, v in IMAGES.items() for (t, cap, who, lic, src) in [v[:5]]) + '</ul></section>'

MAPS_HTML = f'''<section id="maps"><h2>Maps</h2>
<p>Two of the earliest surviving plans of this ground were drawn by a member of the family. Both carry the signature of a &ldquo;Peter Tufts Jun<sup>r</sup>&rdquo;: a town plan of Medford made for the Commonwealth in 1794, and a printed plan of the Charlestown peninsula in 1818. Both originals are described as having no known copyright restrictions, and both are shown here from the holding institutions&rsquo; scans.</p>
<div class="figs">{FIG("map-medford-1794-peter-tufts.jpg")}{FIG("map-charlestown-1818-peter-tufts.jpg")}</div>
<h3>The surveyor</h3>
{Q("Mr. Tufts was a civil engineer by profession, and among the many Peters is designated as &lsquo;Peter, the surveyor.&rsquo; He drew a plan of Charlestown in 1818, and the mass of plans that he left behind him shows how laboriously he was engaged in the surveys of public and private property.", BOOTH + f', p. 23, on Peter Tufts Jr., born 1774, son of <a href="{{P}}profiles/peter-tufts-jr.html">Peter Tufts (1753&ndash;1832)</a>. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth adds on the same page that this Peter (1774&ndash;1825) was keeper of the Powder House, moved with the powder to the new magazine at Cambridgeport in 1815, and died there in 1825.</p>
{UNV("Which Peter Tufts signed the 1794 Medford plan. In 1794 both Peter Tufts (1753&ndash;1832), then living in Medford, and his son Peter (1774&ndash;1825), the surveyor, could have been styled &ldquo;Jun<sup>r</sup>.&rdquo; Booth credits the son with the 1818 Charlestown plan only. The attribution of the 1794 plan to the son is likely but not confirmed.")}
<h3>Other maps showing Tufts land</h3>
<ul>
<li>Loammi Baldwin&rsquo;s manuscript copy, about 1807, of Tufts&rsquo;s 1794 Medford plan. William L. Clements Library, University of Michigan. <a href="https://collections.leventhalmap.org/search/commonwealth-oai:7s75jb12v">Leventhal catalog record</a> (link only; may be under copyright per the holder).</li>
<li>Felton &amp; Parker, <em>Plan of the City of Charlestown</em> (1848), which superseded Tufts&rsquo;s plan and shows parts of Somerville. <a href="https://collections.leventhalmap.org/search/commonwealth:1257b9962">Leventhal Map Center</a>.</li>
<li>Geo. W. Stadly &amp; Co., <em>Atlas of the City of Medford</em> (1897&ndash;99), double sheets 20&ndash;21, with facsimiles of Tufts&rsquo;s 1794 plan, John Sparrell&rsquo;s 1830 plan and H. F. Walling&rsquo;s 1855 map. <a href="https://collections.leventhalmap.org/search/commonwealth:th83pt32s">Leventhal Map Center</a>.</li>
</ul>
{UNV("No map yet located marks the Winter Hill, Powder House or Elm Street Tufts farms by owner name. Later atlases with owners&rsquo; names are still to be checked.")}
</section>
{{DIV}}
<section id="homesteads"><h2>Homesteads</h2>
<h3>Peter Tufts House, Medford (350 Riverside Avenue)</h3>
<p>The brick house long misnamed the &ldquo;Cradock House&rdquo; is a National Historic Landmark (1968). The <em>Medford Historical Register</em> of 1915 assigns its building to the first Peter Tufts &ldquo;some fifteen or twenty years before his death in 1700,&rdquo; first occupied by his son Captain Peter. <span class="cite">({MHR18}, p. 64. <a href="{MHR18_URL}">Text (Perseus)</a>)</span> Photographs are in the Illustrations below.</p>
{UNV("The exact building date and builder. Sources give about 1677&ndash;1680; tree-ring or deed proof has not been seen here.")}
<h3>The Drs. Simon Tufts house, Medford Square</h3>
{Q("A few old residents there are who remember the old house which was successively the home of the elder and younger Drs. Simon, and Turell Tufts, Esq., at Medford square. This, decrepit with age, was demolished in 1867", MHR18 + f", p. 67. <a href=\"{MHR18_URL}\">Text (Perseus)</a>")}
<h3>Peter Tufts of Winter Hill homestead</h3>
{Q("Many remember the old house near the westerly corner of Central street and Broadway, before its removal to Lowell street.", BOOTH + f', p. 21. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth (p. 24) says Joseph Tufts, born 1760, inherited this homestead and lived in it until 1819, and that his son Edmund later hung the sign &ldquo;Edmund Tufts, Printer&rdquo; on the old house. See also <a href="#winter-hill">Winter Hill</a>.</p>
<h3>Peter and Oliver Tufts House, Somerville (78 Sycamore Street)</h3>
{Q("During the Revolution, his father established him on the farm the house of which is now rented by the Somerville Historical society.", BOOTH + f', p. 23, on John Tufts (b. 1755), son of Peter of Winter Hill. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth calls it &ldquo;the headquarters of General Lee&rdquo; and says Oliver Tufts farmed there until his death in 1883 (pp. 23&ndash;24). The house was moved a short distance from its first site and is listed on the National Register (1989). Measured drawings: <a href="https://www.loc.gov/item/ma0809/">Historic American Buildings Survey, MA-809 (Library of Congress)</a>.</p>
<h3>Timothy Tufts house, Elm Street, Somerville</h3>
{Q("This house was built about a year before the Revolution, and replaced an older one which stood on a knoll by a large elm tree somewhat farther back from the street.", BOOTH + f', p. 25, on Timothy Tufts (b. 1735), on Elm Street near Willow Avenue. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
{UNV("Whether the Timothy Tufts house still stands. Booth wrote in 1902&ndash;03; no later source has been checked.")}
<h3>Peter Tufts (of Milk Row) house, Somerville Avenue</h3>
{Q("It is the house familiar to the members of this society as the one on Somerville avenue, which General Greene occupied as his headquarters during the siege of Boston.", BOOTH + f', p. 24, on the dwelling bought of Russell in 1701. <a href="{BOOTH_URL}2">Text (Perseus)</a>')}
<h3>The Powder House farm and the Peter Tufts mansion, 1806</h3>
{Q("In 1788, Peter bought of his cousin, Daniel Tufts, the farm opposite the Powder House, afterwards owned by Charles Tufts, and in 1806 built upon it the large three-storied mansion house taken down a few years ago.", BOOTH + f', p. 22, on Peter Tufts (1753&ndash;1832). <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>The Commonwealth sold the Powder House itself to a Peter Tufts in 1818. It passed to Nathan Tufts, and his heirs gave it to Somerville in 1890 for the park named for him. <a href="https://en.wikipedia.org/wiki/Powder_House_Square">Wikipedia: Powder House Square</a> (tertiary).</p>
{UNV("The Powder House chain of title. Secondary sources disagree: 1818 or 1822 for the Tufts purchase, and 1836 for the passing to Nathan Tufts. Which Peter bought it is not stated. Deeds not yet seen.")}
<h3>Nathan Tufts, butcher and tanner, Charlestown</h3>
{Q("Nathan, the youngest son of Nathan, Sr., was also a resident of Charlestown after his boyhood, and was an extensive butcher and tanner there.", BOOTH + f', p. 21. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth adds that he owned &ldquo;the large farms around the Powder House and Walnut hill afterwards owned by his nephews, Charles and Nathan&rdquo; (p. 21). The Nathan Tufts house itself has not yet been identified.</p>
<h3>Cotton Tufts Jr. homestead, Weymouth (246 Commercial Street)</h3>
<p>The Weymouth Historical Commission&rsquo;s list of historic homes gives 246 Commercial Street as the &ldquo;Cotton Tufts Jr. Homestead,&rdquo; Georgian, built &ldquo;pre 1700.&rdquo; <a href="https://www.weymouth.ma.us/DocumentCenter/View/13676/Demolition-Delay-List--Revised-2026">Town of Weymouth list</a>. The town&rsquo;s Tufts/Smith/Adams Family Collection finding aid adds that the younger Cotton Tufts (1757&ndash;1833) kept a store with James Whittemore where the original Tufts Library was built, and holds an 1877 booklet of plans of the Tufts estate lands in Weymouth, Braintree and Quincy. <a href="https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection">Finding aid</a>. See <a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts</a>.</p>
{UNV("The &ldquo;pre 1700&rdquo; date is the town list&rsquo;s; it predates the Tufts family in Weymouth, so the house was presumably acquired, not built, by them. The 1877 estate plans have not been seen.")}
<h3>Peter Tufts the immigrant, Malden</h3>
<p>Booth (p. 21) writes that the first Peter &ldquo;kept the Ferry between Charlestown and Malden with his brother-in-law, Bridges, in 1646-7,&rdquo; was the largest landholder in Malden at his death in 1700, and lived latterly &ldquo;on the site of the United States Ordnance property, near the Malden river and canal.&rdquo; <a href="{BOOTH_URL}2">Text (Perseus)</a></p>
</section>'''
_EXTRA1 = EXTRA
def EXTRA(path):
    out = _EXTRA1(path)
    if path == "places.html": out = "{DIV}" + MAPS_HTML + out
    if path == "profiles/peter-tufts-jr.html":
        out += '{DIV}<section id="maps"><h2>Maps by His Son</h2><p>His son Peter (1774&ndash;1825), &ldquo;Peter, the surveyor,&rdquo; drew the 1818 <em>Plan of Charlestown Peninsula</em> (Booth, <em>Historic Leaves</em> vol. 1, p. 23). A 1794 plan of Medford signed &ldquo;Peter Tufts jun<sup>r</sup>&rdquo; may be by either man. See <a href="{P}places.html#maps">Places: Maps</a>.</p></section>'
    return out
