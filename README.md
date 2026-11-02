# Tufts Family Heritage

A static heritage website about the Tufts family across generations, from colonial New England onward: the colonial era, the Revolutionary War (including the 250th anniversary of American Independence, 1776–2026, as one chapter), the 19th century, and later generations. It covers genealogy, places, artifacts, and family letters, written in a professional, factual, story-like narrative. The site is an independent family-history project and is not a publication of, or affiliated with, any family association.

## Folder structure
```
index.html             Home: hero, timeline strip, featured stories
generations/           colonial.html, revolution.html (250th banner), 19th-century.html, modern.html
people.html            Searchable A-Z index (data/people.json)
places.html            Winter Hill, Medford & Charlestown, Later Homes
collections.html       Letters, Artifacts, Photographs
sources.html           Bibliography, Page Scans (data/sources.json), Research Notes
profiles/              One HTML page per person (_template.html)
css/ js/               Stylesheet and scripts (search/filters, scan gallery)
data/                  people.json, sources.json
sources/               Quote table (README.md) and page scans (images/)
docs/                  External links only; no large files
config.js              ASSET_BASE_URL
manifest.json          Maps each asset to its storage path
tools/build_pages.py   Regenerates pages with the shared nav, header, and footer
PROJECT_1776_BRIEF.md  Project brief
```

## Navigation
Home | Generations (Colonial 1638–1765, The Revolution 1765–1783, 19th Century, Modern) | People | Places | Collections | Sources. Sections that have no content yet are greyed out and tagged "Coming soon" with a one-line note of what is planned. They still link to real pages, so there are no dead links.

## URL rule
Site files (HTML, CSS, JS, JSON) must never contain hardcoded absolute URLs. Use relative paths, or build asset paths from `ASSET_BASE_URL` in `config.js`. **Sole exception:** the Google Fonts links (fonts.googleapis.com / fonts.gstatic.com) that load Cinzel and EB Garamond. This keeps a future move of media to Cloudflare R2 or Backblaze B2 a one-line change.

## Visual theme
Medieval heraldic styling for a Revolutionary War era subject: parchment background, chainmail-pattern header and footer, heraldic shield and crossed-swords dividers (inline SVG), Cinzel headings, EB Garamond body text. Palette (CSS variables in `css/style.css`): burgundy/crimson, parchment cream, iron gray, gold. All textures are pure CSS or inline SVG; no external images.

## Sources policy
Primary sources only; see `sources/README.md`. Every book citation must show a page scan (`sources/images/`) or an exact quote with its printed page number. Never paraphrase. Missing images are flagged. `data/sources.json` maps each citation to its scan. Book sources include *Tufts Kinsmen*, Vols. I and II (cited as a book title only). Anything unverified is clearly flagged.

## Deployment
GitHub Pages deploys automatically from the root of the `main` branch. `.nojekyll` disables Jekyll processing. A custom domain may be added later.
