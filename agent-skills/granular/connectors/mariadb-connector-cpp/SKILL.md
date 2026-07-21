---
name: mariadb-connector-cpp
description: "MariaDB-specific behavior of MariaDB Connector/C++ (the `sql::` namespace API, modeled on JDBC 4.0) for application code — that a driver is obtained once via `sql::mariadb::get_driver_instance()` and connections come from `driver->connect(url, props)` or `sql::DriverManager::getConnection(url, props)`, both returning a raw `Connection*` you must own; the connection URL is `jdbc:mariadb://host:port/database[?opt=val]` (a `tcp://`/`unix://`/`pipe://` compatibility syntax also exists, JDBC-only); that both `PreparedStatement` parameter indexes and `ResultSet` column indexes are **1-based**, not 0-based, and index 0 or out-of-range throws; that `?` is the only placeholder syntax; that `ResultSet::next()` must be called before the first read and returns `bool`; that `connect()`/`createStatement()`/`prepareStatement()`/`executeQuery()` all return raw pointers with no automatic cleanup — wrap them in `std::unique_ptr`/`std::shared_ptr` (the documented idiom) or call `close()` explicitly, and always in child-before-parent order; that `sql::SQLString` (not `std::string`) is the parameter/return type throughout the API, though it converts to/from both directions; that **autocommit defaults to true** (opposite of Connector/Python's `autocommit=False`), so multi-statement transactions need `conn->setAutoCommit(false)` + `commit()`/`rollback()`; that all errors surface as `sql::SQLException` (and its typed subclasses) carrying `getErrorCode()`/`getSQLState()`; that client-side prepared statements are the default (`useServerPrepStmts=false`) and enabling the statement cache (`cachePrepStmts=true`) currently throws `SQLFeatureNotImplementedException` on this line; and that it is built on top of MariaDB Connector/C. Use when writing or reviewing C++ code that talks to MariaDB via Connector/C++ (the `sql::` API)."
---

# MariaDB Connector/C++

*Last updated: 2026-07-21*

MariaDB Connector/C++ is the official C++ driver for MariaDB, exposing an API modeled on the **JDBC 4.0** object model (`sql::Driver`, `sql::Connection`, `sql::Statement`, `sql::PreparedStatement`, `sql::ResultSet` — the same shapes as MariaDB Connector/J) rather than a procedural C-style API. This skill covers the connector-specific behavior and the traps that bite generated application code; it does not cover installing the library or configuring the server. It is **built on top of MariaDB Connector/C** (`libmariadb`) for the wire protocol, but application code talks only to the `sql::` classes, never to `mysql_*` calls directly.

