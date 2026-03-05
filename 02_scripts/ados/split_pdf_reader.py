"""
split_pdf_reader.py
===================
Implementacion del protocolo Split-PDF de MixtapeTools para ingesta de literaturas sin alucinaciones.
Extrae el texto de un PDF pesado bloqueandose en chunks tolerables por la ventana de contexto.
"""

import sys
from pathlib import Path

def print_usage():
    print("Uso: python split_pdf_reader.py <ruta_al_pdf> [chunk_size]")
    print("Ejemplo: python split_pdf_reader.py paper_metro.pdf 5")

def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)
        
    pdf_path = Path(sys.argv[1])
    if not pdf_path.exists():
        print(f"Error: No se encontro el archivo {pdf_path}")
        sys.exit(1)
        
    chunk_size = int(sys.argv[2]) if len(sys.argv) > 2 else 5
    
    try:
        import PyPDF2
    except ImportError:
        print("Instalando PyPDF2 requerido por la herramienta...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
        import PyPDF2

    print(f"Abriendo: {pdf_path.name}")
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            print(f"Total de paginas: {total_pages}")
            
            # Generar chunks y en caso de integrar directo con el agente, 
            # podriamos soltar el texto estructurado a archivos .md.
            output_dir = pdf_path.parent / f"{pdf_path.stem}_chunks"
            output_dir.mkdir(exist_ok=True)
            
            chunk_files = []
            for start_page in range(0, total_pages, chunk_size):
                end_page = min(start_page + chunk_size, total_pages)
                out_file = output_dir / f"chunk_{start_page+1:03d}_{end_page:03d}.txt"
                
                text = f"--- {pdf_path.name} | Pages {start_page+1}-{end_page} ---\n\n"
                for i in range(start_page, end_page):
                    page = reader.pages[i]
                    text += f"\n[Page {i+1}]\n" + page.extract_text() + "\n"
                
                with open(out_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                chunk_files.append(out_file)
                
            print(f"\nExito: PDF dividido en {len(chunk_files)} chunks en {output_dir}/")
            print("El agente ahora debe leer y generar el 'reading note' secuencialmente.")
            
    except Exception as e:
        print(f"Failed to process PDF: {e}")

if __name__ == "__main__":
    main()
