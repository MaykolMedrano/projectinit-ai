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

print("Generando SCM Placebo Test (Spaghetti Plot)...")

# ==========================================
# SCM Placebo Simulation
# ==========================================
np.random.seed(606)
years = np.arange(1970, 2001)
treatment_year = 1988

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Simulate 20 Placebo Units (Control donor pool)
for i in range(20):
    noise = np.random.normal(0, 1.2, len(years))
    trend = 0.5 * (years - 1970)**1.2
    # Placebos have no treatment effect, just noise around trend
    placebo_gap = np.random.normal(0, 0.8, len(years))
    ax.plot(years, placebo_gap, color='#CCCCCC', linewidth=0.8, alpha=0.5)

# Simulate Treated Unit Gap (The true effect)
true_gap = np.random.normal(0, 0.8, len(years))
mask_post = years >= treatment_year
true_gap[mask_post] -= 1.8 * (years[mask_post] - treatment_year + 1)**1.2

ax.plot(years, true_gap, color=mit_red, linewidth=1.1, label="Treated Unit (Gap)")

# Visual Aids
ax.axhline(0, color="#333333", linestyle="-", linewidth=1.0)
ax.axvline(treatment_year, color="#666666", linestyle="--", linewidth=1.0)

# Styling
ax.set_title("SCM Placebo Test: Gap in Per Capita Cigarette Sales", loc='left', fontsize=13)
ax.set_xlabel("Year")
ax.set_ylabel("Gap (Treated - Synthetic Control)")
ax.legend(loc="lower left", frameon=False)

# Add p-value note
ax.text(1971, ax.get_ylim()[0]*0.9, "Empirical $p$-value: 0.047", fontsize=10, fontweight='bold')

aer_save(fig, str(output_dir / "17_scm_placebo.png"))
print("Guardado en 'outputs/17_scm_placebo.png'")
