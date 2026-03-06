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
steel_blue = AER_COLORS[2]
ochre = AER_COLORS[3]

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

print("Generando Heterogeneous Treatment Effects (HTE) Plot...")

# ==========================================
# HTE Simulation (By Subgroups)
# ==========================================
groups = ['Full Sample', 'Gender', '  Female', '  Male', 'Residence', '  Rural', '  Urban', 'Education', '  High School', '  University']
point_est = [0.85, np.nan, 0.92, 0.78, np.nan, 1.05, 0.65, np.nan, 0.82, 0.88]
conf_low = [0.75, np.nan, 0.80, 0.65, np.nan, 0.85, 0.50, np.nan, 0.70, 0.75]
conf_high = [0.95, np.nan, 1.04, 0.91, np.nan, 1.25, 0.80, np.nan, 0.94, 1.01]

fig, ax = plt.subplots(figsize=(10, 7))
aer_format_axes(ax)

# Reverse for vertical display
groups.reverse()
point_est.reverse()
conf_low.reverse()
conf_high.reverse()

y_pos = np.arange(len(groups))

for i in range(len(groups)):
    if np.isnan(point_est[i]):
        # Category header
        ax.text(ax.get_xlim()[0] - 0.1, y_pos[i], groups[i], verticalalignment='center', fontweight='bold', fontsize=11)
    else:
        # Data point
        color = slate if 'Full' in groups[i] else steel_blue
        ax.errorbar(point_est[i], y_pos[i], xerr=[[point_est[i]-conf_low[i]], [conf_high[i]-point_est[i]]], 
                    fmt='o', color=color, markersize=6, elinewidth=1.2, capsize=0)
        ax.text(ax.get_xlim()[0] - 0.05, y_pos[i], groups[i], verticalalignment='center', fontsize=10)

# Reference line at zero or full sample
ax.axvline(0.85, color=slate, linestyle=":", linewidth=0.8, alpha=0.5, label="Average Treatment Effect")
ax.axvline(0, color="#333333", linestyle="-", linewidth=1.0)

# Styling
ax.set_title("Heterogeneity in Treatment Effects on Labor Supply", loc='left', fontsize=13)
ax.set_xlabel("Estimated Coefficient ($\hat{\\beta}$)")
ax.set_yticks([]) # Labels are custom text
ax.legend(loc="lower right", frameon=False)

aer_save(fig, str(output_dir / "16_hte_subgroups.png"))
print("Guardado en 'outputs/16_hte_subgroups.png'")
