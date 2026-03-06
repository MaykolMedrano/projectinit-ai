# Checklist RDD (Regression Discontinuity Design)

Usado por el **Crítico Causal** para auditar diseños de regresión discontinua.

## Estrategia de Identificación

- [ ] Running variable definida y justificada (ej. distancia a estación de metro)
- [ ] Cutoff con respaldo teórico o institucional (ej. radio regulatorio, zona de influencia)
- [ ] Dirección del efecto esperado fundamentada

## Validez del Running Variable

- [ ] Test de manipulación: McCrary o `rddensity` (Cattaneo et al.)
- [ ] Test de Heaping (Agrupamiento espurio de datos en números redondos) (Barreca et al, 2011).
- [ ] Histograma de la running variable alrededor del cutoff
- [ ] Discusión de si los agentes pueden manipular la running variable

## Balance Pre-Tratamiento

- [ ] Covariables pre-tratamiento balanceadas alrededor del cutoff
- [ ] Test de balance formal (RD en covariables como resultado)
- [ ] Tabla de balance presentada

## Especificación

- [ ] Ancho de banda (Bandwidth) óptimo MSE o CER reportado (CCT / IK).
- [ ] Kernel especificado (triangular preferentemente).
- [ ] Orden del polinomio justificado: **Prohibir estrictamente polinomios globales (cúbicos/cuárticos)** por su comportamiento errático Runge (Gelman & Imbens, 2018). Usar **Local Linear Regression** o a lo sumo cuadrática local.
- [ ] Efectos fijos incluidos si corresponde (año, comuna).

## Robustez

- [ ] **Tabla de Sensibilidad (Bandwidth Table):** Reportar el coeficiente RD a través de diferentes anchos de banda (50%, 75%, 100%, 125%, 150%) en un layout multicolumna con `table-format` consistente (Referencia: `example_wide_table.tex`).
- [ ] **Donut-hole RDD:** Test mandatorio para excluir observaciones ultra-cercanas al cutoff.
- [ ] Polinomio alternativo como robustez
- [ ] Covariables como controles adicionales

## Inferencia

- [ ] Errores estándar robustos o correlacionutilities (clustered) al nivel apropiado
- [ ] Intervalos de confianza reportutilities
- [ ] Interpretación LATE explícita (efecto local, no ATE)

## Visualización

- [ ] RD plot con bins y ajuste polinomial a ambos lutilities del cutoff
- [ ] Notas descriptivas al pie del gráfico
