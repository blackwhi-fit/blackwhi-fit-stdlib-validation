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

## Fichas técnicas por operación

Todos los predicados: introducidos en la candidata `0.1.0`, sin I/O ni capacidades nativas, deterministas, sin mutación y con retorno `bool`. Sus casos positivos, negativos y de frontera están identificados individualmente en `tests/cases.json`, que se ejecuta contra el motor Rust/Starlark real.

### `is_string(value)`

- **Firma:** `is_string(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** string.
- **Ejemplos de valores válidos e inválidos:** `is_string("FIT") → True`; `is_string(4) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_string.*`).

### `is_integer(value)`

- **Firma:** `is_integer(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** int, excluding bool.
- **Ejemplos de valores válidos e inválidos:** `is_integer(4) → True`; `is_integer(True) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_integer.*`).

### `is_number(value)`

- **Firma:** `is_number(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** int | float (not bool).
- **Ejemplos de valores válidos e inválidos:** `is_number(4.5) → True`; `is_number(False) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_number.*`).

### `is_boolean(value)`

- **Firma:** `is_boolean(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** bool.
- **Ejemplos de valores válidos e inválidos:** `is_boolean(True) → True`; `is_boolean(1) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_boolean.*`).

### `is_list(value)`

- **Firma:** `is_list(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** list.
- **Ejemplos de valores válidos e inválidos:** `is_list([]) → True`; `is_list(()) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_list.*`).

### `is_tuple(value)`

- **Firma:** `is_tuple(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** tuple.
- **Ejemplos de valores válidos e inválidos:** `is_tuple((1, 2)) → True`; `is_tuple([1, 2]) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_tuple.*`).

### `is_dict(value)`

- **Firma:** `is_dict(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** dict.
- **Ejemplos de valores válidos e inválidos:** `is_dict({}) → True`; `is_dict([]) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_dict.*`).

### `is_none(value)`

- **Firma:** `is_none(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** NoneType.
- **Ejemplos de valores válidos e inválidos:** `is_none(None) → True`; `is_none(0) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_none.*`).

### `is_scalar(value)`

- **Firma:** `is_scalar(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** string | int | float | bool.
- **Ejemplos de valores válidos e inválidos:** `is_scalar("a") → True`; `is_scalar(None) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_scalar.*`).

### `is_collection(value)`

- **Firma:** `is_collection(value) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; no se realizan conversiones.
- **Tipo aceptado:** list | tuple | dict.
- **Ejemplos de valores válidos e inválidos:** `is_collection({}) → True`; `is_collection("a") → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`is_collection.*`).

### `is_json_value(value, max_depth=32, max_nodes=1024)`

- **Firma:** `is_json_value(value, max_depth=32, max_nodes=1024) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; `max_depth` y `max_nodes` son límites enteros opcionales.
- **Tipo aceptado:** JSON value model; bounded iterative traversal.
- **Ejemplos de valores válidos e inválidos:** `is_json_value({"x": [1]}) → True`; `is_json_value([()]) → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; recorrido iterativo con máximos duros de 32 niveles y 4096 nodos; valores JSON no finitos y tuplas no admitidos.
- **Pruebas asociadas:** `tests/cases.json` (`is_json_value.*`, y `json.*`).

### `type_is(value, expected)`

- **Firma:** `type_is(value, expected) -> bool` (notación documental FIT, no anotación ejecutable).
- **Argumentos:** `value` es el valor examinado; `expected` debe ser un nombre de tipo canónico.
- **Tipo aceptado:** 8 canonical runtime types.
- **Ejemplos de valores válidos e inválidos:** `type_is(None, "NoneType") → True`; `type_is(1, "string") → False`.
- **Errores:** un tipo distinto devuelve `False`, no un error estructurado. Las excepciones globales del motor no quedan absorbidas.
- **Restricciones:** función pura y sin privilegios; comprobación de tipo exacto, sin efectos secundarios ni dependencias externas.
- **Pruebas asociadas:** `tests/cases.json` (`type_is.*`).
