# BLACKWHI — Biblioteca estándar FIT: Validation

**Primera colección:** Tipos y datos básicos · 12 predicados implementados en `packages/core/modules/types.fit`.

**Empresa desarrolladora:** Maobits  
**Desarrollador principal:** Mauricio Chara Hurtado  
**Soporte oficial:** support@blackwhi.com

## Qué contiene

- Código FIT puro con doce operaciones de tipos y datos básicos.
- Manifiesto `fit-library.json` y contrato de empaquetado FIT-03 real.
- Pruebas automatizadas contra el motor Rust/Starlark de BlackWhi (no se emulan resultados en Python).
- Catálogo histórico de 298 validadores **propuestos** y especificaciones ES/EN.
- Guía de integración y construcción reproducible del artefacto `.fitpkg`.

## Pruebas

```bash
python3 scripts/verify_source.py
python3 tests/run_fit_tests.py --engine /ruta/a/blackwhi-v2/crates/fit-engine/target/debug/blackwhi-fit-engine
```

## Crear el paquete con el empaquetador FIT real

```bash
python3 scripts/build_fitpkg.py --blackwhi-root /ruta/a/blackwhi-v2
```

Se requiere un BlackWhi v2 que incluya `tools/fit/fit03_packages_v052.py` y el ejecutable Rust compilado. El comando ensambla un entorno temporal y no modifica el repositorio de BlackWhi v2. La salida aparece en `dist/`. La firma y la publicación remota son procesos independientes todavía no efectuados.

## Uso en otro proyecto FIT

Consulta [la guía de integración](docs/INTEGRATION.es.md). La importación desde un paquete verificado se realiza mediante `load("vendor/com.blackwhi.std.validation.core/0.1.0/modules/types.fit", "is_string")`, cuando la dependencia haya sido resuelta y fijada por el mecanismo FIT-03.

## Licencia

El código fuente original se distribuye bajo **Apache License, Version 2.0** (`SPDX: Apache-2.0`). Consulta [LICENSE](LICENSE) y [NOTICE](NOTICE). Se permite el uso comercial, la modificación y la redistribución conforme a sus términos; las marcas BLACKWHI se gestionan por separado. GitHub no equivale a una publicación firmada en Registry.
