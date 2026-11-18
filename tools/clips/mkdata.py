import json, re
O=json.load(open("out/ocr.json")); E=json.load(open("entries.json"))
MHR='<em>The Medford Historical Register</em>'
MM='<em>The Massachusetts Magazine</em>'
NE='&ldquo;Tufts Genealogy&mdash;Earlier Generations,&rdquo; <em>New England Historical and Genealogical Register</em> 51 (July 1897)'
BG='<em>The Boston-Gazette, and Country Journal</em>'
WR='&ldquo;Medford in the War of the Revolution,&rdquo; ' + MHR + ', vol. II, no. 1 (January 1899)'
TP='&ldquo;The Mills on the Medford Turnpike,&rdquo; ' + MHR + ', vol. XXIII, no. 1 (March 1920)'
CA='&ldquo;Medford a Century Ago&mdash;1819,&rdquo; ' + MHR + ', vol. XXII, no. 4 (December 1919)'
TG='Eliza M. Gill, &ldquo;Turell Tufts and His Family Connections,&rdquo; ' + MHR + ', vol. XVIII (1915)'
# key: (title, source, targets[(file, anchor)], transcription override or None)
D={
"mhr-xxi-why-mystic-tufts-mill":("The Tufts mill below Sullivan Square", '&ldquo;Why Mystic?,&rdquo; '+MHR+', vol. XXI, no. 3 (July 1918), p. 53', [("businesses.html","(July 1918), p. 53")], None),
"mhr-xxiii-turnpike-mills-owners":("The owners of the saw and grist mills on the turnpike", TP+', p. 20', [("businesses.html","&ldquo;The Mills on the Medford Turnpike,&rdquo; pp. 20&ndash;21"),("profiles/william-tufts-1802.html","Mills on the Medford Turnpike"),("profiles/edward-tufts-1806.html","Mills on the Medford Turnpike")], None),
"mhr-xxiii-turnpike-nathan-tufts-cut":("Nathan Tufts&rsquo;s cut through the turnpike, 1834", TP+', p. 21', [("profiles/nathan-tufts-1764.html","Mills on the Medford Turnpike")], None),
"mhr-xxiii-turnpike-cutter-tufts-mill":("Gershom Cutter buys the Tufts mill, 1845", TP+', p. 21', [("businesses.html","He was mainly engaged in sawing of mahogany")], None),
"mhr-xxii-century-ago-tufts-a":("The Tufts map of 1784", CA+', p. 65', [("places.html","Medford a Century Ago")], None),
"mhr-xxii-century-ago-tufts-b":("&ldquo;The old Tufts residence&rdquo;", CA+', p. 66', [("places.html","Medford a Century Ago")], None),
"mhr-xxiv-season-portrait-watch":("The Turell portrait and the Simon Tufts watch", '&ldquo;Season of 1920&ndash;1921,&rdquo; '+MHR+', vol. XXIV, no. 3 (September 1921), pp. 66&ndash;67', [("collections.html","Season of 1920&ndash;1921"),("profiles/simon-tufts-11-1.html","Season of 1920&ndash;1921"),("profiles/turell-tufts.html","Season of 1920&ndash;1921")], None),
"mhr-xi-royall-letter":("Isaac Royall on &ldquo;my Attorney Dr Simon Tufts&rdquo;", '&ldquo;A recently discovered Letter written by Colonel Isaac Royall in 1779,&rdquo; '+MHR+', vol. XI (1908), p. 21', [("collections.html","vol. XI, p. 17. "),("profiles/simon-tufts-11-1.html","vol. XI")], None),
"mhr-xi-mill-dam-cobble-hill":("The Mill Dam between Cobble Hill and Bunker&rsquo;s Hill, January 1776", '&ldquo;The Second Battle of Bunker&rsquo;s Hill,&rdquo; '+MHR+', vol. XI, no. 2 (April 1908), p. 43', [("businesses.html","(April 1908), p. 43")], None),
"mhr-xiv-medford-incidents-crockery":("&ldquo;Medford Incidents&rdquo;: crockery left with Samuel Tufts", '&ldquo;Medford Incidents,&rdquo; '+MHR+', vol. XIV, no. 2 (April 1911), p. 55', [("collections.html","(April 1911), p. 55")], None),
"mhr-xiii-water-supply-samuel-tufts":("Samuel Tufts&rsquo;s mill-dam rights, 1800", '&ldquo;Medford&rsquo;s Water Supply,&rdquo; '+MHR+', vol. XIII, no. 3 (July 1910), p. 61', [("businesses.html","(July 1910), p. 61")], None),
"mhr-viii-loyalists-simon-tufts":("Isaac Royall leaves his estate in the care of Dr. Simon Tufts", '&ldquo;The Loyalists of Medford,&rdquo; '+MHR+', vol. VIII (July 1905), p. 55', [("collections.html","vol. VIII, p. 55")], None),
"mhr-vi-simon-tufts-letters":("&ldquo;Extracts from letters written by Simon Tufts&rdquo;", MHR+', vol. VI, p. 96', [("collections.html","vol. VI, p. 96")], None),
"mhr-xviii-turell-tufts-54":("Turell Tufts and his family", TG+', p. 54', [("profiles/turell-tufts.html","vol. XVIII (1915), p. 54")], None),
"mhr-xviii-turell-tufts-55":("Turell Tufts in town office", TG+', p. 55', [("profiles/turell-tufts.html","vol. XVIII (1915), p. 55")], None),
"mhr-xviii-residences-67":("The Tufts house at Medford Square, demolished 1867", '&ldquo;The Tufts Family Residences,&rdquo; '+MHR+', vol. XVIII (1915), p. 67', [("places.html","XVIII, p. 67"),("profiles/simon-tufts-1700.html","XVIII, p. 67"),("profiles/turell-tufts.html","(1915), p. 67")], None),
"mhr-xli-peter-tufts-house-date":("The 1668 deposition dating the Peter Tufts house", '&ldquo;The Date of the Peter Tufts House,&rdquo; '+MHR+', vol. XLI, no. 2 (June 1938), p. 30', [("places.html","(June 1938), pp. 30&ndash;31"),("profiles/peter-tufts-1617.html","(June 1938), pp. 30&ndash;31")], None),
"mhr-ii-war-revolution-30-nine-tuftses":("&ldquo;Nine Tuftses in the company&rdquo;", WR+', p. 30', [("collections.html","vol. II, no. 1 (January 1899), p. 30")], None),
"mhr-ii-war-revolution-31-simon-tufts":("John Brooks and the home of Dr. Simon Tufts", WR+', p. 31', [("generations/revolution.html","vol. II, no. 1 (January 1899), p. 31"),("profiles/simon-tufts-11-1.html","vol. II, no. 1 (January 1899), p. 31")], None),
"mhr-ii-war-revolution-41-francis-tufts":("Francis Tufts and the White Plains tradition", WR+', p. 41', [("collections.html","vol. II, no. 1 (January 1899), p. 41")], None),
"mhr-ii-war-revolution-47-aaron-tufts":("Aaron Tufts, a veteran of the six-months men", WR+', p. 47', [("collections.html","vol. II, no. 1 (January 1899), p. 47")], None),
"mhr-ii-war-revolution-39":("Lieut. Moses Tufts and Samuel Tufts hire the Canada men, 1776", WR+', p. 39', [("collections.html","(January 1899), p. 39")], None),
"mm-v5-orderly-book-francis-tufts":("&ldquo;Orderly book of Lieut. and Adjutant Francis Tufts&rdquo;", MM+', vol. 5 (1912), p. 13', [("collections.html","vol. 5 (1912), p. 13"),("profiles/francis-tufts-41-4.html","vol. 5")], None),
"mm-v6-mansfield-roster-grimes-tufts":("Grimes Tufts on the roster of Mansfield&rsquo;s regiment", MM+', vol. 6 (1913), p. 149', [("profiles/grimes-tufts-40-8.html","p. 149")], "John Upton / Grimes Tufts"),
"mm-v6-rachel-tufts-francis":("Col. Ebenezer Francis, son of Rachel (Tufts) Francis", MM+', vol. 6 (1913), p. 158', [("profiles/rachel-tufts-francis.html","p. 158"),("profiles/adam-tufts.html","p. 158")], None),
"mm-v7-grimes-tufts-sketch":("Second Lieutenant Grimes Tufts of Lynn", MM+', vol. 7 (1914), p. 44', [("profiles/grimes-tufts-40-8.html","p. 44")], None),
"nehgr-51-300-peter-2":("Capt. Peter Tufts (Peter&sup1;) in the 1897 genealogy", NE+', p. 300', [("profiles/peter-tufts-1648.html","NEHGR 51")], None),
"nehgr-51-301-sarah-hinckley":("Sarah Tufts, wife of Job Hinckley", NE+', p. 301', [("profiles/sarah-tufts-hinckley.html","NEHGR")], None),
"nehgr-51-301-james-2":("James Tufts, killed at Bloody Brook, 1675", NE+', p. 301', [("profiles/james-tufts-1675.html","NEHGR 51")], None),
"nehgr-51-302-thomas-3":("Rev. Thomas Tufts (Harvard 1701)", NE+', p. 302', [("profiles/thomas-tufts-hc1701.html","NEHGR 51")], None),
"nehgr-51-302-john-3":("Rev. John Tufts (Harvard 1708)", NE+', p. 302', [("profiles/john-tufts-hc1708.html","NEHGR 51")], None),
"nehgr-51-303-james-3":("James Tufts of Medford (James&sup2;)", NE+', p. 303', [("profiles/james-tufts-1672.html","NEHGR 51")], None),
"nehgr-51-304-peter-3":("Peter Tufts of Charlestown and Lydia Bucknam", NE+', p. 304', [("profiles/peter-tufts-1697.html","NEHGR 51"),("profiles/anne-adams-tufts.html","NEHGR")], None),
"nehgr-51-305-peter-3-children":("Children of Peter and Lydia Tufts, continued", NE+', p. 305', [("profiles/peter-tufts-1697.html","pp. 304&ndash;305"),("profiles/timothy-tufts.html","NEHGR 51")], None),
"bg-1770-07-23-harvard-masters":("Simon Tufts among the Harvard masters of arts, 1770", BG+', July 23, 1770', [("collections.html","July 23, 1770"),("profiles/simon-tufts-29-1.html","July 1770")],
  "[Masters of Arts, Harvard College, 1770, in two columns:] Thomas Bernard, Adam Winthrop, Edward Oxnard, Lemuel Cushing, Samuel Hancock, Isaac Mansfield, Josiah Moulton, John Rogers, Isaac Smith, Daniel Johnson, Simon Tufts, William Mayhew, Zephaniah Briggs, Elisha Thayer, Henry Herrick, Edmund Freeman, Burrill Devereux, Samuel Willard, Increase Sumner, Elijah Fitch &hellip; Nicholas Dudley, Abraham Wood, William Moore, William Turner, Jeremiah Shaw, Simeon Chase, Enos Hitchcock, Samuel Cheney, Asa Dunbar, Sylvanus Ames, Joseph Farrar, Nathaniel Kidder, Jonathan Frost, Asahel Morse, Aaron Bordman, William Gammage, John Porter, Amos Cotting, Moses Holt."),
"bg-1770-09-03-simon-tufts-justice":("Simon Tufts appointed a justice of the peace, 1770", BG+', September 3, 1770', [("collections.html","September 3, 1770"),("profiles/simon-tufts-11-1.html","September 3, 1770")],
  "&hellip; the same County. Simon Tufts, Esq; to be a Justice of the Peace for the County of Middlesex."),
"bg-1771-06-17-william-tufts-jun":("William Tufts, jun., first to enlist for Louisbourg", BG+', June 17, 1771', [("collections.html","June 17, 1771")],
  "Mr. William Tufts, jun. an Account of whose Death we mentioned the Third Instant, was the first Person that inlisted in the Massachusetts Service, in the Expedition against Louisbourg in 1745."),
"bg-1771-11-25-cotton-tufts-mare":("Cotton Tufts&rsquo;s black mare, stolen or strayed, 1771", BG+', November 25, 1771', [("collections.html","November 25, 1771"),("profiles/cotton-tufts.html","Boston Gazette")],
  "STOLEN or STRAY&rsquo;d on the 25th of October, from the Pasture of Cotton Tufts, Esq; in Weymouth, a black Mare, about 4 Years old, Trots all, with a large white streak in her Forehead, has a large Main, thick Neck, and full Breast, looks much like a Dutch Horse, lately bro&rsquo;t from Nova-Scotia: Whoever will bring or give information of the said Mare so that the Owner may have her again, shall be handsomely Rewarded, by Mr. John Bishop, of Medford, or Cotton Tufts, of Weymouth."),
"bg-1772-06-01-simon-tufts-representative":("&ldquo;Medford, Simon Tufts, Esq.&rdquo; in the list of representatives, 1772", BG+', June 1, 1772', [("collections.html","June 1, 1772")],
  "[From the list of towns and the members returned for them; the Medford line reads:] Medford, Simon Tufts, Esq;"),
"bg-1773-05-24-seccombe-estate":("Simon Tufts, executor of Thomas Seccombe, 1773", BG+', May 24, 1773', [("collections.html","May 24, 1773")],
  "&hellip; upon or are indebted to the Estate of Thomas Seccombe, late of Medford, deceased, are desired to apply to Simon Tufts, Esq; an Executor, or to Jonathan Patten, Attorney to Mrs. Rebeccah Seccombe, Executrix of the last Will and Testament of the Deceased, for Settlement. N. B. Business is carried on at the Shop of the Deceased as heretofore. Medford May 15 1773."),
"bg-1773-11-29-william-tufts-estate":("The estate of William Tufts of Charlestown, 1773", BG+', November 29, 1773', [("collections.html","November 29, 1773")],
  "ALL Persons having Demands on the Estate of William Tufts, late of Charlestown, in the County of Middlesex, deceased, are desired to lodge their Accounts with the Subscriber; and those who are indebted to said Estate are requested to make immediate Payment to NEHEMIAH RAND, Administrator."),
"bg-1774-10-17-mary-tufts-horse":("Two dollars reward: Mary Tufts&rsquo;s horse, 1774", BG+', October 17, 1774', [("collections.html","October 17, 1774")],
  "TWO DOLLARS REWARD. STRAYED or Stolen out of the Pasture of MARY TUFTS, in Medford, a large dark bay Horse, about 11 Years old, 15 Hands high, his Mane cut on the right side, a Star in his Forehead, White by his Nose, Trots and Paces, carries his Head low. Whoever will bring said Horse to me the Subscriber, shall have the above Reward, and all necessary Charges paid by MARY TUFTS."),
"bg-1775-04-03-simon-tufts":("Simon Tufts&rsquo;s public declaration, March 1775", BG+', April 3, 1775', [("collections.html","April 3, 1775")],
  "&hellip; esteeming the Friendship of my Countrymen of more Consequence than any Benefit that could accrue to me thereby.&mdash;I had no Intention from the Beginning of militating with the Association of the Continental Congress, and declare I will not buy or sell any more of said Article till a general Permission therefor takes place: If by the above imprudent Step with Lilly any Offence is given to my Countrymen, am sorry therefor; and hope for a Restoration to their Favour and Confidence. Boston, 30th March 1775. SIMON TUFTS. Suffolk, ss. Boston, April 1, 1775. THEN the above-named Mr. Simon Tufts made Oath to the Truth of the above-written Declaration subscribed by him. Before me, BELCHER NOYES, Justice o&rsquo;Peace."),
"bg-1776-05-09-guns-samuel-tufts":("Soldiers&rsquo; guns left at Samuel Tufts&rsquo;s house, 1776", BG+', May 9, 1776', [("collections.html","May 9, 1776"),("profiles/samuel-tufts-15-3.html","Boston Gazette"),("profiles/samuel-tufts-41-2.html","Boston Gazette")],
  "A List of guns belonging to the following men, formerly soldiers in Col. John Stark&rsquo;s [as the type appears to read] regiment, and left by the subscriber at Mr. Samuel Tufts&rsquo;s house in Medford. The owners may have them again by applying to said Tufts, paying him for his trouble of storage and advertising them."),
}
FIX=[(r"1S(\d\d)",r"18\1"),(r"1G(\d\d)",r"16\1"),(r"16S4","1684"),(r"\bi8(\d\d)",r"18\1"),(r"i820-i825and","1820&ndash;1825 and"),(r"Med ford","Medford"),(r"Maiden","Malden"),(r"Bebecca","Rebecca"),(r"Bichard","Richard"),(r"\bButh\b","Ruth"),(r"Deerfiehl","Deerfield"),(r"Ebcnezer","Ebenezer"),(r"Men\^y","Mercy"),(r"cavalrytroop","cavalry troop"),(r"sixmonths","six months"),(r"Lieut, and","Lieut. and"),(r"\(#\. e\. , Peter\)","(i. e., Peter)"),(r"166869","1668-69"),(r"18 19","1819"),(r"social \.and","social and"),(r"writhin","within"),(r"wras","was"),(r"Disorder 1 complain","Disorder I complain"),(r"into K Hampshire","into &ldquo;Hampshire"),(r"\* *See Register, Vol\. I, p\. 133\.",""),(r"\s*•\s*$",""),(r"Simon Tufts\* to Benjamin Hall, Jr\.f Omeidpore in Bengal\^","Simon Tufts to Benjamin Hall, Jr. Omeidpore in Bengal,"),(r"\b1666, and died 18 June","1666, and died 18 June"),(r"nc marched","he marched"),(r"hebecame","he became"),(r"nth Regiment","11th Regiment"),(r"July 7\. 1777","July 7, 1777"),(r"Hubbarton\. near","Hubbarton, near"),(r"X\. Y\.","N. Y."),(r"Brook's' History","Brooks&rsquo; History"),(r" \(Pope\)"," (Pope)"),(r"\b(Peter|James|John|Jonathan|Thomas|Simon),?(\d)\b",r"\1<sup>\2</sup>"),(r"Ar\. E\. Chronicle","N. E. Chronicle"),(r"1773\.\"\)","1773.)"),(r"1820,\*","1820,"),(r'"',"&quot;"),(r"^\| ","")]
out={}
for k,(t,src,tg,tr) in D.items():
    s=tr if tr else O[k]["ocr"]
    if not tr:
        for a,b in FIX: s=re.sub(a,b,s)
        s=s.replace("&quot;","&rdquo;")
        # pair quotes properly
        s=re.sub(r"&rdquo;(?=\w)","&ldquo;",s); s=re.sub(r"(^|[\s(—])&rdquo;",r"\1&ldquo;",s)
        s=s.replace("&ldquo; ","&ldquo;")
        if s[:1].islower(): s="&hellip; "+s
        if not re.search(r"[.:;!?](&rdquo;)?\)?$",s.strip()): s=s.rstrip(" ,;")+" &hellip;"
        s=s.replace("'","&rsquo;").replace("’","&rsquo;").replace("—","&mdash;").replace("£","&pound;")
        first=E[k].get("lines") and E[k]["lines"][0]>0
    e=E[k]; link=f"https://archive.org/details/{e['id']}/page/n{e['leaf']}/mode/1up"
    out[k]=dict(img=f"clip-{k}.jpg",title=t,source=src,link=link,text=s,targets=tg)
json.dump(out,open("/workspace/project-1776/data/article_clips.json","w"),indent=1,ensure_ascii=False)
print(len(out)); missing=[k for k in O if k not in D]; print("not used:",missing)
