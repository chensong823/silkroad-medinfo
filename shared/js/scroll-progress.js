// shared/js/scroll-progress.js + section-indicator.js
// Top progress bar + right-rail section dots.

(function () {
  'use strict';

  // ---- Top progress bar ----
  var bar = document.createElement('div');
  bar.className = 'scroll-progress';
  bar.innerHTML = '<div class="scroll-progress-bar"></div>';
  document.body.appendChild(bar);
  var barFill = bar.querySelector('.scroll-progress-bar');

  function updateProgress() {
    var h = document.documentElement.scrollHeight - window.innerHeight;
    var pct = h > 0 ? (window.scrollY / h) * 100 : 0;
    barFill.style.width = Math.min(100, Math.max(0, pct)) + '%';
  }
  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();

  // ---- Section indicator (right rail) ----
  var sections = document.querySelectorAll('section[id]');
  if (sections.length < 2) return;

  var indicator = document.createElement('nav');
  indicator.className = 'section-indicator';
  indicator.setAttribute('aria-label', 'Section navigation');
  sections.forEach(function (sec) {
    var btn = document.createElement('button');
    btn.type = 'button';
    btn.setAttribute('aria-label', sec.id || 'section');
    btn.dataset.target = '#' + sec.id;
    btn.addEventListener('click', function () {
      sec.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
    indicator.appendChild(btn);
  });
  document.body.appendChild(indicator);

  function updateActive() {
    var buttons = indicator.querySelectorAll('button');
    var i = 0;
    sections.forEach(function (sec, idx) {
      var rect = sec.getBoundingClientRect();
      var inView = rect.top < window.innerHeight * 0.5 && rect.bottom > window.innerHeight * 0.2;
      if (inView) i = idx;
    });
    buttons.forEach(function (b, bIdx) {
      b.classList.toggle('is-active', bIdx === i);
    });

    // Show indicator after scrolling past hero
    var scrolled = window.scrollY > window.innerHeight * 0.6;
    indicator.classList.toggle('is-visible', scrolled);
  }
  window.addEventListener('scroll', updateActive, { passive: true });
  updateActive();

  // ---- Header scrolled state ----
  var header = document.querySelector('.site-header');
  if (header) {
    function updateHeader() {
      header.classList.toggle('is-scrolled', window.scrollY > 16);
    }
    window.addEventListener('scroll', updateHeader, { passive: true });
    updateHeader();
  }
})();