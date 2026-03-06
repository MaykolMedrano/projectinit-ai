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

print("Generando Spatial Distribution Map...")

# ==========================================
# Spatial Simulation
# ==========================================
np.random.seed(707)
# Simulate clusters of economic activity
n_points = 300
x_coord = np.random.normal(50, 20, n_points)
y_coord = np.random.normal(50, 20, n_points)

# Intensity variable (e.g., productivity)
intensity = 10 + 0.5*x_coord + 0.3*y_coord + np.random.normal(0, 10, n_points)

fig, ax = plt.subplots(figsize=(10, 8))
aer_format_axes(ax)

# Plot Spatial Scatter with Color intensity
sc = ax.scatter(x_coord, y_coord, c=intensity, s=intensity*2, cmap='YlOrRd', alpha=0.7, edgecolors='white', linewidth=0.5)
cb = plt.colorbar(sc, ax=ax, shrink=0.7, pad=0.02)
cb.set_label("Economic Activity Intensity", fontsize=10)
cb.outline.set_visible(False)

# Add spatial cluster indicator (Ellipse)
from matplotlib.patches import Ellipse
ellipse = Ellipse((50, 50), width=60, height=40, angle=30, edgecolor=mit_red, fc='none', lw=1.5, ls='--', label='Statistically Significant Cluster')
ax.add_patch(ellipse)

# Styling
ax.set_title("Spatial Distribution of Industrial Clusters", loc='left', fontsize=13)
ax.set_xlabel("Longitude (Normalized)")
ax.set_ylabel("Latitude (Normalized)")
ax.legend(loc="upper left", frameon=False)

aer_save(fig, str(output_dir / "19_spatial_distribution.png"))
print("Guardado en 'outputs/19_spatial_distribution.png'")
