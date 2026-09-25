---
description: >-
  How to implement, deploy, access, and re-deploy GridGain services, including
  deployment strategies, interceptors, and the IgniteServices framework.
---

# Services

## Overview

A service is a piece of functionality that can be deployed to a GridGain cluster and execute specific operations.
You can have multiple instances of a service on one or multiple nodes.

GridGain services have the following features:

**Load balancing**

In all cases, other than singleton service deployment, GridGain automatically makes sure that approximately equal number of services are deployed on each node within the cluster. Whenever cluster topology changes, GridGain re-evaluates service deployments and may re-deploy an already deployed service to another node for better load balancing.

**Fault tolerance**

GridGain guarantees that services are continuously available, and are deployed according to the specified configuration, regardless of any topology changes or node crashes.

**Hot Redeployment**

You can use GridGain's `DeploymentSpi` configuration to re-deploy services without restarting the cluster. See [Re-deploying Services](#re-deploying-services).

GridGain services can be used as a backbone of a micro-services based solution or application. Learn more about this use case from the following series of articles:

- [Microservices on Top of Apache Ignite - Part I](https://dzone.com/articles/running-microservices-on-top-of-in-memory-data-gri)
- [Microservices on Top of Apache Ignite - Part II](https://dzone.com/articles/running-microservices-on-top-of-in-memory-data-gri-1)
- [Microservices on Top of Apache Ignite - Part III](https://dzone.com/articles/microservices-on-top-of-an-in-memory-data-grid-par)

Refer to a service example implementation in the Apache Ignite [examples](https://github.com/apache/ignite/tree/master/examples/src/main/java/org/apache/ignite/examples/servicegrid).

## Implementing a Service

A service implements the Service interface.
The `Service` interface has three methods:

- `init()`: this method is called by Ignite before the service is deployed (and before the `execute()` method is called)
- `execute()`: starts execution of the service
- `cancel()`:  cancels service execution

In .NET, implement the [`IService`](https://www.gridgain.com/sdk/gridgain8/latest/dotnetdoc/api/Apache.Ignite.Core.Services.IService.html) interface,
which declares the same three methods as `Init()`, `Execute()`, and `Cancel()`.
Each method receives an `IServiceContext` object that exposes the service name, the execution ID, and the cancellation flag.

## Deploying Services

You can deploy your service either programmatically at runtime, or by providing a service configuration as part of the node configuration.
In the latter case, the service is deployed when the cluster starts.

### Deploying Services at Runtime

You can deploy services at runtime via the instance of `IgniteServices`, which can be obtained from an instance of `Ignite` by calling the `Ignite.services()` method.

The `IgniteServices` interface has a number of methods for deploying services:

- `deploy(ServiceConfiguration)` deploys a service defined by a given configuration.
- `deployNodeSingleton(...)` ensures that an instance of the service is running on each server node.
- `deployClusterSingleton(...)` deploys a single instance of the service per cluster. If the cluster node on which the service is deployed stops, GridGain automatically redeploys the service on another node.
- `deployKeyAffinitySingleton(...)` deploys a single instance of the service on the primary node for a given cache key.
- `deployMultiple(...)` deploys the given number of instances of the service.

This is an example of cluster singleton deployment:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

//get the services interface associated with all server nodes
IgniteServices services = ignite.services();

//start a node singleton
services.deployClusterSingleton("myCounterService", new MyCounterServiceImpl());
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

// Get the services interface associated with all server nodes.
var services = ignite.GetServices();

// Deploy a cluster singleton.
services.DeployClusterSingleton("myCounterService", new MyCounterServiceImpl());
```

In .NET, the equivalent interface is [`IServices`](https://www.gridgain.com/sdk/gridgain8/latest/dotnetdoc/api/Apache.Ignite.Core.Services.IServices.html),
obtained by calling `IIgnite.GetServices()`.
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

And here is how to deploy a cluster singleton using `ServiceConfiguration`:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

ServiceConfiguration serviceCfg = new ServiceConfiguration();

serviceCfg.setName("myCounterService");
serviceCfg.setMaxPerNodeCount(1);
serviceCfg.setTotalCount(1);
serviceCfg.setService(new MyCounterServiceImpl());

ignite.services().deploy(serviceCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

var serviceCfg = new ServiceConfiguration
{
    Name = "myCounterService",
    MaxPerNodeCount = 1,
    TotalCount = 1,
    Service = new MyCounterServiceImpl()
};

ignite.GetServices().Deploy(serviceCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Deploying Services at Node Startup

You can specify your service as part of the node configuration and start the service together with the node.
If your service is a node singleton, the service is started on each node of the cluster.
If the service is a cluster singleton, it is started in the first cluster node, and is redeployed to one of the other nodes if the first node terminates.
The service must be available on the classpath of each node.

Below is an example of configuring a cluster singleton service:

{% tabs %}
{% tab title="XML" %}
```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">

    <property name="serviceConfiguration">
        <list>
            <bean class="org.apache.ignite.services.ServiceConfiguration">
                <property name="name" value="myCounterService"/>
                <property name="maxPerNodeCount" value="1"/>
                <property name="totalCount" value="1"/>
                <property name="service">
                    <bean class="org.apache.ignite.snippets.services.MyCounterServiceImpl"/>
                </property>
            </bean>
        </list>
    </property>

</bean>
```
{% endtab %}

{% tab title="Java" %}
```java
ServiceConfiguration serviceCfg = new ServiceConfiguration();

serviceCfg.setName("myCounterService");
serviceCfg.setMaxPerNodeCount(1);
serviceCfg.setTotalCount(1);
serviceCfg.setService(new MyCounterServiceImpl());

IgniteConfiguration igniteCfg = new IgniteConfiguration()
        .setServiceConfiguration(serviceCfg);

// Start the node.
Ignite ignite = Ignition.start(igniteCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Deploying to a Subset of Nodes

When you obtain the `IgniteServices` interface by calling `ignite.services()`, the `IgniteServices` instance is associated with all server nodes.
It means that GridGain chooses where to deploy the service from the set of all server nodes.
You can change the set of nodes considered for service deployment by using various approaches describe below.

### Cluster Singleton

A cluster singleton is a deployment strategy where there is only one instance of the service in the cluster, and GridGain guarantees that the instance is always available.
In case the cluster node on which the service is deployed crashes or stops, GridGain automatically redeploys the instance to another node.

### ClusterGroup

You can use the `ClusterGroup` interface to deploy services to a subset of nodes.
If the service is a node singleton, the service is deployed on all nodes from the subset.
If the service is a cluster singleton, it is deployed on one of the nodes from the subset.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

//deploy the service to the nodes that host the cache named "myCache" 
ignite.services(ignite.cluster().forCacheNodes("myCache"));

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

// Get the services interface associated with the nodes
// that host the cache named "myCache".
var services = ignite.GetCluster().ForCacheNodes("myCache").GetServices();
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Node Filter

You can use node attributes to define the subset of nodes meant for service deployment.
This is achieved by using a node filter.
A node filter is an `IgnitePredicate<ClusterNode>` that GridGain calls for each node associated with the `IgniteService` interface.
If the predicate returns `true` for a given node, the node is included.

{% hint style="warning" %}
The class of the node filter must be present in the classpath of all nodes.
{% endhint %}

Here is an example of a node filter.
The filter includes the server nodes that have the "west.coast.node" attribute.

{% tabs %}
{% tab title="Java" %}
```java
public static class ServiceFilter implements IgnitePredicate<ClusterNode> {
    @Override
    public boolean apply(ClusterNode node) {
        // The service will be deployed on the server nodes
        // that have the 'west.coast.node' attribute.
        return !node.isClient() && node.attributes().containsKey("west.coast.node");
    }
}
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
class ServiceFilter : IClusterNodeFilter
{
    public bool Invoke(IClusterNode node)
    {
        // The service is deployed on the server nodes
        // that have the 'west.coast.node' attribute.
        return !node.IsClient && node.TryGetAttribute<object>("west.coast.node", out _);
    }
}
```

In .NET, a node filter implements the `IClusterNodeFilter` interface, whose `Invoke()` method returns `true` for the nodes to include.
The assembly that contains the filter class must be loaded on all nodes.
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

Deploy the service using the node filter:

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

ServiceConfiguration serviceCfg = new ServiceConfiguration();

// Setting service instance to deploy.
serviceCfg.setService(new MyCounterServiceImpl());
serviceCfg.setName("serviceName");
serviceCfg.setMaxPerNodeCount(1);

// Setting the nodes filter.
serviceCfg.setNodeFilter(new ServiceFilter());

// Getting an instance of IgniteService.
IgniteServices services = ignite.services();

// Deploying the service.
services.deploy(serviceCfg);

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

var serviceCfg = new ServiceConfiguration
{
    // The service instance to deploy.
    Service = new MyCounterServiceImpl(),

    Name = "serviceName",
    MaxPerNodeCount = 1,

    // The node filter.
    NodeFilter = new ServiceFilter()
};

// Deploy the service.
ignite.GetServices().Deploy(serviceCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

### Cache Key

Affinity-based deployment allows you to deploy a service to the primary node for a specific key in a specific cache.
Refer to the [Affinity Colocation](../../architecture/data-modeling/affinity-colocation.md) section for details.
For an affinity-base deployment, specify the desired cache and key in the service configuration.
The cache does not have to contain the key. The node is determined by the affinity function.
If the cluster topology changes in a way that the key is re-assigned to another node, the service is redeployed to that node as well.

{% tabs %}
{% tab title="Java" %}
```java
Ignite ignite = Ignition.start();

//making sure the cache exists
ignite.getOrCreateCache("orgCache");

ServiceConfiguration serviceCfg = new ServiceConfiguration();

// Setting service instance to deploy.
serviceCfg.setService(new MyCounterServiceImpl());

// Setting service name.
serviceCfg.setName("serviceName");
serviceCfg.setTotalCount(1);

// Specifying the cache name and key for the affinity based deployment.
serviceCfg.setCacheName("orgCache");
serviceCfg.setAffinityKey(123);

IgniteServices services = ignite.services();

// Deploying the service.
services.deploy(serviceCfg);

```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
var ignite = Ignition.Start();

// Make sure the cache exists.
ignite.GetOrCreateCache<int, string>("orgCache");

var serviceCfg = new ServiceConfiguration
{
    // The service instance to deploy.
    Service = new MyCounterServiceImpl(),

    Name = "serviceName",
    TotalCount = 1,

    // The cache name and key for the affinity-based deployment.
    CacheName = "orgCache",
    AffinityKey = 123
};

// Deploy the service.
ignite.GetServices().Deploy(serviceCfg);
```
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Accessing Services

You can access the service at runtime via a service proxy.
Proxies can be either _sticky_ or _non-sticky_.
A sticky proxy always connects to the same cluster node to access a remotely deployed service.
A non-sticky proxy load-balances remote service invocations among all cluster nodes on which the service is deployed.

The following code snippet obtains a non-sticky proxy to the service and calls a service method:

{% tabs %}
{% tab title="Java" %}
```java
//access the service by name
MyCounterService counterService = ignite.services().serviceProxy("myCounterService",
        MyCounterService.class, false); //non-sticky proxy

//call a service method
counterService.increment();
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
// Access the service by name. Proxies are non-sticky by default: when a service
// is deployed on multiple nodes, calls are load-balanced between the instances.
// Pass sticky: true to always call the same service instance.
var counterService = ignite.GetServices()
    .GetServiceProxy<IMyCounterService>("myCounterService", sticky: false);

// Call a service method.
counterService.Increment();
```

The .NET thin client can also call services. See [Calling Services]({connectors}/thin-clients/dotnet-thin-client#calling-services) for details, including how to invoke a service asynchronously.
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Service Call Interceptors

{% hint style="warning" %}
This API is experimental and may change in future releases.
{% endhint %}

You can intercept calls to service methods with one or more _service call interceptors_.
An interceptor lets you add middleware logic — such as security checks, auditing, logging, or metrics — that applies to all business methods of a service without changing the service implementation.

A service call interceptor implements the `ServiceCallInterceptor` interface, which has a single method:

```java
public Object invoke(String mtd, Object[] args, ServiceContext ctx, Callable<Object> next) throws Exception;
```

The interceptor receives the method name, the method arguments, and the service context.
Call `next.call()` to pass control to the next interceptor in the chain; the last interceptor in the chain invokes the service method itself.

{% hint style="info" %}
Interceptors apply only to the service's business methods. The lifecycle methods `init()`, `execute()`, and `cancel()` are not intercepted.
{% endhint %}

You register interceptors on the `ServiceConfiguration` object with the `setInterceptors()` method.
When you specify multiple interceptors, they run in the order in which you pass them.

{% tabs %}
{% tab title="Java" %}
```java
// An interceptor that audits every service method call.
ServiceCallInterceptor audit = (mtd, args, ctx, next) -> {
    String sessionId = ctx.currentCallContext().attribute("sessionId");
    AuditProvider prov = AuditProvider.get();

    // Record an event before the method is executed.
    prov.recordStartEvent(ctx.name(), mtd, sessionId);

    try {
        // Execute the remaining interceptors and the service method.
        return next.call();
    }
    catch (Exception e) {
        prov.recordError(ctx.name(), mtd, sessionId, e.getMessage());

        throw e;
    }
    finally {
        // Record a finish event after the method is executed.
        prov.recordFinishEvent(ctx.name(), mtd, sessionId);
    }
};

ServiceConfiguration svcCfg = new ServiceConfiguration()
    .setName("service")
    .setService(new MyServiceImpl())
    .setMaxPerNodeCount(1)
    .setInterceptors(audit);

// Deploy the service.
ignite.services().deploy(svcCfg);
```
{% endtab %}

{% tab title="C#/.NET" %}
unsupported
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Un-deploying Services

To undeploy a service, use the `IgniteServices.cancel(serviceName)` or `IgniteServices.cancelAll()` methods.

{% tabs %}
{% tab title="Java" %}
```java
services.cancel("myCounterService");
```
{% endtab %}

{% tab title="C#/.NET" %}
```csharp
services.Cancel("myCounterService");
```

In .NET, the corresponding methods are `IServices.Cancel(name)` and `IServices.CancelAll()`.
{% endtab %}

{% tab title="C++" %}
unsupported
{% endtab %}
{% endtabs %}

## Re-deploying Services

If you want to update the implementation of a service without stopping the cluster, you can do it if you use the GridGain's [DeploymentSPI configuration](../code-deployment/deploying-user-code.md).

Use the following procedure to redeploy the service:

1. Update the JAR file(s) in the location where the service is stored (pointed to by your `UriDeploymentSpi.uriList` property). GridGain will reload the new classes after the configured update period.
2. Add the service implementation to the classpass of a client node and start the client.
3. Call the `Ignite.services().cancel()` method on the client node to stop the service.
4. Deploy the service from the client node.
5. Stop the client node.

In this way, you don't have to stop the server nodes, so you don't interrupt the operation of your cluster.

## Service Events

The services generate the following events:

|Event Type |Event Description |Where Event Is Fired|
|---|---|---|
|`EVT_SERVICE_METHOD_EXECUTION_STARTED`|Is raised right before a service method execution starts.|The node where the service method execution is failed.|
|`EVT_SERVICE_METHOD_EXECUTION_FINISHED`| Is raised right after a service method execution finishes.|The node where the service method execution is failed.|
|`EVT_SERVICE_METHOD_EXECUTION_FAILED`| Is raised in case a service method execution fails.|The node where the service method execution is failed.|

## New IgniteServices Framework

Starting from version 8.8.1, GridGain offers a newer framework for IgniteServices. We recommend to switch to this framework because it's better optimized and results in lower load on your cluster. To move to the new framework, turn the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` JVM property to `true`.

### Enabling the New Framework (with Downtime)

All nodes in the cluster (both server and client) must have the same `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` value. Therefore, the move to `true` will require a full restart of the cluster and the clients, which will result in downtime.

To move to the new implementation: 

1. Stop all nodes.
2. Change `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` to `true` on all nodes.
3. Restart all  nodes.

### Enabling the New Framework While Upgrading (with Downtime)

In GridGain 8.9.1 and above, `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED=true` by default. When upgrading to one of the GridGain 8.9.x versions, you will automatically move to the new service framework. However, this might also require downtime.

To move to the new framework while upgrading to a new GridGain version with downtime:

1. Stop all nodes.
2. Upgrade to 8.9.x.
3. Restart all nodes.

### Avoiding Downtime While Upgrading

If downtime is not an option in your environment, you can upgrade from GridGain 8.8.x to 8.9.x without enabling the new IgniteServices framework, using the [Rolling Upgrade](../../gridgain8-management/upgrade/rolling-upgrades.md).

#### Upgrading Server Nodes

To upgrade server nodes:

1. Make sure [Rolling Upgrades](../../gridgain8-management/upgrade/rolling-upgrades.md) are enabled.
2. Stop one of the server nodes.
3. Upgrade the version and set `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED=false` for the above server node.
4. Restart the above server node.
5. Repeat steps (2)-(4) for the remaining server nodes.

#### Upgrading Nodes with Thick Clients

To upgrade nodes with a thick client:

1. Stop the client node.
2. Upgrade to the new version.
3. (Optionally, starting from 8.9.4) Add to the configuration file `IGNITE_SERVICES_SET_REMOTE_FILTER_ON_START=true`.
4. Restart the node.
5. Repeat the above steps on the remaining nodes.

Setting `IGNITE_SERVICES_SET_REMOTE_FILTER_ON_START=true` on client nodes initiates optimizations that reduce load on the cluster (compared to the legacy framework). To set the above option to `true`, all server nodes must run GridGain 8.8.39 or above, or 8.9.4 or above. You can set `IGNITE_SERVICES_SET_REMOTE_FILTER_ON_START=true` on nodes while upgrading these nodes to the above GridGain versions.

### Enabling Optimizations with the Legacy Services Framework

To switch on optimizations for the legacy framework while upgrading to a new GridGain version (without downtime): 

1. Make sure that all server nodes have been upgraded to 8.8.39+ or 8.9.4+.
2. Stop a client node.
3. Upgrade the client node to the same version the server nodes had been upgraded to.
4. Set `IGNITE_SERVICES_SET_REMOTE_FILTER_ON_START=true` on the client node.
5. Restart the client node.

If your entire cluster (server and client nodes) is already on GridGain 8.8.39+ or 8.9.4+, all you need to do to switch on the optimizations is to set `IGNITE_SERVICES_SET_REMOTE_FILTER_ON_START=true` when reloading your thick client.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
