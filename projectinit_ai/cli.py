import os
import shutil
import argparse
from pathlib import Path

import projectinit_ai

def main():
    parser = argparse.ArgumentParser(description="Inicializa un nuevo laboratorio de investigación con projectinit-ai (DIME Standards).")
    parser.add_argument("project_name", nargs="?", default="projectinit_ai_lab", help="Nombre del nuevo proyecto/carpeta (por defecto: projectinit_ai_lab)")
    args = parser.parse_args()

    project_name = args.project_name
    target_dir = Path.cwd() / project_name

    if target_dir.exists():
        print(f"[ERROR] El directorio '{project_name}' ya existe.")
        return

    # Path to template inside the package
    pkg_dir = Path(projectinit_ai.__file__).parent
    template_dir = pkg_dir / "template"

    if not template_dir.exists():
        print("[ERROR CRITICO] No se encontro la carpeta de plantilla interna en el paquete.")
        return

    print(f"[*] Inicializando laboratorio de investigacion '{project_name}' (Estandares DIME)...")
    
    # Copy template to the target directory
    shutil.copytree(template_dir, target_dir)

    print(f"[SUCCESS] Proyecto '{project_name}' creado con exito!")
    print("\nSiguientes pasos recomendados:")
    print(f"  1. cd {project_name}")
    print("  2. pip install -r requirements.txt")
    print("  3. Abre tu editor de código preferido (ej. vscode) en la carpeta.")

if __name__ == "__main__":
    main()
