# API pública — Tipos y datos básicos (v0.1.0)

Todas las operaciones son predicados puros que devuelven un booleano y no convierten ni modifican sus entradas.

| Función | Comportamiento |
|---|---|
| `is_string(value)` | Verdadero solo para texto FIT (`string`). |
| `is_integer(value)` | Verdadero solo para `int`; nunca para `bool`. |
| `is_number(value)` | Verdadero para `int` o `float`; nunca `bool`. |
| `is_boolean(value)` | Verdadero solo para `bool`. |
| `is_list(value)` | Verdadero solo para `list`. |
| `is_tuple(value)` | Verdadero solo para `tuple`. |
| `is_dict(value)` | Verdadero solo para `dict`. |
| `is_none(value)` | Verdadero para tipo `NoneType`. |
| `is_scalar(value)` | Texto, entero, flotante o booleano; excluye `None`. |
| `is_collection(value)` | `list`, `tuple` o `dict`, nunca `string`. |
| `is_json_value(value, max_depth=32, max_nodes=1024)` | Recorre estructuras JSON (listas y diccionarios con claves de texto). Rechaza tuplas, claves no textuales y flotantes no finitos. Límites duros: `max_depth≤32` y `max_nodes≤4096`. Los límites inválidos y el agotamiento devuelven `False`. No convierte ni serializa. |
| `type_is(value, expected)` | Igualdad exacta con nombre FIT canónico: `string`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `NoneType`. Tipos desconocidos/no textuales retornan `False`. |

La profundidad cuenta desde el valor raíz a nivel 0. Las colecciones consumen un nivel antes de recorrer sus hijos; el presupuesto de nodos cuenta también la raíz. Si se requiere distinguir entre invalidez y presupuesto agotado, debe utilizarse una API estructurada futura; este predicado solo devuelve `bool`.

**Ejemplos y casos límite ejecutables:** consulta `tests/cases.json`. **Runtime:** BlackWhi Rust/Starlark 0.14.2. **Introducidas en:** v0.1.0 candidata. **Errores:** las funciones no garantizan capturar fallos del motor si se exceden sus propios límites de ejecución globales.
