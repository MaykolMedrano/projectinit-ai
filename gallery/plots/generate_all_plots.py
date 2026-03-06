import sys
from pathlib import Path
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy.stats as stats

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

print("Generando graficos en el directorio 'outputs'...")

# ==========================================
# 1. Regression Discontinuity Design (RDD)
# ==========================================
np.random.seed(42)
N_rdd = 5000  # Datos masivos para un RD creíble
rv_c = np.random.uniform(-10, 0, N_rdd)
rv_t = np.random.uniform(0, 10, N_rdd)

# Relación no lineal subyacente sutil + alto ruido para mostrar el poder del Binning
y_c = 12 + 0.8 * rv_c + 0.05 * rv_c**2 + np.random.normal(0, 4.5, N_rdd)
y_t = 18 + 0.6 * rv_t - 0.02 * rv_t**2 + np.random.normal(0, 4.5, N_rdd)

# 100 bins per side for massive density
bins_c = np.linspace(-10, 0, 100) 
bins_t = np.linspace(0, 10, 100)
means_c = [np.mean(y_c[(rv_c >= bins_c[i]) & (rv_c < bins_c[i+1])]) for i in range(len(bins_c)-1)]
means_t = [np.mean(y_t[(rv_t >= bins_t[i]) & (rv_t <= bins_t[i+1])]) for i in range(len(bins_t)-1)]
bc_c = (bins_c[:-1] + bins_c[1:]) / 2
bc_t = (bins_t[:-1] + bins_t[1:]) / 2

# Fit quadratic polynomial for a more "real" RD look
df_c = pd.DataFrame({'x': rv_c, 'x2': rv_c**2, 'y': y_c})
mod_c = sm.OLS.from_formula('y ~ x + x2', data=df_c).fit()
seq_c = np.linspace(-10, 0, 200)
pred_c = mod_c.get_prediction(pd.DataFrame({'x': seq_c, 'x2': seq_c**2})).summary_frame()

df_t = pd.DataFrame({'x': rv_t, 'x2': rv_t**2, 'y': y_t})
mod_t = sm.OLS.from_formula('y ~ x + x2', data=df_t).fit()
seq_t = np.linspace(0, 10, 200)
pred_t = mod_t.get_prediction(pd.DataFrame({'x': seq_t, 'x2': seq_t**2})).summary_frame()

fig1, ax1 = plt.subplots(figsize=(8, 5))
aer_format_axes(ax1)
# Shaded confidence intervals (Softer, more elegant alpha)
ax1.fill_between(seq_c, pred_c['mean_ci_lower'], pred_c['mean_ci_upper'], color=slate, alpha=0.12, linewidth=0)
ax1.fill_between(seq_t, pred_t['mean_ci_lower'], pred_t['mean_ci_upper'], color=mit_red, alpha=0.12, linewidth=0)
# Clean, crisp binned scatter points with glass-like alpha and strong white edges
ax1.plot(bc_c, means_c, 'o', markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.3, markersize=3, alpha=0.8)
ax1.plot(bc_t, means_t, 's', markerfacecolor=mit_red, markeredgecolor='white', markeredgewidth=0.3, markersize=3, alpha=0.85)
# Strong polynomials
ax1.plot(seq_c, pred_c['mean'], color=slate, linewidth=1.05)
ax1.plot(seq_t, pred_t['mean'], color=mit_red, linewidth=1.05)
ax1.axvline(0, color='#888888', linestyle='--', linewidth=1.0, zorder=0)

ax1.set_xlabel("Test Score (Running Variable centered at Cutoff)")
ax1.set_ylabel("College Enrollment Probability ($Y$)")
aer_save(fig1, str(output_dir / "1_rdd_plot.png"))


# ==========================================
# 2. Event Study (Dynamic DiD)
# ==========================================
time_to_treat = np.arange(-7, 8) # length 15
# Pre-trends ultra planas (validación espectacular)
pre = np.random.normal(0, 0.02, 6) # length 6
base = 0.0 # length 1
# Impacto dinámico que se estabiliza (Sustitución dinámica)
post = np.array([0.22, 0.45, 0.58, 0.65, 0.68, 0.69, 0.69, 0.70]) + np.random.normal(0, 0.015, 8) # length 8
coefs = np.concatenate([pre, [base], post])
# Standard errors realistas (campana invertida al alejarse del tratamiento)
ses = np.array([0.08, 0.07, 0.05, 0.05, 0.04, 0.04, 0.0, 0.04, 0.045, 0.05, 0.06, 0.07, 0.08, 0.09, 0.11]) # length 15
ci_mult = 1.96

