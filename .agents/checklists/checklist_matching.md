# Checklist Matching / PSM (Propensity Score Matching)

Usado por el **Crítico Causal** para auditar diseños basados en matching y propensity score.

## Estrategia de Identificación
- [ ] Supuesto de **selección en observables** (CIA / unconfoundedness) discutido
- [ ] Justificación de por qué no hay confounders omitidos no observables
- [ ] Variables de matching/propensity elegidas con criterio teórico (no solo estadístico)

## Estimación del Propensity Score
- [ ] Modelo de propensity especificado (logit/probit)
- [ ] Variables incluidas justificadas (pre-tratamiento, no post-tratamiento)
- [ ] Propensity score estimado correctamente (no overfitting con demasiadas variables)

## Soporte Común (Common Support)
- [ ] Gráfico de distribución del propensity score para tratados y controles
- [ ] Región de soporte común identificada y reportada
- [ ] Observaciones fuera del soporte común excluidas con criterio explícito
- [ ] Porcentaje de observaciones perdidas por trimming reportado

## Balance Post-Matching
- [ ] Tabla de balance: medias y diferencias estandarizadas antes y después del matching
- [ ] Diferencias estandarizadas < 0.1 (o < 0.25 como máximo tolerable)
- [ ] Razón de varianzas cercana a 1 para cada covariable
- [ ] Test formal de balance (t-test por variable, test conjunto)

## Método de Matching
- [ ] Algoritmo especificado: nearest-neighbor, kernel, caliper, radius, CEM
- [ ] Con o sin reemplazo: justificado
- [ ] Caliper definido si se usa (regla: 0.2 × SD del propensity score)
- [ ] Número de matches (k) reportado si nearest-neighbor

## Estimación del Efecto
- [ ] ATT vs ATE claramente distinguidos
- [ ] Errores estándar correctos (bootstrap si necesario, Abadie-Imbens para NN matching)
- [ ] Efecto estimado interpretado condicionado al soporte común

## Robustez
- [ ] Rosenbaum bounds (sensibilidad a confounders ocultos)
- [ ] Gamma crítico reportado: ¿cuánto sesgo oculto se necesita para anular el efecto?
- [ ] Variación del caliper o número de matches
- [ ] Matching exacto en variables clave como alternativa
- [ ] Comparación con regresión OLS con mismos controles

## Diagnósticos
- [ ] ¿El matching redujo sustancialmente el sesgo vs la muestra completa?
- [ ] ¿Hay suficientes controles para el matching (ratio tratados/controles)?
- [ ] Discusión de limitaciones del supuesto CIA en el contexto específico
