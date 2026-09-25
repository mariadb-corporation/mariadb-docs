---
description: >-
  Use .NET Core to build and run a simple Hello World example that starts a
  node, puts a value into the cache, and then gets the value.
---

# GridGain Quick Start Guide for .NET/C#

This chapter explains how to use .NET Core to build and run a simple Hello World example that starts a node, puts a value into the cache, and then gets the value.

## Prerequisites

GridGain.NET was officially tested on:

{% include "../../.gitbook/includes/gg8-dotnet-prerequisites.md" %}

### (Optional) Open Ports

Depending on your environment and what your plan is, you may want to open additional ports. GridGain uses the following ports:

- 47100-47200 — ports used by GridGain nodes to communicate. Specific ports used depend on node configuration.
- 47500-47600 — ports used by GridGain nodes to discover other nodes in the network. Specific ports used depend on node configuration.
- 10800 — the port used for [thin clients]({connectors}/thin-clients/getting-started-with-thin-clients), [JDBC]({connectors}/sql/jdbc/jdbc-driver) and [ODBC]({connectors}/sql/odbc/odbc-driver) connections.
- 8080 — the port used for [REST API](../../reference/rest-api/README.md).
- 11211 — the port used by [control script](../../reference/cli-tool/README.md) calls. This port should only be opened on nodes that need to send control script messages to other nodes.

## Running a Simple .NET Example

{% hint style="info" %}
GridGain for .NET supports a thick client and a thin client. As this guide focuses on the _thick_ client, you can run the example below after adding the GridGain-Ignite library package.
You do not need to download and install the GridGain distribution to run the example. See [Thick vs. Thin Clients section](../concepts.md#thick-vs.-thin-clients) for more information about the differences between thick and thin clients in GridGain.

For information about the .NET thin client, see [.NET Thin Client]({connectors}/thin-clients/dotnet-thin-client).
{% endhint %}

{% hint style="warning" %}
If you use the thick client without downloading and installing GridGain distribution, some functionality (Logging, etc.) will be missing or not configured.
{% endhint %}

1. Use the CLI (unix shell, Windows CMD or PowerShell, etc.) to run the following two commands:

   `> dotnet new console`

   This creates an empty project, which includes a project file with metadata and a .cs file with code.

   And:

   ```shell
   > dotnet add package GridGain --version {gridgain.version}
   ```

   This modifies the project file - `.csproj` - to add dependencies.

2. Open `Program.cs` in any text editor and replace the contents as follows:

   ```csharp
   using System;
   using Apache.Ignite.Core;
   using GridGain.Core;

   namespace GridGain.GettingStarted
   {
       class Program
       {
           static void Main()
           {
               var cfg = new IgniteConfiguration
               {
                   PluginConfigurations = new[]
                   {
                       // Enable GridGain plugin.
                       new GridGainPluginConfiguration()
                   }
               };

               IIgnite ignite = Ignition.Start(cfg);

               var cache = ignite.GetOrCreateCache<int, string>("my-cache");
               cache.Put(1, "Hello, World");
               Console.WriteLine(cache.Get(1));

               IGridGain gridGain = ignite.GetGridGain();
               Console.WriteLine(gridGain.GetProduct().GetLicense());
           }
       }
   }
   ```

3. Save and then run the program:

   `> dotnet run`

As a result, you should see a node launch and the "Hello, World" text displayed right after the launch.

## Next Steps

From here, you may want to:

- Read more about using GridGain: [Developers Guide](../../gridgain8-usage/README.md), [Administrators Guide](../../gridgain8-management/README.md)
- Use [GridGain Control Center]({tools}/control-center) to monitor your cluster

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
