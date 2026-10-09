// shared/js/reveal.js — silk road medinfo v3
// Enhanced reveal: stagger, scaled, blurred, clip-path, intersection observer.
// Also handles [data-counter] number animations.

(function () {
  'use strict';

  var reduced = matchMedia('(prefers-reduced-motion: reduce)').matches;

  function revealAll() {
    document.querySelectorAll(
      '[data-reveal], [data-reveal-stagger], [data-reveal="rise"], [data-reveal="rise-late"], [data-reveal="scale"], [data-reveal="blur"], [data-cinema]'
    ).forEach(function (el) { el.classList.add('is-revealed'); });
  }

  function countUp(el) {
    var target = parseFloat(el.getAttribute('data-counter'));
    var duration = parseInt(el.getAttribute('data-counter-duration'), 10) || 1200;
    var suffix = el.getAttribute('data-counter-suffix') || '';
    var start = performance.now();
    var startValue = 0;
    function step(now) {
      var elapsed = now - start;
      var t = Math.min(1, elapsed / duration);
      // ease-out cubic
      var eased = 1 - Math.pow(1 - t, 3);
      var val = (startValue + (target - startValue) * eased);
      var display = Number.isInteger(target) ? Math.round(val) : val.toFixed(1);
      el.textContent = display + suffix;
      if (t < 1) requestAnimationFrame(step);
      else el.textContent = target + suffix;
    }
    requestAnimationFrame(step);
  }

  function init() {
    if (reduced || !('IntersectionObserver' in window)) {
      revealAll();
      return;
    }

    var counterObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          countUp(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.4 });

    document.querySelectorAll('[data-counter]').forEach(function (el) {
      var target = parseFloat(el.getAttribute('data-counter'));
      var suffix = el.getAttribute('data-counter-suffix') || '';
      el.textContent = (Number.isInteger(target) ? target : target.toFixed(1)) + suffix;
      counterObserver.observe(el);
    });

    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-revealed');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.05 });

    document.querySelectorAll(
      '[data-reveal], [data-reveal-stagger], [data-reveal="rise"], [data-reveal="rise-late"], [data-reveal="scale"], [data-reveal="blur"], [data-cinema]'
    ).forEach(function (el) { revealObserver.observe(el); });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();