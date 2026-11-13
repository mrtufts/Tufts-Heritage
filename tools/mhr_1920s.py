# Medford Historical Register vols. XXII-XXIV (1919-1921) finds, daily research run 2026-11-12.
MHRIA = "https://archive.org/details/"
_R1920 = f'<em>Medford Historical Register</em>, vol. XXIII, no. 1 (March 1920), &ldquo;The Route of Revere,&rdquo; pp. 21&ndash;22. <a href="{MHRIA}medfordhistorica36medf">Internet Archive</a>'
_S1921 = f'<em>Medford Historical Register</em>, vol. XXIV, no. 3 (Sept. 1921), &ldquo;Season of 1920&ndash;1921,&rdquo; pp. 66&ndash;67. <a href="{MHRIA}medfordhistorica36medf">Internet Archive</a>'
_C1919 = f'<em>Medford Historical Register</em>, vol. XXII, no. 4 (Dec. 1919), &ldquo;Medford a Century Ago&mdash;1819,&rdquo; pp. 65&ndash;66. <a href="{MHRIA}medfordhistorica35medf">Internet Archive</a>'
_ROLL = [("Sergeant Isaac Tufts","isaac-tufts-36-10"),("Corporal John Tufts",None),("James Tufts, Jr.","james-tufts-jr-36-2"),("Samuel Tufts, 3d","samuel-tufts-3d"),("Samuel Tufts","samuel-tufts"),("Jonathan Tufts","jonathan-tufts-36-8"),("Daniel Tufts","daniel-tufts"),("Peter Tufts, Jr.","peter-tufts-jr"),("Ebenezer Tufts","ebenezer-tufts-36-7")]
_ROLL_HTML = ", ".join((f'<a href="{{P}}profiles/{s}.html">{n}</a>' if s else n) for n, s in _ROLL)
TURELL_PORTRAIT = f'''<section id="turell-portrait"><h2>Portrait of the Rev. Ebenezer Turell</h2>
<p><strong>Tufts association:</strong> Bequeathed by the Rev. Ebenezer Turell, Medford&rsquo;s second minister, to the young <a href="{{P}}profiles/turell-tufts.html">Turell Tufts (1770&ndash;1842)</a>, his namesake, who in turn left it to the First Parish church in 1842.</p>
{Q("At the &ldquo;Item &mdash; I give to little Turell Tufts . . . that my shadow may remain&rdquo; the portrait of Ebenezer Turell thus bequeathed was displayed by Mr. Fiske, who had procured it from the First Parish Church for the occasion. At the &ldquo;item, I give to Simon Tufts my watch&rdquo; a silver watch with chain and seal was passed around for inspection.", _S1921 + ", reporting the Medford Historical Society&rsquo;s February 1921 meeting, at which Mr. Mann read a copy of the minister&rsquo;s will made at the Probate office")}
<p>The watch shown at that meeting was not Mr. Turell&rsquo;s own; the Register says it had belonged to Dr. Daniel Osgood and was &ldquo;doubtless similar to Mr. Turell&rsquo;s.&rdquo; Its present whereabouts, and the portrait&rsquo;s, have not been checked since 1921.</p>
{UNV("Which Simon Tufts received the minister&rsquo;s watch is not stated in the Register; Dr. Simon Tufts (1727&ndash;1786), father of Turell Tufts, is the likeliest, but the will itself has not been read here. Note: Pending further work.")}
</section>'''
APRIL1775 = f'''<section id="medford-april-1775"><h2>Medford Houses and Men of April 19, 1775</h2>
<p><strong>Tufts association:</strong> Captain Peter Tufts&rsquo;s brick house (the <a href="{{P}}places.html#homesteads">Peter Tufts House</a>) is one of the few Medford houses the Register could say were standing when Paul Revere rode through, and nine Tufts men are on the town&rsquo;s Lexington alarm roll.</p>
{Q("Of the outlying ones, the brick house of Captain Peter Tufts, that of Nathaniel Wade, the Rogers house on Cross street and the Richard Sprague house on old Ship street, we are sure of.", _R1920)}
<p>The same article calls the roll of the fifty-nine Medford men of Capt. Isaac Hall&rsquo;s company who marched that day. The Tufts names on it are {_ROLL_HTML}. Their service is cited from <em>Massachusetts Soldiers and Sailors</em> on each profile.</p>
</section>'''
MAP1794_NOTE = f'<p id="map-1794-1819">A century later the Register judged the 1794 Tufts plan of Medford &ldquo;probably correct in scale, and, filling requirements, &hellip; a model of pathetic brevity,&rdquo; useful for the location of the meeting-house and mills but giving &ldquo;but little information relative to housing or business&rdquo; ({_C1919}). The Register misprints the year of the resolve as 1784.</p>'
_EXTRA_MHR20 = EXTRA
def EXTRA(path):
    out = _EXTRA_MHR20(path)
    if path == "collections.html": out = "{DIV}" + TURELL_PORTRAIT + out
    if path == "places.html": out = "{DIV}" + APRIL1775 + '<section id="maps-1819-note"><h2>The 1794 Medford Plan, Seen in 1919</h2>' + MAP1794_NOTE + '<p>See <a href="{P}places.html#maps">Maps</a>.</p></section>' + out
    if path == "profiles/turell-tufts.html":
        out += '{DIV}<section id="turell-bequest"><h2>The Minister&rsquo;s Bequest</h2><p>The portrait he left to the church had come to him as a child under the will of the Rev. Ebenezer Turell, who died in 1778.</p>' + Q("I give to little Turell Tufts . . . that my shadow may remain", _S1921) + '<p>See <a href="{P}collections.html#turell-portrait">Collections: Portrait of the Rev. Ebenezer Turell</a>.</p></section>'
    if path == "profiles/simon-tufts-11-1.html":
        out += '{DIV}<section id="turell-watch"><h2>The Rev. Mr. Turell&rsquo;s Watch</h2>' + Q("I give to Simon Tufts my watch", _S1921 + ", quoting the will of the Rev. Ebenezer Turell") + UNV("That this Simon Tufts is Dr. Simon Tufts (1727&ndash;1786) is likely but not confirmed. Note: Pending further work.") + '<p>See <a href="{P}collections.html#turell-portrait">Collections</a>.</p></section>'
    if path == "profiles/peter-tufts-1648.html":
        out += '{DIV}<p>His brick house was still standing in Medford on April 19, 1775 (' + _R1920 + '); see <a href="{P}places.html#medford-april-1775">Places</a>.</p>'
    for n, s in _ROLL:
        if s and path == f"profiles/{s}.html":
            out += '{DIV}<section id="route-of-revere"><h2>Medford Roll of April 19, 1775</h2><p>Listed as &ldquo;' + n + '&rdquo; on the Medford roll of Capt. Isaac Hall&rsquo;s company called in &ldquo;The Route of Revere&rdquo; (' + _R1920 + '). See <a href="{P}places.html#medford-april-1775">Places</a>.</p></section>'
    return out
exec(open("tools/amos_mill_1113.py").read())
