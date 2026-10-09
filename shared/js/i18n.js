// shared/js/i18n.js — Silk Road Medinfo i18n runtime
// Supports:
//   - Dot-notation key lookup across per-namespace JSON
//   - ICU-style placeholders: {name}, {count}
//   - Russian CLDR plural rules (one/few/many/other)
//   - HTML attribute translation: data-i18n, data-i18n-placeholder, data-i18n-aria-label
//   - Plural-aware elements: data-i18n-plural + data-count
//   - Language switcher with localStorage persistence
//   - HTML <html lang> attribute sync

(function (global) {
  'use strict';

  var SUPPORTED = ['zh-CN', 'en', 'ru'];
  var DEFAULT_LOCALE = 'zh-CN';
  var STORAGE_KEY = 'silkroad-locale';

  // CLDR plural rules (subset)
  // Russian: one=1,21,31..; few=2-4,22-24..; many=0,5-20,25-30..; other=fractional
  function ruPlural(n) {
    var v = Math.abs(parseFloat(n));
    var i = Math.floor(v);
    var mod10 = i % 10;
    var mod100 = i % 100;
    if (mod10 === 1 && mod100 !== 11) return 'one';
    if (mod10 >= 2 && mod10 <= 4 && (mod100 < 12 || mod100 > 14)) return 'few';
    if (mod10 === 0 || (mod10 >= 5 && mod10 <= 9) || (mod100 >= 11 && mod100 <= 14)) return 'many';
    return 'other';
  }

  function enPlural(n) {
    return parseFloat(n) === 1 ? 'one' : 'other';
  }

  function zhPlural(n) {
    return 'other'; // Chinese has no grammatical plural form
  }

  function pickPlural(locale, n) {
    if (locale === 'ru') return ruPlural(n);
    if (locale === 'en') return enPlural(n);
    return zhPlural(n);
  }

  // Cache for loaded namespaces per locale
  var cache = {};

  // Async load a locale namespace JSON
  function loadNamespace(locale, namespace) {
    if (!SUPPORTED.indexOf(locale) !== -1) {
      // wait — indexOf returns -1 for missing, use the proper check
    }
    var key = locale + '::' + namespace;
    if (cache[key]) return Promise.resolve(cache[key]);

    var path = resolveLocalePath(locale, namespace);
    return fetch(path, { credentials: 'same-origin' })
      .then(function (r) {
        if (!r.ok) throw new Error('i18n load failed: ' + path + ' (' + r.status + ')');
        return r.json();
      })
      .then(function (data) {
        cache[key] = data;
        return data;
      });
  }

  function resolveLocalePath(locale, namespace) {
    // Files live at /locales/{locale}/{namespace}.json relative to current page
    // The shared/ folder is at /shared/ from the project root
    // For pages under /en/ or /ru/, locale path goes up one level
    var inSubdir = /\/[a-z]{2}(\-[A-Z]{2})?\//.test(window.location.pathname.replace(/index\.html$/, ''));
    var prefix = inSubdir ? '../' : '';
    return prefix + 'locales/' + locale + '/' + namespace + '.json';
  }

  function getKey(data, dottedKey) {
    var parts = dottedKey.split('.');
    var cur = data;
    for (var i = 0; i < parts.length; i++) {
      if (cur == null) return undefined;
      cur = cur[parts[i]];
    }
    return cur;
  }

  function applyPlaceholders(str, params) {
    if (typeof str !== 'string') return str;
    if (!params) return str;
    return str.replace(/\{(\w+)\}/g, function (_m, name) {
      return params[name] != null ? String(params[name]) : '{' + name + '}';
    });
  }

  function applyPlural(strOrMap, count, locale) {
    if (typeof strOrMap === 'string') return strOrMap;
    if (!strOrMap || typeof strOrMap !== 'object') return String(strOrMap || '');
    var cat = pickPlural(locale, count);
    var chosen = strOrMap['_' + cat];
    if (chosen == null) chosen = strOrMap._other || strOrMap._one || strOrMap._few || strOrMap._many || '';
    return applyPlaceholders(chosen, { count: count });
  }

  // i18n core object
  var bundle = {};
  var ready = null;

  function loadAll(locale) {
    var namespaces = ['common', 'cta', 'home', 'projects', 'science', 'services', 'central-asia', 'contact'];
    return Promise.all(namespaces.map(function (ns) {
      return loadNamespace(locale, ns);
    })).then(function (results) {
      bundle = {};
      for (var i = 0; i < namespaces.length; i++) {
        bundle[namespaces[i]] = results[i];
      }
      return bundle;
    });
  }

  function t(key, params) {
    var parts = key.split('.');
    var namespace = parts[0];
    var subKey = parts.slice(1).join('.');
    var data = bundle[namespace];
    if (!data) {
      console.warn('[i18n] namespace not loaded:', namespace);
      return key;
    }
    var value = getKey(data, subKey);
    if (typeof value === 'object' && value && !Array.isArray(value)) {
      // plural map — needs count
      var count = (params && params.count != null) ? params.count : 1;
      var locale = currentLocale();
      return applyPlural(value, count, locale);
    }
    if (Array.isArray(value)) {
      return value;
    }
    return applyPlaceholders(value, params || {});
  }

  function currentLocale() {
    var stored = localStorage.getItem(STORAGE_KEY);
    if (stored && SUPPORTED.indexOf(stored) !== -1) return stored;
    var html = document.documentElement.getAttribute('lang');
    if (html && SUPPORTED.indexOf(html) !== -1) return html;
    return DEFAULT_LOCALE;
  }

  function setLocale(locale, opts) {
    opts = opts || {};
    if (SUPPORTED.indexOf(locale) === -1) {
      console.warn('[i18n] unsupported locale:', locale);
      return Promise.resolve();
    }
    return loadAll(locale).then(function () {
      localStorage.setItem(STORAGE_KEY, locale);
      document.documentElement.setAttribute('lang', locale);
      applyToDOM();
      // Notify listeners
      document.dispatchEvent(new CustomEvent('i18n:locale-changed', { detail: { locale: locale } }));
    });
  }

  function applyToDOM() {
    var locale = currentLocale();

    // Text content
    var textEls = document.querySelectorAll('[data-i18n]');
    textEls.forEach(function (el) {
      var key = el.getAttribute('data-i18n');
      el.textContent = t(key);
    });

    // Placeholders
    var phEls = document.querySelectorAll('[data-i18n-placeholder]');
    phEls.forEach(function (el) {
      var key = el.getAttribute('data-i18n-placeholder');
      el.setAttribute('placeholder', t(key));
    });

    // aria-label
    var ariaEls = document.querySelectorAll('[data-i18n-aria-label]');
    ariaEls.forEach(function (el) {
      var key = el.getAttribute('data-i18n-aria-label');
      el.setAttribute('aria-label', t(key));
    });

    // aria-labelledby / title
    var titleEls = document.querySelectorAll('[data-i18n-title]');
    titleEls.forEach(function (el) {
      var key = el.getAttribute('data-i18n-title');
      el.setAttribute('title', t(key));
    });

    // Plural-aware
    var pluralEls = document.querySelectorAll('[data-i18n-plural]');
    pluralEls.forEach(function (el) {
      var key = el.getAttribute('data-i18n-plural');
      var count = parseInt(el.getAttribute('data-count'), 10) || 0;
      el.textContent = t(key, { count: count });
    });

    // Update <title>
    var titleEl = document.querySelector('head title[data-i18n]');
    if (titleEl) {
      document.title = t(titleEl.getAttribute('data-i18n'));
    }

    // Update language switcher selection state
    var switchers = document.querySelectorAll('[data-lang-switcher]');
    switchers.forEach(function (sw) {
      var opts = sw.querySelectorAll('[data-lang-option]');
      opts.forEach(function (opt) {
        var optLocale = opt.getAttribute('data-lang-option');
        var isActive = optLocale === locale;
        opt.classList.toggle('is-active', isActive);
        opt.setAttribute('aria-current', isActive ? 'true' : 'false');
      });
    });
  }

  function init() {
    ready = loadAll(currentLocale()).then(function () {
      document.documentElement.setAttribute('lang', currentLocale());
      applyToDOM();
      // Wire language switcher
      var switchers = document.querySelectorAll('[data-lang-switcher]');
      switchers.forEach(function (sw) {
        sw.addEventListener('click', function (e) {
          var target = e.target.closest('[data-lang-option]');
          if (!target) return;
          e.preventDefault();
          var newLocale = target.getAttribute('data-lang-option');
          setLocale(newLocale);
        });
      });
      return bundle;
    });
    return ready;
  }

  // Public API
  global.i18n = {
    init: init,
    t: t,
    setLocale: setLocale,
    currentLocale: currentLocale,
    supported: SUPPORTED.slice(),
    whenReady: function () { return ready || Promise.resolve(); },
    refresh: applyToDOM
  };

  // Auto-init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})(window);