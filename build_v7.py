"""IthacaHome V7 photo curation layer. Regenerate V6 base, then apply sitewide image assignments."""
from pathlib import Path
from bs4 import BeautifulSoup
import runpy, shutil

ROOT=Path(__file__).resolve().parent
runpy.run_path(str(ROOT/"build_v6.py"),run_name="__main__")
# Guardrail: keep local owner-verified photos in deliberate, non-overlapping roles.
STORY={
  "index.html": [
    ("hero","/assets/plaza-street.webp"),
    ("Plaza East property card","/assets/plaza-east-exterior.webp"),
    ("SummerHill property card","/assets/summerhill-street.webp"),
    ("kitchen / Plaza East","/assets/plaza-bedroom.webp"),
    ("kitchen / SummerHill","/assets/summerhill-kitchen.webp"),
    ("living / Plaza East","/assets/plaza-living.webp"),
    ("living / SummerHill","/assets/summerhill-living.webp"),
    ("grounds / autumn","/assets/residences-autumn.webp"),
    ("townhouse landscape","/assets/summerhill-residences.webp"),
    ("location details","/assets/summerhill-sign.webp"),
  ],
  "plaza-east.html":[("bedroom detail","/assets/plaza-kitchen.webp")],
  "summerhill.html":[("living fireplace detail","/assets/summerhill-bedroom.webp")],
  "neighborhood.html":[("green outdoor walkway","/assets/lakeside-walk.webp")],
}
for filename,items in STORY.items():
    soup=BeautifulSoup((ROOT/filename).read_text(),"html.parser")
    if filename=="index.html":
        # One photograph for each genuinely different space; no repetitive filler.
        grid=soup.select_one(".mosaic-grid")
        if grid is None: raise RuntimeError("Homepage mosaic grid missing")
        photo_sources={
          "/assets/plaza-bedroom.webp",
          "/assets/summerhill-kitchen.webp",
          "/assets/plaza-living.webp",
          "/assets/summerhill-living.webp",
          "/assets/residences-autumn.webp",
          "/assets/summerhill-residences.webp",
        }
        for button in list(grid.select(".gallery-photo")):
            im=button.find("img")
            if im and im.get("src") not in photo_sources:
                button.decompose()
        assert len(grid.select(".gallery-photo"))==6
        # Give the landscaped autumn photograph the large editorial position;
        # the smaller frames show complementary, different interior spaces.
        for b in grid.select('.gallery-photo'):
            b['class']=[x for x in b.get('class',[]) if x!='mosaic-wide']
        lead=next(b for b in grid.select('.gallery-photo') if b.find('img')['src']=='/assets/residences-autumn.webp')
        lead['class']=lead.get('class',[])+['mosaic-wide']
        grid.insert(0,lead.extract())
        heading=soup.select_one(".home-gallery .heading-grid p")
        if heading:
            heading.string="Kitchens, living spaces and landscaped grounds from both communities. Open a photo to see it larger."
        labels={
          "/assets/plaza-bedroom.webp":("Plaza East kitchen, wood cabinetry","PLAZA EAST · KITCHEN"),
          "/assets/summerhill-kitchen.webp":("SummerHill updated kitchen with white cabinetry","SUMMERHILL · KITCHEN"),
          "/assets/plaza-living.webp":("Plaza East living room with fireplace and deck access","PLAZA EAST · LIVING"),
          "/assets/summerhill-living.webp":("SummerHill bright living space with updated flooring","SUMMERHILL · LIVING"),
          "/assets/residences-autumn.webp":("Autumn landscaping outside townhouses","COMMUNITY · GROUNDS"),
          "/assets/summerhill-residences.webp":("SummerHill townhouses and landscaping","SUMMERHILL · EXTERIOR"),
        }
        for b in grid.select(".gallery-photo"):
            im=b.find("img"); alt,tag=labels[im["src"]]; im["alt"]=alt
            b["aria-label"]="Open photo: "+alt
            lab=b.select_one(".gallery-label")
            if lab: lab.string=tag
        # Intentional pacing: homes -> photography -> amenities -> location.
        homes=soup.select_one("section.homes")
        benefits=soup.select_one("section.benefits")
        gallery=soup.select_one("section.home-gallery")
        if not homes or not benefits or not gallery:raise RuntimeError("Expected homepage section missing")
        benefits.insert_before(gallery.extract())
    if filename in ("plaza-east.html","summerhill.html"):
        is_plaza=filename.startswith("plaza")
        photo="/assets/plaza-kitchen.webp" if is_plaza else "/assets/summerhill-bedroom.webp"
        alt="Bright Plaza East bedroom with white closets and carpet" if is_plaza else "SummerHill open-plan living room with freestanding gas fireplace"
        eyebrow="PLAZA EAST / A BEDROOM" if is_plaza else "SUMMERHILL / THE LIVING SPACE"
        heading="Space to settle in." if is_plaza else "An open place to gather."
        copy=("A bright bedroom with ample wall space and built-in closet access. Specific room sizes and finishes vary by residence."
              if is_plaza else "A sunny open-plan living area with the fireplace as its focal point. Layout and finishes vary by residence.")
        section=BeautifulSoup(f"""
          <section class="curated-interior section" aria-label="Featured interior photograph">
            <div class="container curated-interior-layout">
              <div class="curated-image-wrap">
                <button class="gallery-photo curated-hero-image" type="button" data-gallery-image aria-label="Open featured interior photo">
                  <img src="{photo}" alt="{alt}" loading="lazy" decoding="async">
                  <span class="gallery-expand" aria-hidden="true">↗</span>
                </button>
              </div>
              <div class="curated-image-copy reveal">
                <p class="eyebrow">{eyebrow}</p><h2>{heading}</h2>
                <p>{copy}</p><a class="curated-gallery-jump" href="#gallery">Browse all photographs <span aria-hidden="true">↗</span></a>
              </div>
            </div>
          </section>""","html.parser").select_one("section")
        intro=soup.select_one("section.detail-intro")
        if not intro:raise RuntimeError("Detail introduction missing")
        intro.insert_after(section)
        gh=soup.select_one(".detail-gallery .heading-grid p")
        if gh:gh.string="Photos from the owner's original property gallery. Individual interiors and finishes vary; contact leasing for unit-specific details."
    (ROOT/filename).write_text(str(soup),encoding="utf-8")

