"use strict";
(function () {
  function daysInMonth(year, monthIndex) {
    return new Date(year, monthIndex + 1, 0).getDate();
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("age-form");
    var dobField = document.getElementById("age-dob");
    var readout = document.getElementById("age-readout");
    var value = document.getElementById("age-value");
    var sub = document.getElementById("age-sub");

    // Límite razonable: no permitir fechas futuras en el input
    var todayStr = new Date().toISOString().slice(0, 10);
    dobField.setAttribute("max", todayStr);

    function compute() {
      var raw = dobField.value;
      if (!raw) {
        readout.classList.remove("is-visible");
        return;
      }

      var dob = new Date(raw + "T00:00:00");
      var today = new Date();
      today.setHours(0, 0, 0, 0);

      if (isNaN(dob.getTime()) || dob > today) {
        HR.setText(value, "Fecha no válida");
        HR.setText(sub, "La fecha de nacimiento no puede ser futura.");
        HR.showReadout(readout, true);
        return;
      }

      var years = today.getFullYear() - dob.getFullYear();
      var months = today.getMonth() - dob.getMonth();
      var days = today.getDate() - dob.getDate();

      if (days < 0) {
        months -= 1;
        var prevMonth = today.getMonth() - 1;
        var prevYear = today.getFullYear();
        if (prevMonth < 0) {
          prevMonth = 11;
          prevYear -= 1;
        }
        days += daysInMonth(prevYear, prevMonth);
      }
      if (months < 0) {
        months += 12;
        years -= 1;
      }

      // Próximo cumpleaños
      var nextBirthday = new Date(today.getFullYear(), dob.getMonth(), dob.getDate());
      if (nextBirthday < today) {
        nextBirthday.setFullYear(today.getFullYear() + 1);
      }
      var msPerDay = 1000 * 60 * 60 * 24;
      var daysToNext = Math.round((nextBirthday - today) / msPerDay);

      HR.setText(value, years + " años");
      HR.setText(
        sub,
        months +
          " meses y " +
          days +
          " días adicionales  ·  Faltan " +
          daysToNext +
          " días para tu próximo cumpleaños."
      );
      HR.showReadout(readout, false);
    }

    HR.wireLive(form, compute);
  });
})();
