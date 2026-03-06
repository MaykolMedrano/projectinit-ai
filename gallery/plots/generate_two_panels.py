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

print("Generando Gráfico de 2 Paneles (A/B)...")

# Data Simulation
np.random.seed(123)
x = np.linspace(0, 10, 100)
y1 = 2 + 0.5 * x + np.random.normal(0, 0.5, 100)
y2 = 5 - 0.3 * x + np.random.normal(0, 0.5, 100)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Panel A
aer_format_axes(ax1)
ax1.plot(x, y1, 'o', color=slate, markersize=4, alpha=0.6)
ax1.plot(x, 2 + 0.5 * x, color=slate, linewidth=1.05)
ax1.set_title("Panel A: Positive Correlation", loc='left', fontsize=12)
ax1.set_xlabel("Independent Variable $X_1$")
ax1.set_ylabel("Outcome $Y$")

# Panel B
aer_format_axes(ax2)
ax2.plot(x, y2, 's', color=mit_red, markersize=4, alpha=0.6)
ax2.plot(x, 5 - 0.3 * x, color=mit_red, linewidth=1.05)
ax2.set_title("Panel B: Negative Correlation", loc='left', fontsize=12)
ax2.set_xlabel("Independent Variable $X_2$")
ax2.set_ylabel("Outcome $Y$")

plt.tight_layout()
aer_save(fig, str(output_dir / "7_two_panels.png"))
print("Guardado en 'outputs/7_two_panels.png'")
