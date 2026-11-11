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
