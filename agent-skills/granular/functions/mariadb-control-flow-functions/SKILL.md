---
name: mariadb-control-flow-functions
description: "MariaDB control-flow functions and operators — IF(), IFNULL()/NVL(), NULLIF(), COALESCE(), the CASE operator (simple and searched forms), NVL2(), and DECODE/DECODE_ORACLE. Use when writing SQL that branches on a condition, substitutes for NULL, or matches a value against a list of alternatives in MariaDB."
---

# MariaDB Control-Flow Functions

*Last updated: 2026-07-20*

Catalog of every built-in control-flow function in MariaDB, with signature and
a one-line semantic summary per entry. The `CASE` operator and `DECODE_ORACLE`
are documented here by hand (their pages aren't picked up by the catalog
extractor) — see the "What LLMs Often Miss" table and the canonical pages
linked below. For a function not listed here, fall back to the canonical
reference at
<https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user specifies
> another version. Functions with a `*(since X.Y)*` annotation are only
> available from that version onward; everything else is in every current LTS
> branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes… | Prefer (MariaDB) | Why |
| --- | --- | --- |
| `IF (x > 0) THEN ... END IF;` inside a plain `SELECT` | `IF(x > 0, a, b)` — the **three-argument function** — anywhere an expression is valid | `IF ... THEN ... END IF` is a **statement**, only legal inside stored-program bodies (triggers, procedures, functions). `IF()` the function takes exactly 3 args and returns a value; it works in ordinary SQL |
| `CASE ... END CASE` in a `SELECT` list or `WHERE` clause | `CASE ... END` (no `CASE` after `END`) as an **expression** | The bare `CASE value WHEN ... END` / `CASE WHEN ... END` operator is valid anywhere an expression is valid. `CASE ... END CASE` is the **compound statement** form, legal only inside stored-program bodies |
| `IFNULL(a, b)` when there are more than two fallback candidates | `COALESCE(a, b, c, ...)` | `IFNULL()` is fixed at exactly 2 arguments; `COALESCE()` accepts any number and returns the first non-`NULL`. With exactly two arguments they're equivalent |
| `IFNULL(x, ...)` to test whether `x` is `NULL` | `ISNULL(x)` for a **boolean** test, `IFNULL(x, y)` for a **substitution** | They solve different problems: `ISNULL(expr)` is single-argument and returns `1`/`0`; `IFNULL(expr1, expr2)` is two-argument and returns a **value** (`expr1` or `expr2`) |
| `x / y` where `y` can be `0`, relying on a `NULL`-safe division | `x / NULLIF(y, 0)` | `NULLIF(a, b)` returns `NULL` when `a = b`, otherwise `a` — it's shorthand for `CASE WHEN a=b THEN NULL ELSE a END`. Guarding the divisor with `NULLIF(y, 0)` turns a division error into a `NULL` result instead of failing the statement |
| `COALESCE(int_col, 'literal')` / mixing incompatible types across branches, expecting the DB to "figure it out" | Cast explicit branches to a common type, or rely on documented type-aggregation rules | `COALESCE()`, `IF()`, and `CASE` all aggregate a single result type across their value arguments. A hex literal passed to `COALESCE()` is treated as a **string**, not a number, even though the same literal inserted directly into an `INT` column is treated as a number — a documented gotcha in the `COALESCE` reference page |
| `DECODE(expr, search1, result1, search2, result2, default)` and expecting it to work outside Oracle mode | `DECODE_ORACLE(expr, search1, result1, ...)` for the value-matching form in **any** SQL mode | Plain `DECODE(crypt_str, pass_str)` is the **decryption** function (reverse of `ENCODE()`) in default mode — only **two** arguments. The Oracle-style value-matching form is available under that name only when `sql_mode=ORACLE`; `DECODE_ORACLE` is the synonym that works in all modes |
| `DECODE(expr, NULL, 'x', 'y')` expecting `NULL` to never match | Rely on `NULL`-equals-`NULL` matching, or guard explicitly if that's unwanted | In the Oracle-mode matching form (and in `DECODE_ORACLE`), `NULL` values in the search list are treated as **equivalent** to a `NULL` expr — the opposite of standard SQL `=` semantics, where `NULL = NULL` is `NULL`/unknown |

## Functions

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/control-flow-functions -->
<!-- 5 functions, 2 pages skipped on extraction failure -->

### IF
`IF(expr1,expr2,expr3)`  
If `expr1` is `TRUE` (`expr1 <> 0` and `expr1 <> NULL`) then `IF()` returns `expr2`; otherwise it returns `expr3`.

### IFNULL
`IFNULL(expr1,expr2)`  
If _`expr1`_ is not `NULL`, `IFNULL()` returns _`expr1`_; otherwise it returns_`expr2`_.

### NULLIF
`NULLIF(expr1,expr2)`  
Returns `NULL` if expr1 = expr2 is true, otherwise returns expr1.

### NVL
Alias for `IFNULL`.

### NVL2
`NVL2(expr1,expr2,expr3)`  
The `NVL2` function returns a value based on whether a specified expression is `NULL` or not.
<!-- END GENERATED -->

## See Also

- Canonical reference: <https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions>
- CASE operator (hand-linked, not in the generated catalog): <https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions/case-operator>
- DECODE_ORACLE (hand-linked, not in the generated catalog): <https://mariadb.com/docs/server/reference/sql-functions/control-flow-functions/decode_oracle>
- DECODE (decrypt / Oracle-mode value matching): <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/encryption-hashing-and-compression-functions/decode>
- COALESCE (documented under comparison operators, not control-flow): <https://mariadb.com/docs/server/reference/sql-structure/operators/comparison-operators/coalesce>
- ISNULL / IS NULL operator: <https://mariadb.com/docs/server/reference/sql-structure/operators/comparison-operators/isnull>
- IF statement (stored-program form, distinct from the `IF()` function): <https://mariadb.com/docs/server/reference/sql-statements/programmatic-compound-statements/if>
- CASE statement (stored-program form, distinct from the CASE operator): <https://mariadb.com/docs/server/reference/sql-statements/programmatic-compound-statements/case-statement>
