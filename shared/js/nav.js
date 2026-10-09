// shared/js/nav.js — Silk Road Medinfo v2
// Sticky header behavior, language switcher sync, mobile menu toggle.

(function () {
  'use strict';

  function init() {
    var header = document.querySelector('.site-header');
    if (!header) return;

    // Mark current nav link based on URL
    var path = window.location.pathname.replace(/\/$/, '').replace(/\/index\.html$/, '');
    var navLinks = document.querySelectorAll('.nav-link');
    navLinks.forEach(function (link) {
      var href = link.getAttribute('href') || '';
      if (href && path.endsWith(href.replace(/^\.\//, '').replace(/\/$/, ''))) {
        link.setAttribute('aria-current', 'page');
      }
    });

    // Mobile menu toggle
    var menuToggle = document.querySelector('.menu-toggle');
    var mobileMenu = document.querySelector('.mobile-menu');
    if (menuToggle && mobileMenu) {
      menuToggle.addEventListener('click', function () {
        var isOpen = mobileMenu.classList.toggle('is-open');
        menuToggle.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
        document.body.style.overflow = isOpen ? 'hidden' : '';
      });

      // Close on link click
      mobileMenu.querySelectorAll('a').forEach(function (link) {
        link.addEventListener('click', function () {
          mobileMenu.classList.remove('is-open');
          menuToggle.setAttribute('aria-expanded', 'false');
          document.body.style.overflow = '';
        });
      });
    }

    // Auto-close lightbox & mobile menu on locale change
    document.addEventListener('i18n:locale-changed', function () {
      if (mobileMenu && mobileMenu.classList.contains('is-open')) {
        mobileMenu.classList.remove('is-open');
        if (menuToggle) menuToggle.setAttribute('aria-expanded', 'false');
        document.body.style.overflow = '';
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();