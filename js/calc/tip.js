"use strict";
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("tip-form");
    var billField = document.getElementById("tip-bill");
    var tipField = document.getElementById("tip-percent");
    var peopleField = document.getElementById("tip-people");
    var readout = document.getElementById("tip-readout");
    var value = document.getElementById("tip-value");
    var sub = document.getElementById("tip-sub");

    var quickButtons = document.querySelectorAll("[data-tip-quick]");

    function compute() {
      if (billField.value.trim() === "") {
        readout.classList.remove("is-visible");
        return;
      }

      var bill = HR.toSafeNumber(billField.value);
      var tipPercent = HR.toSafeNumber(tipField.value);
      var people = HR.toSafeNumber(peopleField.value);

      if (bill === null || tipPercent === null || people === null || bill < 0 || tipPercent < 0 || people < 1) {
        HR.setText(value, "Revisa los valores");
        HR.setText(sub, "El total de la cuenta y la propina no pueden ser negativos, y debe haber al menos 1 persona.");
        HR.showReadout(readout, true);
        return;
      }

      people = Math.round(people);
      var tipAmount = (bill * tipPercent) / 100;
      var total = bill + tipAmount;
      var perPerson = total / people;
      var tipPerPerson = tipAmount / people;

      HR.setText(value, HR.formatNumber(perPerson) + " por persona");
      HR.setText(
        sub,
        "Propina total: " +
          HR.formatNumber(tipAmount) +
          " (" +
          HR.formatNumber(tipPerPerson) +
          " por persona)  ·  Total con propina: " +
          HR.formatNumber(total) +
          " entre " +
          people +
          (people === 1 ? " persona" : " personas")
      );
      HR.showReadout(readout, false);
    }

    quickButtons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        tipField.value = btn.getAttribute("data-tip-quick");
        compute();
      });
    });

    HR.wireLive(form, compute);
  });
})();
