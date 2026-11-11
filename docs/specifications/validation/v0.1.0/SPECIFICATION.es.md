# BlackWhi FIT Standard Library — Propuesta de validadores v0.1.0

**Estado:** PROPUESTA, no código FIT implementado ni API aprobada. **Fecha:** 2026-11-10. **Repositorio consumidor examinado:** `com.blackwhi.fitness@0.1.0` (ZIP proporcionado).

## 1. Evidencia del proyecto adjunto

Se revisaron `main.fit`, `modules/project.fit`, `fit-program.json`, `fit-lock.json`, `README.md`, `docs/architecture/PROJECT.md` y `tests/test_foundation.py`. El manifiesto declara `blackwhi.fit.program.v2`, motor `starlark-rust@0.14.2`, sin `required_capabilities`, sin `requested_permissions`; el lockfile tiene `libraries: []`. El proyecto contiene una identidad ejecutable, no autenticación, validación ni paquetes externos. El empaquetado de un repositorio independiente figura como mejora pendiente en su README.

## 2. Reglas arquitectónicas

- Colección amplia **en el catálogo**, pequeña **en cada aplicación**: modularidad, carga explícita, límites y pruebas.
- Validación general y determinista en Standard Library; autenticación real, consultas a red, resolución DNS, comprobación de firmas, listas oficiales y acceso al reloj pertenecen a servicios/SDK o adaptadores con capacidades explícitas.
- Separar la operación de validación de su presentación. Código de error estable e idioma de mensaje localizado en el cliente.
- Los predicados `is_*` podrán devolver booleanos; las comprobaciones `check_*` devolverán contratos de Result. Convenciones definitivas pendientes de aprobación.
- Errores de datos esperables como resultados; bugs de esquema, falta de capacidad o fallo del motor como errores operativos distintos.
- Definir presupuesto por entrada: bytes, elementos, profundidad, reglas, tiempo/recursos del host y número máximo de errores.
- No convertir todos los elementos del inventario en funciones públicas. Consolidar alias, unificar firmas y especificar semántica antes de programar.

## 3. Catálogo propuesto

**298 operaciones conceptuales de validación en 21 familias**, antes de depuración semántica y diseño final de firmas. No equivalen a 298 paquetes ni a 298 funciones ya disponibles.

| Familia | Grupo de despliegue sugerido | Prioridad | Operaciones |
|---|---|---|---:|
| Tipos y datos básicos | `core` | foundation | 12 |
| Presencia, nulidad y obligatoriedad | `core` | foundation | 12 |
| Texto y patrones | `text` | foundation | 24 |
| Unicode e internacionalización | `text` | advanced | 11 |
| Números y límites | `numbers` | foundation | 18 |
| Decimales y formatos numéricos | `numbers` | advanced | 13 |
| Listas, tuplas y colecciones | `collections` | foundation | 16 |
| Objetos y diccionarios | `collections` | foundation | 16 |
| Esquemas estructurales | `schema` | advanced | 18 |
| Reglas entre campos | `schema` | advanced | 12 |
| Fechas y duración | `datetime` | advanced | 20 |
| Identificadores y codificaciones | `formats` | advanced | 14 |
| Redes e IP | `network` | advanced | 15 |
| Web, URL, HTTP y SemVer | `formats` | advanced | 14 |
| Contacto y localización | `formats` | advanced | 14 |
| Nombres, rutas y archivos | `files` | advanced | 15 |
| Metadatos multimedia | `media` | extension | 12 |
| Coordenadas y geodatos | `geo` | extension | 11 |
| Medidas y unidades | `units` | extension | 10 |
| Presupuestos y límites de entrada | `core` | foundation | 11 |
| Composición de reglas | `core` | foundation | 10 |

### 01. Tipos y datos básicos — 12 operaciones

**Espacio de nombres conceptual:** `validate.types` · **Grupo:** `core` · **Fase:** `foundation`.

