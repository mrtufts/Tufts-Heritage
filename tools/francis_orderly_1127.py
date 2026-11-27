# Francis Tufts orderly book, Huntington mssHM 719 vol. 13 (7 Apr–30 May 1782).
# Transcription of Huntington digital images 1–9 of 94 (front cover through manuscript p. 6).
# Images are not hosted; each [Page] heading links to the Huntington Digital Library.

_OB13 = "{P}stories/francis-tufts-orderly-book-1782.html"
_HDL = "https://hdl.huntington.org/digital/collection/p15150coll7/id/{}/"
_LOC = "https://snaccooperative.org/vocab_administrator/resources/8073795"
_MHS = "https://www.masshist.org/collection-guides/view/fa0052"
_MM1 = "https://www.mainememory.net/record/157810"
_MM2 = "https://www.mainememory.net/record/157893"
_H14 = _HDL.format("43338")
_H15 = _HDL.format("42920")
_H16 = _HDL.format("44399")
_H635 = _HDL.format("42481")
_H13 = "https://hdl.huntington.org/digital/collection/p15150coll7/id/44274/"
_CRED_ORIG = "Original: The Huntington Library, San Marino, California, mssHM 719 vol. 13."
_CRED_TR = "Transcription prepared for Tufts Lineage &amp; Legacy; unclear readings are marked [?]."

def _ob_page(n, ptr, label, text):
    import html as _html
    url = _HDL.format(ptr)
    body = _html.escape(text.strip("\n"), quote=False)
    return (
        f'<p class="ob-page" id="image-{n:03d}"><a href="{url}">[{label}]</a></p>\n'
        f"<pre>{body}</pre>\n"
    )

_INTRO = (
    '<p>In the spring of 1782, Lieut. '
    + PL("francis-tufts-41-4", "Francis Tufts")
    + " was adjutant of Col. Michael Jackson&rsquo;s 8th Massachusetts Regiment, then with the Continental Army in the Hudson Highlands. An adjutant&rsquo;s orderly book was the daily register of general, brigade, garrison, and regimental orders. This volume, kept at West Point and the neighboring posts, runs from 7 April to 30 May 1782. Tufts signed the inside cover, &ldquo;Francis Tufts Lieut. &amp; Adj.<sup>t</sup> / April 7<sup>th</sup> 1782.&rdquo;</p>"
    + "<p>The book now at the Huntington Library (mssHM 719 vol. 13) is one of a longer series in his hand. The immediately preceding volume, 10 January to 8 April 1782, is at the Library of Congress (MMC-1239, microfilm 16,806; "
    + f'<a href="{_LOC}">catalog description</a>'
    + "). Later volumes from 1782 and 1783 are also at the Huntington ("
    + f'<a href="{_H14}">mssHM 719 vol. 14</a>, '
    + f'<a href="{_H15}">vol. 15</a>, '
    + f'<a href="{_H16}">vol. 16</a>, and a clothing and pay book, '
    + f'<a href="{_H635}">mssHM 635</a>'
    + "). Others are at the Massachusetts Historical Society ("
    + f'<a href="{_MHS}">Ms. N-1687, microfilm P-394</a>'
    + ") and the Maine Historical Society (Coll. 1507; "
    + f'<a href="{_MM1}">vol. 1</a> and <a href="{_MM2}">vol. 2</a> on the Maine Memory Network).</p>'
    + '<p>The transcription below follows the wording, spelling, abbreviations, and lineation of the manuscript. Words written above the line are placed in the text with a caret (for example, Head Quarters^new). Unclear readings are marked [?]. Each heading links to the corresponding page image in the Huntington Digital Library. The images themselves are not reproduced here.</p>'
    + f'<p class="cite">{_CRED_ORIG}</p>'
    + f'<p class="cite">{_CRED_TR}</p>'
)

_PROGRESS = (
    '<p class="ob-progress"><strong>Transcription in progress: pages 1&ndash;9 of 94.</strong> '
    "The pages below run from the front cover through manuscript page 6 (Huntington digital images 1&ndash;9). "
    "The index on digital image 3 has not yet been transcribed. The remaining images, through 30 May 1782, will follow.</p>"
)

