---
description: >-
  Configure, run, secure, and monitor the DR connector tool that receives data
  from a GridGain 8 cluster and writes it into GridGain 9 tables.
---

# DR Connector Tool

The DR connector tool receives data from a GridGain 8 cluster via Data Center Replication and writes it into GridGain 9 tables.

## Field Mapping Rules

The following rules are used for mapping values between GridGain 8 caches and GridGain 9 tables:

- Cache key fields are mapped to primary key columns of a target table.
- Cache value fields are mapped to non-primary key columns of a target table.
- If a cache field is not present in the configuration it is mapped to a target table column with the same name.
- By default, a plain-type (non-BinaryObject) key is mapped to a column named `_key` in a target table.
- By default, a plain-type (non-BinaryObject) value is mapped to a column named `_val` in a target table.

## Connector Configuration

Connector configuration files use the HOCON format.

{% hint style="info" %}
When migrating data from GridGain 8 to GridGain 9, it is required to set the `timeZone` parameter to match the original client's local time. If it does not match, the restored values may differ from the originals.
{% endhint %}

```
dr-service-config = {
  cacheMapping = [
    # Mapping for key and value object fields to distinct columns.
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        { field = "key1", column = "C1" }
        { field = "key2", column = "C2" }
        { field = "key3", column = "C3" }
        { field = "key4", column = "ignored_column", ignore = true }
      ]
      valueFields = [
        { field = "value1", column = "C4" }
        { field = "value2", column = "ignored_column", ignore = true }
      ]
    }

#    Alternative mapping via EntryTransformer
#    {
#      cache = "cacheName"
#      table = "schemaName.tableName"
#      transformerFactoryClassName = "somepackage.SomeEntryTransformerFactory"
#    }
  ]

  clientConfiguration = {
    serverEndpoints = [ "127.0.0.1:10800" ]
    port = 10800
    connectTimeout = 0
    metricsEnabled = false
    name = "drClient"
    heartbeatInterval = 30000
    heartbeatTimeout = 5000
    backgroundReconnectInterval = 30000

    ssl = {
      enabled = false
      ciphers = ""
      keyStore = {
        password = ""
        path = ""
        type = "PKCS12"
      }
      trustStore = {
        password = ""
        path = ""
        type = "PKCS12"
      }
    }

    authenticator = {
      type = "BASIC"
      identity = "<user>"
      secret = "<password>"
    }
  }

  drReceiverConfiguration = {
    dataCenterId = 1
    inboundHost = ""
    inboundPort = 49000
    drReceiverMetricsEnabled = true
    idleTimeout = 60000
    ignoreMissingTable = true
    selectorCnt = 4
    socketReceiveBufferSize = 0
    socketSendBufferSize = 0
    tcpNodelay = true
    tombstoneTtl = 1800000
    workerThreads = 10
    writeTimeout = 60000
    ssl = {
      enabled = false
      clientAuth = "none"
      ciphers = ""
      keyStore = {
        password = ""
        path = ""
        type = "PKCS12"
      }
      trustStore = {
        password = ""
        path = ""
        type = "PKCS12"
      }
    }
  }

  timeZone = "Europe/Berlin"
}
```

{% hint style="info" %}
The DR connector treats field names as case-sensitive. To preserve mixed-case column names in GridGain 9, enclose them in double quotes when creating the table. Otherwise GridGain 9 stores identifiers in uppercase, and the connector configuration must reference the uppercase column names.
{% endhint %}

The following fields are available:

