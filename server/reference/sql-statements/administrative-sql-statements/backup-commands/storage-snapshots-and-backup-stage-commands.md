---
description: >-
  Combine database commands with storage-level snapshots. Learn the correct
  sequence of BACKUP STAGE commands to freeze writes safely while taking a disk
  snapshot.
---

# Storage Snapshots and BACKUP STAGE Statements

The [BACKUP STAGE](backup-stage.md) statements are a set of statements to make it possible to make an efficient external backup tool. These commands could even be used by tools that perform backups by taking a snapshot of a file system, SAN, or some other kind of storage device.

## Generic Backup Process with Storage Snapshots

A tool that backs up MariaDB by taking a snapshot of a file system, SAN, or some other kind of storage device could use each `BACKUP STAGE` command in the following way:

* First, execute the following:

```sql
BACKUP STAGE START
BACKUP STAGE BLOCK_COMMIT
```

* Then, take the snapshot.
* Then, execute the following:

```sql
BACKUP STAGE END
```

The above ensures that all non-transactional tables are properly flushed to disk before the snapshot is done. Using `BACKUP STAGE` commands is also more efficient than using the [FLUSH TABLES WITH READ LOCK](../flush-commands/flush.md) command as the above set of commands will not block or be blocked by write operations to transactional tables.

Note that when the backup is completed, one should delete all files with the "#sql" prefix, as these are files used by concurrent running `ALTER TABLE`. Note that InnoDB will on server restart automatically delete any tables with the "#sql" prefix.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
