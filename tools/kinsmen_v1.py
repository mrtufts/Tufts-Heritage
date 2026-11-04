# Tufts Kinsmen Vol. I facts, from the owner-supplied roster extract (Nov. 2, 2026).
# The book itself is private and is NOT in this repo. Short statements only, with printed page numbers.
TK1 = "<em>Tufts Kinsmen</em>, Vol. I"
NOSCAN = "owner-supplied extract; page scan not on file"
def V(text, pg, fam):
    return f'<p>{text} <span class="cite">({TK1}, p. {pg}, family no. {fam}; {NOSCAN})</span></p>'
def SIDE(label, a, b):
    return f'<table class="conflict"><caption>Conflict: {label}</caption><tr><th>Source</th><th>Says</th></tr>' + "".join(f"<tr><td>{s}</td><td>{t}</td></tr>" for s, t in (a, b)) + "</table>"
SCANFLAG = "The <em>Tufts Kinsmen</em> Vol. I statements on this page come from an extract supplied by the owner and have not yet been checked against a page scan (citation rule: page scan not on file)."

# ---------- merges into existing profiles ----------
V1MERGE = {
 "peter-tufts-jr": V("Listed as Peter Jr., 3rd, family no. 53-2: born 9 Jan. 1753 in Woburn; died 4 Nov. 1832 in Charlestown; married Hannah Adams.", 178, "53-2") +
  V("Answered the Lexington Alarm and served in the militia at Dorchester Heights in defense of Boston, with other service during the Revolution (the book cites DAR records 14:145, 202&ndash;3 and 41&ndash;56). Head of household in Charlestown in 1820 and 1830.", 178, "53-2") +
  SIDE("death year", (WILD+", p. 52", "&ldquo;died 1836&rdquo;"), (TK1+", p. 178", "died 4 Nov. 1832, Charlestown (agrees with the secondhand DAR A116812 listing)")) +
  SIDE("birthplace", (WYMAN+", p. 965", "&ldquo;Peter, Jan. 9, 1753&rdquo; (issue of Peter 37 of Charlestown; no place stated)"), (TK1+", p. 178", "born 9 Jan. 1753, Woburn")) +
  '<p class="note">Identity match: <strong>clean</strong>. Birth date, wife (Hannah Adams), Lexington Alarm service, and the Charlestown/Medford setting agree with Wyman, Wild, and MSS.</p>',
 "cotton-tufts": V("Dr. Cotton Tufts, family no. 11-4: born 30 May 1732 in Medford; died 8 Dec. 1815 in Weymouth. The book covers him at length on pp. 110&ndash;112.", "110&ndash;112", "11-4") +
  V("His father, Dr. Simon Tufts (11-1), is described as an ardent Whig who treated the wounded after Lexington and Concord and at Bunker Hill. See <a href=\"{P}profiles/simon-tufts-11-1.html\">Dr. Simon Tufts</a>.", 110, "11-1") +
  '<p class="note">Identity match: <strong>clean</strong>. Medford birth, Weymouth death in 1815, and his father Dr. Simon Tufts agree with <em>Tufts Family History</em>, pp. 35, 37. Vol. I supplies the birth date that was missing. Per the owner&rsquo;s note, his Revolutionary service details (e.g. Committee of Safety) are in Vol. II&rsquo;s coverage and are not added here.</p>',
 "caleb-tufts": V("Caleb Tufts, bricklayer and farmer, family no. 44-4: born 1 Sep. 1762 in Medford; died 21 Oct. 1852 in Mystic, Conn.; private in the Revolution, serving three months in 1776; in Southampton, Long Island, N.Y., in 1790; buried in the Old Packer Burying Ground, Mystic.", 166, "44-4") +
  SIDE("birth day", (WILD+", p. 50", "&ldquo;born Sept. 5, 1762&rdquo;"), (TK1+", p. 166", "born 1 Sep. 1762, Medford")) +
  '<p class="note">Identity match: <strong>clean</strong> to Wild&rsquo;s Caleb (Medford, 1762, three months&rsquo; service in 1776, bricklayer and farmer, died Mystic 1852). His brothers Samuel 3rd (44-3) and the parents&rsquo; household are consistent with Wild&rsquo;s &ldquo;son of Samuel and Hannah (Tufts)&rdquo;. The MSS Caleb (Capt. Caleb Brooks&rsquo;s co., Dec. 1776) remains a <strong>possible match</strong> only.</p>',
 "barnabas-tufts": V("Barnabas Tufts, brickmaker, family no. 37-8: born 12 Feb. 1742/3 in Medford; died 1795 in Topsham, Me.; drummer in the Revolution, serving at Albany, N.Y.; from 1760 divided his time between Cumberland County, Me., and Cape Ann, Mass.", 156, "37-8") +
  '<p class="note">Identity match: <strong>strong</strong>. Drummer, service at Albany, and Cape Ann (Gloucester) all agree with the MSS entry &ldquo;TUFTS, BARNABAS, Gloucester. Drummer &hellip; from Albany home.&rdquo;</p>',
 "william-tufts": V("<strong>William Tufts Jr.</strong> (40-2): born 27 Mar. 1736 in Medford; died 27 Apr. 1782; private in Capt. Nathan Sargent&rsquo;s Company of Guards, under Stephen Dana, Col. McIntosh&rsquo;s Regiment (the book cites DAR 92:120). <a href=\"{P}profiles/william-tufts-40-2.html\">Profile</a>", 158, "40-2") +
  V("<strong>Lieut. William Tufts</strong> (13-6): born 10 June 1713 in Charlestown; died 29 Oct. 1783 in Medford; said to have died in service during the Revolution. <a href=\"{P}profiles/william-tufts-13-6.html\">Profile</a>", 116, "13-6") +
  V("<strong>William Tuffs</strong> (35-8): born 1750; served in the Revolution; died 1848 in Elkhart, Ind. <a href=\"{P}profiles/william-tuffs-35-8.html\">Profile</a>", 150, "35-8") +
  '<p class="note"><strong>Possible matches.</strong> The MSS Medford entries for Capt. Stephen Dana&rsquo;s co., Col. McIntosh&rsquo;s regt. (1778) and Capt. Nathan Sergant&rsquo;s co. of guards (1779) fit William Jr. (40-2) closely, but the MSS entries do not give parentage. The MSS &ldquo;2d Lieutenant, Capt. Ezekiel Knowlton&rsquo;s co.&rdquo; (1776) may be Lieut. William (13-6) but gives no town. Wild&rsquo;s William (b. 1762, killed 1777) is a different man and has no Vol. I entry in the extract.</p>',
 "samuel-tufts": V("<strong>Samuel Tufts</strong> (15-3): born 16 Aug. 1732 in Medford; died 31 Dec. 1818; married Hannah Tufts; answered the Lexington alarm; Committee of Safety. <a href=\"{P}profiles/samuel-tufts-15-3.html\">Profile</a>", 119, "15-3") +
  V("<strong>Samuel Tufts 2nd</strong> (41-2): born 19 Aug. 1752 in Medford; died 29 Nov. 1815; Lexington Alarm; Canada 1776; West Point 1780. <a href=\"{P}profiles/samuel-tufts-41-2.html\">Profile</a>", 160, "41-2") +
  V("<strong>Samuel Tufts 3rd</strong> (44-3): born 16 Apr. 1761 in Medford; died 29 Aug. 1803; private at West Point and in Canada. <a href=\"{P}profiles/samuel-tufts-44-3.html\">Profile</a>", 166, "44-3") +
  SIDE("death day of the Samuel born 1752", (WILD+", p. 52", "&ldquo;died Nov. 20, 1815&rdquo; (Samuel 3d)"), (TK1+", p. 160", "died 29 Nov. 1815 (Samuel 2nd, 41-2)")) +
  '<p class="note">Wild&rsquo;s Samuel b. Aug. 16, 1732 (son of Joseph and Lydia, married Hannah Tufts, died 1818) is a <strong>clean match</strong> to 15-3. Wild&rsquo;s Samuel b. April 1761 (son of Samuel and Hannah) is a <strong>clean match</strong> to 44-3. Wild&rsquo;s Samuel 3d b. 1752 is a <strong>possible match</strong> to 41-2: the year agrees, but the death day differs and Vol. I numbering (&ldquo;2nd&rdquo;) differs from Wild&rsquo;s (&ldquo;3d&rdquo;). The individual MSS entries on this page are still not assigned to any one man.</p>',
}
for _s, _h in V1MERGE.items():
    KIN[_s] = KIN.get(_s, "") + '<h3>Vol. I</h3>' + _h
