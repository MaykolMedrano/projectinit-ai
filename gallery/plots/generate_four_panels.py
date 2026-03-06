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

print("Generando Gráfico de 4 Paneles (Grid 2x2)...")

# Data Simulation
np.random.seed(456)
x = np.linspace(-5, 5, 100)

fig, axs = plt.subplots(2, 2, figsize=(12, 10))
axs = axs.flatten()

titles = ["Panel A: Linear", "Panel B: Quadratic", "Panel C: Logit", "Panel D: Noise"]
colors = [slate, mit_red, slate, mit_red]
markers = ['o', 's', '^', 'D']

for i in range(4):
    ax = axs[i]
    aer_format_axes(ax)
    
    if i == 0: y = 0.5 * x
    elif i == 1: y = 0.2 * x**2
    elif i == 2: y = 1 / (1 + np.exp(-x))
    else: y = np.random.normal(0, 1, 100)
    
    noise = np.random.normal(0, 0.2, 100)
    ax.plot(x, y + noise, markers[i], color=colors[i], markersize=3.5, alpha=0.6)
    ax.plot(x, y, color=colors[i], linewidth=1.05)
    
    ax.set_title(titles[i], loc='left', fontsize=11)
    ax.set_xlabel(f"Regresor $X_{i+1}$")
    ax.set_ylabel("Response")

plt.tight_layout()
aer_save(fig, str(output_dir / "8_four_panels.png"))
print("Guardado en 'outputs/8_four_panels.png'")
