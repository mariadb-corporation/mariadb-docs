---
name: mariadb-connector-j-install
description: "Installing and configuring MariaDB Connector/J, the JDBC driver for MariaDB — the Maven and Gradle coordinates `org.mariadb.jdbc:mariadb-java-client`, the driver class `org.mariadb.jdbc.Driver`, and the Java version each release series supports; that the 3.x lines accept only the `jdbc:mariadb:` URL scheme unless `permitMysqlScheme` is set; that JNA is not a transitive dependency and must be added by the application before Unix domain sockets or Windows named pipes will work; and the TLS configuration, where `sslMode` defaults to disabled so encryption has to be requested explicitly, then tuned with `serverSslCert`, truststores, and keystores. Use when adding the driver to a build, wiring a datasource, or configuring TLS."
---

# MariaDB Connector/J: Installation and Configuration

*Last updated: 2026-08-10*

MariaDB Connector/J is the Type 4 JDBC driver for MariaDB, written in pure Java with no dependency on MariaDB Connector/C. This skill covers adding it to a build, configuring the connection URL and datasource, and setting up TLS. For writing JDBC code against it, see **`mariadb-connector-j-usage`**.

> **Default context:** Assume the **3.5** stable line unless the user states otherwise. Connector versions are independent of the MariaDB server version.

## What LLMs Often Miss

| If the agent writes / assumes… | …prefer the MariaDB form |
|---|---|
| Guesses the coordinates from the product name (`mariadb-connector-j`, `mariadb-jdbc`) | The artifact is **`org.mariadb.jdbc:mariadb-java-client`** and the driver class is **`org.mariadb.jdbc.Driver`**. Nothing else registers the `jdbc:mariadb:` scheme |
| Writes a `jdbc:mysql://` URL | From **3.0** onward only **`jdbc:mariadb:`** is accepted by default. `jdbc:mysql:` works only when the **`permitMysqlScheme`** option is present in the URL — and using `jdbc:mariadb:` is what guarantees this driver is chosen when several drivers are on the classpath |
| Configures a Unix domain socket or a Windows named pipe and gets a `ClassNotFoundException` | **JNA is not pulled in transitively.** Those transports use `com.sun.jna`, so the application must add **`net.java.dev.jna:jna`** and **`net.java.dev.jna:jna-platform`** (4.2.1 or later) itself. TCP connections need neither |
| Sets `serverSslCert` and assumes the connection is now encrypted | It is not. **`sslMode` defaults to `disable`** — the certificate option alone changes nothing. TLS starts only when `sslMode` is set to `trust`, `verify-ca`, or `verify-full` (the exception: a credential plugin that requires TLS forces `verify-full`) |
| Reaches for `useSsl=true` / `trustServerCertificate=true` on a 3.x driver | Those are the 2.x spellings. Since 3.0 the single option is **`sslMode`**, with values `disable`, `trust`, `verify-ca`, `verify-full`; `sslMode=true` and `sslMode=1` are aliases for `verify-full` |
| Uses `sslMode=trust` in production because it "makes TLS work" | `trust` encrypts but verifies nothing, so it defends against passive eavesdropping only. Use it to prove the server has TLS enabled, then move to **`verify-full`** |
| Assumes a certificate must be a file on disk | `serverSslCert` accepts three forms: a **full file path**, a **`classpath:`-relative path**, or the **certificate text inline**. The last is what makes a certificate deployable through configuration alone |
| Ships a custom truststore and expects the public CAs to stop working | The connector falls back to the JVM's default truststore when `serverSslCert` does not resolve. Set **`fallbackToSystemTrustStore=false`** to make trust exclusive |
| Targets a Java version the chosen release series does not cover | **3.5, 3.4, and 3.3 run on Java 8, 11, 17, 21, and 25.** Pick the release series from the Java version, not the other way round |
| Recommends the 2.7 line for a Java 8 project | Unnecessary — the current 3.x lines still support Java 8, and 2.7 is a legacy series. Start new work on **3.5** |
| Registers the driver with `Class.forName(...)` because that is the JDBC habit | Service loading handles it: `DriverManager.getConnection("jdbc:mariadb://…")` is enough. `Class.forName("org.mariadb.jdbc.Driver")` still works but is redundant |
| Reaches for an external pool without setting the driver class | With HikariCP or similar, set `driverClassName` to **`org.mariadb.jdbc.Driver`**. The driver also ships its own pool, `MariaDbPoolDataSource`, whereas `MariaDbDataSource` opens a fresh connection on every `getConnection()` |

