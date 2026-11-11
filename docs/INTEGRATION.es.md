# Integración FIT-03 con Validation

1. La biblioteca versionada es `com.blackwhi.std.validation.core@0.1.0`.
2. FIT-03 espera `libraries/fit/com.blackwhi.std.validation.core/0.1.0/fit-library.json` y `modules/types.fit`, con sus hashes exactos.
3. Declara la dependencia con el resolutor real del CLI: `blackwhi fit package lock <path/fit-program.json> com.blackwhi.std.validation.core@0.1.0` (con el programa en el mismo workspace del motor).
4. Importa, por ejemplo:

```python
load("vendor/com.blackwhi.std.validation.core/0.1.0/modules/types.fit", "is_integer", "is_json_value")

is_integer(25) and is_json_value({"age": 25})
```

5. Ejecuta `blackwhi fit package validate`, `build`, `verify` y `run` mediante el CLI real.

**Nota:** el artefacto `.fitpkg` contiene un programa de prueba de integración y la biblioteca versionada vendorizada, porque este es el contrato del empaquetador FIT-03 actual. No se afirma que sea un formato de biblioteca individual ni que esté publicado en el Registry o Store. No ejecutes paquetes desconocidos.