`is_string`, `is_integer`, `is_number`, `is_boolean`, `is_list`, `is_tuple`, `is_dict`, `is_none`, `is_scalar`, `is_collection`, `is_json_value`, `type_is`.

### 02. Presencia, nulidad y obligatoriedad — 12 operaciones

**Espacio de nombres conceptual:** `validate.presence` · **Grupo:** `core` · **Fase:** `foundation`.

`required`, `optional`, `nullable`, `not_null`, `not_empty`, `not_blank`, `defined`, `forbidden`, `required_if`, `forbidden_if`, `exactly_one_present`, `at_least_one_present`.

### 03. Texto y patrones — 24 operaciones

**Espacio de nombres conceptual:** `validate.text` · **Grupo:** `text` · **Fase:** `foundation`.

`length_min`, `length_max`, `length_between`, `length_exact`, `starts_with`, `ends_with`, `contains`, `not_contains`, `equals`, `equals_ignore_case`, `one_of`, `none_of`, `alphabetic`, `alphanumeric`, `ascii`, `printable`, `lowercase`, `uppercase`, `slug`, `identifier`, `regex_match`, `regex_not_match`, `trimmed`, `allowed_characters`.

### 04. Unicode e internacionalización — 11 operaciones

**Espacio de nombres conceptual:** `validate.unicode` · **Grupo:** `text` · **Fase:** `advanced`.

`unicode_scalar_valid`, `utf8_byte_length_max`, `nfc_normalized`, `nfd_normalized`, `nfkc_normalized`, `nfkd_normalized`, `unicode_category_allowed`, `unicode_script_allowed`, `no_bidi_controls`, `no_invisible_controls`, `grapheme_length_between`.

### 05. Números y límites — 18 operaciones

**Espacio de nombres conceptual:** `validate.numbers` · **Grupo:** `numbers` · **Fase:** `foundation`.

`minimum`, `maximum`, `between`, `greater_than`, `less_than`, `non_negative`, `non_positive`, `positive`, `negative`, `nonzero`, `multiple_of`, `finite`, `integer_value`, `safe_integer`, `precision_max`, `scale_max`, `percentage_range`, `unit_interval`.

### 06. Decimales y formatos numéricos — 13 operaciones

**Espacio de nombres conceptual:** `validate.decimal` · **Grupo:** `numbers` · **Fase:** `advanced`.

`integer_string`, `unsigned_integer_string`, `decimal_string`, `decimal_scale`, `decimal_precision`, `decimal_range`, `scientific_notation`, `decimal_separator_allowed`, `sign_allowed`, `currency_code_format`, `money_amount_string`, `basis_points_range`, `fixed_scale_decimal`.

### 07. Listas, tuplas y colecciones — 16 operaciones

**Espacio de nombres conceptual:** `validate.collections` · **Grupo:** `collections` · **Fase:** `foundation`.

`items_min`, `items_max`, `items_between`, `items_non_empty`, `unique_items`, `sorted_ascending`, `sorted_descending`, `all_items`, `any_item`, `no_item`, `contains_item`, `contains_all`, `contains_any`, `no_duplicate_key`, `tuple_size`, `homogeneous_items`.

### 08. Objetos y diccionarios — 16 operaciones

**Espacio de nombres conceptual:** `validate.objects` · **Grupo:** `collections` · **Fase:** `foundation`.

`required_keys`, `allowed_keys`, `forbidden_keys`, `exact_keys`, `properties_min`, `properties_max`, `properties_between`, `required_together`, `mutually_exclusive_keys`, `property_type`, `property_equals`, `property_matches`, `keys_match`, `values_match`, `no_unknown_keys`, `property_name_length`.

### 09. Esquemas estructurales — 18 operaciones

**Espacio de nombres conceptual:** `validate.schema` · **Grupo:** `schema` · **Fase:** `advanced`.

