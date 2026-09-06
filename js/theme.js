/* Alternancia de modo claro/oscuro con persistencia en localStorage */
(function () {
  "use strict";

  var STORAGE_KEY = "hr-theme";
  var root = document.documentElement;

  function applyTheme(theme) {
    if (theme === "dark") {
      root.setAttribute("data-theme", "dark");
    } else {
      root.removeAttribute("data-theme");
    }
    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.setAttribute("aria-pressed", theme === "dark" ? "true" : "false");
      btn.setAttribute(
        "aria-label",
        theme === "dark" ? "Cambiar a modo claro" : "Cambiar a modo oscuro"
      );
    }
  }

  function getPreferredTheme() {
    try {
      var stored = window.localStorage.getItem(STORAGE_KEY);
      if (stored === "dark" || stored === "light") return stored;
    } catch (e) {
      /* localStorage no disponible: seguir con la preferencia del sistema */
    }
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches
      ? "dark"
      : "light";
  }

  var current = getPreferredTheme();
  applyTheme(current);

  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("theme-toggle");
    if (!btn) return;
    applyTheme(current);
    btn.addEventListener("click", function () {
      current = current === "dark" ? "light" : "dark";
      applyTheme(current);
      try {
        window.localStorage.setItem(STORAGE_KEY, current);
      } catch (e) {
        /* si falla el guardado, la preferencia solo dura la sesión */
      }
    });
  });
})();
