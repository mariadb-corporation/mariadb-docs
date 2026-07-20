---
name: mariadb-create-procedure
description: "MariaDB-specific syntax and behavior for CREATE PROCEDURE — OR REPLACE / IF NOT EXISTS (mutually exclusive), DEFINER and SQL SECURITY DEFINER/INVOKER, parameter modes IN/OUT/INOUT (plus IN OUT and NOCOPY in Oracle mode only), parameter DEFAULT values (11.8+), the CONTAINS SQL/NO SQL/READS SQL DATA/MODIFIES SQL DATA characteristics (advisory, default CONTAINS SQL), DETERMINISTIC being a no-op on procedures, required CREATE ROUTINE privilege plus automatic ALTER ROUTINE/EXECUTE grants, and the client-side DELIMITER convention. Use when writing, generating, or reviewing CREATE PROCEDURE statements or stored-procedure bodies that target MariaDB."
---

# CREATE PROCEDURE in MariaDB

*Last updated: 2026-07-20*

This skill covers the **delta between what an LLM tends to write for a "stored procedure" and MariaDB's actual `CREATE PROCEDURE`**. It assumes the agent already knows the general concept (parameters, a procedural body, `CALL` to invoke). Everything below documents MariaDB-specific clauses, privilege behavior, parameter semantics, and the most common LLM traps.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Anything available in current LTS branches (10.6, 10.11, 11.4, 11.8) is shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `CREATE OR REPLACE PROCEDURE ... IF NOT EXISTS` | **Illegal combination** — `OR REPLACE` and `IF NOT EXISTS` cannot be used together (`ER_WRONG_USAGE`). Pick one: `OR REPLACE` to unconditionally drop-and-recreate, or `IF NOT EXISTS` to no-op with a warning if the procedure already exists |
| `DETERMINISTIC` / `NOT DETERMINISTIC` on a procedure, expecting it to affect execution | These characteristics are **parsed but ignored for procedures** — they apply only to stored functions. Don't rely on them for procedure caching/replication decisions |
| Assuming `CONTAINS SQL`/`READS SQL DATA`/etc. is enforced | All four data-access characteristics are **purely advisory/informational** — MariaDB does not verify the body matches the declared clause. Default if omitted is `CONTAINS SQL` |
| A single semicolon-terminated body pasted straight into a script/ORM call | The body's internal `;` terminators need a **client-side** `DELIMITER` change (e.g. `DELIMITER //`) when run through the `mariadb` CLI — this is a client convenience, not server syntax. Sending the CREATE statement over the wire via an API/driver (prepared statement, one string) needs no delimiter juggling at all |
| `IN OUT param_name TYPE` in default (non-Oracle) SQL syntax | `IN OUT` (two words) is valid **only under `sql_mode=ORACLE`**. In default MariaDB mode, only `IN`, `OUT`, and `INOUT` (one word) are valid parameter modes, and `IN` is the default when a mode is omitted |
| `OUT`/`INOUT` params without a session variable at call time | The caller must pass a **user-defined variable** (`@var`) — or, from inside another routine, a local variable/parameter — for each `OUT`/`INOUT` argument, so the returned value has somewhere to land |
| Omitting `DEFINER`, assuming it's NULL/anonymous | Defaults to **`CURRENT_USER`** at creation time (the account that ran `CREATE PROCEDURE`), not left unset. Setting a *different* `DEFINER` requires the `SET USER` (superuser-class) privilege |
| Expecting the procedure creator to always be able to run/alter it | `EXECUTE` and `ALTER ROUTINE` are **auto-granted to the creator** at creation time — but only while `automatic_sp_privileges` (default `1`) is enabled |
| Using `ALTER PROCEDURE` to change parameters or the body | `ALTER PROCEDURE` can only touch **characteristics** (`SQL SECURITY`, data-access clause, `COMMENT`) — never the parameter list or body. To change those, use `CREATE OR REPLACE PROCEDURE` (preserves existing grants) or drop-and-recreate |

## Syntax

```sql
CREATE
    [OR REPLACE]
    [DEFINER = { user | CURRENT_USER | role | CURRENT_ROLE }]
    PROCEDURE [IF NOT EXISTS] sp_name ([proc_parameter[,...]])
    [characteristic ...] routine_body

proc_parameter:
    [ OUT | INOUT | IN OUT ] param_name type |
    [ IN ] param_name type [DEFAULT value_or_expression]

characteristic:
    LANGUAGE SQL
  | [NOT] DETERMINISTIC
  | { CONTAINS SQL | NO SQL | READS SQL DATA | MODIFIES SQL DATA }
  | SQL SECURITY { DEFINER | INVOKER }
  | COMMENT 'string'
```

