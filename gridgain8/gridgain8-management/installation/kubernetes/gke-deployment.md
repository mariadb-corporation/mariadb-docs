---
description: >-
  How to deploy a GridGain cluster on Google Kubernetes Engine (GKE) using the
  gcloud command-line tool.
---

# GridGain on Google Kubernetes Engine

This page explains how to deploy a GridGain cluster on Google Kubernetes Engine.

{% hint style="info" %}
This guide covers the provider-specific steps. It builds on the shared [Generic Kubernetes Instruction](generic-configuration.md), which explains the concepts, prerequisites, and configuration common to all Kubernetes deployments.
{% endhint %}
## Creating a GKE Cluster

A cluster in GKE is a set of nodes that provision resources for the applications that are deployed in the cluster.
You must create a GKE cluster with enough resources (CPU, RAM, and storage) for your use case.

- [Create a cluster](https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster)
- [Configure _kubectl_](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl)

The easiest way to create a cluster is to use the `gcloud` command line tool:

```
$ gcloud container clusters create my-cluster --zone us-west1
...
Creating cluster my-cluster in us-west1... Cluster is being health-checked (master is healthy)...done.
Created [https://container.googleapis.com/v1/projects/gmc-development/zones/us-west1/clusters/my-cluster].
To inspect the contents of your cluster, go to: https://console.cloud.google.com/kubernetes/workload_/gcloud/us-west1/my-cluster?project=my-project
kubeconfig entry generated for my-cluster.
NAME        LOCATION  MASTER_VERSION  MASTER_IP       MACHINE_TYPE   NODE_VERSION    NUM_NODES  STATUS
my-cluster  us-west1  1.14.10-gke.27  35.230.126.102  n1-standard-1  1.14.10-gke.27  9          RUNNING
```

Verify that your `kubectl` is configured correctly:

```shell
$ kubectl get nodes
NAME                                        STATUS   ROLES    AGE   VERSION
gke-my-cluster-default-pool-6e9f3e45-8k0w   Ready    <none>   73s   v1.14.10-gke.27
gke-my-cluster-default-pool-6e9f3e45-b7lb   Ready    <none>   72s   v1.14.10-gke.27
gke-my-cluster-default-pool-6e9f3e45-cmzc   Ready    <none>   74s   v1.14.10-gke.27
gke-my-cluster-default-pool-a2556b36-85z6   Ready    <none>   73s   v1.14.10-gke.27
gke-my-cluster-default-pool-a2556b36-xlbj   Ready    <none>   72s   v1.14.10-gke.27
gke-my-cluster-default-pool-a2556b36-z8fp   Ready    <none>   74s   v1.14.10-gke.27
gke-my-cluster-default-pool-e93974f2-hwkj   Ready    <none>   72s   v1.14.10-gke.27
gke-my-cluster-default-pool-e93974f2-jqj3   Ready    <none>   72s   v1.14.10-gke.27
gke-my-cluster-default-pool-e93974f2-v8xv   Ready    <none>   74s   v1.14.10-gke.27
```

Now you are ready to create Kubernetes resources.

## Kubernetes Configuration

The namespace, service, cluster role, ConfigMap, and node configuration file are the same for every Kubernetes deployment. Follow the [Generic Kubernetes Instruction](generic-configuration.md#kubernetes-configuration) to create these resources.
<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
