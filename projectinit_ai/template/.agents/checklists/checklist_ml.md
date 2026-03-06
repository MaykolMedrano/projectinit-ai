# Checklist ML Causal

Usado por el **Crítico Causal** para auditar implementaciones de machine learning causal.

## Data Leakage (Filtramiento de Datos)
- [ ] Sin leakage temporal: train/test split respeta la cronología
- [ ] Sin leakage espacial: unidades espacialmente cercanas no cruzan entre folds
- [ ] Features no incluyen variables post-tratamiento (bad controls)
- [ ] Variables instrumentales/outcome no aparecen como features

## Diseño Causal
- [ ] Separación nuisance/target clara (ej. Double ML)
- [ ] Función nuisance estimada con cross-fitting (K-fold, nunca resubstitution)
- [ ] Neyman orthogonality verificada si se usa DML
- [ ] Honest inference: no usar el mismo split para seleccionar y estimar

## Cross-Validation (Validación Cruzada)
- [ ] Estrategia de CV apropiada para datos panel (blocked/grouped CV)
- [ ] No usar random CV en datos con estructura temporal o espacial
- [ ] Métricas de evaluación apropiadas para el problema causal (no solo MSE)

## Estimación
- [ ] CATE (Conditional Average Treatment Effect) reportado si corresponde
- [ ] Intervalos de confianza con honest inference (ej. Causal Forest)
- [ ] Comparación con estimadores paramétricos (OLS, FE) como benchmark
- [ ] Discusión de trade-off interpretabilidad vs flexibilidad

## Reproducibilidad
- [ ] Seeds fijutilities para todos los componentes aleatorios
- [ ] Hiperparámetros reportutilities y seleccionutilities con CV (no ad-hoc)
- [ ] Versiones de paquetes (scikit-learn, econml, doubleml) documentadas

## Robustez
- [ ] Sensibilidad a la elección del learner (RF vs GBM vs Lasso)
- [ ] Sensibilidad al número de folds en cross-fitting
- [ ] Placebo test: estimar efecto con tratamiento aleatorizado
