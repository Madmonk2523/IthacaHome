# IthacaHome V10 quality checks

- Six generated HTML pages. Source verified 146 internal/external anchor references, with no broken local navigation paths.
- 35 image placements, all distinct asset URLs across the site. 13 local source files were programmatically checked.
- 22 archived gallery image paths depend on 22 GitHub-hosted assets from the existing repository; the target files were confirmed present, nonzero size, and must remain on main.
- No visible photos depend on the old Wix hostname.
- Stylesheet is a complete standalone design file. No V7/V8/V9 CSS dependencies. Script is a standalone, deferred JS file.
- Progressive enhancement: if JavaScript fails, `.reveal` sections remain visible.
- Form preserves Vercel API integration and unavailable-email messaging. Real email delivery requires Resend credentials and a production test.
- JS syntax and CSS parser checks pass.
- No repeat images by URL, no emojis, no monogram, no latitude/longitude decorations.
- SEO: unique page descriptions and titles, canonical links, open graph, web schema, sitemap, robots, old Wix redirects.
- Responsive CSS includes 1200/950/700/390-pixel layouts and reduced-motion behavior.
- Desktop / mobile runtime browser screenshots are not yet verified in this environment; browser binary did not start. Do a Vercel preview visual test before public migration.
