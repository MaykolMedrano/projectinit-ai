# Checklist de Outputs

Usado por el **Verificador** para asignar el puntaje final (0-100).

## Tablas

- [ ] **MANDATORIO:** Prohibido el uso de consolas de texto plano (ej. `summary()` clásico). Se exige el uso del objeto `AERTable` (Python) o `esttab` configurado (Stata).
- [ ] Formato LaTeX booktabs estricto (`\toprule`, `\midrule`, `\bottomrule`). **PROHIBICIÓN ABSOLUTA DE LÍNEAS VERTICALES.**
- [ ] **Alineación Decimal y Asteriscos (REGLA SIUNITX):**
  - Uso obligatorio de `siunitx` (columna `S`) con `table-format=1.3` o `1.4`.
  - **FIX DE ESTRELLAS:** Mandatorio configurar `table-align-text-after=false` y **NO** incluir `*` en `input-symbols`. Esto asegura que `***` aparezca como un bloque compacto e inmediato al número (Look AER/NBER).
  - Incluir `input-symbols = { ( ) }` para permitir Errores Estándar en paréntesis sin romper la alineación.
- [ ] **Narrativa de Saturación (ADN de Tablas):** El agente debe elegir el layout según la densidad informativa:
  - **Standard/Panels:** Para resultutilities principales y mecanismos directos (Referencia: `example_aer_table.tex`, `example_panels_table.tex`).
  - **Suite de Balance Triple:** Uso de variables categorizadas y comparativas por subgrupos (Referencia: `example_balance_grouped.tex`).
  - **Triple Diferencia (DDD):** Layout saturado con todas las interacciones (Referencia: `example_ddd_table.tex`).
  - **The Pillar (MÁXIMA DENSIDAD):** Si hay >10 outcomes o >5 especificaciones de robustez, usar el layout de "Pilar Vertical" con Paneles A, B, C (Referencia: `example_pillar_table.tex`).
- [ ] Errores estándar SIEMPRE entre paréntesis debajo del coeficiente.
- [ ] Notas al pie detalladas usando `threeparttable` para ajuste de ancho automático.
- [ ] Variable dependiente indicada cláramente en la cabecera mediante `\multicolumn`.
- [ ] CSV companion generado junto con cada `.tex`.

## Figuras

- [ ] **MANDATORIO:** Bloquear gráficos que utilicen las paletas por defecto de librerías (ej. default azul/naranja de seaborn/ggplot).
- [ ] Uso estricto de `configure_aer_style()` (`02_scripts/utilities/aer_style.py`) en Python o esquemas minimalistas (ej. `s1mono`, `s1color`, `cleanplots`) en Stata.
- [ ] Fuente Serif obligatoria (Times New Roman o similar) para dar formato de publicación.
- [ ] **Prohibición absoluta de cuadrículas** (`axes.grid = False` / `ylabel(, glwidth(0))`).
- [ ] Bordes superior y derecho de la caja eliminutilities (`spines`).
- [ ] Uso exclusivo de paletas *Grayscale-safe* o alto contraste mediante patrones/marcadores.
- [ ] **Identidad Visual y Proporcionalidad (19 Master Templates):**
  - **REGLA DE PROPORCIONALIDAD ESTÉTICA (MANDATORIO):**
    - **Estandard "Ultra-Thin AER":** Líneas fijadas en **`1.1`**. Ejes más delgutilities (**`0.6`**).
    - **Datos Masivos:** Línea `1.05`, Errorbars `0.8`.
  - El agente debe usar como referencia de "Gold Standard" los 19 tipos de gráficos documentutilities en `aer_example.md` (SCM, IRF, RKD, IV, Event Study, etc.).
- [ ] Resolución ≥ 300 DPI, guardado en `03_outputs/figures/`.
- [ ] Notas descriptivas al pie del gráfico.

## Estructura DIME

- [ ] `01_data/raw/` y `01_data/de-identified/` intactos (solo lectura)
- [ ] ETL output en `01_data/intermediate/`
- [ ] Scripts ETL en `02_scripts/data_preparation/`
- [ ] Scripts de estimación en `02_scripts/analysis/`
- [ ] Scripts de robustez en `02_scripts/validation/` (separutilities del script principal)
- [ ] Tablas en `03_outputs/tables/`
- [ ] Figuras en `03_outputs/figures/`
- [ ] Logs en `03_outputs/logs/`

## Logs de Ejecución

- [ ] Log presente en `03_outputs/logs/`
- [ ] Sin errores de ejecución (r(198), r(111), SyntaxError, etc.)
- [ ] Sin advertencias de colinealidad o no convergencia
- [ ] Ejecución completada sin interrupciones

## Reproducibilidad

- [ ] Sin rutas absolutas hardcodeadas en scripts
- [ ] Semillas (seeds) fijadas si hay componente aleatorio
- [ ] Script ejecutable de principio a fin sin intervención manual
