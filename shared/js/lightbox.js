// shared/js/lightbox.js — Silk Road Medinfo v2
// Vanilla JS image lightbox. Click any [data-lightbox] image to open.
// Closes on overlay click, X button, or Escape key.

(function (global) {
  'use strict';

  var active = null;
  var lastFocused = null;

  function build(src, alt, caption) {
    var box = document.createElement('div');
    box.className = 'lightbox';
    box.setAttribute('role', 'dialog');
    box.setAttribute('aria-modal', 'true');
    box.setAttribute('aria-label', alt || 'Image');

    var content = document.createElement('div');
    content.className = 'lightbox-content';

    var closeBtn = document.createElement('button');
    closeBtn.className = 'lightbox-close';
    closeBtn.setAttribute('aria-label', 'Close image');
    closeBtn.innerHTML = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M18 6L6 18M6 6l12 12"/></svg>';

    var img = document.createElement('img');
    img.className = 'lightbox-image';
    img.src = src;
    img.alt = alt || '';

    content.appendChild(closeBtn);
    content.appendChild(img);
    if (caption) {
      var cap = document.createElement('div');
      cap.className = 'lightbox-caption';
      cap.textContent = caption;
      content.appendChild(cap);
    }
    box.appendChild(content);

    return { box: box, closeBtn: closeBtn, img: img };
  }

  function open(src, alt, caption) {
    if (active) close();

    var built = build(src, alt, caption);
    document.body.appendChild(built.box);
    document.body.classList.add('is-lightbox-open');
    lastFocused = document.activeElement;

    // Force reflow then add open class for transition
    requestAnimationFrame(function () {
      built.box.classList.add('is-open');
    });

    // Focus the close button for keyboard a11y
    setTimeout(function () { built.closeBtn.focus(); }, 50);

    built.closeBtn.addEventListener('click', close);
    built.box.addEventListener('click', function (e) {
      if (e.target === built.box) close();
    });

    active = built;
  }

  function close() {
    if (!active) return;
    var box = active.box;
    box.classList.remove('is-open');
    document.body.classList.remove('is-lightbox-open');
    setTimeout(function () {
      if (box.parentNode) box.parentNode.removeChild(box);
    }, 400);
    if (lastFocused && lastFocused.focus) {
      lastFocused.focus();
    }
    active = null;
  }

  // Global escape key
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && active) {
      e.preventDefault();
      close();
    }
  });

  // Bind triggers
  document.addEventListener('click', function (e) {
    var trigger = e.target.closest('[data-lightbox]');
    if (!trigger) return;
    e.preventDefault();
    var src = trigger.getAttribute('data-lightbox-src') || trigger.getAttribute('src') || trigger.getAttribute('href');
    var alt = trigger.getAttribute('data-lightbox-alt') || trigger.getAttribute('alt') || '';
    var caption = trigger.getAttribute('data-lightbox-caption') || trigger.getAttribute('alt') || '';
    if (src) open(src, alt, caption);
  });

  // Public API
  global.Lightbox = { open: open, close: close };
})(window);