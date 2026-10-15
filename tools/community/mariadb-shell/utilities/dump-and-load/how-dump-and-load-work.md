---
description: >-
  How a dump takes a consistent snapshot and writes it in parallel chunks, which
  files a dump directory contains, and how a load schedules, retries, and
  resumes its work.
---

# How Dump and Load Work

A dump takes a consistent snapshot of a running server and writes it as compressed data chunks plus metadata, on several threads at once. A load replays the dump on several threads and records each completed step, so that it can resume after an interruption. A copy connects a dump and a load directly, from one server to another.

## The Dump Pipeline

The main thread connects to the source, checks privileges, and takes the locks that make the dump consistent. It then opens one worker session per thread (`threads`, 4 by default), and all workers read from the same snapshot. The workers write the schema and table definitions, split each table into chunks, and dump the chunks in parallel.

* **Metadata first.** The manifest (`@.json`) and the definitions are written before any data, so a load can begin while the dump is still running.
* **Chunks.** Each table is split into chunks of roughly `bytesPerChunk` (64 MB by default) along its primary key or a unique index. Chunks are compressed with zstd by default (`compression` also accepts `gzip` and `none`). A table without a primary key or unique index is still written to several files, but by one thread.
* **Completion marker.** `@.done.json` is written last. A dump directory without it belongs to a dump that is still running or was interrupted.

## Files in a Dump Directory

A dump is a directory of plain files that you can inspect, copy, archive, or upload like any other files. Object names appear in the file names; names that contain characters unsafe for file names are encoded, and the manifest maps them back. On systems that support permissions, directories are created as `rwxr-x---` and files as `rw-r-----`.

