---
description: GridGain 8.8.3 delivers new features and improvements, including checkpoint interval randomization and off-heap storage of deletion tombstones.
hidden: true
---

# GridGain 8.8.3 Release Notes

## New Features

GridGain 8.8.3 provides access to a variety of new features and improvements.

### Randomization of Checkpoint Interval

Starting this version, the user can randomize the checkpoint interval.
In rare cases, identically configured checkpoint frequency of all cluster nodes may increase the transaction processing time.
The new functionality allows to avoid this issue.

Randomization can be done using the control utility. The value is defined as a percentage of the checkpoint frequency.

{% tabs %}
{% tab title="Unix" %}
```shell
control.sh  --property set --name checkpoint.deviation --val 25
```
{% endtab %}

{% tab title="Windows" %}
```shell
control.bat  --property set --name checkpoint.deviation --val 25
```
{% endtab %}
{% endtabs %}

## Changes in Behavior

### Internals of Entries Deletion Are Reworked

Before this version, markers for deleted entries (often called "tombstones") were kept on the Java heap for some time after they had been deleted - this was the requirement of the distributed cache protocol for consistency guarantees.
This led to certain issues, including increased Java heap memory usage and GC pressure.

Starting this version, "tombstones" are stored off-heap instead of on-heap.

For most users, this change is completely transparent.
However, use cases with a lot of deletions may see the following non-functional changes:

- Heap usage may decrease;
- Off-heap usage may increase;
- Update performance may slightly decrease.

## Known Issues

### Rolling Upgrade Fails to Start when Security is Enabled

In GridGain 8.8.3, starting a rolling upgrade with the security feature enabled may cause the **Authorization failed** error.

