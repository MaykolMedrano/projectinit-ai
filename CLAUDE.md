# CLAUDE.MD --- Constitución del Proyecto **[Insertar Nombre de tu Proyecto]**

## Principios Centrales (Core Principles)
1. **DIME-First:** Nunca modificar `/01_data/raw/`. Mantén la higiene de scripts en `data_preparation`, `analysis` y `validation`.
2. **Quality Gates:** Para pasar al estado final, las tablas y figuras deben cumplir con el estándar AER/MIT (booktabs, serif, sin grid).
3. **Audit Adversarial:** Todo script nuevo de análisis (como Creador) debe pasar la revisión del Crítico Code y Crítico Causal.
4. **Validation-Separation:** Las pruebas de robustez/falsificación deben ir en scripts separados en `/02_scripts/validation/`.
5. **No-Guessing:** Si necesitas tomar decisiones sobre variables clave o thresholds que no están en tus instrucciones, pregunta al USER.

## Estructura del Proyecto
- `01_data/raw/` (Inmutables)
- `01_data/intermediate/` (Outputs de ETL)
- `01_data/final/` (Listos para análisis)
- `02_scripts/data_preparation/` (ETL)
- `02_scripts/analysis/` (Main models)
- `02_scripts/validation/` (Event studies, placebo, bandwidth checks)
- `03_outputs/tables/` (.tex y .csv)
- `03_outputs/figures/` (.png/.pdf listos para paper)
- `04_literature/` (Papers, BibTeX, notas de lectura)
- `05_doc/` (Manuscrito, presentaciones, documentación)
- `06_admin/` (IRB, PAP Registrations, NDA)

## Skills Rápidos (Slash Commands)
| Comando | Descripción |
|---------|-------------|
| `/projectinit` | Clona toda tu arquitectura (DIME + Agentes) a un proyecto nuevo. |
| `/contractor-mode` | Ciclo adversario completo (Creador -> Críticos -> Verificador). |
| `/data-analysis` | Exploración obligatoria (summary stats + plots) antes de modelar. |
| `/research-ideation` | Devil's Advocate sobre tu diseño causal antes de programar. |
| `/review-paper` | Audita un documento LaTeX o Markdown (gramática, consistencia, tono). |
| `/qa-quarto` | Loop autónomo Crítico-Fixer sobre manuscritos (max 5 rondas). |
| `/humanizer` | Elimina tono robótico/GPTesco de texto académico. |
| `/split-pdf` | Lee PDFs pesados bloque a bloque sin desbordar contexto. |
| `/audit-replication` | Empaquetamiento AEA Data Editor (código, datos, readme). |

## Estado del Proyecto
- **Etapa:** Configuración inicial del laboratorio digital completada.
- **Siguiente paso:** Ingesta de datos crudos en `01_data/raw/` y diseño de la estrategia de identificación.
