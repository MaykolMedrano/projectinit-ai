import sys
from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.api as sm
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

print("Generando Event Study Largo (Stata Style)...")

# ==========================================
# Event Study (Long Horizon: -20 to 25)
# ==========================================
np.random.seed(111)

time_to_treat = np.arange(-20, 26) # length 46
# Pre-trends ultra planas con fluctuación pequeña
pre = np.random.normal(0, 0.03, 19) 
base = 0.0 
# Impacto dinámico logarítmico (crecimiento sostenido con decrecimiento marginal post tratamiento)
x_post = np.arange(1, 27)
post = 0.8 * np.log(x_post + 1) + np.random.normal(0, 0.04, 26)
coefs = np.concatenate([pre, [base], post])

# Standard errors tipo Stata (Campana: bajos en el centro, muy altos en los extremos)
ses = 0.04 + 0.005 * (np.abs(time_to_treat)**1.2) + np.random.uniform(-0.01, 0.01, 46)
ci_mult = 1.96

fig, ax = plt.subplots(figsize=(12, 6))
aer_format_axes(ax)

ax.axhline(0, color="#666666", linestyle="-", linewidth=1.0, zorder=1)
ax.axvline(-1, color="#888888", linestyle="--", linewidth=1.0, zorder=1)

# PURE STATA STYLE:
# Líneas verticales puras (capsize=0), gris un poco traslúcido o rojo fino
ax.errorbar(time_to_treat, coefs, yerr=ci_mult*ses, fmt='none', ecolor=mit_red, elinewidth=0.8, capsize=0, alpha=0.85, zorder=2)

# Línea conectora muy delgada
ax.plot(time_to_treat, coefs, color=slate, linewidth=1.05, zorder=3)

# Puntos sólidos grises (hueco en -1)
ax.plot(time_to_treat, coefs, "o", markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.5, markersize=5, zorder=4)
ax.plot(-1, 0, "o", markerfacecolor="white", markeredgecolor=slate, markeredgewidth=1.0, markersize=6, zorder=5)

ax.set_xlabel("Quarters Relative to Shock ($k$)")
ax.set_ylabel("Estimated Dynamic Treatment Effect ($\hat{\\beta}_k$)")
ax.set_xticks(np.arange(-20, 26, 5))

aer_save(fig, str(output_dir / "event_study_massive.png"))

print("Guardado en 'outputs/event_study_massive.png'")
