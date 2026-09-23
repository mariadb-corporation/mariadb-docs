---
description: >-
  GridGain 9.1.10 adds ADO.NET integration, ZIP-based deployment units, improved CDC monitoring, and rolling upgrade improvements.
---

# GridGain 9.1.10 Release Notes

## Overview

GridGain 9.1.10 is a private release that fixes the known issue from the previous release and provides support for WASM compute jobs.

## Major Changes

### Rolling Upgrade Improvements

This release features a major change in rolling upgrade procedure that makes it impossible to skip over during rolling upgrades. Rolling upgrade to GridGain 9.1.10 from an earlier version and from GridGain 9.1.10 to a later version is supported, however you must use it during the upgrade procedure (for example, upgrade from 9.1.8 to 9.1.10 and then to 9.1.11).

This is only required for rolling upgrades, upgrades with downtime are not affected.

## New Features

### ADO.NET Integration

This release adds integration with [ADO.NET](../../developers-guide/clients/ado.md). You can install it in the same way as you install the .NET client. Once installed, you execute SQL commands, read data from the cluster and manage transactions via ADO.

The example below shows how you can execute an SQL command:

```csharp
var connStr = "Endpoints=localhost:10800";
await using var conn = new IgniteDbConnection(connStr);
await conn.OpenAsync();
DbCommand cmd = conn.CreateCommand();
cmd.CommandText = "DROP TABLE IF EXISTS Person";
await cmd.ExecuteNonQueryAsync();
```

For more information, see [ADO.NET](../../developers-guide/clients/ado.md) documentation.

### Deployment Units

With this release, you can deploy your code in a `zip` archive preserving its folder structure. To do this, you use the new `/management/v1/deployment/units/zip/{unitId}/{unitVersion}` REST endpoint. Once GridGain receives the archive, it will unpack it and the code will be available from your compute jobs.

For more information about code deployment, see [Code Deployment](../../developers-guide/code-deployment/code-deployment.md) documentation.

### Deployment Unit Context in Compute Jobs

You can now access information about deployment units from your compute jobs with the `JobExecutionContext` object. The object contains the collection of `DeploymentUnitInfo` objects that contain the information about the name, version and path to the deployment unit location.

The example below shows how you can get information about deployment units:

```java
public class DiagnosticJob implements ComputeJob<Void, String> {
    @Override
    public CompletableFuture<String> executeAsync(JobExecutionContext context, Void input) {
        // Access deployment unit information
        String deploymentInfo = context.deploymentUnits().stream()
            .map(unit -> String.format("%s:%s at %s",
                unit.name(),
                unit.version(),
                unit.path()))
            .collect(Collectors.joining(", "));
        return CompletableFuture.completedFuture(deploymentInfo);
    }
}
```

For more information about distributed computing, see [Compute](../../developers-guide/compute/compute.md) documentation.

### Improved CDC Monitoring

This release adds the new `cdc sink status` and `cdc source status` commands. These commands can be used to more accurately monitor [change data capture](../../administrators-guide/change-data-capture/change-data-capture.md).

### Improved CLI Tool Configuration for Docker

This release adds support for the new `GRIDGAIN_CLI_WORK_DIR` environment variable that can be used to configure the directory that will be used to store the files required for the [CLI tool](../../ignite-cli-tool.md) as well as its logs.

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-28884 | Platforms & Clients | Java thin: fixed read-only transaction read timestamp to reflect the transaction start time. |
| IGN-28866 | CLI Tool | When running CLI from the docker image, the configuration and log files are now written to the working directory in the container, /opt/gridgain/work/gridgain9cli by default. Use the GRIDGAIN_CLI_WORK_DIR environment variable to change it. |
| IGN-28865 | CLI Tool | You can now override JVM properties for the CLI tool by setting the GRIDGAIN9_OPTS environment variable. |
| IGN-28845 | General | Fixed a data corruption in "aimem" and "aipersist" engines when inserting data entries with certain very specific payload sizes. |
| IGN-28786 | Cluster SQL Engine | Fixed an issue that caused explicit read-only transactions to fail if the node containing a replica of the involved table left the cluster. |
| IGN-28781 | Code Deployment | Deployment units now support hierarchic structures. |
| IGN-28771 | Cluster Storage Engine | Fixed an issue that made it impossible to add new values to arrays in configuration. |
| IGN-28737 | Distributed Computing | Added JobExecutionContext.deploymentUnits to access arbitrary deployment unit content from a compute job. |
| IGN-24452 | Platforms and Clients | .NET: Added ADO.NET integration (IgniteDbColumn, IgniteDbCommand, IgniteDbConnection, IgniteDbConnectionStringBuilder, IgniteDbDataReader.cs, IgniteDbException.cs, IgniteDbParameter, IgniteDbParameterCollection, IgniteDbTransaction). |
| GG-45265 | Cluster Continuous Queries | Fixed inconsistent behavior when Continuous Query watermark is not set. |
| GG-45061 | Cluster Storage Engine | Improved Rolling Upgrade protocol to ensure upgrade consistency. |
| GG-44941 | Distributed Computing | Added compute.wasm.moduleMaxMemory configuration property to control WebAssembly module memory usage. |
| GG-44616 | Builds and Deliveries | Added cluster configuration parameter to GridGain helm chart. |
| GG-43519 | Cluster Data Snapshots and Recovery | Fixed creation of snapshots for tables that have "expire at" or "archive at" column. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.8`, `9.1.8`

{% hint style="info" %}
When updating from older versions, we recommend updating to version `9.1.8` instead.
{% endhint %}

## Known Limitations

### Rolling Upgrade Over 9.1.10

When performing a rolling upgrade from GridGain 9.1.9 or earlier, it is necessary to first upgrade to 9.1.10 before upgrading to 9.1.11 or a later version. This is caused by improvements in rolling upgrade procedure that make skipping 9.1.10 with a rolling upgrade impossible.

The upgrade to 9.1.10 must be performed for the whole cluster and committed before the next upgrade can be started.

You do not need to perform this intermediary upgrade when upgrading with downtime, as it only affects the rolling upgrade procedure.

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
