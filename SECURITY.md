# Security Policy / Política de seguridad

Please report security vulnerabilities **privately** to **support@blackwhi.com**. Do not publish working exploits or user data in public issues.

- This library currently performs **pure local predicates** and requests no runtime capabilities or permissions.
- `is_json_value` applies fixed maximum limits of 32 levels and 4096 visited nodes. Its default budgets are 32 levels and 1024 visited nodes. The function returns `False` on budget exhaustion; this is not a parsing or conversion interface.
- Local FIT packages are **not a sandbox**. Only execute trusted code; check artifact integrity. Hashes alone are not publisher signatures.
- CI security and runtime verifications must not be bypassed for releases.

A response-time service-level agreement has not been established.
