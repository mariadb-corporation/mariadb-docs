---
description: >-
  GridGain 8.7.30 introduces SQL query tracing, offline readers for SQL indexes and WAL files, and incremental snapshots over newly added caches, along with fixes across all editions.
hidden: true
---

# GridGain 8.7.30 Release Notes

## New Features

This release introduces the following features.

**SQL Tracing**

The release introduces a new tracing-related feature to trace SQL queries.

**SQL Indexes and WAL Files Reader**

The release introduces new tools for offline analysis of SQL indexes and WAL files.

**Incremental Snapshot Over New Caches**

It is possible now to create an incremental snapshot even when new caches are added after the last full snapshot.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31317 | Cluster Control Script | The control script now returns correct error code when terminated with an error. |
| GG-31255 | Platforms & Thin Clients | .NET: Respect cgroup limits in DataRegionConfiguration.DefaultMaxSize. |
| GG-31172 | Platforms & Thin Clients | ODBC: Fixed SQL type for java.sql.Date columns. Previously it was reported as SQL_BINARY, now it is reported as SQL_TYPE_DATE. |
| GG-31165 | Cluster SQL Engine | Ability to trace SQL queries. |
| GG-31135 | Platforms & Thin Clients | .NET: Added AttributeNodeFilter support. |
| GG-30930 | Cluster Control Script | Tools for offline analysis of SQL indexes and WAL files. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31277 | Cluster Data Snapshots and Recovery | Ability to create an incremental snapshot when new caches are added after the last full snapshot. |
| GG-31268 | Cluster Data Replication | Fixed an issue causing a false-positive failure handler triggering during DR initialization. |
| GG-31244 | Cluster Snapshot Utility | Snapshot-utility 'list' and 'info' commands now show snapshot size, and WAL size when PITR is enabled. |
| GG-31225 | Cluster Security | Improved GridGain Security facilitates the debugging and workaround process for the "Security context is not ready" errors. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for more information on how to perform automated upgrades and for details about version compatibility.

See the list of product versions that are compatible with the current version below.
You can perform a rolling-upgrade for any product version that is on the list. Compatibility with other versions is not guaranteed.
If you use a version that is not listed, please contact GridGain for more information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`

### Known Limitations

#### Jetty configuration incompatibility in GridGain 8.7.21 and later

If you are upgrading from 8.7.20 version or earlier, consider an incompatibility issue related to Jetty configuration introduced in GridGain 8.7.21.

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

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and later

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

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