`schema_type`, `schema_enum`, `schema_const`, `schema_all_of`, `schema_any_of`, `schema_one_of`, `schema_not`, `schema_if_then_else`, `dependent_required`, `dependent_schema`, `array_items`, `tuple_items`, `object_properties`, `pattern_properties`, `additional_properties`, `local_reference`, `max_schema_depth`, `max_schema_nodes`.

### 10. Reglas entre campos — 12 operaciones

**Espacio de nombres conceptual:** `validate.cross_field` · **Grupo:** `schema` · **Fase:** `advanced`.

`fields_equal`, `fields_not_equal`, `ordered_fields`, `date_range_order`, `numeric_range_order`, `one_required_of`, `all_or_none`, `implies_field`, `dependent_min`, `dependent_max`, `conditional_requirement`, `conditional_prohibition`.

### 11. Fechas y duración — 20 operaciones

**Espacio de nombres conceptual:** `validate.datetime` · **Grupo:** `datetime` · **Fase:** `advanced`.

`iso_date`, `iso_time`, `iso_datetime`, `rfc3339_datetime`, `utc_offset`, `timezone_identifier`, `calendar_date`, `leap_year`, `date_before`, `date_after`, `date_between`, `datetime_before`, `datetime_after`, `datetime_between`, `age_min`, `age_max`, `weekday_allowed`, `unix_timestamp_range`, `iso_duration`, `duration_range`.

### 12. Identificadores y codificaciones — 14 operaciones

**Espacio de nombres conceptual:** `validate.identifiers` · **Grupo:** `formats` · **Fase:** `advanced`.

`uuid`, `uuid_v1`, `uuid_v4`, `uuid_v5`, `uuid_v6`, `uuid_v7`, `uuid_v8`, `ulid`, `hexadecimal`, `base64`, `base64url`, `sha256_hex`, `sha512_hex`, `id_charset`.

### 13. Redes e IP — 15 operaciones

**Espacio de nombres conceptual:** `validate.network` · **Grupo:** `network` · **Fase:** `advanced`.

`ipv4`, `ipv6`, `ip_address`, `ipv4_cidr`, `ipv6_cidr`, `port`, `hostname`, `dns_label`, `domain_name`, `idn_domain`, `mac_address`, `ip_in_cidr`, `private_ipv4`, `loopback_ip`, `socket_address_format`.

### 14. Web, URL, HTTP y SemVer — 14 operaciones

**Espacio de nombres conceptual:** `validate.web` · **Grupo:** `formats` · **Fase:** `advanced`.

`uri`, `absolute_url`, `relative_url`, `http_url`, `https_url`, `url_path`, `query_string`, `http_method`, `header_name`, `header_value`, `mime_type`, `media_type`, `semver`, `semver_range`.

### 15. Contacto y localización — 14 operaciones

**Espacio de nombres conceptual:** `validate.contacts_i18n` · **Grupo:** `formats` · **Fase:** `advanced`.

`email_format`, `email_domain_format`, `phone_e164`, `phone_extension`, `country_code_alpha2`, `country_code_alpha3`, `language_tag`, `locale_tag`, `postal_code_generic`, `username_format`, `user_handle`, `display_name`, `password_policy`, `password_confirmation`.

### 16. Nombres, rutas y archivos — 15 operaciones

**Espacio de nombres conceptual:** `validate.files_paths` · **Grupo:** `files` · **Fase:** `advanced`.

`safe_relative_path`, `path_without_parent_traversal`, `path_not_absolute`, `path_segment`, `filename`, `file_extension`, `extension_in`, `no_nul_byte`, `filename_length`, `file_size_range`, `file_size_max`, `declared_mime_type`, `allowed_mime_type`, `archive_member_path`, `content_hash_format`.

### 17. Metadatos multimedia — 12 operaciones

**Espacio de nombres conceptual:** `validate.media_metadata` · **Grupo:** `media` · **Fase:** `extension`.

