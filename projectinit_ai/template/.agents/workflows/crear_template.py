"""
crear_template.py
=================
Generador de Repositorio Plantilla / Boilerplate
Este script crea una copia exacta de la estructura DIME actual (carpetas, 
perfiles de agentes, checklists, workflows y scripts auxiliares en utilities/),
pero OMITIENDO los datos crudos, las salidas .log, los manuscritos y los PDFs.

El resultado es una carpeta `dime-ai-template` lista para subirse a GitHub
y usarse como punto de partida para tu próxima tesis o paper.
"""

import os
import shutil
from pathlib import Path

# Definimos que la raiz del proyecto es el directorio padre de `.agents/workflows`
SCRIPT_DIR = Path(__file__).parent.resolve()
PROJECT_ROOT = SCRIPT_DIR.parent.parent

# Definimos donde estara la plantilla nueva (afuera de la carpeta actual por seguridad)
TEMPLATE_ROOT = PROJECT_ROOT.parent / "dime-ai-template"

def ignore_data_and_logs(dir_path, contents):
    """
    Funcion de filtrado para shutil.copytree.
    Retorna una lista con los nombres de archivos/carpetas a ignorar.
    """
    ignored = []
    
    # Lista de extensiones prohibidas (datos, resultutilities generutilities, imagenes pesadas)
    BAD_EXTENSIONS = ('.dta', '.csv', '.xlsx', '.pdf', '.log', '.png', '.jpg', '.pdf', '.tex', '.md', '.docx')
    
    # Excepciones que SI queremos clonar aunque sean .md (Los agentes y documentación core)
    ALLOWED_MD = ('CLAUDE.md', 'README.md', 'task.md', 'implementation_plan.md', 'walkthrough.md')
    
    current_dir_name = Path(dir_path).name
    
    for item in contents:
        item_path = Path(dir_path) / item
        
        # Ignorar carpetas temporales/ocultas comunes
        if item in ('.git', '.venv', '__pycache__', '.pytest_cache'):
            ignored.append(item)
            continue
            
        # Ignorar el contenido de datos y literature (pero mantener la carpeta vacia)
        if current_dir_name in ('raw', 'de-identified', 'intermediate', 'final', 'papers', 'reading_notes', 'bibtex', 'tables', 'figures', 'logs', 'manuscript', 'presentations', 'raw_outputs'):
            ignored.append(item)
            continue

        # Si es un archivo, aplicamos filtros de extension
        if item_path.is_file():
            # Si el archivo MD es uno de los agentes, workflows o checklists, dejarlo pasar
            if '.agents' in item_path.parts:
                continue
                
            if item.endswith(BAD_EXTENSIONS) and item not in ALLOWED_MD:
                ignored.append(item)
                
    return ignored

