# IthacaHome — Architectural Residential Website

An editorial, animated, responsive and accessible website for IthacaHome's **Plaza East** and **SummerHill** residential properties in Ithaca, New York. Uses only the photographs supplied for the project; no generic property stock photography. No npm dependency is required.

## Pages

- `/` — immersive homepage, animated transitions, two-property interactive explorer, filtered floor-plan configuration selector
- `/plaza-east.html` — photography, amenities, floor plans, leasing CTAs
- `/summerhill.html` — photography, amenities, floor plans, leasing CTAs
- `/neighborhood.html` — Cornell / local area / transit / embedded map
- `/contact.html` — validated tour / leasing inquiry form
- `/privacy.html` — initial privacy-information draft; **requires owner review** before publication

## Run locally

From this repository, run:

```bash
python3 -m http.server 8000
```

Open http://localhost:8000. Photos, layouts, navigation, animations and filtering work without any server configuration. **Forms only deliver on a deployed Vercel site with the email environment variables configured**, because local Python's static server doesn't run Vercel functions.

## Deploy with Vercel

1. Import the `Madmonk2523/IthacaHome` repository into Vercel.
2. Framework preset: `Other`; Build Command: **none**; Output Directory: **leave blank**; Root Directory: `./`.
3. Vercel will serve the static HTML/CSS/JS and run `api/inquiry.js` as a serverless Node endpoint.
4. Create a Resend account, verify a sender domain that you control, and configure the environment variables below in Vercel (Production and Preview as desired).
5. Redeploy and submit a genuine test inquiry. The first email should arrive in the leasing inbox. Monitor server logs if needed.
6. Only after approval and testing, point the owner's domain at the deployment. Do **not** change the current website's DNS prematurely.

## Working forms — environment variables

| Variable | Meaning |
|---|---|
| `RESEND_API_KEY` | Secret token from Resend. Set only in Vercel, never commit to GitHub. |
| `CONTACT_FROM_EMAIL` | Verified sender, e.g. `IthacaHome Leasing <leasing@your-verified-domain.com>` |
| `CONTACT_TO_EMAIL` | Optional; defaults to `rentals@ithacahome.com` |

The form validates required fields in the browser and on the server, uses a honeypot, rate-limits repeated requests on a best-effort per-instance basis, and delivers an HTML email to the leasing inbox. It clearly reports any send failure. For heavy traffic, add a CAPTCHA/Cloudflare Turnstile and a persistent rate limiter. Do not add secret keys to frontend files.

## Content checks before publishing

