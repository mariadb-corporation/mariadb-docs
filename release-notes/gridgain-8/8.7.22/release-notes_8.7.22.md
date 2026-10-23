---
description: >-
  GridGain 8.7.22 adds control script commands for binary metadata and a graceful shutdown policy, along with fixes across SQL, the storage engine, and thin clients.
hidden: true
---

# GridGain 8.7.22 Release Notes


## New Features

- Added commands to the control script to view, remove and update the binary types registered in the cluster.

## Changes In Behavior

- The "cache" and "query" rest commands will no longer use the "default" cache if the `cacheName` parameter is not specified.
- The experimental `IgniteConfiguration.environmentType` property is replaced with `TcpCommunicationSpi.forceClientToServerConnections`, which has the same effect.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29764 | Architecture | Removed the "default" cache from the "cache" and Query REST methods, which was used when the `cacheName` parameter was not set. The methods will return an error, "Failed to find mandatory parameter in request: cacheName", if the cache name is not specified. |
| GG-29031 | Architecture | Introduced a graceful shutdown policy that prevents data loss on node shutdown. |
| GG-29690 | Communication | The experimental "environmentType" property was replaced with `TcpCommunicationSpi.forceClientToServerConnections`. Fixed an issue where a deadlock could occur in the TcpCommunicationSpi idle connection worker. |
| GG-29877 | Control Center Agent | Control center agent: Fixed Control Center connection issues. |
| GG-26007 | Diagnostics & Failure Handling | `IgniteWalConverter` can now print WAL log data in a human-readable format. |
| GG-29658 | Discovery | Updated Netty dependency for zookeeper. |
| GG-30118 | Platforms & Thin Clients | ODBC: Decimal columns in SQL result set now have correct precision and scale. |
| GG-29619 | Storage Engine | Improved node start-up time by removing the dependency of system cache rebalancing on user caches. |
| GG-29990 | SQL | Fixed an issue where a node crashed if an index was created on a field with a mismatched data type. |
| GG-30088 | SQL | Fixed an issue where the "name" property of the `QuerySqlField` annotation was not taken into account when verifying field name uniqueness. |
| GG-29781 | Storage Engine | Fixed incorrect synchronization of index and cache stop operations causing nodes to fail with an assertion error. |
| GG-29918 | Storage Engine | Fixed incorrect throttle time calculation for speed-based throttling. |
| GG-29247 | Control Script | Added new control script commands which can be used to manage binary metadata. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29915 | Snapshots | Fixed a bug causing an incremental snapshot to always contain the whole index.bin file. |
| GG-28533 | Snapshots | Added support for non-blocking snapshots. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`

### Known Limitations

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

## We Value Your Feedback
Your comments and suggestions are always welcome. You can reach us here: https://gridgain.freshdesk.com/support/login or docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