_TR = (
    _ob_page(1, "44180", "Page 1. Front cover",
"""From the 7th of April to
the Last of May 1782~
No 16th
[A short word written sideways on the lower right is not yet clearly read.]""")
    + _ob_page(2, "44181", "Page 2. Inside front cover",
"""Orderly Book,
8th Massachusetts Regiment
Francis Tufts Lieut. & Adj.t
April 7th 1782.
[Written sideways at the right edge:] No 8. Draft[?]

[Later bookplate on the lower flyleaf:]
EX LIBRIS
W. K. BIXBY""")
    + _ob_page(3, "44182", "Page 3. Index",
"""[Not yet transcribed. The leaf is a dense manuscript index of subjects with page numbers.]""")
    + _ob_page(4, "44183", "Page 4. Manuscript p. 1",
"""1
Head Quarters^new Newburgh April 7th 1782
The Trial of Major General
McDougall having been delayed by
his objecting to the president, and
some of the members of the court
martial, which was constituted for
the purpose of trying him, and
there being no rule established in
our military code of laws, by which
the right or limitation of challenges
is ascertained; but the president
and members excepted against, having expressed
a desire to be excused from that
duty, it is therefore ordered
that a Major General Howe pre
side at the said court, and
that other members be appointed
in the places of those who have
been challang'd, and decline serving
as also of those who may be absent,
the court will asemble at West
Point, or some convenient place
in the vicinity of it, on Wednesday
next. ——
The Commander in chief
will review the 1st and 2d Connecticut
Brigades, on Thursday next at eleven
oClock. ——
Highlands April 8th 1782
Major Genl Heaths Orders
The special General court
martial whereof Lt Col Commandant
Brooks is president, is dissolved. ——
The general court martial
whereof Major general Howe is appoint""")
    + _ob_page(5, "44184", "Page 5. Manuscript p. 2",
"""2
president. Agreable to the order of the
Commander in chief of the 7th Instant,
is to sit at West Point on Wednesday
next 10 oClock A.M. of which all
concerned will please to take notice
and attend. The court will be
composed of the following members
viz. Brigadier generals James
Clinton & Paterson, Colonels Shepard
Swift, Michael Jackson & Henry
Jackson, Lieut Colonels Commandants
Brooks, Smith, & Sherman, Lieut
Colonels, Pope, Huntington, & Gray,
As soon as the gun Boat is repair
ed, she is to be manned and
take the stationary in the river,
oposit the guard[?] at Fort Montgomery
General Paterson will please
to have it done, after which no vessel
or boat, is to pass down the river
between sun setting and rising,
without permission in writing. ——
Was Tried at the general court
martial of which a Major Darby is pre
=sident, Stephen Wit a soldier,
charged with deserting from the 5th
Massachusetts regiment. The court
from the circumstances of the
prisoners case, adjudge him not
guilty of desertion, and that the
public have no claim on him
for service. The general approves
the opinion of the court, and
orders Wit released from confine
=ment
Garrison Orders April 8th 1782
For the day tomorrow    Lt Col Pope
                         Insp.r Williams""")
    + _ob_page(6, "44185", "Page 6. Manuscript p. 3",
"""3
Brigade Orders April 9th 1782
Adj't tomorrow Marble          Detail
                               Fatigue
Highlands April 9th 1782
Major Ashley is appointed a
member of the general court
martial, whereof Major General^Howe is
president, vice Lieut. Colonel Hunting
=ton, who is indisposed. ——
Garrison Orders April 10th 1782
For the day tomorrow    Major Gibbs
                         Insp.r Williams[?]
Brigade Orders Apr 10th 1782
Adj't tomorrow [Jerry?]
Regimental Orders April 10th 82
At a regimental court martial
whereof Captain Wade was president
Serjeant Major Linsey[?]
of the 8th Massachusetts regiment, was
tryed, charged with violating the orders
of an officer immediately on their be
ing communicated to him, and
for a breach of good order and military
discipline in his Quarters on the
evening of the 6th instant
The court after mature deliberat
=ion, find the prisoner guilty
of the charge, and having considered
the circumstances of the case, sentence
the prisoner to be reprimanded
by the command^ing officer of the
regiment, at the head of the
regiment. The Major Commandt
approves of the opinion of the court,""")
    + _ob_page(7, "44186", "Page 7. Manuscript p. 4",
"""4
But is ^sorry to find that the Serjeant
Major is so ignorant of his duty, and
general orders as to suffer such noise
and racket in the regiment at such
unseasonable hours by those under his
command, and not still it, but join
the party, and refuse an order for
silence, when sent by a commiss
=ioned officer, which is very unmilitary
and unsoldierlike conduct. ——
And orders the prisoner released
from confinement. ——
After Garrison Orders Apr 10th 1782
The troop will beat in future
at eight oclock. ——
The Brigade Quartermaster
will return to Mr Carthy imme
=diately, all the tools which
were drawn for the use of the
troops in hutting last Winter;
and the gentlemen who may have
borrowed of the garrison Quarter
master for their own particular
use are requested to return them as
soon as may be. ——
Garrison Orders April 11th 1782
For the day tomorrow    Major B. Porter
                         Insp.r Williams
Brigade Orders April 11th 1782
Adj't tomorrow Tufts. Sub. for S Oliver
Garrison Orders April 12th 1782
Officer tomorrow    Major Hewitt[?]
                    Insp.r Williams
Brigade Orders April 12th 1782
Adj't tomorrow Marble""")
    + _ob_page(8, "44187", "Page 8. Manuscript p. 5",
"""5
Head Quarters Near Newburgh April 10th 1782
The Regimental Pay Master of
the Massachusetts line, will apply
immediately to Mr Lieut ^the State
Clothier, for as many uniform
coats as will compleat their respec
tive regiments, and put them
into the hands of the regimental
and other taylors imployed by
the public, that they may be
fitted to the men without loss
of time. ——
The Commanding officer
of regiments in the Massachusetts
line, will please to determine
by lot or otherwise, which four
regiment shall be compleated
with Breeches, from the supply
in the hands of their State
Clothier; the pay master of the
regiments, to whom lots they fall
will apply to receive them, with
^their coats. —— The remaining regiments
and the Connecticut line, will
make application to the Assistant
Clothier general for the cloath
and trimmings for their breeches.
The general is exceedingly
concerned to observe, the distressed
State of several corps, for the
want of clothing, he hopes
the embarrassments they have
labor'd under on that account,
are nearly removed, he earnestly
intreates and exhorts, officers of""")
    + _ob_page(9, "44188", "Page 9. Manuscript p. 6",
"""6
every description, to use their
utmost exertions to have the
clothing furnished, and distributed
as early as possible, and particu
larly, that they will pay the
greatest attention to every article
exactly suited in size, and shape,
to the individual to whom it is
designed, nothing can be more
essential than this to the good
appearance of the troops, and
nothing more detrimental than
the want of it. ——
All deserters and prisoners
coming from the enemys lines
are to be sent immediately to
head quarters. ——
Highlands April 12th 1782
Timothy Carter a soldier in the
[8th?] Massachusetts Regiment, acting
as assistant Forage Master to the
[1st?] Massachusetts Brigade, tryed at
the general court martial
whereof Major darby is president,
for disobedience of orders, defraud
ing and abusing Mr Davis, an
inhabitant of Smith clove, &
imbezzeling and selling public
forage to the inhabitants of
Smith clove. The court are of
opinion that he is guilty of
disobeying the orders of Lieut
Trot[?], Quarter Master to the
[The last line continues on the following leaf, not yet transcribed.]""")
)

