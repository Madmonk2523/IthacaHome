# IthacaHome Quality Assurance & Launch Checklist

## Automated checks carried out
- JavaScript syntax verified with `node --check`.
- Custom CSS parsed without syntax errors.
- Internal local asset paths resolved on every production HTML page.
- Browser-rendered desktop and mobile layouts examined using locally inlined website assets.
- Verified responsive layout without horizontal scrolling at 390px and 1440px.
- Interactive property switcher, property bedroom filters and resident FAQs exercised in a browser context.
- Server side `/api/inquiry.js` validates names, email, property and bedroom selections; 4-bedroom SummerHill requests are rejected.

## Before publishing to the owner's domain
- Confirm details of each available floor plan, current prices, dates and availability with owner. This website deliberately avoids presenting static inventory as live.
- Confirm owner's legal name and obtain approvals for public wording, property images and testimonials.
- Inspect at least one live Preview deployment on desktop and phone, including real image load performance and lighthouse scores.
- On Vercel, configure `RESEND_API_KEY` and verified `CONTACT_FROM_EMAIL`, then submit a real inquiry and confirm delivery to `rentals@ithacahome.com`.
- Review the privacy page and fair-housing compliant copy with the property owner.
- Point `ithacahome.com` to Vercel only after approval, preserving email/MX records.