## Installing

### Maven

```xml
<dependency>
    <groupId>org.mariadb.jdbc</groupId>
    <artifactId>mariadb-java-client</artifactId>
    <version>3.5.9</version>
</dependency>
```

### Gradle

```groovy
implementation 'org.mariadb.jdbc:mariadb-java-client:3.5.9'
```

### Optional dependencies

Add these only for the features that need them:

```xml
<!-- Unix domain sockets and Windows named pipes: JNA 4.2.1 or later -->
<dependency>
    <groupId>net.java.dev.jna</groupId>
    <artifactId>jna</artifactId>
    <version>$JNA_VERSION</version>
</dependency>
<dependency>
    <groupId>net.java.dev.jna</groupId>
    <artifactId>jna-platform</artifactId>
    <version>$JNA_VERSION</version>
</dependency>
```

### Manual JAR, and building from source

The `.jar` can be placed on the `CLASSPATH` directly, though a build tool is the better option. To build:

```bash
git clone https://github.com/MariaDB/mariadb-connector-j.git
cd mariadb-connector-j
mvn -Dmaven.test.skip=true package     # result: target/mariadb-java-client-x.y.z.jar
```

Building with the tests enabled (`mvn package`) needs a MariaDB or MySQL server listening on `localhost:3306`, a database named `testj`, and a `root` account with an empty password.

## Configuration

### Connection URL

```
jdbc:mariadb://host:port/database?option1=value1&option2=value2
```

```java
Connection conn = DriverManager.getConnection(
    "jdbc:mariadb://localhost:3306/appdb?user=app&password=secret&sslMode=verify-full");
```

Options can equally be passed as a `Properties` object, which keeps credentials out of a URL that might end up in a log.

### TLS

```java
// Step 1 — confirm the server offers TLS at all (encrypts, verifies nothing)
"jdbc:mariadb://localhost/appdb?user=app&password=secret&sslMode=trust"

// Step 2 — the production setting
"jdbc:mariadb://localhost/appdb?user=app&password=secret"
  + "&sslMode=verify-full&serverSslCert=/etc/ssl/certs/ca.pem"
```

| Option | Effect |
|---|---|
| `sslMode` | `disable` (default), `trust`, `verify-ca`, `verify-full` |
| `serverSslCert` | Server or CA certificate: file path, `classpath:…`, or the certificate text inline |
| `trustStore`, `trustStorePassword`, `trustStoreType` | Use a Java truststore instead of a single certificate |
| `keyStore`, `keyStorePassword`, `keyPassword`, `keyStoreType` | Client certificate for mutual TLS |
| `fallbackToSystemTrustStore` | `false` stops the fallback to the JVM's default CA set |
| `disableSslHostnameVerification` | Legacy spelling; prefer `sslMode=verify-ca` |

If the server's certificate chains to a well-known public CA already in the JVM truststore, `sslMode=verify-full` on its own is enough — no certificate option required.

### Pooling

```java
MariaDbPoolDataSource ds = new MariaDbPoolDataSource(
    "jdbc:mariadb://localhost:3306/appdb?user=app&password=secret&maxPoolSize=20");
```

The built-in pool cleans connection state on release and drops connections that have gone idle, which avoids the classic failure of handing out a connection the server has already closed at `wait_timeout`. With an external pool, configure `org.mariadb.jdbc.Driver` as the driver class and let that pool own the lifecycle.

## See Also

- **`mariadb-connector-j-usage`** — using the driver once it is on the classpath: statements, batches, generated keys, streaming, transactions
- **`mariadb-connector-r2dbc-install`** — the reactive alternative for non-blocking applications
- Canonical reference on `mariadb.com/docs`, consult for edge cases not covered here: <https://mariadb.com/docs/connectors/mariadb-connector-j>
