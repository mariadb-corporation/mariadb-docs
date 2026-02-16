---
description: >-
  The metadata_locks table lists currently held and requested metadata locks,
  which protect database object definitions from concurrent modification.
---

# Performance Schema metadata\_locks Table

{% hint style="info" %}
The `metadata_locks` table is available from MariaDB 10.5.2.
{% endhint %}

## Description

The `metadata_locks` table contains [metadata lock](../../../sql-statements/transactions/metadata-locking.md) information.

To enable metadata lock instrumentation at runtime, issue this statement:

```sql
UPDATE performance_schema.setup_instruments SET enabled='YES', timed='YES' 
  WHERE name LIKE 'wait/lock/metadata%';
```

To enable it permanently, add this to the `[mariadb]` section of the [configuration file](../../../../server-management/install-and-upgrade-mariadb/configuring-mariadb/configuring-mariadb-with-option-files.md) (for instance, `my.cnf`):

```ini
performance-schema-instrument='wait/lock/metadata/sql/mdl=ON'
```

{% hint style="info" %}
Performance Schema must be enabled in the configuration file for this to work (add `performance_schema=ON`).
{% endhint %}

The table is by default autosized, but the size can be configured with the [performance\_schema\_max\_metadata\_locks](../performance-schema-system-variables.md#performance_schema_max_metadata_locks) system variable.

The table is read-only, and [TRUNCATE TABLE](../../../sql-statements/table-statements/truncate-table.md) cannot be used to empty the table.

The table contains the following columns:

* `OBJECT_TYPE`
  * `VARCHAR(64)`
  * Null: No
  * Default: `NULL`
  * Description: Object type. One of `BACKUP`, `COMMIT`, `EVENT`, `FUNCTION`, `GLOBAL`, `LOCKING SERVICE`, `PROCEDURE`, `SCHEMA`, `TABLE`, `TABLESPACE`, `TRIGGER` (unused) or `USER LEVEL LOCK`.
* `OBJECT_SCHEMA`
  * `VARCHAR(64)`
  * Null: Yes
  * Default: `NULL`
  * Description: Object schema.
* `OBJECT_NAME`
  * `VARCHAR(64)`
  * Null: Yes
  * Default: `NULL`
  * Description: Object name.
* `OBJECT_INSTANCE_BEGIN`
  * `BIGINT(20) UNSIGNED`
  * Null: No
  * Default: `NULL`
  * Description: Address in memory of the instrumented object.
* `LOCK_TYPE`
  * `VARCHAR(32)`
  * Null: No
  * Default: `NULL`
  * Description: Lock type. One of `BACKUP_ALTER_COPY`, `BACKUP_BLOCK_DDL`, `BACKUP_COMMIT`, `BACKUP_DDL`, `BACKUP_DML`, `BACKUP_END`, `BACKUP_FLUSH`, [`BACKUP_FTWRL1`](performance-schema-metadata_locks-table.md#backup_ftwrl1), [`BACKUP_START`](performance-schema-metadata_locks-table.md#backup_start), [`BACKUP_TRANS_DML`](performance-schema-metadata_locks-table.md#backup_trans_dml), `BACKUP_WAIT_COMMIT`, `BACKUP_WAIT_DDL`, `BACKUP_WAIT_FLUSH`, `EXCLUSIVE`, `INTENTION_EXCLUSIVE`, `SHARED`, `SHARED_HIGH_PRIO`, `SHARED_NO_READ_WRITE`, `SHARED_NO_WRITE`, `SHARED_READ`, `SHARED_UPGRADABLE`, or `SHARED_WRITE`.
* `LOCK_DURATION`
  * `VARCHAR(32)`
  * Null: No
  * Default: `NULL`
  * Description: Lock duration. One of `EXPLICIT` (locks released by explicit action, for example a global lock acquired with `FLUSH TABLES WITH READ LOCK`) , `STATEMENT` (locks implicitly released at statement end), or `TRANSACTION` (locks implicitly released at transaction end).
* `LOCK_STATUS`
  * `VARCHAR(32)`
  * Null: No
  * Default: `NULL`
  * Description: Lock status. One of `GRANTED`, `KILLED`, `PENDING`, `POST_RELEASE_NOTIFY`, `PRE_ACQUIRE_NOTIFY`, `TIMEOUT`, or `VICTIM`.
* `SOURCE`
  * `VARCHAR(64)`
  * Null: Yes
  * Default: `NULL`
  * Description: Source file containing the instrumented code that produced the event, as well as the line number where the instrumentation occurred. This allows one to examine the source code involved.
* `OWNER_THREAD_ID`
  * `BIGINT(20) UNSIGNED`&#x20;
  * Null: Yes
  * Default: `NULL`
  * Description: Thread that requested the lock.
* `OWNER_EVENT_ID`
  * `BIGINT(20) UNSIGNED`&#x20;
  * Null: Yes
  * Default: `NULL`
  * Description: Event that requested the lock.

## Example

```sql
MariaDB [performance_schema]> SELECT * FROM metadata_locks\G
*************************** 1. row ***************************
          OBJECT_TYPE: TABLE
        OBJECT_SCHEMA: performance_schema
          OBJECT_NAME: metadata_locks
OBJECT_INSTANCE_BEGIN: 105553150198240
            LOCK_TYPE: SHARED_READ
        LOCK_DURATION: TRANSACTION
          LOCK_STATUS: GRANTED
               SOURCE: 
      OWNER_THREAD_ID: 13
       OWNER_EVENT_ID: 1
1 row in set (0.001 sec)
```

## Backup Lock Types

`BACKUP_*` lock types exposed through this table allow for granular locking, as opposed to the [`FLUSH TABLES WITH READ LOCK`](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md#purpose-of-flush-tables-with-read-lock) (FTWRL) statement which essentially freezes the entire database. With granular locking, backup tools like [mariadb-backup](../../../../server-usage/backup-and-restore/mariadb-backup/) can take consistent backups while keeping the database functioning.

### BACKUP\_TRANS\_DML

This lock is the lightest of the three. It is designed to ensure that DML[^1] operations – like `INSERT`, `UPDATE`, and `DELETE` – don't interfere with the backup of transactional tables (for instance, InnoDB).

* This lock **prevents DML changes** to transactional tables during a specific phase of the backup.
* It ensures that the backup tool can reach a consistent state without the data constantly shifting under its feet, but it doesn't block simple `SELECT` queries.

### BACKUP\_START

As the name suggests, this is the initialization lock. When a backup starts, the system needs to set a baseline.

* This lock **prevents** [**DDL**](#user-content-fn-2)[^2] **operations**. This means you cannot `CREATE`, `ALTER`, `RENAME`, or `DROP` tables while this lock is held.
* This lock protects the table structure during file-copy operations.

### BACKUP\_FTWRL1

This is a more refined, less aggressive version of the  `FLUSH TABLES WITH READ LOCK` statement. The "1" in the name signifies it is a specific stage of the backup lock hierarchy.

* This lock acts as a short-lived synchronization point. It ensures all non-transactional tables (like MyISAM) are flushed to disk and that the binary log position is captured accurately.
* Since InnoDB handles its own consistency, this lock is primarily for  "everything else" in your database – ensuring that the metadata and non-InnoDB tables are in a fixed state for a split second.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}

[^1]: DML (Data Manipulation Language): The subset of SQL commands used to add, modify, retrieve, or delete data within existing database tables.

[^2]: 
