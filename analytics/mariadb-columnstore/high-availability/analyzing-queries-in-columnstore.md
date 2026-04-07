# Analyzing Queries

## Determining Active Queries

### SHOW PROCESSLIST

The MariaDB `SHOW PROCESSLIST` statement is used to see a list of active queries on that UM:

```sql
MariaDB [test]> SHOW PROCESSLIST;
+----+------+-----------+-------+---------+------+-------+--------------+
| Id | User | Host | db | Command | Time | State | Info |
+----+------+-----------+-------+---------+------+-------+--------------+
| 73 | root | localhost | ssb10 | Query | 0 | NULL | show processlist
+----+------+-----------+-------+---------+------+-------+--------------+
1 row in set (0.01 sec)
```

### getActiveSQLStatements

_getActiveSQLStatements_ is a mcsadmin command that shows which SQL statements are currently being executed on the database:

```sql
mcsadmin> getActiveSQLStatements
getactivesqlstatements Wed Oct 7 08:38:32 2015
Get List of Active SQL Statements
=================================
Start Time    Time (hh:mm:ss) Session ID SQL Statement
---------------- ---------------- -------------------- ------------------------------------------------------------
Oct 7 08:38:30    00:00:03       73 select c_name,sum(lo_revenue) from customer, lineorder where lo_custkey = c_custkey and c_custkey = 6 group by c_name
```

## Analysis of Individual Queries

### Query Statistics

The `calGetStats` function provides statistics about resources used on the node, and network by the last run query. To collect query statistics across sessions and store them for analysis, see [Query Statistics for MariaDB Enterprise ColumnStore](columnstore-query-tuning/query-statistics-for-mariadb-enterprise-columnstore.md).

Example:

```sql
MariaDB [test]> SELECT count(*) FROM wide2;
+----------+                                       
| count(*) |
+----------+
|  5000000 |
+----------+
1 row in set (0.22 sec)

MariaDB [test]> SELECT calGetStats();
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| calGetStats()                                                                                                                                                                                     |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Query Stats: MaxMemPct-0; NumTempFiles-0; TempFileSpace-0B; ApproxPhyI/O-1931; CacheI/O-2446; BlocksTouched-2443; PartitionBlocksEliminated-0; MsgBytesIn-73KB; MsgBytesOut-1KB; Mode-Distributed |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
1 row in set (0.01 sec)
```

The output contains information on:

* **MaxMemPct** - Peak memory utilization on the [User Module](../architecture/columnstore-user-module.md), likely in support of a large (User Module) based hash join operation.
* **NumTempFiles** - Report on any temporary files created in support of query operations larger than available memory, typically for unusual join operations where the smaller table join cardinality exceeds some configurable threshold.
* **TempFileSpace** - Report on space used by temporary files created in support of query operations larger than available memory, typically for unusual join operations where the smaller table join cardinality exceeds some configurable threshold.
* **PhyI/O** - Number of 8k blocks read from disk, SSD, or other persistent storage.
* **CacheI/O** - Approximate number of 8k blocks processed in memory, adjusted down by the number of discrete PhyI/O calls required.
* **BlocksTouched** - Approximate number of 8k blocks processed in memory.
* **PartitionBlocksEliminated** - The number of block touches eliminated via the Extent Map elimination behavior.
* **MsgBytesIn, MsgByteOut** - Message size in MB sent between nodes in support of the query.

The output is useful to determine how much physical I/O was required, how much data was cached, and how many partition blocks were eliminated through use of extent map elimination. The system maintains min / max values for each extent and uses these to help implement where clause filters to completely bypass extents where the value is outside of the min/max range. When a column is ordered (or semi-ordered) during load such as a time column this offer very large performance gains as the system can avoid scanning many extents for the column.

For additional details about enabling query statistics, required privileges, and historical analysis, see [Query Statistics for MariaDB Enterprise ColumnStore](columnstore-query-tuning/query-statistics-for-mariadb-enterprise-columnstore.md).&#x20;

## Query Plan / Trace

While the MariaDB Server's [EXPLAIN](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/analyze-and-explain-statements/explain) utility can be used to look at the query plan, it is somewhat less helpful for ColumnStore tables as ColumnStore does not use indexes or make use of MariaDB I/O functionality.\
The execution plan for a query on a ColumnStore table is made up of multiple steps. Each step in the query plan performs a set of operations that are issued from the [User Module](../architecture/columnstore-user-module.md) to the set of [Performance Modules](../architecture/columnstore-performance-module.md) in support of a given step in a query.

