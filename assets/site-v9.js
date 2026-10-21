(()=>{'use strict';
const $=(s,scope=document)=>scope.querySelector(s);const $$=(s,scope=document)=>[...scope.querySelectorAll(s)];
const button=$('#menu-button'),menu=$('#mobile-menu');
const setMenu=open=>{if(!button||!menu)return;button.setAttribute('aria-expanded',String(open));button.setAttribute('aria-label',open?'Close menu':'Open menu');menu.setAttribute('aria-hidden',String(!open));menu.classList.toggle('open',open);document.body.classList.toggle('menu-open',open)};
button?.addEventListener('click',()=>setMenu(button.getAttribute('aria-expanded')!=='true'));
$$('#mobile-menu a').forEach(a=>a.addEventListener('click',()=>setMenu(false)));
window.addEventListener('resize',()=>{if(window.innerWidth>700)setMenu(false)},{passive:true});
const observed=$$('.reveal');if('IntersectionObserver'in window){const io=new IntersectionObserver(entries=>{for(const entry of entries)if(entry.isIntersecting){entry.target.classList.add('in-view');io.unobserve(entry.target)}},{rootMargin:'0px 0px 10% 0px',threshold:.08});observed.forEach(x=>io.observe(x))}else observed.forEach(x=>x.classList.add('in-view'));
$('#year')?.replaceChildren(document.createTextNode(String(new Date().getFullYear())));
// Property galleries: first six photos are visible; the rest are progressively disclosed.
const more=$('#show-all-gallery');more?.addEventListener('click',()=>{const expanded=more.getAttribute('aria-expanded')==='true';$$('.gallery-hidden').forEach(el=>{el.style.display=expanded?'none':'block'});more.setAttribute('aria-expanded',String(!expanded));more.textContent=expanded?'View all photographs':'Show fewer photographs'});
let gallery=$$('[data-gallery-item]');let active=0;let beforeOpen=null;const lightbox=$('#lightbox'),lightboxImage=$('#lightbox-image'),caption=$('#lightbox-caption');
function renderPhoto(){let item=gallery[active],source=$('img',item);if(!source||!lightboxImage)return;lightboxImage.src=source.currentSrc||source.src;lightboxImage.alt=source.alt;caption.textContent=`${document.title.split('|')[0].trim()} / ${active+1} of ${gallery.length}`}
function openPhoto(i){if(!lightbox)return;beforeOpen=document.activeElement;active=i;renderPhoto();lightbox.setAttribute('aria-hidden','false');document.body.classList.add('lightbox-open');$('.lightbox-close')?.focus()}
function closePhoto(){if(!lightbox)return;lightbox.setAttribute('aria-hidden','true');document.body.classList.remove('lightbox-open');if(lightboxImage)lightboxImage.removeAttribute('src');beforeOpen?.focus?.()}
gallery.forEach((x,i)=>x.addEventListener('click',()=>openPhoto(i)));
$('.lightbox-close')?.addEventListener('click',closePhoto);
$('.lightbox-prev')?.addEventListener('click',()=>{if(!gallery.length)return;active=(active-1+gallery.length)%gallery.length;renderPhoto()});
$('.lightbox-next')?.addEventListener('click',()=>{if(!gallery.length)return;active=(active+1)%gallery.length;renderPhoto()});
lightbox?.addEventListener('click',e=>{if(e.target===lightbox)closePhoto()});
document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(lightbox?.getAttribute('aria-hidden')==='false')closePhoto();else setMenu(false)}if(lightbox?.getAttribute('aria-hidden')==='false'){if(e.key==='ArrowRight'){active=(active+1)%gallery.length;renderPhoto()}if(e.key==='ArrowLeft'){active=(active-1+gallery.length)%gallery.length;renderPhoto()}}});
// Contact form preselection & validation. Do not claim success until API confirms delivery.
const form=$('#inquiry-form');if(form){const params=new URLSearchParams(location.search);const prop=$('#property'),beds=$('#bedrooms'),message=$('#form-status');const requested=params.get('property');if(['Plaza East','SummerHill','Either'].includes(requested))prop.value=requested;const syncBeds=()=>{const four=$('option[value="4"]',beds);if(four){four.disabled=prop.value==='SummerHill';if(four.disabled&&beds.value==='4')beds.value=''}};syncBeds();prop.addEventListener('change',syncBeds);const initialBed=params.get('bedrooms');if(['2','3','4'].includes(initialBed)){beds.value=initialBed;syncBeds()}
form.addEventListener('submit',async e=>{e.preventDefault();message.textContent='';message.classList.remove('success');const data=Object.fromEntries(new FormData(form));data.name=(data.name||'').trim();data.email=(data.email||'').trim();if(data.name.length<2){message.textContent='Please enter your name.';$('#name').focus();return}if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(data.email)){message.textContent='Please enter a valid email address.';$('#email').focus();return}if(data.property==='SummerHill'&&data.bedrooms==='4'){message.textContent='SummerHill offers two- and three-bedroom layouts.';return}const submit=$('.form-submit',form);submit.disabled=true;submit.textContent='Sending inquiry…';try{const response=await fetch('/api/inquiry',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(data)});const result=await response.json().catch(()=>({}));if(!response.ok||!result.ok)throw Error(result.error||'Unable to send your inquiry. Please email rentals@ithacahome.com.');message.textContent='Thank you. Your inquiry was sent to the leasing team.';message.classList.add('success');form.reset();syncBeds()}catch(err){message.textContent=err.message||'Unable to send your inquiry. Please email rentals@ithacahome.com.'}finally{submit.disabled=false;submit.textContent='Send inquiry'}})
}
})();


