#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MASTER EXECUTION SCRIPT - 00_master.py

Project:     projectinit-ai-repo
Purpose:     One-click reproducible execution of entire project in Python
Standards:   J-PAL (MIT) | DIME (World Bank) | AEA Data Editor
"""

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
log_file = LOGS_DIR / f"master_{timestamp}.log"

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("="*78)
logging.info(f"PROJECT: projectinit-ai-repo")
logging.info("="*78)
logging.info(f"Root:      {PROJECT_ROOT}")
logging.info(f"Started:   {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
logging.info(f"Python:    {sys.version.split()[0]}")
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

logging.info(f"Global Random Seed Set: {GLOBAL_SEED}")

# =============================================================================
# SECTION 4: SEQUENTIAL EXECUTION PIPELINE
# =============================================================================
def run_script(script_path):
    if not script_path.exists():
        logging.warning(f"Script not found (Skipping): {script_path.relative_to(PROJECT_ROOT)}")
        return
        
    logging.info(f"\n>>> Executing Stage: {script_path.relative_to(PROJECT_ROOT)}")
    start_time = time.time()
    
    # Run script as a subprocess maintaining the environment
    result = subprocess.run([sys.executable, str(script_path)], capture_output=True, text=True)
    
    duration = time.time() - start_time
    
    if result.returncode != 0:
        logging.error(f"Error in: {script_path.name}")
        logging.error(result.stderr)
        sys.exit(1)
    else:
        logging.info(f"Success ({duration:.1f}s). Output:\n{result.stdout}")

def main():
    # Uncomment scripts as you develop them. Run in numerical order.
    
    # logging.info("\n--- STAGE 1: Data Preparation ---")
    # run_script(SCRIPTS_DIR / "data_preparation" / "01_import.py")
    # run_script(SCRIPTS_DIR / "data_preparation" / "02_clean.py")
    
    # logging.info("\n--- STAGE 2: Analysis ---")
    # run_script(SCRIPTS_DIR / "analysis" / "01_main_models.py")
    
    # logging.info("\n--- STAGE 3: Validation ---")
    # run_script(SCRIPTS_DIR / "validation" / "01_robustness.py")
    
    logging.info("\n" + "="*78)
    logging.info("PROJECT EXECUTION COMPLETED")
    logging.info("="*78)

if __name__ == "__main__":
    main()
