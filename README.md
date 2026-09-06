# Herramientas Rápidas — sitio de calculadoras online

Sitio estático (HTML + CSS + JS puro, sin build step) listo para publicar en
GitHub Pages o Netlify.

## Estructura

```
/index.html                Página de inicio con las 8 tarjetas de herramientas
/about.html                Acerca de
/contact.html              Formulario de contacto (Formspree) + mailto
/privacy.html              Política de privacidad (cookies, Analytics, AdSense)
/terms.html                Términos de uso
/calculators/*.html        Las 8 calculadoras, una página por herramienta
/css/style.css             Hoja de estilos única (tokens de diseño + modo claro/oscuro)
/js/theme.js               Alternancia de tema con localStorage
/js/utils.js                Utilidades compartidas (sanitización, formato de números)
/js/calc/*.js               Lógica de cada calculadora (un archivo por herramienta)
/img/favicon.svg            Ícono del sitio
/img/og-cover.svg           Imagen de vista previa para redes sociales (placeholder)
/sitemap.xml                 Mapa del sitio para buscadores
/robots.txt                  Reglas de rastreo, apunta al sitemap
/build.py, build_home.py,   Scripts Python usados para GENERAR las páginas HTML.
build_static.py,            No se suben al hosting: son solo la herramienta de
build_calculators.py        construcción. El sitio final ya está generado en los
                             archivos .html de este mismo paquete.
```

## Publicar el sitio

**No necesitas ejecutar nada.** Las páginas HTML ya están generadas. Solo sube
el contenido de esta carpeta (menos los archivos `.py` y este `README.md`, que
son opcionales) a GitHub Pages o Netlify:

- **GitHub Pages:** crea un repositorio, sube estos archivos a la raíz (o a
  `/docs`), y activa Pages en Settings → Pages.
- **Netlify:** arrastra la carpeta al panel de Netlify o conéctala a un
  repositorio; no requiere ningún comando de build (déjalo vacío) y el
  directorio de publicación es la raíz del proyecto.

## Antes de publicar en producción

1. **Dominio real:** reemplaza `https://herramientas-rapidas.example.com` por
   tu dominio real en `build.py` (variable `SITE_URL`), en `sitemap.xml` y en
   `robots.txt`. Si cambias `build.py`, vuelve a ejecutar los tres scripts
   `build_*.py` con `python3` para regenerar los HTML.
2. **Formulario de contacto:** en `contact.html`, reemplaza
   `TU_ID_DE_FORMULARIO` por tu ID real de [Formspree](https://formspree.io)
   (o el servicio de formularios sin backend que prefieras).
3. **Google AdSense:** busca los comentarios
   `<!-- ESPACIO PARA ANUNCIO ADSENSE ... -->` en cada página y pega ahí tu
   bloque de anuncio de AdSense. También deberás añadir el script de
   verificación de AdSense en el `<head>` de cada página una vez que tu cuenta
   esté aprobada, y agregar `https://pagead2.googlesyndication.com` (ya
   incluido) a la política CSP si tu snippet usa otros subdominios.
4. **Google Analytics:** agrega tu snippet de Google Analytics/GA4 antes del
   cierre de `</head>` en cada página (o mediante Google Tag Manager).
5. **Imagen Open Graph:** `img/og-cover.svg` es un marcador de posición.
   Sustitúyelo por una imagen PNG/JPG de 1200×630 px con tu propio diseño y
   actualiza la referencia `og:image` en `build.py` (o directamente en cada
   HTML) a la nueva ruta, ya que algunas redes sociales no renderizan bien
   imágenes SVG en las vistas previas de enlaces.
6. **Tasas de cambio:** en `js/calc/currency.js`, actualiza el objeto
   `RATES_USD` con tasas de cambio reales o conéctalo a una API de tipo de
   cambio si quieres tasas en vivo.

## Seguridad

- Todos los inputs numéricos se validan con `HR.toSafeNumber()` antes de
  usarse; nunca se usa `eval()`.
- Los resultados se escriben con `textContent` (nunca `innerHTML`) para
  evitar inyección de HTML/JS.
- Cada página incluye una cabecera `Content-Security-Policy` básica que
  restringe los orígenes de scripts, estilos e imágenes.
