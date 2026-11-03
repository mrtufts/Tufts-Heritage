# Openly licensed / public-domain illustrations, downloaded into assets/images/ (no hotlinking).
# Captions only name a Tufts person or house when the source file page explicitly does.
C = "https://commons.wikimedia.org/wiki/File:"
IMAGES = {
 "peter-tufts-house-medford.jpg": ("Peter Tufts House, Medford, Mass.", "The Peter Tufts House in Medford, photographed in 2005. The Wikimedia Commons description dates it to about 1678 and calls it possibly the oldest surviving gambrel roof in America. Which Peter Tufts built it is not stated in that source.", "Daderot", "CC BY-SA 3.0", C+"Peter_Tufts_House,_Medford,_Massachusetts.JPG"),
 "peter-oliver-tufts-house-somerville.jpg": ("Peter and Oliver Tufts House, Somerville, Mass.", "The Peter and Oliver Tufts House in Somerville, photographed in 2010.", "Swampyank", "CC BY-SA 3.0", C+"Peter_and_Oliver_Tufts_House_in_Somerville_MA_USA.jpg"),
 "royall-house-1920.jpg": ("Royall House, Medford, Mass. (1920)", "The Royall House in Medford, photographed on 2 November 1920. This was the estate of the Loyalist Col. Isaac Royall.", "Leon H. Abdalian (via Boston Public Library / DPLA)", "Public domain", C+"Royall_House,_Medford,_Mass._-_DPLA_-_fcd3982fa9652a304581fe95cd4c0e83.jpg"),
 "royall-house-east-facade.jpg": ("Isaac Royall House, east (front) facade", "The Isaac Royall House in Medford, front facade, photographed in 2005.", "Daderot", "CC BY-SA 3.0", C+"Isaac_Royall_House,_Medford,_Massachusetts_-_East_(front)_facade.JPG"),
 "cotton-tufts-greenleaf-1804.jpg": ("Dr. Cotton Tufts, by Benjamin Greenleaf (1804)", "Oil on canvas, 1804, by Benjamin Greenleaf (1769&ndash;1821). The source record identifies the sitter as Cotton Tufts and gives Dr. Cotton Tufts himself as the first owner.", "Benjamin Greenleaf", "Public domain", C+"Cotton_Tufts_-_Benjamin_Greenleaf.jpg"),
 "charles-tufts-c1860.jpg": ("Charles Tufts, about 1860", "Charles Tufts, identified in the source as the founder of Tufts College, about 1860.", "Hale&rsquo;s Photograph Rooms / Edwin B. Rollins", "Public domain", C+"Charles_Tufts,_founder_of_Tufts_College,_ca._1860.jpg"),
 "dorchester-heights-monument.jpg": ("Dorchester Heights Monument, South Boston", "The monument on Dorchester Heights, where American cannon forced the British out of Boston in March 1776. Photographed in 1982 for the Historic American Buildings Survey.", "Jet Lowe (HABS/HAER, Library of Congress)", "Public domain", C+"Dorchester_Heights_Monument_(Boston,_MA)_-_general_view.jpg"),
 "old-powder-house-somerville.jpg": ("Old Powder House, Somerville, Mass.", "The Old Powder House in Somerville. Wild places the homes of Peter Tufts Jr. and Daniel Tufts near it (see quotes above). Photographed in 2012.", "Daderot", "CC0", C+"Old_Powder_House_(Somerville,_Massachusetts)_-_DSC04318.JPG"),
 "prospect-hill-monument.jpg": ("Prospect Hill Monument, Somerville, Mass.", "The monument in Prospect Hill Park, Somerville, on the hill where American troops gathered and fortified in 1775. Photographed in 2012.", "Daderot", "CC0", C+"Prospect_Hill_Monument_-_Somerville,_MA_-_DSC03320.JPG"),
 "doolittle-battle-of-lexington-1775.jpg": ("The Battle of Lexington, April 19, 1775 (Doolittle, Plate I)", "A period illustration: detail of Amos Doolittle&rsquo;s 1775 engraving, made after Ralph Earl. It shows the event, not any particular Tufts.", "Amos Doolittle after Ralph Earl", "Public domain", C+"Battle_of_Lexington_Detail.jpg"),
 "trumbull-bunker-hill.jpg": ("The Battle of Bunker&rsquo;s Hill, June 17, 1775 (Trumbull)", "A period illustration: John Trumbull&rsquo;s painting of the battle, 1786.", "John Trumbull", "Public domain", C+"The_Battle_of_Bunker%27s_Hill_June_17_1775_by_John_Trumbull.jpeg"),
 "trumbull-surrender-burgoyne.jpg": ("Surrender of General Burgoyne at Saratoga, October 17, 1777 (Trumbull)", "A period illustration: John Trumbull&rsquo;s painting in the U.S. Capitol Rotunda, commissioned 1817 and completed 1821.", "John Trumbull", "Public domain", C+"Surrender_of_General_Burgoyne.jpg"),
 "henry-tufts-narrative-1807.jpg": ("A Narrative of the Life &hellip; of Henry Tufts (1807), title page", "The title page of <em>A Narrative of the Life, Adventures, Travels and Sufferings of Henry Tufts</em>, printed by Samuel Bragg Jr., Dover, N.H., 1807.", "Samuel Bragg Jr., printer", "Public domain", C+"Henry_Tufts%27_Autobiography.jpg"),
 "farmington-falls-postcard-1907.jpg": ("Farmington Falls, Maine (postcard, 1907)", "A view of Farmington Falls from a 1907 postcard. This is the place, not the mill described in the profile.", "Unknown (1907 postcard)", "Public domain", C+"View_of_Farmington_Falls,_ME.jpg"),
 "fort-independence-castle-island.jpg": ("Fort Independence, Castle Island, South Boston", "Fort Independence on Castle Island in Boston Harbor, photographed in 2005. The present fort dates from the 1800s.", "Paul Keleher", "CC BY 2.0", C+"Fort_Independence,_Castle_Island,_South_Boston.jpg"),
 "cradock-house-medford.jpg": ("Cradock House, Riverside Ave., Medford (about 1895&ndash;1905)", "The so-called Cradock House in Medford, an early colonial brick house, photographed about 1895&ndash;1905.", "Unknown photographer (via DPLA)", "Public domain", C+"Cradock_House,_350_Riverside_Ave.,_1634._-_DPLA_-_664b9bbf74579ce773177aede37bc5a0.jpg"),
}
def FIG(f):
    t, cap, who, lic, src = IMAGES[f]
    return (f'<figure class="hfig"><a href="{{P}}assets/images/{f}"><img src="{{P}}assets/images/{f}" alt="{t}" loading="lazy"></a>'
            f'<figcaption><strong>{t}.</strong> {cap}<span class="credit">Image: {who}. {lic}. <a href="{src}">Source: Wikimedia Commons</a></span></figcaption></figure>')