| Property | Default | Description |
|---|---|---|
| `cache` | | The name of the GridGain 8 cache on the master cluster. The cache name is case-sensitive and should not include the schema. |
| `table` | | The name of the GridGain 9 table on the replica cluster. Table name is case-insensitive by default, so case-sensitive identifiers must be quoted. This name can include the schema as a prefix, in the format `SCHEMA.TABLE`. If schema is not specified, the default `PUBLIC` schema will be used. |
| `keyFields` | | The array denoting the mapping of cache key fields to table columns. Not compatible with `fields` mapping. |
| `keyFields.field` | | The case-sensitive name of the source cache field to get data from. |
| `keyFields.column` | | The case-sensitive name of the target column to write data to. |
| `keyFields.ignore` | false | If set to `true`, the key field will be excluded from data migration. `keyFields.column` is still required for correct migration, but is ignored. |
| `valueFields` | | The array denoting the mapping of cache value fields to table columns. Not compatible with `fields` mapping. |
| `valueFields.field` | | The case-sensitive name of the source cache field to get data from. |
| `valueFields.column` | | The case-sensitive name of the target column to write data to. |
| `valueFields.ignore` | false | If set to `true`, the field is excluded from data migration. `valueFields.column` is still required but is ignored. |
| `fields` | | Alternative configuration. The array denoting the mapping of cache fields to table columns. Not compatible with `keyFields`/`valueFields` mappings. |
| `fields.field` | | Alternative configuration. The case-sensitive name of the source cache field to get data from. |
| `fields.column` | | Alternative configuration. The case-sensitive name of the target column to write data to. |
| `clientConfiguration.serverEndpoints` | | The list of addresses of GridGain 9 nodes with configured client connectors. |
| `clientConfiguration.port` | | The GridGain 9 thin-client port the DR connector connects to. |
| `clientConfiguration.connectTimeout` | | The connection timeout, in milliseconds. |
| `clientConfiguration.metricsEnabled` | | If the metrics are enabled for the connection. |
| `clientConfiguration.name` | | Defines the unique client name. If not specified, generated automatically based on client number in `client_{number}` format. |
| `clientConfiguration.heartbeatInterval` | | Heartbeat message interval, in milliseconds. |
| `clientConfiguration.heartbeatTimeout` | | Heartbeat message timeout, in milliseconds. |
| `clientConfiguration.backgroundReconnectInterval` | | The period of time after which the connector will try to reestablish lost connection, in milliseconds. |
| `clientConfiguration.ssl.enabled` | false | If SSL is enabled for the connection. |
| `clientConfiguration.ssl.ciphers` | | The list of ciphers to enable, separated by comma. |
| `clientConfiguration.ssl.keyStore.type` | PKCS12 | Keystore type. |
| `clientConfiguration.ssl.keyStore.password` | | Keystore password. |
| `clientConfiguration.ssl.keyStore.path` | | Path to the keystore. |
| `clientConfiguration.ssl.trustStore.type` | PKCS12 | Truststore type. |
| `clientConfiguration.ssl.trustStore.password` | | Truststore password. |
| `clientConfiguration.ssl.trustStore.path` | | Path to the truststore. |
| `clientConfiguration.authenticator.type` | | The type of authentication to use (for example, `BASIC`). |
| `clientConfiguration.authenticator.identity` | | The username or identity for authentication. |
| `clientConfiguration.authenticator.secret` | | The password or secret for authentication. |
| `drReceiverConfiguration.dataCenterId` | 1 | The ID of the master GridGain 8 cluster's data center. Only connections from this data center will be allowed. |
| `drReceiverConfiguration.inboundHost` | | Local host name of the connector. |
| `drReceiverConfiguration.inboundPort` | 49000 | The port used for data replication. |
| `drReceiverConfiguration.drReceiverMetricsEnabled` | true | If metrics are enabled. |
| `drReceiverConfiguration.idleTimeout` | 60000 | How long the connector can be idle before the connection is dropped, in milliseconds. |
| `drReceiverConfiguration.ignoreMissingTable` | true | Controls behavior when a target table is missing. If `true`, batches for missing tables are skipped; if `false`, replication fails. |
| `drReceiverConfiguration.selectorCnt` | lowest of 4 and the number of available cores | The number of threads handling connections. |
| `drReceiverConfiguration.socketReceiveBufferSize` | 0 | Socket receive buffer size in bytes. |
| `drReceiverConfiguration.socketSendBufferSize` | 0 | Socket send buffer size in bytes. |
| `drReceiverConfiguration.tcpNodelay` | true | If the `TCP_NODELAY` mode is used. |
| `drReceiverConfiguration.tombstoneTtl` | 1800000 | Tombstone expiration timeout, in milliseconds. |
| `drReceiverConfiguration.workerThreads` | All available threads | The number of worker threads that process batches. |
| `drReceiverConfiguration.writeTimeout` | 60000 | Write timeout for the TCP server connection. |
| `drReceiverConfiguration.ssl.enabled` | false | If SSL is enabled for the connection. |
| `drReceiverConfiguration.ssl.clientAuth` | none | SSL client authentication. Possible values:<br>- `none` - no auth required,<br>- `optional` - the connector will request a certificate, but not fail the connection if none is provided,<br>- `require` - the connector will request a certificate and fail if none is provided. |
| `drReceiverConfiguration.ssl.ciphers` | | The list of ciphers to enable, separated by comma. |
| `drReceiverConfiguration.ssl.keyStore.type` | PKCS12 | Keystore type. |
| `drReceiverConfiguration.ssl.keyStore.password` | | Keystore password. |
| `drReceiverConfiguration.ssl.keyStore.path` | | Path to the keystore. |
| `drReceiverConfiguration.ssl.trustStore.type` | PKCS12 | Truststore type. |
| `drReceiverConfiguration.ssl.trustStore.password` | | Truststore password. |
| `drReceiverConfiguration.ssl.trustStore.path` | | Path to the truststore. |
| `timeZone` | | Specifies the time zone of the data migrated from GridGain 8 to GridGain 9. Set as "Area/City" (for example, "Europe/Berlin") or as a fixed offset like GMT+5 to ensure correct conversion of `TIME`, `DATE`, and `TIMESTAMP` values. |

