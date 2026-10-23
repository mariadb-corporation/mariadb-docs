---
description: >-
  GridGain 8.7.34 delivers a broad set of platform, thin-client, storage engine,
  and SQL improvements and fixed issues across the Community, Enterprise, and
  Ultimate editions.
hidden: true
---

# GridGain 8.7.34 Release Notes

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32675 | Platforms & Thin Clients | .NET: Added services exceptions interoperability between java and .NET |
| GG-32598 | Platforms & Thin Clients | .NET: Fixed inferred SQL table name when query entity value type was generic |
| GG-32578 | Platforms & Thin Clients | Fixed exception during query entity validation when no query fields were defined |
| GG-32575 | Platforms & Thin Clients | .NET: Fixed SQL type name for generic query types |
| GG-32566 | Platforms & Thin Clients | .NET: Fixed arrays and collections deserialization when elements shared a reference to the same object |
| GG-32471 | Platforms & Thin Clients | Java thin: Added containsKeys, clearKey, clearKeys, and getAndPutIfAbsent |
| GG-32470 | Platforms & Thin Clients | Java thin client: Fixed hang on executing ComputeTask with unregistered type |
| GG-32448 | Platforms & Thin Clients | .NET: Examples reworked to .NET Core, can be run from CLI or any IDE, on any OS. Examples can be downloaded from NuGet with dotnet-new command. |
| GG-32442 | Platforms & Thin Clients | .NET: Added implicit Java type registration in ExecuteJavaTask |
| GG-32345 | Platforms & Thin Clients | .NET: Fixed LINQ to SQL translation for queries with JOIN and GROUP BY combined |
| GG-32344 | Platforms & Thin Clients | .NET: Improved primitives deserialization performance |
| GG-32317 | Platforms & Thin Clients | .NET: Improved overloaded service methods handling |
| GG-32315 | Platforms & Thin Clients | .NET: Fixed typed array passing in Services |
| GG-32307 | Platforms & Thin Clients | .NET: Added BinaryConfiguration.TimestampConverter to allow custom user-defined timezone conversion logic |
| GG-32270 | Platforms & Thin Clients | C++ thin client: Added SQL API |
| GG-32268 | Platforms & Thin Clients | .NET: Added BinaryConfiguration.ForceTimestamp to enable interoperable DateTime format globally and allow Timestamp as a cache key and value. |
| GG-32254 | Platforms & Thin Clients | Java thin client: Allowed IPv6 server addresses |
| GG-32252 | Platforms & Thin Clients | .NET: Binary configurations of Ignite Java service params are now avoided to simplify Java service calls |
| GG-32547 | Cluster Storage Engine | Fixed node crash in cases when historical rebalance could not find reserved WAL segments. Now rebalance falls back to the full rebalance procedure |
| GG-32540 | Cluster Storage Engine | Fixed a bug causing server nodes transactions hang after the transaction originator left the grid |
| GG-32585 | Cluster Storage Engine | Fixed an issue with incorrect checkpoint pool size initialization |
| GG-32580 | Cluster Storage Engine | Decreased overall cache operation latency jitter by optimizing checkpoint lock exclusive hold time |
| GG-32503 | Cluster Storage Engine | Fixed null pointer exception thrown during tx recovery |
| GG-32493 | Cluster Storage Engine | Fixed an issue causing a deadlock when user cache was created in parallel with working TTL cleanup thread |
| GG-32452 | Cluster Storage Engine | Adjusted transaction log output when node was stopping |
| GG-32249 | Cluster Storage Engine | Deprecated IGNITE_TO_STRING_INCLUDE_SENSITIVE system property. Added IGNITE_SENSITIVE_DATA_LOGGING system property with possible values: "plain", "hash", "none". |
| GG-31725 | Cluster Storage Engine | Fixed an issue causing a null pointer exception when dumping long running operations during node startup |
| GG-32677 | Cluster Storage Engine | Added property `checkpoint.deviation` for randomization of checkpoint interval. |
| GG-32560 | Cluster SQL Engine | Fixed an issue causing PK index tree corruption in case the table was created via SQL API and the PK had several fields in order different from those specified in field list |
| GG-32522 | Cluster SQL Engine | Fixed an issue that prevents applying sorted-aggregate optimisation for grouping with proper index |
| GG-32395 | Cluster SQL Engine | Fixed incorrect span inheritance in the SQL tracing |
| GG-32199 | Cluster SQL Engine | Fixed an issue causing a caller thread freeze for an uncertain time when cancelling a local lazy query |
| GG-32148 | Cluster SQL Engine | Fixed an issue with OutOfMemoryError on plain SQL query. |
| GG-32727 | Cluster SQL Engine | Fixed an issue causes omitting of NOT NULL constraint validation for columns that are part of compound primary key |
| GG-32595 | Control Center Agent | Fixed null pointer exception on configuration change when Control Center Agent was not supported |
| GG-32548 | Control Center Agent | Added JUL bridge for log4j2 and slf4j |
| GG-32439 | Control Center Agent | Cluster tag is now refreshed in Control Center when the tag is changed via the command line |
| GG-32360 | Control Center Agent | Control Center Agent now merges schema-only metric messages to one message before sending it to Control Center |
| GG-32357 | Control Center Agent | Support collecting limited metrics by Control Center request |
| GG-32355 | Control Center Agent | Added ability to limit metrics collection by Control Center agent |
| GG-32329 | Control Center Agent | Fixed compatibility issue after removing agent from classpath |
| GG-32336 | Cluster Compute Grid | Fixed exception on node stop with collisionSpi enabled. |
| GG-32397 | Cluster Metrics & Monitoring | Added network I/O tracing for SQL |
| GG-32396 | Cluster Metrics & Monitoring | Added partition reservation info and query plan cache hits to tracing |
| GG-32293 | Cluster Deployment | Added cluster tag management API to IgniteCluster interface |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32239 | Cluster Data Replication | Fixed an issue causing a state transfer freeze because of a race between FST start and replication stop |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32462 | Cluster Data Snapshots and Recovery | Added verification of the incremental snapshot's chain metadata |
| GG-32186 | Cluster Data Snapshots and Recovery | Updated commons-vfs version to 2.7.0, increased stability of snapshot workflow with SFTP server. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`

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

In GridGain 8.7.31, Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration lead to an error on the start.

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
