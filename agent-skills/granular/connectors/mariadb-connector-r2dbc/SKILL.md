---
name: mariadb-connector-r2dbc
description: "MariaDB-specific behavior of MariaDB Connector/R2DBC (the `org.mariadb:r2dbc-mariadb` reactive driver implementing the R2DBC SPI) for application code — that the connection URL scheme is `r2dbc:mariadb://user:pw@host:port/db` and factories come from `ConnectionFactories.get(url)` or a `MariadbConnectionConfiguration` builder + `MariadbConnectionFactory`; that placeholders are positional `?` (bound 0-indexed via `.bind(int, value)`) or named `:name` (via `.bind(String, value)`), never mixed with driver-side string interpolation; that NOTHING runs until the `Publisher` returned by `Statement.execute()` (a `Flux<MariadbResult>`) is subscribed, and a `Result` can be consumed exactly once via `.map()` or `getRowsUpdated()`; that `bindNull(index, Class)` needs an explicit type; that `autocommit` defaults to `true` and `useServerPrepStmts` (binary protocol) defaults to `false`; that transactions go through `beginTransaction()`/`commitTransaction()`/`rollbackTransaction()` returning `Mono<Void>` that must itself be subscribed; that connection pooling is not built in and needs `r2dbc-pool`'s `ConnectionPool`/`ConnectionPoolConfiguration`; that calling `.block()` inside a reactive pipeline defeats the whole point and errors surface as `onError` signals (`R2dbcException` subtypes) rather than thrown exceptions; and that `io.r2dbc.spi.Batch` groups distinct un-parameterized SQL strings while `Statement.add()` adds another bound parameter set to the same parameterized SQL. Use when writing or reviewing Java code that talks to MariaDB reactively via R2DBC."
---

# MariaDB Connector/R2DBC

*Last updated: 2026-07-21*

