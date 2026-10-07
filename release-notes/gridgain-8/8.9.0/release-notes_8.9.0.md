---
description: >-
  GridGain 8.9 brings significant new features to GridGain ecosystem.
hidden: true
---

# GridGain 8.9.0 Release Notes

## Overview

GridGain 8.9 brings significant new features to GridGain ecosystem.

New and enhanced integrations with popular data formats - Apache Parquet, Apache Iceberg, CSV, and JSON - help you import data from these files into GridGain, and export data from GridGain to those files. This makes onboarding new applications easier, and allows you to bring GridGain's real-time analytics and transactions to data stored in data lakes and other stores supporting these formats.

For users storing data in JSON format, for example in NoSQL document databases, GridGain now offers a number of new functions to simplify working with JSON data. This allows to easily accelerate workloads using semi-structured data, and enable them to use GridGain's ANSI SQL and ACID transactions.

Users in high-performance environments can benefit from the new NUMA-aware allocation mode. When enabled, GridGain will allocate data to RAM that can interact with the processor fastest, providing a noticeable improvement in performance.

Some outdated modules were removed from the installation package.

## New Features

### Data Import from Parquet, CSV and Iceberg

Both data import and export are handled by using the `COPY INTO` SQL statement. For example, here is how you can import data from your CSV file:

```sql
/* Import data from CSV */
COPY FROM '/localstore/data.csv'
INTO Table1 (name, age)
FORMAT CSV
```

