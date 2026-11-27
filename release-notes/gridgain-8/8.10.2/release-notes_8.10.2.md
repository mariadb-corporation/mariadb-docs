---
description: >-
  GridGain 8.10.2 enables Java thin client partition awareness by default, moves REST and configuration parsing to Jackson 3, and adds cache encryption to the Java thin client.
  Released on 2026-12-02.
---

# GridGain 8.10.2 Release Notes

**Release date:** 2 Dec 2026

## Overview

GridGain 8.10.2 is a maintenance release. It enables partition awareness in the Java thin client by default, and moves JSON and YAML parsing in the REST module, the schema import command, and license loading to Jackson 3.

For the full list of changes in GridGain 8.10, see the [GridGain 8.10.0 Release Notes](../8.10.0/release-notes_8.10.0.md).

## Configuration and Default Value Changes

### Java Thin Client Partition Awareness is Enabled by Default

`ClientConfiguration.affinityAwarenessEnabled` now defaults to `true`. In 8.9.x, 8.10.0, and 8.10.1 it defaulted to `false`.

The client now opens a connection to every server node it knows about, and sends key-based operations and service calls directly to the node that owns the key or runs the service. Make sure that the client can reach every server node on its client connector port. If it can reach only some of them, for example when the cluster is exposed through a single address, call `ClientConfiguration.setAffinityAwarenessEnabled(false)` to keep the previous behavior.

### REST Responses Use Jackson 3

The `ignite-rest-http` module now serializes REST responses with Jackson 3 (package `tools.jackson`). The `libs/optional/ignite-rest-http` folder ships the Jackson 3 `jackson-core` and `jackson-databind` libraries instead of the Jackson 2 ones. `jackson-annotations` stays on Jackson 2. If your code loaded Jackson 2 from that folder, add Jackson 2 to your own classpath.

The JSON format of REST responses does not change, with these exceptions:

- `java.time` values, such as `Instant`, and `Optional` values are now serialized, for example as `"1970-01-01T00:00:00Z"`. Earlier, a response that contained such a value failed.
- When a response cannot be serialized, the `error` text comes from Jackson 3 and includes an `at [No location information]` line before the reference chain.

## New Features

### Cache Encryption from the Java Thin Client

