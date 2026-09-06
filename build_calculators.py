# -*- coding: utf-8 -*-
from build import TOOLS, page_shell, write, tool_schema, icon

TOOLS_BY_ID = {t["id"]: t for t in TOOLS}


def wrap_tool(tool_id, intro_p, panel_html, article_html):
    t = TOOLS_BY_ID[tool_id]
    body = f"""
    <div class="wrap narrow tool-page">
      <div class="intro">
        <span class="badge">Calculadora gratuita</span>
        <h1>{t['name']}</h1>
        <p>{intro_p}</p>
      </div>

      <!-- ESPACIO PARA ANUNCIO ADSENSE - ENCIMA DE LA HERRAMIENTA -->
      <div class="ad-slot" data-size="leaderboard" aria-hidden="true">Espacio publicitario</div>

      <div class="panel">
        {panel_html}
      </div>

      <!-- ESPACIO PARA ANUNCIO ADSENSE - ENTRE HERRAMIENTA Y ARTÍCULO -->
      <div class="ad-slot" data-size="rectangle" aria-hidden="true">Espacio publicitario</div>

      <section class="article">
        {article_html}
      </section>

      <!-- ESPACIO PARA ANUNCIO ADSENSE - FINAL DEL ARTÍCULO -->
      <div class="ad-slot" data-size="banner" aria-hidden="true">Espacio publicitario</div>
    </div>
"""
    return body


def build(tool_id, intro_p, panel_html, article_html, script_name):
    t = TOOLS_BY_ID[tool_id]
    body = wrap_tool(tool_id, intro_p, panel_html, article_html)
    html = page_shell(
        title=f"{t['name']} online gratis | Herramientas Rápidas",
        description=t["desc"],
        canonical_path=t["file"],
        depth=1,
        body=body,
        active="tools",
        extra_schema=tool_schema(t),
        keywords=t["keywords"],
        extra_scripts=f'<script src="../js/calc/{script_name}.js"></script>',
    )
    write(t["file"], html)


# ==================================================================
# 1. Porcentajes
# ==================================================================
build(
    "percentage",
    "Calcula el porcentaje de un número, aplica un aumento o descuento, o averigua "
    "la variación porcentual entre dos cifras.",
    """
        <form id="percentage-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="percentage-mode">Tipo de cálculo</label>
              <select id="percentage-mode">
                <option value="of">¿Cuánto es el X% de un número?</option>
                <option value="increase">Aumentar un número en X%</option>
                <option value="decrease">Descontar X% a un número</option>
                <option value="change">Variación porcentual entre dos números</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label id="label-a" for="percentage-a">Porcentaje (%)</label>
              <input type="text" inputmode="decimal" id="percentage-a" required placeholder="Ej. 15">
            </div>
            <div class="field">
              <label id="label-b" for="percentage-b">Del número</label>
              <input type="text" inputmode="decimal" id="percentage-b" required placeholder="Ej. 200">
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Calcular</button>
          </div>
        </form>
        <div class="readout" id="percentage-readout" role="status">
          <span class="label">Resultado</span>
          <span class="value" id="percentage-value">—</span>
          <p class="sub" id="percentage-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar la calculadora de porcentajes</h2>
        <p>Esta calculadora resuelve las cuatro operaciones con porcentajes más comunes.
        Primero elige el tipo de cálculo en el menú desplegable y luego completa los dos
        campos numéricos; el resultado aparece de inmediato al presionar "Calcular".</p>
        <p>La opción "¿Cuánto es el X% de un número?" es útil, por ejemplo, para saber
        cuánto representa una comisión o un impuesto sobre un monto determinado. La opción
        de aumento sirve para calcular incrementos de precio o de salario, mientras que la
        de descuento es ideal para calcular el precio final de un producto rebajado en una
        oferta o promoción.</p>
        <p>Por último, la variación porcentual compara dos valores —por ejemplo, las ventas
        de este mes frente al mes anterior— y expresa la diferencia como un porcentaje,
        indicando si hubo un aumento o una disminución. Esta calculadora se ejecuta
        completamente en tu navegador: los números que introduces no se envían a ningún
        servidor, por lo que puedes usarla con total privacidad las veces que necesites.</p>
    """,
    "percentage",
)

