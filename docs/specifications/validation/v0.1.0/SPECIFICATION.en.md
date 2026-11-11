# BlackWhi FIT Standard Library — Validator proposal v0.1.0

**Status:** PROPOSAL — neither implemented FIT code nor an approved public API. **Date:** 2026-11-10. **Inspected consumer repository:** `com.blackwhi.fitness@0.1.0` (user-provided ZIP).

## 1. Evidence from the attached project

The files `main.fit`, `modules/project.fit`, `fit-program.json`, `fit-lock.json`, `README.md`, `docs/architecture/PROJECT.md`, and `tests/test_foundation.py` were examined. The manifest declares `blackwhi.fit.program.v2` and the `starlark-rust@0.14.2` engine, with no `required_capabilities` and no `requested_permissions`; the lockfile contains `libraries: []`. The project has an executable project identity, but no authentication, validators, or external packages. Its README lists packaging into an independent repository as a pending improvement.

## 2. Architectural rules

- Maintain a **large catalog**, but a **small footprint per application**: modularity, explicit loading, resource limits, and tests.
- General, deterministic validation belongs in the Standard Library. Actual authentication, network requests, DNS resolution, signature verification, official registries, and clock access belong to services/SDKs or capability-scoped adapters.
- Separate validation from presentation. Keep error codes stable and localize their messages in the client.
- `is_*` predicates may return booleans; `check_*` operations should return the shared Result contract. Final conventions remain subject to approval.
- Represent expected invalid input as results, while distinguishing schema bugs, missing capabilities, and engine failures as operational errors.
- Specify a resource budget per input: bytes, items, nesting depth, rules, host time/resources, and maximum error count.
- Do not turn every inventory entry into a public function. Consolidate aliases, unify signatures, and specify behavior before implementation.

## 3. Proposed catalog

**298 conceptual validation operations across 21 families**, before semantic deduplication and final function-signature design. This does not mean 298 packages or 298 currently implemented functions.

| Family | Suggested deployment group | Priority | Operations |
|---|---|---|---:|
| Basic types and data | `core` | `foundation` | 12 |
| Presence, nullability and requiredness | `core` | `foundation` | 12 |
| Text and patterns | `text` | `foundation` | 24 |
| Unicode and internationalization | `text` | `advanced` | 11 |
| Numbers and bounds | `numbers` | `foundation` | 18 |
| Decimals and numeric formats | `numbers` | `advanced` | 13 |
| Lists, tuples and collections | `collections` | `foundation` | 16 |
| Objects and dictionaries | `collections` | `foundation` | 16 |
| Structural schemas | `schema` | `advanced` | 18 |
| Cross-field rules | `schema` | `advanced` | 12 |
| Dates and durations | `datetime` | `advanced` | 20 |
| Identifiers and encodings | `formats` | `advanced` | 14 |
| Networking and IP | `network` | `advanced` | 15 |
| Web, URLs, HTTP and SemVer | `formats` | `advanced` | 14 |
| Contacts and localization | `formats` | `advanced` | 14 |
| Names, paths and files | `files` | `advanced` | 15 |
| Media metadata | `media` | `extension` | 12 |
| Coordinates and geodata | `geo` | `extension` | 11 |
| Measurements and units | `units` | `extension` | 10 |
| Input budgets and limits | `core` | `foundation` | 11 |
| Rule composition | `core` | `foundation` | 10 |

### 01. Basic types and data — 12 operations

**Conceptual namespace:** `validate.types` · **Group:** `core` · **Tier:** `foundation`.

`is_string`, `is_integer`, `is_number`, `is_boolean`, `is_list`, `is_tuple`, `is_dict`, `is_none`, `is_scalar`, `is_collection`, `is_json_value`, `type_is`.

### 02. Presence, nullability and requiredness — 12 operations

**Conceptual namespace:** `validate.presence` · **Group:** `core` · **Tier:** `foundation`.

`required`, `optional`, `nullable`, `not_null`, `not_empty`, `not_blank`, `defined`, `forbidden`, `required_if`, `forbidden_if`, `exactly_one_present`, `at_least_one_present`.

### 03. Text and patterns — 24 operations

**Conceptual namespace:** `validate.text` · **Group:** `text` · **Tier:** `foundation`.

