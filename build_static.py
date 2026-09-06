# -*- coding: utf-8 -*-
from build import page_shell, write

# ---------------- Acerca de ----------------
about_body = """
    <div class="wrap narrow page-content">
      <h1>Acerca de Herramientas Rápidas</h1>
      <p>Herramientas Rápidas nació de una idea simple: reunir en un mismo sitio las
      calculadoras que la gente busca todos los días en Google, sin anuncios invasivos,
      sin registros y sin descargas de aplicaciones.</p>

      <h2>Nuestra misión</h2>
      <p>Creemos que resolver un cálculo cotidiano —una propina, un porcentaje de
      descuento, la cuota de un préstamo— no debería requerir instalar una app ni crear
      una cuenta. Por eso construimos herramientas ligeras, rápidas y que funcionan
      directamente en el navegador, tanto en el celular como en la computadora.</p>

      <h2>Cómo funcionan las calculadoras</h2>
      <p>Todas las calculadoras del sitio se ejecutan con JavaScript en tu propio
      dispositivo. Esto significa que los números que introduces —tu peso, tu salario,
      el monto de un préstamo— nunca se envían a ningún servidor externo. El cálculo
      ocurre por completo en tu navegador y el resultado se actualiza al instante,
      mientras escribes.</p>
      <p>La única excepción es el conversor de monedas, que consulta un servicio público
      de tipos de cambio para traer la tasa del momento. Esa consulta solo pide la tasa
      de cambio general; no envía el monto que escribiste ni ningún otro dato tuyo.</p>

      <h2>Un proyecto en constante mejora</h2>
      <p>Seguimos agregando nuevas herramientas y afinando las existentes según los
      comentarios de las personas que las usan. Si tienes una idea para una nueva
      calculadora, o encuentras un error en alguna de ellas, nos encantaría saberlo a
      través de la <a href="contact.html">página de contacto</a>.</p>
    </div>
"""
write("about.html", page_shell(
    title="Acerca de | Herramientas Rápidas",
    description="Conoce el proyecto Herramientas Rápidas: calculadoras online gratuitas, "
                 "sin registro, que funcionan directamente en tu navegador.",
    canonical_path="about.html",
    depth=0,
    body=about_body,
    active="about",
))

# ---------------- Contacto ----------------
contact_body = """
    <div class="wrap narrow page-content">
      <h1>Contacto</h1>
      <p>¿Tienes una pregunta, una sugerencia de nueva calculadora o encontraste un error?
      Escríbenos con el formulario de abajo o directamente a
      <a href="mailto:contacto@herramientas-rapidas.example.com">contacto@herramientas-rapidas.example.com</a>.</p>

      <!-- Formulario sin backend propio: se envía mediante Formspree.
           Reemplaza TU_ID_DE_FORMULARIO por el ID real de tu cuenta de Formspree. -->
      <form class="contact-form" action="https://formspree.io/f/TU_ID_DE_FORMULARIO" method="POST">
        <div>
          <label for="name">Nombre</label><br>
          <input type="text" id="name" name="name" required maxlength="120" autocomplete="name">
        </div>
        <div>
          <label for="email">Correo electrónico</label><br>
          <input type="email" id="email" name="email" required maxlength="200" autocomplete="email">
        </div>
        <div>
          <label for="message">Mensaje</label><br>
          <textarea id="message" name="message" rows="6" required maxlength="2000"></textarea>
        </div>
        <button class="btn" type="submit">Enviar mensaje</button>
      </form>

      <p style="margin-top:1.5rem;font-size:.9rem;color:var(--ink-soft);">
        Alternativamente, puedes escribirnos directamente desde tu cliente de correo con el enlace
        <a href="mailto:contacto@herramientas-rapidas.example.com?subject=Consulta%20desde%20Herramientas%20Rapidas">mailto</a>.
      </p>
    </div>
"""
write("contact.html", page_shell(
    title="Contacto | Herramientas Rápidas",
    description="Ponte en contacto con el equipo de Herramientas Rápidas para dudas, "
                 "sugerencias o reportar un error en alguna calculadora.",
    canonical_path="contact.html",
    depth=0,
    body=contact_body,
    active="contact",
))