`OR REPLACE` and `IF NOT EXISTS` are mutually exclusive. `IN OUT` (as two words) and the `NOCOPY` parameter hint are Oracle-mode-only syntax; default-mode MariaDB uses `INOUT` (one word). Parameter `DEFAULT` values/expressions are available on any parameter regardless of mode *(since 11.8)*.

## Parameter Modes

- **`IN`** (default when omitted) — passes a value in; the caller never sees changes made inside the procedure.
- **`OUT`** — starts as `NULL` inside the procedure; its final value is visible to the caller. Must be called with a variable (`@v`, or a routine-local variable/parameter when called from another routine).
- **`INOUT`** — caller-supplied initial value, modifiable, changes visible on return.

```sql
CREATE PROCEDURE simpleproc (OUT param1 INT, IN threshold INT DEFAULT 100)
BEGIN
  SELECT COUNT(*) INTO param1 FROM t WHERE val > threshold;
END;
```

## Characteristics

- **`LANGUAGE SQL`** — the only language currently supported; documentation-only clause.
- **`DETERMINISTIC` / `NOT DETERMINISTIC`** — no effect on procedures (functions only). Default `NOT DETERMINISTIC`.
- **Data-access clauses** (`CONTAINS SQL` / `NO SQL` / `READS SQL DATA` / `MODIFIES SQL DATA`) — advisory only, never validated against the body. Default `CONTAINS SQL` if none given.
- **`SQL SECURITY { DEFINER | INVOKER }`** — controls whose privileges are checked at call time. Default **`DEFINER`**. With `DEFINER`, the routine runs with the definer account's privileges regardless of who calls it; with `INVOKER`, the caller's own privileges are checked.
- **`COMMENT 'string'`** — free-text, shown in `SHOW PROCEDURE STATUS` / `INFORMATION_SCHEMA.ROUTINES`.

## Privileges

- Creating a procedure requires **`CREATE ROUTINE`**.
- Specifying a `DEFINER` other than the calling account requires the `SET USER` privilege.
- The creator is auto-granted **`ALTER ROUTINE`** and **`EXECUTE`** on the new routine (governed by `automatic_sp_privileges`, default on).
- `CREATE OR REPLACE PROCEDURE` preserves existing routine-specific privileges; a plain `DROP PROCEDURE` + `CREATE PROCEDURE` does not.
- `DROP PROCEDURE`/`ALTER PROCEDURE` require `ALTER ROUTINE` on the routine.

## Body and Invocation Notes

- `routine_body` is any valid SQL procedure statement — a single statement, or a `BEGIN ... END` compound block with declarations, handlers, loops, etc.
- Unlike stored functions, **procedures may contain transaction-control statements** (`COMMIT`, `START TRANSACTION`, ...) and DDL (`CREATE`, `DROP`, ...).
- Invoke with `CALL sp_name(...)` — never `SELECT`.
- If the procedure name collides with a built-in SQL function name, a space is required between the name and `(` both when defining and calling it.
- The procedure's effective `sql_mode` is captured **at creation time** and used on every execution afterward, independent of the session's `sql_mode` when it's called.
- Oracle-mode PL/SQL-style procedure bodies are supported under `sql_mode=ORACLE` (a subset of PL/SQL syntax, including `IN OUT` and `NOCOPY` parameters) — a distinct body-syntax mode, not a separate statement.
- `DELIMITER` (e.g. `DELIMITER //`) is a **client convenience** (`mariadb` CLI only) for feeding a multi-statement body containing `;` as one block — it is not server syntax and irrelevant when the `CREATE PROCEDURE` text is sent as a single prepared statement over the protocol.

## See Also

- **`mariadb-create-function`** — stored functions: `DETERMINISTIC` actually matters, single `RETURNS` value, no transaction/DDL statements
- **`mariadb-create-trigger`** — trigger-specific `FOR EACH ROW`, timing, and `OLD`/`NEW` row access
- **`mariadb-call`** — invoking procedures, passing `OUT`/`INOUT` arguments
- Canonical references on `mariadb.com/docs` (consult only for edge cases not covered here):
  - <https://mariadb.com/docs/server/server-usage/stored-routines/stored-procedures/create-procedure>
  - <https://mariadb.com/docs/server/server-usage/stored-routines/stored-procedures/stored-procedure-overview>
  - <https://mariadb.com/docs/server/server-usage/stored-routines/stored-procedures/alter-procedure>
  - <https://mariadb.com/docs/server/server-usage/stored-routines/stored-functions/stored-routine-privileges>
