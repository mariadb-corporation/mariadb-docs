---
description: >-
  MariaDB ColumnStore evaluates queries with MPP execution: ExeMgr
  coordinates job steps across PrimProc nodes with extent elimination and
  parallel aggregation to reduce I/O.
---

# Mariadb ColumnStore Query Evaluation

## Overview

MariaDB ColumnStore is a smart storage engine designed to efficiently execute analytical queries using distributed query execution and massively parallel processing (MPP) techniques.

## Scalability

MariaDB ColumnStore is designed to achieve vertical and horizontal scalability for production analytics using distributed query execution and massively parallel processing (MPP) techniques.

ColumnStore evaluates each query as a sequence of job steps using sophisticated techniques to get the best performance for complex analytical queries. Some types of job steps are designed to scale with the system's resources. As you increase the number of ColumnStore nodes or the number of cores on each node, ColumnStore can use those resources to more efficiently execute those types of job steps.

ColumnStore stores each column on disk in extents. The storage format is designed to maintain scalability, even as the table grows. If an operation does not read parts of a large table, I/O costs are reduced. ColumnStore uses a technique called extent elimination that compares the maximum and minimum values in the extent map to the query's conditions, and it avoids scanning extents that don't satisfy the conditions.

ColumnStore provides exceptional scalability for analytical queries. ColumnStore's design supports targeted scale-out to address increased workload requirements, whether it is a larger query load or increased storage and query processing capacity.

### Horizontal Scalability

MariaDB ColumnStore provides horizontal scalability by executing some types of job steps in a distributed manner using multiple nodes.

When ColumnStore is evaluating a job step, the ExeMgr process or facility on the initiator/aggregator node requests the PrimProc process on each node to perform the job step on different extents in parallel. As more nodes are added, ColumnStore can perform more work in parallel.

ColumnStore also uses massively parallel processing (MPP) techniques to speed up some types of job steps. For some types of aggregation operations, each node can perform an initial local aggregation, and then the initiator/aggregator node only needs to combine the local results and perform a final aggregation. This technique can be very efficient for some types of aggregation operations, such as for queries that use the `AVG(), COUNT(), or SUM()` aggregate functions.

### Vertical Scalability

MariaDB ColumnStore provides vertical scalability by executing some types of job steps in a multi-threaded manner using a thread pool.

When the PrimProc process on a node receives work, it executes the job step on an extent in a multi-threaded manner using a thread pool. Each thread operates on a different block within the extent. As more CPUs are added, ColumnStore can work on more blocks in parallel.

## Extent Elimination

![ECStore-QueryExecutionExtentElimination](<../../.gitbook/assets/ecstore-queryexecutionextentelimination (1).png>)

MariaDB ColumnStore uses extent elimination to scale query evaluation as table size increases.

Most databases are row-based databases that use manually-created indexes to achieve high performance on large tables. This works well for transactional workloads. However, analytical queries tend to have very low selectivity, so traditional indexes are not typically effective for analytical queries.

