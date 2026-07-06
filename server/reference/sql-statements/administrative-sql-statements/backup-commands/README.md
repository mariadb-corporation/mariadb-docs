---
description: >-
  Learn about backup statements for MariaDB Server. This section details SQL
  statements and utilities for creating consistent database backups, essential
  for disaster recovery and data protection.
---

# BACKUP Statements

{% columns %}
{% column %}
{% content-ref url="backup-lock.md" %}
[backup-lock.md](backup-lock.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Protect table files during backups. This command blocks DDL operations like ALTER TABLE while allowing read/write activity, ensuring file consistency for backup tools.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="backup-stage.md" %}
[backup-stage.md](backup-stage.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Control backup phases for external tools. Learn how to cycle through stages like START, BLOCK_DDL, and BLOCK_COMMIT to perform consistent backups with minimal locking.
{% endcolumn %}
{% endcolumns %}

{% columns %}
{% column %}
{% content-ref url="storage-snapshots-and-backup-stage-commands.md" %}
[storage-snapshots-and-backup-stage-commands.md](storage-snapshots-and-backup-stage-commands.md)
{% endcontent-ref %}
{% endcolumn %}

{% column %}
Combine database commands with storage-level snapshots. Learn the correct sequence of BACKUP STAGE commands to freeze writes safely while taking a disk snapshot.
{% endcolumn %}
{% endcolumns %}
