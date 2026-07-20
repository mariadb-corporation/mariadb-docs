---
name: mariadb-prepare
description: "MariaDB-specific behavior of server-side prepared statements — PREPARE / EXECUTE / DEALLOCATE PREPARE and EXECUTE IMMEDIATE — covers the broad preparable-statement allow-list, EXECUTE..USING accepting arbitrary expressions (not just user variables), the stored-function/trigger ban on dynamic SQL, session-local statement lifetime, and EXECUTE IMMEDIATE's DEFAULT/IGNORE bind parameters. Use when writing, generating, or reviewing PREPARE/EXECUTE statements that target MariaDB."
---

# PREPARE / EXECUTE in MariaDB

*Last updated: 2026-07-20*

These are SQL-level ("text protocol") prepared statements: you PREPARE a statement from a string or expression, then EXECUTE it by name. This is a different mechanism from the binary-protocol prepared statements (`COM_STMT_PREPARE` / `COM_STMT_EXECUTE`) that connectors and drivers issue behind the scenes for parameterized queries — the SQL forms below are statements you write and run yourself, typically inside dynamic SQL or stored procedures.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `EXECUTE stmt USING 5` is invalid — "USING only accepts user variables" | In current MariaDB, `EXECUTE ... USING` binds any expression, not just `@variables` — literals, arithmetic, function calls all work. The user-variable-only restriction only applied before 10.2.3, well before the 10.6 baseline. |
| Trying to bind an identifier or table name with `?`: `PREPARE s FROM 'SELECT * FROM ?'` | `?` (or Oracle-mode `:1`, `:name`) can only stand in for a data value, never identifiers/keywords. To parameterize table/column names, concatenate them into the `PREPARE`/`EXECUTE IMMEDIATE` source string itself (the standard "dynamic SQL" pattern). |
| Using `PREPARE`/`EXECUTE`/`EXECUTE IMMEDIATE` inside a stored function or trigger | Not allowed there — MariaDB raises `Dynamic SQL is not allowed in stored function or trigger`. These statements only work inside stored **procedures**. |
| Assuming most statement types can't be prepared (SELECT/DML only) | The allow-list is broad: essentially every SQL statement — DDL, `GRANT`/`REVOKE`, replication and admin commands, `SHOW` variants, compound statements — can be `PREPARE`d, except `PREPARE`, `EXECUTE`, and `DEALLOCATE`/`DROP PREPARE` themselves. |
| Assuming a prepared statement is visible to other connections or survives a session | Prepared statements are strictly session-local (held in a per-thread statement map); they vanish when the session ends or on explicit `DEALLOCATE`. |
| Re-`PREPARE`ing an existing name and expecting an "already exists" error | Re-issuing `PREPARE` with a name already in use implicitly deallocates the old statement first. If the new statement fails to parse, the old one is gone too — there is no rollback to the previous definition. |
| `EXECUTE IMMEDIATE 'sql' USING <subquery-or-function-call>` | Neither the prepare source nor a `USING` parameter can be a subquery or a stored function call directly — bind the result into a user or SP variable first and pass that. |
| Treating `max_prepared_stmt_count` as a per-connection limit | It's a single **global** counter (default 16382) shared across every session on the server — one connection's unclosed statements can starve another's. |
| Only spelling it `DEALLOCATE PREPARE` | `DROP PREPARE` is an exact synonym for `DEALLOCATE PREPARE`. |

## Syntax

```sql
PREPARE stmt_name FROM preparable_stmt;    -- preparable_stmt: a string literal or a user variable
EXECUTE stmt_name [USING @var [, @var] ...];
DEALLOCATE PREPARE stmt_name;   -- DROP PREPARE is a synonym
EXECUTE IMMEDIATE preparable_stmt [USING ...];
```

- `preparable_stmt` / `statement` can be any expression that evaluates to the SQL text — a string literal, a user variable, or a `CONCAT(...)` expression — but it cannot itself be a subquery or a stored function call.
- `stmt_name` is not case-sensitive.
- `USING` arguments are matched positionally to the `?` placeholders in the prepared text; the count must match exactly.
- `EXECUTE IMMEDIATE` additionally accepts `IGNORE` and `DEFAULT` as bind values in its `USING` list (see below).

## Placeholders and the USING Clause

- `?` is a positional data-value placeholder. In Oracle mode (`sql_mode=ORACLE`) MariaDB additionally accepts `:1`, `:2`, ... (or named `:label`) instead of `?`.
- A placeholder can only appear where an expression is legal — never for identifiers, keywords, or clause structure.
- `EXECUTE stmt USING expr [, expr] ...` binds each `USING` expression to the corresponding `?` in source order. In current MariaDB, those expressions can be user variables, literals, or arbitrary expressions — not just `@var_name`.
- Because identifiers can't be bound as parameters, dynamic table/column names are handled by building the identifier into the SQL text before preparing it (classic *dynamic SQL*):

```sql
CREATE PROCEDURE test.count_rows(IN tab_name VARCHAR(64))
BEGIN
  SET @sql = CONCAT('SELECT COUNT(*) FROM ', tab_name);
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END;
```

## Session Scope and Lifetime

