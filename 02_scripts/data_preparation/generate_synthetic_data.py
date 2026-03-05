"""
Generación de Datos Sintéticos — Dry Run Contractor Mode
=========================================================
Simula un panel de avalúos fiscales con discontinuidad espacial
generada por proximidad a estaciones de metro.

Output: 01_data/intermediate/synthetic_rdd_panel.csv
"""

import numpy as np
import pandas as pd
from pathlib import Path

# ── Config ───────────────────────────────────────────────────
SEED = 42
N = 5_000
CUTOFF_KM = 1.0
TRUE_EFFECT = 0.15  # +15% en log(avalúo) para propiedades < 1 km

OUTPUT_DIR = Path(__file__).resolve().parents[2] / "01_data" / "intermediate"
OUTPUT_FILE = OUTPUT_DIR / "synthetic_rdd_panel.csv"

# ── Generación ───────────────────────────────────────────────
np.random.seed(SEED)

# Running variable: distancia al metro (0.05 a 5 km, distribución uniforme)
distancia_metro = np.random.uniform(0.05, 5.0, N)

# Tratamiento: propiedades dentro del cutoff
tratamiento = (distancia_metro < CUTOFF_KM).astype(int)

# Covariables (correlacionadas con distancia pero no colineales)
superficie_m2 = 50 + 80 * np.random.beta(2, 3, N) + 10 * distancia_metro + np.random.normal(0, 5, N)
antiguedad = np.clip(5 + 30 * np.random.beta(2, 5, N) - 3 * distancia_metro + np.random.normal(0, 3, N), 0, 80)
n_dormitorios = np.clip(np.round(1 + 2.5 * np.random.beta(3, 3, N) + 0.3 * (superficie_m2 / 50)), 1, 6).astype(int)
comuna_id = np.random.choice(range(1, 11), N)  # 10 comunas

# Outcome: log(avalúo) con efecto causal en el cutoff
log_avaluo_base = (
    8.5                                          # intercepto
    + 0.005 * superficie_m2                     # más grande = más caro
    - 0.008 * antiguedad                        # más viejo = más barato
    + 0.08 * n_dormitorios                      # más dormitorios = más caro
    - 0.1 * distancia_metro                     # gradiente de precio por distancia
    + np.random.normal(0, 0.3, N)               # ruido
)

# Inyectar efecto causal discontinuo
log_avaluo = log_avaluo_base + TRUE_EFFECT * tratamiento

# ── DataFrame ────────────────────────────────────────────────
df = pd.DataFrame({
    "propiedad_id": range(1, N + 1),
    "distancia_metro_km": np.round(distancia_metro, 4),
    "tratamiento": tratamiento,
    "log_avaluo": np.round(log_avaluo, 6),
    "superficie_m2": np.round(superficie_m2, 1),
    "antiguedad": np.round(antiguedad, 1),
    "n_dormitorios": n_dormitorios,
    "comuna_id": comuna_id,
})

# ── Guardar ──────────────────────────────────────────────────
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
df.to_csv(OUTPUT_FILE, index=False)

# ── Validación de dimensiones ────────────────────────────────
print(f"="*60)
print(f"ETL SYNTHETIC DATA - VALIDACIÓN")
print(f"="*60)
print(f"Filas generadas:    {len(df):,}")
print(f"Columnas:           {list(df.columns)}")
print(f"Tratados (< 1km):   {tratamiento.sum():,} ({tratamiento.mean():.1%})")
print(f"Control  (>=1km):   {(1-tratamiento).sum():,.0f} ({1-tratamiento.mean():.1%})")
print(f"Efecto inyectado:   {TRUE_EFFECT} ({TRUE_EFFECT:.0%})")
print(f"Cutoff:             {CUTOFF_KM} km")
print(f"Output guardado en: {OUTPUT_FILE}")
print(f"\nEstadísticas descriptivas:")
print(df.describe().round(3).to_string())
print(f"\nMissing values:")
print(df.isnull().sum().to_string())
print(f"="*60)
