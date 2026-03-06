---
description: Comando global para crear la estructura DIME y clonar todo el "cerebro AI" (Agent Profiles, Checklists y Workflows) hacia un nuevo proyecto en 10 segundos.
---

# Workflow: Project Init (DIME Template Builder)

Inspirado en el comando `projectinit` de DIME, pero potenciado con Inteligencia Artificial.

## Invocación
Escribe: `/projectinit [NombreDelProyecto]`
Ejemplo: `/projectinit Impacto_Crimen_Vivienda`

## Flujo de Trabajo (Project Scaffolding)

1. El Orquestador captura el `[NombreDelProyecto]`.
2. El sistema ejecuta silenciosamente el script maestro `crear_template.py` pasándole el nombre deseado.
   ```bash
   python .agents/workflows/crear_template.py "NombreDelProyecto"
   ```
3. El script asume la carpeta contenedora principal (`E:\00_Desktop\` o similar) y crea la nueva carpeta del proyecto allí.
4. **¿Qué se copia al nuevo proyecto?**
   - El esqueleto de carpetas DIME vacío (`01_data`, `02_scripts`, `03_outputs`, etc.) con archivos `.gitkeep`.
   - La carpeta maestra `.agents/` con todos tus perfiles de Críticos, Verificadores, y checklists.
   - El archivo `CLAUDE.md` con tus directrices personalizadas.
   - Herramientas auxiliares (`gemini_lit_extractor.py`, `aer_style.py`).
5. **¿Qué NO se copia?** (Para mantener el peso en kilobytes)
   - Datos crudos `.dta` o `.csv`
   - Resultutilities, tablas o figuras previas.
   - Archivos PDF de la literatura.
   - Logs de Stata.
6. El Orquestador notifica el éxito, la ruta exacta del nuevo proyecto, y le recomienda al usuario hacer un `git init` en esa nueva carpeta.
