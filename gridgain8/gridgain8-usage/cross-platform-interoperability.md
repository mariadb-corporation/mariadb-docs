---
description: >-
  How .NET, Java, and C++ platforms interoperate in a mixed GridGain cluster,
  including type compatibility and calling a .NET service from Java.
---

# Cross-Platform Interoperability

GridGain allows different platforms, such as .NET, Java and C++, to interoperate with each other.
Classes defined on different platforms could be converted to each other.

## Type Compatibility

## Mixed Cluster

Java, .NET and .C++ nodes can join the same cluster.

All platforms are built on top of Java, so any node can execute Java computations.
However, .NET and C++ computations can be executed only on the nodes launched from the corresponding platform.

The following .NET functionality is not supported when there is at least one non-.NET node in the cluster:

- Scan Queries with filter
- Continuous Queries with filter
- ICache.Invoke methods
- ICache.LoadCache with filter
- IMessaging.RemoteListen
- IEvents.RemoteQuery

## Calling a .NET Service from Java

Services are an exception to the restrictions above: a .NET service deployed in a mixed cluster can be called from Java nodes.
The service instance still runs on .NET nodes, so the assembly that contains it must be loaded on those nodes.
See [Standalone Nodes]({connectors}/dotnet/net-standalone-nodes) for how to load user assemblies, and [Services](services/services.md) for deployment options.

To call the service from Java, declare a Java interface that mirrors the methods you want to call.
Because .NET and Java use different naming conventions, map each method to its .NET counterpart with the `@PlatformServiceMethod` annotation.

In the example below, `DotnetService` is your own type in both languages: a .NET class that implements
[`IService`](https://www.gridgain.com/sdk/gridgain8/latest/dotnetdoc/api/Apache.Ignite.Core.Services.IService.html), and a Java interface that declares the methods to call.
The two names do not have to match, because the service is resolved by its deployment name.

{% tabs %}
{% tab title="C#/.NET" %}
```csharp
// Your service implementation.
public class DotnetService : IService
{
    public int AddOne(int x) => x + 1;

    // IService implementation omitted.
}

// Deploy it under the name "dotnet-service".
ignite.GetServices().DeployClusterSingleton("dotnet-service", new DotnetService());
```
{% endtab %}

{% tab title="Java" %}
```java
// Your Java view of the same service.
public interface DotnetService {
    @PlatformServiceMethod("AddOne") // Map to the .NET method name.
    int addOne(int x);
}

DotnetService svc = ignite.services().serviceProxy("dotnet-service", DotnetService.class, false);

int y = svc.addOne(5);
```
{% endtab %}
{% endtabs %}

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
