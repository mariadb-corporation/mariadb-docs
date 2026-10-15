---
description: >-
  Reference for util.load_dump: syntax, requirements, conflict handling,
  resuming, and every option that applies to a MariaDB target.
---

# Load Dump Utility

`util.load_dump()` loads a dump created by [`util.dump_instance()`, `util.dump_schemas()` or `util.dump_tables()`](dump-utilities.md) into the server of the global session. It loads table data in parallel, records every completed step so that an interrupted load can resume, and can load the whole dump or only part of it, into the original schema or a renamed one.

For the load pipeline and how chunks are scheduled, see [How Dump and Load Work](how-dump-and-load-work.md).

{% hint style="info" %}
Load options for MySQL HeatWave Service and other MySQL-only features (`heatwaveLoad`, `convertInnoDbVectorStore`, `lakehouseSource`, `disableBulkLoad`, the library filters, and the `histogram` mode of `analyzeTables`) do not apply to a MariaDB target. The built-in help still lists them.
{% endhint %}

## Syntax

{% tabs %}
{% tab title="Python" %}
```python
util.load_dump(url[, options])
```
{% endtab %}

{% tab title="Command line" %}
```sh
mariadb-shell [connection] -- util load-dump <url> [--option=value ...]
```

Option names are accepted in camelCase (`--includeSchemas`) or kebab-case (`--include-schemas`). See [Command Line Integration](../../using-mariadb-shell/command-line-integration.md).
{% endtab %}
{% endtabs %}

| Argument | Description |
| --- | --- |
| `url` | The dump location: a local directory (`/path` or `file:///path`), a `bucket/path` or `container/path` together with a bucket or container option, or an OCI pre-authenticated request. See [Object Storage](object-storage.md). Compressed files are decompressed transparently, and remote files are streamed. |
| `options` | A dictionary of options, for example `{"threads": 8, "schema": "shop_restored"}`. |

Load sessions inherit the connection options of the global session, such as TLS and compression.

## Requirements

### Local Data Loading

Table data is loaded with `LOAD DATA LOCAL INFILE`, so the target server must have `local_infile` enabled. It is `ON` by default in MariaDB Server. When it is off, the load stops before changing anything:

```text
ERROR: The 'local_infile' global system variable must be set to ON in the target server, after the server is verified to be trusted.
mysqlsh.Error: Shell Error (53025): local_infile disabled in server
```

Enable it with `SET GLOBAL local_infile = ON;` for the duration of the load.

### Same Vendor

A dump created from MariaDB Server loads only into MariaDB Server, and a dump created from MySQL only into MySQL. A cross-vendor load is refused before any DDL runs, with error 53039:

```text
ERROR: The dump was produced from MariaDB, but the target server is MySQL. Loading a dump across server vendors is not supported.
```

### Server Versions

The load reports the source and target versions before it starts:

```text
Target is MariaDB 12.3.2-MariaDB. Dump was produced from MariaDB 12.3.2-MariaDB
```

Loading into the same or the next or previous major version is allowed; a different major version is reported in a note. Loading across non-consecutive major versions, for example from 10.11 to 12.3, is refused unless you set `ignoreVersion`. The `lower_case_table_names` setting of the target must match the source.

### Privileges

The loading account needs the privileges to create and fill everything the dump contains:

* `CREATE`, `DROP`, `ALTER`, `INDEX`, `INSERT`, `REFERENCES` and, where present, `CREATE VIEW`, `CREATE ROUTINE`, `ALTER ROUTINE`, `TRIGGER` and `EVENT` on the target schemas. `DROP` is needed for `dropExistingObjects`, and `DELETE` for a resumed load of a table without a unique key, which is truncated first.
* `SET USER` (or `SUPER`) when views, routines, triggers or events have a `DEFINER` other than the loading account.
* With `loadUsers`: `CREATE USER`, plus the privileges being granted, with `GRANT OPTION`.
* With `skipBinlog`: `BINLOG ADMIN` (or `SUPER`) to set `sql_log_bin`.
* With `updateGtidSet`: `REPLICATION SLAVE ADMIN` (or `SUPER`) to set `gtid_slave_pos`.

The loader's sessions turn off `foreign_key_checks`, `unique_checks` and `check_constraint_checks`, so that rows load in any order and rows that violate a `CHECK` constraint on the source can be restored as they were.

## Options

### Selecting What to Load

