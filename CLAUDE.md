# CLAUDE.md — codifykids

Static mirror of the old Wix site, hosted on GitHub Pages
(`vishalsachdev/codifykids`, served from `main:/docs`, custom domain
`www.codifykids.org`). See README.md for layout, known limitations
(dead Wix register form, runtime still loaded from parastorage CDN),
and the DNS records the external domain registrar needs.

- Re-mirror from Wix (while it's still up): `python3 scripts/mirror.py`
- The Wix API key is NOT used anywhere — Wix has no site-export API;
  the site was captured from the rendered public pages.

## Session Log

### 2026-07-04
- Completed: Mirrored www.codifykids.org (8 pages, 39 media assets localized,
  14 full-res originals archived in assets-originals/), stripped the Wix
  free-plan banner, verified all pages render locally, pushed to GitHub
  (HTTPS pushes kept failing mid-transfer; SSH worked), enabled Pages with
  CNAME www.codifykids.org.
- Next: User must update DNS at the registrar (www CNAME →
  vishalsachdev.github.io; apex A → 185.199.108-111.153), then enable
  "Enforce HTTPS" in repo Pages settings once the cert is issued. Decide
  what to do with the dead /register form (stale 2019 content).
