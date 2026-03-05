/*******************************************************************************
* MASTER EXECUTION SCRIPT - 00_master.do
*
* Project:     projectinit-ai-repo
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
global ados          "$scripts/ados"
global datachecks    "$scripts/01_data_checks"

* Output directories (AEA standard)
global outputs       "$root/03_outputs"
global tables        "$outputs/tables"
global figures       "$outputs/figures"
global logs          "$outputs/logs"

* Documentation & Admin
global doc           "$root/05_doc"
global admin         "$root/06_admin"

display as result "{hline 78}"
display as result "PROJECT: projectinit-ai-repo"
display as result "{hline 78}"
display as text "Root:      $root"
display as text "Started:   `c(current_date)' `c(current_time)'"
display as result "{hline 78}"

/*******************************************************************************
SECTION 2: ENVIRONMENT ISOLATION (NBER Standard)
*******************************************************************************/
* Add local ado directory to search path (highest priority)
adopath ++ "$ados"

/*******************************************************************************
SECTION 3: DEPENDENCY MANAGEMENT 
*******************************************************************************/
* Ensure core packages are installed
capture do "$ados/stata_packages.do"

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
display as result "{hline 78}"
display as result "PROJECT EXECUTION COMPLETED"
display as result "{hline 78}"

log close masterlog
