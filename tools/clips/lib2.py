import re, json, os, subprocess
from xml.etree import ElementTree as ET
IA="/workspace/clips/ia"
def T(ws): return re.sub(r"\s+"," "," ".join(w.strip() for w,c in ws)).strip()
def box(ws):
    return (min(c[0] for w,c in ws), min(c[3] for w,c in ws), max(c[2] for w,c in ws), max(c[1] for w,c in ws))  # l,t,r,b
def leaf(id,n):
    i=-1
    for ev,el in ET.iterparse(f"{IA}/{id}.djvu.xml"):
        if el.tag=="OBJECT":
            i+=1
            if i==n:
                pars=[]
                for p in el.iter("PARAGRAPH"):
                    pl=[]
                    for ln in p.iter("LINE"):
                        ws=[(w.text or "",[int(x) for x in w.get("coords").split(",")[:4]]) for w in ln.iter("WORD")]
                        if ws: pl.append(ws)
                    if pl: pars.append(pl)
                return dict(pars=pars,w=int(el.get("width")),h=int(el.get("height")))
            el.clear()
def select(pg,pat,before=0,after=0,maxlines=22,lines=None):
    flat=[(pi,ln) for pi,p in enumerate(pg["pars"]) for ln in p]
    if lines:  # explicit (start,end) indices into flat
        sel=flat[lines[0]:lines[1]+1]
    else:
        hit=[pi for pi,p in enumerate(pg["pars"]) if re.search(pat,re.sub(r"-\s+","",T([w for l in p for w in l])),re.I)]
        if not hit: return None
        ps=set(range(max(0,hit[0]-before),hit[0]+after+1))
        sel=[(pi,ln) for pi,ln in flat if pi in ps]
        if len(sel)>maxlines:
            hl=[k for k,(pi,ln) in enumerate(sel) if re.search(pat,T(ln),re.I)] or [0]
            a=max(0,hl[0]-6); sel=sel[a:a+maxlines]
    return [ln for pi,ln in sel]
def text_of(lines):
    s=""
    for ln in lines:
        t=T(ln)
        if s.endswith("-") and not s.endswith("--"): s=s[:-1]+t
        else: s=(s+" "+t).strip()
    return s
def get_img(id,n):
    f=f"{IA}/{id}_n{n}.jpg"
    if not os.path.exists(f) or os.path.getsize(f)<5000:
        subprocess.run(["curl","-sL","-o",f,f"https://archive.org/download/{id}/page/n{n}.jpg"])
    return f
