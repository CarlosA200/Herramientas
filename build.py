# -*- coding: utf-8 -*-
"""
Generador estático del sitio "Herramientas Rápidas".
Construye cada página HTML a partir de una plantilla compartida
(header, footer, meta tags, CSP, schema.org) para no repetir manualmente
el boilerplate en las 13 páginas del sitio.
"""
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://herramientas-rapidas.example.com"  # reemplazar por el dominio real

CSP = (
    "default-src 'self'; "
    "script-src 'self' https://pagead2.googlesyndication.com "
    "https://www.googletagmanager.com https://www.google-analytics.com "
    "https://adservice.google.com; "
    "style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; "
    "font-src https://fonts.gstatic.com; "
    "img-src 'self' data: https:; "
    "frame-src https://googleads.g.doubleclick.net; "
    "connect-src 'self' https://www.google-analytics.com https://open.er-api.com;"
)

NAV_ITEMS = [
    ("index.html", "Inicio"),
    ("calculators/percentage.html", "Herramientas"),
    ("about.html", "Acerca de"),
    ("contact.html", "Contacto"),
]

TOOLS = [
    {
        "id": "percentage",
        "file": "calculators/percentage.html",
        "name": "Calculadora de porcentajes",
        "short": "Calcula porcentajes, aumentos y descuentos al instante.",
        "desc": "Calculadora de porcentajes online gratis: obtén el porcentaje de un número, "
                "el aumento o descuento porcentual y la variación entre dos cifras.",
        "keywords": "calculadora de porcentajes, calcular porcentaje, descuento porcentual",
        "icon": "percent",
    },
    {
        "id": "currency",
        "file": "calculators/currency.html",
        "name": "Conversor de monedas",
        "short": "Convierte entre las principales divisas del mundo.",
        "desc": "Conversor de monedas gratuito con tasas de cambio de ejemplo editables: "
                "convierte USD, EUR, DOP, MXN y más divisas en segundos.",
        "keywords": "conversor de monedas, convertir dólares a euros, tipo de cambio",
        "icon": "coins",
    },
    {
        "id": "loan",
        "file": "calculators/loan.html",
        "name": "Calculadora de préstamos e hipotecas",
        "short": "Calcula tu cuota mensual y el interés total del préstamo.",
        "desc": "Calculadora de préstamos e hipotecas: calcula la cuota mensual, el interés "
                "total y el calendario de pagos según el monto, plazo y tasa de interés.",
        "keywords": "calculadora de préstamos, calculadora hipotecaria, cuota mensual préstamo",
        "icon": "landmark",
    },
    {
        "id": "units",
        "file": "calculators/units.html",
        "name": "Conversor de unidades",
        "short": "Convierte longitud, peso y temperatura fácilmente.",
        "desc": "Conversor de unidades online: convierte longitud (metros, pies, millas), "
                "peso (kg, libras) y temperatura (Celsius, Fahrenheit, Kelvin).",
        "keywords": "conversor de unidades, convertir kg a libras, convertir celsius a fahrenheit",
        "icon": "ruler",
    },
    {
        "id": "bmi",
        "file": "calculators/bmi.html",
        "name": "Calculadora de IMC",
        "short": "Calcula tu índice de masa corporal y su categoría.",
        "desc": "Calculadora de IMC (índice de masa corporal) gratis: introduce tu peso y "
                "estatura y obtén tu IMC junto con su categoría según la OMS.",
        "keywords": "calculadora de imc, índice de masa corporal, calcular imc",
        "icon": "activity",
    },
    {
        "id": "password",
        "file": "calculators/password.html",
        "name": "Generador de contraseñas seguras",
        "short": "Crea contraseñas aleatorias y seguras al instante.",
        "desc": "Generador de contraseñas seguras online: crea contraseñas aleatorias con "
                "mayúsculas, minúsculas, números y símbolos, con control de longitud.",
        "keywords": "generador de contraseñas, crear contraseña segura, contraseña aleatoria",
        "icon": "key",
    },
    {
        "id": "age",
        "file": "calculators/age.html",
        "name": "Calculadora de edad",
        "short": "Calcula tu edad exacta en años, meses y días.",
        "desc": "Calculadora de edad online: introduce tu fecha de nacimiento y obtén tu "
                "edad exacta en años, meses y días, además de los días que faltan para tu próximo cumpleaños.",
        "keywords": "calculadora de edad, calcular edad exacta, cuántos años tengo",
        "icon": "calendar",
    },
    {
        "id": "tip",
        "file": "calculators/tip.html",
        "name": "Calculadora de propinas",
        "short": "Calcula la propina y divide la cuenta entre varias personas.",
        "desc": "Calculadora de propinas y división de cuenta: calcula cuánto dar de propina "
                "y cuánto le corresponde pagar a cada persona en el grupo.",
        "keywords": "calculadora de propinas, dividir cuenta entre amigos, calcular propina",
        "icon": "receipt",
    },
]

