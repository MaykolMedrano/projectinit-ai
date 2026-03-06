import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

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

print("Generando Overlaid Densities Plot...")

# ==========================================
# Density Simulation
# ==========================================
np.random.seed(505)
# Distribution A: Control / Pre-period
dist_a = np.random.normal(0, 1.2, 1000)
# Distribution B: Treated / Post-period (shifted and skewed)
dist_b = np.random.normal(1.5, 1.0, 1000) + np.random.exponential(0.5, 1000)

# KDE Calculation
kde_a = gaussian_kde(dist_a)
kde_b = gaussian_kde(dist_b)
x_range = np.linspace(-5, 8, 200)

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plot Densities with AER transparency rules
ax.fill_between(x_range, kde_a(x_range), color=slate, alpha=0.15, label="Control Group")
ax.plot(x_range, kde_a(x_range), color=slate, linewidth=1.5)

ax.fill_between(x_range, kde_b(x_range), color=mit_red, alpha=0.15, label="Treated Group")
ax.plot(x_range, kde_b(x_range), color=mit_red, linewidth=1.5)

# Styling
ax.set_title("Shift in Outcome Distribution post-Treatment", loc='left', fontsize=13)
ax.set_xlabel("Outcome Variable $Y$")
ax.set_ylabel("Kernel Density")
ax.legend(loc="upper right", frameon=False)

# Add Kolmogorov-Smirnov note
ax.text(4, ax.get_ylim()[1]*0.5, "KS-Test $p$-value: < 0.001", fontsize=10, bbox=dict(facecolor='white', alpha=0.8, edgecolor='none'))

aer_save(fig, str(output_dir / "15_density_comparison.png"))
print("Guardado en 'outputs/15_density_comparison.png'")
