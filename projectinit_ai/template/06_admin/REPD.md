# REPD: Research Excellence & Replication Protocol

Este documento guía el proceso de empaquetado final para réplica (Estándar AEA/NBER).

## 1. Integridad de Datos

- [ ] Datos `raw/` son de solo lectura.
- [ ] Scripts de limpieza (`02_scripts/data_preparation/`) generan `intermediate/` sin error.
- [ ] Variables de identificación (keys) verificadas.

## 2. Código de Análisis

- [ ] Script maestro (`main.py` o `main.do`) ejecuta todo el flujo.
- [ ] Sin rutas absolutas (Uso de `here()` o `os.path`).
- [ ] Semillas fijadas (`random.seed`).
- [ ] Comentarios profesionales y técnicos (sin emojis) que guían la ejecución.

## 3. Outputs (Standard Protocol)

- [ ] Tablas en `.tex` cumplen el **Protocol: Econometrics** (No vertical lines, siunitx fix).
- [ ] Gráficos en `.png` / `.pdf` (300 DPI) cumplen la **Regla Ultra-Thin**.
- [ ] Logs presentes y limpios en `03_outputs/logs/`.

## 4. Software Environment

- [ ] `requirements.txt` actualizado.
- [ ] `README.md` incluye instrucciones de instalación claras.
