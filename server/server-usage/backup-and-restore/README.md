---
description: >-
  Learn to back up and restore MariaDB Server databases. This section covers
  essential strategies and tools to ensure data safety and quick recovery from
  potential data loss.
---

# Backup & Restore

{% columns %}
{% column %}
{% content-ref url="backup-and-restore-overview.md" %}
[backup-and-restore-overview.md](backup-and-restore-overview.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Complete MariaDB backup and recovery guide. Complete resource for backup methods, mariabackup usage, scheduling, and restoration for production use.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-and-restore-with-mariadb-enterprise-server/forming-a-backup-strategy.md" %}
[forming-a-backup-strategy.md](backup-and-restore-with-mariadb-enterprise-server/forming-a-backup-strategy.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to design a robust backup strategy tailored to your business needs, balancing recovery time objectives and data retention policies.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-and-restore-with-mariadb-enterprise-server/backup-optimization.md" %}
[backup-optimization.md](backup-and-restore-with-mariadb-enterprise-server/backup-optimization.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Discover techniques to optimize your backup processes, including multithreading, incremental backups, and leveraging storage snapshots.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-and-restore-with-mariadb-enterprise-server/mariadb-enterprise-backup.md" %}
[mariadb-enterprise-backup.md](backup-and-restore-with-mariadb-enterprise-server/mariadb-enterprise-backup.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
This page details MariaDB Enterprise Backup, an enhanced version of mariadb-backup with enterprise-specific optimizations and support.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="mariadb-backup/" %}
[mariadb-backup](mariadb-backup/)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Get an overview of MariaDB Backup. This section introduces the hot physical backup tool, explaining its capabilities for efficient and consistent backups of your MariaDB Server.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="innodb-log-archive-pitr.md" %}
[innodb-log-archive-pitr.md](innodb-log-archive-pitr.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Perform point-in-time recovery in MariaDB by replaying archived InnoDB write-ahead logs at startup to restore the server to a specific Log Sequence Number (LSN).
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="replication-as-a-backup-solution.md" %}
[replication-as-a-backup-solution.md](replication-as-a-backup-solution.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Explore how to use replication as part of your backup strategy, allowing you to offload backup tasks to a replica server to reduce load on the primary.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-and-restore-via-dbforge-studio.md" %}
[backup-and-restore-via-dbforge-studio.md](backup-and-restore-via-dbforge-studio.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Learn how to use dbForge Studio, a GUI tool, to perform backup and restore operations for MariaDB databases visually.
{% endcolumn %}
{% endcolumns %}
