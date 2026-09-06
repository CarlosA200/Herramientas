"use strict";
(function () {
  /* Factores de conversión a una unidad base por categoría. */
  var LENGTH_TO_M = {
    mm: 0.001, cm: 0.01, m: 1, km: 1000,
    in: 0.0254, ft: 0.3048, yd: 0.9144, mi: 1609.344,
  };
  var LENGTH_LABELS = {
    mm: "Milímetros (mm)", cm: "Centímetros (cm)", m: "Metros (m)", km: "Kilómetros (km)",
    in: "Pulgadas (in)", ft: "Pies (ft)", yd: "Yardas (yd)", mi: "Millas (mi)",
  };

  var WEIGHT_TO_KG = {
    mg: 0.000001, g: 0.001, kg: 1, t: 1000,
    lb: 0.45359237, oz: 0.028349523,
  };
  var WEIGHT_LABELS = {
    mg: "Miligramos (mg)", g: "Gramos (g)", kg: "Kilogramos (kg)", t: "Toneladas (t)",
    lb: "Libras (lb)", oz: "Onzas (oz)",
  };

  var TEMP_LABELS = { c: "Celsius (°C)", f: "Fahrenheit (°F)", k: "Kelvin (K)" };

  var CATEGORIES = {
    length: { factors: LENGTH_TO_M, labels: LENGTH_LABELS, default: ["m", "ft"] },
    weight: { factors: WEIGHT_TO_KG, labels: WEIGHT_LABELS, default: ["kg", "lb"] },
    temperature: { labels: TEMP_LABELS, default: ["c", "f"] },
  };

  function toCelsius(value, unit) {
    if (unit === "c") return value;
    if (unit === "f") return ((value - 32) * 5) / 9;
    return value - 273.15; // Kelvin
  }
  function fromCelsius(celsius, unit) {
    if (unit === "c") return celsius;
    if (unit === "f") return (celsius * 9) / 5 + 32;
    return celsius + 273.15; // Kelvin
  }

  function populate(select, labels, selected) {
    select.textContent = "";
    Object.keys(labels).forEach(function (key) {
      var opt = document.createElement("option");
      opt.value = key;
      opt.textContent = labels[key];
      if (key === selected) opt.selected = true;
      select.appendChild(opt);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var categorySelect = document.getElementById("units-category");
    var fromSelect = document.getElementById("units-from");
    var toSelect = document.getElementById("units-to");
    var form = document.getElementById("units-form");
    var amountField = document.getElementById("units-amount");
    var readout = document.getElementById("units-readout");
    var value = document.getElementById("units-value");
    var sub = document.getElementById("units-sub");
    var swapBtn = document.getElementById("units-swap");

    function refreshUnitOptions() {
      var cat = CATEGORIES[categorySelect.value];
      populate(fromSelect, cat.labels, cat.default[0]);
      populate(toSelect, cat.labels, cat.default[1]);
    }

    function compute() {
      if (amountField.value.trim() === "") {
        readout.classList.remove("is-visible");
        return;
      }

      var amount = HR.toSafeNumber(amountField.value);
      if (amount === null) {
        HR.setText(value, "Revisa el valor");
        HR.setText(sub, "Introduce un número válido para convertir.");
        HR.showReadout(readout, true);
        return;
      }

      var category = categorySelect.value;
      var from = fromSelect.value;
      var to = toSelect.value;
      var result;

      if (category === "temperature") {
        result = fromCelsius(toCelsius(amount, from), to);
      } else {
        var factors = CATEGORIES[category].factors;
        var base = amount * factors[from];
        result = base / factors[to];
      }

      var labels = CATEGORIES[category].labels;
      HR.setText(value, HR.formatNumber(result, 4));
      HR.setText(
        sub,
        HR.formatNumber(amount, 4) + " " + labels[from] + " equivalen a, en " + labels[to] + ":"
      );
      HR.showReadout(readout, false);
    }

    refreshUnitOptions();
    categorySelect.addEventListener("change", function () {
      refreshUnitOptions();
      compute();
    });

    swapBtn.addEventListener("click", function () {
      var tmp = fromSelect.value;
      fromSelect.value = toSelect.value;
      toSelect.value = tmp;
      compute();
    });

    HR.wireLive(form, compute);
  });
})();
