# Checklist IV (Variables Instrumentales)

Usado por el **Crítico Causal** para auditar diseños con variables instrumentales.

## Estrategia de Identificación
- [ ] Instrumento(s) claramente definido(s)
- [ ] Argumento de **relevancia**: ¿por qué Z predice el tratamiento endógeno?
- [ ] Argumento de **exclusión**: ¿por qué Z afecta Y *solo* a través del tratamiento?
- [ ] Respaldo teórico o institucional del instrumento (no solo estadístico)

## Primera Etapa (First Stage)
- [ ] F-estadístico de la primera etapa reportado
- [ ] Regla de oro: F > 10 (Stock & Yogo, 2005)
- [ ] Kleibergen-Paap rk Wald F-stat si errores clustered o heteroscedásticos
- [ ] Coeficiente de la primera etapa con signo esperado y significativo
- [ ] Gráfico de primera etapa (relación Z → tratamiento) si es informativo

## Sobreidentificación (si hay múltiples instrumentos)
- [ ] Test de Hansen J / Sargan: H0 = instrumentos válidos (no rechazar)
- [ ] Justificación de cada instrumento por separado
- [ ] Discusión de si la exclusión es plausible para *todos* los instrumentos

## Segundo Estadio y Resultados
- [ ] Coeficiente IV interpretado como LATE (efecto local en compliers)
- [ ] Comparación IV vs OLS: ¿IV mayor que OLS? Discutir por qué (sesgo de atenuación, heterogeneidad)
- [ ] Errores estándar correctos (no usar SEs del second stage manual, usar `ivreg2` o `IV2SLS`)

## Weak Instruments (Instrumentos Débiles)
- [ ] Si F < 10: reportar Anderson-Rubin confidence set (robusto a instrumentos débiles)
- [ ] Considerar LIML como alternativo a 2SLS si hay instrumentos débiles
- [ ] Lee (2021) tF adjustment si corresponde

## Robustez
- [ ] Reduced form reportada (efecto de Z directamente sobre Y)
- [ ] Sensibilidad a la inclusión/exclusión de covariables
- [ ] Plausibly exogenous (Conley bounds) si la exclusión es debatible
- [ ] Subgrupos: ¿el efecto varía por tipo de complier?

## Diagnósticos Adicionales
- [ ] Test de endogeneidad (Hausman / Durbin-Wu-Hausman): ¿se justifica usar IV?
- [ ] Si la endogeneidad no es rechazada: OLS puede ser preferido (más eficiente)
- [ ] Discusión de monotonicity assumption para interpretar como LATE
