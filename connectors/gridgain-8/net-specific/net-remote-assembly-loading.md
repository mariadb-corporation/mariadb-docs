---
description: >-
  Enable remote (peer) assembly loading in GridGain.NET so compute tasks and their
  dependencies are deployed automatically across cluster nodes.
---

# Remote Assembly Loading

## Overview

Many GridGain APIs involve remote code execution. For example, GridGain compute tasks are serialized, sent to remote nodes, and executed there.
However, by default, .NET assemblies (DLL files) with those tasks in, must be loaded on remote nodes in order to instantiate
and deserialize tasks' instances.

Before version 2.1 you had to manually load assemblies (using `-assembly` switch with `Apache.Ignite.exe` or some other ways).
Starting Ignite 2.1 you can take advantage of the remote assembly loading feature, that can be enabled with the
`IgniteConfiguration.PeerAssemblyLoadingMode` flag. This configuration property needs to have the same value on all nodes
in the cluster. Another available mode is `CurrentAppDomain`.

## CurrentAppDomain Mode

`PeerAssemblyLoadingMode.CurrentAppDomain` enables automatic on-demand assembly requests to other nodes in cluster,
loading assemblies into [AppDomain](https://msdn.microsoft.com/en-us/library/system.appdomain.aspx) where Ignite node runs.

Consider the following code:

```csharp
// Print Hello World on all cluster nodes.
ignite.GetCompute().Broadcast(new HelloAction());

class HelloAction : IComputeAction
{
  public void Invoke()
  {
    Console.WriteLine("Hello World!");
  }
}
```

- GridGain serializes the `HelloAction` instance and broadcasts to every node in the cluster.
- Remote nodes attempt to deserialize the `HelloAction` instance. If there is no such class in the currently loaded or referenced assemblies,
the nodes request an assembly with the class from the node that initiated the compute task or from other nodes (if necessary).
- The assembly file is sent from the originating or other node as a byte array and loaded with the `Assembly.Load(byte[])` method.

### Versioning

[Assembly-qualified type name](https://msdn.microsoft.com/en-us/library/system.type.assemblyqualifiedname.aspx)
includes the assembly version and is used to resolve types.

If you keep the cluster running, do this change in the logic and see how the assembly gets reloaded automatically:

- Modify `HelloAction` instance to print something else
- Change [AssemblyVersion](https://msdn.microsoft.com/en-us/library/system.reflection.assemblyversionattribute.aspx)
- Recompile and run the application code
- The new version of the assembly will be deployed and executed on other nodes.

Note, if you keep the `AssemblyVersion` unchanged, Ignite will use existing assembly that was previously loaded, since
there are no changes in the type name.

Assemblies with different versions can co-exist and be used side by side. Some nodes can continue running old code, while
other nodes can execute computations with a newer version of the same class.

The `AssemblyVersion` attribute can include asterisk (`*`) to enable the auto-increment on build: `[assembly: AssemblyVersion("1.0.*")]`.
This way you can keep the cluster running, repeatedly modify and run computations, and new assembly versions will be deployed every time.

### Dependencies

Dependent assemblies are also loaded automatically, e.g. when `ComputeAction` calls some code from a different assembly.
Keep that in mind when using heavy frameworks and libraries: single compute call can cause lots of assemblies to be sent over the network.

### Unloading

.NET does not allow assembly unloading. Instead, only the entire `AppDomain` can be unloaded with all assemblies.
Currently available `CurrentAppDomain` mode uses existing `AppDomain`, which means all peer-deployed assemblies will stay
loaded while current `AppDomain` lives. This may cause increased memory usage.
</content>
