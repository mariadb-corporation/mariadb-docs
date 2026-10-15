---
description: >-
  Reference for util.copy_instance, util.copy_schemas and util.copy_tables,
  which copy data and objects directly from one MariaDB server to another
  without writing a dump to disk.
---

# Copy Utilities

The copy utilities run a dump and a load at the same time and connect them in memory. The source is the server of the global session; the target is a second server that you name with connection data. No files are written, and the target starts loading as soon as the first chunks are read from the source.

| Function | Copies | Equivalent to |
| --- | --- | --- |
| `util.copy_instance()` | Every user schema, plus accounts, roles and grants. | `util.dump_instance()` + `util.load_dump()` |
| `util.copy_schemas()` | The schemas you list. | `util.dump_schemas()` + `util.load_dump()` |
| `util.copy_tables()` | The tables, views and sequences you list from one schema. | `util.dump_tables()` + `util.load_dump()` |

The options are those of the [dump utilities](dump-utilities.md) and of the [load utility](load-dump-utility.md), minus the ones that concern files. The [option tables](#options) below list exactly which ones each copy accepts.

## Syntax

{% tabs %}
{% tab title="Python" %}
```python
util.copy_instance(connectionData[, options])
util.copy_schemas(schemas, connectionData[, options])
util.copy_tables(schema, tables, connectionData[, options])
```
{% endtab %}

{% tab title="Command line" %}
```sh
mariadb-shell <source> -- util copy-instance <target> [--option=value ...]
mariadb-shell <source> -- util copy-schemas <schema>[,<schema>...] <target> [--option=value ...]
mariadb-shell <source> -- util copy-tables <schema> <table>[,<table>...] <target> [--option=value ...]
```

See [Command Line Integration](../../using-mariadb-shell/command-line-integration.md).
{% endtab %}
{% endtabs %}

| Argument | Description |
| --- | --- |
| `connectionData` | The target server, as a URI string such as `"admin@db2.example.com:3306"` or a dictionary of connection options. Both forms accept everything a shell connection accepts, including `mariadb+ssh://` tunnels and TLS options. See [Connection URIs and Options](../../connecting/connection-uris-and-options.md). |
| `schemas` | `copy_schemas` only. A non-empty list of schema names. |
| `schema` | `copy_tables` only. The schema that holds the tables. |
| `tables` | `copy_tables` only. A list of table, view and sequence names. Pass an empty list together with `{"all": True}` to copy the whole schema. |
| `options` | A dictionary of options. |

If the target connection fails, the copy stops with `Could not connect to the target instance: ...` before it reads anything from the source. When the target URI has no password and none is stored, the shell prompts for it in interactive mode.

## Requirements

* A global session to the source server. Without one, the copy raises an error.
* **Same vendor on both ends.** A MariaDB source copies only to a MariaDB target. A mismatch is refused before anything is read:

  ```text
  The source instance is MariaDB and the target instance is MySQL. Copying across server vendors is not supported.
  ```
* The privileges of a dump on the source account and of a load on the target account. See [Dump Utilities](dump-utilities.md#privileges) and [Load Dump Utility](load-dump-utility.md#privileges).
* `local_infile` enabled on the target, as for any load. See [Local Data Loading](load-dump-utility.md#local-data-loading).
* The same version rules as `util.load_dump()`: non-consecutive major versions need `ignoreVersion`.

## How a Copy Differs from Dump and Load

* **No dump, no progress file.** An interrupted copy cannot resume; run it again with `dropExistingObjects` or `ignoreExistingObjects`, or drop what was copied first.
* **No deadlock retries.** Data flows as a stream, so a chunk rolled back by a deadlock on the target cannot be resent; the copy fails instead.
* **Two thread pools.** `threads` sets both the number of reading sessions on the source and the number of loading sessions on the target.
* **Output.** Lines from the dumping side start with `SRC:` and lines from the loading side with `TGT:`. Load progress is not shown. At the end, the copy prints the binary log file, position and GTID position of the source at the time of the copy.
* **Fixed settings.** Data is not compressed; `loadDdl`, `loadData` and `loadUsers` follow `ddlOnly`, `dataOnly` and `users`; the target version is taken from the target server.

## Options

Options marked as not accepted are rejected with `Invalid options: <name>`.

### Selection

| Option | Type | Default | Applies to | Description |
| --- | --- | --- | --- | --- |
| `includeSchemas`, `excludeSchemas` | list of strings | empty | `copy_instance` | Copy only, or skip, these schemas. |
| `users` | bool | `True` | `copy_instance` | Copy accounts, roles and grants. The account used on the target is skipped. |
| `includeUsers`, `excludeUsers` | list of strings | not set | `copy_instance` | Copy only, or skip, these accounts (`'user'@'host'` or `'user'`). |
| `includeTables`, `excludeTables` | list of strings | empty | `copy_instance`, `copy_schemas` | Copy only, or skip, these tables, views and sequences (`schema.table`). |
| `routines` | bool | `True` | `copy_instance`, `copy_schemas` | Copy procedures, functions and packages. |
| `includeRoutines`, `excludeRoutines` | list of strings | empty | `copy_instance`, `copy_schemas` | Copy only, or skip, these routines. |
| `events` | bool | `True` | `copy_instance`, `copy_schemas` | Copy events. |
| `includeEvents`, `excludeEvents` | list of strings | empty | `copy_instance`, `copy_schemas` | Copy only, or skip, these events. |
| `triggers` | bool | `True` | all | Copy triggers. |
| `includeTriggers`, `excludeTriggers` | list of strings | empty | all | Copy only, or skip, these triggers (`schema.table` or `schema.table.trigger`). |
| `all` | bool | `False` | `copy_tables` | Copy every table, view and sequence of the schema; `tables` must be empty. |
| `ddlOnly` | bool | `False` | all | Copy only definitions. |
| `dataOnly` | bool | `False` | all | Copy only rows. Cannot be combined with `dropExistingObjects`. |
| `where` | dictionary | not set | all | Maps `schema.table` to an SQL condition; only matching rows are copied. |
| `partitions` | dictionary | not set | all | Maps `schema.table` to a list of partitions to copy. |
| `schema` | string | not set | all | Create the objects in this schema on the target. Allowed only when one schema is copied. |

### Consistency, Performance and Integrity

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `consistent` | bool | `True` | Copy a consistent snapshot of the source. See [Dump Utilities](dump-utilities.md#consistency). |
| `skipConsistencyChecks` | bool | `False` | Skip the extra checks run when the backup lock cannot be taken. |
| `threads` | int | `4` | Number of reading sessions on the source, and the same number of loading sessions on the target. |
| `chunking` | bool | `True` | Split tables into chunks. |
| `bytesPerChunk` | string | `"64M"` | Approximate chunk size. Minimum `"128k"`. |
| `maxRate` | string | `"0"` | Maximum read rate per source thread, in bytes per second. `"0"` means no limit. |
| `maxBytesPerTransaction` | string | the value of `bytesPerChunk` | Maximum data per `LOAD DATA` statement on the target. Minimum `4096`. |
| `checksum` | bool | `False` | Compute checksums on the source and verify the copied tables against them on the target. |
| `tzUtc` | bool | `True` | Transfer `TIMESTAMP` values in UTC. |
| `defaultCharacterSet` | string | `"utf8mb4"` | Character set of the sessions on both ends. |

### Target Handling

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dropExistingObjects` | bool | `False` | Drop objects and accounts that already exist on the target before creating them. Schemas are not dropped. |
| `ignoreExistingObjects` | bool | `False` | Keep existing objects and copy the rest. |
| `handleGrantErrors` | string | `"abort"` | `"abort"`, `"drop_account"` or `"ignore"`, as for `util.load_dump()`. |
| `deferTableIndexes` | string | `"fulltext"` | `"off"`, `"fulltext"` or `"all"`. |
| `loadIndexes` | bool | `True` | Create deferred indexes at the end. |
| `analyzeTables` | string | `"off"` | `"on"` runs `ANALYZE TABLE` on each copied table. |
| `sessionInitSql` | list of strings | `[]` | Statements to run in every loading session on the target. |
| `skipBinlog` | bool | `False` | Do not write the copy to the target's binary log. |
| `updateGtidSet` | string | `"off"` | `"replace"` or `"append"` writes the source's GTID position to the target's `gtid_slave_pos`. |
| `ignoreVersion` | bool | `False` | Copy between non-consecutive major versions. |

### General

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dryRun` | bool | `False` | Run all checks on both servers and print what would be done, without changing the target. |
| `showProgress` | bool | `True` when stdout is a terminal | Print the source's progress. |

### Not Accepted

The following dump and load options do not apply to a copy and are rejected: all remote storage options, `compression`, the data format options (`dialect`, `fields*`, `linesTerminatedBy`), `targetVersion`, `loadDdl`, `loadData`, `loadUsers`, `progressFile`, `resetProgress`, `waitDumpTimeout`, `showMetadata`, `backgroundThreads`, `characterSet` and `createInvisiblePKs`. `copy_schemas` also rejects the schema and user filters; `copy_tables` rejects every include and exclude filter except those for triggers.

{% hint style="info" %}
MySQL HeatWave Service options are not available for MariaDB sources. The built-in help lists `compatibility`, which is refused for a MariaDB source, and `ocimds` is not accepted at all. The library filters, `allowDataMasking` and `dataMaskingPolicies` have no effect on MariaDB.
{% endhint %}

## Examples

### Copy a Schema to Another Server

```text
MariaDB localhost:3306 ssl  Py > util.copy_schemas(["world"], "root@db2.example.com:3306", {"threads": 4})
Copying DDL and Data from in-memory FS, source: db1.example.com:3306, target: db2.example.com:3306.
SRC: Acquiring global read lock
SRC: Global read lock acquired
SRC: 1 schemas will be dumped and within them 1 table, 0 views.
SRC: All transactions have been started
SRC: Locking instance for backup
SRC: Global read lock has been released
SRC: Running data dump using 4 threads.
TGT: Dump is still ongoing, data will be loaded as it becomes available.
TGT: Target is MariaDB 12.3.2-MariaDB. Dump was produced from MariaDB 12.3.2-MariaDB
TGT: Checking for pre-existing objects - done
...
SRC: Rows written: 500
...
TGT: 1 chunks (500 rows, 11.18 KB) for 1 tables in 1 schemas were loaded in 0 sec (avg throughput 11.18 KB/s, 500.00 rows/s)
TGT: 2 DDL files were executed in 0 sec.
TGT: 0 warnings were reported during the load.

---
Dump_metadata:
  Binlog_file: ''
  Binlog_position: 0
  GTID_position: ''
```

The binary log fields are empty here because the source runs without a binary log.

### Rehearse a Copy

```python
util.copy_schemas(["world"], "root@db2.example.com:3306", {"dryRun": True})
```

The dry run checks privileges on the source, connects to the target, checks the versions and looks for existing objects, then reports `No data loaded.` It holds no lock on the source: the lock lines read as checks, such as `SRC: The current user can acquire a global read lock`. If the schema already exists on the target, the dry run reports the conflicts as the real copy would.

### Copy Some Rows into a Differently Named Schema

```python
util.copy_tables("shop", ["customers"], "root@db2.example.com:3306", {
    "schema": "crm",
    "where": {"shop.customers": "country = 'DE'"},
})
```

```text
TGT: 1 chunks (500 rows, 17.94 KB) for 1 tables in 1 schemas were loaded in 0 sec (avg throughput 17.94 KB/s, 500.00 rows/s)
```

### Copy a Whole Server with Selected Accounts

```python
util.copy_instance("admin@db2.example.com:3306", {
    "excludeSchemas": ["staging"],
    "includeUsers": ["app", "reporting"],
    "threads": 8,
    "checksum": True,
})
```

### Copy Through an SSH Tunnel

```python
util.copy_schemas(["shop"], "mariadb+ssh://admin@db2.example.com:3306")
```

The shell opens an SSH connection to `db2.example.com` and reaches the target server through it, so a target that listens only on its loopback interface can be copied to. See [SSH Tunnels](../../connecting/ssh-tunnels.md) for bastion hosts and SSH options.

## Related Pages

{% content-ref url="dump-utilities.md" %}
[dump-utilities.md](dump-utilities.md)
{% endcontent-ref %}

{% content-ref url="load-dump-utility.md" %}
[load-dump-utility.md](load-dump-utility.md)
{% endcontent-ref %}
