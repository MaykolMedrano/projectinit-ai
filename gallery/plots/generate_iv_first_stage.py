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

print("Generando IV Dashboard (First Stage & Reduced Form)...")

# ==========================================
# IV Simulation
# ==========================================
np.random.seed(303)
# Let Z be the instrument (e.g., lottery win)
Z = np.random.uniform(0, 10, 200)
# First Stage: D (Endogenous) = alpha * Z + eta
D = 2 + 0.8 * Z + np.random.normal(0, 1.5, 200)
# Reduced Form: Y = beta * Z + epsilon
Y = 5 + 0.5 * Z + np.random.normal(0, 2, 200)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Panel A: First Stage
aer_format_axes(ax1)
ax1.plot(Z, D, 'o', color=slate, markersize=4.5, alpha=0.5)
ax1.plot(Z, 2 + 0.8 * Z, color=slate, linewidth=1.1, label="First-Stage Prediction")
ax1.set_title("Panel A: First Stage ($Z \\to D$)", loc='left', fontsize=12)
ax1.set_xlabel("Instrument ($Z$)")
ax1.set_ylabel("Endogenous Regressor ($D$)")
ax1.legend(loc="upper left", frameon=False)

# Panel B: Reduced Form
aer_format_axes(ax2)
ax2.plot(Z, Y, 's', color=mit_red, markersize=4.5, alpha=0.5)
ax2.plot(Z, 5 + 0.5 * Z, color=mit_red, linewidth=1.1, label="Reduced Form Fit")
ax2.set_title("Panel B: Reduced Form ($Z \\to Y$)", loc='left', fontsize=12)
ax2.set_xlabel("Instrument ($Z$)")
ax2.set_ylabel("Outcome Variable ($Y$)")
ax2.legend(loc="upper left", frameon=False)

plt.tight_layout()
aer_save(fig, str(output_dir / "13_iv_dashboard.png"))
print("Guardado en 'outputs/13_iv_dashboard.png'")
