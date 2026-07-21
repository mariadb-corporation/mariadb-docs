---
name: mariadb-connector-c
description: "MariaDB-specific behavior of MariaDB Connector/C (the `libmariadb` client library implementing the MariaDB/MySQL client-server protocol in C) for application code — that the public API is still `mysql_`-prefixed (`mysql_init`, `mysql_real_connect`, `mysql_query`, `mysql_store_result`, ...) with only a handful of `mariadb_`-prefixed extensions; that `mysql_init()` must run before `mysql_real_connect()`; the buffered-vs-unbuffered split between `mysql_store_result()` and `mysql_use_result()` and the mandatory `mysql_free_result()`; that literal values must go through `mysql_real_escape_string()` when not using prepared statements (the classic SQL-injection trap); the `?`-placeholder prepared-statement API (`mysql_stmt_init`/`mysql_stmt_prepare`, `MYSQL_BIND` arrays, `mysql_stmt_bind_param`/`execute`/`bind_result`/`fetch`); that autocommit is on by default so transactions need `mysql_autocommit(conn,0)` + `mysql_commit()`/`mysql_rollback()`; separate connection-level (`mysql_errno`/`mysql_error`) vs statement-level (`mysql_stmt_errno`/`mysql_stmt_error`) error handling; that options (`mysql_optionsv()`) must be set after `mysql_init()` but before connecting; and that `mysql_real_query()` (with an explicit length) is the binary-safe alternative to `mysql_query()`. Use when writing or reviewing C code that talks to MariaDB via Connector/C (`libmariadb`) or via the connectors built on top of it."
---

# MariaDB Connector/C

*Last updated: 2026-07-21*

MariaDB Connector/C is the LGPL-licensed C client library (`libmariadb`) implementing the MariaDB/MySQL client-server protocol. It is the foundation other MariaDB connectors build on — Connector/Python's C extension, Connector/ODBC, and Connector/C++ all link against it — and it is API-compatible with the classic MySQL C client library, so `mysql.h` and the `mysql_*` function names carry over directly. This skill covers the connector-specific behavior and the traps that bite generated application code; it does not cover installing the library or configuring the server.

> **Default context:** Assume the **3.4** stable release series (GA February 2025; `mariadb_config --cc_version` reports the exact patch, e.g. `3.4.10`) unless the user states otherwise. Connector/C is compatible with all MariaDB and MySQL server versions — its version is independent of the server version it connects to, and behavior below applies across the 3.x line unless annotated.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Calls `mysql_real_connect()` on a raw/stack `MYSQL` struct, or skips init | Call **`mysql_init(NULL)`** first (it allocates and returns a `MYSQL *`, or initializes a struct you pass in) — every other function except `mysql_options()` fails until `mysql_real_connect()` succeeds on that handle |
| Reaches for `mariadb_connect()`, `mariadb_query()`, etc., assuming a `mariadb_`-prefixed API | The public API is still **`mysql_`-prefixed** — `mysql_init`, `mysql_real_connect`, `mysql_query`, `mysql_store_result`, `mysql_close`, and friends — for MySQL C API compatibility. Only a handful of *extension* functions use `mariadb_` (e.g. `mariadb_reconnect()`, `mariadb_get_info()`, `mariadb_stmt_execute_direct()`); `mariadb_connect()` itself is just a macro wrapping `mysql_real_connect()` |
| Builds SQL by concatenating/`sprintf`-ing string values into the query text passed to `mysql_query()` | **SQL-injection trap.** Escape every literal string with **`mysql_real_escape_string(mysql, to, from, length)`** first (the `to` buffer must be `length*2+1` bytes), or — preferably — use the prepared-statement API with `?` placeholders instead of building SQL text at all |
| Calls `mysql_query()`/`mysql_store_result()` and moves straight to the next query | A result-returning statement needs one of **`mysql_store_result()`** (buffered — pulls the whole set into client memory; enables `mysql_num_rows()`/`mysql_data_seek()`) or **`mysql_use_result()`** (unbuffered — row-by-row, blocks the connection until every row is fetched or the result is freed). One of the two **must** be called even for a query with no rows, and the result **must** be released with **`mysql_free_result()`** — otherwise the next query on that connection fails |
| Calls `mysql_num_rows()` / `mysql_data_seek()` on an unbuffered result | Those require **`mysql_store_result()`**; `mysql_use_result()` sets don't support random access or a row count until fully consumed |
| Interpolates `%d`/`%s`-style values into a query string instead of using placeholders | Use the **prepared-statement API** with `?` markers: `mysql_stmt_init()` → `mysql_stmt_prepare(stmt, "...WHERE id=?", length)` → build a `MYSQL_BIND` array → `mysql_stmt_bind_param(stmt, bind)` → `mysql_stmt_execute(stmt)`. For a result set, bind a second `MYSQL_BIND` array with `mysql_stmt_bind_result()` and loop `mysql_stmt_fetch(stmt)` until it returns `MYSQL_NO_DATA` |
| Assumes autocommit is off, or that DML needs an explicit `START TRANSACTION` | **Autocommit is ON by default** — each statement is its own transaction. For multi-statement transactions, disable it once with **`mysql_autocommit(conn, 0)`**, then use **`mysql_commit()`**/**`mysql_rollback()`** (or the `COMMIT`/`ROLLBACK` SQL statements); a new transaction starts automatically after each commit/rollback — no manual `START TRANSACTION` needed |
| Checks one error API for everything, or checks connection errors after a statement-handle call | Connection-level calls (`mysql_real_connect`, `mysql_query`, `mysql_store_result`, ...) report through **`mysql_errno()`**/**`mysql_error()`**; `MYSQL_STMT`-level calls (`mysql_stmt_prepare`, `mysql_stmt_execute`, ...) have their **own** error context: **`mysql_stmt_errno()`**/**`mysql_stmt_error()`**/`mysql_stmt_sqlstate()`. Checking the wrong one silently misses the real error |
| Sets TLS/charset/timeout options after connecting, or via `mysql_real_connect()` args alone | Set options with **`mysql_optionsv()`** (or the older `mysql_options()`) **after `mysql_init()` but before `mysql_real_connect()`** — e.g. `MYSQL_OPT_SSL_CA`, `MYSQL_SET_CHARSET_NAME`, `MYSQL_OPT_CONNECT_TIMEOUT`. Options set post-connect are ignored until the next connect/reconnect |
| Uses `mysql_query()` for statements that may carry binary data or embedded NUL bytes | `mysql_query()` takes a **NUL-terminated** string and is **not** binary-safe. Use **`mysql_real_query(mysql, query, length)`**, which takes an explicit length, for binary-safe execution |
| Reads only the first result after `CALL`ing a stored procedure or a multi-statement query | Stored-procedure calls and multi-statement queries (`MARIADB_OPT_MULTI_STATEMENTS`) can return **multiple result sets** — loop with **`mysql_next_result()`** (or `mysql_stmt_next_result()` for prepared statements), calling `mysql_store_result()`/`mysql_use_result()` + `mysql_free_result()` each time, until no more results remain |
| Passes `-1` as a length to `mysql_real_query()` or `mysql_real_escape_string()`, expecting auto-detection everywhere | Only **`mysql_stmt_prepare()`** treats `length == (unsigned long)-1` as "compute via `strlen()`". The binary-safe functions (`mysql_real_query()`, `mysql_real_escape_string()`) need the **actual** byte length — passing `-1` there is a bug, not a shortcut |
| Calls `mysql_close()` while `MYSQL_STMT`/`MYSQL_RES` handles from that connection are still open | Free every result with `mysql_free_result()` and close every prepared statement with `mysql_stmt_close()` **before** `mysql_close()` on the connection |

