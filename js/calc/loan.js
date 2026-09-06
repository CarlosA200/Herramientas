"use strict";
(function () {
  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("loan-form");
    var readout = document.getElementById("loan-readout");
    var value = document.getElementById("loan-value");
    var sub = document.getElementById("loan-sub");
    var tableBody = document.getElementById("loan-table-body");
    var tableWrap = document.getElementById("loan-table-wrap");

    var amountField = document.getElementById("loan-amount");
    var rateField = document.getElementById("loan-rate");
    var yearsField = document.getElementById("loan-years");

    function compute() {
      if (
        amountField.value.trim() === "" &&
        rateField.value.trim() === "" &&
        yearsField.value.trim() === ""
      ) {
        readout.classList.remove("is-visible");
        tableWrap.style.display = "none";
        return;
      }

      var principal = HR.toSafeNumber(amountField.value);
      var annualRate = HR.toSafeNumber(rateField.value);
      var years = HR.toSafeNumber(yearsField.value);

      if (
        principal === null ||
        annualRate === null ||
        years === null ||
        principal <= 0 ||
        annualRate < 0 ||
        years <= 0
      ) {
        HR.setText(value, "Revisa los valores");
        HR.setText(
          sub,
          "El monto y el plazo deben ser mayores que cero, y la tasa no puede ser negativa."
        );
        HR.showReadout(readout, true);
        tableWrap.style.display = "none";
        return;
      }

      var months = Math.round(years * 12);
      var monthlyRate = annualRate / 100 / 12;
      var payment;

      if (monthlyRate === 0) {
        payment = principal / months;
      } else {
        payment =
          (principal * monthlyRate) /
          (1 - Math.pow(1 + monthlyRate, -months));
      }

      var totalPaid = payment * months;
      var totalInterest = totalPaid - principal;

      HR.setText(value, HR.formatNumber(payment) + " / mes");
      HR.setText(
        sub,
        "Interés total: " +
          HR.formatNumber(totalInterest) +
          "  ·  Total pagado: " +
          HR.formatNumber(totalPaid) +
          "  ·  " +
          months +
          " cuotas"
      );
      HR.showReadout(readout, false);

      // Tabla resumen de los primeros 12 meses (o menos, si el plazo es corto)
      tableBody.textContent = "";
      var balance = principal;
      var rowsToShow = Math.min(months, 12);
      for (var i = 1; i <= rowsToShow; i++) {
        var interestPortion = balance * monthlyRate;
        var principalPortion = payment - interestPortion;
        balance = Math.max(0, balance - principalPortion);

        var tr = document.createElement("tr");
        var cells = [
          i,
          HR.formatNumber(payment),
          HR.formatNumber(interestPortion),
          HR.formatNumber(principalPortion),
          HR.formatNumber(balance),
        ];
        cells.forEach(function (val) {
          var td = document.createElement("td");
          td.textContent = String(val);
          tr.appendChild(td);
        });
        tableBody.appendChild(tr);
      }
      tableWrap.style.display = "";
    }

    HR.wireLive(form, compute);
  });
})();
