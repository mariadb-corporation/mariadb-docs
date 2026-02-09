---
description: >-
  This guide indicates where the various system and status variables of MariaDB
  Server are found.
---

# System & Status Variables Guide

System variables and status variables serve two distinct roles in MariaDB: System variables are the "knobs" you turn to change how the server behaves, while status variables are the "gauges" you watch to see how the server is performing.

Because MariaDB is modular, these variables are often grouped by their specific functional area or plugin.

***

## What you do with System Variables

**System variables are configuration settings.** You use them to define the environment, set resource limits, and tune performance.

* **Configuration & Tuning:** You modify these to optimize the server for your workload. For example, you might increase `innodb_buffer_pool_size` to allow the database to cache more data in memory, reducing disk I/O.
* **Controlling Behavior:** You use them to toggle features on or off. Setting `read_only` to `1` ensures no data can be modified (useful for maintenance or replicas).
* **Enforcing Constraints:** You set limits to prevent resource exhaustion. For example, `max_connections` prevents the server from being overwhelmed by too many simultaneous users.
* **Session Personalization:** Many variables can be set at the Session level. This means you can change how the server behaves just for your current connection – like changing the `sql_mode` to be more or less strict – without affecting other users.

## What you use Status Variables for

**Status variables are read-only counters and metrics.** You use them to monitor the health and activity of the server.

* **Performance Monitoring:** You check status variables to see if your system tuning is working. If you see high numbers for `Select_full_join`, it tells you that your queries are missing indexes.
* **Health Checks:** You use them to identify bottlenecks. If `Aborted_connects` is high, you might have network issues or a client with the wrong password attempting to connect repeatedly.
* **Resource Tracking:** They tell you how much of your allocated resources are actually being used. Comparing `Max_used_connections` against your system variable `max_connections` helps you decide if you need to scale up.
* **Capacity Planning:** By monitoring variables like `Bytes_sent` and `Bytes_received` over time, you can forecast when you will need to upgrade your hardware or network bandwidth.

## Comparison at a Glance

| **Feature**   | **System Variables**                  | **Status Variables**       |
| ------------- | ------------------------------------- | -------------------------- |
| Analogy       | Steering wheel / Gas pedal            | Speedometer / Fuel gauge   |
| Action        | Set (change the value)                | View (read the value)      |
| Purpose       | Control and configuration             | Monitoring and diagnostics |
| SQL Statement | `SET GLOBAL ...` or `SET SESSION ...` | `SHOW STATUS ...`          |

## Pages Documenting Variables

Here is the comprehensive list of pages that document variables.

### Core Server Variables

* Server System Variables (The main list for general server configuration)
  * [https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables](https://mariadb.com/docs/server/server-management/variables-and-modes/server-system-variables)
* Server Status Variables (Real-time monitoring metrics)
  * [https://mariadb.com/docs/server/server-management/variables-and-modes/server-status-variables](https://mariadb.com/docs/server/server-management/variables-and-modes/server-status-variables)
* Performance Schema System Variables
  * [https://mariadb.com/docs/server/reference/system-tables/performance-schema/performance-schema-system-variables](https://mariadb.com/docs/server/reference/system-tables/performance-schema/performance-schema-system-variables)

### Storage Engine Specific Variables

* Aria System Variables
  * [https://mariadb.com/docs/server/server-usage/storage-engines/aria/aria-system-variables](https://mariadb.com/docs/server/server-usage/storage-engines/aria/aria-system-variables)
* InnoDB System Variables
  * [https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables](https://mariadb.com/docs/server/server-usage/storage-engines/innodb/innodb-system-variables)
* MyISAM System Variables
  * [https://mariadb.com/docs/server/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables](https://mariadb.com/docs/server/server-usage/storage-engines/myisam-storage-engine/myisam-system-variables)
* CONNECT System Variables
  * [https://mariadb.com/docs/server/server-usage/storage-engines/connect/connect-system-variables](https://mariadb.com/docs/server/server-usage/storage-engines/connect/connect-system-variables)
* Spider System Variables
  * [https://mariadb.com/docs/server/server-usage/storage-engines/spider/spider-system-variables](https://mariadb.com/docs/server/server-usage/storage-engines/spider/spider-system-variables)

### Replication & Performance Variables

* Replication and Binary Log System Variables
  * [https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-and-binary-log-system-variables](https://mariadb.com/docs/server/ha-and-performance/standard-replication/replication-and-binary-log-system-variables)
* Thread Pool System and Status Variables
  * [https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables](https://mariadb.com/docs/server/ha-and-performance/optimization-and-tuning/buffers-caches-and-threads/thread-pool/thread-pool-system-status-variables)

### Plugin Specific Variables

* Audit Plugin Options and System Variables
  * [https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables](https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-options-and-system-variables)
* Audit Plugin Status Variables
  * [https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-status-variables](https://mariadb.com/docs/server/reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-status-variables)
* Encryption Plugin System Variables (for instance, File Key Management)
  * [https://mariadb.com/docs/server/reference/plugins/encryption-plugins/file-key-management-plugin-system-variables](https://www.google.com/search?q=https://mariadb.com/docs/server/reference/plugins/encryption-plugins/file-key-management-plugin-system-variables\&authuser=1)

### Index / Master List

* Full list of MariaDB options, system and status variables
  * [https://mariadb.com/docs/server/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables](https://mariadb.com/docs/server/server-management/variables-and-modes/full-list-of-mariadb-options-system-and-status-variables)
  * _Note: This page acts as a directory that links back to the detailed pages above._
