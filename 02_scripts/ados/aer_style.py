"""
AER/MIT Publication Style — Tablas y Figuras
=============================================
Modulo reutilizable que estandariza el output academico.
Basado en PublicationPlotter y AERTableBuilder de research_agent_ia.

Uso:
    from aer_style import configure_aer_style, AERTable
    configure_aer_style()  # Llamar UNA VEZ al inicio del script
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from typing import Dict, Any, List, Optional


# ═════════════════════════════════════════════════════════════════
# FIGURAS — Estilo AER/QJE/JPE
# ═════════════════════════════════════════════════════════════════

def configure_aer_style():
    """Configura matplotlib con estilo AER. Llamar una vez al inicio."""
    mpl.rcParams.update({
        # Fonts — Serif (Times New Roman / Computer Modern)
        "font.family": "serif",
        "font.serif": ["Times New Roman", "DejaVu Serif", "Bitstream Vera Serif"],
        "font.size": 10,
        "axes.titlesize": 11,
        "axes.labelsize": 10,
        "xtick.labelsize": 9,
        "ytick.labelsize": 9,
        "legend.fontsize": 9,

        # Layout — Minimalista
        "figure.figsize": (6.5, 4),      # AER column width
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "axes.spines.right": False,       # Sin borde derecho
        "axes.spines.top": False,         # Sin borde superior
        "axes.linewidth": 0.8,

        # Colores — Grayscale-friendly
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "black",
        "axes.grid": False,               # Sin grid (AER standard)

        # Lineas y marcadores
        "lines.linewidth": 1.2,
        "lines.markersize": 4,
        "errorbar.capsize": 3,

        # Texto
        "text.color": "black",
        "axes.labelcolor": "black",
        "xtick.color": "black",
        "ytick.color": "black",
    })

# Paleta grayscale-safe para multiples series
AER_COLORS = ["#000000", "#555555", "#999999", "#CCCCCC"]
AER_MARKERS = ["o", "s", "^", "D"]


def aer_save(fig, path, **kwargs):
    """Guarda figura con defaults AER (300 DPI, tight, white bg)."""
    fig.savefig(path, dpi=300, bbox_inches="tight", facecolor="white", **kwargs)
    plt.close(fig)


# ═════════════════════════════════════════════════════════════════
# TABLAS — Estilo LaTeX booktabs (AER)
# ═════════════════════════════════════════════════════════════════

class AERTable:
    """
    Genera tablas LaTeX estilo AER con booktabs.
    Sin lineas verticales. Solo toprule, midrule, bottomrule.
    """

    @staticmethod
    def regression_table(
        models_dict: Dict[str, Any],
        title: str = "Regression Results",
        label: str = "tab:results",
        dep_var: str = "",
        note: str = "",
        fe_rows: Optional[Dict[str, List[str]]] = None,
    ) -> str:
        """
        Tabla de regresion multi-columna estilo Stargazer/AER.

        Args:
            models_dict: {'(1) OLS': result, '(2) FE': result, ...}
            title: Titulo de la tabla
            label: Label LaTeX
            dep_var: Nombre de la variable dependiente
            note: Nota al pie adicional
            fe_rows: {'Unit FE': ['No', 'Yes'], 'Time FE': ['No', 'Yes']}
        """
        col_names = list(models_dict.keys())
        n_cols = len(col_names)

        # Recopilar parametros unicos
        all_params = set()
        for res in models_dict.values():
            all_params.update(res.params.index.tolist())
        sorted_params = sorted(p for p in all_params if p not in ("const", "Intercept"))

        # Body
        body_lines = []
        for param in sorted_params:
            row_coef = [param.replace("_", r"\_")]
            row_se = [""]
            for name in col_names:
                res = models_dict[name]
                if param in res.params:
                    coef = res.params[param]
                    pval = res.pvalues[param]
                    se = res.bse[param] if hasattr(res, "bse") else (
                        res.std_errors[param] if hasattr(res, "std_errors") else np.nan
                    )
                    stars = "$^{***}$" if pval < 0.01 else "$^{**}$" if pval < 0.05 else "$^{*}$" if pval < 0.1 else ""
                    row_coef.append(f"{coef:.4f}{stars}")
                    row_se.append(f"({se:.4f})")
                else:
                    row_coef.append("")
                    row_se.append("")
            body_lines.append(" & ".join(row_coef) + r" \\")
            body_lines.append(" & ".join(row_se) + r" \\")

        # FE indicators
        fe_lines = []
        if fe_rows:
            fe_lines.append(r"\midrule")
            for fe_name, values in fe_rows.items():
                fe_lines.append(" & ".join([fe_name] + values) + r" \\")

        # Stats
        obs_vals = []
        r2_vals = []
        for res in models_dict.values():
            obs_vals.append(f"{int(res.nobs):,}")
            r2_vals.append(f"{res.rsquared:.3f}")

        dep_line = f"& \\multicolumn{{{n_cols}}}{{c}}{{\\textit{{Dep. var: {dep_var}}}}} \\\\" if dep_var else ""

        latex = f"""\\begin{{table}}[htbp]
\\centering
\\caption{{{title}}}
\\label{{{label}}}
\\begin{{threeparttable}}
\\begin{{tabular}}{{l{"c" * n_cols}}}
\\toprule
{dep_line}
 & {" & ".join(col_names)} \\\\
\\midrule
{chr(10).join(body_lines)}
{chr(10).join(fe_lines)}
\\midrule
Observations & {" & ".join(obs_vals)} \\\\
$R^2$ & {" & ".join(r2_vals)} \\\\
\\bottomrule
\\end{{tabular}}
\\begin{{tablenotes}}
\\small
\\item Standard errors in parentheses. $^{{***}}$ p$<$0.01, $^{{**}}$ p$<$0.05, $^{{*}}$ p$<$0.1.{" " + note if note else ""}
\\end{{tablenotes}}
\\end{{threeparttable}}
\\end{{table}}"""
        return latex

    @staticmethod
    def summary_table(df: pd.DataFrame, title: str = "Summary Statistics",
                      label: str = "tab:summary") -> str:
        """Tabla de estadisticas descriptivas estilo AER."""
        stats = df.describe().T[["count", "mean", "std", "min", "25%", "50%", "75%", "max"]]
        stats.columns = ["N", "Mean", "Std. Dev.", "Min", "P25", "Median", "P75", "Max"]

        body = []
        for var, row in stats.iterrows():
            vals = [str(var).replace("_", r"\_")]
            vals.append(f"{int(row['N']):,}")
            for col in ["Mean", "Std. Dev.", "Min", "P25", "Median", "P75", "Max"]:
                vals.append(f"{row[col]:.3f}")
            body.append(" & ".join(vals) + r" \\")

        return f"""\\begin{{table}}[htbp]
\\centering
\\caption{{{title}}}
\\label{{{label}}}
\\begin{{tabular}}{{lcccccccc}}
\\toprule
Variable & N & Mean & Std. Dev. & Min & P25 & Median & P75 & Max \\\\
\\midrule
{chr(10).join(body)}
\\bottomrule
\\end{{tabular}}
\\end{{table}}"""
