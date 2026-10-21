# IthacaHome V6 — photo and deployment verification (20 October 2026)

## What changed
- Homepage now uses 12 unique property/community photo assets (one hero, two property cards, eight-image collage, one location teaser).
- Plaza East has 12 distinct original-site source-photo URLs (one hero, eleven gallery tiles).
- SummerHill has ten distinct original-site source-photo URLs (one hero, nine gallery tiles).
- Location page uses its own separate photo.
- No image URL is repeated within any page or across the six-page website.
- Removed repeated generic fallback photos from property galleries; an unavailable source photo now displays a neutral unavailable state rather than duplicating a picture.
- Existing direct navigation, lightbox, inquiry endpoint, mobile menu, and reduced-motion preference retained.

## Testing
- Static page image-URL and local-asset audit passed: 35 unique image placements overall.
- JS passed `node --check`; CSS parsed without errors.
- Locally rendered desktop and mobile homepage in Chromium without JavaScript exceptions or horizontal overflow.
- External Wix CDN photo fetching could not be fully verified in this restricted browser; website owner should supply original files and approve photo selections before replacing the live site.
- API inquiry email is still dependent on production Resend keys and a verified sender.
- Current ithacahome.com website remains untouched.

## Source attribution
- Client-supplied images and marketing flyer; separate original-gallery photos from the owner's current IthacaHome.com pages, each documented in IMAGE_SOURCES.md.
- The extra photos are hotlinked from the original site rather than copied from Apartments.com.


## Cutover-readiness update
- All 22 historic Wix gallery images were archived in GitHub and production HTML references local copies.
- No duplicated image URLs in any production page; 35 unique image placements overall.
- Old Wix page paths have Vercel redirects in `vercel.json`.
- Production Vercel form email and DNS cutover still require operator testing before shutting down Wix.
