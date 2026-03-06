* Manejador de Dependencias Base (AEA Standard)

local ssc_packages "reghdfe ftools ivreg2 estout coefplot blindfolds rddensity rdrobust outreg2"

foreach pkg in `ssc_packages' {
    capture which `pkg'
    if _rc == 111 {
        ssc install `pkg', replace
    }
}
disp "Todos los paquetes de Stata base instalutilities."
