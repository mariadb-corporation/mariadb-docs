---
description: >-
  Discover InnoDB, the default storage engine for MariaDB Server. Learn about
  its transaction-safe capabilities, foreign key support, and high performance
  for demanding workloads.
---

# InnoDB

{% columns %}
{% column %}
{% content-ref url="innodb-storage-engine-introduction.md" %}
[innodb-storage-engine-introduction.md](innodb-storage-engine-introduction.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
An overview of the InnoDB storage engine, detailing its support for ACID transactions, row-level locking, and crash recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-file-format.md" %}
[innodb-file-format.md](innodb-file-format.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the different file formats supported by InnoDB, such as Antelope and Barracuda, and how they impact table features and storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-limitations.md" %}
[innodb-limitations.md](innodb-limitations.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
A list of constraints and limits within the InnoDB engine, including maximum table size, column counts, and index key lengths.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="auto_increment-handling-in-innodb.md" %}
[auto_increment-handling-in-innodb.md](auto_increment-handling-in-innodb.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page explains how InnoDB manages AUTO_INCREMENT columns, including initialization behavior, gap handling, and potential restart effects.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binary-log-group-commit-and-innodb-flushing-performance.md" %}
[binary-log-group-commit-and-innodb-flushing-performance.md](binary-log-group-commit-and-innodb-flushing-performance.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how group commit works with InnoDB to improve performance by reducing the number of disk syncs required during transaction commits.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-asynchronous-io.md" %}
[innodb-asynchronous-io.md](innodb-asynchronous-io.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore how InnoDB uses asynchronous I/O on various operating systems to handle multiple read and write requests concurrently without blocking.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-buffer-pool.md" %}
[innodb-buffer-pool.md](innodb-buffer-pool.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete InnoDB Buffer Pool guide for MariaDB. Complete reference documentation for implementation, configuration, and usage with comprehensive examples and.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-change-buffering.md" %}
[innodb-change-buffering.md](innodb-change-buffering.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the change buffer, an optimization that delays secondary index writes to reduce I/O overhead for non-unique index modifications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-data-scrubbing.md" %}
[innodb-data-scrubbing.md](innodb-data-scrubbing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This feature allows for the secure deletion of data by overwriting deleted records in tablespaces and logs to prevent data recovery.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-doublewrite-buffer.md" %}
[innodb-doublewrite-buffer.md](innodb-doublewrite-buffer.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The doublewrite buffer is a storage area where InnoDB writes pages before writing them to the data file, preventing data corruption from partial page writes.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-flush-method.md" %}
[innodb-flush-method.md](innodb-flush-method.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Detailed description of the innodb_flush_method variable, its various settings, and effects.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-lock-modes.md" %}
[innodb-lock-modes.md](innodb-lock-modes.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
InnoDB employs Row-Level Locking with Shared (S) and Exclusive (X) locks, along with Intention locks, to manage concurrent transaction access.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-log-archiving.md" %}
[innodb-log-archiving.md](innodb-log-archiving.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Retain the full InnoDB write-ahead log history (from MariaDB 13.0) by archiving log files, enabling point-in-time recovery and incremental backups.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-monitors.md" %}
[innodb-monitors.md](innodb-monitors.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
InnoDB Monitors, such as the Standard, Lock, and Tablespace monitors, provide detailed internal state information to the error log for diagnostics.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-page-compression.md" %}
[innodb-page-compression.md](innodb-page-compression.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This feature enables transparent page-level compression for tables using algorithms like LZ4 or Zlib, reducing storage requirements.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-page-flushing.md" %}
[innodb-page-flushing.md](innodb-page-flushing.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about the background processes that flush dirty pages from the buffer pool to disk, including adaptive flushing algorithms to optimize I/O.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-purge.md" %}
[innodb-purge.md](innodb-purge.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The purge process is a garbage collection mechanism that removes old row versions from the undo log that are no longer required for MVCC.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-undo-log.md" %}
[innodb-undo-log.md](innodb-undo-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The undo log stores the "before" image of data modified by active transactions, supporting rollbacks and consistent read views.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-redo-log.md" %}
[innodb-redo-log.md](innodb-redo-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
The redo log is a disk-based transaction log used during crash recovery to replay incomplete transactions and ensure data durability.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-strict-mode.md" %}
[innodb-strict-mode.md](innodb-strict-mode.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
InnoDB Strict Mode enforces stricter SQL compliance, returning errors instead of warnings for invalid CREATE TABLE options or potential data loss.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-system-variables.md" %}
[innodb-system-variables.md](innodb-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to InnoDB system variables for MariaDB. Complete reference for buffer pool, I/O tuning, transaction settings, and optimization for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-versions.md" %}
[innodb-versions.md](innodb-versions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page is outdated. It's left in place because release notes for old MariaDB versions refer to it (MariaDB < 10.3).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-architecture-for-mariadb-enterprise-server/" %}
[innodb-architecture-for-mariadb-enterprise-server](innodb-architecture-for-mariadb-enterprise-server/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand InnoDB's architecture for MariaDB Enterprise Server. This section details its components and their interactions, focusing on performance, scalability, and reliability for enterprise workloa
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-online-ddl/" %}
[innodb-online-ddl](innodb-online-ddl/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform online DDL operations with InnoDB in MariaDB Server. Learn how to alter tables without blocking read/write access, ensuring high availability for your applications.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-row-formats/" %}
[innodb-row-formats](innodb-row-formats/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore InnoDB row formats in MariaDB Server. Understand different formats like Compact, Dynamic, and Compressed, and how they impact storage efficiency and performance for your data.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-tablespaces/" %}
[innodb-tablespaces](innodb-tablespaces/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Manage InnoDB tablespaces in MariaDB Server. Understand their role in data organization, performance, and recovery, including file-per-table and shared tablespaces.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-troubleshooting/" %}
[innodb-troubleshooting](innodb-troubleshooting/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Troubleshoot InnoDB issues in MariaDB Server. Find solutions and best practices for common problems, ensuring your InnoDB-based applications run smoothly and efficiently.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-enterprise-server-innodb-operations/" %}
[mariadb-enterprise-server-innodb-operations](mariadb-enterprise-server-innodb-operations/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about InnoDB operations in MariaDB Enterprise Server. This section covers critical management tasks, including configuration, performance tuning, and troubleshooting for enterprise-grade deploym
{% endcolumn %}
{% endcolumns %}
