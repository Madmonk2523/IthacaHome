/* IthacaHome — deliberately dependency-free motion & interaction. */
(() => {
  'use strict';
  const $ = (s, context=document) => context.querySelector(s);
  const $$ = (s, context=document) => [...context.querySelectorAll(s)];
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // Sticky navigation, subtle image motion, progress indicator.
  const header = $('#site-header');
  const progress = $('#scroll-progress');
  let scheduled = false;
  function onScroll() {
    const y = window.scrollY || 0;
    header?.classList.toggle('scrolled', y > 84);
    if (progress) {
      const room = document.documentElement.scrollHeight - innerHeight;
      progress.style.width = `${room ? Math.min(100,(y / room) * 100) : 0}%`;
    }
    if (!reduceMotion && y < innerHeight * 1.5) {
      const hero = $('.hero-home .hero-image');
      if (hero) hero.style.transform = `scale(${1 + Math.min(.085,y * .000085)}) translate3d(0,${Math.min(35,y*.03)}px,0)`;
    }
    scheduled = false;
  }
  window.addEventListener('scroll', () => { if(!scheduled){requestAnimationFrame(onScroll);scheduled = true;} }, {passive:true});
  onScroll();
  $('#year') && ($('#year').textContent = new Date().getFullYear());

  // Navigation overlay on small screens.
  const menuButton = $('#menu-toggle');
  const menu = $('#mobile-nav');
  const setMenu = open => {
    menu?.classList.toggle('open', open);
    header?.classList.toggle('menu-open', open);
    document.body.classList.toggle('no-scroll', open);
    menu?.setAttribute('aria-hidden', String(!open));
    menuButton?.setAttribute('aria-expanded', String(open));
    menuButton?.setAttribute('aria-label', open ? 'Close menu':'Open menu');
  };
  menuButton?.addEventListener('click', () => setMenu(!menu?.classList.contains('open')));
  $$('#mobile-nav a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
  document.addEventListener('keydown',ev=>{ if(ev.key==='Escape') setMenu(false); });

  // Respect prefers-reduced-motion; reveal on entry, no heavy animation library.
  const reveals = $$('.reveal');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const obs = new IntersectionObserver(entries => entries.forEach(entry => {
      if(entry.isIntersecting){entry.target.classList.add('is-visible'); obs.unobserve(entry.target);}
    }),{rootMargin:'0px 0px -9% 0px',threshold:.03});
    reveals.forEach(el => obs.observe(el));
  } else reveals.forEach(el=>el.classList.add('is-visible'));

  // An architecturally-inspired property switcher.
  const properties = {
    plaza: {
      image:'/assets/plaza-east-exterior.webp',alt:'Plaza East exterior and residences',
      label:'PLAZA EAST / ITHACA, NY',no:'01',eyebrow:'THE SIGNATURE COLLECTION',
      title:'Plaza <em>East.</em>',description:'Open, light-filled apartments and townhouses designed with space to live your way. Thoughtful finishes, private bedrooms, and everyday ease.',
      bedrooms:'02 — 04',feature:'PRIVATE',featureLabel:'EN-SUITE BATHROOMS',link:'/plaza-east.html',linkText:'Discover Plaza East'
    },
    summer: {
      image:'/assets/summerhill-residences.webp',alt:'SummerHill townhouse exterior',
      label:'SUMMERHILL / ITHACA, NY',no:'02',eyebrow:'THE TOWNHOUSE COLLECTION',
      title:'Summer<em>Hill.</em>',description:'Newly refreshed interiors, generous two-level layouts, and all the ingredients for feeling at home — from private decks to in-unit laundry.',
      bedrooms:'02 — 03',feature:'UPDATED',featureLabel:'INTERIORS',link:'/summerhill.html',linkText:'Discover SummerHill'
    }
  };
  let current = 'plaza';
  let switchTimer;
  function updateProperty(key) {
    if(key === current) return;
    current=key;
    const x=properties[key];
    const content=$('#explorer-content');
    const img=$('#explorer-img');
    if(!content || !img) return;
    content.classList.add('switching');
    img.style.opacity='.35';
    $$('#explorer-tab-plaza, #explorer-tab-summer').forEach(b=>{
      const active=b.dataset.explore===key;
      b.classList.toggle('is-active',active);
      b.setAttribute('aria-selected',String(active));
    });
    clearTimeout(switchTimer);
    switchTimer=setTimeout(()=>{
      img.src=x.image; img.alt=x.alt;
      $('#explorer-label').textContent=x.label;
      $('#explorer-no').textContent=x.no;
      $('#explorer-eyebrow').textContent=x.eyebrow;
      $('#explorer-title').innerHTML=x.title;
      $('#explorer-description').textContent=x.description;
      $('#explorer-bedrooms').textContent=x.bedrooms;
      $('#explorer-feature').textContent=x.feature;
      $('#explorer-feature-label').textContent=x.featureLabel;
      $('#explorer-link').href=x.link;
      $('#explorer-link').innerHTML=x.linkText+' <span>↗</span>';
      $('#explorer-count').textContent=x.no;
      content.classList.remove('switching');
      img.onload=()=>img.style.opacity='1';
      if(img.complete) img.style.opacity='1';
    }, reduceMotion ? 0 : 210);
  }
  $$('[data-explore]').forEach(b => {
    b.addEventListener('click',()=>updateProperty(b.dataset.explore));
    b.addEventListener('keydown',e=>{
      if(e.key==='ArrowRight'||e.key==='ArrowLeft') {
        e.preventDefault();const newKey=b.dataset.explore==='plaza'?'summer':'plaza';updateProperty(newKey);$(`[data-explore="${newKey}"]`)?.focus();
      }
    });
  });

  // Bedroom/property configurator: actual types, not misleading real-time vacancy claims.
  const configurations = [
    {p:'plaza',title:'2-bedroom apartment',beds:2,baths:'Ask for floor plan',kind:'APARTMENT'},
    {p:'plaza',title:'2-bedroom townhouse',beds:2,baths:'Ask for floor plan',kind:'TOWNHOUSE'},
    {p:'plaza',title:'3-bedroom apartment',beds:3,baths:'Ask for floor plan',kind:'APARTMENT'},
    {p:'plaza',title:'3-bedroom townhouse',beds:3,baths:'Ask for floor plan',kind:'TOWNHOUSE'},
    {p:'plaza',title:'4-bedroom residence',beds:4,baths:'Contact for layout',kind:'RESIDENCE'},
    {p:'summer',title:'2-bedroom townhouse',beds:2,baths:'Ask for floor plan',kind:'TOWNHOUSE'},
    {p:'summer',title:'3-bedroom townhouse',beds:3,baths:'Ask for floor plan',kind:'TOWNHOUSE'}
  ];
  let fitProperty='all',fitBeds='all';
  const fitResults=$('#fit-results');
  function drawConfigurations(){
    if(!fitResults) return;
    const matches=configurations.filter(c=>(fitProperty==='all'||fitProperty===c.p)&&(fitBeds==='all'||String(c.beds)===fitBeds));
    fitResults.innerHTML=matches.length?matches.map((c,i)=>{
      const property=c.p==='plaza'?'PLAZA EAST':'SUMMERHILL';
      return `<a class="fit-card" style="animation-delay:${Math.min(i,6)*45}ms" href="/contact.html?property=${c.p}&beds=${c.beds}" aria-label="Inquire about ${c.title} at ${property}"><div class="fit-card-top"><span>${property} / ${c.kind}</span><span>↗</span></div><h3>${c.title}</h3><div class="fit-card-bottom"><span>${c.baths}</span><span class="inquire">INQUIRE <span>↗</span></span></div></a>`;
    }).join(''):'<div class="fit-empty">No matching layouts in this collection. Try another filter.</div>';
  }
  drawConfigurations();
  $$('[data-fit-property],[data-fit-beds]').forEach(button=>button.addEventListener('click',()=>{
    const isProp=button.hasAttribute('data-fit-property');
    const attr=isProp?'data-fit-property':'data-fit-beds';
    if(isProp) fitProperty=button.dataset.fitProperty; else fitBeds=button.dataset.fitBeds;
    $$(`[${attr}]`).forEach(b=>{const active=b===button;b.classList.toggle('active',active);b.setAttribute('aria-pressed',String(active));});
    drawConfigurations();
  }));

  // Accessible expanding photo gallery.
  const lightbox=$('#lightbox');
  const pictures=$$('[data-lightbox-image]');
  let pictureIndex=0,lastActive=null;
  function displayPicture(i){
    if(!pictures.length) return;
    pictureIndex=(i+pictures.length)%pictures.length;
    const chosen=pictures[pictureIndex];
    const image=$('img',lightbox);
    if(image){image.src=chosen.dataset.lightboxImage;image.alt=chosen.dataset.lightboxTitle||'Property photo';}
    $('.lightbox-caption',lightbox).textContent=chosen.dataset.lightboxTitle||'IthacaHome';
  }
  function closeLightbox(){
    lightbox?.classList.remove('open');lightbox?.setAttribute('aria-hidden','true');document.body.classList.remove('no-scroll');
    lastActive?.focus();
  }
  pictures.forEach((item,index)=>item.addEventListener('click',()=>{
    lastActive=document.activeElement;displayPicture(index);lightbox?.classList.add('open');lightbox?.setAttribute('aria-hidden','false');document.body.classList.add('no-scroll');$('.lightbox-close',lightbox)?.focus();
  }));
  $('.lightbox-close')?.addEventListener('click',closeLightbox);
  $('.lightbox-prev')?.addEventListener('click',()=>displayPicture(pictureIndex-1));
  $('.lightbox-next')?.addEventListener('click',()=>displayPicture(pictureIndex+1));
  lightbox?.addEventListener('click',e=>{if(e.target===lightbox)closeLightbox();});
  document.addEventListener('keydown',e=>{
    if(!lightbox?.classList.contains('open'))return;
    if(e.key==='Escape')closeLightbox();
    if(e.key==='ArrowLeft')displayPicture(pictureIndex-1);
    if(e.key==='ArrowRight')displayPicture(pictureIndex+1);
  });

  // Leasing requests route through a serverless email endpoint with explicit feedback.
  const form=$('#inquiry-form');
  const search=new URLSearchParams(location.search);
  const propertyChoice=$('#form-property');
  const bedsChoice=$('#form-bedrooms');
  if(propertyChoice){
    const target=search.get('property');
    if(target==='plaza')propertyChoice.value='Plaza East';
    if(target==='summer')propertyChoice.value='SummerHill';
    if(target==='either')propertyChoice.value='Either';
    propertyChoice.addEventListener('change',()=>{
      const four=$('option[value="4"]',bedsChoice);
      if(four){four.disabled=propertyChoice.value==='SummerHill';if(four.disabled&&bedsChoice.value==='4')bedsChoice.value='';}
    });
    propertyChoice.dispatchEvent(new Event('change'));
  }
  if(bedsChoice && ['2','3','4'].includes(search.get('beds')) && !(propertyChoice?.value === 'SummerHill' && search.get('beds') === '4')) bedsChoice.value=search.get('beds');
  form?.addEventListener('submit',async ev=>{
    ev.preventDefault();
    if(!form.reportValidity())return;
    const submit=$('.form-submit',form);const feedback=$('#form-feedback');
    const values=Object.fromEntries(new FormData(form).entries());
    const previous=submit.innerHTML;
    submit.disabled=true;submit.innerHTML='SENDING... <span class="arrow-circle">↗</span>';
    feedback.hidden=true;feedback.classList.remove('error');
    try{
      const response=await fetch(form.action,{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(values)});
      let result={};try{result=await response.json()}catch{}
      if(!response.ok)throw new Error(result.error||'We could not send your message. Please email our leasing team directly.');
      form.reset();
      feedback.textContent='Thank you — your inquiry has been sent to IthacaHome. Our leasing team will follow up by email.';
      feedback.hidden=false;
      feedback.scrollIntoView({behavior:reduceMotion?'auto':'smooth',block:'center'});
    }catch(error){
      feedback.classList.add('error');
      feedback.textContent=error.message||'Unable to submit. Please email rentals@ithacahome.com directly.';
      feedback.hidden=false;
    }finally{submit.disabled=false;submit.innerHTML=previous;}
  });
})();