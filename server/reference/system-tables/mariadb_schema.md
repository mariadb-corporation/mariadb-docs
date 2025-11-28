---
description: >-
  This system database contains crucial metadata about the server, including
  information schema, statistics, and optimizer hints, for internal operations.
---

# mariadb\_schema

{% hint style="info" %}
`mariadb_schema` was introduced in [MariaDB 10.3.24](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-3-series/mariadb-10324-release-notes), [MariaDB 10.4.14](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-10-4-series/mariadb-10414-release-notes) and [MariaDB 10.5.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-10-5-series/mariadb-1055-release-notes).
{% endhint %}

`mariadb_schema` is a data type qualifier that allows one to create MariaDB native date types in an [SQL\_MODE](../../server-management/variables-and-modes/sql_mode.md) that has conflicting data type translations.

In [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), if you create a table with the [DATE](../data-types/date-and-time-data-types/date.md) type, it actually creates a [DATETIME](../data-types/date-and-time-data-types/datetime.md#oracle-mode) column to match what an Oracle user is expecting. To be able to create a MariaDB `DATE` in Oracle mode, you would have to use `mariadb_schema`:

```sql
CREATE TABLE t1 (d mariadb_schema.DATE);
```

`mariadb_schema` is also shown if you create a table with `DATE` in MariaDB native mode and then do a [SHOW CREATE TABLE](../sql-statements/administrative-sql-statements/show/show-create-table.md) in `ORACLE` mode:

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" mariadb_schema.DATE DEFAULT NULL
) |
+-------+--------------------------------------------------------------+
```

When the server sees the `mariadb_schema` qualifier, it disables sql\_mode-specific data type translation and interprets the data type literally, so for example `mariadb_schema.DATE` is interpreted as the traditional MariaDB `DATE` data type, no matter what the current SQL mode is.

The `mariadb_schema` prefix is displayed only when the data type name would be ambiguous otherwise. The prefix is displayed together with MariaDB `DATE` when [SHOW CREATE TABLE](../sql-statements/administrative-sql-statements/show/show-create-table.md) is executed in [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle). The prefix is not displayed when [SHOW CREATE TABLE](../sql-statements/administrative-sql-statements/show/show-create-table.md) is executed in SQL\_MODE=DEFAULT, or when a non-ambiguous data type is displayed.

{% hint style="info" %}
The `mariadb_schema` prefix can be used with any data type, including non-ambiguous ones.
{% endhint %}

```sql
CREATE OR REPLACE TABLE t1 (a mariadb_schema.INT);
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------+
| Table | Create Table                                     |
+-------+--------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "a" INT(11) DEFAULT NULL
) |
+-------+--------------------------------------------------+
```

The `mariadb_schema` prefix is only used in the following case:

* For a MariaDB native [DATE](../data-types/date-and-time-data-types/date.md) type when running [SHOW CREATE TABLE](../sql-statements/administrative-sql-statements/show/show-create-table.md) in [Oracle mode](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle).

## History

When running with [SQL\_MODE=ORACLE](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/about/compatibility-and-differences/sql_modeoracle), MariaDB server translates the data type `DATE` to `DATETIME`, for better Oracle compatibility:

```sql
SET SQL_mode=ORACLE;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SHOW CREATE TABLE t1;
+-------+---------------------------------------------------+
| Table | Create Table                                      |
+-------+---------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" datetime DEFAULT NULL
) |
+-------+---------------------------------------------------+
```

Notice, `DATE` was translated to `DATETIME`.

This translation may cause some ambiguity. Suppose you create a table with a column of the traditional MariaDB `DATE` data type using the default SQL mode, but then switche to `SQL_MODE=ORACLE` and run a [SHOW CREATE TABLE](../sql-statements/administrative-sql-statements/show/show-create-table.md) statement:

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
```

Before `mariadb_schema` was introduced, the above script displayed:

```sql
CREATE TABLE "t1" (
  "d" DATE DEFAULT NULL
);
```

This had two problems:

* It was confusing for the reader: its not clear if it is the traditional MariaDB `DATE`, or is it Oracle-alike date (which is actually `DATETIME`);
* It broke replication and caused data type mismatch on the master and on the slave (see [MDEV-19632](https://jira.mariadb.org/browse/MDEV-19632)).

To address this problem, starting from the mentioned versions, MariaDB uses the idea of qualified data types:

```sql
SET sql_mode=DEFAULT;
CREATE OR REPLACE TABLE t1 (
  d DATE
);
SET SQL_mode=ORACLE;
SHOW CREATE TABLE t1;
+-------+--------------------------------------------------------------+
| Table | Create Table                                                 |
+-------+--------------------------------------------------------------+
| t1    | CREATE TABLE "t1" (
  "d" mariadb_schema.DATE DEFAULT NULL
) |
+-------+--------------------------------------------------------------+
```

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
