# Dedicated Perseus and Adams Papers pass (owner request C, 2026-11-03). Each hit cited separately.
def PH_(vol, pg, doc, ch): return f'{vol}, p. {pg}. <a href="{PU(doc, ch)}">Perseus</a>'
HL = lambda v: f"<em>Historic Leaves</em> (Somerville Historical Society), vol. {v}"
MR = lambda v: f"<em>Medford Historical Register</em>, vol. {v}"
BR = "Brooks, <em>History of Medford</em>"
PERS = [
 ("early April 1775", "A Peter Tufts deposed that, a fortnight before Lexington, Col. Isaac Royall told him &ldquo;it would not do for us to resist Great Britain.&rdquo; Which Peter is not stated.", PH_(BR, 174, "2001.05.0104", 5)),
 ("1775&ndash;79", "Royall&rsquo;s letters to Dr. Simon Tufts (1727&ndash;1786) as his agent. See <a href='#doctors-letters'>Letters of the Tufts Doctors</a>.", PH_(BR, "173&ndash;175", "2001.05.0104", 5)),
 ("April 30, 1778", "General Court resolve &ldquo;On petition of Simon Tufts&rdquo; directing &ldquo;Simon Tufts, Esq., of Medford&rdquo; to deliver Royall&rsquo;s estate to the Medford committee.", PH_(BR, 179, "2001.05.0104", 5)),
 ("April&ndash;June 1778", "The same resolve (dated April 23) and Simon Tufts&rsquo;s later formal appointment as agent after the Medford selectmen certified for him.", PH_(MR("VIII"), 55, "2005.05.0008", 14)),
 ("June 17, 1775", "&ldquo;After the battle of Bunker Hill, Anne Tufts assisted in binding up the wounds of eight wounded soldiers who were brought to her house&rdquo;; later she visited Burgoyne&rsquo;s captive army on Winter Hill.", PH_(HL(1), "21&ndash;22", "2001.05.0309", 7)),
 ("April 18, 1775", "Samuel Tufts &ldquo;is said to have spread the alarm of the British march&rdquo;; his house later sheltered Gen. Greene. Tradition only.", PH_(HL(6), 15, "2001.05.0306", 2)),
 ("1775&ndash;77", "Of a Medford company of 1775: &ldquo;There were nine Tuftses &hellip; all kinsmen. Seven of them were voters in 1776-7.&rdquo;", PH_(MR("III"), 30, "2005.05.0002", 2)),
 ("October 7, 1777", "Francis Tufts at Stillwater caught up the fallen colors and bore them over the redoubt; commissioned ensign by Gates. The writer says the earlier White Plains version &ldquo;cannot be true.&rdquo;", PH_(MR("III"), "41&ndash;42", "2005.05.0002", 2)),
 ("1775&ndash;76", "&ldquo;Aaron Tufts and William Bucknam were also veterans, and had been honorably discharged from the army six months before.&rdquo;", PH_(MR("III"), 47, "2005.05.0002", 2)),
 ("1776&ndash;1793", "Timothy Tufts and Samuel Tufts in turn directed the Milk Row school; Timothy first named on October 10, 1776.", PH_(HL(3), "90&ndash;93", "2001.05.0303", 14)),
 ("1771&ndash;1783", "School committee lists naming Peter Tufts Jr. (1771&ndash;72), Timothy Tufts (1776&ndash;77, 1783) and Samuel Tufts (1778&ndash;79).", PH_(HL(4), "21&ndash;22", "2001.05.0304", 4)),
 ("1781", "&ldquo;Peter Tufts, in 1781, for twenty days spent for the town as an assessor, was voted &pound; 403 2s.&rdquo;, a mark of wartime inflation.", PH_(HL(3), 66, "2001.05.0303", 11)),
 ("before 1776", "John Brooks, later governor, trained with Dr. Simon Tufts (1727&ndash;1786) and &ldquo;went thence to the army.&rdquo;", PH_(BR, "305&ndash;307", "2001.05.0104", 9)),
]
ADM = [
 ("August 5 or 12, 1766", "John Adams, Diary", "&ldquo;drank Tea at Dr. Simons Tufts&rsquo;s at Medford.&rdquo; The editors identify him as Simon Tufts (1727&ndash;1786).", "ADMS-01-01-02-0010-0007-0001", "Diary and Autobiography of John Adams, vol. 1"),
 ("August 21, 1776", "John Adams to Abigail Adams", "Compares a man&rsquo;s small head with &ldquo;our Friend Pemberton or Dr. Simon Tufts.&rdquo;", "ADMS-04-02-02-0065", "Adams Family Correspondence, vol. 2, pp. 103&ndash;105"),
 ("August 29, 1776", "William Tudor to John Adams", "Major John Brooks &ldquo;studied Physick with Doctor Tufts of Medford.&rdquo;", "ADMS-06-05-02-0003", "Papers of John Adams, vol. 5, pp. 7&ndash;9"),
 ("March 22, 1786", "Mary Cranch to Abigail Adams", "&ldquo;Doctor Simon Tufts is thought to be in a consumtion.&rdquo;", "ADMS-04-07-02-0031", "Adams Family Correspondence, vol. 7, pp. 102&ndash;113"),
 ("May 22, 1786", "Abigail Adams to John Quincy Adams", "English papers carry claims by &ldquo;Lord Gorge Gorden, mr Simon Tufts and mr Lewis Gray&rdquo; that John Adams was paid by the French ambassador.", "ADMS-04-07-02-0063", "Adams Family Correspondence, vol. 7"),
 ("May 24, 1786", "John Adams to Mercy Otis Warren", "Same affair. The editors name the source as &ldquo;Simon Tufts Jr., a loyalist refugee,&rdquo; Cotton Tufts&rsquo;s nephew.", "ADMS-06-18-02-0162", "Papers of John Adams, vol. 18, pp. 310&ndash;312"),
 ("September 28, 1786", "Mary Cranch to Abigail Adams", "&ldquo;Doctor Simon Tufts is just gone in a consumtion.&rdquo;", "ADMS-04-07-02-0131", "Adams Family Correspondence, vol. 7, pp. 348&ndash;351"),
 ("December 31, 1786", "Mary Cranch to Abigail Adams", "&ldquo;Doctor Simon Tufts dy&rsquo;d last Sunday.&rdquo;", "ADMS-04-07-02-0165", "Adams Family Correspondence, vol. 7, pp. 420&ndash;423"),
 ("August 23, 1787", "John Quincy Adams, Diary", "A visit the editors identify as to Elizabeth Hall Tufts, widow of Dr. Simon Tufts.", "ADMS-03-02-02-0002-0008-0024", "Diary of John Quincy Adams, vol. 2"),
 ("1764&ndash;1801", "Dr. Cotton Tufts and the Adamses", "188 letters by or to Cotton Tufts. See <a href='#doctors-letters'>Letters of the Tufts Doctors</a>.", "", "Adams Papers digital edition"),
]
RP = ('<section id="perseus-adams"><h2>Revolutionary-Era Tufts in Perseus and the Adams Papers</h2><p>A search of the full texts of Brooks&rsquo;s <em>History of Medford</em>, the <em>Medford Historical Register</em> (vols. 1&ndash;30) and <em>Historic Leaves</em> (vols. 1&ndash;8) on the Perseus Digital Library, and of the Massachusetts Historical Society&rsquo;s Adams Papers digital edition, turned up these Revolutionary-era references. Each is cited separately.</p><h3>Perseus Digital Library</h3>'
  + TH.replace("<th>Correspondents</th>", "") .replace("<th>Topic</th>", "<th>Finding</th>")
  + "".join(f'<tr><td>{d}</td><td>{t}</td><td class="cite">{c}</td></tr>' for d, t, c in PERS) + '</tbody></table>'
  + UNV("Traditions are reported as the sources give them. Samuel Tufts&rsquo;s alarm ride and Anne Tufts&rsquo;s nursing rest on <em>Historic Leaves</em> alone. Which Peter Tufts gave the 1775 deposition is not identified.")
  + '<h3>Adams Papers</h3>' + TH
  + "".join(f'<tr><td>{d}</td><td>{w}</td><td>{t}</td><td class="cite"><em>{s}</em>.' + (f' <a href="{MHSV}{i}">MHS digital edition</a> &middot; <a href="{FO(i)}">Founders Online</a>' if i else "") + '</td></tr>' for d, w, t, i, s in ADM) + '</tbody></table></section>')
_EXTRA8 = EXTRA
def EXTRA(path):
    out = _EXTRA8(path)
    if path == "collections.html": out = out.replace('<section id="doctors-letters">', RP + "{DIV}" + '<section id="doctors-letters">', 1)
    if path == "profiles/simon-tufts-29-1.html": out += '{DIV}<section id="gordon-affair"><h2>The 1786 London Newspaper Affair</h2><p>In May 1786 Abigail Adams wrote of claims in the English papers by &ldquo;Lord Gorge Gorden, mr Simon Tufts and mr Lewis Gray&rdquo; that John Adams was paid by the French ambassador (<a href="' + MHSV + 'ADMS-04-07-02-0063">MHS</a>). The Adams Papers editors call the source &ldquo;Simon Tufts Jr., a loyalist refugee,&rdquo; Cotton Tufts&rsquo;s nephew (<em>Papers of John Adams</em>, vol. 18, p. 312, note. <a href="' + MHSV + 'ADMS-06-18-02-0162">MHS</a>).</p>' + UNV("That the Simon Tufts of 1786 is this man (1750&ndash;1801) is likely but is the editors&rsquo; identification.") + '</section>'
    return out
