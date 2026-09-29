---
description: >-
  Call Java services from a GridGain.NET application, including service interface
  mapping and method resolution.
---

# Java Services Execution from Ignite.NET

## Overview

GridGain.NET can work with Java services the same way as with .NET services. To call a Java service from a .NET application, you need to know the interface of the service.

## Example

Let's review how to use this capability by taking a usage example.

### Create Java Service

{% code title="Java" %}
```java
public class MyJavaService implements Service {
  // Service method to be called from .NET
  public String testToUpper(String x) {
    return x.toUpperCase();
  }

  // Service interface implementation
  @Override public void cancel(ServiceContext context) { // No-op.  }
  @Override public void init(ServiceContext context) throws Exception { // No-op. }
  @Override public void execute(ServiceContext context) throws Exception { // No-op. }
}
```
{% endcode %}

This Java service can be deployed on any nodes (.NET, C++, Java-only), so there are no restrictions on deployment options:

{% code title="Java" %}
```java
ignite.services().deployClusterSingleton("myJavaSvc", new MyJavaService());
```
{% endcode %}

### Call Java Service From .NET

Create a version of the service interface for .NET:

{% code title="C#" %}
```csharp
// Interface can have any name
interface IJavaService
{
  // Method must have the same name (case-sensitive) and same signature:
  // argument types and order.
  // Argument names and return type do not matter.
  string testToUpper(string str);
}
```
{% endcode %}

Get the service proxy and invoke the method:

{% code title="C#" %}
```csharp
var config = new IgniteConfiguration
{
  // Make sure that Java service class is in classpath on all nodes, including .NET
  JvmClasspath = @"c:\my-project\src\Java\target\classes\"
}

var ignite = Ignition.Start(config);

// Make sure to use the same service name as in deployment
var prx = ignite.GetServices().GetServiceProxy<IJavaService>("myJavaSvc");
string result = prx.testToUpper("invoking Java service...");
Console.WriteLine(result);
```
{% endcode %}

## Interface Methods Mapping

The .NET service interface is mapped to its Java counterpart dynamically. This happens at the time of the method invocation:

- It is not necessary to specify all Java service methods in the .NET interface.
- The .NET interface can have members that are not present in Java service. You won't get any exception until you call these missing methods.

The Java methods are resolved the following way:

- Ignite looks for a method with the specified name and parameter count. If there is only one exist, Ignite will use it.
- Among the matched methods Ignite looks for a method with compatible arguments (via `Class.isAssignableFrom`). Ignite invoke the matched method or throws an exception in case of ambiguity.
- The method return type is ignored, since .NET and Java do not allow identical methods with different return types.

The return type is ignored when resolving the Java method, but it does determine how the .NET side invokes it. If you declare the method with a `Task`, `Task<TResult>`, `ValueTask`, or `ValueTask<TResult>` return type, the proxy returns a task that you can await. With the thin client, the invocation is asynchronous and the calling thread is not blocked; with the thick client shown above, the invocation is synchronous and the result is returned as an already-completed task. The Java service itself stays synchronous in both cases. See [Calling Services](../clients/dotnet-thin-client.md#calling-services) for an example.

See [Platform Interoperability, Type Compatibility section](net-platform-interoperability.md) for details on method arguments and result mapping. Note, that the `params/varargs` are also supported, since in .NET and Java these are syntactic sugar for object arrays.
