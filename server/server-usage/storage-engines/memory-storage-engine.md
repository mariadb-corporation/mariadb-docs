---
description: >-
  The MEMORY storage engine stores tables in RAM for fast access, but data is
  lost upon server restart.
---

# MEMORY

Contents of the MEMORY storage engine (previously known as HEAP) are stored in memory rather than on disk.

It is best-used for read-only caches of data from other tables, or for temporary work areas.

Since the data is stored in memory, it is highly vulnerable to power outages or hardware failure, and is unsuitable for permanent data storage. In fact, after a server restart, `MEMORY` tables are recreated (because the definition file is stored on disk), but they are empty. It is possible to re-populate them with a query using the `--init-file` server startup option.

Variable-length types like [VARCHAR](../../reference/data-types/string-data-types/varchar.md) can be used in MEMORY tables. From MariaDB 13.2, so can [BLOB](../../reference/data-types/string-data-types/blob.md), [TEXT](../../reference/data-types/string-data-types/text.md), [JSON](../../reference/data-types/string-data-types/json.md), and [geometry](../../reference/sql-structure/geometry/geometry-types.md) columns. See [BLOB, TEXT, and Geometry Columns](#blob-text-and-geometry-columns).

## BLOB, TEXT, and Geometry Columns

{% hint style="info" %}
This feature is available from MariaDB 13.2.
{% endhint %}

A MEMORY table can contain columns of these types:

* `TINYBLOB`, `BLOB`, `MEDIUMBLOB`, and `LONGBLOB`.
* `TINYTEXT`, `TEXT`, `MEDIUMTEXT`, and `LONGTEXT`, including `JSON`, which is an alias for `LONGTEXT`.
* `GEOMETRY` and its subtypes, such as `POINT`, `LINESTRING`, and `POLYGON`. Spatial functions such as `ST_AsText()` work on these columns as on any other table.

Before MariaDB 13.2, creating a MEMORY table with such a column fails with an error.

### Indexes on BLOB, TEXT, and Geometry Columns

A MEMORY table can't have an index that includes a `BLOB`, `TEXT`, `JSON`, or geometry column. This applies to `HASH` and `BTREE` indexes, prefix indexes, `UNIQUE` keys, and primary keys alike. MEMORY tables don't support `SPATIAL` indexes. Index the other columns of the table instead:

```sql
CREATE TABLE t1 (a INT, b BLOB, KEY (b)) ENGINE=MEMORY;
ERROR 1073 (42000): BLOB column `b` can't be used in key specification in the MEMORY table

CREATE TABLE t1 (a INT NOT NULL, b BLOB, PRIMARY KEY (a)) ENGINE=MEMORY;
```

### Memory Usage of BLOB and TEXT Values

MEMORY tables use fixed-length rows. The row itself holds only the length and location of each `BLOB` or `TEXT` value. The value is stored in additional fixed-size chunks of the same size as a row, allocated from the table's memory. As a consequence:

* `BLOB` and `TEXT` data counts toward the [max\_heap\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) limit of the table. When the limit is reached, an insert fails with a "table is full" error.
* A value always occupies at least one chunk. In a table with wide rows, short values can use considerably more memory than their length.

### Internal Temporary Tables

The server uses internal temporary tables to resolve statements such as `GROUP BY`, `DISTINCT`, `UNION`, derived tables, common table expressions, and some subqueries. Before MariaDB 13.2, if such a temporary table had a `BLOB` or `TEXT` column, it was always created on disk, using the [Aria](aria/aria-storage-engine.md) storage engine. That happened even when the actual values were short, for example a small `JSON` document.

From MariaDB 13.2, such temporary tables are created as MEMORY tables as well. As with any internal temporary table, they are converted to Aria tables if they grow larger than the smaller of [max\_heap\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) and [tmp\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_table_size). An internal temporary table is still created on disk from the start in these cases:

* [tmp\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#tmp_table_size) is set to `0`.
* The statement uses full-text search (`MATCH ... AGAINST`) on the result of a derived table or a `UNION`.

As a result, the [Created\_tmp\_disk\_tables](../../ha-and-performance/optimization-and-tuning/system-variables/server-status-variables.md#created_tmp_disk_tables) status variable can grow more slowly after an upgrade to MariaDB 13.2. For the same reason, `INFORMATION_SCHEMA` tables with `TEXT` columns, for example `ROUTINES` and `VIEWS`, report `MEMORY` instead of `Aria` in the `ENGINE` column, and `Fixed` in the `ROW_FORMAT` column, of [INFORMATION\_SCHEMA.TABLES](../../reference/system-tables/information-schema/information-schema-tables/information-schema-tables-table.md).

## Memory Usage

The maximum total size of MEMORY tables cannot exceed the [max\_heap\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) system server variable. When a table is created this value applies to that table, and when the server is restarted this value applies to existing tables. Changing this value has no effect on existing tables. However, executing a `ALTER TABLE ... ENGINE=MEMORY` statement applies the current value of `max_heap_table_size` to the table. Also, it is possible to change the session value of `max_heap_table_size` before creating a table, to make sure that tables created by other sessions are not affected.

The `MAX_ROWS` table option provides a hint about the number of rows you plan to store in them. This is not a hard limit that cannot be exceeded, and does not allow to exceed `max_heap_table_size`. The storage engine uses max\_heap\_table\_size and MAX\_ROWS to calculate the maximum memory that could be allocated for the table.

Memory allocated to a MEMORY table is freed by running [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md) or [TRUNCATE TABLE](../../reference/sql-statements/table-statements/truncate-table.md), or rebuilding with [ALTER TABLE tbl\_name ENGINE = MEMORY](../../reference/sql-statements/data-definition/alter/alter-table/). When rows are deleted, space is not automatically freed.

## Replication

The data in MEMORY tables are lost when a server restarts.
To reflect this result in [replication](../../ha-and-performance/standard-replication/), the first time a server uses a MEMORY table after a restart, it writes a TRUNCATE statement for that table with a “generated by server” comment to the binary log, so its replicas are also emptied.

{% hint style="warning" %}
In non-circular replication, restarting a replica will diverge from its primaries in both MEMORY table data and [GTID](../../ha-and-performance/standard-replication/gtid/README.md).
The contents and replication must be resynchronized to fix this issue.
Alternatively, if consistency is not required (e.g., for cache data), then the replica should have a different Domain ID than its primaries to satisfy [GTID strict mode](../../ha-and-performance/standard-replication/gtid/gtid-system-variables.md#gtid_strict_mode).

If the MEMORY tables are not required for replication at all, then [excluding them from replication](../../ha-and-performance/standard-replication/replication-filters.md) avoids this problem entirely.
{% endhint %}

## Index Type

The MEMORY storage engine permits indexes to be either B-tree or Hash. Hash is the default type for MEMORY. See [Storage Engine index types](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) for more on their characteristics.

A MEMORY table can have up to 64 indexes, 16 columns for each index and a maximum key length of 3072 bytes.

## Example

The following example shows how to create a `MEMORY` table with a given maximum size, as described above.

```sql
SET max_heap_table_size = 1024*516;

CREATE TABLE t (a VARCHAR(10), b INT) ENGINE = MEMORY;

SET max_heap_table_size = @@max_heap_table_size;
```

## See Also

* [Performance of MEMORY tables](../../reference/product-development/server-development/quality/benchmarks-and-long-running-tests/benchmarks/performance-of-memory-tables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
