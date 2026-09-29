---
description: >-
  GridGain 8.7.33 deprecates the control.sh --deactivate command and delivers a
  broad set of improvements and fixed issues across the Community, Enterprise,
  and Ultimate editions.
hidden: true
---

# GridGain 8.7.33 Release Notes

## Changes in Behavior

### Deactivating an In-Memory Cluster

Starting this version `control.sh --deactivate` command is deprecated. It is recommended to use `control.sh --set-state inactive` instead.
Also, starting this version `control.sh --deactivate` command will no longer work on a cluster with in-memory caches.
The reason for this change is that deactivation causes all in-memory data to be deleted which is normally not the indented result.
If you wish to deactivate a cluster with in-memory caches, use a new `--force` parameter of the `--set-state` command: `control.sh --set-state inactive --force`.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32146 | Cluster Storage Engine | Fixed an issue that led to an `AssertionError` when a client node was joining or leaving concurrently with `ATOMIC` cache updates. |
| GG-32129 | Cluster SQL Engine | Fixed an issue causing duplicated rows in query results when partition eviction was in progress. |
| GG-32115 | Cluster Storage Engine | Updated hibernate-core to version 5.4.24.Final and jackson-databind to version 2.11.0. |
| GG-32099 | Cluster Metrics & Monitoring | Fixed "allocated RAM" metric for clusters with both persistent and in-memory caches. |
| GG-32093 | Platforms & Thin Clients | .NET: Added an ability to enable Java peer class loading via IgniteConfiguration. |
| GG-32067 | Control Center Agent | Fixed a bug causing propagation of the wrong connection status. |
| GG-32061 | Control Center Agent | Fixed incorrect parsing of the URI command parameters. |
| GG-32043 | Cluster Compute Grid | Added an ability to use the server's version of a class when both server and client have the same class and peer class loading is enabled. |
| GG-32042 | Platforms & Thin Clients | .NET: Added RendezvousAffinityFunction.BackupFilter with a single predefined implementation - ClusterNodeAttributeAffinityBackupFilter. |
| GG-32041 | Cluster Communication | Fixed an issue with the local cluster group using incorrect node id after reconnecting. |
| GG-32019 | Cluster Communication | Fixed an issue with the inverse connection request that was not canceled immediately when node failure is detected. |
| GG-32015 | Cluster SQL Engine | Fixed an issue with unsupported SQL data type INTERVAL: the INTERVAL value is converted to BIGINT data type for the result set. Also added implicit conversion from/to numeric types. |
| GG-31997 | Platforms & Thin Clients | .NET: Fixed CachePartialUpdateException when key and value referenced the same objects in an async cache operation. |
| GG-31993 | Cluster Storage Engine | Updated Opencensus to 0.28.2 version. |
| GG-31978 | GridGain Integrations | Updated Jetty to 9.4.35.v20201120 version. |
| GG-31969 | Cluster Storage Engine | Added new system property IGNITE_EXECUTE_DURABLE_BACKGROUND_TASKS_ON_NODE_START_OR_ACTIVATE to turn off execution of background tasks on node start or cluster activation. |
| GG-31937 | Cluster Storage Engine | Fixed an issue that led to incorrect mapping of transactions. |
| GG-31936 | Cluster SQL Engine | Fixed an issue causing incorrect SQL results when an open-range predicate over a primary key was used. |
| GG-31927 | Platforms & Thin Clients | Fixed issue with asynchronous operations blocking user threads on updates. |
| GG-31920 | Platforms & Thin Clients | .NET: Fixed NullPointerException in ICache.GetAffinity on client nodes. |
| GG-31919 | Platforms & Thin Clients | Fixed unexpected channel close due to inactivity. |
| GG-31916 | Cluster Storage Engine | Fixed an issue with collecting metrics for not initialized data region. |
| GG-31909 | Cluster SQL Engine | Added limited support for LEFT JOIN from REPLICATED tables to PARTITIONED. |
| GG-31893 | Cluster Storage Engine | Fixed possible deadlocks when unordered keys passed to putAll, removeAll. |
| GG-31892 | Cluster Storage Engine | Fixed an issue that could lead to node failure when -DIGNITE_PDS_LOG_CP_READ_LOCK_HOLDERS=true option was used. |
| GG-31867 | Cluster Metrics & Monitoring | Added new LastCheckpointStart metric indicating the start time of the checkpoint. |
| GG-31855 | Cluster Control Script | Fixed an issue that led to NullPointerException when diagnostic connectivity command was used. |
| GG-31796 | Platforms & Thin Clients | Added new PROBE command to determine whether the node is fully started. |
| GG-31790 | Control Center Agent | Improved names for threads created by agent thread pools. |
| GG-31757 | Platforms & Thin Clients | .NET: Fixed misleading exception when LINQ expression could not be translated to SQL. |
| GG-31653 | Cluster Storage Engine | Fixed an issue when a node's failure handler could be triggered by a long persistent caches recovery on startup. |
| GG-31629 | Cluster Discovery | Renamed JVM_OPTS to MANAGEMENT_JVM_OPTS in management.bat and management.sh |
| GG-31276 | Cluster Storage Engine | Fixed an issue with the Ignite Out Of Memory error that triggered failure handler. |
| GG-31197 | Cluster Affinity and Baseline Topology | control.sh --deactivate now requires an additional option --force to deactivate an in-memory cluster. |
| GG-31800 | Cluster Control Script | `control.sh  --indexes_list` now correctly shows indexes created via the `CREATE INDEX` statement. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32142 | Cluster Data Replication | Fixed an issue causing excessive Java heap memory usage when Data Center Replication was enabled for TRANSACTIONAL caches. |
| GG-32017 | Cluster Data Replication | Fixed an issue that could lead to node hanging after a restart when Native Persistence and Data Center Replication were used. |
| GG-31968 | Cluster Data Replication | Fixed a bug when a connection to a remote data center could be unexpectedly closed under load. |
| GG-31720 | Cluster Data Replication | Fixed an issue when data center replication could hang on node deactivation. |
| GG-31983 | Cluster Security | Fixed a compatibility issue when the security subject could not be properly deserialized. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31907 | Cluster Data Snapshots and Recovery | Fixed point-in-time recovery when multiple nodes were running on a single physical machine. |
| GG-31557 | Cluster Data Snapshots and Recovery | Added snapshot events for tracking create, check, copy, and delete operations. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`

### Known Limitations

#### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

If you are upgrading from version 8.7.20 or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting a new version, an exception is thrown with an error message similar to the following:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`.
See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches
the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

Please fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX.
Default settings are known to cause issues if customized (for example, secure the connection).
Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
