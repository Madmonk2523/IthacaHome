/* Additional lightweight editorial interactions. Base functionality in script.js. */
(() => {
  'use strict';
  const track = document.querySelector('#resident-slider');
  if (track) {
    const cards = Array.from(track.querySelectorAll('.resident-quote'));
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    function move(dir) {
      const width = cards[0]?.getBoundingClientRect().width || 420;
      track.scrollBy({left: dir * (width + 23), behavior: reduced ? 'auto' : 'smooth'});
    }
    document.querySelector('#resident-prev')?.addEventListener('click', () => move(-1));
    document.querySelector('#resident-next')?.addEventListener('click', () => move(1));
    track.addEventListener('keydown', ev => {
      if (ev.key === 'ArrowRight') { ev.preventDefault(); move(1); }
      if (ev.key === 'ArrowLeft') { ev.preventDefault(); move(-1); }
    });
  }
  const accordion = [...document.querySelectorAll('.faq-row')];
  accordion.forEach(item => item.addEventListener('toggle', () => {
    if (!item.open) return;
    accordion.forEach(other => { if (other !== item) other.open = false; });
  }));
  // Update explorer's secondary editorial image to match the selected collection.
  const mini = document.querySelector('#explorer-mini');
  const tabs = [...document.querySelectorAll('[data-explore]')];
  function syncMini(prop) {
    if (!mini) return;
    mini.src = prop === 'summer' ? '/assets/summerhill-kitchen.webp' : '/assets/plaza-living.webp';
    mini.alt = prop === 'summer' ? 'SummerHill renovated kitchen' : 'Plaza East sunlit living room';
  }
  tabs.forEach(tab => tab.addEventListener('click', () => syncMini(tab.dataset.explore)));
  // Avoid relying on a browser's aggressive scroll animation preference.
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    document.querySelectorAll('.site-reveal-curtain').forEach(x => x.remove());
  }
})();