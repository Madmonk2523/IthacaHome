# Editorial photography allocation — V12

Unique photo placement is enforced at **site level** rather than only per page.

## Homepage (5)

1. `residences-autumn.webp`: shared-property opening hero with townhouse facade and autumn foliage.
2. `plaza-east-exterior.webp`: Plaza East property card.
3. `summerhill-street.webp`: SummerHill property card.
4. `plaza-bedroom.webp`: Plaza East kitchen in the interior comparison (legacy filename is misleading).
5. `summerhill-kitchen.webp`: SummerHill kitchen in the "A closer look" tiles.

## Plaza East (12)

- `property-gallery/plaza-01.webp`: property hero.
- `plaza-living.webp`: living room feature; shows fireplace and deck access.
- `plaza-kitchen.webp`: bedroom feature; legacy filename is misleading, content is a bedroom.
- `property-gallery/plaza-02.webp`, `plaza-03.webp`, and `plaza-06.webp` through `plaza-12.webp`: archived property photos, unique image paths. The duplicated kitchen and living-room images (`plaza-04.webp` and `plaza-05.webp`) are excluded from the gallery.

## SummerHill (12)

- `property-gallery/summerhill-01.webp`: property hero.
- `summerhill-bedroom.webp`: open-plan living feature; legacy filename is misleading.
- `summerhill-living.webp`: bedroom feature; legacy filename is misleading.
- `property-gallery/summerhill-01.webp` through `summerhill-10.webp`: archived property photos, unique image paths. As above, detailed per-unit captions require verification.

## Location (2)

- `lakeside-walk.webp`: atmospheric Ithaca landscape; not represented as a property amenity.
- `summerhill-sign.webp`: authentic property sign and landscaped entry.

## Excluded from placement

- `ithacahome-logo.webp` is not used as a photograph because the user requested a clean full wordmark rather than the cropped older mark.
- Remaining older duplicates and generated previews are kept only in source history and are not referenced in V9 HTML.

There are 32 active image placements across the six pages, and every source path is unique. `plaza-street.webp` is used only as social-preview metadata and is not placed as a page photo. Gallery image bytes are retained in `assets/property-gallery/`; preserve that directory during deployment.
