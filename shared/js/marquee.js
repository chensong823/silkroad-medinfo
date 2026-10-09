// shared/js/marquee.js — silk road medinfo v3
// Duplicate marquee content so the loop is seamless.
// Pure JS, no deps. Works with any .marquee element containing .marquee-track.

(function () {
  'use strict';

  function init() {
    document.querySelectorAll('.marquee, .ribbon').forEach(function (m) {
      var track = m.querySelector('.marquee-track, .ribbon-track');
      if (!track) return;
      // Duplicate content for seamless loop
      var clone = track.cloneNode(true);
      clone.setAttribute('aria-hidden', 'true');
      // Mark duplicate items
      Array.from(clone.children).forEach(function (c) {
        c.setAttribute('aria-hidden', 'true');
        c.setAttribute('tabindex', '-1');
      });
      track.appendChild(clone);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();