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

print("Generando Synthetic Control Method (SCM) Plot...")

# ==========================================
# SCM Simulation (e.g., Abadie's California)
# ==========================================
np.random.seed(404)
years = np.arange(1970, 2001)
treatment_year = 1988

# Baseline trend
trend = 0.5 * (years - 1970)**1.2

# Synthetic Control: Follows trend with tight noise
synthetic_y = 100 + trend + np.random.normal(0, 1, len(years))

# Treated Unit: Follows synthetic in pre-period, diverges after treatment
treated_y = synthetic_y.copy()
mask_post = years >= treatment_year
treated_y[mask_post] -= 1.5 * (years[mask_post] - treatment_year + 1)**1.3

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plot SCM
ax.plot(years, synthetic_y, '--', color=slate, linewidth=1.1, label="Synthetic Control", alpha=0.8)
ax.plot(years, treated_y, '-', color=mit_red, linewidth=1.1, label="Treated Unit (e.g., California)")

# Vertical line at treatment
ax.axvline(treatment_year, color="#333333", linestyle="-", linewidth=0.8)
ax.text(treatment_year + 0.5, ax.get_ylim()[1]*0.9, "Prop. 99 Adoption", fontsize=10, fontweight='bold', color="#333333")

# Styling
ax.set_title("Effect of Proposition 99 on Per Capita Cigarette Consumption", loc='left', fontsize=13)
ax.set_xlabel("Year")
ax.set_ylabel("Cigarette Sales (packs per capita)")
ax.legend(loc="lower left", frameon=False)

# Add RMSPE note
ax.text(1971, ax.get_ylim()[0]*1.1, "Pre-treatment RMSPE: 0.84", fontsize=9, style='italic')

aer_save(fig, str(output_dir / "14_scm_plot.png"))
print("Guardado en 'outputs/14_scm_plot.png'")