Object names use the form `schema.object` (or `schema.table.trigger`), quoted with backticks where required. The filters apply to whatever the dump contains; they cannot add objects the dump does not have.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `loadDdl` | bool | `True` | Run the DDL scripts of the dump. |
| `loadData` | bool | `True` | Load table data. |
| `loadUsers` | bool | `False` | Create the accounts and roles in the dump and apply their grants. Statements for the account running the load are skipped. |
| `includeSchemas` | list of strings | not set | Load only these schemas. |
| `excludeSchemas` | list of strings | not set | Skip these schemas. |
| `includeTables` | list of strings | not set | Load only these tables and views (`schema.table`). Sequences are selected by the same option. |
| `excludeTables` | list of strings | not set | Skip these tables, views and sequences. |
| `includeRoutines` | list of strings | not set | Load only these procedures, functions and packages (`schema.routine`). |
| `excludeRoutines` | list of strings | not set | Skip these routines. |
| `includeEvents` | list of strings | not set | Load only these events (`schema.event`). |
| `excludeEvents` | list of strings | not set | Skip these events. |
| `includeTriggers` | list of strings | not set | Load only these triggers: `schema.table` for all triggers of a table, `schema.table.trigger` for one. |
| `excludeTriggers` | list of strings | not set | Skip these triggers. |
| `includeUsers` | list of strings | not set | Load only these accounts, as `'user'@'host'` or `'user'` for every host. Takes effect only with `loadUsers`. |
| `excludeUsers` | list of strings | not set | Skip these accounts. |
| `schema` | string | not set | Load into this schema instead of the original one. Allowed only when the dump, after filtering, contains exactly one schema. The schema is created if it does not exist. A column `DEFAULT` that uses a sequence of the same schema follows the rename. |

### Handling Existing Objects

Before it creates anything, the load checks the target for tables, views, sequences, routines, packages, triggers, events and accounts that the dump would create. Without either option below, any match stops the load and nothing is changed:

```text
Checking for pre-existing objects...
ERROR: Schema `shop_restored` already contains a table named `orders`
ERROR: Schema `shop_restored` already contains a sequence named `order_seq`
ERROR: One or more objects in the dump already exist in the destination database. You must either exclude these objects from the load, enable the 'dropExistingObjects' option to drop them automatically, or enable the 'ignoreExistingObjects' option to ignore them.
mysqlsh.Error: Shell Error (53021): While 'Checking for pre-existing objects': Duplicate objects found in destination database
```

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dropExistingObjects` | bool | `False` | Drop each existing object, then create it from the dump. Schemas themselves are not dropped. Accounts are dropped and re-created, except that the grants of the `PUBLIC` role are merged, never revoked. Cannot be combined with `ignoreExistingObjects`. |
| `ignoreExistingObjects` | bool | `False` | Keep existing objects and load the rest. Existing tables and views are not re-created; for other objects the `CREATE` statement still runs. Data is still loaded into existing tables unless you set `loadData: False`: rows with the same unique key are replaced, and a table without a unique key receives the rows a second time. Cannot be combined with `dropExistingObjects`. |
| `handleGrantErrors` | string | `"abort"` | What to do when a `GRANT` or `REVOKE` fails while loading accounts: `"abort"` stops the load, `"drop_account"` drops the account and continues, `"ignore"` reports the error and continues; a failed grant that lists several privileges is then retried one privilege at a time, so that as many as possible are applied. |

With `ignoreExistingObjects`, each match becomes a note:

```text
NOTE: Schema `shop_restored` already contains a table named `orders`, ignoring...
NOTE: Schema `shop_restored` already contains a sequence named `order_seq`, ignoring...
NOTE: One or more objects in the dump already exist in the destination database but will be ignored because the 'ignoreExistingObjects' option was enabled.
```

### Progress and Resuming

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `progressFile` | string | `load-progress.<server_id>.json` in the dump location | Where to record load progress: a local path, or an `http://`/`https://` URL written with `PUT` requests. An empty string disables progress tracking, and with it resuming. Required when loading through an OCI pre-authenticated request. |
| `resetProgress` | bool | `False` | Discard the recorded progress and load the whole dump again. Objects loaded earlier are not removed, so drop them first or combine this with `dropExistingObjects` or `ignoreExistingObjects`. |
| `showProgress` | bool | `True` when stdout is a terminal | Print progress while loading. |
| `waitDumpTimeout` | float | `0` | Load a dump that is still being written. When all available chunks are loaded, wait up to this many seconds for more before giving up. `0` or less disables waiting. The load ends early when the dump completes. |

On MariaDB the default progress file is named after the target's `server_id`, because MariaDB has no `server_uuid`. The built-in help shows the MySQL name.

### Performance

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `threads` | int | `4` | Number of parallel sessions that load data. Tables are spread over the threads, largest first; a chunked table can use several threads at once. |
| `backgroundThreads` | int | `threads` for a local dump, four times `threads` for a remote one | Additional threads that fetch metadata and DDL files. |
| `maxBytesPerTransaction` | string | taken from the dump | Maximum amount of data loaded by one `LOAD DATA` statement. Accepts `k`, `M`, `G`; minimum `4096`. When not set, the dump's `bytesPerChunk` is used, but only for data files larger than 1.5 times that size. Smaller transactions reduce undo and replication lag on large tables. |

