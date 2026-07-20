---
name: mariadb-information-functions
description: "MariaDB information functions — session and server metadata: LAST_INSERT_ID, ROW_COUNT, FOUND_ROWS, DATABASE/SCHEMA, USER/CURRENT_USER/SESSION_USER/SYSTEM_USER, CURRENT_ROLE, VERSION, CONNECTION_ID, CHARSET, COLLATION, COERCIBILITY, BENCHMARK, DEFAULT, LAST_VALUE, ROWNUM, BINLOG_GTID_POS, DECODE_HISTOGRAM. Use when writing SQL that reads auto-increment IDs, affected/found row counts, the current database or authenticated user, the server version, or connection/session metadata in MariaDB."
---

# MariaDB Information Functions

*Last updated: 2026-07-20*

Catalog of every built-in information function in MariaDB, with signature and
a one-line semantic summary per entry. For a function not listed here, fall
back to the canonical reference at
<https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/information-functions>.

> **Default context:** Assume MariaDB **11.8 LTS** unless the user specifies
> another version. Functions with a `*(since X.Y)*` annotation are only
> available from that version onward; everything else is in every current LTS
> branch (10.6, 10.11, 11.4, 11.8).

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
| --- | --- |
| `LAST_INSERT_ID()` after a multi-row `INSERT` and expects the ID of the *last* row inserted | It returns the **first** automatically-generated `AUTO_INCREMENT` value of that statement, not the last. Subsequent rows' IDs are implied by increment, not returned |
| Worrying that `LAST_INSERT_ID()` is contaminated by other sessions inserting concurrently | It's **per-connection** (server-side, tied to the session), not global — safe under concurrency. Read it immediately after the `INSERT` on the same connection; a stored function or trigger that changes it restores the prior value on exit, so callers outside it never see the trigger's value |
| `ROW_COUNT()` returning `0` after a `SELECT` | It returns **-1** for any statement that returns a result set (`SELECT`, `SHOW`, `DESC`, `HELP`), even an empty one, and after a failed/rolled-back statement. `0` means a DDL or no-result statement genuinely affected nothing |
| Assuming `ROW_COUNT()` after `UPDATE` always means "rows actually changed" | It's the number of rows *changed* by default, but becomes the number of rows *matched* by the `WHERE` clause when the client connects with `CLIENT_FOUND_ROWS` — the two can differ |
| Reaching for `SQL_CALC_FOUND_ROWS` + `FOUND_ROWS()` to get a total count alongside a `LIMIT`ed page of results | Legacy pattern, discouraged for new code — it disables some query optimizations. Prefer a separate `SELECT COUNT(*) ...` with the same `WHERE` clause (see `mariadb-select`) |
| `DATABASE()` returning an empty string `''` when no database is selected | It returns `NULL`, not `''` — test with `IS NULL` |
| Parsing `VERSION()` as a bare version number | The string embeds a `-MariaDB` suffix (e.g. `11.8.1-MariaDB`) plus optional `-log`/`-debug`/`-embedded`/`-valgrind` suffixes — always account for it when detecting the fork or parsing the numeric part |
| Treating `USER()` and `CURRENT_USER()` as interchangeable | `USER()` is the user/host the client presented at connection; `CURRENT_USER()` is the account actually used to check privileges (e.g. the `DEFINER` inside a stored routine with `SQL SECURITY DEFINER`). They differ whenever a role, proxy user, or `DEFINER` context is involved — a real security-relevant distinction |
| Assuming `SESSION_USER()` is just another alias for `USER()` | That was true only before 11.7. From 11.7 onward `SESSION_USER()` instead captures `CURRENT_USER()` as of session start and stays fixed inside stored routines/views (unlike `CURRENT_USER()`, which can change under `DEFINER`). `SYSTEM_USER()` remains a plain synonym for `USER()` in both eras — don't conflate the two `*_USER()` synonyms |

## Functions

