# IthacaHome · deliberate photography map

**Goal:** A visitor sees each image once, where it does the most work. Pictures are not recycled on other pages, even as a hero or thumbnail. Every visual on the site belongs to an identifiable place or room type, not a decorative stock-image filler.

## Home — orientation and decision

| Order | Photo | Purpose |
|---|---|---|
| 1 | `assets/plaza-street.webp` | Full-width opening: one establishing view of the property grounds |
| 2 | `assets/plaza-east-exterior.webp` | Plaza East property card: architecture / parking context |
| 3 | `assets/summerhill-street.webp` | SummerHill property card: distinguish its townhouse exteriors |
| 4 | `assets/residences-autumn.webp` | Large editorial mosaic anchor: landscaping and seasonality |
| 5 | `assets/plaza-bedroom.webp` | Smaller gallery tile: Plaza East **wood-cabinet kitchen** (the filename is misleading) |
| 6 | `assets/summerhill-kitchen.webp` | Contrast kitchen: SummerHill **white cabinets** |
| 7 | `assets/plaza-living.webp` | Plaza East living room: fireplace / natural light |
| 8 | `assets/summerhill-living.webp` | SummerHill separate living-space view: updated flooring |
| 9 | `assets/summerhill-residences.webp` | Townhouse grounds from a second independent angle |
| 10 | `assets/summerhill-sign.webp` | Neighborhood/location teaser; shows the actual SummerHill sign |

## Plaza East — architecture, then rooms

`assets/property-gallery/plaza-01.webp`: full-width exterior hero from the owner's older gallery. `assets/plaza-kitchen.webp`: its own featured **bedroom / closets** editorial section (the filename is misleading). `assets/property-gallery/plaza-02.webp` through `plaza-12.webp`: a separate 11-image detailed gallery with no repetition. Archived photos are credited to the owner's preexisting gallery; descriptions are conservative because exact apartment and finish details differ.

## SummerHill — townhouse identity, then living space

`assets/property-gallery/summerhill-01.webp`: property hero from the owner's older gallery. `assets/summerhill-bedroom.webp`: featured **open-plan living area / freestanding fireplace** (again, the filename is misleading). `assets/property-gallery/summerhill-02.webp` through `summerhill-10.webp`: nine additional distinct gallery items only on this page.

## Location — a true sense of place

`assets/lakeside-walk.webp`: wooden walkway and green landscape. Used **only** on the Location page, never as another homepage or hero filler.

## Intentionally excluded from the active pages

The extracted marketing-flyer JPEGs (`flyer-extract-65.jpg` through `flyer-extract-72.jpg`) duplicate the room or townhouse photographs already converted to optimized WebP images. These are kept in the working copy for provenance but do not appear on the public site. The local brand-mark image is a logo, not a property photograph.

## Verification scope

- All **35** rendered photo paths are unique sitewide. No URL is reused.
- All **13** visually reviewed, active local property photographs are different shots; a perceptual difference-hash check finds no near-duplicates in that subset.
- GitHub has **22** archived gallery assets with **22 distinct Git blob hashes**. Their original-source mapping is documented in `scripts/wix_photo_sources.json`. Distinct hashes do *not* prove distinct scenes, so owner review of the deployed galleries remains the final check against visually similar alternate crops.
- No active website images use Wix or Apartments.com URLs. Only third-party tours/maps/fonts are externally linked.
