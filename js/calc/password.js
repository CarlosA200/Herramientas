"use strict";
(function () {
  var SETS = {
    lower: "abcdefghijklmnopqrstuvwxyz",
    upper: "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    numbers: "0123456789",
    symbols: "!@#$%^&*()-_=+[]{}?",
  };

  function secureRandomInt(maxExclusive) {
    var range = maxExclusive;
    var array = new Uint32Array(1);
    var limit = Math.floor(0xffffffff / range) * range;
    var val;
    do {
      window.crypto.getRandomValues(array);
      val = array[0];
    } while (val >= limit);
    return val % range;
  }

  function generatePassword(length, options) {
    var pool = "";
    var guaranteed = [];
    Object.keys(options).forEach(function (key) {
      if (options[key]) {
        pool += SETS[key];
        guaranteed.push(SETS[key][secureRandomInt(SETS[key].length)]);
      }
    });
    if (pool === "") return null;

    var chars = guaranteed.slice();
    while (chars.length < length) {
      chars.push(pool[secureRandomInt(pool.length)]);
    }
    // Barajar (Fisher-Yates) usando aleatoriedad criptográfica
    for (var i = chars.length - 1; i > 0; i--) {
      var j = secureRandomInt(i + 1);
      var tmp = chars[i];
      chars[i] = chars[j];
      chars[j] = tmp;
    }
    return chars.slice(0, length).join("");
  }

  function estimateStrength(length, options) {
    var poolSize = 0;
    Object.keys(options).forEach(function (key) {
      if (options[key]) poolSize += SETS[key].length;
    });
    if (poolSize === 0) return { label: "—", bits: 0 };
    var bits = Math.log2(poolSize) * length;
    var label = "Débil";
    if (bits >= 80) label = "Muy fuerte";
    else if (bits >= 60) label = "Fuerte";
    else if (bits >= 40) label = "Aceptable";
    return { label: label, bits: Math.round(bits) };
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("password-form");
    var lengthField = document.getElementById("password-length");
    var lengthOut = document.getElementById("password-length-out");
    var optLower = document.getElementById("opt-lower");
    var optUpper = document.getElementById("opt-upper");
    var optNumbers = document.getElementById("opt-numbers");
    var optSymbols = document.getElementById("opt-symbols");
    var readout = document.getElementById("password-readout");
    var value = document.getElementById("password-value");
    var sub = document.getElementById("password-sub");
    var copyBtn = document.getElementById("password-copy");

    function generate() {
      HR.setText(lengthOut, lengthField.value);

      var length = HR.toSafeNumber(lengthField.value);
      if (length === null) length = 16;
      length = Math.min(64, Math.max(6, Math.round(length)));

      var options = {
        lower: optLower.checked,
        upper: optUpper.checked,
        numbers: optNumbers.checked,
        symbols: optSymbols.checked,
      };

      var password = generatePassword(length, options);
      if (!password) {
        HR.setText(value, "Selecciona al menos un tipo de carácter");
        HR.setText(sub, "Marca minúsculas, mayúsculas, números o símbolos.");
        HR.showReadout(readout, true);
        return;
      }

      var strength = estimateStrength(length, options);
      HR.setText(value, password);
      HR.setText(sub, "Fortaleza estimada: " + strength.label + " (~" + strength.bits + " bits de entropía).");
      HR.showReadout(readout, false);
    }

    // Se genera al instante al mover el control de longitud o cambiar las
    // opciones marcadas; el botón "Generar" crea otra al azar con los mismos
    // ajustes.
    lengthField.addEventListener("input", HR.debounce(generate, 80));
    [optLower, optUpper, optNumbers, optSymbols].forEach(function (el) {
      el.addEventListener("change", generate);
    });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      generate();
    });

    generate();

    copyBtn.addEventListener("click", function () {
      var text = value.textContent;
      if (!text || text.indexOf(" ") !== -1) return; // evita copiar mensajes de error
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          var original = copyBtn.textContent;
          copyBtn.textContent = "¡Copiada!";
          setTimeout(function () {
            copyBtn.textContent = original;
          }, 1500);
        });
      }
    });
  });
})();