`image_dimensions`, `image_width`, `image_height`, `image_aspect_ratio`, `video_duration`, `frame_rate`, `video_dimensions`, `audio_duration`, `sample_rate`, `audio_channels`, `bitrate_range`, `codec_identifier`.

### 18. Coordenadas y geodatos — 11 operaciones

**Espacio de nombres conceptual:** `validate.geo` · **Grupo:** `geo` · **Fase:** `extension`.

`latitude`, `longitude`, `coordinates`, `longitude_latitude_pair`, `altitude`, `bounding_box`, `point_in_box`, `geojson_position`, `geojson_bbox`, `geojson_geometry_shape`, `coordinate_precision`.

### 19. Medidas y unidades — 10 operaciones

**Espacio de nombres conceptual:** `validate.measurements` · **Grupo:** `units` · **Fase:** `extension`.

`unit_symbol`, `measurement_object`, `measurement_unit_match`, `compatible_units`, `quantity_positive`, `quantity_non_negative`, `measurement_min`, `measurement_max`, `measurement_between`, `duration_nonnegative`.

### 20. Presupuestos y límites de entrada — 11 operaciones

**Espacio de nombres conceptual:** `validate.safety_limits` · **Grupo:** `core` · **Fase:** `foundation`.

`string_byte_budget`, `collection_item_budget`, `object_property_budget`, `nesting_depth_budget`, `schema_complexity_budget`, `regex_pattern_length`, `max_error_count`, `sanitized_error_metadata`, `forbidden_sensitive_field`, `pii_field_marked`, `data_retention_days_range`.

### 21. Composición de reglas — 10 operaciones

**Espacio de nombres conceptual:** `validate.composition` · **Grupo:** `core` · **Fase:** `foundation`.

`rule_all`, `rule_any`, `rule_one`, `rule_not`, `rule_when`, `rule_each`, `rule_field`, `rule_optional`, `rule_nullable`, `rule_transform_then_validate`.

## 4. Colección independiente Results & Errors

Se debe diseñar primero un contrato de resultado que pueda expresar múltiples problemas sin exponer secretos:

```json
{
  "ok": false,
  "value": null,
  "errors": [
    {
      "code": "VALIDATION.STRING.LENGTH_MIN",
      "path": "profile.display_name",
      "message_key": "validation.string.length_min",
      "params": {
        "min": 2
      },
      "severity": "error"
    }
  ],
  "warnings": [],
  "meta": {
    "rules_evaluated": 1
  }
}
```

Contratos sugeridos: `ok(value)`, `err(code, path, params)`, `combine_results(results)`, `map_result(result, transform)`, `first_error(result)`, `has_error(result, code)`, `as_form_errors(result)`. Estos nombres son ejemplos conceptuales, no APIs FIT funcionales.

Errores de validación: `REQUIRED`, `TYPE_MISMATCH`, `INVALID_FORMAT`, `OUT_OF_RANGE`, `LENGTH_MIN`, `LENGTH_MAX`, `UNKNOWN_FIELD`, `INVALID_SCHEMA`, `RESOURCE_LIMIT`, `UNSUPPORTED_FORMAT`. Errores operativos separados: `ENGINE_FAILURE`, `CAPABILITY_UNAVAILABLE`, `DEPENDENCY_UNAVAILABLE`. Mantener `message_key` translatable, sin mensajes incrustados ni registrar credenciales.

## 5. Empaquetado FIT: colección ≠ paquete ≠ módulo

Propuesta inicial de **grupos cohesivos**: `com.blackwhi.std.result`, `com.blackwhi.std.validation.core`, `.text`, `.numbers`, `.collections`, `.schema`, `.datetime`, `.formats`, `.network`, `.files`; extensiones opcionales `.media`, `.geo`, `.units`. El nombre final depende del contrato del Registry y de la política de nombres reservados.

Cada grupo contiene varios módulos `.fit` con `load()` locales; importaciones entre paquetes solo cuando el resolver real y el lockfile las soporten. **No inventar** una URI de importación remota que el motor no haya implementado. No incluir todas las dependencias por defecto en Fitness.

