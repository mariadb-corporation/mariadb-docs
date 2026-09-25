---
description: >-
  Monitoring and command-line changes when migrating from Apache Ignite 2 to
  GridGain 8, covering logs, metrics, system views, events, and the CLI tools.
---

# Monitoring and CLI Changes

This section covers changes to the monitoring stack (logs, metrics, system views, events) and to the command-line tools (`control.sh`, `ignite.sh`, `sqlline`, `ignite-cdc.sh`).

You can skip it if you have no monitoring, metrics, or log-parsing tooling and no operational scripts or automation to carry over.

## Monitoring

- *Logs:* the shipped Log4j config format differs, `IGNITE_QUIET` defaults to `false` (more verbose), and the log file-name pattern changed. Update log-parsing tooling.
- *Metrics:* `Ignite.metrics()` and the new `MetricRegistry` API are unavailable. Use JMX or `ReadOnlyMetricRegistry`.
- *System views:* several Ignite-only views (node attributes/metrics, baseline, SQL plan history, snapshot) are unavailable. Query the `SYS` schema or use JMX.
- *Events:* event code 149 means different things in the two products, and several Ignite-only events (snapshot, consistency, SQL query execution) are unavailable. Update event listeners that filter by code.

## CLI Changes

The command-line tools are mostly compatible, but several commands and mechanisms differ. See [Control Script](../../../reference/cli-tool/README.md) for the full `control.sh` reference.

### control.sh

These `control.sh` commands, subcommands, and arguments changed:

| Category | Command or item | Change and what to do |
|---|---|---|
| Removed command | `--cdc` | Not supported. Use [Data Center Replication](../../data-center-replication/introduction.md) instead. |
|  | `--consistency` | Use `--cache partition_reconciliation`. |
|  | `--system-view` | Use the `SYS` schema or JMX. |
|  | `--performance-statistics` | Not supported. Use JMX metrics or an external APM. |
| `--cache` subcommand | `create` | Removed. Define the cache in node configuration (XML), or create a table with SQL `CREATE TABLE` DDL. |
|  | `scan` | Removed. Use a SQL `SELECT`, or a [`ScanQuery`](https://www.gridgain.com/sdk/gridgain8/latest/javadoc/org/apache/ignite/cache/query/ScanQuery.html) through the cache API. |
|  | `metrics` | Removed. Enable and read cache metrics over JMX (`CacheMetricsMXBean`) instead. |
|  | `idle_verify_dump` | Renamed. Call `idle_verify --dump` instead. |
| Argument | `--ssl-factory` | Not available. |
|  | `--enable-experimental` | Set the `IGNITE_ENABLE_EXPERIMENTAL_COMMAND` system property instead. |
| Changed command | `--snapshot` | An Apache Ignite 2 compatibility layer over GridGain snapshots, supporting the `create`, `cancel`, `restore`, and `status` actions. For the native tool, use [`snapshot-utility.sh`](../../snapshots/snapshots-management-tool.md). |
| Changed output | `--state` | Prints `Cluster is active`, `Cluster is inactive`, or `Cluster is active (read-only)` instead of Ignite's `Cluster state: ACTIVE` format. Update scripts that parse the output. |

### ignite.sh

Apache Ignite signals a successful restart by writing a file (`RESTART_SUCCESS_FILE`, set with `-DIGNITE_SUCCESS_FILE`); GridGain signals it with process exit code `250`. Update custom restart wrappers to test for exit code `250` instead of the file. The JVM `--add-opens` set and the shipped Log4j2 configuration also differ.

### sqlline

* Pass custom JVM options in `SQL_JVM_OPTS`. Apache Ignite uses `JVM_OPTS`.
* The command-history file location changed: Apache Ignite sets `--historyFile` to `~/.sqlline/ignite_history`; GridGain leaves the `sqlline` default.

### ignite-cdc.sh

Not available. GridGain has no CDC at all. For cross-cluster replication, use [Data Center Replication](../../data-center-replication/introduction.md); for other consumers, see the CDC entry in [Features to Replace](features-to-replace.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
