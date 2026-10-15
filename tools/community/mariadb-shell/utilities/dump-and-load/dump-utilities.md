---
description: >-
  Reference for util.dump_instance, util.dump_schemas and util.dump_tables:
  syntax, required privileges, output locations, and every option that applies
  to a MariaDB source.
---

# Dump Utilities

The three dump utilities write a logical, parallel dump of a running MariaDB Server to a local directory or to object storage. They share one engine and almost all of their options. They differ only in what they select:

| Function | Dumps |
| --- | --- |
| `util.dump_instance()` | Every user schema on the server, plus accounts, roles and grants. |
| `util.dump_schemas()` | The schemas you list, with all of their objects. Accounts are not included. |
| `util.dump_tables()` | The tables, views and sequences you list from one schema. Routines and events are not included. |

Load any of these dumps with [`util.load_dump()`](load-dump-utility.md). To move data between two servers without writing files, use the [copy utilities](copy-utilities.md). For how a dump achieves consistency and how its chunks are written, see [How Dump and Load Work](how-dump-and-load-work.md). For the files a dump contains, see [What a Dump Carries](what-a-dump-carries.md).

{% hint style="info" %}
Options that exist only for MySQL HeatWave Service and other MySQL-only features (`ocimds`, `compatibility`, `lakehouseTarget`, data masking, libraries) are not available for MariaDB sources. The built-in help still lists some of them. `ocimds` and `compatibility` are refused with an error, `lakehouseTarget` cannot be used without `ocimds`, and the data masking and library options have no effect on a MariaDB server.
{% endhint %}

## Syntax

{% tabs %}
{% tab title="Python" %}
```python
util.dump_instance(outputUrl[, options])
util.dump_schemas(schemas, outputUrl[, options])
util.dump_tables(schema, tables, outputUrl[, options])
```
{% endtab %}

{% tab title="Command line" %}
```sh
mariadb-shell [connection] -- util dump-instance <outputUrl> [--option=value ...]
mariadb-shell [connection] -- util dump-schemas <schema>[,<schema>...] --output-url=<outputUrl> [--option=value ...]
mariadb-shell [connection] -- util dump-tables <schema> <table>[,<table>...] --output-url=<outputUrl> [--option=value ...]
```

Option names are accepted in camelCase (`--outputUrl`) or kebab-case (`--output-url`). List values are comma-separated. See [Command Line Integration](../../using-mariadb-shell/command-line-integration.md).
{% endtab %}
{% endtabs %}

