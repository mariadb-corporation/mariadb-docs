---
description: >-
  Sample YAML manifests for GridGainCluster and operator Helm values, including
  Alpha feature-gate examples.
---

# Examples Catalog

The [examples catalog](https://gridgain-operator.mariadb.com/examples/manifests.tar.gz) contains sample manifests that show the operator in a practical way. Helm is the supported operator install.

* Download the [examples catalog](https://gridgain-operator.mariadb.com/examples/manifests.tar.gz):

```sh
curl -sLO https://gridgain-operator.mariadb.com/examples/manifests.tar.gz
mkdir -p examples
tar -xzf manifests.tar.gz -C examples
```

* Create a license Secret. The operator does not ship a license. `license-secret.example.yaml` shows the Secret shape only.

```sh
kubectl create secret generic gridgaincluster-license \
  --from-file=gridgain-license.xml=/path/to/your/gridgain-license.xml
```

* Apply one `GridGainCluster` per namespace:

```sh
kubectl apply -f examples/gridgaincluster.yaml
```

These manifests use 1 replica and 1Gi memory so they fit a local cluster. Raise both for production. `apiVersion` is `gridgain.gridgain.com/v1`.

Some examples rely on external dependencies. Install them when they apply:

* [prometheus-operator](https://github.com/prometheus-community/helm-charts/tree/main/charts/kube-prometheus-stack) for metrics
* PKCS12 Secrets for the CRDTLS sample (`alpha/gridgaincluster-tls.yaml`)

Complement the examples with the [API reference](api-reference.md).

## GA (Default Feature Gates)

| File | Purpose |
| ---- | ------- |
| `license-secret.example.yaml` | Shape of the license Secret (placeholder only). |
| `gridgaincluster.yaml` | Copy this. Ungated fields only. Same cluster as [Quickstart](quickstart.md). |
| `gridgaincluster-minimal.yaml` | Smallest valid cluster. |
| `gridgaincluster-openshift.yaml` | OpenShift `restricted-v2`. See [Helm](installation/helm.md#openshift). |
| `gridgaincluster-upgrade.yaml` | `spec.upgrade` reference. See [Updates](updates.md). |
| `gridgaincluster-networkpolicy.yaml` | Workload NetworkPolicy. |
| `gridgaincluster-scheduling.yaml` | Topology spread and PDB. |
| `gridgaincluster-logging.yaml` | Custom Log4j2. |

On OpenShift, apply `gridgaincluster-openshift.yaml` instead of `gridgaincluster.yaml` or `gridgaincluster-minimal.yaml`. The operator default UID `1000` / `fsGroup` `2000` fails `restricted-v2`. The OpenShift manifest leaves those IDs unset so the constraint assigns them from the namespace range.

## Alpha (Enable Named Feature Gates)

See [Configuration](configuration.md#feature-gates). These gates are Kubernetes Alpha: off by default, not for production, and their API is not guaranteed to stay compatible. Enable the matching Helm `manager.featureGates` values before you apply these files.

| File | Gates |
| ---- | ----- |
| `alpha/gridgaincluster-metrics.yaml` | Metrics |
| `alpha/gridgaincluster-auth.yaml` | Auth |
| `alpha/gridgaincluster-tls.yaml` | CRDTLS (create PKCS12 Secrets first) |
| `alpha/gridgain-alpha-features.yaml` | All six (TLS stays disabled until you add stores) |

## Operator Install

Install the charts from [Helm](installation/helm.md). Use these files for overlay values and for a cluster in the operator namespace.

| File | Purpose |
| ---- | ------- |
| `operator/values-single-namespace.yaml` | Helm `currentNamespaceOnly: true`. |
| `operator/gridgaincluster.yaml` | CR for the operator namespace in that mode. |
| `operator/servicemonitor.yaml` | Operator `/metrics` for Prometheus Operator. |
| `operator/values-metrics.yaml` | Helm values that render the chart ServiceMonitor. |

```sh
helm upgrade --install gridgain8-operator gridgain8-operator/gridgain8-operator \
  -n gridgain-k8s-operator-system --create-namespace \
  -f examples/operator/values-single-namespace.yaml \
  --version 1.0.0
kubectl apply -n gridgain-k8s-operator-system -f examples/operator/gridgaincluster.yaml
```

This catalog does not install Prometheus.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
