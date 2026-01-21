---
description: >-
  The MEMORY storage engine stores tables in RAM for fast access, but data is
  lost upon server restart
---

# MEMORY

Contents of the MEMORY storage engine (previously known as HEAP) are stored in memory rather than on disk.

It is best-used for read-only caches of data from other tables, or for temporary work areas.

Since the data is stored in memory, it is highly vulnerable to power outages or hardware failure, and is unsuitable for permanent data storage. In fact, after a server restart, `MEMORY` tables are recreated (because the definition file is stored on disk), but they are empty. It is possible to re-populate them with a query using the `--init-file` server startup option.

Variable-length types like [VARCHAR](../../reference/data-types/string-data-types/varchar.md) can be used in MEMORY tables. [BLOB](../../reference/data-types/string-data-types/blob.md) or [TEXT](../../reference/data-types/string-data-types/text.md) columns are not supported for MEMORY tables.

## Memory Usage

The maximum total size of MEMORY tables cannot exceed the [max\_heap\_table\_size](../../ha-and-performance/optimization-and-tuning/system-variables/server-system-variables.md#max_heap_table_size) system server variable. When a table is created this value applies to that table, and when the server is restarted this value applies to existing tables. Changing this value has no effect on existing tables. However, executing a `ALTER TABLE ... ENGINE=MEMORY` statement applies the current value of `max_heap_table_size` to the table. Also, it is possible to change the session value of `max_heap_table_size` before creating a table, to make sure that tables created by other sessions are not affected.

The `MAX_ROWS` table option provides a hint about the number of rows you plan to store in them. This is not a hard limit that cannot be exceeded, and does not allow to exceed `max_heap_table_size`. The storage engine uses max\_heap\_table\_size and MAX\_ROWS to calculate the maximum memory that could be allocated for the table.

Memory allocated to a MEMORY table is freed by running [DROP TABLE](../../reference/sql-statements/data-definition/drop/drop-table.md) or [TRUNCATE TABLE](../../reference/sql-statements/table-statements/truncate-table.md), or rebuilding with [ALTER TABLE tbl\_name ENGINE = MEMORY](../../reference/sql-statements/data-definition/alter/alter-table/). When rows are deleted, space is not automatically freed.

## Index Type

The MEMORY storage engine permits indexes to be either B-tree or Hash. Hash is the default type for MEMORY. See [Storage Engine index types](../../ha-and-performance/optimization-and-tuning/optimization-and-indexes/storage-engine-index-types.md) for more on their characteristics.

A MEMORY table can have up to 64 indexes, 16 columns for each index and a maximum key length of 3072 bytes.

## Replication

MEMORY tables are lost when a server restarts. In order to achieve this result in [replication](../../ha-and-performance/standard-replication/), the first time a primary uses a MEMORY table after a restart, it writes a DELETE statement for that table to the binary log, so that replicas are also emptied.

## Example

The following example shows how to create a `MEMORY` table with a given maximum size, as described above.

```sql
SET max_heap_table_size = 1024*516;

CREATE TABLE t (a VARCHAR(10), b INT) ENGINE = MEMORY;

SET max_heap_table_size = @@max_heap_table_size;
```

## See Also

* [Performance of MEMORY tables](/broken/spaces/WCInJQ9cmGjq1lsTG91E/pages/qnjMjiyRC0dWALAFvdZL)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
