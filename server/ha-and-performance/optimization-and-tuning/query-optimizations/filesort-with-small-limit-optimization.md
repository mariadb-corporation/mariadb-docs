# Filesort with Small LIMIT Optimization

## Optimization Description

When `n` is sufficiently small, the optimizer will use a [priority queue](https://en.wikipedia.org/wiki/Priority_queue) for sorting. Before the optimization's porting to [MariaDB 10.0](https://app.gitbook.com/s/aEnK0ZXmUbJzqQrTjFyb/community-server/old-releases/10.0/changes-improvements-in-mariadb-10-0), the alternative was, roughly speaking, to sort the entire output and then pick only first `n` rows.

NOTE: The problem of choosing which index to use for query with ORDER BY ... LIMIT is a different problem, see [optimizer\_join\_limit\_pref\_ratio-optimization](optimizer_join_limit_pref_ratio-optimization.md).

## Optimization Visibility in MariaDB

There are two ways to check whether filesort has used a priority queue.

### Status Variable

The first way is to check the [Sort\_priority\_queue\_sorts](../system-variables/server-status-variables.md#sort_priority_queue_sorts) status variable. It shows the number of times that sorting was done through a priority queue. (The total number of times sorting was done is a sum [Sort\_range](../system-variables/server-status-variables.md#sort_range) and [Sort\_scan](../system-variables/server-status-variables.md#sort_scan)).

### Slow Query Log

The second way is to check the slow query log. When one uses [Extended statistics in the slow query log](statistics-for-optimizing-queries/slow-query-log-extended-statistics.md) and specifies [log\_slow\_verbosity=query\_plan](../system-variables/server-system-variables.md#log_slow_verbosity), [slow query log](../../../server-management/server-monitoring-logs/slow-query-log/) entries look like this

```sql
# Time: 140714 18:30:39
# User@Host: root[root] @ localhost []
# Thread_id: 3  Schema: test  QC_hit: No
# Query_time: 0.053857  Lock_time: 0.000188  Rows_sent: 11  Rows_examined: 100011
# Full_scan: Yes  Full_join: No  Tmp_table: No  Tmp_table_on_disk: No
# Filesort: Yes  Filesort_on_disk: No  Merge_passes: 0  Priority_queue: Yes
SET TIMESTAMP=1405348239;SET TIMESTAMP=1405348239;
SELECT * FROM t1 WHERE col1 BETWEEN 10 AND 20 ORDER BY col2 LIMIT 100;
```

Note the "Priority\_queue: Yes" on the last comment line. (`pt-query-digest` is able to parse slow query logs with the Priority\_queue field)

As for `EXPLAIN`, it will give no indication whether filesort uses priority queue or the generic quicksort and merge algorithm. `Using filesort` will be shown in both cases, by both MariaDB and MySQL.

## See Also

* [LIMIT Optimization](https://dev.mysql.com/doc/refman/5.6/en/limit-optimization.html) page in the MySQL 5.6 manual (search for "priority queue").
* MySQL WorkLog entry, [WL#1393](https://dev.mysql.com/worklog/task/?id=1393)
* [MDEV-415](https://jira.mariadb.org/browse/MDEV-415), [MDEV-6430](https://jira.mariadb.org/browse/MDEV-6430)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
