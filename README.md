# sinani.ai

Personal portfolio — mechatronics &amp; AI systems.

Static single-page site. No build step. `index.html` is served directly by GitHub Pages.

## Files
- `index.html` — the entire site (HTML + CSS + JS inline)
- `CNAME` — custom domain config for GitHub Pages (`sinani.ai`)

## Deploy
Served via GitHub Pages from the `main` branch root. Settings → Pages.

## Edit
Projects live in the `<section id="work">` block of `index.html`. Each is an
`<article class="card">` — duplicate or delete to curate. Status, domain and
stack live in the `.meta` row of each card.
