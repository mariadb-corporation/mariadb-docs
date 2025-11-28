# OPTIMIZE TABLE

## Syntax

```bnf
OPTIMIZE [NO_WRITE_TO_BINLOG | LOCAL] TABLE
    tbl_name [, tbl_name] ...
    [WAIT n | NOWAIT]
```

## Description

`OPTIMIZE TABLE` has two main functions. It can either be used to defragment tables, or to update the InnoDB fulltext index.

#### WAIT/NOWAIT

Set the lock wait timeout. See [WAIT and NOWAIT](../../../reference/sql-statements/transactions/wait-and-nowait.md).

### Defragmenting

`OPTIMIZE TABLE` works for [InnoDB](../../../server-usage/storage-engines/innodb/) (before [MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes), only if the [innodb\_file\_per\_table](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_file_per_table) server system variable is set), [Aria](../../../server-usage/storage-engines/aria/), [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) and [ARCHIVE](../../../server-usage/storage-engines/archive.md) tables, and should be used if you have deleted a large part of a table or if you have made many changes to a table with variable-length\
rows (tables that have [VARCHAR](../../../reference/data-types/string-data-types/varchar.md), [VARBINARY](../../../reference/data-types/string-data-types/varbinary.md), [BLOB](../../../reference/data-types/string-data-types/blob.md), or [TEXT](../../../reference/data-types/string-data-types/text.md) columns). Deleted rows are maintained in a\
linked list and subsequent `INSERT` operations reuse old row positions.

This statement requires [SELECT and INSERT privileges](../../../reference/sql-statements/account-management-sql-statements/grant.md) for the table.

By default, `OPTIMIZE TABLE` statements are written to the [binary log](../../../server-management/server-monitoring-logs/binary-log/) and will be [replicated](../../standard-replication/replication-overview.md). The `NO_WRITE_TO_BINLOG` keyword (`LOCAL` is an alias) will ensure the statement is not written to the binary log.

`OPTIMIZE TABLE` statements are not logged to the binary log if [read\_only](../system-variables/server-system-variables.md#read_only) is set. See also [Read-Only Replicas](../../standard-replication/read-only-replicas.md).

`OPTIMIZE TABLE` is also supported for partitioned tables. You\
can use`[ALTER TABLE](../../../../reference/sql-statements-and-structure/sql-statements/data-definition/alter/alter-table.md) ... OPTIMIZE PARTITION`\
to optimize one or more partitions.

You can use `OPTIMIZE TABLE` to reclaim the unused space and to defragment the data file. With other storage engines, `OPTIMIZE TABLE` does nothing by default, and returns this message: " The storage engine for the table doesn't support optimize". However, if the server has been started with the `--skip-new` option, `OPTIMIZE TABLE` is linked to [ALTER TABLE](../../../reference/sql-statements/data-definition/alter/alter-table/), and recreates the table. This operation frees the unused space and updates index statistics.

The [Aria](../../../server-usage/storage-engines/aria/) storage engine supports [progress reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for this statement.

If a [MyISAM](../../../server-usage/storage-engines/myisam-storage-engine/) table is fragmented, [concurrent inserts](../../../reference/sql-statements/data-manipulation/inserting-loading-data/concurrent-inserts.md) will not be performed until an `OPTIMIZE TABLE` statement is executed on that table, unless the [concurrent\_insert](../system-variables/server-system-variables.md#concurrent_insert) server system variable is set to `ALWAYS`.

### Updating an InnoDB fulltext index

When rows are added or deleted to an InnoDB [fulltext index](../optimization-and-indexes/full-text-indexes/), the index is not immediately re-organized, as this can be an expensive operation. Change statistics are stored in a separate location. The fulltext index is only fully re-organized when an `OPTIMIZE TABLE` statement is run.

By default, an OPTIMIZE TABLE will defragment a table. In order to use it to update fulltext index statistics, the [innodb\_optimize\_fulltext\_only](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_optimize_fulltext_only) system variable must be set to `1`. This is intended to be a temporary setting and should be reset to `0` once the fulltext index has been re-organized.

Since fulltext re-organization can take a long time, the [innodb\_ft\_num\_word\_optimize](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_ft_num_word_optimize) variable limits the re-organization to a number of words (2000 by default). You can run multiple OPTIMIZE statements to fully re-organize the index.

### Defragmenting InnoDB tablespaces

[MariaDB 10.1.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-1-series/mariadb-10-1-1-release-notes) merged the Facebook/Kakao defragmentation patch, allowing one to use `OPTIMIZE TABLE` to defragment InnoDB tablespaces. For this functionality to be enabled, the [innodb\_defragment](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment) system variable must be enabled. No new tables are created and there is no need to copy data from old tables to new tables. Instead, this feature loads `n` pages (determined by [innodb-defragment-n-pages](../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_defragment_n_pages)) and tries to move records so that pages would be full of records and then frees pages that are fully empty after the operation. Note that tablespace files (including ibdata1) will not shrink as the result of defragmentation, but one will get better memory utilization in the InnoDB buffer pool as there are fewer data pages in use.

See [Defragmenting InnoDB Tablespaces](defragmenting-innodb-tablespaces.md) for more details.

## See Also

* [Optimize Table in InnoDB with ALGORITHM set to INPLACE](../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-inplace-alter-algorithm.md#optimize-table)
* [Optimize Table in InnoDB with ALGORITHM set to NOCOPY](../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-nocopy-alter-algorithm.md#optimize-table)
* [Optimize Table in InnoDB with ALGORITHM set to INSTANT](../../../server-usage/storage-engines/innodb/innodb-online-ddl/innodb-online-ddl-operations-with-the-instant-alter-algorithm.md#optimize-table)

<sub>_This page is licensed: GPLv2, originally from_</sub> [<sub>_fill\_help\_tables.sql_</sub>](https://github.com/MariaDB/server/blob/main/scripts/fill_help_tables.sql)

{% @marketo/form formId="4316" %}
