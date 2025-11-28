---
icon: cloud-binary
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
---

# Data Loading & Backup

This section describes an overview of MariaDB Cloud data migration, loading, offloading, backup, and restore operations. It covers everything from moving your original data to the cloud database to regularly replicating data in and out, as well as creating backup copies to prevent data loss in the event of disasters or other significant incidents.

## Migration, Data Loading

MariaDB Cloud provides multiple ways to migrate and load data that includes managed migration services, logical dumps, replication-based migrations, and common file imports.

{% content-ref url="migration-data-loading/" %}
[migration-data-loading](migration-data-loading/)
{% endcontent-ref %}

## Data Offloading

MariaDB Cloud offers multiple options for exporting or offloading data from a database service. These options include logical dumps, backup service offloading to your own cloud storage, or outbound replication. These methods enable you to move or rebuild your database somewhere else, integrate with other systems, and keep synchronized failover copies.

{% content-ref url="data-offloading/" %}
[data-offloading](data-offloading/)
{% endcontent-ref %}

## Backup and Restore

MariaDB Cloud provides complete backup and restore features to protect your data and maintain business continuity. You can create snapshot backups, full (physical) backups, incremental backups, and logical (mariadb-dump) backups based on your workload and recovery needs.

{% content-ref url="backup-and-restore/" %}
[backup-and-restore](backup-and-restore/)
{% endcontent-ref %}

