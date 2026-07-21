---
name: mariadb-connector-odbc
description: "MariaDB-specific behavior of MariaDB Connector/ODBC (the ODBC 3.8-compliant driver built on MariaDB Connector/C) for application code — that the DSN-less connection string keyword is `DRIVER={MariaDB ODBC 3.2 Driver}` (Windows) or a registered driver name / `.so` path (unixODBC/iODBC on Linux and macOS); that parameter markers are always the positional `?` via `SQLBindParameter`, never named or `%s`; that a single Unicode (`SQLWCHAR`) driver binary serves both ANSI and Unicode apps via `SQL_ATTR_ANSI_APP`; that `SQLPrepare`+`SQLExecute` defaults to server-side prepared statements (binary protocol) while `SQLExecDirect` defaults to client-side (text protocol) unless `EDSERVER`/`SQL_ATTR_EXECDIRECT_ON_SERVER` is set; that autocommit is ON by default (the connector issues `SET autocommit=1` at connect) so transactional code needs an explicit `SQLSetConnectAttr(..., SQL_ATTR_AUTOCOMMIT, SQL_AUTOCOMMIT_OFF, ...)` or a `COMMIT`; that the legacy `OPTION`/`OPTIONS` bitmask (found-rows, compression, multi-statements, auto-reconnect, ...) coexists with named keywords like `AUTO_RECONNECT` and `NAMEDPIPE`; that TLS is enabled implicitly by setting any of `SSLCA`/`SSLCERT`/`SSLKEY`/`SSLCIPHER`/`SSLCAPATH` (or explicitly via `FORCETLS=1`); that native error codes returned via `SQLGetDiagRec` are the raw MariaDB server error numbers, not ODBC-defined codes; and that from Python, `pyodbc.connect(\"DRIVER={...};SERVER=...\")` is the idiomatic entry point, not a MariaDB-specific module. Use when writing or reviewing application code (C/C++, or via a wrapper like pyodbc) that talks to MariaDB through the ODBC API."
---

# MariaDB Connector/ODBC

*Last updated: 2026-07-21*

MariaDB Connector/ODBC is an ODBC 3.8-compliant driver for MariaDB and MySQL, built on top of **MariaDB Connector/C** (`libmariadb`) for the actual client-server protocol work. Applications never link against it directly — they go through the standard **ODBC API** (`SQLConnect`/`SQLDriverConnect`, `SQLExecDirect`, `SQLBindParameter`, ...) mediated by a **Driver Manager** (unixODBC on Linux, iODBC on macOS, the built-in ODBC Driver Manager on Windows), or through a language wrapper on top of that API — most commonly **pyodbc** from Python. This skill covers the connector-specific behavior and the traps that bite generated application code; it does not cover installing the driver or configuring the server.

