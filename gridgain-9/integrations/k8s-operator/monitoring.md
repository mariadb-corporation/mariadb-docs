---
description: >-
  Expose GridGain 9 cluster metrics through JMX and integrate with Prometheus
  when running clusters with the Kubernetes Operator.
---

# Monitoring

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

The operator supports exposing GridGain cluster metrics through JMX and integrating with Prometheus for collection and alerting.

## JMX Metrics

GridGain exposes internal metrics over JMX. The operator can run a JMX exporter sidecar that converts these metrics into a format that Prometheus can scrape. Enable JMX monitoring through the `jmx` field:

```yaml
spec:
  jmx:
    enabled: true
    port: 9404
```

The `port` field defaults to 9404 and accepts any value between 1 and 65535. The exporter listens on this port and serves metrics in Prometheus exposition format.

### Custom JMX Rules

The `config` field accepts a YAML string that configures the JMX exporter's scraping rules. Use it to select which MBeans are exported and how they are named:

```yaml
spec:
  jmx:
    enabled: true
    port: 9404
    config: |
      lowercaseOutputName: true
      lowercaseOutputLabelNames: true
      rules:
        - pattern: '^java.lang<type=OperatingSystem><>SystemLoadAverage'
          name: os_system_load_average
          help: "System load average"
          type: GAUGE
        - pattern: '^java.lang<type=Memory><HeapMemoryUsage>used'
          name: jvm_memory_heap_used
          help: "JVM heap memory used"
          type: GAUGE
        - pattern: '^java.lang<type=Memory><NonHeapMemoryUsage>used'
          name: jvm_memory_nonheap_used
          help: "JVM non-heap memory used"
          type: GAUGE
        - pattern: '^java.lang<type=GarbageCollector, name=(.*)><>CollectionCount'
          name: jvm_gc_collection_total
          labels:
            gc: "$1"
          type: COUNTER
```

Without a custom `config`, the exporter uses its default rule set, which may export a large number of metrics. Providing explicit rules lets you control the cardinality and relevance of the exported data.

## Prometheus Integration

To make the metrics discoverable by Prometheus, add scrape annotations to the pod template using `podAnnotations`:

```yaml
spec:
  podAnnotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9404"
    prometheus.io/path: "/metrics"
```

These annotations follow the convention used by the Prometheus Kubernetes service discovery configuration. When Prometheus is configured to discover targets by pod annotations, it will automatically start scraping the JMX exporter endpoint on each GridGain pod.

### Exposing Metrics Externally

If you need to access metrics from outside the Kubernetes cluster — for example, from an external Grafana instance — define a service that exposes the JMX port:

```yaml
spec:
  services:
    - name: metrics
      type: LoadBalancer
      ports:
        - name: jmx
          port: 9404
          targetPort: 9404
        - name: rest
          port: 10300
          targetPort: 10300
```

For clusters that only need internal Prometheus scraping, the pod annotations are sufficient and no additional service is required.
