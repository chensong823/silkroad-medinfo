// shared/js/main.js — Silk Road Medinfo v2
// Bootstrap: load all shared modules in correct order.

(function () {
  'use strict';

  // Modules are loaded synchronously in index.html <script> tags.
  // This file is for any additional global setup after DOM is ready.

  function init() {
    // Update copyright year
    var yearEl = document.querySelector('[data-current-year]');
    if (yearEl) {
      yearEl.textContent = String(new Date().getFullYear());
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();