# ==================================================================
# 2. Monedas
# ==================================================================
build(
    "currency",
    "Convierte entre las principales divisas del mundo con tasas de cambio reales, "
    "actualizadas automáticamente.",
    """
        <form id="currency-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="currency-amount">Monto</label>
              <input type="text" inputmode="decimal" id="currency-amount" required placeholder="Ej. 100" value="100">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="currency-from">De</label>
              <select id="currency-from"></select>
            </div>
            <div class="field" style="flex:0 0 auto;align-self:flex-end;">
              <button class="btn btn-swap" type="button" id="currency-swap" aria-label="Intercambiar monedas">⇄</button>
            </div>
            <div class="field">
              <label for="currency-to">A</label>
              <select id="currency-to"></select>
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Convertir</button>
            <span class="rate-status" id="currency-rate-status" role="status">
              <span class="rate-dot" aria-hidden="true"></span>
              <span id="currency-rate-status-text">Consultando tasas en vivo…</span>
            </span>
          </div>
        </form>
        <div class="readout" id="currency-readout" role="status">
          <span class="label">Resultado en vivo</span>
          <span class="value" id="currency-value">—</span>
          <p class="sub" id="currency-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar el conversor de monedas</h2>
        <p>Escribe el monto, elige la moneda de origen y la de destino: el resultado se
        actualiza solo, sin necesidad de presionar ningún botón. El botón central con la
        flecha doble intercambia rápidamente las dos monedas seleccionadas.</p>
        <p>Las tasas de cambio se obtienen en tiempo real de un servicio público de tipos
        de cambio y se actualizan automáticamente durante tu visita, así que reflejan el
        valor del mercado del momento y no un número fijo escrito en el código. Cuando
        cargan por primera vez o si tu conexión falla, la herramienta guarda la última
        tasa conocida en tu propio navegador y sigue funcionando con ese último valor
        hasta que pueda volver a consultar el servicio.</p>
        <p>Es una herramienta práctica para hacerte una idea del valor de una cantidad en
        otra divisa, por ejemplo antes de un viaje o una compra internacional. Para
        transacciones reales o decisiones financieras importantes, verifica siempre la
        tasa vigente con tu banco o casa de cambio, ya que puede incluir un margen o
        comisión adicional sobre la tasa de mercado.</p>
    """,
    "currency",
)

# ==================================================================
# 3. Préstamos / hipotecas
# ==================================================================
build(
    "loan",
    "Calcula la cuota mensual, el interés total y un resumen de amortización de tu "
    "préstamo o hipoteca.",
    """
        <form id="loan-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="loan-amount">Monto del préstamo</label>
              <input type="text" inputmode="decimal" id="loan-amount" required placeholder="Ej. 150000">
            </div>
            <div class="field">
              <label for="loan-rate">Tasa de interés anual (%)</label>
              <input type="text" inputmode="decimal" id="loan-rate" required placeholder="Ej. 7.5">
            </div>
            <div class="field">
              <label for="loan-years">Plazo (años)</label>
              <input type="text" inputmode="decimal" id="loan-years" required placeholder="Ej. 20">
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Calcular cuota</button>
          </div>
        </form>
        <div class="readout" id="loan-readout" role="status">
          <span class="label">Cuota mensual estimada</span>
          <span class="value" id="loan-value">—</span>
          <p class="sub" id="loan-sub"></p>
        </div>
        <div id="loan-table-wrap" style="display:none;overflow-x:auto;">
          <table class="result-table">
            <thead>
              <tr><th>Mes</th><th>Cuota</th><th>Interés</th><th>Capital</th><th>Saldo restante</th></tr>
            </thead>
            <tbody id="loan-table-body"></tbody>
          </table>
        </div>
    """,
    """
        <h2>Cómo usar la calculadora de préstamos e hipotecas</h2>
        <p>Introduce el monto total del préstamo, la tasa de interés anual y el plazo en
        años, y la calculadora aplicará la fórmula estándar de amortización francesa
        (cuota fija) para mostrarte la cuota mensual, el interés total que pagarás durante
        toda la vida del préstamo y el total pagado al final.</p>
        <p>Debajo del resultado principal se muestra una tabla con el desglose de los
        primeros doce meses: cuánto de cada cuota corresponde a interés, cuánto a capital,
        y cuál es el saldo pendiente después de cada pago. Esto ayuda a visualizar cómo, al
        inicio del préstamo, una parte mayor de la cuota se destina a intereses.</p>
        <p>Esta calculadora es útil tanto para préstamos personales como para hipotecas de
        vivienda, y te permite comparar rápidamente distintos escenarios cambiando el
        plazo o la tasa de interés para ver cómo afectan la cuota mensual. Ten en cuenta
        que el resultado es una estimación basada en una tasa fija durante todo el plazo;
        no incluye seguros, comisiones ni otros cargos que tu entidad financiera pueda
        aplicar, por lo que la cuota real de tu préstamo puede variar ligeramente.</p>
    """,
    "loan",
)

