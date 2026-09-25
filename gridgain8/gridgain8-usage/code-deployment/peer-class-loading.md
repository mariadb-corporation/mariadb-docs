---
description: >-
  How peer class loading deploys user classes from a local node to remote nodes
  in GridGain, including deployment modes and user versions.
---

# Peer Class Loading

## Overview

Peer class loading refers to loading classes from a local node where they are defined to remote nodes.
With peer class loading enabled, you don't have to manually deploy your Java code on each node in the cluster and re-deploy it each time it changes.
GridGain automatically loads the classes from the node where they are defined to the nodes where they are required.

For example, when [querying data](../key-value-api/using-scan-queries.md) with a custom transformer, you only need to define your tasks on the client node that initiates the computation, and GridGain loads the classes to the server nodes.

When enabled, peer class loading is used to deploy the following classes:

- Tasks and jobs submitted via the [compute interface](../distributed-computing/distributed-computing.md).
- Transformers and filters used with [scan queries](../key-value-api/using-scan-queries.md) and [continuous queries](../continuous-queries.md).
- Stream transformers, receivers and visitors used with [data streamers](../data-streaming.md#data-streamers).
- [Entry processors](../colocating-computations.md#entry-processor).

When defining the classes listed above, we recommend that each class is created as either a separate class or inner static class and not as a lambda or anonymous inner class. Non-static inner classes are serialized together with its enclosing class. If some fields of the enclosing class cannot be serialized, you will get serialization exceptions.

{% hint style="warning" %}
The peer class loading functionality does not deploy the key and object classes of the entries stored in caches.
{% endhint %}

{% hint style="warning" %}
The peer class loading functionality allows any client to deploy custom code to the cluster. If you want to use it in production environments, make sure only authorized clients have access to the cluster.
{% endhint %}

This is what happens when a class is required on remote nodes:

- GridGain checks if the class is available in the local classpath, i.e. if it has been loaded at system initialization, and if it has, it is returned. No class loading from a peer node takes place in this case.
- If the class is not available locally, then a request for the class definition is sent to the originating node. The originating node sends the class's byte-code and the class is loaded on the worker node. This happens once per class. When the class definition is loaded on a node, it does not have to be loaded again.

{% hint style="info" %}
**Deploying 3rd Party Libraries**

When utilizing peer class loading, you should be aware of the libraries that get loaded from peer nodes vs. libraries that are already available locally in the class path. We suggest you should include all 3rd party libraries into the class path of every node. This can be achieved by copying your JAR files into the `{GRIDGAIN_HOME}/libs` folder. This way you do not transfer megabytes of 3rd party classes to remote nodes every time you change a line of code.
{% endhint %}

## Enabling Peer Class Loading

Here is how you can configure peer class loading:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <!-- Enable peer class loading. -->
    <property name="peerClassLoadingEnabled" value="true"/>
    <!-- Set deployment mode. -->
    <property name="deploymentMode" value="ISOLATED"/>

    <property name="discoverySpi">
        <bean class="org.apache.ignite.spi.discovery.tcp.TcpDiscoverySpi">
            <property name="ipFinder">
                <bean class="org.apache.ignite.spi.discovery.tcp.ipfinder.vm.TcpDiscoveryVmIpFinder">
                    <property name="addresses">
                        <list>
                            <value>127.0.0.1:47500..47509</value>
                        </list>
                    </property>
                </bean>
            </property>
        </bean>
    </property>
</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
IgniteConfiguration cfg = new IgniteConfiguration();

cfg.setPeerClassLoadingEnabled(true);
cfg.setDeploymentMode(DeploymentMode.CONTINUOUS);

// Start the node.
Ignite ignite = Ignition.start(cfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var cfg = new IgniteConfiguration
{
    PeerAssemblyLoadingMode = PeerAssemblyLoadingMode.CurrentAppDomain
};
var ignite = Ignition.Start(cfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

The following table describes parameters related to peer class loading.

|Parameter| Description | Default value|
|---|---|---|
|`peerClassLoadingEnabled`| Enables/disables peer class loading. | `false`|
|`deploymentMode` | The peer class loading mode. | `SHARED`|
| `peerClassLoadingExecutorService` | Configures a thread pool to be used for peer class loading. If not configured, a default pool is used.  | `null`|
| `peerClassLoadingExecutorServiceShutdown` |Peer class loading executor service shutdown flag. If the flag is set to `true`, the peer class loading thread pool is forcibly shut down when the node stops. | `true`|
|`peerClassLoadingLocalClassPathExclude` |List of packages in the system class path that should be P2P loaded even if they exist locally. | `null`|
|`peerClassLoadingMissedResourcesCacheSize`| Size of missed resources cache. Set to 0 to avoid caching of missing resources. | 100|

## Peer Class Loading Modes

### PRIVATE and ISOLATED

Classes deployed within the same class loader on the master node still share the same class loader remotely on worker nodes.
However, the tasks deployed from different master nodes does not share the same class loader on worker nodes.
This is useful in development environments when different developers can be working on different versions of the same classes.
There is no difference between `PRIVATE` and `ISOLATED` deployment modes since the `@UserResource` annotation has been removed.
Both constants were kept for backward-compatibility reasons and one of them is likely to be removed in a future major release.

In this mode, classes get un-deployed when the master node leaves the cluster.

### SHARED

This is the default deployment mode.
In this mode, classes from different master nodes with the same user version share the same class loader on worker nodes.
Classes are un-deployed when all master nodes leave the cluster or the user version changes.
This mode allows classes coming from different master nodes to share the same instances of user resources on remote nodes (see below).
This method is specifically useful in production as, in comparison to `ISOLATED` mode which has a scope of a single class loader on a single master node, `SHARED` mode broadens the deployment scope to all master nodes.

In this mode, classes get un-deployed when all the master nodes leave the cluster.

### CONTINUOUS

In `CONTINUOUS` mode, the classes do not get un-deployed when master nodes leave the cluster.
Un-deployment only happens when a class user version changes.
The advantage of this approach is that it allows tasks coming from different master nodes to share the same instances of user resources on worker nodes.
This allows the tasks executing on worker nodes to reuse, for example, the same instances of connection pools or caches.
When using this mode, you can start up multiple stand-alone worker nodes, define user resources on the master nodes, and have them initialized once on worker nodes regardless of which master node they came from.
In comparison to the `ISOLATED` deployment mode which has a scope of a single class loader on a single master node, `CONTINUOUS` mode broadens the deployment scope to all master nodes which is specifically useful in production.

In this mode, classes do not get un-deployed even if all the master nodes leave the cluster.

## Un-Deployment and User Versions

The classes deployed with peer class loading have their own lifecycle. On certain events (when the master node leaves or the user version changes, depending on deployment mode), the class information is un-deployed from the cluster: the class definition is erased from all nodes and the user resources linked with that class definition are also optionally erased (again, depending on deployment mode).

User version comes into play whenever you want to redeploy classes deployed in `SHARED` or `CONTINUOUS` modes. By default, GridGain  automatically detects if the class loader has changed or a node is restarted. However, if you would like to change and redeploy the code on a subset of nodes, or in the case of `CONTINUOUS` mode, kill every living deployment, you should change the user version.
User version is specified in the `META-INF/ignite.xml` file of your class path as follows:

```xml
<!-- User version. -->
<bean id="userVersion" class="java.lang.String">
    <constructor-arg value="0"/>
</bean>
```

By default, all GridGain startup scripts (ignite.sh or ignite.bat) pick up the user version from the `IGNITE_HOME/config/userversion` folder. Usually, you just need to update the user version under that folder. However, in case of GAR or JAR deployment, you should remember to provide the `META-INF/ignite.xml` file with the desired user version in it.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
