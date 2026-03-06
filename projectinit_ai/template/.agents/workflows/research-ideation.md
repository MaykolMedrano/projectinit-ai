---
description: Sesión interactiva tipo "Devil's Advocate" donde el sistema cuestiona destructivamente tu diseño causal empírico antes de programar una línea de código.
---

# Workflow: Causal Research Ideation

Inspirado en el comando `/research-ideation` de Pedro Sant'Anna.

## Invocación

Escribe: `/research-ideation`

## Flujo de Trabajo (Adversarial Design)

1. El usuario describe su pregunta de investigación empírica (ej. "¿Cómo afecta la construcción del metro a los precios de vivienda? Usaré un RDD").
2. El Orquestador convoca inmediatamente al **Crítico Causal** y al **Revisor de Dominio (Economía Espacial)**.
3. Ambos perfiles asumen el rol combinado de **Abogado del Diablo (Devil's Advocate)**.
4. Proceden a atacar el diseño con preguntas destructivas pero constructivas, enfocándose en la identificación causal y la alineación teórica.
   - Ejemplos de ataque: "¿Qué asegura que el gobierno no puso el metro justamente donde los precios iban a subir de todas formas (endogeneidad espacial)?" o "¿Qué pasa si las expectativas de la línea ya estaban capitalizadas hace 5 años?".
   - **Rigurosidad:** Cuestionar tempranamente problemas de *Low Power* (muestras pequeñas sin significancia real) y la debilidad teórica intrínseca de los instrumentos (*Weak Instruments invisibles para el F-stat clásico*).
5. El Agente detiene su ejecución mediante la herramienta `notify_user` para que el usuario responda, se defienda o corrija su diseño en base a los ataques.
6. El ciclo de entrevista iterativa dura tantas fases como el usuario requiera, hasta alcanzar una especificación "Bullet-proof" antes de pasar al código.
