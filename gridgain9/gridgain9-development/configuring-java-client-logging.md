---
description: >-
  Configure logging for the GridGain 9 Java thin client using java.util.logging, Logback, or Log4j2.
---

# How to Configure Logging for the Java Thin Client

## Prerequisites

- **Java 11** or later
- **A GridGain 9 thin client dependency** in your Maven or Gradle project
- **A running cluster** for verification ([How to Start a Cluster With Docker Compose](../gridgain9-management/installation/start-cluster-docker-compose.md))
- **Framework-specific** (pick one):
  - **java.util.logging**: No additional dependencies (included in the JDK)
  - **Logback**: `slf4j-api` 2.0+ and `logback-classic` 1.5+
  - **Log4j2**: `log4j-api`, `log4j-core`, and `log4j-jpl` 2.24+

{% code title="Maven dependency" %}
```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-client</artifactId>
    <!-- Use the latest GridGain 9 version -->
    <version>LATEST_GRIDGAIN_9_VERSION</version>
</dependency>
```
{% endcode %}

GridGain 9 artifacts are hosted on the GridGain Nexus repository, not Maven Central. Add this to your `pom.xml`:

{% code title="Required repository" %}
```xml
<repositories>
    <repository>
        <id>gridgain-external</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>
```
{% endcode %}

The group ID is `org.gridgain`, but the artifact name keeps the `ignite-` prefix. All Java packages remain `org.apache.ignite.*`.

## Overview

Configure diagnostic logging for the GridGain 9 Java thin client using java.util.logging (JUL), Logback with SLF4J, or Log4j2. The thin client uses `System.Logger` (Java 9+) and routes to JUL by default. Three framework sections follow: pick the one that matches your project and skip the others.

JUL uses different level names than Logback and Log4j2. The level mapping table below applies to all three configurations.

## Level Name Mapping

JUL rejects level names like `DEBUG` or `TRACE` with `IllegalArgumentException: Bad level "DEBUG"`. Use the correct names for your framework:

| Severity | System.Logger | java.util.logging | Logback / Log4j2 |
|----------|---------------|-------------------|-------------------|
| Most verbose | `TRACE` | `FINER` | `TRACE` |
| Diagnostic | `DEBUG` | `FINE` | `DEBUG` |
| Informational | `INFO` | `INFO` | `INFO` |
| Potential issues | `WARNING` | `WARNING` | `WARN` |
| Failures | `ERROR` | `SEVERE` | `ERROR` |

## Configure java.util.logging

JUL is the default backend with no additional dependencies.

### Properties File Approach

Create a file named `logging.properties`:

{% code title="logging.properties" %}
```properties
# Both the logger and handler levels must be set for messages to appear.
handlers = java.util.logging.ConsoleHandler

# Logger level
org.apache.ignite.internal.client.level = FINE

# Handler level (must also be FINE or lower to pass messages through)
java.util.logging.ConsoleHandler.level = FINE
java.util.logging.ConsoleHandler.formatter = java.util.logging.SimpleFormatter
```
{% endcode %}

`org.apache.ignite.internal.client.level = FINE` sets the client package to diagnostic output. The `ConsoleHandler.level` must also be `FINE` or the handler filters out the messages before they reach the console.

Load the properties file at JVM startup:

```bash
java -Djava.util.logging.config.file=logging.properties -jar your-app.jar
```

### Programmatic Approach

Configure JUL in code if JVM startup parameters are not modifiable:

```java
import java.util.logging.*;

static void configureLogging() {
    Logger igniteLogger = Logger.getLogger("org.apache.ignite.internal.client");
    igniteLogger.setLevel(Level.FINE);

    ConsoleHandler handler = new ConsoleHandler();
    handler.setLevel(Level.FINE);
    handler.setFormatter(new SimpleFormatter());
    igniteLogger.addHandler(handler);
}
```

Call `configureLogging()` before creating the `IgniteClient`.

### Verify JUL Output

Connect to the cluster. Connection events appear at `FINE` level on standard error:

```text
FINE: Connection established [remoteAddress=127.0.0.1/<unresolved>:10800]
INFO: Partition assignment change notification received [remoteAddress=127.0.0.1/<unresolved>:10800]
FINE: Connection closed [remoteAddress=127.0.0.1/<unresolved>:10800]
```

