---
description: >-
  GridGain 9.1.29 adds a license-management privilege and a DCR source-address
  allow list, fixes a thin-client protocol vulnerability, and adds SQL SHA2 and
  .NET features.
  Released on 2026-11-10.
---

# GridGain 9.1.29 Release Notes

**Release date:** 10 Nov 2026

## Overview

GridGain 9.1.29 adds a license-management privilege and a source-address allow list for data center replication, fixes a thin-client protocol vulnerability, adds the SQL `SHA2` function, and extends the .NET client with partitioned broadcast and new ADO.NET parameter types.

## Major Changes

### New Privilege Required to Replace the License

Replacing cluster license now requires the new `MANAGE_LICENSE` action. It is required to replace the license with the REST API or the `license update` CLI command. A cluster configuration update that changes the `ignite.license` part of the configuration requires both `MANAGE_LICENSE` and `WRITE_CLUSTER_CONFIG`. A user without the privilege gets an authorization error.

When you upgrade a cluster to 9.1.29, the built-in `system` role receives `MANAGE_LICENSE` automatically. Other roles are not updated, including roles that were granted all actions. Before upgrading, grant the new action to the roles that replace the license:

```sql
GRANT PRIVILEGES MANAGE_LICENSE TO cluster_admin;
```

See [User Permissions and Roles](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/oHbGEk22iR73P3x6DryR/security/authentication-and-authorization/user-permissions-and-roles) for the full list of actions.

### Source Cluster Address Validation for Data Center Replication

Data center replication now checks the source cluster addresses a replication connects to. By default, IP addresses in the link-local, any-local, and multicast ranges and the IP addresses of known cloud instance metadata services are refused. Host names are not resolved, so they are accepted.

To allow only specific addresses, set the new `ignite.dcr.sourceClusterAddressAllowList` cluster configuration property. When the list is not empty, only the listed addresses are allowed:

```bash
cluster config update 'ignite.dcr.sourceClusterAddressAllowList=["10.0.0.5:10800", "dc2.example.com"]'
```

Addresses are checked when a replication is created or started. `dcr create` and `dcr start` fail with the new `GG-DCR-14` error if an address is not allowed. A replication that GridGain restarts automatically, for example after a node restart or an error, moves to the `FAILED` state. A running replication is not affected until it is started again.

{% hint style="warning" %}
A replication whose source cluster address is in a range refused by default fails the next time it is started after the upgrade. To keep it running, add the address to `ignite.dcr.sourceClusterAddressAllowList`.
{% endhint %}

