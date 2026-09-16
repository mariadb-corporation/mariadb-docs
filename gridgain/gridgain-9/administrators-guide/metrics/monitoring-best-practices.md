---
description: >-
  Best practices for monitoring a production GridGain 9 cluster: which metrics
  to watch, the alerts to configure, and how to diagnose problems.
---

# Monitoring Best Practices

This guide describes best practices for monitoring a running GridGain 9 cluster in production. It describes what to watch, what healthy looks like, what to alert on, and how to diagnose problems.

## Monitoring Architecture

GridGain 9 exposes cluster state through four complementary channels. Each answers a different question, and a complete strategy uses all four.

| Channel | Answers | Best consumed by |
| --- | --- | --- |
| Metrics | What are the numbers over time? Rates, saturation, and latencies. | Prometheus and Grafana, an OpenTelemetry backend, JMX, Zabbix. |
| System views | What is happening right now? Live transactions, locks, queries, and partition health. | JDBC, thin clients. |
| Events | What happened, and who did it? The audit and lifecycle trail. | An alerting system, through a webhook or log sink. |
| CLI, REST, and logs | Is the cluster up and joined? What do health probes report? | Kubernetes probes, scripts, and log aggregation. |

Keep these facts in mind when you plan collection:

* **Metric collection is per node, but exporter configuration is cluster-wide.** When you configure an exporter, every node applies it. Each node still reports its own values.
* **Prometheus is supported through an exporter.** Nodes do not serve a Prometheus endpoint for Prometheus to scrape directly. Instead, you connect the two with the OpenTelemetry (OTLP) exporter or with JMX.
* **There is no system view for node topology.** Use the CLI `cluster topology` command and the `topology.cluster` and `topology.local` metrics instead.

## Key Metrics to Watch

Most of the time you need to watch a small subset of available metrics. The tables below group that set into six signal groups, ordered by priority. The first two groups are specific to a distributed database. The last four follow the standard latency, traffic, errors, and saturation model.

For the full description of each metric, see [Available Metrics](metrics-list.md).

### Availability and Quorum

These metrics tell you whether the cluster can handle data. Watch them first.

| Metric | Meaning | Watch for |
| --- | --- | --- |
| `metastorage.MajorityAvailable` | `1` when the Meta Storage majority is present. | `0` means the cluster cannot commit metadata. |
| `metastorage.AvailablePeers` | Reachable Meta Storage peers. | A value below the expected peer count. |
| `metastorage.SafeTimeLag` | Meta Storage safe-time lag. | Sustained growth, which means metadata propagation is stalling. |
| `topology.cluster.TotalNodes` | Nodes in the logical topology. | Any drop from the expected cluster size. |
| `schema.sync.Waits` | Waits for schema synchronization. | High or rising values, which can indicate Meta Storage problems. |

### Data Safety

