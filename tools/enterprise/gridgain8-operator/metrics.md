---
description: >-
  Operator and GridGain metrics, scrape annotations, and the ServiceMonitor
  overlay. No alerts or PrometheusRule objects are shipped.
---

# Metrics

The operator can expose Prometheus metrics for itself and, with a feature gate, configure GridGain pods for scraping. This is a capability, not a required monitoring stack.

{% hint style="info" %}
This operator does not ship Prometheus, Grafana, Alertmanager, or PrometheusRule objects. Point your collector at the endpoints below, or apply the ServiceMonitor overlay if you already run Prometheus Operator.
{% endhint %}

## Operator Metrics

Unauthenticated HTTP on port `8080`, path `/metrics`, Service `gridgain-k8s-operator-controller-manager-metrics-service`. Same pattern as MariaDB Enterprise Kubernetes Operator.

Enable the chart ServiceMonitor when Prometheus Operator CRDs are installed:

```yaml
metrics:
  enabled: true
  serviceMonitor:
    enabled: true
    # additionalLabels:
    #   release: kube-prometheus-stack
```

Or apply a ServiceMonitor in the operator namespace:

```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: gridgain-k8s-operator
  labels:
    app.kubernetes.io/name: gridgain-k8s-operator
    control-plane: controller-manager
spec:
  selector:
    matchLabels:
      app.kubernetes.io/name: gridgain-k8s-operator
      control-plane: controller-manager
  namespaceSelector:
    matchNames:
      - gridgain-k8s-operator-system
  endpoints:
    - port: metrics
      path: /metrics
      interval: 30s
      scrapeTimeout: 25s
```

The same object is `operator/servicemonitor.yaml` in the [examples catalog](examples-catalog.md). Helm overlay: `operator/values-metrics.yaml`. Edit `namespaceSelector` if you did not use `gridgain-k8s-operator-system`. Restrict who can reach port `8080` with a NetworkPolicy if needed.

## GridGain Pod Metrics

Off by default. Set the Metrics feature gate, then `spec.metricsEnabled: true`. The sample adds scrape annotations on port **9000**:

```yaml
spec:
  metricsEnabled: true
  podAnnotations:
    prometheus.io/scrape: "true"
    prometheus.io/port: "9000"
    prometheus.io/path: "/metrics"
```

The complete cluster is `alpha/gridgaincluster-metrics.yaml` in the [examples catalog](examples-catalog.md). To confirm the exporter, `curl http://127.0.0.1:9000/metrics` inside the GridGain container.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
