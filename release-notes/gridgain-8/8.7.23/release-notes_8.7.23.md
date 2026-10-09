---
description: >-
  GridGain 8.7.23 adds support for Spark 2.4 and delivers fixes across caching, the control script, SQL, and snapshots.
hidden: true
---

# GridGain 8.7.23 Release Notes


## New Features

- Added support for Spark 2.4.

## Changes in Behavior

This version is not compatible with Control Center 2020.07.00.
If you want to update, be sure to update your Control Center to version 2020.08.00 or later.

## Known Issues

- There is a known issue in this version that can cause an error during a [Point-in-Time](https://www.gridgain.com/docs/latest/administrators-guide/snapshots/point-in-time-recovery#point-in-time-recovery) recovery procedure.
It is safe to enable point-in-time recovery, but if you do so, we recommend you avoid restoring to point-in-time.
However, you can restore regular full and incremental snapshots.
In case you need to perform a point-in-time recovery, please contact GridGain Support.

## Fixed Issues

### Community Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-21923 | Baseline Topology | Fixed an issue where enabling baseline topology autoadjustment did not register non-baseline nodes. |
| GG-29270 | Cache | Fixed an issue with creating a cache backed by an external storage on a node that is excluded from the affinity distribution. |
| GG-29075 | Cache | Fixed an issue with concurrent expiration of cache entries touched by the `get` operation, which caused a node failure. |
| GG-21620 | Control Script | The control script now prints the cache size to the output of the `control.sh --cache list` command. |
| GG-30236 | Docker Image | Fixed an issue with the Docker image not being able to parse the `OPTION_LIBS` parameter  when it contained multiple modules. |
| GG-30085 | Platforms & Thin Clients | .NET: Fixed an NPE in the query cursor. |
| GG-30084 | Platforms & Thin Clients | .NET: Fixed `TransactionScope` behavior with read-only cache operations. |
| GG-30083 | Platforms & Thin Clients | .Net Thin Client: Fixed a memory leak that could occur when the Compute API was used. |
| GG-29957 | Platforms & Thin Clients | Fixed an issue where the order of the results returned by the Redis MGET method was incorrect. |
| GG-22225 | Storage Engine | Some internal threads that used to be anonymous now have descriptive names. |
| GG-30108 | SQL | Fixed an issue where an SQL index ended up in a broken state during data insertion when both  persistence and SQL  on-heap caching were enabled. |

### Ultimate Edition Changes

| Issue ID | Category | Description |
| --- | --- | --- |
| GG-29755 | Snapshots | Added a configuration check that fails fast the node when snapshots and point-in-time recovery are configured but the `gridgain-ultimate` module is not on the classpath. Added a warning when indexes are configured but the `ignite-indexing` module is not on the classpath. |

## Support & Lifecycle

The 8.7.X minor version will be under full support till Dec 31, 2021.
For more details please see the [Version Lifecycle](https://www.gridgain.com/docs/latest/installation-guide/versioning-and-support-lifecycle#gridgain-releases-full-support) page.

## Installation and Upgrade Information
See the [Rolling Upgrades](https://www.gridgain.com/docs/latest/administrators-guide/rolling-upgrades) page for information about how to perform automated upgrades and for details about version compatibility.

Below is a list of versions that are compatible with the current version.
You can rolling-upgrade from any of those.
Compatibility with other versions is not guaranteed.
If you are on a version that is not listed, contact GridGain for the information on upgrade options.

`8.4.2-p11`, `8.4.3-p1`, `8.4.4`, `8.4.5`, `8.4.6`, `8.4.7`, `8.4.8`, `8.4.8-p8`, `8.4.9`, `8.4.10`, `8.4.11`, `8.4.12`, `8.4.13`, `8.4.14`, `8.4.14-p2`, `8.4.15`, `8.4.16`, `8.5.3`, `8.5.5`, `8.5.6`, `8.5.7`, `8.5.8`, `8.5.8-p6`, `8.5.9`, `8.5.10`, `8.5.11`, `8.5.12`, `8.5.13`, `8.5.14`, `8.5.15`, `8.5.16`, `8.5.17`, `8.5.18`, `8.5.19`, `8.5.20`, `8.5.22`, `8.5.23`, `8.7.2`, `8.7.2-p12`, `8.7.2-p13`, `8.7.3`, `8.7.4`, `8.7.5`, `8.7.6`, `8.7.7`, `8.7.8`, `8.7.9`, `8.7.10`, `8.7.11`, `8.7.12`, `8.7.13`, `8.7.14`, `8.7.15`, `8.7.16`, `8.7.17`, `8.7.18`, `8.7.19`, `8.7.19-p1`, `8.7.20`, `8.7.21`, `8.7.22`

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
