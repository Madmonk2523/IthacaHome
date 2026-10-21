# Safe Wix-to-Vercel migration

Do not cancel Wix yet. Before retirement:

1. Verify all 22 new images in `assets/property-gallery/` exist in GitHub, and the current site has zero Wix-hosted image URLs.
2. Deploy this exact repository to a Vercel **preview URL first**; check all pages, images, galleries, desktop/mobile navigation, old-page redirects and the 3D-tour link.
3. Configure `RESEND_API_KEY`, `CONTACT_FROM_EMAIL` and optional `CONTACT_TO_EMAIL` on Vercel. Verify the sending domain and submit a real tour inquiry, confirming that it reaches the leasing inbox.
4. Confirm the **domain registrar** and maintain ownership/renewal of `ithacahome.com`. If Wix manages the domain, separate domain registration from site hosting before cancelling any plan.
5. Save all DNS records. Preserve email MX, SPF, DKIM and DMARC entries, plus other third-party verification records; do not cancel the rental email service.
6. Change only the required website A/CNAME entries according to the Vercel project instructions; keep the old site available during DNS propagation.
7. Verify both root domain and www with valid HTTPS, email delivery, sitemap/Search Console and redirects from legacy property pages.
8. Cancel old **site hosting** only after several days of confirmed functionality; never cancel the domain or email by accident.

The Apartments.com 3D tour and OpenStreetMap embed are separate third-party services, not Wix dependencies. Their availability is managed independently.
