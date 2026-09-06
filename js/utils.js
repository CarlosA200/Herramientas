/* Utilidades compartidas: nunca usar eval() ni innerHTML con datos del usuario. */
"use strict";

var HR = window.HR || {};

/**
 * Convierte un valor de input en un número finito y seguro.
 * Devuelve null si el valor no es un número válido.
 */
HR.toSafeNumber = function (raw) {
  if (typeof raw !== "string") return null;
  var cleaned = raw.trim().replace(",", ".");
  if (cleaned === "" || !/^-?\d*\.?\d+$/.test(cleaned)) return null;
  var num = Number(cleaned);
  return Number.isFinite(num) ? num : null;
};

/** Escribe texto plano en un elemento sin interpretar HTML (evita XSS). */
HR.setText = function (el, text) {
  if (!el) return;
  el.textContent = text;
};

/** Formatea un número con separador de miles y decimales fijos. */
HR.formatNumber = function (num, decimals) {
  if (typeof decimals !== "number") decimals = 2;
  if (!Number.isFinite(num)) return "—";
  return num.toLocaleString("es-ES", {
    minimumFractionDigits: decimals,
    maximumFractionDigits: decimals,
  });
};

/** Muestra un panel de resultado (readout) y opcionalmente marca error. */
HR.showReadout = function (el, isError) {
  if (!el) return;
  el.classList.add("is-visible");
  el.classList.toggle("error", !!isError);
};

/** Sanea texto libre (nombre, mensaje) quitando cualquier marcado HTML. */
HR.sanitizePlainText = function (raw) {
  if (typeof raw !== "string") return "";
  var div = document.createElement("div");
  div.textContent = raw;
  return div.textContent.trim().slice(0, 2000);
};

/** Devuelve una versión "debounced" de fn: espera `wait` ms de silencio antes de ejecutar. */
HR.debounce = function (fn, wait) {
  var timer = null;
  return function () {
    var args = arguments;
    var ctx = this;
    clearTimeout(timer);
    timer = setTimeout(function () {
      fn.apply(ctx, args);
    }, wait || 150);
  };
};

/**
 * Conecta un formulario para que se recalcule en tiempo real:
 * - al escribir/cambiar cualquier campo (con un pequeño debounce), y
 * - al enviar el formulario (Enter o clic en el botón), de forma inmediata.
 * `compute` es la función que valida y pinta el resultado; no recibe argumentos.
 */
HR.wireLive = function (form, compute, options) {
  if (!form || typeof compute !== "function") return;
  var wait = (options && options.wait) || 180;
  var debounced = HR.debounce(compute, wait);

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    compute();
  });

  var fields = form.querySelectorAll("input, select, textarea");
  fields.forEach(function (field) {
    var evt = field.tagName === "SELECT" || field.type === "checkbox" || field.type === "range"
      ? "input"
      : "input";
    field.addEventListener(evt, debounced);
  });

  if (options && options.runOnLoad) {
    compute();
  }
};

window.HR = HR;
