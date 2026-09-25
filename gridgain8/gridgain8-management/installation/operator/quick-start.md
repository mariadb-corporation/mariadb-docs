---
description: >-
  A quick-start guide to deploying a default persistent GridGain cluster with
  GridGain Operator and accessing Control Center integration.
---

# Getting Started

This section explains how to use GridGain Operator to deploy a default persistent cluster. As a result, you should have a running cluster that operates within the most recent GridGain Enterprise Edition version. The steps are described as simple as possible. The quick-start guide does not contain much technical details, please refer to the [Operator Configuration](operator-configuration.md) section for more details.

## Prerequisites

For this quick-start guide, your Kubernetes cluster is assumed to have a default dynamic storage provisioner. However, a storage class can be specified manually.

### Download Operator

Follow the steps in the [Operator Download](operator-download.md) section to get the release bundle. Unzip an archive to any folder and change your working directory to that folder.

### Create Operator Namespace

```shell
kubectl create namespace apache-ignite-operator
```

### Apply CRDs

```
kubectl apply -f crds/crds.yaml -n apache-ignite-operator
```

### Apply RBAC

```shell
kubectl apply -f rbac.yaml -n apache-ignite-operator
```

### Deploy the Operator

```shell
kubectl apply -f operator.yaml -n apache-ignite-operator
```

### Deploy Custom Resources

```shell
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

{% hint style="warning" %}
The processing might take awhile. You can monitor progress by using the -w command
{% endhint %}

```shell
kubectl get pods -n apache-ignite -w 
```

Output:

```
NAME                           READY   STATUS    RESTARTS   AGE
apache-ignite-cluster-0   1/1     Running   0          1m
apache-ignite-cluster-1   1/1     Running   0          1m
```

### Access Control Center Integration

The default stateful set is preconfigured to include all necessary libraries for accessing Control Center, which is free and cloud-based. If your environment can access external websites, then, after the pods started to run, you can find the connection link to [Control Center]({tools}/control-center). The link expires within five minutes.

```
kubectl logs apache-ignite-cluster-0 -n apache-ignite | grep  https://control.gridgain.com
...
[13:12:51]  https://control.gridgain.com
[13:12:51]  https://control.gridgain.com/go/0d77ae1f-113e-4d90-a96e-9d4021a54de3
```

### Cluster Termination

To remove active cluster alongside the namespace and clean all resources, please refer to the [Cluster Termination](operator-configuration.md#cluster-termination) section.

## Conclusion

In this quick start guide, we showed how to deploy the GridGain Enterprise Edition cluster with the default settings and access the shared Control Center using the connection URL found within the logs.

## What's Next

Playing around the default cluster might be a good starting point, but for advanced usage please refer to the [Operator Configuration](operator-configuration.md) page.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
