# Revolutionary War icons: musket = extensive military service;
# pistol = limited service or support of the war effort.
import re, json, pathlib
RW_SERVICE = json.load(open("data/rw_service.json"))
RW_LABEL = {
    "musket": "Revolutionary War service: extensive",
    "pistol": "Revolutionary War service: limited service or support of the war effort",
}
# Non-profile pages that still identify a classified person.
RW_HREF_SLUG = {
    "generations/colonial.html#peter-1728": "peter-tufts-winter-hill",
}

def RW_icon(slug, pre="{P}"):
    kind = RW_SERVICE.get(slug)
    if not kind:
        return ""
    return (f'<img class="rw-icon" src="{pre}assets/icons/{kind}.svg" width="22" height="10" alt="" '
            f'title="{RW_LABEL[kind]}" aria-label="{RW_LABEL[kind]}">')

def RW_mark(kind, pre="{P}"):
    """Icon for an individual service entry on a composite page (not keyed to a slug)."""
    if kind not in RW_LABEL:
        return ""
    return (f'<img class="rw-icon" src="{pre}assets/icons/{kind}.svg" width="22" height="10" alt="" '
            f'title="{RW_LABEL[kind]}" aria-label="{RW_LABEL[kind]}">')

def _add_icon_to_anchor(attrs, inner, slug, pre):
    if slug not in RW_SERVICE or 'class="rw-icon"' in inner:
        return None
    icon = RW_icon(slug, pre)
    if re.search(r'<h[1-6]\b', inner, re.I):
        inner = re.sub(r'(</h[1-6]>)', icon + r'\1', inner, count=1, flags=re.I)
    else:
        inner = inner + icon
    return f'<a {attrs}>{inner}</a>'

def RW_apply(html, pre, path=None):
    """Insert icons beside veteran names in profile links, alias links, titles, and plain-name mentions. Idempotent."""
    def _sub_profile(m):
        attrs, slug, inner = m.group(1), m.group(2), m.group(3)
        out = _add_icon_to_anchor(attrs, inner, slug, pre)
        return out if out is not None else m.group(0)
    html = re.sub(
        r'<a\s+([^>]*href="(?:(?:\.\./)*)profiles/([a-z0-9-]+)\.html"[^>]*)>(.*?)</a>',
        _sub_profile, html, flags=re.S | re.I)

    def _sub_alias(m):
        attrs, href, inner = m.group(1), m.group(2), m.group(3)
        # normalize href to a key without leading ../
        key = re.sub(r'^(?:\.\./)+', '', href)
        slug = RW_HREF_SLUG.get(key)
        if not slug:
            return m.group(0)
        out = _add_icon_to_anchor(attrs, inner, slug, pre)
        return out if out is not None else m.group(0)
    html = re.sub(
        r'<a\s+([^>]*href="((?:(?:\.\./)*)generations/colonial.html#peter-1728)"[^>]*)>(.*?)</a>',
        _sub_alias, html, flags=re.S | re.I)

    if path and path.startswith("profiles/") and path.endswith(".html"):
        slug = path[len("profiles/"):-5]
        hm = re.search(r'<header[^>]*>.*?<h1>(.*?)</h1>', html, re.S)
        if slug in RW_SERVICE and hm and 'class="rw-icon"' not in hm.group(1):
            html = re.sub(r'(<header[^>]*>\s*.*?<h1>)(.*?)(</h1>)',
                          lambda m: m.group(1) + m.group(2) + RW_icon(slug, pre) + m.group(3),
                          html, count=1, flags=re.S)

    # Plain-text mentions of Peter of Winter Hill (do not invent new wording).
    if "peter-tufts-winter-hill" in RW_SERVICE:
        icon = RW_icon("peter-tufts-winter-hill", pre)
        name_re = re.compile(
            r'Peter(?:(?:\s|&nbsp;)+Tufts)?(?:\s|&nbsp;)+of(?:\s|&nbsp;)+Winter(?:\s|&nbsp;)+Hill'
            r'(?:(?:\s|&nbsp;)*\((?:1728)(?:&ndash;|–|-)(?:1791)\))?'
        )
        def _plain(m):
            after = html[m.end():m.end()+250]
            if re.match(r'(?:\s*</[^>]+>)?\s*<img class="rw-icon"', after):
                return m.group(0)
            return m.group(0) + icon
        html = name_re.sub(_plain, html)
    return html

def RW_finalize():
    root = pathlib.Path(".")
    for p in list(root.glob("*.html")) + list(root.glob("generations/*.html")) + list(root.glob("profiles/*.html")):
        if p.name.startswith("_"):
            continue
        rel = str(p).replace("\\", "/")
        pre = "../" * rel.count("/")
        html = p.read_text()
        new_html = RW_apply(html, pre, rel)
        if new_html != html:
            p.write_text(new_html)
    people_path = pathlib.Path("data/people.json")
    people = json.loads(people_path.read_text())
    changed = False
    for rec in people:
        kind = RW_SERVICE.get(rec.get("slug"))
        if kind:
            if rec.get("rw") != kind:
                rec["rw"] = kind
                changed = True
        elif "rw" in rec:
            rec.pop("rw")
            changed = True
    if changed:
        people_path.write_text(json.dumps(people, indent=2) + "\n")
