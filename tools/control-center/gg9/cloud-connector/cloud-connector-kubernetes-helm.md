---
description: >-
  Installing the GridGain Cloud Connector on Kubernetes with a Helm chart,
  including configuration, upgrade, and uninstall.
---

# Deploying Cloud Connector on Kubernetes with a Helm Chart

This section provides a step-by-step process for installing the Cloud Connector on Kubernetes using [Kubernetes Helm Chart](https://helm.sh/).

## Prerequisites

- Kubernetes cluster version 1.26 or later
- Helm version 3 or later
- PersistentVolume provisioner support in the persistence configuration

{% hint style="info" %}
Older versions of Kubernetes and Helm have not been tested; use at your own risk.
{% endhint %}

## Step 1: Add Helm Chart repository

To add the Helm chart repository, run the following commands:

```bash
helm repo add gridgain https://gridgain.github.io/helm-charts/
helm repo update
```

## Step 2: Prepare configuration file

Configure the `values.yaml` file to set up the [Cloud Connector](connect-cloud-connector.md). It is mandatory to specify the content section for the connector to function properly.

- Set your Control Center credentials and the `base-url` that points to the connector URL. The `base-url` must be accessible from the monitored cluster nodes. Below is an example configuration:

  ```yaml
      content: |-
        connector:
          cc-url: http://control-center.gridgain.svc.cluster.local
          base-url: http://connector.namespace.svc.cluster.local:80
          name: Control Center Cloud Connector
          username: <provide your Control Center username here>
          password: <provide your Control Center password here>
  ```
- By default Cloud Connector will be exposed to Kubernetes network using `ClusterIP` service and `80` port. Ensure that port value in the `base-url` matches the `httpPort`.

  ```yaml
  service:
    enabled: true
    httpPort: 80
    type: ClusterIP
  ```
- If you want to expose your Cloud Connector outside of Kubernetes network (e.g. to monitor GridGain 9 clusters out of Kubernetes network) configure the `ingress` settings as shown below. The `ingress.host` must match the `base-url` parameter from `application.properties` file provided along with Cloud Connector [installation](connect-cloud-connector.md).

  ```yaml
  ingress:
    enabled: true
    test: false
    hosts:
      - host: "connector.example.io"
        paths:
          - path: "/api/v1/metrics"
          - path: "/api/v1/events"
    tls:
    - hosts:
        - connector.example.io
      secretName: connector.example.io-tls
  ```

## Step 3: Install the Helm Chart

To install the chart with the default configuration, use the following command:

```bash
helm install my-release gridgain/cc-spring-app -f values.yaml
```

This installs GridGain 9 on your Kubernetes cluster.

## Step 4: Update the Helm Chart installation

To apply updates or reconfigure the installation, use the following command:

```bash
helm upgrade my-release gridgain/cc-spring-app -f values.yaml
```

## Uninstalling GridGain

To remove the installation from your Kubernetes cluster, use the following command:

```bash
helm uninstall my-release
```

## Getting Help

For more information about available options and values, refer to the Helm chart [documentation on Artifact Hub](https://artifacthub.io/packages/helm/gridgain/cc-spring-app).

If you have questions or concerns, [open an issue](https://github.com/gridgain/helm-charts/issues) in our GitHub repository.