# ---------------- Privacidad ----------------
privacy_body = """
    <div class="wrap narrow page-content">
      <h1>Política de privacidad</h1>
      <p><em>Última actualización: 6 de septiembre de 2026.</em></p>

      <p>En Herramientas Rápidas ("nosotros", "el sitio") respetamos tu privacidad y nos
      comprometemos a proteger los datos personales que puedas compartir al usar nuestras
      calculadoras y páginas. Esta política explica qué información se recopila, cómo se
      utiliza y qué opciones tienes al respecto.</p>

      <h2>1. Información que no recopilamos</h2>
      <p>Las calculadoras de este sitio (porcentajes, monedas, préstamos, unidades, IMC,
      contraseñas, edad y propinas) se ejecutan por completo en tu navegador mediante
      JavaScript. Los valores que introduces en ellas —montos, fechas, peso, estatura,
      etc.— no se envían ni almacenan en ningún servidor: el cálculo ocurre localmente en
      tu dispositivo.</p>
      <p>El conversor de monedas consulta, además, un servicio público externo de tipos de
      cambio para mostrar la tasa del momento. Esta consulta solo solicita la tabla
      general de tasas; no incluye el monto ni las monedas que elegiste. La última tasa
      recibida se guarda en el almacenamiento local de tu propio navegador para que la
      herramienta siga funcionando si te quedas sin conexión.</p>

      <h2>2. Formulario de contacto</h2>
      <p>Si usas el formulario de la página de <a href="contact.html">contacto</a>, el
      nombre, correo electrónico y mensaje que escribas se envían a través de un proveedor
      externo de formularios (Formspree) únicamente para poder responderte. Esta
      información no se utiliza con fines publicitarios ni se comparte con terceros más
      allá de lo necesario para gestionar tu consulta.</p>

      <h2>3. Cookies y almacenamiento local</h2>
      <p>Utilizamos el almacenamiento local del navegador (localStorage) para recordar tu
      preferencia de modo claro u oscuro. Este dato se guarda únicamente en tu dispositivo
      y no se transmite a ningún servidor.</p>
      <p>Además, este sitio puede utilizar cookies propias y de terceros con fines de
      análisis de tráfico y publicidad, como se detalla a continuación.</p>

      <h2>4. Google Analytics</h2>
      <p>Podemos utilizar Google Analytics para entender cómo se usa el sitio (páginas
      visitadas, tiempo de permanencia, dispositivo, ubicación aproximada). Google
      Analytics utiliza cookies propias para recopilar esta información de forma anónima
      y agregada. Puedes obtener más información sobre cómo Google trata estos datos en la
      <a href="https://policies.google.com/privacy" rel="noopener" target="_blank">política de privacidad de Google</a>.</p>

      <h2>5. Google AdSense y publicidad</h2>
      <p>Este sitio puede mostrar anuncios a través de Google AdSense. Google, como
      proveedor externo, utiliza cookies para publicar anuncios basados en las visitas
      previas de un usuario a este y otros sitios web. El uso de cookies publicitarias por
      parte de Google permite mostrar anuncios relevantes a los usuarios.</p>
      <p>Puedes inhabilitar el uso de la cookie de publicidad personalizada de Google
      visitando la
      <a href="https://adssettings.google.com" rel="noopener" target="_blank">Configuración de anuncios de Google</a>.
      También puedes consultar
      <a href="https://www.aboutads.info" rel="noopener" target="_blank">www.aboutads.info</a>
      para más información sobre cómo inhabilitar cookies de publicidad de otros proveedores.</p>

      <h2>6. Tus opciones sobre las cookies</h2>
      <p>La mayoría de los navegadores te permiten rechazar o eliminar cookies desde su
      configuración. Ten en cuenta que bloquear todas las cookies puede afectar el
      funcionamiento de algunas funciones del sitio, como la preferencia de tema.</p>

      <h2>7. Enlaces a otros sitios</h2>
      <p>Este sitio puede incluir enlaces a otras páginas web. No nos hacemos
      responsables de las prácticas de privacidad de esos sitios externos; te
      recomendamos leer su propia política de privacidad.</p>

      <h2>8. Cambios a esta política</h2>
      <p>Podemos actualizar esta política de privacidad ocasionalmente para reflejar
      cambios legales o en nuestras prácticas. Publicaremos cualquier cambio en esta
      misma página junto con la fecha de última actualización.</p>

      <h2>9. Contacto</h2>
      <p>Si tienes preguntas sobre esta política de privacidad, puedes escribirnos desde la
      <a href="contact.html">página de contacto</a>.</p>
    </div>
"""
write("privacy.html", page_shell(
    title="Política de privacidad | Herramientas Rápidas",
    description="Política de privacidad de Herramientas Rápidas: uso de cookies, Google "
                 "Analytics, Google AdSense y tratamiento de datos personales.",
    canonical_path="privacy.html",
    depth=0,
    body=privacy_body,
    active="",
))

