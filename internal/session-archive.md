# Session archive — codifykids

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