`length_min`, `length_max`, `length_between`, `length_exact`, `starts_with`, `ends_with`, `contains`, `not_contains`, `equals`, `equals_ignore_case`, `one_of`, `none_of`, `alphabetic`, `alphanumeric`, `ascii`, `printable`, `lowercase`, `uppercase`, `slug`, `identifier`, `regex_match`, `regex_not_match`, `trimmed`, `allowed_characters`.

### 04. Unicode and internationalization — 11 operations

**Conceptual namespace:** `validate.unicode` · **Group:** `text` · **Tier:** `advanced`.

`unicode_scalar_valid`, `utf8_byte_length_max`, `nfc_normalized`, `nfd_normalized`, `nfkc_normalized`, `nfkd_normalized`, `unicode_category_allowed`, `unicode_script_allowed`, `no_bidi_controls`, `no_invisible_controls`, `grapheme_length_between`.

### 05. Numbers and bounds — 18 operations

**Conceptual namespace:** `validate.numbers` · **Group:** `numbers` · **Tier:** `foundation`.

`minimum`, `maximum`, `between`, `greater_than`, `less_than`, `non_negative`, `non_positive`, `positive`, `negative`, `nonzero`, `multiple_of`, `finite`, `integer_value`, `safe_integer`, `precision_max`, `scale_max`, `percentage_range`, `unit_interval`.

### 06. Decimals and numeric formats — 13 operations

**Conceptual namespace:** `validate.decimal` · **Group:** `numbers` · **Tier:** `advanced`.

`integer_string`, `unsigned_integer_string`, `decimal_string`, `decimal_scale`, `decimal_precision`, `decimal_range`, `scientific_notation`, `decimal_separator_allowed`, `sign_allowed`, `currency_code_format`, `money_amount_string`, `basis_points_range`, `fixed_scale_decimal`.

### 07. Lists, tuples and collections — 16 operations

**Conceptual namespace:** `validate.collections` · **Group:** `collections` · **Tier:** `foundation`.

`items_min`, `items_max`, `items_between`, `items_non_empty`, `unique_items`, `sorted_ascending`, `sorted_descending`, `all_items`, `any_item`, `no_item`, `contains_item`, `contains_all`, `contains_any`, `no_duplicate_key`, `tuple_size`, `homogeneous_items`.

### 08. Objects and dictionaries — 16 operations

**Conceptual namespace:** `validate.objects` · **Group:** `collections` · **Tier:** `foundation`.

`required_keys`, `allowed_keys`, `forbidden_keys`, `exact_keys`, `properties_min`, `properties_max`, `properties_between`, `required_together`, `mutually_exclusive_keys`, `property_type`, `property_equals`, `property_matches`, `keys_match`, `values_match`, `no_unknown_keys`, `property_name_length`.

### 09. Structural schemas — 18 operations

**Conceptual namespace:** `validate.schema` · **Group:** `schema` · **Tier:** `advanced`.

`schema_type`, `schema_enum`, `schema_const`, `schema_all_of`, `schema_any_of`, `schema_one_of`, `schema_not`, `schema_if_then_else`, `dependent_required`, `dependent_schema`, `array_items`, `tuple_items`, `object_properties`, `pattern_properties`, `additional_properties`, `local_reference`, `max_schema_depth`, `max_schema_nodes`.

### 10. Cross-field rules — 12 operations

**Conceptual namespace:** `validate.cross_field` · **Group:** `schema` · **Tier:** `advanced`.

`fields_equal`, `fields_not_equal`, `ordered_fields`, `date_range_order`, `numeric_range_order`, `one_required_of`, `all_or_none`, `implies_field`, `dependent_min`, `dependent_max`, `conditional_requirement`, `conditional_prohibition`.

### 11. Dates and durations — 20 operations

**Conceptual namespace:** `validate.datetime` · **Group:** `datetime` · **Tier:** `advanced`.

`iso_date`, `iso_time`, `iso_datetime`, `rfc3339_datetime`, `utc_offset`, `timezone_identifier`, `calendar_date`, `leap_year`, `date_before`, `date_after`, `date_between`, `datetime_before`, `datetime_after`, `datetime_between`, `age_min`, `age_max`, `weekday_allowed`, `unix_timestamp_range`, `iso_duration`, `duration_range`.

### 12. Identifiers and encodings — 14 operations

**Conceptual namespace:** `validate.identifiers` · **Group:** `formats` · **Tier:** `advanced`.

`uuid`, `uuid_v1`, `uuid_v4`, `uuid_v5`, `uuid_v6`, `uuid_v7`, `uuid_v8`, `ulid`, `hexadecimal`, `base64`, `base64url`, `sha256_hex`, `sha512_hex`, `id_charset`.

