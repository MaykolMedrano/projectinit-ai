# Checklist ETL Espacial

Usado por el **Crítico Code** para auditar scripts de limpieza y preparación de datos.

## Datos de Entrada
- [ ] Fuente de datos documentada (SII, MINVU, INE, etc.)
- [ ] Variables originales listadas con descripción
- [ ] Formato de entrada especificado (CSV, DTA, SHP, GeoJSON)

## Integridad de Datos
- [ ] Conteo de observaciones antes y después de cada filtro
- [ ] Tratamiento de valores faltantes (missing values) documentado y justificado
- [ ] Outliers identificados (criterio: IQR, percentiles, conocimiento de dominio)
- [ ] Duplicados verificados y eliminados con criterio explícito
- [ ] Variables de identificación únicas (rol, manzana, comuna)

## Componente Espacial
- [ ] CRS (sistema de coordenadas) explícito y consistente entre capas
- [ ] Join espacial documentado (tipo: nearest, within, intersects)
- [ ] Distancias calculadas en metros (no en grados)
- [ ] Buffer de exclusión definido si aplica (ej. 50m alrededor de estaciones)
- [ ] Variables de distancia verificadas con casos conocidos

## Estructura DIME
- [ ] `01_data/raw/` NO fue modificado (solo lectura)
- [ ] Output guardado en `01_data/intermediate/`
- [ ] Script guardado en `02_scripts/data_preparation/`
- [ ] Nombres de archivos descriptivos y sin espacios

## Reproducibilidad
- [ ] Sin rutas absolutas hardcodeadas
- [ ] Semillas (seeds) fijadas si hay componente aleatorio
- [ ] Log de ejecución limpio (sin errores ni advertencias críticas)
- [ ] Versiones de paquetes documentadas (requirements.txt o environment)