for _p in PROFILES:
    if _p["slug"] == "peter-tufts-jr":
        _p.update(dates="1753 &ndash; 1832 (1836 per Wild; see conflict)", died="1832",
          unverified="A separate MSS entry, &ldquo;TUFTS, PETER. Private, Capt. Benjamin Blaney's co. &hellip;&rdquo; (p. 137), gives no town, so it is not attached to him. DAR records themselves have not been seen.")
    elif _p["slug"] == "cotton-tufts":
        _p.update(dates="1732 &ndash; 1815", born="1732",
          unverified="State senate and ratifying-convention service come only from the secondary <em>Tufts Family History</em>. The same page lists &ldquo;Cotton, Jr. (Esq), (1791-1872)&rdquo; with dates identical to &ldquo;Quincy (1791-1872)&rdquo;, an apparent error in the source (p. 35).")
    elif _p["slug"] == "caleb-tufts":
        _p.update(dates="1762 &ndash; 1852", unverified="That the MSS Caleb (Dec. 1776, Capt. Caleb Brooks's co.) is this man.")
    elif _p["slug"] == "barnabas-tufts":
        _p.update(dates="1742/3 &ndash; 1795", born="1743", died="1795", town="Medford; Gloucester (Cape Ann); Topsham, Me.",
          family="<p>Vol. II places him as Barnabas5, son of John4 (see below).</p>",
          unverified="")
    elif _p["slug"] in ("william-tufts", "samuel-tufts"):
        pass
    elif _p["slug"] == "zachariah-tufts":
        pass

