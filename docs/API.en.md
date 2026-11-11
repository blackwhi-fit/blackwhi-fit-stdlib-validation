# Public API — Types & Basic Data (v0.1.0)

All twelve predicates are pure boolean functions. They never coerce or mutate their arguments.

| Function | Contract |
|---|---|
| `is_string(value)` | Exactly the FIT `string` type. |
| `is_integer(value)` | Exactly `int`; never `bool`. |
| `is_number(value)` | Exactly `int` or `float`; never `bool`. |
| `is_boolean(value)` | Exactly `bool`. |
| `is_list(value)` | Exactly `list`. |
| `is_tuple(value)` | Exactly `tuple`. |
| `is_dict(value)` | Exactly `dict`. |
| `is_none(value)` | Exactly `NoneType`. |
| `is_scalar(value)` | `string`, `int`, `float`, `bool`; not `None`. |
| `is_collection(value)` | `list`, `tuple`, `dict`; not `string`. |
| `is_json_value(value, max_depth=32, max_nodes=1024)` | Checks nested JSON-compatible lists and string-keyed dicts. Rejects tuples, non-string keys, and non-finite floating point values. Hard limits: `max_depth≤32`, `max_nodes≤4096`. Invalid budgets and exhaustion return `False`. Does not serialize or convert. |
| `type_is(value, expected)` | Exact canonical FIT type name: `string`, `int`, `float`, `bool`, `list`, `tuple`, `dict`, `NoneType`. Unknown/non-string type names return `False`. |

The root is depth zero; collections require an additional depth level for children. The node budget counts the root. Since these are only predicates, a False from `is_json_value` does not distinguish an unsupported value from exhausted budgets; future structured result APIs can distinguish these cases.

Executable examples, valid/invalid/boundary inputs, expected outcomes and related tests: `tests/cases.json`. Runtime: BlackWhi Rust/Starlark 0.14.2. Introduced in: candidate v0.1.0. Errors: functions do not claim to catch the host engine's global execution budget failures.

## Individual API profiles

All predicates were introduced in candidate `0.1.0`, perform no I/O, request no native capabilities, are deterministic and non-mutating, and return `bool`. Individually named positive, negative and boundary cases live in `tests/cases.json`, executed against the actual Rust/Starlark worker.

### `is_string(value)`

- **Signature:** `is_string(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** string.
- **Valid/invalid examples:** `is_string("FIT") → True`; `is_string(4) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_string.*`).

### `is_integer(value)`

- **Signature:** `is_integer(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** int, excluding bool.
- **Valid/invalid examples:** `is_integer(4) → True`; `is_integer(True) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_integer.*`).

### `is_number(value)`

- **Signature:** `is_number(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** int | float (not bool).
- **Valid/invalid examples:** `is_number(4.5) → True`; `is_number(False) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_number.*`).

### `is_boolean(value)`

- **Signature:** `is_boolean(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** bool.
- **Valid/invalid examples:** `is_boolean(True) → True`; `is_boolean(1) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_boolean.*`).

### `is_list(value)`

- **Signature:** `is_list(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** list.
- **Valid/invalid examples:** `is_list([]) → True`; `is_list(()) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_list.*`).

### `is_tuple(value)`

- **Signature:** `is_tuple(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** tuple.
- **Valid/invalid examples:** `is_tuple((1, 2)) → True`; `is_tuple([1, 2]) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_tuple.*`).

### `is_dict(value)`

- **Signature:** `is_dict(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** dict.
- **Valid/invalid examples:** `is_dict({}) → True`; `is_dict([]) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_dict.*`).

### `is_none(value)`

- **Signature:** `is_none(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** NoneType.
- **Valid/invalid examples:** `is_none(None) → True`; `is_none(0) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_none.*`).

### `is_scalar(value)`

- **Signature:** `is_scalar(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** string | int | float | bool.
- **Valid/invalid examples:** `is_scalar("a") → True`; `is_scalar(None) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_scalar.*`).

### `is_collection(value)`

- **Signature:** `is_collection(value) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; no coercion is performed.
- **Accepted type(s):** list | tuple | dict.
- **Valid/invalid examples:** `is_collection({}) → True`; `is_collection("a") → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`is_collection.*`).

### `is_json_value(value, max_depth=32, max_nodes=1024)`

- **Signature:** `is_json_value(value, max_depth=32, max_nodes=1024) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; `max_depth` and `max_nodes` are optional integer work limits.
- **Accepted type(s):** JSON value model; bounded iterative traversal.
- **Valid/invalid examples:** `is_json_value({"x": [1]}) → True`; `is_json_value([()]) → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; bounded iterative traversal: maximum depth 32, nodes 4096, no nonfinite floats or tuples.
- **Related tests:** `tests/cases.json` (`is_json_value.*`, and `json.*`).

### `type_is(value, expected)`

- **Signature:** `type_is(value, expected) -> bool` (documentation notation, not FIT type annotation).
- **Arguments:** `value` is inspected; `expected` must be an exact canonical type string.
- **Accepted type(s):** 8 canonical runtime types.
- **Valid/invalid examples:** `type_is(None, "NoneType") → True`; `type_is(1, "string") → False`.
- **Failure behavior:** unexpected types return `False` rather than a structured error; global engine exceptions are not suppressed.
- **Constraints:** pure, capability-free operation; exact runtime type check, no side effects or external dependencies.
- **Related tests:** `tests/cases.json` (`type_is.*`).
