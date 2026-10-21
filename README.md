# IthacaHome — Design V9

A purpose-built residential leasing website for Plaza East and SummerHill in Ithaca, New York.

## Navigation

- `/` — introduction and community overview
- `/plaza-east.html` — Plaza East photos, amenities, and floor plans
- `/summerhill.html` — SummerHill photos, amenities, and floor plans
- `/neighborhood.html` — East Hill location and directions
- `/contact.html` — leasing inquiry and tour requests
- `/privacy.html` — inquiry privacy information

## Design and dependencies

- All six pages load **only** `/assets/site-v9.css` and `/assets/site-v9.js`. Do not remove these assets.
- Website photography is all local `/assets/` media, including 22 archived images under `/assets/property-gallery/` already stored on GitHub.
- 35 unique photo placements across all six pages. No photo URL is reused on another page. Six property-gallery photos are visible initially on each property page; the remaining photos become visible using the gallery's "View all" control.
- Motion respects `prefers-reduced-motion`. No monogram, emoji, latitude/longitude decoration, or decorative arrows.
- Existing `api/inquiry.js` is unchanged and requires the environment variables in `.env.example` to actually deliver inquiries.

## Deploy

This is a static HTML/CSS/JS site with one Vercel serverless `/api/inquiry` handler. Import the GitHub `Madmonk2523/IthacaHome` repository into Vercel using the repository root and **Other** framework. Verify every image and the form on the Vercel preview URL before switching the live domain.

## Critical migration precautions

Keep the existing Wix subscription and `ithacahome.com` DNS untouched until the Vercel site is publicly accessible and a real inquiry email has been delivered successfully. Preserve all email MX, TXT, SPF, DKIM, and DMARC records for `rentals@ithacahome.com`.

## QA

See `QA-V9.md` for checks completed and limitations. Visual browser navigation was blocked in the container; browser screenshots produced via print rendering do not constitute a production browser pass.

