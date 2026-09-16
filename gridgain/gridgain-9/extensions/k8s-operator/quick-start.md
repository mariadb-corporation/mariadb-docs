---
description: >-
  Install the GridGain Kubernetes Operator, deploy a three-node GridGain 9
  cluster, and verify it using the CLI tool.
---

# Quick Start

{% hint style="warning" %}
Kubernetes operator is an experimental feature. The configuration may change in a subsequent release.
{% endhint %}

This guide walks you through installing the operator, deploying a three-node GridGain 9 cluster, and verifying that everything is working.

## Prerequisites

- A valid GridGain 9 license.
- A Kubernetes cluster running version 1.22 or later. The operator uses `apiextensions.k8s.io/v1` CRDs and server-side apply, both of which require Kubernetes 1.22+.
- `kubectl` configured with administrative access to the target cluster.
- Container registry access: The default controller image is `gridgain/gridgain9-k8s-operator:0.1.0` on Docker Hub. If you use a private registry or custom image, adjust the `Deployment` in `resources/controller-resources.yaml` before applying it.

## Install the Operator

Installation is a two-step process: you apply the Custom Resource Definition first, then deploy the controller and its supporting resources.

### Install the CRD

Download the [Custom Resource Definition](https://github.com/gridgain/gridgain9-k8s-operator/blob/main/resources/crd.yaml) file and apply it to register the `GridGain9Cluster` resource type with the Kubernetes API server:

```bash
kubectl apply --server-side=true -f crd.yaml
```

The `--server-side=true` flag is recommended. Client-side application may fail or time out on objects of this size.

### Install Controller Resources

Download the [controller manifest](https://github.com/gridgain/gridgain9-k8s-operator/blob/main/resources/controller-resources.yaml) file and apply it:

```bash
kubectl apply --server-side=true -f controller-resources.yaml
```

This creates the `gridgain9-system` namespace, a dedicated ServiceAccount, default roles and bindings, a metrics service, and the `gridgain9-controller-manager` Deployment.

### Verify the Installation

Confirm that the CRD is registered and the controller is running:

```bash
# Checks if CRD is installed.
kubectl get crd gridgain9clusters.gridgain-9.gridgain.com
# Checks if the controller is created.
kubectl get deployment -n gridgain9-system gridgain9-controller-manager
# Checks if the controller pod is running.
kubectl get pods -n gridgain9-system
```

The `gridgain9clusters` resource should appear in the CRD list, and the controller pod should be in a `Running` state.

## Deploy a Cluster

### Create a License Secret

GridGain 9 requires a license for cluster initialization. In this tutorial, we will create a secret to safely manage the license. Create a Kubernetes Secret from your license file:

```bash
kubectl create secret generic gridgain-license \
  --from-file=license.conf=/path/to/your/license.json
```

The Secret must reside in the same namespace where you will create the `GridGain9Cluster` resource.

For quick tests or demos, you can skip the Secret and embed the license content directly in the manifest using `spec.license.content`.

### Apply the Cluster Manifest

Create a file named `simple-cluster.yaml` with the following content:

```yaml
apiVersion: gridgain-9.gridgain.com/v1
kind: GridGain9Cluster
metadata:
  name: simple-cluster
spec:
  replicas: 3
  image:
    registry: docker.io
    repository: gridgain/gridgain9
    tag: "9.1"
  persistence:
    enabled: true
    size: 20Gi
  license:
    secretName: gridgain-license
    secretKey: license.conf
    mountPath: /opt/gridgain/etc/license.conf
```

{% hint style="info" %}
In the example above, we use the specific GridGain version. You can remove the `image` element to install the latest GridGain version instead.
{% endhint %}

Then, apply it:

```bash
kubectl apply -f simple-cluster.yaml
```

This deploys a three-node cluster as specified in the `replicas` configuration, with 20Gi persistent volumes for each. The operator creates a StatefulSet, a headless service for node discovery, and a `Job` to initialize the cluster with your license.

### Verify the Deployment

Watch the cluster resource until the Phase shows `Running`:

```bash
kubectl get gg9 simple-cluster
```

Check that all pods are ready:

```bash
kubectl get pods -l app.kubernetes.io/instance=simple-cluster
```

Verify the cluster topology from inside a pod:

```bash
# Checks if all nodes are running, found each other and formed a topology
kubectl exec simple-cluster-0 -- /opt/gridgain9cli/bin/gridgain9 cluster topology physical
# Checks cluster status
kubectl exec simple-cluster-0 -- /opt/gridgain9cli/bin/gridgain9 cluster status
# Checks if all nodes are correctly included in the cluster
kubectl exec simple-cluster-0 -- /opt/gridgain9cli/bin/gridgain9 cluster topology logical
```

## Use the CLI Tool

Once the cluster is running, the GridGain CLI tool is available inside each pod at `/opt/gridgain9cli/bin/gridgain9`. For this tutorial, we will connect to a node in the cluster, and then use the CLI tool to execute some simple queries.

- First, open an interactive shell on one of the pods:

  ```bash
  kubectl exec -it simple-cluster-0 -- bash
  ```

- From inside the pod, start the CLI tool:

  ```bash
  /opt/gridgain9cli/bin/gridgain9
  ```

- Confirm the connection to the cluster, then enter the SQL REPL mode by typing `sql`.
- Create a table:

  ```sql
  CREATE TABLE IF NOT EXISTS Person (id int primary key, city varchar, name varchar, age int, company varchar);
  ```

- Insert some data:

  ```sql
  INSERT INTO Person (id, city, name, age, company) VALUES (1, 'London', 'John Doe', 42, 'Apache');
  INSERT INTO Person (id, city, name, age, company) VALUES (2, 'New York', 'Jane Doe', 36, 'Apache');
  ```

- Query the data:

  ```sql
  SELECT * FROM Person;
  ```

- To leave the SQL REPL mode, type `exit;`.

For more information about available SQL statements, see the [SQL Reference](../../sql-reference/ddl.md) section.

## Clean Up

To remove the cluster and all resources the operator created for it:

```bash
kubectl delete gg9 simple-cluster
```

The operator uses a finalizer to ensure graceful shutdown and cleanup of all nodes.

{% hint style="warning" %}
The operator does not clean up persist files created for nodes. If the cluster is restarted later, it will use the same persistence. To fully clean up remaining files for a clean restart:

```bash
kubectl delete pvc persistence-simple-cluster-0 persistence-simple-cluster-1 persistence-simple-cluster-2
```
{% endhint %}

To remove the operator itself, remove the CRD and the resources:

```bash
kubectl delete -f controller-resources.yaml
kubectl delete -f crd.yaml
```

{% hint style="info" %}
Deleting the CRD removes the `GridGain9Cluster` API entirely. Make sure all custom resources are deleted first to avoid stuck objects.
{% endhint %}
