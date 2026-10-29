---
description: >-
  Planning reference for upgrading from GridGain 8.9 to 8.10: choosing a rolling or offline upgrade, upgrade constraints, and the scope and effort of each change.
---

# What to Know Before Upgrading to GridGain 8.10

Read this page before you upgrade a cluster from GridGain 8.9.39 to 8.10. It helps you choose an upgrade path, find the changes that affect you, and estimate the work. When you are ready, follow the [Upgrade Procedure](upgrade-procedure.md).

{% hint style="info" %}
This guide uses 8.9.39 for the primary starting version, 8.9.x for behavior across the 8.9 line, and 8.9 for a cluster or node that you work with.
{% endhint %}

## Supported Starting Versions

You can upgrade to 8.10 from the following 8.9.x releases.

<details>

<summary>Show supported releases</summary>

`8.9.0`, `8.9.1`, `8.9.5`, `8.9.8`, `8.9.9`, `8.9.12`, `8.9.13`, `8.9.14`, `8.9.14-p2`, `8.9.15`, `8.9.16`, `8.9.16-p1`, `8.9.16-p2`, `8.9.16-p3`, `8.9.17`, `8.9.17-p1`, `8.9.18`, `8.9.19`, `8.9.20`, `8.9.20-p1`, `8.9.20-p2`, `8.9.21`, `8.9.22`, `8.9.22-p1`, `8.9.22-p2`, `8.9.23`, `8.9.23-p1`, `8.9.24`, `8.9.25`, `8.9.26`, `8.9.27`, `8.9.28`, `8.9.29`, `8.9.30`, `8.9.31`, `8.9.32`, `8.9.33`, `8.9.33-p1`, `8.9.34`, `8.9.35`, `8.9.36`, `8.9.37`, `8.9.38`, `8.9.39`

</details>

