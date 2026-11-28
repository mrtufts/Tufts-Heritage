# Artifacts sections (data/artifacts.json) and five profiles of the Alstead / Exeter line (28 Nov. 2026).
# Free public sources only; unverified identifications sit in red boxes ending "Note: Pending further work."
import json as _ar_json

_HURD = ('Duane Hamilton Hurd, ed., <em>History of Cheshire and Sullivan Counties, New Hampshire</em> (Philadelphia: J. W. Lewis, 1886), Alstead sketch of Timothy Tufts, '
         '<a href="https://accessgenealogy.com/new-hampshire/biographical-sketch-of-timothy-tufts.htm">transcribed at Access Genealogy</a> (printed page not confirmed)')
_FAG = "https://www.findagrave.com/memorial/30067762/james-tufts"
_MHS = "https://mths.mt.gov/Research/Compass/Facts"
_INT = "https://digitalcommons.law.ou.edu/indianserialset/1976"
_KV2 = "<em>Tufts Kinsmen</em>, Vol.&nbsp;II"
_KV1 = "<em>Tufts Kinsmen</em>, Vol.&nbsp;I"
_TBL = "timothy-tufts"
_T62, _J98, _T24, _J29, _JA = "timothy-tufts-1762", "jonas-tufts-1798", "timothy-tufts-1824", "james-tufts-1829", "james-arthur-tufts-1855"

# ---- Profiles ----
_nf_new(_T62, "Timothy Tufts Jr. (1762&ndash;1802)", "16 June 1762 &ndash; 3 Oct. 1802", "Menotomy (Arlington); Cambridge; Lynnfield, Mass.", "1762", "1802", "The Revolution",
  "Son of Timothy and Anne (Adams) Tufts; father of Jonas Tufts of Charlestown, N.H.",
  "<p>Timothy Tufts Jr. was born at Menotomy (now Arlington) on June 16, 1762, a son of " + PL(_TBL, "Timothy Tufts (1735&ndash;1805)") + " and " + PL("anne-adams-tufts", "Anne (Adams) Tufts") + ". He married at Cambridge on May 9, 1784, Beulah Prentice, daughter of Daniel and Deborah (Wyeth) Prentice, who died at Charlestown on October 30, 1795. On January 7, 1797, at Charlestown, he married Submit Flagg of Concord, born in Marlborough and baptized there in 1776. " + _KV1 + ", p.&nbsp;108, no. 54-1.</p>"
  "<p>The family record lists six children by his first wife and four by his second. The family appears to have lived at Lynnfield in 1788 and 1791; he was head of a household there in 1790 and was back in Cambridge in 1800. He died at Cambridge on October 3, 1802, and his estate was valued at $14,850 (" + _KV1 + ", p.&nbsp;108). Submit married, second, Elijah Simonds in 1807 and later lived at Charlestown, New Hampshire, where she died in 1844.</p>"
  "<p>His son " + PL(_J98, "Jonas Tufts (1798&ndash;1879)") + " carried the line to New Hampshire.</p>",
  "<p>No military service is recorded for him in the family record (" + _KV1 + ", p.&nbsp;108).</p>",
  "<p>Parents: " + PL(_TBL, "Timothy Tufts (1735&ndash;1805)") + " and " + PL("anne-adams-tufts", "Anne (Adams) Tufts") + ". Children by Beulah Prentice: Mary P., Timothy, Artemas, William, Anna and a second William. Children by Submit Flagg: Jonas, Submit, Joshua and Burr. Son " + PL(_J98, "Jonas Tufts (1798&ndash;1879)") + ".</p>",
  "<strong>Dates and places</strong> come from <em>Tufts Kinsmen</em> alone (Vol.&nbsp;I, p.&nbsp;108); the Cambridge, Charlestown and Lynnfield records behind them have not been checked here. Note: Pending further work.",
  "<ul><li><strong>Beulah Prentice</strong> (Feb. 1761 &ndash; 30 Oct. 1795), daughter of Daniel and Deborah (Wyeth) Prentice; married May 9, 1784, at Cambridge by Rev. John Miller (" + _KV1 + ", p.&nbsp;108).</li><li><strong>Submit (Mitty) Flagg</strong> (bapt. 1776 &ndash; 1844), daughter of Joseph and Abigail (Bruce) Flagg; married January 7, 1797, at Charlestown (" + _KV1 + ", p.&nbsp;108).</li></ul>",
  [(_TBL, "father Timothy Tufts (1735&ndash;1805)", "son Timothy Tufts Jr. (1762&ndash;1802)"),
   ("anne-adams-tufts", "mother Anne (Adams) Tufts", "son Timothy Tufts Jr. (1762&ndash;1802)")])