fig2, ax2 = plt.subplots(figsize=(9, 5.5))
aer_format_axes(ax2)
ax2.axhline(0, color="#666666", linestyle="-", linewidth=1.0, zorder=1)
ax2.axvline(-1, color="#888888", linestyle="--", linewidth=1.0, zorder=1)
# Error bars slightly translucent so they don't overpower the markers
ax2.errorbar(time_to_treat, coefs, yerr=ci_mult*ses, fmt='none', ecolor=mit_red, elinewidth=0.8, capsize=0, alpha=0.75, zorder=2)
ax2.plot(time_to_treat, coefs, color=slate, linewidth=1.05, zorder=3)
ax2.plot(time_to_treat, coefs, "o", markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.5, markersize=6, zorder=4)
ax2.plot(-1, 0, "o", markerfacecolor="white", markeredgecolor=slate, markeredgewidth=1.0, markersize=7, zorder=5)

ax2.set_xlabel("Years Since Policy Adoption ($k$)")
ax2.set_ylabel("Estimated Treatment Effect (Log Earnings)")
ax2.set_xticks(np.arange(-7, 8, 2))
aer_save(fig2, str(output_dir / "2_event_study.png"))


# ==========================================
# 3. Binscatter
# ==========================================
np.random.seed(99)
N_bs = 25000 # Super massive data set
x_bs = np.random.lognormal(mean=2, sigma=0.8, size=N_bs)
y_bs = 4.5 * np.log(x_bs + 1) + np.random.normal(0, 5, N_bs) 

# Trim extreme tails for better visualization
mask = (x_bs < np.percentile(x_bs, 99))
x_bs = x_bs[mask]
y_bs = y_bs[mask]

# 150 finely gridded bins to show a near-continuous mass
bins_bs = np.linspace(min(x_bs), max(x_bs), 150) 
bc_bs = (bins_bs[:-1] + bins_bs[1:]) / 2
bm_y = np.array([np.mean(y_bs[(x_bs >= bins_bs[i]) & (x_bs < bins_bs[i+1])]) for i in range(len(bins_bs)-1)])
valid = ~np.isnan(bm_y)
bc_bs = bc_bs[valid]
bm_y = bm_y[valid]

# Fit logarithmic relationship visually
df_bs = pd.DataFrame({'x': np.log(bc_bs + 1), 'y': bm_y})
mod_bs = sm.OLS.from_formula('y ~ x', data=df_bs).fit()
seq_bs = np.linspace(min(bc_bs), max(bc_bs), 100)
pred_bs_mean = mod_bs.get_prediction(pd.DataFrame({'x': np.log(seq_bs + 1)})).summary_frame()['mean']

fig3, ax3 = plt.subplots(figsize=(8, 5))
aer_format_axes(ax3)
ax3.plot(bc_bs, bm_y, 'o', markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.3, markersize=3.5, alpha=0.80, zorder=3)
ax3.plot(seq_bs, pred_bs_mean, color=mit_red, linewidth=1.05, zorder=2) # MIT Red Fit line
ax3.set_xlabel("Firm Size (Employees)")
ax3.set_ylabel("Log Productivity (Value Added)")
aer_save(fig3, str(output_dir / "3_binscatter.png"))


# ==========================================
# 4. Coefficient Plot (Massive Meta-Analysis Style)
# ==========================================
# Generate 35 covariates/studies
labels_fp = [f"Covariate / Feature {i:02d}" for i in range(1, 36)]
# Create a trend where mostly everything is null, but a few pop out
coefs_fp = np.random.normal(0, 0.2, 35)
coefs_fp[5], coefs_fp[12], coefs_fp[28] = 1.2, -0.9, 1.8
ses_fp = np.random.uniform(0.05, 0.4, 35)

fig4, ax4 = plt.subplots(figsize=(8, 8)) # Taller canvas for 35 vars
aer_format_axes(ax4)
ax4.axvline(0, color="#888888", linestyle="--", linewidth=1.0, zorder=1)
y_pos = np.arange(len(labels_fp))
# Add 90% and 95% CIs nested for visual complexity
ax4.errorbar(coefs_fp, y_pos, xerr=1.96*ses_fp, fmt='none', ecolor='#A0A0A0', elinewidth=0.8, capsize=0, zorder=2)
ax4.errorbar(coefs_fp, y_pos, xerr=1.645*ses_fp, fmt='o', color=slate, ecolor=slate, elinewidth=1.8, capsize=0, markersize=4, markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.3, zorder=3)