### Sample Cache Mappings

#### Mapping a Composite Key Cache

The configuration below maps fields K1, K2, K3 of cache key objects to columns COL_1, COL_2, COL_3 of the target table and fields V1, V2, V3 from cache value objects to columns COL_4, COL_5, COL_6 of the target table, and ignoring fields K4 and V4.

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        { field = "K1", column = "COL_1" }
        { field = "K2", column = "COL_2" }
        { field = "K3", column = "COL_3" }
        { field = "K4", column = "ignored_column", ignore = true }
      ]
      valueFields = [
        { field = "V1", column = "COL_4" }
        { field = "V2", column = "COL_5" }
        { field = "V3", column = "COL_6" }
        { field = "V4", column = "ignored_column", ignore = true }
      ]
    }
  ]
}
```

#### Mapping a Plain Type Key Cache

When mapping a cache with a plain type key, it is required to use the `_key` field name to specify the key field.

The example below shows how you can map a plain type key:

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        # This example is valid.
        { field = "_key", column = "ID" }

        # The example below would not work.
        #{ field = "id", column = "ID" }
      ]
      valueFields = [
        { field = "name", column = "NAME" }
        { field = "age", column = "AGE" }
      ]
    }
  ]
}
```

#### Mapping a Plain Type Value Cache

When mapping a cache with a plain type value, it is required to use the `_val` field name to specify the value field.

The example below shows how you can map a plain type value:

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        { field = "USERID", column = "USERID" }
        { field = "CITYID", column = "CITYID" }
      ]
      valueFields = [
        # This example is valid.
        { field = "_val", column = "NAME" }

        # This example would not work
        # { field = "AGE", column = "AGE" }
      ]
    }
  ]
}
```

#### Mapping a Cache With Keys Duplicated in Values

If both the key and one of the values have the same name, you have to ignore one of the fields for the migration to work correctly.

The example below shows how you can ignore the duplicate:

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      keyFields = [
        { field = "_key", column = "ID" }
      ]
      valueFields = [
        { field = "name", column = "NAME" }
        { field = "age", column = "AGE" }
        # Ignore the duplicate.
        { field = "id", column = "", ignore = true }
      ]
    }
  ]
}
```

### Custom Data Transformations

For complex data migration scenarios that cannot be handled by simple field-to-column mapping, the DR connector supports a transformer Java API that can be used to implement custom transformation logic. To implement it, you create the transformer class, package it into a jar and add it to DR connector's classpath.

{% hint style="info" %}
Custom transformer mapping is not compatible with other ways to map your fields.
{% endhint %}

#### Implementing a Transformer Factory

The transformer factory class must be public and contain a static `EntryTransformer create()` method. This method must return an instance of `EntryTransformer` that implements your transformation logic.

Below is a basic example that converts all field values to strings:

```java
package somepackage;

public class StringifyTransformerFactory {

    // This class must exist with this specific name.
    public static EntryTransformer create() {
        return (keyReader, valueReader) -> {
            // Read key fields and convert to strings
            Tuple key = Tuple.create();
            for (String fieldName : keyReader.fieldNames()) {
                Object fieldValue = keyReader.readField(fieldName);
                key.set(fieldName, String.valueOf(fieldValue));
            }

            // Handle deletions - valueReader is null for removed entries
            if (valueReader == null) {
                return Result.remove(key);
            }

            // Read value fields and convert to strings
            Tuple value = Tuple.create();
            for (String fieldName : valueReader.fieldNames()) {
                Object fieldValue = valueReader.readField(fieldName);
                value.set(fieldName, String.valueOf(fieldValue));
            }

            return Result.upsert(key, value);
        };
    }
}
```

