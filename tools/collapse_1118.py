# Collapsible major h2 sections on the four long pages (Nov 18).
# Post-process after site_nav / notfound. Wraps top-level h2 sections in
# <details class="sec-fold">; does not change wording or existing ids.
import pathlib as _cf_pl, re as _cf_re

CF_PAGES = (
    "collections.html",
    "places.html",
    "profiles/cotton-tufts.html",
    "businesses.html",
)

CF_CONTROLS = (
    '<p class="sec-fold-controls">'
    '<button type="button" class="sec-fold-expand">Expand all</button>'
    ' <span aria-hidden="true">&middot;</span> '
    '<button type="button" class="sec-fold-collapse">Collapse all</button>'
    "</p>\n"
)


def _cf_main(h):
    a = h.find("<main>")
    b = h.rfind("</main>")
    return (a + 6, b) if a >= 0 and b > a else (None, None)


def _cf_top_sections(m):
    """Return (start, end) spans of top-level <section>...</section> in main text."""
    spans, depth, start = [], 0, None
    for mo in _cf_re.finditer(r"</?section\b[^>]*>", m):
        if mo.group(0).startswith("</"):
            depth -= 1
            if depth == 0 and start is not None:
                spans.append((start, mo.end()))
                start = None
        else:
            if depth == 0:
                start = mo.start()
            depth += 1
    return spans


def _cf_wrap_page(html):
    a, b = _cf_main(html)
    if a is None:
        return html, 0
    m = html[a:b]
    spans = _cf_top_sections(m)
    out, last, wrapped, intro_done = [], 0, 0, False
    for start, end in spans:
        out.append(m[last:start])
        sec = m[start:end]
        om = _cf_re.match(r"<section\b([^>]*)>\s*", sec)
        if not om:
            out.append(sec)
            last = end
            continue
        rest_at = om.end()
        hm = _cf_re.match(r"<h2([^>]*)>(.*?)</h2>", sec[rest_at:], flags=_cf_re.S)
        if not hm:
            # Intro or flag blocks with no h2 stay visible and unwrapped.
            # A leading intro section already fills the "first section stays open" role,
            # so later h2 sections all start collapsed.
            if not intro_done:
                intro_done = True
            out.append(sec)
            last = end
            continue
        h2 = hm.group(0)
        body = sec[:rest_at] + sec[rest_at + hm.end():]
        attrs = om.group(1)
        cls = _cf_re.search(r'\bclass="([^"]+)"', attrs)
        dcls = "sec-fold"
        if cls and "soon" in cls.group(1).split():
            dcls += " soon"
        open_attr = ""
        if not intro_done:
            dcls += " sec-fold-intro"
            open_attr = " open"
            intro_done = True
        out.append(
            f'<details class="{dcls}"{open_attr}>\n<summary>{h2}</summary>\n{body}\n</details>'
        )
        wrapped += 1
        last = end
    out.append(m[last:])
    m2 = "".join(out)
    if wrapped and "sec-fold-controls" not in m2:
        toc = _cf_re.search(r'<nav class="toc"[^>]*>.*?</nav>', m2, flags=_cf_re.S)
        if toc:
            ins = toc.end() - len("</nav>")
            m2 = m2[:ins] + CF_CONTROLS + m2[ins:]
        else:
            m2 = CF_CONTROLS + m2
    return html[:a] + m2 + html[b:], wrapped


def CF_finalize():
    stats = {}
    for f in CF_PAGES:
        path = _cf_pl.Path(f)
        if not path.exists():
            stats[f] = "missing"
            continue
        h2, n = _cf_wrap_page(path.read_text())
        path.write_text(h2)
        stats[f] = n
    print("collapse_1118:", stats)
    return stats


CF_finalize()