ColumnStore uses extent elimination to achieve high performance, without requiring manually created indexes. ColumnStore automatically partitions all data into [extents](columnstore-storage-architecture.md#extents). ColumnStore stores the minimum and maximum values for each extent in the [extent map](columnstore-storage-architecture.md#extent-map). ColumnStore uses the minimum and maximum values in the extent map to perform extent elimination.

When ColumnStore performs extent elimination, it compares the query's join conditions and filter conditions (i.e., WHERE clause) to the minimum and maximum values for each extent in the extent map. If the extent's minimum and maximum values fall outside the bounds of the query's conditions, ColumnStore skips that extent for the query.

Extent elimination is automatically performed for every query. It can significantly decrease I/O for columns with clustered values. For example, extent elimination works effectively for series, ordered, patterned, and time-based data.

## Custom Select Handler

The ColumnStore storage engine plugin implements a custom select handler to fully take advantage of ColumnStore's capabilities.

All storage engines interact with ES using an internal handler API, which is highly extensible. Storage engines can implement different features by implementing different methods within the handler API.

For select statements, the handler API transforms each query into a `SELECT_LEX` object, which is provided to the select handler.

The generic select handler is not optimal for ColumnStore, because:

* ColumnStore selects data by column, but the generic selects handler selects data by row
* ColumnStore supports parallel query evaluation, but the generic select handler does not
* ColumnStore supports distributed aggregations, but the generic select handler does not
* ColumnStore supports distributed functions, but the generic select handler does not
* ColumnStore supports extent elimination, but the generic select handler does not
* ColumnStore has its own query planner, but the generic select handler cannot use it

## Smart Storage Engine

The ColumnStore storage engine plugin is known as a smart storage engine, because it implements a custom select handler. MariaDB ColumnStore integrates with MariaDB Enterprise Server using the ColumnStore storage engine plugin. The ColumnStore storage engine plugin enables MariaDB Enterprise Server to interact with ColumnStore tables.

If a storage engine implements a custom select handler, it is known as a smart storage engine.

As a smart storage engine, the ColumnStore storage engine plugin tightly integrates ColumnStore with ES, but it has enough independence to efficiently execute analytical queries using a completely unique approach.

### Configure the Select Handler

The ColumnStore storage engine can use either the custom select handler or the generic select handler. The select handler can be configured using the `columnstore_select_handler` system variable:

| Value | Description                                                                                                                                                                                                                                 |
| ----- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AUTO  | <ul><li>When set to <code>AUTO</code>, ColumnStore automatically chooses the best select handler for a given SELECT query.</li><li><code>AUTO</code> was added in ColumnStore 6.</li></ul>                            |
| OFF   | <ul><li>When set to <code>OFF</code>, ColumnStore uses the generic select handlers for all <code>SELECT</code> queries.</li><li>It is not recommended to use this value, unless recommended by MariaDB Support.</li></ul>        |
| ON    | <ul><li>When set to <code>ON</code>, ColumnStore uses the custom select handlers for all <code>SELECT</code> queries.</li><li><code>ON</code> is the default.</li></ul> |

### Unsupported SQL Syntax and Fallback Behavior

The custom select handler translates each query's internal structure into a ColumnStore Execution Plan (CSEP). If a `SELECT` query uses syntax that the custom select handler does not support, the behavior depends on the value of the `columnstore_select_handler` system variable:

* When set to `AUTO`, ColumnStore falls back to the generic select handler, and MariaDB Enterprise Server executes the query itself. The query completes and raises warning code `9999`, with a message such as `MCS select_handler execution failed, falling back to server execution`. Run `SHOW WARNINGS` after the query to see the warning.
* When set to `ON` (the default), the query fails with an error instead of falling back.

When a query falls back, the server performs the joins, aggregation, `ORDER BY`, `LIMIT`, and expression evaluation itself, on rows streamed from ColumnStore, so the query loses distributed aggregation and distributed function evaluation. Per-table work still happens inside ColumnStore: it reads only the columns the query needs, applies the conditions the server pushes down, and still performs [extent elimination](mariadb-enterprise-columnstore-query-evaluation.md#extent-elimination) on them. Treat warning `9999` as a signal to check whether the query can be rewritten using syntax the custom select handler supports.

{% hint style="info" %}
The custom select handler translates the query's internal structure into a CSEP rather than forwarding the original SQL text. Syntax added in a newer MariaDB Server release is translated without any change to ColumnStore when the change is purely syntactical and the internal item types stay the same. ColumnStore needs explicit support when the change alters an item type, uses a new item attribute, or moves an attribute — in that case, support can lag behind the server release that added the syntax.
{% endhint %}

## Joins

MariaDB ColumnStore performs join operations using hash joins.

By default, hash joins are performed in memory.

### Configure In-Memory Joins

MariaDB ColumnStore can be configured to allocate more memory for hash joins.

The relevant configuration options are:

| Section  | Option               | Description                                                                                                                                                                                                                                                                                                 |
| -------- | -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HashJoin | PmMaxMemorySmallSide | <ul><li>Configures the amount of memory available for a single join.</li><li>Valid values are from <code>0</code> to <code>4</code> GB.</li><li>Default value is <code>1</code> GB.</li></ul>                                                                                                               |
| HashJoin | TotalUmMemory        | <ul><li>Configures the amount of memory available for all joins.</li><li>Values can be specified as a percentage of total system memory or as a specific amount of memory.</li><li>Valid percentage values are from <code>0</code> to <code>100%</code></li><li>Default value is <code>25%</code></li></ul> |

For example, to configure ColumnStore to use more memory for hash joins using the mcsSetConfig utility:

```sql
$ mcsSetConfig HashJoin PmMaxMemorySmallSide 2G
$ mcsSetConfig HashJoin TotalUmMemory '40%'
```

### Configure Disk-Based Joins

MariaDB Enterprise ColumnStore can be configured to perform disk-based joins.

The relevant configuration options are:

| Section      | Option              | Description                                                                                                                                                                           |
| ------------ | ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| HashJoin     | AllowDiskBasedJoin  | <ul><li>Enables disk-based joins</li><li>Valid values are <code>Y</code> and <code>N</code></li><li>Default value is <code>N</code></li></ul>                                         |
| HashJoin     | TempFileCompression | <ul><li>Enables compression for temporary files used by disk-based joins</li><li>Valid values are <code>Y</code> and <code>N</code></li><li>Default value is <code>N</code></li></ul> |
| SystemConfig | SystemTempFileDir   | <ul><li>Configures the directory used for temporary files used by disk-based joins and aggregations</li><li>Default value is <code>/tmp/columnstore_tmp_files</code></li></ul>        |

For example, to configure Enterprise ColumnStore to perform disk-based joins using the `mcsSetConfig` utility:

```bash
mcsSetConfig HashJoin AllowDiskBasedJoin Y
mcsSetConfig HashJoin TempFileCompression Y
mcsSetConfig SystemConfig SystemTempFileDir /mariadb/tmp
```

## Aggregations

MariaDB Enterprise ColumnStore performs aggregation operations on all nodes in a distributed manner, and then all nodes send their results to a single node, which combines the results and performs the final aggregation.

By default, aggregation operations are performed in memory.

### Configure Disk-Based Aggregations

In Enterprise ColumnStore 5.6.1 and later, disk-based aggregations can be configured.

The relevant configuration options are:

| Section        | Option                    | Description                                                                                                                                                                           |
| -------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| RowAggregation | AllowDiskBasedAggregation | <ul><li>Enables disk-based joins</li><li>Valid values are <code>Y</code> and <code>N</code></li><li>Default value is <code>N</code></li></ul>                                         |
| RowAggregation | Compression               | <ul><li>Enables compression for temporary files used by disk-based joins</li><li>Valid values are <code>Y</code> and <code>N</code></li><li>Default value is <code>N</code></li></ul> |
| SystemConfig   | SystemTempFileDir         | <ul><li>Configures the directory used for temporary files used by disk-based joins and aggregations</li><li>Default value is <code>/tmp/columnstore_tmp_files</code></li></ul>        |

For example, to configure Enterprise ColumnStore to perform disk-based aggregations using the `mcsSetConfig` utility:

```sql
$ mcsSetConfig RowAggregation AllowDiskBasedAggregation Y
$ mcsSetConfig RowAggregation Compression SNAPPY
$ mcsSetConfig SystemConfig SystemTempFileDir /mariadb/tmp
```

## Query Planning

The ColumnStore storage engine plugin is a smart storage engine, so MariaDB Enterprise ColumnStore to plan its own queries using the [custom select handler](mariadb-enterprise-columnstore-query-evaluation.md#custom-select-handler).

MariaDB Enterprise ColumnStore's query planning is divided into two steps:

* ES provides the query's `SELECT_LEX` object to the [custom select handler](mariadb-enterprise-columnstore-query-evaluation.md#custom-select-handler). The custom select handler builds a ColumnStore Execution Plan (CSEP).
* The custom select handler provides the CSEP to the [ExeMgr process or facility](mariadb-enterprise-columnstore-query-evaluation.md#exemgr-process-facility) on the same node. ExeMgr performs [extent elimination](mariadb-enterprise-columnstore-query-evaluation.md#extent-elimination) and creates a job list.

## ExeMgr Process/Facility

The ColumnStore storage engine provides the CSEP to the ExeMgr process or facility on the same node, which will act as the initiator/aggregator node for the query.

Starting with MariaDB Enterprise ColumnStore 22.08, the ExeMgr facility has been integrated into the PrimProc process, so it is no longer a separate process.

ExeMgr performs multiple tasks:

* Performs extent elimination.
* Views the optimizer statistics.
* Transforms the CSEP to a job list, which consists of job steps.
* Assigns distributed job steps to the PrimProc process on each node.
* Evaluates non-distributed job steps itself.
* Provides final query results to ES.

## Query Evaluation Process

![ECStore-QueryExecutionwith-S3-FlowChart](<../../.gitbook/assets/ecstore-queryexecutionwith-s3-flowchart (1).png>)

When Enterprise ColumnStore executes a query, it goes through the following process:

1. The client or application sends the query to MariaDB MaxScale's listener port.
2. The query is processed by the Read/Write Split Router (`readwritesplit`) service associated with the listener.
3. The service routes the query to the ES TCP port on a ColumnStore node.
4. MariaDB Enterprise Server (ES) evaluates the query using the handler interface.

* The handler interface builds a `SELECT_LEX` object to represent the query.
* The handler interface provides the `SELECT_LEX` object to the ColumnStore storage engine's select handler.
* The select handler transforms the `SELECT_LEX` object into a ColumnStore Execution Plan (CSEP).
* The select handler provides the CSEP to the ExeMgr facility on the same node, which will act as the initiator/aggregator node for the query.

5. `ExeMgr` transforms the CSEP into a job list, which consists of job steps.
6. `ExeMgr` evaluates each job step sequentially.

* If it is a non-distributed job step, `ExeMgr` evaluates the job step itself.
* If it is a distributed job step, `ExeMgr` provides the job step to the PrimProc process on each node. The PrimProc process on each node evaluates the job step in a multi-threaded manner using a thread pool. After the PrimProc process on each node evaluates its job step, the results are returned to `ExeMgr` on the initiator/aggregator node as a Row Group.

7. After all job steps are evaluated, `ExeMgr` returns the results to ES.
8. ES returns the results to MaxScale.
9. MaxScale returns the results to the client or application.

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
