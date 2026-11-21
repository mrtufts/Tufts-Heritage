# Merge the two profiles of the same man, John Tufts (1754-1839):
# keep profiles/john-tufts-53-3.html as the base, fold in unique matter
# from john-tufts-1754, and turn 1754 into a redirect (same pattern as
# the Henry / Joseph merges in nas_finds_1118.py).
import os as _jm_os, json as _jm_json, re as _jm_re

_JM_KEEP = "john-tufts-53-3"
_JM_GONE = "john-tufts-1754"
_JM_MARK = "granddaughter of James Tufts of Medford"

def _jm_get(slug):
    for p in PROFILES:
        if p["slug"] == slug:
            return p
    return None

def _jm_rew_str(s):
    if not isinstance(s, str):
        return s
    s = s.replace("profiles/" + _JM_GONE + ".html", "profiles/" + _JM_KEEP + ".html")
    # leftover "see also" wording after the href is already remapped
    s = s.replace("the same man: see also John Tufts (b. 1754)", "")
    s = s.replace("the same man: see also Cpl. John Tufts (1754&ndash;1839)", "")
    s = _jm_re.sub(r">John Tufts \(b\. 1754\)<", ">Cpl. John Tufts (1754&ndash;1839)<", s)
    s = s.replace("See " + 'PL("' + _JM_KEEP + '",', "See ")  # no-op safety
    return s

def _jm_rew(obj):
    if isinstance(obj, str):
        return _jm_rew_str(obj)
    if isinstance(obj, list):
        return [_jm_rew(x) for x in obj]
    if isinstance(obj, dict):
        out = {}
        for k, v in obj.items():
            nk = _JM_KEEP if k == _JM_GONE else k
            if nk in out and k == _JM_GONE:
                continue
            out[nk] = _jm_rew(v)
        return out
    if isinstance(obj, tuple):
        return tuple(_jm_rew(list(obj)))
    return obj

def _jm_merge_rel():
    if "REL" not in globals():
        return
    gone_rels = list(REL.pop(_JM_GONE, []))
    keep_rels = list(REL.get(_JM_KEEP, []))
    seen = {s for s, _ in keep_rels}
    for s, lab in gone_rels:
        if s in (_JM_GONE, _JM_KEEP):
            continue
        if s not in seen:
            keep_rels.append((s, lab))
            seen.add(s)
    keep_rels = [(s, lab) for s, lab in keep_rels if s not in (_JM_GONE, _JM_KEEP)]
    REL[_JM_KEEP] = keep_rels
    for k in list(REL.keys()):
        new, seen = [], set()
        for s, lab in REL[k]:
            if s == _JM_GONE:
                s = _JM_KEEP
                if "same man" in lab.lower() or "see also" in lab.lower():
                    continue
            if s == k or s in seen:
                continue
            seen.add(s)
            new.append((s, lab))
        REL[k] = new

def _jm_merge_maps():
    for name in ("SP", "DAR", "WTID", "GENI", "KIN"):
        if name not in globals():
            continue
        m = globals()[name]
        if not isinstance(m, dict):
            continue
        if _JM_GONE in m:
            if _JM_KEEP not in m or not m[_JM_KEEP]:
                m[_JM_KEEP] = m[_JM_GONE]
            del m[_JM_GONE]
        for k in list(m.keys()):
            m[k] = _jm_rew(m[k])
    if "PAGE_FIGS" in globals():
        src = "profiles/%s.html" % _JM_GONE
        dst = "profiles/%s.html" % _JM_KEEP
        if src in PAGE_FIGS:
            PAGE_FIGS.setdefault(dst, [])
            for x in PAGE_FIGS.pop(src):
                if x not in PAGE_FIGS[dst]:
                    PAGE_FIGS[dst].append(x)
    if "RW_SERVICE" in globals():
        RW_SERVICE.pop(_JM_GONE, None)
        RW_SERVICE.setdefault(_JM_KEEP, "pistol")
    if "NF_REDIRECTS" in globals():
        NF_REDIRECTS["profiles/%s.html" % _JM_GONE] = _JM_KEEP + ".html"
    if "_NF_GONE" in globals() and isinstance(_NF_GONE, dict):
        _NF_GONE[_JM_GONE] = _JM_KEEP

