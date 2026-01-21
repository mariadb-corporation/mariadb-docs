---
description: >-
  This guide explains various methods for copying tables between MariaDB
  databases and servers, including using FLUSH TABLES FOR EXPORT and mysqldump.
---

# Copying Tables Between Databases and Servers

With MariaDB it's very easy to copy tables between different MariaDB databases\
and different MariaDB servers. This works for tables created with the [Archive](../storage-engines/archive.md), [Aria](../storage-engines/aria/), [CSV](../storage-engines/csv/), [InnoDB](../storage-engines/innodb/), [MyISAM](../storage-engines/myisam-storage-engine/), [MERGE](../storage-engines/merge.md), and [XtraDB](../storage-engines/innodb/) engines.

The normal procedures to copy a table is:

```
FLUSH TABLES db_name.table_name FOR EXPORT

# Copy the relevant files associated with the table

UNLOCK TABLES;
```

The table files can be found in [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir)/databasename (you can execute`SELECT @@datadir` to find the correct directory).\
When copying the files, you should copy all files with the same\
table\_name + various extensions. For example, for an Aria table of\
name foo, you will have files foo.frm, foo.MAI, foo.MAD and possibly\
foo.TRG if you have [triggers](../triggers-events/triggers/).

If one wants to distribute a table to a user that doesn't need write\
access to the table and one wants to minimize the storage size of the\
table, the recommended engine to use is Aria or MyISAM as one can\
pack the table with [aria\_pack](../../clients-and-utilities/aria-clients-and-utilities/aria_pack.md) or [myisampack](../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) respectively to make it notablly\
smaller. MyISAM is the most portable format as it's not dependent on\
whether the server settings are different. Aria and InnoDB require the same\
block size on both servers.

## Copying Tables When the MariaDB Server is Down

The following storage engines support export without `FLUSH TABLES ... FOR EXPORT`, assuming the source server is down and the receiving server is not accessing the files during the copy.

| Engine                                              | Comment                                                                                                                                                                                                         |
| --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Archive](../storage-engines/archive.md)            |                                                                                                                                                                                                                 |
| [Aria](../storage-engines/aria/)                    | Requires clean shutdown. Table will automatically be fixed on the receiving server if aria\_chk --zerofill was not run. If aria\_chk --zerofill is run, then the table is immediately usable without any delays |
| [CSV](../storage-engines/csv/)                      |                                                                                                                                                                                                                 |
| [MyISAM](../storage-engines/myisam-storage-engine/) |                                                                                                                                                                                                                 |
| [MERGE](../storage-engines/merge.md)                | .MRG files can be copied even while server is running as the file only contains a list of tables that are part of merge.                                                                                        |

## Copying Tables Live From a Running MariaDB Server

For all of the above storage engines (Archive, Aria, CSV, MyISAM and MERGE), one can copy tables even from a live server under the following circumstances:

* You have done a `FLUSH TABLES` or `FLUSH TABLE table_name` for the specific table.
* The server is not accessing the tables during the copy process.

The advantage of [FLUSH TABLES table\_name FOR EXPORT](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md) is that the table is read locked until [UNLOCK TABLES](../../reference/sql-statements/transactions/lock-tables.md) is executed.

**Warning**: If you do the above live copy, you are doing this on **your own risk** as if you do something wrong, the copied table is very likely to be corrupted. The original table will of course be fine.

## An Efficient Way to Give Someone Else Access to a Read Only Table

If you want to give a user access to some data in a table for the user to use in\
their MariaDB server, you can do the following:

First let's create the table we want to export. To speed up things, we\
create this without any indexes. We use `TRANSACTIONAL=0 ROW_FORMAT=DYNAMIC` for Aria to use the smallest possible row format.

```
CREATE TABLE new_table ... ENGINE=ARIA TRANSACTIONAL=0;
ALTER TABLE new_table DISABLE_KEYS;
# Fill the table with data:
INSERT INTO new_table SELECT * ...
FLUSH TABLE new_table WITH READ LOCK;

# Copy table data to some external location, like /tmp with something
# like cp /my/data/test/new_table.* /tmp/

UNLOCK TABLES;
```

Then we pack it and generate the indexes. We use a big sort buffer to speed\
up generating the index.

```
> ls -l /tmp/new_table.*
-rw-rw---- 1 mysql my 42396148 Sep 21 17:58 /tmp/new_table.MAD
-rw-rw---- 1 mysql my     8192 Sep 21 17:58 /tmp/new_table.MAI
-rw-rw---- 1 mysql my     1039 Sep 21 17:58 /tmp/new_table.frm
> aria_pack /tmp/new_table
Compressing /tmp/new_table.MAD: (922666 records)
- Calculating statistics
- Compressing file
46.07%
> aria_chk -rq --ignore-control-file --sort_buffer_size=1G /tmp/new_table
Recreating table '/tmp/new_table'
- check record delete-chain
- recovering (with sort) Aria-table '/tmp/new_table'
Data records: 922666
- Fixing index 1
State updated
> ls -l /tmp/new_table.*
-rw-rw---- 1 mysql my 26271608 Sep 21 17:58 /tmp/new_table.MAD
-rw-rw---- 1 mysql my 10207232 Sep 21 17:58 /tmp/new_table.MAI
-rw-rw---- 1 mysql my     1039 Sep 21 17:58 /tmp/new_table.frm
```

The procedure for MyISAM tables is identical, except that [myisamchk](../../clients-and-utilities/myisam-clients-and-utilities/myisamchk.md) doesn't have the `--ignore-control-file` option.

## Copying InnoDB's Transportable Tablespaces

InnoDB's file-per-table tablespaces are transportable, which means that you can copy a file-per-table tablespace from one MariaDB Server to another server. See [Copying Transportable Tablespaces](../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) for more information.

## Importing Tables

Tables that use most storage engines are immediately usable when their files are copied to the new [datadir](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#datadir).

However, this is not true for tables that use [InnoDB](../storage-engines/innodb/). InnoDB tables have to be imported with [ALTER TABLE ... IMPORT TABLESPACE](../../reference/sql-statements/data-definition/alter/alter-table/#import-tablespace). See [Copying Transportable Tablespaces](../storage-engines/innodb/innodb-tablespaces/innodb-file-per-table-tablespaces.md#copying-transportable-tablespaces) for more information.

## See Also

* [FLUSH TABLES FOR EXPORT](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush-tables-for-export.md)
* [FLUSH TABLES](../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md)
* [myisampack](../../clients-and-utilities/myisam-clients-and-utilities/myisampack.md) - Compressing the MyISAM data file for easier distribution.
* [aria\_pack](../../clients-and-utilities/aria-clients-and-utilities/aria_pack.md) - Compressing the Aria data file for easier distribution
* [mariadb-dump](../../clients-and-utilities/backup-restore-and-import-clients/mariadb-dump.md) - Copying tables to other SQL servers. You can use the `--tab` to create a CSV file of your table content.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
