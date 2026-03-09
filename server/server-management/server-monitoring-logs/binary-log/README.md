---
description: >-
  Understand the binary log in MariaDB Server. This section explains its role in
  replication and point-in-time recovery, detailing its format, management, and
  use for data integrity.
layout:
  width: default
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: false
  metadata:
    visible: true
  tags:
    visible: true
---

# Binary Log

The binary log (binlog) contains a record of all changes to the databases.

{% columns %}
{% column %}
{% content-ref url="overview-of-the-binary-log.md" %}
[overview-of-the-binary-log.md](overview-of-the-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Introduction to the purpose and structure of the binary log, explaining how it records data changes (DML[^1]) and structure changes (DDL[^2]) for replication and recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="activating-the-binary-log.md" %}
[activating-the-binary-log.md](activating-the-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Instructions for enabling the binary log using the `--log-bin` option and configuring the log file basename and index file.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-log-formats.md" %}
[binary-log-formats.md](binary-log-formats.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed comparison of the three binary logging formats: Statement-based (SBR), Row-based (RBR), and Mixed, including their pros, cons, and configuration via binlog\_format.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="using-and-maintaining-the-binary-log.md" %}
[using-and-maintaining-the-binary-log.md](using-and-maintaining-the-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete binary log maintenance: `PURGE BINARY LOGS`/`RESET MASTER`, `expire_logs_days` & `binlog_expire_logs_seconds`, `FLUSH BINARY LOGS`, and `SHOW SLAVE STATUS`.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../ha-and-performance/standard-replication/innodb-based-binary-log.md" %}
[innodb-based-binary-log.md](../../../ha-and-performance/standard-replication/innodb-based-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
MariaDB 12.3 introduces a new binary log implementation that stores binlog events directly in InnoDB-managed tablespaces instead of separate files on disk.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="compressing-events-to-reduce-size-of-the-binary-log.md" %}
[compressing-events-to-reduce-size-of-the-binary-log.md](compressing-events-to-reduce-size-of-the-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Guide to using the `log_bin_compress` system variable to compress binary log events, reducing storage usage and network bandwidth during replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="flashback.md" %}
[flashback.md](flashback.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explains how to use the Flashback feature (via `mysqlbinlog --flashback`) to rollback transactions by reversing the binary log events, useful for recovering from accidental data modifications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="group-commit-for-the-binary-log.md" %}
[group-commit-for-the-binary-log.md](group-commit-for-the-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Describes the group commit optimization, which improves performance by committing multiple transactions to the binary log in a single disk I/O operation.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="relay-log.md" %}
[relay-log.md](relay-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Overview of the relay log, a set of log files created by a replica server to store events received from the primary's binary log before executing them.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="../../../ha-and-performance/standard-replication/selectively-skipping-replication-of-binlog-events.md" %}
[selectively-skipping-replication-of-binlog-events.md](../../../ha-and-performance/standard-replication/selectively-skipping-replication-of-binlog-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn techniques to bypass specific replication events. This guide explains how to ignore individual transactions or errors to restore replication flow after a stoppage.
{% endcolumn %}
{% endcolumns %}

[^1]: DML (Data Manipulation Language): The subset of SQL commands used to add, modify, retrieve, or delete data within existing database tables.

[^2]: DDL (Data Definition Language): The subset of SQL commands used to create, modify, or destroy the structure of database objects (like tables, indexes, and databases) rather than the data itself.