_nf_new(_J98, "Jonas Tufts (1798&ndash;1879)", "1 Sept. 1798 &ndash; 3 Sept. 1879", "Charlestown (Somerville), Mass.; Charlestown and Walpole, N.H.", "1798", "1879", "19th Century",
  "Son of Timothy Tufts Jr. and Submit (Flagg) Tufts; the first of his line in New Hampshire",
  "<p>Jonas Tufts was born at Charlestown (now Somerville), Massachusetts, on September 1, 1798, the eldest child of " + PL(_T62, "Timothy Tufts Jr.") + " and his second wife, Submit Flagg. On May 1, 1823, at Charlestown, New Hampshire, he married Sarah Labaree, born at Littleton on May 1, 1799, a daughter of Dr. Benjamin and Hannah (Farwell) Labaree. " + _KV1 + ", p.&nbsp;246, no. 135-1.</p>"
  "<p>The family record says that he settled first at South Charlestown, where he owned a large brick house, and later at Walpole, where in 1876 he bought a house on Westminster Street East. Sarah Labaree was a sister of Rev. Benjamin Labaree, president of Middlebury College (" + _KV1 + ", p.&nbsp;247). Jonas died at Walpole on September 3, 1879, and Sarah on May 1, 1893 (" + _KV1 + ", p.&nbsp;246). Find a Grave gives the same years, 1798&ndash;1879 and 1799&ndash;1893 (<a href=\"" + _FAG + "\">memorial 30067762, family links</a>).</p>"
  "<p>Of their six children, " + PL(_T24, "Timothy (1824&ndash;1901)") + " became a merchant at Alstead and " + PL(_J29, "James (1829&ndash;1884)") + ", a Middlebury graduate, a lawyer and acting governor of Montana Territory.</p>",
  "<p>No military service is recorded for him in the family record (" + _KV1 + ", pp.&nbsp;246&ndash;247).</p>",
  "<p>Father: " + PL(_T62, "Timothy Tufts Jr. (1762&ndash;1802)") + ". Mother: Submit (Flagg) Tufts. Children: " + PL(_T24, "Timothy (1824&ndash;1901)") + "; Sarah; " + PL(_J29, "James (1829&ndash;1884)") + "; Martha F.; Clarissa J.; Susan (" + _KV1 + ", p.&nbsp;246).</p>",
  "<strong>Dates and places</strong> rest on <em>Tufts Kinsmen</em>, Vol.&nbsp;I, p.&nbsp;246, and the Find a Grave years; the Charlestown, N.H., and Walpole records have not been checked here. Note: Pending further work.",
  "<ul><li><strong>Sarah Labaree</strong> (1 May 1799 &ndash; 1 May 1893), daughter of Dr. Benjamin and Hannah (Farwell) Labaree; married May 1, 1823, at Charlestown, N.H. (" + _KV1 + ", p.&nbsp;246).</li></ul>",
  [(_T62, "father Timothy Tufts Jr. (1762&ndash;1802)", "son Jonas Tufts (1798&ndash;1879)"),
   (_T24, "son Timothy Tufts of Alstead (1824&ndash;1901)", "father Jonas Tufts (1798&ndash;1879)"),
   (_J29, "son Hon. James Tufts (1829&ndash;1884)", "father Jonas Tufts (1798&ndash;1879)")])

