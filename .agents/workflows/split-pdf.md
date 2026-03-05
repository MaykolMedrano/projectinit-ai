---
description: Comando para extraer la metodología y resultados de PDFs completos usando la API de Gemini 2.5 Flash.
---

# Split-PDF Reader Skill (Gemini Edition)

Inspirado en el protocolo de lectura profunda de MixtapeTools, mejorado con el contexto masivo de LLMs.

## Invocación
1. Deposita tus PDFs en la carpeta `04_literature/papers/`
2. Ejecuta en tu terminal el extractor automatizado:
   ```bash
   python 02_scripts/ados/gemini_lit_extractor.py
   ```
*(Opcional: puedes pasar la ruta de un solo PDF como argumento).*

## Flujo de Trabajo (Deep Literature Extraction)

1. El script lee y extrae todo el texto crudo del PDF usando `PyMuPDF` (optimizador de alta velocidad).
2. Se envía el texto completo (+100 páginas si es necesario) a la API de **Gemini 2.5 Flash**, aprovechando su inmensa ventana de contexto de 1 millón de tokens.
3. Gemini es forzado mediante un prompt estricto a devolver únicamente un archivo Markdown (`.md`) estructurado.
4. El archivo generado se guarda automáticamente en `04_literature/reading_notes/[nombre_paper]_note.md`.
5. El sistema detecta papers ya procesados para no gastar cuota de API (caché).

### ¿Qué extrae la IA?
- Abstract Ejecutivo (TL;DR)
- Pregunta de Investigación Principal
- Estrategia de Identificación Empírica (Causal)
- Datos y Fuentes
- Resultados y Magnitudes Principales (Números Duros)
- Amenazas a la Validez / Limitaciones
