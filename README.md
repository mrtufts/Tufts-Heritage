# Tufts Revolutionary Heritage: Project 1776

A static heritage website by the **Tufts Kinsmen Association** honoring the **250th anniversary of American Independence (1776–2026)**. The site documents Tufts family Revolutionary War service, genealogy, historical places (including the Winter Hill farm, Medford, MA), artifacts, and family letters, in a professional, factual, story-like narrative.

## Folder structure
```
index.html        Landing page
config.js         ASSET_BASE_URL (single asset location setting)
manifest.json     Maps each document to its storage URL
css/              Stylesheets
js/               Scripts
profiles/         One HTML page per soldier (_template.html is the starting point)
data/             JSON records (soldiers.json)
sources/          Approved primary source list and source notes
docs/             External links only; no large files
PROJECT_1776_BRIEF.md  Project brief
```

## URL rule
Site files (HTML, CSS, JS, JSON) must never contain hardcoded absolute URLs. Use relative paths, or build asset paths from `ASSET_BASE_URL` in `config.js`. **Sole exception:** the Google Fonts links (fonts.googleapis.com / fonts.gstatic.com) that load Cinzel and EB Garamond. This keeps a future move of media to Cloudflare R2 or Backblaze B2 a one-line change.

## Visual theme
Medieval heraldic styling for a Revolutionary War era subject: parchment background, chainmail-pattern header and footer, heraldic shield and crossed-swords dividers (inline SVG), Cinzel headings, EB Garamond body text. Palette (CSS variables in `css/style.css`): burgundy/crimson, parchment cream, iron gray, gold. All textures are pure CSS or inline SVG; no external images.

## Sources policy
Primary sources only; see `sources/README.md`. Anything unverified is clearly flagged.

## Deployment
GitHub Pages deploys automatically from the root of the `main` branch. `.nojekyll` disables Jekyll processing. A custom domain may be added later.

## Contact
Shannon Tufts, President, Tufts Kinsmen Association.
