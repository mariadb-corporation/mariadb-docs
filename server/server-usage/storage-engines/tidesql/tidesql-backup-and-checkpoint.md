---
description: >-
  Online backup of a TideSQL data directory, durable checkpoints that flush and
  copy the database, and flushing a table for a physical copy.
---

# TideSQL Backup and Checkpoint

{% hint style="warning" %}
The target path for a backup or a checkpoint must not exist, or must be empty. The engine does not overwrite an existing populated directory.
{% endhint %}

## Online Backup

Setting `tidesdb_backup_dir` to a directory path triggers a consistent backup of the whole TidesDB data directory:

```sql
SET GLOBAL tidesdb_backup_dir = '/path/to/backup';
```

The backup runs without blocking reads and writes. The target directory must not exist or must be empty. The engine frees the calling connection's own transaction before starting, because the backup waits for open transactions to drain and would otherwise wait on the caller. After it completes, the variable reflects the path of the last successful backup. Clear it with an empty string:

```sql
SET GLOBAL tidesdb_backup_dir = '';
```

## Checkpoint

Setting `tidesdb_checkpoint_dir` takes a checkpoint, which forces a durability barrier on the live database and then writes a consistent copy of it to the given path:

```sql
SET GLOBAL tidesdb_checkpoint_dir = '/path/to/checkpoint';
```

The path must not exist or must be empty. The durability barrier flushes the memtable and forces the value log, the write-ahead log, and the manifest to disk regardless of the sync mode, so the live database is fully durable to this point, and the copy left at the path is a consistent, directly-openable database. This differs from `tidesdb_backup_dir` above, which writes the same kind of copy but does not force the extra durability barrier on the live database first. Use a checkpoint when you want the running database made durable as part of the snapshot, and a backup when you only need the copy.

## Flush for a Physical Copy

`FLUSH TABLES ... FOR EXPORT` takes a table lock so the data directory files hold still while you copy them, and `UNLOCK TABLES` releases it after copying:

```sql
FLUSH TABLES orders FOR EXPORT;
-- copy the column family directories from tidesdb_data/
UNLOCK TABLES;
```

<sub>_This page is licensed: GPLv2_</sub>
