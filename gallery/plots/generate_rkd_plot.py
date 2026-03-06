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

print("Generando Regression Kink Design (RKD)...")

# ==========================================
# RKD Simulation
# ==========================================
np.random.seed(202)
x = np.linspace(-5, 5, 200)
threshold = 0

# Kink: slope changes from 0.5 to 1.5 at the threshold
y = 10 + 0.5 * x + 1.0 * (x - threshold) * (x > threshold)
noise = np.random.normal(0, 0.4, 200)
y_obs = y + noise

# Binning for the scatter
bins = np.linspace(-5, 5, 25)
bin_centers = (bins[:-1] + bins[1:]) / 2
bin_means = [y_obs[(x >= bins[i]) & (x < bins[i+1])].mean() for i in range(len(bins)-1)]

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plot Binned Means
ax.plot(bin_centers, bin_means, 'o', color=slate, markersize=5, alpha=0.5, label="Binned Means")

# Plot Kink Lines
x_left = np.linspace(-5, 0, 100)
x_right = np.linspace(0, 5, 100)
ax.plot(x_left, 10 + 0.5 * x_left, color=slate, linewidth=1.1)
ax.plot(x_right, 10 + 0.5 * x_right + 1.0 * x_right, color=mit_red, linewidth=1.1, label="Linear Fits")

# Visual aid at kink
ax.axvline(0, color="#AAAAAA", linestyle=":", linewidth=1.0)

# Styling
ax.set_title("Regression Kink Design (RKD): UI Benefit Slope Change", loc='left', fontsize=13)
ax.set_xlabel("Running Variable (e.g., Previous Earnings)")
ax.set_ylabel("Outcome (e.g., Unemployment Duration)")
ax.legend(loc="upper left", frameon=False)

aer_save(fig, str(output_dir / "12_rkd_plot.png"))
print("Guardado en 'outputs/12_rkd_plot.png'")
