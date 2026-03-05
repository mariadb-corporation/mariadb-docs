---
description: >-
  Overview of the metrics collected by Enterprise Manager, including MariaDB
  Server counters, MaxScale performance data, and node-level system resource
  utilization.
---

# Metrics

## MariaDB Server Metrics

MariaDB Server metrics are gathered with the Prometheus exporter for MySQL and stored in Enterprise Manager’s Prometheus with the `mariadb` prefix. The agent runs the exporter with the following collector flags:

| Collector name                           | Description                                                                                                                             |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| collect.binlog\_size                     | Reports binary log files and their sizes to track binlog count and total disk usage/growth.                                             |
| collect.engine\_innodb\_status           | Parses `SHOW ENGINE INNODB STATUS` to expose InnoDB internals (waits, deadlocks, transaction and I/O snapshots).                        |
| collect.info\_schema.innodb\_metrics     | Reads `INFORMATION_SCHEMA.INNODB_METRICS` for detailed InnoDB counters (buffer pool, I/O, log, lock, purge, recovery, etc.).            |
| collect.info\_schema.innodb\_tablespaces | Exposes per-tablespace/file size and allocation details from Information Schema for space-usage monitoring.                             |
| collect.info\_schema.processlist         | Exposes current session/thread activity (users, hosts, commands, states, runtimes) based on the process list.                           |
| collect.info\_schema.replica\_host       | Discovers replica hosts via Information Schema (MariaDB-friendly alternative to `SHOW SLAVE HOSTS`) for topology visibility.            |
| collect.slave\_hosts                     | Emits replica host topology using `SHOW SLAVE HOSTS`/`SHOW REPLICA HOSTS` (note: MariaDB expects the legacy `SHOW SLAVE HOSTS` syntax). |
| collect.slave\_status                    | Exposes replication status from `SHOW SLAVE/REPLICA STATUS` (I/O/SQL thread states, positions/GTID, seconds behind, etc.).              |

## MaxScale Metrics

MariaDB Enterprise Manager collects a wide range of time-series metrics from your MariaDB MaxScale instances to provide deep insight into their performance, health, and activity. Monitoring these metrics is crucial for diagnosing performance bottlenecks, ensuring high availability, and understanding how your database proxy is handling application traffic.

Here is the list of available [MaxScale metrics](../../../../mariadb-enterprise-operator/metrics.md#maxscale-metrics) collected by Enterprise Manager.

## Node Metrics

Node metrics provide crucial information about the health and performance of the underlying hardware and operating system on each monitored host. These metrics are essential for diagnosing infrastructure bottlenecks, understanding resource utilization, and planning for future capacity.

MariaDB Enterprise Manager gathers these metrics using **Prometheus Node Exporter**, which includes a default set of collectors.

Key metrics collected by default include:

* **CPU Usage**: Overall and per-core utilization, load average, and context switching.
* **Memory**: Total, used, free, and cached memory, including swap space.
* **Disk I/O**: Read/write operations, throughput (bytes per second), and I/O time.
* **Filesystem Usage**: Total, used, and available space for each mounted filesystem.
* **Network Traffic**: Data sent and received, packets, and network interface errors.

For a complete and detailed list of all metrics gathered by the default collectors, please refer to the official [Prometheus Node Exporter documentation](https://prometheus.io/docs/guides/node-exporter/).

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