ax4.set_yticks(y_pos)
ax4.set_yticklabels(labels_fp)
ax4.set_xlabel("Treatment Effect on Adoption Rate (90% and 95% CIs)")
aer_save(fig4, str(output_dir / "4_coefplot.png"))


# ==========================================
# 5. McCrary Density
# ==========================================
np.random.seed(88)
N_mcc = 15000
rv_mc_c = np.random.normal(-5, 4, int(N_mcc*0.55)) # Manipulación: Hay más gente amontonada justo antes del cero
rv_mc_t = np.random.normal(5, 4, int(N_mcc*0.45))
rv_mc_c = np.append(rv_mc_c, np.random.uniform(-1, 0, 800)) # Spike in manipulacion
rv_mc = np.concatenate([rv_mc_c[rv_mc_c < 0], rv_mc_t[rv_mc_t > 0]])

fig5, ax5 = plt.subplots(figsize=(8, 5))
aer_format_axes(ax5)
# Dense transparent histograms (120 bins for needle-thin bars)
ax5.hist(rv_mc[rv_mc < 0], bins=120, density=True, color="white", edgecolor=slate, linewidth=0.5, alpha=0.85, zorder=2)
ax5.hist(rv_mc[rv_mc >= 0], bins=120, density=True, color="white", edgecolor=mit_red, linewidth=0.5, alpha=0.85, zorder=2)

kde_c = stats.gaussian_kde(rv_mc[rv_mc < 0])
kde_t = stats.gaussian_kde(rv_mc[rv_mc >= 0])
x_c = np.linspace(-15, 0, 200)
x_t = np.linspace(0, 15, 200)
ax5.plot(x_c, kde_c(x_c), color=slate, linewidth=1.05, zorder=3)
ax5.plot(x_t, kde_t(x_t), color=mit_red, linewidth=1.05, zorder=3)

ax5.axvline(0, color="#444444", linestyle="--", linewidth=1.0, zorder=1)
ax5.set_xlabel("Poverty Score (Threshold at 0)")
ax5.set_ylabel("Density (Testing for Sorting)")
aer_save(fig5, str(output_dir / "5_mccrary.png"))


# ==========================================
# 6. Covariate Balance (Love Plot - Massive)
# ==========================================
# 30 covariates
covs_lp = [f"Baseline Covariate {i:02d}" for i in range(1, 31)]
# Raw SMDs are wild
smd_u = np.random.normal(0, 0.4, 30)
# Matched SMDs are tightly bounded within 0.1
smd_m = np.random.normal(0, 0.03, 30)

fig6, ax6 = plt.subplots(figsize=(8, 7)) # Taller canvas
aer_format_axes(ax6)
y_pos_lp = np.arange(len(covs_lp))
ax6.axvline(0, color="#444444", linestyle="-", linewidth=1.0, zorder=1)
# Zona aceptable en gris suave
ax6.axvspan(-0.1, 0.1, color='#F0F0F0', alpha=0.6, zorder=0)
ax6.axvline(0.1, color="#BBBBBB", linestyle=":", linewidth=1.0, zorder=1)
ax6.axvline(-0.1, color="#BBBBBB", linestyle=":", linewidth=1.0, zorder=1)

ax6.plot(smd_u, y_pos_lp, 'o', markerfacecolor="white", markeredgecolor="#999999", markeredgewidth=0.8, markersize=4.5, label="Raw Sample", zorder=3)
ax6.plot(smd_m, y_pos_lp, 'o', markerfacecolor=slate, markeredgecolor='white', markeredgewidth=0.4, markersize=5, label="Propensity Score Matched", zorder=4)

ax6.set_yticks(y_pos_lp)
ax6.set_yticklabels(covs_lp)
ax6.set_xlabel("Standardized Mean Difference (SMD)")
ax6.legend(loc="upper left", bbox_to_anchor=(0.5, 1.05))
aer_save(fig6, str(output_dir / "6_loveplot.png"))

print("¡Listo! 6 graficos de Causal Econometrics compilados en 'example_plots/outputs/'.")
