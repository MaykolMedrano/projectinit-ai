---
description: Iteración autónoma (Crítico vs Creador) sobre documentos (manuscritos LaTeX o Markdown) hasta alcanzar la perfección o un máximo de 5 rondas.
---

# Workflow: Auto QA Loop para Documentos

Inspirado en el comando `/qa-quarto` (Adversarial QA) de Pedro Sant'Anna.

## Invocación
Escribe: `/qa-quarto [archivo.tex o archivo.md]`

## Flujo de Trabajo (Loop Iterativo Autónomo)

1. El Orquestador carga el archivo indicado.
2. Inicia la **Ronda 1**:
   - Activa al **Agente Revisor de Manuscrito** (Crítico).
   - El Crítico lee el archivo y emite un reporte con fallas `Critical`, `Major` y `Minor`.
   - Si no hay fallas (solo Minor o cero), el Orquestador emite un dictamen "APPROVED" y termina el flujo.
3. Si hay fallas `Critical` o `Major`:
   - El Orquestador activa al **Agente Creador** asumiendo el rol de "Fixer".
   - El Fixer implementa las correcciones exigidas por el Crítico directamente en el archivo.
4. Se repite el ciclo desde el paso 2 (Ronda 2).
5. **Condición de Parada:** El ciclo termina cuando el Crítico emite "APPROVED" o se alcanza el **máximo de 5 rondas**.
6. El Orquestador notifica al usuario el fin del loop junto con un breve sumario de los cambios realizados.