These metrics tell you whether the cluster can lose or refuse data. Partition health is the most important signal here. You can read it as a metric or from a system view. See [Checking Partition Health](#checking-partition-health).

| Signal | Meaning | Watch for |
| --- | --- | --- |
| Global partition state `UNAVAILABLE` | A partition has no healthy replica. | Any occurrence. Data is offline. |
| Global partition state `DEGRADED` or `READ_ONLY` | `DEGRADED` means healthy replicas form a majority but redundancy is reduced. `READ_ONLY` means healthy replicas do not form a majority, so the partition cannot accept writes. | Any occurrence. Fault tolerance is reduced. |
| Local partition state `BROKEN` | The partition state machine on a node threw an exception. The partition needs manual recovery. | Any occurrence. |
| Local partition state `CATCHING_UP` | A replica on a node has not replicated its part of the Raft log yet. | A state that persists, which means a replica is not keeping up. |
| `zones.<zone>.TotalUnrebalancedPartitionsCount` | Partitions waiting to rebalance. | A non-zero value that does not decrease. |
| `dcr.replications.<name>.<table>.ReplicationLag` | Data center replication lag. | Sustained or growing lag. |

### Saturation

These metrics tell you how much resource headroom each node has.

| Metric | Meaning | Watch for |
| --- | --- | --- |
| `jvm.memory.heap.FreePercent` | Free heap headroom. | Low values, which risk garbage collection pressure and out-of-memory errors. |
| `jvm.gc.CollectionTimePercent` | Time spent in garbage collection. | High values, which mean stop-the-world pauses. |
| `os.CpuLoad` and `os.LoadAverage` | Host CPU pressure. | Sustained high values compared to `os.AvailableProcessors`. |
| `thread.pools.<name>.QueueSize` | Executor queue depth. | Sustained saturated pools, especially partition and query pools. |
| `storage.aipersist.checkpoint.SpeedBasedThrottlingPercentage` | Write throttling caused by checkpointing. | Frequent or rising throttling, which means write pressure. |
| `storage.aipersist.<region>.PageReplacements` | Page cache evictions. | Sustained high values, which mean the data region is too small. |

### Latency

These metrics tell you how long operations take. Watch for high percentiles rather than averages, and compare them against your own baseline.

| Metric | Meaning | Watch for |
| --- | --- | --- |
| `transactions.RwDuration` and `transactions.RoDuration` | Transaction duration distributions. | High percentiles, which point to contention or a slow path. |
| `storage.aipersist.checkpoint.LastCheckpointDuration` | Time to complete a checkpoint. | A growth trend, which points to storage pressure. |

### Errors

These metrics tell you how often operations fail. A low failure rate is normal under load, so alert on a rise against your baseline rather than on any single failure.

| Metric | Meaning | Watch for |
| --- | --- | --- |
| `sql.queries.Failed`, `sql.queries.TimedOut`, `sql.queries.ExceededMemoryQuota` | SQL failures. | An increase over the baseline rate. |
| `transactions.RwRollbacks` and `transactions.RoRollbacks` | Rolled-back transactions. | A rise in the rollback ratio against commits. |
| `client.handler.RequestsFailed` and `client.handler.SessionsRejected` | Client-facing failures. | An increase over the baseline rate. |
| `messaging.messageHandlingFailures` and `messaging.invokeTimeouts` | Inter-node messaging failures. | Rising values, which mean node-to-node communication is degraded. |

### Traffic

These metrics describe normal load. Use them for capacity planning and to set baselines for the error and latency alerts.

| Metric | Meaning | Watch for |
| --- | --- | --- |
| `transactions.TotalCommits` | Transaction throughput. | A sudden drop, which can point to an upstream stall. |
| `client.handler.RequestsProcessed` and `client.handler.SessionsActive` | Client load. | Trends against your baseline. |
| `storage.aipersist.StorageSize` and `log.storage.TotalLogStorageSize` | Disk footprint. | Growth against available disk capacity. |
| `license.DaysToLicenseExpiration` | Days until the license expires. | A shrinking value, so you can plan renewal. |

## Recommended Alerts

The alerts below use three severities. Treat the thresholds as starting points and tune them to your workload.

* **P1** — page an operator immediately.
* **P2** — open a ticket and investigate.
* **P3** — track for trends and capacity planning.

Not every alert comes from a metric. License and authentication alerts come from events. The readiness alert comes from a REST probe. The failure-handler and blocked-worker alerts come from logs. See [Monitoring Events](#monitoring-events), [Health Checks and Probes](#health-checks-and-probes), and [Monitoring Logs](#monitoring-logs).

### P1 Alerts

| Alert | Condition | Action |
| --- | --- | --- |
| Meta Storage quorum lost | `metastorage.MajorityAvailable == 0` | Restore Meta Storage nodes. The cluster cannot commit metadata. |
| Partition unavailable | A partition reports the global `UNAVAILABLE` state. | Investigate node loss. You may need to reset partitions. |
| Partition broken | A replica reports the local `BROKEN` state. | Perform manual recovery. |
| Node down | `topology.cluster.TotalNodes` is below the expected count for more than one to two minutes. | Find and restart the missing node. |
| Readiness failing | `GET /health/readiness` is not `UP` for several minutes. | The node has not joined the logical topology. Investigate the join. |
| License lockout | A `LICENSE_EXPIRED`, `LICENSE_VIOLATED`, or `LICENSE_NODE_REJECTED` event, or `license.DaysToLicenseExpiration` at or below zero. | Apply a valid license. |
| Failure handler fired | A failure-handler entry appears in the node log. | The node may be compromised. Investigate the root cause. |
| Heap critical | `jvm.memory.heap.FreePercent < 10` | An out-of-memory error is imminent. Investigate load and heap sizing. |
| Garbage collection critical | `jvm.gc.CollectionTimePercent > 25` | The node is effectively stalled by garbage collection. |

### P2 Alerts

| Alert | Condition |
| --- | --- |
| Heap pressure | `jvm.memory.heap.FreePercent < 20` |
| Garbage collection pressure | `jvm.gc.CollectionTimePercent > 10` |
| Redundancy degraded | A partition reports the global `DEGRADED` or `READ_ONLY` state. |
| Stuck rebalance | `TotalUnrebalancedPartitionsCount > 0` and flat for more than 15 minutes. |
| Write throttling | `SpeedBasedThrottlingPercentage` is high, or checkpoint throttling time is rising. |
| SQL error or timeout spike | The rate of `sql.queries.Failed` plus `sql.queries.TimedOut` is above the baseline. |
| Rollback spike | The ratio of `RwRollbacks` to total transactions is above the baseline. |
| Transaction latency | A high percentile of `RwDuration` or `RoDuration`. |
| Client failures | The rate of `client.handler.RequestsFailed` or rejected sessions is rising. |
| Blocked worker | A blocked critical-worker entry appears in the node log. |
| Messaging degraded | `messaging.invokeTimeouts` or slow-response counts are rising. |
| Replication lag | `dcr.replications.<name>.<table>.ReplicationLag` is sustained or growing. |
| Authentication attack | A burst of `USER_AUTHENTICATION_FAILURE` or `USER_AUTHORIZATION_FAILURE` events. |
| License expiring | `license.DaysToLicenseExpiration < 30` |
| CPU saturation | `os.CpuLoad` is sustained high compared to `os.AvailableProcessors`. |

### P3 Alerts

Track these signals for capacity planning:

* Disk growth: `storage.aipersist.StorageSize` and `log.storage.TotalLogStorageSize` against disk capacity.
* Checkpoint duration trend.
* Page cache evictions: `storage.aipersist.<region>.PageReplacements`.
* Cache effectiveness: SQL plan cache hit ratio and cache hit percentage.
* Throughput baselines: `transactions.TotalCommits` and `client.handler.RequestsProcessed`.

## Diagnostics

When an alert fires, use these steps to find the cause.

### Checking Cluster Health

Run these CLI checks in order to confirm the cluster is up and fully joined:

1. Check the overall cluster state. Look at `initialized`, `nodeCount`, and the Meta Storage node list.

   ```bash
   cluster status
   ```
2. Check that each node reports the `STARTED` state.

   ```bash
   node status
   ```
3. Compare the logical and physical topologies. A node that is physically present but missing from the logical topology has not fully joined.

   ```bash
   cluster topology logical
   cluster topology physical
   ```
4. Check partition health. See [Checking Partition Health](#checking-partition-health).

### Checking Partition Health

Partition health is the primary data-safety signal. You can read it from a system view, from the CLI, or as metrics.

The `SYSTEM.GLOBAL_ZONE_PARTITION_STATES` view reports cluster-wide partition health. List every partition that is not fully available:

```sql
SELECT * FROM system.global_zone_partition_states
WHERE partition_state <> 'AVAILABLE';
```

The `SYSTEM.LOCAL_ZONE_PARTITION_STATES` view reports per-node partition health. List partitions in trouble on any node:

```sql
SELECT * FROM system.local_zone_partition_states
WHERE partition_state IN ('BROKEN', 'UNAVAILABLE', 'CATCHING_UP');
```

You can also read partition health from the `recovery partitions states` CLI command:

```bash
recovery partitions states --global
```

{% hint style="info" %}
Each table also exposes its partition health as metrics, under the `partition.states.zone.<zoneId>.table.<tableId>` metric source. Use these metrics to alert on partition health from your metrics backend instead of polling the system view.
{% endhint %}

For the full list of partition states and recovery actions, see [Disaster Recovery](../disaster-recovery.md).

### Finding Long-Running Transactions

The `SYSTEM.TRANSACTIONS` view lists active transactions. Order by start time to find the oldest:

```sql
SELECT * FROM system.transactions
ORDER BY transaction_start_time ASC;
```

### Diagnosing Blocked Transactions

The `SYSTEM.LOCKS` view lists active locks. Join it to `SYSTEM.TRANSACTIONS` to find which transaction holds an exclusive lock:

```sql
SELECT t.coordinator_node_id, t.transaction_state, l.object_id, l.lock_mode
FROM system.locks l
JOIN system.transactions t ON l.transaction_id = t.transaction_id
WHERE l.lock_mode IN ('X', 'IX', 'SIX');
```

### Finding Runaway Queries

The `SYSTEM.SQL_QUERIES` view lists in-flight SQL. Order by start time to find long-running queries, then cancel one if needed:

```sql
SELECT * FROM system.sql_queries
ORDER BY query_start_time ASC;
```

### Detecting Data Skew

The `SYSTEM.LOCAL_ZONE_PARTITION_STATES` view reports estimated rows per partition. Order by that column to find uneven data distribution:

```sql
SELECT zone_name, partition_id, estimated_rows
FROM system.local_zone_partition_states
ORDER BY estimated_rows DESC;
```

## Health Checks and Probes

GridGain 9 serves health endpoints on the REST port, `10300` by default. Use them for liveness and readiness checks, and in scripts.

| Endpoint | Meaning | Use as |
| --- | --- | --- |
| `GET /health/liveness` | `UP` while the process and REST server are running. | A liveness probe. |
| `GET /health/readiness` | `UP` only after the node joins the logical topology. | A readiness probe. |
| `GET /health` | An aggregate check. Returns an error before the cluster is initialized. | A supplementary check. |
| `GET /management/v1/cluster/state` | Returns `409 Conflict` with the `Cluster is not initialized` title until the cluster is initialized. | An initialization check. |
| `GET /management/v1/node/state` | Returns the node name and state. | A scriptable node check. |

On Kubernetes, the operator wires the liveness and readiness endpoints as pod probes. See [Monitoring with the Kubernetes Operator](../../extensions/k8s-operator/monitoring.md).

## Monitoring Events

Events record what happened in the cluster and who caused it. They are the basis for audit and security alerting. You route events to a log file or to a webhook by configuring a channel and a sink.

For the full setup, see [Working with Events](../../developers-guide/events/overview.md). For the event catalog, see [Available Events](../../developers-guide/events/events-list.md).

### Alert-Worthy Events

Route these events to your alerting system:

| Event | Severity | Action |
| --- | --- | --- |
| `USER_AUTHENTICATION_FAILURE` | P2 | Alert on bursts, which can indicate a brute-force attempt. |
| `USER_AUTHORIZATION_FAILURE` | P2 | Alert on bursts, which can indicate privilege probing. |
| `COMPUTE_JOB_FAILED`, `COMPUTE_TASK_FAILED` | P2 | Alert on a rising failure rate. |

## Monitoring Logs

GridGain 9 server nodes log through `java.util.logging`. The configuration file is `etc/gridgain.java.util.logging.properties`. By default, each node writes a rotating log file, and the LogPush metric exporter writes a separate metrics log file.

Alert on these log signals:

* **Failure handler fired.** The node hit a critical failure, such as an out-of-memory error. Treat as P1.
* **Blocked critical worker.** A worker exceeded its allowed liveness lag. The node may be stalled. Treat as P2.
* **Topology change.** A node left or was suspected. Watch for unexpected membership churn.
* **Checkpoint duration.** Growing checkpoint times point to storage pressure.
* **Raft quorum.** Leader-election or quorum-loss messages map to broken or unavailable partitions.

## See Also

* [Configuring Metrics](configuring-metrics.md) — how to enable metric sources and set up exporters.
* [System Views](system-views.md) — the full catalog of views used in [Diagnostics](#diagnostics).
