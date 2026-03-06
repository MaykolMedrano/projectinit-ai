"""
Generacion de datos sinteticos para panel DiD
===================================================
Dry Run 2: Verificando reglas de separacion de scripts.
"""

import pandas as pd
import numpy as np
from pathlib import Path

# Paths DIME
BASE_DIR = Path(__file__).resolve().parents[2]
OUTPUT_DIR = BASE_DIR / "01_data" / "intermediate"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

def generate_did_data(n_units=500, n_periods=10, treatment_period=5):
    np.random.seed(42)
    
    # Unidades
    units = pd.DataFrame({
        "unit_id": range(1, n_units + 1),
        "treated": np.random.binomial(1, 0.5, n_units),
        "unit_fe": np.random.normal(10, 2, n_units)
    })
    
    # Tiempo
    periods = pd.DataFrame({
        "time_id": range(1, n_periods + 1),
        "time_fe": np.sin(np.linspace(0, 2*np.pi, n_periods))
    })
    
    # Panel
    df = units.merge(periods, how="cross")
    
    # Variables DiD
    df["post"] = (df["time_id"] >= treatment_period).astype(int)
    df["T_P"] = df["treated"] * df["post"]
    
    # Efecto dinamico (Parallel trends holds pre-treatment, effect phases in)
    true_effect = 0.5
    # Let's say effect grows linearly from treatment time
    df["dynamic_effect"] = np.where(
        (df["treated"] == 1) & (df["time_id"] >= treatment_period),
        true_effect * (df["time_id"] - treatment_period + 1),
        0
    )
    
    # Outcome (y_it = unit_fe + time_fe + treatment_effect + error)
    df["y"] = df["unit_fe"] + df["time_fe"] + df["dynamic_effect"] + np.random.normal(0, 1, n_units * n_periods)
    
    # Classic DiD single effect is the average over post periods
    print(f"Generated DiD Panel: {n_units} units, {n_periods} periods.")
    print(f"Treatment starts at t={treatment_period}")
    return df

if __name__ == "__main__":
    df = generate_did_data()
    out_path = OUTPUT_DIR / "synthetic_did_panel.csv"
    df.to_csv(out_path, index=False)
    print(f"Saved to: {out_path}")
