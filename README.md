# CodifyKids — static site

Static mirror of the former Wix site (`www.codifykids.org`), hosted free on
GitHub Pages.

## Layout

- `docs/` — the published site (GitHub Pages serves this directory from `main`).
  8 pages: home, `/register`, `/blog-1`, and 5 blog posts under `/post/...`.
- `docs/assets/wixstatic/` — media downloaded from Wix's CDN and rewritten into
  the pages, so the site does not depend on the Wix account staying alive.
- `assets-originals/` — full-resolution originals of every media file
  (not published; preservation backup).
- `scripts/mirror.py` — the script that produced `docs/` (re-run it to
  re-mirror while the Wix site is still up).

## Known limitations

- Pages still load the Wix rendering runtime (JS/CSS) from
  `static.parastorage.com`, and a few responsive image variants are generated
  at runtime against `static.wixstatic.com`. If Wix ever removes those, pages
  fall back to the locally bundled image versions; text/layout come from the
  saved HTML.
- The `/register` signup form posted to Wix's backend — on GitHub Pages it no
  longer submits anywhere. Replace it (e.g. Google Form link) or delete the
  page content if registration is still needed.
- Blog like/comment counters were Wix-backed and render as empty placeholders.
- The Wix free-plan banner was removed (`freemiumBanner` flag flipped +
  `#WIX_ADS` hidden by injected CSS).

## Domain

`codifykids.org` DNS is managed outside GitHub. Point it at GitHub Pages:

- `www` CNAME → `vishalsachdev.github.io`
- apex A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
  `185.199.111.153`

The custom domain is set in the repo's Pages settings (also pinned by
`docs/CNAME`).
