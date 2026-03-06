import sys
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Configurar ruta a los scripts de la plantilla
root = Path(r"e:\00_Desktop\projectinit-ai-repo")
sys.path.append(str(root / "projectinit_ai" / "template" / "02_scripts" / "ados"))

from aer_style import configure_aer_style, aer_format_axes, aer_save, AER_COLORS, AER_LINESTYLES

# Configurar Estilo AER Puro
configure_aer_style()

# Use the refined palette
colors = AER_COLORS 
styles = AER_LINESTYLES # ["-", "--", ":", "-."]

output_dir = Path("outputs")
output_dir.mkdir(exist_ok=True)

print("Generando Multi-Series Time Plot (Mensual + Linestyles)...")

# ==========================================
# Multi-Series Time Plot (Monthly)
# ==========================================
np.random.seed(999)
# Usar frecuencia mensual explicita (ME en versiones nuevas de pandas)
dates = pd.date_range(start="2018-01-01", periods=36, freq='ME')
x = np.arange(len(dates))

# Series 1: Stable growth (e.g., Core Inflation)
s1 = 2 + 0.05 * x + np.random.normal(0, 0.1, len(dates))
# Series 2: Volatile (e.g., Energy Prices)
s2 = 5 + 2 * np.sin(x / 4) + np.random.normal(0, 0.5, len(dates))
# Series 3: Trend change (e.g., Interest Rates)
s3 = 1 + 0.1 * x * (x < 18) + (1.8 - 0.05 * (x-18)) * (x >= 18) + np.random.normal(0, 0.05, len(dates))
# Series 4: Benchmark (e.g., Target)
s4 = np.full(len(dates), 2.5)

fig, ax = plt.subplots(figsize=(10, 6))
aer_format_axes(ax)

# Plotting Series with variation in color and linestyle
ax.plot(dates, s1, label="Core Inflation", color=colors[0], linestyle=styles[0], linewidth=1.5)
ax.plot(dates, s2, label="Energy Prices", color=colors[1], linestyle=styles[1], linewidth=1.5)
ax.plot(dates, s3, label="Policy Rate", color=colors[2], linestyle=styles[2], linewidth=1.5)
ax.plot(dates, s4, label="Inflation Target", color=colors[3], linestyle=styles[3], linewidth=1.2)

# Styling
ax.set_xlabel("Monthly Timeline (2018-2020)")
ax.set_ylabel("Annual Percentage Rate (%)")
ax.legend(loc="upper left", ncol=2, frameon=False, fontsize=9)

# Formatting dates
fig.autofmt_xdate()

aer_save(fig, str(output_dir / "10_multi_series.png"))
print("Guardado en 'outputs/10_multi_series.png'")
