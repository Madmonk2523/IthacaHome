# IthacaHome — editorial residence website

Static website for Plaza East Apartments & Townhouses and SummerHill Townhouses, East Hill, Ithaca, New York.

## Pages
- `/` — cinematic homepage, property comparisons, interiors, location benefits, resident testimonial, FAQ
- `/plaza-east.html` — Plaza East details, photo gallery, apartment and townhouse floor-plan types
- `/summerhill.html` — SummerHill details, gallery and floor-plan types
- `/neighborhood.html` — East Hill / Cornell location and transit
- `/contact.html` — leasing inquiry form and contact details
- `/privacy.html` — privacy information (owner review required)

## Design & accessibility
- Custom responsive CSS in `assets/site.css`; behavior in `assets/site.js`
- Cinematic hero, masked-title animation, staged image reveals, restrained parallax, scroll reveal, and responsive photo gallery viewer
- Motion respects `prefers-reduced-motion`
- No emoji icons, no monogram, no geographic coordinate decorations
- Content stays visible when JavaScript does not load (progressive enhancement)
- Photo assignments are unique across the six pages (35 placements, 35 distinct asset paths)

## Photography / important preservation instruction
- 13 photos are in `/assets/*.webp` in this local build and in the repository.
- 22 archived property-gallery photos already live on GitHub at `/assets/property-gallery/{plaza-01..12,summerhill-01..10}.webp`. **Do not delete or replace that directory during upload.**
- Every image used in the site is hosted as a local project path; **none** load from the old Wix website.
- `photo-manifest.json` lists all placements. Identical image use is not deliberately repeated across pages.

## Leasing form
- The contact page posts JSON to `/api/inquiry` (Vercel serverless handler already in repository).
- Set `RESEND_API_KEY`, `CONTACT_FROM_EMAIL`, and optionally `CONTACT_TO_EMAIL` in the Vercel environment.
- `CONTACT_FROM_EMAIL` must be an authorized sender for the email service.
- Until configured, the endpoint returns a visible 503 and the form shows the direct leasing email—do not claim messages were sent.
- Owner should approve text, privacy policy, prices/availability, pet rules and photos before launch.

## Development
- Serve from repo root with `python -m http.server 8000` for static pages; the API route requires Vercel to actually send emails.
- `python qa_v10.py` audits links, source paths, SEO tags and photo uniqueness.
- `node --check assets/site.js` validates JavaScript syntax.
- `python build.py` regenerates the six HTML pages, sitemap, Vercel redirects and favicon from the reviewed content.

## Launch
- Import connected GitHub repository into Vercel (static preset / no build command), or use its existing GitHub-connected Vercel project.
- Keep the original domain and email DNS untouched until the preview, form, and owner review pass.
- Confirm old Wix URLs redirect properly and `robots.txt` / `sitemap.xml` resolve after domain change.
