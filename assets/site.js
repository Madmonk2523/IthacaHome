(()=>{'use strict';document.documentElement.classList.add('has-js');
const $=(s,el=document)=>el.querySelector(s), $$=(s,el=document)=>[...el.querySelectorAll(s)];
const reduce=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
const header=$('#header'),progress=$('.reading-progress');
const scrollTick=()=>{const y=window.scrollY;header?.classList.toggle('is-condensed',y>48);if(progress){const total=document.documentElement.scrollHeight-window.innerHeight;progress.style.transform=`scaleX(${total?Math.min(1,y/total):0})`}};
window.addEventListener('scroll',scrollTick,{passive:true});scrollTick();
const toggle=$('#nav-toggle'),mobile=$('#nav-mobile');
const setMenu=(open)=>{toggle?.setAttribute('aria-expanded',String(open));toggle?.setAttribute('aria-label',open?'Close navigation':'Open navigation');mobile?.classList.toggle('is-open',open);mobile?.toggleAttribute('inert',!open);document.body.classList.toggle('locked',open);if(!open)toggle?.focus()};
toggle?.addEventListener('click',()=>setMenu(toggle.getAttribute('aria-expanded')!=='true'));
$$('#nav-mobile a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
document.addEventListener('click',e=>{if(toggle?.getAttribute('aria-expanded')==='true'&&!header?.contains(e.target))setMenu(false)});
window.addEventListener('resize',()=>{if(window.innerWidth>900&&toggle?.getAttribute('aria-expanded')==='true')setMenu(false)},{passive:true});
document.addEventListener('keydown',e=>{if(e.key==='Escape'&&toggle?.getAttribute('aria-expanded')==='true')setMenu(false)});
if('IntersectionObserver' in window&&!reduce){const ob=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add('visible');ob.unobserve(entry.target)}}),{threshold:.09,rootMargin:'0px 0px -25px 0px'});$$('.reveal').forEach(el=>ob.observe(el))}else{$$('.reveal').forEach(el=>el.classList.add('visible'))}
// Just a small amount of parallax on the large hero image. No motion on touch devices.
const heroImg=$('.hero-picture .hero-photo');if(heroImg&&!reduce&&window.matchMedia('(hover:hover) and (min-width: 900px)').matches){let ticking=false;window.addEventListener('scroll',()=>{if(ticking)return;ticking=true;requestAnimationFrame(()=>{const rect=heroImg.parentElement.getBoundingClientRect();const offset=Math.max(-30,Math.min(30,-rect.top*.04));heroImg.style.transform=`translateY(${offset}px) scale(1.06)`;ticking=false})},{passive:true})}
const chips=$$('.filter-chip');const floors=$$('.floor-row');
function filterFloors(val){chips.forEach(b=>{let active=b.dataset.filter===val;b.classList.toggle('is-active',active);b.setAttribute('aria-pressed',String(active))});floors.forEach(r=>r.hidden=val!=='all'&&r.dataset.beds!==val)}
chips.forEach(chip=>chip.addEventListener('click',()=>filterFloors(chip.dataset.filter)));
const gallery=$('[data-gallery]'),more=$('.gallery-more'),dialog=$('#lightbox');let items=[],pos=0,lastFocus=null;
function allVisible(){return $$('.gallery-item:not([hidden])',gallery)}
more?.addEventListener('click',()=>{const expanded=more.getAttribute('aria-expanded')==='true';$$('.gallery-item[data-hidden]',gallery).forEach(e=>e.hidden=expanded);more.setAttribute('aria-expanded',String(!expanded));more.textContent=expanded?'View all photographs':'Show fewer photographs'});
if(gallery&&more){$$('.gallery-item[data-hidden]',gallery).forEach(el=>el.hidden=true)}
function renderImg(){let item=items[pos];if(!item)return;let im=$('img',item);$('#lightbox-img').src=im.currentSrc||im.src;$('#lightbox-img').alt=im.alt;$('#lightbox-caption').textContent=item.dataset.caption||im.alt;$('#lightbox-count').textContent=`${String(pos+1).padStart(2,'0')} / ${String(items.length).padStart(2,'0')}`}
function openPhoto(item){items=$$('.gallery-item',gallery).filter(el=>!el.querySelector('img')?.classList.contains('image-error'));pos=items.indexOf(item);if(pos<0)return;lastFocus=document.activeElement;renderImg();if(dialog?.showModal){dialog.showModal();document.body.classList.add('locked')}else{dialog?.setAttribute('open','');document.body.classList.add('locked')}}
function closePhoto(){dialog?.close?.();dialog?.removeAttribute('open');document.body.classList.remove('locked');lastFocus?.focus?.()}
gallery?.addEventListener('click',e=>{const item=e.target.closest('.gallery-item');if(item)openPhoto(item)});
$('.lightbox-close')?.addEventListener('click',closePhoto);$('.lightbox-prev')?.addEventListener('click',()=>{pos=(pos-1+items.length)%items.length;renderImg()});$('.lightbox-next')?.addEventListener('click',()=>{pos=(pos+1)%items.length;renderImg()});
dialog?.addEventListener('click',e=>{if(e.target===dialog)closePhoto()});dialog?.addEventListener('close',()=>{document.body.classList.remove('locked');lastFocus?.focus?.()});
document.addEventListener('keydown',e=>{if(!dialog?.open)return;if(e.key==='ArrowLeft'){pos=(pos-1+items.length)%items.length;renderImg()}if(e.key==='ArrowRight'){pos=(pos+1)%items.length;renderImg()}});
// Hide missing galleries rather than substituting a repeated photograph.
$$('.gallery-item img').forEach(im=>im.addEventListener('error',()=>{im.classList.add('image-error');im.parentElement.hidden=true}));
const form=$('#inquiry-form');
if(form){const property=form.elements.property,bedrooms=form.elements.bedrooms,feedback=$('#form-feedback'),submit=$('.form-submit');const params=new URLSearchParams(location.search);const prop=params.get('property'),bed=params.get('bedrooms');if(['Plaza East','SummerHill','Either'].includes(prop))property.value=prop;if(['2','3','4'].includes(bed))bedrooms.value=bed;
const syncBedrooms=()=>{const four=bedrooms.querySelector('option[value="4"]');four.disabled=property.value==='SummerHill';if(four.disabled&&bedrooms.value==='4')bedrooms.value=''};syncBedrooms();property.addEventListener('change',syncBedrooms);
form.addEventListener('submit',async e=>{e.preventDefault();feedback.classList.remove('success');feedback.textContent='';if(!form.checkValidity()){form.reportValidity();return}const data=Object.fromEntries(new FormData(form));submit.disabled=true;submit.textContent='Sending…';try{const response=await fetch('/api/inquiry',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});const result=await response.json().catch(()=>({}));if(!response.ok)throw Error(result.error||'We could not send your message. Please email rentals@ithacahome.com instead.');feedback.classList.add('success');feedback.textContent='Your message has been sent. The leasing team will follow up by email.';form.reset();syncBedrooms()}catch(err){feedback.textContent=err.message||'Unable to send. Please email rentals@ithacahome.com instead.'}finally{submit.disabled=false;submit.textContent='Send leasing inquiry'}})}
$('#year')&&($('#year').textContent=new Date().getFullYear());
})();