def main():
    import sys
    if sys.stdout.encoding != 'utf-8':
        try:
            sys.stdout.reconfigure(encoding='utf-8')
        except AttributeError:
            pass

    print("==================================================")
    print("GENERADOR DE PLANTILLA DIME + AGENTES")
    print("==================================================")
    
    # Manejar el nombre del proyecto desde el CLI
    project_name = "dime-ai-template"
    if len(sys.argv) > 1:
        project_name = sys.argv[1].strip()
        
    template_root = PROJECT_ROOT.parent / project_name
    
    print(f"Origen del proyecto: {PROJECT_ROOT}")
    print(f"Destino de la plantilla: {template_root}")
    
    if template_root.exists():
        print(f"\nAVISO: La carpeta '{project_name}' ya existe.")
        print("Operación cancelada para proteger tus datos. Borra la carpeta o usa otro nombre.")
        return
        
    print(f"\nClonando estructura a '{project_name}' y omitiendo datos/PDFs/logs pesutilities...")
    
    # shutil.copytree crea toda la estructura, usando el filtro 'ignore'
    shutil.copytree(PROJECT_ROOT, template_root, ignore=ignore_data_and_logs)
    
    # Recrear limpiamente las carpetas clave para que queden vacías pero listas
    empty_folders = [
        "01_data/raw", "01_data/de-identified", "01_data/intermediate", "01_data/final", "01_data/codebooks",
        "02_scripts/01_data_checks",
        "03_outputs/tables", "03_outputs/figures", "03_outputs/logs",
        "04_literature/papers", "04_literature/reading_notes", "04_literature/bibtex",
        "05_doc/manuscript", "05_doc/presentations",
        "06_admin/pre_analysis_plan", "06_admin/irb_ethics", "06_admin/data_agreements"
    ]
    
    print("\nAsegurando carpetas DIME base (vacías):")
    for folder in empty_folders:
        dir_to_create = template_root / folder
        dir_to_create.mkdir(parents=True, exist_ok=True)
        # Crear un archivo .gitkeep oculto para que git siga la carpeta vacía
        gitkeep = dir_to_create / ".gitkeep"
        gitkeep.touch()
        print(f"  + {folder}/.gitkeep")
        
    print("\nGenerando Scripts Maestros de Reproducibilidad (AEA/DIME):")
    
    # 1. 00_master.do (Stata)
    master_do = template_root / "02_scripts" / "00_master.do"
    master_do.write_text(f"""/*******************************************************************************
* MASTER EXECUTION SCRIPT - 00_master.do
*
* Project:     {project_name}
*
* Purpose:     One-click reproducible execution of entire project
* Standards:   J-PAL (MIT) | DIME (World Bank) | AEA Data Editor
*******************************************************************************/

clear all
macro drop _all
set more off
set varabbrev off           // Prevent ambiguous abbreviations
set type double             // Precision

/*******************************************************************************
SECTION 1: DYNAMIC PATH CONFIGURATION (VIRTUALIZATION)
*******************************************************************************/

* Root directory (automatically detected if running from project root)
global root "`c(pwd)'"

* Data directories (J-PAL/DIME standard)
global data          "$root/01_data"
global raw           "$data/raw"
global deidentified  "$data/de-identified"
global intermediate  "$data/intermediate"
global final         "$data/final"

* Script directories
global scripts       "$root/02_scripts"
global utilities          "$scripts/utilities"
global datachecks    "$scripts/01_data_checks"

* Output directories (AEA standard)
global outputs       "$root/03_outputs"
global tables        "$outputs/tables"
global figures       "$outputs/figures"
global logs          "$outputs/logs"

* Documentation & Admin
global doc           "$root/05_doc"
global admin         "$root/06_admin"

display as result "{{hline 78}}"
display as result "PROJECT: {project_name}"
display as result "{{hline 78}}"
display as text "Root:      $root"
display as text "Started:   `c(current_date)' `c(current_time)'"
display as result "{{hline 78}}"

/*******************************************************************************
SECTION 2: ENVIRONMENT ISOLATION (NBER Standard)
*******************************************************************************/
* Add local ado directory to search path (highest priority)
adopath ++ "$utilities"

/*******************************************************************************
SECTION 3: DEPENDENCY MANAGEMENT 
*******************************************************************************/
* Ensure core packages are installed
capture do "$utilities/stata_packages.do"

/*******************************************************************************
SECTION 4: REPRODUCIBILITY SETTINGS
*******************************************************************************/
set seed 20251222           // IMPORTANT: Set unique seed for your project
set linesize 120            
set maxvar 32000            

/*******************************************************************************
SECTION 5: AUDIT TRAIL (Timestamped Logging)
*******************************************************************************/
local datetime = subinstr("`c(current_date)' `c(current_time)'", " ", "_", .)
local datetime = subinstr("`datetime'", ":", "-", .)

log using "$logs/master_`datetime'.log", replace text name(masterlog)

/*******************************************************************************
SECTION 6: SEQUENTIAL EXECUTION
*******************************************************************************/

* display as result "Stage 1: Data Preparation"
* do "$scripts/data_preparation/01_clean.do"

* display as result "Stage 2: Analysis"
* do "$scripts/analysis/01_main_regressions.do"

* display as result "Stage 3: Validation"
* do "$scripts/validation/01_robustness.do"

display ""
display as result "{{hline 78}}"
display as result "PROJECT EXECUTION COMPLETED"
display as result "{{hline 78}}"

log close masterlog
""", encoding="utf-8")
    print("  + 02_scripts/00_master.do")

    # 2. 00_master.py (Python)
    master_py = template_root / "02_scripts" / "00_master.py"
    master_py.write_text(f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
MASTER EXECUTION SCRIPT - 00_master.py

Project:     {project_name}
Purpose:     One-click reproducible execution of entire project in Python
Standards:   J-PAL (MIT) | DIME (World Bank) | AEA Data Editor
\"\"\"

import os
import sys
import time
import logging
import subprocess
from pathlib import Path
from datetime import datetime

# =============================================================================
# SECTION 1: GLOBAL PATH CONFIGURATION
# =============================================================================
# Root directory (automatically detected if running from project root)
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data directories (J-PAL/DIME standard)
DATA_DIR          = PROJECT_ROOT / "01_data"
RAW_DIR           = DATA_DIR / "raw"
DEIDENTIFIED_DIR  = DATA_DIR / "de-identified"
INTERMEDIATE_DIR  = DATA_DIR / "intermediate"
FINAL_DIR         = DATA_DIR / "final"

# Script directories
SCRIPTS_DIR       = PROJECT_ROOT / "02_scripts"
CODE_CHECKS       = SCRIPTS_DIR / "01_data_checks"

# Output directories (AEA standard)
OUTPUTS_DIR       = PROJECT_ROOT / "03_outputs"
TABLES_DIR        = OUTPUTS_DIR / "tables"
FIGURES_DIR       = OUTPUTS_DIR / "figures"
LOGS_DIR          = OUTPUTS_DIR / "logs"

# Ensure output directories exist
for d in [TABLES_DIR, FIGURES_DIR, LOGS_DIR]:
    d.mkdir(parents=True, exist_ok=True)

# =============================================================================
# SECTION 2: AUDIT TRAIL (Timestamped Logging)
# =============================================================================
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = LOGS_DIR / f"master_{{timestamp}}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("="*78)
logging.info(f"PROJECT: {project_name}")
logging.info("="*78)
logging.info(f"Root:      {{PROJECT_ROOT}}")
logging.info(f"Started:   {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
logging.info(f"Python:    {{sys.version.split()[0]}}")
logging.info("="*78)

# =============================================================================
# SECTION 3: REPRODUCIBILITY SETTINGS
# =============================================================================
# Set seeds across common data science libraries if they are installed
GLOBAL_SEED = 20251222

try:
    import numpy as np
    np.random.seed(GLOBAL_SEED)
except ImportError:
    pass

try:
    import pandas as pd
    import random
    random.seed(GLOBAL_SEED)
except ImportError:
    pass

logging.info(f"Global Random Seed Set: {{GLOBAL_SEED}}")

# =============================================================================
# SECTION 4: SEQUENTIAL EXECUTION PIPELINE
# =============================================================================
def run_script(script_path):
    if not script_path.exists():
        logging.warning(f"Script not found (Skipping): {{script_path.relative_to(PROJECT_ROOT)}}")
        return
        
    logging.info(f"\\n>>> Executing Stage: {{script_path.relative_to(PROJECT_ROOT)}}")
    start_time = time.time()
    
    # Run script as a subprocess maintaining the environment
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    
    duration = time.time() - start_time
    
    if result.returncode != 0:
        logging.error(f"Error in: {{script_path.name}}")
        logging.error(result.stderr)
        sys.exit(1)
    else:
        logging.info(f"Success ({{duration:.1f}}s). Output:\\n{{result.stdout}}")

def main():
    # Uncomment scripts as you develop them. Run in numerical order.
    
    # logging.info("\\n--- STAGE 1: Data Preparation ---")
    # run_script(SCRIPTS_DIR / "data_preparation" / "01_import.py")
    # run_script(SCRIPTS_DIR / "data_preparation" / "02_clean.py")
    
    # logging.info("\\n--- STAGE 2: Analysis ---")
    # run_script(SCRIPTS_DIR / "analysis" / "01_main_models.py")
    
    # logging.info("\\n--- STAGE 3: Validation ---")
    # run_script(SCRIPTS_DIR / "validation" / "01_robustness.py")
    
    logging.info("\\n" + "="*78)
    logging.info("PROJECT EXECUTION COMPLETED")
    logging.info("="*78)

if __name__ == "__main__":
    main()
""", encoding="utf-8")
    print("  + 02_scripts/00_master.py")

    # 3. stata_packages.do
    stata_pkgs = template_root / "02_scripts" / "utilities" / "stata_packages.do"
    stata_pkgs.write_text("""* Manejador de Dependencias Base (AEA Standard)

local ssc_packages "reghdfe ftools ivreg2 estout coefplot blindfolds rddensity rdrobust outreg2"

foreach pkg in `ssc_packages' {
    capture which `pkg'
    if _rc == 111 {
        ssc install `pkg', replace
    }
}
disp "Todos los paquetes de Stata base instalutilities."
""", encoding="utf-8")
    print("  + 02_scripts/utilities/stata_packages.do")

    # 4. requirements.txt
    reqs = template_root / "requirements.txt"
    reqs.write_text("""pandas>=2.0.0
geopandas>=0.13.0
statsmodels>=0.14.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
google-generativeai==0.5.2
PyMuPDF==1.24.4
""", encoding="utf-8")
    print("  + requirements.txt")

    # 5. LICENSE (MIT)
    license_file = template_root / "LICENSE"
    license_file.write_text("""MIT License

Copyright (c) 2026 Maykol Medrano

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
""", encoding="utf-8")
    print("  + LICENSE")

    print(f"\n¡ÉXITO! Tu nuevo proyecto está listo en:\n{template_root}")
    print("\nSugerencia: Abre esa carpeta, inicia un repo en GitHub (`git init`) y ")
    print("comienza a investigar.")

if __name__ == "__main__":
    main()
