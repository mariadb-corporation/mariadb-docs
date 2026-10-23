---
description: >-
  GridGain 8.7.43 speeds up node startup with checkpoint history snapshots, applies
  multiple security updates, and includes a range of improvements and bug fixes.
hidden: true
---

# GridGain 8.7.43 Release Notes

## New Features

### Sped up Node Start

GridGain now periodically creates checkpoint history snapshots. This significantly speeds up node startup time by removing the need to read checkpoint to prepare node history for PME.

### Multiple Security Updates

Multiple recently found vulnerabilities were fixed.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34591 | Platforms & Thin Clients | .NET: Fixed platform cache not restoring data from persistent storage after node restart. |
| GG-34576 | Cluster Communication | Suppressed a non-informative ClosedChannelException which was logged in some cases. |
| GG-34575 | Cluster SQL Engine | Fixed inline-size calculation for PK of varchar(N) column. |
| GG-34573 | Cluster Storage Engine | Fixed an issue that caused speed-based writes throttling to fail in protecting Checkpoint Buffer from exhaustion. |
| GG-34571 | Binary Objects | Fixed unexpected object deserialization on concurrent operations when binary projection was used. |
| GG-34433 | Binary Objects | Fixed an AssertionError when getting unassigned field in BinaryObjectBuilder. |
| GG-34429 | Cluster Storage Engine | Fixed a rare case when rebalance did not happen during a client joining the cluster. |
| GG-34406 | Platforms & Thin Clients | Java thin: reduced memory usage by avoiding extra buffer copy. |
| GG-34403 | Platforms & Thin Clients | .NET: Fixed dynamically generated types deserialization support. |
| GG-34381 | Platforms & Thin Clients | Fixed potential out of memory exception in thin client protocol handler that could be caused by erroneous data. |
| GG-34348 | Cluster Storage Engine | IGNITE_WAIT_FOR_BACKUPS_ON_SHUTDOWN system property was deprecated. Use ShutdownPolicy instead. |
| GG-34279 | Cluster Storage Engine | Introduced checkpoint history snapshots to speed up node startup process. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34592 | Control Center Agent | Added APIs (Java, control.sh, and JMX) to change cluster ID and cluster secret. |
| GG-34574 | Cluster Security | Updated jackson-databind and log4j2 version to fix a vulnerability. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34473 | Cluster Data Snapshots and Recovery | Fixed rare snapshot failures which could happen if Transparent Data Encryption was enabled. |
| GG-34396 | Cluster Data Snapshots and Recovery | Fixed a rare freeze during custom snapshot operation. |

### Control Center Agent Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-34560 | Control Center Agent | Fixed CVE-2021-44832. |
| GG-34242 | Control Center Agent | Reverted SSL validation for Control Center Agent. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.26-p1`, `8.7.27`, `8.7.27-p1`, `8.7.28`, `8.7.29`, `8.7.29-p1`, `8.7.30`, `8.7.31`, `8.7.32`, `8.7.33`, `8.7.33-p2`, `8.7.34`, `8.7.35`, `8.7.36`, `8.7.37`, `8.7.38`, `8.7.39`, `8.7.40`, `8.7.41`, `8.7.42`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`

## Known Limitations

### Jetty Configuration Incompatibility in GridGain 8.7.21 and Later

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

### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and Later

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

### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the
provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect.
Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

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

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
