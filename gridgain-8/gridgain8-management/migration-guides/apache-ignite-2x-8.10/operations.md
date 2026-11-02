---
description: >-
  Monitoring and command-line changes when migrating from Apache Ignite 2.18 to
  GridGain 8.10, covering logs, metrics, system views, events, and the CLI tools.
---

# Monitoring and CLI Changes

This page covers changes to the monitoring stack (logs, metrics, system views, events) and to the command-line tools (`control.sh`, `ignite.sh`, `sqlline`, `ignite-cdc.sh`).

*Skip this page if you have no monitoring, metrics, or log-parsing tooling and no operational scripts or automation to carry over.*

## Monitoring

- *Logs:* GridGain 8 ships `ignite-log4j2.xml` as the logging configuration. `IGNITE_QUIET` defaults to `false`, so output is more verbose, and `ignite.sh -q` restores quiet output. With the default logger, the log file is `work/log/ignite-<nodeId>.0.log`. Apache Ignite 2.18's separate `consistency.log` appender is gone, and sensitive values are hashed by default. Update log-parsing tooling.
- *Metrics:* `Ignite.metrics()`, `IgniteMetrics`, and the `MetricRegistry` API are available with the same signatures as in Ignite 2.18. Creating custom registries requires the `CUSTOM_METRICS_MANAGE` permission on a secured cluster.
- *Java Management Extensions (JMX):* the MBean names differ.
  - Ignite 2.18 uses metric-registry MBeans (`group=threadPools`, `group=cacheGroups`, `group=io,name=datastorage`, `group=io,name="dataregion.<name>"`, `group=sql`, `group=client,name=connector`, `group=communication`, `group=snapshot`). GridGain 8 uses the older naming (`group="Thread Pools"`, `group="Cache groups"`, `group=DataRegionMetrics`, `group="Persistent Store",name=DataStorageMetrics`, `group=SnapshotMetrics`).
  - The `group=management` MBeans that wrap `control.sh` commands in Ignite 2 are absent. The `Snapshot`, `Defragmentation`, `Metrics`, `SqlQuery`, `FailureHandling`, and `BaselineAutoAdjust` MBeans exist, with fewer operations. Use `control.sh` for the rest. `PerformanceStatistics` has no MBean.
  - GridGain 8 does not expose the metric registries over JMX by default (`NoopMetricExporterSpi`), while Ignite 2.18 defaults to `JmxMetricExporterSpi`. To get the Ignite 2 registry MBean names back, set `JmxMetricExporterSpi` in `IgniteConfiguration.metricExporterSpi`.
  - Update every JMX query, exporter pattern, and dashboard that addresses these MBeans by name, and compare the attributes on staging.
- *System views:* the `SYS` schema has the same views as Ignite 2.18, except `SNAPSHOT`, `PAGES_TIMESTAMP_HISTOGRAM`, and `STATISTICS_GLOBAL_DATA`. It adds `CACHE_LOCKS`, `CACHE_EXPLICIT_LOCKS`, `PLUGINS`, and `SERVICES_DISTRIBUTION`. Use JMX or `control.sh` instead of the missing views.
- *Events:* event codes 149, 150, 151, 170, and 171 mean different things in the two products, and several Ignite-only events (snapshot, consistency, SQL query execution) are unavailable. Update event listeners that filter by code.

## CLI Changes

The command-line tools are mostly compatible, but several commands and mechanisms differ. See [Control Script](../../../reference/cli-tool/README.md) for the full `control.sh` reference.

### control.sh

These `control.sh` commands, subcommands, and arguments changed:

| Category | Command or item | Change and what to do |
|---|---|---|
| Removed command | `--cdc` | Not supported. Use [Data Center Replication](../../data-center-replication/introduction.md) instead. |
| Removed command | `--consistency` | Use `--cache partition_reconciliation`. |
| Removed command | `--performance-statistics` | Not supported. Use JMX metrics or an external APM. |
| `--cache` subcommand | `create` | Removed. Define the cache in node configuration (XML), or create a table with SQL `CREATE TABLE` DDL. |
| `--cache` subcommand | `scan` | Removed. Use a SQL `SELECT`, or a [`ScanQuery`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/cache/query/ScanQuery.html) through the cache API. |
| `--cache` subcommand | `metrics` | Removed. Enable and read cache metrics over JMX (`CacheMetricsMXBean`) instead. |
| `--cache` subcommand | `schedule_indexes_rebuild` | Removed. |
| Argument | `--ssl-factory` | Not available. |
| Argument | `--enable-experimental` | Set the `IGNITE_ENABLE_EXPERIMENTAL_COMMAND` system property instead. |
| Changed command | `--snapshot` | An Ignite 2 compatibility layer over GridGain 8 snapshots: `create <name> [--incremental --dest --sync]`, `cancel (--id\|--name)`, `restore <name> [--increment --groups --src --sync]`, and `status`. `--snapshot check` is not available. For the native tool, use [`snapshot-utility.sh`](../../snapshots/snapshots-management-tool.md). |
| Changed command | `--rolling-upgrade` | Subcommands are `start`, `finish`, and `force`. |
| Changed command | `--deactivate --force` | Not available. |
| Changed command | `--kill snapshot`, `--kill consistency` | Not available. |
| Changed command | `--tracing-configuration`, `--wal` | Hidden unless `IGNITE_ENABLE_EXPERIMENTAL_COMMAND=true` is set. |
| Changed command | `--diagnostic` | Has no subcommands. |
| Confirmation | state-changing commands | They prompt for `y`; pipe `echo y \|` in scripts, as with Ignite 2. |
| Changed output | `--state` | Prints `Cluster is active`, `Cluster is inactive`, or `Cluster is active (read-only)` instead of Ignite 2's `Cluster state: ACTIVE` format. Update scripts that parse the output. |

### ignite.sh

Ignite 2 signals a successful restart by writing a file (`RESTART_SUCCESS_FILE`, set with `-DIGNITE_SUCCESS_FILE`); GridGain 8 signals it with process exit code `250`. Update custom restart wrappers to test for exit code `250` instead of the file. The JVM `--add-opens` set and the shipped Log4j2 configuration also differ.

### sqlline

* Pass custom JVM options in `SQL_JVM_OPTS`. Ignite 2 uses `JVM_OPTS`.
* The command-history file location changed. Ignite 2 sets `--historyFile` to `~/.sqlline/ignite_history`, and GridGain 8 leaves the `sqlline` default (`~/.sqlline/history`). If a different `sqlline` version wrote that file, `sqlline` prints `Bad history file syntax` at startup. The message is harmless, and removing the file silences it.

### ignite-cdc.sh

Not available. GridGain 8 has no CDC feature or tooling. For cross-cluster replication, use [Data Center Replication](../../data-center-replication/introduction.md); for other consumers, see the CDC entry in [Features to Replace](features-to-replace.md).
