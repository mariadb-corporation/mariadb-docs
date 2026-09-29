---
description: >-
  Export GridGain 9 table data to Kafka topics with the GridGain Kafka Source
  Connector — configuration, topic mapping, and type conversion.
---

# Kafka Source Connector

The Kafka Source connector enables exporting data from GridGain 9 tables to Kafka topics.

{% hint style="info" %}
Kafka Source for GridGain 9 is a different connector from GridGain 8 Kafka Connector and requires different configuration.
{% endhint %}

## Guarantees

The Kafka Source connector guarantees "at least once" delivery of every table row update.

## Compatibility

GridGain Kafka Sink Connector is compatible with Kafka 3.9 and 4.0. Support for earlier Kafka versions may be limited. Earlier versions may have [limited functionality](https://kafka.apache.org/40/documentation.html#upgrade_400_notable_connect).

## Installation

Download the Kafka Source connector from the provided link (packaged together with the [Kafka Sink connector](kafka-sink.md)) and install it following the [recommended procedure for manual installation](https://docs.confluent.io/platform/current/connect/install.html#install-a-connector-manually).

## Configuration

Configure the following parameters for the Kafka Source connector.

|Parameter|Description|Default value|
|---|---|---|
|name|Required. The name of the Kafka Source connector.||
|connector.class|Required. The class name of the Kafka Source connector. Should be `org.gridgain.kafka.source.GridGainSourceConnector`.||
|ignite.tables|Required. Comma-separated list of names of the GridGain tables to export the data from.||
|ignite.addresses|Required. Comma-separated list of GridGain server addresses (client endpoints).||
|date.mode|Conversion mode for DATE columns: `INT32_ARRAY`, `STRING`, or `KAFKA_DATE`.||
|datetime.mode|Conversion mode for DATETIME columns: `INT32_ARRAY`, `STRING`, or `KAFKA_TIMESTAMP`.||
|ignite.authenticator.basic.password|Password for basic authentication to the GridGain cluster.||
|ignite.authenticator.basic.username|Username for basic authentication to the GridGain cluster.||
|ignite.background.reconnect.interval|Background reconnect interval in milliseconds. Set to 0 to disable background reconnect.||
|ignite.connect.timeout|Socket connection timeout, in milliseconds.|5000|
|ignite.heartbeat.interval|An interval at which the client sends heartbeat messages to the cluster, in milliseconds. 0 disables heartbeats.|1000|
|ignite.heartbeat.timeout|Heartbeat response timeout, in milliseconds. The connection is closed if the response is not received before the timeout occurs.|5000|
|ignite.query.page.size|The number of entries to be fetched from the cluster in one network call.||
|ignite.query.prefetch.pages|The number of query pages to be requested before Kafka demands to reduce idling.||
|ignite.ssl.ciphers|Comma-separated list of ciphers to be used to set up the SSL connection.||
|ignite.ssl.clientAuthenticationMode|Client authentication mode: `NONE`, `OPTIONAL`, or `REQUIRE`.|`NONE`|
|ignite.ssl.enabled|If true, an SSL/TLS connection is established.||
|ignite.ssl.key.store.password|Keystore password to be used to set up the SSL connection.||
|ignite.ssl.key.store.path|Keystore path to be used to set up the SSL connection.||
|ignite.ssl.trust.store.password|Truststore password to be used to set up the SSL connection.||
|ignite.ssl.trust.store.path|Truststore path to be used to set up the SSL connection.||
|ignite.table.name.regex|The regular expression pattern that will be replaced in the topic name. See the examples below for how to use regular expressions.||
|ignite.table.name.regex.replacement|The value regular expression match will be replaced by.||
|ignite.table.name.regex.1|Optional ordering for regular expressions. Expressions with lower number will be applied first.||
|ignite.table.name.regex.replacement.1|Optional ordering for regular expressions. Expressions with lower number will be applied first.||
|poll.interval|The data polling interval in milliseconds.||
|schema.cache.max.size|The maximum number of GridGain-Kafka schema pairs to cache.||
|tasks.max|The maximum number of source tasks running in parallel.||
|time.mode|Conversion mode for TIME columns: `INT32_ARRAY`, `STRING`, or `KAFKA_TIME`.||
|timestamp.mode|Conversion mode for TIMESTAMP columns: `FLOAT64`, `INT64`, `STRING`, or `KAFKA_TIMESTAMP`.||

## Kafka Topic Mapping

By default, a GridGain table name is used as a target Kafka topic name. You can use regular expressions to implement custom table/topic mapping rules.

When applying regular expressions to map GridGain tables to Kafka topics, Kafka Source applies only the first regular expression that returns matches.

In the example below, any text in the GridGain table will be replaced with `MyTable`:

```properties
ignite.table.name.regex=.*
ignite.table.name.regex.replacement=MyTable
```

You can use standard regular expression substitution syntax. The example below will replace `topic` with `table` while maintaining the number:

```properties
ignite.table.name.regex=topic-(\d*)
ignite.table.name.regex.replacement=table-$1
```

Multiple regular expressions can be used to handle different table names. The example below first tries to match `topic-(\d*)`, and if no matches are found in topic name, tries to use the `customer-(\d)` expression.

```properties
ignite.table.name.regex=topic-(\d*)
ignite.table.name.regex.replacement=table-$1

ignite.table.name.regex.1=customer-(\d)
ignite.table.name.regex.replacement.2=from-$1
```

## Utilization

1. In GridGain, create tables with the names specified in `gridgain-kafka-connect-source.properties`.
2. Add the connector binaries to your Kafka installation.
3. Run Kafka.
4. Start adding data to the specified GridGain tables.
5. Verify that the data you have added appears in the corresponding Kafka topics.

## Type Conversion

The Kafka Source connector generates Kafka schemas according to the following data type conversion rules:

|GridGain Type|Kafka Type|
|---|---|
|BOOLEAN|BOOLEAN|
|INT8|INT8|
|INT16|INT16|
|INT32|INT32|
|INT64|INT64|
|FLOAT|FLOAT32|
|DOUBLE|FLOAT64|
|BYTE_ARRAY|BYTES|
|DECIMAL|STRING|
|DATE|ARRAY, STRING, or INT32, depending on `date.mode`|
|TIME|ARRAY, STRING, or INT32, depending on `time.mode`|
|DATETIME|ARRAY or STRING or INT64, depending on `datetime.mode`|
|TIMESTAMP|FLOAT64, INT64, or STRING, depending on `timestamp.mode`|
|UUID|STRING|
|STRING|STRING|

{% hint style="info" %}
For nullable GridGain columns, we use the optional Kafka type.
{% endhint %}

The above data type conversions have been tested for all standard serializers and deserializers:

- JSON
- JSON with schema
- Avro
- Protobuf
