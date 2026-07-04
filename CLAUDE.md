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

### 2026-07-04
- Completed: Extracted www.codifykids.org from Wix end-to-end. Phase 1:
  mirrored 8 pages + media, stripped free-plan banner, published to GitHub
  Pages with CNAME www.codifykids.org. Phase 2 (independence): headless-
  Chrome DOM snapshots with all Wix JS removed, localized CSS + the 8 fonts
  actually used, removed dead blog chrome (search/likes/share), deleted the
  stale /register page (form posted to Wix), fixed home title, removed
  "Proudly created with Wix.com". Verified zero external requests except
  the YouTube embed + outbound content links.
- Next: User must update DNS at the registrar (www CNAME →
  vishalsachdev.github.io; apex A → 185.199.108-111.153), then enable
  "Enforce HTTPS" in repo Pages settings once the cert is issued.
