---
description: >-
  Streaming extension modules from the Apache Ignite Extensions project that can
  be used with GridGain 8 to push data to or pull data from external data
  sources.
---

# Apache Ignite Extensions

You can use extensions designed for Apache Ignite with GridGain without extra work. The following streaming extension modules can be used with GridGain:

| Extension | Version |
|---|---|
| [Camel Streamer](https://ignite.apache.org/docs/extensions/camel/camel-streamer) | 1.0.0 |
| [Flink Streamer](https://ignite.apache.org/docs/extensions/flink/flink-streamer) | 1.0.0 |
| [Flume Sink](https://ignite.apache.org/docs/extensions/flume/flume-sink) | 1.0.0 |
| [Ignite ML](https://github.com/apache/ignite-extensions/tree/master/modules/ml-ext) | 1.0.0 |
| [JMS Streamer](https://ignite.apache.org/docs/extensions/jms/jms-streamer) | 1.0.0 |
| [Kafka Streamer](https://ignite.apache.org/docs/extensions/kafka/kafka-streamer) | 1.0.0 |
| [MQTT Streamer](https://ignite.apache.org/docs/extensions/mqtt/mqtt-streamer) | 1.0.0 |
| [Pub Sub](https://ignite.apache.org/docs/extensions/pub-sub/pub-sub) | 1.0.0 |
| [RocketMQ Streamer](https://ignite.apache.org/docs/extensions/rocketmq/rocketmq-streamer) | 1.0.0 |
| [Spark](https://ignite.apache.org/docs/latest/extensions-and-integrations/ignite-for-spark/overview) 3.2 and 2.4 | 3.0.0 |
| [Spring Boot](https://ignite.apache.org/docs/extensions/spring/spring-boot) | 1.0.0 |
| [Spring Data](https://ignite.apache.org/docs/extensions/spring/spring-data) | 2.0.0 |
| [Spring Data](https://ignite.apache.org/docs/extensions/spring/spring-data) 2.0 | 1.0.0 |
| [Spring Data](https://ignite.apache.org/docs/extensions/spring/spring-data) 2.2 | 1.0.0 |
| [Twitter Streamer](https://ignite.apache.org/docs/extensions/twitter/twitter-streamer) | 1.0.0 |
| [ZeroMQ Streamer](https://ignite.apache.org/docs/extensions/zeromq/zeromq-streamer) | 1.0.0 |

The main purpose of streaming extension modules is the ability to push data to or pull data from the corresponding data sources.

These modules are not part of the GridGain release but available as open-source code in the [Apache Ignite Extensions repository](https://github.com/apache/ignite-extensions).

Binaries are available in Maven Repository. For example, the following snippet should be added to `pom.xml` file in order to add the Kafka Streamer to a project:

```xml
<dependency>
    <groupId>org.apache.ignite</groupId>
    <artifactId>ignite-kafka</artifactId>
    <version>2.9.0</version>
</dependency>
```

Binaries must be available to a GridGain node at runtime. It could be achieved by copying the corresponding `jar`-files to the `libs` folder of the GridGain distribution directory.
