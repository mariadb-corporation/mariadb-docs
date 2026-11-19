---
description: >-
  How GridGain 9 collects and uses SQL statistics: statistics objects, column
  groups, manual refresh, and system views.
---

# SQL Statistics

The GridGain SQL engine uses a cost-based optimizer. For each query, the optimizer compares several execution plans and selects the plan with the lowest estimated cost. The cost depends on the number of rows that each operator returns, and the optimizer calculates this number from statistics.

By default, GridGain collects only the *table size*, which is the approximate number of rows in each table. GridGain maintains this value automatically. For all other estimates, the optimizer uses fixed assumptions. For example, it assumes that a range condition returns 25% of the rows. These assumptions can be far from the real data. A wrong estimate can lead to a wrong join order, a wrong join algorithm, or a wrong choice between an index scan and a table scan.

To replace the assumptions with measured values, collect *column statistics*. Column statistics describe the distribution of values in columns and in groups of columns. To collect them, do the following:

1. Create a *statistics object*. A statistics object is a named object in the schema of a table. It defines the columns of the table that GridGain analyzes.
2. Collect the data with the `REFRESH STATISTICS` statement.

Accurate estimates do not make each query faster. The effect depends on the query, so measure the execution time of your queries before and after the collection of statistics. For a step-by-step example with measurements on a TPC-H data set, see [How to Improve Query Performance With SQL Statistics](../../../gridgain9-get-started/how-to-guides/improve-query-performance-sql-statistics.md).

## Limitations

* Column statistics are collected only on request. Automatic refresh is not available.
* The collection always reads all rows of the table. Sampling is not available.
* You cannot create statistics objects in system schemas.
* Histograms and null counts are available only for single-column groups.
* A statistics object must contain at least one column group. You cannot remove all column groups with `ALTER STATISTICS`. Use `DROP STATISTICS` instead.

## Statistics Objects and Column Groups

A statistics object belongs to one table and contains one or more *column groups*. A column group is a single column or a set of columns of the table. Each column group tells GridGain what to measure:

* A single-column group describes the values of one column. The optimizer uses it for conditions, joins, and grouping on this column.
* A multi-column group describes the combinations of values in several columns. The optimizer needs it when the values of the columns depend on each other. Without the group, the optimizer treats the columns as independent.

One table can have several statistics objects.

### Collected Values

GridGain collects the following values for each column group:

| Statistic | Single Column | Multiple Columns | Description |
| --- | --- | --- | --- |
| Total count | Yes | Yes | The number of rows in the table at collection time. |
| Distinct count | Yes | Yes | The approximate number of distinct values, or distinct combinations of values for a group of columns. `NULL` is not counted as a value. |
| Null count | Yes | No | The number of rows where the column is `NULL`. |
| Histogram | Yes | No | An equi-height histogram with up to 254 buckets. It describes how the values are distributed across the value range. |

The distinct count and the histogram are estimates. GridGain calculates them with probabilistic data structures, so the reported values can differ from the exact values by a few percent.

For string and binary columns, the histogram stores only the first 64 characters or bytes of each value.

### Default Column Groups

When you create a statistics object, you can list the column groups or use the default set.

The default set contains:

* For each hash index, a group with all columns of the index.
* For each sorted index, a group for each prefix of the index columns. For an index on `(a, b, c)`, the groups are `(a)`, `(a, b)`, and `(a, b, c)`.
* A group with the colocation columns of the table.
* Each column of the table as a separate group. GridGain stops adding single-column groups when the set contains 100 groups.

The order of columns in a group is not important. The groups `(a, b)` and `(b, a)` are the same group.

GridGain resolves the default set one time, when you run the statement. If you add a column or an index later, the statistics object does not change. To add the new groups, run `ALTER STATISTICS ... ADD COLUMN GROUPS (DEFAULT)`.

### Choosing Column Groups

The default set is a good start for most tables. A multi-column group that is not in the default set is useful when all these conditions are true:

* Queries filter or group by the columns together.
* The values of the columns depend on each other. For example, `city` and `zip_code`, or `brand` and `manufacturer`.
* The `EXPLAIN` output shows a row estimate that is far from the real number of rows.

