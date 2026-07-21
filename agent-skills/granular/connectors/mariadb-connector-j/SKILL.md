---
name: mariadb-connector-j
description: "MariaDB-specific behavior of MariaDB Connector/J (the `org.mariadb.jdbc:mariadb-java-client` JDBC driver) for application code — that JDBC 4 auto-registers the driver so `Class.forName` is unneeded; that the URL scheme is `jdbc:mariadb://host:port/db?opts` (`jdbc:mysql:` only works with `permitMysqlScheme`); that `useServerPrepStmts` defaults to `false` so `PreparedStatement` uses client-side parameter substitution unless explicitly enabled; that batched `INSERT`s already use the `COM_STMT_BULK` protocol by default (`useBulkStmtsForInserts=true`), and that `getGeneratedKeys()` after a bulk insert returns *all* generated ids against a MariaDB 11.5+ server (or when statements are pipelined), not a single id; that JDBC `autocommit` defaults to `true` (opposite of the Python/C connectors) so transactions need an explicit `setAutoCommit(false)`; that `setFetchSize(Integer.MIN_VALUE)` throws (fetch size must be `>= 0`) and even a positive fetch size doesn't stop the server sending all rows underneath; that pooling should go through `MariaDbPoolDataSource` (default `maxPoolSize` 8) or an external pool, not a hand-rolled one; and that failover/multi-host URLs use a comma-separated host list with an HA-mode prefix, not driver code. Use when writing or reviewing Java code that talks to MariaDB with the `mariadb-java-client` JDBC driver."
---

# MariaDB Connector/J

*Last updated: 2026-07-21*

MariaDB Connector/J is the official JDBC driver for MariaDB and MySQL — Maven coordinates `org.mariadb.jdbc:mariadb-java-client`, LGPL-licensed. This skill covers the connector-specific behavior and the traps that bite generated application code. It is **pure Java** — it implements the client/server protocol itself and does **not** depend on MariaDB Connector/C (unlike Connector/Python or Connector/ODBC).

