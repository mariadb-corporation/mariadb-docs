---
hidden: true
description: >-
  Start and configure standalone GridGain.NET nodes from the command line, XML files,
  or as a Windows service, and load user assemblies for remote code execution.
---

# GridGain.NET Standalone Nodes

## Overview

An GridGain.NET node can be started within the code of a .NET application by using `Ignition.Start()` or as a separate
process with `Apache.Ignite.exe` executable located under `{apache_ignite_release}\platforms\dotnet\bin` folder.
Internally `Apache.Ignite.exe` references `Apache.Ignite.Core.dll` and uses `Ignition.Start()` as you would normally do,
and can be configured with command line arguments, listed below, by passing them as command line options or setting directly
in `Apache.Ignite.exe.config` file.

Usually, you start server nodes in the standalone mode. An Ignite cluster is a group of server nodes interconnected
together in order to provide shared resources like RAM and CPU to your applications.

## Prerequisites

When launching a GridGain.NET node, [.NET SDK 8 or later](https://dotnet.microsoft.com/download/dotnet) and [Java 8 or later](http://www.oracle.com/technetwork/java/javase/downloads/index.html) are required.

{% hint style="info" %}
.NET 8 is only required to run a GridGain.NET node using the provided binary (`Apache.Ignite.Executable` on macOS and Linux, `Apache.Ignite.exe` on Windows). When using Ignite as a library in your own code, the minimum requirement is `netstandard2.0`, which is implemented by .NET Core 2.0+ and .NET Framework 4.6.1+
{% endhint %}

## Starting a Standalone Node via Command Line

Below you can see basic Ignite parameters that can be passed as command line arguments when a node is started with
`Apache.Ignite.exe` executable:

| Command Line Argument | Description |
|---|---|
| `-IgniteHome` | A path to Ignite installation directory (if not provided, the `IGNITE_HOME` environment variable is used) |
| `-ConfigFileName` | A path to the app.config file (if not provided, `Apache.Ignite.exe.config` is used). |
| `-ConfigSectionName` | The name of the `IgniteConfigurationSection` from a configuration file. |
| `-SpringConfigUrl` | A path to a Spring configuration file. |
| `-JvmDllPath` | A path to JVM library `jvm.dll` (if not provided, `JAVA_HOME` environment variable is used). |
| `-JvmClasspath` | The classpath to pass to JVM started by GridGain.NET internally (use to enlist additional JAR files). |
| `-SuppressWarnings` | Whether or not to print warnings. |
| `-J<javaOption>` | Additional JVM options to be used during the initialization of the JVM. |
| `-Assembly` | Additional .NET assemblies to be loaded. |
| `-JvmInitialMemoryMB` | Initial Java heap size, in megabytes. Maps to the `-Xms` Java parameter. |
| `-JvmMaxMemoryMB` | Maximum Java heap size, in megabytes. Maps to the `-Xmx` Java parameter. |
| `/install` | Installs Ignite Windows service with provided options. |
| `/uninstall` | Uninstalls Ignite Windows service. |

```bash
Apache.Ignite.exe -ConfigFileName=c:\ignite\my-config.xml -ConfigSectionName=igniteConfiguration -Assembly=c:\ignite\my-code.dll -J-Xms1024m -J-Xmx2048m
```

You can also start the node by using the `Apache.Ignite.Executable.dll` on any system:

```bash
dotnet platforms/dotnet/bin/net8.0/Apache.Ignite.Executable.dll -ConfigFileName=c:\ignite\my-config.xml -ConfigSectionName=igniteConfiguration -Assembly=c:\ignite\my-code.dll -J-Xms1024m -J-Xmx2048m
```

On Linux systems, you can use the `Apache.Ignite.Executable`:

```bash
chmod +x platforms/dotnet/bin/net8.0/Apache.Ignite.Executable
platforms/dotnet/bin/net8.0/Apache.Ignite.Executable -ConfigFileName=c:\ignite\my-config.xml -ConfigSectionName=igniteConfiguration -Assembly=c:\ignite\my-code.dll -J-Xms1024m -J-Xmx2048m
```

## Configure Standalone Node via XML Files

A standalone node can be configured with app.config XML or Spring XML (or both). Every command line argument, listed above,
can also be used in `Apache.Ignite.exe.config` under `appSettings` section:

{% code title="Apache.Ignite.exe.config" %}
```xml
<configuration>
  <configSections>
    <section name="igniteConfiguration" type="Apache.Ignite.Core.IgniteConfigurationSection, Apache.Ignite.Core" />
  </configSections>

  <igniteConfiguration springConfigUrl="c:\ignite\spring.xml">
    <cacheConfiguration name="myCache" cacheMode="Replicated" />
  </igniteConfiguration>

  <appSettings>
    <add key="Ignite.Assembly.1" value="my-assembly.dll"/>
    <add key="Ignite.Assembly.2" value="my-assembly2.dll"/>
    <add key="Ignite.ConfigSectionName" value="igniteConfiguration" />
  </appSettings>
</configuration>
```
{% endcode %}

This example defines the `igniteConfiguration` section and uses it to start Ignite via the `Ignite.ConfigSectionName` setting.
It also references the Spring XML configuration file, whose settings will be added to the specified configuration.

## Load User Assemblies

Some Ignite APIs involve remote code execution and require you to load assemblies with your code into `Apache.Ignite.exe`
via `-Assembly` command line argument or `Ignite.Assembly` app setting.

The following functionality requires a corresponding assembly to be loaded on all nodes:

- ICompute (supports automatic loading, see [Remote Assembly Loading](net-remote-assembly-loading.md))
- Scan Queries with filter
- Continuous Queries with filter
- ICache.Invoke methods
- ICache.LoadCache with filter
- IServices
- IMessaging.RemoteListen
- IEvents.RemoteQuery

{% hint style="info" %}
**Missing User Assemblies**

If a user assembly cannot be located a `Could not load file or assembly 'MyAssembly'` or one of its dependencies
exception will be thrown.

Note, that it is also necessary to add any dependencies of the user assembly to the list.
{% endhint %}

## GridGain.NET as Windows Service

`Apache.Ignite.exe` can be installed as a Windows Service so it is started automatically via `/install` command line argument.
All other command line arguments will be preserved and used each time the service starts. Use `/uninstall` to uninstall the service.

```bash
Apache.Ignite.exe /install -J-Xms513m -J-Xmx555m -ConfigSectionName=igniteConfiguration
```
</content>
