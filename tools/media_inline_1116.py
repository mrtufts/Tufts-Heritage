# Inline pictures (Nov 16): places existing repo images beside the passages that name their
# subject, and makes cropped detail images from existing originals. Uses only images already
# in assets/images; originals are never overwritten. Runs after all pages are written.
import re as _mi_re, json as _mi_json, os as _mi_os, glob as _mi_glob
try:
    from PIL import Image as _mi_Image
except ImportError:
    _mi_Image = None

# (new file, parent file, crop box as fractions l,t,r,b, detail label)
MI_CROPS = [
    ("cotton-tufts-greenleaf-1804-crop-face.jpg", "cotton-tufts-greenleaf-1804.jpg", (0.22, 0.03, 0.68, 0.40), "face"),
    ("henry-tufts-narrative-1807-crop-title.jpg", "henry-tufts-narrative-1807.jpg", (0.04, 0.04, 0.96, 0.42), "title"),
    ("map-medford-1794-crop-title.jpg", "map-medford-1794-peter-tufts.jpg", (0.02, 0.58, 0.42, 0.90), "title cartouche"),
]
_mi_man = _mi_json.load(open("manifest.json"))
_mi_man_changed = False
for _new, _par, _box, _what in MI_CROPS:
    if _par not in IMAGES:
        continue
    _dst = "assets/images/" + _new
    if not _mi_os.path.exists(_dst) and _mi_Image is not None:
        _im = _mi_Image.open("assets/images/" + _par).convert("RGB")
        _w, _h = _im.size
        _im.crop((int(_box[0]*_w), int(_box[1]*_h), int(_box[2]*_w), int(_box[3]*_h))).save(_dst, quality=90)
    _t, _cap, _who, _lic, _src, *_lab = IMAGES[_par]
    IMAGES[_new] = (f"{_t} (detail: {_what})", f"Detail ({_what}) cropped from the full image. {_cap}", _who, _lic, _src, *_lab)
    _pm = _mi_man.get("images", {}).get(_par)
    if _pm is not None and _new not in _mi_man["images"]:
        _e = dict(_pm); _e["path"] = _dst; _e["title"] = _mi_re.sub(r"<[^>]+>", "", IMAGES[_new][0]); _e["derived_from"] = _pm.get("path", "assets/images/" + _par)
        _mi_man["images"][_new] = _e; _mi_man_changed = True
if _mi_man_changed:
    open("manifest.json", "w").write(_mi_json.dumps(_mi_man, indent=2, ensure_ascii=False) + "\n")

# (regex naming the subject, image file, restrict to these pages or None for all profiles/stories)
MI_RULES = [
    (r"Narrative|memoir", "henry-tufts-narrative-1807-crop-title.jpg", ["profiles/henry-tufts-1748.html"]),
    (r"Greenleaf|portrait|physician|Weymouth", "cotton-tufts-greenleaf-1804-crop-face.jpg", ["profiles/cotton-tufts.html"]),
    (r"1794|surveyor|plan of", "map-medford-1794-peter-tufts.jpg", ["profiles/peter-tufts-jr.html", "profiles/peter-tufts-1774.html"]),
    (r"1794", "map-medford-1794-crop-title.jpg", ["places.html"]),
    (r"Anne Adams|married|born", "anne-adams-tufts-pioneer-mothers-1912.jpg", ["profiles/anne-adams-tufts.html"]),
    (r"tablet|marker|Daughters of the American Revolution|D\.A\.R\.", "anne-adams-tufts-tablet-hmdb.jpg", ["profiles/anne-adams-tufts.html"]),
    (r"Royall House|Isaac Royall&rsquo;s house", "royall-house-1920.jpg", None),
    (r"Powder House", "old-powder-house-somerville.jpg", None),
    (r"Prospect Hill", "prospect-hill-monument.jpg", None),
    (r"Dorchester Heights", "dorchester-heights-monument.jpg", None),
    (r"Ticonderoga", "ticonderoga-fort.jpg", None),
    (r"West Point", "west-point-c1780.jpg", None),
    (r"Freeman&rsquo;s Farm|Saratoga", "saratoga-freemans-farm.jpg", None),
    (r"Bunker Hill|Bunker&rsquo;s Hill|Breed&rsquo;s Hill", "trumbull-bunker-hill.jpg", None),
    (r"White Plains", "white-plains-plan-1796.jpg", None),
    (r"Fort Washington", "fort-washington-attack-1776.jpg", None),
    (r"North Bridge", "old-north-bridge-concord.jpg", None),
    (r"Noddle&rsquo;s Island|Noddles Island", "noddles-island-fort-1776.jpg", None),
    (r"Chelsea Creek", "chelsea-creek-1775.jpg", None),
    (r"Fort William Henry|Lake George", "fort-william-henry-plan.jpg", None),
    (r"Castle Island|Fort Independence|Castle William", "fort-independence-castle-island.jpg", None),
    (r"Granary Burying Ground", "granary-burying-ground.jpg", None),
    (r"Salem Street Burying Ground", "salem-street-burying-ground-marker.jpg", None),
    (r"Cradock House", "cradock-house-medford.jpg", None),
    (r"Tufts College", "tufts-college-1854.jpg", None),
    (r"Burning of Charlestown|Charlestown was burned|burned Charlestown|burning of Charlestown", "burning-of-charlestown-1775.jpg", None),
    (r"Lee, N\.\s?H\.|Lee, New Hampshire", "lee-nh-town-hall.jpg", None),
    (r"Topsham", "topsham-mason-st.jpg", None),
    (r"Farmington Falls", "farmington-falls-postcard-1907.jpg", None),
    (r"Yankeetown", "yankeetown-ohio.jpg", None),
    (r"American Academy of Arts and Sciences", "aaas-ancient-seal.png", None),
    (r"Abigail Adams", "abigail-adams-blyth.jpg", None),
    (r"Horatio Gates|Gen\. Gates|General Gates", "horatio-gates-stuart.jpg", None),
    (r"Burgoyne", "trumbull-surrender-burgoyne.jpg", None),
    (r"Schuyler", "philip-schuyler-trumbull.jpg", None),
    (r"Henry Knox|Gen\. Knox", "henry-knox-stuart.jpg", None),
    (r"Mill Prison", "mill-prison-diary-russell-1781-07-08.jpg", None),
]
MI_MAX_PER_PAGE = 2
# Mentions that name the subject only in passing (a bequest, a relative's later career): no picture.
MI_SKIP = {("profiles/nathan-tufts-1764.html", "trumbull-bunker-hill.jpg"), ("profiles/cotton-tufts.html", "trumbull-bunker-hill.jpg"),
           ("profiles/francis-tufts-20-1.html", "tufts-college-1854.jpg")}