{% hint style="success" %}
**Checkpoint:**
A `FINE: Connection established` message appears in the console output when the client connects. If no output appears, verify that both the logger and handler levels are set to `FINE`.
{% endhint %}

## Configure Logback With SLF4J

Logback requires an adapter to bridge `System.Logger` to SLF4J. Add the dependencies, create the adapter and factory classes, and pass the factory to the client builder.

### Add Logback Dependencies

{% code title="pom.xml" %}
```xml
<dependency>
    <groupId>ch.qos.logback</groupId>
    <artifactId>logback-classic</artifactId>
    <version>1.5.16</version>
</dependency>
<dependency>
    <groupId>org.slf4j</groupId>
    <artifactId>slf4j-api</artifactId>
    <version>2.0.16</version>
</dependency>
```
{% endcode %}

### Create the System.Logger Adapter

Create the adapter that implements `System.Logger` and delegates to SLF4J:

{% code title="Slf4jSystemLoggerAdapter.java" %}
```java
import org.slf4j.Logger;

import java.text.MessageFormat;
import java.util.ResourceBundle;

public class Slf4jSystemLoggerAdapter implements System.Logger {

    private final Logger slf4jLogger;

    public Slf4jSystemLoggerAdapter(Logger slf4jLogger) {
        this.slf4jLogger = slf4jLogger;
    }

    @Override
    public String getName() {
        return slf4jLogger.getName();
    }

    @Override
    public boolean isLoggable(Level level) {
        return switch (level) {
            case TRACE -> slf4jLogger.isTraceEnabled();
            case DEBUG -> slf4jLogger.isDebugEnabled();
            case INFO -> slf4jLogger.isInfoEnabled();
            case WARNING -> slf4jLogger.isWarnEnabled();
            case ERROR -> slf4jLogger.isErrorEnabled();
            default -> slf4jLogger.isInfoEnabled();
        };
    }

    @Override
    public void log(Level level, ResourceBundle bundle, String msg, Throwable thrown) {
        switch (level) {
            case TRACE -> slf4jLogger.trace(msg, thrown);
            case DEBUG -> slf4jLogger.debug(msg, thrown);
            case INFO -> slf4jLogger.info(msg, thrown);
            case WARNING -> slf4jLogger.warn(msg, thrown);
            case ERROR -> slf4jLogger.error(msg, thrown);
            default -> slf4jLogger.info(msg, thrown);
        }
    }

    @Override
    public void log(Level level, ResourceBundle bundle, String format, Object... params) {
        String msg = (params != null && params.length > 0)
                ? MessageFormat.format(format, params)
                : format;

        switch (level) {
            case TRACE -> slf4jLogger.trace(msg);
            case DEBUG -> slf4jLogger.debug(msg);
            case INFO -> slf4jLogger.info(msg);
            case WARNING -> slf4jLogger.warn(msg);
            case ERROR -> slf4jLogger.error(msg);
            default -> slf4jLogger.info(msg);
        }
    }
}
```
{% endcode %}

`isLoggable()` delegates level checks to the SLF4J logger. The two `log()` overloads handle throwables and format parameters respectively. `MessageFormat.format()` applies `{0}`, `{1}` substitution before passing the message to SLF4J.

### Create the LoggerFactory

{% code title="Slf4jLoggerFactory.java" %}
```java
import org.apache.ignite.lang.LoggerFactory;

public class Slf4jLoggerFactory implements LoggerFactory {

    @Override
    public System.Logger forName(String name) {
        return new Slf4jSystemLoggerAdapter(
                org.slf4j.LoggerFactory.getLogger(name));
    }
}
```
{% endcode %}

### Pass the Factory to the Client Builder

```java
IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .loggerFactory(new Slf4jLoggerFactory())
        .build();
```

### Configure logback.xml

{% code title="src/main/resources/logback.xml" %}
```xml
<configuration>
    <appender name="CONSOLE" class="ch.qos.logback.core.ConsoleAppender">
        <encoder>
            <pattern>%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n</pattern>
        </encoder>
    </appender>

    <logger name="org.apache.ignite.internal.client" level="DEBUG" additivity="false">
        <appender-ref ref="CONSOLE"/>
    </logger>

    <root level="INFO">
        <appender-ref ref="CONSOLE"/>
    </root>
</configuration>
```
{% endcode %}

