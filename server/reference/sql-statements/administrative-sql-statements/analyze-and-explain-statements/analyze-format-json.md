# ANALYZE FORMAT=JSON

`ANALYZE FORMAT=JSON` is a mix of the [EXPLAIN FORMAT=JSON](explain-format-json.md) and [ANALYZE](analyze-statement.md) statement features. The `ANALYZE FORMAT=JSON $statement` will execute `$statement`, and then print the output of `EXPLAIN FORMAT=JSON`, amended with data from the query execution.

## Basic Execution Data

You can get the following also from tabular `ANALYZE` statement form:

* `r_rows` is provided for any node that reads rows. It shows how many rows were read, on average.
* `r_filtered` is provided whenever there is a condition that is checked. It shows the percentage of rows left after checking the condition.

## Advanced Execution Data

The most important data not available in the regular tabular `ANALYZE` statement are:

* `r_loops` field. This shows how many times the node was executed. Most query plan elements have this field.
* `r_total_time_ms` field. It shows how much time in total, in milliseconds, was spent executing this node. If the node has subnodes, their execution time is included.
  * For UPDATE and DELETE statements, top-level `query_block.r_total_time_ms` does include the time to make row deletions/updates but does NOT include the time to commit the changes.
* `r_buffer_size` field. Query plan nodes that make use of buffers report the size of buffer that was used.

### InnoDB engine statistics

Starting from [MariaDB 10.6.15](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-6-series/mariadb-10-6-15-release-notes), [MariaDB 10.8.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-8-series/mariadb-10-8-8-release-notes), [MariaDB 10.9.8](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/mariadb-10-9-8-release-notes), [MariaDB 10.10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-10-series/mariadb-10-10-6-release-notes), [MariaDB 10.11.5](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/mariadb-10-11-series/mariadb-10-11-5-release-notes), [MariaDB 11.0.3](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-0-series/mariadb-11-0-3-release-notes), [MariaDB 11.1.2](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-1-series/mariadb-11-1-2-release-notes) and [MariaDB 11.2.1](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-11-2-series/mariadb-11-2-1-release-notes) ([MDEV-31577](https://jira.mariadb.org/browse/MDEV-31577)), the following statistics are reported for InnoDB tables:

```json
"r_engine_stats": {
        "pages_accessed":  integer,
        "pages_updated": integer,
        "pages_read_count": integer,
        "pages_prefetch_read_count": integer,
        "pages_read_time_ms": double,
        "old_rows_read": integer
      }
```

Only non-zero members are printed.

* `pages_accessed` is the total number of buffer pool pages accessed when reading this table.
* `pages_updated` is the total number of buffer pool pages that were modified during the execution of the statement.
* `pages_read_count` is the number of pages that InnoDB had to read from disk for this table. If the query touches "hot" data in the InnoDB buffer pool, this value will be 0 and not present.
* `pages_prefetch_read_count` Number of pages for which read-ahead was initiated. Not all such pages will necessarily be accessed.
* `pages_read_time_ms` is the total time spent reading the table.
* `old_rows_read` is the number of old row versions that InnoDB had to read. Old row version is the version of the row that is not visible to this transaction.

## SHOW ANALYZE FORMAT=JSON

**MariaDB starting with** [**10.9**](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/mariadb-community-server-release-notes/old-releases/release-notes-mariadb-10-9-series/what-is-mariadb-109)

`SHOW ANALYZE FORMAT=JSON for <connection_id>`\
extends `ANALYZE [FORMAT=JSON] <select>` to allow one to analyze a query currently running in another connection.

## Data About Individual Query Plan Nodes

* `filesort` node reports whether sorting was done with `LIMIT n` parameter, and how many rows were in the sort result.
* `block-nl-join` node has `r_loops` field, which allows to tell whether `Using join buffer` was efficient.
* `range-checked-for-each-record` reports counters that show the result of the check.
* `expression-cache` is used for subqueries, and it reports how many times the cache was used, and what cache hit ratio was.
* `union_result` node has `r_rows` so one can see how many rows were produced after UNION operation and so forth.

## Use Cases

See [Examples of ANALYZE FORMAT=JSON](analyze-formatjson-examples.md).

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