def GALLERY(h, files, id_="images"):
    return f'<section id="{id_}" class="gallery"><h2>{h}</h2><div class="figs">' + "".join(FIG(f) for f in files) + '</div></section>'
PAGE_FIGS = {
 "generations/colonial.html": ["peter-tufts-house-medford.jpg", "cradock-house-medford.jpg"],
 "generations/revolution.html": ["doolittle-battle-of-lexington-1775.jpg", "trumbull-bunker-hill.jpg", "dorchester-heights-monument.jpg", "trumbull-surrender-burgoyne.jpg"],
 "generations/19th-century.html": ["charles-tufts-c1860.jpg"],
 "places.html": ["peter-tufts-house-medford.jpg", "peter-oliver-tufts-house-somerville.jpg", "old-powder-house-somerville.jpg", "prospect-hill-monument.jpg", "royall-house-1920.jpg", "royall-house-east-facade.jpg", "cradock-house-medford.jpg", "dorchester-heights-monument.jpg", "fort-independence-castle-island.jpg", "farmington-falls-postcard-1907.jpg"],
 "collections.html": ["cotton-tufts-greenleaf-1804.jpg", "charles-tufts-c1860.jpg", "henry-tufts-narrative-1807.jpg"],
 "profiles/cotton-tufts.html": ["cotton-tufts-greenleaf-1804.jpg"],
 "profiles/simon-tufts-11-1.html": ["trumbull-bunker-hill.jpg", "royall-house-1920.jpg"],
 "profiles/henry-tufts-25-1.html": ["henry-tufts-narrative-1807.jpg"],
 "profiles/francis-tufts-20-1.html": ["farmington-falls-postcard-1907.jpg", "dorchester-heights-monument.jpg"],
 "profiles/francis-tufts-41-4.html": ["trumbull-surrender-burgoyne.jpg"],
 "profiles/andrew-tufts-43-3.html": ["trumbull-surrender-burgoyne.jpg"],
 "profiles/nathan-tuffs-35-9.html": ["trumbull-bunker-hill.jpg", "trumbull-surrender-burgoyne.jpg"],
 "profiles/james-tufts-jr-36-2.html": ["prospect-hill-monument.jpg", "dorchester-heights-monument.jpg"],
 "profiles/john-tufts-49-2.html": ["prospect-hill-monument.jpg"],
 "profiles/isaac-tufts-36-10.html": ["doolittle-battle-of-lexington-1775.jpg", "dorchester-heights-monument.jpg"],
 "profiles/peter-tufts-jr.html": ["old-powder-house-somerville.jpg", "dorchester-heights-monument.jpg"],
 "profiles/samuel-tufts-15-3.html": ["doolittle-battle-of-lexington-1775.jpg"],
 "profiles/ebenezer-tufts-36-7.html": ["doolittle-battle-of-lexington-1775.jpg"],
 "profiles/grimes-tufts-40-8.html": ["doolittle-battle-of-lexington-1775.jpg"],
}
CREDITS = '<section id="image-credits"><h2>Image Credits</h2><p>Illustrations are public domain or openly licensed. Each is stored on this site and linked to its source file page, which carries the full license terms. CC BY-SA images may be reused under the same license.</p><ul>' + "".join(
    f'<li><a href="{{P}}assets/images/{f}">{t}</a>. {who}. {lic}. <a href="{src}">Wikimedia Commons file page</a></li>' for f, (t, cap, who, lic, src) in IMAGES.items()) + '</ul></section>'
def EXTRA(path):
    out = ""
    if path in PAGE_FIGS:
        out += "{DIV}" + GALLERY("Pictures" if path.startswith("profiles/") else "Illustrations", PAGE_FIGS[path])
    if path == "sources.html": out += "{DIV}" + CREDITS
    return out
