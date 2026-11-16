---
description: >-
  SQL changes when upgrading from GridGain 9.1 to 9.2: the CREATE ZONE syntax, removed system view columns, the removed __part alias, the ADD keyword, microsecond precision, EXPLAIN output, and the query protocol.
---

# SQL and System View Changes

GridGain 9.2 removes the `CREATE ZONE ... WITH` syntax and the legacy columns of the system views. It also reserves the `ADD` keyword, keeps microseconds in date and time values, and replaces the query protocol, so that SQL does not work across 9.1 and 9.2 nodes.

## The Query Protocol Changed

This section applies if you use a rolling upgrade. A full-cluster upgrade is not affected, because no node runs a different version.

GridGain 9.2 replaces the SQL query protocol, and the two versions do not understand each other. As a result, a SQL query that needs a node of the other version fails while the cluster runs both versions, in both directions:

- A 9.1 node that coordinates a query and maps a fragment onto a 9.2 node gets the error `IGN-CMN-65535: Legacy query start protocol is no longer supported, the sending node must be upgraded`.
- A 9.2 node that coordinates a query and maps a fragment onto a 9.1 node, while a rolling upgrade is in progress, fails with `IGN-SQL-8: The query was mapped onto node '<node>' which runs version <version> and does not support latest query execution protocol, wait for the rolling upgrade to finish and retry the query`.

A query fails only if one of its fragments is mapped onto a node of the other version, so in a mixed cluster some queries succeed and others fail. Do not rely on it.