- Verify exact Plaza East washer/dryer inclusions, which differ across existing site pages; the new site cautiously says laundry hookups / select units with machines.
- Confirm exact floor plans, rent, and live vacancies. The selector shows **floor plan types, not live vacancies or prices**.
- Confirm the owner's preferred company name, phone and address; currently uses the supplied flyer / existing site's information.
- Confirm all photos match their property titles (some supplied images don't identify their exact property unambiguously).
- Have property manager and counsel review the privacy information, marketing claims, fair-housing requirements and any local rental disclosure obligations.
- Have the owner approve the domain migration and Google Business Profile eligibility separately.

## Editing

`build.py` contains the shared navigation, footers, page layouts, property data and text. Run `python3 build.py` to regenerate the HTML files after changes.

Styling and motion are in `assets/styles.css` and `assets/script.js`. Both are dependency-free. The serverless email handler is `api/inquiry.js`. All supplied project photos are in `assets/`.

## Github

To connect: push the project files to `https://github.com/Madmonk2523/IthacaHome` after authorizing a GitHub connection. The repository was empty when this site was created. Do not force-push if it gains content in the meantime.


## Signature edition: flyer + existing website

The signature visual system is layered in `assets/editorial.css` and `assets/editorial.js`. It uses the owner's IthacaHome flyer for the historic roofline identity, deep burgundy / navy / cream / brass palette, and actual Plaza East / SummerHill photography. The existing `ithacahome.com` pages supplied the leasing FAQs, neighborhood details, resident story excerpts, the links to 3D tours, and the definitions of the different floor-plan types. The site avoids claiming live availability or current prices.

Source-material references for owner verification before publication:
- https://www.ithacahome.com/ (community descriptions, neighborhood, reviews)
- https://www.ithacahome.com/faq-s (rental FAQs and pet policies)
- https://www.ithacahome.com/copy-of-summerhill-townhouses (Plaza East)
- https://www.ithacahome.com/copy-2-of-plaza-east-luxury-townhou (SummerHill)
- https://www.apartments.com/plaza-east-summerhill-townhouses-ithaca-ny/przvhlr/ (virtual tours, published third-party information)

For a **full source regeneration**, run:

```bash
python3 -m pip install beautifulsoup4
python3 build.py
python3 enhance.py
python3 refine.py
```

The generated static pages are already included in the repository, so there is no build step for Vercel. The redevelopment includes cinematic photo treatments, architectural type, responsive layouts, scroll reveals, interactive residence comparisons, floor-plan filtering, virtual-tour links, resident stories, an accessible FAQ, and a validated tour-request form. The Resend environment variables described above are still required for form delivery. Avoid placing any API secrets in this public repository.

## Refined design (October 2026)

The latest version uses the full **ITHACA HOME** wordmark only (no IH initials), with a streamlined desktop/mobile navigation: Properties, Neighborhood, FAQ, Schedule a Tour. It removes all decorative latitude/longitude labels, badge/seal clutter, and polaroid treatments. The homepage features a clean photographic hero and direct leasing actions. The additional `assets/refinement.css` and `assets/refinement.js` layers implement responsive styling, restrained motion, parallax, and navigation highlighting, including reduced-motion support. All six public pages use these enhancements.

The site remains a static, multi-page front-end with a Vercel serverless inquiry endpoint. A Resend API key and verified sender domain are still necessary for production email delivery. Unit availability and prices are **not** represented as real-time data; confirm those with the owner prior to advertising availability.

## V5 — Direct Navigation / Site Refresh (2026-10-20)

**V5 is the canonical current edition.** Run `python3 build_v5.py` to regenerate all six static HTML pages. The active stylesheet and interaction script are `/assets/site-v5.css` and `/assets/site-v5.js`; older `build.py`, `enhance.py`, `refine.py`, and V4 CSS/JS are retained only as historical source and should not be run for the new design.

- The main header offers Plaza East, SummerHill, Location, and Schedule a tour, directly. There are no submenu decisions.
- Clearer, shorter marketing copy focuses on floor plan types, community features, Cornell proximity, and contact.
- Scroll-triggered section reveals, kinetic hover/photo transitions, and a photo lightbox honor prefers-reduced-motion.
- No photo URL appears more than once per page. Images from the client-provided flyer and original property photos are used locally; extra photos on the original IthacaHome.com website are loaded from distinct Wix CDN URLs, with local fallbacks. See `IMAGE_SOURCES.md` for a full list. External CDN assets need live verification before launch.
- Photo galleries, direct property navigation, mobile menu, leasing form, and compatibility with `api/inquiry.js` were audited at desktop and mobile widths. See `QA-v5.md`.

The old site / Apartments.com links are used as content and 3D-tour references, not as real-time vacancy data. Owner must verify source imagery and consent before production migration.


## V6 photograph update (20 October 2026)
- 33 distinct photos across four image-bearing pages, with no repeats anywhere in the six-page site.
- Pages generated by `python build_v6.py`, with new motion/gallery styling in `assets/site-v6.css` and JS in `assets/site-v6.js`.
- Gallery imagery from original IthacaHome Wix CDN; local owner-supplied photos on home/location. See `IMAGE_SOURCES.md` for source URLs and approval notes.


## Shutdown-safe image migration (October 2026)

The 22 images previously hotlinked from the legacy Wix site have been archived as
`assets/property-gallery/plaza-01.webp` through `plaza-12.webp` and
`summerhill-01.webp` through `summerhill-10.webp` in the GitHub repository.
**No production HTML photo source should refer to Wix.** The importer remains as
an audit trail, not an essential runtime dependency. Keep these photo files in
GitHub and in every deployment. Confirm the property owner's rights to use them.

Before decommissioning Wix: deploy to Vercel, test every gallery and the form,
point the `ithacahome.com` DNS records at Vercel, and preserve the domain
registration and email MX/SPF/DKIM records. Do not cancel mail or domain service.
Legacy page URLs redirect through `vercel.json`.


## V7 — Deliberate photography / no reuse (2026-10-21)

**`build_v7.py` is the current generator.** Run `python3 build_v7.py` to regenerate the six public pages and V7 CSS/JS. It generates `photo-manifest.json` and `IMAGE_SOURCES.md`, and applies a controlled, sitewide assignment of every photograph. Previous generators are retained as historical source and should not be used for production.

Each selected image gets exactly **one placement anywhere in the website**. Two archive images (`plaza-04.webp`, `plaza-05.webp`) were removed from the published galleries after the GitHub pixel audit identified visually repeated homepage shots. The home page establishes location and compares communities; property detail pages each add a verified interior photo and a separate archived-gallery sequence; the Location page features a distinct outdoor view. Visually duplicated client flyer extracts are excluded. The legacy Wix image URLs are not used by the website.

See `PHOTO_PLACEMENT.md`, `photo-manifest.json`, `QA-v7.md`, and `scripts/photo_audit_v7.py`. All 22 property-gallery WebP images are already versioned in GitHub under `assets/property-gallery`; do not delete that directory.
