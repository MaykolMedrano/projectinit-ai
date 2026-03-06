/*
Template Estandar DIME -- Ejecucion en Stata
=========================================================
Creador:  Usar este esqueleto para todos los scripts de Stata.
Requisitos: reghdfe, estout, ftools
*/

clear all
set more off
capture log close

// -- Rutas (Ajustadas automaticamente por el Creador) --
global BASE "..." // Configurar ruta raiz dinamicamente
global DATA_IN "${BASE}/01_data/intermediate"
global DATA_OUT "${BASE}/01_data/final"
global TABLES "${BASE}/03_outputs/tables"
global FIGURES "${BASE}/03_outputs/figures"
global LOGS "${BASE}/03_outputs/logs"

// -- Iniciar Log --
log using "${LOGS}/nombre_script.log", replace text

disp "========================================================="
disp " INICIANDO ESTIMACION: [METODO] (Ej. RDD Especificacion Principal)"
disp "========================================================="

// 1. Cargar Datos
// use "${DATA_IN}/datos_limpios.dta", clear

// 2. Definicion de Variables (Checklist Causal)
// global y var_dependiente
// global treat tratamiento
// global controls var1 var2

// 3. Estimacion Principal
// reghdfe $y $treat $controls, absorb(efecto1 efecto2) vce(cluster var_cluster)
// est store modelo1

// 4. Salida de Tablas (Estilo AER / LaTeX booktabs)
/*
esttab modelo1 using "${TABLES}/tabla_resultutilities.tex", ///
    replace booktabs ///
    se(%9.4f) b(%9.4f) star(* 0.10 ** 0.05 *** 0.01) ///
    keep($treat) ///
    stats(N r2, fmt(%9.0fc %9.3f) labels("Observations" "$ R^2 $")) ///
    addnotes("Standard errors in parentheses clustered at the ... level.")
*/

disp "========================================================="
disp " EJECUCION COMPLETADA CON EXITO"
disp "========================================================="

log close
exit, clear
