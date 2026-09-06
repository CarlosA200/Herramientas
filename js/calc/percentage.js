"use strict";
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("percentage-form");
    var readout = document.getElementById("percentage-readout");
    var value = document.getElementById("percentage-value");
    var sub = document.getElementById("percentage-sub");
    var modeSelect = document.getElementById("percentage-mode");
    var fieldA = document.getElementById("percentage-a");
    var fieldB = document.getElementById("percentage-b");
    var labelA = document.getElementById("label-a");
    var labelB = document.getElementById("label-b");

    var MODES = {
      "of": { a: "Porcentaje (%)", b: "Del número" },
      "increase": { a: "Número inicial", b: "Porcentaje de aumento (%)" },
      "decrease": { a: "Número inicial", b: "Porcentaje de descuento (%)" },
      "change": { a: "Número inicial", b: "Número final" },
    };

    function updateLabels() {
      var mode = modeSelect.value;
      var cfg = MODES[mode] || MODES.of;
      HR.setText(labelA, cfg.a);
      HR.setText(labelB, cfg.b);
    }

    function compute() {
      updateLabels();
      var mode = modeSelect.value;

      if (fieldA.value.trim() === "" && fieldB.value.trim() === "") {
        readout.classList.remove("is-visible");
        return;
      }

      var a = HR.toSafeNumber(fieldA.value);
      var b = HR.toSafeNumber(fieldB.value);

      if (a === null || b === null) {
        HR.setText(value, "Revisa los valores");
        HR.setText(sub, "Introduce solo números válidos en ambos campos.");
        HR.showReadout(readout, true);
        return;
      }

      var result, subText;

      if (mode === "of") {
        result = (a / 100) * b;
        subText = a + "% de " + HR.formatNumber(b) + " es:";
      } else if (mode === "increase") {
        result = a + (a * b) / 100;
        subText = "Aumentar " + HR.formatNumber(a) + " en " + b + "% resulta en:";
      } else if (mode === "decrease") {
        result = a - (a * b) / 100;
        subText = "Aplicar " + b + "% de descuento a " + HR.formatNumber(a) + " resulta en:";
      } else {
        if (a === 0) {
          HR.setText(value, "No es posible dividir entre cero");
          HR.setText(sub, "El número inicial no puede ser 0 para calcular la variación.");
          HR.showReadout(readout, true);
          return;
        }
        result = ((b - a) / Math.abs(a)) * 100;
        subText =
          "La variación de " + HR.formatNumber(a) + " a " + HR.formatNumber(b) + " es:";
      }

      HR.setText(sub, subText);
      HR.setText(
        value,
        mode === "change" ? HR.formatNumber(result) + " %" : HR.formatNumber(result)
      );
      HR.showReadout(readout, false);
    }

    updateLabels();
    modeSelect.addEventListener("change", compute);
    HR.wireLive(form, compute);
  });
})();
