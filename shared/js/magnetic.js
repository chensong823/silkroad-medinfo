// shared/js/magnetic.js — silk road medinfo v3
// Make [data-magnetic] elements lean toward the cursor (max 12px shift).

(function () {
  'use strict';

  if (matchMedia('(hover: none)').matches) return;

  var els = document.querySelectorAll('[data-magnetic]');
  els.forEach(function (el) {
    var strength = parseFloat(el.getAttribute('data-magnetic')) || 0.3;
    var bounds = 80; // px around element to start attracting

    el.addEventListener('mousemove', function (e) {
      var rect = el.getBoundingClientRect();
      var cx = rect.left + rect.width / 2;
      var cy = rect.top + rect.height / 2;
      var dx = e.clientX - cx;
      var dy = e.clientY - cy;
      var dist = Math.sqrt(dx * dx + dy * dy);
      if (dist < bounds) {
        var factor = (1 - dist / bounds) * strength;
        el.style.transform = 'translate(' + (dx * factor).toFixed(1) + 'px,' + (dy * factor).toFixed(1) + 'px)';
      }
    });

    el.addEventListener('mouseleave', function () {
      el.style.transform = '';
    });
  });
})();