### 13. Networking and IP — 15 operations

**Conceptual namespace:** `validate.network` · **Group:** `network` · **Tier:** `advanced`.

`ipv4`, `ipv6`, `ip_address`, `ipv4_cidr`, `ipv6_cidr`, `port`, `hostname`, `dns_label`, `domain_name`, `idn_domain`, `mac_address`, `ip_in_cidr`, `private_ipv4`, `loopback_ip`, `socket_address_format`.

### 14. Web, URLs, HTTP and SemVer — 14 operations

**Conceptual namespace:** `validate.web` · **Group:** `formats` · **Tier:** `advanced`.

`uri`, `absolute_url`, `relative_url`, `http_url`, `https_url`, `url_path`, `query_string`, `http_method`, `header_name`, `header_value`, `mime_type`, `media_type`, `semver`, `semver_range`.

### 15. Contacts and localization — 14 operations

**Conceptual namespace:** `validate.contacts_i18n` · **Group:** `formats` · **Tier:** `advanced`.

`email_format`, `email_domain_format`, `phone_e164`, `phone_extension`, `country_code_alpha2`, `country_code_alpha3`, `language_tag`, `locale_tag`, `postal_code_generic`, `username_format`, `user_handle`, `display_name`, `password_policy`, `password_confirmation`.

### 16. Names, paths and files — 15 operations

**Conceptual namespace:** `validate.files_paths` · **Group:** `files` · **Tier:** `advanced`.

`safe_relative_path`, `path_without_parent_traversal`, `path_not_absolute`, `path_segment`, `filename`, `file_extension`, `extension_in`, `no_nul_byte`, `filename_length`, `file_size_range`, `file_size_max`, `declared_mime_type`, `allowed_mime_type`, `archive_member_path`, `content_hash_format`.

### 17. Media metadata — 12 operations

**Conceptual namespace:** `validate.media_metadata` · **Group:** `media` · **Tier:** `extension`.

`image_dimensions`, `image_width`, `image_height`, `image_aspect_ratio`, `video_duration`, `frame_rate`, `video_dimensions`, `audio_duration`, `sample_rate`, `audio_channels`, `bitrate_range`, `codec_identifier`.

### 18. Coordinates and geodata — 11 operations

**Conceptual namespace:** `validate.geo` · **Group:** `geo` · **Tier:** `extension`.

`latitude`, `longitude`, `coordinates`, `longitude_latitude_pair`, `altitude`, `bounding_box`, `point_in_box`, `geojson_position`, `geojson_bbox`, `geojson_geometry_shape`, `coordinate_precision`.

### 19. Measurements and units — 10 operations

**Conceptual namespace:** `validate.measurements` · **Group:** `units` · **Tier:** `extension`.

`unit_symbol`, `measurement_object`, `measurement_unit_match`, `compatible_units`, `quantity_positive`, `quantity_non_negative`, `measurement_min`, `measurement_max`, `measurement_between`, `duration_nonnegative`.

### 20. Input budgets and limits — 11 operations

**Conceptual namespace:** `validate.safety_limits` · **Group:** `core` · **Tier:** `foundation`.

`string_byte_budget`, `collection_item_budget`, `object_property_budget`, `nesting_depth_budget`, `schema_complexity_budget`, `regex_pattern_length`, `max_error_count`, `sanitized_error_metadata`, `forbidden_sensitive_field`, `pii_field_marked`, `data_retention_days_range`.

### 21. Rule composition — 10 operations

**Conceptual namespace:** `validate.composition` · **Group:** `core` · **Tier:** `foundation`.

`rule_all`, `rule_any`, `rule_one`, `rule_not`, `rule_when`, `rule_each`, `rule_field`, `rule_optional`, `rule_nullable`, `rule_transform_then_validate`.

## 4. Independent Results & Errors collection

Design a result contract first, capable of representing multiple issues without leaking secrets:

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

Suggested contracts: `ok(value)`, `err(code, path, params)`, `combine_results(results)`, `map_result(result, transform)`, `first_error(result)`, `has_error(result, code)`, `as_form_errors(result)`. These are conceptual names, **not working FIT APIs**.

