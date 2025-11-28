# What's New in MariaDB Enterprise Server 10.6?

{% include "../../.gitbook/includes/latest-es-10.6.md" %}

MariaDB Enterprise Server 10.6 introduces the new features listed below.

## Atomic DDL

DDL (Data Definition Language) statements are now atomic operations. If the DDL statement is not fully successful, the operation will be rolled back. When the server crashes or is killed in the middle of a DDL statement, the operation is rolled back during crash recovery when the server is restarted.

During crash recovery, the server uses the DDL log to determine if an operation needs to be rolled back. When the [binary log](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/data-types/string-data-types/binary) is enabled, the crash recovery process ensures that the successful operations are written to the binary log and that the unsuccessful operations are not.

By default, the DDL log is at `ddl-recovery.log` in the [datadir](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/server-system-variables#datadir). When DDL statements are being executed, the DDL log is synchronized to disk very frequently. If you want to configure a custom path for the DDL log, the [log-ddl-recovery](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/starting-and-stopping-mariadb/mariadbd-options) option can be used.

As of this release, the following storage engines fully support atomic DDL:

* [Aria](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/aria)
* [InnoDB](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/innodb)
* [MyISAM](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/myisam-storage-engine)
* [MyRocks](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/storage-engines/myrocks)

## SKIP LOCKED

[SELECT \[ FOR UPDATE | LOCK IN SHARED MODE \] .. SKIP LOCKED](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) ignores already-locked rows.

One use case for this feature is within applications that sell a limited resource, such as ticketing, rentals, or seat-based sales. In these applications, you need a way to display only the available inventory. This can be accomplished by querying available inventory and skipping locked rows.

```sql
SELECT *
FROM ticketing
WHERE claimed = 0 AND section = 'B'
ORDER BY row DESC
LIMIT 10
FOR UPDATE SKIP LOCKED;
```

## Enterprise Audit Object Filters

[MariaDB Enterprise Audit](https://mariadb.com/resources/blog/mariadb-enterprise-audit-the-new-plugin) allows database-specific and table-specific filters.

For example:

```json
{
  "connect_event" : "ALL",
  "table_event" : ["READ","WRITE",{"ignore_tables" : "mysql.*"}],
  "query_event" : ["DDL",{"tables" : "test.t2"}]
}
```

## JSON\_TABLE

[JSON\_TABLE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) returns a table from JSON data.

Queryable rows and columns are produced based on the JSON input, but are not stored in a table on disk. Column mappings are defined in a JSON path expression.

Prior to this release, the [JSON\_VALUE()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_value) and [JSON\_QUERY()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_query) functions could be used to retrieve values from JSON data on a per-column basis.

With `JSON_TABLE()`:

* JSON data can `JOIN` with existing tables.
* A table can be created from JSON data using [CREATE TABLE .. AS SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/create/create-table) against a `JSON_TABLE()`.
* [NESTED PATH](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_table) enables extraction of nested data from JSON arrays and objects.

## Sys Schema

sys schema provides a set of views, functions, and stored procedures to aid DBA analysis of the [Performance Schema](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/system-tables/performance-schema).

## OFFSET Syntax

Additional syntax is supported for [SELECT .. OFFSET](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select)

`OFFSET start { ROW | ROWS } FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES }` is an alternative to `LIMIT .. OFFSET`

The `WITH TIES` option requires the use of `ORDER BY` and allows the number of rows to exceed the `FETCH` count to ensure that the final row in the chunk includes any additional rows that have the same values in the `ORDER BY` fields (eliminating the need to fetch the next chunk to check for spill-over).

* For example, the following query can return more than 10 rows if there are more `username` rows that match the `username` in the 10th row (the order of the `purchase` values within the complete set of each username's records is non-deterministic):

```sql
SELECT username, purchase
FROM user_purchases
ORDER BY username
OFFSET 305 ROWS
FETCH NEXT 10 ROW WITH TIES;
```

* For example, the following query specifies `ONLY` instead of `WITH TIES`, so the query can't return more than 10 rows:

```sql
SELECT username, purchase
FROM user_purchases
ORDER BY username, purchase
OFFSET 0 ROWS
FETCH NEXT 10 ROWS ONLY;
```

## Enhanced Consistency for Semi-sync Replication

When [rpl\_semi\_sync\_slave\_enabled=ON](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/semisynchronous-replication#rpl_semi_sync_slave_enabled), consistency is guaranteed for a Primary server in an HA (Primary/Replica) topology when using semi-synchronous replication.

Prior to this release, when using semi-synchronous replication, if a Primary crashed before sending a transaction to the Replica, on restart the Primary could recover incomplete InnoDB transactions when rejoining as a Replica.

With this release, when using semi-synchronous replication and with `rpl_semi_sync_slave_enabled=ON`, incomplete transactions will be rolled-back on the Replica, ensuring the new Primary (former Replica) and new Replica (former Primary) remain in sync.

## Enhanced Compatibility with Oracle

Expanded compatibility with Oracle through new functions:

* Added function [ADD\_MONTHS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/date-time-functions/add_months)
* Added function [ROWNUM()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/rownum)
* Added function [SYS\_GUID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/miscellaneous-functions/sys_guid)
* Added function [TO\_CHAR()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/string-functions/to_char)

Expanded compatibility with Oracle through [sql\_mode=ORACLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/variables-and-modes/sql_mode) enhancements:

* With `sql_mode=ORACLE` added `MINUS` as an alias to `EXCEPT`
* With `sql_mode=ORACLE` improved `SYSDATE` to allow use without parenthesis.
* With `sql_mode=ORACLE` supports a [rownum](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/rownum) pseudo-column name as an alias for the [ROWNUM()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/secondary-functions/information-functions/rownum) function.
* With `sql_mode=ORACLE` subqueries in a `FROM` clause do not require the AS clause.

## Enhanced Compatibility with Sybase SQL Anywhere

Enhanced compatibility with Sybase SQL Anywhere through \[sql\_mode=EXTENDED\_ALIASES]

* With `sql_mode=EXTENDED_ALIASES`, alias resolution and use of column aliases in the SQL [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) list and `WHERE` clause.
* With `sql_mode=EXTENDED_ALIASES`, support use of an alias in the [SELECT](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-manipulation/selecting-data/select) list before the alias is defined.
* With `sql_mode=EXTENDED_ALIASES`, if the same label is used for an alias and a column, the alias is used.

## Backported Features

[MariaDB Enterprise Server 10.6.9-5](10.6.9-5.md)

* The UUID data type has been backported for more efficient storage of UUID values.

[MariaDB Enterprise Server 10.6.11-6](10.6.11-6.md)

* The new [slave\_max\_statement\_time system variable](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/ha-and-performance/standard-replication/replication-and-binary-log-system-variables) is available to set the maximum execution time for queries on replica nodes.
* To simplify maintenance, the [ALTER TABLE statement](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/data-definition/alter/alter-table) supports new clauses to convert tables to partitions, and partitions to tables

[MariaDB Enterprise Server 10.6.12-7](10.6.12-7.md)

* In previous releases, the number of undo logs was configurable before InnoDB was initialized. With this release, the number of undo logs can also be configured after install

[MariaDB Enterprise Server 10.6.15-10](10.6.15-10.md)

* [JSON\_OVERLAPS()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_overlaps) has been backported
* [JSON\_SCHEMA\_VALID()](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-functions/special-functions/json-functions/json_schema_valid) has been backported

[MariaDB Enterprise Server 10.6.16-11](10.6.16-11.md)

* A new view `sys.privileges_by_table_by_level` in the sys schema, to show privileges granted to a table on a global, schema, or table level
* Option s3\_debug can now be changed without the need to restart the server
* New Time Zone Options `%Z` and `%z` for DATE\_FORMAT
* Server Audit Log with Milliseconds Precision Timestamps

## Available Versions

* [MariaDB Enterprise Server 10.6.23-19](10.6.23-19.md)
* [MariaDB Enterprise Server 10.6.22-18](10.6.22-18.md)
* [MariaDB Enterprise Server 10.6.21-17](10.6.21-17.md)
* [MariaDB Enterprise Server 10.6.20-16](10.6.20-16.md)
* [MariaDB Enterprise Server 10.6.19-15](10.6.19-15.md)
* [MariaDB Enterprise Server 10.6.18-14](10.6.18-14.md)
* [MariaDB Enterprise Server 10.6.17-13](10.6.17-13.md)
* [MariaDB Enterprise Server 10.6.17-12](10.6.17-12.md)
* [MariaDB Enterprise Server 10.6.16-11](10.6.16-11.md)
* [MariaDB Enterprise Server 10.6.15-10](10.6.15-10.md)
* [MariaDB Enterprise Server 10.6.14-9](10.6.14-9.md)
* [MariaDB Enterprise Server 10.6.12-8](10.6.12-8.md)
* [MariaDB Enterprise Server 10.6.12-7](10.6.12-7.md)
* [MariaDB Enterprise Server 10.6.11-6](10.6.11-6.md)
* [MariaDB Enterprise Server 10.6.9-5](10.6.9-5.md)
* [MariaDB Enterprise Server 10.6.8-4](10.6.8-4.md)
* [MariaDB Enterprise Server 10.6.7-3](10.6.7-3.md)
* [MariaDB Enterprise Server 10.6.5-2](10.6.5-2.md)
* [MariaDB Enterprise Server 10.6.4-1](10.6.4-1.md)

See also: [All MariaDB Enterprise Releases](../all-releases.md)

## Installation Instructions <a href="#installation-instructions" id="installation-instructions"></a>

* [Deploy MariaDB Enterprise with Repositories](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/mariadb-package-repository-setup-and-usage)
* [Deploy MariaDB Enterprise with Package Tarballs](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-mariadb/binary-packages/package-tarballs)
* [Deploy MariaDB Enterprise with Docker](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/automated-mariadb-deployment-and-administration/docker-and-mariadb/deploy-mariadb-enterprise-server-with-docker)

## Upgrade Instructions <a href="#upgrade-instructions" id="upgrade-instructions"></a>

* [Upgrade to MariaDB Enterprise Server 10.6](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/server-management/install-and-upgrade-mariadb/installing-enterprise-server/mariadb-enterprise-server-upgrade-paths/mariadb-enterprise-server-10.6/upgrade-to-mariadb-enterprise-server-10.6)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formid="4316" formId="4316" %}