MariaDB Connector/R2DBC is the official reactive, non-blocking driver for MariaDB implementing the [R2DBC](https://r2dbc.io) SPI — Maven coordinates `org.mariadb:r2dbc-mariadb`. It is **100% pure Java** (Java 8+), built on Reactor and Netty, and does **not** depend on Connector/C. This skill covers the connector-specific behavior and the traps that bite generated application code. It is a separate, independently-versioned sibling of **MariaDB Connector/J** (the blocking JDBC driver, also pure Java) — same vendor, different API paradigm; do not assume JDBC idioms (blocking calls, `try`-with-resources returning a live `ResultSet`) carry over.

> **Default context:** Assume the **1.4** line (`r2dbc-mariadb` 1.4.1) unless the user states otherwise; 1.0 and 1.1 have reached end of life. The connector follows the [R2DBC 1.0.0 spec](https://r2dbc.io/spec/1.0.0.RELEASE/spec/html/) (a legacy `r2dbc-mariadb-0.9.1-spec` artifact exists for the older spec). Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| A JDBC-style URL (`jdbc:mariadb://...`) or a bare host string | The R2DBC URL scheme is **`r2dbc:mariadb://[user:pw@]host[:port][,host2...]/db[?opt=val]`** — the registered driver id is `mariadb`. Get a factory with `ConnectionFactories.get(url)`, or build one explicitly: `MariadbConnectionConfiguration.builder()...build()` + `new MariadbConnectionFactory(config)` |
| `%s`/f-string/concat SQL, or assumes only `?` works | Two placeholder styles, never string-built SQL: positional **`?`** bound by **0-based** index (`.bind(0, val)`), and named **`:name`** bound by name (`.bind("name", val)`). Both are parsed from the same SQL text; pick one style per statement |
| Expects `execute()` to run the query immediately | `Statement.execute()` returns a **`Flux<MariadbResult>`** (a cold `Publisher`) — **nothing hits the wire until it is subscribed** (`.subscribe()`, `Mono.from(...).block()`, a Reactor operator chain, etc.). Building the statement and calling `execute()` alone does nothing |
| Reads a `Result` twice, or ignores it after `execute()` | A `Result` is **consume-once, forward-only**: call exactly one of `.map(BiFunction<Row,RowMetadata,T>)` or `.getRowsUpdated()`. Not fully consuming it can leave the corresponding statement incomplete |
| Binds `null` as a plain value | `.bind(index, null)` is invalid — use **`bindNull(index, Class<?> type)`** (or the named overload) so the driver knows the SQL type to send |
| Assumes DML needs an explicit commit, or that autocommit is off | **`autocommit` defaults to `true`** — new connections auto-commit each statement. To use transactions, call `setAutoCommit(false)` or explicitly `beginTransaction()` |
| Expects server-side prepared statements (binary protocol) by default | **`useServerPrepStmts` defaults to `false`** — the text protocol is used (parameters substituted client-side) unless set to `true`, which switches to server-side prepare + a prepare-result LRU cache (`prepareCacheSize`, default 256) |
| Calls `conn.commit()` / `conn.rollback()` (JDBC-style) | Transactions are reactive: **`beginTransaction()`**, **`commitTransaction()`**, **`rollbackTransaction()`** each return `Mono<Void>` — they are no-ops until subscribed, e.g. `Mono.from(connection.beginTransaction()).block()` or chained into the pipeline |
| Calls `.block()` inside a reactive chain to "simplify" the code | Blocking a Netty event-loop thread inside the pipeline is the classic reactive anti-pattern — it defeats non-blocking I/O and can deadlock the loop. Compose with `Mono`/`Flux` operators end-to-end; only `.block()` at the outermost boundary (e.g. `main`, a test) |
| Wraps calls in `try/catch (SQLException)` expecting a thrown exception | Errors are delivered as an **`onError` signal**, not a synchronous throw — subscribe with an error handler (`.doOnError()`, `.onErrorResume()`, etc.). Errors surface as typed `R2dbcException` subclasses (e.g. `R2dbcBadGrammarException`, `R2dbcDataIntegrityViolationException`, `R2dbcTransientResourceException`) derived from the server's SQLSTATE class |
| Hand-rolls a pool or opens a new connection per request | No pooling is built in — add **`r2dbc-pool`** and wrap the `MariadbConnectionFactory` in `ConnectionPoolConfiguration.builder(factory).maxSize(...).build()` → `new ConnectionPool(poolConfig)`; borrow with `pool.create()`, return by `.close()` |
| Loops single-row `execute()` calls for a bulk insert | Call **`Statement.add()`** between `.bind()` calls on the *same* parameterized statement to queue another parameter set, then `execute()` once — one round trip covers all bound rows |
| Uses `io.r2dbc.spi.Batch` expecting parameter binding | `Batch` (`conn.createBatch().add(sql1).add(sql2)...`) groups **distinct, already-literal SQL strings with no parameter binding** — for parameterized bulk operations use `Statement.add()` instead (see above) |
| Assumes TLS is on by default | `sslMode` defaults to **`DISABLE`** (no TLS) — set it explicitly (`TRUST`/`VERIFY_CA`/`VERIFY_FULL`) for anything beyond local development |

## Connection, query, and result mapping

```java
import io.r2dbc.spi.ConnectionFactories;
import io.r2dbc.spi.ConnectionFactory;
import io.r2dbc.spi.Connection;
import io.r2dbc.spi.Result;
import reactor.core.publisher.Flux;
import reactor.core.publisher.Mono;

ConnectionFactory factory =
    ConnectionFactories.get("r2dbc:mariadb://app:secret@localhost:3306/appdb");

Flux<String> names = Mono.from(factory.create())
    .flatMapMany(conn ->
        Flux.from(conn.createStatement("SELECT name FROM t WHERE qty > ?")
                .bind(0, 0)          // positional, 0-based
                .execute())
            .flatMap(result -> result.map((row, meta) -> row.get("name", String.class)))
            .concatWith(Mono.from(conn.close()).then(Mono.empty())));

names.subscribe(System.out::println);   // nothing runs before this subscribe
```

Transactions (manual, reactive — no implicit commit/rollback):

```java
Mono<Void> work = Mono.from(factory.create())
    .flatMap(conn -> Mono.from(conn.beginTransaction())
        .then(Mono.from(conn.createStatement(
                "INSERT INTO t (name) VALUES (:name)")
            .bind("name", "widget")
            .execute()))
        .flatMap(res -> Mono.from(res.getRowsUpdated()))
        .then(Mono.from(conn.commitTransaction()))
        .onErrorResume(e -> Mono.from(conn.rollbackTransaction()).then(Mono.error(e)))
        .then(Mono.from(conn.close())));

work.block();   // only block at the outermost boundary
```

## See Also

- **`mariadb-connector-j`** — the blocking JDBC sibling (also pure Java, no Connector/C); use it when the application isn't reactive
- **`mariadb-transactions`** / **`mariadb-set-transaction`** — server-side semantics behind `beginTransaction()`/`commitTransaction()`/isolation levels
- **`mariadb-prepare`** — server-side prepared statements, what `useServerPrepStmts=true` uses under the hood
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-r2dbc>