Chunks of the same table load in parallel, except for tables on non-transactional engines (Aria, MyISAM and others) and tables with a `UNIQUE ... WITHOUT OVERLAPS` key, which load one chunk at a time while other tables use the remaining threads. A chunk rolled back by a deadlock is retried.

### Indexes and Statistics

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `deferTableIndexes` | string | `"fulltext"` | Create secondary indexes after the data is loaded, which is usually faster: `"off"` creates all indexes with the table, `"fulltext"` defers only full-text indexes, `"all"` defers every index except the primary key. |
| `loadIndexes` | bool | `True` | With deferred indexes, create them at the end of the load. Set it to `False` to load data now and create indexes in a later run. |
| `analyzeTables` | string | `"off"` | `"on"` runs `ANALYZE TABLE` on every table after it is loaded. Works even when all `load*` options are off. |

`analyzeTables` does not collect MariaDB's engine-independent statistics. Run `ANALYZE TABLE ... PERSISTENT FOR ALL` on the tables that need them. See [Limitations](limitations.md).

### Data Integrity

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `checksum` | bool | `False` | Verify each loaded table against the checksum stored in the dump. Requires a dump created with `checksum: True`. |
| `createInvisiblePKs` | bool | `False` | Add an invisible primary key to every table that has none: `` `my_row_id` BIGINT UNSIGNED AUTO_INCREMENT INVISIBLE PRIMARY KEY ``. Useful before setting up Galera, which needs a primary key on every table. |
| `characterSet` | string | taken from the dump | Character set of the load sessions. By default the one used for the dump (`utf8mb4` unless set). |

### Replication and Binary Log

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `updateGtidSet` | string | `"off"` | `"replace"` or `"append"` writes the GTID position recorded in the dump to the target's `gtid_slave_pos`, so that a replica can start with `MASTER_USE_GTID = slave_pos` from the point of the dump. `"replace"` requires the dumped position to contain the target's current `gtid_slave_pos`; `"append"` requires the two to share no replication domain. Refused while any replica thread is running. |
| `skipBinlog` | bool | `False` | Set `sql_log_bin = 0` in the load sessions, so the load is not written to the target's binary log. |
| `showMetadata` | bool | `False` | Print the binary log file, position and GTID position recorded in the dump, in YAML. |

On a Galera node, `updateGtidSet` sets the position on that node only. Start the replica on the node you loaded. For provisioning a replica step by step, see [Quick Start](quick-start.md).

### Session and Compatibility

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `sessionInitSql` | list of strings | `[]` | SQL statements to run in every session that loads data, for example `["SET SESSION innodb_lock_wait_timeout = 600"]`. Failing statements are not retried. |
| `ignoreVersion` | bool | `False` | Load even if the source and target major versions are not consecutive. |

### General

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dryRun` | bool | `False` | Read the dump, run every check (version, vendor, existing objects, `local_infile`), and print the steps the load would take, without changing the target. |

### Remote Storage

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `s3BucketName` | string | not set | Amazon S3 bucket. Related options: `s3CredentialsFile`, `s3ConfigFile`, `s3Profile`, `s3Region`, `s3EndpointOverride`. |
| `osBucketName` | string | not set | OCI Object Storage bucket. Related options: `osNamespace`, `ociConfigFile`, `ociProfile`, `ociAuth`. |
| `azureContainerName` | string | not set | Azure Blob Storage container. Related options: `azureConfigFile`, `azureStorageAccount`, `azureStorageSasToken`. |

See [Object Storage](object-storage.md).

## Resuming an Interrupted Load

The load writes every step to the progress file: each DDL script, each data chunk, each deferred index. Running the same `util.load_dump()` call again skips what is complete and continues with the rest. A chunk that was in flight when the load stopped is loaded again; duplicate rows are discarded by the server, and a table without a unique key is truncated before it is reloaded.

Pressing Ctrl+C once stops scheduling new work and lets running chunks finish. Pressing it again rolls back the active transactions.

```text
MariaDB localhost:3306 ssl  Py > util.load_dump("/backups/items", {"threads": 2})
...
Loading data...
Starting data load
^C -- Load interrupted. Canceling remaining work. Press ^C again to abort current tasks and rollback active transactions (slow).
Loading data - done
270 chunks (1.05M rows, 182.85 MB) for 1 tables in 1 schemas were loaded in 2 sec (avg throughput 69.07 MB/s, 398.39K rows/s)
...
RuntimeError: Aborted

