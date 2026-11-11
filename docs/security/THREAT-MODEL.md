# Threat model — Types & Basic Data

| Threat | Mitigation | Limitation |
|---|---|---|
| Numeric coercion of boolean | Exact `type()` comparisons | No support for user-defined numeric wrappers. |
| Nested JSON stack overflow | Iterative traversal using bounded worklist | Engine has separate global tick/heap ceilings. |
| Invalid JSON key/value type | Reject tuples and non-string dict keys | Does not check textual JSON serialization output. |
| NaN/Inf in JSON | Explicit rejection based on Rust/Starlark special float spellings | Test on every supported runtime version. |
| Unbounded depth/nodes | Hard depth 32 and nodes 4096 | Predicate returns False when limits are exceeded. |
| Malicious FIT package source | SHA-pinned, verifiable package bytes | Hashes are NOT publisher signatures; local execution is NOT a sandbox. |
| Supply-chain tampering | Package verification, exact dependency pins, optional signed publishing in future | Publisher identity and signature are not yet authenticated. |
