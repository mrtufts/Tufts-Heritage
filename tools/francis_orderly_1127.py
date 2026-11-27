# Francis Tufts orderly book, Huntington mssHM 719 vol. 13 (7 Apr–30 May 1782).
# Huntington digital images 1–94 are shown from the Library's IIIF URLs (not hosted here).
# A diplomatic transcription stands under pages 1–9.

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

_IIIF = "https://hdl.huntington.org/digital/iiif/p15150coll7/{ptr}/full/800,/0/default.jpg"
_LEAVES = [
    (1, '44180', 'Front Cover'),
    (2, '44181', 'Inside Front Cover'),
    (3, '44182', 'Index'),
    (4, '44183', 'p. 1'),
    (5, '44184', 'p. 2'),
    (6, '44185', 'p. 3'),
    (7, '44186', 'p. 4'),
    (8, '44187', 'p. 5'),
    (9, '44188', 'p. 6'),
    (10, '44189', 'p. 7'),
    (11, '44190', 'p. 8'),
    (12, '44191', 'p. 9'),
    (13, '44192', 'p. 10'),
    (14, '44193', 'p. 11'),
    (15, '44194', 'p. 12'),
    (16, '44195', 'p. 13'),
    (17, '44196', 'p. 14'),
    (18, '44197', 'p. 15'),
    (19, '44198', 'p. 16'),
    (20, '44199', 'p. 17'),
    (21, '44200', 'p. 18'),
    (22, '44201', 'p. 19'),
    (23, '44202', 'p. 20'),
    (24, '44203', 'p. 21'),
    (25, '44204', 'p. 22'),
    (26, '44205', 'p. 23'),
    (27, '44206', 'p. 24'),
    (28, '44207', 'p. 25'),
    (29, '44208', 'p. 26'),
    (30, '44209', 'p. 27'),
    (31, '44210', 'p. 28'),
    (32, '44211', 'p. 29'),
    (33, '44212', 'p. 30'),
    (34, '44213', 'p. 31'),
    (35, '44214', 'p. 32'),
    (36, '44215', 'p. 33'),
    (37, '44216', 'p. 34'),
    (38, '44217', 'p. 35'),
    (39, '44218', 'p. 36'),
    (40, '44219', 'p. 37'),
    (41, '44220', 'p. 38'),
    (42, '44221', 'p. 39'),
    (43, '44222', 'p. 40'),
    (44, '44223', 'p. 41'),
    (45, '44224', 'p. 42'),
    (46, '44225', 'p. 43'),
    (47, '44226', 'p. 44'),
    (48, '44227', 'p. 45'),
    (49, '44228', 'p. 46'),
    (50, '44229', 'p. 47'),
    (51, '44230', 'p. 48'),
    (52, '44231', 'p. 49'),
    (53, '44232', 'p. 50'),
    (54, '44233', 'p. 51'),
    (55, '44234', 'p. 52'),
    (56, '44235', 'p. 53'),
    (57, '44236', 'p. 54'),
    (58, '44237', 'p. 55'),
    (59, '44238', 'p. 56'),
    (60, '44239', 'p. 57'),
    (61, '44240', 'p. 58'),
    (62, '44241', 'p. 59'),
    (63, '44242', 'p. 60'),
    (64, '44243', 'p. 61'),
    (65, '44244', 'p. 62'),
    (66, '44245', 'p. 63'),
    (67, '44246', 'p. 64'),
    (68, '44247', 'p. 65'),
    (69, '44248', 'p. 66'),
    (70, '44249', 'p. 67'),
    (71, '44250', 'p. 68'),
    (72, '44251', 'p. 69'),
    (73, '44252', 'p. 70'),
    (74, '44253', 'p. 71'),
    (75, '44254', 'p. 72'),
    (76, '44255', 'p. 73'),
    (77, '44256', 'p. 74'),
    (78, '44257', 'p. 75'),
    (79, '44258', 'p. 76'),
    (80, '44259', 'p. 77'),
    (81, '44260', 'p. 78'),
    (82, '44261', 'p. 79'),
    (83, '44262', 'p. 80'),
    (84, '44263', 'p. 81'),
    (85, '44264', 'p. 82'),
    (86, '44265', 'p. 83'),
    (87, '44266', 'p. 84'),
    (88, '44267', 'p. 85'),
    (89, '44268', 'p. 86'),
    (90, '44269', 'Chart 1'),
    (91, '44270', 'Chart 2'),
    (92, '44271', 'Inside back Cover'),
    (93, '44272', 'Back cover'),
    (94, '44273', 'Spine')
]

def _ob_page(n, ptr, label, text=""):
    import html as _html
    url = _HDL.format(ptr)
    src = _IIIF.format(ptr=ptr)
    alt = _html.escape(label + ", orderly book of Lieut. Francis Tufts, The Huntington Library, mssHM 719 vol. 13")
    cap = _html.escape(label)
    fig = (
        f'<p class="ob-page" id="image-{n:03d}"><a href="{url}">[{cap}]</a></p>\n'
        f'<figure class="ob-scan"><a href="{url}">'
        f'<img src="{src}" alt="{alt}" loading="lazy" width="800"></a>'
        f"<figcaption>{cap}</figcaption></figure>\n"
    )
    if text and text.strip():
        body = _html.escape(text.strip("\n"), quote=False)
        fig += f"<pre>{body}</pre>\n"
    return fig

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
    + '<p>The transcription below follows the wording, spelling, abbreviations, and lineation of the manuscript. Words written above the line are placed in the text with a caret (for example, Head Quarters^new). Unclear readings are marked [?]. Each leaf is shown from the Huntington Digital Library; the heading or image opens that page there.</p>'
    + f'<p class="cite">{_CRED_ORIG}</p>'
    + f'<p class="cite">{_CRED_TR}</p>'
)

_PROGRESS = '<p class="ob-progress">Transcription of pages 1&ndash;9; remaining pages shown as scanned.</p>'

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
# Remaining leaves (10-94): Huntington scans only, no added transcription.
_BY_PTR = {n: (ptr, title) for n, ptr, title in _LEAVES}
_HAVE = {1, 2, 3, 4, 5, 6, 7, 8, 9}
for _n, _ptr, _title in _LEAVES:
    if _n in _HAVE:
        continue
    _TR += _ob_page(_n, _ptr, f"Page {_n}")

page(
    "stories/francis-tufts-orderly-book-1782.html",
    "Orderly Book of Lieut. Francis Tufts, 1782 | Tufts Lineage &amp; Legacy",
    "A Primary Source",
    "Orderly Book of Lieut. Francis Tufts, April&ndash;May 1782",
    "8th Massachusetts Regiment, kept at West Point and the Hudson Highlands",
    '<section id="the-book"><h2>The Adjutant&rsquo;s Book, Spring 1782</h2>'
    + _INTRO
    + "</section>{DIV}"
    + '<section id="the-pages"><h2>The Pages</h2>'
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