<!-- BEGIN GENERATED -->
<!-- Extracted from server/reference/sql-functions/secondary-functions/information-functions -->
<!-- 21 functions, 1 pages skipped on extraction failure -->

### BENCHMARK
`BENCHMARK(count,expr)`  
The BENCHMARK() function executes the expression `expr` repeatedly `count` times.

### BINLOG_GTID_POS
`BINLOG_GTID_POS(binlog_filename,binlog_offset)`  
The BINLOG_GTID_POS() function takes as input an old-style binary log position in the form of a file name and a file offset.

### CHARSET
`CHARSET(str)`  
Returns the character set of the string argument.

### COERCIBILITY
`COERCIBILITY(str)`  
Returns the collation coercibility value of the string argument.

### COLLATION
`COLLATION(str)`  
Returns the collation of the string argument.

### CONNECTION_ID
`CONNECTION_ID()`  
Returns the connection ID for the connection.

### CURRENT_ROLE
`CURRENT_ROLE, CURRENT_ROLE()`  
Returns the current role name.

### CURRENT_USER
`CURRENT_USER, CURRENT_USER()`  
Returns the user name and host name combination for the MariaDB account that the server used to authenticate the current client.

### DATABASE
`DATABASE()`  
Returns the default (current) database name as a string in the utf8 character set.

### DECODE_HISTOGRAM
`DECODE_HISTOGRAM(hist_type,histogram)`  
Returns a string of comma separated numeric values corresponding to a probability distribution represented by the histogram of type `hist_type` (`SINGLE_PREC_HB` or `DOUBLE_PREC_HB`).

### DEFAULT
`DEFAULT(col_name)`  
Returns the default value for a table column.

### FOUND_ROWS
`FOUND_ROWS()`  
A SELECT statement may include a LIMIT clause to restrict the number of rows the server returns to the client.

### LAST_INSERT_ID
`LAST_INSERT_ID(), LAST_INSERT_ID(expr)`  
`LAST_INSERT_ID()` (no arguments) returns the first automatically generated value successfully inserted for an AUTO_INCREMENT column as a result of the most recently executed `INSERT`\ statement.

### LAST_VALUE
`LAST_VALUE(expr,[expr,...])`  
`LAST_VALUE()` evaluates all expressions and returns the last.

### ROWNUM
`ROWNUM()`  
`ROWNUM()` returns the current number of accepted rows in the current context.

### ROW_COUNT
`ROW_COUNT()`  
`ROW_COUNT()` returns the number of rows updated, inserted or deleted by the preceding statement.

### SCHEMA
`SCHEMA()`  
This function is a synonym for DATABASE().

### SESSION_USER
`SESSION_USER()`  
{% tabs %} {% tab title="Current" %} Shows the value of CURRENT_USER() when the session was created, that is, it shows a `user@host` pair from the mysql.global_priv table, like `CURRENT_USER()`, but unlike `CURRENT_USER()` it will not change inside stored routines and views.

### SYSTEM_USER
`SYSTEM_USER()`  
`SYSTEM_USER()` is a synonym for USER().

### USER
`USER()`  
Returns the current MariaDB user name and host name, given when authenticating to MariaDB, as a string in the utf8 character set.

### VERSION
`VERSION()`  
Returns a string that indicates the MariaDB server version.
<!-- END GENERATED -->

## See Also

- **`mariadb-select`** — why `SQL_CALC_FOUND_ROWS`/`FOUND_ROWS()` is discouraged in favor of a separate `COUNT(*)` query
- **`mariadb-create-table`** — `AUTO_INCREMENT` columns (source of `LAST_INSERT_ID()`) and column `DEFAULT` clauses (source of `DEFAULT(col)`)
- **`mariadb-window-functions`** — `LAST_VALUE(expr) OVER (...)` as a window function, distinct from its non-window scalar form
- Canonical reference on `mariadb.com/docs`: <https://mariadb.com/docs/server/reference/sql-functions/secondary-functions/information-functions>
