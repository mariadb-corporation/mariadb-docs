---
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

# Backup Examples

MariaDB offers a complete API-based backup capability to meet the data protection and recovery options. You can create and manage various backup types, including snapshots, physical backups, logical backups, incremental backups, and binary log backups.

## Snapshot Backup Examples

Create instant point-in-time snapshots of your MariaDB Cloud database services using one-time snapshot backups or cron-scheduled API calls.

{% content-ref url="snapshot-backup-examples.md" %}
[snapshot-backup-examples.md](snapshot-backup-examples.md)
{% endcontent-ref %}

## Physical Backup Examples

Execute full physical backups of your database files using MariaDB Cloud's API with support for one-time execution or automated scheduling examples.

{% content-ref url="physical-backup-examples.md" %}
[physical-backup-examples.md](physical-backup-examples.md)
{% endcontent-ref %}

## Logical Backup Examples

Create logical dump backups of your databases using API calls. It includes cron scheduling backups.

{% content-ref url="logical-backup-examples.md" %}
[logical-backup-examples.md](logical-backup-examples.md)
{% endcontent-ref %}

## Incremental Backup Examples

Captures only the data that has modified since the last full backup, with one-time and cron-based examples.

{% content-ref url="incremental-backup-examples.md" %}
[incremental-backup-examples.md](incremental-backup-examples.md)
{% endcontent-ref %}

## Binary Log Backup Examples

Configure the binary log backups, which are required for point-in-time recovery. It includes both one-time and cron-scheduled backups.

{% content-ref url="binarylog-backup-examples.md" %}
[binarylog-backup-examples.md](binarylog-backup-examples.md)
{% endcontent-ref %}

## Other Backup API Examples

Manage backup schedules and monitor backup status using API calls. It includes listing, retrieving, updating, or deleting backup schedules, and checking the status of backup jobs.

{% content-ref url="other-backup-api-examples.md" %}
[other-backup-api-examples.md](other-backup-api-examples.md)
{% endcontent-ref %}
