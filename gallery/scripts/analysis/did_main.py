"""
Estimacion Principal DiD (Clasico)
=====================================
Dry Run 2: Especificacion principal (sin validacion de supuestos aqui).
Output en tablas de LATEX con estilo AER.
"""

import pandas as pd
import statsmodels.api as sm
from pathlib import Path
import sys

# Paths
BASE = Path(__file__).resolve().parents[2]
DATA_FILE = BASE / "01_data" / "intermediate" / "synthetic_did_panel.csv"
TABLES_DIR = BASE / "03_outputs" / "tables"
TABLES_DIR.mkdir(parents=True, exist_ok=True)

# AER Style
sys.path.insert(0, str(BASE / "02_scripts"))
from utilities.aer_style import AERTable

# Data
df = pd.read_csv(DATA_FILE)

# -- Estimacion 1: Pooled OLS (naive) --
# y = a + b1*(Treated) + b2*(Post) + bD*(T_P) + e
X_pooled = sm.add_constant(df[["treated", "post", "T_P"]])
m_pooled = sm.OLS(df["y"], X_pooled).fit(cov_type="cluster", cov_kwds={"groups": df["unit_id"]})

# -- Estimacion 2: Two-Way Fixed Effects (TWFE) --
# Usamos linearmodels o creamos dummies (dado que son simulutilities y N es pequeño, uso dummies aqui, pero en la practica linearmodels/reghdfe)
try:
    from linearmodels.panel import PanelOLS
    # Set index for panel
    df_panel = df.set_index(["unit_id", "time_id"])
    exog = sm.add_constant(df_panel["T_P"])
    m_twfe = PanelOLS(df_panel["y"], exog, entity_effects=True, time_effects=True).fit(cov_type="clustered", cluster_entity=True)
except ImportError:
    # Fallback to statsmodels dummy variables if linearmodels not installed
    print("WARNING: linearmodels not found. Using statsmodels dummies for TWFE.")
    X_fe = pd.get_dummies(df["unit_id"], drop_first=True).astype(int).join(
           pd.get_dummies(df["time_id"], drop_first=True).astype(int)).join(df[["T_P"]])
    X_fe = sm.add_constant(X_fe)
    m_twfe_ols = sm.OLS(df["y"], X_fe).fit(cov_type="cluster", cov_kwds={"groups": df["unit_id"]})
    # Mocking for table
    class MockPanelResult:
        def __init__(self, res):
            self.params = res.params
            self.pvalues = res.pvalues
            self.bse = res.bse
            self.nobs = res.nobs
            self.rsquared = res.rsquared
    m_twfe = MockPanelResult(m_twfe_ols)


# Tablas AER
print("Generando tabla LaTeX...")
models = {
    "(1) Pooled": m_pooled,
    "(2) TWFE": m_twfe
}

latex_table = AERTable.regression_table(
    models,
    title="Difference-in-Differences Estimation",
    label="tab:did_main",
    dep_var="Y",
    note="SEs clustered at the unit level.",
    fe_rows={"Unit FE": ["No", "Yes"], "Time FE": ["No", "Yes"]}
)

tex_path = TABLES_DIR / "did_main_results.tex"
with open(tex_path, "w") as f:
    f.write(latex_table)

print(f"Estimacion principal lista. Tabla guardada en {tex_path}")

# Info a consola
print(f"Pooled DiD effect (T_P): {m_pooled.params['T_P']:.4f} (p={m_pooled.pvalues['T_P']:.4f})")
if hasattr(m_twfe, 'params'):
    print(f"TWFE DiD effect (T_P): {m_twfe.params['T_P']:.4f} (p={m_twfe.pvalues['T_P']:.4f})")
