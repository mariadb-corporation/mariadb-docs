# MaxScale Exasol CDC

{% hint style="info" %}
This functionality is available from MaxScale 26.10.
{% endhint %}

## Overview

Exasol CDC replicates the changes of a MariaDB server into Exasol. It is part of
the [binlogrouter](maxscale-binlogrouter.md): the binlogrouter replicates the
binary logs of a MariaDB primary, and Exasol CDC applies the row and
schema changes in those logs to Exasol, using ODBC.

Exasol CDC is enabled by setting
[odbc\_connection\_string](#odbc_connection_string) in a binlogrouter service,
and started with [cdc-start](#starting-and-stopping).

An existing database can be copied into Exasol with a [bulk copy](#bulk-copy).

The replication position is stored in Exasol, in the table
`maxscale_cdc.gtid_current_pos`, so replication resumes where it stopped after
a restart of MaxScale.

Rows are collected into batches, called cycles, limited by
[odbc\_perf\_max\_buffered\_rows](#odbc_perf_max_buffered_rows) and
[odbc\_perf\_max\_buffer\_time](#odbc_perf_max_buffer_time). Up to
[odbc\_perf\_ncycles](#odbc_perf_ncycles) cycles are applied in parallel.

## Requirements

On the MariaDB primary:
```
binlog_format=ROW
binlog_row_image=FULL
binlog_row_metadata=FULL
```
Replicated tables must use a transactional storage engine, normally InnoDB.

The Exasol user of the connection must be able to create, alter and drop
schemas and tables. If users are replicated, it must also be able to create
users and roles and to grant privileges.

## Settings

The settings are given in the binlogrouter service. None of them are dynamic:

### `odbc_connection_string`

* Type: string
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: The ODBC connection string for Exasol.

```
odbc_connection_string=DRIVER=/usr/lib64/maxscale/exasol/current/lib/libexaodbc.so;EXAHOST=exasoldb:8563;UID=cdc_user;PWD=cdc_password;FINGERPRINT=NOCERTCHECK
```

Referring to the driver through the `current` symbolic link keeps the
configuration working when a MaxScale update brings a new driver. The driver can
also be declared in `/etc/odbcinst.ini` and the connection given as a DSN, see
[ODBC](maxscale-exasolrouter.md#odbc) in the Exasolrouter documentation.

MaxScale adds the driver options that make Exasol exchange text as UTF-8, so
they need not be given.

### `odbc_include_tables`

* Type: stringlist
* Mandatory: No
* Dynamic: No
* Default: `""` (all tables)
* Description: The schemas and tables to replicate

The tables to replicate, `schema.table`, or `schema.*` for all tables
of a schema. A table that is not listed is not replicated, and DDL on it is
ignored.
```
odbc_include_tables=shop.orders,shop.customers,stats.*
```

### `odbc_insert_only_tables`

* Type: stringlist
* Mandatory: No
* Dynamic: No
* Default: `""`
* Description: Tables whose data is kept in Exasol when it is deleted in MariaDB

The tables, `schema.table`, or `schema.*` for all tables of a schema, whose
data is kept in Exasol when it is deleted in MariaDB. Inserts and updates are
replicated as for any other table, but deletes are not, so a row deleted in
MariaDB remains in Exasol. Neither are the statements that would remove data
from the table in Exasol: `TRUNCATE TABLE`, `DROP TABLE` and
`ALTER TABLE ... DROP COLUMN`. Other DDL, such as adding a column, is handled
as for any other table.

The tables are identified by name. If a table is renamed to a name that is
not listed, its data remains in Exasol under the new name, but deletes and
DDL on it are then replicated as for any other table.

A table listed here is replicated even if it is not listed in
[`odbc_include_tables`](#odbc_include_tables).

A `DROP DATABASE` is not replicated if any of its tables, or the schema
itself with `schema.*`, is listed here. All tables of the schema are then
kept in Exasol, including those that are not listed.

```
odbc_insert_only_tables=audit.events,history.*
```

### `odbc_case`

* Type: [enum](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#enumerations)
* Mandatory: No
* Dynamic: No
* Values: `keep`, `sensitive`, `insensitive`
* Default: `keep`
* Description: Exasol identifier comparison

How Exasol compares identifiers. `sensitive` and `insensitive` set the Exasol
system parameter `SQL_IDENTIFIER_COMPARISON` when replication starts; `keep`
leaves it as it is.
You are strongly advised to set odbc_case to `insensitive`, as it matches how MariaDB
compares column names and prevents errors.

**Note** The parameter is system-wide in Exasol, so it affects all users of the
database.

### `odbc_create_table_from_sql`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Create tables from `CREATE TABLE`

If `true`, a table is created in Exasol when its `CREATE TABLE` is replicated.
If `false`, it is created when a row of the table is first inserted, and
DDL on a table that does not yet exist in Exasol is ignored.

The setting becomes `true` if [odbc\_manage\_user\_grants](#odbc_manage_user_grants) is true.

### `odbc_stop_on_error`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `true`
* Description: Whether to stop replication on an error

What should happen when a transaction cannot be applied to Exasol, see
[Errors](#errors).

### `odbc_manage_user_grants`

* Type: [boolean](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#booleans)
* Mandatory: No
* Dynamic: No
* Default: `false`
* Description: Whether to replicate users, roles and grants

Replicate users, roles and grants, see [Users and Grants](#users-and-grants).
Enabling this also enables
[`odbc_create_table_from_sql`](#odbc_create_table_from_sql).

### Tuning

{% hint style="warning" %}
These settings may change or be removed in a later release, as tuning is
expected to become largely automatic.
{% endhint %}

#### `odbc_perf_max_buffered_rows`

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `750000`
* Description: Max rows to buffer before pipeline processing

The maximum number of accumulated rows that are applied as one batch.

#### `odbc_perf_max_buffer_time`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `2s`
* Description: Longest time rows are accumulated before pipeline processing

The longest time rows are accumulated before they are applied.

#### `odbc_perf_max_buffer_time_in_idle`

* Type: [duration](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#durations)
* Mandatory: No
* Dynamic: No
* Default: `500ms`
* Description: Longest time rows are accumulated with an idle pipeline

The longest time rows are accumulated while the pipeline is idle.

#### `odbc_perf_ncycles`

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `4`, range 1 to 4
* Description: Number of parallel cycles

How many cycles are applied in parallel. A lower value uses less memory and
loads Exasol less. If there is reason to tune CDC memory usage it is better
to first lower odbc_perf_max_buffered_rows. Only then odbc_perf_ncycles if needed.

#### `odbc_perf_nthreads`

* Type: count
* Mandatory: No
* Dynamic: No
* Default: `0` (no limit)
* Description: Threads in pipeline

The maximum number of threads used for applying data.
It is not recommended that this value be changed.

#### `odbc_perf_batch_size`

* Type: [size](../../maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide.md#sizes)
* Mandatory: No
* Dynamic: No
* Default: `200Mi`
* Description: Network request payload size

The largest amount of data (payload) sent to Exasol in one network request.

## Starting and Stopping

```
maxctrl call command binlogrouter cdc-start <service> [gtid=<gtid> | bulk-copy=<file>]
maxctrl call command binlogrouter cdc-stop <service>
```
A new Exasol CDC is stopped until `cdc-start` is run. Whether it is running or
stopped is remembered over restarts of MaxScale, in the file `cdc-state.json` in
the binlog directory.

* Without arguments, `cdc-start` continues from the position stored in Exasol.
  If Exasol has no stored position, replication starts from the first binary
  log of the binlogrouter.
* `gtid=<gtid>` starts replicating from the given GTID. Only the changes after
  it reach Exasol, so to get all the data, the binary logs must go back to when
  it was created; otherwise use `bulk-copy`.
* `bulk-copy=<file>` copies the source into Exasol first, see
  [Bulk Copy](#bulk-copy).

`gtid` and `bulk-copy` cannot be given together.

## Bulk Copy

A bulk copy creates the tables of a MariaDB server in Exasol, copies their
rows, and stores the GTID position of the server in Exasol. Replication then
continues from that position.

The source must be a replica of the primary the binlogrouter replicates from,
and it must not change during the copy: stop its replication and set it
`read_only`. The copy refuses to start if replication is running on the source,
and fails if the GTID position of the source changes during the copy. The
binlogrouter must still have the binary logs from the position of the source
onwards. This means that the binlogrouter should be started before the source
replication is stopped.

The copy is described in a JSON file on the MaxScale host:
```
{
  "source": {
    "host": "10.0.0.7",
    "port": 3306,
    "user": "copier",
    "password": "secret"
  },
  "schemas": [
    "shop",
    {"schema": "stats", "tables": ["daily", "monthly"]}
  ]
}
```
* `port` is optional, the default is 3306.
* A schema given as a string is copied in full; with `tables`, only those tables
  are copied.

The file is read when `cdc-start` is run, so an error in it fails the command.

A table that already exists in Exasol is dropped and copied again, unless it
has more than 10000 rows and the same number of rows as in the source. Such a
table is left as is, so running an interrupted copy again does not copy the
large tables that it already completed.

## Users and Grants

### Copying Users

```
maxctrl call command binlogrouter cdc-copy-users <service> host=<host> [port=<port>]
```
Copies the users and roles of a MariaDB server into Exasol, with their grants.
The `user` and `password` of the service are used for connecting to the server.
Users and roles that already exist in Exasol are skipped.

The progress is shown as `copy_users` in the [diagnostics](#monitoring).

### Replicating Users

With [odbc\_manage\_user\_grants](#odbc_manage_user_grants), `CREATE USER`,
`DROP USER`, `CREATE ROLE`, `DROP ROLE`, `GRANT` and `REVOKE` are replicated.

* The host part of a user is dropped: `'bob'@'%'` and `'bob'@'10.0.0.1'` are
  both the user `bob` in Exasol.
* Privileges without an Exasol equivalent are ignored.
* Passwords are not replicated: MariaDB stores only password hashes, so users
  get a random password in Exasol.

## DDL

Replicated:
* `CREATE DATABASE`, `DROP DATABASE`
* `CREATE TABLE`, `CREATE TABLE ... LIKE`, `DROP TABLE`, `TRUNCATE TABLE`,
  `RENAME TABLE`
* `ALTER TABLE ... ADD [COLUMN]`, `DROP [COLUMN]`, `RENAME COLUMN`

Ignored, as indexes and constraints are not replicated:
* `ADD INDEX`, `ADD KEY`, `ADD UNIQUE`, `ADD PRIMARY KEY`, `ADD FOREIGN KEY`,
  `ADD CONSTRAINT`, `DROP INDEX`

**Not supported.** These statements are ignored, so the table in Exasol no
longer matches the one in MariaDB. Replication may then stop at a later row
that does not fit.
* `ALTER TABLE ... MODIFY` and `CHANGE`, that is, changing the type of a column
* `ALTER TABLE ... RENAME TO`
* An `ALTER TABLE` with more than one kind of change, such as `ADD c INT, DROP d`
* `ALTER TABLE ... ALGORITHM=...` or `LOCK=...`
* `DROP COLUMN IF EXISTS`
* `CREATE OR REPLACE TABLE` and `CREATE OR REPLACE DATABASE`, which leave the
  existing table or schema as it is
* Partition operations
* `ALTER USER`, `SET PASSWORD`, `RENAME USER`
* Views, triggers, stored routines, events and sequences

## Type Mapping

| MariaDB | Exasol |
|---|---|
| `TINYINT`, `SMALLINT`, `MEDIUMINT`, `INT`, `BIGINT`, `YEAR`, `BIT` | `DECIMAL(n,0)` |
| `DECIMAL(p,s)` | `DECIMAL(p,s)`, at most 36 digits |
| `FLOAT`, `DOUBLE` | `DOUBLE` |
| `DATE` | `DATE` |
| `DATETIME`, `TIMESTAMP` | `TIMESTAMP` |
| `TIME` | `TIMESTAMP` on 1970-01-01 |
| `CHAR(n)`, `VARCHAR(n)` | `CHAR(n)`, `VARCHAR(n)` |
| `TEXT`, `JSON` | `VARCHAR(2000000)` |
| `ENUM`, `SET` | `VARCHAR` |
| `BINARY`, `VARBINARY`, `BLOB`, `INET4`, `INET6`, `UUID` | `VARCHAR`, always `NULL` |
| Spatial types | `GEOMETRY`, always `NULL` |

An empty string is stored as `NULL`, as Exasol does not distinguish the two.

## Errors

If a transaction cannot be applied, Exasol CDC first finds out which
transaction failed, which can take a moment. Then:
* With [odbc\_stop\_on\_error](#odbc_stop_on_error)`=true`, replication stops
  and the GTID and the error of the transaction are logged. Fix the cause and
  run `cdc-start`.
* With `odbc_stop_on_error=false`, the transaction is skipped with a warning and
  replication continues. The data in Exasol then differs from MariaDB.

If Exasol cannot be reached, MaxScale retries until it can; the `state` is
`connecting` meanwhile.

## Monitoring

The state of Exasol CDC is in the `CDC` object of the service diagnostics,
`maxctrl show service <service>`:

| Field | Meaning |
|---|---|
| `state` | `stopped`, `copying`, `connecting` or `replicating` |
| `stats.cycles` | Batches applied |
| `stats.rows` | Rows applied |
| `stats.rows_per_cycle` | Average rows per batch |
| `stats.rows_last_60s` | Rows applied in the last minute |
| `stats.replication_lag_ms` | Age of the oldest change in MariaDB that is not yet in Exasol |
| `stats.cdc_lag_avg_ms` | Average time from reading a row to it being in Exasol |
| `stats.cycle_time_avg_ms` | Average time to apply a batch |
| `copy_users` | Progress of `cdc-copy-users` |

Statistics per table:
```
maxctrl call command binlogrouter cdc-stats <service>
maxctrl call command binlogrouter cdc-reset-stats <service>
```

## Examples

```
[CDC-Service]
type=service
router=binlogrouter
user=maxuser
password=maxpwd
cluster=MariaDB-Monitor
select_master=true
server_id=7000
odbc_connection_string=DRIVER=/usr/lib64/maxscale/exasol/current/lib/libexaodbc.so;EXAHOST=exasoldb:8563;UID=cdc_user;PWD=cdc_password
odbc_include_tables=shop.*
odbc_case=insensitive
```

First start, copying the database:
```
maxctrl call command binlogrouter cdc-start CDC-Service bulk-copy=/etc/maxscale/copy.json
```

## Limitations

* A table without a primary key replicates incorrectly when it has identical
  rows: duplicates collapse into one row, and deleting one of them deletes all.
* Binary data (`BINARY`, `VARBINARY`, `BLOB`, `UUID`, `INET4`, `INET6`) and
  spatial data are stored as `NULL`.
* Compressed binary logs (`log_bin_compress=ON`) are not supported.
* `TIME` values that are negative or 24 hours or more are not stored correctly.
* `DECIMAL` values with more than 36 digits do not fit.
* The DDLs listed under [DDL](#ddl) as not supported are ignored.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>