MI_LOG = []

def _mi_ok_image(f):
    if f not in IMAGES: return False
    cap = " ".join(str(x) for x in IMAGES[f][:3])
    return not _mi_re.search(r"AI rendition|Comparable example|comparable example|not the Tufts", cap)

def _mi_place(path):
    h = open(path).read()
    pre = "../" * path.count("/")
    a = h.find("<main>"); b = h.rfind("</main>")
    if a < 0: return
    stop = len(h)
    for mk in ('<h2>Links and Resources', 'class="links-resources"', 'id="related"', '<h2>Sources', '<h2>Authoritative IDs'):
        k = h.find(mk, a)
        if 0 < k < stop: stop = k
    stop = min(stop, b)
    added = 0
    for pat, img, only in MI_RULES:
        if added >= MI_MAX_PER_PAGE: break
        if only is not None and path not in only: continue
        if only is None and not (path.startswith("profiles/") or path.startswith("stories/")): continue
        if (path, img) in MI_SKIP or not _mi_ok_image(img) or ("assets/images/" + img) in h: continue
        if not _mi_os.path.exists("assets/images/" + img): continue
        for mo in _mi_re.finditer(r"<p>(.*?)</p>", h[a:stop], _mi_re.S):
            s = a + mo.start()
            txt = mo.group(1)
            if not _mi_re.search(pat, _mi_re.sub(r"<[^>]+>", " ", txt)): continue
            before = h[a:s]
            if any(before.count("<" + t) > before.count("</" + t + ">") for t in ("blockquote", "table", "figure", "details", "ul", "ol", "nav")): continue
            if before.count('<div class="flag"') > before.count("</div>") - before.count("<div") + before.count('<div class="flag"'):  # cheap guard
                pass
            # skip paragraphs inside an Unverified box
            last_flag = before.rfind('<div class="flag"')
            if last_flag >= 0 and before.find("</div>", last_flag) < 0: continue
            fig = FIG(img, "hfig-flow mi-inline").replace("{P}", pre)
            h = h[:s] + fig + h[s:]
            stop += len(fig); b += len(fig)
            MI_LOG.append((path, img)); added += 1
            break
    if added:
        open(path, "w").write(h)

for _p in sorted(_mi_glob.glob("profiles/*.html") + _mi_glob.glob("stories/*.html") + ["places.html"]):
    if not _mi_os.path.basename(_p).startswith("_"):
        _mi_place(_p)
print("media_inline:", len(MI_LOG), "placements")
open("/tmp/media_inline_log.txt", "w").write("\n".join(f"{p}\t{i}" for p, i in MI_LOG))
