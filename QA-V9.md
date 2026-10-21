# IthacaHome V9 / pre-deployment QA

- Reviewed 6 pages and 95 internal page links.
- 35 image placements using 35 distinct image paths (no reused image URLs across pages).
- Preserves 22 archived gallery WebP files already on GitHub. This local working copy does not include their bytes; the GitHub base tree does.
- All local image and style paths resolve.
- No remaining Wix photo dependencies in the HTML.
- JavaScript parses under Node 22; CSS parses using tinycss2.
- Contact form preserves Vercel /api/inquiry integration and validates input before submission.
- Browser automation in this environment blocked navigation, so a reliable visual and end-to-end Vercel check still needs completion.
- Never retire Wix or change domain/email DNS until a live Vercel preview and real email delivery have been verified.