* Full Column Scan - an operation that scans each entry in a column using all available threads on the Performance Modules. Speed of operation is generally related to the size of the data type and the total number of rows in the column. The closest analogy for a traditional system is an index scan operation.
* Partitioned Column Scan - an operation that uses the Extent Map to identify that certain portions of the column do not contain any matching values for a given set of filters. The closest analogy for a traditional row-based DBMS is a partitioned index scan, or partitioned table scan operation.
* Column lookup by row offset - once the set of matching filters have been applied and the minimal set of rows have been identified; additional blocks are requested using a calculation that determines exactly which block is required. The closest analogy for a traditional system is a lookup by `rowid`.

These operations are automatically executed together in order to execute appropriate filters and column lookup by row offset.

### Viewing the ColumnStore Query Plan

In MariaDB ColumnStore there is a set of SQL tracing stored functions provided to see the distributed query execution plan between the nodes.

The basic steps to using these SQL tracing stored functions are:

1. Start the trace for the particular session.
2. Execute the SQL statement in question.
3. Review the trace collected for the statement.\
   As an example, the following session starts a trace, issues a query against a 6 million row fact table and 300,000 row dimension table, and then reviews the output from the trace:

```sql
MariaDB [test]> SELECT calSetTrace(1);
+----------------+
| calSetTrace(1) |
+----------------+
|              0 |
+----------------+
1 row in set (0.00 sec)

MariaDB [test]> SELECT c_name, sum(o_totalprice)
    -> FROM customer, orders
    -> WHERE o_custkey = c_custkey
    -> AND c_custkey = 5
    -> GROUP BY c_name;
+--------------------+-------------------+
| c_name             | sum(o_totalprice) |
+--------------------+-------------------+
| Customer#000000005 |         684965.28 |
+--------------------+-------------------+
1 row in set, 1 warning (0.34 sec)

MariaDB [test]> SELECT calGetTrace();
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    --------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    ----------------------------------------------------------------------------------------------------------+
| calGetTrace()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    --------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    ----------------------------------------------------------------------------------------------------------+
|
Desc Mode Table           TableOID ReferencedColumns        PIO LIO PBE Elapsed Rows
BPS  PM   customer        3024     (c_custkey,c_name)       0   43  36  0.006   1
BPS  PM   orders          3038     (o_custkey,o_totalprice) 0   766 0   0.032   3
HJS  PM   orders-customer 3038     -                        -   -   -   -----   -
TAS  UM   -               -        -                        -   -   -   0.021   1
 |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    --------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                                                                                    ----------------------------------------------------------------------------------------------------------+
1 row in set (0.00 sec)
```

The columns headings in the output are as follows:

* Desc – Operation being executed. Possible values:
  * **BPS - Batch Primitive Step**: scanning or projecting the column blocks.
  * **CES - Cross Engine Step**: Performing Cross engine join
  * **DSS - Dictionary Structure Step**: a dictionary scan for a particular variable length string value.
  * **HJS - Hash Join Step**: Performing a hash join between 2 tables
  * **HVS - Having Step**: Performing the having clause on the result set
  * **SQS - Sub Query Step**: Performing a sub query
  * **TAS - Tuple Aggregation step**: the process of receiving intermediate aggregation results from other nodes.
  * **TNS - Tuple Annexation Step**: Query result finishing, e.g. filling in constant columns, limit, order by and final distinct cases.
  * **TUS = Tuple Union step**: Performing a SQL union of 2 sub queries.
  * **TCS = Tuple Constant Step**: Process Constant Value Columns
  * **WFS = Window Function Step**: Performing a window function.
* **Mode –** Where the operation was performed within the PrimProc[^1] library
* **Table** – Table for which columns may be scanned/projected.
* **TableOID – ObjectID** for the table being scanned.
* **ReferencedOIDs – ObjectIDs** for the columns required by the query.
* **PIO – Physical I/O** (reads from storage) executed for the query.
* **LIO – Logical I/O** executed for the query, also known as Blocks Touched.
* **PBE – Partition Blocks Eliminated** identifies blocks eliminated by Extent Map min/max.
* **Elapsed** – Elapsed time for a give step.
* **Rows** – Intermediate rows returned.

{% hint style="info" %}
**Note:** The time recorded is the time from PrimProc[^2] and `ExeMgr`. Execution time from withing mysqld is not tracked here. There could be extra processing time in `mysqld` due to a number of factors such as `ORDER BY`.
{% endhint %}

## Cache Clearing to Enable Cold Testing

