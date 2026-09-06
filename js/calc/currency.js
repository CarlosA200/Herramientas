"use strict";
(function () {
  /* Conversor de monedas con tasas de cambio EN VIVO.
     Fuente: open.er-api.com (API pública y gratuita, sin clave, con CORS
     habilitado, actualizada aprox. una vez al día por el Banco Central Europeo
     y fuentes de mercado). Si la consulta falla, se usa la última tasa que
     el propio navegador guardó localmente, y si tampoco existe, una tabla de
     respaldo aproximada como último recurso. */

  var API_URL = "https://open.er-api.com/v6/latest/USD";
  var STORAGE_KEY = "hr-currency-rates-v1";
  var CACHE_MAX_AGE_MS = 6 * 60 * 60 * 1000; // 6 horas

  var LABELS = {
    USD: "Dólar estadounidense (USD)",
    EUR: "Euro (EUR)",
    DOP: "Peso dominicano (DOP)",
    MXN: "Peso mexicano (MXN)",
    GBP: "Libra esterlina (GBP)",
    JPY: "Yen japonés (JPY)",
    CAD: "Dólar canadiense (CAD)",
    COP: "Peso colombiano (COP)",
  };

  // Respaldo de último recurso, solo si no hay caché ni conexión disponibles.
  var FALLBACK_RATES_USD = {
    USD: 1, EUR: 0.92, DOP: 60.5, MXN: 18.1, GBP: 0.79, JPY: 149.5, CAD: 1.36, COP: 4100,
  };

  var state = {
    rates: null,
    fetchedAt: null,
    isFallback: false,
  };

  function readCache() {
    try {
      var raw = window.localStorage.getItem(STORAGE_KEY);
      if (!raw) return null;
      var parsed = JSON.parse(raw);
      if (parsed && parsed.rates && parsed.fetchedAt) return parsed;
    } catch (e) {
      /* localStorage no disponible o dato corrupto: se ignora */
    }
    return null;
  }

  function writeCache(rates, fetchedAt) {
    try {
      window.localStorage.setItem(
        STORAGE_KEY,
        JSON.stringify({ rates: rates, fetchedAt: fetchedAt })
      );
    } catch (e) {
      /* si falla el guardado, la app sigue funcionando solo sin caché */
    }
  }

  function formatTime(iso) {
    try {
      var d = new Date(iso);
      return d.toLocaleString("es-ES", {
        day: "2-digit",
        month: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      });
    } catch (e) {
      return "";
    }
  }

  function populateSelect(select) {
    Object.keys(LABELS).forEach(function (code) {
      var opt = document.createElement("option");
      opt.value = code;
      opt.textContent = LABELS[code];
      select.appendChild(opt);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    var form = document.getElementById("currency-form");
    var amountField = document.getElementById("currency-amount");
    var fromSelect = document.getElementById("currency-from");
    var toSelect = document.getElementById("currency-to");
    var readout = document.getElementById("currency-readout");
    var value = document.getElementById("currency-value");
    var sub = document.getElementById("currency-sub");
    var swapBtn = document.getElementById("currency-swap");
    var statusEl = document.getElementById("currency-rate-status");
    var statusText = document.getElementById("currency-rate-status-text");

    populateSelect(fromSelect);
    populateSelect(toSelect);
    fromSelect.value = "USD";
    toSelect.value = "EUR";

    function setStatus(mode, text) {
      statusEl.classList.remove("is-loading", "is-error");
      if (mode) statusEl.classList.add(mode);
      HR.setText(statusText, text);
    }

    function compute() {
      if (!state.rates) return;
      if (amountField.value.trim() === "") {
        readout.classList.remove("is-visible");
        return;
      }

      var amount = HR.toSafeNumber(amountField.value);
      var from = fromSelect.value;
      var to = toSelect.value;

      if (amount === null || amount < 0) {
        HR.setText(value, "Revisa el monto");
        HR.setText(sub, "Introduce un número igual o mayor que cero.");
        HR.showReadout(readout, true);
        return;
      }
      if (!state.rates[from] || !state.rates[to]) {
        HR.setText(value, "Moneda no reconocida");
        HR.setText(sub, "Selecciona una moneda válida de la lista.");
        HR.showReadout(readout, true);
        return;
      }

      var inUsd = amount / state.rates[from];
      var result = inUsd * state.rates[to];

      HR.setText(value, HR.formatNumber(result) + " " + to);
      HR.setText(
        sub,
        HR.formatNumber(amount) +
          " " +
          from +
          " equivalen a, con la tasa " +
          (state.isFallback ? "aproximada" : "en vivo") +
          (state.fetchedAt ? " del " + formatTime(state.fetchedAt) : "") +
          ":"
      );
      HR.showReadout(readout, false);
    }

    swapBtn.addEventListener("click", function () {
      var tmp = fromSelect.value;
      fromSelect.value = toSelect.value;
      toSelect.value = tmp;
      compute();
    });

    // 1) Muestra de inmediato cualquier tasa guardada en este navegador,
    //    para que la herramienta funcione al instante sin esperar la red.
    var cached = readCache();
    if (cached) {
      state.rates = cached.rates;
      state.fetchedAt = cached.fetchedAt;
      state.isFallback = false;
      var age = Date.now() - new Date(cached.fetchedAt).getTime();
      setStatus(
        age > CACHE_MAX_AGE_MS ? "is-loading" : null,
        "Tasa guardada del " + formatTime(cached.fetchedAt) + " — actualizando…"
      );
    } else {
      setStatus("is-loading", "Consultando tasas en vivo…");
    }

    HR.wireLive(form, compute);

    // 2) Consulta el servicio en vivo y reemplaza la tasa en cuanto responde.
    fetch(API_URL)
      .then(function (res) {
        if (!res.ok) throw new Error("Respuesta no válida del servicio de tasas");
        return res.json();
      })
      .then(function (data) {
        if (!data || data.result !== "success" || !data.rates) {
          throw new Error("Formato de datos inesperado");
        }
        var now = new Date().toISOString();
        state.rates = data.rates;
        state.fetchedAt = now;
        state.isFallback = false;
        writeCache(data.rates, now);
        setStatus(null, "Tasas en vivo actualizadas · " + formatTime(now));
        compute();
      })
      .catch(function () {
        if (state.rates) {
          // Ya teníamos una tasa en caché: seguimos con ella, solo avisamos.
          setStatus(
            "is-error",
            "Sin conexión con el servicio de tasas — usando la última guardada (" +
              formatTime(state.fetchedAt) +
              ")"
          );
        } else {
          // Ni red ni caché disponibles: último recurso.
          state.rates = FALLBACK_RATES_USD;
          state.fetchedAt = null;
          state.isFallback = true;
          setStatus(
            "is-error",
            "No se pudo conectar con el servicio de tasas — usando valores aproximados"
          );
          compute();
        }
      });
  });
})();
