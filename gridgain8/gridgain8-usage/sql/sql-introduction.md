---
description: >-
  An introduction to GridGain's distributed SQL database, covering simple, distributed, and local queries, distributed joins, aggregation, and timezones.
---

# Working with SQL

GridGain comes with ANSI-99 compliant, horizontally scalable and fault-tolerant distributed SQL database. The distribution is provided either by partitioning the data across cluster nodes or by full replication, depending on the use case.

As a SQL database, GridGain supports all DML commands including SELECT, UPDATE, INSERT, and DELETE queries and also implements a subset of DDL commands relevant for distributed systems.

You can interact with GridGain as you would with any other SQL enabled storage by connecting with [JDBC]({connectors}/sql/jdbc/jdbc-driver) or [ODBC](sql-introduction.md) drivers from both external tools and applications. Java, .NET and C++ developers can leverage native  [SQL APIs](sql-api.md).

Internally, SQL tables have the same data structure as [key-value caches](../../architecture/data-modeling/introduction.md#key-value-cache-vs.-sql-table). It means that you can change partition distribution of your data and leverage [affinity collocation techniques](../../architecture/data-modeling/affinity-colocation.md) for better performance.

GridGain's SQL engine uses H2 Database to parse and optimize queries and generate execution plans.

## Simple Queries

Simple queries, for example a SELECT query from a single table, only interact with the target table, and are executed on the node where the data is stored. Thus, these queries do not need collocation.

## Distributed Queries

More complicated queries often need to compare data from multiple rows. These queries are executed in a distributed manner:

- The query is parsed and split into multiple “map” queries and a single “reduce” query.
- All the map queries are executed on all the nodes where required data resides. If the required data is not present (this can happen, for example, when the subquery requires data from multiple tables) the query may fail. To ensure this does not happen, [collocate](../../architecture/data-modeling/affinity-colocation.md) the data before performing complex queries.
- All the nodes provide result sets of local execution to the query initiator that, in turn, will merge provided result sets into the final results.

You can force a query to be processed locally, i.e. on the subset of data that is stored on the node where the query is executed.

By default, the queries that require multiple records are executed on a specific node, and data required for these queries must be [collocated](../../architecture/data-modeling/affinity-colocation.md) with the other data. Depending on the query you perform, the data in it

### Distributed JOIN

In GridGain, JOIN operations are executed with the assumption that the data is collocated. If your operation attempts a JOIN on non-collocated data, you may see incorrect results.

In case you need to perform a join on non-collocated data, you can perform the [non-collocated join](distributed-joins.md#non-collocated-joins) instead. This comes at a cost of performance for the whole query, as data will be transferred to the node before query execution.

Due to the high data load caused by JOIN operations, using non-collocated joins should be the last resort for when you cannot collocate data. This may have a significant impact on your performance and load.

### Collocated Aggregation

GridGain assumes that data you query by using the aggregations (for example, `GROUP BY` or `ORDER BY`) is not collocated. Aggregation is partially done on mappers, and then transferred to the reducer for final aggregation. In most cases this provides better performance due to the load being distributed across the cluster, but sometimes it may mean that the reducer has to handle unexpectedly large load.

In some scenarios it is better to run the aggregated queries on a single node. If you know in advance that the data you are querying is already collocated, and your query does not need non-collocated data, you can use `SqlFieldsQuery.collocated = true` to tell the SQL engine that all required data for the query is located on the same node. This will reduce network traffic between the nodes and query execution time, but will cause issues if required data cannot be found and may affect query performance due to all query load being processed by one node.

When this flag is set to `true`, the query is executed on individual nodes first and the results are sent to the reducer node for final calculation.

Consider the following example, in which we assume that the data is collocated by `department_id` (in other words, the `department_id` field is configured as the affinity key).

```sql
SELECT SUM(salary) FROM Employee GROUP BY department_id
```

Because of the nature of the SUM operation, GridGain will sum the salaries across the elements stored on individual nodes, and then send these sums to the reducer node where the final result will be calculated.
This operation is already distributed, and enabling the `collocated` flag will only slightly improve performance.

Let's take a slightly different example:

```sql
SELECT AVG(salary) FROM Employee GROUP BY department_id
```

In this example, GridGain has to fetch all (`salary`, `department_id`) pairs to the reducer node and calculate the results there. However, if employees are collocated by the `department_id` field, i.e. employee data for the same department is stored on the same node, setting `SqlFieldsQuery.collocated = true` will reduce query execution time because GridGain will calculate the averages for each department on the individual nodes and send the results to the reducer node for final calculation.

### WHERE Clause

GridGain always assumes that the data used in the `WHERE` clause is collocated. For example, the following query must be executed with both `Salaries` and `Employees` collocated.

```sql
SELECT * FROM Salaries WHERE salary = (SELECT MAX(salary) FROM Employees WHERE Age=42)
```

This clause is not affected by the  `SqlFieldsQuery.collocated = true` property.

## Local Queries

If a query is executed over a [replicated](../../architecture/data-modeling/data-partitioning.md#replicated) table, it will be run against the local data.

Queries over partitioned tables are executed in a distributed manner.
However, you can force local execution of a query over a partitioned table.
See [Local Execution](sql-api.md#local-execution) for details.

## Concurrent Queries

Queries in GridGain 8 do not preserve transactional boundaries. As a result, if an update is performed concurrently with a read operation, it is possible to read both the old and new data within the same query, as well as reading the same data from both before the update and after.

In most scenarios read operations can be executed safely, but in high-load environments multiple queries may start affecting each other.

{% hint style="info" %}
As all SQL operations are transactional in [GridGain 9](https://www.gridgain.com/docs/gridgain9/latest/developers-guide/sql/calcite-based-sql-engine), this behavior changes and concurrent queries are safe to execute.
{% endhint %}

## Working in Multiple Timezones

Each GridGain cluster exists in one timezone. All `DATE`, `TIME` or `TIMESTAMP` operations are performed relative to this specific timezone. However, because clients can operate in different timezones, GridGain converts time for operations performed from thin clients to represent a local user's timezone.

For operations performed directly on caches, cluster's timezone is used. If you perform direct cache operations from multiple time zones, make sure you keep track of the timezone users are in.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
