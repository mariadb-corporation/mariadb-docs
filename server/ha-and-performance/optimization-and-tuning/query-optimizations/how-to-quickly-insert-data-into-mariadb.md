# How to Quickly Insert Data Into MariaDB

This article describes different techniques for inserting data quickly into MariaDB.

## Background

When inserting new data into MariaDB, the things that take time are (in order of importance):

* Syncing data to disk (as part of the end of transactions)
* Adding new keys. The larger the index, the more time it takes to keep keys updated.
* Checking against foreign keys (if they exist).
* Adding rows to the storage engine.
* Sending data to the server.

The following describes the different techniques (again, in order of importance) you can use to quickly insert data into a table.

## Disabling Keys

You can temporarily disable updating of non-unique indexes. This is mostly useful when there are zero (or very few) rows in the table into which you are inserting data.

```sql
ALTER TABLE table_name DISABLE KEYS;
BEGIN;
... inserting data WITH INSERT OR LOAD DATA ....
COMMIT;
ALTER TABLE table_name ENABLE KEYS;
```

In many storage engines (at least MyISAM and Aria),`ENABLE KEYS` works by scanning through the row data and collecting keys, sorting them and then creating the index blocks. This is an order of magnitude\
faster than creating the index one row at a time and it also uses less key buffer memory.

**Note:** When you insert into an **empty table** with [INSERT](../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md) or [LOAD DATA](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md), MariaDB **automatically** does a [DISABLE KEYS](../../../reference/sql-statements/data-definition/alter/alter-table/) before and an [ENABLE KEYS](../../../reference/sql-statements/data-definition/alter/alter-table/)\
afterwards.

When inserting big amounts of data, integrity checks are sensibly time-consuming. It is possible to disable the `UNIQUE` indexes and the [foreign keys](../optimization-and-indexes/foreign-keys.md) checks using the [unique\_checks](../system-variables/server-system-variables.md#unique_checks) and the [foreign\_key\_checks](../system-variables/server-system-variables.md#foreign_key_checks) system variables:

```sql
SET @@session.unique_checks = 0;
SET @@session.foreign_key_checks = 0;
```

For InnoDB tables, the [AUTO\_INCREMENT lock mode](../../../server-usage/storage-engines/innodb/auto_increment-handling-in-innodb.md) can be temporarily set to 2, which is the fastest setting:

```sql
SET @@global.innodb_autoinc_lock_mode = 2;
```

Also, if the table has [INSERT triggers](../../../server-usage/triggers-events/triggers/) or [PERSISTENT](../../../reference/sql-statements/data-definition/create/generated-columns.md) columns, you may want to drop them, insert all data, and recreate them.

## Loading Text Files

The **fastest way** to insert data into MariaDB is through the [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) command.

The simplest form of the command is:

```sql
LOAD DATA INFILE 'file_name' INTO TABLE table_name;
```

You can also read a file locally on the machine where the client is running by using:

```sql
LOAD DATA LOCAL INFILE 'file_name' INTO TABLE table_name;
```

This is not as fast as reading the file on the server side, but the difference is not that big.

`LOAD DATA INFILE` is very fast because:

1. there is no parsing of SQL.
2. data is read in big blocks.
3. if the table is empty at the beginning of the operation, all non-unique indexes are disabled during the operation.
4. the engine is told to cache rows first and then insert them in big blocks (At least MyISAM and Aria support this).
5. for empty tables, some transactional engines (like Aria) do not log the inserted data in the transaction log because one can roll back the operation by just doing a [TRUNCATE](../../../reference/sql-statements/table-statements/truncate-table.md) on the table.

Because of the above speed advantages there are many cases, when you need to insert **many** rows at a time, where it may be faster to create a file locally, add the rows there, and then use `LOAD DATA INFILE` to load them; compared to using `INSERT` to insert the rows.

You will also get [progress reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for`LOAD DATA INFILE`.

### mariadb-import

You can import many files in parallel with [mariadb-import](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) (`mysqlimport` before [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105)). For example:

```
mariadb-import --use-threads=10 database text-file-name [text-file-name...]
```

Internally [mariadb-import](../../../clients-and-utilities/backup-restore-and-import-clients/mariadb-import.md) uses [LOAD DATA INFILE](../../../reference/sql-statements/data-manipulation/inserting-loading-data/load-data-into-tables-or-index/load-data-infile.md) to read in the data.

## Inserting Data with INSERT Statements

### Using Big Transactions

When doing many inserts in a row, you should wrap them with `BEGIN / END` to avoid doing a full transaction (which includes a disk sync) for every row. For example, doing a begin/end every 1000 inserts will speed up your inserts by almost 1000 times.

```sql
BEGIN;
INSERT ...
INSERT ...
END;
BEGIN;
INSERT ...
INSERT ...
END;
...
```

The reason why you may want to have many `BEGIN/END` statements instead of just one is that the former will use up less transaction log space.

### Multi-Value Inserts

You can insert many rows at once with multi-value row inserts:

```sql
INSERT INTO table_name VALUES(1,"row 1"),(2, "row 2"),...;
```

The limit for how much data you can have in one statement is controlled by the [max\_allowed\_packet](../system-variables/server-system-variables.md#max_allowed_packet) server variable.

## Inserting Data Into Several Tables at Once

If you need to insert data into several tables at once, the best way to do so is to enable multi-row statements and send many inserts to the server at once:

```sql
INSERT INTO table_name_1 (auto_increment_key, data) VALUES (NULL,"row 1");
INSERT INTO table_name_2 (auto_increment, reference, data) VALUES (NULL, LAST_INSERT_ID(), "row 2");
```

[LAST\_INSERT\_ID()](../../../reference/sql-functions/secondary-functions/information-functions/last_insert_id.md) is a function that returns the last`auto_increment` value inserted.

By default, the command line `mariadb` client will send the above as multiple statements.

To test this in the `mariadb` client you have to do:

```sql
delimiter ;;
SELECT 1; SELECT 2;;
delimiter ;
```

**Note:** for multi-query statements to work, your client must specify the`CLIENT_MULTI_STATEMENTS` flag to `mysql_real_connect()`.

## Server Variables That Can be Used to Tune Insert Speed

| Option                                                                                                                        | Description                                                    |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [innodb\_buffer\_pool\_size](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_buffer_pool_size) | Increase this if you have many indexes in InnoDB/XtraDB tables |
| [key\_buffer\_size](../../../server-usage/storage-engines/myisam-storage-engine/myisam-system-variables.md#key_buffer_size)   | Increase this if you have many indexes in MyISAM tables        |
| [max\_allowed\_packet](../system-variables/server-system-variables.md#max_allowed_packet)                                     | Increase this to allow bigger multi-insert statements          |
| [read\_buffer\_size](../system-variables/server-system-variables.md#read_buffer_size)                                         | Read block size when reading a file with LOAD DATA             |

See [Server System Variables](../system-variables/server-system-variables.md) for the full list of server variables.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