# ==================================================================
# 4. Unidades
# ==================================================================
build(
    "units",
    "Convierte medidas de longitud, peso y temperatura entre los sistemas métrico e "
    "imperial.",
    """
        <form id="units-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="units-category">Categoría</label>
              <select id="units-category">
                <option value="length">Longitud</option>
                <option value="weight">Peso</option>
                <option value="temperature">Temperatura</option>
              </select>
            </div>
            <div class="field">
              <label for="units-amount">Valor</label>
              <input type="text" inputmode="decimal" id="units-amount" required placeholder="Ej. 10">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label for="units-from">De</label>
              <select id="units-from"></select>
            </div>
            <div class="field" style="flex:0 0 auto;align-self:flex-end;">
              <button class="btn" type="button" id="units-swap" aria-label="Intercambiar unidades">⇄</button>
            </div>
            <div class="field">
              <label for="units-to">A</label>
              <select id="units-to"></select>
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Convertir</button>
          </div>
        </form>
        <div class="readout" id="units-readout" role="status">
          <span class="label">Resultado</span>
          <span class="value" id="units-value">—</span>
          <p class="sub" id="units-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar el conversor de unidades</h2>
        <p>Selecciona primero la categoría que quieres convertir —longitud, peso o
        temperatura—, luego elige la unidad de origen y la unidad de destino, introduce el
        valor y presiona "Convertir". El menú de unidades se actualiza automáticamente
        según la categoría elegida.</p>
        <p>Para longitud, la herramienta cubre desde milímetros hasta millas, pasando por
        centímetros, metros, kilómetros, pulgadas, pies y yardas. Para peso, convierte
        entre miligramos, gramos, kilogramos, toneladas, libras y onzas. Y para
        temperatura, permite convertir entre grados Celsius, Fahrenheit y Kelvin usando
        las fórmulas estándar de conversión.</p>
        <p>Este tipo de conversor es especialmente útil cuando se combinan recetas,
        manuales o especificaciones técnicas que usan el sistema métrico con otras que
        usan el sistema imperial, algo muy común al comparar productos internacionales o
        seguir instrucciones de otro país. Todos los cálculos se hacen directamente en tu
        navegador de forma instantánea, sin necesidad de recargar la página.</p>
    """,
    "units",
)

