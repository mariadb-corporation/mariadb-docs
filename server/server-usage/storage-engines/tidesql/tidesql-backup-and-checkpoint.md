---
description: >-
  Online backup of a TideSQL data directory, durable checkpoints that flush and
  copy the database, and why FLUSH TABLES FOR EXPORT is not a backup.
---

# TideSQL Backup and Checkpoint

## Online Backup

Setting `tidesdb_backup_dir` to a directory path triggers a consistent backup of the whole TidesDB data directory:

```sql
SET GLOBAL tidesdb_backup_dir = '/path/to/backup';
```

The backup flushes the memtable, holds off compaction and value-log reclaim while it copies the manifest, the value log, and every SSTable the manifest references, and syncs those files first. It takes no lock that writers wait on, so reads and writes continue while it runs. The last directory of the path is created if it does not exist, and its parent must already exist. The directory must be new or empty. One that already holds files, such as an earlier backup, is refused before anything is flushed or copied, so a backup never mixes with another, and the statement fails naming the directory.

The engine rolls back and frees the calling connection's own open transaction before starting, so run the backup from a connection with no uncommitted work. After it completes, the variable reflects the path of the last successful backup. If the memtable cannot drain, or a compaction or value-log reclaim does not release in time, the statement fails with an error and the variable keeps its previous value. Clear it with an empty string:

```sql
SET GLOBAL tidesdb_backup_dir = '';
```

## Checkpoint

Setting `tidesdb_checkpoint_dir` takes a checkpoint, which forces a durability barrier on the live database and then writes a consistent copy of it to the given path:

```sql
SET GLOBAL tidesdb_checkpoint_dir = '/path/to/checkpoint';
```

The durability barrier flushes the memtable, then forces every SSTable, the write-ahead log, the value log, and the manifest to disk regardless of the sync mode, so the live database is fully durable to this point. The engine then runs the same copy as `tidesdb_backup_dir`, so the copy left at the path is a consistent, directly-openable database. The same directory rules apply, and the calling connection's own open transaction is rolled back first, as for a backup. After it completes, the variable reflects the path of the last successful checkpoint, and a failure leaves it at its previous value.

The difference from a backup is the barrier on the live database, most notably the forced sync of the active write-ahead log, which a backup does not do because it copies no WAL. Use a checkpoint when you want the running database made durable as part of the snapshot, and a backup when you only need the copy.

## FLUSH TABLES FOR EXPORT

{% hint style="warning" %}
`FLUSH TABLES ... FOR EXPORT` is not a backup method for TideSQL tables. Use `tidesdb_backup_dir` or `tidesdb_checkpoint_dir` instead.
{% endhint %}

The engine accepts `FLUSH TABLES ... FOR EXPORT`, which takes a server-level table lock that blocks writes to the table until `UNLOCK TABLES`. The engine does nothing further for it. It does not flush the memtable, and the library's background flush and compaction keep rewriting files under the data directory while the lock is held, so copying column family directories under this lock does not produce a consistent copy.

<sub>_This page is licensed: GPLv2_</sub>
