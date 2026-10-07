---
description: GridGain 8.8.21 changes trial license packaging, adds new control script commands, and delivers fixes across Community, Enterprise, and Control Center Agent components.
hidden: true
---

# GridGain 8.8.21 Release Notes

## Packaging and Trial License File Changes

In the course of streamlining our licensing and trial policies, GridGain Ultimate® and GridGain Enterprise®  artifacts have been changed. Direct link downloads, Maven and Docker artifacts no longer include a trial license file. A 30-day trial license with no CPU or node limit and a limited uptime is included with the downloads available on the [Try Free](https://www.gridgain.com/tryfree) section of the website.
If you use a trial license in a production or development environment, you will need to [install](https://www.gridgain.com/docs/latest/installation-guide/licenses) your purchased license files. Otherwise, the cluster will not start after the upgrade is done, and you will see an error message on node startup.

If you have any questions, please contact your GridGain Account Executive or [GridGain Support](https://support.gridgain.com/).

These changes do not affect GridGain Community Edition.

## New Features

### New Control Script Commands

New commands `idle_verify` and `rebuild-partition-tree` were added to control script. With these commands, you can detect partition reserve counter(HWM) inconsistency or rebuild the B+Tree for a partition.

## Known Issues

### Docker Images

Due to a known issue, GridGain does not provide .NET Docker images for this release. This will be fixed in the next release.

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35565 | GridGain Integrations | AWS SDK version upgraded to 1.12.261 to fix CVE-2022-31159. |
| GG-35559 | Cluster Storage Engine | Fixed an issue when an index was not rebuilt if a node was restarted during schema change process. |
| GG-35528 | GridGain Integrations | Updated jnr-posix from 3.0.50 to 3.1.15 to fix CWE-416. |
| GG-35484 | Platforms & Thin Clients | Improved service name lookup performance and reduced service startup times. |
| GG-35482 | Cluster Storage Engine | Fixed logical recovery of TDE caches. |
| GG-35449 | Cluster Continuous Queries | Added an ability to use Java-based remote filter for continuous query from C++ thick client. |
| GG-35422 | Platforms & Thin Clients | Java thin: Fixed hang on client startup when deprecated TLS version is used. |
| GG-35392 | Cluster Discovery | Fixed the node resolving obsolete addresses from the previously restarted and killed nodes. |
| GG-35376 | Cluster Communication | Spring Core version upgraded from 5.2.21 to 5.2.22. |
| GG-35370 | Cluster SQL Engine | Fixed an issue causing a wrong result to be returned if subquery with filter is used on the left table of LEFT JOIN. |
| GG-35222 | Cluster Affinity and Baseline Topology | Fixed an issue that could lead to unexpected partition map exchange on client nodes. |
| GG-32626 | Cluster SQL Engine | Fixed the issue when a query with 'in' condition with a sub-query returned multiplicative data. |
| GG-30920 | Cluster Storage Engine | Sped up of partition state restoration on node startup. |
| GG-30761 | GridGain Integrations | Updated jcloud to fix a guava-related CVE. |
| GG-30557 | Control Center Agent | Included common dependencies (Spring, Jackson) into control center agent jar to prevent possible Maven issues. |
| GG-35191 | Data Regions | Added numa-aware allocation for data regions. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35596 | Cluster Data Replication | Fixed a rare issue that caused DR thread failure. |
| GG-35550 | Cluster Communication | The copy-dependencies.sh script now also pulls gridgain-ultimate binaries if you use GridGain Ultimate Edition. |
| GG-35530 | GridGain Integrations | Fixed CVE-2022-22971 and CVE-2022-22970. |
| GG-35526 | GridGain Integrations | Updated Jetty from 9.4.43 to 9.4.48 to fix CVE-2022-2047. |
| GG-35505 | Cluster Data Replication | Fixed the issue when node could fail to start with NPE during activation. |
| GG-35462 | Cluster Data Replication | Added rebuild-partition-tree command to control script. |
| GG-35366 | Cluster Data Replication | Fixed bad network utilization by DR due to the batching process. |
| GG-35234 | GridGain Integrations | Fixed data region validation when BACKLOG policy is used |
| GG-32304 | Control Script | Control.sh command 'idle_verify' can now detect partition reserve counter inconsistencies. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-35551 | Control Center Agent | Fixed saving of an artifact with a query in an external link. |
| GG-35543 | Control Center Agent | Fixed a node failing to restart when a code deployment artifact is not available. |
| GG-35496 | Control Center Agent | Fixed sending multiple instances of metrics after reconnecting the agent. |
| GG-34749 | Control Center Agent | Fixed an issue when websocket connection failed. |
| GG-32136 | Control Center Agent | Added Control Center server URI validation. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.29-p1`, `8.7.42-p2`, `8.8.2-p1`, `8.8.4-p2`, `8.8.8-p1`, `8.8.9-p1`, `8.8.13-p2`, `8.8.16-p2`, `8.8.18-p1`, `8.7.22`, `8.7.28`, `8.7.32`, `8.7.34`, `8.7.38`, `8.8.1`, `8.8.2`, `8.8.3`, `8.8.4`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.9`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.17`, `8.8.18`, `8.8.19`, `8.8.20`

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

#### .NET: GridGain Nuget Package Misses GridGain.Ignite Jars in 8.8.17

Set `<PrivateAssets>None</PrivateAssets>` for the `GridGain.Ignite` dependency in GridGain project, so that jars from there are included.

#### .NET: Docker Images Need Additional Configuration

To run .NET SDK commands, install the .NET SDK. For more details, click [here](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=net60#dependencies).

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