- Prepared statements live in a per-session (thread-local) map. Other connections cannot see or execute them, and they disappear when the session ends.
- `PREPARE`ing a name that's already in use implicitly deallocates the previous statement of that name before preparing the new one.
- A statement `PREPARE`d inside a stored procedure is **not** automatically deallocated when the procedure returns — it stays live for the rest of the session. Calling such a procedure repeatedly (e.g., in a loop) without an explicit `DEALLOCATE PREPARE` accumulates statements and can hit `max_prepared_stmt_count`.
- `max_prepared_stmt_count` (global, default `16382`) caps the total number of prepared statements open across *all* sessions on the server at once; setting it to `0` disables prepared statements entirely. Exceeding it raises `ERROR 1461: Can't create more than max_prepared_stmt_count statements`.
- A prepared statement can reference user-defined `@variables`, but not stored-procedure local variables or IN/OUT parameters directly — pass those in via `USING` or via a session variable.
- MariaDB may transparently re-prepare a statement (up to 3 attempts) if the table/view metadata it depends on changed between `PREPARE` and `EXECUTE` (for example, a DDL statement ran on another connection in between) — this is invisible to the caller unless the retry limit is exhausted.

## What Can Be Prepared

- Essentially every SQL statement can be `PREPARE`d and `EXECUTE`d — `SELECT`, DML, DDL (`CREATE`/`ALTER`/`DROP TABLE`, indexes, users, views, databases), `GRANT`/`REVOKE`, replication and administrative commands, most `SHOW` variants, `CALL`, and compound statements — **except** `PREPARE`, `EXECUTE`, and `DEALLOCATE`/`DROP PREPARE` themselves.
- The prepare source cannot contain a subquery or a stored function call — MariaDB rejects it with `ER_SUBQUERIES_NOT_SUPPORTED` ("... does not support subqueries or stored functions") at parse time.
- A statement that can't be directly prepared (e.g., `SIGNAL`) can still run indirectly: if a stored procedure body contains it, preparing and executing `CALL that_procedure()` works fine.

## EXECUTE IMMEDIATE

`EXECUTE IMMEDIATE` is a MariaDB extension that combines `PREPARE` + `EXECUTE` + `DEALLOCATE PREPARE` into a single statement — no name is assigned and nothing is left behind afterward:

```sql
EXECUTE IMMEDIATE 'SELECT 1';
-- shorthand for:
PREPARE stmt FROM 'SELECT 1';
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

- It supports complex expressions as the prepare source and as bind parameters, e.g. `EXECUTE IMMEDIATE CONCAT('SELECT COUNT(*) FROM ', 't1', ' WHERE a=?') USING 5+5;`.
- Same restriction as `PREPARE`: the source and `USING` parameters cannot be subqueries or stored function calls directly — assign to a variable first as a workaround.
- `USING` parameters can additionally be the pseudo-values `DEFAULT` (bind as if the column's `DEFAULT` were used) or `IGNORE` (bind as if the value were omitted, subject to strict-mode handling), on top of ordinary expressions.
- User and stored-procedure variables can be used as `OUT` parameters, e.g. `EXECUTE IMMEDIATE 'CALL p1(?)' USING @a;` writes the procedure's `OUT` value back into `@a`.
- Allowed inside stored procedures, not inside stored functions or triggers (same rule as `PREPARE`/`EXECUTE`).
- It increments `Com_execute_immediate` plus `Com_stmt_prepare`, `Com_stmt_execute`, and `Com_stmt_close`, but **not** `Com_execute_sql` — that counter is reserved for the explicit `PREPARE`..`EXECUTE` path. Useful for telling the two code paths apart in `SHOW STATUS`.

## Prepared Statements Inside Stored Routines

- `PREPARE`, `EXECUTE`, `EXECUTE IMMEDIATE`, and `DEALLOCATE PREPARE` are all allowed inside stored **procedures**.
- None of them are allowed inside stored **functions** or **triggers** — MariaDB raises `Dynamic SQL is not allowed in stored function or trigger` for both.
- `PREPARE` itself fails fast on a syntax error, so procedures sometimes use it purely as a validity check on caller-supplied SQL text (wrapped in a handler, then immediately `DEALLOCATE`d without ever `EXECUTE`ing).

## Examples

```sql
-- Basic PREPARE / EXECUTE with a placeholder
CREATE TABLE t1 (a INT, b CHAR(10));
INSERT INTO t1 VALUES (1,'one'), (2,'two'), (3,'three');

PREPARE test FROM 'SELECT * FROM t1 WHERE a=?';
SET @param = 2;
EXECUTE test USING @param;
DEALLOCATE PREPARE test;

-- Dynamic table name (identifiers must be concatenated, not bound)
CREATE PROCEDURE test.stmt_test(IN tab_name VARCHAR(64))
BEGIN
  SET @sql = CONCAT('SELECT COUNT(*) FROM ', tab_name);
  PREPARE stmt FROM @sql;
  EXECUTE stmt;
  DEALLOCATE PREPARE stmt;
END;

-- EXECUTE IMMEDIATE with a DEFAULT bind parameter
CREATE OR REPLACE TABLE t2 (a INT DEFAULT 10);
EXECUTE IMMEDIATE 'INSERT INTO t2 VALUES (?)' USING DEFAULT;

-- EXECUTE IMMEDIATE with an OUT parameter
DELIMITER $$
CREATE OR REPLACE PROCEDURE p1(OUT a INT)
BEGIN
  SET a := 10;
END;
$$
DELIMITER ;
SET @a = 2;
EXECUTE IMMEDIATE 'CALL p1(?)' USING @a;
SELECT @a;   -- 10
```

## See Also

- **`mariadb-create-procedure`** — the routine context where dynamic SQL (`PREPARE`/`EXECUTE`) is allowed; it is banned in functions and triggers.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/prepared-statements/prepare-statement>
  - <https://mariadb.com/docs/server/reference/sql-statements/prepared-statements/execute-statement>
  - <https://mariadb.com/docs/server/reference/sql-statements/prepared-statements/deallocate-drop-prepare>
  - <https://mariadb.com/docs/server/reference/sql-statements/prepared-statements/execute-immediate>
