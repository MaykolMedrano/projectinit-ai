# Checklist de Outputs

Usado por el **Verificador** para asignar el puntaje final (0-100).

## Tablas
- [ ] Formato LaTeX booktabs (`\toprule`, `\midrule`, `\bottomrule`)
- [ ] Sin líneas verticales
- [ ] CSV companion generado junto con cada `.tex`
- [ ] Notas al pie con significancia estadística (*, **, ***)
- [ ] Errores estándar entre paréntesis
- [ ] Variable dependiente indicada en la cabecera
- [ ] Observaciones y R² reportados
- [ ] Label LaTeX único para referencias cruzadas (`\ref{}`)

## Figuras
- [ ] Estilo AER aplicado (`configure_aer_style()` de `02_scripts/ados/aer_style.py`)
- [ ] Fuente serif (Times New Roman o similar)
- [ ] Sin cuadrícula (axes.grid = False)
- [ ] Resolución ≥ 300 DPI
- [ ] Bordes superior y derecho eliminados (spines)
- [ ] Notas descriptivas al pie del gráfico
- [ ] Paleta segura para escala de grises (grayscale-safe) si es para publicación
- [ ] Guardada con `aer_save()` en `03_outputs/figures/`

## Estructura DIME
- [ ] `01_data/raw/` y `01_data/de-identified/` intactos (solo lectura)
- [ ] ETL output en `01_data/intermediate/`
- [ ] Scripts ETL en `02_scripts/data_preparation/`
- [ ] Scripts de estimación en `02_scripts/analysis/`
- [ ] Scripts de robustez en `02_scripts/validation/` (separados del script principal)
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