Validation error categories: `REQUIRED`, `TYPE_MISMATCH`, `INVALID_FORMAT`, `OUT_OF_RANGE`, `LENGTH_MIN`, `LENGTH_MAX`, `UNKNOWN_FIELD`, `INVALID_SCHEMA`, `RESOURCE_LIMIT`, `UNSUPPORTED_FORMAT`. Keep operational errors distinct: `ENGINE_FAILURE`, `CAPABILITY_UNAVAILABLE`, `DEPENDENCY_UNAVAILABLE`. Preserve localizable `message_key` values, avoid embedding user-facing messages in the validator, and never log credentials.

## 5. FIT packaging: collection ≠ package ≠ module

Proposed **cohesive groups**: `com.blackwhi.std.result`, `com.blackwhi.std.validation.core`, `.text`, `.numbers`, `.collections`, `.schema`, `.datetime`, `.formats`, `.network`, `.files`; optional extensions: `.media`, `.geo`, `.units`. Final package names depend on Registry contracts and reserved-name policy.

Each group contains multiple `.fit` modules using local `load()` statements. Cross-package imports must wait until the actual resolver and lockfile support them. **Do not invent** a remote import URI that the runtime has not implemented. Do not add all packages as default Fitness dependencies.

```text
blackwhi-fit-standard-library/        # proposed repository; absent from the ZIP
  results/                       # success, error and aggregation contracts
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

## 6. Critical semantic considerations

- **Unicode:** counting Unicode code points, grapheme clusters, and UTF-8 bytes gives different answers; state the unit for each rule.
- **Email:** checking syntax does not prove the mailbox exists or that a user controls it; a single regex is not a complete solution.
- **Passwords:** local length/policy checks cannot prove password strength or replace the identity provider's security rules.
- **URLs:** a syntactically valid URL is not necessarily safe to fetch; SSRF and redirects require contextual checks in the requesting service.
- **Paths:** a relative path without `..` is not sufficient to guarantee confinement when symbolic links exist; the authorized host must resolve and check the actual path.
- **Files/media:** extensions and declared metadata cannot prove actual file contents; byte inspection, malware scanning, and decoding belong to specialized host services.
- **Time:** pass the current/reference date explicitly; deterministic validators must not read the clock implicitly.
- **Country, locale and timezone:** checking the shape of a code is not proof of membership in an official registry. Version the reference dataset when needed.
- **Money/decimals:** prefer exact decimal-string rules or scaled integers; do not assume arbitrary `float` precision.
- **Regex:** verify actual engine support before publishing an API, bound patterns and input size, and mitigate ReDoS risks.
- **Starlark:** standard recoverable Python exceptions are not available; prefer explicit results. The host decides which capabilities exist.

## 7. Implementation phases and acceptance criteria

**Phase 0 — Contracts and tests:** specify Results & Errors, the semantics of `missing` versus `None`, pure validation rules, JSON serialization, naming, versioning, metadata schemas, and compatibility tests against the real Rust/Starlark engine. Audit the package resolver and lockfile before introducing cross-package integrations.

**Phase 1 — Fitness-ready core:** types, presence, basic text, numbers, lists, objects, composition, and input budgets. Prove a form-validation flow (name, email, confirmation, explicit reference date) without authenticating against a server yet.

**Phase 2 — Formats and schemas:** email, E.164, UUID, ISO/RFC3339 dates, SemVer, structural schema, cross-field rules, and Unicode. Begin integrating with Expo forms, validating again in the backend.

**Phase 3 — Optional extensions:** networking, URLs, files, coordinates, media, and units with strengthened tests, budgets, and host adapters where necessary.

Validator-level acceptance criteria: defined input/output contracts; valid/invalid cases and boundaries; type validation; positive, negative, edge-case, internationalization, property/fuzz tests when appropriate; reproducibility; resource cost; ES/EN documentation; engine compatibility; SPDX license; and an actually signed and verifiable `.fitpkg` when the publishing pipeline supports it. Do not claim a package is published before that milestone.

## 8. External reference sources

- OWASP Input Validation Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html
- OWASP Email Validation & Verification: https://cheatsheetseries.owasp.org/cheatsheets/Email_Validation_and_Verification_Cheat_Sheet.html
- JSON Schema 2020-12: https://json-schema.org/specification
- RFC 9562 UUID: https://www.rfc-editor.org/rfc/rfc9562.html
- Starlark Language Specification: https://github.com/bazelbuild/starlark/blob/master/spec.md

**Notice:** all catalog entries and code samples in this document are proposals; the user-provided `blackwhi-fitness.zip` and the user's local installation have not been modified.
