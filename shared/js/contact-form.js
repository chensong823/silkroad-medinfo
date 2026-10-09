// shared/js/contact-form.js — v2 stub.
// Canonical implementation lives in shared/components/contact-form.js
// This file exists for backwards-compat with already-shipped pages.

(function () {
  'use strict';
  // Bootstrap deferred — wait for DOM ready
  function tryBootstrap() {
    if (window.ContactForm && window.ContactForm.bind) {
      document.querySelectorAll('[data-contact-form]').forEach(function (f) {
        window.ContactForm.bind(f);
      });
      return;
    }
    // Fallback: simple validation if component script failed
    setTimeout(tryBootstrap, 100);
  }
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', tryBootstrap);
  } else {
    tryBootstrap();
  }
})();