# System-Versioned Tables

MariaDB supports temporal data tables in the form of system-versioning tables (allowing you to query and operate on historic data, discussed below), [application-time periods](application-time-periods.md) (allow you to query and operate on a temporal range of data), and [bitemporal tables](bitemporal-tables.md) (which combine both system-versioning and [application-time periods](application-time-periods.md)).

## System-Versioned Tables

System-versioned tables store the history of all changes, not only data which is currently applicable. This allows data analysis for any point in time, auditing of changes and comparison of data from different points in time. Typical uses cases are:

* Forensic analysis & legal requirements to store data for N years.
* Data analytics (retrospective, trends etc.), e.g. to get your staff information as of one year ago.
* Point-in-time recovery - recover a table state as of particular point in time.

System-versioned tables were first introduced in the SQL:2011 standard.

### Creating a System-Versioned Table

The [CREATE TABLE](../../sql-statements/data-definition/create/create-table.md) syntax has been extended to permit creating a system-versioned table. To be system-versioned, according to SQL:2011, a table must have two generated columns, a period, and a special table option clause:

```sql
CREATE TABLE t(
   x INT,
   start_timestamp TIMESTAMP(6) GENERATED ALWAYS AS ROW START,
   end_timestamp TIMESTAMP(6) GENERATED ALWAYS AS ROW END,
   PERIOD FOR SYSTEM_TIME(start_timestamp, end_timestamp)
) WITH SYSTEM VERSIONING;
```

In MariaDB, you can use a simplified syntax:

```sql
CREATE TABLE t (
   x INT
) WITH SYSTEM VERSIONING;
```

In the latter case, no extra columns will be created, and they won't clutter the output of, say, `SELECT * FROM t`. The versioning information will still be stored, and it can be accessed via the pseudo-columns `ROW_START` and `ROW_END`:

```sql
SELECT x, ROW_START, ROW_END FROM t;
```

### Adding or Removing System Versioning To/From a Table

An existing table can be [altered](../../sql-statements/data-definition/alter/alter-table/) to enable system versioning for it.

```sql
CREATE TABLE t(
  x INT
);
```

```sql
ALTER TABLE t ADD SYSTEM VERSIONING;
```

```sql
SHOW CREATE TABLE t\G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE `t` (
  `x` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 WITH SYSTEM VERSIONING
```

Similarly, system versioning can be removed from a table:

```sql
ALTER TABLE t DROP SYSTEM VERSIONING;
```

```sql
SHOW CREATE TABLE t\G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE `t` (
  `x` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

You can also add system versioning with all columns created explicitly:

```sql
ALTER TABLE t ADD COLUMN ts TIMESTAMP(6) GENERATED ALWAYS AS ROW START,
              ADD COLUMN te TIMESTAMP(6) GENERATED ALWAYS AS ROW END,
              ADD PERIOD FOR SYSTEM_TIME(ts, te),
              ADD SYSTEM VERSIONING;
```

```sql
SHOW CREATE TABLE t\G
*************************** 1. row ***************************
       Table: t