You can now create an encrypted cache from the Java thin client with `ClientCacheConfiguration.setEncryptionEnabled(true)`. Every server node must be configured with an encryption SPI, the cache must be persistent, and the server nodes must run GridGain 8.10.2 or later.

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-53019 | Cluster Security | Fixed an SQL DDL injection through an unescaped double quote in a cache schema, table, field, or index name, which let a client that can create a cache run arbitrary H2 statements on the server. |
| GG-53011 | Platforms & Thin Clients | JDBC now supports passing the `local` flag for performing local queries. |
| GG-52987 | Builds and Deliveries | The `ignite-gce` module now ships with Guava included. |
| GG-52920 | Cluster Architecture | Fixed an issue where partition map exchange did not wait for an update to an atomic cache that had already passed the topology check. |
| GG-52863 | Platforms & Thin Clients | .NET: Fixed an issue where a failed compute task sometimes threw a generic `IgniteException` instead of the exception from user code (`Map`, `OnResult`, `Reduce`, or job serialization). |
| GG-52829 | Cluster Data Snapshots and Recovery | Fixed a possible deadlock when pages were replaced in memory while a snapshot was being created. |
| GG-52721 | Cluster Data Snapshots and Recovery | Fixed an issue where restoring a snapshot stalled and then hung when a baseline node was offline. |
| GG-52657 | Cluster Control Script | Schema import scripts: YAML aliases in the configuration file are now rejected with an error. Earlier, an alias was read as the literal text of its name. |
| GG-52652 | Cluster Storage Engine | Fixed an issue where, after a cluster was deactivated and activated again, a checkpoint was not started when a data region had too many dirty pages. |
| GG-52651 | Cluster Architecture | Fixed an issue where a partition could stay on a node after an affinity change instead of being evicted. |
| GG-52541 | Modules and Packaging | ZooKeeper IP finder: Node registration data is now serialized with Jackson 3. The module no longer depends on Jackson 2. |
| GG-52535 | Licensing | GridGain Enterprise and Ultimate no longer ship Jackson 2 in `libs`, except `jackson-annotations`, which Jackson 3 also uses. |
| GG-52533 | Cluster REST API | The REST HTTP module (`ignite-rest-http`) now uses Jackson 3 and no longer ships Jackson 2, except `jackson-annotations`, which Jackson 3 also uses. |
| GG-52522 | Cluster Data Replication | Fixed the issue where DR transitive updates took place regardless of the `GG_DR_DISABLE_TRANSITIVE_UPDATES` option. |
| GG-52310 | Platforms & Thin Clients | C++: Added `ignite_future` as a part of the async framework. |
| GG-52295 | Platforms & Thin Clients | C++: Added the thread pool executor to the public API. |
| GG-52146 | Platforms & Thin Clients | C++: The thin client now sends the `client.user-agent` attribute when it connects. |
| GG-52123 | Platforms & Thin Clients | .NET: Thin client: Added user attributes configuration. |
| GG-52035 | Cluster Data Replication | Fixed an issue where DR receiver metrics stayed registered after the cache was destroyed. |
| GG-51763 | Platforms & Thin Clients | C++: The minimum required CMake version is raised to 3.10. |
| GG-51736 | Platforms & Thin Clients | .NET: Fixed an issue where the thin client data streamer `Flush()` sometimes completed without an error even though the flush failed. |
| GG-51078 | Cluster Discovery | Graceful shutdown of network-segmented nodes no longer leads to metastorage divergence. |
| GG-50843 | GridGain Integrations | Kafka `SourceTask` can now recover from client disconnect errors. |
| GG-50826 | Platforms & Thin Clients | Fixed a possible null pointer exception in the Java thin client retry logic. |
| GG-50825 | Platforms & Thin Clients | Fixed an issue where one failed flush stopped data streamer auto-flush permanently in the Java thin client. |
| GG-50824 | Platforms & Thin Clients | Fixed a possible bug that caused heartbeats to starve other async operations in the Java thin client. |
| GG-50254 | Cluster Data Replication | Introduced a new DR sender hub metric, `OldestUnacknowledgedBatchAge`. |
| GG-49514 | Platforms & Thin Clients | Java thin client: Affinity awareness is now set to `true` by default. |
| GG-49411 | Platforms & Thin Clients | .NET: Added `IIgniteClient.DestroyCaches`. |
| GG-48225 | Cluster Architecture | Fixed a rare issue that could trigger the configured failure handler when a cache was stopped during rebalancing. |
| GG-47704 | Platforms & Thin Clients | Java thin client: Added `ClientCacheConfiguration.encryptionEnabled`. |
| GG-36084 | Diagnostics and Failure Handling | Improved rebalance and PME logging. |
| GG-14908 | Cluster Data Snapshots and Recovery | Fixed snapshot creation progress going above 100% in the snapshot utility's `STATUS` output. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

If you upgrade from GridGain 8.9.x, read the [Breaking Changes](../8.10.0/release-notes_8.10.0.md#breaking-changes) and the [Installation and Upgrade Information](../8.10.0/release-notes_8.10.0.md#installation-and-upgrade-information) sections of the GridGain 8.10.0 release notes first.

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`, `8.9.40`, `8.10.0`, `8.10.1`

{% hint style="info" %}
Rolling upgrade is only possible if both nodes have the `IGNITE_EVENT_DRIVEN_SERVICE_PROCESSOR_ENABLED` property manually set to the same value. Due to the change to the default value, rolling upgrade will fail unless actions are taken.
{% endhint %}

### Older Thin Clients Compatibility

In most cases, older versions of thin clients should be compatible with newer versions of GridGain.
Below is the list of versions of thin clients that are tested for compatibility with the latest version.
The compatibility also means that you can safely update from any version on the list to any subsequent version.

`8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`, `8.9.40`, `8.10.0`, `8.10.1`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`, `2.14.0`, `2.15.0`, `2.16.0`, `2.17.0`, `2.18.0`

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
