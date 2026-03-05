"""
gemini_lit_extractor.py
=======================
Extractor automático de literatura profunda usando la API de Gemini 2.5 Flash.
Toma PDFs masivos ubicados en `04_literature/papers/` y usa el inmenso contexto
de Gemini para extraer notas metodológicas estructuradas en `04_literature/reading_notes/`.

Requisitos:
- pip install google-generativeai pymupdf

Uso:
- python 02_scripts/ados/gemini_lit_extractor.py [opcional: paper.pdf]
"""

import sys
import os
import time
from pathlib import Path
import json

try:
    import fitz  # PyMuPDF
except ImportError:
    print("PyMuPDF (fitz) no encontrado. Instalando...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pymupdf"])
    import fitz

try:
    import google.generativeai as genai
except ImportError:
    print("google-generativeai no encontrado. Instalando...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
    import google.generativeai as genai

# Configuración de Rutas DIME
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent.parent
LIT_PAPERS_DIR = PROJECT_ROOT / "04_literature" / "papers"
LIT_NOTES_DIR = PROJECT_ROOT / "04_literature" / "reading_notes"

def extract_text_from_pdf(pdf_path):
    """Extrae el texto crudo completo de un PDF usando PyMuPDF."""
    print(f"📄 Extrayendo texto de: {pdf_path.name}")
    try:
        doc = fitz.open(pdf_path)
        full_text = []
        for page in doc:
            full_text.append(page.get_text())
        return "\n".join(full_text)
    except Exception as e:
        print(f"❌ Error leyendo PDF {pdf_path.name}: {e}")
        return None

def analyze_paper_with_gemini(text, filename, api_key):
    """Envía el paper completo a Gemini y pide un Markdown DIME-friendly."""
    print(f"🧠 Enviando a Gemini-2.5-Flash (~{len(text)//4} tokens)...")
    
    genai.configure(api_key=api_key)
    # Gemini 2.5 Flash tiene 1M de tokens, ideal para PDFs enteros
    model = genai.GenerativeModel("gemini-2.5-flash")
    
    prompt = f"""Eres un Asistente de Investigación (PhD en Economía Urbana) audaz y extremadamente preciso.
Tu misión es leer este paper académico COMPLETO y extraer la estructura empírica para una tesis.

**Reglas Críticas:**
- Responde ÚNICA Y EXCLUSIVAMENTE en el formato Markdown exacto que te doy abajo. No agregues preámbulos como "Aquí tienes" ni nada fuera de la plantilla markdown.
- Ve directo al grano. Odias la palabrería ("fluff"). Los economistas preferimos datos duros.
- Para las magnitudes, rescata los números exactos reportados (ej. "aumenta 4.5%", "coeficiente 0.12").
- Si el documento no menciona algo claramente, pon "No especificado explícitamente".

**Plantilla Markdown a devolver:**

```markdown
# Reading Note: {filename}

## 1. Abstract Ejecutivo (TL;DR)
[Resumen de 3 o 4 líneas directas]

## 2. Pregunta de Investigación Principal
[Una oración clara]

## 3. Estrategia de Identificación Empírica (Causal)
- **Modelo:** [Ej. RDD, DiD Espacial, IV]
- **Variable de Tratamiento (X):** [Definición exacta, ej. Distancia al metro en km]
- **Variable de Resultado (Y):** [Definición, ej. Logaritmo del precio por m2]
- **Supuestos Claves Discutidos:** [Ej. Tendencias paralelas, manipulacion nula en el cutoff]
- **Contexto Geográfico/Temporal:** [País, ciudad, años analizados]

## 4. Datos y Fuentes
- [Breve punteo de los datos usados, niveles de agregación]

## 5. Resultados y Magnitudes Principales (Números Duros)
- [Punteo de los coeficientes principales y sus significancias. Ej. "Apertura del metro incrementa el valor del suelo en X% dentro de un radio de Y metros."]

## 6. Amenazas a la Validez / Limitaciones
- [Punteo de lo que los autores admiten que podría estar sesgado, o spillovers no resueltos]
```

Aquí está el texto completo del paper extraído en crudo:
---------------------------------------------------------
{text}
"""

    try:
        # Se envia el prompt crudo. El SDK maneja el largo del contexto automagicamente.
        response = model.generate_content(prompt)
        
        # Limpiar output (a veces la IA devuelve ```markdown al principio)
        content = response.text.strip()
        if content.startswith("```markdown"):
            content = content[11:]
        if content.endswith("```"):
            content = content[:-3]
            
        return content.strip()
    except Exception as e:
        print(f"❌ Error de API Gemini: {e}")
        return None

def process_single_pdf(pdf_path, api_key):
    """Flujo completo para un archivo individual."""
    output_note_path = LIT_NOTES_DIR / f"{pdf_path.stem}_note.md"
    
    if output_note_path.exists():
        print(f"⏭️ Saltando {pdf_path.name} (Ya existe: {output_note_path.name})")
        return True
        
    text = extract_text_from_pdf(pdf_path)
    if not text:
        return False
        
    # Verificar si el texto es muy corto (probablemente falló la extracción o es imagen)
    if len(text) < 2000:
        print(f"⚠️ El texto extraído de {pdf_path.name} es sospechosamente corto. PDF escaneado sin OCR?")
        return False
        
    markdown_note = analyze_paper_with_gemini(text, pdf_path.name, api_key)
    
    if markdown_note:
        with open(output_note_path, 'w', encoding='utf-8') as f:
            f.write(markdown_note)
        print(f"✅ Extracción exitosa guardada en: {output_note_path.relative_to(PROJECT_ROOT)}")
        return True
    return False

def main():
    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("❌ ERROR CRÍTICO: No se encontró la variable de entorno GOOGLE_API_KEY.")
        print("Por favor configura tu llave en la terminal antes de ejecutar:")
        print("cmd  -> set GOOGLE_API_KEY=tu_llave_aqui")
        print("bash -> export GOOGLE_API_KEY=tu_llave_aqui")
        sys.exit(1)

    print("\n=======================================================")
    print("🧠 GEMINI AUTO-LITERATURE EXTRACTOR (v2.5 Flash Edition)")
    print("=======================================================\n")
    
    LIT_PAPERS_DIR.mkdir(parents=True, exist_ok=True)
    LIT_NOTES_DIR.mkdir(parents=True, exist_ok=True)

    # Si se pasa un archivo específico
    if len(sys.argv) > 1:
        target_path = Path(sys.argv[1])
        if target_path.exists():
            print(f"Modo Archivo Único: Procesando {target_path.name}")
            process_single_pdf(target_path, api_key)
        else:
            print(f"❌ No se encontró el archivo {target_path}")
        sys.exit(0)

    # Modo Batch: procesar toda la carpeta papers/
    pdf_files = list(LIT_PAPERS_DIR.glob("*.pdf"))
    
    if not pdf_files:
        print(f"ℹ️ No se encontraron archivos .pdf en {LIT_PAPERS_DIR.relative_to(PROJECT_ROOT)}")
        print(f"⚠️ Por favor, deposita tus PDFs descargados allí e intenta de nuevo.")
        sys.exit(0)
        
    print(f"🔍 Encontrados {len(pdf_files)} PDFs en cola...")
    
    for i, pdf_path in enumerate(pdf_files):
        print(f"\n[{i+1}/{len(pdf_files)}] Procesando...")
        success = process_single_pdf(pdf_path, api_key)
        
        # Rate Limiting (Evitar saturar la cuota gratuita)
        if success and i < len(pdf_files) - 1:
            print("⏳ Esperando 5 segundos por el rate-limit de Google API...")
            time.sleep(5)
            
    print("\n✨ Proceso Finalizado. ¡Revisa tu carpeta reading_notes!")

if __name__ == "__main__":
    main()
