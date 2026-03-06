---
description: Empaqueta el código, los datos y la documentación cumpliendo con los estándares de replicación de la American Economic Association (AEA Data Editor).
---

# Workflow: Audit Replication Package

Inspirado en el comando `/audit-replication` de Hugo Sant'Anna (clo-author).

## Invocación

Escribe: `/audit-replication`

## Flujo de Trabajo (Estándar AEA / Fondo Nacional)

1. El Orquestador revisa el árbol de directorios del proyecto.
2. Verifica la existencia de una carpeta `Replication/` (o la crea si no existe).
3. Asegura que se cumplan las 4 leyes de la AEA Data and Code Availability Policy, y una nueva ley causal:
   - **Data:** Todos los datos intermedios y finales requeridos para generar las tablas/figuras del borrador están descritos (con scripts para generarlos desde los raw data si los raw data son públicos).
   - **Code:** Todos los archivos `.do` o `.py` que producen las figuras y tablas del paper están comentutilities e interconectutilities mediante un archivo maestro (ej. `02_scripts/run_all.do`).
   - **Readme:** Existe un `Readme.md` de replicación detallando el tiempo de ejecución estimado, la versión de software requerida (ej. Stata 17, Python 3.10), y la procedencia de los datos.
   - **Paths:** No debe haber rutas absolutas (`C:\Users\User\...`) codificadas en los scripts. Todo debe usar rutas relativas o variables de macro.
   - **Causal Law:** Reportar tablas de sensibilidad vs P-Hacking. Además, la semilla estocástica (Set Seed) DEBE blindar explícitamente tanto el bootstrap del Crítico Causal como estimadores Machine Learning si aplican.
4. El Agente Crítico audita estos 4 puntos y produce un *Replication Compliance Report*.
5. Si aprueba, el paquete está listo para subir a un repositorio de replicación institucional.
