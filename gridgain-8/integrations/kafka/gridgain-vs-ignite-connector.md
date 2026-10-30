---
description: >-
  Compares the open source Apache Ignite Kafka Connector with the GridGain Kafka Connector feature by feature.
---

# GridGain vs. Apache Ignite Kafka Connector

Open source Apache Ignite includes a different Ignite Kafka Connector implementation than GridGain. The table below compares Open Source Ignite and GridGain Kafka Connectors.

| Feature | Apache Ignite Connector | GridGain Connector |
|---|---|---|
| Scalability | **Limited**<br>Source connector is not parallel.<br>Sink connector is parallel. | Source connector creates a task per cache.<br>Sink connector is parallel. |
| At least once processing semantics | **NO**<br>Source data might be lost during connector restart or rebalancing. | **YES**<br>Source connector can be configured to resume from the last committed offset. |
| Exactly once processing semantics | **NO** | **YES** |
| Preserving source data schema | **NO** | **YES** |
| Handling multiple caches | **NO** | **YES**<br>Connector can be configured to handle any number of caches. |
| Dynamic Reconfiguration | **NO** | **YES**<br>Source connector detects added or removed caches and re-configures itself. |
| Initial Data Load | **NO** | **YES** |
| Handling data removals | **YES** | **YES** |
| Serialization and Deserialization of data | **YES** | **YES** |
| Filtering | **Limited**<br>Only source connector supports a filter. | Both source and sink connectors support filters. |
| Transformations | Kafka SMTs | Kafka SMTs |
| DevOps | Some free-text error logging. | Health Model defined. |
| Support | Apache Ignite Community | Supported by GridGain, certified by Confluent. |
| Packaging | Uber JAR | Connector Package |
| Deployment | Plugin PATH on all Kafka Connect workers. | Plugin PATH on all Kafka Connect workers.<br>CLASSPATH on all GridGain nodes. |
| Kafka API Version | 0.10 | 2.0 |
| Source API | Ignite events | Ignite continuous queries |
| Sink API | Ignite data streamer | Ignite data streamer |
