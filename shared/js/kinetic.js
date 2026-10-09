// shared/js/kinetic.js — silk road medinfo v3
// Per-character / per-word animation for h1.hero-headline.
// Splits text into chars (keeping word boundaries) and applies sequential reveal.

(function () {
  'use strict';

  function splitText(el) {
    var html = el.innerHTML;
    // Preserve any inline elements like <em class="accent">...</em>
    if (el.dataset.kineticDone) return;
    el.dataset.kineticDone = '1';

    var result = '';
    var ci = 0;
    function processNode(node) {
      if (node.nodeType === Node.TEXT_NODE) {
        var text = node.textContent;
        for (var i = 0; i < text.length; i++) {
          var ch = text[i];
          if (ch === ' ') {
            result += ' ';
          } else {
            result += '<span class="char" style="--char-i:' + ci + '">' + escapeHTML(ch) + '</span>';
            ci++;
          }
        }
      } else if (node.nodeType === Node.ELEMENT_NODE) {
        var tag = node.tagName.toLowerCase();
        if (tag === 'br') {
          result += '<br>';
          return;
        }
        var attrs = '';
        for (var j = 0; j < node.attributes.length; j++) {
          var a = node.attributes[j];
          attrs += ' ' + a.name + '="' + a.value + '"';
        }
        result += '<' + tag + attrs + '>';
        for (var k = 0; k < node.childNodes.length; k++) {
          processNode(node.childNodes[k]);
        }
        result += '</' + tag + '>';
      }
    }

    var tmp = document.createElement('div');
    tmp.innerHTML = html;
    for (var i = 0; i < tmp.childNodes.length; i++) {
      processNode(tmp.childNodes[i]);
    }
    el.innerHTML = result;
  }

  function escapeHTML(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return ({ '&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;' })[c];
    });
  }

  function init() {
    document.querySelectorAll('.hero-flagship .hero-headline').forEach(splitText);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();