**Workaround**: Use the `control-utility.sh` to start the rolling upgrade and explicitly specify the coordinator node host with the `--host xxxx --port xxxx` parameters   (coordinator node is the oldest node in cluster topology).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-32723 | Cluster SQL Engine | Fixed an issue that caused omitting of NOT NULL constraint validation for columns that were part of compound primary key. |
| GG-32699 | Platforms & Thin Clients | .NET: Fixed DllNotFoundException in single file deployment on .NET 5 |
| GG-32673 | Control Center Agent | Fixed an issue that led to incorrect calculation of query execution time. |
| GG-32657 | Cluster Storage Engine | Added an ability to randomize the checkpoint interval. |
| GG-32651 | Cluster Rolling Upgrade | Fixed an issue where control utility could not finish rolling upgrade procedure. |
| GG-32643 | Platforms & Thin Clients | .NET Thin Client: Added an automated check confirming that client binary configuration is compatible to server binary configuration on client start. |
| GG-32622 | Platforms & Thin Clients | .NET: Added services exceptions interoperability between java and .NET |
| GG-32596 | Cluster Rolling Upgrade | Fixed an issue when the rolling-upgrade procedure could be erroneously considered as finished one after the cluster restart. |
| GG-32583 | Cluster Storage Engine | Fixed a bug that caused wrong initialization of CPU checkpoint thread pool. |
| GG-32544 | Cluster SQL Engine | Fixed PK index tree corruption issue. |
| GG-32543 | Platforms & Thin Clients | .NET: Fixed inferred SQL table name when query entity value type was generic. |
| GG-32517 | Cluster SQL Engine | Fixed an issue when CREATE TABLE did not use encryptionEnabled property of cache template. |
| GG-32516 | Platforms & Thin Clients | .NET: Fixed arrays and collections deserialization when elements shared a reference to the same object. |
| GG-32510 | Cluster Communication | Fixed a bug when messaging-related metrics were updated before full initialization of Tcp Communication SPI. |
| GG-32499 | Cluster Storage Engine | Fixed an issue when transactions could freeze on server nodes after the node that started the transaction left the cluster. |
| GG-32476 | Platforms & Thin Clients | .NET: Fixed an issue that caused incorrect registration of binary type name for generic query types. |
| GG-32464 | Platforms & Thin Clients | Java thin client: Fixed executing ComputeTask with unregistered type freezing. |
| GG-32463 | Platforms & Thin Clients | Java thin client: Added the following new methods to the client cache API: containsKeys, clearKey, clearKeys and getAndPutIfAbsent. |
| GG-32451 | Cluster Storage Engine | Adjusted transaction log output when node is stopping. |
| GG-32440 | Platforms & Thin Clients | .NET: Examples reworked to .NET Core, now they can be run from CLI or any IDE of any OS. |
| GG-32433 | Cluster Storage Engine | Improved collecting of rebalancing statistics. |
| GG-32394 | Cluster SQL Engine | Fixed an issue that caused incorrect spans inheritance in the SQL tracing. |
| GG-32393 | Platforms & Thin Clients | .NET: Added implicit Java type registration in ExecuteJavaTask. |
| GG-32381 | Cluster Storage Engine | Fixed an issue that could lead to OutOfMemoryError when rebalance was in progress. |
| GG-32327 | Cluster Storage Engine | Fixed an issue that prevented switching to full rebalance when historical rebalance was not able to find reserved WAL segments. |
| GG-32323 | Cluster Storage Engine | Fixed an issue that caused a deadlock when user cache was created in parallel with TTL worker was in progress. |
| GG-32233 | Cluster Storage Engine | Significantly reduced the time of exclusive lock that was needed for a checkpoint. |
| GG-32194 | GridGain Integrations | Removed OSGi modules from GridGain distribution. |
| GG-32084 | Cluster Storage Engine | Fixed an issue that led to cluster instability when WAL archive was disabled. |
| GG-31637 | Control Center Agent | Fixed a bug that caused NullPointerException on configuration change when Control Center Agent was not supported. |
| GG-31235 | Cluster Data Replication | Added replication for removal operations to Incremental Data Replication. |
| GG-31142 | Cluster Communication | Added support of IGNITE_ENABLE_FORCIBLE_NODE_KILL flag when inverse connection protocol is used. |
| GG-30867 | Control Center Agent | Added JUL bridge for log4j2 and slf4j. |
| GG-30273 | GridGain Integrations | Improved SpringData support: multiple ignite instances on same JVM, projections, Page and Stream, advanced parameter binding and SpEL. |
| GG-29695 | Cluster Communication | Fixed an issue when connection closed by the one node could lead to infinite connection attempts on the other node. |
| GG-28839 | Control Center Agent | Fixed an issue when changing a cluster's tag did not reflect by Control Center. |
| GG-19071 | Cluster SQL Engine | Fixed an issue that blocked applying sorted-aggregate optimisation for grouping with proper index. |
| GG-32759 | Cluster Affinity and Baseline Topology | Fixed an issue that led to the fact that auto adjustment of baseline was not triggered under certain conditions. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-30094 | Cluster Data Snapshots and Recovery | Fixed bug when incremental snapshot could be scheduled before full snapshot. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`, `8.7.31`, `8.7.32`,
`8.7.33`,
`8.8.1`, `8.8.2`

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

#### Jetty Does Not Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

Starting from 8.7.31 version, GridGain no longer attempts to automatically enable the remote JMX.
Default settings are known to cause issues if customized (for example, secure the connection).
Also, in most cases, remote JMX is not required since many tools use local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

To continue using remote JMX, you need to manually specify the required JMX settings.
Please see the example below.
Note that you don't need remote JMX if you use a local connection,
such as connecting JConsole to a GridGain process on the same host.

```bash
export JVM_OPTS="-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=33333 \
    -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false"

bin/ignite.sh
```

### Rolling Upgrade from GridGain 8.7.9 and Earlier Fails if Data Center Replication is Enabled

Rolling upgrades from GridGain 8.7.9 and earlier to current GridGain version fails if [data center replication](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/data-center-replication/introduction) is enabled and under load.

To work around this issue, you can first upgrade to GridGain 8.7.21, or a later 8.7.x version, and then to current version.

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
