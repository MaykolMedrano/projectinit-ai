---
description: Activa el Modo Contratista con el ciclo adversario completo (Plan → Creador → Crítico Code + Crítico Causal → Verificador).
---

# Modo Contratista — Flujo v4

## Activación
`Orquestador: Modo Contratista. [instrucción]`
Opcional: `Score mínimo: 70`

## Ciclo

1. **Orquestador** genera plan + identifica datos MCP.
2. **Creador — ETL**: `01_data/raw/` → `01_data/intermediate/`. Script en `02_scripts/data_preparation/`.
3. **Crítico Code** audita ETL con `checklist_etl_spatial.md`. Si falla → Creador corrige.
4. **Creador — Estimación**: script en `02_scripts/analysis/` sobre datos limpios.
5. Ejecución:
   - Stata: `stata-mp -b do script.do` → log a `03_outputs/logs/`
   - Python: `python script.py > 03_outputs/logs/output.log 2>&1`

> **Estructura completa:** `01_data/` → `02_scripts/` → `03_outputs/` → `04_literature/` → `05_doc/`
6. **Doble Auditoría** (paralela):
   - **Crítico Code**: log, código, DIME.
   - **Crítico Causal**: identificación, SUTVA, checklist metodológico.
7. Errores -> Orquestador genera **Agent Handoff Template** para el Creador (máx 5 rondas).
8. **Verificador** califica 0–100 con `checklist_outputs.md`.
   - `≥ umbral` → cierre.
   - `< umbral` → nueva ronda.
   - 5 rondas fallidas → escalación al usuario.

## Perfiles Principales (Contractor Loop)
- [orquestador.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/orquestador.md)
- [agente_creador.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_creador.md)
- [agente_critico.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_critico.md)
- [agente_critico_causal.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_critico_causal.md)
- [agente_verificador.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_verificador.md)

## Perfiles Auxiliares (Otros Workflows)
- [agente_revisor_dominio.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_revisor_dominio.md)
- [agente_revisor_manuscrito.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_revisor_manuscrito.md)
- [agente_presentador.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_presentador.md)
- [agente_auditor_tesis.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_auditor_tesis.md)
- [agente_docente_ayudantia.md](file:///C:/Users/User/.gemini/antigravity/brain/ad915fcc-5e5c-47e9-a5fd-1929f0694e1b/agente_docente_ayudantia.md)

