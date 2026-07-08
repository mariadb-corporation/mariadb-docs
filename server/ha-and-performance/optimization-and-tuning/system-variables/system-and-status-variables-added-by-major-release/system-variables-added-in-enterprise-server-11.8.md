---
description: System variables added in MariaDB Enterprise Server 11.8.
---

# System Variables Added in Enterprise Server 11.8

This is a list of [system variables](../server-system-variables.md) that are new in MariaDB Enterprise Server 11.8, relative to the previous Enterprise Server release series, Enterprise Server 11.4.

Because Enterprise Server backports selected features across release lines, some system variables that were introduced in Community Server 11.5 through 11.8 are **not** listed here: they had already been backported into Enterprise Server 11.4 and so were not new in Enterprise Server 11.8. Examples are `max_tmp_total_space_usage` and the `mhnsw_*` vector-index variables.

<table><thead><tr><th width="567.7999267578125">Variable</th><th>Added</th></tr></thead><tbody><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#binlog_large_commit_threshold">binlog_large_commit_threshold</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../../../../server-usage/storage-engines/innodb/innodb-system-variables.md#innodb_adaptive_hash_index_cells">innodb_adaptive_hash_index_cells</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../../../../server-management/server-monitoring-logs/slow-query-log/log_slow_always_query_time-system-variable.md">log_slow_always_query_time</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../server-system-variables.md#max_open_cursors">max_open_cursors</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#slave_abort_blocking_timeout">slave_abort_blocking_timeout</a></td><td>Enterprise Server 11.8</td></tr><tr><td>wsrep_sync_wait_timeout</td><td>Enterprise Server 11.8</td></tr></tbody></table>

## See Also

* [System Variables Added in MariaDB 11.8](system-variables-added-in-mariadb-11-8.md) (Community Server)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