Sometimes it can be useful to clear caches to allow understanding of un-cached and cached query access. The `calFlushCache()` function will clear caches on all servers. This is only really useful for testing query performance:

```sql
MariaDB [test]> SELECT calFlushCache();
```

## Viewing Extent Map Information

It can be useful to view details about the extent map for a given column. This can be achieved using the edit item process on any ColumnStore server. Available arguments can be provided by using the `-h` flag. The most common use is to provide the column object id with the `-o` argument which will output details for the column and in this case the `-t` argument is provided to show min / max values as dates:

```sql
editem -o 3032 -t
Col OID = 3032, NumExtents = 10, width = 4
428032 - 432127 (4096) min: 1992-01-01, max: 1993-06-21, seqNum: 1, state: valid, fbo: 0, DBRoot: 1, part#: 0, seg#: 0, HWM: 0; status: avail
502784 - 506879 (4096) min: 1992-01-01, max: 1993-06-22, seqNum: 1, state: valid, fbo: 0, DBRoot: 2, part#: 0, seg#: 1, HWM: 0; status: unavail
708608 - 712703 (4096) min: 1993-06-21, max: 1994-12-11, seqNum: 1, state: valid, fbo: 0, DBRoot: 1, part#: 0, seg#: 2, HWM: 0; status: unavail
766976 - 771071 (4096) min: 1993-06-22, max: 1994-12-12, seqNum: 1, state: valid, fbo: 0, DBRoot: 2, part#: 0, seg#: 3, HWM: 0; status: unavail
989184 - 993279 (4096) min: 1994-12-11, max: 1996-06-01, seqNum: 1, state: valid, fbo: 4096, DBRoot: 1, part#: 0, seg#: 0, HWM: 8191; status: avail
1039360 - 1043455 (4096) min: 1994-12-12, max: 1996-06-02, seqNum: 1, state: valid, fbo: 4096, DBRoot: 2, part#: 0, seg#: 1, HWM: 8191; status: avail
1220608 - 1224703 (4096) min: 1996-06-01, max: 1997-11-22, seqNum: 1, state: valid, fbo: 4096, DBRoot: 1, part#: 0, seg#: 2, HWM: 8191; status: avail
1270784 - 1274879 (4096) min: 1996-06-02, max: 1997-11-22, seqNum: 1, state: valid, fbo: 4096, DBRoot: 2, part#: 0, seg#: 3, HWM: 8191; status: avail
1452032 - 1456127 (4096) min: 1997-11-22, max: 1998-08-02, seqNum: 1, state: valid, fbo: 0, DBRoot: 1, part#: 1, seg#: 0, HWM: 1930; status: avail
1510400 - 1514495 (4096) min: 1997-11-22, max: 1998-08-02, seqNum: 1, state: valid, fbo: 0, DBRoot: 2, part#: 1, seg#: 1, HWM: 1930; status: avail
```

Here it can be seen that the extent maps for the `o_orderdate` (object id 3032) column are well partitioned since the order table source data was sorted by the `order_date`. This example shows 2 separate DBRoot values as the environment was a 2-node combined deployment.

Column object ids may be found by querying the `calpontsys.syscolumn` metadata table (deprecated) or `information_schema.columnstore_columns` table (version 1.0.6+).

## Query Statistics History

MariaDB ColumnStore query statistics history can be retrieved for analysis. By default the query stats collection is disabled. To enable the collection of query stats, the element in the `ColumnStore.XML` configuration file should be set to Y (default is N).

```sql
<QueryStats>
<Enabled>Y</Enabled>
</QueryStats>
```

Cross Engine Support must also be enabled before enabling Query Statistics. See the [Cross Engine Configuration](../management/managing-columnstore-database-environment/configuring-columnstore-cross-engine-joins.md) section.

For Querystats Cross Engine User needs INSERT Privilege on querystats table.

Example:

```sql
grant INSERT on infinidb_querystats.querystats to 'cross_engine'@'127.0.0.1';
grant INSERT on infinidb_querystats.querystats to 'cross_engine'@'localhost';
```

When enabled the history of query statistics across all sessions along with execution time, and those stats provided by `calgetstats()` is stored in a table in the `infinidb_querystats` schema. Only queries in the following ColumnStore syntax are available for statistics monitoring:

* `SELECT`
* `INSERT`
* `UPDATE`
* `DELETE`
* `INSERT ... SELECT`
* `LOAD DATA INFILE`

## Query Statistics Table

When QueryStats is enabled, the query statistics history is collected in the `querystats` table in the `infinidb_querystats` schema.

The columns of this table are:

