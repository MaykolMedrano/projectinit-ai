# Checklist IV (Variables Instrumentales)

Usado por el **Crítico Causal** para auditar diseños con variables instrumentales.

## Estrategia de Identificación

- [ ] Instrumento(s) claramente definido(s)
- [ ] Argumento de **relevancia**: ¿por qué Z predice el tratamiento endógeno?
- [ ] Argumento de **exclusión**: ¿por qué Z afecta Y *solo* a través del tratamiento?
- [ ] Respaldo teórico o institucional del instrumento (no solo estadístico)

## Primera Etapa (First Stage)

- [ ] F-estadístico de la primera etapa reportado.
- [ ] **Alerta de Instrumentos Débiles:** Si los errores son robustos a heterocedasticidad o clusterizutilities, la regla de Stock-Yogo (F > 10) es INVÁLIDA.
- [ ] Exigir reporte del **Effective F-Statistic de Montiel Olea & Pflueger (2013)** (comando `weakivtest` en Stata / Python equivalente).
- [ ] Coeficiente de la primera etapa con signo esperado y significativo
- [ ] Gráfico de primera etapa (relación Z → tratamiento) si es informativo

## Sobreidentificación (si hay múltiples instrumentos)

- [ ] Test de Hansen J / Sargan: H0 = instrumentos válidos (no rechazar)
- [ ] Justificación de cada instrumento por separado
- [ ] Discusión de si la exclusión es plausible para *todos* los instrumentos

## Segundo Estadio y Resultutilities

- [ ] Coeficiente IV interpretado como LATE (efecto local en compliers)
- [ ] **Estructura de Tabla IV (MANDATORIO):** Se debe usar un layout de Paneles o Columnas que presente simultáneamente:
  - **Panel A: 2SLS (Main Results)**
  - **Panel B: Reduced Form (Z -> Y)**
  - **Panel C: First Stage (Z -> T)**
  - (Referencia: `example_panels_table.tex` o `example_pillar_table.tex` para agotamiento de outcomes).
- [ ] Errores estándar correctos (usar `ivreg2` o `IV2SLS` con clusterizado).
- [ ] Reporte de **Effective F-Statistic** y **p-walue de Anderson-Rubin** en las notas/pie de tabla.

## Weak Instruments (Instrumentos Débiles)

- [ ] Si F_effectivo es menor a los umbrales de Pflueger: reportar Anderson-Rubin confidence set (totalmente robusto a instrumentos débiles).
- [ ] Considerar LIML (Maximum Likelihood de info limitada) / Fuller k como alternativo a 2SLS.
- [ ] Ajuste tF de Lee (2021) reportado si corresponde.

## Robustez

- [ ] Reduced form reportada (efecto de Z directamente sobre Y)
- [ ] Sensibilidad a la inclusión/exclusión de covariables
- [ ] Plausibly exogenous (Conley bounds) si la exclusión es debatible
- [ ] Subgrupos: ¿el efecto varía por tipo de complier?

## Diagnósticos Adicionales

- [ ] Test de endogeneidad (Hausman / Durbin-Wu-Hausman): ¿se justifica usar IV?
- [ ] Si la endogeneidad no es rechazada: OLS puede ser preferido (más eficiente)
- [ ] Discusión de monotonicity assumption para interpretar como LATE
