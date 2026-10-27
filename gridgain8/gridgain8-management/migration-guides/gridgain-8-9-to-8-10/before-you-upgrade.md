---
description: >-
  Planning reference for upgrading from GridGain 8.9 to 8.10: choosing a rolling or offline upgrade, upgrade constraints, and the scope and effort of each change.
---

# What to Know Before Upgrading to GridGain 8.10

This page is the starting point for planning an upgrade from GridGain 8.9.x to GridGain 8.10. Use it to choose an upgrade path, find the changes that affect your deployment, and estimate the work involved.

When you are ready to upgrade, follow the step-by-step [Upgrade Procedure](upgrade-procedure.md).

## Choose Your Upgrade Path

You can upgrade a cluster in one of two ways:

- *Rolling upgrade.* You upgrade the nodes one at a time while the cluster stays available. This path uses [Rolling Upgrades](../../upgrade/rolling-upgrades.md), a GridGain Enterprise and Ultimate feature, and requires `rollingUpdatesEnabled=true` on every 8.9 node.
- *Offline upgrade.* You stop the cluster, install 8.10, and start all nodes from the 8.10 distribution. This path does not need `rollingUpdatesEnabled`.

Which path fits depends on the current configuration of your 8.9 cluster:

| Your 8.9 cluster | Path |
| --- | --- |
| Every node has `rollingUpdatesEnabled=true` | Rolling upgrade. No downtime for the upgrade itself. On Enterprise Edition, the backup needs a short stop of the whole cluster: see [Step 3](upgrade-procedure.md#step-3-back-up-the-data). |
| `rollingUpdatesEnabled` is not set, and you can schedule one full-cluster restart | Offline upgrade in that restart window. This is the simpler choice: you stop the cluster anyway, so there is no need to enable Rolling Upgrades first. |
| `rollingUpdatesEnabled` is not set, and you want to use Rolling Upgrades | Restart the whole cluster once with the property set, then run the rolling upgrade. See [Step 2](upgrade-procedure.md#step-2-restart-the-cluster). |

## Upgrade Constraints

Plan the upgrade with these constraints in mind:

- *Java 17 or later is required.* Every server node, client application, and application that embeds GridGain must run on Java 17 or later. See [Java 17 or Later](platform-and-modules.md#java-17-or-later).
- *Downgrade is not supported.* An 8.9 node cannot join the cluster after the rolling upgrade is finished. GridGain recommends backing up the 8.9 data before you upgrade: a full snapshot on Ultimate Edition, or a copy of `storagePath`, `walPath`, and `walArchivePath` of every node on Enterprise Edition. To go back to 8.9 after the upgrade is finished, you restore that backup, and everything written after the backup is lost. See [Recovery Path](upgrade-procedure.md#recovery-path).
- *Caches without backups are unavailable during a rolling upgrade.* Partitions that live on a stopped node cannot be served. See [Application Behavior During a Rolling Upgrade](upgrade-procedure.md#application-behavior-during-a-rolling-upgrade).
- *Some integrations have no 8.10 replacement.* Mesos deployments stay on 8.9.x. See [Removed Modules and Integrations](platform-and-modules.md#removed-modules-and-integrations).

## Which Pages Apply to You

Which pages you need depends on your role:

- *You administer the cluster.* You install, configure, and run the server nodes. Read the whole guide, starting with the [Upgrade Procedure](upgrade-procedure.md).
- *You develop an application* that embeds GridGain or connects to a cluster someone else administers. Read [Platform, Modules, and Packaging](platform-and-modules.md), [Client and Driver Changes](clients-and-drivers.md), and the permission and REST changes in [Security, Permission, and Licensing Changes](security-and-licensing.md). Coordinate the switch with the cluster administrators.
- *You maintain operational tooling* such as monitoring, scripts, and automation. Read [Configuration and Default Value Changes](configuration-and-defaults.md), and the `control.sh`, snapshot, and rolling-upgrade commands in the [Upgrade Procedure](upgrade-procedure.md).

## Upgrade Scope and Effort

Use the following tables to identify the work relevant to your environment and estimate the effort involved.

The tables group changes by responsibility: application developers and cluster operators. Two columns help you evaluate each item:

- *Applies if* — when the item is relevant. If it does not apply to your deployment, skip it.
- *Effort* — the kind of work involved:
  - *Mechanical* — a package rename, path change, or similar update with no logic changes.
  - *Config-only* — set, remove, or restore a configuration property; no code changes.
  - *Code* — a contained code change, such as a renamed API call or a small rework.
  - *Redesign* — adopt a different system or API; expect design work, implementation, and re-testing.

Some items show a range, such as *Mechanical to Code*: the effort spans those two levels depending on what your deployment uses.

### For Application Developers

These changes affect application and client code.

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 17 or later | Always, for every application that embeds GridGain, and for the thin client and JDBC driver | Mechanical | [Java 17 or Later](platform-and-modules.md#java-17-or-later) |
| Spring 7 and Spring Data module rename | Your application embeds GridGain through Spring | Mechanical to Code | [Spring 7 Required](platform-and-modules.md#spring-7-required) |
| Hibernate 7.4 | You use the Hibernate second-level cache | Code | [Hibernate 7 Required](platform-and-modules.md#hibernate-7-required) |
| Gridify API replaced by the compute API | You use `@Gridify` | Code | [Gridify API Removed](platform-and-modules.md#gridify-api-removed) |
| AWS module replaced by `ignite-aws-ext` | You use the S3 checkpoint SPI or the S3, ELB, or ALB IP finders | Code | [AWS Module Removed](platform-and-modules.md#aws-module-removed) |
| Machine learning module replaced by an extension | You use `ignite-ml` | Code | [Machine Learning Module Removed](platform-and-modules.md#machine-learning-module-removed) |
| Local store replaced by native persistence or `CacheStore` | You use `@CacheLocalStore` or `CacheFileLocalStore` | Redesign | [Local Store Support Removed](platform-and-modules.md#local-store-support-removed) |
| Cassandra store on DataStax driver 4 | You use the Cassandra store | Code | [Cassandra Store Uses the DataStax Driver 4](platform-and-modules.md#cassandra-store-uses-the-datastax-driver-4) |
| Modules with no replacement | You use Mesos | Redesign (stay on 8.9.x) | [Removed Modules and Integrations](platform-and-modules.md#removed-modules-and-integrations) |
| Java thin client timeouts | A thin client operation runs longer than 60 seconds | Config-only | [Java Thin Client Timeouts Have Default Values](clients-and-drivers.md#java-thin-client-timeouts-have-default-values) |
| Thin clients in a mixed-version cluster | Thin clients connect during a rolling upgrade, or 8.10 clients connect to 8.9 servers, and you use vector indexes or `withPartitionRecover()` | Config-only | [Thin Clients and Mixed Versions](clients-and-drivers.md#thin-clients-and-mixed-versions) |
| .NET and C++ client changes | You use the .NET or C++ client | Mechanical to Code | [Client and Driver Changes](clients-and-drivers.md) |
| REST scan queries with a filter class | You send `EXECUTE_SCAN_QUERY` with `className` | Config-only | [REST Scan Queries With a Filter Class](security-and-licensing.md#rest-scan-queries-with-a-filter-class) |
| Thin client permission and filter checks | Thin clients call Java services or register continuous query remote filters | Config-only | [Thin Client Permission and Filter Checks](security-and-licensing.md#thin-client-permission-and-filter-checks) |
| JMX object metrics are strings | A JMX tool reads `ObjectMetric` attributes | Code | [JMX Object Metrics Are Strings](configuration-and-defaults.md#jmx-object-metrics-are-strings) |

### For Cluster Operators

These changes affect cluster configuration, deployment, and operational tooling.

| What changes | Applies if | Effort | Details |
| --- | --- | --- | --- |
| Java 17 or later on every server host | Always | Config-only | [Java 17 or Later](platform-and-modules.md#java-17-or-later) |
| New `libs` folder and packaging changes | Always | Mechanical | [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes) |
| Rolling Upgrades and snapshots on 8.9 | You use the rolling upgrade path | Config-only | [Upgrade Procedure](upgrade-procedure.md) |
| Per-feature license checks | Always: compare your license with your configuration | Config-only | [Per-Feature License Checks](security-and-licensing.md#per-feature-license-checks) |
| Jetty 12 | You use a custom `jetty.xml` for the REST connector | Config-only | [Jetty 12 Is the Only REST Implementation](platform-and-modules.md#jetty-12-is-the-only-rest-implementation) |
| Lucene lines | You run `ignite-lucene-8`, or want to use Lucene 10 | Mechanical | [Lucene](platform-and-modules.md#lucene) |
| `ignite-ssh` module removed | You start remote nodes with `startNodes()` | Contact GridGain Support | [SSH Module Removed](platform-and-modules.md#ssh-module-removed) |
| SFTP host key verification | You send snapshots to an SFTP destination | Config-only | [SFTP Snapshot Transport Verifies the Host Key by Default](configuration-and-defaults.md#sftp-snapshot-transport-verifies-the-host-key-by-default) |
| Server-side SQL `COPY` | You use `COPY` against files or object stores | Config-only | [Server-Side SQL COPY](security-and-licensing.md#server-side-sql-copy) |
| Vector search limits | You use vectors with more than 4096 dimensions, or request more than 10000 neighbors | Config-only | [Vector Search Limits](configuration-and-defaults.md#vector-search-limits) |
| Stale system properties | Your startup scripts set an Apache Ignite property that GridGain does not support | Config-only | [Startup Messages for Stale Properties](configuration-and-defaults.md#startup-messages-for-stale-properties) |
| Control Center agent and OpenCensus | Your 8.9 node loads `control-center-agent` (in `libs` by default up to 8.9.38) or `ignite-opencensus` (in `libs` by default) | Mechanical | [Distribution and Packaging Changes](platform-and-modules.md#distribution-and-packaging-changes) |
