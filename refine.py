"""Refine the IthacaHome editorial website with owner flyer + existing site details.
Run after build.py and enhance.py. Idempotent.
"""
from pathlib import Path
from bs4 import BeautifulSoup
P=Path(__file__).resolve().parent
TOURS='https://www.apartments.com/plaza-east-summerhill-townhouses-ithaca-ny/przvhlr/'

def fragment(x):return BeautifulSoup(x,'html.parser')
for name in ['index.html','plaza-east.html','summerhill.html','neighborhood.html','contact.html','privacy.html']:
    p=P/name
    s=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
    if s.html.has_attr('data-final-refinement'):continue
    s.html['data-final-refinement']='3'
    stylesheet=s.new_tag('link',rel='stylesheet',href='/assets/editorial.css')
    s.head.append(stylesheet)
    script=s.new_tag('script',src='/assets/editorial.js',defer=True)
    s.body.append(script)
    # Branding from owner's flyer. Already enhanced by enhance.py.
    for img in s.select('img'):
        if img.get('src')=='/assets/plaza-kitchen.webp':img['alt']='Plaza East bright bedroom with adjacent living spaces'
        if img.get('src')=='/assets/plaza-bedroom.webp':img['alt']='Plaza East full kitchen with wood cabinetry'
        if img.get('src')=='/assets/summerhill-bedroom.webp':img['alt']='SummerHill open-plan living space and tiled floors'
        if img.get('src')=='/assets/summerhill-living.webp':img['alt']='SummerHill renovated bedroom with new flooring'
    s.select_one('.site-header').append(fragment('<div class="nav-utility">222 SUMMERHILL DR. / ITHACA NY</div>'))
    # Use clean nav and include renters' FAQ access everywhere.
    nav=s.select_one('.desktop-nav')
    if nav:
        exp=nav.select_one('a[data-nav="experience"]')
        if exp:exp.string='The IthacaHome difference'
        if name=='index.html':
            faq=s.new_tag('a',href='/#faq');faq.string='FAQ';nav.insert(-1,faq)
        else:
            faq=s.new_tag('a',href='/#faq');faq.string='FAQ';nav.insert(-1,faq)
    mobile=s.select_one('#mobile-nav')
    if mobile:
        a=s.new_tag('a',href='/#faq');a.string='Leasing FAQ'
        contact=next((x for x in mobile.select('a') if x.get('href')=='/contact.html'),None)
        if contact:contact.insert_before(a)
    footer_menu=s.select_one('.footer-grid > div:nth-of-type(2)')
    if footer_menu:
        link=s.new_tag('a',href='/#faq');link.string='Leasing FAQ';footer_menu.append(link)
        ext=s.new_tag('a',href=TOURS,target='_blank',rel='noopener noreferrer');ext.string='Explore 3D tours ↗';footer_menu.append(ext)
    # Owner-provided original logo accent in footer
    if name=='index.html':
        hero=s.select_one('.hero-home')
        if hero:
            hero.append(fragment('''<div class="hero-issue" aria-hidden="true"><span>EXCLUSIVE RESIDENCES</span><span>NO. 001 · ITHACA NY</span></div><div class="hero-grid-lines" aria-hidden="true"></div>'''))
        # Place a sourced testimonial section right after neighborhood signature.
        signature=s.select_one('.signature-section')
        if signature:
            signature.insert_after(fragment('''
<section class="residents-section section-shell" id="resident-stories" aria-label="What residents say">
 <div class="residents-heading reveal"><div class="section-index"><span class="section-index-line"></span> 04 / PEOPLE MAKE THE PLACE</div><h2>Good spaces.<br><em>Great stories.</em></h2><p>Real residents. Real reasons to call IthacaHome home.</p></div>
 <div class="residents-slider" id="resident-slider" tabindex="0" aria-label="Resident testimonial carousel">
  <article class="resident-quote"><span class="quote-no">01 / 03</span><span class="giant-quote" aria-hidden="true">“</span><blockquote>“Love this place! The staff was amazing...”</blockquote><div class="resident-byline"><strong>AYLA</strong><span>Resident · shared on IthacaHome.com</span></div></article>
  <article class="resident-quote"><span class="quote-no">02 / 03</span><span class="giant-quote" aria-hidden="true">“</span><blockquote>Grateful for the team's help creating a safe, comfortable stay.</blockquote><div class="resident-byline"><strong>JAEJEONG</strong><span>Resident · message paraphrased from IthacaHome.com</span></div></article>
  <article class="resident-quote"><span class="quote-no">03 / 03</span><span class="giant-quote" aria-hidden="true">“</span><blockquote>Four years at SummerHill, and appreciation for the caring management team.</blockquote><div class="resident-byline"><strong>SHAOQUN</strong><span>Resident · message paraphrased from IthacaHome.com</span></div></article>
 </div><div class="resident-controls"><span>WORDS FROM OUR COMMUNITY / 03</span><div><button id="resident-prev" type="button" aria-label="Previous resident story">←</button><button id="resident-next" type="button" aria-label="Next resident story">→</button></div></div>
</section>'''))
        # Install FAQ after property floor-plan explorer.
        fit=s.select_one('.find-fit')
        if fit:
            fit.insert_after(fragment(f'''
<section class="tour-spotlight" id="virtual-tours"><div class="tour-backdrop"><img src="/assets/plaza-living.webp" loading="lazy" alt="Plaza East light-filled living room and fireplace"></div><div class="tour-backdrop-shade"></div><div class="tour-content"><span class="eyebrow">CAN'T MAKE IT IN PERSON?</span><h2>Take a closer <em>look.</em></h2><p>Step inside with virtual tours and explore floor plans at your own pace.</p><a href="{TOURS}" target="_blank" rel="noopener noreferrer">EXPLORE 3D TOURS <span>↗</span></a></div><div class="tour-index" aria-hidden="true">IH / TAKE A TOUR</div></section>
<section class="faq-section section-shell" id="faq"><div class="faq-heading"><div class="section-index"><span class="section-index-line"></span> 06 / THE DETAILS</div><h2>Good to <em>know.</em></h2><p>Answers to a few common questions, adapted from IthacaHome's existing rental website.</p><a href="/contact.html">Still curious? Let's talk ↗</a></div>
<div class="faq-list">
 <details class="faq-row"><summary><span class="faq-number">01</span><span>Are leases typically one year?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>Yes. Leases are generally annual, although shorter stays are sometimes possible. Ask the leasing team about current options.</div></details>
 <details class="faq-row"><summary><span class="faq-number">02</span><span>Are the residences furnished?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>Residences are normally rented unfurnished. Photos may show staged spaces. Inquire if you need a furnished option.</div></details>
 <details class="faq-row"><summary><span class="faq-number">03</span><span>Are pets welcome?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>Yes—pets are welcome, subject to the community's current pet rules. The first pet has no additional monthly charge; ask about additional pets and any applicable restrictions.</div></details>
 <details class="faq-row"><summary><span class="faq-number">04</span><span>How far is Cornell?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>The existing IthacaHome website describes the Cornell main campus as approximately one mile away. A nearby TCAT stop provides another option; check published bus timetables for current service.</div></details>
 <details class="faq-row"><summary><span class="faq-number">05</span><span>What's included in the rent?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>The owner's leasing flyer lists internet, cable, water, sewer and snow removal among included services. Check the terms of your specific lease for the final inclusions and fees.</div></details>
 <details class="faq-row"><summary><span class="faq-number">06</span><span>How do I arrange a tour or ask about availability?</span><span class="faq-plus" aria-hidden="true">+</span></summary><div>Send a leasing inquiry online, or email <a href="mailto:rentals@ithacahome.com">rentals@ithacahome.com</a>. The leasing team can share current availability, pricing and viewing options.</div></details>
</div></section>'''))
        # Make imagery and labels accurate rather than swapped by filenames
        imgs=s.select('.final-gallery-grid figure')
        if len(imgs)==3:
            imgs[0].select_one('figcaption').string='PLAZA EAST / PRIVATE LIVING SPACE'
            imgs[1].select_one('figcaption').string='SUMMERHILL / FRESHLY FINISHED BEDROOM'
            imgs[2].select_one('figcaption').string='SUMMERHILL / OPEN LIVING SPACE'
        # section numbers sequential by new order, no need to promise they are chronological
    elif name in ('plaza-east.html','summerhill.html'):
        intro=s.select_one('.detail-intro')
        if intro:
            plaza=name.startswith('plaza')
            addition='Plaza East: private bath in each bedroom, central A/C, high ceilings, fireplaces and private decks.' if plaza else 'SummerHill: remodeled kitchens and flooring, gas fireplaces, ceiling fans and in-unit laundry.'
            intro.append(fragment(f'<p class="property-source-note">{addition} Ask about specific floor plans and current availability.</p>'))
        gallery=s.select_one('.detail-gallery')
        if gallery:
            gallery.insert_after(fragment(f'''<section class="details-story section-shell"><div><div class="section-index"><span class="section-index-line"></span> SEE IT FOR YOURSELF</div><h2>Step inside.<br><em>Look around.</em></h2><p>Want to explore at your own pace? View the existing property 3D tours, floor plan illustrations and more photography.</p><a href="{TOURS}" target="_blank" rel="noopener noreferrer">VIEW THE 3D TOURS ↗</a></div><div class="details-story-photo"><img src="/assets/{'plaza-bedroom.webp' if plaza else 'summerhill-kitchen.webp'}" loading="lazy" alt="{'Plaza East fitted kitchen' if plaza else 'SummerHill kitchen with white cabinetry'}"></div></section>'''))
        if name.startswith('plaza'):
            note=s.select_one('.community-amenity-note')
            if note:note.append(' Washer/dryer configurations and availability should be confirmed for the individual apartment or townhouse.')
    elif name=='neighborhood.html':
        cards=s.select_one('.neighborhood-cards')
        if cards:cards.insert_after(fragment('''<section class="area-walk section-shell"><div class="area-walk-photo"><img src="/assets/lakeside-walk.webp" alt="Boardwalk through a natural meadow near Ithaca" loading="lazy"></div><div class="area-walk-copy"><div class="section-index"><span class="section-index-line"></span> A LITTLE BIT OF EVERYTHING</div><h2>Closer to<br><em>your everyday.</em></h2><p>East Hill Plaza offers a grocery store, Collegetown Bagels, a fitness center, a salon and other neighborhood conveniences, according to the property's existing website.</p><p>A nearby TCAT stop helps make Cornell and greater Ithaca easier to reach. Verify current schedules directly with TCAT.</p><a href="https://tcatbus.com/" target="_blank" rel="noopener noreferrer">EXPLORE TCAT SERVICE ↗</a></div></section>'''))
    elif name=='contact.html':
        side=s.select_one('.contact-form-side')
        if side:side.append(fragment('''<div class="contact-side-note"><span>EMAIL IS PREFERRED</span><a href="mailto:rentals@ithacahome.com">rentals@ithacahome.com ↗</a><p>222 Summerhill Drive, Ithaca, NY 14850</p></div>'''))
    p.write_text(str(s),encoding='utf8')
print('Refinements complete')