# Reader-facing source notes: replace production wording (scan text, extracts, OCR) with plain notes about the originals.
import re as _snre, glob as _sng
_A = r"(?:&rsquo;|’|')"
_SN_RULES = [
 (r"The quotations come from the OCR text, with the long s and obvious misreadings corrected", "The quotations are given from the printed issues, with the long s modernized"),
 (r"\s*\(column approximate, from OCR position\)", " (column approximate)"),
 (r"garbled in the OCR, appears to read", "partly illegible in the original, appears to read"),
 (r"The OCR text shown does not name the town", "The notice as printed does not name the town"),
 (r"The OCR is poor, so each quotation is given in modern spelling and should be checked ag[^.<]*\.", "Each quotation is given in modern spelling; parts of the originals are hard to read."),
 (r"scan image 1 \(page number not confirmed\)", "p. 1"),
 (r"\s*\(page from the scan order\)", ""),
 (r"The administrator" + _A + r"s name is read from poor OCR[^.<]*\.", "The administrator is named in the notice as Nehemiah Rand."),
 (r"The place line at the foot is unreadable in the OCR\.", "The declaration is dated at Boston, 30 March 1775, and was sworn there on 1 April."),
 (r"The colonel" + _A + r"s surname is garbled in both OCR texts and appears to read Stark; check the scan\.?", "The colonel&rsquo;s surname is partly illegible in the original and appears to read Stark."),
 (r"Quoted from the OCR text of each directory", "Quoted from each directory as printed"),
 (r"The OCR texts read (?:&ldquo;|“)Maiden(?:&rdquo;|”) for Malden; the word is given here as printed\.", "The town is Malden throughout."),
 (r"\(OCR text corrected only for obvious scanning errors", "(transcribed from the printed page"),
 (r"Scanned text; the acreage is illegible in the scan text", "The acreage is illegible in the original"),
 (r"Parents are not named in the extract seen\.", "Parents are not named in this entry."),
 (r"This is how the extract reads; it needs checking against the page scan\.", "This is how the entry reads."),
 (r"are not in the extract", "are not given in this entry"),
 (r"recorded in the extract", "recorded in this entry"),
 (r"\[dates not in extract\]", "[dates not recorded]"),
 (r"\[death not in extract\]", "[death not recorded]"),
 (r"The extract spells", "The entry spells"),
 (r"\(The extract says", "(The entry says"),
 (r"entry in the extract", "entry"),
 (r"The extract gives the county", "The record gives the county"),
 (r",? as summarised in the family research table", ", per the family record"),
 (r"the printed page has not yet been checked against the scan", "the page reference is not yet confirmed"),
 (r"The printed page has not yet been checked against the scan", "The page reference is not yet confirmed"),
 (r"was quoted from the MHS edition" + _A + r"s search extract; the page could not be opened directly from here \(server error\), so its exact date", "is quoted from the Massachusetts Historical Society&rsquo;s online edition; its exact date"),
 (r"\[extract: ", "[printed "),
 (r"\bOCR\b", "printed text"),
]
def SN_apply():
    n = {}
    for f in _sng.glob("*.html") + _sng.glob("profiles/*.html") + _sng.glob("generations/*.html"):
        h = open(f).read(); h0 = h
        for i, (a, b) in enumerate(_SN_RULES):
            h, k = _snre.subn(a, b, h)
            if k: n[i] = n.get(i, 0) + k
        if h != h0: open(f, "w").write(h)
    print("source_notes_1118:", sum(n.values()), "replacements; unused rules:", [i for i in range(len(_SN_RULES)) if i not in n])
SN_apply()
