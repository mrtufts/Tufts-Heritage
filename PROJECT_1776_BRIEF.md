> **Scope change Nov 2, 2026:** The site is now a general **Tufts Lineage & Legacy** site covering the family across generations: colonial, Revolutionary, 19th century, and later. The 250th anniversary and the Revolutionary War are one chapter, not the whole site. The site must not be presented as a work of, or associated with, any family association, and must not reference one. *Tufts Kinsmen* Vols. I/II are still cited as a book source. Also added: every book citation must show a page scan or an exact quote with its printed page number, with no paraphrase, and missing images are flagged. The original brief below is kept unchanged.

# TUFTS LINEAGE & LEGACY WEBSITE BRIEF

**Owner:** Shannon Tufts (tuftss@hotmail.com). Location: Clearwater/Largo, FL. Timezone: America/New_York.

## Vision
A static heritage website honoring the 250th anniversary of American Independence, documenting Tufts family Revolutionary War service, genealogy, historical places (Winter Hill farm, Medford MA), artifacts, family letters, and verified resources. Professional, factual, story-like narrative tone. Primary sources only: Tufts Kinsmen Vols I/II, DAR, Massachusetts Soldiers and Sailors of the Revolutionary War, Find A Grave, town records of Charlestown/Medford, Revere's 1798 letter to Jeremy Belknap, Deposition of Paul Revere (MHS). Flag anything unverified.

## Current live site
The owner's earlier research index (address kept privately, not linked from this site) lists ~30 Tufts soldiers with bios, sources, notes. Last updated April 16, 2026. Contact: Shannon Tufts.

## Planned repo
`project-1776` on GitHub (user to create). Layout: `index.html`, `profiles/` (one HTML per soldier), `css/`, `js/`, `data/` (JSON records), `sources/`, `docs/` (external links only, no large files), `config.js` with single `ASSET_BASE_URL` variable. Always relative paths or the config variable; never hardcoded absolute URLs. GitHub Pages auto-deploys from `main`.

## Storage strategy
Start on GitHub Pages (1 GB repo limit, 100 MB per file, 100 GB/month bandwidth). When the archive grows large, migrate media to Cloudflare R2 (~$0.015/GB/month, zero egress) or Backblaze B2. Migration: upload files to bucket, rewrite URLs via `ASSET_BASE_URL` in `config.js`, update `manifest.json` mapping every document to its storage URL, commit and push. User creates R2/B2 account and provides API keys securely when ready.

## Domain
Custom domain planned (root A records to 185.199.108.153, 185.199.110.153, 260.253.112.200, 260.253.113.200; www CNAME to username.github.io). Registrar TBD. Cloudflare free tier optional for DNS + SSL + caching.

> ⚠️ UNVERIFIED / LIKELY ERROR: 260.253.112.200 and 260.253.113.200 are not valid IPv4 addresses (octets max at 255). GitHub Pages' documented apex IPs are 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153. Confirm before configuring DNS.

## Research bots to draw from
- "Revere & Peter Tufts Research" (agent 3c241326-ff26-4c46-8600-7ce42bf58263)
- "Albert C. Tufts Research" (agent d5f554d8-eab5-4713-b0a2-eb7d9bf379f7)

Incorporate their verified findings into drafts with source notes.

## Key decisions (Nov 2026)
1. Static site on GitHub Pages for free hosting, HTTPS, and bot-driven Git workflow.
2. Asset URL config variable from day one so a future R2/B2 migration is a find-and-replace, not a rewrite.
3. `docs/` holds links only; large PDFs (e.g., Helen Tilden Wild's *Medford in the Revolution*) stay on archive.org or external hosts.
4. Bot migration from GitHub to R2/B2 is a single unattended task once API keys are provided (~15 min user setup plus one afternoon of bot work).
5. Website name, style, and layout changes flow through the owner's main Grok conversation; the bot executes, doesn't decide.

## Next steps
User creates GitHub account + empty repo, connects GitHub, then prompts bot to scaffold (index, one sample profile — Aaron Tufts from existing bio — CSS, config.js) and enable Pages.
