# Post-process (Nov 18): Tufts Kinsmen Vol. I citations use the book's printed page numbers.
# Earlier extracts cited PDF page numbers for pages 101 and up (printed = PDF - 73).
# Printed citations already correct and left alone: Aaron 93-4 (p. 177, on aaron-tufts and essex-privateer pages)
# and every number below 101. Also writes redirect pages for merged profiles.
import glob as _kp_glob, re as _kp_re
_KP_KEEP177 = {"profiles/aaron-tufts.html", "essex-privateer.html"}
def _kp_fix(n):
    return n - 73 if 101 <= n <= 441 else n
def _kp_page(f, h):
    out, last = [], 0
    for m in _kp_re.finditer(r"(Vol\. I,? (?:p|pp)\. )(\d+)((?:&ndash;|&#8211;|–)(\d+))?", h):
        if "Kinsmen" not in h[max(0, m.start() - 220):m.start()]:
            continue
        if h.rfind('class="link-desc"', 0, m.start()) > h.rfind('</span>', 0, m.start()):
            continue  # link summaries repeat page text that already carries printed numbers
        a = int(m.group(2)); b = int(m.group(4)) if m.group(4) else None
        if a < 101 or (a == 177 and f in _KP_KEEP177):
            continue
        rep = m.group(1) + str(_kp_fix(a)) + (m.group(3)[:-len(m.group(4))] + str(_kp_fix(b)) if b else "")
        out.append(h[last:m.start()]); out.append(rep); last = m.end()
    out.append(h[last:])
    return "".join(out)
def _kp_trim_quotes(h):
    # Vol. I is in copyright: long verbatim passages give way to the citation alone (the page text already summarises them).
    def rep(m):
        cite = m.group(2)
        if "Kinsmen" in cite and "Vol. I" in cite and "Vol. II" not in cite and len(_kp_re.sub("<[^>]+>", "", m.group(1)).split()) > 25:
            return '<p class="cite">Source: ' + cite + '</p>'
        return m.group(0)
    return _kp_re.sub(r'<blockquote>(.*?)</blockquote>\s*<p class="cite">(.*?)</p>', rep, h, flags=_kp_re.S)
def KP_finalize():
    n = 0
    for f in _kp_glob.glob("*.html") + _kp_glob.glob("profiles/*.html") + _kp_glob.glob("generations/*.html"):
        h = open(f).read()
        h2 = _kp_trim_quotes(_kp_page(f, h))
        if f == "sources.html":
            h2 = h2.replace("Vol. I (2010), pp. 105, 110&ndash;112, 116, 119&ndash;120, 128&ndash;130, 133, 136&ndash;137, 141&ndash;142, 145, 150, 152&ndash;166, 175&ndash;181.",
                            "Vol. I (2010), pp. 19, 31&ndash;39, 43, 46&ndash;47, 50&ndash;51, 55&ndash;57, 60&ndash;64, 68&ndash;69, 72, 77&ndash;93, 102&ndash;108, 150, 161, 165, 167&ndash;168, 177, 192, 243 (printed page numbers).")
        if h2 != h:
            open(f, "w").write(h2); n += 1
    try:
        NF_write_redirects()
    except NameError:
        pass
    print("kinsmen_pages_1118: files updated", n)
KP_finalize()
