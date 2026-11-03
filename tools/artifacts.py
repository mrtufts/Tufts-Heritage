# Muskets, Adams letters, and people added after the Project 1776 index audit (2026-11-03).
AHS = "https://arlingtonhistorical.pastperfectonline.com/webobject/"
M131 = MSS + ", p. 131"; M132 = MSS + ", p. 132"
def NP(slug, name, town, bio, service, unv, family="<p>Family placement not yet established from a cited source.</p>"):
    return dict(slug=slug, name=name, dates="[dates not confirmed]", town=town, born="", died="", era="The Revolution", line="Undetermined", bio=bio, service=service, family=family, unverified=unv)
PROFILES += [
 NP("ephraim-tufts", "Ephraim Tufts", "Menotomy (Arlington), Mass. [unconfirmed]",
  '<p>Ephraim Tufts is known so far from two muskets in the Arlington Historical Society collection. The first, a French Charleville-pattern flintlock dated about 1763&ndash;1773, is recorded as &ldquo;Formerly the property of Ephraim Tufts &ndash; inherited from his father.&rdquo; The second is a British-pattern musket of about 1810&ndash;1830, and the catalog calls that dating &ldquo;consistent with ownership by Ephraim Tufts.&rdquo; Both came to the Society from Omar Whittemore. See <a href="{P}collections.html#muskets">Collections: The Tufts Muskets</a>.</p>',
  '<p>No Revolutionary service record for an Ephraim Tufts has been found in <em>Massachusetts Soldiers and Sailors</em>, vol. XVI (the Tufts entries, pp. 130&ndash;140).</p>',
  "Ephraim Tufts&rsquo;s dates, residence and parents. The catalog names an Ebenezer Tufts among the people linked to the older musket, which may make Ebenezer his father, but the record does not say so. The catalog does not say that either musket was used on April 19, 1775; it lists that date only as a search term."),
 NP("aaron-tufts", "Aaron Tufts", "Medford",
  '<p>Aaron Tufts of Medford enlisted for three years in the Continental Army in 1777. He served in Capt. James Bancroft&rsquo;s company of Col. Michael Jackson&rsquo;s regiment from March 1777 to February 1780, then went out again with Medford&rsquo;s six-months men in 1780.</p>',
  Q("Tufts, Aaron, Medford. List of men raised to serve in the Continental Army from 1st Middlesex Co. regt., as returned by Lieut. Stephen Hall; residence, Medford; engaged for town of Medford; joined Capt. Bancroft's co., Col. Jackson's regt.; term, 3 years", M131) + Q("marched to camp July 4, 1780; discharged Dec. 12, 1780; service, 5 mos. 20 days", M131),
  "His dates and parentage. Other compilations report that he was captured at sea in 1781 and died in Old Mill Prison, Plymouth, England; that is not in the record quoted here. Wild (p. 20) is reported to name him at Breyman&rsquo;s redoubt, Oct. 7, 1777; the page scan is not yet on file."),
 NP("adam-tufts", "Adam Tufts", "Chelsea and Malden",
  '<p>Adam Tufts enlisted from Chelsea in February 1777 for three years in Capt. Moses Greenleaf&rsquo;s company, Col. Ebenezer Francis&rsquo;s regiment, which marched to Bennington and the northern army. He was reported dead on April 16, 1778.</p>',
  Q("Private, Capt. Moses Greenleaf's co., Col. Benjamin Tupper's regt.; Continental Army pay accounts for service from Feb. 4, 1777, to April 16, 1778; reported died April 16, 1778", M131),
  "His family line. A Malden list also names an Adam Tufts &ldquo;engaged for town of Malden&rdquo; (p. 131); whether this is the same man is not confirmed. No link to the main Tufts line is established."),
 NP("benjamin-tufts", "Benjamin Tufts", "Medford",
  '<p>Benjamin Tufts helped pay for Medford&rsquo;s soldiers sent to Canada and to New York in 1776, and served himself in Capt. Benjamin Blaney&rsquo;s company of guards at Cambridge in 1778. A Benjamin Tufts was also one of the brickmakers of the Fountain Yards (see <a href="{P}businesses.html#fountain-yards">Businesses</a>).</p>',
  Q("Private, Capt. Benjamin Blaney's co., Col. Eleazer Brooks's regt. of guards; joined Jan. 12, 1778; service to April 3, 1778, 82 days, at Cambridge.", MSS + ", pp. 131&ndash;132"),
  "His dates and parentage, and whether he is the Fountain Yards brickmaker."),
 NP("cato-tufts", "Cato Tufts", "Medford",
  '<p>Cato Tufts of Medford is one of the men of color who served in the first years of the war. He was in Capt. Ephraim Corey&rsquo;s company, Col. William Prescott&rsquo;s regiment, in the camp at Cambridge in October 1775. In 1776 he was a matross in Col. Thomas Crafts&rsquo;s artillery regiment at Boston. The record ends with the note that he was &ldquo;drummed out&rdquo; between August and November 1776.</p>',
  Q("Tufts, Cato, Medford. Capt. Ephraim Corey's co., Col. William Prescott's regt.; order for bounty coat dated Camp at Cambridge, Oct. 31, 1775; also, Matross, Capt. James Swan's (1st) co., Col. Thomas Crafts's (Artillery) regt.", M132),
  "Whether he fought at Bunker Hill. Prescott&rsquo;s regiment fought there, and bounty coats went to men in service in 1775, but the record does not place him at the battle. His status (free or enslaved), his dates, and the household whose name he bore are not established."),
 NP("daniel-tufts", "Daniel Tufts", "Medford",
  '<p>Daniel Tufts marched with Capt. Isaac Hall&rsquo;s Medford company on the Lexington alarm of April 19, 1775. In July 1778 he served with the guards stationed at Winter Hill. Wild records that he lived near the Powder House, and that the land under his house was set off to Charlestown in 1811 (see <a href="{P}places.html#medford-charlestown">Places</a>). In 1788 he sold the farm opposite the Powder House to his cousin Peter Tufts (Booth, <em>Historic Leaves</em> vol. 1, p. 22).</p>',
  Q("Tufts, Daniel, Medford. Private, Capt. Isaac Hall's co., Col. Thomas Gardner's regt., which assembled April 19, 1775; service, 5 days", M132) + Q("Capt. Nathan Sargeant's co., Col. Jacob Gerrish's regt. of guards; detached July 2, 1778; service to July 17, 1778, 15 days; regiment stationed at Winter Hill.", M132),
  "His dates and parents. That the Daniel of this record is the Daniel of the Powder House farm is likely but not confirmed."),
 NP("hutchinson-tufts", "Hutchinson Tufts", "Medford",
  '<p>Hutchinson Tufts helped pay for the men Medford hired to go to Canada and to New York in 1776. A Hutchinson Tufts was also among the brickmakers of the Fountain Yards (see <a href="{P}businesses.html#fountain-yards">Businesses</a>).</p>',
  Q("Tufts, Hutchinson. Account of money paid by persons to hire men to go to Canada [year not given], examined and allowed by a committee at Medford Oct. 8, 1776", MSS + ", p. 134"),
  "His dates. No field service is recorded for him."),
 NP("nathan-tufts-jr", "Nathan Tufts Jr.", "Medford",
  '<p>Nathan Tufts Jr. helped pay for the men sent to New York in 1776 and served 82 days with Capt. Benjamin Blaney&rsquo;s guards at Cambridge in 1778.</p>',
  Q("Tufts, Nathan, Jr. Account of money paid by persons to hire men who went to New York in Sept., 1776, examined and allowed by a committee at Medford Jan. 13, 1777; also, Private, Capt. Benjamin Blaney's co., Col. Eleazer Brooks's regt. of guards; joined Jan. 12, 1778; service to April 3, 1778, 82 days, at Cambridge.", MSS + ", p. 137"),
  "His dates and whether he is Nathan the Charlestown tanner (see Businesses). Compare also Nathan Tufts (15-7)."),
 NP("samuel-tufts-3d", "Samuel Tufts 3d", "Medford",
  '<p>Samuel Tufts 3d of Medford marched with Capt. Isaac Hall&rsquo;s company on April 19, 1775. Medford had at least three men named Samuel Tufts at the time, and the numeral set him apart from the others.</p>',
  Q("Tufts, Samuel, 3d, Medford. Private, Capt. Isaac Hall's co., Col. Thomas Gardner's regt., which assembled April 19, 1775; service, 5 days.", MSS + ", p. 139"),
  "His dates and parents. Not yet matched to a family number."),
]
MUSKETS = f'''<section id="muskets"><h2>The Tufts Muskets</h2>
<p>The Arlington Historical Society, which keeps the Jason Russell House, holds two muskets catalogued as the property of Ephraim Tufts. The Society&rsquo;s online catalog lists both. They are not illustrated here because the catalog grants no reuse license; follow the links to see them.</p>
<h3>Musket, catalog no. 1907.11.1: French Charleville pattern, about 1763&ndash;1773</h3>
{Q("Flint lock musket - With bayonet c. 1763-1773, French Barrel rings missing. American -made muskets were patterned after this French model. Formerly the property of Ephraim Tufts - inherited from his father. Bayonet is probably British, added later. Lock Plate &lsquo;Charleville R&rsquo;", f'Arlington Historical Society, catalog no. 1907.11.1. Source: Omar Whittemore. <a href="{AHS}A6A8A54E-2B3B-49DD-94D5-607561794660">Catalog record</a>')}
{TA('Owned by <a href="{{P}}profiles/ephraim-tufts.html">Ephraim Tufts</a>, who inherited it from his father. The catalog links the record to Ebenezer Tufts and Ephraim Tufts Whittemore.', "catalog no. 1907.11.1")}
{UNV("Who Ephraim&rsquo;s father was, and whether this musket was carried on April 19, 1775. The catalog gives &ldquo;April 19, 1775 Lexington &amp; Concord&rdquo; only as a search term. The Jason Russell House guide describes a Charleville 1763 musket on the kitchen wall only as being &ldquo;of the kind&rdquo; Colonial troops used. It has not been confirmed that this is the Tufts musket.")}
<h3>Musket, catalog no. 1907.11.3: British India pattern, about 1810&ndash;1830</h3>
{Q("This appears to be a 3rd-pattern/India pattern British musket from ca. 1810-1830. &hellip; This dating is also consistent with ownership by Ephraim Tufts", f'Arlington Historical Society, catalog no. 1907.11.3. Source: Omar Whittemore. <a href="{AHS}11A3FED3-F109-4586-9DA0-174329339745">Catalog record</a>')}
{TA('Catalogued as owned by <a href="{{P}}profiles/ephraim-tufts.html">Ephraim Tufts</a>. This is a militia arm of the early 1800s, not a Revolutionary weapon.', "catalog no. 1907.11.3")}
<h3>Related: Capt. Benjamin Locke&rsquo;s musket, catalog no. 1924.5.1</h3>
{Q("This gun was carried by Capt. Benjamin Locke (Aug 5, 1738 - Dec. 7, 1791). Capt. Locke was born at the &lsquo;Feet of the Rocks&rsquo; Menotomy, now Arlington. he was captain of a company of minutemen at Lexington and Bunker Hill.", f'Arlington Historical Society, catalog no. 1924.5.1. <a href="{AHS}A41AC27E-2924-4742-8626-470757279760">Catalog record</a>; see also <a href="https://arlingtonhistorical.org/benjamin-locke-menotomy-minute-man/">&ldquo;Benjamin Locke: Menotomy Minute Man&rdquo;</a>')}
{UNV("Any Tufts connection. Another family index says this musket was &ldquo;donated via Effie Tufts.&rdquo; The museum record instead says it was presented in 1924 by the children of Benjamin Delmont Locke and William Henry Locke, and names no Tufts. The barrel is marked &ldquo;TK&rdquo;; its meaning is not stated. Locke was not a Tufts, though the families intermarried: Peter Tufts Jr. (b. 1774) married Martha Locke (Booth, p. 22).")}
<p>The Society also holds a portrait catalogued as &ldquo;Mrs Amos Locke nee Sally Tufts&rdquo; (no. 1915.7.1B). <a href="https://arlingtonhistorical.pastperfectonline.com/photo/F8D78A69-41C6-4E05-9734-560754397332">Catalog record</a>.</p>
</section>'''
L = lambda url, lab: f'<a href="{url}">{lab}</a>'
FA = "https://founders.archives.gov/documents/Adams/"
LETTERS = f'''<section id="adams-letters"><h2>Letters: The Adams Correspondence</h2>
<p>Dr. Cotton Tufts of Weymouth was Abigail Adams&rsquo;s uncle by marriage, and the Adamses&rsquo; physician, adviser and, while John Adams served abroad, their business agent. His name runs through their letters. The quotations below have been checked against the Adams Papers editions.</p>
<ul>
<li><strong>John Adams to Abigail Adams, 7 July 1775:</strong> &ldquo;I am grieved for Dr. Tufts's ill Health: but rejoiced exceedingly at his virtuous Exertions in the Cause of his Country.&rdquo; {L("https://www.masshist.org/digitaladams/archive/doc?id=L17750707ja","Massachusetts Historical Society")}</li>
<li><strong>Abigail Adams to John Adams, 16 July 1775:</strong> &ldquo;Dr. Tufts, Col. Quincy, Mr. Tudor, Mr. Thaxter all have wrote you now.&rdquo; {L("https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-04-01-02-0162","Adams Papers")} &middot; {L(FA+"04-01-02-0162","Founders Online")}</li>
<li><strong>Abigail Adams to John Adams, 13 July 1776:</strong> &ldquo;My Sister Betsy and her Little Neice, Cotton Tufts and Mr. Thaxter&rdquo; were among the household gathered for smallpox inoculation. The editors identify this Cotton Tufts as Cotton Tufts Jr. (1757&ndash;1833). {L("https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-04-02-02-0026","Adams Papers")}</li>
<li><strong>Cotton Tufts to John Adams, 6 August 1776:</strong> &ldquo;Last Week I received Yours of July the 20th. also Dr. Rushs Letter on Inoculation for which You and the learned and benevolent Dr. have my sincere Thanks.&rdquo; {L("https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-04-02-02-0050","Adams Papers")}</li>
<li><strong>John Adams to Abigail Adams, 22 March 1797:</strong> &ldquo;As to the farms I must leave all to you and Dr. Tufts.&rdquo; {L("https://www.masshist.org/digitaladams/archive/doc?id=L17970322ja","Massachusetts Historical Society")}</li>
<li><strong>John Adams to Abigail Adams, 7 April 1797:</strong> &ldquo;If Dr. Tufts has any Money of mine in his hands, I should be glad if he would Supply my Nephew and take his Security.&rdquo; {L("https://www.masshist.org/digitaladams/archive/doc?id=L17970407ja","Massachusetts Historical Society")}</li>
<li><strong>Abigail Smith to Cotton Tufts, 2 April 1764:</strong> a letter from the future Abigail Adams to her &ldquo;Dear Unkle,&rdquo; written during the 1764 smallpox inoculations. {L("https://www.masshist.org/publications/adams-papers/index.php/view/ADMS-04-01-02-0013","Adams Papers")}</li>
</ul>
{UNV("The 1764 letter is sometimes listed as written by Cotton Tufts, with the quotation &ldquo;Physicians and civic authorities early recognized&hellip;&rdquo;. In the Adams Papers it is Abigail Smith&rsquo;s letter <em>to</em> him, and that sentence appears to be editorial commentary, not the letter&rsquo;s text.")}
<p>See <a href="{{P}}profiles/cotton-tufts.html">Dr. Cotton Tufts</a>.</p>
</section>'''
FARM = f'''<section id="farmington-tufts-house"><h2>Tufts House, Farmington, Maine (1810)</h2>
<p>&ldquo;Built by Francis Tufts, a brickmaker,&rdquo; the Federal-style brick house was made from &ldquo;clay Tufts took from the banks of the nearby Sandy River.&rdquo; The Maine Historic Preservation Commission adds that Tufts came from Medford with his family in 1775 and built the first mills at Farmington Falls. It was listed on the National Register in 1979. <span class="cite">(<a href="https://www.maine.gov/mhpc/did-you-know/tufts-house-1810-farmington-franklin-county">Maine Historic Preservation Commission</a>)</span></p>
{TA('Built and lived in by Francis Tufts, brickmaker and millwright of Farmington Falls.', '<a href="https://www.maine.gov/mhpc/did-you-know/tufts-house-1810-farmington-franklin-county">MHPC</a>')}
{UNV('Whether this Francis is <a href="{{P}}profiles/francis-tufts-20-1.html">Rev. Francis Tufts (20-1)</a>. The Medford origin and the Farmington Falls mills fit his profile; the identity is not confirmed.')}
</section>'''
AUDIT = f'''<section id="index-audit"><h2>Names Under Research</h2>
<p>These names appear in other published Tufts family indexes. They are not yet confirmed here, and none was found among the Tufts entries of <em>Massachusetts Soldiers and Sailors</em>, vol. XVI, pp. 130&ndash;140.</p>
{UNV("<strong>Ichabod Tufts</strong> (said to be killed at Bunker Hill, 1775); <strong>Elias Tufts</strong> (said to have served in the 15th Massachusetts); <strong>Frederick Tufts</strong> (said to be a sergeant of colonial militia); <strong>James Tufts (1726&ndash;1786)</strong> (supporter of the cause). Each needs a primary record.")}
</section>'''
PLACE_AUDIT = UNV("Claims from other Tufts indexes that are not yet confirmed: that the Timothy Tufts House was &ldquo;a gathering place for Medford militia&rdquo; (Booth places it on Elm Street in Charlestown, now Somerville, and does not say this); that Anne Adams Tufts nursed &ldquo;Hessian prisoners&rdquo; at a Winter Hill hospital (Booth, p. 22, says she nursed eight wounded soldiers after Bunker Hill, and later the dying wife of one of Burgoyne&rsquo;s prisoners); and that the Powder House land was Tufts-owned in 1774.")
_EXTRA3 = EXTRA
def EXTRA(path):
    out = _EXTRA3(path)
    if path == "collections.html": out = "{DIV}" + MUSKETS + "{DIV}" + LETTERS + out
    if path == "places.html": out = "{DIV}" + FARM + "{DIV}" + '<section id="index-claims"><h2>Claims Under Research</h2>' + PLACE_AUDIT + '</section>' + out
    if path == "people.html": out = "{DIV}" + AUDIT + out
    if path == "profiles/cotton-tufts.html": out += '{DIV}<section id="letters"><h2>Letters</h2><p>See <a href="{P}collections.html#adams-letters">the Adams correspondence</a>.</p></section>'
    if path == "profiles/francis-tufts-20-1.html": out += '{DIV}<section id="farmington-house"><h2>Tufts House, Farmington</h2><p>An 1810 brick house built by &ldquo;Francis Tufts, a brickmaker&rdquo; may be his; the identity is Unverified. See <a href="{P}places.html#farmington-tufts-house">Places</a>.</p></section>'
    return out