| File | Contents |
| --- | --- |
| `@.json` | The manifest: the dump options, the dumped schemas, the source server version and vendor, its binary log file, position, and GTID position, and its global system variables. See [What a Dump Carries](what-a-dump-carries.md#the-manifest). |
| `@.sql`, `@.post.sql` | Statements run at the start and at the end of a load. |
| `@.users.sql` | Accounts, roles, grants, and default roles. Written by `util.dump_instance()` when `users` is enabled. |
| `@.checksums.json` | Checksums of the table data, written when `checksum` is enabled. |
| `@.done.json` | The completion marker, with the number of rows and bytes written per table. |
| `schema.json`, `schema.sql` | Metadata of a schema, and its DDL: the `CREATE DATABASE` statement, sequences, events, routines, and packages. |
| `schema@table.json`, `schema@table.sql` | Metadata of a table (columns, storage engine, primary key, compression, triggers), and its `CREATE TABLE` statement. |
| `schema@view.pre.sql`, `schema@view.sql` | A placeholder for a view, created first so that other views can refer to it, and the view's real definition. |
| `schema@table@0.tsv.zst`, `schema@table@1.tsv.zst`, ... | Data chunks of a table. The last chunk has a double `@`, for example `schema@table@@7.tsv.zst`. |
| `schema@table@partition@@0.tsv.zst` | Data chunks of one partition of a partitioned table. |
| `*.idx` | An index file next to each data file, which the load uses to split the file into transactions and to track progress. |

The extension of a data file shows its format and compression: `.tsv.zst` for the default dialect with zstd, `.tsv.gz` with gzip, and `.tsv` without compression. The `csv`, `csv-unix`, and `csv-rfc-unix` dialects use `.csv`, and custom field and line settings use `.txt`. With `chunking` disabled, each table or partition is written to a single file without a chunk number, such as `schema@table.tsv`.

A load writes one more file, its progress file, next to the dump by default. See [Resuming a Load](#resuming-a-load).

## Consistency on MariaDB

With `consistent` enabled (the default), every table is dumped as of the same point in time, even while applications keep writing. On MariaDB, the dump combines three mechanisms, each in its own session:

1. **A brief global read lock.** `FLUSH TABLES WITH READ LOCK` stops writes for the moment it takes all worker sessions to start their transactions, so that they start at the same point. It is released as soon as they have.
2. **Consistent-snapshot transactions.** Each worker session runs `SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ` and `START TRANSACTION WITH CONSISTENT SNAPSHOT`, and reads from that snapshot for the rest of the dump. Writes to InnoDB tables continue meanwhile.
3. **The backup lock.** A dedicated session runs `BACKUP STAGE START` and `BACKUP STAGE BLOCK_DDL`, which blocks schema changes for the length of the dump, so that no table changes its definition while it is being dumped. The session waits at most five minutes for the lock. If it cannot get it, the dump lists the statements that hold it and fails. The lock is released with `BACKUP STAGE END` when the dump ends, also when it fails or is interrupted.

While `BACKUP STAGE BLOCK_DDL` is held:

| Another session runs | Result |
| --- | --- |
| DDL (`CREATE`, `ALTER`, `DROP`, `RENAME`, ...) | Waits until the dump ends |
| DML on InnoDB tables, or on Aria tables with `TRANSACTIONAL=1` | Runs |
| DML on MyISAM tables | Waits until the dump ends |
| Account management (`CREATE USER`, `GRANT`, ...) | Runs |

{% hint style="info" %}
Only tables on a transactional engine, such as InnoDB, are guaranteed to be dumped with consistent data. Writes to MyISAM tables are blocked for the whole dump.
{% endhint %}

The global read lock waits for as long as the server's `lock_wait_timeout` allows, which is one day by default on MariaDB. This is the same behavior as `mariadb-dump` and `mariadb-backup`. While it waits behind a long-running statement, it also blocks other sessions' writes, so to bound the wait, lower `lock_wait_timeout` for the dump account or the server.

### Without the RELOAD Privilege

Both locks require the `RELOAD` privilege. Without it, the dump reports that the backup lock is not available and continues as follows:

* **With `LOCK TABLES`,** the dump locks every dumped table, and the grant tables in the `mysql` schema, with `LOCK TABLES ... READ` while the snapshot transactions start. Schema changes are not blocked during the dump. Instead, the dump checks the binary log afterwards: if the GTID position or binary log position moved, it reads the binary log events of that period and fails if any of them was DDL. This check needs the binary log enabled and the `BINLOG MONITOR` privilege.
* **Without `LOCK TABLES` either,** the dump fails. Use `"consistent": False` to dump without any lock, at the cost of consistency.

`skipConsistencyChecks` turns off the binary log check.

## The Load Pipeline

The load opens the dump, compares it with the target, and checks for objects that already exist on the target before it changes anything. It then creates accounts (with `loadUsers`), schemas, and tables, and loads the data chunks in parallel. It finishes with deferred indexes, views, table statistics (with `analyzeTables`), and checksum verification (with `checksum`).

* **Validation.** The load refuses a dump made from a server of the other vendor, and one whose source used a different `lower_case_table_names`.
* **Existing objects.** Without `dropExistingObjects` or `ignoreExistingObjects`, the load lists every object that already exists on the target and stops before changing anything.
* **Session setup.** On a MariaDB target, the load sessions turn off `foreign_key_checks`, `unique_checks`, and `check_constraint_checks`, so that rows load in any order and rows that violate a `CHECK` constraint on the source are restored as they are. `sessionInitSql` adds your own statements, and `skipBinlog` turns off binary logging for the load sessions.
* **Indexes.** `deferTableIndexes` creates secondary indexes after the data is loaded, which is usually faster. The default, `fulltext`, defers only full-text indexes.

### Resuming a Load

The load records every step, completed or failed, in a progress file. By default the file is `load-progress.<server_id>.json` in the dump directory, where `<server_id>` is the `server_id` of the target. With `progressFile` you choose another path; an empty string turns progress tracking off.

If you run the same load again, it skips the completed steps and retries the rest. Chunks that were started but not finished are loaded again: duplicate rows are discarded by the server, and a table without a unique key is truncated before its chunks are reloaded. Resuming assumes that nobody changed the partially loaded data in between.

`resetProgress` discards the progress file and loads the whole dump again. It does not drop what was already loaded, so drop those objects first or combine it with `dropExistingObjects`.

### Loading While a Dump Runs

With `waitDumpTimeout` set to a number of seconds, a load follows a dump that is still being written. It loads the tables and chunks that are available, then waits for more. It finishes when `@.done.json` appears. If the timeout passes while it is waiting, the load stops with an error and warns that the imported data may be incomplete; run it again to resume. This works for local directories and for object storage.

### How Chunks Are Scheduled

Data loads are spread across threads to keep all of them busy while limiting lock contention on any one table. With more tables than threads, threads work on different tables, larger tables first. With more threads than tables, larger tables get proportionally more threads, and the chunks of one table load in parallel. Some tables load one chunk at a time:

| Table | Chunks load | Why |
| --- | --- | --- |
| InnoDB and other transactional engines | In parallel | Row-level locking makes this the fastest case |
| Non-transactional engines (Aria, MyISAM, MEMORY, ...) | One at a time per table | Writes take a table lock anyway, and a failed chunk leaves at most one partial chunk behind |
| Tables with a `UNIQUE ... WITHOUT OVERLAPS` key | One at a time per table | Concurrent inserts into such an index deadlock on MariaDB |

The target decides which engines are transactional. While such a table loads one chunk at a time, the remaining threads load other tables. The partitions of a partitioned table count separately, so they still load concurrently.

Tables with a `WITHOUT OVERLAPS` key are loaded with `LOAD DATA ... IGNORE` instead of `REPLACE`, because MariaDB refuses `REPLACE` on them.

### Deadlock Retries

A chunk whose transaction is rolled back by a deadlock is retried from its start, with increasing delays. On MariaDB this covers error 1213 and error 4060, which a deadlock inside `LOAD DATA ... IGNORE` reports at commit. Transactions stay bounded in size: `maxBytesPerTransaction` caps the bytes per `LOAD DATA` statement, and defaults to the `bytesPerChunk` value of the dump.

## Copy

`util.copy_instance()`, `util.copy_schemas()`, and `util.copy_tables()` run a dump on the source and a load on the target at the same time, connected in memory. No files are written, and the target begins loading as soon as the source begins dumping. In the output, `SRC:` lines come from the dump and `TGT:` lines from the load. Because the data is a live stream, a copy cannot retry a chunk after a deadlock or resume after an interruption; run it again with `dropExistingObjects` or `ignoreExistingObjects`. See [Copy Utilities](copy-utilities.md).
