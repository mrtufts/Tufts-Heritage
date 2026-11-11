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
TA_FIG = {
 "peter-tufts-house-medford.jpg": "The house of the first Peter Tufts and Capt. Peter Tufts (Medford Historical Register XVIII, pp. 60&ndash;64).",
 "cradock-house-medford.jpg": "This is the Peter Tufts House under its older, mistaken name (Medford Historical Register XVIII, p. 64).",
 "peter-oliver-tufts-house-somerville.jpg": "Farm of John Tufts (b. 1755) and later of Oliver Tufts (Booth, <em>Historic Leaves</em> vol. 1, pp. 23&ndash;24).",
 "old-powder-house-somerville.jpg": "Peter Tufts Jr. and Daniel Tufts lived opposite it (Wild, pp. 50, 52); his son Peter was its keeper (Booth, p. 23).",
 "royall-house-1920.jpg": "Peter Tufts (b. 1753) settled early on &ldquo;the Royal farm in Medford&rdquo; (Booth, <em>Historic Leaves</em> vol. 1, p. 22).",
 "royall-house-east-facade.jpg": "Peter Tufts (b. 1753) settled early on &ldquo;the Royal farm in Medford&rdquo; (Booth, p. 22).",
 "isaac-royall-family-feke.jpg": "Peter Tufts (b. 1753) settled early on &ldquo;the Royal farm in Medford&rdquo; (Booth, p. 22).",
 "dorchester-heights-monument.jpg": "Family tradition places Peter Tufts (b. 1753) in the party that fortified the Heights; Booth p. 22 gives it as &ldquo;It is related.&rdquo; Unverified.",
 "prospect-hill-monument.jpg": "Service of James Tufts Jr. (36-2) and John Tufts (49-2); see their profiles for the cited records.",
 "noddles-island-fort-1776.jpg": "Service of James Tufts Jr. (36-2) and Ebenezer Tufts (36-7); see their profiles for the cited records.",
 "fort-independence-castle-island.jpg": "Tied to Henry Tufts (25-1); see his profile for the cited source.",
 "farmington-falls-postcard-1907.jpg": "Tied to Rev. Francis Tufts (20-1); see his profile for the cited source.",
 "granary-burying-ground.jpg": "Tomb 109, &ldquo;Lorenzo Draper and Francis Tufts 1811&rdquo; (Find a Grave memorial 21755667).",
 "siege-of-boston-1775-map.jpg": "Shows Winter Hill, home of Peter Tufts of Winter Hill (Jones, p. 129).",
 "weymouth-first-church.jpg": "Dr. Cotton Tufts was a deacon of the First Church, Weymouth, for more than forty years (Weymouth Tufts/Smith/Adams finding aid).",
 "medford-square-1913.jpg": "The Drs. Simon Tufts house stood at Medford Square until 1867 (Medford Historical Register XVIII, p. 67).",
 "medford-1880-birdseye.jpg": "Medford: Peter Tufts House, the Drs. Simon Tufts house, and Tufts College (see Places).",
 "mystic-river-medford.jpg": "Ferry, brickyards, fishing rights and mills of the Tufts family lay along the Mystic (Booth part 1 p. 21; Brooks pp. 355&ndash;356, 385). See The Mystic River above.",
}
for _f, _a in TA_FIG.items():
    if _f in IMAGES:
        _v = list(IMAGES[_f]); _v[1] += f' <em>Tufts association:</em> {_a}'; IMAGES[_f] = tuple(_v)
CREDITS = '<section id="image-credits"><h2>Image Credits</h2><p>Illustrations are public domain or openly licensed, except photographs from The Historical Marker Database (HMdb.org), which are used noncommercially with the attribution its terms require. Each is stored on this site and linked to its source page, which carries the full terms. CC BY-SA images may be reused under the same license.</p><ul>' + "".join(
    f'<li><a href="{{P}}assets/images/{f}">{t}</a>. {who}. {lic}. <a href="{src}">{(v[5]+" page") if len(v)>5 else "Wikimedia Commons file page"}</a></li>' for f, v in IMAGES.items() for (t, cap, who, lic, src) in [v[:5]]) + '</ul></section>'

