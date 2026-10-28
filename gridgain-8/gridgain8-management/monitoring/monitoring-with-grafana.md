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

Set the JMX port and add the JMX exporter as a Java agent when starting a node:

```shell
export IGNITE_JMX_PORT=45000
export JVM_OPTS="-javaagent:jmx_prometheus_javaagent-0.12.0.jar=8080:config.yaml -DIGNITE_MBEAN_APPEND_CLASS_LOADER_ID=false"
```

{% code title="config.yaml" %}
```yaml
hostPort: 127.0.0.1:45000
ssl: false
lowercaseOutputLabelNames: false
lowercaseOutputName: false
```
{% endcode %}

You can connect to a single node and monitor its global metrics. If you want to monitor every node, add the JMX exporter to each node.