See [Restricting Source Cluster Addresses](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/oHbGEk22iR73P3x6DryR/gridgain9-management/backup-and-replication/data-center-replication/configuring-replication#restricting-source-cluster-addresses).

### DR Connector Default Heap Size

The DR connector now sets its heap size itself unless you size the heap explicitly. It starts with `-Xms2g` and a maximum heap of 6 GB, which fits the traffic of a single GridGain 8 sender with default settings. On a host or container with little memory, the maximum is lowered to 70% of RAM. On a large host, it is raised to 25% of RAM.

The DR connector Docker image no longer sets `JVM_MAX_MEM="12g"`, `JVM_MIN_MEM="6g"`, `JVM_GC`, or `JVM_G1HeapRegionSize`, so a container that relied on these values starts with a smaller heap after the upgrade.

To size the heap explicitly, set the `JVM_MAX_MEM` and `JVM_MIN_MEM` environment variables, or pass heap flags such as `-Xmx` and `-Xms` in `EXTRA_JVM_ARGS`. When you pass heap flags, no default is applied.

## New Features

### SHA2 SQL Function

The new `SHA2(str, hash_len)` function returns the SHA-2 hash of a string or binary value as a hexadecimal string, compatible with MariaDB. `hash_len` sets the hash length in bits: `224`, `256`, `384`, or `512`. `0` is the same as `256`. See [Operators and Functions](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/oHbGEk22iR73P3x6DryR/reference/sql/operators-and-functions#sha2).

### Partitioned Broadcast in the .NET Client

The .NET client can now broadcast a compute job to every partition of a table. `BroadcastJobTarget.Table()` runs one job for each partition, on the node that holds the partition's primary replica, and the job reads its partition from `IJobExecutionContext.Partition`. This matches the partitioned broadcast already available in the Java API. See [About Distributed Computing](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/oHbGEk22iR73P3x6DryR/gridgain9-development/distributed-computing-and-services/distributed-computing/about-distributed-computing).

### New ADO.NET Parameter Types

The ADO.NET driver now accepts `char`, `DateOnly`, `TimeOnly`, `DateTimeOffset`, `TimeSpan`, and `ulong` parameters. `DateOnly` and `TimeOnly` are sent as `DATE` and `TIME`, `DateTimeOffset` as `TIMESTAMP WITH LOCAL TIME ZONE`, and `TimeSpan` as a `VARCHAR` string. The data reader adds `GetChar`, and `GetFieldValue<T>` reads the new types back. See [ADO.NET Integration](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/CjGYMsT2MVP4nd3IyW2L/clients/dotnet/ado).

### Client Type in Connection Events

Clients now report their type and version when they connect, in the `GridGain-<client>/<version>` format, for example `GridGain-Java/9.1.29`. Client connection events include this value in the new `clientUserAgent` field. The field is omitted for clients that do not send it, such as clients of earlier versions. See [Available Events](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/oHbGEk22iR73P3x6DryR/gridgain9-development/messaging-and-events/events/available-events).

## Improvements and Fixed Issues

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-53309 | Builds and Deliveries | Docker images: The JDK 26 option is replaced with JDK 27. The default JDK version is unchanged. |
| GG-52991 | Builds and Deliveries | Updated third-party libraries, including Netty 4.2.19.Final and Jackson 2.22.4. |
| GG-52643 | Platforms & Clients | .NET: Added partitioned compute broadcast (`BroadcastJobTarget.Table`), which runs a job on each partition of a table. |
| GG-52614 | Cluster SQL Engine | Fixed a `NullPointerException` on SQL sequence access during concurrent DDL. |
| GG-52604 | Platforms & Clients | Java client: A failed split batch operation now reports the actual error. |
| GG-52599 | Cluster Security | Replacing the cluster license now requires the new `MANAGE_LICENSE` privilege. |
| GG-52552 | Platforms & Clients | Removed the `msgpack-core` dependency. |
| GG-52513 | Cluster SQL Engine | Added the `SHA2` SQL function. |
| GG-52501 | Cluster Data Replication | The DR connector now waits for a missing metadata schema. |
| GG-52475 | Cluster Data Replication | DR receiver connections are now closed when the receiver stops. |
| GG-52472 | General | REST connections are now closed when the node stops. |
| GG-52362 | Cluster Storage Engine | Columnar secondary-storage replication no longer stops the node when the primary replica's node leaves. |
| GG-52355 | Cluster Data Replication | Fixed an issue where the DR connector could stop replicating after the GridGain 8 sender reconnected and resent metadata for several types, if one of the types had new fields. The DR connector no longer needs a restart to recover. |
| GG-52263 | Cluster Continuous Queries | Fixed a lost wakeup of continuous query long polling. |
| GG-52257 | General | A failure of the last batch of a stopped index build no longer stops the node. |
| GG-52229 | General | Leases are no longer lost cluster-wide while the Meta Storage leader node stops. |
| GG-52213 | General | The data streamer is now protected from exceptions thrown by the result subscriber's `onComplete`. |
| GG-52212 | General | The data streamer result subscriber is now notified about an error before the streamer future completes. |
| GG-52194 | Cluster Data Replication | DR connector: Processing of a single chunk now times out after 10 minutes, or after the batch transaction timeout plus 1 second if that is longer. The batch is then cancelled and a warning is logged. |
| GG-52181 | Platforms & Clients | Java client: Failed connection attempts are no longer counted as lost connections in metrics. |
| GG-52180 | Platforms & Clients | Thin client connections are now closed when the client connector stops. |
| GG-52141 | Cluster SQL Engine | Optimized the execution time of read-only `SELECT COUNT(*)` queries by removing an unnecessary clock synchronization wait. |
| GG-52126 | General | Features now stay unavailable on a node started during a rolling upgrade until the upgrade is committed. |
| GG-52124 | Platforms & Clients | Added support for a user agent string on clients. Client connection events include it in the `clientUserAgent` field. |
| GG-51941 | General | Fixed the persistent state of recovered transactions not being vacuumized. |
| GG-51933 | Platforms & Clients | Fixed an integer overflow in `ClientMessageUnpacker.skipValues` (CVE-2026-90473). |
| GG-51890 | Cluster Storage Engine | A page memory out-of-memory error now reaches the client as `STORAGE_OUT_OF_MEMORY_ERR` ("Out of memory in data region"). |
| GG-51870 | Platforms & Clients | .NET: EF Core: Fixed optimistic concurrency conflict detection. |
| GG-51869 | Platforms & Clients | .NET: EF Core: Fixed SQL literals for `Guid` and `DateTimeOffset`. |
| GG-51868 | Platforms & Clients | .NET: EF Core: Fixed `string.Contains` and `IndexOf` translation. |
| GG-51867 | Platforms & Clients | .NET: EF Core: Fixed long identifier handling. Identifiers are now shortened to 128 characters. |
| GG-51866 | Platforms & Clients | .NET: EF Core: Fixed unique constraint handling. Unique indexes are now created as non-unique indexes, with a warning. |
| GG-51865 | Platforms & Clients | .NET: EF Core: Fixed query parameters for update batches. |
| GG-51860 | Migration Tools | Updated the GridGain 8 dependency to 8.9.38. |
| GG-51856 | Platforms & Clients | .NET: EF Core: Fixed `bool` mapped to an integer column. |
| GG-51855 | Platforms & Clients | .NET: Fixed ADO.NET and EF Core failing on `char`, `DateOnly`, `TimeOnly`, `DateTimeOffset`, `TimeSpan`, `ulong`, and `byte` values above 127. |
| GG-51853 | Cluster SQL Engine | Fixed a `ClassCastException` on a dynamic `LIMIT` in a correlated subquery. |
| GG-51829 | Cluster SQL Engine | Fixed a `ClassCastException` in partition pruning for a dynamic parameter of a narrower numeric type. |
| GG-51812 | Cluster Data Replication | The DR connector now applies a default heap size. |
| GG-51786 | Cluster SQL Engine | Fixed a mapping exception triggered by a topology change during primary assignment resolution. |
| GG-51619 | General | Fixed a cluster reporting the pre-upgrade version after a CMG node restart. |
| GG-51591 | General | Fixed an update command that could stop both non-primary replicas and make a partition lose quorum. |
| GG-51501 | Builds and Deliveries | The SBOM now follows CycloneDX 1.6. |
| GG-51460 | CLI Tool | The CLI now reports the HTTP status and response body when a REST error response is not a problem document. |
| GG-51200 | General | A node removed from the logical topology now reports a critical failure, and the failure handler decides what happens next. |
| GG-50993 | Cluster Data Snapshots and Recovery | Fixed a bug where an incremental snapshot could revive rows if a rebalance happened between it and the full snapshot. |
| GG-50717 | Cluster SQL Engine | `EXPLAIN` now prints `collation` only where it differs from the input. |
| GG-50636 | Cluster SQL Engine | A query is now recovered if a node leaves before the query fragments start. |
| GG-50373 | General | A node that publishes a validated system attribute with a value different from the rest of the cluster is now denied the join. |
| GG-50360 | General | Fixed cluster initialization with nodes on different JDK versions. |
| GG-49626 | Cluster Data Replication | Added source cluster address validation and the `ignite.dcr.sourceClusterAddressAllowList` property. |
| GG-48000 | Cluster Data Replication | Fixed missing table names in the DCR table validation error. |

## Upgrade Information

You can upgrade to current GridGain version from previous releases. Below is a list of versions that are compatible with the current version. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`9.1.21`, `9.1.22`, `9.1.23`, `9.1.24`, `9.1.25`, `9.1.26`, `9.1.27`, `9.1.28`

When updating from older versions, we recommend updating to version `9.1.21` first, before performing an update to current version.

## Known Limitations

### Data Restoration After Data Rebalance

Currently, data rebalance may cause partition distribution to change and cause issues with snapshots and data recovery. In particular:

- It is currently not possible to restore a `LOCAL` snapshot if data rebalance happened after snapshot creation. This will be addressed in one of the upcoming releases.
- It is currently not possible to perform point-in-time recovery if data rebalance happened after table creation. This will be addressed in one of the upcoming releases.

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://mariadb.com/support/.
