import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurar ruta a los scripts de la plantilla
root = Path(r"e:\00_Desktop\projectinit-ai-repo")
sys.path.append(str(root / "projectinit_ai" / "template" / "02_scripts" / "ados"))

from aer_style import configure_aer_style, aer_format_axes, aer_save, AER_COLORS

# Configurar Estilo AER Puro
configure_aer_style()

slate = AER_COLORS[0]
mit_red = AER_COLORS[1]
output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

print("Generando DiD Parallel Trends...")

# ==========================================
# Parallel Trends Simulation
# ==========================================
np.random.seed(777)
years = np.arange(2010, 2021)
treatment_year = 2015

# Baseline trend
base_trend = 0.5 * (years - 2010)

# Control Group: Baseline trend + noise
control_y = 10 + base_trend + np.random.normal(0, 0.1, len(years))
control_se = 0.15 + 0.01 * (years - 2010)

# Treatment Group: Baseline trend + divergence after treatment
treatment_y = 10 + base_trend + np.random.normal(0, 0.1, len(years))
mask_post = years >= treatment_year
treatment_y[mask_post] += 1.5 * (years[mask_post] - treatment_year + 1)**0.6
treatment_se = 0.15 + 0.01 * (years - 2010)

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plotting Trends
ax.plot(years, control_y, 'o-', color=slate, linewidth=1.2, markersize=4.5, label="Control Group", alpha=0.9)
ax.fill_between(years, control_y - 1.96*control_se, control_y + 1.96*control_se, color=slate, alpha=0.1, linewidth=0)

ax.plot(years, treatment_y, 's-', color=mit_red, linewidth=1.2, markersize=4.5, label="Treatment Group", alpha=0.9)
ax.fill_between(years, treatment_y - 1.96*treatment_se, treatment_y + 1.96*treatment_se, color=mit_red, alpha=0.1, linewidth=0)

# Vertical line at treatment
ax.axvline(treatment_year - 0.5, color="#888888", linestyle="--", linewidth=1.0)
ax.text(treatment_year - 0.4, ax.get_ylim()[1]*0.95, "Policy Adoption", fontsize=10, color="#666666")

ax.set_xlabel("Year")
ax.set_ylabel("Outcome Variable (Log Scale)")
ax.set_xticks(years)
ax.legend(loc="upper left", frameon=False)

aer_save(fig, str(output_dir / "9_parallel_trends.png"))
print("Guardado en 'outputs/9_parallel_trends.png'")
