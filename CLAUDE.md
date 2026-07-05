# CLAUDE.md — codifykids

Fully self-contained static version of the old Wix site, hosted on GitHub
Pages (`vishalsachdev/codifykids`, served from `main:/docs`, custom domain
`www.codifykids.org`). No Wix dependency remains — no scripts, all
images/CSS/fonts local. See README.md for layout, the two-step extraction
pipeline (scripts/mirror.py + scripts/staticize.py), and the DNS records
the external registrar needs.

- The Wix API key is NOT used anywhere — Wix has no site-export API;
  the site was captured from the rendered public pages.
- Pushes: HTTPS to GitHub failed repeatedly mid-transfer on this network;
  origin is set to SSH, which works.

## Session Log

### 2026-07-05 (frontend rebuild)
- Completed: Replaced the snapshotted Wix DOM with a hand-authored responsive
  site (docs/assets/site.css + 7 HTML pages, generated posts via
  scripts/build_posts.py). Same palette + URLs; code-tag section motif;
  real portraits (IMG_4477=Shreya, IMG_1216=Aryan — the old "press gallery"
  images were actually people); 640KB total. Pruned all unused Wix assets.
- Next: content is verbatim from 2020 ("Our Current Camp" = April 2020) —
  user may want a copy refresh if camps resume.

*Older entries: internal/session-archive.md*
