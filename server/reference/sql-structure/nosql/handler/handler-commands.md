# HANDLER

## Syntax

```sql
HANDLER tbl_name OPEN [ [AS] alias]
HANDLER tbl_name READ index_name { = | >= | <= | < } (value1,value2,...)
    [ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name READ index_name { FIRST | NEXT | PREV | LAST }
    [ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name READ { FIRST | NEXT }
    [ WHERE where_condition ] [LIMIT ... ]
HANDLER tbl_name CLOSE
```

## Description

The `HANDLER` statement provides direct access to table storage engine interfaces for key lookups and key or table scans. It is available for at least [Aria](../../../../server-usage/storage-engines/aria/), [Memory](../../../../server-usage/storage-engines/memory-storage-engine.md), [MyISAM](../../../../server-usage/storage-engines/myisam-storage-engine/) and [InnoDB](../../../../server-usage/storage-engines/innodb/) tables (and should work with most 'normal' storage engines, but not with system tables, [MERGE](../../../../server-usage/storage-engines/merge.md) or [views](../../../../server-usage/views/)).

`HANDLER ... OPEN` opens a table, allowing it to be accessible to subsequent `HANDLER ... READ` statements. The table can either be opened using an alias, or a table name. If opened with an alias, references to this table by further HANDLER statements must use this alias, and not the table name. If opened with a table name qualified by database name, further references to this table must use the unqualified table name. For example, if a table is opened with `db1.t1`, further references must use `t1`.

The table object is only closed when `HANDLER ... CLOSE` is called by the session, or the session closes, and is not shared by other sessions.

[Prepared statements](../../../sql-statements/prepared-statements/) work with `HANDLER READ`, which gives a much higher performance (50% speedup) as there is no parsing and all data is transformed in binary (without conversions to text, as with the normal protocol).

The `HANDLER` command does not work with [partitioned tables](../../../../server-usage/partitioning-tables/).

## Key Lookup

A key lookup is started with:

```sql
HANDLER tbl_name READ index_name { = | >= | <= | < }  (value,value) [LIMIT...]
```

The values stands for the value of each of the key columns. For most key types, except for `HASH` keys in `MEMORY` storage engine, you can use a prefix subset of its columns.

If you are using LIMIT, then in case of >= or > then there is an implicit NEXT implied, while if you are using <= or < then there is an implicit PREV implied.

After the initial read, you can use the following to scan rows in key order:

```sql
HANDLER tbl_name READ index_name NEXT [ LIMIT ... ]
or
HANDLER tbl_name READ index_name PREV [ LIMIT ... ]
```

{% hint style="warning" %}
Note that the row order is not defined for keys with duplicated values, and will vary from engine to engine.
{% endhint %}

## Key Scans

You can scan a table in key order by doing this:

```sql
HANDLER tbl_name READ index_name FIRST [ LIMIT ... ]
HANDLER tbl_name READ index_name NEXT  [ LIMIT ... ]
```

Alternatively, if the handler supports backwards key scans (which most do), you can use this:

```sql
HANDLER tbl_name READ index_name LAST [ LIMIT ... ]
HANDLER tbl_name READ index_name PREV [ LIMIT ... ]
```

## Table Scans

You can scan a table in row order by doing this:

```sql
HANDLER tbl_name READ FIRST [ LIMIT ... ]
HANDLER tbl_name READ NEXT  [ LIMIT ... ]
```

## Limitations

As this is a direct interface to the storage engine, some limitations may apply for what you can do and what happens if the table changes. Here are some of the common limitations.

### Finding 'Old Rows'

`HANDLER READ` is not transaction-safe, consistent or atomic. It's okay for the storage engine to return rows that existed when you started the scan, but that were later deleted. This can happen as the storage engine may cache rows as part of the scan from a previous read.

You may also find rows committed since the scan originally started.

### Invisible Columns

`HANDLER ... READ` also reads the data of [invisible columns](../../../sql-statements/data-definition/create/invisible-columns.md).

### System-Versioned Tables

`HANDLER ... READ` reads everything from [system-versioned tables](../../temporal-tables/system-versioned-tables.md), and so includes `row_start` and `row_end` fields, as well as all rows that have since been deleted or changed, including when history partitions are used.

### Other Limitations

* If you do an [ALTER TABLE](../../../sql-statements/data-definition/alter/alter-table/), all your `HANDLER`s for that table are automatically closed.
* If you do an `ALTER TABLE` for a table that is used by some other connection with `HANDLER`, the `ALTER TABLE` query waits for the `HANDLER` to be closed.
* For `HASH` keys, you must use all key parts when searching for a row.
* For `HASH` keys, you can't do a key scan of all values. You can only find all rows with the same key value.
* While each `HANDLER READ` command is atomic, if you do a scan in many steps, some engines may give you [error 1020](../../../error-codes/mariadb-error-codes-1000-to-1099/e1020.md) if the table changed between the commands. Please refer to the [specific engine handler page](./) if this happens.

## Error Codes

* [Error 1031](../../../error-codes/mariadb-error-codes-1000-to-1099/e1031.md) (`ER_ILLEGAL_HA`) Table storage engine for 't1' doesn't have this option
  * If you get this for `HANDLER OPEN` it means the storage engine doesn't support `HANDLER` calls.
  * If you get this for `HANDLER READ` , it means you are trying to use an incomplete `HASH` key.
* [Error 1020](../../../error-codes/mariadb-error-codes-1000-to-1099/e1020.md) (`ER_CHECKREAD`) Record has changed since last read in table '...'
  * This means that the table changed between two reads, and the handler can't handle this case for the given scan.

## Examples

```sql
CREATE TABLE t1 (f1 INT);

INSERT INTO t1 VALUES (1),(2),(3);

HANDLER t1 OPEN;

HANDLER t1 READ NEXT;
+------+
| f1   |
+------+
|    1 |
+------+

HANDLER t1 READ NEXT;
+------+
| f1   |
+------+
|    2 |
+------+
```

In the previous example, the `HANDLER` was opened with the `t1` table name. Since `HANDLER`s use unqualified table names, trying to access another table with this same name, even though it's in another database, will result in ambiguity. An alias needs to be used to avoid the ambiguity, resulting in [Error 1066: Not unique table/alias](broken-reference/):

```sql
CREATE DATABASE db_new;

CREATE TABLE db_new.t1 (id INT);

INSERT INTO db_new.t1 VALUES (4),(5),(6);

HANDLER db_new.t1 OPEN;
ERROR 1066 (42000): Not unique table/alias: 't1'

HANDLER db_new.t1 OPEN AS db_new_t1;

HANDLER db_new_t1 READ NEXT LIMIT 3;
+------+
| id   |
+------+
|    4 |
|    5 |
|    6 |
+------+
```

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