| Argument | Description |
| --- | --- |
| `outputUrl` | Where to write the dump. See [Output Location](#output-location). |
| `schemas` | `dump_schemas` only. A non-empty list of schema names. Every schema must exist. |
| `schema` | `dump_tables` only. The schema that holds the tables. |
| `tables` | `dump_tables` only. A list of table, view and sequence names in `schema`. Every name must exist. Pass an empty list together with `{"all": True}` to dump every table and view of the schema. |
| `options` | A dictionary of options. Keys use camelCase, for example `{"threads": 8, "ddlOnly": True}`. |

All three functions use the global session's connection and open additional connections with the same options (TLS, compression and so on), one per thread.

## Requirements

* MariaDB Server 10.11 or later as the source.
* An open global session to the source server.
* Schema object names in the `latin1` or `utf8` character set.
* Data is guaranteed consistent only for transactional tables (InnoDB, and Aria with `TRANSACTIONAL=1`). See [How Dump and Load Work](how-dump-and-load-work.md).

The following are never dumped: the system schemas `information_schema`, `mysql`, `performance_schema` and `sys`; the internal accounts `mariadb.sys`, `mysql.sys`, `mysql.session` and `mysql.infoschema`; and the rows of log tables such as `mysql.general_log`, `mysql.slow_log` and `mysql.transaction_registry`.

### Privileges

| Privilege | Needed for |
| --- | --- |
| `SELECT` on the dumped tables and views | Reading definitions and data. The dump checks for it before it starts. |
| `SHOW VIEW` | Dumping views. |
| `TRIGGER` | Dumping triggers (`triggers: True`, the default). |
| `EVENT` | Dumping events (`events: True`, the default). |
| `RELOAD` | A consistent dump: the brief `FLUSH TABLES WITH READ LOCK` and MariaDB's backup lock (`BACKUP STAGE`). |
| `BINLOG MONITOR` | Recording the binary log file, position and GTID position in the dump. |
| `SELECT` on the `mysql` schema | Dumping accounts and roles (`dump_instance` with `users: True`). |
| `LOCK TABLES` | Only when `RELOAD` is missing: the fallback that locks every dumped table and the grant tables in `mysql`. |

Routines owned by other accounts also require the right to see their bodies, for example `SELECT` on `mysql.proc`.

When `RELOAD` is missing, the dump does not fail outright. It warns and falls back to `LOCK TABLES`:

```text
NOTE: Backup lock is not available to the account 'dumper2'@'%' and DDL changes will not be blocked. The dump may fail with an error if schema changes are made while dumping.
Acquiring global read lock
WARNING: The current user lacks privileges to acquire a global read lock using 'FLUSH TABLES WITH READ LOCK'. Falling back to LOCK TABLES...
...
NOTE: In order to create a consistent dump, either:
 * Use an account which has the RELOAD privilege.
 * Enable binary logging.
 * Enable binary logging and use an account which has the BINLOG MONITOR or SUPER privileges.
```

If the account lacks `LOCK TABLES` as well, the dump stops with error 52002 (`Unable to lock tables`). Set `consistent: False` to dump without any locks.

## Output Location

`outputUrl` names a directory:

| Form | Storage |
| --- | --- |
| `/path/to/dir` or `file:///path/to/dir` | Local or network file system (the default). A relative path is resolved against the current directory. |
| `bucket/path` with `osBucketName` | OCI Object Storage. |
| `bucket/path` with `s3BucketName` | Amazon S3 or an S3-compatible service. |
| `container/path` with `azureContainerName` | Azure Blob Storage. |
| An OCI pre-authenticated request (PAR) URL | OCI Object Storage, through the PAR. |

Remote storage options are described in [Object Storage](object-storage.md).

For a local directory:

* If the directory does not exist, it is created, but its parent must exist. The dump does not create intermediate directories.
* If the directory exists, it must be empty. Otherwise the dump stops before connecting any worker:

  ```text
  ValueError: Cannot proceed with the dump, the specified directory '/backups/shop' already exists at the target location /backups/shop and is not empty.
  ```
* On systems that support permissions, directories are created as `rwxr-x---` and files as `rw-r-----`.

The dump is complete when `@.done.json` has been written. A directory without it holds a dump that is still running or was interrupted.

## Options

Unless a row says otherwise, an option applies to all three functions.

### Filtering

Object names use the form `schema.object` (or `schema.table.trigger`) and must be quoted with backticks where the name requires it, for example ``"`my-db`.`order items`"``. A name that does not exist, or that belongs to a schema that is not dumped, is ignored. Naming the same object in an include and an exclude option is an error (`Conflicting filtering options`).

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `includeSchemas` | list of strings | empty | `dump_instance` only. Dump only these schemas. |
| `excludeSchemas` | list of strings | empty | `dump_instance` only. Skip these schemas. |
| `includeTables` | list of strings | empty | `dump_instance`, `dump_schemas`. Dump only these tables and views (`schema.table`). Sequences are selected by the same option. |
| `excludeTables` | list of strings | empty | `dump_instance`, `dump_schemas`. Skip these tables, views and sequences. |
| `includeRoutines` | list of strings | empty | `dump_instance`, `dump_schemas`. Dump only these stored procedures and functions (`schema.routine`). Oracle-mode packages are selected by the same option. |
| `excludeRoutines` | list of strings | empty | `dump_instance`, `dump_schemas`. Skip these routines. Excluding `db.name` skips the package, its body, and any function or procedure of that name. |
| `includeEvents` | list of strings | empty | `dump_instance`, `dump_schemas`. Dump only these events (`schema.event`). |
| `excludeEvents` | list of strings | empty | `dump_instance`, `dump_schemas`. Skip these events. |
| `includeTriggers` | list of strings | empty | Dump only these triggers: `schema.table` for all triggers of a table, `schema.table.trigger` for one. |
| `excludeTriggers` | list of strings | empty | Skip these triggers, in the same format. |
| `includeUsers` | list of strings | not set | `dump_instance` only. Dump only these accounts, as `'user'@'host'` or `'user'` for every host. Roles granted to a selected account are added automatically, and a note lists them. |
| `excludeUsers` | list of strings | not set | `dump_instance` only. Skip these accounts. An explicit exclusion wins over a role added automatically. |

### Content Selection

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `users` | bool | `True` | `dump_instance` only. Dump accounts, roles and grants. `includeUsers` and `excludeUsers` cannot be used when this is `False`. |
| `routines` | bool | `True` | `dump_instance`, `dump_schemas`. Dump stored procedures, functions and packages. |
| `events` | bool | `True` | `dump_instance`, `dump_schemas`. Dump events. |
| `triggers` | bool | `True` | Dump triggers. |
| `ddlOnly` | bool | `False` | Dump only object definitions, no rows. |
| `dataOnly` | bool | `False` | Dump only rows, no definitions. Cannot be combined with `ddlOnly`. |
| `all` | bool | `False` | `dump_tables` only. Dump every table, view and sequence of the schema. The `tables` argument must then be an empty list. |

There is no option for sequences: they follow the table filters. `dump_tables` dumps exactly the objects you name, so if a table's column `DEFAULT` draws from a sequence you did not list, the dump warns that the table cannot be created where the sequence does not exist:

```text
WARNING: Table `shop`.`orders` has a column DEFAULT which references sequence `order_seq`. The sequence is not included in this dump, so the table cannot be created unless a sequence of that name already exists in the schema it is loaded into.
```

### Rows and Partitions

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `where` | dictionary | not set | Maps `schema.table` to an SQL condition. Only matching rows are dumped. The condition must have balanced parentheses. |
| `partitions` | dictionary | not set | Maps `schema.table` to a list of partition or subpartition names. Only those partitions are dumped. A partition that does not exist is an error. |

Rows filtered with `where` are not checked against foreign keys, and the load does not check them either, because it disables foreign key checks. Filter related tables consistently.

MariaDB does not allow partition selection on a system-versioned table, so naming one in `partitions` is an error. Such tables are always dumped whole, current rows only. See [MariaDB-Specific Features](mariadb-specific-features.md).

### Chunking and Performance

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `threads` | int | `4` | Number of parallel sessions that read data. Must be greater than 0. |
| `chunking` | bool | `True` | Split each table's data into several files so that a single table can be dumped and loaded in parallel. When `False`, each table goes to one file. A table without a primary key or a unique index cannot be split by key; its data is still written to several files, but by a single thread. |
| `bytesPerChunk` | string | `"64M"` | Approximate size of each chunk before compression. Setting it enables chunking. Accepts the suffixes `k`, `M` and `G`. Minimum `"128k"`. |
| `maxRate` | string | `"0"` | Maximum read rate per thread, in bytes per second, with the same suffixes. `"0"` means no limit. Use it to protect a busy production server. |

### Compression and Checksums

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `compression` | string | `"zstd;level=1"` | Compression of the data files: `"zstd"`, `"gzip"` or `"none"`, optionally with a level, such as `"zstd;level=8"` or `"gzip;level=6"`. Cannot be empty. |
| `checksum` | bool | `False` | Compute a checksum of each dumped table (or `where`/`partitions` selection) and store it in the dump, so that `util.load_dump()` can verify the loaded data with its own `checksum` option. |

### Consistency

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `consistent` | bool | `True` | Produce a dump in which all tables reflect the same point in time. On MariaDB this takes a brief global read lock, starts a consistent-snapshot transaction in every worker session, and holds the backup lock `BACKUP STAGE BLOCK_DDL` for the length of the dump. `False` takes no locks. |
| `skipConsistencyChecks` | bool | `False` | Skip the additional checks that a consistent dump runs when the backup lock cannot be acquired, such as verifying that no DDL ran during the dump. |

The backup lock waits at most five minutes to be granted. While it is held, schema changes and writes to MyISAM tables are blocked; InnoDB writes continue. See [How Dump and Load Work](how-dump-and-load-work.md) for the full locking sequence.

### Data Format

Data files are written in a delimited text format, by default tab-separated with backslash escapes. Columns that cannot be stored safely as text, such as `BLOB`, are Base64-encoded; each such value must stay below roughly 0.74 times the target server's `max_allowed_packet`.

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dialect` | string | `"default"` | Preset for the field and line options below: `default`, `csv`, `tsv`, `csv-unix` or `csv-rfc-unix`. The individual options override the preset. |
| `fieldsTerminatedBy` | string | `"\t"` | Field separator. |
| `fieldsEnclosedBy` | char | `''` | Character that encloses field values. |
| `fieldsOptionallyEnclosed` | bool | `False` | When `True`, only some values (strings) are enclosed by `fieldsEnclosedBy`. When `False`, all are. |
| `fieldsEscapedBy` | char | `'\'` | Escape character. |
| `linesTerminatedBy` | string | `"\n"` | Line terminator. |
| `defaultCharacterSet` | string | `"utf8mb4"` | Character set of the dump sessions and of the data files. |
| `tzUtc` | bool | `True` | Dump `TIMESTAMP` values in UTC, so that a dump can be loaded into a server in another time zone. |

The dialect presets set these values:

| Dialect | Separator | Enclosure | Optionally enclosed | Escape | Line end |
| --- | --- | --- | --- | --- | --- |
| `default` | tab | none | no | `\` | LF |
| `csv` | `,` | `"` | yes | `\` | CR LF |
| `tsv` | tab | `"` | yes | `\` | CR LF |
| `csv-unix` | `,` | `"` | no | `\` | LF |
| `csv-rfc-unix` | `,` | `"` | yes | none (`"` doubled) | LF |

`csv-rfc-unix` follows RFC 4180 and writes `NULL` as an unquoted `NULL`. The `json` dialect is not supported for dumps.

### General

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `dryRun` | bool | `False` | Check privileges and options, and report what would be dumped, without holding locks or writing files. |
| `showProgress` | bool | `True` when stdout is a terminal | Print progress while dumping. |
| `targetVersion` | string | the MariaDB version the shell was built against | The MariaDB Server version you plan to load the dump into. It is validated and recorded in the dump's metadata. For a MariaDB source this is a MariaDB version, not a MySQL or Shell version, and it cannot be newer than the build's MariaDB version (13.1.0 for MariaDB Shell 26.9.5). |

A `targetVersion` that is too new is refused:

```text
ValueError: Target MariaDB version '99.0.0' is newer than the MariaDB version this Shell was built against (13.1.0). When dumping from MariaDB, the 'targetVersion' option takes a MariaDB server version.
```

### Remote Storage

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| `s3BucketName` | string | not set | Amazon S3 bucket. Related options: `s3CredentialsFile`, `s3ConfigFile`, `s3Profile`, `s3Region`, `s3EndpointOverride`. |
| `osBucketName` | string | not set | OCI Object Storage bucket. Related options: `osNamespace`, `ociConfigFile`, `ociProfile`, `ociAuth`. |
| `azureContainerName` | string | not set | Azure Blob Storage container. Related options: `azureConfigFile`, `azureStorageAccount`, `azureStorageSasToken`. |

The bucket or container must already exist. Individual files are limited to 1.2 TiB. For every storage option, see [Object Storage](object-storage.md).

## Examples

### Dump One Schema

```text
MariaDB localhost:3306 ssl  Py > util.dump_schemas(["shop"], "/backups/shop", {"threads": 4})
Acquiring global read lock
Global read lock acquired
Initializing - done
Gathering information...
1 schemas will be dumped and within them 3 tables, 1 view, 1 sequence, 1 routine, 1 trigger.
Gathering information - done
All transactions have been started
Locking instance for backup
Global read lock has been released
...
Schemas dumped: 1
Tables dumped: 3
Uncompressed data size: 1.26 MB
Compressed data size: 87.17 KB
Compression ratio: 14.5
Rows written: 42000
```

The dump directory then holds the manifest (`@.json`), the global scripts (`@.sql`, `@.post.sql`), one script and metadata file per schema and table, the compressed data chunks (`shop@orders@@0.tsv.zst` and so on), and `@.done.json`.

### Dump Selected Rows of a Few Tables

Dump the first quarter's orders, the Finnish customers, and the sequence the `orders` table draws its keys from:

```python
util.dump_tables("shop", ["orders", "customers", "order_seq"], "/backups/shop-q1", {
    "where": {
        "shop.orders": "placed BETWEEN '2025-01-01' AND '2025-03-31'",
        "shop.customers": "country = 'FI'",
    },
})
```

```text
2 tables and 0 views and 1 sequences will be dumped and within them 1 trigger.
...
Tables dumped: 2
Rows written: 5449
```

### Dump the Whole Server with Selected Accounts

```python
util.dump_instance("/backups/full-2026-10-05", {
    "excludeSchemas": ["world"],
    "includeUsers": ["dumper"],
    "checksum": True,
})
```

```text
1 out of 6 schemas will be dumped and within them 4 tables, 1 view, 1 sequence, 1 routine, 1 trigger.
1 out of 8 users will be dumped.
...
Running data dump using 4 threads. Checksumming enabled.
...
Computing checksum - done
```

The schema count includes the system schemas, which are always skipped.

### Check a Dump Before Running It

```python
util.dump_instance("/backups/full", {"dryRun": True})
```

The dry run checks privileges and reports the objects it would dump, without holding any lock or creating the directory. To check the privileges, it takes the global read lock and releases it at once, and it reports the locks as checks, such as `The current user can acquire a global read lock`, instead of `Global read lock acquired`.

### Dump Definitions Only

```python
util.dump_tables("shop", [], "/backups/shop-ddl", {"all": True, "ddlOnly": True})
```

### Throttle a Dump of a Busy Server

```python
util.dump_schemas(["shop"], "/backups/shop", {"threads": 2, "maxRate": "20M", "compression": "zstd;level=3"})
```

### Run a Dump from the Command Line

```sh
mariadb-shell root@localhost:3306 -- util dump-schemas shop,world \
  --output-url=/backups/shop-world \
  --exclude-tables=shop.order_items,shop.audit_log \
  --threads=2
```

```sh
mariadb-shell root@localhost:3306 -- util dump-tables shop audit_log \
  --output-url=/backups/audit-ddl --ddl-only
```

Options that take a dictionary, such as `where` and `partitions`, accept one `schema.table` entry per option, or the whole dictionary as JSON. A `partitions` entry maps to a list, so give it as JSON:

```sh
mariadb-shell root@localhost:3306 -- util dump-tables shop orders,audit_log \
  --output-url=/backups/shop-recent \
  --where="shop.orders=created_at >= '2026-01-01'" \
  --partitions='{"shop.audit_log": ["p2026"]}'
```

## Related Pages

{% content-ref url="load-dump-utility.md" %}
[load-dump-utility.md](load-dump-utility.md)
{% endcontent-ref %}

{% content-ref url="copy-utilities.md" %}
[copy-utilities.md](copy-utilities.md)
{% endcontent-ref %}

{% content-ref url="limitations.md" %}
[limitations.md](limitations.md)
{% endcontent-ref %}
