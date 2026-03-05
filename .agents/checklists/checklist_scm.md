# Checklist SCM (Synthetic Control Method)

Usado por el **Crítico Causal** para auditar diseños de control sintético.

## Estrategia de Identificación
- [ ] Unidad tratada claramente definida (ej. comuna, zona censal)
- [ ] Timing de tratamiento preciso
- [ ] Justificación de por qué SCM es apropiado (pocos tratados, serie larga)

## Pool de Donantes
- [ ] Pool de donantes definido con criterio claro
- [ ] Donantes nunca expuestos al tratamiento (ni directa ni indirectamente)
- [ ] Discusión de donantes potencialmente contaminados (spillovers)
- [ ] Número de donantes reportado

## Ajuste Pre-Tratamiento
- [ ] RMSPE pre-tratamiento reportado
- [ ] Gráfico de ajuste pre-tratamiento (unidad tratada vs sintético)
- [ ] Predictores y períodos pre-tratamiento usados en la optimización listados
- [ ] Pesos de los donantes reportados (verificar que no domine uno solo)

## Inferencia
- [ ] Placebo in-space: permutar el tratamiento a cada donante
- [ ] Ratio RMSPE post/pre para rankear el efecto real vs placebos
- [ ] p-valor basado en la distribución de ratios placebo
- [ ] Placebo in-time: aplicar SCM en un período pre-tratamiento falso

## Robustez
- [ ] Leave-one-out: excluir iterativamente cada donante con peso alto
- [ ] Sensibilidad a los predictores seleccionados
- [ ] Sensibilidad al período pre-tratamiento usado
- [ ] SCM con covariables adicionales

## Visualización
- [ ] Gap plot (diferencia tratado - sintético a lo largo del tiempo)
- [ ] Spaghetti plot con todos los placebos in-space
- [ ] Notas descriptivas al pie