_nf_new(_T24, "Timothy Tufts of Alstead (1824&ndash;1901)", "29 May 1824 &ndash; 17 Dec. 1901", "Charlestown and Alstead, N.H.", "1824", "1901", "19th Century",
  "Son of Jonas and Sarah (Labaree) Tufts; merchant, farmer and town treasurer of Alstead, N.H.",
  "<p>Timothy Tufts was born at Charlestown, New Hampshire, on May 29, 1824, the eldest child of " + PL(_J98, "Jonas Tufts") + " and Sarah (Labaree) Tufts. Hurd&rsquo;s county history says that he had a common-school and academy education and taught for several years, until 1844, when he went into trade as a clerk in Alstead village. In 1848 he formed a partnership with Oliver B. Campbell, and from 1851 he conducted the business alone. He kept a farm on road 28, belonged to the Congregational church, and was town treasurer for more than ten years (" + _HURD + ").</p>"
  "<p>The 1884&ndash;85 business directory lists him as &ldquo;justice of the peace, dealer in general merchandise, and farmer 200&rdquo; on Main Street, with a clerk in his store (Hamilton Child, <em>Business Directory of Cheshire County, N.H., 1884&ndash;85</em>, Alstead entries, <a href=\"https://www.familyfindings.com/2006/08/nh-alstead-directory-1884/\">transcribed at Family Findings</a>). He died at Bellows Falls, Vermont, on December 17, 1901 (" + _KV2 + ", p.&nbsp;165, no. 309-1).</p>"
  "<p>On December 29, 1849, at Alstead, he married Hannah Sophia Phillette Kingsbury. Their son " + PL(_JA, "James Arthur Tufts") + " became a professor at Phillips Exeter Academy. Timothy&rsquo;s brother was " + PL(_J29, "Hon. James Tufts") + ".</p>",
  "<p>Civil office: town treasurer of Alstead for more than ten years, and justice of the peace (" + _HURD + "; 1884&ndash;85 directory). No military service is recorded for him in the family record.</p>",
  "<p>Parents: " + PL(_J98, "Jonas Tufts (1798&ndash;1879)") + " and Sarah (Labaree) Tufts. Brother: " + PL(_J29, "Hon. James Tufts (1829&ndash;1884)") + ". Sisters: Sarah, Martha F., Clarissa J. and Susan. Children (" + _KV2 + ", p.&nbsp;405): Sophia (b. and d. May 1853); " + PL(_JA, "James Arthur (1855&ndash;1938)") + "; John T. (12 Mar. 1861 &ndash; 15 Feb. 1862); Sarah (14 Sept. 1863 &ndash; 24 Feb. 1864).</p>",
  "<strong>Death at Bellows Falls, Vt.</strong> is from <em>Tufts Kinsmen</em>, Vol.&nbsp;II, p.&nbsp;165, only; Find a Grave and other sources give the year 1901. <strong>Printed page of Hurd&rsquo;s sketch</strong> has not been confirmed. Note: Pending further work.",
  "<ul><li><strong>Hannah Sophia Phillette Kingsbury</strong> (18 Dec. 1825 &ndash; 18 Apr. 1900), daughter of Joseph and Kezia (Kingsbury) Kingsbury; married December 29, 1849, at Alstead, and died there (" + _KV2 + ", p.&nbsp;165). Hurd gives her as &ldquo;H. Sophia P., daughter of Joseph Kingsbury.&rdquo;</li></ul>",
  [(_J98, "father Jonas Tufts (1798&ndash;1879)", "son Timothy Tufts of Alstead (1824&ndash;1901)"),
   (_J29, "brother Hon. James Tufts (1829&ndash;1884)", "brother Timothy Tufts of Alstead (1824&ndash;1901)"),
   (_JA, "son James Arthur Tufts (1855&ndash;1938)", "father Timothy Tufts of Alstead (1824&ndash;1901)")])

