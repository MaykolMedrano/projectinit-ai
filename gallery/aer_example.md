# Documentación de Estándares: Gráficos y Tablas NBER/AER (Pillar Version)

Este documento es el repositorio maestro de estilo para la producción de papers de élite.

---

## 1. El Arte de las Tablas (Saturated & Pillar Suite)

Hemos consolidado 11 niveles de templates LaTeX. El "Pillar" representa el nivel máximo de densidad informativa permitido por el ojo humano:

### A. La Gran Tabla de Resultados (The Pillar)

*Archivo: [example_pillar_table.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_pillar_table.tex)*

Consolida toda la historia del paper en un solo "Pilar" vertical. Cruza **10+ Outcomes** con **5 Especificaciones** de robustez mediante paneles temáticos.
![Pillar Table Render](/render_pillar_extreme_vertical_table_1772814815432.png)

### B. Identificación Causal y Mecanismos

* **Triple Diferencia (DDD):** [example_ddd_table.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_ddd_table.tex)
    ![DDD Table Render](/render_ddd_saturated_table_1772814533020.png)

* **Matriz de Heterogeneidad:** [example_heterogeneity_matrix.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_heterogeneity_matrix.tex)
    ![Heterogeneity Matrix Render](/render_heterogeneity_matrix_saturated_1772814548984.png)

### C. Suite de Balance y Caracterización

* **Summary Stats Avanzados:** [example_sumstats_advanced.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_sumstats_advanced.tex)
* **Balance Triple (Standard, Categorized, Subgroups):** Ver archivos `example_balance_*.tex`.

---

## 2. Galería de Gráficos Econométricos (19 Master Templates)

*(Consultar versiones anteriores para la galería completa de 19 gráficos causal/time-series)*

---

**Identidad Visual:** Todas las tablas y gráficos están diseñados bajo la **Regla de Proporcionalidad Estética** (Línea 1.1, Ejes 0.6) y alineación decimal perfecta vía `siunitx`.
