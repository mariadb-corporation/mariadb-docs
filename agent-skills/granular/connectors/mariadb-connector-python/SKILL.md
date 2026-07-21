---
name: mariadb-connector-python
description: "MariaDB-specific behavior of MariaDB Connector/Python (the `mariadb` PyPI module, a PEP-249 / DB API 2.0 driver) for application code — that the default paramstyle is qmark (`?`), not format (`%s`), and styles must not be mixed; that string formatting must never build SQL; that autocommit is off by default so DML needs `conn.commit()`; that a single parameter needs a one-tuple `(v,)`; that the text protocol is default and `binary=True` switches to server-side prepared statements; that cursors are buffered by default; connection pooling via `ConnectionPool` (default size 5, max 64); `callproc()` for stored procedures; the DB API exception hierarchy under `mariadb.Error`; and that the module is a C extension built on Connector/C. Use when writing or reviewing Python code that talks to MariaDB with the `mariadb` module."
---

# MariaDB Connector/Python

*Last updated: 2026-07-21*

MariaDB Connector/Python is the official Python driver for MariaDB — the `mariadb` module on PyPI (`pip install mariadb`), implementing the Python DB API 2.0 ([PEP-249](https://peps.python.org/pep-249)). This skill covers the connector-specific behavior and the traps that bite generated application code. It is a **C extension built on MariaDB Connector/C**, so a build needs the C connector's development files (`mariadb_config` on the `PATH`) — it is not pure Python on the 1.1 line.

> **Default context:** Assume the **1.1** stable line unless the user states otherwise. Behavior shared with older 1.x releases is shown without annotation; features added in the newer **2.0** line (`mariadb://` URI connection strings, async `asyncConnect`/`create_async_pool`, a pure-Python implementation) are marked *since 2.0*. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `%s` placeholders everywhere (`WHERE id = %s`) | The default **paramstyle is `qmark`** — use `?`: `cursor.execute("SELECT ... WHERE id = ?", (id,))`. `%s` (format) is accepted for compatibility, but **mixing `?` and `%s` in one statement raises**. Prefer `?` |
| Builds SQL with f-strings / `%` / `.format()` / string concat | Never. Pass values as the second argument to `execute()`; the connector escapes them. `cursor.execute("... VALUES (?, ?)", (a, b))` |
| Passes a single parameter as a scalar (`execute(sql, id)`) | Parameters must be a **tuple or list**; a single value needs a one-element tuple: `(id,)` — note the trailing comma. `executemany()` takes a **list of tuples** |
| Assumes autocommit is on; INSERT/UPDATE "disappear" | **`autocommit` is `False` by default.** Call `conn.commit()` after DML, or open the connection with `autocommit=True`. On close without commit, the transaction rolls back |
| Uses a libpq-style DSN (`"host=... dbname=..."`) or a MySQL URL | `connect()` takes **keyword args**: `mariadb.connect(host="localhost", port=3306, user=..., password=..., database=...)`. *Since 2.0* a `mariadb://user:pw@host/db` URI string is also accepted (kwargs override URI values) |
| Imports `MySQLdb`, `pymysql`, or `mysql.connector` | The module is **`mariadb`** (`import mariadb`). API is DB API 2.0 but the module name, C-extension nature, and `?` paramstyle differ from those drivers |
| Expects server-side prepared statements by default | The **text protocol is the default**. Set **`binary=True`** for the binary protocol (server-side prepared statements) — at the cursor (`conn.cursor(binary=True)`), or *since 2.0* at the connection. (`prepared=True` is deprecated in favor of `binary=True`) |
| Expects the driver to auto-reconnect after a dropped connection | **No automatic reconnection.** (The `reconnect` parameter was removed in 2.0.) Use a connection pool, or call `conn.reconnect()` explicitly |
| Streams a huge result set with a default cursor | Cursors are **buffered by default** — the whole result is pulled into memory. For large results use `conn.cursor(buffered=False)` and iterate row by row |
| Loops `execute()` for bulk insert/update | Use **`executemany(sql, list_of_tuples)`** — far fewer round trips. All tuples must have the **same types**; signal NULL / column default with `mariadb.constants.INDICATOR` values, not `None`-as-default |
| Hand-rolls a pool, or opens a new connection per request | Use **`mariadb.ConnectionPool(pool_name="app", pool_size=5)`**; borrow with `pool.get_connection()` and return it by `conn.close()`. `pool_size` defaults to 5, **max 64**; `pool_reset_connection=True` (default) resets each connection before reuse |
| Calls a stored procedure by string-building `CALL ...` with OUT params | Use **`cursor.callproc("proc_name", (in1, in2))`**; read OUT/INOUT results from the returned sequence / a following result set |
| Catches `Exception` or a MySQL driver's error class | Catch **`mariadb.Error`** (the DB API base). Subclasses: `OperationalError`, `IntegrityError`, `ProgrammingError`, `DataError`, `InterfaceError`, `InternalError`, `NotSupportedError`, `PoolError`. `.errno` / `.sqlstate` are on the exception |

## Connection essentials

```python
import mariadb

# Keyword-argument connection (works on all supported versions)
conn = mariadb.connect(
    host="localhost", port=3306,
    user="app", password="secret",
    database="appdb",
    autocommit=False,          # the default; shown for clarity
)

# since 2.0 — URI connection string
conn = mariadb.connect("mariadb://app:secret@localhost:3306/appdb")

with conn.cursor() as cur:
    cur.execute("INSERT INTO t (name, qty) VALUES (?, ?)", ("widget", 5))
    conn.commit()                      # autocommit is off by default

    cur.execute("SELECT id, name FROM t WHERE qty > ?", (0,))   # note (0,)
    for row in cur:                    # buffered by default
        print(row)
```

Common `connect()` keywords: `host` (default `localhost`; a comma-separated list gives simple failover), `port` (default `3306`), `user`/`username`, `password`/`passwd`, `database`/`db`, `unix_socket`, `autocommit`, and the SSL/TLS options. Result-shape options include `dictionary=True` (rows as dicts) and `named_tuple=True`. Some options apply only to the C extension — see the connection-class reference.

## Pooling

```python
import mariadb

pool = mariadb.ConnectionPool(
    pool_name="app", pool_size=8,      # max 64; pool_reset_connection defaults to True
    host="localhost", user="app", password="secret", database="appdb",
)

conn = pool.get_connection()
try:
    with conn.cursor() as cur:
        cur.execute("SELECT 1")
        cur.fetchone()
finally:
    conn.close()                        # returns the connection to the pool (does not really close it)
```

## See Also

- **`mariadb-connector-c`** — the underlying C client library this module wraps (build-time dependency)
- **`mariadb-transactions`** / **`mariadb-set-transaction`** — the server-side semantics behind `conn.commit()` / `conn.rollback()` and isolation levels
- **`mariadb-prepare`** — server-side prepared statements, what `binary=True` uses under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-python>
