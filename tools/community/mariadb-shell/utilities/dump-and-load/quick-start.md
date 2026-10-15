---
description: >-
  Prerequisites for the dump and load utilities, and examples for four common
  tasks: a full backup, a restore under a new name, a server-to-server copy,
  and provisioning a replica.
---

# Quick Start

This page lists what the source and target servers need, and then walks through four common tasks. Each example is a starting point: the [Dump Utilities](dump-utilities.md), [Load Dump Utility](load-dump-utility.md), and [Copy Utilities](copy-utilities.md) pages describe every option.

## Before You Start

* **Connect in Python mode.** The examples are Python calls on the `util` object:

  ```sh
  mariadb-shell --py mariadb://admin@db1.example.com:3306
  ```

* **Server version.** The utilities work with MariaDB 10.11 or later, on the source and on the target.
* **Privileges on the source.** The dump account needs `SELECT`, `SHOW VIEW`, `EVENT`, and `TRIGGER` on the dumped schemas. For a consistent dump it also needs `RELOAD`, which allows the global read lock and the backup lock. `BINLOG MONITOR` lets the dump record the binary log and GTID position. Dumping accounts with `util.dump_instance()` needs `SELECT` on the `mysql` schema. See [Consistency on MariaDB](how-dump-and-load-work.md#consistency-on-mariadb) for what happens without `RELOAD`.
* **`local_infile` on the target.** The load sends data with `LOAD DATA LOCAL INFILE`, so the target server must allow it. MariaDB enables `local_infile` by default; if it was turned off, turn it on before the load:

  ```sql
  SET GLOBAL local_infile = ON;
  ```

* **Try it first.** Every dump, load, and copy function accepts `"dryRun": True`. A dry run checks privileges and options and reports what would be done, without writing anything.

## Back Up a Server to Amazon S3

The following call dumps every user schema, together with accounts, roles, and grants, to the prefix `backups/2026-10-05` of an existing S3 bucket. The credentials come from `~/.aws/credentials` unless you name a profile or a file with `s3Profile` or `s3CredentialsFile`.

```python
util.dump_instance("backups/2026-10-05", {
    "s3BucketName": "acme-db-backups",
    "threads": 8,
    "checksum": True,
})
```

A load reads the dump directly from the bucket:

```python
util.load_dump("backups/2026-10-05", {
    "s3BucketName": "acme-db-backups",
    "loadUsers": True,
    "checksum": True,
})
```

Without `s3BucketName`, the same calls write to and read from a local directory. See [Object Storage](object-storage.md) for S3-compatible services, OCI, and Azure.

{% hint style="warning" %}
The object storage backends have not been validated against MariaDB. Local and network file systems are fully tested. See [Object Storage](object-storage.md).
{% endhint %}

## Restore a Schema Under a New Name

Dump one schema on the source:

```python
util.dump_schemas(["sales"], "/backups/sales", {"threads": 8})
```

Then load it on the target into a schema with a different name. The `schema` option works when the dump, or the part of it that you select, contains exactly one schema:

```python
util.load_dump("/backups/sales", {"schema": "sales_restored", "threads": 8})
```

Column defaults that draw from a sequence of the same schema follow the schema to its new name. To restore only part of a larger dump instead, select the objects with `includeSchemas` or `includeTables` on the load:

```python
util.load_dump("/backups/full", {"includeTables": ["sales.orders", "sales.order_items"]})
```

## Copy Schemas to Another Server

While connected to the source, copy schemas directly to a target server. The copy runs a dump and a load at the same time and passes the data in memory, so no files are written:

```python
util.copy_schemas(["sales", "inventory"], "mariadb://admin@db2.example.com:3306", {"threads": 8})
```

Use `util.copy_instance("mariadb://admin@db2.example.com:3306", {...})` to copy the whole server, accounts included, or `util.copy_tables()` to copy selected tables. The target must allow `local_infile`, as for a load.

## Provision a Replica

A dump records the GTID position of the source at the moment of the snapshot. Loading it with `updateGtidSet` stores that position on the target, so that replication starts with the first transaction after the dump.

1. On the primary, dump the server. The primary must have the binary log enabled, and the dump account needs `BINLOG MONITOR` so that the position is recorded:

   ```python
   util.dump_instance("/backups/for-replica", {"threads": 8})
   ```

2. On the new replica, an empty server with replication not running, load the dump:

   ```python
   util.load_dump("/backups/for-replica", {
       "loadUsers": True,
       "excludeUsers": ["root"],
       "updateGtidSet": "replace",
       "threads": 8,
   })
   ```

   `updateGtidSet: "replace"` sets `gtid_slave_pos` to the position in the dump. `excludeUsers` skips the `root` accounts, which already exist on a new server; without it, the load stops and lists them as existing objects.

3. Point the replica at the primary and start replication. The replication account (`repl` here) must exist on the primary with the `REPLICATION SLAVE` privilege:

   ```sql
   CHANGE MASTER TO
     MASTER_HOST = 'db1.example.com',
     MASTER_PORT = 3306,
     MASTER_USER = 'repl',
     MASTER_PASSWORD = '...',
     MASTER_USE_GTID = slave_pos;
   START REPLICA;
   ```

   `START REPLICA` is the current spelling; `START SLAVE` is the older one and does the same. Add the `MASTER_SSL*` options that your replication setup requires.

The replica receives exactly the transactions committed on the primary after the dump.

## If a Load Is Interrupted

Run the same `util.load_dump()` call again. The load reads its progress file and continues with the steps that did not complete. To discard the progress and start over, add `"resetProgress": True`; objects that were already created are not dropped, so remove them first or add `"dropExistingObjects": True`. See [How Dump and Load Work](how-dump-and-load-work.md#resuming-a-load).
