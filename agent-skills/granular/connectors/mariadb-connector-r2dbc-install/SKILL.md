---
name: mariadb-connector-r2dbc-install
description: "Installing and configuring MariaDB Connector/R2DBC, the reactive non-blocking driver for MariaDB — the Maven coordinates `org.mariadb:r2dbc-mariadb`, the fact that it implements R2DBC rather than JDBC so connections come from `ConnectionFactories.get()` with an `r2dbc:mariadb://` URL and never from `DriverManager`; that connection pooling is a separate `io.r2dbc:r2dbc-pool` dependency rather than a built-in; that `sslMode` defaults to disabled so TLS must be requested explicitly and then tuned with `serverSslCert` or a truststore; and the parameter names that differ from the JDBC driver, notably `username` and `socket`. Use when adding the driver to a build, wiring a `ConnectionFactory`, or configuring pooling and TLS."
---

# MariaDB Connector/R2DBC: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/R2DBC is the reactive driver for MariaDB: pure Java, built on Reactor and Netty, implementing the R2DBC SPI rather than JDBC. This skill covers adding it to a build and configuring it. For writing reactive code against it, see **`mariadb-connector-r2dbc-usage`**.

> **Default context:** Assume the **1.4** stable line unless the user states otherwise. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Adds `org.mariadb.jdbc:mariadb-java-client` for a reactive application | Different artifact, different SPI. R2DBC is **`org.mariadb:r2dbc-mariadb`** — note the shorter group ID. The JDBC driver cannot serve an R2DBC `ConnectionFactory` |
| Calls `DriverManager.getConnection("r2dbc:mariadb://…")` | R2DBC has no `DriverManager`. Obtain a factory with **`ConnectionFactories.get("r2dbc:mariadb://…")`** or build a `MariadbConnectionConfiguration` and pass it to `MariadbConnectionFactory` |
| Writes a `jdbc:mariadb://` URL | The R2DBC scheme is **`r2dbc:mariadb://`**; the registered driver identifier is `mariadb` |
| Expects a built-in pool, or reaches for the JDBC driver's `MariaDbPoolDataSource` | Pooling in R2DBC is a **separate dependency**, `io.r2dbc:r2dbc-pool`, which wraps any `ConnectionFactory`. Nothing pools by default |
| Uses `user=` in the URL or configuration | The parameter is **`username`**. Similarly the Unix socket parameter is **`socket`**, not `socketPath` or `localSocket` |
| Sets `serverSslCert` and assumes TLS is on | **`sslMode` defaults to `DISABLE`.** Nothing is encrypted until `sslMode` is set to `trust`, `verify-ca`, or `verify-full` |
| Ships a private CA and expects the JVM's public CAs to stop applying | The driver falls back to the system truststore. Set **`fallbackToSystemTrustStore=false`** (and `fallbackToSystemKeyStore=false` for client certificates) to make trust exclusive |
| Blocks on the returned `Publisher` — `.block()` in request-handling code | The whole point is non-blocking. A `Mono`/`Flux` must be composed and returned, not resolved; blocking on a Reactor thread can deadlock the event loop |
| Targets a recent Java baseline and drops Java 8 support from the build | The connector is compiled for **Java 8**, so it does not force the application's baseline upward |
| Mixes an arbitrary `r2dbc-spi` version into the build | The driver is built against a specific R2DBC SPI release (**1.0.0.RELEASE** on the 1.4 line). Let Maven resolve it transitively rather than pinning a different one |
| Assumes prepared statements behave as they do in the JDBC driver | Server-side prepared statements are governed by **`useServerPrepStmts`** and cached according to **`prepareCacheSize`** — set them deliberately for a reactive workload |

## Installing

### Maven

```xml
<dependency>
    <groupId>org.mariadb</groupId>
    <artifactId>r2dbc-mariadb</artifactId>
    <version>1.4.1</version>
</dependency>

<!-- Only if the application pools connections -->
<dependency>
    <groupId>io.r2dbc</groupId>
    <artifactId>r2dbc-pool</artifactId>
    <version>1.0.2.RELEASE</version>
</dependency>
```

### Gradle

```groovy
implementation 'org.mariadb:r2dbc-mariadb:1.4.1'
implementation 'io.r2dbc:r2dbc-pool:1.0.2.RELEASE'
```

Reactor and Netty arrive transitively. A manual JAR install is possible — the driver and `r2dbc-pool` both need to be on the `CLASSPATH` — but a build tool is far less error-prone given the transitive graph.

## Configuration

### From a URL

```java
ConnectionFactory factory = ConnectionFactories.get(
    "r2dbc:mariadb://app:secret@db.example.com:3306/appdb?sslMode=verify-full");
```

### Programmatically

The builder makes the options discoverable and keeps credentials out of a URL string:

```java
MariadbConnectionConfiguration conf = MariadbConnectionConfiguration.builder()
    .host("db.example.com")
    .port(3306)
    .username("app")               // username, not user
    .password("secret")
    .database("appdb")
    .connectTimeout(Duration.ofSeconds(10))
    .useServerPrepStmts(true)
    .build();

MariadbConnectionFactory factory = new MariadbConnectionFactory(conf);
```

For a local server, replace host and port with `.socket("/var/run/mysqld/mysqld.sock")`.

### TLS

```java
MariadbConnectionConfiguration.builder()
    .host("db.example.com").username("app").password("secret")
    .sslMode(SslMode.VERIFY_FULL)
    .serverSslCert("/etc/ssl/certs/ca.pem")
    .build();
```

| Parameter | Purpose |
|---|---|
| `sslMode` | `DISABLE` (default), `TRUST`, `VERIFY_CA`, `VERIFY_FULL`, `TUNNEL` |
| `serverSslCert` | CA or server certificate to trust |
| `clientSslCert`, `clientSslKey`, `clientSslPassword` | Client certificate for mutual TLS |
| `tlsProtocol` | Allowed protocol versions |
| `fallbackToSystemTrustStore`, `fallbackToSystemKeyStore` | `false` disables the JVM-default fallback |
| `sslContextBuilderCustomizer` | Escape hatch for anything the named options do not cover |

### Pooling

```java
ConnectionPoolConfiguration poolConf = ConnectionPoolConfiguration.builder(factory)
    .maxSize(20)
    .maxIdleTime(Duration.ofMinutes(30))
    .build();

ConnectionPool pool = new ConnectionPool(poolConf);
```

`ConnectionPool` is itself a `ConnectionFactory`, so the rest of the application is unaffected by whether pooling is present.

### Spring Data R2DBC

With Spring Boot, the same driver is configured through `spring.r2dbc.url` and friends, and Spring builds the `ConnectionFactory`. The driver dependency and the URL scheme are unchanged; only the wiring moves into configuration properties.

## See Also

- **`mariadb-connector-r2dbc-usage`** — using the driver once installed: statements, parameter binding, result mapping, transactions, batches
- **`mariadb-connector-j-install`** — the blocking JDBC alternative, when a reactive stack is not in play
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-r2dbc>

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
