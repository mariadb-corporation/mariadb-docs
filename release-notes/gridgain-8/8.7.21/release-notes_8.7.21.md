---
description: >-
  GridGain 8.7.21 upgrades the Jetty dependency to address security issues and delivers fixes across caching, thin clients, integrations, and the snapshot utility.
hidden: true
---

# GridGain 8.7.21 Release Notes

## Changes in Behavior

### Jetty Configuration

In this version, Jetty dependency has been upgraded from 9.4.22 to 9.4.26 to address security issues.
The new version has a breaking change, which causes some Jetty configurations not to work.
Please see the [Known Limitations](#known-limitations) section below for more information.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-25084 | Affinity and Baseline Topology | Introduced new cluster activation/deactivation API. Added the ability to activate cluster in read-only mode. |
| GG-29720 | Cache | Fixed a possible `NullPointerException` in Cache API that could be thrown when a client reconnected. |
| GG-29699 | General | Fixed an issue with registering lambda's enclosing class in the marshaller that could cause errors when the fields of the enclosing class were changed. |
| GG-28374 | Platforms & Thin Clients | .NET: Added an implementation of `IgniteLock` reentrant lock. |
| GG-29795 | Platforms & Thin Clients | .NET: Added the ability to use `SqlFieldsQuery` as an initial query in `ContinuousQuery`. |
| GG-29575 | Platforms & Thin Clients | .NET: Fixed an issue with invoking service methods with typed arrays as an argument. |

### Enterprise Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29532 | Data Replication | Fixed an issue where the failure handler reported DR threads as blocked even though Data Replication was not configured. |
| GG-28348 | Integrations | Fixed an issue where a large amount of tasks in Kafka Sink Connector led to performance degradation due to POJO deserialization. |
| GG-29705 | Integrations | Fixed a cursor leak in `RunningQueryManager` when executing queries via spring-data repositories. |
| GG-29706 | Integrations | Fixed the incorrect processing of non-comparable keys in the repository methods `findAllById(ids)` and `deleteAllById(ids)` for spring-data. |
| GG-27799 | Integrations | Added an option to prevent flushing every record in Kafka Sink Connector. Instead, you can set the `flushOnOffsetCommit` property to flush records on offset commit. |
| GG-29272 | Integrations | Updated spring-data dependencies to recent versions. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-14450 | Snapshot utility | Added the `-verbose` option to the snapshot utility, which prints the topology information when users create a snapshot. |
| GG-25597 | Snapshot utility | Fixed the incorrect report of the progress of the snapshot create operation in the snapshot utility when compression was enabled. |

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`,
`8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`

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