This is why a rolling upgrade from 9.1 to 9.2 needs a pause of the SQL workload. Stop all SQL traffic, including JDBC, ODBC, scheduled jobs, and the SQL CLI, from `upgrade start` until `upgrade commit` finishes, and start it again afterward. Key-value and table API operations are not affected. Schema changes are blocked during a rolling upgrade anyway. See [Rolling Upgrade](../../upgrade/rolling-upgrade.md#limitations).

If you cannot pause SQL, use a [full-cluster upgrade](../../upgrade/full-cluster-upgrade.md).

## CREATE ZONE Syntax

The `WITH` form of `CREATE ZONE` is removed. 9.1 accepted both forms. 9.2 accepts only the form with an optional option list in parentheses, and the `STORAGE PROFILES` clause is required:

```sql
-- 9.1 (no longer accepted)
CREATE ZONE my_zone WITH PARTITIONS = 25, REPLICAS = 3, STORAGE_PROFILES = 'default';

-- 9.2
CREATE ZONE my_zone (PARTITIONS 25, REPLICAS 3) STORAGE PROFILES ['default'];
```

A statement in the old form fails with a parse error that starts with `Failed to parse query`.

The options change as follows:

| 9.1 `WITH` option | 9.2 clause |
| --- | --- |
| `PARTITIONS = n` | `PARTITIONS n` |
| `REPLICAS = n` or `REPLICAS = ALL` | `REPLICAS n` or `REPLICAS ALL` |
| `QUORUM_SIZE = n` | `QUORUM SIZE n` |
| `DISTRIBUTION_ALGORITHM = 'x'` | `DISTRIBUTION ALGORITHM 'x'` |
| `DATA_NODES_FILTER = '...'` | `NODES FILTER '...'` |
| `DATA_NODES_AUTO_ADJUST_SCALE_UP = n` | `AUTO SCALE UP n` or `AUTO SCALE UP OFF` |
| `DATA_NODES_AUTO_ADJUST_SCALE_DOWN = n` | `AUTO SCALE DOWN n` or `AUTO SCALE DOWN OFF` |
| `CONSISTENCY_MODE = 'x'` | `CONSISTENCY MODE 'x'` |
| `STORAGE_PROFILES = 'a, b'` | `STORAGE PROFILES ['a', 'b']` |

The Java Catalog DSL generates the new syntax, so code that builds zones with `ZoneDefinition` needs no change. Search your SQL scripts, deployment tooling, and documentation for `CREATE ZONE` and `WITH`. Zones that already exist are not affected.

For all options, see [Distribution Zones](../../../reference/sql/distribution-zones.md).

## Zone Names Are Simple Identifiers

The zone name in `CREATE ZONE`, `ALTER ZONE`, and `DROP ZONE` must be a simple identifier. A name with a schema, such as `public.my_zone`, does not parse and fails with `Failed to parse query`. Zones do not belong to a schema. 9.1 accepted a qualified name and silently kept only its last part. See [Distribution Zones](../../../reference/sql/distribution-zones.md).

```sql
-- 9.1 (no longer accepted)
DROP ZONE public.my_zone;

-- 9.2
DROP ZONE my_zone;
```

Other statements already used a simple identifier, for example `CREATE TABLE ... ZONE my_zone`.

## System View Columns Removed

9.2 removes the legacy columns of the system views. Each has a replacement column that already exists in 9.1, so you can update your queries before you upgrade.

| View | Removed column | Use instead |
| --- | --- | --- |
| `INDEXES` | `TYPE`, `IS_UNIQUE`, `COLUMNS`, `STATUS` | `INDEX_TYPE`, `IS_UNIQUE_INDEX`, `INDEX_COLUMNS`, `INDEX_STATE` |
| `SEQUENCES` | `ID`, `NAME`, `DATA_TYPE`, `INCREMENT`, `MINIMUM_VALUE`, `MAXIMUM_VALUE`, `START_VALUE`, `CACHE_VALUE` | `SEQUENCE_ID`, `SEQUENCE_NAME`, `SEQUENCE_DATA_TYPE`, `SEQUENCE_INCREMENT`, `SEQUENCE_MINIMUM_VALUE`, `SEQUENCE_MAXIMUM_VALUE`, `SEQUENCE_START_VALUE`, `SEQUENCE_CACHE_VALUE` |
| `SYSTEM_VIEWS` | `ID`, `SCHEMA`, `NAME`, `TYPE` | `VIEW_ID`, `SCHEMA_NAME`, `VIEW_NAME`, `VIEW_TYPE` |
| `SYSTEM_VIEW_COLUMNS` | `NAME`, `TYPE`, `NULLABLE`, `PRECISION`, `SCALE`, `LENGTH` | `COLUMN_NAME`, `COLUMN_TYPE`, `IS_NULLABLE_COLUMN`, `COLUMN_PRECISION`, `COLUMN_SCALE`, `COLUMN_LENGTH` |
| `TABLES` | `SCHEMA`, `NAME`, `ID`, `PK_INDEX_ID`, `COLOCATION_KEY_INDEX`, `ZONE` | `SCHEMA_NAME`, `TABLE_NAME`, `TABLE_ID`, `TABLE_PK_INDEX_ID`, `TABLE_COLOCATION_COLUMNS`, `ZONE_NAME` |
| `TABLE_COLUMNS` | `SCHEMA`, `TYPE`, `NULLABLE`, `PREC`, `SCALE`, `LENGTH` | `SCHEMA_NAME`, `COLUMN_TYPE`, `IS_NULLABLE_COLUMN`, `COLUMN_PRECISION`, `COLUMN_SCALE`, `COLUMN_LENGTH` |
| `ZONES` | `NAME`, `PARTITIONS`, `REPLICAS`, `CONSISTENCY_MODE` | `ZONE_NAME`, `ZONE_PARTITIONS`, `ZONE_REPLICAS`, `ZONE_CONSISTENCY_MODE` |
| `COMPUTE_TASKS` | `ID`, `STATUS`, `CREATE_TIME`, `START_TIME`, `FINISH_TIME` | `COMPUTE_TASK_ID`, `COMPUTE_TASK_STATUS`, `COMPUTE_TASK_CREATE_TIME`, `COMPUTE_TASK_START_TIME`, `COMPUTE_TASK_FINISH_TIME` |
| `SQL_QUERIES` | `ID`, `PHASE`, `TYPE`, `SCHEMA`, `START_TIME`, `PARENT_ID`, `STATEMENT_NUM` | `QUERY_ID`, `QUERY_PHASE`, `QUERY_TYPE`, `QUERY_DEFAULT_SCHEMA`, `QUERY_START_TIME`, `PARENT_QUERY_ID`, `QUERY_STATEMENT_ORDINAL` |
| `LOCKS` | `TX_ID`, `MODE` | `TRANSACTION_ID`, `LOCK_MODE` |
| `TRANSACTIONS` | `ID`, `STATE`, `START_TIME`, `TYPE`, `PRIORITY` | `TRANSACTION_ID`, `TRANSACTION_STATE`, `TRANSACTION_START_TIME`, `TRANSACTION_TYPE`, `TRANSACTION_PRIORITY` |
| `LICENSES` | `ID`, `EDITION`, `COMMON_INFO`, `LIMITS`, `FEATURES` | `LICENSE_ID`, `LICENSE_EDITION`, `LICENSE_COMMON_INFO`, `LICENSE_LIMITS`, `LICENSE_FEATURES` |

For example, a query that lists the tables of a zone changes as follows:

```sql
-- 9.1 (fails in 9.2)
SELECT name FROM system.tables WHERE schema = 'PUBLIC' AND zone = 'MY_ZONE';

-- 9.1 and 9.2
SELECT table_name FROM system.tables WHERE schema_name = 'PUBLIC' AND zone_name = 'MY_ZONE';
```

A query that uses a removed column fails with `IGN-SQL-4: Failed to validate query ... Column 'NAME' not found in any table`. Monitoring queries, dashboards, and scripts that read system views are the most common place to find the old names. For all columns, see [System Views](../../../reference/monitoring/system-views.md).

{% hint style="warning" %}
After a rolling upgrade, the system views keep their 9.1 definitions until you restart the nodes. Until then, a query such as `SELECT * FROM system.zones` fails with an internal error (`class java.lang.Integer cannot be cast to class java.lang.String`). Restart the nodes after `upgrade commit`. A full-cluster upgrade needs no restart.
{% endhint %}

## The __part Alias Is Removed

Every table has the hidden column `__PARTITION_ID`. In 9.1, the legacy alias `__part` (also written `"__PART"`) returned the same value. 9.2 removes the alias, and a query that uses it fails.

```sql
-- 9.1 (fails in 9.2)
SELECT __part, id FROM my_table;

-- 9.1 and 9.2
SELECT __partition_id, id FROM my_table;
```

`__PARTITION_ID` is a hidden `BIGINT` column and is not part of `SELECT *`. Unquoted names are upper-cased, so `__partition_id` works. You can now use `__part` as an ordinary column name. For more information, see [Partition-Specific SELECTs](../../../gridgain9-development/sql/sql-api.md#partition-specific-selects).

## ADD Is a Reserved Word

`ADD` is now a reserved word. An unquoted `ADD` as the name of a table, column, or alias fails with a parse error. Put the name in double quotes:

```sql
CREATE TABLE "ADD" (id INT PRIMARY KEY, "ADD" INT);
```

Unquoted names are stored in upper case. An object that you created in 9.1 with an unquoted `add` is named `ADD`, so you must write `"ADD"` from 9.2. See [Reserved Keywords](../../../reference/sql/keywords.md).

## Date and Time Values Keep Microseconds

SQL in 9.1 evaluated `TIME`, `TIMESTAMP`, and `TIMESTAMP WITH LOCAL TIME ZONE` values and day-time intervals with millisecond precision. Digits after the milliseconds were lost, even when the column had a higher precision. 9.2 keeps microseconds in literals, casts, arithmetic, comparisons, dynamic parameters, and `DEFAULT` values. Digits after the sixth are truncated, not rounded:

```sql
SELECT TIMESTAMP '2008-01-01 00:00:01.9999995'::TIMESTAMP(9)::VARCHAR;
-- 2008-01-01 00:00:01.999999000
```

The storage format does not change, and the maximum declared precision is still 9. The default precision is also unchanged. `TIME(7)` to `TIME(9)` are still accepted, but SQL keeps only six digits.

Values that 9.1 already stored through SQL keep their millisecond precision, because 9.1 truncated them when you inserted them. Only values that you write on 9.2 keep microseconds. A query that compares, orders, or filters on fractions of a second can return different rows after the upgrade, because new values differ below one millisecond. Check these queries.

For more information, see [Data Types](../../../reference/sql/data-types.md).

## EXPLAIN Output Changed

The `EXPLAIN` output of 9.2 prints aggregates under new names, and a `phase` attribute marks the two phases of a two-phase aggregate:

| 9.1 operator | 9.2 operator |
| --- | --- |
| `ColocatedHashAggregate` | `HashAggregate` without `phase` |
| `MapHashAggregate` | `HashAggregate` with `phase: PARTIAL` |
| `ReduceHashAggregate` | `HashAggregate` with `phase: FINAL` |
| `ColocatedSortAggregate` | `StreamAggregate` without `phase` |
| `MapSortAggregate` | `StreamAggregate` with `phase: PARTIAL` |
| `ReduceSortAggregate` | `StreamAggregate` with `phase: FINAL` |

Update any tool that parses `EXPLAIN` text. The `DISABLE_RULE` hints for the aggregate rules are also renamed: `Colocated*` is now `SinglePhase*`, and `MapReduce*` is now `TwoPhase*`. The `Sort` rules are now `Stream` rules. A hint with an old name is ignored. The [List of EXPLAIN Operators](../../../reference/sql/explain-operators-list.md) page has the same 9.1-to-9.2 operator mapping and describes each operator. For the statement itself, see [EXPLAIN](../../../reference/sql/explain-statement.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
