"""
Validacion de Supuestos DiD -- Event Study (Tendencias Paralelas)
=================================================================
Dry Run 2: Verificacion de la arquitectura (separacion de scripts de robustez).
Debe usar estilo AER para el grafico. Output a 03_outputs/figures/.
"""

import pandas as pd
import numpy as np
import statsmodels.api as sm
from pathlib import Path
import sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Paths
BASE = Path(__file__).resolve().parents[2]
DATA_FILE = BASE / "01_data" / "intermediate" / "synthetic_did_panel.csv"
FIGURES_DIR = BASE / "03_outputs" / "figures"
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

# AER Style
sys.path.insert(0, str(BASE / "02_scripts"))
from utilities.aer_style import configure_aer_style
configure_aer_style()

# Data
df = pd.read_csv(DATA_FILE)

# -- Relative Time (Event Study) --
treatment_period = 5
df["rel_time"] = df["time_id"] - treatment_period

# Create lag/lead dummies
lags_leads = range(-4, 6) # From -4 to +5
for k in lags_leads:
    df[f"lag_lead_{k}"] = (df["treated"] == 1) & (df["rel_time"] == k)
    df[f"lag_lead_{k}"] = df[f"lag_lead_{k}"].astype(int)

# Omitted category is usually t=-1
omit = -1
covariates = [f"lag_lead_{k}" for k in lags_leads if k != omit]

# TWFE using statsmodels (standard OLS with unit/time dummies)
X_units = pd.get_dummies(df["unit_id"], drop_first=True, prefix="u").astype(int)
X_time = pd.get_dummies(df["time_id"], drop_first=True, prefix="t").astype(int)

X_cols = X_units.join(X_time).join(df[covariates])
X_cols = sm.add_constant(X_cols)

print("Running Event Study estimation...")
m_event = sm.OLS(df["y"], X_cols).fit(cov_type="cluster", cov_kwds={"groups": df["unit_id"]})

# Extract coefficients and CIs
coefs = []
errors = []
lower_err = []
upper_err = []

for k in lags_leads:
    if k == omit:
        coefs.append(0)
        errors.append([0, 0])
        continue
        
    var_name = f"lag_lead_{k}"
    beta = m_event.params[var_name]
    ci = m_event.conf_int().loc[var_name]
    
    coefs.append(beta)
    # The shape for plt.errorbar yerr is (2, N)
    errors.append([beta - ci[0], ci[1] - beta])

errors = np.array(errors).T

# -- Plot AER Style --
print("Generando Event Study Plot (AER Style)...")
fig, ax = plt.subplots(figsize=(6.5, 4))

ax.errorbar(list(lags_leads), coefs, yerr=errors, fmt="o-", color="black", 
            ecolor="black", elinewidth=1, capsize=3, markersize=5, label="Estimate & 95% CI")

ax.axhline(0, color="gray", linestyle="-", linewidth=0.5)
ax.axvline(omit, color="gray", linestyle="--", linewidth=0.8, alpha=0.5, label="Omitted Period (t=-1)")

ax.set_xlabel("Years Relative to Treatment")
ax.set_ylabel("Estimated Effect on Y")
ax.legend(frameon=False, loc="upper left")

# Adhering to the new checklist requirement: Note at the bottom of the figure
# We add this directly onto the figure space below the x-axis label.
note_text = "Note: N=500 units, T=10 periods. The event study omits t=-1 as the baseline. Error bars represent 95% confidence intervals clustered at the unit level."
fig.text(0.01, -0.05, note_text, ha='left', va='top', fontsize=8, wrap=True)

fig.tight_layout()
fig_path = FIGURES_DIR / "did_event_study.png"
fig.savefig(fig_path, dpi=300, bbox_inches="tight", facecolor="white")
plt.close(fig)

print(f"Validation plot saved to {fig_path}")