# ---------- new profiles ----------
def NP(slug, name, fam, born, died, dates, town, bio, facts, unv="", line="", loyalist=False):
    body = "".join(V(t, pg, fam) for t, pg in facts)
    if loyalist:
        body = '<p class="flag"><strong>Loyalist.</strong> This man sided with the Crown during the Revolution. He is included as part of the family record, not as a Patriot soldier.</p>' + body
    PROFILES.append(dict(slug=slug, name=name, dates=dates, town=town, born=born, died=died, era="The Revolution", line=line or f"Tufts Kinsmen family no. {fam}",
        bio=bio, service=body, family=f"<p>Family number {fam} in <em>Tufts Kinsmen</em>, Vol. I. Parents are not named in the extract seen.</p>",
        unverified=(unv + " " if unv else "") + "No other source on this site has yet been checked for this man.", kicker="Loyalist" if loyalist else ""))

NP("simon-tufts-11-1", "Dr. Simon Tufts", "11-1", "", "", "[dates not in extract]", "Medford",
   "<p>Dr. Simon Tufts of Medford, older brother of Dr. Cotton Tufts (both children of family no. 11 in Tufts Kinsmen Vol. I), was an ardent Whig and a justice of the peace from 1770. When the fighting began he cared for the wounded on both sides, and he spent the war in the awkward role of guardian to a Loyalist neighbor&rsquo;s estate.</p>",
   [("Ardent Whig; justice of the peace 1770; took depositions and bound wounds after Lexington and Concord; attended the wounded on both sides at Bunker Hill; lent bounty money for the war.", 110),
    ("Reluctantly served as conservator of the estate of the Tory Col. Isaac Royall; testified before the Committee of Safety that he believed Royall a friend to the American cause; the Committee refused and ordered the estate surrendered. After Royall&rsquo;s death in 1781 the state returned the estate to Simon as trustee.", 110),
    ("Fellow of the Massachusetts Medical Society 1782; died from a fall from his horse.", 110)],
   "Birth and death dates are not in the extract. Service was civil and medical, not military.", line="Older brother of Dr. Cotton Tufts")
NP("william-tufts-13-6", "Lieut. William Tufts", "13-6", "1713", "1783", "1713 &ndash; 1783", "Charlestown; Medford",
   "<p>Lieut. William Tufts was a generation older than most of the family&rsquo;s Revolutionary soldiers. Born in Charlestown in 1713, he had helped build Fort Lawrence on the Bay of Fundy, and he died at Medford in 1783.</p>",
   [("Born 10 June 1713 in Charlestown; died 29 Oct. 1783 in Medford.", 116),
    ("Served building Fort Lawrence, Bay of Fundy, with his brother James and nephew James Jr.; described as dying in service during the Revolution.", 116)],
   "Which MSS William entry, if any, is his (possibly the 1776 2d Lieutenant in Capt. Ezekiel Knowlton&rsquo;s co.; see <a href=\"{P}profiles/william-tufts.html\">William Tufts (several men)</a>).")
NP("joseph-tufts-jr-15-2", "Capt. Joseph Tufts Jr.", "15-2", "1731", "1778", "1730/1 &ndash; 1778", "Medford",
   "<p>Capt. Joseph Tufts Jr. of Medford served the Revolution at home, on the town&rsquo;s Committee of Correspondence and Safety. He died in December 1778.</p>",
   [("Born 21 Feb. 1730/1 in Medford; died 6 Dec. 1778; married Hannah Cutter.", 119),
    ("Served on the Committee of Correspondence and Safety; also served on the Grand Jury.", 119)])
NP("samuel-tufts-15-3", "Samuel Tufts (1732&ndash;1818)", "15-3", "1732", "1818", "1732 &ndash; 1818", "Medford",
   "<p>Samuel Tufts was 42 when Paul Revere&rsquo;s alarm reached Medford, and he answered it. He later sat on the town&rsquo;s Committee of Safety, and he was the father of Revolutionary soldiers Samuel 3rd and Caleb.</p>",
   [("Born 16 Aug. 1732 in Medford; died 31 Dec. 1818; married Hannah Tufts (36-6).", 119),
    ("Answered Paul Revere&rsquo;s call to bear arms at the Lexington alarm; served on the Committee of Safety; head of household 1790&ndash;1810.", 119)],
   "Clean match to Wild, p. 53 (&ldquo;Son of Joseph and Lydia (Francis); born Aug. 16, 1732; married Hannah Tufts; died 1818&rdquo;). See also <a href=\"{P}profiles/samuel-tufts.html\">Samuel Tufts (several men)</a>.")
NP("nathan-tufts-15-7", "Nathan Tufts (1741&ndash;1784)", "15-7", "1741", "1784", "1741 &ndash; 1784", "Medford",
   "<p>Nathan Tufts of Medford supported the war with money rather than a musket, lending toward the bounties paid to enlisting men in 1776.</p>",
   [("Born 5 Oct. 1741 in Medford; died 12 June 1784; lent money for bounty in 1776.", 120)], "Financial support only; no military service recorded in the extract.")