```text
blackwhi-fit-standard-library/        # repositorio propuesto; no existe en el ZIP
  results/                       # contrato de éxito, error y agregación
  validation/
    core/
    text/
    numbers/
    collections/
    schema/
    datetime/
    formats/
    network/
    files/
    optional/
      media/
      geo/
      units/
  docs/
  tests/
```

## 6. Características semánticas críticas

- **Unicode:** contar puntos de código, grafemas y bytes UTF-8 no es equivalente; documentar unidad en cada regla.
- **Email:** validar formato no demuestra existencia ni propiedad del buzón; no construir una expresión regular única como si resolviera todo.
- **Contraseñas:** las reglas locales de longitud/política no prueban que una contraseña sea segura ni reemplazan las políticas del proveedor de identidad.
- **URL:** un URL formalmente válido no es seguro para accederlo; SSRF y redirecciones necesitan validación contextual en el servicio que realiza la petición.
- **Rutas:** una ruta relativa sin `..` no garantiza confinamiento tras enlaces simbólicos; resolver y comprobar en el host autorizado.
- **Archivo/media:** los metadatos y extensiones no demuestran el contenido real; la inspección de bytes, malware y descodificación pertenecen a un host especializado.
- **Tiempo:** la fecha actual es entrada explícita; no ocultar llamadas al reloj en un validador determinista.
- **Country, locale y timezone:** comprobar forma de un código no prueba su pertenencia a una lista oficial. Si se necesita lista, versionar la base de datos.
- **Dinero/decimales:** reglas exactas sobre cadenas decimales o enteros escalados; no asumir precisión arbitraria de `float`.
- **Regex:** evaluar soporte real del motor antes de exponer API, limitar patrones y tamaño de entrada, y prevenir ReDoS.
- **Starlark:** ausencia de excepciones recuperables estándar; priorizar resultados explícitos. El host define capacidades disponibles.

## 7. Fases de implementación y criterios de aceptación

**Fase 0 — Contratos y pruebas:** definir Results & Errors, semántica de `missing` vs `None`, reglas puras, serialización JSON, nomenclatura, versiones, esquema de metadatos y pruebas de compatibilidad de Starlark con el motor Rust real. Auditar resolver de paquetes y lockfiles antes de conexiones externas.

**Fase 1 — Core usable por Fitness:** tipos, presencia, texto básico, números, listas, objetos, composición y presupuestos. Realizar flujo de validación de un formulario (nombre, correo, confirmación, fecha explícita) sin autenticar contra un servidor todavía.

**Fase 2 — Format & schemas:** email, E.164, UUID, fecha ISO/RFC3339, semver, esquema estructural, reglas entre campos, Unicode. Empezar integraciones con formularios Expo, validando otra vez en backend.

**Fase 3 — Extensiones optativas:** red, URL, archivos, coordenadas, medios y unidades con pruebas reforzadas, presupuestos y adaptadores del host cuando sean necesarios.

Criterios por validador: especificación de entrada y salida; casos válidos/invalidos; límites; validación de tipos; tests positivos, negativos, frontera, internacionalización, propiedad/fuzz donde aplique; reproducibilidad; coste; documentación ES/EN; compatibilidad con motor; licencia SPDX; empaquetado `.fitpkg` real firmado y verificable cuando la cadena de distribución lo permita. Nada de mostrar como publicado antes de ese hito.

## 8. Fuentes de referencia externas

- OWASP Input Validation Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- OWASP Email Validation & Verification: https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html
- JSON Schema 2020-12: https://json-schema.org/specification
- RFC 9562 UUID: https://www.rfc-editor.org/rfc/rfc9562.html
- Starlark Language Specification: https://github.com/bazelbuild/starlark/blob/master/spec.md

**Advertencia:** todo catálogo y código de este documento son propuestas; no se ha modificado `blackwhi-fitness.zip` ni ninguna instalación local del usuario.
