---
description: >-
  The Information Schema VECTOR_INDEXES table reports the size, node counts and
  cache usage of each MHNSW vector index.
---

# Information Schema VECTOR\_INDEXES Table

{% hint style="info" %}
This table is available from [MariaDB 13.1](https://jira.mariadb.org/browse/MDEV-34805).
{% endhint %}

The [Information Schema](../) `VECTOR_INDEXES` table reports the size, node counts and cache usage of each [vector index](../../../sql-structure/vectors/) in the server. It holds one row per vector index, which means one row per table, because a table can have at most one vector index.

The table is provided by the built-in `VECTOR_INDEXES` Information Schema plugin, which ships alongside the `mhnsw` plugin and is available in a default build. Its [plugin maturity](../../../plugins/plugin-overview.md) is beta in MariaDB 13.1.

It contains the following columns:

| Column              | Type                  | Description                                                                                                                                                                                                                          |
| ------------------- | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| TABLE\_CATALOG      | `varchar(64)`         | Always `def`.                                                                                                                                                                                                                        |
| TABLE\_SCHEMA       | `varchar(64)`         | Database containing the indexed table.                                                                                                                                                                                               |
| TABLE\_NAME         | `varchar(64)`         | Name of the indexed table.                                                                                                                                                                                                           |
| INDEX\_NAME         | `varchar(64)`         | Name of the vector index.                                                                                                                                                                                                            |
| VECTOR\_DIMENSIONS  | `int(10) unsigned`    | Number of dimensions of the indexed [VECTOR](../../../data-types/numeric-data-types/vector.md) column.                                                                                                                               |
| INDEX\_SIZE         | `bigint(19) unsigned` | On-disk size of the graph table in bytes, that is its data length plus its index length. `NULL` if the graph table cannot be opened.                                                                                                  |
| TOTAL\_NODES        | `bigint(19) unsigned` | Number of rows the storage engine reports for the graph table, each row being one node of the graph. See [Accuracy of the node counts](#accuracy-of-the-node-counts) below.                                                           |
| CACHED\_NODES       | `bigint(19) unsigned` | Number of graph nodes currently held in the index cache. `0` while the index is not cached.                                                                                                                                           |
| DELETED\_ROWS       | `bigint(19) unsigned` | Estimated number of nodes in the graph that no longer have a row in the table, computed as `TOTAL_NODES` minus the number of rows the engine reports for the table, and never negative. `NULL` if the graph table cannot be opened.   |
| SUBDIST\_ENABLED    | `varchar(3)`          | Whether the partial-distance optimization is in use: `YES`, `NO`, or `NULL` while the server has not yet gathered enough statistics to decide. See [SUBDIST\_ENABLED](#subdist_enabled) below.                                        |
| MEMORY\_SIZE        | `bigint(19) unsigned` | Memory currently allocated for the index cache, in bytes. `0` while the index is not cached.                                                                                                                                          |

## Example

For a table with 1000 rows, after a vector search has populated the index cache:

```sql
SELECT * FROM INFORMATION_SCHEMA.VECTOR_INDEXES WHERE TABLE_NAME = 't'\G
*************************** 1. row ***************************
    TABLE_CATALOG: def
     TABLE_SCHEMA: test
       TABLE_NAME: t
       INDEX_NAME: v
VECTOR_DIMENSIONS: 2
       INDEX_SIZE: 229376
      TOTAL_NODES: 1000
     CACHED_NODES: 225
     DELETED_ROWS: 0
  SUBDIST_ENABLED: NO
      MEMORY_SIZE: 4194176
```

## Privileges

A vector index is only listed if the connection has a privilege on the indexed table, or a column-level privilege on the indexed vector column itself. A privilege on some other column of the table is not enough:

```sql
GRANT SELECT (id) ON db.t TO 'u'@'localhost';
-- the index on db.t.v is not listed

GRANT SELECT (v) ON db.t TO 'u'@'localhost';
-- the index on db.t.v is listed
```

## Cache Usage

`CACHED_NODES` and `MEMORY_SIZE` describe the in-memory copy of the graph, not the index itself, and both read `0` until the cache is populated. Whether an operation populates it depends on the storage engine: with InnoDB, `INSERT` alone leaves the cache empty and the first vector search fills it, while Aria and MyISAM already cache nodes while rows are inserted. Flushing the table with [FLUSH TABLES](../../../sql-statements/administrative-sql-statements/flush-commands/flush.md) discards the cache, so both columns fall back to `0` until the index is used again.

`MEMORY_SIZE` is capped per index by [mhnsw\_max\_cache\_size](../../../sql-structure/vectors/vector-system-variables.md#mhnsw_max_cache_size). Because the vector index cache is not instrumented in the [Performance Schema](../../performance-schema/), this column is the only way to see how much memory an individual vector index is using.

## Accuracy of the Node Counts

`TOTAL_NODES` and, because it is derived from it, `DELETED_ROWS` are taken from the storage engine's row counts, and are therefore only as accurate as the engine's statistics.

For InnoDB, both are estimates and can be far off: a table that has never had a row deleted can report thousands of deleted rows, and `ANALYZE TABLE` or a higher [innodb\_stats\_persistent\_sample\_pages](../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_stats_persistent_sample_pages) does not improve them. Aria and MyISAM keep exact row counts and report exact values.

`INDEX_SIZE` covers the graph table only, so it does not match [INFORMATION\_SCHEMA.TABLES](information-schema-tables-table.md)`.INDEX_LENGTH` for a table that has other indexes, such as a primary key.

## SUBDIST\_ENABLED

For high-dimensional vectors, MariaDB can compute a distance over the first 192 dimensions only and use it as a lower bound, skipping the full computation when that bound is already too large to be a candidate. This optimization is only eligible for vectors of 384 dimensions or more, and MariaDB decides whether to use it from statistics gathered while the index is searched.

`SUBDIST_ENABLED` reports the outcome:

* `NO` — the optimization is not in use, either because the vector has fewer than 384 dimensions, or because the collected statistics showed it would not be reliable for this data.
* `YES` — the optimization is in use.
* `NULL` — the vector has 384 dimensions or more, but the server has not yet seen enough searches to decide.

## See Also

* [Vector Overview](../../../sql-structure/vectors/vector-overview.md)
* [CREATE TABLE with Vectors](../../../sql-structure/vectors/create-table-with-vectors.md)
* [Vector System Variables](../../../sql-structure/vectors/vector-system-variables.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
