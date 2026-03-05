# Checklist RDD (Regression Discontinuity Design)

Usado por el **Crítico Causal** para auditar diseños de regresión discontinua.

## Estrategia de Identificación
- [ ] Running variable definida y justificada (ej. distancia a estación de metro)
- [ ] Cutoff con respaldo teórico o institucional (ej. radio regulatorio, zona de influencia)
- [ ] Dirección del efecto esperado fundamentada

## Validez del Running Variable
- [ ] Test de manipulación: McCrary o `rddensity` (Cattaneo et al.)
- [ ] Histograma de la running variable alrededor del cutoff
- [ ] Discusión de si los agentes pueden manipular la running variable

## Balance Pre-Tratamiento
- [ ] Covariables pre-tratamiento balanceadas alrededor del cutoff
- [ ] Test de balance formal (RD en covariables como resultado)
- [ ] Tabla de balance presentada

## Especificación
- [ ] Ancho de banda (Bandwidth) óptimo reportado (CCT / IK / CV)
- [ ] Kernel especificado (triangular, uniforme, epanechnikov)
- [ ] Orden del polinomio justificado (lineal preferido, cuadrático como robustez)
- [ ] Efectos fijos incluidos si corresponde (año, comuna)

## Robustez
- [ ] Sensibilidad al ancho de banda (50%, 75%, 125%, 150% del óptimo)
- [ ] Placebo en cutoffs falsos (ej. ±500m del cutoff real)
- [ ] Donut-hole RDD (excluir observaciones muy cercanas al cutoff)
- [ ] Polinomio alternativo como robustez
- [ ] Covariables como controles adicionales

## Inferencia
- [ ] Errores estándar robustos o correlacionados (clustered) al nivel apropiado
- [ ] Intervalos de confianza reportados
- [ ] Interpretación LATE explícita (efecto local, no ATE)

## Visualización
- [ ] RD plot con bins y ajuste polinomial a ambos lados del cutoff
- [ ] Notas descriptivas al pie del gráfico