> **Default context:** Assume the **cpp-1.0** line (`CMakeLists.txt` reports `MACPP_VERSION "1.00.0008"`, i.e. 1.0.8) unless the user states otherwise. Connector/C++ is compatible with current MariaDB and MySQL servers — its version is independent of the server version it connects to.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Constructs a `Connection` directly, or expects a constructor-based driver | Get the singleton driver via **`sql::Driver* driver = sql::mariadb::get_driver_instance();`**, then call `driver->connect(url, props)` (returns `nullptr` on error — check before use) or the static `sql::DriverManager::getConnection(url, props)` (throws instead) |
| Uses a bare `host:port` string or an ad-hoc DSN | Connection URLs use **JDBC syntax**: `jdbc:mariadb://host[:port]/[database][?opt1=val1&opt2=val2]` (port defaults to 3306). A `tcp://`/`unix://`/`pipe://` compatibility syntax also exists but only for `sql::Driver::connect()`, not `DriverManager` |
| Uses `%s`/`$1`/named placeholders in a `PreparedStatement` | The only placeholder is **positional `?`** — `"INSERT INTO t (a,b,c) VALUES (?, ?, ?)"`, bound with `setString(1, ...)`, `setInt(2, ...)`, etc. |
| Binds/reads with a 0-based index (`setString(0, ...)`, `getString(0)`) | **Both `PreparedStatement` parameter indexes and `ResultSet` column indexes are 1-based.** Index 0 or an out-of-range index throws `sql::IllegalArgumentException` (a `sql::SQLException` subclass) — the classic off-by-one for anyone used to 0-based arrays |
| Reads a column before calling `next()`, or ignores its return value | **`ResultSet::next()` must be called before any `getXxx()`** and returns `bool` — `false` means no more rows (or the set was empty); reading before the first `next()` or after it returns `false` throws |
| Leaks or manually `delete`s the pointers from `connect()`/`createStatement()`/`prepareStatement()`/`executeQuery()` | These factory methods return **raw owning pointers** — the caller is responsible for cleanup. The documented idiom wraps them immediately: `std::unique_ptr<sql::Connection> conn(driver->connect(url, props));`, `std::shared_ptr<sql::PreparedStatement> stmt(conn->prepareStatement(sql));`. Destroy/close children (`Statement`/`ResultSet`) before the `Connection` they came from |
| Passes `std::string` everywhere and expects implicit `sql::SQLString` transparency | API signatures use **`sql::SQLString`**, not `std::string`. It constructs implicitly from `std::string`/`const char*` and converts to `const char*`, but there is no implicit `operator std::string()` — construct `sql::SQLString url("jdbc:mariadb://...")` explicitly where needed |
| Assumes autocommit is off and INSERT/UPDATE need an explicit commit | **Autocommit defaults to `true`** (matching the MariaDB server default) — the opposite of Connector/Python's `autocommit=False`. Single statements commit themselves; only disable it (`conn->setAutoCommit(false)`) for multi-statement transactions, then `commit()`/`rollback()` explicitly |
| Catches `std::exception` generically, or checks a return code for errors | Catch **`sql::SQLException`** (derives from `std::runtime_error`) by reference — `catch (sql::SQLException &e)`. Read `e.getErrorCode()` / `e.getSQLState()` / `e.what()`. Typed subclasses exist for specific cases (`SQLIntegrityConstraintViolationException`, `SQLSyntaxErrorException`, `SQLTimeoutException`, `BatchUpdateException`, ...) |
| Expects server-side prepared statements or a statement cache by default | **Client-side prepared statements are the default** (`useServerPrepStmts=false`); set it `true` to use server-side `PREPARE`/`EXECUTE`. Don't set `cachePrepStmts=true` — on this connector line it throws `sql::SQLFeatureNotImplementedException("Callable/Prepared statement caches are not supported yet")` at connect time |
| Loops `executeUpdate()` for bulk insert | Use `PreparedStatement::addBatch()` + `executeBatch()`/`executeLargeBatch()`; the `rewriteBatchedStatements` and `useBulkStmts` connection options further optimize batched `INSERT`s (the two are mutually exclusive — `rewriteBatchedStatements` wins if both are set) |
| Wants the last auto-increment value or a `ResultSetMetaData`/schema introspection call | `Statement::getGeneratedKeys()` returns a `ResultSet` of generated keys after an insert; `ResultSet::getMetaData()` gives column info (`ResultSetMetaData`); `Connection::getMetaData()` gives database/schema info (`DatabaseMetaData`) |
| Shares one `Connection`/`Statement`/`ResultSet` across threads without synchronization | `get_driver_instance()` returns a **process-wide singleton** and is safe to call from multiple threads to obtain independent connections, but individual `Connection`/`Statement`/`ResultSet` objects are not documented as safe for concurrent multi-threaded use — give each thread (or task) its own connection |

## Connect, prepare, iterate, and transact

```c++
#include <iostream>
#include <mariadb/conncpp.hpp>

int main() {
  try {
    // One process-wide driver singleton
    sql::Driver* driver = sql::mariadb::get_driver_instance();

    sql::SQLString url("jdbc:mariadb://192.0.2.1:3306/appdb");
    sql::Properties properties({
        {"user", "app"},
        {"password", "secret"},
      });

    // connect() returns a raw pointer -- wrap it immediately
    std::unique_ptr<sql::Connection> conn(driver->connect(url, properties));
    if (!conn) {
      std::cerr << "connection failed" << std::endl;
      return 1;
    }

    // autocommit defaults to true; disable it for a multi-statement transaction
    conn->setAutoCommit(false);
    try {
      std::unique_ptr<sql::PreparedStatement> ins(
          conn->prepareStatement("INSERT INTO t (name, qty) VALUES (?, ?)"));
      ins->setString(1, "widget");   // parameter index is 1-based
      ins->setInt(2, 5);
      ins->executeUpdate();

      conn->commit();
    }
    catch (sql::SQLException& e) {
      conn->rollback();
      throw;
    }

    // SELECT + iterate the ResultSet
    std::unique_ptr<sql::PreparedStatement> sel(
        conn->prepareStatement("SELECT id, name FROM t WHERE qty > ?"));
    sel->setInt(1, 0);
    std::unique_ptr<sql::ResultSet> res(sel->executeQuery());

    while (res->next()) {                     // must call next() before reading
      int32_t id = res->getInt(1);             // column index is 1-based
      sql::SQLString name = res->getString("name");  // or by column label
      std::cout << id << ": " << name << std::endl;
    }

    conn->close();  // also happens implicitly when the unique_ptr goes out of scope
  }
  catch (sql::SQLException& e) {
    std::cerr << "SQL error [" << e.getErrorCode() << " " << e.getSQLState()
               << "]: " << e.what() << std::endl;
    return 1;
  }
  return 0;
}
```

## See Also

- **`mariadb-connector-c`** — the underlying C client library (`libmariadb`) this driver is built on
- **`mariadb-transactions`** — the server-side semantics behind `commit()`/`rollback()` and isolation levels set via `setTransactionIsolation()`
- **`mariadb-prepare`** — server-side prepared statements, what `useServerPrepStmts=true` uses under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-cpp>
