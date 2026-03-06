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

print("Generando Impulse Response Function (IRF)...")

# ==========================================
# IRF Simulation (e.g., Monetary Shock)
# ==========================================
np.random.seed(101)
horizons = np.arange(0, 21)

# Response function: A shock that peaks and then decays
response = 1.0 * np.exp(-0.2 * horizons) * np.sin(0.4 * horizons + 0.5)
# Confidence bands (asymptotic)
se = 0.15 + 0.02 * horizons

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plot IRF
ax.plot(horizons, response, 'o-', color=slate, linewidth=1.1, markersize=5, label="Impulse Response")
ax.fill_between(horizons, response - 1.96*se, response + 1.96*se, color=slate, alpha=0.1, label="95% CI")

# Zero line
ax.axhline(0, color="#333333", linewidth=1.0, linestyle="-")

# Styling
ax.set_title("Response of GDP to a 1% Interest Rate Shock", loc='left', fontsize=13)
ax.set_xlabel("Quarters after Shock")
ax.set_ylabel("Percentage Points (%)")
ax.set_xticks(horizons[::2])
ax.legend(loc="upper right", frameon=False)

aer_save(fig, str(output_dir / "11_irf_plot.png"))
print("Guardado en 'outputs/11_irf_plot.png'")