## Connect, Prepared Statement, and Transaction

```c
#include <mysql.h>
#include <stdio.h>
#include <string.h>

MYSQL *conn = mysql_init(NULL);
if (!mysql_real_connect(conn, "localhost", "app", "secret",
                         "appdb", 3306, NULL, 0))
{
    fprintf(stderr, "connect failed: %s\n", mysql_error(conn));
    mysql_close(conn);
    return 1;
}

/* Prepared statement with a `?` placeholder */
MYSQL_STMT *stmt = mysql_stmt_init(conn);
const char *sql = "SELECT name, qty FROM t WHERE qty > ?";
mysql_stmt_prepare(stmt, sql, strlen(sql));

int min_qty = 0;
MYSQL_BIND param[1];
memset(param, 0, sizeof(param));
param[0].buffer_type = MYSQL_TYPE_LONG;
param[0].buffer      = &min_qty;
mysql_stmt_bind_param(stmt, param);

mysql_stmt_execute(stmt);

char name[64];
int qty;
unsigned long name_len;
my_bool is_null[2];

MYSQL_BIND result[2];
memset(result, 0, sizeof(result));
result[0].buffer_type   = MYSQL_TYPE_STRING;
result[0].buffer        = name;
result[0].buffer_length = sizeof(name);
result[0].length        = &name_len;
result[0].is_null       = &is_null[0];
result[1].buffer_type   = MYSQL_TYPE_LONG;
result[1].buffer        = &qty;
result[1].is_null       = &is_null[1];
mysql_stmt_bind_result(stmt, result);

while (mysql_stmt_fetch(stmt) == 0)
    printf("%s: %d\n", name, qty);

mysql_stmt_close(stmt);

/* Transaction: autocommit is on by default, so turn it off explicitly */
mysql_autocommit(conn, 0);
if (mysql_query(conn, "UPDATE t SET qty = qty - 1 WHERE id = 1") != 0 ||
    mysql_query(conn, "UPDATE t SET qty = qty + 1 WHERE id = 2") != 0)
{
    fprintf(stderr, "update failed: %s\n", mysql_error(conn));
    mysql_rollback(conn);
}
else
{
    mysql_commit(conn);
}

mysql_close(conn);
```

## See Also

- **`mariadb-connector-python`** — the `mariadb` module's C extension links against this library
- **`mariadb-connector-odbc`** / **`mariadb-connector-cpp`** — also built on top of Connector/C
- **`mariadb-transactions`** — the server-side semantics behind `mysql_commit()`/`mysql_rollback()`
- **`mariadb-prepare`** — server-side prepared statements, what the `MYSQL_STMT` API drives
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-c>
