"""IthacaHome visual design system, derived from the owner's leasing flyer.
Run after build.py. Idempotent for direct re-runs.
"""
from pathlib import Path
from bs4 import BeautifulSoup
from html import escape
P=Path(__file__).resolve().parent

brand_mark='''<span class="roof-mark" aria-hidden="true"><svg viewBox="0 0 94 34" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M2 29L47 4L92 29" stroke="currentColor" stroke-width="3" stroke-linecap="square"/><path d="M15 29H79" stroke="currentColor" stroke-opacity=".48" stroke-width="1"/></svg></span><span class="brand-lettering"><span>ITHACA</span><strong>HOME</strong></span>'''
benefits = [
('01','Everyday ease','Internet, cable, water, sewer & snow removal included'),
('02','Close to Cornell','Near a TCAT stop with frequent campus connections'),
('03','Right at home','Pet friendly — first pet free'),
('04','Here when needed','On-site maintenance & online service requests')]

for filename in ['index.html','plaza-east.html','summerhill.html','neighborhood.html','contact.html','privacy.html']:
    path=P/filename
    soup=BeautifulSoup(path.read_text(encoding='utf8'),'html.parser')
    if soup.html.has_attr('data-design-version'): continue
    soup.html['data-design-version']='2'
    head=soup.head
    font=soup.new_tag('link',rel='stylesheet',href='https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=Manrope:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500;1,600&display=swap')
    head.append(font)
    theme=head.select_one('meta[name="theme-color"]');theme['content']='#831a27'
    brand=soup.select_one('.site-header .brand')
    if brand:brand.clear();brand.append(BeautifulSoup(brand_mark,'html.parser'))
    footer_logo=soup.select_one('.footer-logo')
    if footer_logo:footer_logo.clear();footer_logo.append(BeautifulSoup(brand_mark,'html.parser'))
    nav=soup.select_one('.desktop-nav')
    if nav:
        nav.select_one('.nav-contact').string=''
        nav.select_one('.nav-contact').append(BeautifulSoup('<span>Schedule a tour</span><span class="nav-cta-arrow">↗</span>','html.parser'))
    if soup.select_one('.site-header'):
        soup.select_one('.site-header').insert_after(BeautifulSoup('<span class="header-scanline" aria-hidden="true"></span>','html.parser'))
    footer=soup.select_one('.footer')
    if footer:
        footer.select_one('.footer-top .eyebrow').string='THE NEXT CHAPTER STARTS HERE'
        footer.select_one('.footer-grid p').string='Thoughtfully maintained apartments and townhouses near Cornell University. Ithaca, New York.'
    main=soup.select_one('main')
    if not main:continue
    if filename=='index.html':
        hero=soup.select_one('.hero-home')
        img=hero.select_one('img.hero-image');img['src']='/assets/plaza-street.webp';img['alt']='Plaza East apartments and landscaped grounds in Ithaca, NY';img['width']='2048';img['height']='1600'
        hero.select_one('.hero-topline').clear()
        hero.select_one('.hero-topline').append(BeautifulSoup('<span>PLAZA EAST + SUMMERHILL / ITHACA, NEW YORK</span><span>EXPLORE THE COLLECTION &nbsp; ↘</span>','html.parser'))
        hero.select_one('.hero-kicker').clear()
        hero.select_one('.hero-kicker').append(BeautifulSoup('<span class="dot"></span> LUXURY APARTMENTS &amp; TOWNHOUSES <span class="hero-kicker-line"></span> NEAR CORNELL UNIVERSITY','html.parser'))
        hero.select_one('h1').clear()
        hero.select_one('h1').append(BeautifulSoup('<span class="hero-title-line">A better way</span><span class="hero-title-line hero-title-indent">to <em>live.</em></span>','html.parser'))
        hero.select_one('.hero-bottom-copy p').string='Room to settle in. Space to thrive. Exceptional apartments and townhouses with the conveniences you want, right where you want to be.'
        hero.select_one('.hero-rail').clear();hero.select_one('.hero-rail').append(BeautifulSoup('<span>42°26′ N / 76°29′ W</span><span>SCROLL TO EXPLORE ↓</span>','html.parser'))
        hero.append(BeautifulSoup('''<div class="hero-polaroid" aria-hidden="true"><div class="hero-polaroid-image"><img src="/assets/plaza-living.webp" alt="" width="450" height="300"></div><div class="polaroid-caption"><span>01 / PLAZA EAST</span><span>THE SPACE YOU DESERVE ↗</span></div></div><div class="hero-vertical">ITHACAHOME — YOUR PLACE IN ITHACA</div><div class="hero-corner-seal" aria-hidden="true">IH<br><small>NY</small></div>''','html.parser'))
        ticker=soup.select_one('.ticker')
        ticker.replace_with(BeautifulSoup('''<section class="perks-strip" aria-label="Community highlights"><div class="perks-track"><div><span class="perk-icon">✳</span><span>2, 3 &amp; 4 BEDROOM LAYOUTS</span></div><div><span class="perk-icon">✳</span><span>UTILITIES INCLUDED</span></div><div><span class="perk-icon">✳</span><span>PET FRIENDLY / FIRST PET FREE</span></div><div><span class="perk-icon">✳</span><span>MINUTES FROM CORNELL</span></div></div></section>''','html.parser'))
        intro=soup.select_one('.intro')
        intro.select_one('.intro-side .section-index').clear(); intro.select_one('.intro-side .section-index').append(BeautifulSoup('<span class="section-index-line"></span> 01 / THE ITHACAHOME EXPERIENCE','html.parser'))
        intro.select_one('.intro-body h2').clear();intro.select_one('.intro-body h2').append(BeautifulSoup('More of what<br>makes a house<br><em>feel like home.</em>','html.parser'))
        intro.select_one('.intro-under p').string='Spacious floor plans, professionally landscaped grounds, included utilities, on-site maintenance, and a location that keeps Cornell close. Consider this your invitation to live a little better.'
        intro.select_one('.starburst').string='✳'
        intro.select_one('.intro-stamp').replace_with(BeautifulSoup('''<div class="intro-editorial-photos" aria-label="IthacaHome residences"><figure class="intro-photo-large"><img src="/assets/summerhill-kitchen.webp" alt="SummerHill townhouse bright remodeled kitchen" loading="lazy"><figcaption>SUMMERHILL / REMODELED INTERIORS</figcaption></figure><figure class="intro-photo-small"><img src="/assets/plaza-bedroom.webp" alt="Plaza East spacious kitchen" loading="lazy"><figcaption>PLAZA EAST / SPACES TO CALL YOUR OWN</figcaption></figure></div>''','html.parser'))
        homes=soup.select_one('.residences-section')
        homes.select_one('.micro-kicker').string='TWO DISTINCT COMMUNITIES. ONE PLACE TO CALL HOME.'
        homes.select_one('.residences-head-right h2').clear();homes.select_one('.residences-head-right h2').append(BeautifulSoup('Find your<br><em>perfect fit.</em>','html.parser'))
        homes.select_one('#explorer-img')['src']='/assets/plaza-street.webp'
        homes.select_one('#explorer-description').string='Spacious apartments and townhouses with high ceilings, fireplaces, private decks, air conditioning, free parking, and a full private bathroom in each bedroom.'
        panel=homes.select_one('.property-explorer-image')
        panel.append(BeautifulSoup('''<div class="explorer-mini-image"><img id="explorer-mini" src="/assets/plaza-living.webp" alt="Plaza East bright living room" loading="lazy"><span>STEP INSIDE ↗</span></div>''','html.parser'))
        homes.select_one('.explorer-eyebrow').string='THE PLAZA EAST COLLECTION'
        homes.select_one('#explorer-feature').string='EN-SUITE'
        homes.select_one('#explorer-feature-label').string='BATHROOMS'
        mini_nav=BeautifulSoup('''<div class="residences-mini-nav"><a href="/plaza-east.html"><span>EXPLORE PROPERTY 01</span><strong>Plaza East ↗</strong></a><a href="/summerhill.html"><span>EXPLORE PROPERTY 02</span><strong>SummerHill ↗</strong></a></div>''','html.parser')
        homes.append(mini_nav)
        pr=soup.select_one('.principles')
        pr.select_one('.principles-heading h2').clear();pr.select_one('.principles-heading h2').append(BeautifulSoup('The extras that<br><em>change everything.</em>','html.parser'))
        pr.select_one('.principles-heading p').string='Every detail is thoughtfully considered to make each day a little easier.'
        cards=pr.select('.principle')
        details=[('01','◈','A simpler everyday.','Internet, cable, water, sewer, and snow removal included.'),('02','↗','Better connected.','Near a TCAT stop with service to Cornell University and local destinations.'),('03','✳','Made for real life.','On-site maintenance, an online repair portal, and beautifully maintained grounds.')]
        for el,(n,icon,title,desc) in zip(cards,details):
            el.select_one('.principle-no').string=n;el.select_one('.principle-art').string=icon;el.select_one('h3').string=title;el.select_one('p').string=desc
        pr.insert_after(BeautifulSoup('''<section class="signature-section" aria-label="Designed around your life"><div class="signature-visual"><img src="/assets/summerhill-street.webp" alt="SummerHill townhouses with landscaped lawns and parking" loading="lazy"><span class="signature-coordinate">42°26′N / ITHACA, NY</span></div><div class="signature-info"><span class="section-index">THE EVERYDAY / ELEVATED</span><div class="signature-index">IH / 02</div><h2>Good living.<br><em>Great location.</em></h2><p>Near East Hill Plaza and a TCAT stop with frequent connections to Cornell, IthacaHome places everything within easier reach.</p><div class="signature-facts"><div><strong>02</strong><span>EV charging stations</span></div><div><strong>90%</strong><span>Maintenance requests resolved the same day*</span></div></div><small>*According to the property's leasing materials.</small><a class="signature-link" href="/neighborhood.html">GET TO KNOW THE NEIGHBORHOOD <span>↗</span></a></div></section>''','html.parser'))
        interlude=soup.select_one('.interlude')
        interlude.select_one('.interlude-photo img')['src']='/assets/residences-autumn.webp'
        interlude.select_one('h2').clear();interlude.select_one('h2').append(BeautifulSoup('Come home to<br><em>something more.</em>','html.parser'))
        fit=soup.select_one('.find-fit');fit.select_one('h2').clear();fit.select_one('h2').append(BeautifulSoup('Your space.<br><em>Your way.</em>','html.parser'))
        fit.select_one('.fit-head p').string='Browse the bedroom configurations across our two communities. Then inquire about specific available residences and rates.'
        # Add photo-backed inviting tour closer.
        soup.select_one('.contact-strip').insert_before(BeautifulSoup('''<section class="final-gallery"><div class="final-gallery-title"><span>THE GALLERY / A LOOK INSIDE</span><h2>Imagine yourself <em>here.</em></h2><a href="/contact.html">SCHEDULE A PRIVATE TOUR ↗</a></div><div class="final-gallery-grid"><figure><img src="/assets/plaza-kitchen.webp" loading="lazy" alt="Plaza East kitchen with wood cabinetry"><figcaption>PLAZA EAST / KITCHEN</figcaption></figure><figure><img src="/assets/summerhill-living.webp" loading="lazy" alt="SummerHill townhouse refreshed bedroom"><figcaption>SUMMERHILL / INTERIOR</figcaption></figure><figure><img src="/assets/summerhill-bedroom.webp" loading="lazy" alt="SummerHill townhouse living area"><figcaption>SUMMERHILL / LIVING</figcaption></figure></div></section>''','html.parser'))
    elif filename in ('plaza-east.html','summerhill.html'):
        plaza=filename.startswith('plaza')
        detail=soup.select_one('.detail-hero')
        detail.select_one('img')['src']='/assets/plaza-street.webp' if plaza else '/assets/summerhill-street.webp'
        detail.select_one('img')['alt']='Plaza East apartment residences and parking' if plaza else 'SummerHill townhouse residences and landscaping'
        detail.select_one('.detail-hero-inner .eyebrow').string='ITHACAHOME / THE SIGNATURE COLLECTION' if plaza else 'ITHACAHOME / THE TOWNHOUSE COLLECTION'
        detail.select_one('.detail-hero-inner h1').clear()
        detail.select_one('.detail-hero-inner h1').append(BeautifulSoup('Plaza <em>East.</em>' if plaza else 'Summer<em>Hill.</em>','html.parser'))
        detail.select_one('.detail-bottom p').string=('Apartments and townhouses with generous rooms, private bathrooms, and thoughtful everyday conveniences.' if plaza else 'Newly remodeled two-level townhouses with private decks, updated kitchens and room to live well.')
        detail.append(BeautifulSoup('''<div class="detail-side-note">THE ITHACAHOME COLLECTION / ITHACA, NY</div>''','html.parser'))
        gallery=soup.select_one('.gallery-grid')
        gallery.clear()
        shots=([
            ('plaza-street.webp','Plaza East exterior and landscaped entrance'),
            ('plaza-kitchen.webp','Plaza East kitchen and cabinetry'),
            ('plaza-living.webp','Plaza East living room and fireplace'),
            ('plaza-bedroom.webp','Plaza East bedroom')]
            if plaza else [
            ('summerhill-street.webp','SummerHill townhouses exterior'),
            ('summerhill-kitchen.webp','SummerHill renovated white kitchen'),
            ('summerhill-living.webp','SummerHill interior'),
            ('summerhill-bedroom.webp','SummerHill living and fireplace')])
        for i,(file,description) in enumerate(shots,1):
            gallery.append(BeautifulSoup(f'<button class="gallery-item {"gallery-major" if i==1 else ""}" type="button" data-lightbox-image="/assets/{file}" data-lightbox-title="{escape(description,quote=True)}" aria-label="View photo: {escape(description,quote=True)}"><img src="/assets/{file}" alt="{escape(description,quote=True)}" loading="lazy"><span>{i:02d} / VIEW IMAGE ↗</span></button>','html.parser'))
        intro=soup.select_one('.detail-intro .detail-intro-copy p')
        intro.string=('Plaza East offers two-, three- and four-bedroom floor plans with air conditioning, tall ceilings, spacious rooms, fireplaces, private decks, free parking, and full private bathrooms in each bedroom. Ask us about the layout and included features of your specific residence.' if plaza else 'SummerHill offers newly remodeled two- and three-bedroom townhouses with bedrooms upstairs, refreshed kitchen cabinets and flooring, large windows with blinds, in-unit washer and dryer, private decks, gas fireplaces, ceiling fans, and free parking.')
        amenities=soup.select_one('.amenity-list')
        amenities.clear()
        items=(['Air conditioning','High ceilings & spacious rooms','Full private bathroom in each bedroom','In-unit laundry room','Fireplace','Large windows with blinds','Private deck','Free parking'] if plaza else ['New kitchen cabinets','New flooring','Large windows with blinds','In-unit washer & dryer','Private deck','Gas fireplace','Ceiling fans','Free parking'])
        for it in items: amenities.append(BeautifulSoup(f'<li><span class="feature-star">✳</span>{escape(it)}</li>','html.parser'))
        amenities.insert_after(BeautifulSoup('''<p class="community-amenity-note">Across the IthacaHome community: professionally landscaped grounds, on-site maintenance, an online repair request platform, two EV charging stations and pet-friendly living. Utilities included: internet, cable, water, sewer and snow removal. First pet free. Confirm details for your individual lease.</p>''','html.parser'))
        # Distinctive home detail photo block for richness.
        amenities.insert_after(BeautifulSoup(f'''<div class="property-photo-interlude"><img src="/assets/{'plaza-living.webp' if plaza else 'summerhill-kitchen.webp'}" alt="{'Plaza East bright living area with fireplace' if plaza else 'SummerHill newly remodeled kitchen'}" loading="lazy"><div><span>IT'S ALL IN THE DETAILS</span><strong>{'A little more space. A lot more possibility.' if plaza else 'Recently refreshed. Ready for what comes next.'}</strong></div></div>''','html.parser'))
    elif filename=='neighborhood.html':
        img=soup.select_one('.detail-hero-bg img');img['src']='/assets/lakeside-walk.webp'
        intro=soup.select_one('.neighborhood-intro p')
        if intro:intro.string='Find yourself close to Cornell University, East Hill Plaza, and nearby TCAT service. According to IthacaHome leasing materials, the bus stop offers frequent connections to campus; check TCAT for current timetables.'
    elif filename=='contact.html':
        img=soup.select_one('.contact-header-image img');img['src']='/assets/plaza-street.webp';img['alt']='Plaza East residences in Ithaca, New York'
        soup.select_one('.contact-hero-copy h1').clear();soup.select_one('.contact-hero-copy h1').append(BeautifulSoup('Come see<br><em>for yourself.</em>','html.parser'))
        soup.select_one('.contact-hero-copy p').string='We would love to show you around. Explore availability, ask about floor plans, or schedule your visit to Plaza East or SummerHill.'
        soup.select_one('.contact-form-side h2').clear();soup.select_one('.contact-form-side h2').append(BeautifulSoup('Your next home<br><em>starts here.</em>','html.parser'))
        soup.select_one('.side-property-photo img')['src']='/assets/summerhill-street.webp'
        soup.select_one('.side-property-photo img')['alt']='SummerHill townhouses landscaped exterior'
    # A load-in curtain with graceful reduced-motion fallback, independent of form and content.
    curtain=BeautifulSoup('''<div class="site-reveal-curtain" aria-hidden="true"><span>IH / ITHACAHOME</span></div>''','html.parser')
    soup.body.insert(0,curtain)
    path.write_text(str(soup),encoding='utf8')
print('Applied IthacaHome editorial design system.')