For more information, see [SQL Reference](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/operational-commands#copy-into).

### JSON Functions

JSON functions simplify work with JSON stored in SQL. For example, use the following function to access a field of a JSON document that's stored in a column of a table:

```sql
SELECT JSON_QUERY(T.JSON_FIELD, '$.a.b.c') FROM T;
```

For more information, see [JSON Functions](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/json-functions).

### NUMA Memory Allocation

NUMA-aware memory allocation can be used in high-performance environments. To make sure GridGain is using NUMA allocation, set up the `memoryAllocator` property in data regions configuration:

```
<property name="memoryAllocator">
  <bean class="org.apache.ignite.mem.NumaAllocator">
    <constructor-arg>
      <bean class="org.apache.ignite.mem.SimpleNumaAllocationStrategy"/>
    </constructor-arg>
  </bean>
</property>
```

You can configure either simple or interleaved allocation strategy for either the entire cluster or for specific nodes.  For more information, see [NUMA-Aware memory allocation](https://www.gridgain.com/docs/gridgain8/latest/perf-troubleshooting-guide/memory-tuning#numa-aware-memory-allocation) section of the documentation.

## Changes in Behavior

### COPY Command Changes

In GridGain Enterprise and Ultimate editions, a new [SQL `COPY` command](https://www.gridgain.com/docs/gridgain8/latest/sql-reference/operational-commands#copy-into) was introduced. The new implementation is supported on all clients, and supports not only CSV format, but also Parquet and Iceberg.

The syntax for CSV remains unchanged in the new implementation. As the new implementation is executed on node rather than thin client, make sure the **node** has access to the folder used for exporting or importing data.

## Visor CMD and Visor GUI Removed From Installation

Visor CMD and Visor GUI are both legacy desktop-based management utilities for GridGain that have been in the End-of-Life state for several years, not receiving bug fixes or security updates. Starting 8.9.0, these utilities are no longer shipped as part of GridGain Platform.

Users of these utilities should upgrade to GridGain Control Center - the latest management console for GridGain Platform and Apache Ignite. [Connect your cluster in minutes](https://www.gridgain.com/products/control-center) with no installation required or [Contact us](https://www.gridgain.com/contact) for details.

## Removed Modules

The optional `scalar`, `scalar-2.10`, and `spark` modules are no longer provided with GridGain 8.9.

Spark integration can be migrated to Apache Ignite Extension `spark` module:

```
<dependency>
  <groupId>org.apache.ignite</groupId>
  <artifactId>ignite-spark-ext</artifactId>
  <version>${ignite-spark-ext.version}</version>
</dependency>
```

## Improvements and Fixed Issues

### Enterprise Edition Changes

| Issue ID | Category | Description |
|---|---|---|
| GG-36899 | Cluster SQL Engine | It is now possible to export cache data to a CSV file. |
| GG-36898 | Cluster SQL Engine | It is now possible to import data from CSV files. |
| GG-36815 | Licenses | Added the specific time when the license grace period ends to log messages. |
| GG-36722 | General | Removed support for Visor CMD. |
| GG-36721 | General | Removed the ignite-scalar optional module. |
| GG-36430 | Licenses | License end date now triggers immediate cluster termination. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

### Migrating From GridGain 8.X

When migrating from GridGain 8.8 to GridGain 8.9, no special actions are required for core functionality migration. By using [rolling upgrades](https://www.gridgain.com/docs/gridgain8/latest/installation-guide/rolling-upgrades), you can update from any GridGain version listed below.

{% hint style="info" %}
While updates from GridGain 8.7.X and earlier 8.8.X  versions are possible, they may require additional actions to your configuration and  depending on cumulative changes in the version.
{% endhint %}

- If you are using GridGain Enterprise or Ultimate, the `COPY` command was reworked as described in the COPY Command Changes section. The syntax for working with CSV remains the same, but the path is now calculated on the **node** and the client. This change does not affect GridGain Community edition.

  To disable this behavior and use the old copy command, pass the `disabledFeatures=SERVER_BULK_LOAD` parameter in the JDBC connection command:

  ```
  jdbc:ignite:thin://127.0.0.1/?disabledFeatures=SERVER_BULK_LOAD
  ```

- If you are using one of the optional modules listed in the Removed Modules section, they will continue to work, but compatibility and stability on GridGain 8.9 is not guaranteed. Consider using the alternatives:
  - Visor CMD and GUI can be replaced by [GridGain Control Center](https://www.gridgain.com/docs/control-center/latest/overview#system-requirements).
  - The spark module can be replaced by the Spark [Ignite Extension](https://github.com/apache/ignite-extensions).

### Older GridGain Versions Compatibility

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for information on upgrade options.

`8.7.22`, `8.7.28`, `8.7.29-p1`, `8.7.32`, `8.7.34`, `8.7.38`, `8.7.42-p2`, `8.8.1`, `8.8.2`, `8.8.2-p1`, `8.8.3`, `8.8.4`, `8.8.4-p2`, `8.8.5`, `8.8.6`, `8.8.7`, `8.8.8`, `8.8.8-p1`, `8.8.9`, `8.8.9-p1`, `8.8.10`, `8.8.11`, `8.8.12`, `8.8.13`, `8.8.13-p2`, `8.8.14`, `8.8.15`, `8.8.16`, `8.8.16-p2`, `8.8.17`, `8.8.18`, `8.8.18-p1`, `8.8.19`, `8.8.19-p1`, `8.8.20`, `8.8.21`, `8.8.22`, `8.8.22-p1`, `8.8.23`, `8.8.23-p3`, `8.8.24`, `8.8.25`, `8.8.25-p1`, `8.8.26`, `8.8.27`, `8.8.28`, `8.8.29`, `8.8.30`, `8.8.31`, `8.8.32`, `8.8.33`, `8.8.34`

### Apache Ignite Versions Compatibility

Below is a list of versions that are tested for basic compatibility with the current version. If you are on a version that is not listed, contact GridGain for information on upgrade options.

`2.11.1`, `2.12.0`, `2.13.0`,  `2.14.0`

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

#### .NET: GridGain Nuget Package Misses GridGain.Ignite Jars in 8.8.17 and Later

Add the `GridGain.Ignite` dependency to your project, so that jars from it are included.

#### .NET: Docker Images Need Additional Configuration

To run .NET SDK commands, install the .NET SDK. For more details, click [here](https://docs.microsoft.com/en-us/dotnet/core/install/windows?tabs=net60#dependencies).

## We Value Your Feedback

Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