def _jm_fold():
    keep, gone = _jm_get(_JM_KEEP), _jm_get(_JM_GONE)
    if keep is None:
        print("john_merge_1120: keep profile missing")
        return
    if gone is None:
        # Already removed in this process; still remap and ensure the redirect.
        _jm_merge_rel()
        _jm_merge_maps()
        _jm_rewrite_all_profiles()
        print("john_merge_1120: gone profile already absent; redirect kept")
        return

    keep["name"] = "Cpl. John Tufts (1754&ndash;1839)"
    keep["dates"] = "24 Nov. 1754 &ndash; 9 Sep. 1839"
    keep["born"] = "1754"
    keep["died"] = "1839"
    keep["town"] = "Winter Hill, Charlestown (now Somerville), Mass."
    keep["line"] = "Son of Peter and Anne (Adams) Tufts of Winter Hill"
    keep["era"] = gone.get("era") or keep.get("era") or "The Revolution"

    # Combined opening, then the sections already appended to 53-3 (farm, DAR).
    opening = (
        "<p>John Tufts was born on November 24, 1754, in Charlestown, the second son of "
        + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill")
        + " and " + PL("anne-adams-tufts", "Anne Adams Tufts")
        + ", and the younger brother of " + PL("peter-tufts-jr", "Peter Tufts Jr.")
        + ". On the morning of April 19, 1775, his father rode out on Paul Revere&rsquo;s alarm, "
        + "and family accounts say John was charged to stay behind and take care of things. "
        + "Ellen Chase, drawing on Jones&rsquo;s <em>Under Colonial Roofs</em>, tells what followed:</p>"
        + Q("Paul Revere's alarm took Peter to the front, his son John, a lad of eighteen, being charged to stay behind and take care of things. The boy, however, could not be pacified at home and followed on, up beyond Lexington. While crossing one of the hills he met Elizabeth Perry, crying and running from her blazing home. He guarded her to her relatives and three years later made her his bride.",
            CHS(3, 99) if "CHS" in globals() else "Ellen Chase, <em>The Beginnings of the American Revolution</em>, vol. III (1910), p. 99")
        + Q("John Tufts, the second son of Peter of Winter Hill, was a scientific farmer and gardener. During the Revolution, his father established him on the farm the house of which is now rented by the Somerville Historical society.",
            BTH(23) if "BTH" in globals() else "Edward C. Booth, &ldquo;The Tufts Family in Somerville,&rdquo; <em>Historic Leaves</em>, vol. 1 (1902&ndash;03), p. 23")
        + "<p>Booth calls that house &ldquo;the headquarters of General Lee&rdquo; (p. 23); it stayed in the family through his son "
        + PL("oliver-tufts-1801", "Oliver Tufts (1801&ndash;1883)")
        + ". Elizabeth Perry was, Booth notes, a granddaughter of James Tufts of Medford. They had thirteen children, among them John Jr.; Benjamin, a milk farmer on Washington Street; Oliver, who kept the old Lee house until his death in 1883; Leonard, father of James W. Tufts, the maker of soda-water apparatus; and Asa (Booth, pp. 23&ndash;24).</p>"
    )
    rest = keep.get("bio", "")
    # Drop the short Chase sentence that the 53-3 page opened with, and any
    # "see also the other John page" DAR pointer that belonged only to 1754.
    rest = _jm_re.sub(
        r"<p>John Tufts was the younger brother of .*?</p>",
        "",
        rest,
        count=1,
        flags=_jm_re.S,
    )
    if _JM_MARK not in keep.get("bio", ""):
        keep["bio"] = opening + rest
    keep["bio"] = _jm_rew_str(keep["bio"])

    keep["family"] = (
        "<p>Family number 53-3 in <em>Tufts Kinsmen</em>, Vol. I. Father: "
        + PL("peter-tufts-winter-hill", "Peter Tufts of Winter Hill")
        + ". Mother: " + PL("anne-adams-tufts", "Anne Adams Tufts")
        + ". Brother: " + PL("peter-tufts-jr", "Peter Tufts Jr.")
        + ". Son: " + PL("oliver-tufts-1801", "Oliver Tufts (1801&ndash;1883)")
        + ". Nephew: " + PL("peter-tufts-1774", "Peter Tufts the surveyor")
        + ".</p>"
    )
    # Keep existing service text (corporal, dates, estate); do not carry over
    # the 1754 note that no Massachusetts Soldiers and Sailors match was found.
    if not keep.get("service"):
        keep["service"] = gone.get("service", "")

    unv_parts = []
    for blob in (keep.get("unverified", ""), gone.get("unverified", "")):
        blob = (blob or "").strip()
        if not blob:
            continue
        # Death is now known from the family record; drop the pending note.
        blob = _jm_re.sub(r"<strong>Death:</strong>\s*Note: Pending further work\.\s*", "", blob)
        if blob and blob not in unv_parts:
            unv_parts.append(blob)
    extra = (
        "<strong>Number of children:</strong> Booth (pp. 23&ndash;24) names thirteen; "
        "the family record of his son Oliver calls Oliver the twelfth of twelve. "
        "Note: Pending further work."
    )
    if extra not in "".join(unv_parts):
        unv_parts.append(extra)
    keep["unverified"] = " ".join(unv_parts)

    if "SP" in globals():
        if _JM_GONE in SP and (not SP.get(_JM_KEEP)):
            SP[_JM_KEEP] = SP[_JM_GONE]

    PROFILES[:] = [p for p in PROFILES if p["slug"] != _JM_GONE]
    _jm_merge_rel()
    _jm_merge_maps()
    _jm_rewrite_all_profiles()

    # So later post-processors do not treat the stale full page as live.
    stale = "profiles/%s.html" % _JM_GONE
    if _jm_os.path.exists(stale):
        _jm_os.remove(stale)

    print("john_merge_1120: merged", _JM_GONE, "into", _JM_KEEP, "; profiles", len(PROFILES))

def _jm_rewrite_all_profiles():
    for p in PROFILES:
        for k, v in list(p.items()):
            p[k] = _jm_rew(v)

_jm_fold()

exec(open("tools/swan_brooks_1121.py").read())