# ==================================================================
# 5. IMC
# ==================================================================
build(
    "bmi",
    "Calcula tu índice de masa corporal (IMC) a partir de tu peso y estatura, en "
    "unidades métricas o imperiales.",
    """
        <form id="bmi-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="bmi-unit">Sistema de unidades</label>
              <select id="bmi-unit">
                <option value="metric">Métrico (kg / cm)</option>
                <option value="imperial">Imperial (lb / in)</option>
              </select>
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label id="bmi-weight-unit" for="bmi-weight">Peso (kg)</label>
              <input type="text" inputmode="decimal" id="bmi-weight" required placeholder="Ej. 70">
            </div>
            <div class="field">
              <label id="bmi-height-unit" for="bmi-height">Estatura (cm)</label>
              <input type="text" inputmode="decimal" id="bmi-height" required placeholder="Ej. 170">
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Calcular IMC</button>
          </div>
        </form>
        <div class="readout" id="bmi-readout" role="status">
          <span class="label">Tu IMC</span>
          <span class="value" id="bmi-value">—</span>
          <p class="sub" id="bmi-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar la calculadora de IMC</h2>
        <p>Elige el sistema de unidades que prefieras —métrico o imperial—, introduce tu
        peso y tu estatura, y presiona "Calcular IMC". La calculadora te mostrará tu
        índice de masa corporal junto con la categoría general en la que se ubica, según
        los rangos de referencia utilizados por la Organización Mundial de la Salud.</p>
        <p>El índice de masa corporal se calcula dividiendo el peso (en kilogramos) entre
        el cuadrado de la estatura (en metros). Es una fórmula sencilla y ampliamente
        utilizada porque solo requiere dos medidas, pero justamente por su simplicidad
        tiene limitaciones: no distingue entre masa muscular y masa grasa, por lo que
        puede no ser representativa en personas muy musculosas, deportistas de alto
        rendimiento, embarazadas, niños o adultos mayores.</p>
        <p>Por esta razón, el resultado de esta calculadora debe interpretarse únicamente
        como una referencia general y no como un diagnóstico médico. Si te preocupa tu
        peso o tu salud, lo más recomendable es consultar a un médico o nutricionista, que
        podrá evaluar tu caso considerando otros factores como la composición corporal, la
        edad y tus antecedentes de salud.</p>
    """,
    "bmi",
)

# ==================================================================
# 6. Contraseñas
# ==================================================================
build(
    "password",
    "Genera contraseñas aleatorias y seguras, con control sobre la longitud y los "
    "tipos de caracteres incluidos.",
    """
        <form id="password-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="password-length">Longitud: <span id="password-length-out">16</span> caracteres</label>
              <input type="range" id="password-length" min="6" max="64" value="16">
            </div>
          </div>
          <div class="field-row">
            <div class="field">
              <label><input type="checkbox" id="opt-lower" checked> Minúsculas (a-z)</label>
            </div>
            <div class="field">
              <label><input type="checkbox" id="opt-upper" checked> Mayúsculas (A-Z)</label>
            </div>
            <div class="field">
              <label><input type="checkbox" id="opt-numbers" checked> Números (0-9)</label>
            </div>
            <div class="field">
              <label><input type="checkbox" id="opt-symbols"> Símbolos (!@#...)</label>
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Generar contraseña</button>
          </div>
        </form>
        <div class="readout" id="password-readout" role="status">
          <span class="label">Contraseña generada</span>
          <span class="value mono" id="password-value" style="font-size:1.3rem;word-break:break-all;">—</span>
          <p class="sub" id="password-sub"></p>
          <div class="btn-row" style="margin-top:.75rem;">
            <button class="btn" type="button" id="password-copy">Copiar</button>
          </div>
        </div>
    """,
    """
        <h2>Cómo usar el generador de contraseñas seguras</h2>
        <p>Mueve el control deslizante para elegir la longitud de la contraseña —cuanto
        más larga, más segura será— y marca los tipos de caracteres que quieres incluir:
        minúsculas, mayúsculas, números y símbolos. Presiona "Generar contraseña" para
        crear una combinación aleatoria y usa el botón "Copiar" para llevarla al
        portapapeles.</p>
        <p>Esta herramienta utiliza la API criptográfica segura del navegador
        (<code>crypto.getRandomValues</code>) en lugar de un generador de números
        pseudoaleatorios simple, lo que produce contraseñas mucho más difíciles de
        predecir. Además, se asegura de incluir al menos un carácter de cada tipo
        seleccionado antes de completar el resto de la contraseña de forma aleatoria.</p>
        <p>Junto al resultado se muestra una estimación de la fortaleza de la contraseña
        en bits de entropía, calculada a partir de la longitud y la variedad de
        caracteres utilizados. En general, se recomienda usar contraseñas de al menos 12
        a 16 caracteres, combinando varios tipos de carácter, y utilizar una contraseña
        distinta para cada servicio importante. Ninguna contraseña generada aquí se
        almacena ni se envía a ningún servidor: todo el proceso ocurre en tu navegador.</p>
    """,
    "password",
)

