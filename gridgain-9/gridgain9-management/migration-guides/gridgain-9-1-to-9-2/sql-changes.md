---
description: >-
  SQL changes in the GridGain 9.1 to 9.2 upgrade: CREATE ZONE syntax, system view columns, the __part alias, the ADD keyword, microsecond precision, EXPLAIN output, and query protocol.
---

# SQL and System View Changes

GridGain 9.2 replaces the query protocol, removes the `CREATE ZONE ... WITH` syntax and the legacy system view columns, reserves the `ADD` keyword, and keeps microseconds in date and time values.

## The Query Protocol Changed

This section applies if you use a rolling upgrade. A full-cluster upgrade is not affected, because no node runs a different version.

GridGain 9.2 replaces the SQL query protocol, and the two versions do not understand each other. While the cluster runs both versions, a query that needs a node of the other version fails in both directions:

- A 9.1 node that coordinates a query and maps a fragment onto a 9.2 node gets the error `IGN-CMN-65535: Legacy query start protocol is no longer supported, the sending node must be upgraded`.
- A 9.2 node that coordinates a query and maps a fragment onto a 9.1 node, while a rolling upgrade is in progress, fails with `IGN-SQL-8: The query was mapped onto node '<node>' which runs version <version> and does not support latest query execution protocol, wait for the rolling upgrade to finish and retry the query`.

A query fails only if one of its fragments is mapped onto a node of the other version, so in a mixed cluster some queries succeed and others fail.

Stop all SQL traffic, including JDBC, ODBC, scheduled jobs, and the SQL CLI, from `upgrade start` until `upgrade commit` finishes. Key-value and table API operations are not affected. Schema changes are also blocked during a rolling upgrade. See [Rolling Upgrade](../../upgrade/rolling-upgrade.md#limitations).

If you cannot pause SQL, use a [full-cluster upgrade](../../upgrade/full-cluster-upgrade.md).

## CREATE ZONE Syntax

The `WITH` form of `CREATE ZONE` is removed. 9.1 accepted both forms. 9.2 accepts only the form with an option list in parentheses. The `STORAGE PROFILES` clause is required in both versions:

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

The Java Catalog DSL generates the new syntax, so code that builds zones with `ZoneDefinition` needs no change. Search your SQL scripts and deployment tooling for `CREATE ZONE` with `WITH`. Existing zones are not affected.

For all options, see [Distribution Zones](../../../reference/sql/distribution-zones.md).

## Zone Names Are Simple Identifiers

The zone name in `CREATE ZONE`, `ALTER ZONE`, and `DROP ZONE` must be a simple identifier, because zones do not belong to a schema. A name such as `public.my_zone` fails with `Failed to parse query`. 9.1 accepted it and silently kept only the last part. See [Distribution Zones](../../../reference/sql/distribution-zones.md).

```sql
-- 9.1 (no longer accepted)
DROP ZONE public.my_zone;

-- 9.2
DROP ZONE my_zone;
```

## System View Columns Removed

9.2 removes the legacy columns of the system views. Each has a replacement that already exists in 9.1, so you can update your queries before you upgrade.

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
-- 9.1 (no longer accepted)
SELECT name FROM system.tables WHERE schema = 'PUBLIC' AND zone = 'MY_ZONE';

-- 9.1 and 9.2
SELECT table_name FROM system.tables WHERE schema_name = 'PUBLIC' AND zone_name = 'MY_ZONE';
```

A query that uses a removed column fails with `IGN-SQL-4: Failed to validate query ... Column 'NAME' not found in any table`. Check monitoring queries, dashboards, and scripts first. For all columns, see [System Views](../../../reference/monitoring/system-views.md).

## Restart a Node After a Rolling Upgrade

This section applies if you use a rolling upgrade.

After the commit, the system views keep their 9.1 definitions until a node restarts, and queries against them can fail. Restart one node after `upgrade commit`. It registers the 9.2 definitions for the whole cluster, so the other nodes need no restart. A full-cluster upgrade needs no restart.

## The __part Alias Is Removed

Every table has the hidden `BIGINT` column `__PARTITION_ID`, which is not part of `SELECT *`. In 9.1, the alias `__part` (also written `"__PART"`) returned the same value. 9.2 removes the alias, and a query that uses it fails.

```sql
-- 9.1 (no longer accepted)
SELECT __part, id FROM my_table;

-- 9.1 and 9.2
SELECT __partition_id, id FROM my_table;
```

You can now use `__part` as an ordinary column name. See [Partition-Specific SELECTs](../../../gridgain9-development/sql/sql-api.md#partition-specific-selects).

## ADD Is a Reserved Word

`ADD` is now a reserved word. An unquoted `ADD` as the name of a table, column, or alias fails with a parse error. Put the name in double quotes:

```sql
CREATE TABLE "ADD" (id INT PRIMARY KEY, "ADD" INT);
```

Unquoted names are stored in uppercase. An object that you created in 9.1 with an unquoted `add` is named `ADD`, so you must write `"ADD"` from 9.2. See [Reserved Keywords](../../../reference/sql/keywords.md).

## Date and Time Values Keep Microseconds

9.1 evaluated `TIME`, `TIMESTAMP`, and `TIMESTAMP WITH LOCAL TIME ZONE` values and day-time intervals with millisecond precision, even when the column had a higher precision. 9.2 keeps microseconds in literals, casts, arithmetic, comparisons, dynamic parameters, and `DEFAULT` values. Digits after the sixth are truncated, not rounded:

```sql
SELECT TIMESTAMP '2008-01-01 00:00:01.9999995'::TIMESTAMP(9)::VARCHAR;
-- 2008-01-01 00:00:01.999999000
```

`TIME(7)` to `TIME(9)` are still accepted, but SQL keeps only six digits.

Values stored by 9.1 keep their millisecond precision, and only values that you write on 9.2 carry microseconds. A query that compares, orders, or filters on fractions of a second can therefore return different rows after the upgrade. Check these queries.

For more information, see [Data Types](../../../reference/sql/data-types.md).

## EXPLAIN Output Changed

The `EXPLAIN` output of 9.2 prints aggregates under new names, and a `phase` attribute marks the two phases of a two-phase aggregate. For example, `MapHashAggregate` becomes `HashAggregate` with `phase: PARTIAL`, and `ReduceSortAggregate` becomes `StreamAggregate` with `phase: FINAL`. The [List of EXPLAIN Operators](../../../reference/sql/explain-operators-list.md) page has the full 9.1-to-9.2 operator mapping. Update any tool that parses `EXPLAIN` text.

The `DISABLE_RULE` hint names of the aggregate rules are also renamed, and a hint with an old name is ignored without an error:

| 9.1 rule | 9.2 rule |
| --- | --- |
| `ColocatedHashAggregateConverterRule` | `SinglePhaseHashAggregateConverterRule` |
| `ColocatedSortAggregateConverterRule` | `SinglePhaseStreamAggregateConverterRule` |
| `MapReduceHashAggregateConverterRule` | `TwoPhaseHashAggregateConverterRule` |
| `MapReduceSortAggregateConverterRule` | `TwoPhaseStreamAggregateConverterRule` |

The rules for set operations, such as `ColocatedMinusConverterRule` and `MapReduceIntersectConverterRule`, keep their names. For the statement itself, see [EXPLAIN](../../../reference/sql/explain-statement.md).

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