Create Table: CREATE TABLE `t` (
  `x` int(11) DEFAULT NULL,
  `ts` timestamp(6) GENERATED ALWAYS AS ROW START,
  `te` timestamp(6) GENERATED ALWAYS AS ROW END,
  PERIOD FOR SYSTEM_TIME (`ts`, `te`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 WITH SYSTEM VERSIONING
```

**MariaDB starting with** [**11.7**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/mariadb-11-7-rolling-releases/what-is-mariadb-117)

{% tabs %}
{% tab title="Current" %}
It is possible to convert a versioned table from implicit to explicit `row_start`/`row_end` columns. Note that, in order to do any `ALTER` on a system versioned table, [system\_versioning\_alter\_history](system-versioned-tables.md#system_versioning_alter_history) must be set to `KEEP`.

```sql
CREATE OR REPLACE TABLE t1 (x INT) WITH SYSTEM VERSIONING;

SET system_versioning_alter_history = keep;

ALTER TABLE t1 ADD COLUMN rs TIMESTAMP(6) AS ROW START, 
  ADD COLUMN re TIMESTAMP(6) AS ROW END, ADD PERIOD FOR SYSTEM_TIME (rs,re)
```
{% endtab %}

{% tab title="< 11.7" %}
It is **not** possible to convert a versioned table from implicit to explicit `row_start`/`row_end` columns. Doing so results in a duplicate row error:

```sql
CREATE OR REPLACE TABLE t1 (x INT) WITH SYSTEM VERSIONING;

SET system_versioning_alter_history = keep;

ALTER TABLE t1 ADD COLUMN rs TIMESTAMP(6) AS ROW START, 
  ADD COLUMN re TIMESTAMP(6) AS ROW END, ADD PERIOD FOR SYSTEM_TIME (rs,re);

ERROR 4134 (HY000): Duplicate ROW START column `rs`
```
{% endtab %}
{% endtabs %}

### Inserting Data

When data is inserted into a system-versioned table, it is given a _row\_start_ value of the current timestamp, and a _row\_end_ value of [FROM\_UNIXTIME](../../sql-functions/date-time-functions/from_unixtime.md) (`2147483647.999999`). The current timestamp can be adjusted by setting the [timestamp system variable](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp):

```sql
SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2022-10-24 23:09:38 |
+---------------------+
 
INSERT INTO t VALUES(1);
 
SET @@timestamp = UNIX_TIMESTAMP('2033-10-24');

INSERT INTO t VALUES(2);
 
SET @@timestamp = default;

INSERT INTO t VALUES(3);
 
SELECT a,row_start,row_end FROM t;
+------+----------------------------+----------------------------+
| a    | row_start                  | row_end                    |
+------+----------------------------+----------------------------+
|    1 | 2022-10-24 23:09:38.951347 | 2038-01-19 05:14:07.999999 |
|    2 | 2033-10-24 00:00:00.000000 | 2038-01-19 05:14:07.999999 |
|    3 | 2022-10-24 23:09:38.961857 | 2038-01-19 05:14:07.999999 |
+------+----------------------------+----------------------------+
```

### Querying Historical Data

#### `SELECT`

To query the historical data one uses the clause `FOR SYSTEM_TIME` directly after the table name (before the table alias, if any). SQL:2011 provides three syntactic extensions:

* `AS OF` is used to see the table as it was at a specific point in time in the past:

```sql
SELECT * FROM t FOR SYSTEM_TIME AS OF TIMESTAMP'2016-10-09 08:07:06';
```

* `BETWEEN start AND end` will show all rows that were visible at any point between two specified points in time. It works inclusively, a row visible exactly at start or exactly at end will be shown too.

```sql
SELECT * FROM t FOR SYSTEM_TIME BETWEEN (NOW() - INTERVAL 1 YEAR) AND NOW();
```

* `FROM start TO end` will also show all rows that were visible at any point between two specified points in time, including start, but excluding end.

```sql
SELECT * FROM t FOR SYSTEM_TIME FROM '2016-01-01 00:00:00' TO '2017-01-01 00:00:00';
```

Additionally, MariaDB implements a non-standard extension.

* `ALL` will show all rows, historical and current.

```sql
SELECT * FROM t FOR SYSTEM_TIME ALL;
```

{% tabs %}
{% tab title="Current" %}
If the `FOR SYSTEM_TIME` clause is not used, the table shows the _current_ data. This is usually the same as if you had specified `FOR SYSTEM_TIME AS OF CURRENT_TIMESTAMP`, unless you've adjusted the _row\_start_ value:

```sql
CREATE OR REPLACE TABLE t (a int) WITH SYSTEM VERSIONING;

SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2022-10-24 23:43:37 |
+---------------------+

INSERT INTO t VALUES (1);

SET @@timestamp = UNIX_TIMESTAMP('2033-03-03');

INSERT INTO t VALUES (2);

DELETE FROM t;

SET @@timestamp = default;


SELECT a, row_start, row_end FROM t FOR SYSTEM_TIME ALL;
+------+----------------------------+----------------------------+
| a    | row_start                  | row_end                    |
+------+----------------------------+----------------------------+
|    1 | 2022-10-24 23:43:37.192725 | 2033-03-03 00:00:00.000000 |
|    2 | 2033-03-03 00:00:00.000000 | 2033-03-03 00:00:00.000000 |
+------+----------------------------+----------------------------+
2 rows in set (0.000 sec)


SELECT a, row_start, row_end FROM t FOR SYSTEM_TIME AS OF CURRENT_TIMESTAMP;
+------+----------------------------+----------------------------+
| a    | row_start                  | row_end                    |
+------+----------------------------+----------------------------+
|    1 | 2022-10-24 23:43:37.192725 | 2033-03-03 00:00:00.000000 |
+------+----------------------------+----------------------------+
1 row in set (0.000 sec)


SELECT a, row_start, row_end FROM t;
Empty set (0.001 sec)
```
{% endtab %}

{% tab title="< 10.11" %}
If the `FOR SYSTEM_TIME` clause is not used, the table shows the _current_ data. This is usually the same as if you had specified `FOR SYSTEM_TIME AS OF CURRENT_TIMESTAMP`, unless you've adjusted the _row\_start_ value (only possible by setting the [secure\_timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp) variable):

```sql
CREATE OR REPLACE TABLE t (a int) WITH SYSTEM VERSIONING;

SELECT NOW();
+---------------------+
| NOW()               |
+---------------------+
| 2022-10-24 23:43:37 |
+---------------------+

INSERT INTO t VALUES (1);

SET @@timestamp = UNIX_TIMESTAMP('2033-03-03');

INSERT INTO t VALUES (2);

DELETE FROM t;

SET @@timestamp = default;


SELECT a, row_start, row_end FROM t FOR SYSTEM_TIME ALL;
+------+----------------------------+----------------------------+
| a    | row_start                  | row_end                    |
+------+----------------------------+----------------------------+
|    1 | 2022-10-24 23:43:37.192725 | 2033-03-03 00:00:00.000000 |
|    2 | 2033-03-03 00:00:00.000000 | 2033-03-03 00:00:00.000000 |
+------+----------------------------+----------------------------+
2 rows in set (0.000 sec)


SELECT a, row_start, row_end FROM t FOR SYSTEM_TIME AS OF CURRENT_TIMESTAMP;
+------+----------------------------+----------------------------+
| a    | row_start                  | row_end                    |
+------+----------------------------+----------------------------+
|    1 | 2022-10-24 23:43:37.192725 | 2033-03-03 00:00:00.000000 |
+------+----------------------------+----------------------------+
1 row in set (0.000 sec)


SELECT a, row_start, row_end FROM t;
Empty set (0.001 sec)
```
{% endtab %}
{% endtabs %}

#### Views and Subqueries

When a system-versioned table is used in a view or in a subquery in the from clause, `FOR SYSTEM_TIME` can be used directly in the view or subquery body, or (non-standard) applied to the whole view when it's being used in a `SELECT`:

```sql
CREATE VIEW v1 AS SELECT * FROM t FOR SYSTEM_TIME AS OF TIMESTAMP'2016-10-09 08:07:06';
```

Or:

```sql
CREATE VIEW v1 AS SELECT * FROM t;
SELECT * FROM v1 FOR SYSTEM_TIME AS OF TIMESTAMP'2016-10-09 08:07:06';
```

#### Use in Replication and Binary Logs

Tables that use system-versioning implicitly add the `row_end` column to the Primary Key. While this is generally not an issue for most use cases, it can lead to problems when re-applying write statements from the binary log or in replication environments, where a primary retries an SQL statement on the replica.

Specifically, these writes include a value on the `row_end` column containing the timestamp from when the write was initially made. The re-occurrence of the Primary Key with the old system-versioning columns raises an error due to the duplication.

To mitigate this with MariaDB Replication, set the [secure\_timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp) system variable to `YES` on the replica. When set, the replica uses its own system clock when applying to the row log, meaning that the primary can retry as many times as needed without causing a conflict. The retries generate new historical rows with new values for the `row_start` and `row_end` columns.

### Transaction-Precise History in InnoDB

A point in time when a row was inserted or deleted does not necessarily mean that a change became visible at the same moment. With transactional tables, a row might have been inserted in a long transaction, and became visible hours after it was inserted.

For some applications — for example, when doing data analytics on one-year-old data — this distinction does not matter much. For others — forensic analysis — it might be crucial.

MariaDB supports transaction-precise history (only for the [InnoDB storage engine](../../../server-usage/storage-engines/innodb/)) that allows seeing the data exactly as it would've been seen by a new connection doing a `SELECT` at the specified point in time — rows inserted _before_ that point, but committed _after_ will not be shown.

To use transaction-precise history, InnoDB needs to remember not timestamps, but transaction identifier per row. This is done by creating generated columns as `BIGINT UNSIGNED`, not `TIMESTAMP(6)`:

```sql
CREATE TABLE t(
   x INT,
   start_trxid BIGINT UNSIGNED GENERATED ALWAYS AS ROW START,
   end_trxid BIGINT UNSIGNED GENERATED ALWAYS AS ROW END,
   PERIOD FOR SYSTEM_TIME(start_trxid, end_trxid)
) WITH SYSTEM VERSIONING;
```

These columns must be specified explicitly, but they can be made [INVISIBLE](../../sql-statements/data-definition/create/invisible-columns.md) to avoid cluttering `SELECT *` output.

Note that if you are using an engine that does not support system versioning with transaction ids, you will get an error like "`start_trxid` must be of type `TIMESTAMP(6)` for system-versioned table `t`".

When one uses transaction-precise history, one can optionally use transaction identifiers in the `FOR SYSTEM_TIME` clause:

```sql
SELECT * FROM t FOR SYSTEM_TIME AS OF TRANSACTION 12345;
```

This shows the data, exactly as it was seen by the transaction with the identifier 12345.

Data for this feature is stored in the [mysql.transaction\_registry table](../../system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md).

### Storing the History Separately

When the history is stored together with the current data, it increases the size of the table, so current data queries — table scans and index searches — will take more time, because they will need to skip over historical data. If most queries on that table use only current data, it might make sense to store the history separately, to reduce the overhead from versioning.

This is done by partitioning the table by `SYSTEM_TIME`. Because of the [partition pruning](../../../server-usage/partitioning-tables/partition-pruning-and-selection.md) optimization, all current data queries will only access one partition, the one that stores current data.

This example shows how to create such a partitioned table:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME (
    PARTITION p_hist HISTORY,
    PARTITION p_cur CURRENT
  );
```

In this example, all history will be stored in the partition `p_hist` while all current data will be in the partition `p_cur`. The table must have exactly one current partition and at least one historical partition.

Partitioning by `SYSTEM_TIME` also supports automatic partition rotation. You can rotate historical partitions by time or by size. This example shows how to rotate partitions by size:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME LIMIT 100000 (
    PARTITION p0 HISTORY,
    PARTITION p1 HISTORY,
    PARTITION pcur CURRENT
  );
```

MariaDB starts writing history rows into partition `p0`, and at the end of the statement that wrote the 100000th row, MariaDB will switch to partition `p1`. There are only two historical partitions, so when `p1` overflows, MariaDB will issue a warning, but will continue writing into it.

Similarly, one can rotate partitions by time:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME INTERVAL 1 WEEK (
    PARTITION p0 HISTORY,
    PARTITION p1 HISTORY,
    PARTITION p2 HISTORY,
    PARTITION pcur CURRENT
  );
```

This means that the history for the first week after the table was created will be stored in `p0`. The history for the second week — in `p1`, and all later history will go into `p2`. One can see the exact rotation time for each partition in the [INFORMATION\_SCHEMA.PARTITIONS](../../system-tables/information-schema/information-schema-tables/information-schema-partitions-table.md) table.

It is possible to combine partitioning by `SYSTEM_TIME` and subpartitions:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME
    SUBPARTITION BY KEY (x)
    SUBPARTITIONS 4 (
    PARTITION ph HISTORY,
    PARTITION pc CURRENT
  );
```

#### Default Partitions

{% hint style="info" %}
Default Partitions are available from MariaDB 10.5.
{% endhint %}

Since partitioning by current and historical data is such a typical use case, it is possible to use a simplified statement to do so. Instead of the following statement:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING 
  PARTITION BY SYSTEM_TIME (
    PARTITION p0 HISTORY,  
    PARTITION pn CURRENT 
);
```

You can use:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING 
  PARTITION BY SYSTEM_TIME;
```

You can also specify the number of partitions, which is useful if you want to rotate history by time, for example:

```sql
CREATE TABLE t (x INT) WITH SYSTEM VERSIONING 
  PARTITION BY SYSTEM_TIME 
    INTERVAL 1 MONTH 
    PARTITIONS 12;
```

Specifying the number of partitions without specifying a rotation condition results in a warning:

```sql
CREATE OR REPLACE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME PARTITIONS 12;
Query OK, 0 rows affected, 1 warning (0.518 sec)

Warning (Code 4115): Maybe missing parameters: no rotation condition for multiple HISTORY partitions.
```

While specifying only one partition results in an error:

```sql
CREATE OR REPLACE TABLE t (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME PARTITIONS 1;
ERROR 4128 (HY000): Wrong partitions for `t`: must have at least one HISTORY and exactly one last CURRENT
```

#### Automatically Creating Partitions

{% hint style="info" %}
Creating partitions with `AUTO` is available from MariaDB 10.9.1.
{% endhint %}

**T**he `AUTO` keyword can be used to automatically create history partitions:

```sql
CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING
    PARTITION BY SYSTEM_TIME INTERVAL 1 HOUR AUTO;

CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING
   PARTITION BY SYSTEM_TIME INTERVAL 1 MONTH
   STARTS '2021-01-01 00:00:00' AUTO PARTITIONS 12;

CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME LIMIT 1000 AUTO;
```

Or with explicit partitions:

```sql
CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME INTERVAL 1 HOUR AUTO
  (PARTITION p0 HISTORY, PARTITION pn CURRENT);
```

To disable or enable auto-creation, one can use `ALTER TABLE` by adding or removing `AUTO` from the partitioning specification:

```sql
CREATE TABLE t1 (x INT) WITH SYSTEM VERSIONING
  PARTITION BY SYSTEM_TIME INTERVAL 1 HOUR AUTO;

# Disables auto-creation:
ALTER TABLE t1 PARTITION BY SYSTEM_TIME INTERVAL 1 HOUR;

# Enables auto-creation:
ALTER TABLE t1 PARTITION BY SYSTEM_TIME INTERVAL 1 HOUR AUTO;
```

If the rest of the partitioning specification is identical to `CREATE TABLE`, no repartitioning will be done (for details see [MDEV-27328](https://jira.mariadb.org/browse/MDEV-27328)).

### Removing Old History

Because it stores all the history, a system-versioned table might grow very large over time. There are many options to trim down the space and remove the old history.

One can completely drop the versioning from the table and add it back again, this deletes all the history:

```sql
ALTER TABLE t DROP SYSTEM VERSIONING;
ALTER TABLE t ADD SYSTEM VERSIONING;
```

It might be a rather time-consuming operation, though, as the table needs to be rebuilt, possibly twice (depending on the storage engine).

Another option would be to use partitioning and drop some of historical partitions:

```sql
ALTER TABLE t DROP PARTITION p0;
```

{% hint style="warning" %}
You cannot drop a current partition or the only historical partition.
{% endhint %}

As a third option; you can use a variant of the [DELETE](../../sql-statements/data-manipulation/changing-deleting-data/delete.md) statement to prune the history:

```sql
DELETE HISTORY FROM t;
```

Or only old history up to a specific point in time:

```sql
DELETE HISTORY FROM t BEFORE SYSTEM_TIME '2016-10-09 08:07:06';
```

Or to a specific transaction (with `BEFORE SYSTEM_TIME TRANSACTION xxx`).

To protect the integrity of the history, this statement requires a special [DELETE HISTORY](../../sql-statements/account-management-sql-statements/grant.md#table-privileges) privilege.

Currently, using the `DELETE HISTORY` statement with a `BEFORE SYSTEM_TIME` greater than the `ROW_END` of the active records (as a [TIMESTAMP](../../data-types/date-and-time-data-types/timestamp.md), this has a maximum value of `'2038-01-19 03:14:07'` [UTC](../../data-types/string-data-types/character-sets/internationalization-and-localization/coordinated-universal-time.md)) results in the historical records being dropped, and the active records being deleted and moved to history. See [MDEV-25468](https://jira.mariadb.org/browse/MDEV-25468).

The [TRUNCATE TABLE](../../sql-statements/table-statements/truncate-table.md) statement drops all historical records from a system-versioned table.

Historic data is protected from `TRUNCATE` statements, as per the SQL standard, and an [Error 4137](../../error-codes/mariadb-error-codes-4100-to-4199/e4137.md) is instead raised:

```sql
TRUNCATE t;
ERROR 4137 (HY000): System-versioned tables do not support TRUNCATE TABLE
```

### Excluding Columns From Versioning

Another MariaDB extension allows one to version only a subset of columns in a table. This is useful, for example, if you have a table with user information that should be versioned, but one column is, let's say, a login counter that is incremented often and is not interesting to version. Such a column can be excluded from versioning by declaring it `WITHOUT VERSIONING`

```sql
CREATE TABLE t (
   x INT,
   y INT WITHOUT SYSTEM VERSIONING
) WITH SYSTEM VERSIONING;
```

A column can also be declared `WITH VERSIONING`, that will automatically make the table versioned. The statement below is equivalent to the one above:

```sql
CREATE TABLE t (
   x INT WITH SYSTEM VERSIONING,
   y INT
);
```

## System Variables

A number of system variables are related to system-versioned tables:

#### system\_versioning\_alter\_history

* Description: SQL:2011 does not allow [ALTER TABLE](../../sql-statements/data-definition/alter/alter-table/) on system-versioned tables. When this variable is set to `ERROR`, an attempt to alter a system-versioned table will result in an error. When this variable is set to `KEEP`, `ALTER TABLE` will be allowed, but the history will become incorrect — querying historical data will show the new table structure. This mode is still useful, for example, when adding new columns to a table. Note that if historical data contains or would contain nulls, attempting to `ALTER` these columns to be `NOT NULL` will return an error (or warning if [strict\_mode](../../../server-management/variables-and-modes/sql_mode.md#strict-mode) is not set).
* Command line: `--system-versioning-alter-history=value`
* Scope: Global, Session
* Dynamic: Yes
* Type: Enum
* Default Value: `ERROR`
* Valid Values: `ERROR`, `KEEP`

#### `system_versioning_asof`

* Description: If set to a specific timestamp value, an implicit `FOR SYSTEM_TIME AS OF` clause will be applied to all queries. This is useful if one wants to do many queries for history at the specific point in time. Set it to `'DEFAULT'` to restore the default behavior. Has no effect on DML, so queries such as [INSERT .. SELECT](../../sql-statements/data-manipulation/inserting-loading-data/insert-select.md) and [REPLACE .. SELECT](../../sql-statements/data-manipulation/changing-deleting-data/replace.md) need to state AS OF explicitly.

**Note**: You need to use quotes around the name `'DEFAULT'` when setting the session value, unquoted literal `DEFAULT` will restore the current global value instead.

* Command line: None
* Scope: Global, Session
* Dynamic: Yes
* Type: Varchar
* Default Value: `DEFAULT`

#### system\_versioning\_innodb\_algorithm\_simple

* Description: Never fully implemented and removed in the following release.
* Command line: `--system-versioning-innodb-algorithm-simple[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Type: Boolean
* Default Value: `ON`
* Introduced: MariaDB 10.3.4
* Removed: MariaDB 10.3.5

#### system\_versioning\_insert\_history

* Description: Allows direct inserts into ROW\_START and ROW\_END columns if [secure\_timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#secure_timestamp) allows changing [timestamp](../../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#timestamp).
* Command line: `--system-versioning-insert-history[={0|1}]`
* Scope: Global, Session
* Dynamic: Yes
* Type: Boolean
* Default Value: `OFF`
* Introduced: MariaDB 10.11.0

## Limitations

* Versioning clauses cannot be applied to [generated (virtual and persistent) columns](../../sql-statements/data-definition/create/generated-columns.md).
* [mariadb-dump](../../../clients-and-utilities/legacy-clients-and-utilities/mysqldump.md) did not read historical rows from versioned tables, and so historical data would not be backed up. Also, a restore of the timestamps would not be possible as they cannot be defined by an insert/a user. From [MariaDB 10.11](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/10.11/what-is-mariadb-1011), use the `-H` or `--dump-history` options to include the history.

## See Also

* [Application-Time Periods](application-time-periods.md)
* [Bitemporal Tables](bitemporal-tables.md)
* [mysql.transaction\_registry Table](../../system-tables/the-mysql-database-tables/mysql-transaction_registry-table.md)
* [MariaDB Temporal Tables](https://youtu.be/uBoUlTsU1Tk) (video)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