MAPS_HTML = f'''<section id="maps"><h2>Maps</h2>
<p>Two of the earliest surviving plans of this ground were drawn by a member of the family. Both carry the signature of a &ldquo;Peter Tufts Jun<sup>r</sup>&rdquo;: a town plan of Medford made for the Commonwealth in 1794, and a printed plan of the Charlestown peninsula in 1818. Both originals are described as having no known copyright restrictions, and both are shown here from the holding institutions&rsquo; scans.</p>
<div class="figs">{FIG("map-medford-1794-peter-tufts.jpg")}{FIG("map-charlestown-1818-peter-tufts.jpg")}</div>
<h3>The surveyor</h3>
{TA("Both plans were drawn by a Peter Tufts Jr.; the 1818 plan by Peter (1774&ndash;1825), surveyor, son of Peter Tufts (1753&ndash;1832).", BOOTH + f', p. 23. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("Mr. Tufts was a civil engineer by profession, and among the many Peters is designated as &lsquo;Peter, the surveyor.&rsquo; He drew a plan of Charlestown in 1818, and the mass of plans that he left behind him shows how laboriously he was engaged in the surveys of public and private property.", BOOTH + f', p. 23, on Peter Tufts Jr., born 1774, son of <a href="{{P}}profiles/peter-tufts-jr.html">Peter Tufts (1753&ndash;1832)</a>. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth adds on the same page that this Peter (1774&ndash;1825) was keeper of the Powder House, moved with the powder to the new magazine at Cambridgeport in 1815, and died there in 1825.</p>
{UNV("Which Peter Tufts signed the 1794 Medford plan. In 1794 both Peter Tufts (1753&ndash;1832), then living in Medford, and his son Peter (1774&ndash;1825), the surveyor, could have been styled &ldquo;Jun<sup>r</sup>.&rdquo; Booth credits the son with the 1818 Charlestown plan only. The attribution of the 1794 plan to the son is likely but not confirmed.")}
<h3>Other maps showing Tufts land</h3>
{TA("The Baldwin copy and Stadly facsimile reproduce Peter Tufts Jr.&rsquo;s 1794 survey; the 1848 plan covers the same Charlestown ground.", "catalog records linked below")}
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
{TA("Built by or for the first Peter Tufts and occupied by his son Capt. Peter Tufts; probable birthplace of Dr. Simon Tufts (b. 1700).", MHR18 + ", pp. 60&ndash;64")}
<p>The brick house long misnamed the &ldquo;Cradock House&rdquo; is a National Historic Landmark (1968). The <em>Medford Historical Register</em> of 1915 assigns its building to the first Peter Tufts &ldquo;some fifteen or twenty years before his death in 1700,&rdquo; first occupied by his son Captain Peter. <span class="cite">({MHR18}, p. 64. <a href="{MHR18_URL}">Text (Perseus)</a>)</span> Photographs are in the Illustrations below.</p>
{UNV("The exact building date and builder. Sources give about 1677&ndash;1680; tree-ring or deed proof has not been seen here.")}
<h3>The Drs. Simon Tufts house, Medford Square</h3>
{TA("Residence of Dr. Simon Tufts (1700&ndash;1747), his son Dr. Simon Tufts (1726&ndash;1786), and Turell Tufts, Esq.", MHR18 + ", p. 67")}
{Q("A few old residents there are who remember the old house which was successively the home of the elder and younger Drs. Simon, and Turell Tufts, Esq., at Medford square. This, decrepit with age, was demolished in 1867", MHR18 + f", p. 67. <a href=\"{MHR18_URL}\">Text (Perseus)</a>")}
<h3>Peter Tufts of Winter Hill homestead</h3>
{TA("Residence of Peter Tufts of Winter Hill (1728&ndash;1791), then of his son Joseph (1760&ndash;1819); later the printing office of Edmund Tufts.", BOOTH + f', p. 21, 24. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("Many remember the old house near the westerly corner of Central street and Broadway, before its removal to Lowell street.", BOOTH + f', p. 21. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth (p. 24) says Joseph Tufts, born 1760, inherited this homestead and lived in it until 1819, and that his son Edmund later hung the sign &ldquo;Edmund Tufts, Printer&rdquo; on the old house. See also <a href="#winter-hill">Winter Hill</a>.</p>
<h3>Peter and Oliver Tufts House, Somerville (78 Sycamore Street)</h3>
{TA("Farm of John Tufts (b. 1755), set up by his father Peter of Winter Hill during the Revolution; later Oliver Tufts&rsquo;s farm; Gen. Charles Lee&rsquo;s headquarters.", BOOTH + f', p. 23&ndash;24. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("During the Revolution, his father established him on the farm the house of which is now rented by the Somerville Historical society.", BOOTH + f', p. 23, on John Tufts (b. 1755), son of Peter of Winter Hill. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth calls it &ldquo;the headquarters of General Lee&rdquo; and says Oliver Tufts farmed there until his death in 1883 (pp. 23&ndash;24). The house was moved a short distance from its first site and is listed on the National Register (1989). Measured drawings: <a href="https://www.loc.gov/item/ma0809/">Historic American Buildings Survey, MA-809 (Library of Congress)</a>.</p>
<h3>Timothy Tufts house, Elm Street, Somerville</h3>
{TA("Farm and house of Timothy Tufts, Esq. (b. 1735), selectman and justice of the peace, received from his father Peter of Milk Row.", BOOTH + f', p. 25. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("This house was built about a year before the Revolution, and replaced an older one which stood on a knoll by a large elm tree somewhat farther back from the street.", BOOTH + f', p. 25, on Timothy Tufts (b. 1735), on Elm Street near Willow Avenue. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
{UNV("Whether the Timothy Tufts house still stands. Booth wrote in 1902&ndash;03; no later source has been checked.")}
<h3>Peter Tufts (of Milk Row) house, Somerville Avenue</h3>
{TA("Dwelling bought of Russell in 1701 and inherited by Peter Tufts of Milk Row from his father John; Gen. Nathanael Greene&rsquo;s headquarters during the siege.", BOOTH + f', p. 24. <a href="{BOOTH_URL}2">Perseus</a>')}
{Q("It is the house familiar to the members of this society as the one on Somerville avenue, which General Greene occupied as his headquarters during the siege of Boston.", BOOTH + f', p. 24, on the dwelling bought of Russell in 1701. <a href="{BOOTH_URL}2">Text (Perseus)</a>')}
<h3>The Powder House farm and the Peter Tufts mansion, 1806</h3>
{TA("Farm bought by Peter Tufts (1753&ndash;1832) from his cousin Daniel Tufts in 1788, with his 1806 mansion; Powder House later held by Nathan Tufts&rsquo;s heirs.", BOOTH + f', p. 22. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("In 1788, Peter bought of his cousin, Daniel Tufts, the farm opposite the Powder House, afterwards owned by Charles Tufts, and in 1806 built upon it the large three-storied mansion house taken down a few years ago.", BOOTH + f', p. 22, on Peter Tufts (1753&ndash;1832). <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>The Commonwealth sold the Powder House itself to a Peter Tufts in 1818. It passed to Nathan Tufts, and his heirs gave it to Somerville in 1890 for the park named for him. <a href="https://en.wikipedia.org/wiki/Powder_House_Square">Wikipedia: Powder House Square</a> (tertiary).</p>
{UNV("The Powder House chain of title. Secondary sources disagree: 1818 or 1822 for the Tufts purchase, and 1836 for the passing to Nathan Tufts. Which Peter bought it is not stated. Deeds not yet seen.")}
<h3>Nathan Tufts, butcher and tanner, Charlestown</h3>
{TA("Business of Nathan Tufts, son of Nathan Sr.; his landholdings around the Powder House and Walnut Hill.", BOOTH + f', p. 21. <a href="{BOOTH_URL}7">Perseus</a>')}
{Q("Nathan, the youngest son of Nathan, Sr., was also a resident of Charlestown after his boyhood, and was an extensive butcher and tanner there.", BOOTH + f', p. 21. <a href="{BOOTH_URL}7">Text (Perseus)</a>')}
<p>Booth adds that he owned &ldquo;the large farms around the Powder House and Walnut hill afterwards owned by his nephews, Charles and Nathan&rdquo; (p. 21). Sawyer identifies his house as the one on Chelsea Street first built by Aaron Putnam and later known as the home of Dr. Lambert (Timothy T. Sawyer, <em>Old Charlestown</em>, 1902, pp. 168, 171). The same Nathan built the mill pond and tide mill at the Neck; see <a href="{{P}}businesses.html#nathan-tufts-tide-mill">Tide mill of Nathan Tufts</a>.</p>
<h3>Cotton Tufts Jr. homestead, Weymouth (246 Commercial Street)</h3>
{TA("Homestead of Cotton Tufts Jr. (1757&ndash;1833), who also kept a store with James Whittemore.", '<a href="https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection">Weymouth finding aid</a>')}
<p>The Weymouth Historical Commission&rsquo;s list of historic homes gives 246 Commercial Street as the &ldquo;Cotton Tufts Jr. Homestead,&rdquo; Georgian, built &ldquo;pre 1700.&rdquo; <a href="https://www.weymouth.ma.us/DocumentCenter/View/13676/Demolition-Delay-List--Revised-2026">Town of Weymouth list</a>. The town&rsquo;s Tufts/Smith/Adams Family Collection finding aid adds that the younger Cotton Tufts (1757&ndash;1833) kept a store with James Whittemore where the original Tufts Library was built, and holds an 1877 booklet of plans of the Tufts estate lands in Weymouth, Braintree and Quincy. <a href="https://www.weymouth.ma.us/DocumentCenter/View/545/Tufts-Smith-Adams-Family-Collection">Finding aid</a>. See <a href="{{P}}profiles/cotton-tufts-jr.html">Cotton Tufts (1757&ndash;1833)</a> and <a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts</a>.</p>
{UNV("The &ldquo;pre 1700&rdquo; date is the town list&rsquo;s; it predates the Tufts family in Weymouth, so the house was presumably acquired, not built, by them. The 1877 estate plans have not been seen.")}
<h3>Peter Tufts the immigrant, Malden</h3>
{TA("Ferry kept by Peter Tufts (1617&ndash;1700), Malden&rsquo;s largest landholder at his death.", BOOTH + f', p. 21. <a href="{BOOTH_URL}2">Perseus</a>')}
<p>Booth (p. 21) writes that the first Peter &ldquo;kept the Ferry between Charlestown and Malden with his brother-in-law, Bridges, in 1646-7,&rdquo; was the largest landholder in Malden at his death in 1700, and lived latterly &ldquo;on the site of the United States Ordnance property, near the Malden river and canal.&rdquo; <a href="{BOOTH_URL}2">Text (Perseus)</a></p>
</section>
{{DIV}}
<section id="powder-house"><h2>The Powder House and Revolutionary Landmarks</h2>
<h3>The Old Powder House, Somerville (Nathan Tufts Park)</h3>
<p>The stone tower on Quarry Hill was built as a windmill in the early 1700s. In 1747 the province bought the &ldquo;stone edifice, formerly a windmill&rdquo; and a quarter-acre of land and made it a gunpowder magazine. It stood then in Charlestown, close to the Medford line. On September 1, 1774, troops sent by Gov. Thomas Gage removed the provincial powder stored there. Rumor spread that blood had been shed, and thousands of militiamen marched toward Boston and Cambridge. This was the &ldquo;Powder Alarm.&rdquo; The magazine served until 1818, when the state sold it. <span class="cite">(<a href="https://boston1775.blogspot.com/2016/03/the-powderhouse-public-resource-or.html">J. L. Bell, <em>Boston 1775</em>, March 2016</a>; <a href="https://en.wikipedia.org/wiki/Powder_Alarm">Wikipedia: Powder Alarm</a>, tertiary)</span></p>
{TA("Peter Tufts (1753&ndash;1832) bought the farm opposite the Powder House in 1788. His son Peter (1774&ndash;1825) was the keeper of the Powder House until 1815. Nathan Tufts, the butcher and tanner, owned &ldquo;the large farms around the Powder House and Walnut hill.&rdquo; The magazine and its lot were later Tufts property, and the family gave them to Somerville in 1890 as Nathan Tufts Park.", BOOTH + f', pp. 21&ndash;23. <a href="{BOOTH_URL}7">Perseus</a>; <a href="https://sah-archipedia.org/buildings/MA-01-SM13">SAH Archipedia</a>')}
{UNV("Tufts ownership of the magazine lot itself. The Boston 1775 blog and Wikipedia say the state sold it to &ldquo;Peter Tufts&rdquo; in 1818; SAH Archipedia says the Tufts family acquired it in 1822. Neither names which Peter, and the deed has not been seen. Booth confirms Tufts farms around the Powder House, not the purchase of the magazine itself. No Tufts is yet documented in the events of September 1, 1774.")}
<p>Pictured in the Illustrations below. See <a href="{{P}}profiles/peter-tufts-jr.html">Peter Tufts Jr.</a></p>
<h3>Winter Hill fort and the alarm route</h3>
<p>The 1890 marker in Paul Revere Park, Winter Hill, commemorates Paul Revere&rsquo;s ride and the Winter Hill fort. It stands beside the Anne Adams Tufts tablet (see <a href="#winter-hill">Winter Hill</a>).</p>
{TA("Revere&rsquo;s route passed the Winter Hill farm of Peter Tufts, whom he woke on April 19, 1775.", JONES+", p. 129")}
{UNV("The marker&rsquo;s full text and the exact site of the Winter Hill fort have not been transcribed here.")}
<h3>Prospect Hill and Fort No. 3</h3>
{Q("A barrack for the soldiers was erected on the homestead lot during the siege of Boston by Colonel Patterson, and Fort No. 3 took its beginning near the same point.", BOOTH + f', part 1, p. 23. <a href="{BOOTH_URL}2">Perseus</a>')}
{TA("The lot was the homestead of Nathaniel Tufts (1692&ndash;1741), on Washington Street near Union Square. By the Revolution it had passed to his son William (d. 1773).", BOOTH + ", part 1, pp. 22&ndash;23")}
<p>Prospect Hill is pictured in the Illustrations below. For Tufts service there, see <a href="{{P}}profiles/james-tufts-jr-36-2.html">James Tufts Jr.</a> and <a href="{{P}}profiles/john-tufts-49-2.html">John Tufts (49-2)</a>.</p>
<h3>Headquarters houses</h3>
<p>Two Tufts houses served as American headquarters during the siege: Gen. Greene&rsquo;s at the Peter Tufts house on Somerville Avenue, and Gen. Lee&rsquo;s at the John and Oliver Tufts house. See <a href="#homesteads">Homesteads</a>.</p>
{UNV("Other landmarks still to research: Ploughed Hill (Mount Benedict), Cobble Hill, the Medford and Charlestown taverns on the 1775 alarm route, and the Cambridgeport magazine kept by Peter Tufts from 1815.")}
</section>'''
_EXTRA1 = EXTRA
def EXTRA(path):
    out = _EXTRA1(path)
    if path == "places.html": out = "{DIV}" + MAPS_HTML + out
    if path == "profiles/peter-tufts-jr.html":
        pass
        out += '{DIV}<section id="maps"><h2>Maps by His Son</h2><p>His son Peter (1774&ndash;1825), &ldquo;Peter, the surveyor,&rdquo; drew the 1818 <em>Plan of Charlestown Peninsula</em> (Booth, <em>Historic Leaves</em> vol. 1, p. 23). A 1794 plan of Medford signed &ldquo;Peter Tufts jun<sup>r</sup>&rdquo; may be by either man. See <a href="{P}places.html#maps">Places: Maps</a> and <a href="{P}places.html#powder-house">the Powder House</a>, beside the farm he bought in 1788.</p></section>'
    return out
exec(open("tools/businesses.py").read())
