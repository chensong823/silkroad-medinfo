// shared/js/view-transitions.js — silk road medinfo v3
// Use View Transitions API for smooth page navigation where supported.
// Falls back to a soft fade for browsers without API support.

(function () {
  'use strict';

  var hasVT = typeof document.startViewTransition === 'function';

  if (!hasVT) {
    // Soft fade fallback
    var style = document.createElement('style');
    style.textContent = 'body { opacity: 0; transition: opacity 0.3s ease; } body.is-loaded { opacity: 1; }';
    document.head.appendChild(style);
    requestAnimationFrame(function () {
      document.body.classList.add('is-loaded');
    });
    return;
  }

  // On initial load, animate in
  document.addEventListener('DOMContentLoaded', function () {
    document.startViewTransition(function () {
      document.body.classList.add('is-loaded');
    });
  });

  // Intercept same-origin link clicks for smooth transition
  document.addEventListener('click', function (e) {
    var a = e.target.closest('a[href]');
    if (!a) return;
    var href = a.getAttribute('href');
    if (!href || href.startsWith('#') || href.startsWith('http') || href.startsWith('mailto')) return;
    if (a.target === '_blank' || e.metaKey || e.ctrlKey || e.shiftKey) return;

    e.preventDefault();
    document.startViewTransition(function () {
      window.location.href = href;
    });
  });
})();