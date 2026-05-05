---
description: >-
  Performance concepts for MariaDB ColumnStore: PrimProc query optimization
  and orchestration, Extent Map metadata for I/O reduction, batch primitive
  steps, and shared storage for failover.
---

# Performance Concepts

## Introduction

The high level components of the ColumnStore architecture are:

* **PrimProc:** PrimProc (Primitives Processor) is responsible for parsing the SQL requests into an optimized set of primitive job steps executed by one or more servers. PrimProc is thus responsible for query optimization and orchestration of query execution by the servers. While every instance has their own PrimProc in a multi-server deployment, each query begins and ends on the same PrimProc it originated from. A database load balancer such as MariaDB MaxScale can be deployed to appropriately balance external requests against individual servers. PrimProc also executes granular job steps received from the server (mariadbd) in a multi-threaded manner. ColumnStore allows distribution of the work across many servers.
* **Extent Maps:** ColumnStore maintains metadata about each column in a shared distributed object known as the Extent Map. The primary node references the Extent Map to help assist in generating the correct primitive job steps. The primary node server references the Extent Map to identify the correct disk blocks to read. Each column is made up of one or more files and each file can contain multiple extents. As much as possible the system attempts to allocate contiguous physical storage to improve read performance.
* **Storage:** ColumnStore can use either local storage or shared storage (e.g. SAN or EBS) to store data. Using shared storage allows for data processing to fail over to another node automatically in case of a server failing.

## Data Loading

The system supports full MVCC ACID transactional logic via Insert, Update, and Delete statements. The MVCC architecture allows for concurrent query and DML / batch load. Although DML is supported, the system is optimized more for batch inserts and so larger data loads should be achieved through a batch load. The most flexible and optimal way to load data is via the cpimport tool. This tool optimizes the load path and can be run centrally or in parallel on each server.

If the data contains a time or (time correlated ascending value) column then significant performance gains will be achieved if the data is sorted by this field and also typically queried with a where clause on that column. This is because the system records a minimum and maximum value for each extent providing for a system maintained range partitioning scheme. This allows the system to completely eliminate scanning an extent map if the query includes a where clause for that field limiting the results to a subset of extent maps.

## Query Execution

MariaDB ColumnStore has its own query optimizer and execution engine distinct from the MariaDB server implementation. This allows for scaling out query execution to multiple servers, and to optimize for handling data stored as columns rather than rows. As such, the factors influencing query performance are very different:

A query is first parsed by the MariaDB server (mariadbd) process and passed through to the ColumnStore storage engine. This passes the request onto the PrimProc[^1] process which is responsible for optimizing and orchestrating execution of the query. The PrimProc module's optimizer creates a series of batch primitive steps that are executed on all nodes in the cluster. Since multiple servers can be deployed, this allows for scale-out execution of the queries. The optimizer attempts to process query execution in parallel. However, certain operations inherently must be executed centrally, for example final result ordering. Filtering, joins, aggregates, and `GROUP BY` clauses are general.y pushed down and executed in parallel in PrimProc on all servers. In PrimProc, batch primitive steps are performed at a granular level where individual threads operate on individual 1K-8K blocks within an extent. This enables a larger multi-core server to be fully consumed and scale out within a single server. The current batch primitive steps available in the system include:

* **Single Column Scan:** Scan one or more Extents for a given column based on a single column predicate, including operators like `=`, `<>`, `IN (list)`, `BETWEEN`, and `ISNULL`. See the first scan section of [performance configuration](mariadb-columnstore-performance-related-configuration-settings.md) for additional details on tuning this.
* **Additional Single Column Filters:** Project additional columns for any rows found by a previous scan and apply additional single column predicates as needed. Access of blocks is based on row identifier, going directly to the blocks. See the additional column read section of [performance configuration](mariadb-columnstore-performance-related-configuration-settings.md) for additional details on tuning this.
* **Table Level Filters:** Project additional columns as required for any table level filters such as `column1 < column2`, or more advanced functions and expressions. Access of blocks is again based on row identifier, going directly to the blocks.
* **Project Join Columns for Joins:** Project additional join columns as needed for any join operations. Access of blocks is again based on row identifier, going directly to the blocks. See the join tuning section of [performance configuration](mariadb-columnstore-performance-related-configuration-settings.md) for additional details on tuning this.
* **Execute Multi-Join:** Apply one or more hash join operation against projected join columns, and use that value to probe a previously built hash map. Build out tuples as needed to satisfy inner or outer join requirements. See the multi-table join section of [performance configuration](mariadb-columnstore-performance-related-configuration-settings.md) for additional details on tuning this.
* **Cross-Table Level Filters:** Project additional columns from the range of rows for the Primitive Step as needed for any cross-table level filters such as `table1.column1 < table2.column2`, or more advanced functions and expressions. Access of blocks is again based on row identifier, going directly to the blocks.
* **Aggregation/Distinct Operation Part 1:** Apply any local group by, distinct, or aggregation operation against the set of joined rows assigned to a given Batch Primitive. Part 1 of this process is handled by PrimProc.
* **Aggregation/Distinct Operation Part 2:** Apply any final group by, distinct, or aggregation operation against the set of joined rows assigned to a given Batch Primitive. This processing is handled by PrimProc[^1]. See the memory management section of [performance configuration](mariadb-columnstore-performance-related-configuration-settings.md) for additional details on tuning this.

## ColumnStore Query Execution Paradigms

The following items should be considered when thinking about query execution in ColumnStore vs a row based store such as InnoDB.

