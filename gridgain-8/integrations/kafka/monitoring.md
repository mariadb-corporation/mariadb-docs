---
description: >-
  Describes GridGain Kafka Connector logging, the event IDs and recommended actions, and how exceptions are handled by Kafka Connect.
---

# Kafka Connector Monitoring

## Logging

GridGain Kafka Connector logs operationally significant events using Log4j. The Connector package does not include the `log4j.properties` and `log4j.xml` configuration files - you need to provide your own configuration. By default, Log4j looks for a configuration file in the classpath. You can also specify the full path of the configuration file with this system property: `-Dlog4j.configuration=path/to/log4j-configuration-file`.

Every Connector log message starts from a numeric event ID delimited from the rest of the message with the `#` sign. For example:

`15000 # Spring XML configuration path is invalid: /invalid/path/ignite.xml`

The Event ID uniquely identifies a problem and the logged event category indicates the event severity:

**ERROR**: a critical error occurred and the Connector is completely non-operational.

**WARNING**: the Connector's health is degraded.

**INFO**: the Connector is fully operational, the event was logged for informational purposes only.

| Event ID | Severity | Description | Action |
|---|---|---|---|
| 15000 | ERROR | Source or Sink Connector misconfiguration | Analyse error details, fix connector configuration, restart connector. |
| 15001 | INFO | Source or Sink connector changed or ignored some configuration to start successfully. | Consider changing connector configuration as described in the message. |
| 15010 | ERROR | Sink connector failed to build Ignite object: the data was not streamed into sink Ignite cache. | Analyse error details.<br>Contact GridGain if enhancing Sink connector is needed. |
| 15011 | WARNING | Source connector failed to build Kafka schema: schema-less data was streamed into Kafka. | Analyse error details.<br>Contact GridGain if enhancing Source connector is needed. |
| 15020 | ERROR | Source connector Backlog infrastructure failure. | Source connector restart or Backlog cleanup might be needed depending on the error details. |
| 15030 | WARNING | Source connector continuous query failed.<br>Source connector will be re-trying the operation. | Analyse error details.<br>Something maybe wrong with source Ignite grid. |
| 15040 | WARNING | Sink connector failed to write data into sink cache.<br>Sink connector will be re-trying the operation. | Analyse error details.<br>Something maybe wrong with sink Ignite grid. |
| 15050 | ERROR | Source or Sink connector failed to instantiate custom data filter. | Make sure Custom data filter JAR is on the Kafka CLASSPATH. |
| 15051 | ERROR | Exception thrown from custom data filter. | Review and fix the custom data filter implementation. |
| 15060 | INFO | Source or Sink connector connected to Ignite grid. | |
| 15061 | INFO | Source or Sink connector disconnected from Ignite grid. | |
| 15070 | ERROR | Ignite Binary Converter failed to convert data to (for Source connector) or from (for Sink Connector) Kafka format. | Analyse error details.<br>Contact GridGain if enhancing Ignite Binary Converter is needed. |

## Exception Handling

GridGain Kafka Connector's lifetime is managed by the Kafka Connect framework.

The Connector converts all caught exceptions to [Kafka Errors](https://kafka.apache.org/0100/javadoc/org/apache/kafka/connect/errors/package-summary.html). The framework would either retry the operation or restart the Connector depending on the error.