# ==================================================================
# 7. Edad
# ==================================================================
build(
    "age",
    "Calcula tu edad exacta en años, meses y días a partir de tu fecha de nacimiento.",
    """
        <form id="age-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="age-dob">Fecha de nacimiento</label>
              <input type="date" id="age-dob" required>
            </div>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Calcular edad</button>
          </div>
        </form>
        <div class="readout" id="age-readout" role="status">
          <span class="label">Tu edad</span>
          <span class="value" id="age-value">—</span>
          <p class="sub" id="age-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar la calculadora de edad</h2>
        <p>Selecciona tu fecha de nacimiento en el campo de calendario y presiona
        "Calcular edad". La herramienta compara esa fecha con la fecha actual y calcula tu
        edad exacta en años completos, además de los meses y días adicionales desde tu
        último cumpleaños.</p>
        <p>El cálculo tiene en cuenta la duración real de cada mes —incluyendo los años
        bisiestos— para que el resultado en meses y días sea preciso, y no una simple
        aproximación. Además, la calculadora te indica cuántos días faltan exactamente
        para tu próximo cumpleaños, algo útil si quieres planificar una celebración con
        anticipación.</p>
        <p>Esta herramienta es útil no solo para saber tu propia edad exacta, sino también
        para calcular la edad de otra persona, la antigüedad de un documento o cuánto
        tiempo ha pasado desde una fecha determinada. Todo el cálculo se realiza en tu
        navegador usando el reloj de tu propio dispositivo, por lo que ningún dato de
        fecha de nacimiento se envía ni se guarda en ningún servidor externo.</p>
    """,
    "age",
)

# ==================================================================
# 8. Propinas
# ==================================================================
build(
    "tip",
    "Calcula cuánto dar de propina y cuánto le corresponde pagar a cada persona del "
    "grupo.",
    """
        <form id="tip-form" novalidate>
          <div class="field-row">
            <div class="field">
              <label for="tip-bill">Total de la cuenta</label>
              <input type="text" inputmode="decimal" id="tip-bill" required placeholder="Ej. 50">
            </div>
            <div class="field">
              <label for="tip-percent">Propina (%)</label>
              <input type="text" inputmode="decimal" id="tip-percent" required placeholder="Ej. 10" value="10">
            </div>
            <div class="field">
              <label for="tip-people">Número de personas</label>
              <input type="text" inputmode="numeric" id="tip-people" required placeholder="Ej. 4" value="1">
            </div>
          </div>
          <div class="btn-row" style="margin-bottom:1rem;">
            <button class="btn" type="button" data-tip-quick="10">10%</button>
            <button class="btn" type="button" data-tip-quick="15">15%</button>
            <button class="btn" type="button" data-tip-quick="20">20%</button>
          </div>
          <div class="btn-row">
            <button class="btn" type="submit">Calcular propina</button>
          </div>
        </form>
        <div class="readout" id="tip-readout" role="status">
          <span class="label">Cada persona paga</span>
          <span class="value" id="tip-value">—</span>
          <p class="sub" id="tip-sub"></p>
        </div>
    """,
    """
        <h2>Cómo usar la calculadora de propinas</h2>
        <p>Introduce el total de la cuenta, el porcentaje de propina que deseas dejar —o
        usa uno de los botones rápidos de 10%, 15% o 20%— y el número de personas entre
        las que se dividirá el pago. Al presionar "Calcular propina", la herramienta
        muestra cuánto le corresponde pagar a cada persona, incluyendo su parte de la
        propina.</p>
        <p>El resultado detallado también indica el monto total de la propina, cuánto
        representa esa propina por persona, y el total general de la cuenta ya incluida
        la propina. Esto es especialmente útil en restaurantes o salidas grupales donde se
        quiere dividir el gasto de forma justa y transparente entre todos los
        comensales.</p>
        <p>El porcentaje de propina habitual varía según el país y el tipo de servicio,
        pero suele situarse entre el 10% y el 20% del total de la cuenta en muchos
        lugares. Esta calculadora te permite ajustar libremente ese porcentaje según la
        costumbre local o la calidad del servicio recibido, y ver de inmediato cómo cambia
        el monto que le toca pagar a cada persona del grupo.</p>
    """,
    "tip",
)

print("Calculadoras generadas correctamente.")