# ---------------- Términos ----------------
terms_body = """
    <div class="wrap narrow page-content">
      <h1>Términos de uso</h1>
      <p><em>Última actualización: 6 de septiembre de 2026.</em></p>

      <p>Al acceder y utilizar Herramientas Rápidas aceptas los siguientes términos de
      uso. Si no estás de acuerdo con alguno de ellos, te pedimos no utilizar el sitio.</p>

      <h2>1. Uso del sitio</h2>
      <p>Herramientas Rápidas ofrece calculadoras y conversores de uso gratuito con fines
      informativos y de conveniencia. Puedes usar el sitio para fines personales o
      profesionales, siempre que sea de manera lícita y sin intentar dañar su
      funcionamiento.</p>

      <h2>2. Exactitud de los resultados</h2>
      <p>Nos esforzamos por que los cálculos de cada herramienta sean precisos, pero no
      garantizamos que estén libres de errores en el cien por ciento de los casos. Los
      resultados se ofrecen "tal cual" y con fines orientativos; no deben considerarse
      asesoría financiera, médica, legal ni de ningún otro tipo profesional.</p>
      <p>Por ejemplo, los resultados de la calculadora de préstamos, de IMC o de
      propinas son aproximaciones basadas en los datos que introduces y en fórmulas
      estándar; para decisiones importantes, te recomendamos confirmar los cálculos con un
      profesional calificado (asesor financiero, médico, contador, etc.).</p>

      <h2>3. Propiedad intelectual</h2>
      <p>El diseño, el código y los textos de este sitio son propiedad de Herramientas
      Rápidas, salvo donde se indique lo contrario. No está permitido copiar o
      redistribuir el contenido del sitio sin autorización.</p>

      <h2>4. Publicidad</h2>
      <p>Este sitio puede mostrar anuncios de terceros, incluyendo Google AdSense. No nos
      hacemos responsables del contenido de los anuncios mostrados por estas redes
      publicitarias.</p>

      <h2>5. Limitación de responsabilidad</h2>
      <p>En la medida permitida por la ley, Herramientas Rápidas no será responsable de
      ningún daño directo o indirecto derivado del uso, o la imposibilidad de uso, de las
      calculadoras y del contenido de este sitio.</p>

      <h2>6. Modificaciones</h2>
      <p>Podemos modificar estos términos de uso en cualquier momento. El uso continuado
      del sitio después de publicados los cambios implica la aceptación de los nuevos
      términos.</p>

      <h2>7. Contacto</h2>
      <p>Para cualquier consulta sobre estos términos, puedes escribirnos desde la
      <a href="contact.html">página de contacto</a>.</p>
    </div>
"""
write("terms.html", page_shell(
    title="Términos de uso | Herramientas Rápidas",
    description="Términos y condiciones de uso del sitio Herramientas Rápidas y sus "
                 "calculadoras online gratuitas.",
    canonical_path="terms.html",
    depth=0,
    body=terms_body,
    active="",
))
