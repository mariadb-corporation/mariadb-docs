---
description: >-
  Basic examples of using GridGain Operator: scaling a cluster, switching to
  Ignite, rolling upgrades, switching to in-memory mode, and adjusting configuration.
---

# Basic Operations Examples

This section contains basic examples of GridGain Operator usage. The section does not include a full set of possible operations that you can do with Operator, but should provide you with a knowledge on how to perform some of the operations using Operator.

All examples assume that you have a deployed cluster with the default settings. Please refer to the [Getting Started](quick-start.md) section for more details.

This section uses the following assumptions:

- A dedicated namespace for operator deployment is created. See the [Create Operator namespace](quick-start.md#create-operator-namespace) section for GridGain Operator configuration.
- CustomResourceDefinitions is deployed, See the [Apply CRDs](quick-start.md#apply-crds) section for more details.
- RBAC is configured. See the [Apply RBAC](quick-start.md#apply-rbac) section for more details.
- Operator is deployed. See the [Deploy the Operator](quick-start.md#deploy-the-operator) section for more details.
- `Ignite` and `IgniteConfig` resources are deployed. See the [Deploy the Operator](quick-start.md#deploy-custom-resources) section for more details.

## Scaling a Cluster

With the default settings, a cluster has two server nodes available. To bring a new node or to remove a current one, adjust the `number_of_nodes` parameter for the `Ignite` custom resource.

### 1. Change `number_of_nodes` to `3` and save the 'ignite.yaml' file

```
  # Number of pods.
  # ---
  number_of_nodes: 3
```

Save the file changes

### 2. Apply changes in the `Ignite` custom resource

```
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
```

Changes should be automatically propagated to the operator and after a short time you should notice a new node available:

```
kubectl get pods -n apache-ignite -w
NAME                      READY   STATUS    RESTARTS   AGE
apache-ignite-cluster-0   1/1     Running   0          87s
apache-ignite-cluster-1   1/1     Running   0          75s
apache-ignite-cluster-2   0/1     Pending   0          0s
apache-ignite-cluster-2   0/1     Pending   0          1s
apache-ignite-cluster-2   0/1     ContainerCreating   0          1s
```

## Switching to Ignite Version

{% hint style="warning" %}
It is not possible to switch between GridGain or Apache Ignite versions without cleaning up the resources. Please refer to the [Cluster Termination](operator-configuration.md#cluster-termination) section for more details on cleaning resources.
{% endhint %}

By default, Operator deploys the latest GridGain version. To switch to Ignite cluster, adjust the [Cluster Image](operator-configuration.md#cluster_image)

### 1. Change the `Ignite` Resource

Adjust `ignite.yaml` and make the following changes:

```
...
cluster_image: apacheignite/ignite:latest
...
```

Save the file changes.

### 2. Apply Changes

To deploy a new cluster, run the following commands: 

```
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

### 3. Check the Result

```
kubectl get pods -n apache-ignite -w
NAME                      READY   STATUS    RESTARTS   AGE
apache-ignite-cluster-0   1/1     Running   0          2m42s
apache-ignite-cluster-1   1/1     Running   0          70s
apache-ignite-cluster-2   1/1     Running   0          54s
```

## Rolling Upgrade

Suppose you have previously deployed a cluster with the following GridGain version specified in `Ignite` resource:

```
...
cluster_image: "cluster_image: "gridgain/enterprise:8.7.32""
...
```

And now you want to upgrade to a newer version, for example, `8.7.33`.

### 1. Make sure that the `RollingUpgrade` property is configured

Open `ignite_config.yaml` and add the following lines if absent:

```
...
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="pluginConfigurations">
        <list>
            <bean class="org.gridgain.grid.configuration.GridGainConfiguration">
                <property name="rollingUpdatesEnabled" value="true"/>
            </bean>
        </list>
    </property>
...
```

Save the file and apply changes

```
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

### 2. Change the image

Modify `ignite.yaml` and set a newer image version:

```
...
cluster_image: "cluster_image: "gridgain/enterprise:8.7.33""
...
```

Save the file and apply changes

```
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
```

### 3. Check the result

Note, PODs are restarted one-by-one:

```
kubectl get pods -n apache-ignite -w

NAME                      READY   STATUS        RESTARTS   AGE
apache-ignite-cluster-0   1/1     Running       0          6m37s
apache-ignite-cluster-1   1/1     Running       0          4m58s
apache-ignite-cluster-2   0/1     Terminating   0          4m41s
apache-ignite-cluster-2   0/1     Terminating   0          4m45s
apache-ignite-cluster-2   0/1     Terminating   0          4m45s
apache-ignite-cluster-2   0/1     Pending       0          0s
apache-ignite-cluster-2   0/1     Pending       0          0s
apache-ignite-cluster-2   0/1     ContainerCreating   0          0s
```

## Switching to In-Memory Mode

By default, Operator comes with a persistent cluster configuration. To switch to pure in-memory mode, perform the following changes:

{% hint style="warning" %}
It is not possible to switch between in-memory or persistent modes without cleaning up the resources. Please refer to the [Cluster Termination](operator-configuration.md#cluster-termination) section for more details on cleaning resources.
{% endhint %}

### 1. Change 'cluster_type' to 'in-memory' for `Ignite` CR

```
...
  # Cluster Type {"persistence", "in-memory"}
  # ---
  cluster_type: "in-memory"
...
```

Save `ignite.yaml` file.

### 2. Change `IgniteConfig` CR to the following one:

`ignite_config.yaml`

```
apiVersion: gridgain.com/v1
kind: IgniteConfig
metadata:
  name: ignite-config
spec:
  config: |-
          <?xml version="1.0" encoding="UTF-8"?>
          <beans xmlns="http://www.springframework.org/schema/beans"
                 xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                 xsi:schemaLocation="
                  http://www.springframework.org/schema/beans
                  http://www.springframework.org/schema/beans/spring-beans.xsd">

              <bean class="org.apache.ignite.configuration.IgniteConfiguration">               
                  <property name="discoverySpi">
                      <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
                          <property name="ipFinder">
                              <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.kubernetes.TcpDiscoveryKubernetesIpFinder">
                                  <property name="namespace" value="<namespace>"/>
                                  <property name="serviceName" value="<cluster_name>-service"/>
                              </bean>
                          </property>
                      </bean>
                  </property>
              </bean>
          </beans>
```

Save the `ignite_config.yaml` file.

### 3. Deploy modified CRs

```
kubectl apply -f crds/ignite.yaml -n apache-ignite-operator
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

## Cluster Configuration Adjustment

### 1. Make changes in the `IgniteConfig` resource

To make internal configuration changes, adjust the `ignite_config.yaml` file. For example, you want to deploy a new cache with a name "cacheName":

```
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    ...

    <property name="cacheConfiguration">
        <bean class="org.apache.ignite.configuration.CacheConfiguration">
            <property name="name" value="cacheName"/>
            <property name="cacheMode" value="PARTITIONED"/>
        </bean>
    </property>
```

Make the changes and save the file.

### 2. Apply changes

Apply changes:

```
kubectl apply -f crds/ignite_config.yaml -n apache-ignite-operator
```

### 3. Check the result

Nodes are restarted automatically in order to reflect new changes.

```
kubectl get pods -n apache-ignite -w
NAME                      READY   STATUS    RESTARTS   AGE
apache-ignite-cluster-0   1/1     Running   0          2m34s
apache-ignite-cluster-1   1/1     Running   0          2m19s
apache-ignite-cluster-2   1/1     Running   0          2m7s
apache-ignite-cluster-0   1/1     Terminating   0          2m36s
apache-ignite-cluster-1   1/1     Terminating   0          2m22s
apache-ignite-cluster-2   1/1     Terminating   0          2m10s
apache-ignite-cluster-0   0/1     Terminating   0          2m38s
apache-ignite-cluster-2   0/1     Terminating   0          2m12s
apache-ignite-cluster-0   0/1     Terminating   0          2m39s
apache-ignite-cluster-0   0/1     Terminating   0          2m39s
apache-ignite-cluster-0   0/1     Pending       0          0s
apache-ignite-cluster-1   0/1     Terminating   0          2m24s
apache-ignite-cluster-0   0/1     Pending       0          0s
apache-ignite-cluster-0   0/1     ContainerCreating   0          0s
apache-ignite-cluster-0   0/1     Running             0          5s
```

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