##### Handling Results

The `Result` class supports three operation types:

| Type | Description |
|---|---|
| `UPSERT` | Insert or update an entry. Both key and value must be non-null. |
| `REMOVE` | Delete an entry. Only key is required, value is null. |
| `SKIP` | Skip the entry (no operation). Use this to filter out entries. |

##### Handling Binary Objects

The `BinaryObjectReader` interface provides methods to access fields from GridGain 8 binary objects:

- **`typeName()`** - Returns the type name of the binary object
- **`fieldNames()`** - Returns a list of all field names in the object
- **`readField(String name)`** - Reads and returns the value of the specified field

Field values are returned as Java objects and can be null either when the field doesn't exist or when the field value is null.

#### Adding a Custom Data Transformer

To use a custom transformer in your replication, make it available to the connector and set the configuration to use the factory class.

{% hint style="warning" %}
The `transformerFactoryClassName` configuration option is mutually exclusive with `fields`, `keyFields`, and `valueFields`. You must use either field mapping OR a custom transformer, not both.
{% endhint %}

- Add a jar containing the transformer factory class to the DR connector classpath (the `/lib` directory in the DR connector by default). The transformer factory must be implemented as described [above](#implementing-a-transformer-factory).
- Specify the factory class name in your cache mapping configuration using the `transformerFactoryClassName` property:

```
dr-service-config = {
  cacheMapping = [
    {
      cache = "cacheName"
      table = "schemaName.tableName"
      transformerFactoryClassName = "somepackage.StringifyTransformerFactory"
    }
  ]
}
```

## Running the Connector Tool

### Deployment Recommendations

Only one connector instance is supported per replication stream. Do not run multiple connectors for the same cache mapping.

### Running the Tool Locally

To start the connector tool, use the `start.sh` script. You can provide the configuration for the script by using the `config-path` parameter and specifying the path to the [Connector Configuration](#connector-configuration).

```bash
./start.sh --config-path etc/example.conf
```

To pass additional JVM arguments to the connector, such as heap size, set the `EXTRA_JVM_ARGS` environment
variable. The script inherits the variable from the environment, so you do not need to edit `start.sh`:

```bash
export EXTRA_JVM_ARGS="-Xms4g -Xmx4g"
./start.sh --config-path etc/example.conf
```

### Running the Tool in Docker

The connector tool is available on DockerHub.

When running the connector tool in docker, keep in mind the following:

- You need to mount the configuration in your container.

  {% hint style="info" %}
  The configuration file must be editable by the `gridgain` user (user ID in the container is 1001).
  {% endhint %}
- Open the port for connection from your GridGain 8 cluster. This port is specified in the `dr-service-config.drReceiverConfiguration.inboundPort` [Connector Configuration](#connector-configuration) parameter.
- If you run GridGain 9 in a different network, open the port for the connection to that network. GridGain 9 server endpoint is specified in the `dr-service-config.clientConfiguration.serverEndpoints` [Connector Configuration](#connector-configuration) parameter.
- If you are using a [Custom Data Transformer](#adding-a-custom-data-transformer), mount the directory with the jar file, and then use the `EXTRA_CLASSPATH` environment variable to load it.

To start the connector tool, start the container, specifying all required parameters, for example:

```bash
docker run -p {host_port}:{inbound_port} \
  -v /host_config_path:/opt/gridgain-dr-connector/etc/custom \
  -v /host_libs_directory:/opt/custom-libs \
  -e EXTRA_CLASSPATH=/opt/custom-libs \
  gridgain/gridgain-dr-connector:9.1 \
  --config-path /opt/gridgain-dr-connector/etc/custom/config.conf
```

The example above assumes mounts `host_config_path` and `/host_libs_directory` directories that should contain configuration and custom libraries respectively.

You can also use docker compose. Here is the example of the above configuration in docker compose format:

```
services:

  dr-connector:
    container_name: dr-connector
    image: gridgain-dr-connector:9.1
    tty: true
    volumes:
      - /host_config_path:/opt/gridgain-dr-connector/etc/custom
      - /host_libs_directory:/opt/custom-libs
    ports:
      - "{host_port}:{inbound_port}"
    environment:
      - EXTRA_CLASSPATH=/opt/custom-libs
    command: ["--config-path", "/opt/gridgain-dr-connector/etc/custom/config.conf"]
```

Then you can start the docker image with docker compose:

```bash
docker compose up -d
```

## Configuring SSL/TLS Between DR Connector and GridGain 9 Cluster

The default way to configure SSL/TLS is to update the configuration with SSL properties. The example below is in the HOCON format.

```
dr-service-config = {

  clientConfiguration = {
    ssl = {
      enabled = true
      clientAuth = "require"
      ciphers = ""
      keyStore = {
        password = "may be empty"
        path = "must not be empty"
        type = "PKCS12"
      }
      trustStore = {
        password = "may be empty"
        path = "must not be empty"
        type = "PKCS12"
      }
    }
  }
}
```

## Configuring SSL/TLS Between DR Connector and GridGain 8 Cluster

The default way to configure SSL/TLS is to update the configuration with SSL properties. The example below is in the HOCON format.

```
dr-service-config = {
  drReceiverConfiguration = {
    ssl = {
      enabled = true
      clientAuth = "require"
      ciphers = ""
      keyStore = {
        password = "may be empty"
        path = "must not be empty"
        type = "PKCS12"
      }
      trustStore = {
        password = "may be empty"
        path = "must not be empty"
        type = "PKCS12"
      }
    }
  }
}
```

## Monitoring

The DR connector exposes metrics that you can use to monitor replication progress. Metrics are enabled by setting `drReceiverConfiguration.drReceiverMetricsEnabled` to `true` in the [Connector Configuration](#connector-configuration).

Two sets of metrics are available: per-cache metrics and global metrics.

### Per-Cache Metrics

Per-cache metrics (`DrReceiverCacheMetricsMxBean`) are reported separately for each replicated cache. Values are measured over a rolling time window and reset periodically:

| Metric | Description |
|---|---|
| `batchesReceived` | Number of batches received from remote sender hubs. |
| `batchesAcked` | Number of batches processed successfully. |
| `batchesFailed` | Number of batches that produced errors during processing. |
| `entriesReceived` | Number of cache entries received from remote sender hubs. |
| `entriesAcked` | Number of cache entries processed successfully. |
| `bytesReceived` | Total bytes received from remote sender hubs. |
| `messageQueueLength` | Message queue length. |
| `messageQueueSizeBytes` | Message queue size in bytes. |

### Global Metrics

Global metrics (`DrReceiverMxBean`) accumulate values since connector startup:

| Metric | Description |
|---|---|
| `totalBatchesReceived` | Total number of batches received from remote sender hubs since startup. |
| `totalBatchesAcked` | Total number of batches processed successfully since startup. |
| `totalBatchesFailed` | Total number of failed batch processing attempts since startup. |
| `totalEntriesReceived` | Total number of cache entries received from remote sender hubs since startup. |
| `totalEntriesAcked` | Total number of cache entries processed successfully since startup. |
| `totalBytesReceived` | Total bytes received from remote sender hubs since startup. |
| `totalMessageQueueLength` | Total message queue length. |
| `totalMessageQueueSizeBytes` | Total message queue size in bytes. |
| `localInboundHost` | Local host name the receiver hub TCP server is bound to. |
| `localInboundPort` | Local port number of the receiver hub TCP server. |
| `selectorCount` | Number of selector threads in the receiver hub's TCP server. |
| `workerThreads` | Number of server worker threads. |
| `writeTimeout` | Write timeout for sender hub socket connections, in milliseconds. |
| `socketSendBufferSize` | Socket send buffer size, in bytes. |
| `socketReceiveBufferSize` | Socket receive buffer size, in bytes. |
| `tcpNodelay` | Whether the `TCP_NODELAY` flag is enabled for server sockets. |
| `idleTimeout` | Idle timeout for sender hub socket connections, in milliseconds. |
| `tombstoneTtl` | Tombstone expiration timeout, in milliseconds. |

### Logging Configuration

DR connector Tool uses `java.util.logging` for logging. Default configuration file is located in `<dr-connector-directory>/etc/receiver.java.util.logging.properties`.
Default log file is `<dr-connector-directory>/log/dr-receiver-0.log`. Logging is configured to perform periodic log file rotation.

## Stopping the Connector

Once data replication is no longer needed (for example, the load was shifted to GridGain 9 cluster), stop the replication process on the GridGain 8 master cluster and then use the `stop.sh` script to stop the connector.

```bash
./stop.sh
```
