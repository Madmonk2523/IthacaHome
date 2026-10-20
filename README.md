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
