---
description: >-
  Add the GridGain 9 Java client to a project, connect to a cluster,
  authenticate, configure logging, and read client connection metrics.
---

# Java Client

GridGain 9 clients connect to the cluster via a standard socket connection. Unlike GridGain 8, there is no separate Thin and Thick clients in GridGain 9. All clients are 'thin'.

Clients do not become a part of the cluster topology, never hold any data, and are not used as a destination for compute calculations.

## Getting Started

### Prerequisites

{% include "../../../.gitbook/includes/prereqs-java.md" %}

### Installation

Java client can be added to your project by using GridGain maven repository:

- Add GridGain repository to your project:

```
<repositories>
    <repository>
        <id>GridGain External Repository</id>
        <url>https://www.gridgainsystems.com/nexus/content/repositories/external</url>
    </repository>
</repositories>
```

- Add the GridGain client dependency

```xml
<dependency>
    <groupId>org.gridgain</groupId>
    <artifactId>ignite-client</artifactId>
    <version>9.1</version>
</dependency>
```

## Connecting to Cluster

To initialize a client, use the `IgniteClient` class:

{% code title="Java" %}
```java
try (org.apache.ignite.client.IgniteClient client = org.apache.ignite.client.IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .build()
) {
    client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS Person;");
}
```
{% endcode %}

## Authentication

To pass [authentication](../../administrators-guide/security/authentication.md#basic-authentication) information, use the `IgniteClientAuthenticator` class and pass it to `IgniteClient` builder:

{% code title="Java" %}
```java
IgniteClientAuthenticator auth = BasicAuthenticator.builder().username("myUser").password("myPassword").build();

try (IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .authenticator(auth)
        .build()
) {
    client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS Person;");
}
```
{% endcode %}

## Logging

To configure client logging, add `loggerFactory`:

```java
try (IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .loggerFactory(System::getLogger)
        .build()
) {
    client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS Person;");
}
```

The client logs connection errors, reconnects, and retries.

### Limitations

There are limitations to user types that can be used for such a mapping. Some limitations are common, and others are platform-specific due to the programming language used.

- Only flat field structure is supported, meaning no nesting user objects. This is because Ignite tables, and therefore tuples have flat structure themselves;
- Fields should be mapped to Ignite types;
- All fields in user type should either be mapped to Table column or explicitly excluded;
- All columns from Table should be mapped to some field in the user type;
- *Java only*: Users should implement [Mapper](https://www.gridgain.com/sdk/gridgain9/latest/javadoc/org/apache/ignite/table/mapper/package-summary.html) classes for user types for more flexibility;

## Client Metrics

### Java

When running Java client, you need to enable metrics in the client builder:

```java
try (IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .metricsEnabled(true)
        .build()
) {
    client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS Person;");
}
```

After that, client metrics will be available to any Java monitoring tool, for example [JDK Mission Control](https://www.oracle.com/java/technologies/jdk-mission-control.html).

#### Available Java Metrics

| Metric name | Description |
| --- | --- |
| ConnectionsActive | The number of currently active connections. |
| ConnectionsEstablished | The number of established connections. |
| ConnectionsLost | The number of connections lost. |
| ConnectionsLostTimeout | The number of connections lost due to a timeout. |
| HandshakesFailed | The number of failed handshakes. |
| HandshakesFailedTimeout | The number of handshakes that failed due to a timeout. |
| RequestsActive | The number of currently active requests. |
| RequestsSent | The number of requests sent. |
| RequestsCompleted | The number of completed requests. Requests are completed once a response is received. |
| RequestsRetried | The number of request retries. |
| RequestsFailed | The number of failed requests. |
| BytesSent | The amount of bytes sent. |
| BytesReceived | The amount of bytes received. |
| StreamerBatchesSent | The number of data streamer batches sent. |
| StreamerItemsSent | The number of data streamer items sent. |
| StreamerBatchesActive | The number of existing data streamer batches. |
| StreamerItemsQueued | The number of queued data streamer items. |

## Client Connection Configuration

There is a number of configuration properties managing the connection between the client and GridGain cluster:

```java
try (IgniteClient client = IgniteClient.builder()
        .addresses("127.0.0.1:10800")
        .connectTimeout(5000)
        .heartbeatInterval(30000)
        .heartbeatTimeout(5000)
        .operationTimeout(3000)
        .backgroundReconnectInterval(30000)
        .retryPolicy(new RetryLimitPolicy().retryLimit(8))
        .build()
) {
    client.sql().execute(null, "CREATE SEQUENCE IF NOT EXISTS Person;");
}
```

| Configuration name | Description |
| --- | --- |
| connectTimeout | Client connection timeout, in milliseconds. |
| heartbeatInterval | Heartbeat message interval, in milliseconds. |
| heartbeatTimeout | Heartbeat message timeout, in milliseconds. |
| operationTimeout | Operation timeout, in milliseconds. |
| backgroundReconnectInterval | Background reconnect interval, in milliseconds. |
| retryPolicy | Retry policy. By default, all read operations are retried up to 16 times, and write operations are not retried. |
</content>
