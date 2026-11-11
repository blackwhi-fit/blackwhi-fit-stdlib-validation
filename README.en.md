# BLACKWHI — FIT Standard Library: Validation

**First collection:** Types & Basic Data · 12 implemented type predicates in `packages/core/modules/types.fit`.

**Software development company:** Maobits  
**Lead Developer:** Mauricio Chara Hurtado  
**Official support:** support@blackwhi.com

## Contents

- Twelve pure FIT predicates using the actual language and runtime semantics.
- Genuine FIT-03 library manifest and version-pinned package envelope.
- Rust/Starlark runtime test cases (no Python predicate reimplementation).
- Snapshot of the 298-validator **proposal catalog** and bilingual architecture documentation.
- Reproducible package build script using the original BlackWhi FIT-03 worker.

## Verify

```bash
python3 scripts/verify_source.py
python3 tests/run_fit_tests.py --engine /path/to/blackwhi-v2/crates/fit-engine/target/debug/blackwhi-fit-engine
python3 scripts/build_fitpkg.py --blackwhi-root /path/to/blackwhi-v2
```

The Rust binary and original FIT-03 tooling must already exist in the specified BlackWhi v2 workspace. Build execution uses a private temporary copy of the required official toolchain files and never modifies the BlackWhi workspace. Artifacts are written to `dist/`. Signing and remote publishing are separate, not yet completed steps.

Read [Integration](docs/INTEGRATION.en.md) for a version-pinned FIT import.

## License

**Not selected.** No open-source rights, redistribution grants or trademark licenses are implied. Approve a legal license before public publication.
