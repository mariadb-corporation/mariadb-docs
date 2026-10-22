---
description: >-
  Configure monitoring of a GridGain 8 cluster with Grafana and Prometheus, using
  the JMX exporter as a Java agent to expose metrics.
---

# Monitoring with Grafana and Prometheus

This chapter explains how to configure monitoring of a GridGain cluster with Grafana and Prometheus.

## Prerequisites

- Install [Grafana](https://grafana.com/get).
- Install [Prometheus](https://prometheus.io/download/).
- Install the [JMX exporter](https://github.com/prometheus/jmx_exporter).

The JMX exporter runs as a Java agent and exports metrics to the Prometheus server. Grafana then uses the Prometheus server as a data source.

## Configuring Cluster Nodes

Open a JMX port with the standard JVM system properties and add the JMX exporter as a Java agent when starting a node. The GridGain start scripts do not read a JMX port variable, so pass the properties in `JVM_OPTS`:

```shell
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=45000 -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -javaagent:jmx_prometheus_javaagent-0.12.0.jar=8080:config.yaml -DIGNITE_MBEAN_APPEND_CLASS_LOADER_ID=false"
```

These `jmxremote` settings turn off authentication and SSL, so use them only on a trusted network.

{% code title="config.yaml" %}
```yaml
hostPort: 127.0.0.1:45000
ssl: false
lowercaseOutputLabelNames: false
lowercaseOutputName: false
```
{% endcode %}

You can connect to a single node and monitor its global metrics. If you want to monitor every node, add the JMX exporter to each node.

## See Also

- [How to Monitor GridGain 8 With Prometheus and Grafana](prometheus-grafana-step-by-step.md)
- [How to Monitor GridGain Clusters With New Relic](new-relic.md)
