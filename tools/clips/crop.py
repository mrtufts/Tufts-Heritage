import sys, json; sys.path.insert(0,'.')
from lib2 import *
from PIL import Image, ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES=True
Image.MAX_IMAGE_PIXELS=None
G="per_boston-gazette_the-boston-gazette-and-country-journal_"
E=json.load(open("entries.json"))
import os
ONLY=sys.argv[1:]
out=json.load(open('out/ocr.json')) if os.path.exists('out/ocr.json') else {}
for k,e in E.items():
    if ONLY and k not in ONLY: continue
    pg=leaf(e["id"],e["leaf"])
    if not pg: print(k,"NO LEAF"); continue
    if e.get("until"):
        flat=[ln for p in pg["pars"] for ln in p]
        a=[i for i,l in enumerate(flat) if re.search(e["pat"],T(l))][0]
        b=[i for i,l in enumerate(flat) if i>=a and re.search(e["until"],T(l))][0]
        e["lines"]=[a,b]
    if e.get("around"):
        flat=[ln for p in pg["pars"] for ln in p]
        h=[i for i,l in enumerate(flat) if re.search(e.get("pat","Tufts"),T(l))][0]
        e["lines"]=[max(0,h-e["around"][0]),h+e["around"][1]]
    ls=select(pg,e.get("pat","Tufts"),e.get("before",0),e.get("after",0),e.get("max",22),e.get("lines"))
    if e.get("only") and k not in sys.argv[1:]: pass
    if not ls: print(k,"NO HIT"); continue
    l=min(box(x)[0] for x in ls); t=min(box(x)[1] for x in ls); r=max(box(x)[2] for x in ls); b=max(box(x)[3] for x in ls)
    im=Image.open(get_img(e["id"],e["leaf"])); sx=im.width/pg["w"]; sy=im.height/pg["h"]
    pad=int(25*sx)
    crop=im.crop((max(0,int(l*sx)-pad),max(0,int(t*sy)-pad),min(im.width,int(r*sx)+pad),min(im.height,int(b*sy)+pad)))
    if crop.width>1400: crop=crop.resize((1400,int(crop.height*1400/crop.width)))
    crop.convert("RGB").save(f"out/{k}.jpg",quality=85)
    out[k]=dict(ocr=text_of(ls),size=crop.size,full=im.size)
    print(k,crop.size,"|",out[k]["ocr"][:150])
json.dump(out,open("out/ocr.json","w"),indent=1)