### Data Scanning and Filtering

ColumnStore is optimized for large scale aggregation / OLAP queries over large data sets. As such indexes typically used to optimize query access for row based systems do not make sense since selectivity is low for such queries. Instead ColumnStore gains performance by only scanning necessary columns, utilizing system maintained partitioning, and utilizing multiple threads and servers to scale query response time.

Since ColumnStore only reads the necessary columns to resolve a query, only include the necessary columns required. For example, `SELECT *` is significantly slower than `SELECT col1, col2 FROM tbl`.

Datatype size is important. If say you have a column that can only have values 0 through 100 then declare this as a tinyint as this will be represented with 1 byte rather than 4 bytes for int. This reduces the I/O cost by 4 times.

For string types, an important threshold is `CHAR(9)` and `VARCHAR(8)` or greater. Each column storage file uses a fixed number of bytes per value. This enables fast positional lookup of other columns to form the row. Currently the upper limit for columnar data storage is 8 bytes. So. for strings longer than this, the system maintains an additional 'dictionary' extent where the values are stored. The columnar extent file then stores a pointer into the dictionary. For example, it is more expensive to read and process a `VARCHAR(8)` column than a `CHAR(8)` column. Where possible, you get better performance if you can utilize shorter strings, especially if you avoid the dictionary lookup. All `TEXT`/`BLOB` data types in ColumnStore 1.1 onward utilize a dictionary and do a multiple-block 8KB lookup to retrieve that data if required. The longer the data, the more blocks are retrieved, and the greater is a potential performance impact.

In a row-based system, adding redundant columns adds to the overall query cost, but in a columnar system a cost is only occurred if the column is referenced. Therefore, additional columns should be created to support different access paths. For instance, store a leading portion of a field in one column to allow for faster lookups, but additionally store the long-form value as another column. Scans on a shorter code or a leading-portion column are faster.

ColumnStore distributes function application across all nodes for greater performance, but this requires a distributed implementation of the function in addition to the MariaDB server implementation. See [Distributed Functions](../reference/columnstore-distributed-functions.md) for the full list.

{% hint style="info" %}
Its important to note that ColumnStore does not have a cost based optimizer, so for optimal extent elimination and performance, your first `WHERE` clause predicate order should be based on the same column order that the data is imported by. Example: Most use cases with a date column benefit from a natural sort. (Today's data are being inserted after yesterday's data.) Having the first column to filter by date helps efficiently filter through records. `WHERE DATE='x'` outperforms a query based on a column with random values as the first predicate. Compare different query plans using `calSetTrace` and `calGetTrace`. Optimizing for the lowest PIO/LIO and highest PBE. See also [CSEP](columnstore-query-tuning/query-plans-and-optimizer-trace/columnstore-execution-plan-csep-for-mariadb-enterprise-columnstore.md).
{% endhint %}

### Joins

Hash joins are utilized by ColumnStore to optimize for large scale joins and avoid the need for indexes and the overhead of nested loop processing. ColumnStore maintains table statistics so as to determine the optimal join order. This is implemented by first identifying the small table side (based on extent map data) and materializing the necessary rows from that table for the join. If the size of this is less than the configuration setting `PmMaxMemorySmallSide`, the join is pushed down into PrimProc[^1] for distributed in-memory processing. Otherwise, the larger side rows is not processed in a distributed manner for joining, and only the `WHERE` clause on that side is executed across all PrimProc modules in the cluster. If the join is too large for memory, disk-based join can be enabled to allow the query to complete.

### Aggregations

Similarly to scalar functions ColumnStore distributes aggregate evaluation as much as possible. However some post processing is required to combine the final results. Enough memory must exist to handle queries with a very large number of values in the aggregate columns.

Aggregation performance is also influenced by the number of distinct aggregate column values. Generally, the same number of rows with 100 distinct values computes faster than 10000 distinct values. This is due to increased memory management as well as transfer overhead.

{% hint style="info" %}
`SELECT COUNT()` is internally optimized to be `SELECT COUNT(COL-N)`, where `COL-N` is the column that uses the least number of bytes for storage. For example it would be pick a `CHAR(1)` column over int column because `CHAR(1)` uses 1 byte for storage and int uses 4 bytes. The implementation still honors ANSI semantics in that `SELECT COUNT()` will include nulls in the total count as opposed to an explicit `SELECT(COL-N)` which excludes `NULL` values in the count.
{% endhint %}

### ORDER BY and LIMIT

`ORDER BY` and `LIMIT` are implemented at the very end by the `mariadbd` server process on the temporary result set table. This means that the unsorted results must be fully retrieved before either are applied. The performance overhead of this is minimal on small to medium results, but for larger results, it can be significant.

### Complex Queries

Subqueries are executed in sequence thus the subquery intermediate results must be materialized and then the join logic applies with the outer query.

Window functions are executed as part of final aggregation in PrimProc[^1] due to the need for ordering of the window results. The ColumnStore window function engines uses a dedicated faster sort process.

### Partitioning

Automated system partitioning of columns is provided by ColumnStore. As data is loaded into extent maps, the system will capture and maintain min/max values of column data in that extent map. New rows are appended to each extent map until full at which point a new extent map is created. For column values that are ordered or semi-ordered this allows for very effective data partitioning. By using the min and max values, entire extent maps can be eliminated and not read to filter data. This generally works particularly well for time dimension / series data or similar values that increase over time.

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: PrimProc is the ColumnStore Primitives Processor.
