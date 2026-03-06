---
description: Flujo estricto que obliga a la exploración rigurosa de datos (summary stats y plots) antes de intentar ajustar un modelo final.
---

# Workflow: Data Analysis Pre-Flight

Inspirado en el comando `/data-analysis` de Pedro Sant'Anna.

## Invocación

Escribe: `/data-analysis [script_o_dataset]`

## Flujo de Trabajo (Filosofía "Design Before Results")

1. No se permite al Agente Creador escribir el script final de estimación sin pasar por este filtro.
2. El Agente Creador debe escribir un script temporal o celda de exploración que arroje:
   - Estadísticas descriptivas completas (Summary Stats).
   - Plots de distribución de las variables clave (Outcome y Running Variable / Tratamiento).
   - Verificación de valores nulos (missing values) y atípicos (outliers).
   - **Heaping Test:** Verificar agrupaciones espurias en números redondos para variables continuas (Barreca et al, 2011).
   - **Moran's I:** Si hay datos geográficos, reportar autocorrelación espacial para prever errores Conley.
3. El Agente Crítico Code revisará los resultutilities de esta exploración temporal.
   - Verifica si la estrategia de limpieza de NAs fue correcta.
   - Verifica si la distribución de las variables sugiere necesidad de transformaciones (ej. logaritmos).
4. Solo cuando el Crítico aprueba la "salud de los datos" (Data Health), se autoriza al Creador a proceder al script de estimación final en `02_scripts/analysis/`.
5. El Orquestador solicita aprobación del usuario validando que la salud de los datos cumple las reglas antes de modelar.
