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
    """Configura matplotlib con estilo AER 'Opportunity Insights' Ultra-Clean."""
    mpl.rcParams.update({
        # Fonts — Computer Modern (La fuente original y pura de LaTeX)
        "font.family": "serif",
        "font.serif": ["Computer Modern Roman", "cmr10", "STIXGeneral"],
        "mathtext.fontset": "cm",         # Renderizado matemático idéntico a LaTeX
        "axes.formatter.use_mathtext": True, # Requerido para signos negativos en ticks con cmr10
        "font.size": 12,
        "axes.titlesize": 14,
        "axes.titleweight": "bold",       # Títulos con impacto
        "axes.labelsize": 12,             # Balance optimizado para legibilidad
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        "legend.fontsize": 10,
        "legend.frameon": False,          

        # Layout — Proporción dorada 
        "figure.figsize": (8, 5),      
        "figure.dpi": 300,
        "savefig.dpi": 300,
        "axes.spines.right": False,      
        "axes.spines.top": False,         
        "axes.linewidth": 0.6,            # Líneas delgadas de ejes

        # Grid — Cero Grid
        "figure.facecolor": "white",
        "axes.facecolor": "white",
        "axes.edgecolor": "#333333",      
        "axes.grid": False,               # Sin grillas distractoras

        # Lineas y marcadores
        "lines.linewidth": 1.0,           # Líneas limpias y más delgadas
        "lines.markersize": 5,            # Marcadores un poco más pequeños
        "errorbar.capsize": 0,

        # Ticks 
        "xtick.direction": "out",
        "ytick.direction": "out",
        "xtick.major.size": 5,
        "ytick.major.size": 5,

        # Texto — Alto contraste pero no negro agresivo
        "text.color": "#111111",          
        "axes.labelcolor": "#222222",     
        "xtick.color": "#333333",         
        "ytick.color": "#333333",
    })

def aer_format_axes(ax=None):
    """
    Aplica el principio de Tufte: Offset spines.
    Separa físicamente los ejes de los datos para un look respirable y premium.
    """
    if ax is None:
        ax = plt.gca()
    
    # Despegar los ejes izquierdo y fondo por 5 puntos (Proporción dorada Tufte)
    ax.spines['left'].set_position(('outward', 5))
    ax.spines['bottom'].set_position(('outward', 5))
    
    # Asegurar que arriba/derecha estén invisibles
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    
    # Limpiar ticks innecesarios
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')

# Paleta Clásica Top-Tier (NBER/AER)
# Dark Charcoal (Off-Black), Harvard Crimson, Steel Blue, Gold/Ochre
# El Charcoal oscuro (#333333) da esa sensación de "tinta de altísima calidad".
AER_COLORS = ["#333333", "#9A1B1E", "#4E79A7", "#E15759", "#F28E2B"] 
AER_MARKERS = ["o", "s", "^", "D", "v"]
AER_LINESTYLES = ["-", "--", ":", "-."]


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
