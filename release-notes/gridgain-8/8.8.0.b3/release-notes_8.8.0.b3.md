---
description: >-
  GridGain 8.8.0.b3 is a beta release providing early access to new features such as
  PDS defragmentation status and Transparent Data Encryption CLI management.
hidden: true
---

# GridGain 8.8.0.b3 BETA Release Notes

## Introduction

GridGain 8.8 Beta provides early access to new features and improvements for development and testing needs.

## New Features

**PDS Defragmentation status and parallelism**

When used with Native Persistence, Ignite persists caches' data to disk to enable durability. These files grow automatically when new data is added to the caches, but don't shrink when existing data is removed. In most scenarios it is not an issue as space is reused when new data is added again, but in some situations it is possible that the files occupy much more disk space than required.

Defragmentation feature enables to compact the files and return disk space back to operating system.

Defragmentation status can be accessed via either JMX ("Defragmentation" bean) or control.sh:

```shell
control.sh --defragmentation status
```

**Transparent Data Encryption CLI Management**

Transparent data encryption automatically and silently protects data in rest (persistence). You can configure master key using control.sh:

```shell
# Starts master key rotation.
control.sh --encryption change_master_key newMasterKeyName

# Displays cluster's current master key name.
control.sh --encryption get_master_key_name
```

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31846 | Platforms & Thin Clients | .NET: Fixed a NullPointerException when IIgnite.GetAffinity is called before IIgnite.GetCache |
| GG-31798 | Cluster Control Script | `control.sh --indexes_list` will now correctly print indexes added via `CREATE INDEX` statement |
| GG-31791 | Control Center Agent | Statistics for queries executed from client nodes will now be correctly sent to the GridGain Control Center |
| GG-31772 | Platforms & Thin Clients | Java Thin Client: Idle connections will not longer unexpectedly close |
| GG-31737 | Control Center Agent | Fixed an issue when a node with Control Center Agent installed could hang on a cluster topology change |
| GG-31636 | Control Center Agent | Fixed an issue when management.sh wouldn't work if the oldest node in the cluster is a client |
| GG-31574 | Control Center Agent; Cluster SQL Engine | Running queries executed from client nodes will now be correctly sent to the GridGain Control Center |
| GG-31564 | Cluster Communication | Fix hanging of node if inverse connection is requested and paired connections are enabled |
| GG-31559 | Cluster Data Replication | Fixed an issue when a node occasionally wouldn't stop gracefully while Full State Transfer is active |
| GG-31545 | Cluster Storage Engine | Added control.(sh\|bat) command to clean and backup corrupted cache files. |
| GG-31513 | Cluster Control Script | `control.sh --diagnostic connectivity` now works properly if topology change happens during the command execution |
| GG-31457 | Cluster Diagnostic & Failure Handling | Removed a misleading stack trace from the "Blocked system-critical thread" error message |
| GG-31385 | Platforms & Thin Clients | .NET Thin Client: Fixed an issue causing excessive JVM metaspace growth on client connections |
| GG-31179 | Common Lang | ignite-log4j module is no longer a part of the binary package. ignite-log4j is no longer enabled automatically when it is available on the classpath - ignite-log4j2 is enabled automaticallt instead |
| GG-31092 | Control Center Agent | Control Center Agent threads now have meaningful names |
| GG-30884 | Control Center Agent | Added link to documentation about connection to GridGain Control Center on agent start |
| GG-29922 | Cluster Storage Engine | Fixed an error when metrics are collected for an empty data region |
| GG-29756 | Cluster Affinity and Baseline Topology | `control.sh --deactivate` now requires an additional option `--force` to deactivate an in-memory cluster |
| GG-29194 | Cluster SQL Engine | Added ability to create tables for existed caches |
| GG-28316 | Cluster SQL Engine | Added limited support for LEFT JOIN from REPLICATED tables to PARTITIONED. See "SQL Joins" documentation section for details |
| GG-18652 | Cluster SQL Engine | Improved SQL statistics and optimizer. Note that SQL execution plans may change due to this improvement |
| GG-31915 | Common Lang | Upgraded google-api-client from 1.30.10 to 1.31.1, opencensus from 0.22.0 to 0.28.2, grpc-context from 1.19.0 to 1.27.2 |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-14570 | Cluster Data Snapshots and Recovery | maxWalArchiveSize will be considered when Point-in-Time Recovery is enabled |
| GG-31355 | Cluster Data Snapshots and Recovery | Add consistency checker of nextSnapshotTag and lastSuccessfulSnapshotTag for snapshots. |
| GG-30538 | Cluster Data Snapshots and Recovery | Point-in-Time Recovery will now work correctly if the multiple nodes use the same persistence folder |
| GG-30351 | Cluster Data Snapshots and Recovery | Added snapshot events for tracking create, check, copy and delete operations. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for the information on upgrade options.

- 8.5.3
- 8.5.5
- 8.5.6
- 8.5.7
- 8.5.8
- 8.5.8-p6
- 8.5.9
- 8.5.10
- 8.5.11
- 8.5.12
- 8.5.13
- 8.5.14
- 8.5.15
- 8.5.16
- 8.5.17
- 8.5.18
- 8.5.19
- 8.5.20
- 8.5.22
- 8.5.23
- 8.5.24
- 8.7.2
- 8.7.2-p12
- 8.7.2-p13
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.6
- 8.7.7
- 8.7.8
- 8.7.9
- 8.7.10
- 8.7.11
- 8.7.12
- 8.7.13
- 8.7.14
- 8.7.15
- 8.7.16
- 8.7.17
- 8.7.18
- 8.7.19
- 8.7.19-p1
- 8.7.20
- 8.7.21
- 8.7.22
- 8.7.23
- 8.7.24
- 8.7.25
- 8.7.26
- 8.7.27
- 8.7.28
- 8.7.29
- 8.7.30

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

To workaround this issue, alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`. See the configuration example at the [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication) page.

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` changed from `1` to `min(4, number of CPU / 4)`. It may cause a compatibility issue under the following conditions:

- When a Rolling Upgrade is performed
- The upgrade is performed from 8.5.7 version (or earlier) to 8.5.x or from 8.7.3 (or earlier) to 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration does not have the property `IgniteConfiguration.rebalanceThreadPoolSize`, so the default value is used

In this case, an exception is thrown with an error message similar to the following:

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, change the configuration of the server nodes to `rebalanceThreadPoolSize=1` so that it matches the previous default configuration. For example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect. Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX. Default settings are known to cause issues if customized (for example, secure the connection). Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings. Please see the example below. Note that you don't need remote JMX if you use a local connection, such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
