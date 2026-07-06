---
description: >-
  Replicate data with MariaDB Server. This section covers primary and replica
  setup, binary log formats, global transaction IDs, and multi-source, parallel,
  and semisynchronous replication.
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

# Replication

{% columns %}
{% column %}
{% content-ref url="replication-overview.md" %}
[replication-overview.md](replication-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the core concepts of MariaDB standard replication. Learn about the primary-replica architecture, data redundancy strategies, and how to scale read operations effectively.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="choosing-a-replication-strategy.md" %}
[choosing-a-replication-strategy.md](choosing-a-replication-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Choose a MariaDB replication strategy by matching the replication method and format to your goal — reducing downtime, scaling reads, or aggregating data — and weigh the trade-offs.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-based-binary-log.md" %}
[innodb-based-binary-log.md](innodb-based-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
From MariaDB 12.3, the binary log can be stored in InnoDB-managed, page-structured files integrated with InnoDB crash recovery, instead of traditional flat binary log files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-based-binary-log.md" %}
[innodb-based-binary-log.md](innodb-based-binary-log.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
From MariaDB 12.3, the binary log can be stored in InnoDB-managed, page-structured files integrated with InnoDB crash recovery, instead of traditional flat binary log files.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-statements.md" %}
[replication-statements.md](replication-statements.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access the complete reference of SQL statements used to manage replication. This guide covers commands for controlling primaries, configuring replicas, and monitoring status.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="setting-up-replication.md" %}
[setting-up-replication.md](setting-up-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete guide to MariaDB replication setup. Complete walkthrough for primary-replica topology with binary logging and GTID configuration.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="gtid.md" %}
[gtid.md](gtid.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete GTID replication reference: CHANGE MASTER master_use_gtid=current_pos|slave_pos, gtid_slave_pos table (InnoDB), START REPLICA UNTIL master_gtid_pos.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="read-only-replicas.md" %}
[read-only-replicas.md](read-only-replicas.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to configure replicas as read-only instances. This ensures data integrity by preventing accidental writes on the replica while allowing it to process replication events.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multi-source-replication.md" %}
[multi-source-replication.md](multi-source-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover how to replicate data from multiple primaries to a single replica. This guide covers the configuration for aggregating data from different sources into one MariaDB instance.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="multi-master-ring-replication.md" %}
[multi-master-ring-replication.md](multi-master-ring-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore the ring topology where each server acts as both primary and replica. Learn the configuration steps and caveats for setting up a circular replication environment.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="delayed-replication.md" %}
[delayed-replication.md](delayed-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn to configure a time lag for your replica. Delayed replication helps recover from human errors on the primary, such as accidental drop commands, by preserving older states.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="parallel-replication.md" %}
[parallel-replication.md](parallel-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Boost MariaDB Server replication performance with parallel replication. This section explains how to configure replicas to apply events concurrently, reducing lag and improving throughput.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="semisynchronous-replication.md" %}
[semisynchronous-replication.md](semisynchronous-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Enhance data consistency with semisynchronous replication. Ensure that the primary waits for at least one replica to acknowledge receipt of a transaction before committing.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="row-based-replication-with-no-primary-key.md" %}
[row-based-replication-with-no-primary-key.md](row-based-replication-with-no-primary-key.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the performance implications and best practices for replicating tables without primary keys when using row-based logging, including how to avoid full table scans.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="unsafe-statements-for-statement-based-replication.md" %}
[unsafe-statements-for-statement-based-replication.md](unsafe-statements-for-statement-based-replication.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Identify SQL statements that are non-deterministic and unsafe for statement-based replication. Learn why these queries cause divergence and how to switch to row-based logging.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-filters.md" %}
[replication-filters.md](replication-filters.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to filter specific databases or tables from being replicated. This guide covers configuration options to replicate only the data you need on specific replicas.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-threads.md" %}
[replication-threads.md](replication-threads.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Gain insight into the background threads that drive replication. Understand the roles of the I/O thread, SQL thread, and binlog dump thread in moving data between servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-and-foreign-keys.md" %}
[replication-and-foreign-keys.md](replication-and-foreign-keys.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how foreign key constraints interact with replication. Learn best practices for managing cascading deletes and updates across primary and replica servers.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-and-binary-log-system-variables.md" %}
[replication-and-binary-log-system-variables.md](replication-and-binary-log-system-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete Replication and Binary Log System Variables reference for MariaDB. Complete guide for configuration values, scope settings, and performance impact.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-and-binary-log-status-variables.md" %}
[replication-and-binary-log-status-variables.md](replication-and-binary-log-status-variables.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
View the status variables used to monitor replication health. Learn how to interpret metrics regarding log positions, connection status, and event counts.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binlog-event-checksum-interoperability.md" %}
[binlog-event-checksum-interoperability.md](binlog-event-checksum-interoperability.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn about checksum compatibility between different MariaDB versions. Ensure older replicas can correctly verify binary log events generated by newer primaries.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="binlog-event-checksums.md" %}
[binlog-event-checksums.md](binlog-event-checksums.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure checksums to detect data corruption in binary logs. Learn how to enable verification to ensure the integrity of replication events during transmission and storage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="changing-a-replica-to-become-the-primary.md" %}
[changing-a-replica-to-become-the-primary.md](changing-a-replica-to-become-the-primary.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Follow the procedure to promote a replica to a primary role. This guide details the steps for planned failovers or topology reorganization with minimal downtime.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-when-the-primary-and-replica-have-different-table-definitions.md" %}
[replication-when-the-primary-and-replica-have-different-table-definitions.md](replication-when-the-primary-and-replica-have-different-table-definitions.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand the rules and limitations when replicating between tables with differing structures. Learn how attribute promotion and column handling work in row-based replication.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="enhancements-for-start-transaction-with-consistent-snapshot.md" %}
[enhancements-for-start-transaction-with-consistent-snapshot.md](enhancements-for-start-transaction-with-consistent-snapshot.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to start a consistent transaction for backups or replication setup. This command ensures a consistent view of the database without locking tables unnecessarily.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="restricting-speed-of-reading-binlog-from-primary-by-a-replica.md" %}
[restricting-speed-of-reading-binlog-from-primary-by-a-replica.md](restricting-speed-of-reading-binlog-from-primary-by-a-replica.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Configure throughput limits for replication traffic. Learn to throttle the binlog download speed to prevent replication from consuming all available network bandwidth.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="running-triggers-on-the-replica-for-row-based-events.md" %}
[running-triggers-on-the-replica-for-row-based-events.md](running-triggers-on-the-replica-for-row-based-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Understand how triggers behave under row-based replication. Learn when and why triggers are not executed on the replica and how to manage complex logic in this mode.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="selectively-skipping-replication-of-binlog-events.md" %}
[selectively-skipping-replication-of-binlog-events.md](selectively-skipping-replication-of-binlog-events.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn techniques to bypass specific replication events. This guide explains how to ignore individual transactions or errors to restore replication flow after a stoppage.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="obsolete-replication-information/" %}
[obsolete-replication-information](obsolete-replication-information/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Access documentation for deprecated or removed replication features. Review this historical context when upgrading legacy systems or migrating to newer MariaDB versions.
{% endcolumn %}
{% endcolumns %}