> **Default context:** Assume the **3.5.x** line (current release `3.5.9`) unless the user states otherwise. Connector versions are independent of the MariaDB server version — a 3.x connector routinely talks to a 10.6/10.11/11.x server.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| `Class.forName("org.mariadb.jdbc.Driver")` before connecting | **Not needed.** The driver self-registers via the JDBC 4 `META-INF/services/java.sql.Driver` mechanism — `DriverManager.getConnection(url)` alone finds it. The legacy call still works, but only add it if targeting JDBC 3-era containers |
| A `jdbc:mysql://host:3306/db` URL | Use **`jdbc:mariadb://host:port/db?opts`**. The `jdbc:mysql:` prefix is only accepted when the `permitMysqlScheme` option is present in the URL — otherwise the driver won't claim it |
| Builds SQL with string concat / `String.format()` / `+` | Never. Use **`PreparedStatement`** with `?` placeholders and `setX(index, value)` — the driver escapes/binds values, closing off SQL injection |
| Expects server-side prepared statements (binary protocol) by default | **`useServerPrepStmts` defaults to `false`.** `PreparedStatement` parameter substitution happens **client-side** (text protocol) unless you set `useServerPrepStmts=true` on the URL. Enable it when the application reuses a bounded set of statements that stays within the prepare cache (`prepStmtCacheSize`, default **250**) — repeated executions then reuse the server-side prepare, a substantial win. Leave it at the default when queries are mostly distinct: each fills a cache slot and consumes a server-side prepare (watch `max_prepared_stmt_count`) for no reuse benefit |
| Loops single `executeUpdate()` calls for bulk insert/update | Use **`addBatch()` / `executeBatch()`**. For `INSERT` batches, 3.x already sends them via the `COM_STMT_BULK` protocol by default (`useBulkStmtsForInserts=true`, `useBulkStmts` itself stays `false` for non-insert statements) — no extra option needed for the common case |
| Reads `getGeneratedKeys()` after a batch insert expecting a single id | Against a **MariaDB 11.5+** server (bulk unit-results capability, [MDEV-30366](https://jira.mariadb.org/browse/MDEV-30366)), or when statements are **pipelined** rather than sent as one bulk command, `getGeneratedKeys()` returns **all** generated ids — one per inserted row. Against older servers you can't rely on getting every id back from a single bulk insert, so verify against your target server rather than assuming a fixed single value |
| Assumes autocommit is off; wraps every statement in `setAutoCommit(false)` needlessly, or forgets to call it | **`autocommit` defaults to `true`** (standard JDBC, opposite of Connector/Python and Connector/C). For a transaction, call `conn.setAutoCommit(false)` once, then `conn.commit()` / `conn.rollback()` explicitly — don't rely on statement-level commit |
| Streams a huge `ResultSet` with `setFetchSize(Integer.MIN_VALUE)` | **Throws `SQLException`** — MariaDB Connector/J requires `rows >= 0`. Use a **positive** value, e.g. `stmt.setFetchSize(1000)`, on a `TYPE_FORWARD_ONLY` statement to stream row-by-row. Even then, the fetch size is capped internally (16384) and **the server still sends all rows** to the client socket — running another statement on the same connection before the stream is fully read pulls the remainder into memory (OOM risk); use a separate connection for concurrent work |
| Hand-rolls a pool, or opens a new `Connection` per request | Use **`MariaDbPoolDataSource`** (internal pool: `maxPoolSize` default **8**, `minPoolSize` defaults to `maxPoolSize`, `maxIdleTime` default **600s**) or wrap the plain `MariaDbDataSource`/driver URL with an external pool (HikariCP). `connection.close()` on a pooled connection returns it to the pool — it doesn't disconnect — and resets autocommit, isolation level, and any active transaction (rolled back) |
| Builds a custom failover/round-robin loop over multiple hosts | Multi-host URLs are native: **`jdbc:mariadb:sequential://host1,host2,host3/db`** (also `replication:`, `loadbalance:`, `load-balance-read:` prefixes) — comma-separate hosts in one URL instead of driver-side retry code |
| Enables TLS with `useSSL=true&verifyServerCertificate=true` (other-driver naming) | Use **`sslMode`**: `disable` (default) / `trust` / `verify-ca` / `verify-full`. Certificate/key material via `serverSslCert`, `trustStore`/`trustStorePassword`, `keyStore`/`keyStorePassword` — not `verifyServerCertificate` |
| Catches a generic `Exception` or expects a MariaDB-specific exception class | The driver throws the **standard `java.sql.SQLException` hierarchy** mapped from the server's SQLSTATE: `SQLIntegrityConstraintViolationException`, `SQLSyntaxErrorException`, `SQLTransactionRollbackException`, `SQLTransientConnectionException`, `SQLNonTransientConnectionException`. Read `.getErrorCode()` / `.getSQLState()` for the MariaDB-specific code, don't string-match `.getMessage()` |
| Sets `Statement.executeUpdate(sql, Statement.RETURN_GENERATED_KEYS)` and assumes it "just works" for any statement | `getGeneratedKeys()` only returns rows when `RETURN_GENERATED_KEYS` was explicitly requested on that statement/`prepareStatement()` call — it's not implicit for a plain `INSERT` |

## Connection, prepared statements, and a transaction

```java
import java.sql.*;

// JDBC 4 auto-registers the driver — no Class.forName() needed
try (Connection conn = DriverManager.getConnection(
        "jdbc:mariadb://localhost:3306/appdb", "app", "secret")) {

    conn.setAutoCommit(false);   // autocommit defaults to true — turn it off for a transaction

    try (PreparedStatement ps = conn.prepareStatement(
            "INSERT INTO t (name, qty) VALUES (?, ?)")) {
        ps.setString(1, "widget");
        ps.setInt(2, 5);
        ps.executeUpdate();
        conn.commit();
    } catch (SQLException e) {
        conn.rollback();
        throw e;
    }

    try (PreparedStatement ps = conn.prepareStatement(
            "SELECT id, name FROM t WHERE qty > ?")) {
        ps.setInt(1, 0);
        try (ResultSet rs = ps.executeQuery()) {
            while (rs.next()) {
                System.out.println(rs.getInt("id") + " " + rs.getString("name"));
            }
        }
    }
}
```

## Pooling with `MariaDbPoolDataSource`

```java
import org.mariadb.jdbc.MariaDbPoolDataSource;
import java.sql.*;

try (MariaDbPoolDataSource pool = new MariaDbPoolDataSource(
        "jdbc:mariadb://localhost:3306/appdb?user=app&password=secret&maxPoolSize=10")) {

    try (Connection conn = pool.getConnection();
         Statement stmt = conn.createStatement();
         ResultSet rs = stmt.executeQuery("SELECT 1")) {
        rs.next();
    } // conn.close() (implicit) returns the connection to the pool, it doesn't disconnect
}
```

## See Also

- **`mariadb-connector-r2dbc`** — the reactive, non-blocking sibling driver for Java (also pure Java, no Connector/C dependency)
- **`mariadb-transactions`** / **`mariadb-set-transaction`** — the server-side semantics behind `conn.commit()` / `conn.rollback()` and isolation levels
- **`mariadb-prepare`** — server-side prepared statements, what `useServerPrepStmts=true` uses under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-j>
