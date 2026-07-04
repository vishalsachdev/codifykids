# CodifyKids — static site

Fully self-contained static version of the former Wix site
(`www.codifykids.org`), hosted free on GitHub Pages. No Wix account, CDN,
or JavaScript runtime is needed — every page is plain HTML/CSS with all
images and fonts served from this repo.

## Layout

- `docs/` — the published site (GitHub Pages serves this directory from `main`).
  7 pages: home, `/blog-1`, and 5 blog posts under `/post/...`.
- `docs/assets/` — all images (`wixstatic/`), stylesheets (`css/`), and fonts
  (`fonts/`) the pages use.
- `assets-originals/` — full-resolution originals of every media file
  (not published; preservation backup).
- `scripts/mirror.py` — step 1 of the extraction: mirrored the rendered Wix
  pages and localized media.
- `scripts/staticize.py` — step 2: took script-free DOM snapshots (rendered
  headlessly), localized CSS/fonts, and scrubbed Wix branding.

## What changed vs. the Wix site

- `/register` was deleted — its signup form posted to Wix's backend (dead on
  a static host) and the content was stale (2019 workshops).
- All Wix JavaScript removed. Interactive blog chrome that depended on it
  (search, like/comment counters, share buttons) was removed; everything
  else is intact, including the YouTube news-clip embed.
- Wix free-plan banner and "Proudly created with Wix.com" footer removed;
  home page `<title>` fixed (was "Feeding Our Kids | ...").
- The only external requests left are the YouTube embed on one post and
  genuine outbound links in blog content.

## Domain

`codifykids.org` DNS is managed outside GitHub. Point it at GitHub Pages:

- `www` CNAME → `vishalsachdev.github.io`
- apex A records → `185.199.108.153`, `185.199.109.153`, `185.199.110.153`,
  `185.199.111.153`

The custom domain is pinned by `docs/CNAME`; enable "Enforce HTTPS" in the
repo's Pages settings once the certificate is issued after the DNS switch.