> **Default context:** Assume the **3.2** stable release series (currently 3.2.10 GA) unless the user states otherwise. Connector/ODBC's version is independent of the MariaDB server version it connects to — behavior below applies across the 3.x line unless annotated with a specific version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Guesses the driver name, or copies one from another database's ODBC setup | On Windows the registered name is **`{MariaDB ODBC 3.2 Driver}`** (version number changes per series). On Linux/macOS with unixODBC/iODBC, `Driver=` is either a path to `libmaodbc.so`/`libmaodbc.dylib` or the driver name you registered in `odbcinst.ini` — there is no fixed string, it must match what `odbcinst -i -d` installed |
| Named or `%s`/`:name` parameter placeholders | ODBC only has **positional `?` markers**, bound in order with `SQLBindParameter` (or passed positionally through a wrapper, e.g. `cursor.execute(sql, params)` in pyodbc). No named-parameter support |
| Builds SQL with string formatting/concatenation | Never. Bind values through `SQLBindParameter`/the wrapper's parameter API — the driver sends them as protocol-level parameters, not as text spliced into the query |
| Assumes a separate ANSI driver package is needed for legacy apps | MariaDB Connector/ODBC ships **one Unicode (`SQLWCHAR`) driver binary** that serves both ANSI and Unicode applications; the Driver Manager sets `SQL_ATTR_ANSI_APP` and the driver converts transparently — no separate ANSI-only driver package to install |
| Expects `SQLExecDirect` to always use server-side prepared statements | `SQLExecDirect` defaults to **client-side prepare** (`SQL_ATTR_EXECDIRECT_ON_SERVER` = `SQL_FALSE` by default); set that attribute (or the `EDSERVER` connection-string option, *since 3.2.5*) to force server-side prepare/binary protocol for one-shot execution |
| Expects `SQLPrepare`+`SQLExecute` to use the text protocol | The opposite default: `SQLPrepare` uses **server-side prepared statements** (binary protocol) unless `SQL_ATTR_PREPARE_ON_CLIENT` is `SQL_TRUE` (or the `PREPONCLIENT` connection-string option, *since 3.2.0*) forces client-side prepare |
| Assumes autocommit is off until told otherwise | **Autocommit is ON by default** — the connector sends `SET autocommit=1` at connect time, matching the ODBC standard default (`SQL_AUTOCOMMIT_ON`). Turn it off with `SQLSetConnectAttr(dbc, SQL_ATTR_AUTOCOMMIT, (SQLPOINTER)SQL_AUTOCOMMIT_OFF, 0)` before starting manual transaction control, then call `SQLEndTran(SQL_HANDLE_DBC, dbc, SQL_COMMIT)` / `SQL_ROLLBACK` |
| Ignores the legacy `OPTION`/`OPTIONS` bitmask connection parameter | It is still live and stacks with named keywords: bit 2 = return matched (not changed) rows, bit 2048 = compression, bit 4194304 = `AUTO_RECONNECT`, bit 67108864 = allow multiple statements per query (needed to run a batch of `;`-separated statements). Prefer the equivalent named keyword (`AUTO_RECONNECT=1`, etc.) when one exists — it is more readable than computing bit sums |
| Assumes TLS needs an explicit "enable SSL" switch before certs matter | Setting **any** of `SSLCA`/`SSLCERT`/`SSLKEY`/`SSLCIPHER`/`SSLCAPATH` auto-enables TLS enforcement. Use **`FORCETLS=1`** to require TLS without supplying certificate material, and **`SSLVERIFY=1`** separately to verify the server certificate against `SSLCA` |
| Treats `SQLGetDiagRec`'s native-error field as an ODBC-defined code | It is the raw **MariaDB server error number** (`mysql_errno()`), e.g. `1146` for "table doesn't exist" — cross-reference it against server error codes, not an ODBC error table. `SQLSTATE` is the server's mapped 5-character state |
| Runs several statements at once on one connection without buffering results first | The MariaDB protocol allows only one command in flight per connection; fetch or discard a statement's result set before issuing another on the **same connection** (no MARS-style interleaving). Use separate statement handles sequentially, a connection pool, or `OPTION` bit 67108864 only for literal multi-statement *batches* (`stmt1; stmt2;`) in a single `SQLExecDirect` call, which has its own limitations for cross-statement dependencies |
| Connects with `mariadb.connect(...)` (the Python `mariadb` module) when the app is ODBC-based | From Python via ODBC, use **pyodbc**: `pyodbc.connect("DRIVER={MariaDB ODBC 3.2 Driver};SERVER=...;...")`. pyodbc is a generic ODBC wrapper — it is not MariaDB-specific, but it inherits every behavior above (autocommit-on default, `?` markers, native error = server error number) |
| Assumes pyodbc commits automatically after `execute()` | pyodbc's `Connection.autocommit` defaults to **`False`** at the *pyodbc* layer (distinct from the ODBC/server-level default above) — call `conn.commit()` explicitly, or construct with `pyodbc.connect(..., autocommit=True)` |

## Connection essentials

```c
/* DSN-less connection string, C/C++ via SQLDriverConnect */
SQLWCHAR *ConnStr = L"DRIVER={MariaDB ODBC 3.2 Driver};"
                     L"SERVER=127.0.0.1;PORT=3306;"
                     L"DATABASE=appdb;UID=app;PASSWORD=secret;"
                     L"SSLCA=/etc/mysql/certs/ca.pem;SSLVERIFY=1";
```

```
# Equivalent unixODBC/iODBC odbc.ini DSN entry
[MariaDB-appdb]
Driver   = MariaDB ODBC 3.2 Driver
SERVER   = 127.0.0.1
PORT     = 3306
DATABASE = appdb
UID      = app
PASSWORD = secret
SSLCA    = /etc/mysql/certs/ca.pem
SSLVERIFY = 1
```

```python
import pyodbc

conn = pyodbc.connect(
    "DRIVER={MariaDB ODBC 3.2 Driver};"
    "SERVER=127.0.0.1;PORT=3306;DATABASE=appdb;UID=app;PWD=secret",
    autocommit=False,   # pyodbc's own default; shown for clarity
)
cur = conn.cursor()
cur.execute(
    "INSERT INTO t (name, qty) VALUES (?, ?)",  # positional ? markers only
    ("widget", 5),
)
conn.commit()   # required: neither pyodbc nor a manual OFF toggle auto-commits

cur.execute("SELECT id, name FROM t WHERE qty > ?", (0,))
for row in cur.fetchall():
    print(row.id, row.name)

cur.close()
conn.close()
```

## See Also

- **`mariadb-connector-c`** — the underlying `libmariadb` client library that does the actual protocol work
- **`mariadb-transactions`** — server-side semantics behind `SQLEndTran`/`conn.commit()` and isolation levels (`SQL_ATTR_TXN_ISOLATION` maps directly to `SET SESSION TRANSACTION ISOLATION LEVEL`)
- **`mariadb-prepare`** — server-side prepared statements, what `SQLPrepare`'s default (and `EDSERVER`) use under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-odbc>
