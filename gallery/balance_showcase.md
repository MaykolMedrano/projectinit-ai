# Triple Master Balance Suite: RCT Validation Standards

Las tablas de balance son el "pacto de confianza" inicial. Aquí tienes 3 ejemplos de layouts adaptados a diferentes niveles de densidad de datos.

---

## 1. Balance Lineal Estándar (Standard)

*Archivo: [example_balance_table.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_balance_table.tex)*

Ideal para RCTs con pocos controles principales. Incluye columna de diferencia y p-value del t-test.

![Standard Balance](/render_balance_table_1772812678586.png)

---

## 2. Balance Categorizado por Paneles (Grouped)

*Archivo: [example_balance_grouped.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_balance_grouped.tex)*

Para papers con 20+ variables. Agrupamos por **Panel A: Demografía**, **Panel B: Economía**, etc., para mantener el hilo narrativo.

![Grouped Balance](/render_balance_grouped_categorized_1772812874818.png)

---

## 3. Balance Comparativo por Subgrupos (Wide/Horizontal)

*Archivo: [example_balance_subgroups.tex](file:///e:/00_Desktop/projectinit-ai-repo/example_balance_subgroups.tex)*

Un layout apaisado (landscape) que valida que la aleatorización fue exitosa *dentro* de grupos clave (ej. Urbanos vs Rurales).

![Subgroup Balance](/render_balance_subgroups_comparative_1772812902091.png)

---

**Nota Final:** Todos los elementos diseñados para ser compilables en `Standard LaTeX` o con `siunitx` para perfección decimal.
