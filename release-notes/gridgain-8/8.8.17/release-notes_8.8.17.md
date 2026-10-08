---
description: >-
  GridGain 8.8.17 adds thread pool monitoring for thin clients and includes a large
  number of fixes across thin clients, the storage and SQL engines, and data replication.
hidden: true
---

# GridGain 8.8.17 Release Notes

## New Features

### Monitoring Thread Pools on Thin Clients

Client thread pool is now registered, allowing for monitoring of thread pool metrics for thin clients. The JMX bean has a following name: `org.apache:group="Thread Pools",name=GridThinClientExecutor`. For more information about metrics in GridGain, see the [Metrics section](https://www.gridgain.com/docs/gridgain8/latest/administrators-guide/monitoring-metrics/configuring-metrics).

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34775 | Platforms & Thin Clients | ODBC: SQL_ATTR_CONNECTION_TIMEOUT now affects network operations during statement execution. |
| GG-34726 | Cluster Storage Engine | Fixed an issue that led to "Failed to get page store for the given cache ID" error on cache start. |
| GG-34716 | Cluster Data Replication | Fixed a rare case of CorruptedTree exception that could happen during data upload when using data streamer with ongoing data center replication. |
| GG-34714 | Cluster Storage Engine | Fixed page restore on bad CRC not marking the page as dirty. |
| GG-34697 | Platforms & Thin Clients | .NET Thin: Added IRetryPolicy interface to control retry behavior when an operation fails due to a connection issue. |
| GG-34696 | Cluster SQL Engine | Fixed an issue that caused a query to be stuck infinitely when partition pruning optimization was applied and query parallelism was enabled. |
| GG-34678 | Cluster Compute Grid | Fixed Compute Grid monitoring not working with thick clients. |
| GG-34672 | Cluster Discovery | Fixed an issue that led to failure to join a new node to the cluster in the Karaf container. |
| GG-34661 | Platforms & Thin Clients | ODBC: Fixed streaming mode. |
| GG-34657 | Distributed Data Structures | Fixed an issue with IgniteAtomicSequence that led to AssertionError. |
| GG-34656 | Platforms & Thin Clients | ODBC: MSI Installer now can be built by using CMake. See modules/platforms/cpp/DEVNOTES.txt for details |
| GG-34636 | Cluster Storage Engine | Fixed NPE during control.sh --persistence info command evaluation after maintenance mode. |
| GG-34634 | Platforms & Thin Clients | C++ Thin: Fixed a bug which caused thin clients to ignore OPENSSL_HOME environment variable if there were OpenSSL libs in PATH. Added support of OpenSSL 3.0 for C++ thin client and ODBC. |
| GG-34627 | GridGain Integrations | Fixed method name clash issues in Ignite repository and CrudRepository for Spring Data. |
| GG-34617 | Platforms & Thin Clients | Fixed serialization of 'System.Enum' fields in .NET. |
| GG-34602 | Cluster Storage Engine | Fixed an issue where a full rebalance could be used instead of a historical after a cache re-creation. |
| GG-34546 | Cluster Affinity and Baseline Topology | Fixed an issue that caused a failed deactivation of the cluster. |
| GG-34536 | Platforms & Thin Clients | Java Thin: Added RetryPolicy interface to control retry behavior when an operation fails due to a connection issue. |
| GG-34534 | Cluster SQL Engine | Fixed cache API for tables with custom value types and wrapped keys. |
| GG-34493 | Platforms & Thin Clients | .NET: Added GetServiceDescriptors to Thin Client Services. |
| GG-34492 | Platforms & Thin Clients | Java Thin: added ClientServices.serviceDescriptors. |
| GG-34395 | Cluster Storage Engine | Fixed an issue that led to failures of server nodes due to short history of affinity assignments. |
| GG-34387 | Cluster SQL Engine | Added an ability to specify inline size of PK and affinity key indexes from CREATE TABLE command. |
| GG-34309 | Platforms & Thin Clients | Java thin client: Added thin client thread pool monitoring. |
| GG-34170 | Platforms & Thin Clients | C++ Thin: SSL certificate, private key and CA are not mandatory for clients anymore. |
| GG-34154 | Platforms & Thin Clients | Thin client: Fixed a bug that could result in transaction rollback by timeout when multiple transactions are run in parallel from the same client. |
| GG-34025 | Platforms & Thin Clients | C++: Removed VS project files. Removed ignite-jni as separate module. It's now part of ignite-core. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34883 | Cluster Data Replication | Fix the issue when some entries were missed during incremental DR. |
| GG-34220 | Cluster Storage Engine | Added compatibility with JDK 17. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34785 | Cluster Snapshot Utility | Fixed a security issue in snapshot utility script. |

### Control Center Agent Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-34727 | Control Center Agent | Added support of negative priorities for compute tasks. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version. You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed. If you are on a version that is not listed, contact GridGain for information on upgrade options.

- 8.7.2-p15
- 8.7.3
- 8.7.4
- 8.7.5
- 8.7.5-p1
- 8.7.6
- 8.7.6-p1
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
- 8.7.26-p1
- 8.7.27
- 8.7.27-p1
- 8.7.28
- 8.7.29
- 8.7.29-p1
- 8.7.30
- 8.7.31
- 8.7.32
- 8.7.33
- 8.7.33-p2
- 8.7.34
- 8.7.35
- 8.7.36
- 8.7.37
- 8.7.38
- 8.7.39
- 8.7.40
- 8.7.41
- 8.7.42
- 8.7.43
- 8.8.1
- 8.8.2
- 8.8.3
- 8.8.4
- 8.8.5
- 8.8.6
- 8.8.7
- 8.8.8
- 8.8.9
- 8.8.10
- 8.8.11
- 8.8.12
- 8.8.13
- 8.8.14
- 8.8.15
- 8.8.16

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

#### Jetty Doesn't Accept Incorrect Configuration in GridGain 8.7.31 and Later

In GridGain 8.7.31 Jetty was upgraded to 9.4.33. Starting that version, Jetty has more strict validation of the provided configuration files. Before that version, an incorrectly spelled property in the configuration file had no effect. Starting this version, errors in the configuration will lead to an error on start.

Your setup may be affected if:

- You use the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration for REST
- The custom configuration has errors in it

You will need to fix the custom Jetty configuration before upgrading.

#### `ignite.sh` No Longer Enables Remote JMX by Default in GridGain 8.7.31 and Later

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

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
