# Checklist DiD (Difference-in-Differences)

Usado por el **Crítico Causal** para auditar diseños de diferencias en diferencias.

## Estrategia de Identificación
- [ ] Grupo de tratamiento definido y justificado
- [ ] Grupo de control definido y justificado
- [ ] Timing de tratamiento claro (fecha de apertura de estación, anuncio, construcción)
- [ ] Discusión de efectos de anticipación (anticipation effects, ¿se capitalizó antes del tratamiento?)

## Tendencias Paralelas (Parallel Trends)
- [ ] Test visual: gráfico de tendencias pre-tratamiento para tratados vs control
- [ ] Test formal: coeficientes pre-tratamiento no significativos en event study
- [ ] Event study plot con intervalos de confianza
- [ ] Discusión de por qué las tendencias serían paralelas en ausencia de tratamiento

## Adopción Escalonada (Staggered Treatment)
- [ ] Si hay múltiples periodos de tratamiento: identificar si hay sesgo por timing
- [ ] Goodman-Bacon decomposition o diagnóstico similar
- [ ] Estimador robusto considerado: Callaway-Sant'Anna, Sun-Abraham o Borusyak et al.
- [ ] Justificación de por qué el estimador TWFE es adecuado (si se usa)

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
