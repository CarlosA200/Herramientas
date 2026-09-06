"use strict";
(function () {
  function categoryFor(bmi) {
    if (bmi < 18.5) return "Bajo peso";
    if (bmi < 25) return "Peso saludable";
    if (bmi < 30) return "Sobrepeso";
    return "Obesidad";
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("bmi-form");
    var unitSelect = document.getElementById("bmi-unit");
    var weightField = document.getElementById("bmi-weight");
    var heightField = document.getElementById("bmi-height");
    var weightUnitLabel = document.getElementById("bmi-weight-unit");
    var heightUnitLabel = document.getElementById("bmi-height-unit");
    var readout = document.getElementById("bmi-readout");
    var value = document.getElementById("bmi-value");
    var sub = document.getElementById("bmi-sub");

    function updateUnitLabels() {
      var metric = unitSelect.value === "metric";
      HR.setText(weightUnitLabel, metric ? "Peso (kg)" : "Peso (libras)");
      HR.setText(heightUnitLabel, metric ? "Estatura (cm)" : "Estatura (pulgadas)");
    }

    function compute() {
      updateUnitLabels();

      if (weightField.value.trim() === "" && heightField.value.trim() === "") {
        readout.classList.remove("is-visible");
        return;
      }

      var weight = HR.toSafeNumber(weightField.value);
      var height = HR.toSafeNumber(heightField.value);

      if (weight === null || height === null || weight <= 0 || height <= 0) {
        HR.setText(value, "Revisa los valores");
        HR.setText(sub, "El peso y la estatura deben ser números mayores que cero.");
        HR.showReadout(readout, true);
        return;
      }

      var bmi;
      if (unitSelect.value === "metric") {
        var meters = height / 100;
        bmi = weight / (meters * meters);
      } else {
        // imperial: peso en libras, estatura en pulgadas
        bmi = (weight / (height * height)) * 703;
      }

      HR.setText(value, HR.formatNumber(bmi, 1));
      HR.setText(sub, "Categoría: " + categoryFor(bmi) + " (clasificación general de la OMS).");
      HR.showReadout(readout, false);
    }

    updateUnitLabels();
    unitSelect.addEventListener("change", compute);
    HR.wireLive(form, compute);
  });
})();
