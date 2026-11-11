# FIT-03 version-pinned Validation integration

1. Library identity: `com.blackwhi.std.validation.core@0.1.0`.
2. Install `fit-library.json` and `modules/types.fit` under `libraries/fit/com.blackwhi.std.validation.core/0.1.0/` in the trusted BlackWhi workspace, preserving their exact SHA-256 values.
3. Resolve into `fit-lock.json` using the supported `blackwhi fit package lock <path/fit-program.json> com.blackwhi.std.validation.core@0.1.0` operation.
4. Import the function from a package's vendored library:

```python
load("vendor/com.blackwhi.std.validation.core/0.1.0/modules/types.fit", "is_string")

is_string("BlackWhi")
```

5. Run the actual CLI `validate`, `build`, `verify` and `run` actions.

**Format note:** FIT-03 v0.5.2 packages a runnable program and hash-pinned vendored libraries in a `.fitpkg`; it is not yet a library-only artifact contract. This repository exports a real, executable, verified package envelope and a separate library source manifest. No remote publication is claimed.
