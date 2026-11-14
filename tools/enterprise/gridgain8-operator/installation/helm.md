---
description: >-
  Install, upgrade, and uninstall the MariaDB GridGain 8 Kubernetes Operator
  with Helm, including CRDs, OpenShift, and supported Kubernetes versions.
---

# Helm

Helm is the supported way to install the MariaDB GridGain 8 Kubernetes Operator. The operator is split into two charts so you can manage Custom Resource Definitions independently of the controller.

* `gridgain8-operator-crds`: the `GridGainCluster` CRD.
* `gridgain8-operator`: the controller, webhook, RBAC, and related resources.

## Prerequisites

* A MariaDB Enterprise Platform Ultimate subscription. The 1.0.0 GA release is available only to Ultimate customers.
* Kubernetes `1.35` or later (`kubeVersion: ">=1.35.0-0"`).
* Helm 3 or later.
* A Docker pull Secret for `docker.mariadb.com`. See [Customer Access to docker.mariadb.com](../../mariadb-enterprise-operator/customer-access-to-docker-mariadb-com.md).

cert-manager is **not** required. The operator provisions webhook TLS itself. To use cert-manager instead, set `webhook.cert.certManager.enabled=true` after installing cert-manager.

## Supported Versions

The operator version is independent of the GridGain 8 image tag. This release is the `1.x` line.

| Operator version | Supported Kubernetes | Notes |
| ---------------- | -------------------- | ----- |
| `1.0.0` | `>=1.35.0-0` | Current `1.x` line. Tested on Kubernetes `1.35`. |

Support covers the three latest Kubernetes versions on [CNCF-certified](https://www.cncf.io/training/certification/software-conformance/) distributions. This release requires Kubernetes 1.35 or later (`kubeVersion: ">=1.35.0-0"`) and was tested on Kubernetes 1.35. Validation is on upstream Kubernetes. Amazon EKS, Google Kubernetes Engine, Azure Kubernetes Service, VMware Tanzu Kubernetes Grid, and other CNCF-certified platforms are in scope. Misconfigured clusters, CSI, and CNI issues are not.

Pin a release with `--version 1.0.0`. After patch releases exist, `--version "1.*"` installs the latest `1.x` chart.

## Installing CRDs

Helm does not upgrade CRDs the way it upgrades other templates. Install CRDs from the dedicated chart:

```sh
helm repo add gridgain8-operator https://gridgain-operator.mariadb.com
helm repo update
helm install gridgain8-operator-crds gridgain8-operator/gridgain8-operator-crds --version 1.0.0
```

## Installing the Operator

Prepare a `values.yaml` that references your registry Secret:

```yaml
imagePullSecrets:
  - name: mariadb-enterprise
```

```sh
helm install gridgain8-operator gridgain8-operator/gridgain8-operator \
  -n gridgain-k8s-operator-system --create-namespace \
  -f values.yaml \
  --version 1.0.0
```

Wait until the controller is Ready:

```sh
kubectl -n gridgain-k8s-operator-system rollout status \
  deploy/gridgain-k8s-operator-controller-manager
```

Leave `crds.enabled` at `false` (the default) and install the CRD chart first. If this chart owns the CRDs and you later uninstall it, Kubernetes deletes every `GridGainCluster`.

## Deployment Modes

### Cluster-Wide

The default. The operator watches `GridGainCluster` resources in every namespace. The validating webhook is enabled.

### Single Namespace

Set `currentNamespaceOnly: true`. RBAC is a Role, not a ClusterRole. The webhook is **disabled**. Only `GridGainCluster` objects in the operator namespace are reconciled. Admission then relies on CRD OpenAPI and CEL only.

{% code title="values-single-namespace.yaml" %}
```yaml
currentNamespaceOnly: true
imagePullSecrets:
  - name: mariadb-enterprise
```
{% endcode %}

The same values file is `operator/values-single-namespace.yaml` in the [examples catalog](../examples-catalog.md). Apply `operator/gridgaincluster.yaml` in the operator namespace after install.

## OpenShift

The operator is tested with Helm on **OpenShift 4.22.1**. It is **not** Red Hat certified and does **not** appear in OperatorHub. Install it with the same Helm charts as on Kubernetes.

Use the [global pull secret](../../mariadb-enterprise-operator/customer-access-to-docker-mariadb-com.md#openshift) so every namespace can pull `docker.mariadb.com/gridgain8-operator`.

The operator default `podSecurityContext` sets UID `1000` and `fsGroup` `2000`, which `restricted-v2` rejects. Leave those IDs unset so the constraint assigns them from the namespace range. The complete cluster is `gridgaincluster-openshift.yaml` in the [examples catalog](../examples-catalog.md):

```yaml
spec:
  podSecurityContext:
    runAsNonRoot: true
    seccompProfile:
      type: RuntimeDefault
  containerSecurityContext:
    runAsNonRoot: true
    allowPrivilegeEscalation: false
    capabilities:
      drop: ["ALL"]
    seccompProfile:
      type: RuntimeDefault
```

{% hint style="warning" %}
Do not deploy operands in the `default` or `kube-system` namespaces on OpenShift. OpenShift does not assign a SecurityContext there.
{% endhint %}

## Upgrading

Upgrade the CRD chart first, then the operator chart. Skip the CRD chart only when the release notes say the CRDs did not change. Use `--version <new-version>` for the charts you are installing, not the version already running.

`--reuse-values` keeps the image tag from the installed chart. To pin a tag, add `--set image.tag=<new-version>`.

The full commands and what happens to running clusters are on [Updates](../updates.md#upgrade-the-operator). Changing the GridGain **image version** is a different procedure: [Change the GridGain Server Version](../updates.md#change-the-gridgain-server-version).

## Uninstalling

{% hint style="danger" %}
Uninstalling the CRD chart deletes the CRDs and every `GridGainCluster` that uses them.
{% endhint %}

Uninstall the operator first. CRDs and running GridGain pods stay until you remove the CRD chart.

```sh
helm uninstall gridgain8-operator -n gridgain-k8s-operator-system
helm uninstall gridgain8-operator-crds
```

## Operator Helm Values

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| crds.enabled | bool | `false` | Whether this chart should install the CRDs. Install `gridgain8-operator-crds` first. |
| currentNamespaceOnly | bool | `false` | Watch only the operator namespace. Disables the webhook and uses a Role. |
| image.repository | string | `docker.mariadb.com/gridgain8-operator` | Operator image repository. |
| image.tag | string | `""` | Image tag. Empty uses the chart `appVersion`. |
| image.pullPolicy | string | `IfNotPresent` |  |
| imagePullSecrets | list | `[]` | Pull Secrets for `docker.mariadb.com`. |
| replicaCount | int | `1` | Operator replicas. |
| manager.featureGates | object | all `false` | Alpha feature gates. See [Configuration](../configuration.md#feature-gates). |
| metrics.enabled | bool | `false` | Create a ServiceMonitor for operator `/metrics`. Requires Prometheus Operator CRDs. |
| metrics.serviceMonitor.enabled | bool | `true` | Create the ServiceMonitor when `metrics.enabled` is true. |
| pdb.enabled | bool | `false` | PodDisruptionBudget for the operator. |
| webhook.cert.certManager.enabled | bool | `false` | Use cert-manager for webhook TLS instead of built-in certificates. |

The table lists the values used most often. Other chart keys keep their chart defaults.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