`additivity="false"` on the GridGain logger prevents messages from propagating to the root logger. Without it, each client message appears twice.

### Verify Logback Output

Connect to the cluster. Connection events appear at `DEBUG` level:

```text
12:20:18.299 [nioEventLoopGroup-2-1] DEBUG o.a.i.i.client.TcpClientChannel - Connection established [remoteAddress=127.0.0.1/<unresolved>:10800]
12:20:18.348 [nioEventLoopGroup-2-1] INFO  o.a.i.i.client.TcpClientChannel - Partition assignment change notification received [remoteAddress=127.0.0.1/<unresolved>:10800]
12:20:18.352 [nioEventLoopGroup-2-1] DEBUG o.a.i.i.client.TcpClientChannel - Connection closed [remoteAddress=127.0.0.1/<unresolved>:10800]
```

The abbreviated logger name `o.a.i.i.client.TcpClientChannel` corresponds to `org.apache.ignite.internal.client.TcpClientChannel`. The `%logger{36}` pattern shortens package segments to fit within 36 characters.

{% hint style="success" %}
**Checkpoint:**
A `DEBUG ... TcpClientChannel - Connection established` message appears in the console output. If no output appears, verify that the `Slf4jLoggerFactory` is passed to the client builder and that `logback.xml` is on the classpath.
{% endhint %}

## Configure Log4j2

The `log4j-jpl` module bridges `System.Logger` to Log4j2 automatically via `ServiceLoader`. No custom adapter or factory class is needed.

### Add Log4j2 Dependencies

{% code title="pom.xml" %}
```xml
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-api</artifactId>
    <version>2.24.3</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-core</artifactId>
    <version>2.24.3</version>
</dependency>
<dependency>
    <groupId>org.apache.logging.log4j</groupId>
    <artifactId>log4j-jpl</artifactId>
    <version>2.24.3</version>
</dependency>
```
{% endcode %}

`log4j-jpl` registers a `System.LoggerFinder` via `META-INF/services`. The JVM discovers it on the first call to `System.getLogger()` and routes all `System.Logger` output to Log4j2.

### Build the Client

The standard builder uses `System.Logger` internally, and `log4j-jpl` intercepts it:

```java
IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .build();
```

### Configure log4j2.xml

{% code title="src/main/resources/log4j2.xml" %}
```xml
<?xml version="1.0" encoding="UTF-8"?>
<Configuration status="WARN">
    <Appenders>
        <Console name="Console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n"/>
        </Console>
    </Appenders>
    <Loggers>
        <Logger name="org.apache.ignite.internal.client" level="DEBUG" additivity="false">
            <AppenderRef ref="Console"/>
        </Logger>
        <Root level="INFO">
            <AppenderRef ref="Console"/>
        </Root>
    </Loggers>
</Configuration>
```
{% endcode %}

The `status="WARN"` attribute on `<Configuration>` controls Log4j2's own internal logging. The GridGain client logger is set to `DEBUG` with `additivity="false"` to prevent duplicate output through the root logger.

### Verify Log4j2 Output

Connect to the cluster. Connection events appear at `DEBUG` level:

```text
12:19:49.199 [nioEventLoopGroup-2-1] DEBUG org.apache.ignite.internal.client.TcpClientChannel - Connection established [remoteAddress=127.0.0.1/<unresolved>:10800]
12:19:49.260 [nioEventLoopGroup-2-1] INFO  org.apache.ignite.internal.client.TcpClientChannel - Partition assignment change notification received [remoteAddress=127.0.0.1/<unresolved>:10800]
12:19:49.265 [nioEventLoopGroup-2-1] DEBUG org.apache.ignite.internal.client.TcpClientChannel - Connection closed [remoteAddress=127.0.0.1/<unresolved>:10800]
```

The full class name `org.apache.ignite.internal.client.TcpClientChannel` appears because the name fits within the `%logger{36}` width limit. The output format matches the `PatternLayout` in `log4j2.xml`.

{% hint style="success" %}
**Checkpoint:**
A `DEBUG ... TcpClientChannel - Connection established` message appears in the console output. If no output appears, verify that `log4j-jpl` is on the classpath and that `log4j2.xml` is in `src/main/resources/`.
{% endhint %}

## Log Categories

