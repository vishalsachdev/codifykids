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

### 2026-07-04
- Completed: Extracted www.codifykids.org from Wix end-to-end. Phase 1:
  mirrored 8 pages + media, stripped free-plan banner, published to GitHub
  Pages with CNAME www.codifykids.org. Phase 2 (independence): headless-
  Chrome DOM snapshots with all Wix JS removed, localized CSS + the 8 fonts
  actually used, removed dead blog chrome (search/likes/share), deleted the
  stale /register page (form posted to Wix), fixed home title, removed
  "Proudly created with Wix.com". Verified zero external requests except
  the YouTube embed + outbound content links.
- 2026-07-05 follow-up: DNS switched at Squarespace (registrar; serves via
  legacy Google Cloud DNS nameservers for ex-Google-Domains registrations).
  Cert issuance needed a domain remove/re-add nudge. HTTPS enforced;
  www + apex + .com redirect all verified. MIGRATION COMPLETE. Wix account
  can be closed. Open question for user: whether @codifykids.org email
  forwarding matters (old Google Domains gmr MX are dead; Squarespace
  Email Forwarding rules would replace them).
