---
description: Audita un documento académico (LaTeX o Markdown) buscando fallas gramaticales, tono y consistencia con las tablas/figuras generadas.
---

# Revisión de Manuscrito Académico

## Activación
Escribe: `/review-paper [archivo.tex]`

## Flujo

1. Lee el archivo indicado por el usuario con la herramienta `view_file`.
2. Asume el rol del **Agente Revisor de Manuscrito** (academic proofreader).
3. Evalúa el documento con las siguientes lentes:
   - **Gramática y Redacción (Wording):** Nivel AER/MIT, claridad en voz pasiva/activa, sin adornos excesivos.
   - **Cruces de Referencia:** Uso de `\ref{}` en vez de números fijos (hardcoded).
   - **Consistencia:** Verifica que las cifras mencionadas en el texto coincidan con lo expuesto en las tablas LaTeX (generalmente ubicadas en `03_outputs/tables/`).
4. Presenta tu reporte estructurado indicando fallas **Critical**, **Major** y **Minor (Suggestions)**, según el perfil del Revisor de Manuscrito.
5. Pregunta al usuario si desea que apliques las correcciones directamente sobre el archivo.
