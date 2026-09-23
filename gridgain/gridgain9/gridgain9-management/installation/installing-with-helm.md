---
description: >-
  Deploy, configure, update, and uninstall a GridGain 9 cluster on Kubernetes
  using the GridGain Helm chart.
---

# Installing GridGain 9 on Kubernetes using Helm Chart

This guide walks you through deploying a GridGain 9 cluster on Kubernetes using [Kubernetes Helm Chart](https://helm.sh/).

## Prerequisites

- Kubernetes cluster version 1.26 or more recent
- Helm version 3 or more recent
- PersistentVolume provisioner support in the persistence configuration

{% hint style="info" %}
Older versions of Kubernetes and Helm have not been tested and may not work as expected.
{% endhint %}

## Version Lifecycle

The information about versioning and lifecycle of GridGain 9 is available on the [Versioning page](https://www.gridgain.com/versioning-and-support-lifecycle).

## Installing Helm Chart

### Step 1: Add the Helm Repository

First, add the Helm chart repository with the following commands:

```bash
helm repo add gridgain https://gridgain.github.io/helm-charts/
helm repo update
```

### Step 2: Install the Helm Chart

Install the chart with the default configuration:

```bash
helm install my-release gridgain/gridgain9
```

This installs GridGain 9 on your Kubernetes cluster.

## Configuring Installation

GridGain provides extensive helm chart examples in a dedicated [GitGub repository](https://github.com/gridgain/helm-charts/tree/main/charts/gridgain9/examples).

The [complete example](https://github.com/gridgain/helm-charts/tree/main/charts/gridgain9/examples/complete) shows how to set up a production-ready version of GridGain 9 with Helm.

## Updating Installation

To update your GridGain installation with new configuration or values:

1. Modify the desired settings in your `values.yaml` file;
2. Apply the changes using the Helm upgrade command:

   ```bash
   helm upgrade my-release gridgain/gridgain9 -f values.yaml
   ```

## Uninstalling GridGain

To remove the installation from your Kubernetes cluster, use the following command:

```bash
helm uninstall my-release
```

## Limitations and Considerations

When running GridGain 9 in a Kubernetes environment, the node configuration becomes **read-only** and cannot be modified by using the `gridgain9 node config update` CLI command. This is by design, as node configuration is managed via Kubernetes resources.

{% hint style="warning" %}
While it is technically possible to make the node configuration writable by using an init container that copies the mounted configuration from one location to another (and pointing GridGain 9 to this new location), we **strongly discourage** this approach. It is not native to the Kubernetes model, and any changes made to the configuration will be lost during pod restarts or re-deployments.
{% endhint %}

## Getting Help

For more information about available options and values, refer to the Helm chart documentation on [Artifact Hub](https://artifacthub.io/packages/helm/gridgain/gridgain9).

If you have questions or concerns, [open an issue](https://github.com/gridgain/helm-charts/issues) in our GitHub repository.