NP("francis-tufts-20-1", "Rev. Francis Tufts", "20-1", "1744", "1833", "1744 &ndash; 1833", "Medford; Lincoln Co., Me.; Farmington, Me.; Ohio",
   "<p>Francis Tufts enlisted from the Maine frontier, served at Dorchester Heights, and lived to become a Freewill Baptist minister. In 1831, in his late eighties, he set out by wagon for Ohio, where he died two years later.</p>",
   [("Born 21 July 1744 in Medford; died 2 Oct. 1833 at Yankeetown, Ohio; Freewill Baptist minister.", "128&ndash;130"),
    ("Private, enlisting from Lincoln County, Me.: ten months in the Massachusetts militia, beginning by dislodging Tories stealing cattle on the Penobscot River; later at Tiverton, R.I., and at Dorchester Heights during the evacuation of the King&rsquo;s troops from Boston. Pension 4 Oct. 1823.", "128&ndash;130"),
    ("Built the first mill at Farmington Falls, 1788; ruling elder and deacon of the Farmington church; met his nephew Charles Tufts (later benefactor of Tufts College) in Medford before his 1831 wagon trip to Ohio.", "128&ndash;130")])
NP("james-tufts-jr-36-2", "James Tufts Jr.", "36-2", "1726", "1786", "1726 &ndash; 1786", "Medford",
   "<p>A Medford farmer, James Tufts Jr. is credited with some of the town&rsquo;s earliest acts of resistance, fetching gunsmith&rsquo;s tools from Charlestown in March 1775.</p>",
   [("Born 15 Jan. 1726 in Medford; died 5 Nov. 1786; farmer.", 152),
    ("Described as &ldquo;undoubtedly the earliest Medford man to defend acknowledged liberties in March 1775,&rdquo; citing the Benjamin Hall ledger: &ldquo;Paid James Tufts for going to Charlestown twice for gunsmith&rsquo;s tools.&rdquo;", 152),
    ("Assembled on Prospect Hill (now Somerville); marched to Dorchester Heights and Noddle&rsquo;s Island.", 152)],
   "Possible match to &ldquo;Tufts James Jr.&rdquo; on the Medford 1925 Minute Men monument; not confirmed.")
NP("ebenezer-tufts-36-7", "Ebenezer Tufts", "36-7", "1737", "1809", "1737 &ndash; 1809", "Medford",
   "<p>Ebenezer Tufts, a Medford brickburner, answered the Lexington alarm and later stood guard over the Convention Troops, Burgoyne&rsquo;s captured army.</p>",
   [("Born 18 Mar. 1737 in Medford; died 26 Feb. 1809; brickburner.", 153),
    ("Answered the Lexington alarm; private, serving as a guard of the Convention Troops; marched to Noddle&rsquo;s Island.", 153)],
   "Possible match to &ldquo;Tufts Ebenezer&rdquo; on the Medford 1925 Minute Men monument; not confirmed.")
NP("jonathan-tufts-36-8", "Jonathan Tufts", "36-8", "1739", "1784", "1739 &ndash; 1784", "Medford",
   "<p>Jonathan Tufts, brickmaker of Medford, served as a private in the lines around Boston.</p>",
   [("Born 25 Feb. 1739 in Medford; died 26 Sep. 1784; brickmaker; private, served in the lines around Boston.", 153)],
   "Possible match to &ldquo;Tufts Jonathan&rdquo; on the Medford 1925 Minute Men monument; not confirmed.")
NP("isaac-tufts-36-10", "Sgt. Isaac Tufts", "36-10", "1744", "1823", "1744 &ndash; 1823", "Medford",
   "<p>Isaac Tufts answered the Lexington alarm and served as a sergeant, including at Dorchester Heights.</p>",
   [("Born 10 Oct. 1744 in Medford; died 22 July 1823; sergeant; answered the Lexington alarm; served at Dorchester Heights.", 154)],
   "Possible match to &ldquo;Tufts Isaac Sergeant&rdquo; on the Medford 1925 Minute Men monument; the rank agrees but this is not confirmed.")
NP("william-tufts-40-2", "William Tufts Jr. (1736&ndash;1782)", "40-2", "1736", "1782", "1736 &ndash; 1782", "Medford",
   "<p>William Tufts Jr. of Medford served as a private in a company of guards near Boston late in the war, and died in 1782.</p>",
   [("Born 27 Mar. 1736 in Medford; died 27 Apr. 1782.", 158),
    ("Private in Capt. Nathan Sargent&rsquo;s Company of Guards, under Stephen Dana, Col. McIntosh&rsquo;s Regiment, Massachusetts Line (the book cites DAR 92:120).", 158),
    ("His brother Aaron (40-4) marched in the French War in 1757 for the relief of Fort William Henry and never returned.", 158)],
   "Possible match to the MSS Medford entries for Capt. Stephen Dana&rsquo;s co. (1778) and Capt. Nathan Sergant&rsquo;s co. of guards (1779); see <a href=\"{P}profiles/william-tufts.html\">William Tufts (several men)</a>.")
NP("moses-tufts-40-6", "Lieut. Moses Tufts", "40-6", "1744", "1805", "1744 &ndash; abt. 1805", "Medford; Chelsea; Newcastle, Me.",
   "<p>Moses Tufts, a schoolteacher, served as First Lieutenant in Capt. Isaac Hall&rsquo;s company at Dorchester Heights and went north with the Canadian expedition of 1776.</p>",
   [("Baptized 7 Oct. 1744 in Medford; died about 1805 at Newcastle, Me.; taught school in Medford and Chelsea.", 158),
    ("First Lieutenant in Isaac Hall&rsquo;s company at Dorchester Heights, March 1776; Canadian expedition July 1776; at Ticonderoga.", 158)])
