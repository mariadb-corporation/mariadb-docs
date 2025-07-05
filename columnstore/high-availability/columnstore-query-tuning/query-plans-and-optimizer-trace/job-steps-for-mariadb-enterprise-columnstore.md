---
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Job Steps

## Overview

When Enterprise ColumnStore executes a query, the [ExeMgr process](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#exemgr-processfacility) on the initiator/aggregator node translates the ColumnStore execution plan (CSEP) into a job list. A job list is a sequence of job steps.

Enterprise ColumnStore uses many different types of job steps that provide different scalability benefits:

* Some types of job steps perform operations in a distributed manner, using multiple nodes to operate to different extents. Distributed operations provide horizontal scalability.
* Some types of job steps perform operations in a multi-threaded manner using a thread pool. Performing multi-threaded operations provides vertical scalability.

As you increase the number of ColumnStore nodes or the number of cores on each node, Enterprise ColumnStore can use those resources to more efficiently execute job steps.

For additional information, see "[MariaDB Enterprise ColumnStore Query Evaluation](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md).".

## Batch Primitive Step (BPS)

Enterprise ColumnStore defines a **batch primitive** step to handle many types of tasks, such as scanning/filtering columns, JOIN operations, aggregation, functional filtering, and projecting (putting values into a `SELECT` list).

In `calGetTrace()` output, a batch primitive step is abbreviated BPS.

Batch primitive steps are evaluated on multiple nodes in parallel. The PrimProc process on each node evaluates the batch primitive step to one extent at a time. The PrimProc process uses a thread pool to operate on individual blocks within the extent in parallel.

## Cross Engine Step (CES)

Enterprise ColumnStore defines a **cross-engine** step to perform cross-engine joins, in which a ColumnStore table is joined with a table that uses a different storage engine.

In `calGetTrace()` output, a cross-engine step is abbreviated CES.

Cross-engine steps are evaluated locally by the ExeMgr process on the initiator/aggregator node.

Enterprise ColumnStore can perform cross-engine joins when the mandatory utility user is properly configured.

For additional information, refer to the "Mandatory Utility User Account."

## Dictionary Structure Step (DSS)

Enterprise ColumnStore defines a **dictionary structure** step to scan the dictionary extents that ColumnStore uses to store variable-length string values.

In `calGetTrace()` output, a dictionary structure step is abbreviated DSS.

Dictionary structure steps are evaluated on multiple nodes in parallel. The PrimProc process on each node evaluates the dictionary structure step to one extent at a time. It uses a thread pool to operate on individual blocks within the extent in parallel.

Dictionary structure steps can require a lot of I/O for a couple of reasons:

* Dictionary structure steps do not support extent elimination, so all extents for the column must be scanned.
* Dictionary structure steps must read the column extents to find each pointer and the dictionary extents to find each value, so it doubles the number of extents to scan.

It is generally recommended to avoid queries that will cause dictionary scans.

For additional information, see "Avoid Creating Long String Columns".

## Hash Join Step (HJS)

Enterprise ColumnStore defines a **hash join** step to perform a hash join between two tables.

In `calGetTrace()` output, a hash join step is abbreviated HJS.

Hash join steps are evaluated locally by the ExeMgr process on the initiator/aggregator node.

Enterprise ColumnStore performs the hash join in memory by default. If you perform large joins, you may be able get better performance by changing some configuration defaults with mcsSetConfig:

* Enterprise ColumnStore can be configured to use more memory for in-memory hash joins.
* Enterprise ColumnStore can be configured to use disk-based joins.

For additional information, see "[Configure in-memory joins](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-in-memory-joins)" and "[Configure Disk-Based Joins](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-disk-based-joins)".

## Having Step (HVS)

Enterprise ColumnStore defines a **having step** to evaluate a HAVING clause on a result set.

In `calGetTrace()` output, a having step is abbreviated HVS.

## Subquery Step (SQS)

Enterprise ColumnStore defines a subquery step to evaluate a subquery.

In calGetTrace() output, a subquery step is abbreviated SQS.

## Tuple Aggregation Step (TAS)

Enterprise ColumnStore defines a **tuple aggregation** step to collect intermediate aggregation prior to the final aggregation and evaluation of the results.

In `calGetTrace()` output, a tuple aggregation step is abbreviated TAS.

Tuple aggregation steps are primarily evaluated by the ExeMgr process on the initiator/aggregator node. However, the PrimProc process on each node also plays a role, since the PrimProc process on each node provides the intermediate aggregation results to the ExeMgr process on the initiator/aggregator node.

## Tuple Annexation Step (TNS)

Enterprise ColumnStore defines a **tuple annexation** step to perform the final aggregation and evaluation of the results.

In `calGetTrace()` output, a tuple annexation step is abbreviated TNS.

Tuple annexation steps are evaluated locally by the ExeMgr process on the initiator/aggregator node.

Enterprise ColumnStore 5 performs aggregation operations in memory. As a consequence, more complex aggregation operations require more memory in that version.

In Enterprise ColumnStore 6, disk-based aggregations can be enabled.

For additional information, see "[Configure Disk-Based Aggregations](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#configure-disk-based-aggregations)".

## Tuple Union Step (TUS)

Enterprise ColumnStore defines a **tuple union** step to perform a union of two subqueries.

In `calGetTrace()` output, a tuple union step is abbreviated TUS.

Tuple union steps are evaluated locally by the ExeMgr process on the initiator/aggregator node.

## Tuple Constant Step (TCS)

Enterprise ColumnStore defines a tuple constant step to evaluate constant values.

In calGetTrace() output, a tuple constant step is abbreviated TCS.

Tuple constant steps are evaluated locally by the ExeMgr process on the initiator/aggregator node.

## Window Function Step (WFS)

Enterprise ColumnStore defines a **window function** step to evaluate window functions.

In `calGetTrace()` output, a window function step is abbreviated WFS.

Window function steps are evaluated locally by the [ExeMgr process](../../../architecture/mariadb-enterprise-columnstore-query-evaluation.md#exemgr-processfacility) on the initiator/aggregator node.

<sub>_This page is: Copyright © 2025 MariaDB. All rights reserved._</sub>

{% @marketo/form formId="4316" %}
