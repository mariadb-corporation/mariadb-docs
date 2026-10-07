---
description: >-
  GridGain 8.7.24 delivers fixes and improvements across continuous queries, rebalancing, SQL indexing, thin clients, and the storage engine.
hidden: true
---

# GridGain 8.7.24 Release Notes


## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-30311 | Continuous Queries | Continuous queries are no longer deployed to client nodes, since client nodes don’t store data. |
| GG-29740 | Control Script | The code that processes control script commands is now provided as a separate module (`ignite-control-utility`, enabled by default in the binary package). |
| GG-30074 | GMC | Optimized data transfer for snapshot descriptors. |
| GG-30386 | Platforms & Thin Clients | .NET: Improved serialization performance for enum fields. |
| GG-30266 | Platforms & Thin Clients | .NET: Added continuous query API for .NET Thin Client. |
| GG-30206 | Platforms & Thin Clients | C++: Implemented cluster API. |
| GG-30146 | Rebalance | Introduced a heuristic to determine when a historical rebalancing is more efficient. The `-DIGNITE_PDS_WAL_REBALANCE_THRESHOLD` property is still present, but its default value was changed to 500. The heuristic is applied to the partitions that are larger than the given value. |
| GG-27964 | Rebalance | Fixed a rare bug that caused partition consistency conflicts during a historical rebalance. |
| GG-28024 | SQL | <br>The default index inline size for varchar and binary columns was increased. For VARCHAR columns with a given length (e.g. `VARCHAR (15)`), the default inline size is calculated as `length + 3`.<br>For composite indexes, the default inline size is the sum of default inline sizes of each column plus the inline size of the primary key.<br>The default value for the `IGNITE_MAX_INDEX_PAYLOAD_SIZE` was increased to 64. |
| GG-30394 | Storage Engine | Fixed an issue when a node could crash during Point-in-Time Recovery procedure. Also fixed an issue when a historical rebalance erroneously wouldn’t start. |
| GG-29896 | Transactions | Fixed an issue which could cause an error when a transaction and a cache destroy operation were executed concurrently. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`, `8.7.23`

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
Your comments and suggestions are always welcome. You can reach us here: docs@gridgain.com

Please visit the [documentation](https://gridgain.com/docs) for more information.
