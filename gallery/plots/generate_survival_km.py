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

print("Generando Survival Analysis (Kaplan-Meier)...")

# ==========================================
# Survival (KM) Simulation
# ==========================================
time = np.linspace(0, 50, 100)

# Group A: Control (Fast decay)
surv_a = np.exp(-0.08 * time)
# Group B: Treated (Slow decay / Persistence)
surv_b = np.exp(-0.04 * time)

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plot KM Curves (Step-wise behavior)
ax.step(time, surv_a, where='post', color=slate, linewidth=1.1, label="Control Group")
ax.fill_between(time, surv_a*0.9, surv_a*1.1, color=slate, alpha=0.1, step='post')

ax.step(time, surv_b, where='post', color=mit_red, linewidth=1.1, label="Treated Group")
ax.fill_between(time, surv_b*0.92, surv_b*1.08, color=mit_red, alpha=0.1, step='post')

# Styling
ax.set_title("Kaplan-Meier Survival Estimates: Time to Re-employment", loc='left', fontsize=13)
ax.set_xlabel("Weeks since Layoff")
ax.set_ylabel("Probability of Remaining Unemployed")
ax.set_ylim(0, 1.05)
ax.legend(loc="upper right", frameon=False)

# Add Hazard Ratio note
ax.text(5, 0.2, "Hazard Ratio: 0.52 (0.41, 0.65)\nLog-rank $p < 0.001$", fontsize=10, bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

aer_save(fig, str(output_dir / "18_survival_km.png"))
print("Guardado en 'outputs/18_survival_km.png'")