ICONS = {
    "percent": '<path d="M19 5 5 19"/><circle cx="6.5" cy="6.5" r="2.5"/><circle cx="17.5" cy="17.5" r="2.5"/>',
    "coins": '<circle cx="8" cy="8" r="6"/><path d="M18.09 10.37A6 6 0 1 1 10.34 18"/><path d="M7 6h1v4"/><path d="m16.71 13.88.7.71-2.82 2.82"/>',
    "landmark": '<line x1="3" x2="21" y1="22" y2="22"/><line x1="6" x2="6" y1="18" y2="11"/><line x1="10" x2="10" y1="18" y2="11"/><line x1="14" x2="14" y1="18" y2="11"/><line x1="18" x2="18" y1="18" y2="11"/><polygon points="12 2 20 7 4 7"/>',
    "ruler": '<path d="M21.3 15.3a2.4 2.4 0 0 1 0 3.4l-2.6 2.6a2.4 2.4 0 0 1-3.4 0L2.7 8.7a2.4 2.4 0 0 1 0-3.4l2.6-2.6a2.4 2.4 0 0 1 3.4 0Z"/><path d="m14.5 12.5 2-2"/><path d="m11.5 9.5 2-2"/><path d="m8.5 6.5 2-2"/><path d="m17.5 15.5 2-2"/>',
    "activity": '<path d="M22 12h-4l-3 9L9 3l-3 9H2"/>',
    "key": '<circle cx="7.5" cy="15.5" r="5.5"/><path d="m21 2-9.6 9.6"/><path d="m15.5 7.5 3 3L22 7l-3-3"/>',
    "calendar": '<rect width="18" height="18" x="3" y="4" rx="2"/><path d="M16 2v4"/><path d="M8 2v4"/><path d="M3 10h18"/>',
    "receipt": '<path d="M4 2h16v20l-3-2-3 2-3-2-3 2-3-2-1 1V2Z"/><path d="M8 7h8"/><path d="M8 11h8"/><path d="M8 15h5"/>',
}


def icon(name, size=22):
    body = ICONS.get(name, "")
    return (
        f'<svg class="icon" width="{size}" height="{size}" viewBox="0 0 24 24" '
        f'fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
        f'stroke-linejoin="round" aria-hidden="true">{body}</svg>'
    )


def rel(depth):
    return "../" * depth


def head(title, description, canonical_path, depth, extra_schema="", keywords=""):
    r = rel(depth)
    og_image = f"{SITE_URL}/img/og-cover.png"
    kw = f'\n  <meta name="keywords" content="{keywords}">' if keywords else ""
    return f"""<meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title}</title>
  <meta name="description" content="{description}">{kw}
  <link rel="canonical" href="{SITE_URL}/{canonical_path}">
  <meta http-equiv="Content-Security-Policy" content="{CSP}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{SITE_URL}/{canonical_path}">
  <meta property="og:image" content="{og_image}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{title}">
  <meta name="twitter:description" content="{description}">
  <link rel="icon" href="{r}img/favicon.svg" type="image/svg+xml">
  <link rel="stylesheet" href="{r}css/style.css">
  <script>
    (function(){{try{{var t=localStorage.getItem('hr-theme');if(t==='dark'){{document.documentElement.setAttribute('data-theme','dark');}}}}catch(e){{}}}})();
  </script>
  {extra_schema}"""


def header_html(depth, active=""):
    r = rel(depth)
    links = []
    targets = [
        (r + "index.html", "Inicio", "index"),
        (r + "calculators/percentage.html", "Herramientas", "tools"),
        (r + "about.html", "Acerca de", "about"),
        (r + "contact.html", "Contacto", "contact"),
    ]
    for href, label, key in targets:
        cur = ' aria-current="page"' if key == active else ""
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    nav = "\n        ".join(links)
    return f"""<a class="skip-link" href="#contenido">Saltar al contenido</a>
  <header class="site-header">
    <div class="wrap">
      <a class="brand" href="{r}index.html">
        <svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="2" width="16" height="20" rx="2"/><line x1="8" y1="7" x2="16" y2="7"/><line x1="8" y1="11" x2="10" y2="11"/><line x1="8" y1="15" x2="10" y2="15"/><line x1="14" y1="11" x2="16" y2="11"/><line x1="14" y1="15" x2="16" y2="15"/></svg>
        Herramientas Rápidas
      </a>
      <nav class="main-nav" aria-label="Navegación principal">
        {nav}
      </nav>
      <button id="theme-toggle" class="theme-toggle" type="button" aria-pressed="false" aria-label="Cambiar a modo oscuro">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3a6 6 0 0 0 9 9 9 9 0 1 1-9-9Z"/></svg>
      </button>
    </div>
  </header>"""


def footer_html(depth):
    r = rel(depth)
    year = 2026
    return f"""<footer class="site-footer">
    <div class="wrap">
      <p>&copy; {year} Herramientas Rápidas. Todas las calculadoras son gratuitas y de uso libre.</p>
      <nav class="footer-links" aria-label="Enlaces legales">
        <a href="{r}privacy.html">Política de privacidad</a>
        <a href="{r}terms.html">Términos de uso</a>
        <a href="{r}contact.html">Contacto</a>
      </nav>
    </div>
  </footer>
  <script src="{r}js/theme.js"></script>"""


def page_shell(title, description, canonical_path, depth, body, active="", extra_schema="",
               keywords="", body_class="", extra_scripts=""):
    r = rel(depth)
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
  {head(title, description, canonical_path, depth, extra_schema, keywords)}
</head>
<body class="{body_class}">
  {header_html(depth, active)}
  <main id="contenido">
    {body}
  </main>
  {footer_html(depth)}
  <script src="{r}js/utils.js"></script>
  {extra_scripts}
</body>
</html>
"""


def tool_schema(tool):
    return f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebApplication",
    "name": "{tool['name']}",
    "url": "{SITE_URL}/{tool['file']}",
    "applicationCategory": "UtilitiesApplication",
    "operatingSystem": "Any",
    "description": "{tool['desc']}",
    "offers": {{
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "USD"
    }}
  }}
  </script>"""


def write(path, content):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", path)
