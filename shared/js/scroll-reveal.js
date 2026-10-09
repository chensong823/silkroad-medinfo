// shared/js/scroll-reveal.js — Silk Road Medinfo v2
// IntersectionObserver-based reveal. Capped total stagger.
// Respects prefers-reduced-motion.

(function (global) {
  'use strict';

  var reducedMotion = global.matchMedia && global.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init() {
    if (reducedMotion) {
      // Immediately mark everything as revealed
      document.querySelectorAll('[data-reveal], [data-reveal-stagger]').forEach(function (el) {
        el.classList.add('is-revealed');
      });
      return;
    }

    if (!('IntersectionObserver' in global)) {
      // No IO support: just show everything
      document.querySelectorAll('[data-reveal], [data-reveal-stagger]').forEach(function (el) {
        el.classList.add('is-revealed');
      });
      return;
    }

    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          observer.unobserve(entry.target);
        }
      });
    }, {
      rootMargin: '0px 0px -10% 0px',
      threshold: 0.05
    });

    document.querySelectorAll('[data-reveal], [data-reveal-stagger]').forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})(window);