---
description: Rebaja el tono "robótico" o "GPTesco" de un texto académico, haciéndolo sonar como un investigador humano y pulido.
---

# Workflow: Humanizer (Des-robotización Textual)

Inspirado en el comando `/humanizer` de Hugo Sant'Anna (clo-author).

## Invocación
Escribe: `/humanizer [archivo_o_texto]`

## Flujo de Trabajo

1. El Agente lee el texto o documento proporcionado (generalmente la introducción o conclusión del paper).
2. Se asume el rol de **Editor Humano**.
3. Se aplica la "Dieta de Vocabulario":
   - **ELIMINAR:** "Crucial", "Vital", "Delve into", "Underscores", "Sheds light on", "In conclusion", "Moreover", "Furthermore".
   - **SUSTITUIR POR:** Verbos directos y precisos. Voz activa ("Estimamos" en lugar de "Fue estimado que").
4. Se varían las longitudes de las oraciones. (Evitar la estructura: Sujeto + Verbo + Predicado monótono).
5. Se eliminan afirmaciones grandilocuentes ("Este paper revoluciona la literatura de...").
6. El output se presenta al usuario, ofreciendo reemplazar el archivo original con la versión "humanizada".
