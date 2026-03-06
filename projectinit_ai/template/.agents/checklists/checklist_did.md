# Checklist DiD (Difference-in-Differences)

Usado por el **Crítico Causal** para auditar diseños de diferencias en diferencias.

## Estrategia de Identificación

- [ ] Grupo de tratamiento definido y justificado
- [ ] Grupo de control definido y justificado
- [ ] Timing de tratamiento claro (fecha de apertura de estación, anuncio, construcción)
- [ ] Discusión de efectos de anticipación (anticipation effects, ¿se capitalizó antes del tratamiento?)

## Tendencias Paralelas (Parallel Trends)

- [ ] Test visual: gráfico de tendencias pre-tratamiento para tratutilities vs control
- [ ] Test formal de *Pre-trends*: Ojo con el **Low Power** (Roth, 2022). Un test no significativo no significa que las tendencias sean paralelas. Discutir poder estadístico.
- [ ] Análisis de sensibilidad a violaciones de tendencias paralelas (Rambachan & Roth, 2023) "Honest DiD".
- [ ] Event study plot con intervalos de confianza uniformes
- [ ] Discusión explícita de la historia institucional que valida el supuesto de tendencias paralelas.

## Adopción Escalonada (Staggered Treatment)

- [ ] **Identificación Saturada (DDD):** Si existe un tercer nivel de variación (ej. Grupo), se debe presentar una tabla de Triple Diferencia (DDD) que muestre explícitamente la triple interacción y sus componentes (Referencia: `example_ddd_table.tex`).
- [ ] **Prueba de Robustez (Pillar):** Si la especificación DiD principal es sensible, presentar la tabla "Pillar" agotando outcomes y controles (Referencia: `example_pillar_table.tex`).
- [ ] Si hay múltiples periodos de tratamiento: identificar si hay sesgo por timing derivado del supuesto de homogeneidad de efectos.
- [ ] Diagnóstico del Teorema de **Goodman-Bacon**: reportar si existen *pesos negativos* (Negative Weights) usando controles ya tratutilities.
- [ ] Estimador robusto seleccionado si hay pesos negativos: Callaway-Sant'Anna, Sun-Abraham o Borusyak et al.
- [ ] Justificación de por qué el estimador TWFE clásico (OLS) es adecuado (solo si la adopción es simultánea).

## SUTVA y Spillovers

- [ ] Discusión de SUTVA (Stable Unit Treatment Value Assumption)
- [ ] Evaluación de spillovers espaciales (¿el tratamiento contamina al control?)
- [ ] Buffer de exclusión si aplica (ej. excluir propiedades 500m-1km de estación)
- [ ] Discusión de efectos de equilibrio general

## Especificación

- [ ] Efectos fijos de unidad y tiempo incluidos
- [ ] Errores estándar clustered al nivel apropiado (unidad de tratamiento)
- [ ] Covariables time-varying justificadas (evitar bad controls)

## Robustez

- [ ] Grupo de control placebo (unidades nunca tratadas en zona sin metro)
- [ ] Trimming temporal (excluir períodos muy lejanos)
- [ ] Heterogeneidad por subgrupos (tipo de propiedad, comuna, quintil)
- [ ] Sensibilidad a la definición de tratamiento/control

## Inferencia

- [ ] Número de clusters suficiente (regla: ≥ 30-50)
- [ ] Wild cluster bootstrap si pocos clusters
- [ ] Interpretación ATT explícita
