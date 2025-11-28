# Engine-Independent Table Statistics

## Introduction

Before [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-0-series/changes-improvements-in-mariadb-10-0), the MySQL/MariaDB optimizer relied on storage engines (e.g. InnoDB) to provide statistics for the query optimizer. This approach worked; however it had some deficiencies:

* Storage engines provided poor statistics (this was\
  fixed to some degree with the introduction of [Persistent Statistics](innodb-persistent-statistics.md)).
* The statistics were supplied through the MySQL Storage Engine Interface, which puts a lot of restrictions on what kind of data is supplied (for example, there is no way to get any data about value distribution in a non-indexed column)
* There was little control of the statistics. There was no way to "pin" current statistic values, or provide some values on your own, etc.

Engine-independent table statistics lift these limitations.

* Statistics are stored in regular tables in the `mysql` database.
  * it is possible for a DBA to read and update the values.
* More data is collected/used.

[Histogram-based statistics](histogram-based-statistics.md) are a subset of engine-independent table statistics that can improve the query plan chosen by the optimizer in certain situations.

Statistics are stored in three tables, [mysql.table\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-table_stats-table.md), [mysql.column\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-column_stats-table.md) and [mysql.index\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-index_stats-table.md).

Use or update of data from these tables is controlled by [use\_stat\_tables](../../system-variables/server-system-variables.md#use_stat_tables) variable. Possible values are listed below:

| Value                         | Meaning                                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 'never'                       | The optimizer doesn't use data from statistics tables.                                                                                                                          |
| 'complementary'               | The optimizer uses data from statistics tables if the same kind of data is not provided by the storage engine.                                                                  |
| 'preferably'                  | Prefer the data from statistics tables, if it's not available there, use the data from the storage engine.                                                                      |
| 'complementary\_for\_queries' | Same as complementary, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md)).       |
| 'preferably\_for\_queries'    | Same as preferably, but for queries only (to avoid needlessly collecting for [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md)). Default. |

## Collecting Statistics with the ANALYZE TABLE Statement

Engine-independent statistics are collected by doing full table and full index scans, and this process can be quite expensive.

The [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement can be used to collect table statistics. However, simply running `ANALYZE TABLE table_name` does not collect engine-independent (or histogram) statistics by default.

When the [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement is executed, MariaDB makes a call to the table's storage engine, and the storage engine collects its own statistics for the table. The specific behavior depends on the storage engine. For the default [InnoDB](../../../../server-usage/storage-engines/innodb/) storage engine, see [InnoDB Persistent Statistics](innodb-persistent-statistics.md) for more information.

[ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) may also collect engine-independent statistics for the table. The specific behavior depends on the value of the [use\_stat\_tables](../../system-variables/server-system-variables.md#use_stat_tables) system variable. Engine-independent statistics will only be collected if one of the following is true:

* The [use\_stat\_tables](../../system-variables/server-system-variables.md#use_stat_tables) system variable is set to `complementary` or `preferably`.
* The [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement includes the `PERSISTENT FOR` clause.

The [use\_stat\_tables](../../system-variables/server-system-variables.md#use_stat_tables) system variable is set to `preferably_for_queries` by default. With this value, engine-independent statistics are used by default if available, but they are not collected by default. If you want to use engine-independent statistics with the default configuration, then you will have to collect them by executing the [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement and by specifying the `PERSISTENT FOR` clause. It is recommended to collect engine-independent statistics on as-needed basis, so typically one will not have engine-independent statistics for all indexes/all columns.

When to collect statistics is very dependent on the dataset. If data changes frequently it may be necessary to collect statistics more frequently, and the benefits may be very noticeable (see [This one trick can make MariaDB 30x faster!](https://mariadb.org/mariadb-30x-faster/)). If the data distribution is relatively static, the costs of collecting may outweigh any benefits.

### Collecting Statistics for Specific Columns or Indexes

The syntax for the [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement has been extended with the `PERSISTENT FOR` clause. This clause allows one to collect engine-independent statistics only for particular columns or indexes. This clause also allows one to collect engine-independent statistics, regardless of the value of the [use\_stat\_tables](../../system-variables/server-system-variables.md#use_stat_tables) system variable. For example:

```sql
ANALYZE TABLE table_name PERSISTENT FOR ALL;
```

Statistics for columns using the [BLOB](../../../../reference/data-types/string-data-types/blob.md) and [TEXT](../../../../reference/data-types/string-data-types/text.md) data types are not collected. If a column using one of these types is explicitly specified, then a warning is returned.

### Examples of Statistics Collection

```sql
-- update all engine-independent statistics for all columns and indexes
ANALYZE TABLE tbl PERSISTENT FOR ALL;

-- update specific columns and indexes:
ANALYZE TABLE tbl PERSISTENT FOR COLUMNS (col1,col2,...) INDEXES (idx1,idx2,...);

-- empty lists are allowed:
ANALYZE TABLE tbl PERSISTENT FOR COLUMNS (col1,col2,...) INDEXES ();
ANALYZE TABLE tbl PERSISTENT FOR COLUMNS () INDEXES (idx1,idx2,...);

-- the following will only update mysql.table_stats fields:
ANALYZE TABLE tbl PERSISTENT FOR COLUMNS () INDEXES ();

-- when use_stat_tables is set to 'COMPLEMENTARY' or 'PREFERABLY', 
-- a simple ANALYZE TABLE  collects engine-independent statistics for all columns and indexes.
SET SESSION use_stat_tables='COMPLEMENTARY';
ANALYZE TABLE tbl;
```

## Manual Updates to Statistics Tables

Statistics are stored in three tables, [mysql.table\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-table_stats-table.md), [mysql.column\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-column_stats-table.md) and [mysql.index\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-index_stats-table.md).

It is possible to update statistics tables manually. One should modify the table(s) with regular [INSERT](../../../../reference/sql-statements/data-manipulation/inserting-loading-data/insert.md)/[UPDATE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/update.md)/[DELETE](../../../../reference/sql-statements/data-manipulation/changing-deleting-data/delete.md) statements. Statistics data will be re-read when the tables are re-opened. One way to force all tables to be re-opened is to issue [FLUSH TABLES](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) command.

A few scenarios where one might need to update statistics tables manually:

* Deleting the statistics. Currently, the [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) command will collect the statistics, but there is no special command to delete statistics.
* Running `ANALYZE` on a different server. To collect engine-independent statistics ANALYZE TABLE does a full table scan, which can put too much load on the server. It is possible to run ANALYZE on the slave, and then take the data from statistics tables on the slave and apply it on the master.
* In some cases, knowledge of the database allows one to compute statistics manually in a more efficient way than `ANALYZE` does. One can compute the statistics manually and put it into the database.

## See Also

* [Index Statistics](../../optimization-and-indexes/index-statistics.md)
* [InnoDB Persistent Statistics](innodb-persistent-statistics.md)
* [Histogram-based Statistics](histogram-based-statistics.md)
* [JSON histograms](https://mariadb.org/10-7-preview-feature-json-histograms/) (mariadb.org blog)
* [Improving MariaDB’s optimizer with better selectivity estimates - Sergey Petrunia - Server Fest 2021](https://www.youtube.com/watch?v=bsl7Fis0onE) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
