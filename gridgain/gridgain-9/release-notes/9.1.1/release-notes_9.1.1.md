---
description: >-
  GridGain 9.1.1 reworks CREATE ZONE syntax and adds snapshot encryption, .NET distributed computing, and further configuration and logging improvements.
---

# GridGain 9.1.1 Release Notes

## Overview

GridGain 9.1.1 is a big milestone release with support for new storage type, big license changes and a host of improvements and enhancements.

## Major Changes

### Configuration Changes

This release features a major rework of node and cluster configuration, making configuration names more consistent and reorganizing some parameters.

Below is the summary of the changes:

- All configuration property names now include the units used.
- A number of default values were changed to better work in real environments

You can continue using previously set up node and cluster configurations.

### CREATE ZONE Syntax Changes

The  [CREATE ZONE](../../sql-reference/distribution-zones.md) and [ALTER ZONE](../../sql-reference/distribution-zones.md#alter-zone) command syntax was significantly reworked. All additional parameters (specified in the `WITH` parameter) are now part of common syntax.

Below is the example of creating a distribution zone:

```sql
-- Previously used syntax.
CREATE ZONE IF NOT EXISTS "myExampleZone" WITH STORAGE_PROFILES='default', REPLICAS=3, PARTITIONS=2;

-- Current syntax.
CREATE ZONE IF NOT EXISTS "myExampleZone" (REPLICAS 3, PARTITIONS 2) STORAGE PROFILES['default'];
```

Previously used syntax is supported for backwards compatibility.

## New Features

### Snapshot Encryption

Starting with this release, if [data encryption](../../administrators-guide/security/tde.md) is enabled on the cluster, your snapshots will also be encrypted.

You can also manually set snapshot encryption when creating then by using the `encryption-provider` parameter.

```bash
cluster snapshot create --type=full --tables=PERSON --destination=relative-path-example --encryption-provider=keystore
```

### .NET Distributed Computing

This release adds support for .NET compute jobs and stream receivers. You can now implement your jobs and receivers in .NET (C#, F#, and others), deploy them to the cluster, and run them from any supported client or language.

Here is an example of a simple compute job:

```csharp
JobDescriptor<string, string> jobDesc = JobDescriptor.Of(new HelloJob()) with { DeploymentUnits = [...] };
var jobTarget = JobTarget.AnyNode(await client.GetClusterNodesAsync());
var jobExec = await client.Compute.SubmitAsync(jobTarget, jobDesc, arg: "world");

public class HelloJob : IComputeJob<string, string>
{
    public ValueTask<string> ExecuteAsync(IJobExecutionContext context, string arg, CancellationToken cancellationToken) =>
        ValueTask.FromResult("Hello " + arg);
}
```

### Removing All Data From Tables

New `removeAll()` and `deleteAll()` methods can be used to remove all data from key-value and record views respectively.

For example:

```java
KeyValueView<AccountKey, Account> kvView = client.tables()
        .table("accounts")
        .keyValueView(AccountKey.class, Account.class);

AccountKey key = new AccountKey(123456);

Account value = new Account(
        "John",
        "Smith",
        100.00d
);

kvView.put(null, key, value);

kvView.removeAll(null)
```

### COPY INTO batchSize Parameter

With this release, you can choose how many entries are processed at a time when executing the `COPY INTO` operation. By default, 1024 entries are batched. If you want to change the value, use the `batchSize` parameter:

```sql
/* Import data from CSV with custom quotation character */
COPY FROM '/path/to/dir/data.csv'
INTO Table1 (name, age)
FORMAT CSV
WITH 'batchSize'='2048';
```

### New Distribution Zone QUORUM_SIZE Parameter

You can now manually set the required number of available replicas in the distribution zone by setting the `QUORUM_SIZE` parameter. If at any point there are fewer replicas available than set in the `QUORUM_SIZE`, the consensus is lost and updating the table will be impossible until the required number is once again available. Previously written data will still be available.

You can set the quorum size to a specific number.

Below is the example of setting quorum size:

```sql
CREATE ZONE IF NOT EXISTS exampleZone (REPLICAS 3, QUORUM SIZE 3) STORAGE PROFILES['default'];
```

### Batched Execution Cancellation

The `executeBatch()` and `executeBatchAsync()` methods now return cancellation token that can be used to cancel these operations.

### Logging Improvement

This release features major effort in improving logging in GridGain 9. A large number of errors that previously caused unexpected exceptions are now correctly caught, categorized and reported with a [correct code](../../administrators-guide/handling-exceptions.md).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
|---|---|---|
| IGN-27727 | General | Improved log messages when a node in the cluster stops. |
| IGN-27725 | General | Added removeAll() and deleteAll() methods to key-value and record view APIs. |
| IGN-27632 | Platforms and Clients | Added support for .NET data streamer receiver implementations. |
| IGN-27609 | SQL | Fixed an issue that caused inconsistent behavior of the JOIN command that has sub-queries in the ON clause referencing the right table of the JOIN. |
| IGN-27514 | Platforms and Clients | .NET: Added synchronous Dispose method to ITransaction. |
| IGN-27483 | General | Lower throttling limit increased to 50%, and upper throttling limit reduced to 75%. |
| IGN-27482 | General | Fixed a rare case that could lead to data loss during partition rebalancing. |
| IGN-27480 | General | Page throttling limits are now configurable. |
| IGN-27457 | CLI Tool | Improved error message that is thrown when a node fails to initialize. |
| IGN-27456 | General | You can now pass numerals in configuration without quoting them. |
| IGN-27449 | Platforms and Clients | Added .NET compute jobs support: implemented jobs in .NET (C#), deployment of dlls in deployment units, calls from any language or client. |
| IGN-27448 | Platforms and Clients | Added support for distributed computing in .NET client. |
| IGN-27427 | SQL | SQL_QUERIES system view now returns the same query as was submitted. |
| IGN-27422 | SQL | Added support for UUID literal. |
| IGN-27418 | Distributed Computing | Added a dedicated error IGN-COMPUTE-14 code for cancelling compute jobs. |
| IGN-27365 | General | Metastorage compaction no longer prevents other operations from reading data. |
| IGN-27336 | General | Fixed an issue that could cause partitions recovery to time out. |
| IGN-27276 | SQL | The __part system column is now case-insensitive. |
| IGN-27274 | SQL | Time values are now truncated consistently. |
| IGN-27170 | SQL | You can now only specify year up to year 9999 in temporal data types. |
| IGN-27139 | SQL | When using the FORCE_INDEX hint, you will now receive an error if index name is incorrect. |
| IGN-27055 | SQL | Reworked CREATE ZONE command syntax. |
| IGN-27053 | SQL | Calcite version updated from 1.38.0 to 1.39.0. |
| IGN-26924 | SQL | You can now cancel batched queries. |
| IGN-26731 | General | Added QUORUM_SIZE parameter for distribution zones. |
| IGN-26565 | SQL | Improved type checking in LIMIT and OFFSET clauses. |
| IGN-26396 | General | Fixed potential rebalancing failure caused by catalog compaction. |
| IGN-25928 | General | Fixed a rare data corruption during concurrent remove operations, when multiple clients try to remove data from the same index tree in multiple threads. |
| IGN-25513 | SQL | Fixed an error that caused the query to fail if SET clause of the UPDATE statement included sub-queries. |
| IGN-25361 | Distributed Computing | .NET: Added support for IIgniteTuple as Compute and Data Streamer Receiver inputs and outputs. |
| GG-43282 | Cluster SQL Engine | Added support for batchSize parameter to COPY FROM command. |
| GG-43244 | Cluster Data Snapshots and Recovery | Fixed a false-positive error that happened when clearing snapshot tombstones. |
| GG-43195 | General | Updated json-smart from version 2.4.7 to version 2.5.2. |
| GG-43163 | GridGain Integrations | Kafka sink: Fixed LocalDate conversion with Avro converter. |
| GG-43153 | Cluster SQL Engine | Improved error message when COPY command does not find a table or column. |
| GG-43143 | Cluster Data Replication | Fixed an issue that could lead to OOM error during data center replication. |
| GG-43142 | Cluster Data Replication | Data center replication now considers table schemas. |
| GG-43141 | General | Fixed an issue that caused data center replication to fail when using JDK 17. |
| GG-43116 | Cluster Storage Engine | Fixed an issue that caused an exception when invalid encryption configuration is provided on node startup. |
| GG-43099 | Cluster Data Snapshots and Recovery | Point-in-time recovery commands now use --id parameter. |
| GG-43097 | Cluster Data Snapshots and Recovery | Point-in-time recovery now operates on a per-table basis. |
| GG-43078 | Cluster Storage Engine | Fixed an issue with columnar storage on Mac systems with ARM architecture. |
| GG-43002 | GridGain Integrations | Kafka source: Fixed potential endless polling loop. |
| GG-42945 | Cluster SQL Engine | Fixed an issue causing a query to fail when ON clause of join contains scalar sub-query referencing left side of a join. |
| GG-42841 | Cluster Storage Engine | Fixed a rare race when GridGain is restarted with columnar storage enabled. |
| GG-42671 | Cluster SQL Engine | Data expiry is now checked every 30 seconds. |
| GG-42537 | Cluster SQL Engine | Improved error message that is returned when trying to set unsupported expression as DEFAULT. |
| GG-42486 | Cluster Storage Engine | Updated RocksDB from 8.11.3.2 to 9.10.0.1. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.0`

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

### Data Center Replication With Complex Topologies

Complex Data Center Replication topologies (for example, the ones involving cycles) of 3 or more data centers are not supported. This will be addressed in an upcoming releases.

### SQL Performance in Complex Scenarios

There are known issues with the performance of SQL read-write transactions in complex read-write scenarios. These issues will be addressed in an upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: http://support.gridgain.com/.