_nf_new(_J29, "Hon. James Tufts of Montana (1829&ndash;1884)", "19 Sept. 1829 &ndash; 18 Aug. 1884", "Charlestown, N.H.; Iowa; Nebraska; Dakota, Idaho and Montana Territories", "1829", "1884", "19th Century",
  "Son of Jonas and Sarah (Labaree) Tufts; lawyer and acting governor of Montana Territory",
  "<p>James Tufts was born at Charlestown, New Hampshire, on September 19, 1829, a son of " + PL(_J98, "Jonas Tufts") + " and Sarah (Labaree) Tufts. He graduated from Middlebury College in 1855 and was admitted to the bar at Burlington, Iowa, in 1857. In 1859 he moved to Niobrara in Nebraska Territory, where he was elected probate judge and sat in the territorial legislature (" + _KV2 + ", p.&nbsp;166, no. 309-3; <a href=\"" + _FAG + "\">Find a Grave</a>; " + _HURD + ").</p>"
  "<p>In Dakota Territory he was secretary of the legislative council in 1861&ndash;62, and in 1863 he went to Idaho, where he served in the territorial House and was its first Speaker (<a href=\"" + _FAG + "\">Find a Grave</a>). He was Secretary of Montana Territory from March 28, 1867, to April 19, 1869 (<a href=\"" + _MHS + "\">Montana Historical Society, <em>Compass: Facts</em></a>). With Gov. Green Clay Smith absent, the executive duties fell to him. The Interior Department later transmitted his account for the period June 10, 1868, to July 1, 1869, as &ldquo;acting governor and ex-officio superintendent of Indian affairs&rdquo; (<a href=\"" + _INT + "\">letter of 16 Feb. 1871, U.S. Congressional Serial Set</a>).</p>"
  "<p>He was an unsuccessful candidate for Montana&rsquo;s seat as delegate to Congress and afterward returned to Niobrara to farm and practice law. He died there on August 18, 1884, and is buried at L&rsquo;Eau Qui Court Cemetery (<a href=\"" + _FAG + "\">Find a Grave</a>). Hurd calls him the brother of " + PL(_T24, "Timothy Tufts of Alstead") + ".</p>",
  "<p>Public offices: probate judge and legislator in Nebraska Territory; secretary of the council in Dakota Territory; Speaker of the first Idaho territorial House; Secretary and acting governor of Montana Territory. No military service is recorded for him in the family record (" + _KV2 + ", p.&nbsp;166).</p>",
  "<p>Parents: " + PL(_J98, "Jonas Tufts (1798&ndash;1879)") + " and Sarah (Labaree) Tufts. Brother: " + PL(_T24, "Timothy Tufts of Alstead (1824&ndash;1901)") + ". Nephew: " + PL(_JA, "James Arthur Tufts (1855&ndash;1938)") + ".</p>",
  "<strong>Dates of his acting governorship</strong> differ by source: the Montana Historical Society lists summer 1868 to summer 1869, the Interior Department account runs from June 10, 1868, to July 1, 1869, and some compilations give only March&ndash;April 1869. <strong>The year of his run for delegate</strong> is 1869 in one source and 1870 in <em>Tufts Kinsmen</em>, Vol.&nbsp;II, p.&nbsp;166, which also misprints his Middlebury year as 1885 (Hurd and Find a Grave give 1855) and credits him with the first book on Montana, which has not been located here. Note: Pending further work.",
  "<p>He did not marry (" + _KV2 + ", p.&nbsp;166).</p>",
  [(_J98, "father Jonas Tufts (1798&ndash;1879)", "son Hon. James Tufts (1829&ndash;1884)"),
   (_T24, "brother Timothy Tufts of Alstead (1824&ndash;1901)", "brother Hon. James Tufts (1829&ndash;1884)"),
   (_JA, "nephew James Arthur Tufts (1855&ndash;1938)", "uncle Hon. James Tufts (1829&ndash;1884)")])

