// shared/js/cursor.js — silk road medinfo v3
// Custom cursor with magnetic hover states on interactive elements.

(function () {
  'use strict';

  // Skip on touch
  if (matchMedia('(hover: none)').matches) return;
  if (matchMedia('(max-width: 768px)').matches) return;

  // Create cursor nodes
  var dot = document.createElement('div');
  dot.className = 'cursor-dot';
  var ring = document.createElement('div');
  ring.className = 'cursor-ring';
  document.body.appendChild(dot);
  document.body.appendChild(ring);

  var mx = -100, my = -100;       // current target mouse position
  var rx = -100, ry = -100;       // actual rendered ring position (smoothed)
  var dx = -100, dy = -100;       // actual rendered dot position

  document.addEventListener('mousemove', function (e) {
    mx = e.clientX;
    my = e.clientY;
  }, { passive: true });

  // Hover detection
  var HOVER_SELECTOR = 'a, button, [data-magnetic], input, select, textarea, [role="button"], label[for]';

  function updateHover(e) {
    var el = e.target.closest(HOVER_SELECTOR);
    if (!el) {
      document.body.removeAttribute('data-cursor');
      return;
    }
    if (el.matches('input, textarea, select')) {
      document.body.setAttribute('data-cursor', 'text');
    } else if (el.matches('a[href], button')) {
      document.body.setAttribute('data-cursor', 'link');
    } else if (el.matches('[data-magnetic]')) {
      document.body.setAttribute('data-cursor', 'hover');
    } else {
      document.body.setAttribute('data-cursor', 'hover');
    }
  }

  document.addEventListener('mouseover', updateHover, { passive: true });
  document.addEventListener('mouseleave', function () {
    document.body.removeAttribute('data-cursor');
  });

  document.addEventListener('mouseleave', function () {
    ring.classList.remove('is-active');
  });
  document.addEventListener('mouseenter', function () {
    ring.classList.add('is-active');
  });

  function loop() {
    // Dot snaps immediately
    dx = mx;
    dy = my;
    dot.style.transform = 'translate(' + (dx - 3) + 'px,' + (dy - 3) + 'px)';
    // Ring lags slightly for parallax feel
    rx += (mx - rx) * 0.18;
    ry += (my - ry) * 0.18;
    ring.style.transform = 'translate(' + (rx - 18) + 'px,' + (ry - 18) + 'px)';
    requestAnimationFrame(loop);
  }
  requestAnimationFrame(loop);
})();