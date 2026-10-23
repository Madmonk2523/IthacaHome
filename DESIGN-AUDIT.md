# IthacaHome / Visual and functional audit (V13)

## V13 navigation and content

- Desktop navigation now exposes Home, Plaza East, SummerHill, Neighborhood, and Contact directly on every page, alongside the tour action.
- Mobile navigation includes every page, a visible privacy link, active-page state, Escape-to-close, focus handling, and resize cleanup.
- Added an Explore page directory to every footer so visitors can move between the complete site without returning to the home page.
- Checked the former IthacaHome FAQ (`/faq-s`) and updated the pet answer with its three-pet limit, breed restrictions, and published additional-pet fees; fees are clearly identified as subject to change.
- Used the supplied 2025–26 rental sheet for historical utility, parking, and pet details. Old rent prices are intentionally not presented as current quotes.

## V12 visual refresh

- Reworked the shared visual system across the homepage, property, neighborhood, and contact pages with a forest-green, warm-stone, and terracotta palette.
- Rebalanced the homepage into a responsive editorial composition: full-bleed lead photography, offset property cards, a high-contrast amenities band, and clearer location and inquiry calls to action.
- Simplified the shared navigation and added a readable, keyboard-dismissable mobile menu presentation at tablet and phone widths.
- Kept the existing local photo assignments unique; no image source is intentionally reused across pages.
- Updated location copy from the live IthacaHome website: East Hill Plaza and its TCAT stop are about a three-minute walk away; Cornell is about a 15-minute walk or three-minute drive; Routes 82 and 51 are cited with a link to the TCAT schedule.
- Rechecked the six-page static audit and JavaScript syntax after the redesign.

## Problems found and addressed

- The previous opening photo was dominated by the parking lot. The new opening uses the user's autumn courtyard photograph with trees and townhouse facades. The photograph was moved, not reused.
- The dark, text-heavy left hero competed with the photography. The editorial panel now uses warm cream, deep green, burgundy emphasis, and more coherent spacing.
- The page used decorative offsets (the second property card, the second interior photo) that created awkward empty gaps. They are substantially reduced.
- The neighborhood preview reused a photograph needed for the new hero. It now uses real proximity information, not another stock image or photo duplication.
- On phones the copy previously pushed the first photograph below the fold. The image now appears first, with responsive cropping and a compact leasing call to action.
- Giant detail titles, headings, and excessive padding on smaller screens are scaled back.
- Copy is less slogan-driven; titles and descriptions favor floor-plan types, layout features, leasing information, and nearby Cornell access.
- Missing dimension attributes contributed to layout shifts. Local images now declare their intrinsic dimensions.
- The property galleries continue to use unique locally hosted GitHub/WebP paths; none of the site's photo src URLs repeat across pages.
- Scroll animations progressively enhance readable content; JavaScript or observer failures do not hide paragraphs or photos.
- The entry photo is preloaded; metadata sharing image is kept in sync with the new hero.
- Accurate bedroom and bathroom options from the old property pages are retained; price and live unit availability remain subject to owner confirmation.

## Not yet certified

- Live production email deliverability must be tested with verified Resend sender credentials.
- Automated browser navigation is blocked in the local sandbox; local screenshot construction is an approximate proof of layout.
- Independently inspect real mobile devices and the protected Vercel deployment before turning off Wix.