_nf_new(_JA, "Prof. James Arthur Tufts of Phillips Exeter (1855&ndash;1938)", "26 Apr. 1855 &ndash; 21 Nov. 1938", "Alstead and Exeter, N.H.", "1855", "1938", "19th Century",
  "Son of Timothy and Hannah Sophia (Kingsbury) Tufts; teacher at Phillips Exeter Academy for fifty years",
  "<p>James Arthur Tufts, known to generations of Exeter alumni as &ldquo;Tuffy,&rdquo; was born at Alstead, New Hampshire, on April 26, 1855, the son of " + PL(_T24, "Timothy Tufts") + " and Hannah Sophia (Kingsbury) Tufts. He entered Phillips Exeter Academy in 1872, graduated from Harvard in 1878, and returned that year to teach there (" + _KV2 + ", pp.&nbsp;405&ndash;406, no. 583-2). Hurd, writing in 1886, calls him a professor at Exeter who had married Effie Locke of Arlington, Massachusetts, in 1878 and had a son and a daughter (" + _HURD + ").</p>"
  "<p>The family record says he became Odlin Professor of English in 1885 and Professor of English Literature in 1907, was secretary of the faculty from 1889, compiled the Academy&rsquo;s general catalogue of 1783&ndash;1903, and served as secretary of the New England Alumni Association of Phillips Exeter from 1891 until his death. He sat in the New Hampshire Senate from 1919 to 1922, the last year as its president, and received honorary degrees from Dartmouth (1917), the University of New Hampshire (1920) and Boston University (1928) (" + _KV2 + ", pp.&nbsp;405&ndash;406). He died at Exeter on November 21, 1938.</p>"
  "<p>His eldest child, Effie Miriam, born November 27, 1879, died on November 2, 1903, after her dress caught fire in the yard of the family home; her mother was burned trying to save her (Thomas W. Tufts, <a href=\"http://tuftsgenealogy.blogspot.com/search?q=Effie+Miriam\">Tufts Family Genealogy</a>, post of 1 Dec. 2012). Letters of condolence from that November and December are described below.</p>",
  "<p>Civil and academic service: Phillips Exeter faculty 1878 to about 1938; New Hampshire Senate 1919&ndash;1922 (" + _KV2 + ", pp.&nbsp;405&ndash;406). No military service is recorded for him in the family record.</p>",
  "<p>Parents: " + PL(_T24, "Timothy Tufts of Alstead (1824&ndash;1901)") + " and Hannah Sophia (Kingsbury) Tufts. Uncle: " + PL(_J29, "Hon. James Tufts (1829&ndash;1884)") + ". Grandfather: " + PL(_J98, "Jonas Tufts (1798&ndash;1879)") + ". Children by Effie Locke, as listed in the family record: Effie M., Irving E., Theodora, Delmont L., James A. and Helen (" + _KV2 + ", p.&nbsp;405).</p>",
  "<strong>Date of the first marriage:</strong> December 21, 1878, in <em>Tufts Kinsmen</em>, Vol.&nbsp;II, p.&nbsp;405 (Arlington records cited there); a family blog gives December 12. <strong>The death of Effie Miriam Tufts</strong> on November 2, 1903, rests on that family blog alone; the Exeter newspaper report it mentions has not been seen. <strong>The children&rsquo;s dates</strong> are in a later part of the family record that has not been consulted. Note: Pending further work.",
  "<ul><li><strong>Effie Locke</strong> (25 Nov. 1853 &ndash; 29 Oct. 1931), adopted daughter of Benjamin Delmont and Sarah (Child) Locke of Arlington; married December 21, 1878, at Arlington (" + _KV2 + ", pp.&nbsp;405&ndash;406).</li><li><strong>Ruth Burrage Kilbourn</strong> (23 Feb. 1888 &ndash; 12 Mar. 1951), daughter of William Arthur and Abbie Fletcher (Goss) Kilbourn; married May 8, 1936, at Petersham; no issue (" + _KV2 + ", p.&nbsp;406).</li></ul>",
  [(_T24, "father Timothy Tufts of Alstead (1824&ndash;1901)", "son James Arthur Tufts (1855&ndash;1938)"),
   (_J29, "uncle Hon. James Tufts (1829&ndash;1884)", "nephew James Arthur Tufts (1855&ndash;1938)"),
   (_J98, "grandfather Jonas Tufts (1798&ndash;1879)", "grandson James Arthur Tufts (1855&ndash;1938)")])

# ---- Render Artifacts sections from data/artifacts.json ----
def _ar_render(items):
    out = '<section id="artifacts"><h2>Artifacts</h2>'
    for it in items:
        if it["image"]:
            _up_img(it["image"], it["title"], it["text"], it["who"], it["lic"], it["url"], it["label"])
            out += FIG(it["image"], "hfig-flow")
        else:
            out += ('<div class="artifact-text"><p><strong>' + it["title"] + ".</strong> " + it["text"]
                    + '<span class="credit">Source: <a href="' + it["url"] + '">' + it["label"] + "</a> (" + it["who"] + ").</span></p></div>")
        if it.get("flag"):
            out += UNV(it["flag"])
    return out + "</section>"

_AR = _ar_json.load(open("data/artifacts.json", encoding="utf-8"))
_ar_by = {}
for _it in _AR:
    if _it.get("skip_profile"):
        continue
    _ar_by.setdefault(_it["profile"], []).append(_it)
for _slug, _items in _ar_by.items():
    _up_add(_slug, _ar_render(_items), 'id="artifacts"')
# Samuel (11-5) and Timothy (1735) are placed in the Unverified section as well.
for _slug in ("samuel-tufts-11-5", "timothy-tufts"):
    for _it in _ar_by[_slug]: _up_unv(_slug, _it["flag"])
_up_unv("mercy-brooks-tufts", "The invitation of 31 December 1807 is addressed to &ldquo;Mr and Mrs Tufts&rdquo;; that the lady is Mercy rests on the 2014 RR Auction catalogue&rsquo;s reading of the household, not on her name. Note: Pending further work.")
print("artifacts_1128b done")
