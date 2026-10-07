---
description: >-
  GridGain 8.7.25 improves Control Center Agent flexibility and adds index rebuild metrics, with fixes across SQL, storage, and data replication.
hidden: true
---

# GridGain 8.7.25 Release Notes


## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30463 | Atomic Cache | Reduced memory consumption when no MVCC caches are configured in the cluster |
| GG-30311 | Continuous Queries | Continuous queries are no longer deployed to client nodes, since client nodes don’t store data. |
| GG-30536 | Control Center Agent | Control Center agent now prints out a connection link as a result of token generation for convenience |
| GG-30229 | Control Center Agent | Control Center agent is no longer required to be present on all cluster nodes. The cluster can connect to Control Center when at least one node has Control Center Agent enabled. The nodes without the Control Center agent will not report metrics. |
| GG-30234 | Discovery | Updated Zookeeper dependencies: Netty to version 4.1.51.Final, log4j was excluded. |
| GG-29682 | General | Fixed a class loading exception when the package name started with 'class'. |
| GG-28939 | Integrations | Fixed an issue when default fetch size was used for data preloading for read-through cache instead of the size configured in JDBC dialect. |
| GG-30456 | Metrics & Monitoring | Added metrics that provide information about the progress of index rebuild operations. |
| GG-29934 | SQL | Fixed an issue where a primary key index contained fields in an incorrect order. |
| GG-28601 | SQL | Introduced a mode of executing `UPDATE` queries in which GridGain updates the records on the nodes where they are stored instead of fetching the records to the node that initiates the query.<br>This mode was previously available for JDBC/ODBC connections, but is now available for the queries executed via `SqlFieldsQuery` as well. See the `SqlFieldsQuery.setSkipReducerOnUpdate(boolean)` method description for details. |
| GG-29950 | SQL | Fixed an issue when a suboptimal index was chosen for a query with an `ORDER BY` expression. |
| GG-30341 | Storage Engine | Fixed an issue that could cause long pauses when speed-based write throttling was used. |
| GG-28146 | Storage Engine | Added a BinaryObject method that allows you to perform unmarshalling with a custom classloader. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30203 | Data Replication | Data Replication: Added an example with authorization via SSL certificates. |
| GG-30524 | Data Replication | The path to a keystore in `SslContextFactory` can now point to a classpath location. Previously, it was resolved only as a file system location. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30358 | Snapshot utility | Snapshot utility is now able to connect to client nodes. |
| GG-28818 | Snapshot utility | Snapshot utility: added verbose mode. |
| GG-28121 | Snapshots & PITR | Added the ability to add a prefix to the snapshot directory when creating snapshots programmatically. You can pass the prefix as an argument to the constructor of `SnapshotCreateParams`. |

## Installation and Upgrade Information

See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.5.24`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`, `8.7.24`

### Known Limitations

If you are upgrading from version 8.7.20 or earlier, you must take into account an incompatibility related to Jetty
configuration, which was introduced in GridGain 8.7.21.

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
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