NP("george-tufts-40-7", "George Tufts", "40-7", "1747", "1796", "1746/7 &ndash; 1796", "Medford; Concord",
   "<p>George Tufts enlisted for three years. When he went home sick in 1780, the army recorded him as a deserter.</p>",
   [("Born 10 Jan. 1746/7 in Medford; died 25 Aug. 1796 in Concord.", 159),
    ("Enlisted in the army for three years but was reported deserted in 1780 when he returned home sick.", 159)])
NP("grimes-tufts-40-8", "Lieut. Grimes Tufts", "40-8", "1748", "1808", "1748 &ndash; 1808", "Medford; Lynn",
   "<p>Grimes Tufts, a Medford brickmaker, turned out as a minuteman on the Lexington Alarm and rose to lieutenant.</p>",
   [("Born 4 Dec. 1748 in Medford; died 23 Dec. 1808 in Lynn; brickmaker.", 159),
    ("Minuteman who answered the Lexington Alarm; Lieutenant during the Revolution.", 159)])
NP("samuel-tufts-41-2", "Samuel Tufts 2nd (1752&ndash;1815)", "41-2", "1752", "1815", "1752 &ndash; 1815", "Medford",
   "<p>Samuel Tufts 2nd answered the Lexington Alarm, went to Canada in 1776, and served at West Point in 1780.</p>",
   [("Born 19 Aug. 1752 in Medford; died 29 Nov. 1815.", 160),
    ("Answered the Lexington Alarm; private, going to Canada in 1776 and to West Point, N.Y., in 1780; head of household in Medford 1790 and 1810.", 160)],
   "Possible match to Wild&rsquo;s Samuel 3d (born 1752, died Nov. 20, 1815, p. 52). The death day differs (20 vs. 29 Nov.). See <a href=\"{P}profiles/samuel-tufts.html\">Samuel Tufts (several men)</a>.")
NP("francis-tufts-41-4", "Lieut. Francis Tufts (1756&ndash;1823)", "41-4", "1756", "1823", "1756 &ndash; 1823", "Lancaster; Boston",
   "<p>At Saratoga, Francis Tufts picked up the Continental flag from a fallen standard-bearer and led his company into battle with it. Gen. Horatio Gates noticed, and he was made an ensign on the spot. After the war he ran a distillery in Boston, on the lane that came to be called Tufts Street.</p>",
   [("Born 8 May 1756 in Lancaster, Mass.; died 18 Aug. 1823 in Boston; distiller.", 160),
    ("Private and sergeant under Capt. Isaac Hall and Capt. Ephraim Wheeler, Col. Jackson&rsquo;s Regiment; later adjutant.", 160),
    ("At the Battle of Saratoga he recovered the Continental flag from a fallen standard-bearer and led his outfit into battle waving it; noticed by Gen. Horatio Gates and promoted to Ensign; promoted Lieutenant 1779.", 160),
    ("After the war lived on Essex Street, Boston, below the Liberty Tree near Kingston Street, where he set up a distillery; the lane became Tufts Street. Buried in tomb 109, Granary Burying Ground. His army dispatch case was found by a junk dealer and turned over to the Massachusetts Historical Society.", 160)],
   "")
NP("david-tufts-41-7", "Cpl. David Tufts", "41-7", "1763", "1823", "1763 &ndash; 1823", "Medford; Billerica; Lynn",
   "<p>David Tufts was at Concord on the first day of the war, aged eleven by the dates given. He later served in the Continental Army as a corporal and became Lynn&rsquo;s first express driver.</p>",
   [("Born 17 June 1763 in Medford; died 6 July 1823 in Lynn; trader, expressman, and hotel keeper.", 162),
    ("In the Battle of Concord on the first day of the Revolution; later guarded the Convention troops; joined the Continental Army at Claverack, N.Y., 1779; enlisted again at Billerica in 1781 for three years in the 2nd Massachusetts Regiment, rising from private to corporal; applied for a pension 7 Apr. 1818 at Lynn.", 162),
    ("First express driver in Lynn; kept a hotel in Market Square.", 162)],
   "Birth year 1763 would make him about 11 at Concord in 1775. This is how the extract reads; it needs checking against the page scan.")
NP("joseph-tufts-43-1", "Joseph Tufts (of Danvers)", "43-1", "", "", "[dates not in extract]", "Danvers",
   "<p>Joseph Tufts served as a private and helped pay the bounties of 1776.</p>",
   [("Private in the Revolution; lent bounty money 1776; head of household in Danvers 1820.", 164)], "Birth and death dates are not in the extract.")
NP("andrew-tufts-43-3", "Andrew Tufts", "43-3", "1761", "1836", "1761 &ndash; 1836", "Medford; Worcester",
   "<p>Andrew Tufts served as a private with the Northern Army at Saratoga.</p>",
   [("Born 6 Jan. 1761 in Medford; died 20 Apr. 1836 in Worcester; private with the Northern Army at Saratoga, N.Y.; head of household 1790 and 1800.", 164)])
