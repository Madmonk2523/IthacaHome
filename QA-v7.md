# IthacaHome V7: photography curation QA

Date: 2026-10-21

### Scope and methodology

- Visually inspected the user-supplied and flyer-derived photo set, including the room/exterior composites. Excluded the eight flyer-extract images that duplicate the edited WebP originals. Corrected mislabeled file descriptions (`plaza-bedroom.webp` is a kitchen; `plaza-kitchen.webp` is a bedroom; `summerhill-bedroom.webp` is a living space).
- Allocated each photograph to one page and one role: establishing/hero, property chooser, editorial interior, location, or property detail gallery. See `PHOTO_PLACEMENT.md` and generated `photo-manifest.json`.
- Checked all 22 archived owner-gallery image paths and unique blob SHAs on GitHub. These originals are not mounted in the local working copy. The GitHub Actions `Photography integrity` check does pixel-level near-duplicate analysis on a full checkout.
- 35 content image placements / 35 distinct image URLs across Home, Plaza East, SummerHill and Location. No picture is used a second time as a card, hero, thumbnail, or gallery tile on another page.
- 13 active local photographs decode successfully; none is a near match to another active local photograph under a 64-bit dHash Hamming threshold of <= 5.
- No displayed photograph hotlinks Wix or Apartments.com. The 22 archived photos are local to the deployed repo. Google Fonts, mapping tiles, and the linked external 3D tours still depend on their respective third-party services.

### Checks

- Generator: `python3 build_v7.py` (regenerates six pages and assignment manifest)
- Code: `node --check assets/site-v7.js`, `node --check api/inquiry.js`
- CSS: tinycss2 parser; no parse errors in the new V7 layer
- Page asset refs: generated site paths verified; 22 archived gallery photos confirmed present by GitHub connector
- Sitewide placement: `python3 scripts/photo_audit_v7.py`; on GitHub `--strict` also analyzes archived photo pixels
- Leasing forms: retain previous browser validation and Vercel serverless handler; live email delivery requires Resend credentials

### Limitations / launch gate

Browser navigation to the local test server is currently blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR`), so full visual browser regression testing on V7 has not been completed. GitHub Actions can audit actual archive image pixels on the full checkout. Before replacing ithacahome.com, the owner should approve the photography placement and confirm unit photos/amenities, test live inquiries on Vercel, and preserve email/DNS settings.
