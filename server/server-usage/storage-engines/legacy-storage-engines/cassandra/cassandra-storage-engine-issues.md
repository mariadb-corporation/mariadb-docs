# Cassandra Storage Engine Issues

CassandraSE is no longer actively being developed and has been removed in [MariaDB 10.6](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/mariadb-10-6-series/what-is-mariadb-106). See [MDEV-23024](https://jira.mariadb.org/browse/MDEV-23024).

This page lists difficulties and peculiarities of [Cassandra Storage Engine](cassandra-storage-engine-overview.md). I'm not putting them into bug tracker because it is not clear whether these properties should be considered bugs.

## No way to get E(#rows in column family)

There seems to be no way to get even a rough estimate of how many different keys are present in a column family. I'm using an arbitrary value of 1000 now, which causes

* EXPLAIN will always show rows=1000 for full table scans. In the future, this may cause poor query plans.
* `DELETE FROM table` always prints "1000 rows affected", with no regards how many records were actually there in the table.

```
MariaDB [j1]> delete from t1;
Query OK, 1000 rows affected (0.14 sec)
```

We could use the new [engine-independent-table-statistics](../../../../ha-and-performance/optimization-and-tuning/query-optimizations/statistics-for-optimizing-queries/engine-independent-table-statistics.md) feature to get some data statistics.

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
