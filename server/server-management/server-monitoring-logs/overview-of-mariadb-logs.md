---
description: >-
  An introductory guide to the various logs available in MariaDB, including the
  Error Log, General Query Log, Slow Query Log, and Binary Log, and how to
  enable or disable them.
---

# Overview of MariaDB Logs

There are many variables in MariaDB that you can use to define what to log and when to log.

This page will give you an overview of the different logs and how to enable/disable logging to these.

{% hint style="info" %}
Storage engines and plugins can have their logs too. For example, InnoDB keeps an [Undo Log](../../server-usage/storage-engines/innodb/innodb-undo-log.md) and a Redo Log which are used for rollback and crash recovery. However, this page only lists MariaDB server logs.
{% endhint %}

## Standardized Log Naming

Use the [--log-basename](../starting-and-stopping-mariadb/mariadbd-options.md#log-basename) startup setting to establish a common base name for all log files. This option configures the base name for the _Error Log_, _General Query Log_, _Slow Query Log_, and _Binary Log_ simultaneously. Using a standardized base name ensures consistency across different logs and simplifies management in multi-instance or clustered environments.

### [Error Log](error-log.md)

* Always enabled by default.
* Records all critical errors encountered by the server.
  * Useful for diagnosing startup failures, crashes, and internal server errors.
* Can be configured to record varying levels of warnings and notes.

### [General Query Log](general-query-log.md)

* Records a record of when clients connect or disconnect, and every SQL statement received from clients.
* Useful for debugging queries and monitoring client activity.
* For security and compliance auditing, use the [MariaDB Audit Plugin](../../reference/plugins/mariadb-audit-plugin/mariadb-audit-plugin-overview.md) or [MariaDB Enterprise Audit](../../reference/plugins/mariadb-enterprise-audit.md) instead.

### [Slow Query Log](slow-query-log/)

* Records all SQL queries that take more than a defined threshold of time to execute.
* Useful for identifying performance bottlenecks and queries that require optimization.
* Can be filtered or sampled to reduce log volume on high-traffic servers.

### [Binary Log](binary-log/overview-of-the-binary-log.md)

* Records all statements that change data (DML and DDL) in a binary format.
* Essential for replication topologies where the server acts as a primary.
* Required for point-in-time recovery and database restoration.

### Parsing Reference for Tool Developers

To support the development of log parsers (e.g., Fluentd, Logstash, Splunk), the following tables standardize identification fields and structural characteristics across all MariaDB Server logs.

#### Cross-Log Field Standardization

The following data points are represented differently across various logs but refer to the same internal identifiers.

| Standardized Name | General/Slow Log Field | Audit Log Field     | Error Log Field       | Binary Log (Text) |
| ----------------- | ---------------------- | ------------------- | --------------------- | ----------------- |
| Thread ID         | `thread_id`            | `connectionid`      | `Thread ID`           | `at {ID}`         |
| Server ID         | `server_id`            | N/A (Uses Hostname) | N/A (Uses Process ID) | `server id`       |

#### Structural Characteristics for Parsers

| Log Type          | Primary Format    | Record Start Indicator   | Multi-line Support       |
| ----------------- | ----------------- | ------------------------ | ------------------------ |
| Error Log         | Positional String | Timestamp (`YYYY-MM-DD`) | No (Except Stack Traces) |
| General Query Log | Positional String | Timestamp                | Yes (SQL Payloads)       |
| Slow Query Log    | Tagged Header     | `# User@Host:`           | Yes (Always)             |
| Binary Log (Text) | Tagged Header     | `# at {Position}`        | Yes (Event Chunks)       |
| Enterprise Audit  | CSV               | N/A (Standard Line)      | No                       |

**Parser Developer Checklist**

* Handle Multi-line Records: Assume that General and Slow Query logs will contain newlines within SQL statements.
* Standardize Identifiers: Always map `connectionid` and `thread_id` to a single `thread_id` field in your monitoring backend to allow cross-log correlation.
* Identify Record Starts: For Slow Query logs, use `# User@Host:` as the only reliable indicator of a new record.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
