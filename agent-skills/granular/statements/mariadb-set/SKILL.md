---
name: mariadb-set
description: "MariaDB-specific syntax and behavior for SET — GLOBAL/SESSION/LOCAL scope rules and their session-isolation semantics, the SET STATEMENT ... FOR extension (and its fixed list of 13 variables it cannot touch), `=`/`:=` equivalence for user variables inside SET (but not outside it), var = DEFAULT restore semantics, the SUPER privilege gate on SET GLOBAL, and the absence of SET PERSIST (MariaDB persists via config file, not SQL). Use when writing, generating, or reviewing SET statements (system/session/user variables, options, and SET STATEMENT ... FOR) that target MariaDB."
---

# SET in MariaDB

*Last updated: 2026-07-20*

This skill covers the delta between generic "assign a variable" SQL and MariaDB's `SET` — its scope keywords, the `SET STATEMENT ... FOR` per-query extension, and a persistence model that has no `SET PERSIST` equivalent.

> **Default context:** Assume MariaDB **11.8 LTS** (GA May 2025) unless the user states another version. Features available across current LTS branches (10.6, 10.11, 11.4, 11.8) are shown without a "since" annotation; only newer-than-10.6 features carry one.

## What LLMs Often Miss

| If the agent writes / suggests… | …prefer the MariaDB form |
|---|---|
| `SET PERSIST var = value;` (or `SET PERSIST_ONLY`) to make a global setting survive a restart | **Does not exist in MariaDB** — there is no `PERSIST` keyword in the grammar at all. To persist a setting, write it to a config file (e.g. `/etc/mysql/mariadb.conf.d/`) or run `SET GLOBAL var=value` and separately update the config file for the next restart |
| `GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'user'` before letting an app run `SET GLOBAL ...` | That privilege identifier doesn't exist in MariaDB. `SET GLOBAL` is gated by the **`SUPER`** privilege (some individual global variables — e.g. those touching binlogging or replication — instead check a narrower admin privilege such as `BINLOG ADMIN` or `REPLICATION MASTER ADMIN`, but the default check is `SUPER`) |
| `SET GLOBAL max_connections=500;` then expecting the *current* session to see the new value immediately | A global change affects only **new** connections — not the session that issued it, and not any other already-open session. Reconnect (or read `@@global.var` explicitly) to see it take effect |
| `SET x := 5;` inside a `SELECT` or other expression to assign a user variable | `:=` is required for user-variable assignment **outside** `SET` (e.g. `SELECT @x := 5`). Inside `SET`, both `SET @x = 5` and `SET @x := 5` work — `SET` is the one place plain `=` is accepted for a user variable |
| A per-query tweak like `SET wait_timeout=5; SELECT ...; SET wait_timeout=@@global.wait_timeout;` to scope a setting to one statement | Use the MariaDB extension **`SET STATEMENT wait_timeout=5 FOR SELECT ...`** instead — except `wait_timeout` is one of a fixed list of variables `SET STATEMENT` cannot set (see below); for those, the manual save/restore pattern is still required |
| `SET STATEMENT sql_mode='ANSI_QUOTES' FOR SELECT "col" FROM t;` and expecting `"col"` to be treated as an identifier | The whole statement is **parsed before** `SET STATEMENT` takes effect, so variables that affect parsing (charset settings, `sql_mode=ANSI_QUOTES`, etc.) don't retroactively change how the `FOR` statement itself was parsed |
| `SET sql_mode = NULL;` or omitting a reset path entirely | Use `SET sql_mode = DEFAULT` (session → resets to the current global value) or `SET GLOBAL sql_mode = DEFAULT` (global → resets to the compiled-in server default) |
| Writing `SET SESSION` when a variable turns out to be global-only, or vice versa | If a variable has a session value, omitting `GLOBAL`/`SESSION` behaves as `SESSION`; if it's global-only, omitting them applies to the global value. Setting the wrong scope explicitly is a hard error (`ERROR 1229` — variable is GLOBAL, use `SET GLOBAL`; `ERROR 1228` — variable is SESSION, can't use `SET GLOBAL`), not a silent no-op |
| `SET LOCAL var = value;` assuming it differs from `SET SESSION` | `LOCAL` is a plain synonym for `SESSION` — identical parse action, no behavioral difference, use either |

## Syntax

```sql
SET variable_assignment [, variable_assignment] ...

variable_assignment:
      user_var_name (= | :=) expr
    | [GLOBAL | SESSION | LOCAL] system_var_name = expr
    | [@@global. | @@session. | @@local. | @@] system_var_name = expr
    | system_var_name = DEFAULT
```

- Multiple assignments in one statement are comma-separated and can mix scopes and variable kinds freely: `SET @x = 1, GLOBAL max_connections = 500, @@session.sql_mode = DEFAULT;`
- `GLOBAL`, `SESSION`, and `LOCAL` are the keyword forms; `@@global.`, `@@session.`, `@@local.`, and bare `@@` are the equivalent variable-reference forms — `SET @@GLOBAL.max_connections = 500` and `SET GLOBAL max_connections = 500` are fully equivalent (same code path).
- Omitting a scope keyword defaults to `SESSION` if the variable has a session value, otherwise to `GLOBAL`.
- `SET @x = expr` and `SET @x := expr` are both accepted for user variables inside `SET` — but only `:=` is valid for a user-variable assignment anywhere else (e.g. inside a `SELECT` expression).

## Variable Scopes — GLOBAL / SESSION / LOCAL

