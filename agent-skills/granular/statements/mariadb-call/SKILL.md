---
name: mariadb-call
description: "MariaDB-specific syntax and behavior for CALL — optional parentheses when a procedure takes no arguments, OUT/INOUT parameters that must bind to user-defined variables, procedures returning result sets directly to the client (unlike stored functions), the EXECUTE privilege requirement, CALL as a prepared statement, and max_sp_recursion_depth for recursive procedures. Use when writing, generating, or reviewing CALL statements that invoke MariaDB stored procedures."
---

# CALL in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between invoking a routine in standard SQL and MariaDB's `CALL`**. It assumes the agent already knows that `CALL` invokes a previously defined stored procedure. Everything below documents MariaDB-specific parameter passing, result-set semantics, privileges, prepared-statement support, and recursion — plus the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `CALL sp_name();` for every invocation, even with zero parameters | Parentheses are optional when there are no arguments: `CALL sp_name;` and `CALL sp_name();` are equivalent. Don't assume the parens are mandatory |
| `CALL sp_name('literal_out_placeholder', ...)` for an `OUT`/`INOUT` parameter | `OUT` and `INOUT` parameters must be bound to a **user-defined variable** (`@var`), not a literal — the server writes the returned value back into that variable. Read it with a follow-up `SELECT @var;` |
| Treating a called procedure's `SELECT` output like a function's return value | A stored procedure can send **one or more result sets straight to the client** (each `SELECT` in its body produces one) — a stored function cannot do this at all, it only returns a scalar via `RETURN`. Don't conflate the two |
| Assuming `CALL` always needs `EXECUTE`-plus-`SELECT` privilege on referenced tables | The caller needs the **`EXECUTE`** privilege on the procedure itself (or a broader routine/DB-level grant); the procedure's own body statements run with the privileges implied by `SQL SECURITY DEFINER`/`INVOKER`, not the caller's table grants |
| Writing a recursive procedure and expecting it to just work | Recursion is **disabled by default**. Set the session variable `max_sp_recursion_depth` (default `0`, range `0`–`255`) to a nonzero value before calling a self-recursive procedure, or it fails immediately |
| Calling a result-set-returning procedure from inside a stored function or trigger | Not allowed — a procedure that contains a `SELECT` (or dynamic SQL) cannot be invoked from a function or trigger context; the server raises an error rather than silently discarding the extra result set |

## Syntax

```sql
CALL sp_name([parameter[, ...]]);
CALL sp_name;          -- parens optional with no arguments
CALL db_name.sp_name(parameter[, ...]);
```

- Parentheses may be omitted entirely when the procedure takes no parameters — `CALL p` and `CALL p()` are equivalent.
- The procedure name can be schema-qualified (`db_name.sp_name`); back-tick either identifier if it's a reserved word or contains special characters.
- Any amount of whitespace (spaces, tabs, newlines) is allowed between the procedure name and the opening `(`.

## `OUT` / `INOUT` Parameters

```sql
CALL total_orders(@customer_id, @total);   -- @total is OUT or INOUT
SELECT @total;                             -- read the value back
```

- Values passed for `OUT` and `INOUT` parameters must be **user-defined variables** (`@var`) at the top SQL level — not literals or expressions. Inside another stored program, a local variable or the enclosing routine's own parameter can also be used.
- If the procedure body never assigns a value to an `OUT` parameter, the bound variable is set to `NULL` (its prior value is lost) when `CALL` returns.
- `CALL` supports placeholders (`?`) for `OUT`/`INOUT` parameters in prepared statements, not just `IN` parameters.

## Result Sets

A stored procedure can return result sets directly to the client — each top-level `SELECT` executed in the procedure body produces one:

```sql
CALL report_summary();   -- may emit one SELECT's worth of rows, or several
```

- Whether the client can receive more than one result set from a single `CALL` depends on the client capability flag `CLIENT_MULTI_RESULTS`. Modern client libraries (including the MariaDB Connectors) set this by default; without it, only a single result set may come back, and prepared statements cannot be used inside the called procedure.
- Consuming multiple result sets is a client-API concern (a "more results" loop in the connector) rather than `CALL` syntax.
- After the procedure returns, `ROW_COUNT()` reports the affected-rows count of the **last** statement executed inside the routine.

## Privileges

Calling a procedure requires the **`EXECUTE`** privilege on that routine (granted directly, via a routine-level `GRANT EXECUTE ON PROCEDURE`, or implied by ownership/broader grants). This is independent of whatever table privileges the procedure's body statements need — those are evaluated against the definer or invoker per the routine's `SQL SECURITY` clause.

## Prepared Statements

```sql
PREPARE stmt FROM 'CALL sp_name(?, ?, ?)';
SET @a = 1, @out_val = NULL;
EXECUTE stmt USING @a, @out_val, @out_val;
```

`CALL` can be executed as a prepared statement, with placeholders for `IN`, `OUT`, and `INOUT` parameters alike.

## Recursion

Stored procedures may call themselves (or each other, mutually) recursively. This is governed by the session variable `max_sp_recursion_depth`:

- **Default: `0`** — recursion is disabled.
- Range: `0`–`255`.
- Set it before the call: `SET max_sp_recursion_depth = 10;`

## See Also

- **`mariadb-create-procedure`** — defining the stored procedure that `CALL` invokes, including parameter modes (`IN`/`OUT`/`INOUT`) and `SQL SECURITY`
- Canonical reference on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/stored-routine-statements/call>
