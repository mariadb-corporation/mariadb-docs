---
description: >-
  GridGain 8.7.29 adds scheduled snapshot checks and delivers fixes across the Control Center Agent, the SQL engine, storage, and thin clients.
hidden: true
---

# GridGain 8.7.29 Release Notes


## New Features

### Checking snapshots on a schedule

Added ability to schedule snapshot checks using Snapshot Utility

## Improvements and Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30975 | Control Center Agent | Fixed a bug preventing the GridGain cluster activation/deactivation (8.7.27 and higher) via Control Center 2020.08.00. |
| GG-31084 | Control Center Agent | Fixed an error that led to “Connection closed” message when multiple Control Center URIs are configured. |
| GG-31085 | Cluster SQL Engine | Fixed an issue causing errors on arithmetic operations that use DATE, TIME, and TIMESTAMP types. |
| GG-30757 | Cluster Storage Engine | Fixed an issue where compute jobs could not load user-defined classes through peer class loading. |
| GG-29269 | Cluster Storage Engine | Fixed an issue where the cache size could return a wrong value when TTL is enabled. |
| GG-30931 | Platforms & Thin Clients | Added support of using CMake for building Ignite C++ on Windows platform. |
| GG-31018 | Cluster Control Script | Fixed an issue with the 'help' command for control command line utility. |
| GG-28222 | Platforms & Thin Clients | Added shuffling of remote IP addresses for ODBC and C++ thin clients that can be useful for cases when DNS-level balancing is used. |
| GG-30825 | Cluster SQL Engine | Fixed the JDBC property names reported to external tools. |
| GG-30492 | Cluster SQL Engine | Disabled optional usage of ICU4J in H2 library which prevented it from working on recent JVM1.8 patch levels such as u262. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-24792 | Cluster Snapshot Utility | Added ability to schedule snapshot checks using Snapshot Utility. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those. Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`,
`8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`,
`8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`,
`8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`,
`8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`, `8.7.25`, `8.7.26`, `8.7.27`, `8.7.28`

### Known Limitations

#### Jetty configuration incompatibility in GridGain 8.7.21 and later

If you are upgrading from version 8.7.20 or earlier, you must take into account an incompatibility related to Jetty configuration, which was introduced in GridGain 8.7.21.

Your setup may be affected if:

- You're using the `ignite-rest-http` module (e.g. to connect to GridGain Web Console)
- You have a custom Jetty configuration that enables SSL for REST
- Your Jetty configuration uses the `org.eclipse.jetty.util.ssl.SslContextFactory` class
- The keystore specified in the Jetty configuration contains both the CA certificate and the private certificate

In this case, after starting the new version, you'll see an error similar to:

```text
java.lang.IllegalStateException: KeyStores with multiple certificates are not supported on the base class
org.eclipse.jetty.util.ssl.SslContextFactory. (Use org.eclipse.jetty.util.ssl.SslContextFactory$Server
or org.eclipse.jetty.util.ssl.SslContextFactory$Client instead)
```

To workaround this issue, you need to alter the Jetty configuration to use `org.eclipse.jetty.util.ssl.SslContextFactory$Server` or `org.eclipse.jetty.util.ssl.SslContextFactory$Client`.
For a configuration example, see [Client Certificate Authentication](https://www.gridgain.com/docs/latest/administrators-guide/security/authentication#client-certificate-authentication).

#### Default `rebalanceThreadPoolSize` in GridGain 8.7.26 and later

In GridGain 8.7.26, the default value of the property `IgniteConfiguration.rebalanceThreadPoolSize` has changed from `1` to `min(4, number of CPU / 4)`.
It may cause a compatibility issue under the following conditions:

- A Rolling Upgrade is being performed
- The upgrade is performed from a version 8.5.7 or earlier for 8.5.x, or 8.7.3 or earlier for 8.7.x
- The server nodes have at least 8 CPU cores
- The nodes configuration don't have the property `IgniteConfiguration.rebalanceThreadPoolSize` set (i.e. the default value is used)

In this case, you'll see an error similar to

```text
сlass org.apache.ignite.IgniteException: Rebalance configuration mismatch (fix configuration or set -DIGNITE_SKIP_CONFIGURATION_CONSISTENCY_CHECK=true system property).
Different values of such parameter may lead to rebalance process instability and hanging.  [rmtNodeId=5fc58fb7-209d-489a-8034-0127a81abed6, locRebalanceThreadPoolSize = 4, rmtRebalanceThreadPoolSize = 1]
```

To workaround this issue, you need to change the configuration of the server nodes to set `rebalanceThreadPoolSize=1` so that it matches
the old default. Example:

```xml
<bean class="org.apache.ignite.configuration.IgniteConfiguration">
    <property name="rebalanceThreadPoolSize" value="1"/>

    <!-- The rest of the configuration goes here -->
</bean>
```

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