NP("samuel-tufts-44-3", "Samuel Tufts 3rd (1761&ndash;1803)", "44-3", "1761", "1803", "1761 &ndash; 1803", "Medford",
   "<p>Samuel Tufts 3rd, son of Samuel and brother of Caleb, served as a private at West Point and in Canada. By trade he was a fagot maker, binding the bundles of branches used to fill deep trenches before drain pipes.</p>",
   [("Born 16 Apr. 1761 in Medford; died 29 Aug. 1803; private, with service at West Point, N.Y., and Canada.", 166),
    ("Fagot maker: bundles of branches and twigs used to fill deep trenches before drain pipes were invented.", 166)],
   "Clean match to Wild, p. 52 (&ldquo;Enlisted, 1780, for 6 mos.; age 19. Son of Samuel and Hannah (Tufts); born April, 1761&rdquo;). See <a href=\"{P}profiles/samuel-tufts.html\">Samuel Tufts (several men)</a>.")
NP("john-tufts-49-2", "John Tufts (of Prospect Hill)", "49-2", "", "", "[dates not in extract]", "Prospect Hill (Somerville)",
   "<p>John Tufts served as a private and farmed on Prospect Hill, in what is now Somerville.</p>",
   [("Private in the Revolution; farm on Prospect Hill [Somerville]; estate inventory $6,390 real estate and $1,195 personal.", 175)], "Birth and death dates are not in the extract.")
NP("john-tufts-53-3", "Cpl. John Tufts (1754&ndash;1839)", "53-3", "1754", "1839", "1754 &ndash; 1839", "Charlestown (Winter Hill)",
   "<p>John Tufts was the younger brother of Peter Tufts Jr. Ellen Chase recorded that on April 19, 1775, he was &ldquo;a lad of eighteen, being charged to stay behind and take care of things.&rdquo;</p>",
   [("Born 24 Nov. 1754 in Charlestown; died 9 Sep. 1839.", 178),
    ("Minuteman at the Lexington Alarm; Corporal in the Massachusetts militia under Capt. Isaac Hall of Medford (the book cites DAR 83:66 and 162:255).", 178),
    ("Considered non compos in 1806; dismissed from First Church, Charlestown, in 1817 to join the Second Church; estate $16,909.", 178)],
   "Possible match to &ldquo;Tufts John Corporal&rdquo; on the Medford 1925 monument.", line="Peter Tufts of Winter Hill")
NP("john-tufts-22-1", "John Tufts (of Windham, Conn.)", "22-1", "1755", "", "1755 &ndash; after 1835", "Windham, Conn.; Ashford; Stephentown, N.Y.; Ludlow, Mass.",
   "<p>John Tufts of Windham, Connecticut, served three tours: north to Ticonderoga in 1775, the siege of Boston and New York in 1776, and the Hudson Highlands in 1778.</p>",
   [("Born 25 Oct. 1755 in Windham, Conn.; died after 1835 in Ludlow, Mass. (pension file NADC 10417 is cited).", 133),
    ("April 1775 volunteered for six months in Capt. Starr&rsquo;s Co., Col. Hinman&rsquo;s Regt., Connecticut militia; marched by Kent and Canaan, Conn., Stockbridge and Sheffield, Mass., Albany, and Fort George under Gen. Philip Schuyler, to Fort Ticonderoga until discharged.", 133),
    ("January 1776 in Col. Webb&rsquo;s Regt. (Capt. Leavinsworth); at Roxbury until the British left Boston in March 1776; then entrenchments at Providence, R.I.; shipped from New London to join the army on Long Island but fell sick, was sent to a New York hospital, and went home in the fall of 1776.", 133),
    ("Spring 1778, substitute for a Pomfret draftee in Capt. Daniel Allen&rsquo;s Co., Col. Wylly&rsquo;s Regt., Gen. Parsons&rsquo;s Brigade: West Point, White Plains, and Quaker Hill. Moved to Ashford 1786, Stephentown, N.Y., and Ludlow, Mass., 1818; head of household 1820.", 133)])
NP("henry-tufts-25-1", "Henry Tufts (of Lee, N.H.)", "25-1", "1735", "", "abt. 1735 &ndash; [death not in extract]", "Boston; Newmarket and Lee, N.H.",
   "<p>Henry Tufts is the family&rsquo;s most notorious member. He signed the Association Test and served as a private, but he is remembered for his 1806 memoir of crime, imprisonment, escape, and years of doctoring learned among the Saint Francis Indians.</p>",
   [("Born about 1735; signed the Association Test of loyalty circulated by order of the Continental Congress; private in the Revolution.", "136&ndash;137"),
    ("Apprenticed as a tailor on Fleet Street, Boston&rsquo;s North End; followed his brother Thomas to Newmarket, N.H.; petitioned in Nov. 1765 for the division of Durham and the forming of the parish of Lee.", "105, 136&ndash;137"),
    ("Published his memoir, <em>The Life, Adventures, Travels and Sufferings of Henry Tufts</em>, at Dover, N.H., in 1806.", "136&ndash;137"),
    ("Convicted June 1793 and sentenced to hang on 14 Aug. 1793 (the book calls the sentence unjust); commuted to life imprisonment at Castle Island, Boston Harbor; escaped from the Salem jail in 1798.", "136&ndash;137"),
    ("Spent three years with the Saint Francis Indians of Qu&eacute;bec, learning doctoring from Molly Ockit; the town of Limerick paid him for doctoring its poor.", "136&ndash;137")],
   "The order of imprisonment and escape is as given in the extract.")