page(
    "stories/francis-tufts-orderly-book-1782.html",
    "Orderly Book of Lieut. Francis Tufts, 1782 | Tufts Lineage &amp; Legacy",
    "A Primary Source",
    "Orderly Book of Lieut. Francis Tufts, April&ndash;May 1782",
    "8th Massachusetts Regiment, kept at West Point and the Hudson Highlands",
    '<section id="the-book"><h2>The Adjutant&rsquo;s Book, Spring 1782</h2>'
    + _INTRO
    + "</section>{DIV}"
    + '<section id="transcription"><h2>The Transcription</h2>'
    + _PROGRESS
    + '<div class="ob-trans">\n'
    + _TR
    + "</div>"
    + f'<p class="cite">{_CRED_ORIG} {_CRED_TR} '
    + f'<a href="{_H13}">View the volume in the Huntington Digital Library</a>.</p>'
    + "</section>",
)

# Update the existing orderly-book section on Francis's profile: the book has now been located.
_OLD_UNV = UNV(
    "The list gives no dates for Francis Tufts. That he is the Francis Tufts of this page, who rose to adjutant in Col. Jackson&rsquo;s regiment (the 8th Massachusetts), is likely but not stated. Where the orderly book is held today has not been traced. Note: Pending further work."
)
_NEW_OB = (
    '<p>The volume listed there, 10 January to 8 April 1782, is at the Library of Congress (MMC-1239, microfilm 16,806; '
    + f'<a href="{_LOC}">catalog description</a>). '
    + "The next volume in the series, 7 April to 30 May 1782, is at the Huntington Library, San Marino, California, mssHM 719 vol. 13. "
    + "Francis Tufts signed it on the inside cover as lieutenant and adjutant of the 8th Massachusetts Regiment. "
    + 'A transcription of the opening leaves is on <a href="'
    + _OB13
    + '">Orderly Book of Lieut. Francis Tufts, April&ndash;May 1782</a>.</p>'
    + "<p>Other orderly books in his hand are also at the Huntington ("
    + f'<a href="{_H14}">vol. 14</a>, <a href="{_H15}">vol. 15</a>, <a href="{_H16}">vol. 16</a>, and '
    + f'<a href="{_H635}">mssHM 635</a>'
    + "), the Massachusetts Historical Society ("
    + f'<a href="{_MHS}">Ms. N-1687, microfilm P-394</a>'
    + "), and the Maine Historical Society (Coll. 1507; "
    + f'<a href="{_MM1}">vol. 1</a> and <a href="{_MM2}">vol. 2</a>).</p>'
)
for _p in PROFILES:
    if _p["slug"] == "francis-tufts-41-4" and _OLD_UNV in _p.get("bio", ""):
        _p["bio"] = _p["bio"].replace(_OLD_UNV, _NEW_OB)
        break