MariaDB localhost:3306 ssl  Py > util.load_dump("/backups/items", {"threads": 2})
...
NOTE: Load progress file detected. Load will be resumed from where it was left, assuming no external updates were made.
You may enable the 'resetProgress' option to discard progress for this instance and force it to be completely reloaded.
Loading data...
Starting data load
Loading data - done
115 chunks (1.50M rows, 260.54 MB) for 1 tables in 1 schemas were loaded in 1 sec (avg throughput 61.36 MB/s, 351.77K rows/s)
```

{% hint style="warning" %}
Resuming assumes that nobody changed the partially loaded objects between the attempts. If they were changed, start over: drop the loaded objects and run the load with `resetProgress: True`.
{% endhint %}

The progress file belongs to the pair of dump and target server, not to the target schema. Loading the same dump a second time into the same server, for example under another `schema` name, finds the earlier progress and loads nothing (`There was no remaining data left to be loaded.`). Use `resetProgress: True` or a different `progressFile` for the second load.

## Examples

### Restore a Schema Under a New Name

```text
MariaDB localhost:3306 ssl  Py > util.load_dump("/backups/shop", {"schema": "shop_restored"})
Loading DDL and Data from '/backups/shop' using 4 threads.
Opening dump...
Opening dump - done
Dump is complete.
Target is MariaDB 12.3.2-MariaDB. Dump was produced from MariaDB 12.3.2-MariaDB
Scanning metadata - done
Checking for pre-existing objects - done
...
4 chunks (42.00K rows, 1.26 MB) for 3 tables in 1 schemas were loaded in 0 sec (avg throughput 1.26 MB/s, 42.00K rows/s)
6 DDL files were executed in 0 sec.
Data load duration: 0 sec
Total duration: 0 sec
0 warnings were reported during the load.
```

The sequence `order_seq` is restored too, and the `DEFAULT nextval(...)` of `orders` points to `shop_restored`.

### Check a Load Without Changing Anything

```text
MariaDB localhost:3306 ssl  Py > util.load_dump("/backups/shop", {"schema": "shop_restored", "dryRun": True})
...
NOTE: dryRun enabled, no changes will be made.
Target is MariaDB 12.3.2-MariaDB. Dump was produced from MariaDB 12.3.2-MariaDB
Checking for pre-existing objects - done
...
No data loaded.
6 DDL files were executed in 0 sec.
```

### Restore a Whole Server with Accounts

```python
util.load_dump("/backups/full-2026-10-05", {
    "loadUsers": True,
    "dropExistingObjects": True,
    "checksum": True,
    "threads": 8,
})
```

```text
Loading DDL, Data and Users from '/backups/full-2026-10-05' using 8 threads.
...
NOTE: Schema `shop` already contains a table named `order_items`, dropping...
...
Creating user accounts - done
Applying grants to user accounts - done
...
Verifying checksum information - done
1 accounts were loaded
7 checksums were verified in 3 sec.
```

### Load Only Some Tables

```python
util.load_dump("/backups/full", {"includeTables": ["shop.customers", "shop.orders", "shop.order_seq"]})
```

### Load Definitions and Data in Separate Runs

```python
util.load_dump("/backups/shop", {"loadData": False})   # definitions only
util.load_dump("/backups/shop", {"loadDdl": False})    # data; resumes from the first run's progress
```

{% hint style="warning" %}
A definitions-only run also creates the triggers. In a normal load, triggers are created after the data; when the data is loaded in a later run, the triggers already exist and fire for every loaded row. In a test, an `AFTER INSERT` trigger that writes to an audit table added a row there for each loaded order. Exclude such triggers from the first run with `excludeTriggers`, and load them afterwards with `includeTriggers`.
{% endhint %}

### Add Primary Keys While Loading

```python
util.load_dump("/backups/shop", {"schema": "shop_pk", "createInvisiblePKs": True})
```

A table without a primary key, such as `audit_log`, is created with the invisible key:

```sql
CREATE TABLE `audit_log` (
  `my_row_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT INVISIBLE,
  `msg` varchar(200) DEFAULT NULL,
  `at` datetime DEFAULT NULL,
  PRIMARY KEY (`my_row_id`)
) ENGINE=InnoDB ...
```

### Load from the Command Line

```sh
mariadb-shell root@localhost:3306 -- util load-dump /backups/shop-world \
  --include-schemas=world --dry-run
```

## Related Pages

{% content-ref url="dump-utilities.md" %}
[dump-utilities.md](dump-utilities.md)
{% endcontent-ref %}

{% content-ref url="copy-utilities.md" %}
[copy-utilities.md](copy-utilities.md)
{% endcontent-ref %}

{% content-ref url="mariadb-specific-features.md" %}
[mariadb-specific-features.md](mariadb-specific-features.md)
{% endcontent-ref %}
