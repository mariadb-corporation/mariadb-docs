# InnoDB Persistent Statistics

InnoDB statistics are stored on disk and are therefore persistent. Prior to [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0), InnoDB statistics were not stored on disk, meaning that on server restarts the statistics would need to be recalculated, which is both needless computation, as well as leading to inconsistent query plans.

There are a number of variables that control persistent statistics:

* [innodb\_stats\_persistent](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent) - when set (the default) enables InnoDB persistent statistics.
* [innodb\_stats\_auto\_recalc](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_auto_recalc) - when set (the default), persistent statistics are automatically recalculated when the table changes significantly (more than 10% of the rows)
* [innodb\_stats\_persistent\_sample\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages) - Number of index pages sampled (default 20) when estimating cardinality and statistics for indexed columns. Increasing this value will increases index statistics accuracy, but use more I/O resources when running [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md).

These settings can be overwritten on a per-table basis by use of the [STATS\_PERSISTENT](../../../../reference/sql-statements/data-definition/create/create-table.md#stats_persistent), [STATS\_AUTO\_RECALC](../../../../reference/sql-statements/data-definition/create/create-table.md#stats_auto_recalc) and [STATS\_SAMPLE\_PAGES](../../../../reference/sql-statements/data-definition/create/create-table.md#stats_sample_pages) clauses in a [CREATE TABLE](../../../../reference/sql-statements/data-definition/create/create-table.md) or [ALTER TABLE](../../../../reference/sql-statements/data-definition/alter/alter-table/) statement.

Details of the statistics are stored in two system tables in the [mysql database](https://mariadb.com/kb/en/the-mysql-database-table):

* [innodb\_table\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-innodb_table_stats.md)
* [innodb\_index\_stats](../../../../reference/system-tables/the-mysql-database-tables/mysql-innodb_index_stats.md)

The [ANALYZE TABLE](../../../../reference/sql-statements/table-statements/analyze-table.md) statement can be used to recalculate InnoDB statistics.

The [RENAME TABLE](../../../../reference/sql-statements/data-definition/rename-table.md) statement triggers a reload of the statistics.

**MariaDB starting with** [**10.11.12**](https://mariadb.com/kb/en/mariadb-101112-release-notes/)

Prior to [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10.11.12-release-notes), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-6-release-notes) and [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-8-series/mariadb-11-8-2-release-notes), [FLUSH TABLES](../../../../reference/sql-statements/administrative-sql-statements/flush-commands/flush.md) also caused InnoDB statistics to be reloaded. From [MariaDB 10.11.12](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-11-series/mariadb-10.11.12-release-notes), [MariaDB 11.4.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-4-series/mariadb-11-4-6-release-notes) and [MariaDB 11.8.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-11-8-series/mariadb-11-8-2-release-notes), this is no longer the case.

## See Also

* [Index Statistics](../../optimization-and-indexes/index-statistics.md)
* [Engine-independent Statistics](engine-independent-table-statistics.md)
* [Histogram-based Statistics](histogram-based-statistics.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