_FO_EXTRA = EXTRA
def EXTRA(path):
    out = _FO_EXTRA(path)
    if path == "collections.html":
        _sec = (
            '{DIV}<section id="francis-tufts-orderly-book"><h2>Lieut. Francis Tufts&rsquo;s Orderly Book, 1782</h2>'
            '<p>Lieut. '
            + PL("francis-tufts-41-4", "Francis Tufts")
            + ", adjutant of the 8th Massachusetts Regiment, kept a series of orderly books in 1777&ndash;1783. "
            "A transcription of the Huntington volume for 7 April&ndash;30 May 1782 (mssHM 719 vol. 13) is on "
            f'<a href="{_OB13}">Orderly Book of Lieut. Francis Tufts, April&ndash;May 1782</a>.</p></section>'
        )
        if 'id="francis-tufts-orderly-book"' not in out:
            if '<section id="muskets">' in out:
                out = out.replace('<section id="muskets">', _sec + "{DIV}" + '<section id="muskets">', 1)
            else:
                out += _sec
    if path == "sources.html":
        _li = (
            "<li>Orderly book of the 8th Massachusetts Regiment, 7 April&ndash;30 May 1782, kept by Lieut. and Adjutant Francis Tufts. "
            "The Huntington Library, San Marino, California, mssHM 719 vol. 13. "
            f'<a href="{_H13}">Huntington Digital Library</a>. '
            f'Transcription of the opening leaves: <a href="{_OB13}">on this site</a>.</li>'
        )
        if "mssHM 719 vol. 13" not in out:
            out = out.replace("</ul></section>", _li + "\n</ul></section>", 1)
    return out

print("francis_orderly_1127 done")
