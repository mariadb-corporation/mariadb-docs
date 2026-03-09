---
description: The CONNECT storage engine.
---

# Inward and Outward Tables

There are two broad categories of file-based CONNECT tables. Inward and Outward. They are described below.

## Outward Tables

Tables are "outward" when their file name is specified in the CREATE TABLE statement using the _file\_name_ option.

Firstly, remember that CONNECT implements MED (Management of External Data). This means that the "true" CONNECT tables – "outward tables" – are based on data that belongs to files that can be produced by other applications or data imported from another DBMS.

Therefore, their data is "precious" and should not be modified except by specific commands such as [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md), [UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md), or [DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md). For other commands such as [CREATE](../../../../reference/sql-statements/data-definition/create/), [DROP](../../../../reference/sql-statements/data-definition/drop/), or [ALTER](../../../../reference/sql-statements/data-definition/alter/) their data is never modified or erased.

Outward tables can be created on existing files or external tables. When they are dropped, only the local description is dropped, the file or external table is not dropped or erased. Also, [DROP TABLE](../../../../reference/sql-statements/data-definition/drop/drop-table.md) does not erase the indexes.

[ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) produces the following warning, as a reminder:

```
Warning (Code 1105): This is an outward table, table data were not modified.
```

If the specified file does not exist, it is created when data is inserted into the table. If a [SELECT](../../../../reference/sql-statements/data-manipulation/selecting-data/select.md) is issued before the file is created, the following error is produced:

```
Warning (Code 1105): Open(rb) error 2 on <file_path>: No such file or directory
```

### Altering Outward Tables

When an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) is issued, it just modifies the table definition accordingly without changing the data. [ALTER](../../../../reference/sql-statements/data-definition/alter/) can be used safely to, for instance, modify options such as MAPPED, HUGE or READONLY but with extreme care when modifying column definitions or order options because some column options such as FLAG should also be modified or may become wrong.

Changing the table type with [ALTER](../../../../reference/sql-statements/data-definition/alter/) often makes no sense. But many suspicious alterations can be acceptable if they are just meant to correct an existing wrong definition.

Translating a CONNECT table to another engine is fine but the opposite is forbidden when the target CONNECT table is not table based or when its data file exists (because when the target table data cannot be changed and if the source table is dropped, the table data would be lost). However, it can be done to create a new file-based tables when its file does not exist or is void.

Creating or dropping indexes is accepted because it does not modify the table data. However, it is often unsafe to do it with an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement that does other modifications.

Of course, all changes are acceptable for empty tables.

**Note:** Using outward tables requires the [FILE](../../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege.

## Inward Tables

A special type of file-based CONNECT tables are “inward” tables. They are file-based tables whose file name is not specified in the [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) statement (no _file\_name_ option).

Their file are located in the current database directory and their name will default to tablename.type where tablename is the table name and type is the table type folded to lower case. When they are created without using a`CREATE TABLE ... SELECT ...` statement, an empty file is made at create\
time and they can be populated by further inserts.

They behave like tables of other storage engines and, unlike outward CONNECT tables, they are erased when the table is dropped. Of course they should not be read-only to be usable. Even though their utility is limited, they can be used for testing purposes or when the user does not have the [FILE](../../../../reference/sql-statements/account-management-sql-statements/grant.md#global-privileges) privilege.

### Altering Inward Tables

One thing to know, because CONNECT builds indexes in a specific way, is that all index modifications are done using an "in-place" algorithm – meaning not using a temporary table. This is why, when indexing is specified in an [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement containing other changes that cannot be done "in-place", the statement cannot be executed and raises an error.

Converting an inward table to an outward table, using an `ALTER TABLE` statement specifying a new file name and/or a new table type, is restricted the same way it is when converting a table from another engine to an outward table. However there are no restrictions to convert another engine table to a CONNECT inward table.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
