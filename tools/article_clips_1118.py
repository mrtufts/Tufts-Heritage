# Article clippings: a cropped image of the cited section of each newspaper, magazine or journal article,
# with an inline transcription, credit and link to the full page scan. Crops are made offline by
# tools/clips/crop.py from Internet Archive page images; data/article_clips.json holds captions and text.
import json as _acj, re as _acre, os as _aco
_AC = _acj.load(open("data/article_clips.json"))
_AC_FIX = [("vol. III, p. 30.", "vol. II, no. 1 (January 1899), p. 30."),
           ("vol. III, p. 31,", "vol. II, no. 1 (January 1899), p. 31,"),
           ("vol. III, p. 41&ndash;42.", "vol. II, no. 1 (January 1899), pp. 41&ndash;42."),
           ("vol. III, p. 47.", "vol. II, no. 1 (January 1899), p. 47.")]
def _ac_year(src):
    m = _acre.findall(r"\b(1[6-9]\d\d)\b", src)
    return int(m[0]) if m else 0
def _ac_fig(k, e, pre):
    y = _ac_year(e["source"].split("<em>")[-1]) or _ac_year(e["source"])
    lic = ("Public domain (published %d)" % y) if 0 < y < 1930 else "Shown for non-commercial historical use"
    return ('<figure class="hfig hfig-flow mi-inline clip-fig" id="clip-%s"><a href="%sassets/images/%s"><img src="%sassets/images/%s" alt="Clipping: %s" loading="lazy"></a>'
            '<figcaption><strong>Clipping: %s.</strong> Detail of the page: %s.<span class="credit">Image: page scan via Internet Archive, cropped. %s. <a href="%s">Source: Internet Archive (full page)</a></span></figcaption></figure>'
            '<blockquote class="clip-text"><p>%s</p></blockquote><p class="cite">Transcription of the clipping above: %s. <a href="%s">View the page scan</a></p>'
            % (k, pre, e["img"], pre, e["img"], _acre.sub("<[^>]+>|&[a-z]+;", "", e["title"]), e["title"], e["source"], lic, e["link"], e["text"], e["source"], e["link"]))
def _ac_inside(h, i, tag):
    return h.rfind("<" + tag, 0, i) > h.rfind("</" + tag + ">", 0, i)
def _ac_row(h, i):
    a = h.rfind("<tr", 0, i); b = h.find("</tr>", i)
    return a != -1 and 'class="cite"' in h[a:b] and h.rfind("</tr>", 0, i) < a
def AC_apply():
    miss = []
    files = {}
    for k, e in _AC.items():
        for f, a in e["targets"]:
            files.setdefault(f, []).append((k, e, a))
    for f, items in files.items():
        if not _aco.path.exists(f): miss.append((f, "no file")); continue
        h = open(f).read(); h0 = h
        for o, n in _AC_FIX: h = h.replace(o, n)
        pre = "../" * f.count("/")
        for k, e, a in items:
            if ('id="clip-%s"' % k) in h: continue
            m0 = h.find("<main"); i = h.find(a, m0)
            while i != -1 and ((_ac_inside(h, i, "table") and not _ac_row(h, i)) or _ac_inside(h, i, "figure") or _ac_inside(h, i, "nav") or _ac_inside(h, i, "summary")):
                i = h.find(a, i + 1)
            if i == -1: miss.append((f, k)); continue
            if _ac_inside(h, i, "table"):
                j = h.find("</tr>", i) + 5
                h = h[:j] + '<tr class="clip-row"><td colspan="3">' + _ac_fig(k, e, pre) + '</td></tr>' + h[j:]
                continue
            ends = [x for x in (h.find("</p>", i), h.find("</li>", i), h.find("</blockquote>", i)) if x != -1]
            j = min(ends); j = h.find(">", j) + 1
            if h[j:j+40].lstrip().startswith('<p class="cite">'):
                j = h.find("</p>", j) + 4
            h = h[:j] + _ac_fig(k, e, pre) + h[j:]
        if h != h0: open(f, "w").write(h)
    if miss: print("article clips not placed:", miss)
AC_apply()
