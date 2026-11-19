---
description: >-
  Collect SQL statistics on a TPC-H data set in GridGain 9, measure the effect
  on query time, and add column groups for correlated columns.
---

# How to Improve Query Performance With SQL Statistics

## Prerequisites

- A running GridGain 9 cluster and the [CLI tool](../../reference/cli-tool.md)
- [Server-side file access](../../reference/sql/operational-commands.md#server-side-file-access) allowed in the configuration of each node, to load the data with `COPY`
- A TPC-H data set with scale factor 1 as CSV files with the `|` delimiter. You can generate the data with the `dbgen` tool from the [TPC-H toolkit](https://www.tpc.org/tpch/). The files that were used for this guide have no delimiter at the end of the line.

## Overview

[SQL statistics](../../tuning-and-troubleshooting/performance-tuning/sql-tuning/sql-statistics.md) give the optimizer accurate row estimates, and with accurate estimates the optimizer can select a better plan. But a different plan is not always a faster plan. For this reason, this guide measures the execution time of a query before and after the collection of statistics. It walks through the task in the order you do it on your own data: measure a query, create and collect the statistics, compare the plan and the time, check the other queries, and add a column group for correlated columns.

Use this guide when a query is slow and its `EXPLAIN` output shows row estimates that are far from the real numbers of rows.

The numbers in this guide come from the following environment:

- A cluster of three GridGain 9 nodes on one computer. Each node has a 6 GB heap.
- The TPC-H data set with scale factor 1. The `lineitem` table contains 6,001,215 rows.
- The default distribution zone.
- Queries run through the JDBC driver.

The query was measured in four rounds. A round measures the query without statistics, then with statistics. Each measurement has 10 runs after 3 warm-up runs. The guide shows the median of all runs. The results on your hardware and your data are different. Use the same method to measure your own queries.

{% hint style="info" %}
The `EXPLAIN` output in this guide is shortened. It shows only the operators and the attributes that are important for the example. The estimates on your cluster can differ by a few percent, because the statistics are approximate.
{% endhint %}

## Load the Data

Create the TPC-H tables with the [gg9-tpch-schema.sql](../../.gitbook/assets/gg9-tpch-schema.sql) script:

```bash
sql --file /path/gg9-tpch-schema.sql
```

Then run a `COPY` statement for each table. The statement below loads the `lineitem` table:

```sql
COPY FROM '/path/tpch/lineitem.csv'
INTO lineitem (l_orderkey, l_partkey, l_suppkey, l_linenumber, l_quantity, l_extendedprice,
               l_discount, l_tax, l_returnflag, l_linestatus, l_shipdate, l_commitdate,
               l_receiptdate, l_shipinstruct, l_shipmode, l_comment)
FORMAT CSV
WITH 'delimiter'='|';
```

After the data load, the optimizer knows only the size of each table. Wait about a minute for GridGain to update the table sizes, then check the estimate of a full scan:

```sql
EXPLAIN PLAN FOR SELECT * FROM lineitem;
```

```
Exchange
    est: (rows=6001215)
  TableScan
      table: PUBLIC.LINEITEM
      est: (rows=6001215)
```

{% hint style="success" %}
**Checkpoint:** The estimate of the table scan is equal to the number of rows in the table. If the estimate is smaller, wait for the next update of the table sizes and run the statement again.
{% endhint %}

## Measure the Query Without Statistics

This guide uses the TPC-H query 17. The query finds the parts of one brand and one container type, and calculates the revenue of the small orders of these parts:

```sql
SELECT sum(l_extendedprice) / 7.0 AS avg_yearly
  FROM lineitem, part
 WHERE p_partkey = l_partkey
   AND p_brand = 'Brand#23'
   AND p_container = 'MED BOX'
   AND l_quantity < (
       SELECT 0.2 * avg(l_quantity)
         FROM lineitem
        WHERE l_partkey = p_partkey);
```

Run the query several times and write down the execution time. In the CLI, use the `--timed` option:

```bash
sql --timed --file /path/q17.sql
```

In the test environment, the query takes **7.6 seconds**.

Now look at the plan. Add `EXPLAIN PLAN FOR` before the query:

```
HashJoin
    predicate: AND(<(L_QUANTITY, *(0.2, $f1)), =(P_PARTKEY, L_PARTKEY))
    est: (rows=465828)
  TableScan
      table: PUBLIC.LINEITEM
      est: (rows=6001215)
  MergeJoin
      predicate: =(P_PARTKEY, L_PARTKEY)
      est: (rows=133094)
    StreamAggregate
        group: [L_PARTKEY]
        aggregation: [SUM(L_QUANTITY), COUNT()]
        est: (rows=1200243)
      IndexScan
          table: PUBLIC.LINEITEM
          index: L_PK_SK
          est: (rows=6001215)
    Sort
        collation: [P_PARTKEY ASC]
        est: (rows=22178)
      TableScan
          table: PUBLIC.PART
          predicate: AND(=(P_BRAND, _UTF-8'Brand#23'), =(P_CONTAINER, _UTF-8'MED BOX'))
          est: (rows=22178)
```

Two estimates in this plan are far from the real data:

- The filter on the `part` table. The optimizer expects 22,178 rows. The real number is 204.
- The number of distinct part keys in `lineitem`. The optimizer expects 1,200,243 groups. The real number is 200,000.

Because the optimizer expects many rows from `part`, it selects a merge join. For the merge join, it reads all 6 million rows of `lineitem` through an index to get them in the order of the part key.

{% hint style="success" %}
**Checkpoint:** You have the execution time of the query without statistics, and you know which estimates in the plan are wrong.
{% endhint %}

## Create and Collect Statistics

Create a statistics object for each table. The statements below use the [default set of column groups](../../tuning-and-troubleshooting/performance-tuning/sql-tuning/sql-statistics.md#default-column-groups): the index columns, the colocation columns, and each column of the table.

```sql
CREATE STATISTICS region_stats ON region;
CREATE STATISTICS nation_stats ON nation;
CREATE STATISTICS supplier_stats ON supplier;
CREATE STATISTICS customer_stats ON customer;
CREATE STATISTICS part_stats ON part;
CREATE STATISTICS partsupp_stats ON partsupp;
CREATE STATISTICS orders_stats ON orders;
CREATE STATISTICS lineitem_stats ON lineitem;
```

Check the column groups of a statistics object:

```sql
SELECT columns_group_id, column_names
  FROM system.statistics_column_groups
 WHERE statistics_name = 'LINEITEM_STATS'
 ORDER BY columns_group_id;
```

```
COLUMNS_GROUP_ID | COLUMN_NAMES
-----------------+-------------------------
0                | L_ORDERKEY
1                | L_PARTKEY
2                | L_SUPPKEY
3                | L_ORDERKEY, L_LINENUMBER
4                | L_PARTKEY, L_SUPPKEY
5                | L_LINENUMBER
6                | L_QUANTITY
...              | ...
17               | L_COMMENT
```

The set contains each column of the table and two groups of two columns. The group `(L_ORDERKEY, L_LINENUMBER)` comes from the primary key. The group `(L_PARTKEY, L_SUPPKEY)` comes from the indexes on these columns.

The statistics objects are empty at this point. Collect the statistics for all of them:

```sql
REFRESH ALL STATISTICS;
```

The statement waits until the collection is complete. In the test environment, the collection for all eight tables takes 11 seconds.

Check the result in the `COLLECTED_STATISTICS` system view:

```sql
SELECT column_names, total_count, distinct_count, nulls_count
  FROM system.collected_statistics
 WHERE statistics_name = 'LINEITEM_STATS'
 ORDER BY columns_group_id;
```

```
COLUMN_NAMES             | TOTAL_COUNT | DISTINCT_COUNT | NULLS_COUNT
-------------------------+-------------+----------------+------------
L_ORDERKEY               | 6001215     | 1531163        | 0
L_PARTKEY                | 6001215     | 197825         | 0
L_SUPPKEY                | 6001215     | 10076          | 0
L_ORDERKEY, L_LINENUMBER | 6001215     | 5908425        | null
L_PARTKEY, L_SUPPKEY     | 6001215     | 799595         | null
L_LINENUMBER             | 6001215     | 7              | 0
L_QUANTITY               | 6001215     | 50             | 0
L_DISCOUNT               | 6001215     | 11             | 0
L_RETURNFLAG             | 6001215     | 3              | 0
L_LINESTATUS             | 6001215     | 2              | 0
L_SHIPDATE               | 6001215     | 2526           | 0
...                      | ...         | ...            | ...
```

The distinct counts are estimates. For example, the table contains 200,000 distinct part keys, and the statistics report 197,825. The null count is collected only for single columns.

The `HISTOGRAM` column contains the histogram of a column in the JSON format. The output below is formatted for readability. Each bucket has the start value, the fraction of rows in the bucket, and the number of distinct values in the bucket:

```sql
SELECT histogram
  FROM system.collected_statistics
 WHERE statistics_name = 'LINEITEM_STATS' AND column_names = 'L_RETURNFLAG';
```

```json
{
  "target_histogram_size": 254,
  "histogram_hb": [
    {"start": "A", "end": "A", "size": 0.24698431900873408, "ndv": 1},
    {"start": "N", "end": "N", "size": 0.5065695863254358, "ndv": 1},
    {"start": "R", "end": "R", "size": 0.24644609466583017, "ndv": 1}
  ]
}
```

The histogram shows that about half of the rows have the `N` flag, and the other two values have about a quarter of the rows each.

{% hint style="success" %}
**Checkpoint:** The `COLLECTED_STATISTICS` view has a row for each column group of each statistics object, and the `TOTAL_COUNT` value is equal to the number of rows in the table.
{% endhint %}

## Compare the Plan and the Execution Time

After the collection, GridGain builds a new plan for the query. Run `EXPLAIN` for the TPC-H query 17 again:

```
HashJoin
    predicate: AND(<(L_QUANTITY, *(0.2, $f1)), =(P_PARTKEY, L_PARTKEY))
    est: (rows=4125)
  TableScan
      table: PUBLIC.LINEITEM
      est: (rows=6001215)
  HashJoin
      predicate: =(P_PARTKEY, L_PARTKEY)
      est: (rows=194)
    HashAggregate
        group: [L_PARTKEY]
        aggregation: [SUM(L_QUANTITY), COUNT()]
        est: (rows=197825)
      TableScan
          table: PUBLIC.LINEITEM
          est: (rows=6001215)
    TableScan
        table: PUBLIC.PART
        predicate: AND(=(P_BRAND, _UTF-8'Brand#23'), =(P_CONTAINER, _UTF-8'MED BOX'))
        est: (rows=196)
```

The estimates are now close to the real data:

- The filter on `part` returns 196 rows instead of 22,178. The real number is 204. The histograms show that `Brand#23` is in 3.9% of the rows and `MED BOX` is in 2.5% of the rows. The product of these fractions is about 0.1% of 200,000 rows.
- The aggregate returns 197,825 groups instead of 1,200,243. This is the distinct count of the `l_partkey` column.

With these estimates, the optimizer changes the plan. It does not need the sorted input, so it replaces the index scan with a table scan, the stream aggregate with a hash aggregate, and the merge join with a hash join. The sort of the `part` rows is not necessary.

Run the query again and compare the time:

| | Without Statistics | With Statistics |
| --- | --- | --- |
| Execution time, median | 7.6 s | 5.2 s |
| Execution time, medians of the rounds | 7.5 s to 7.8 s | 5.1 s to 5.3 s |

The query is 1.45 times faster, and the result is the same in each round.

{% hint style="success" %}
**Checkpoint:** The `est` values in the plan are close to the real numbers of rows, and the execution time of the query is lower than the time you measured without statistics.
{% endhint %}

## Check the Other Queries

Statistics change the estimates of all queries that use the tables. In the test environment, the plans of 10 of the 22 TPC-H queries change after the collection of statistics.

The effect on the execution time depends on the query:

- A query gets faster when a wrong estimate caused an expensive operation, such as a sort or a scan through an index, as in the query 17.
- Many queries keep the same time. A more accurate estimate does not always lead to a different plan, and a different plan does not always differ in cost.

For this reason, measure the full workload, not only the query that you want to improve. If the time of a query changes in the wrong direction, see [Troubleshooting](#troubleshooting).

## Add a Column Group for Correlated Columns

Single-column statistics describe each column separately. When a query has conditions on several columns, the optimizer multiplies the fractions of the conditions. This is correct only if the columns are independent.

In the `part` table, each brand belongs to one manufacturer. For example, all parts of `Brand#12` have the manufacturer `Manufacturer#1`. Look at the estimate for a query that filters by the two columns:

```sql
EXPLAIN PLAN FOR
SELECT p_partkey, p_name
  FROM part
 WHERE p_mfgr = 'Manufacturer#1' AND p_brand = 'Brand#12';
```

```
TableScan
    table: PUBLIC.PART
    predicate: AND(=(P_MFGR, _UTF-8'Manufacturer#1'), =(P_BRAND, _UTF-8'Brand#12'))
    est: (rows=1621)
```

The estimate is 1,621 rows, and the query returns 8,167 rows. The optimizer multiplies the fraction of the manufacturer (about 1/5) by the fraction of the brand (about 1/25). In the real data, the condition on the manufacturer does not remove any rows of the brand.

Add a column group for the two columns and collect the statistics:

```sql
ALTER STATISTICS part_stats ADD COLUMN GROUPS ((p_mfgr, p_brand));

REFRESH STATISTICS part_stats;
```

The group has 25 distinct combinations, which is the same as the number of brands:

```sql
SELECT column_names, distinct_count
  FROM system.collected_statistics
 WHERE statistics_name = 'PART_STATS' AND column_names IN ('P_MFGR', 'P_BRAND', 'P_MFGR, P_BRAND');
```

```
COLUMN_NAMES    | DISTINCT_COUNT
----------------+---------------
P_MFGR          | 5
P_BRAND         | 25
P_MFGR, P_BRAND | 25
```

Run the `EXPLAIN` statement again. The estimate is now 8,000 rows:

```
TableScan
    table: PUBLIC.PART
    predicate: AND(=(P_MFGR, _UTF-8'Manufacturer#1'), =(P_BRAND, _UTF-8'Brand#12'))
    est: (rows=8000)
```

The `lineitem` table has the same type of dependency between the `l_returnflag` and `l_linestatus` columns. Without a group, the optimizer expects 6 groups for a `GROUP BY` on these columns. With the group `(l_returnflag, l_linestatus)`, it expects 4 groups, which is the real number.

{% hint style="warning" %}
A correct estimate does not make a query faster by itself. In the test environment, the two queries above and a join of the filtered parts with `lineitem` keep the same plans and the same execution time after the groups are added. A column group gives a faster query only when the wrong estimate is the reason for a slow plan.
{% endhint %}

{% hint style="success" %}
**Checkpoint:** The distinct count of the group `(P_MFGR, P_BRAND)` is equal to the distinct count of `P_BRAND`, and the estimate of the filter is close to the real number of rows.
{% endhint %}

## Find Candidates for Column Groups

Use this procedure for your own queries:

1. Find a slow query and run `EXPLAIN` for it. Find the operators with conditions on several columns of one table, or with a `GROUP BY` on several columns.
2. Compare the `est` value with the real number of rows. To get the real number, run `SELECT COUNT(*)` with the same conditions.
3. If the difference is large, compare the distinct counts. If the distinct count of the group is much smaller than the product of the distinct counts of the columns, the columns are correlated. Add a column group for them.
4. Collect the statistics, check the `EXPLAIN` output, and measure the execution time again. If the time does not change, remove the group to keep the collection fast.

## Troubleshooting

<details>
<summary>The estimates do not change after CREATE STATISTICS</summary>

`CREATE STATISTICS` and `ALTER STATISTICS` only register the column groups. The optimizer uses the statistics only after `REFRESH STATISTICS`. Check that the `COLLECTED_STATISTICS` system view has rows for the statistics object.

</details>

<details>
<summary>The estimate of a table scan is not equal to the number of rows</summary>

GridGain updates the table sizes periodically. The default period is 60 seconds. Wait for the next update and run `EXPLAIN` again.

</details>

<details>
<summary>The estimates are correct, but the query time does not change</summary>

A more accurate estimate does not always lead to a different plan. Compare the `EXPLAIN` output with and without statistics. If the operators are the same, the wrong estimate was not the reason for the slow query. Look for other reasons with [EXPLAIN](../../tuning-and-troubleshooting/performance-tuning/sql-tuning/using-explain.md).

</details>

<details>
<summary>A query is slower with statistics</summary>

1. Compare the `EXPLAIN` output with and without statistics, and find the operator that changed.
2. Check the estimates of the inputs of this operator against the real numbers of rows.
3. If an estimate is wrong because the columns are correlated, add a column group.
4. If the optimizer does not select the best plan with correct estimates, fix the plan for this query with [optimizer hints](../../reference/sql/optimizer-hints.md).

</details>

## Related

- [SQL Statistics](../../tuning-and-troubleshooting/performance-tuning/sql-tuning/sql-statistics.md) - Full description of statistics objects, column groups, collection, and monitoring.
- [How to Improve Queries With EXPLAIN Command](../../tuning-and-troubleshooting/performance-tuning/sql-tuning/using-explain.md) - Read query execution plans and diagnose performance issues.
- [REFRESH STATISTICS](../../reference/sql/operational-commands.md#refresh-statistics) - Syntax of the statement that collects statistics.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
