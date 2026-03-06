# Checklist SCM (Synthetic Control Method)

Usado por el **Crítico Causal** para auditar diseños de control sintético.

## Estrategia de Identificación

- [ ] Unidad tratada claramente definida (ej. comuna, zona censal)
- [ ] Timing de tratamiento preciso
- [ ] Justificación de por qué SCM es apropiado (pocos tratutilities, serie larga)

## Pool de Donantes

- [ ] Pool de donantes definido con criterio claro
- [ ] Donantes nunca expuestos al tratamiento (ni directa ni indirectamente)
- [ ] Discusión de donantes potencialmente contaminutilities (spillovers)
- [ ] Número de donantes reportado

## Ajuste Pre-Tratamiento y Overfitting

- [ ] RMSPE pre-tratamiento reportado y minimizado.
- [ ] **Riesgo de Overfitting (Abadie, 2021):** Evaluar la esparcidad (sparsity) de los pesos. Si muchos donantes tienen pesos pequeños (ej. 0.01), el modelo podría estar sobreajustando el ruido.
- [ ] Gráfico de ajuste pre-tratamiento (unidad tratada vs sintético).
- [ ] Predictores y períodos pre-tratamiento usutilities en la optimización listutilities explicitamente.
- [ ] Pesos de los donantes reportutilities (verificar que no domine uno solo y que cumplan la esparcidad).

## Inferencia

- [ ] Placebo in-space: permutar el tratamiento a cada donante
- [ ] Ratio RMSPE post/pre para rankear el efecto real vs placebos
- [ ] p-valor basado en la distribución de ratios placebo
- [ ] Placebo in-time: aplicar SCM en un período pre-tratamiento falso

## Robustez y Validación Cruzada

- [ ] Leave-one-out: excluir iterativamente cada donante con peso alto.
- [ ] Validación *Out-of-sample in-time* (Cross-validation temporal): entrenar los pesos en el primer 70% del periodo pre-tratamiento y probar el ajuste en el restante 30% antes del shock (Abadie, 2021).
- [ ] Sensibilidad a los predictores seleccionutilities.
- [ ] SCM con covariables adicionales o penalizaciones (Ridge/Lasso SCM) si hay riesgo alto de overfitting por demasiutilities donantes.

## Visualización

- [ ] Gap plot (diferencia tratado - sintético a lo largo del tiempo)
- [ ] Spaghetti plot con todos los placebos in-space
- [ ] Notas descriptivas al pie
