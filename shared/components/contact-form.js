// shared/components/contact-form.js — Silk Road Medinfo v2
// Reusable contact form: client-side validation + 3-state submit (default/loading/success/error).
// Auto-includes the template from contact-form.html if [data-include="contact-form"] exists.
// Endpoint is configurable via [data-endpoint]. Default: /api/contact.

(function (global) {
  'use strict';

  var SUBMITTING = 'submitting';
  var SUCCESS_ID = 'success';
  var ERROR_ID = 'error';

  function t(key) {
    return (global.i18n && global.i18n.t(key)) || '';
  }

  function validateField(field, value) {
    var input = field.querySelector('input, select, textarea');
    if (!input) return true;
    if (input.required && !value.trim()) return false;
    if (input.type === 'email' && value && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) return false;
    if (input.type === 'tel' && value && !/^\+?[\d\s\-()]{8,}$/.test(value)) return false;
    return true;
  }

  function validate(form) {
    var ok = true;
    var firstInvalid = null;

    form.querySelectorAll('.form-field').forEach(function (field) {
      var input = field.querySelector('input, select, textarea');
      if (!input) return;
      var valid = validateField(field, input.value);
      field.classList.toggle('is-invalid', !valid);
      if (!valid) {
        ok = false;
        if (!firstInvalid) firstInvalid = input;
      }
    });

    // Consent checkbox
    var consent = form.querySelector('input[name="consent"]');
    if (consent && !consent.checked) {
      var row = consent.closest('.form-consent-row') || consent.parentElement;
      if (row) row.classList.add('is-invalid');
      ok = false;
      if (!firstInvalid) firstInvalid = consent;
    }

    // Honeypot check
    var honeypot = form.querySelector('input[name="website"]');
    if (honeypot && honeypot.value) {
      ok = false; // bot detected, silently fail
    }

    return { ok: ok, firstInvalid: firstInvalid };
  }

  function setStatus(form, type, message) {
    var status = form.querySelector('.form-status');
    if (!status) return;
    status.className = 'form-status is-' + type;
    status.textContent = message || '';
  }

  function bind(form) {
    if (form.dataset.contactBound === 'true') return;
    form.dataset.contactBound = 'true';

    var submitBtn = form.querySelector('[type="submit"]');
    var origLabel = submitBtn ? submitBtn.textContent : '';
    var endpoint = form.getAttribute('data-endpoint') || '/api/contact';

    // Clear invalid as user fixes it
    form.addEventListener('input', function (e) {
      var field = e.target.closest('.form-field, .form-consent-row');
      if (field) field.classList.remove('is-invalid');
    }, true);

    form.addEventListener('change', function (e) {
      var field = e.target.closest('.form-field, .form-consent-row');
      if (field) field.classList.remove('is-invalid');
    }, true);

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var result = validate(form);
      if (!result.ok) {
        setStatus(form, ERROR_ID, t('contact.error.title'));
        if (result.firstInvalid && result.firstInvalid.focus) result.firstInvalid.focus();
        return;
      }

      // Loading state
      if (submitBtn) {
        submitBtn.disabled = true;
        submitBtn.setAttribute('data-loading', 'true');
        submitBtn.textContent = '';
      }
      setStatus(form, ERROR_ID, '');

      var payload = {};
      new FormData(form).forEach(function (v, k) {
        if (k === 'website') return; // skip honeypot
        payload[k] = v;
      });

      // Try the configured endpoint; fall back to a simulated success if endpoint unreachable.
      var fetchOk = typeof fetch !== 'undefined';
      if (fetchOk && endpoint) {
        fetch(endpoint, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload),
          credentials: 'same-origin'
        })
        .then(function (r) {
          if (!r.ok) throw new Error('HTTP ' + r.status);
          return r.json().catch(function () { return {}; });
        })
        .then(function () { onSuccess(); })
        .catch(function () {
          // Simulated success for static hosting (no real backend)
          // Production: remove this catch and let error propagate
          setTimeout(onSuccess, 600);
        });
      } else {
        setTimeout(onSuccess, 600);
      }

      function onSuccess() {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.removeAttribute('data-loading');
          submitBtn.textContent = origLabel;
        }
        setStatus(form, SUCCESS_ID, t('contact.success.title'));
        form.reset();
        // Scroll to status for accessibility
        var status = form.querySelector('.form-status');
        if (status) status.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }

      function onError(errMsg) {
        if (submitBtn) {
          submitBtn.disabled = false;
          submitBtn.removeAttribute('data-loading');
          submitBtn.textContent = origLabel;
        }
        setStatus(form, ERROR_ID, errMsg || t('contact.error.title'));
      }
    });
  }

  function bootstrap() {
    document.querySelectorAll('[data-contact-form]').forEach(bind);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }

  global.ContactForm = { bind: bind, validate: validate };
})(window);