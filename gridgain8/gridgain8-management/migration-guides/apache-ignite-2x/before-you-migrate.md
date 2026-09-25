---
description: >-
  Planning reference for migrating from Apache Ignite 2.18 to GridGain 8:
  prerequisites, migration constraints, a compatibility summary, and effort estimates.
---

# What to Know Before Migrating from Apache Ignite 2.x

This page is the starting point for planning a migration from Apache Ignite 2.18 to the latest GridGain 8 Ultimate release. Use it to identify the changes relevant to your deployment and estimate the work involved.

GridGain 8 forked from Apache Ignite around version 2.7. The two products remain largely compatible, so most APIs, configuration, on-disk formats, and application code carry over unchanged.

Most migration work falls into three areas: cluster cutover, configuration changes, and feature replacement. The sections below explain each area and help you determine which changes apply to your deployment.

*On this page:*

* [Before You Begin](#before-you-begin) — the license, downtime, and backups to have in place first
* [Migration Constraints](#migration-constraints) — hard rules that shape the cutover plan
* [Compatibility Summary](#compatibility-summary) — what works, what doesn't, at a glance
* [Migration Scope and Effort](#migration-scope-and-effort) — the ranked work list: who each change affects and how much effort it takes

*Detailed topics:*

* [Features to Replace](features-to-replace.md) — features that need a code change or a workaround
* [Configuration and Validation Changes](configuration.md) — changed defaults, removed properties, binary field ordering
* [APIs, Clients, and Extensions](apis-and-clients.md) — the SQL engine, per-language client changes, and custom plugins and SPIs
* [Artifacts and Deployment](artifacts-and-modules.md) — distribution, build coordinates, Docker, modules
* [Monitoring and CLI Changes](operations.md) — logs, metrics, system views, events, and `control.sh` / `ignite.sh`
* [Security Authorization Changes](security-authorization.md) — permission grants that changed or were removed in GridGain 8

When you are ready to execute the migration, follow the step-by-step [Migration Procedure](migration-procedure.md).

## Before You Begin

Have the following in place before you plan the migration:

- *A GridGain 8 license.* GridGain 8 Ultimate Edition requires a license file. The enterprise features that migrations most often depend on, such as Data Center Replication, enterprise snapshots, and enterprise security, will not start without a valid one. Obtain the license and install it as described in [Licensing](../../licensing.md).
- *Scheduled downtime.* The cutover stops the whole cluster, converts it, and restarts it on GridGain. Ignite and GridGain nodes cannot run together, so there is no rolling upgrade (see [Migration Constraints](#migration-constraints)).
- *Backup storage.* Reserve space for a full backup of the persistence directory, taken before the first GridGain start. It is your only rollback path once GridGain writes.
- *Distributions.* The GridGain 8 distribution for your platform, plus your existing Apache Ignite distribution kept archived until the migration is confirmed stable.

The [Migration Procedure](migration-procedure.md) expands these into a pre-cutover checklist.

## Migration Constraints

Keep in mind these constraints before migrating your cluster:

- *One-way upgrade.* Once GridGain writes to the persistence directory, Apache Ignite can no longer read it.
- *CDC must be off at the last write.* GridGain can start on Ignite's persistence only if Change Data Capture was disabled when the data was last written. Stop all CDC processes and disable CDC before the final checkpoint and shutdown.
- *Full cutover, no mixed topology.* Ignite and GridGain server nodes cannot coexist in one cluster, and clients are not cross-compatible.
- *In-memory data is not carried over.* Data in non-persistent regions does not survive the cutover. Plan to reload it from its original sources, as after any cluster restart. See [Persistent and In-Memory Clusters](migration-procedure.md).
- *Planned downtime is required.* The whole cluster stops, converts, and restarts as GridGain; all clients are updated before reconnecting.
- *No in-place rollback* after the first GridGain write. Rollback is possible only by restoring a pre-cutover backup.

These constraints mean that all server nodes and clients must be upgraded together. Take a full backup before the first GridGain start and keep the Ignite distribution archived until the migration is confirmed stable.

## Compatibility Summary

This is the high-level picture of what works, what does not, and what needs attention.

| Area | Status | What it means for you |
|---|---|---|
| Inter-node protocols (Discovery, Communication) | Incompatible | Ignite and GridGain server nodes cannot coexist in one cluster, so a full cutover is required. |
| Thick clients (join the topology) | Incompatible | Clients must be rebuilt against GridGain and updated before connecting. |
| Thin client, JDBC, ODBC protocols | Incompatible | Update all clients before connecting. They may appear to connect because the protocols share common roots, but fail on anything beyond basic operations. |
| Persistent data | Compatible, one-way | GridGain can start on Ignite's [Native Persistence](../../../architecture/storage/native-persistence.md) if conditions are met (clean shutdown, CDC disabled, consistent binary field-sort setting). Once GridGain writes, Ignite can no longer read it. |
| In-memory data | Not carried over | Data in non-persistent regions does not survive the full-cluster cutover. Reload it the way you reload after any restart: `CacheStore` loading or your data-loading jobs. |
| Configuration | Mostly compatible | Some defaults differ, some properties don't exist in GridGain, and GridGain validates more strictly. |
| APIs (Java, SQL, REST) | Mostly compatible | Core cache, compute, and service APIs are largely compatible. Differences exist in specific areas. |
| CLI (`ignite.sh`, `control.sh`) | Mostly compatible | Some commands are added, removed, or renamed. |
| Runtime behavior | Differs in places | Stricter validation, different error handling, and changed service-deployment timing, even where the same code compiles and runs. |

Most APIs are compatible, so most application code compiles and runs unchanged once rebuilt against GridGain. The main exceptions are features that were removed or replaced. Check which of the following apply to your deployment:

- *Replaced by a GridGain enterprise equivalent* with a different API. For example, CDC is replaced by Data Center Replication.
- *Experimental Ignite features that were dropped.* Where a supported alternative exists, migrate to it. For example, the Calcite engine is replaced by H2.
- *Features with no direct equivalent.* These require a workaround or redesign. For example, Cache Dump.

The [Features to Replace](features-to-replace.md) topic describes each affected feature and the required migration path. Configuration related to removed features must also be removed; see [Server Configuration Differences](configuration.md).

## Migration Scope and Effort

Use the following tables to identify the work relevant to your environment and estimate the effort involved.

The tables group changes by responsibility: application developers and cluster operators. Within each group, items are roughly ordered from changes that affect every migration to changes that apply only to specific features.

Two columns help you evaluate each item:

- *Applies if* — when the item is relevant. If it does not apply to your deployment, skip it.
- *Effort* — the kind of work involved:
  - *Mechanical* — a package rename, path change, or similar update with no logic changes.
  - *Config-only* — set, remove, or restore a configuration property; no code changes.
  - *Code* — a contained code change, such as a renamed API call or a small rework.
  - *Redesign* — adopt a different system or API; expect design work, implementation, and re-testing.

Some items show a range, such as *Mechanical to Code*: the effort spans those two levels depending on which features your deployment uses.

### For Application Developers

These changes affect application and client code.

| What changes | Applies if | Effort | Details |
|---|---|---|---|
| Build coordinates and dependencies | Always | Mechanical | [Build Coordinates](artifacts-and-modules.md#build-coordinates) |
| Rebuild and update all clients | Always | Mechanical and Code | [Clients](apis-and-clients.md#clients) |
| Calcite SQL engine → H2 | You set `queryEngine=calcite` | Code + re-test queries | [SQL Changes](apis-and-clients.md#sql-changes) |
| CDC → Data Center Replication or Kafka Connect | You run Change Data Capture | Redesign | [Features to Replace](features-to-replace.md) |
| Snapshots → GridGain snapshots | You script or automate Ignite snapshots | Redesign | [Features to Replace](features-to-replace.md) |
| Security plugins → GridGain security | You use a custom `GridSecurityProcessor` or built-in authentication | Redesign | [Features to Replace](features-to-replace.md) |
| Security permissions → remap to the GridGain 8 set | Your security policy grants fine-grained admin permissions existing in Ignite 2.18 (`ADMIN_CLUSTER_STATE`, `ADMIN_KILL`, `ADMIN_USER_ACCESS`, and similar) | Mechanical | [Security Authorization Changes](security-authorization.md) |
| Custom plugins and SPIs | You maintain custom SPI or plugin implementations | Code and Redesign | [Plugins and Custom SPIs](apis-and-clients.md) |
| Other feature replacements (Read Repair, service interceptors, Metrics API, transaction-aware queries, Cache Dump, multi-disk storage, Performance Statistics, thin-client callbacks) | You use the specific feature | Code | [Features to Replace](features-to-replace.md) |

### For Cluster Operators

These changes affect cluster configuration, deployment, and operational tooling.

| What changes | Applies if | Effort | Details |
|---|---|---|---|
| Changed configuration defaults | Always | Config-only | [Changed Defaults](configuration.md#changed-defaults) |
| Removed configuration properties | You configured CDC, snapshots, Calcite, or multi-disk storage | Config-only | [Removed Configuration Properties](configuration.md#removed-configuration-properties) |
| Binary object field-sort property | You set `IGNITE_BINARY_SORT_OBJECT_FIELDS` | Config-only | [Binary Object Field Ordering](configuration.md) |
| Security permissions → remap to the GridGain 8 set | Your security policy grants fine-grained admin permissions that GridGain 8 no longer recognizes (`ADMIN_CLUSTER_STATE`, `ADMIN_KILL`, `ADMIN_USER_ACCESS`, and similar) | Mechanical | [Security Authorization Changes](security-authorization.md) |
| CLI and script changes | You have operational scripts or automation | Code | [CLI Changes](operations.md) |
| Monitoring (logs, metrics, system views, events) | You have monitoring or log-parsing tooling | Code | [Monitoring](operations.md#monitoring) |
| Docker / container setup | You run in containers | Mechanical | [Docker](artifacts-and-modules.md#docker) |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