* **queryID** - A unique identifier assigned to the query
* **Session ID** (sessionID) - The session number that executed the statement.
* **queryType** - The type of the query whether insert, update, delete, select, delete, insert select or load data infile
* **query** - The text of the query
* **Host** (host) - The host that executed the statement.
* **User ID** (user) - The user that executed the statement.
* **Priority** (priority) The priority the user has for this statement.
* **Query Execution Times** (startTime, endTime) Calculated as end time – start time.
  * **start time** - the time that the query gets to ExeMgr, DDLProc, or DMLProc
  * **end time** - the time that the last result packet exits ExeMgr, DDLProc or DMLProc
* **Rows returned or affected** (rows) -The number of rows returned for `SELECT` queries, or the number of rows affected by DML queries. Not valid for DDL and other query types.
* **Error Number** (errNo) - The IDB error number if this query failed, 0 if it succeeded.
* **Physical I/O** (phyIO) - The number of blocks that the query accessed from the disk, including the pre-fetch blocks. This statistic is only valid for the queries that are processed by ExeMgr, i.e. `SELECT`, `DML` with `WHERE` clause, and `INSERT SELECT`.
* **Cache I/O** (cacheIO) - The number of blocks that the query accessed from the cache. This statistic is only valid for queries that are processed by ExeMgr, i.e. `SELECT`, `DML` with `WHERE` clause, and `INSERT SELEC`T.
* **Blocks Touched** (blocksTouched) - The total number of blocks that the query accessed physically and from the cache. This should be equal or less than the sum of physical I/O and cache I/O. This statistic is only valid for queries that are processed by ExeMgr, i.e. `SELECT`, `DML` with `WHERE` clause, and `INSERT SELECT`.
* **Partition Blocks Eliminated** (CPBlocksSkipped) - The number of blocks being eliminated by the extent map casual partition. This statistic is only valid for queries that are processed by ExeMgr, i.e. `SELECT`, `DML` with `WHERE` clause, and `INSERT SELECT`.
* **Messages to other nodes** (`msgOutUM`) - The number of messages in bytes that ExeMgr sends to the PrimProc[^2]. If a message needs to be distributed to all the PMs, the sum of all the distributed messages will be counted. Only valid for queries that are processed by ExeMgr, i.e. `SELECT`, `DML` with `WHERE` clause, and `INSERT SELECT`.
* **Messages from other nodes** (`msgInUM`) - The number of messages in bytes that PrimProc[^2] sends to the ExeMgr. Only valid for queries that are processed by `ExeMgr`, i.e. `SELECT`, `DML` with where clause, and `INSERT SELECT`.
* **Memory Utilization** (`maxMemPct`) - This field shows memory utilization in support of any join, group by, aggregation, distinct, or other operation.
* **Blocks Changed** (`blocksChanged`) - Total number of blocks that queries physically changed on disk. This is only for delete/update statements.
* **Temp Files** (`numTempFiles`) - This field shows any temporary file utilization in support of any join, group by, aggregation, distinct, or other operation.
* **Temp File Space** (`tempFileSpace`) - This shows the size of any temporary file utilization in support of any join, group by, aggregation, distinct, or other operation.

## Query Statistics Viewing

Users can view the query statistics by selecting the rows from the query stats table in the `infinidb_querystats` schema. Examples listed below:

* Example 1: List execution time, rows returned for all the select queries within the past 12 hours:

```sql
MariaDB [infinidb_querystats]> select queryid, query, endtime-starttime, rows from querystats 
where starttime >= now() - interval 12 hour and querytype = 'SELECT';
```

* Example 2: List the three slowest running select queries of session 2 within the past 12 hours:

```sql
MariaDB [infinidb_querystats]> select a.* from (select endtime-starttime execTime, query from queryStats 
where sessionid = 2 and querytype = 'SELECT' and starttime >= now()-interval 12 hour
order by 1 limit 3) a;
```

* Example 3: List the average, min and max running time of all the INSERT SELECT queries within the past 12 hours:

```sql
MariaDB [infinidb_querystats]> select min(endtime-starttime), max(endtime-starttime), avg(endtime-starttime) from querystats 
where querytype='INSERT SELECT' and starttime >= now() - interval 12 hour;
```

## See Also

* [Query Statistics for MariaDB Enterprise ColumnStore](columnstore-query-tuning/query-statistics-for-mariadb-enterprise-columnstore.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}

[^1]: PrimProc is the ColumnStore Primitives Processor

[^2]: PrimProc is the ColumnStore Primitives Processor.
