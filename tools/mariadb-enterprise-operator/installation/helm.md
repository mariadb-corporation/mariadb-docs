# Helm

Helm is the preferred way to install MariaDB Enterprise Kubernetes Operator in Kubernetes clusters. This documentation aims to provide guidance on how to manage the installation and upgrades of both the CRDs and the operator via Helm charts.

## Prerequisites

Configure your [customer credentials as described in the documentation](../customer-access-to-docker-mariadb-com.md#customer-credentials) to be able to pull images.

## Charts

MariaDB Enterprise Kubernetes Operator is splitted into two different helm charts for better convenience:

* `mariadb-enterprise-operator-crds`: Bundles the [CustomResourceDefinitions](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/) required by the operator.
* `mariadb-enterprise-operator`: Contains all the template manifests required to install the operator. Refer to the [operator helm values](helm.md#operator-helm-values) section for detailed information about the supported values.

## Control-plane

The operator extends the Kubernetes control plane and consists of the following components deployed via Helm:

* `operator`: The `mariadb-enterprise-operator` itself that performs the CRD reconciliation.
* `webhook`: The Kubernetes control-plane delegates CRD validations to this HTTP server. Kubernetes requires TLS to communicate with the webhook server.
* `cert-controller`: Provisions TLS certificates for the webhook. You can see it as a minimal [cert-manager](https://cert-manager.io/) that is intended to work only with the webhook. It is optional and can be replaced by cert-manager.

## Installing CRDs

Helm has certain [limitations when it comes to manage CRDs](https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#some-caveats-and-explanations). To address this, we are providing the CRDs in a separate chart, [as recommended by the official Helm documentation](https://helm.sh/docs/chart_best_practices/custom_resource_definitions/#method-2-separate-charts). This allows us to manage the installation and updates of the CRDs independently from the operator. For example, you can uninstall the operator without impacting your existing `MariaDB` CRDs.

CRDs can be installed in your cluster by running the following commands

```sh
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds
```

## Installing the operator

The first step is to prepare a `values.yaml` file to specify your previously configured [customer credentials](../customer-access-to-docker-mariadb-com.md#customer-credentials):

```yaml
imagePullSecrets:
  - name: mariadb-enterprise

webhook:
  imagePullSecrets:
      - name: mariadb-enterprise

certController:
  imagePullSecrets:
    - name: mariadb-enterprise
```

Then, you can proceed to install the operator:

```sh
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml
```

If you have the [prometheus operator](https://prometheus-operator.dev/) and [cert-manager](https://cert-manager.io/docs/installation/) already installed in your cluster, it is recommended to leverage them to scrape the operator metrics and provision the webhook certificate respectively:

```sh
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml \
  --set metrics.enabled=true --set webhook.cert.certManager.enabled=true
```
Refer to the [operator helm values](helm.md#operator-helm-values) section for detailed information about the supported values.

## Long-Term Support Versions

MariaDB Enterprise Kubernetes Operator provides stable Long-Term Support (LTS) versions.

| Version | Supported Kubernetes Versions | Description | Latest Version |
|---------|------------------------------|-------------|--------------|
| `25.10` | `>=1.32.0-0 <= 1.34.0-0` | LTS 25.10. It was tested to work up to kubernetes v1.34. | `25.10.0` |

If you instead wish to install a specific LTS release, you can do:

```sh
helm install --version "25.10.*" mariadb-enterprise-operator-crds mariadb-enterprise-operator/mariadb-enterprise-operator-crds
helm install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator \
  -f values.yaml \
  --version "25.10.*"
```

Where: `--version "25.10.*"` installs the most recent available release within the 25.10 series.

## Deployment modes

The following deployment modes are supported:

#### Cluster-wide

The operator watches CRDs in all namespaces and requires cluster-wide RBAC permissions to operate. This is the default deployment mode, enabled through the default configuration values:

```sh
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator mariadb-enterprise-operator/mariadb-enterprise-operator
```

#### Single namespace

By setting `currentNamespaceOnly=true`, the operator will only watch CRDs within the namespace it is deployed in, and the RBAC permissions will be restricted to that namespace as well:

```sh
helm repo add mariadb-enterprise-operator https://operator.mariadb.com
helm install mariadb-enterprise-operator \
  -n databases --create-namespace \
  -f values.yaml \
  --set currentNamespaceOnly=true \
  mariadb-enterprise-operator/mariadb-enterprise-operator
```

## Updates

{% hint style="info" %}
Make sure you read and understand the [updates documentation](../updates.md) before proceeding to update the operator.
{% endhint %}

{% hint style="warning" %}
To install a Long-Term Support (LTS) version instead, replace `<new-version>` with your desired LTS release.
For example: `--version "25.10.*"` will automatically install the latest available patch within that LTS series.
{% endhint %}

The first step is upgrading the CRDs that the operator depends on:

```sh
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator-crds \
  --version <new-version> \
  mariadb-enterprise-operator/mariadb-enterprise-operator-crds
```

Once updated, you may proceed to upgrade the operator:

```sh
helm repo update mariadb-enterprise-operator
helm upgrade --install mariadb-enterprise-operator \
  --version <new-version> \
  mariadb-enterprise-operator/mariadb-enterprise-operator
```

Whenever a new version of the operator is released, an upgrade guide is linked in the [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-enterprise-operator) if additional upgrade steps are required. Be sure to review the [release notes](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-enterprise-operator) and follow the version-specific upgrade guides accordingly.

## Operator high availability

The operator can run in high availability mode to prevent downtime during updates and ensure continuous reconciliation of your CRs, even if the node where the operator runs goes down. To achieve this, you need:

* Multiple replicas
* Configure `Pod` anti-affinity
* Configure `PodDisruptionBudgets`

You can achieve this by providing the following values to the helm chart:

```yaml
ha:
  enabled: true
  replicas: 3

affinity:
  podAntiAffinity:
    requiredDuringSchedulingIgnoredDuringExecution:
    - labelSelector:
        matchExpressions:
        - key: app.kubernetes.io/name
          operator: In
          values:
          - mariadb-enterprise-operator
        - key: app.kubernetes.io/instance
          operator: In
          values:
          - mariadb-enterprise-operator
      topologyKey: kubernetes.io/hostname

pdb:
  enabled: true
  maxUnavailable: 1
```

You may similarly configure the `webhook` and `cert-controller` components to run in high availability mode by providing the same values to their respective sections. Refer to the [operator helm values](helm.md#operator-helm-values) for detailed information.

## Uninstalling

{% hint style="danger" %}
Uninstalling the `mariadb-enterprise-operator-crds` Helm chart will remove the CRDs and their associated resources, resulting in downtime.
{% endhint %}

First, uninstall the `mariadb-enterprise-operator` Helm chart. This action will not delete your CRDs, so your operands (i.e. `MariaDB` and `MaxScale`) will continue to run without the operator's reconciliation.

```sh
helm uninstall mariadb-enterprise-operator
```

At this point, if you also want to delete CRDs and the operands running in your cluster, you may proceed to uninstall the `mariadb-enterprise-operator-crds` Helm chart:

```sh
helm uninstall mariadb-enterprise-operator-crds
```

## Operator helm values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| affinity | object | `{}` | Affinity to add to controller Pod |
| certController.affinity | object | `{}` | Affinity to add to cert-controller container |
| certController.caLifetime | string | `"26280h"` | CA certificate lifetime. It must be greater than certLifetime. |
| certController.certLifetime | string | `"2160h"` | Certificate lifetime. |
| certController.enabled | bool | `true` | Specifies whether the cert-controller should be created. |
| certController.extrArgs | list | `[]` | Extra arguments to be passed to the cert-controller entrypoint |
| certController.extraVolumeMounts | list | `[]` | Extra volumes to mount to cert-controller container |
| certController.extraVolumes | list | `[]` | Extra volumes to pass to cert-controller Pod |
| certController.ha.enabled | bool | `false` | Enable high availability |
| certController.ha.replicas | int | `3` | Number of replicas |
| certController.image.pullPolicy | string | `"IfNotPresent"` |  |
| certController.image.repository | string | `"docker.mariadb.com/mariadb-enterprise-operator"` |  |
| certController.image.tag | string | `""` | Image tag to use. By default the chart appVersion is used |
| certController.imagePullSecrets | list | `[]` |  |
| certController.nodeSelector | object | `{}` | Node selectors to add to cert-controller container |
| certController.pdb.enabled | bool | `false` | Enable PodDisruptionBudget for the cert-controller. |
| certController.pdb.maxUnavailable | int | `1` | Maximum number of unavailable Pods. You may also give a percentage, like `50%` |
| certController.podAnnotations | object | `{}` | Annotations to add to cert-controller Pod |
| certController.podSecurityContext | object | `{}` | Security context to add to cert-controller Pod |
| certController.priorityClassName | string | `""` | priorityClassName to add to cert-controller container |
| certController.privateKeyAlgorithm | string | `"ECDSA"` | Private key algorithm to be used for the CA and leaf certificate private keys. One of: ECDSA or RSA. |
| certController.privateKeySize | int | `256` | Private key size to be used for the CA and leaf certificate private keys. Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096) |
| certController.renewBeforePercentage | int | `33` | How long before the certificate expiration should the renewal process be triggered. For example, if a certificate is valid for 60 minutes, and renewBeforePercentage=25, cert-controller will begin to attempt to renew the certificate 45 minutes after it was issued (i.e. when there are 15 minutes (25%) remaining until the certificate is no longer valid). |
| certController.requeueDuration | string | `"5m"` | Requeue duration to ensure that certificate gets renewed. |
| certController.resources | object | `{}` | Resources to add to cert-controller container |
| certController.securityContext | object | `{}` | Security context to add to cert-controller Pod |
| certController.serviceAccount.annotations | object | `{}` | Annotations to add to the service account |
| certController.serviceAccount.automount | bool | `true` | Automounts the service account token in all containers of the Pod |
| certController.serviceAccount.enabled | bool | `true` | Specifies whether a service account should be created |
| certController.serviceAccount.extraLabels | object | `{}` | Extra Labels to add to the service account |
| certController.serviceAccount.name | string | `""` | The name of the service account to use. If not set and enabled is true, a name is generated using the fullname template |
| certController.serviceMonitor.additionalLabels | object | `{}` | Labels to be added to the cert-controller ServiceMonitor |
| certController.serviceMonitor.enabled | bool | `true` | Enable cert-controller ServiceMonitor. Metrics must be enabled |
| certController.serviceMonitor.interval | string | `"30s"` | Interval to scrape metrics |
| certController.serviceMonitor.metricRelabelings | list | `[]` |  |
| certController.serviceMonitor.relabelings | list | `[]` |  |
| certController.serviceMonitor.scrapeTimeout | string | `"25s"` | Timeout if metrics can't be retrieved in given time interval |
| certController.tolerations | list | `[]` | Tolerations to add to cert-controller container |
| certController.topologySpreadConstraints | list | `[]` | topologySpreadConstraints to add to cert-controller container |
| clusterName | string | `"cluster.local"` | Cluster DNS name |
| config.exporterImage | string | `"mariadb/mariadb-prometheus-exporter-ubi:1.1.0"` | Default MariaDB exporter image |
| config.exporterMaxscaleImage | string | `"mariadb/maxscale-prometheus-exporter-ubi:1.1.0"` | Default MaxScale exporter image |
| config.galeraLibPath | string | `"/usr/lib64/galera/libgalera_enterprise_smm.so"` | Galera Enterprise library path to be used with Galera |
| config.mariadbDefaultVersion | string | `"11.4"` | Default MariaDB Enterprise version to be used when unable to infer it via image tag |
| config.mariadbImage | string | `"docker.mariadb.com/enterprise-server:11.4.7-4.1"` | Default MariaDB Enterprise image |
| config.maxscaleImage | string | `"docker.mariadb.com/maxscale:25.01.3-1"` | Default MaxScale Enterprise image |
| crds | object | `{"enabled":false}` | CRDs |
| crds.enabled | bool | `false` | Whether the helm chart should create and update the CRDs. It is false by default, which implies that the CRDs must be managed independently with the mariadb-enterprise-operator-crds helm chart. **WARNING** This should only be set to true during the initial deployment. If this chart manages the CRDs and is later uninstalled, all MariaDB instances will be DELETED. |
| currentNamespaceOnly | bool | `false` | Whether the operator should watch CRDs only in its own namespace or not. |
| extrArgs | list | `[]` | Extra arguments to be passed to the controller entrypoint |
| extraEnv | list | `[]` | Extra environment variables to be passed to the controller |
| extraEnvFrom | list | `[]` | Extra environment variables from preexiting ConfigMap / Secret objects used by the controller using envFrom |
| extraVolumeMounts | list | `[]` | Extra volumes to mount to the container. |
| extraVolumes | list | `[]` | Extra volumes to pass to pod. |
| fullnameOverride | string | `""` |  |
| ha.enabled | bool | `false` | Enable high availability of the controller. If you enable it we recommend to set `affinity` and `pdb` |
| ha.replicas | int | `3` | Number of replicas |
| image.pullPolicy | string | `"IfNotPresent"` |  |
| image.repository | string | `"docker.mariadb.com/mariadb-enterprise-operator"` |  |
| image.tag | string | `""` | Image tag to use. By default the chart appVersion is used |
| imagePullSecrets | list | `[]` |  |
| logLevel | string | `"INFO"` | Controller log level |
| metrics.enabled | bool | `false` | Enable operator internal metrics. Prometheus must be installed in the cluster |
| metrics.serviceMonitor.additionalLabels | object | `{}` | Labels to be added to the controller ServiceMonitor |
| metrics.serviceMonitor.enabled | bool | `true` | Enable controller ServiceMonitor |
| metrics.serviceMonitor.interval | string | `"30s"` | Interval to scrape metrics |
| metrics.serviceMonitor.metricRelabelings | list | `[]` |  |
| metrics.serviceMonitor.relabelings | list | `[]` |  |
| metrics.serviceMonitor.scrapeTimeout | string | `"25s"` | Timeout if metrics can't be retrieved in given time interval |
| nameOverride | string | `""` |  |
| nodeSelector | object | `{}` | Node selectors to add to controller Pod |
| pdb.enabled | bool | `false` | Enable PodDisruptionBudget for the controller. |
| pdb.maxUnavailable | int | `1` | Maximum number of unavailable Pods. You may also give a percentage, like `50%` |
| podAnnotations | object | `{}` | Annotations to add to controller Pod |
| podSecurityContext | object | `{}` | Security context to add to controller Pod |
| pprof.enabled | bool | `false` | Enable the pprof HTTP server. |
| pprof.port | int | `6060` | The port where the pprof HTTP server listens. |
| priorityClassName | string | `""` | priorityClassName to add to controller Pod |
| rbac.aggregation.enabled | bool | `true` | Specifies whether the cluster roles aggrate to view and edit predefinied roles |
| rbac.enabled | bool | `true` | Specifies whether RBAC resources should be created |
| resources | object | `{}` | Resources to add to controller container |
| securityContext | object | `{}` | Security context to add to controller container |
| serviceAccount.annotations | object | `{}` | Annotations to add to the service account |
| serviceAccount.automount | bool | `true` | Automounts the service account token in all containers of the Pod |
| serviceAccount.enabled | bool | `true` | Specifies whether a service account should be created |
| serviceAccount.extraLabels | object | `{}` | Extra Labels to add to the service account |
| serviceAccount.name | string | `""` | The name of the service account to use. If not set and enabled is true, a name is generated using the fullname template |
| tolerations | list | `[]` | Tolerations to add to controller Pod |
| topologySpreadConstraints | list | `[]` | topologySpreadConstraints to add to controller Pod |
| webhook.affinity | object | `{}` | Affinity to add to webhook Pod |
| webhook.annotations | object | `{}` | Annotations for webhook configurations. |
| webhook.cert.ca.key | string | `""` | File under 'ca.path' that contains the full CA trust chain. |
| webhook.cert.ca.path | string | `""` | Path that contains the full CA trust chain. |
| webhook.cert.certManager.duration | string | `""` | Duration to be used in the Certificate resource, |
| webhook.cert.certManager.enabled | bool | `false` | Whether to use cert-manager to issue and rotate the certificate. If set to false, mariadb-enterprise-operator's cert-controller will be used instead. |
| webhook.cert.certManager.issuerRef | object | `{}` | Issuer reference to be used in the Certificate resource. If not provided, a self-signed issuer will be used. |
| webhook.cert.certManager.privateKeyAlgorithm | string | `"ECDSA"` | Private key algorithm to be used for the CA and leaf certificate private keys. One of: ECDSA or RSA. |
| webhook.cert.certManager.privateKeySize | int | `256` | Private key size to be used for the CA and leaf certificate private keys. Supported values: ECDSA(256, 384, 521), RSA(2048, 3072, 4096) |
| webhook.cert.certManager.renewBefore | string | `""` | Renew before duration to be used in the Certificate resource. |
| webhook.cert.certManager.revisionHistoryLimit | int | `3` | The maximum number of CertificateRequest revisions that are maintained in the Certificate’s history. |
| webhook.cert.path | string | `"/tmp/k8s-webhook-server/serving-certs"` | Path where the certificate will be mounted. 'tls.crt' and 'tls.key' certificates files should be under this path. |
| webhook.cert.secretAnnotations | object | `{}` | Annotatioms to be added to webhook TLS secret. |
| webhook.cert.secretLabels | object | `{}` | Labels to be added to webhook TLS secret. |
| webhook.enabled | bool | `true` | Specifies whether the webhook should be created. |
| webhook.extrArgs | list | `[]` | Extra arguments to be passed to the webhook entrypoint |
| webhook.extraVolumeMounts | list | `[]` | Extra volumes to mount to webhook container |
| webhook.extraVolumes | list | `[]` | Extra volumes to pass to webhook Pod |
| webhook.ha.enabled | bool | `false` | Enable high availability |
| webhook.ha.replicas | int | `3` | Number of replicas |
| webhook.hostNetwork | bool | `false` | Expose the webhook server in the host network |
| webhook.image.pullPolicy | string | `"IfNotPresent"` |  |
| webhook.image.repository | string | `"docker.mariadb.com/mariadb-enterprise-operator"` |  |
| webhook.image.tag | string | `""` | Image tag to use. By default the chart appVersion is used |
| webhook.imagePullSecrets | list | `[]` |  |
| webhook.nodeSelector | object | `{}` | Node selectors to add to webhook Pod |
| webhook.pdb.enabled | bool | `false` | Enable PodDisruptionBudget for the webhook. |
| webhook.pdb.maxUnavailable | int | `1` | Maximum number of unavailable Pods. You may also give a percentage, like `50%` |
| webhook.podAnnotations | object | `{}` | Annotations to add to webhook Pod |
| webhook.podSecurityContext | object | `{}` | Security context to add to webhook Pod |
| webhook.port | int | `9443` | Port to be used by the webhook server |
| webhook.priorityClassName | string | `""` | priorityClassName to add to webhook Pod |
| webhook.resources | object | `{}` | Resources to add to webhook container |
| webhook.securityContext | object | `{}` | Security context to add to webhook container |
| webhook.serviceAccount.annotations | object | `{}` | Annotations to add to the service account |
| webhook.serviceAccount.automount | bool | `true` | Automounts the service account token in all containers of the Pod |
| webhook.serviceAccount.enabled | bool | `true` | Specifies whether a service account should be created |
| webhook.serviceAccount.extraLabels | object | `{}` | Extra Labels to add to the service account |
| webhook.serviceAccount.name | string | `""` | The name of the service account to use. If not set and enabled is true, a name is generated using the fullname template |
| webhook.serviceMonitor.additionalLabels | object | `{}` | Labels to be added to the webhook ServiceMonitor |
| webhook.serviceMonitor.enabled | bool | `true` | Enable webhook ServiceMonitor. Metrics must be enabled |
| webhook.serviceMonitor.interval | string | `"30s"` | Interval to scrape metrics |
| webhook.serviceMonitor.metricRelabelings | list | `[]` |  |
| webhook.serviceMonitor.relabelings | list | `[]` |  |
| webhook.serviceMonitor.scrapeTimeout | string | `"25s"` | Timeout if metrics can't be retrieved in given time interval |
| webhook.tolerations | list | `[]` | Tolerations to add to webhook Pod |
| webhook.topologySpreadConstraints | list | `[]` | topologySpreadConstraints to add to webhook Pod |

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
