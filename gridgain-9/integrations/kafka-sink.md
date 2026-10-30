---
description: >-
  Import Kafka topic data into GridGain 9 tables with the GridGain Kafka Sink
  Connector — configuration, topic mapping, type conversion, and streamer
  receivers.
---

# Kafka Sink Connector

Kafka Sink Connector integrates Kafka with GridGain 9, exporting topic data into GridGain tables.

{% hint style="info" %}
Kafka Sink for GridGain 9 is a different connector from GridGain 8 Kafka Connector and requires different configuration.
{% endhint %}

## Guarantees

GridGain Kafka sink provides the following guarantees:

- At least once delivery.
- Automatic failover and reconnection to GridGain cluster.
- Message order within the same GridGain partition is preserved. Message order across different partitions is not defined.

## Compatibility

GridGain Kafka Sink Connector is compatible with Kafka 3.9 and 4.0. Support for earlier Kafka versions may be limited. Earlier versions may have [limited functionality](https://kafka.apache.org/40/documentation.html#upgrade_400_notable_connect).

## Kafka Sink Configuration

### Installation

Download the Kafka Sink connector from the provided link (packaged together with the [Kafka Source connector](kafka-source.md)) and install it following the [recommended procedure for manual installation](https://docs.confluent.io/platform/current/connect/install.html#install-a-connector-manually).

### Configuration

GridGain Kafka sink connector uses the standard Kafka configuration file to define configuration properties.

Below is the example of the configuration file:

```properties
name=gridgain-kafka-connect-sink
topics=topic1,topic2,topic3
connector.class=org.gridgain.kafka.sink.GridGainSinkConnector
tasks.max=1

ignite.addresses=host1:10800,host2:10800
ignite.operationTimeout=30000

ignite.table.name.regex=^events$
ignite.table.name.regex.replacement=Events
ignite.table.name.regex.1=.*
ignite.table.name.regex.replacement.1=UserEvents

unmapped.field.policy=FAIL
drop.key.fields=sampleKey
drop.value.fields=sampleValue
```

|Parameter|Description|Default value|
|---|---|---|
|name|The name of GridGain kafka connector.||
|topics|The list of topics that will be copied to GridGain.||
|connector.class|The class name of the GridGain Sink connector.||
|tasks.max|The maximum number of sink tasks running in parallel.||
|retry.backoff|The period of time before retrying the request, in milliseconds.|3000|
|nested.struct.mode|How nested STRUCT fields are handled. Possible values are: `CONCAT`, `FLATTEN`, `IGNORE`, `DISALLOW`.|CONCAT (separator defined in `nested.struct.concat.separator`)|
|nested.struct.concat.separator|The separator that is used to concatenate nested field names into Ignite column name when `nested.struct.mode` is set to `CONCAT`. For example, if separator is `_` and nested field is `address.street`, the column name will be `address_street`.|Underscore symbol (`_`)|
|flush.mode|Flush mode. Possible values are: `KAFKA` - Kafka decides when to flush, based on `offset.flush.interval.ms` configuration, `ON_PUT` - flush on every put. This causes more frequent flushes and may affect performance.|`KAFKA`|
|ignite.addresses|Required. Addresses of the GridGain nodes the data will be sent to.||
|ignite.authenticator.basic.password|Password for basic authentication to the GridGain cluster.||
|ignite.authenticator.basic.username|Username for basic authentication to the GridGain cluster.||
|ignite.background.reconnect.interval|Background reconnect interval in milliseconds. Set to 0 to disable background reconnect.||
|ignite.connect.timeout|Socket connection timeout, in milliseconds.|5000|
|ignite.error.handling.policy|Error handling policy. Supported values: `LOG_ONLY` - the entry will be skipped while writing the error to the log. `STOP_TASK` - the task will be stopped when the error happens. `DEAD_LETTER_QUEUE` - problematic records will be redirected to the configured Dead Letter Queue topic without stopping the processing.|`LOG_ONLY`|
|ignite.heartbeat.interval|An interval at which the client sends heartbeat messages to the cluster, in milliseconds. 0 disables heartbeats.|1000|
|ignite.heartbeat.timeout|Heartbeat response timeout, in milliseconds. The connection is closed if the response is not received before the timeout occurs.|5000|
|ignite.reconnect.interval|Reconnect interval, in milliseconds. 0 disables background reconnects.|30_000|
|ignite.ssl.client.authentication.mode|Client authentication mode: `NONE`, `OPTIONAL`, or `REQUIRE`.|`NONE`|
|ignite.ssl.ciphers|Comma-separated list of ciphers to be used to set up the SSL connection.||
|ignite.ssl.enabled|If true, an SSL/TLS connection is established.||
|ignite.ssl.key.store.password|Keystore password to be used to set up the SSL connection.||
|ignite.ssl.key.store.path|Keystore path to be used to set up the SSL connection.||
|ignite.ssl.trust.store.password|Truststore password to be used to set up the SSL connection.||
|ignite.ssl.trust.store.path|Truststore path to be used to set up the SSL connection.||
|ignite.streamer.auto.flush.interval|Ignite data streamer's auto-flush interval. The interval, in milliseconds, after which the data streamer will automatically flush the data to the cluster.|5000|
|ignite.streamer.page.size|Ignite data streamer's page size. The number of entries that will be sent to the cluster per network call.|1000|
|ignite.streamer.parallel.ops|Ignite data streamer's parallel operations. The number of parallel operations per partition. Defines how many in-flight requests can be active per partition.|1|
|ignite.streamer.retry.limit|Ignite data streamer's retry limit. The number of retries in case of a connection issue.|16|
|ignite.streamer.receiver.class.name|Specifies the fully qualified class name of the custom receiver to use with the streamer. The receiver must implement `DataStreamerReceiver<Tuple, Tuple, Void>` to ensure proper integration with the connector||
|ignite.streamer.receiver.deployment.units|Accepts a comma-separated list of deployment units in the format `name:version`. Use this property together with the `ignite.streamer.receiver.class.name` for the system to be able to find your receiver.||
|ignite.table.name.regex|The regular expression pattern that will be replaced in the topic name. See the examples below for how to use regular expressions.||
|ignite.table.name.regex.replacement|The value regular expression match will be replaced by.||
|ignite.table.name.regex.1|Optional ordering for regular expressions. Expressions with lower number will be applied first.||
|ignite.table.name.regex.replacement.1|Optional ordering for regular expressions. Expressions with lower number will be applied first.||
|unmapped.field.policy|If set to `FAIL`, the sink will fail when a field without mapping is found. If set to `IGNORE`, the missing field will be skipped and replication will continue.|FAIL|
|drop.key.fields|A comma-separated list of fields to ignore from the key part of the Kafka record. Use `*` to drop the entire key. Nested fields can be specified using dot notation, for example, `address.street`.||
|drop.value.fields|A comma-separated list of fields to ignore from the value part of the Kafka record. Use `*` to drop the entire value. Nested fields can be specified using dot notation, for example, `address.street`.||

### Incoming Data Transformation

To apply changes to incoming data, you can use Kafka Single Message Transformations (SMTs) that allow you to modify messages as they flow through the connector. They let you convert field types, rename or remove fields, flatten nested structures, filter values, and more.

For detailed options and examples, please refer to the official SMT [documentation](https://www.confluent.io/blog/kafka-connect-single-message-transformation-tutorial-with-examples/).

For more advanced transformations beyond SMTs, see the *Streamer Receiver* section.

### Streamer Receiver

Streamer Receiver functionality allows you to process incoming Kafka data with your own custom logic, implemented in Java, and deployed to GridGain cluster.

You can specify the deployment unit containing your receiver via `ignite.streamer.receiver.deployment.units` parameter along with `ignite.streamer.receiver.class.name`. If you decide to use a receiver, add these parameters to your [connector configuration](#configuration) and define your deployment units and receiver name:

```properties
ignite.streamer.receiver.class.name=com.mycompany.MyReceiver
ignite.streamer.receiver.deployment.units=moduleOne:1.0,moduleTwo:2.0
```

If no deployment unit is specified, the receiver class may not be found on the server. The connector forwards the configuration to the streamer regardless, but to deploy a component in the cluster, it must be included in a deployment unit for the system to know where to look for the receiver class.

Keep in mind that a single receiver is used for the entire connector, which means the same receiver processes all topics defined in the connector. If you require different processing logic for different topics, you should either create separate connectors or implement topic-specific checks within your receiver’s code.

{% hint style="info" %}
Your receiver must implement `DataStreamerReceiver<Tuple, Tuple, Void>` interface. Receiver argument is a `Tuple` with additional information, such as Kafka topic name and GridGain table name.
{% endhint %}

Below is an example of a simple receiver implementation:

```java
/**
 * Simple receiver that stores incoming data as string in the table.
 * Target table must have key, val and topic columns:
 * CREATE TABLE testReceiverBasic (key BIGINT PRIMARY KEY, val VARCHAR, topic VARCHAR).
 */
class ToStringReceiver implements DataStreamerReceiver<Tuple, Tuple, Void> {
    @Override
    @Nullable
    public CompletableFuture<List<Void>> receive(List<Tuple> page, DataStreamerReceiverContext ctx, @Nullable Tuple arg) {
        // "topic" and "table" parameters are provided by the GridGain Sink Connector.
        String topicName = arg.stringValue("topic");
        String tableName = arg.stringValue("table");

        Table table = ctx.ignite().tables().table(tableName);

        for (Tuple kafkaRecord : page) {
            Tuple ggRow = Tuple.create()
                    .set("key", kafkaRecord.longValue("key"))
                    .set("val", kafkaRecord.toString())
                    .set("topic", topicName);

            table.recordView().upsert(null, ggRow);
        }

        return null;
    }
}
```

### Kafka Topic Mapping

When applying regular expressions to map Kafka topics to GridGain tables, Kafka Sink applies only the first regular expression that returns matches.

In the example below, any text in Kafka topic will be replaced by MyTable:

```properties
ignite.table.name.regex=.*
ignite.table.name.regex.replacement=MyTable
```

You can use standard regular expression substitution syntax. The example below will replace `topic` with `table` while maintaining the number:

```properties
ignite.table.name.regex=topic-(\d*)
ignite.table.name.regex.replacement=table-$1
```

Multiple regular expressions can be used to handle different topic names. The example below first tries to match `topic-(\d*)`, and if no matches are found in topic name, tries to use the `customer-(\d)` expression.

```properties
ignite.table.name.regex=topic-(\d*)
ignite.table.name.regex.replacement=table-$1

ignite.table.name.regex.1=customer-(\d)
ignite.table.name.regex.replacement.2=from-$1
```

## GridGain Configuration

On the receiving GridGain cluster, you need to manually create tables and schemas that match the data from your Kafka topics. Tables are not created automatically, and failure to have the correct table available will cause an error.

## Type Conversion

GridGain Kafka Sink Connector uses the schema of the GridGain table to convert Kafka topic messages. For example, when GridGain column has the `INT32` type, we expect Kafka data to have the `INT8`, `INT16`, `INT32`, or `INT64` data type.

Full list of supported conversions is provided below:

|GridGain Type|Kafka Type|
|---|---|
|INT8|INT8, INT16, INT32, INT64|
|INT16|INT8, INT16, INT32, INT64|
|INT32|INT8, INT16, INT32, INT64|
|INT64|INT8, INT16, INT32, INT64|
|FLOAT|FLOAT, DOUBLE|
|DOUBLE|FLOAT, DOUBLE|
|DATE|STRING, ARRAY|
|TIME|STRING, ARRAY|
|DATETIME|STRING, ARRAY, LONG|
|TIMESTAMP|STRING, ARRAY, DOUBLE|
|UUID|STRING|
|BYTE_ARRAY|STRING, ARRAY, BYTES|
|DECIMAL|STRING, LONG, FLOAT, DOUBLE|

Those conversions have been tested for all standard serializers and deserializers:

- Json
- Json with schema
- Avro
- Protobuf