- **`GLOBAL`** changes the server-wide default. It affects **new** sessions only — not the session that ran the `SET GLOBAL`, and not any session already connected.
- **`SESSION`** (and its synonym **`LOCAL`**) changes the current connection only.
- Setting a variable with the wrong scope is a hard error, not a fallback:

```sql
SET innodb_sync_spin_loops = 60;
-- ERROR 1229 (HY000): Variable 'innodb_sync_spin_loops' is a GLOBAL variable
--   and should be set with SET GLOBAL

SET GLOBAL skip_parallel_replication = ON;
-- ERROR 1228 (HY000): Variable 'skip_parallel_replication' is a SESSION variable
--   and can't be used with SET GLOBAL
```

- Setting `GLOBAL` requires the **`SUPER`** privilege by default (a handful of individual global variables instead gate on a narrower privilege, such as replication/binlog admin variants — check the specific variable if `SUPER` alone doesn't work).
- `SET` does **not** persist a global change across a server restart. There is no `SET PERSIST` in MariaDB — to survive a restart, also update the value in a configuration file.

## `SET var = DEFAULT`

```sql
SET sql_mode = DEFAULT;         -- session var -> resets to the current GLOBAL value
SET GLOBAL sql_mode = DEFAULT;  -- global var  -> resets to the compiled-in server default
```

`SET session_var = @@GLOBAL.session_var` achieves the same effect as `SET session_var = DEFAULT` by explicitly copying the current global value.

## SET STATEMENT ... FOR (MariaDB Extension)

```sql
SET STATEMENT var1 = value1 [, var2 = value2, ...] FOR statement;
```

Sets one or more system variables for the duration of a single statement, then automatically restores the prior session value — roughly:

```sql
SET @save_value = @@var1;
SET SESSION var1 = value1;
statement;
SET SESSION var1 = @save_value;
```

Notes and traps:

- `value` must be a constant literal — it cannot reference a table or a stored routine (subqueries/table references in the `SET STATEMENT` clause itself are rejected).
- The whole statement is parsed **before** `SET STATEMENT` variables take effect, so anything that influences parsing (client/connection charset variables, `sql_mode=ANSI_QUOTES`, etc.) won't retroactively change how the `FOR` statement was parsed.
- It works with prepared statements — `SET STATEMENT var=val FOR PREPARE ...` and `SET STATEMENT var=val FOR EXECUTE stmt_name` are both valid targets.
- Setting a `SESSION` variable *inside* the `FOR` statement (e.g. `SET STATEMENT x=1 FOR SET SESSION x=2`) is pointless: the inner `SET SESSION` takes effect, then gets reverted to the pre-`SET STATEMENT` value once the outer statement finishes.
- A fixed set of 13 variables **cannot** be set via `SET STATEMENT` at all (attempting it raises `ER_SET_STATEMENT_NOT_SUPPORTED`) — `autocommit`, `character_set_client`, `character_set_connection`, `character_set_filesystem`, `collation_connection`, `debug_sync`, `interactive_timeout`, `profiling`, `profiling_history_size`, `query_cache_type`, `skip_replication`, `sql_log_off`, `wait_timeout`.

```sql
SET STATEMENT max_statement_time=1000 FOR SELECT ...;
SET STATEMENT optimizer_switch='materialization=off' FOR SELECT ...;
SET STATEMENT join_cache_level=6, optimizer_switch='mrr=on' FOR SELECT ...;
```

## Examples

```sql
-- multiple scopes and kinds in one statement
SET @request_id = UUID(), SESSION sql_mode = 'STRICT_ALL_TABLES', GLOBAL max_connections = 500;

-- inline user-variable assignment inside an expression (needs :=, not =)
SELECT (@a := 1);
SELECT @a;

-- restore a session variable to the server default
SET GLOBAL max_error_count = 256;
SET SESSION max_error_count = DEFAULT;   -- picks up the new global value, 256

-- bound a single query without touching session state
SET STATEMENT max_statement_time=2 FOR SELECT SLEEP(10);
```

Read variable state back with `SHOW VARIABLES` or `INFORMATION_SCHEMA.SYSTEM_VARIABLES`, which exposes `SESSION_VALUE` and `GLOBAL_VALUE` side by side (a `NULL` in either column means the variable doesn't have that scope).

## Related SET Forms (Separate Statements)

These share the `SET` keyword but are documented — and should be reasoned about — separately:

| Statement | Purpose |
|---|---|
| `SET NAMES` / `SET CHARACTER SET` | Set the client/connection/results character set (and collation) in one shot |
| `SET PASSWORD` | Change an account's authentication credential |
| `SET ROLE` / `SET DEFAULT ROLE` | Activate a role for the session, or set a user's default role |
| `SET TRANSACTION` | Set isolation level / access mode for the next transaction or the whole session |
| `SET sql_log_bin` | Session-only toggle for binary logging — no `GLOBAL` form, and it needs the `SUPER` privilege |
| `SET PATH` *(since 12.3)* | Set the schema search path used to resolve unqualified stored-routine/package calls |

## See Also

- **`mariadb-set-transaction`** — isolation level and access mode assignment via `SET TRANSACTION`, a distinct statement from general `SET`.
- **`mariadb-show`** — `SHOW VARIABLES` to read GLOBAL/SESSION variable values back.
- Canonical references on `mariadb.com/docs`:
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/set-commands/set>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/set-commands/set-statement>
  - <https://mariadb.com/docs/server/reference/sql-statements/administrative-sql-statements/set-commands/set-sql_log_bin>