NP("thomas-tufts-25-3", "Thomas Tufts (of Lee, N.H.)", "25-3", "1757", "1834", "1757 &ndash; 1834", "Lee, N.H.",
   "<p>Thomas Tufts of Lee, New Hampshire, served as a private and later as a town highway surveyor.</p>",
   [("Born 1757; died 1834; highway surveyor; private in the Revolution.", 137)],
   "")
NP("eliphalet-tufts-25-4", "Eliphalet Tufts", "25-4", "1759", "", "1759 &ndash; after 1807", "Lee, N.H.",
   "<p>Eliphalet Tufts of Lee, New Hampshire, joined the Continental Army under Gates at Saratoga in 1777 and served on and off in New Hampshire regiments until late 1781.</p>",
   [("Born 1759; died after 1807, unmarried.", 137),
    ("Joined the Continental Army under Gen. Horatio Gates at Saratoga, 1777; at Soldiers Fortune near West Point, N.Y., 1778; mustered by Col. Wentworth into Capt. Sias&rsquo;s Co., 29 Sep. 1779; Capt. George Tuttle&rsquo;s Co., Col. Stephen Evans&rsquo;s Regt., N.H. Militia.", 137),
    ("Recruit for the three N.H. Continental regiments, mustered at Kingston, N.H., by Josiah Bartlett; served 4 July to 6 Dec. 1780, with pay for 100 miles of travel to Worcester; 1781 in Capt. Joshua Woodman&rsquo;s Co., Col. Daniel Reynolds&rsquo;s Regt., N.H. Militia, discharged 11 Nov. 1781.", 137)])
NP("samuel-tufts-28-11", "Capt. Samuel Tufts (Loyalist)", "28-11", "1758", "1819", "1758 &ndash; 1819", "Nova Scotia; Boston; near Quoddy Point, Me.",
   "<p>Samuel Tufts, a master mariner, was a Nova Scotian Loyalist. In 1782 his schooner was taken by the American frigate <em>Alliance</em> under Capt. John Barry, and he was sent to Bermuda as Barry&rsquo;s messenger.</p>",
   [("Born 2 Oct. 1758; died 14 Jan. 1819 in Boston; master mariner; Nova Scotian Loyalist.", 141),
    ("Captain of the schooner <em>Dolly</em>, sailing Bermuda to Halifax, captured 4 Aug. 1782 by the American frigate <em>Alliance</em>, Capt. John Barry, with a cargo of brown sugar, molasses, onions, and limes. (The extract says &ldquo;out of New London Conn.&rdquo;)", 141),
    ("Barry put Samuel aboard a pilot boat to Saint George with a letter to the Governor of Bermuda threatening to stay three weeks hindering shipping unless all American prisoners were released. Samuel later settled near Quoddy Point, Me.", 141)],
   "His brother Joshua Bradstreet Tufts (28-12) is recorded without Revolutionary service.", loyalist=True)
NP("simon-tufts-29-1", "Simon Tufts (Loyalist, 1750&ndash;1801)", "29-1", "1750", "1801", "1750 &ndash; 1801", "Medford; Boston; Cape Town",
   "<p>Simon Tufts, Harvard 1767, was a merchant and a committed Loyalist. He was charged with selling tea, banished, and his estate was confiscated. He died at the Cape of Good Hope on his way home from India.</p>",
   [("Born 7 Apr. 1750 in Medford; died Dec. 1801 at Cape Town, South Africa; Harvard 1767.", 142),
    ("Devout Loyalist, losing his commerce; charged in 1775 by the Boston Committee of Inspection with selling tea, examined, and made a sworn statement that the Committee published.", 142),
    ("Arrested by the Council of Massachusetts in April 1776, proscribed and banished; his estate was forfeited and confiscated in 1778. Returning home from India after the war, he fell sick in port at the Cape of Good Hope.", 142)],
   "Not to be confused with Dr. Simon Tufts (11-1).", loyalist=True)
NP("william-tuffs-35-8", "William Tuffs (1750&ndash;1848)", "35-8", "1750", "1848", "1750 &ndash; 1848", "Schoharie, N.Y.; Ohio; Elkhart, Ind.",
   "<p>William Tuffs (the family name spelled the old way) went west after the war and died in Indiana in 1848, aged ninety-seven. A DAR chapter in Elkhart bears his name.</p>",
   [("Born 20 Sep. 1750, Medford by his own pension affidavit (&ldquo;Mystic/West Medford&rdquo;), though the book notes no birth record was found and the Piscataqua wilderness of N.H. is more likely.", 150),
    ("Fully accredited Revolutionary service; also claimed War of 1812 service; on the 1840 Pensioners List.", 150),
    ("Did not return home after the war: Schoharie, N.Y. (then Albany Co.), 1790; then Pennsylvania; Streetsboro, Ohio; Michigan Territory 1834; died at Elkhart, Ind., 19 Sep. 1848; buried in Bonneville Cemetery near Bristol, Ind. The Elkhart DAR chapter is named for him.", 150),
    ("Family tales say he took part in the Boston Tea Party, but he is not listed among the Lodge of Masons participants.", 150)],
   "Birthplace is disputed in the source itself. The Tea Party story is family tradition only.")
