---
description: Status variables added in MariaDB Enterprise Server 11.8.
---

# Status Variables Added in Enterprise Server 11.8

This is a list of [status variables](../../server-status-variables.md) that are new in MariaDB Enterprise Server 11.8, relative to the previous Enterprise Server release series, Enterprise Server 11.4.

Because Enterprise Server backports selected features across release lines, some status variables that were introduced in Community Server 11.5 through 11.8 are **not** listed here: they had already been backported into Enterprise Server 11.4 and so were not new in Enterprise Server 11.8. Examples are `Max_tmp_space_used` and `Tmp_space_used`.

<table><thead><tr><th width="567.7999267578125">Variable</th><th>Added</th></tr></thead><tbody><tr><td>Feature_vector_index</td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_pending">innodb_async_reads_pending</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_queue_size">innodb_async_reads_queue_size</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_tasks_running">innodb_async_reads_tasks_running</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_total_count">innodb_async_reads_total_count</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_total_enqueues">innodb_async_reads_total_enqueues</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_reads_wait_slot_sec">innodb_async_reads_wait_slot_sec</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_pending">innodb_async_writes_pending</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_queue_size">innodb_async_writes_queue_size</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_tasks_running">innodb_async_writes_tasks_running</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_total_count">innodb_async_writes_total_count</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_total_enqueues">innodb_async_writes_total_enqueues</a></td><td>Enterprise Server 11.8</td></tr><tr><td><a href="../innodb-status-variables.md#innodb_async_writes_wait_slot_sec">innodb_async_writes_wait_slot_sec</a></td><td>Enterprise Server 11.8</td></tr></tbody></table>

## See Also

* [Status Variables Added in MariaDB 11.8](../community-server/status-variables-added-in-mariadb-11-8.md) (Community Server)
* [System Variables Added in Enterprise Server 11.8](system-variables-added-in-enterprise-server-11.8.md)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