{% hint style="info" %}
If your cluster runs a release that is not listed, contact MariaDB [support](https://mariadb.com/support/) before you upgrade. Behavior can differ in places between releases. See the [release notes](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/aEnK0ZXmUbJzqQrTjFyb/gridgain-8/README.md) for the releases between your version and 8.9.39 first.
{% endhint %}

## Choose Your Upgrade Path

- *Rolling upgrade.* You upgrade the nodes one at a time while the cluster stays available. It uses [Rolling Upgrades](../../upgrade/rolling-upgrades.md), an Enterprise and Ultimate feature, and requires `rollingUpdatesEnabled=true` on every 8.9 node.
- *Offline upgrade.* You stop the cluster and start every node from the 8.10 distribution. It does not need `rollingUpdatesEnabled`.

The right path depends on your 8.9 cluster:

| Your 8.9 cluster | Path |
| --- | --- |
| Every node has `rollingUpdatesEnabled=true` | Rolling upgrade, with no downtime for the upgrade itself. On Enterprise Edition, the backup needs a short stop of the whole cluster. See [Step 3](upgrade-procedure.md#step-3-back-up-the-data). |
| `rollingUpdatesEnabled` is not set, and you can schedule one full-cluster restart | Offline upgrade in that window. It is simpler, because you stop the cluster anyway. |
| `rollingUpdatesEnabled` is not set, and you want a rolling upgrade | Restart the whole cluster once with the property set, then upgrade. See [Step 2](upgrade-procedure.md#step-2-restart-the-cluster). |

## Upgrade Constraints

- *Java 17 or later is required.* Every server node, client application, and application that embeds GridGain must run on it. See [Java 17 or Later](platform-and-modules.md#java-17-or-later).
- *Downgrade is not supported.* An 8.9 node cannot join the cluster after the rolling upgrade is finished. Back up the 8.9 data first. On Ultimate Edition, take a full snapshot. On Enterprise Edition, which has no snapshots, copy the `db` folder of every node, and also the folders that `storagePath`, `walPath`, and `walArchivePath` point to if you set them. After the upgrade, restoring that backup is the only way to recover 8.9, and everything written after the backup is lost. See [Recovery Path](upgrade-procedure.md#recovery-path).
- *Caches without backups are unavailable during a rolling upgrade.* Partitions on a stopped node cannot be served. See [Application Behavior During a Rolling Upgrade](upgrade-procedure.md#application-behavior-during-a-rolling-upgrade).
- *Some integrations have no 8.10 replacement.* Mesos deployments stay on 8.9.x. See [Removed Modules and Integrations](platform-and-modules.md#removed-modules-and-integrations).

## Which Pages Apply to You

- *Cluster administrators* install, configure, and run the server nodes. Read the whole guide, starting with the [Upgrade Procedure](upgrade-procedure.md).
- *Application developers* embed GridGain or connect to a cluster that someone else administers. Read [Platform, Modules, and Packaging Changes](platform-and-modules.md), [Client and Driver Changes](clients-and-drivers.md), and the permission and REST changes in [Security, Permission, and Licensing Changes](security-and-licensing.md). Coordinate the switch with the cluster administrators.
- *Teams that maintain operational tooling* such as monitoring, scripts, and automation read [Configuration and Default Value Changes](configuration-and-defaults.md), and the `control.sh`, snapshot, and rolling-upgrade commands in the [Upgrade Procedure](upgrade-procedure.md).

## Upgrade Scope and Effort

The tables list each change, when it applies to you, and the effort it needs. If an item does not apply to your deployment, skip it.

*Effort* is one of the following:

- *Mechanical.* A rename, path change, or similar update with no logic changes.
- *Config-only.* Set, remove, or restore a configuration property. No code changes.
- *Code.* A contained code change, such as a renamed API call.
- *Redesign.* Adopt a different system or API. Expect design work and retesting.
- *Contact Support.* No documented replacement exists. Contact MariaDB [support](https://mariadb.com/support/) before you upgrade.

A range such as *Mechanical to Code* means that the effort depends on what you use.

### For Application Developers

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 17 or later | Always: embedding applications, the thin client, and the JDBC driver | Mechanical | [Java 17 or Later](platform-and-modules.md#java-17-or-later) |
| Spring 7 and Spring Data module rename | Your application embeds GridGain through Spring | Mechanical to Code | [Spring 7 Required](platform-and-modules.md#spring-7-required) |
| Hibernate 7.4 | You use the Hibernate second-level cache | Code | [Hibernate 7 Required](platform-and-modules.md#hibernate-7-required) |
| Gridify API replaced by the compute API | You use `@Gridify` | Code | [Gridify API Removed](platform-and-modules.md#gridify-api-removed) |
| AWS module replaced by `ignite-aws-ext` | You use the S3 checkpoint SPI or the S3, ELB, or ALB IP finders | Code | [AWS Module Removed](platform-and-modules.md#aws-module-removed) |
| Machine learning module replaced by an extension | You use `ignite-ml` | Code | [Machine Learning Module Removed](platform-and-modules.md#machine-learning-module-removed) |
| Local store replaced by native persistence or `CacheStore` | You use `@CacheLocalStore` or `CacheFileLocalStore` | Redesign | [Local Store Support Removed](platform-and-modules.md#local-store-support-removed) |
| Cassandra store on DataStax driver 4 | You use the Cassandra store | Code | [Cassandra Store Uses the DataStax Driver 4](platform-and-modules.md#cassandra-store-uses-the-datastax-driver-4) |
| Modules with no replacement | You use Mesos. Stay on 8.9.x or move to another system | Redesign | [Removed Modules and Integrations](platform-and-modules.md#removed-modules-and-integrations) |
| Java thin client timeouts | A thin client operation runs longer than 60 seconds | Config-only | [Java Thin Client Timeouts Have Default Values](clients-and-drivers.md#java-thin-client-timeouts-have-default-values) |
| Thin clients in a mixed-version cluster | An 8.10 client uses vector indexes or `withPartitionRecover()` against an 8.9 server, including during a rolling upgrade | Config-only | [Thin Clients and Mixed Versions](clients-and-drivers.md#thin-clients-and-mixed-versions) |
| .NET and C++ client changes | You use the .NET or C++ client | Mechanical to Code | [Client and Driver Changes](clients-and-drivers.md) |
| REST scan queries with a filter class | You send `EXECUTE_SCAN_QUERY` with `className` | Config-only | [REST Scan Queries With a Filter Class](security-and-licensing.md#rest-scan-queries-with-a-filter-class) |
| Thin client permission and filter checks | Thin clients call Java services or register continuous query remote filters | Config-only | [Thin Client Permission and Filter Checks](security-and-licensing.md#thin-client-permission-and-filter-checks) |
| JMX object metrics are strings | A JMX tool reads `ObjectMetric` attributes | Code | [JMX Object Metrics Are Strings](configuration-and-defaults.md#jmx-object-metrics-are-strings) |

### For Cluster Administrators

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 17 or later on every server host | Always | Mechanical | [Java 17 or Later](platform-and-modules.md#java-17-or-later) |
| New `libs` folder and packaging changes | Always | Mechanical | [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes) |
| Rolling Upgrades and snapshots on 8.9 | You use the rolling upgrade path | Config-only | [Upgrade Procedure](upgrade-procedure.md) |
| Per-feature license checks | Always. Compare your license with your configuration | Config-only | [Per-Feature License Checks](security-and-licensing.md#per-feature-license-checks) |
| Jetty 12 | You use a custom `jetty.xml` for the REST connector | Config-only | [Jetty 12 Is the Only REST Implementation](platform-and-modules.md#jetty-12-is-the-only-rest-implementation) |
| Lucene lines | You run `ignite-lucene-8`, or want to use Lucene 10 | Mechanical | [Lucene](platform-and-modules.md#lucene) |
| `ignite-ssh` module removed | You start remote nodes with `startNodes()` | Contact Support | [SSH Module Removed](platform-and-modules.md#ssh-module-removed) |
| SFTP host key verification | You send snapshots to an SFTP destination | Config-only | [SFTP Snapshot Transport Verifies the Host Key by Default](configuration-and-defaults.md#sftp-snapshot-transport-verifies-the-host-key-by-default) |
| Server-side SQL `COPY` | You use `COPY` against files or object stores | Config-only | [Server-Side SQL COPY](security-and-licensing.md#server-side-sql-copy) |
| Vector search limits | You use vectors with more than 4096 dimensions, or request more than 10000 neighbors | Config-only | [Vector Search Limits](configuration-and-defaults.md#vector-search-limits) |
| Stale system properties | Your startup scripts set an unsupported Apache Ignite property | Config-only | [Startup Messages for Stale Properties](configuration-and-defaults.md#startup-messages-for-stale-properties) |
| Control Center agent and OpenCensus | Your 8.9 node loads `control-center-agent` or `ignite-opencensus` | Mechanical | [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes) |
