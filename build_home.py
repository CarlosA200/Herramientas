# -*- coding: utf-8 -*-
from build import TOOLS, icon, page_shell, write, SITE_URL

cards = []
for t in TOOLS:
    cards.append(f"""
      <a class="tool-card" href="{t['file']}">
        <span class="icon">{icon(t['icon'])}</span>
        <h2>{t['name']}</h2>
        <p>{t['short']}</p>
      </a>""")

body = f"""
    <section class="hero">
      <div class="wrap">
        <p class="eyebrow-free">Resultados en vivo, mientras escribes</p>
        <h1>Herramientas rápidas para tus números de cada día</h1>
        <p>Ocho calculadoras online, sin registro y sin descargas: porcentajes, monedas
        (con tasas de cambio reales y actualizadas), préstamos, unidades, IMC,
        contraseñas, edad y propinas. Todo funciona directamente en tu navegador.</p>
      </div>
    </section>

    <div class="wrap">
      <!-- ESPACIO PARA ANUNCIO ADSENSE - CABECERA -->
      <div class="ad-slot" data-size="leaderboard" aria-hidden="true">Espacio publicitario</div>

      <h2 style="margin-top:2rem;">Elige una herramienta</h2>
      <div class="tool-grid">{''.join(cards)}
      </div>

      <!-- ESPACIO PARA ANUNCIO ADSENSE - CONTENIDO -->
      <div class="ad-slot" data-size="rectangle" aria-hidden="true">Espacio publicitario</div>

      <section class="article">
        <h2>¿Por qué usar Herramientas Rápidas?</h2>
        <p>Reunimos en un solo lugar las calculadoras que más se necesitan en el día a día:
        desde resolver un porcentaje de descuento hasta estimar la cuota mensual de una
        hipoteca. Cada herramienta se ejecuta enteramente en tu navegador, así que tus datos
        nunca se envían a ningún servidor: la privacidad está garantizada porque los cálculos
        se hacen en tu propio dispositivo.</p>
        <p>El sitio funciona igual de bien en el celular, la tablet o la computadora, y
        puedes cambiar entre modo claro y modo oscuro según tu preferencia. Si tienes
        sugerencias sobre una nueva calculadora que te gustaría ver, escríbenos desde la
        página de <a href="contact.html">contacto</a>.</p>
      </section>
    </div>
"""

schema = f"""<script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "Herramientas Rápidas",
    "url": "{SITE_URL}/index.html"
  }}
  </script>"""

html = page_shell(
    title="Herramientas Rápidas | Calculadoras y conversores online gratis",
    description="Calculadoras y conversores online gratuitos: porcentajes, monedas, "
                 "préstamos, unidades, IMC, contraseñas, edad y propinas. Rápido y sin registro.",
    canonical_path="index.html",
    depth=0,
    body=body,
    active="index",
    extra_schema=schema,
    keywords="calculadoras online, herramientas gratis, conversor de unidades",
)
write("index.html", html)
