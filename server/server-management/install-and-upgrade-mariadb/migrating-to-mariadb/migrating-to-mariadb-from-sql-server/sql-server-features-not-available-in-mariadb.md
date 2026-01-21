---
description: Features available in Microsoft SQL Server that aren't available in MariaDB.
---

# SQL Server Features Not Available in MariaDB

{% include "https://app.gitbook.com/s/GxVnu02ec8KJuFSxmB93/~/reusable/UQS8KgfG8jtpHBvT83fL/" %}

When planning a migration between different DBMSs, one of the most important aspects to consider is that the new database system will probably miss some features supported by the old one. This is not relevant for all users. The most widely used features are supported by most DBMSs. However, it is important to make a list of unsupported features and check which of them are currently used by applications. In most cases it is possible to implement such features on the application side, or simply stop using them.

This page has a list of SQL Server features that are not supported in MariaDB. The list is not exhaustive.

## Introduced in SQL Server versions older than 2016

* Full outer joins.
* `GROUP BY CUBE` syntax.
* `MERGE` statement.
* In MariaDB, indexes are always ascending. Defining them as `ASC` or `DESC` has no effect.
  * For single-column indexes, the performance difference between an `ORDER BY ... ASC` and `DESC` is negligible.
  * For multiple-column indexes, an index may be unusable for certain queries because `DESC` is not supported. In some cases, a [generated column](../../../../reference/sql-statements/data-definition/create/generated-columns.md) can be used to invert the order of an index (for example, the expression `0 - price` can be indexed to index the prices in a descending order).
* The [WITH](../../../../reference/sql-statements/data-manipulation/selecting-data/common-table-expressions/with.md) syntax is currently only supported for the `SELECT` statement.
* Filtered indexes (`CREATE INDEX ... WHERE`).
* Autonomous transactions.
* User-defined types.
* Rules.
* [Triggers](../../../../server-usage/triggers-events/triggers/) don't support the following features:
  * Triggers on DDL and login.
  * `INSTEAD OF` triggers.
  * The `DISABLE TRIGGER` syntax.
* [Cursors](../../../../reference/sql-statements/programmatic-compound-statements/programmatic-compound-statements-cursors/) advanced features.
  * Global cursors.
  * `DELETE ... CURRENT OF`, `UPDATE ... CURRENT OF` statements: MariaDB cursors are read-only.
  * Specifying a direction (MariaDB cursors can only advance by one row).
* Synonyms.
* Table variables.
* Queues.
* XML indexes, XML schema collection, XQuery.
* User access to system functionalities, for example:
  * Running system commands (`xp_cmdshell()`).
  * Sending emails (`sp_send_dbmail()`).
  * Sending HTTP requests.
* External languages, external libraries (MariaDB only supports procedural SQL and PL/SQL).
* Negative permissions (the `DENY` command).
* Snapshot replication. See [Provisioning a Slave](mariadb-replication-overview-for-sql-server-users.md#provisioning-a-slave).

## Introduced in SQL Server 2016

* Native data masking
* PolyBase (however, [MariaDB 10.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/what-is-mariadb-105) supports accessing Amazon S3 via the [S3 storage engine](../../../../server-usage/storage-engines/s3-storage-engine/) and several DBMSs via [CONNECT](../../../../server-usage/storage-engines/connect/))
* R and Python services
* ColumnStore indexes. MariaDB has a storage engine called [ColumnStore](../../../../architecture/topologies/columnstore-object-storage/), but this is a completely different feature.

## Introduced in SQL Server 2017

* Adaptive joins
* Graph SQL

## See Also

* [SQL Server Features Implemented Differently in MariaDB](sql-server-features-implemented-differently-in-mariadb.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
