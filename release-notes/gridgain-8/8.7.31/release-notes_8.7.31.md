---
description: >-
  GridGain 8.7.31 adds a PROBE REST command for Kubernetes readiness probes and
  delivers improvements and fixed issues across the Community, Enterprise, and
  Ultimate editions.
hidden: true
---

# GridGain 8.7.31 Release Notes

## New Features

**REST Command to Check If a Node is Ready**

A new `PROBE` command has been added to GridGain's REST interface. This command checks if the node has fully started and
connected to the cluster.

The `PROBE` command can be used to implement Kubernetes' readiness probe
and better integrate with Kubernetes' orchestration capabilities. Below is an example of the readiness probe
configuration.

```yaml
readinessProbe:
  httpGet:
      path: /ignite?cmd=probe
      port: 8080
  initialDelaySeconds: 5
  failureThreshold: 3
  periodSeconds: 10
  timeoutSeconds: 10
```

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31378 | Architecture | Added a new PROBE command to the REST interface to determine whether the node has fully started. |
| GG-31518 | SQL | Fix an issue related to the return type of the SYSDATE function and convert INTERVAL data type to long implicitly to provide backward compatibility. |
| GG-31516 | Platforms & Thin Clients | Updated Jetty dependency to 9.4.33. Invalid argument names in Jetty configuration files will now lead to startup failures. |
| GG-31367 | Cluster Control Script | Removed default insecure JMX configuration from scripts. Now JMX can be enabled through the corresponding JVM_OPTS variable. |
| GG-31346 | Integrations | Spring Data integration introspects the fields of the key object (in case of using a compound key) |
| GG-31306 | Cluster Control Script | Remove usage of JVM_OPTS in control.sh and snapshot-utility.sh in favor of CONTROL_JVM_OPTS and SNAP_UTIL_JVM_OPTS |
| GG-31296 | SQL | Fixed invalid warning message when SQL MERGE command is executed. |
| GG-31124 | Platforms & Thin Clients | ODBC: Nullability information is now available for columns. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31577 | Control Center Agent | Fixed management.sh errors occurring when the oldest node in the cluster is started without a Control Centre agent. |
| GG-31299 | Architecture | Added GridGain BOM (Bill of Materials) |
| GG-31401 | GridGain Integrations | GridGain Kafka Connect: Added support for Date, Time, Timestamp, Decimal, and optional types for Kafka Source Connector. Added support of schema-less data for Kafka Sink Connector. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-31458 | Cluster Security | Fixed a bug when client nodes of versions 8.7.3 and earlier could not connect to the cluster with Cluster Security enabled. |
| GG-31372 | Snapshot utility | Errors from remote nodes are now printed if snapshot utility verbose mode is enabled. |
| GG-31698 | Cluster Security | Fixed node stopping by FailureHandler where security context for a thin client is not propagated yet. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`, `8.7.29`, `8.7.30`

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
class org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
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

Starting version 8.7.31, GridGain no longer attempts to automatically enable remote JMX.
Default settings are known to cause issues if one wants to customize them (e.g. secure the connection).
Also, in most cases, remote JMX is not required since many tools use a local JMX connections (not using TCP).

Your setup may be affected if:

- You start GridGain nodes via `ignite.sh` script
- You connect to GridGain nodes' JMX interface remotely over TCP using the default configuration

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