The client creates loggers from fully qualified class names. Use these names in your logging configuration to control verbosity per component:

| Category | What it logs |
|----------|-------------|
| `org.apache.ignite.internal.client.TcpClientChannel` | Connection establishment, heartbeats, request/response cycles |
| `org.apache.ignite.internal.client.ReliableChannel` | Failover decisions, retry attempts, channel selection |
| `org.apache.ignite.internal.client.sql.ClientSql` | SQL query execution, partition awareness routing |
| `org.apache.ignite.internal.client.table.ClientTable` | Table operations, schema version management |
| `org.apache.ignite.internal.streamer.StreamerSubscriber` | Bulk data streaming, batch processing (this category is outside the `org.apache.ignite.internal.client` parent) |
| `org.apache.ignite.internal.client.ClientTimeoutWorker` | Operation timeout detection and handling |

The parent category `org.apache.ignite.internal.client` controls the client logging categories that start with that prefix with a single entry. Data streamer logging is configured separately, through the streamer category above. Use the specific categories above to enable verbose logging for one component without increasing output from the others.

## Production Recommendations

Set the client logger to `WARN` (`WARNING` in JUL) in production. Connection failures, heartbeat timeouts, and handshake errors appear at `WARN` level; per-request output does not.

**Logback:**

```xml
<logger name="org.apache.ignite.internal.client" level="WARN" additivity="false">
```

**Log4j2:**

```xml
<Logger name="org.apache.ignite.internal.client" level="WARN" additivity="false">
```

**java.util.logging:**

```properties
org.apache.ignite.internal.client.level = WARNING
```

Enable `DEBUG` (`FINE` in JUL) temporarily to troubleshoot connection or failover issues. `TRACE` (`FINER` in JUL) logs every outbound request with operation code and destination address; use it only for short diagnostic sessions.

## Troubleshooting

<details>

<summary>No log output appears</summary>

The client connects and operates normally, but no log messages appear in the console or log file.

**JUL:** Both the logger level and the handler level must be set. A logger set to `FINE` with a handler still at `INFO` produces no `FINE`-level output. Set both:

```properties
org.apache.ignite.internal.client.level = FINE
java.util.logging.ConsoleHandler.level = FINE
```

**Logback/Log4j2:** Verify that the configuration file is on the classpath (`src/main/resources/`). Verify that the logger name matches exactly: `org.apache.ignite.internal.client`.

**Logback only:** Verify that the `Slf4jLoggerFactory` is passed to the client builder. Without it, the client uses JUL regardless of the Logback configuration.

</details>

<details>

<summary>"Bad level" exception at startup</summary>

`IllegalArgumentException: Bad level "DEBUG"` when loading `logging.properties`.

Replace the SLF4J/Log4j2 level name with the JUL equivalent. `DEBUG` becomes `FINE`, `TRACE` becomes `FINER`, `ERROR` becomes `SEVERE`, and `WARN` becomes `WARNING`.

</details>

<details>

<summary>Logs appear on console but not in file</summary>

Console output shows client log messages, but the expected log file is empty or missing.

**JUL:** Add the file handler to the `handlers` property and verify that the application has write permission to the target directory:

```properties
handlers = java.util.logging.ConsoleHandler, java.util.logging.FileHandler
java.util.logging.FileHandler.pattern = %h/ignite-client%u.log
java.util.logging.FileHandler.level = FINE
```

The `%h` token resolves to the user home directory. The `%u` token adds a unique number to prevent file conflicts when multiple JVMs run simultaneously.

**Logback/Log4j2:** Add a file appender to the GridGain logger in the configuration file and verify the log directory exists.

</details>

<details>

<summary>Duplicate log messages</summary>

Each client log message appears twice in the console output.

**Logback:** Set `additivity="false"` on the GridGain logger. Without this attribute, messages propagate to the root logger and appear from both the GridGain appender and the root appender.

```xml
<logger name="org.apache.ignite.internal.client" level="DEBUG" additivity="false">
```

**Log4j2:** The same fix applies with Log4j2's capitalized element name:

```xml
<Logger name="org.apache.ignite.internal.client" level="DEBUG" additivity="false">
```

</details>

## Related

- [How to Start a Cluster with Docker Compose](../gridgain9-management/installation/start-cluster-docker-compose.md) - Set up the 3-node development cluster used to verify logging output.
