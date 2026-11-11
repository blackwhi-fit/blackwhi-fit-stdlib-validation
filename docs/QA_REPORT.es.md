# BlackWhi FIT Validation — Informe de aceptación local

**Hito:** FIT-STDLIB-VAL-01 · **Fecha:** 2026-11-11 · **Estado:** candidato local verificable.

- **Código FIT:** 12 predicados en `packages/core/modules/types.fit`.
- **Ejecución:** 255 casos ejecutados exitosamente con un binario auténtico BlackWhi FIT Engine (`starlark-rust 0.14.2`, protocolo 1, `0.3.0+fit02.7`) extraído del código facilitado para este proyecto.
- **Seguridad:** `run-secure`, sin capacidades nativas concedidas. Rechazo de NaN/Inf, estructuras incompatibles y límites por profundidad, nodos y amplitud de colección.
- **Empaquetado:** ejecución del trabajador oficial `tools/fit/fit03_packages_v052.py`: `validate`, `pack`, `verify`, `run` PASS.
- **Consumidor independiente:** programa con otro identificador, que carga la biblioteca versionada mediante `load()`: `validate`, `pack`, `verify`, `run` PASS.
- **Reproducibilidad:** dos construcciones consecutivas generaron el mismo SHA-256.
- **Licencia y publicación:** pendientes de autorización. No se han probado GitHub Actions ni el flujo de publicación en Registry/Store.

La aceptación en el Ubuntu del usuario debe repetirse contra su copia actual del motor y CLI. Este documento no debe interpretarse como una certificación formal de seguridad ni como garantía de compatibilidad con versiones futuras.
