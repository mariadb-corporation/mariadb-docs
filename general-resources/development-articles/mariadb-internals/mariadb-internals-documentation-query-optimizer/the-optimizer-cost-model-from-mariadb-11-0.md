# The Optimizer Cost Model from MariaDB 11.0

## Background

Before [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110), the MariaDB Query optimizer used a 'basic cost' of 1 for:

* One disk access
* Fetching a key
* Fetching a row based on the rowid (= unique row identifier) from the key

There were some smaller costs:

* filter lookup: 0.01
* Examining a where clause: 0.20
* Comparing two keys: 0.05
* Fetching a row through an index from a temporary memory table: 0.05

The above costs are reasonable for finding out the best index to use.\
However, they where not good for finding out if we should use a table scan,\
index scan or range lookup. The cost for the different engines were\
not properly calibrated.

## New Cost Model

In [MariaDB 11.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/release-notes-mariadb-11-0-series/what-is-mariadb-110) we have fixed the above shortcomings by changing the\
basic cost for 'storage engine operations' to be 1 millisecond. This\
means that for most queries the query cost (`LAST_QUERY_COST`) should be\
close (or at least proportional) to the time the server is spending in\
the storage engine + join\_cache + sorting.

Note that the user level costs are in **microseconds** (as milliseconds\
would have so many zero's that it makes it hard to compare values).

The engine costs have also been separated into smaller parts to make things more\
accurate.

The "disk"-read cost now assumes a mid level SSD disk with 400MB/second. This can be changed by the end user by modifying `OPTIMIZER_DISK_READ_COST`.

All engine specific costs are visible in`information_schema.optimizer_costs`.

For example:

The "default" cost for an engine can be found with:

```sql
SELECT * FROM information_schema.optimizer_costs WHERE engine="DEFAULT"\G
*************************** 1. row ***************************
                         ENGINE: DEFAULT
       OPTIMIZER_DISK_READ_COST: 10.240000
OPTIMIZER_INDEX_BLOCK_COPY_COST: 0.035600
     OPTIMIZER_KEY_COMPARE_COST: 0.011361
        OPTIMIZER_KEY_COPY_COST: 0.015685
      OPTIMIZER_KEY_LOOKUP_COST: 0.435777
   OPTIMIZER_KEY_NEXT_FIND_COST: 0.082347
      OPTIMIZER_DISK_READ_RATIO: 0.020000
        OPTIMIZER_ROW_COPY_COST: 0.060866
      OPTIMIZER_ROW_LOOKUP_COST: 0.130839
   OPTIMIZER_ROW_NEXT_FIND_COST: 0.045916
   OPTIMIZER_ROWID_COMPARE_COST: 0.002653
      OPTIMIZER_ROWID_COPY_COST: 0.002653
```

The above costs are the default (base) for all engines and should be reasonable for engines that does not have a clustered index (like [MyISAM](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/myisam-storage-engine/README.md), [Aria](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/aria/README.md) etc). The default costs can be changed by specifying just the cost as an argument, like `mariadbd --optimizer-disk-read-cost=20` or from SQL: `set global optimizer_disk_read_cost=20`. An engine specific cost can be tuned by prefixing the cost with the engine name, like `set global innodb.optimizer_disk_read_cost=20`.

An engine can tune some or all of the above cost in the storage engine interface.\
Here follows the cost for the [InnoDB storage engine](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/community/storage-engines/innodb/README.md).

```sql
SELECT * FROM information_schema.optimizer_costs WHERE engine="innodb"\G
*************************** 1. row ***************************
                         ENGINE: InnoDB
       OPTIMIZER_DISK_READ_COST: 10.240000
OPTIMIZER_INDEX_BLOCK_COPY_COST: 0.035600
     OPTIMIZER_KEY_COMPARE_COST: 0.011361
        OPTIMIZER_KEY_COPY_COST: 0.015685
      OPTIMIZER_KEY_LOOKUP_COST: 0.791120
   OPTIMIZER_KEY_NEXT_FIND_COST: 0.099000
      OPTIMIZER_DISK_READ_RATIO: 0.020000
        OPTIMIZER_ROW_COPY_COST: 0.060870
      OPTIMIZER_ROW_LOOKUP_COST: 0.765970
   OPTIMIZER_ROW_NEXT_FIND_COST: 0.070130
   OPTIMIZER_ROWID_COMPARE_COST: 0.002653
      OPTIMIZER_ROWID_COPY_COST: 0.002653
```

As can be seen, the `ROW_LOOKUP_COST` is close to the `KEY_LOOKUP_COST`,\
which is because InnoDB has clustered primary key indexes and is using it\
to find the row from a secondary index.

Some engines, like `HEAP`/`MEMORY` implement their own cost\
functions as different indexes in the same engine can have different costs. This is\
why some of the cost numbers for these engines are 0.

There are also some SQL level costs that are independent of the storage engine:

```sql
SELECT * FROM information_schema.global_variables WHERE variable_name LIKE "%WHERE%cost%" OR variable_name LIKE "%scan%cost%";
+---------------------------+----------------+
| VARIABLE_NAME             | VARIABLE_VALUE |
+---------------------------+----------------+
| OPTIMIZER_SCAN_SETUP_COST | 10.000000      |
| OPTIMIZER_WHERE_COST      | 0.032000       |
+---------------------------+----------------+
```

## Description of the Different Cost Variables

Time and cost are quite interchangeable in the new cost model. Below we will use cost for most\
things, except for `OPTIMIZER_DISK_READ_COST` as one should use published/tested timings for the SSD/harddisk if one wants to change the value..

| Variable                            | Type    | Description                                                                                                                                                                                                                                                                                  |
| ----------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Variable                            | Type    | Description                                                                                                                                                                                                                                                                                  |
| OPTIMIZER\_DISK\_READ\_COST         | Engine  | Time in microseconds to read a 4K block from a disk/SSD. The default is set for a 400MB/second SSD                                                                                                                                                                                           |
| OPTIMIZER\_INDEX\_BLOCK\_COPY\_COST | Engine  | Cost to lock and a copy a block from the global cache to a local cache. This cost is added for every block accessed, independent of whether they are cached or not                                                                                                                           |
| OPTIMIZER\_KEY\_COMPARE\_COST       | Engine  | Cost to compare two keys                                                                                                                                                                                                                                                                     |
| OPTIMIZER\_KEY\_COPY\_COST          | Engine  | Cost to copy a key from the index to a local buffer as part of searching for a key                                                                                                                                                                                                           |
| OPTIMIZER\_KEY\_LOOKUP\_COST        | Engine  | Cost to find a key entry in the index (index read)                                                                                                                                                                                                                                           |
| OPTIMIZER\_KEY\_NEXT\_FIND\_COST    | Engine  | Cost to find the next key in the index (index next)                                                                                                                                                                                                                                          |
| OPTIMIZER\_DISK\_READ\_RATIO        | Engine  | The ratio of BLOCK\_NOT\_IN\_CACHE/CACHE\_READS. The cost of disk usage is calculated as estimated\_blocks \* OPTIMIZER\_DISK\_READ\_RATIO \* OPTIMIZER\_DISK\_READ\_COST. A value of 0 means that all blocks are always in the cache. A value of 1 means that a block is never in the cache |
| OPTIMIZER\_ROW\_COPY\_COST          | Engine  | Cost of copying a row to a local buffer. Should be slightly more than OPTIMIZER\_KEY\_COPY\_COST                                                                                                                                                                                             |
| OPTIMIZER\_ROW\_LOOKUP\_COST        | Engine  | Cost to find a row based on the rowid (Rowid is stored in the index together with the key)                                                                                                                                                                                                   |
| OPTIMIZER\_ROW\_NEXT\_FIND\_COST    | Engine  | Cost of finding the next row                                                                                                                                                                                                                                                                 |
| OPTIMIZER\_ROWID\_COMPARE\_COST     | Engine  | Cost of comparing two rowids                                                                                                                                                                                                                                                                 |
| OPTIMIZER\_ROWID\_COPY\_COST        | Engine  | Cost of copying a rowid from the index                                                                                                                                                                                                                                                       |
| OPTIMIZER\_SCAN\_SETUP\_COST        | Session | Cost of starting a table or index scan. This has a low value to encourage the optimizer to use index lookup also tables with very few rows                                                                                                                                                   |
| OPTIMIZER\_WHERE\_COST              | Session | Cost to execute the WHERE clause for every found row. Increasing this variable will encourage the optimizer to find plans which read fewer rows                                                                                                                                              |

More information of the costs and how they were calculated can be found in the `Docs/optimizer_costs.txt` file in the [MariaDB Source distributions](https://github.com/mariadb-corporation/docs-server/blob/test/general-resources/clients-and-utilities/server-client-software/download/getting-the-mariadb-source-code.md).

## Other Optimizer Cost Changes

* When counting disk accesses, we assume that all rows and index data are cached for the duration of the query. This is to avoid the following problem:
  * table t1 with 1 million\_rows is scanned
    * For each row we do a lookup in table t2, which has only 10 rows

If we would count all lookups in t2, there would be 1 million lookups. If this would be the case, the optimizer would choose to use a join cache on the rows in t1 and do a table scan over t2.

* The cost of sorting (filesort) is now more accurate, which allows the optimizer to better choose between index scan and filesort for `ORDER BY/GROUP BY` queries.

A lot of rule-based cost has been changed to be cost-based:

* The decision to use an index (and which index) for resolving `ORDER BY/GROUP BY` were only partly cost-based before.
* The old optimizer would limit the number of ‘expected key lookups’ to 10% of the number of rows. This would cause the optimizer to use an index to scan a big part of a table when a full table scan would be much faster. This code is now removed.
* InnoDB would limit the number of rows in a range to 50% of the total rows, which would confuse the optimizer for big ranges. The cap is now removed.
* If there was a usable filter for an index, it was sometimes used without checking the complete cost of the filter.
* ‘Aggregate distinct optimization with indexes’ is now cost-based. This will change many queries from "Using index for group-by (scanning)” to “Using index for group-by”.

## Other Notable Plan Changes

* Indexes can now be used for `ORDER BY/GROUP BY` in sub queries (instead of filesort)
* Derived tables and queries with `UNION` can now create a distinct key (instead of a key with duplicates) to speed up key accesses.
* Indexes with more used key parts are preferred if the number of resulting rows is the same:
  * `WHERE key_part_1 = 1 and key_part_2 < 10`
  * This will now use a `RANGE` over both key parts instead of using lookups on key\_part\_1.
* For very small tables, index lookup is preferred over table scan.
* `EXPLAIN` does not report "Using index" for scans using a clustered primary key as technically this a table scan.

## When the Optimizer Changes Matter

The new, improved optimizer should be able to find a better plan

* If you are using queries with more than two tables.
* If you have indexes with a lot of identical values.
* If you are using ranges that cover more than 10% of a table.
  * `WHERE key between 1 and 1000 -- Table has values 1-2000`
* If you have complex queries when not all used columns are or can be indexed.
  * In which case you may need to depend on selectivity to get the right plan.
* If you are using queries mixing different storage engines.
  * Like using tables from both InnoDB and Memory in the same query.
* If you have had to use `FORCE INDEX` to get a good plan.
* If using [ANALYZE TABLE](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/table-statements/analyze-table) made your plans worse (or not good enough).
* If your queries have lots of derived tables (subselects).
* You are using `ORDER BY / GROUP BY` that could be resolved via indexes.

## Changing Costs

All engine and “SQL level” cost variables can be changed via\
MariaDB startup options, in configuration files or dynamically using SQL.

### In Configuration Files (and Command Line)

```
[mariadbd]
# Archive is using a hard disk (typical seek is 8-10 ms)
archive.OPTIMIZER_DISK_READ_COST=8000
# All other engines are using an SSD.
OPTIMIZER_DISK_READ_COST=10.240000
```

### From SQL

```sql
# Tell optimizer TO find a plan WITH AS few accepted ROWS AS possible
SET SESSION OPTIMIZER_WHERE_COST=1.0;
# Inform the optimizer that InnoDB buffer pool has a 80% hit rate
SET GLOBAL innodb.OPTIMIZER_DISK_READ_RATIO=0.20;
```

* Note engine costs are `GLOBAL` while other costs can also be `SESSION`.
* To keep things fast, engine-specific costs are stored in the table definition (TABLE\_SHARE). One effect of this is that if one changes the cost for an engine, it will only take effect when new, not previously cached tables are accessed. You can use [FLUSH TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) to force the table to use the new costs at next access.

### Examples of Changing Costs

* `OPTIMIZER_WHERE_COST` is added as a cost for all 'accepted rows'. Increasing this variable will cause the optimizer to choose plans with less estimated rows.
* One can specify the kind of disk used by the system by changing `OPTIMIZER_DISK_READ_COST`. This should be the time to do a random read of a 4096 byte block.
* The cost of a potential disk read is calculated as `OPTIMIZER_DISK_READ_COST * OPTIMIZER_DISK_READ_RATIO`. Increasing `OPTIMIZER_DISK_READ_RATIO` will inform the optimizer that not all data is cached.
* `OPTIMIZER_SCAN_SETUP_COST` will increase the cost of a table scan. One can increase this to avoid using table scans.

## For Storage Engine Developers

The costs for an engine are set the following way when the engine plugin is loaded/initialized:

* Copy the "default" storage engine costs to the plugin engine costs.
  * \#handlerton->costs`points to the engine specific cost data.`
* Call `handlerton->update_optimizer_costs()` to let the storage engine update the costs.
* Apply all user specific engine costs (from configuration files/startup) to the engine costs structure.
* When a TABLE\_SHARE is created, the costs are copied from `handlerton->costs` to `TABLE_SHARE.optimizer_costs` . `handler::update_optimizer_costs()` is called to allow the engine to tune the cost for this specific table instance. This is done to avoid having to take any "cost" mutex while running queries.
* User changes to engine costs are stored in the data pointed to by `handlerton->costs`. This is why [FLUSH TABLES](https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/reference/sql-statements/administrative-sql-statements/flush-commands/flush) is needed to activate new engine costs.
* To speed up cost access for the optimizer, `handler::set_optimizer_costs()` is called for each query to copy `OPTIMIZER_WHERE_COST` and `OPTIMIZER_SCAN_SETUP_COST` to the engine cost structure.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