To add such a group, list it in the `CREATE STATISTICS` statement, or [add it to an existing statistics object](#changing-a-statistics-object) with `ALTER STATISTICS ... ADD COLUMN GROUPS`.

Do not add a group for independent columns. The optimizer already calculates a correct estimate from the single-column statistics, and each additional group makes the collection slower.

## Managing Statistics

If authorization is enabled, the statements in this section require the statistics privileges. For the list of privileges, see [User Permissions and Roles](../../../security/user-permissions-and-roles.md).

### Creating a Statistics Object

Use the [`CREATE STATISTICS`](../../../reference/sql/ddl.md#create-statistics) statement. You can use the default set of column groups or list the column groups:

```sql
-- Creates a statistics object with the default set of column groups.
CREATE STATISTICS person_stats ON Person;

-- Creates a statistics object with two single-column groups and one group of two columns.
CREATE STATISTICS city_stats ON City (population, country_id, (country_id, region_id));
```

GridGain creates the statistics object in the schema of the table.

{% hint style="warning" %}
`CREATE STATISTICS` only registers the statistics object. It does not read the table. The optimizer starts to use the statistics after you run `REFRESH STATISTICS`.
{% endhint %}

### Collecting Statistics

Use the [`REFRESH STATISTICS`](../../../reference/sql/operational-commands.md#refresh-statistics) statement to collect the data for an existing statistics object:

```sql
-- Collects one statistics object.
REFRESH STATISTICS person_stats;

-- Collects all statistics objects of a table.
REFRESH STATISTICS FROM Person;

-- Collects all statistics objects in the cluster.
REFRESH ALL STATISTICS;
```

By default, the statement waits until the collection is complete. To run the collection in the background and get control back immediately, add `NO WAIT`:

```sql
REFRESH ALL STATISTICS NO WAIT;
```

### Changing a Statistics Object

Use the [`ALTER STATISTICS`](../../../reference/sql/ddl.md#alter-statistics) statement to add or remove column groups:

```sql
ALTER STATISTICS person_stats ADD COLUMN GROUPS ((city_id, zip_code));

ALTER STATISTICS person_stats DROP COLUMN GROUPS (age);
```

A new column group has no data until the next `REFRESH STATISTICS`. When you remove a column group, the optimizer stops using its data immediately.

### Dropping a Statistics Object

Use the [`DROP STATISTICS`](../../../reference/sql/ddl.md#drop-statistics) statement:

```sql
-- Drops one statistics object.
DROP STATISTICS person_stats;

-- Drops all statistics objects of a table.
DROP STATISTICS FROM Person;
```

After the drop, the optimizer uses the default assumptions for the affected columns.

GridGain also removes statistics when you change the schema:

* When you drop a table or drop a schema with `CASCADE`, GridGain drops the statistics objects of the dropped tables.
* When you drop a column, GridGain removes the column groups that contain the column. If no column groups remain, GridGain drops the statistics object.
* When you drop an index, the statistics object does not change. The column groups of the index stay in the statistics object.

## Monitoring Statistics

The following [system views](../../../reference/monitoring/system-views.md) show the state of the statistics:

| System View | Content |
| --- | --- |
| [`STATISTICS`](../../../reference/monitoring/system-views.md#statistics) | The statistics objects. |
| [`STATISTICS_COLUMN_GROUPS`](../../../reference/monitoring/system-views.md#statistics_column_groups) | The column groups of each statistics object. |
| [`COLLECTED_STATISTICS`](../../../reference/monitoring/system-views.md#collected_statistics) | The collected values for each column group. A column group that is not collected yet is not in this view. |
| [`STATISTICS_GATHERING_JOBS`](../../../reference/monitoring/system-views.md#statistics_gathering_jobs) | The collections that are in progress on each node. |

The query below shows the collected values for a table:

```sql
SELECT statistics_name, column_names, collected_at, total_count, distinct_count, nulls_count
  FROM system.collected_statistics
 WHERE schema_name = 'PUBLIC' AND table_name = 'PERSON';
```

The query below finds the column groups that have no collected data:

```sql
SELECT g.schema_name, g.table_name, g.statistics_name, g.column_names
  FROM system.statistics_column_groups g
  LEFT JOIN system.collected_statistics c
    ON c.statistics_id = g.statistics_id AND c.columns_group_id = g.columns_group_id
 WHERE c.statistics_id IS NULL;
```

The query below shows the progress of a running collection:

```sql
SELECT node_name, schema_name, table_name, completed_partitions, total_partitions
  FROM system.statistics_gathering_jobs;
```

To see how statistics change a plan, compare the `est` values in the [`EXPLAIN`](using-explain.md) output before and after the collection.

## How the Optimizer Uses Statistics

The optimizer uses column statistics in these cases:

* **Comparison with a literal**. For conditions such as `=`, `<>`, `<`, `<=`, `>`, `>=`, `BETWEEN`, and `IN`, the optimizer reads the histogram of the column and estimates how many rows match.
* **Equality with a value that is not a literal**. For example, with a dynamic parameter. The optimizer divides the number of rows by the distinct count of the column.
* **Equality on several columns**. When a condition fixes the values of several columns, and a column group covers these columns, the optimizer uses the distinct count of the group. This keeps the correlation between the columns. Without the group, the optimizer treats the columns as independent.
* **Null checks**. For `IS NULL` and `IS NOT NULL`, the optimizer uses the null count.
* **Grouping and distinct operations**. For `GROUP BY` and `DISTINCT`, the optimizer uses the distinct count to estimate the number of result rows.
* **Joins**. Accurate estimates of the join inputs and the distinct counts of the join columns help the optimizer select the join order and the join algorithm.

If statistics do not cover a column or a condition, the optimizer uses the default assumptions for this part of the query. The plans for tables without statistics do not change.

## How Collection Works

When you run `REFRESH STATISTICS`, the node that receives the statement coordinates the collection:

1. The coordinator sends requests to the nodes that hold the data of the table.
2. Each node scans its partitions and calculates the statistics. All partitions are read at the same timestamp in a read-only transaction, so the collection does not block updates and does not take locks.
3. The coordinator merges the results from all nodes into one result for each column group.
4. The coordinator saves the result to a system table. The statistics are available after a cluster restart.
5. Each node loads the new statistics into its memory, and the cached query plans for the table become invalid. The next execution of a query builds a new plan.

If several statistics objects of one table are collected together, GridGain reads the table one time.

The collection reads all rows of the table. When you work with large tables, account for the CPU and disk resources that each node needs to read all table data:

* Run `REFRESH STATISTICS` when the load is low.
* Limit the number of partitions that a node scans at the same time with the `ignite.sql.statistics.collectionConcurrency` [node configuration property](../../../reference/configuration/node-configuration-parameters.md#sql-configuration).
* Use `NO WAIT` when the client must not wait for a long operation.

## Keeping Statistics Up to Date

GridGain does not refresh column statistics automatically. The statistics describe the table at collection time. The optimizer uses them as ratios, such as the fraction of rows that match a condition, and applies the ratios to the current table size. For this reason, statistics stay useful while the distribution of the data is stable, even if the table grows.

Run `REFRESH STATISTICS` in these cases:

* After the initial data load or a bulk load.
* After the distribution of values changes. For example, when new values appear in a status column, or a date range moves forward.
* After you add column groups with `ALTER STATISTICS`.
* On a schedule, if the data changes continuously. Use the `COLLECTED_AT` column of the [`COLLECTED_STATISTICS`](../../../reference/monitoring/system-views.md#collected_statistics) system view to find the age of the statistics.

You do not need to refresh the table size. GridGain updates it automatically with the period set in the `ignite.sql.statistics.autoRefresh.staleRowsCheckIntervalSeconds` [cluster configuration property](../../../reference/configuration/cluster-configuration-parameters.md#sql-configuration).

## Reloading Statistics on a Node

Each node keeps the collected statistics in memory and updates them automatically. If the plans on one node do not show the current statistics, you can load the statistics from the storage again with the [`sql statistics reload`](../../../reference/cli-tool.md#sql-statistics-reload) CLI command:

```bash
sql statistics reload --table=PUBLIC.PERSON
```

The command does not collect statistics and affects only the node that the CLI is connected to.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
