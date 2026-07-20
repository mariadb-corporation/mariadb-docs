---
name: mariadb-create-function
description: "MariaDB-specific syntax and behavior for CREATE FUNCTION across its three distinct forms — stored functions (RETURNS + RETURN, IN/OUT/INOUT parameters, DETERMINISTIC/binlog interaction), stored aggregate functions (CREATE AGGREGATE FUNCTION with FETCH GROUP NEXT ROW), and loadable user-defined functions (CREATE FUNCTION ... SONAME 'lib.so', a plugin_dir-loaded shared library unrelated to stored routines). Use when writing, generating, or reviewing any CREATE FUNCTION statement, a custom aggregate, or a UDF registration targeting MariaDB."
---

# CREATE FUNCTION in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between standard SQL stored functions and MariaDB's three CREATE FUNCTION forms**: (1) ordinary **stored functions**, (2) **stored aggregate functions** (`CREATE AGGREGATE FUNCTION`), and (3) **loadable UDFs** (`CREATE FUNCTION ... SONAME`) — a mechanism unrelated to stored routines that loads a compiled shared library. These three share a keyword but almost nothing else; do not conflate them.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| Assuming stored function parameters are `IN`-only, like standard SQL | MariaDB allows `OUT` and `INOUT` (`IN OUT` is the same thing) on function parameters *(since 10.8)* — but they can only be supplied when the function is called from a `SET` assignment, not from a `SELECT`. Calling with an `OUT`/`INOUT` arg from `SELECT` raises error 4186, "OUT or INOUT argument N for function X is not allowed here" |
| Omitting `DETERMINISTIC`/`NOT DETERMINISTIC` and assuming a sensible default | The characteristic defaults to **`NOT DETERMINISTIC`** if omitted — the pessimistic default, not the optimistic one |
| Creating a non-deterministic function on a server with binary logging on and being surprised by an error | With `--log-bin` on and `log_bin_trust_function_creators=OFF` (the default), creating **any** stored function requires a `SUPER`-class privilege (`LOG BIN TRUSTED SP CREATOR`); a **non-deterministic** function whose data-access characteristic is `CONTAINS SQL` or `MODIFIES SQL DATA` is rejected outright regardless of privilege. Set `log_bin_trust_function_creators=ON` (session/global) for dev/test convenience, or mark the function `DETERMINISTIC`+`READS SQL DATA` if that's actually true |
| Writing an aggregate as a regular scalar function plus a `GROUP BY` hack | Use `CREATE AGGREGATE FUNCTION` with a loop containing `FETCH GROUP NEXT ROW` — the MariaDB-specific mechanism for custom aggregates, callable in `GROUP BY` queries and as a window function |
| Writing `CREATE FUNCTION foo RETURNS INT SONAME 'lib.so'` and expecting it to behave like a stored function | It's a completely different object — a **UDF**, backed by a compiled shared library the server loads from `plugin_dir`, recorded in `mysql.func`. No SQL body, no `BEGIN...END`, no `RETURN` statement — `RETURNS` here is restricted to `STRING`\|`INTEGER`\|`REAL`\|`DECIMAL` only |
| Assuming a stored function silently shadows or is shadowed consistently by a same-named UDF | Unqualified function-call resolution order is: native built-ins, then **UDFs**, then type constructors, then **stored functions** last. A UDF named `foo` always wins over a stored function named `foo` for unqualified calls |
| Writing a regular `SELECT ...` inside a stored function body to fetch a value | Not permitted — any statement returning a result set is disallowed in a stored function. Use `SELECT ... INTO var` (or a subselect in the `RETURN` expression) instead |
| Forgetting a `RETURN` in the function body | Compile-time error (`ER_SP_NORETURN`) if no `RETURN` appears anywhere in the body; if execution reaches the end without having *executed* one at runtime, error `ER_SP_NORETURNEND` ("FUNCTION x ended without RETURN") |

## Stored Functions

```sql
CREATE [OR REPLACE]
    [DEFINER = {user | CURRENT_USER | role | CURRENT_ROLE}]
    FUNCTION [IF NOT EXISTS] func_name ([func_parameter[,...]])
    RETURNS type
    [characteristic ...]
    RETURN expr | func_body   -- func_body: BEGIN...END containing a RETURN
```

