# MariaDB Features Not Available in SQL Server

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

Some MariaDB features are not available in SQL Server.

At first glance, it is not important to know about those features to migrate from SQL Server to MariaDB. However, this is not the case. Using MariaDB features that are not in SQL Server allows one to obtain more advantages from the migration, getting the most from MariaDB.

This page has a list of MariaDB features that are not supported in SQL Server. The list is not exhaustive.

## Plugin Architecture

* [Storage engines](../../../../server-usage/storage-engines/).
* [Authentication plugins](../../../../reference/plugins/authentication-plugins/).
* [Encryption plugins](../../../../security/securing-mariadb/encryption/data-at-rest-encryption/key-management-and-encryption-plugins/).
* [ColumnStore](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/rBEU9juWLfTDcdwF3Q14/) is a columnar storage engine designed to scale horizontally. It runs on a specific edition of MariaDB, so currently it cannot be used in combination with other engines.

## SQL

* The [sql\_mode](../../../variables-and-modes/sql_mode.md) variable determines in which cases an SQL statement should fail with an error, and in which cases it should succeed with a warning even if it is not entirely correct. For example, when a statement tries to insert a string in a column which is not big enough to contain it, it could fail, or it could insert a truncated string and emit a warning. It is a tradeoff between reliability and flexibility.
  * [SQL\_MODE=MSSQL](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modemssql) allows one to use a small subset of SQL Server proprietary syntax.
* The [CREATE ... IF EXISTS, CREATE OR REPLACE, DROP ... IF NOT EXISTS](syntax-differences-between-mariadb-and-sql-server.md#if-exists-if-not-exists-or-replace) options are supported for most [DDL statements](../../../../reference/sql-statements/data-definition/).
* [SHOW](syntax-differences-between-mariadb-and-sql-server.md#show-statements) statements.
* [SHOW CREATE](syntax-differences-between-mariadb-and-sql-server.md#show-create-statements) statements.
* [SHOW PROCESSLIST](../../../../reference/sql-statements/administrative-sql-statements/show/show-processlist.md) and [PERFORMANCE\_SCHEMA THREAD table](../../../../reference/system-tables/performance-schema/performance-schema-tables/performance-schema-threads-table.md) provide much richer information, compared to SQL Server `sp_who()` and `sp_who2()` procedures.
* [CHECKSUM TABLE](../../../../reference/sql-statements/table-statements/checksum-table.md) statement.
* [PL/SQL support](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle) (only for stored procedures and stored functions).
* Row constructors.
* `BEFORE` [triggers](../../../../server-usage/triggers-events/triggers/).
* [HANDLER](../../../../reference/sql-structure/nosql/handler/handler-commands.md) statements, to scroll table rows ordered by an index or in their physical order.
* [DO](../../../../reference/sql-statements/stored-routine-statements/do.md) statement, to call functions without returning a result set.
* [BENCHMARK()](../../../../reference/sql-functions/secondary-functions/information-functions/benchmark.md) function, to measure the speed of an SQL expression.

See also [Syntax Differences between MariaDB and SQL Server](syntax-differences-between-mariadb-and-sql-server.md).

## Types

* [Character sets and collations](../../../../reference/data-types/string-data-types/character-sets/) don't depend on column type. They can be set globally, or at database, table or column level.
* Columns may use non-constant expressions as the [DEFAULT](../../../../reference/sql-statements/data-definition/create/create-table.md#default-column-option) value. [TIMESTAMP](../../../../reference/data-types/date-and-time-data-types/timestamp.md) columns may have a `DEFAULT` value.
* [UNSIGNED](../../../../reference/data-types/numeric-data-types/numeric-data-type-overview.md#signed-unsigned-and-zerofill) numeric types.
* [Dynamic columns](../../../../reference/sql-structure/nosql/dynamic-columns.md) (note that JSON is usually preferred to this feature).

See also [SQL Server and MariaDB Types Comparison](sql-server-and-mariadb-types-comparison.md).

### JSON

For compatibility with some other database systems, MariaDB supports the [JSON](../../../../reference/data-types/string-data-types/json.md) pseudo-type. However, it is just an alias for:

`LONGTEXT CHECK (JSON_VALID(column_name))`

[JSON\_VALID()](../../../../reference/sql-functions/special-functions/json-functions/json_valid.md) is the MariaDB equivalent of SQL Server's `ISJSON()`.

## Features

* [Flashback](../../../server-monitoring-logs/binary-log/flashback.md) functionality allows one to "undo" the changes that happened after a certain point in time.
* [Partitioned tables](../../../../server-usage/partitioning-tables/) support the following features:
  * Tables can be partitioned based on [multiple columns](../../../../server-usage/partitioning-tables/partitioning-types/range-columns-and-list-columns-partitioning-types.md).
  * Several [partitioning types](../../../../server-usage/partitioning-tables/partitioning-overview.md#partitioning-types) are available.
  * Subpartitions.
* [Progress reporting](https://app.gitbook.com/s/WCInJQ9cmGjq1lsTG91E/development-articles/mariadb-internals/using-mariadb-with-your-programs-api/progress-reporting) for some typically expensive statements.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