# CSS is a small additive layer, avoiding a framework or new runtime dependency.
shutil.copyfile(ROOT/"assets/site-v6.css",ROOT/"assets/site-v7.css")
with (ROOT/"assets/site-v7.css").open("a") as f:
    f.write("""
/* V7 / carefully paced property photography */
.mosaic-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));grid-template-rows:repeat(3,minmax(190px,18vw));gap:12px}
.mosaic-grid .gallery-photo{min-height:0}
.mosaic-grid .mosaic-wide{grid-column:1/3;grid-row:1/3}
.curated-interior{padding-top:0;background:var(--paper)}
.curated-interior-layout{display:grid;grid-template-columns:minmax(0,1.25fr) minmax(280px,.75fr);align-items:center;gap:clamp(32px,7vw,118px)}
.curated-image-wrap{height:clamp(360px,43vw,620px);overflow:hidden;border-radius:3px}
.curated-hero-image{width:100%;height:100%;display:block;position:relative;border:0;cursor:zoom-in;text-align:left}
.curated-hero-image img{width:100%;height:100%;object-fit:cover;object-position:center}
.curated-image-copy h2{font:400 clamp(55px,6vw,94px)/1 var(--serif);letter-spacing:-.04em;margin:22px 0 26px}
.curated-image-copy>p:not(.eyebrow){font-size:16px;line-height:1.8;max-width:33ch;color:var(--muted)}
.curated-gallery-jump{display:inline-flex;gap:16px;margin-top:30px;padding-bottom:9px;border-bottom:1px solid currentColor;font-weight:600;font-size:13px}
.curated-gallery-jump span{transition:transform .28s}
.curated-gallery-jump:hover span{transform:translate(3px,-3px)}
@media(max-width:900px){.mosaic-grid{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:220px;grid-template-rows:none}.mosaic-grid .mosaic-wide{grid-column:span 2;grid-row:span 1;min-height:380px}.mosaic-grid .gallery-photo:last-child{grid-column:span 2;min-height:280px}.curated-interior-layout{grid-template-columns:1fr;gap:32px}.curated-image-wrap{height:clamp(330px,60vw,530px)}.curated-image-copy h2{font-size:68px}}
@media(max-width:500px){.mosaic-grid{grid-template-columns:repeat(2,minmax(0,1fr));grid-auto-rows:190px;gap:9px}.mosaic-grid .mosaic-wide{min-height:265px}.curated-interior{padding-top:0}.curated-image-wrap{height:300px}.curated-image-copy h2{font-size:56px}.curated-image-copy>p:not(.eyebrow){font-size:14px}}
@media(prefers-reduced-motion:reduce){.curated-gallery-jump span,.curated-hero-image img{transition:none!important}}
""")
shutil.copyfile(ROOT/"assets/site-v6.js",ROOT/"assets/site-v7.js")
for name in ["index.html","plaza-east.html","summerhill.html","neighborhood.html","contact.html","privacy.html"]:
    html=(ROOT/name).read_text().replace("/assets/site-v6.css","/assets/site-v7.css").replace("/assets/site-v6.js","/assets/site-v7.js")
    (ROOT/name).write_text(html,encoding="utf-8")
print("V7 regenerated. Strategic photo assignments:",sum(len(x) for x in STORY.values()),"local visual assets plus archived property gallery images.")

# Keep IMAGE_SOURCES.md accurate after every regeneration.
import json
manifest=[]
for name in ["index.html","plaza-east.html","summerhill.html","neighborhood.html"]:
    soup=BeautifulSoup((ROOT/name).read_text(),"html.parser")
    for photo in soup.select('main img[src]'):
        if not photo['src']:continue
        manifest.append({"page":name,"src":photo['src'],"description":photo.get('alt','')})
(ROOT/"photo-manifest.json").write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n",encoding="utf8")
lines=["# IthacaHome photography sources — V7", "", "All photographs used on the site are served from local `/assets/` paths in the new repository. The 22 historic gallery photos were archived from the owner's original Wix site and are stored in `assets/property-gallery/` in GitHub. The additional community and interior photographs were supplied by the client or extracted from their marketing flyer.", "", "The visitor-facing pages do not hotlink Wix or Apartments.com photos. The Apartments.com 3D tour link opens on their website and requires that external site to remain available.", "", "Every rendered content-image path is assigned to exactly one place across the entire website. See `photo-manifest.json` and `PHOTO_PLACEMENT.md` for placements. Appearance-based checks can confirm exact local duplicates; visually similar variants in archived photos should be reviewed during final owner proofing.", "", "Client should confirm rights to all property photography before publication."]
(ROOT/"IMAGE_SOURCES.md").write_text("\n".join(lines)+"\n",encoding="utf8")