- `func_parameter`: `[IN | OUT | INOUT | IN OUT] param_name type [DEFAULT value]`. `IN` is the default direction. `DEFAULT` on a parameter is a MariaDB extension, not standard SQL.
- **`RETURNS` is the declaration** (the type, stated once, in the header); **`RETURN`** is the *statement* that produces a value and exits — either a bare expression (`RETURN expr;`) or inside a `BEGIN...END` compound body, which must contain at least one `RETURN`.
- `characteristic`: `LANGUAGE SQL` (accepted, no effect — SQL is the only language) | `[NOT] DETERMINISTIC` | `{CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA}` (informational only, unchecked; defaults to `CONTAINS SQL` if omitted) | `SQL SECURITY {DEFINER | INVOKER}` (defaults to `DEFINER`) | `COMMENT 'string'`.
- Requires the `CREATE ROUTINE` privilege to create, `EXECUTE` to call; creation auto-grants `EXECUTE`/`ALTER ROUTINE` to the creator even when `DEFINER` names someone else.
- Stored-function-only restrictions (beyond the general stored-routine limitations): no statement that returns a result set (use `SELECT ... INTO`), no `FLUSH`, no explicit/implicit commit or rollback, no recursion, cannot modify a table already in use by the invoking statement, no prepared statements (`PREPARE`/`EXECUTE`/dynamic SQL).

```sql
CREATE FUNCTION hello(s CHAR(20)) RETURNS CHAR(50) DETERMINISTIC
  RETURN CONCAT('Hello, ', s, '!');
```

## Stored Aggregate Functions

```sql
CREATE [OR REPLACE] [DEFINER = ...] AGGREGATE FUNCTION [IF NOT EXISTS]
    func_name ([func_parameter[,...]]) RETURNS type
BEGIN
    -- declarations
    DECLARE CONTINUE HANDLER FOR NOT FOUND RETURN return_val;
    LOOP
        FETCH GROUP NEXT ROW;   -- pulls the next row of the current group
        -- accumulate into local state
    END LOOP;
END;
```

- Everything about a plain stored function applies, plus: the `AGGREGATE` keyword, and `FETCH GROUP NEXT ROW` inside the loop — MariaDB's mechanism for driving the row-by-row accumulation. There is no separate "initialize/iterate/terminate" API to implement (unlike UDF aggregates below); it's one loop with a `NOT FOUND` handler that fires when the group is exhausted, from which you `RETURN` the accumulated result.
- Callable in `GROUP BY` queries and as a window function, exactly like a built-in aggregate.
- Oracle-mode (`sql_mode=ORACLE`) syntax is also supported, using `RETURN` (not `RETURNS`) in the header and an `EXCEPTION WHEN NO_DATA_FOUND` block instead of a `CONTINUE HANDLER`.

## User-Defined (Loadable) Functions — `CREATE FUNCTION ... SONAME`

```sql
CREATE [OR REPLACE] [AGGREGATE] FUNCTION [IF NOT EXISTS] function_name
    RETURNS {STRING | INTEGER | REAL | DECIMAL}
    SONAME 'shared_library_name';
```

This is **not** a stored function — no body, no `BEGIN...END`, no `RETURN`. It registers a function implemented in a compiled shared library (`.so`/`.dll`), loaded from the `plugin_dir` directory. `shared_library_name` is a **basename**, not a path.

- Requires the `INSERT` privilege on the `mysql` database (`INSERT` + `DELETE` if `OR REPLACE` is used) — a different privilege model from stored routines' `CREATE ROUTINE`. Registration adds a row to `mysql.func`.
- `RETURNS` here is limited to four keywords: `STRING`, `INTEGER`, `REAL`, `DECIMAL`. `DECIMAL` UDFs are implemented at the C level the same way as `STRING` UDFs (no native C decimal type in the calling convention).
- `AGGREGATE` marks the UDF as an aggregate (summary) function, implemented via the UDF aggregate C API rather than `FETCH GROUP NEXT ROW`. Aggregate UDFs can also be used as window functions.
- Statements using UDFs are **not safe for statement-based replication**.
- **Name-collision precedence**: for an unqualified call, MariaDB resolves native built-ins first, then UDFs, then type constructors, then stored functions last — a UDF shadows a same-named stored function, not the other way around.
- To upgrade a UDF's library, `DROP FUNCTION` first, replace the library file, then `CREATE FUNCTION` again — swapping the library in place under a loaded UDF can crash the server.

## See Also

- **`mariadb-create-procedure`** — shared stored-routine surface (parameters, characteristics, privileges) without the `RETURNS`/`RETURN` requirement
- **`mariadb-create-trigger`** — another routine body context governed by the same `log_bin_trust_function_creators` binlog-safety gate
- Canonical references on `mariadb.com/docs` (consult for edge cases not covered here):
  - <https://mariadb.com/docs/server/reference/sql-statements/data-definition/create/create-function>
  - <https://mariadb.com/docs/server/server-usage/stored-routines/stored-functions/stored-aggregate-functions>
  - <https://mariadb.com/docs/server/server-usage/user-defined-functions/create-function-udf>
