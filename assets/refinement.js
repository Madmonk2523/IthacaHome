/* Ithaca Home: small, intentional interaction layer; no animation dependency. */
(()=>{
 'use strict';
 const reduced=matchMedia('(prefers-reduced-motion: reduce)').matches;
 const coarse=matchMedia('(pointer:coarse)').matches;
 const $=(s,c=document)=>c.querySelector(s);
 const $$=(s,c=document)=>[...c.querySelectorAll(s)];
 // Highlight which section the visitor is reading; keep navigation usable.
 const page=document.body.dataset.page;
 let active=page==='neighborhood'?'neighborhood':page==='contact'?'contact':['plaza','summer','plaza-east','summerhill'].includes(page)?'properties':null;
 const navs=$$('[data-nav]');
 const mark=key=>navs.forEach(n=>{if(n.dataset.nav===key){n.setAttribute('aria-current','page');n.classList.add('active')}else{n.removeAttribute('aria-current');n.classList.remove('active')}});
 if(active)mark(active);
 if(page==='home' && 'IntersectionObserver' in window){
   const homeLinks=new IntersectionObserver(entries=>{
     entries.forEach(e=>{
       if(!e.isIntersecting)return;
       if(e.target.id==='properties')mark('properties');
       else if(e.target.id==='faq')mark('faq');
     });
   },{rootMargin:'-20% 0px -55% 0px',threshold:0});
   ['properties','faq'].forEach(id=>{const el=document.getElementById(id);if(el)homeLinks.observe(el)});
 }
 if(reduced)return;
 // Parallax with requestAnimationFrame: tiny displacement, fewer layout reads.
 const images=$$('.intro-editorial-photos img,.signature-visual>img,.interlude img,.property-photo-interlude img');
 let tick=false;
 const update=()=>{
   const h=innerHeight;
   for(const img of images){
     const box=img.parentElement.getBoundingClientRect();
     if(box.bottom<0||box.top>h)continue;
     const relative=(box.top+box.height/2-h/2)/h;
     img.style.setProperty('--parallax',`${Math.round(-relative*23)}px`);
   }
   tick=false;
 };
 if(images.length){addEventListener('scroll',()=>{if(!tick){tick=true;requestAnimationFrame(update)}},{passive:true});addEventListener('resize',update);requestAnimationFrame(update)}
 // Restrained directional movement on interactive property actions.
 if(!coarse){$$('.hero-actions a,.nav-contact,.hero-feature-card').forEach(node=>{
   node.addEventListener('pointermove',ev=>{
     const b=node.getBoundingClientRect();
     const x=(ev.clientX-b.left)/b.width-.5;
     const y=(ev.clientY-b.top)/b.height-.5;
     node.style.setProperty('--hover-x',`${(x*5).toFixed(1)}px`);
     node.style.setProperty('--hover-y',`${(y*4).toFixed(1)}px`);
   },{passive:true});
   node.addEventListener('pointerleave',()=>{node.style.removeProperty('--hover-x');node.style.removeProperty('--hover-y')},{passive:true});
 })}
 // Hover animations are progressive enhancement; the entire site works without JS.
})();