NP("nathan-tuffs-35-9", "Nathan Tuffs (1752&ndash;1827)", "35-9", "1752", "1827", "1752 &ndash; 1827", "Portsmouth, N.H.; Bethel, Vt.",
   "<p>Nathan Tuffs fought from Lexington to Yorktown. He was an artilleryman in Knox&rsquo;s regiment, a prisoner after Fort Washington, and a three-year man in the 13th Massachusetts.</p>",
   [("Born 16 Dec. 1752 in Portsmouth, N.H.; died 5 Aug. 1827 at Bethel, Vt., unmarried; moved to Bethel 1820.", 150),
    ("Volunteer at Lexington, probably on the retreat of the King&rsquo;s troops from Concord; May 1775 enlisted at Cambridge as a private for eight months in Capt. Thomas Wait Foster&rsquo;s Co., Col. Gridley&rsquo;s [extract: &ldquo;Guidley&rsquo;s&rdquo;] Regt. of Artillery; in Dec. 1775 re-enlisted for a year in the same regiment, commanded in 1776 by Col. Knox.", 150),
    ("Credited with Bunker Hill, Bemis Heights, the capture of Burgoyne, and the surrender of Cornwallis; taken prisoner at Fort Washington in 1776 and held two months before parole.", 150),
    ("Enlisted again 20 Feb. 1777 for three years in Capt. Aaron Haines&rsquo;s Co., Col. Wigglesworth&rsquo;s 13th Regt.; honorably discharged at Snake Hill near Newburgh, N.Y.; on the pension roll 5 Mar. 1819 at $96.99 a year, receiving $885.33 in all.", 150)],
   "The extract spells the artillery colonel &ldquo;Guidley&rdquo;; Gridley is the likely reading but is not confirmed.")

KIN_BY_MARRIAGE = [
 ("Samuel Teel", "husband of Elizabeth Tufts (36-5)", "2nd Lieutenant in the Revolution.", 152, "36-5"),
 ("Isaac Greenleaf", "husband of Mary Tufts Jr. (41-1)", "Private; served at Noddle&rsquo;s Island and in New York, 1776.", 159, "41-1"),
 ("Thomas Pritchard", "husband of Lucy Tufts (41-3)", "Sergeant at the Lexington Alarm; recruiting officer after the British left Boston, commissioned Captain; commanded a company in the 1776 New York campaign, where his maneuvers won Washington&rsquo;s approval.", 160, "41-3"),
 ("Ebenezer Thompson", "husband of Hannah Tufts (44-1)", "Private, guarding the Convention Troops.", 165, "44-1"),
 ("Jonathan Foster Jr.", "husband of Susanna Tufts (52-3)", "Paid a man to go to Canada in 1776.", 176, "52-3"),
 ("Seth Stone", "husband of Mary Tufts (52-4)", "Lieutenant; later of Marlborough, N.H. (1791&ndash;94) and Pittsford, Vt.", 177, "52-4"),
 ("Joseph Adams", "husband of Anna Tufts (53-11)", "Sergeant in Capt. Oliver Titcomb&rsquo;s Co., Col. Jacob Gerrish&rsquo;s Regt., guarding Burgoyne&rsquo;s surrendered army; hauled with his oxen for the Dorchester Heights fortifications; buried a silver tankard during the war that is now used in the communion service of the Arlington church.", 181, "53-11"),
 ("Joshua Simonds", "husband of Pamela Tufts (31-4)", "Officer in the Revolution (the book cites DUDL 841).", 145, "31-4"),
 ("John Albre", "husband of Lydia Tufts (31-6)", "Officer in the Revolution (DUDL 841); lived in Salem, Acworth, N.H., and Daniels Street, Salem.", 145, "31-6"),
 ("Thomas Brooks Jr.", "husband of Mercy Tufts Jr. (11-6)", "Captain in the Revolution and Representative to the General Court.", 112, "11-6"),
]
KIN_HTML = '<section id="kin-by-marriage"><h2>Kin by Marriage</h2><p>Men who married into the Tufts family and served the Revolution. Short entries only.</p><ul>' + "".join(
    f'<li><strong>{n}</strong>, {r}: {t} <span class="cite">({TK1}, p. {pg}; {NOSCAN})</span></li>' for n, r, t, pg, f in KIN_BY_MARRIAGE) + '</ul>' + \
  f'<p class="note">Also in Vol. I but not profiled: Aaron Tufts (40-4), baptized 1740, marched from Lancaster to Springfield in 1757 for the relief of Fort William Henry in the French War and never returned (p. 158). Joshua Bradstreet Tufts (28-12, 1760&ndash;1835), brother of the Loyalist Capt. Samuel Tufts, was raised in Nova Scotia, and no Revolutionary service is recorded for him. After the war he invested with Alexander Hamilton in the Manhattan Water Co. (p. 142).</p>' + \
  '</section>'
