---
description: System variables added in MariaDB Enterprise Server 12.3.
---

# System Variables Added in Enterprise Server 12.3

This is a list of [system variables](../server-system-variables.md) that are new in MariaDB Enterprise Server 12.3, relative to the previous Enterprise Server release series, Enterprise Server 11.8.

Because Enterprise Server backports selected features across release lines, some system variables that were introduced in Community Server 12.0, 12.1, and 12.3 are **not** listed here: they had already been backported into Enterprise Server 11.8 and so were not new in Enterprise Server 12.3. Examples are `analyze_max_length`, `aria_pagecache_segments`, `max_open_cursors`, and `metadata_locks_instances`.

<table><thead><tr><th width="567.7999267578125">Variable</th><th>Added</th></tr></thead><tbody><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#binlog_directory">binlog_directory</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#binlog_row_event_fragment_threshold">binlog_row_event_fragment_threshold</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#binlog_storage_engine">binlog_storage_engine</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#create_tmp_table_binlog_formats">create_tmp_table_binlog_formats</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#innodb_binlog_state_interval">innodb_binlog_state_interval</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#master_info_file">master_info_file</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../server-system-variables.md#optimizer_record_context">optimizer_record_context</a></td><td>Enterprise Server 12.3</td></tr><tr><td>path</td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#replicate_same_server_id">replicate_same_server_id</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../standard-replication/replication-and-binary-log-system-variables.md#show_slave_auth_info">show_slave_auth_info</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="../../../../security/encryption/data-in-transit-encryption/ssltls-system-variables.md#ssl_passphrase">ssl_passphrase</a></td><td>Enterprise Server 12.3</td></tr><tr><td><a href="https://app.gitbook.com/s/3VYeeVGUV4AMqrA3zwy7/reference/galera-cluster-system-variables#wsrep_applier_retry_count">wsrep_applier_retry_count</a></td><td>Enterprise Server 12.3</td></tr></tbody></table>

## See Also

* [System Variables Added in MariaDB 12.3](system-variables-added-in-mariadb-12.3.md) (Community Server)

<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>

{% @marketo/form formId="4316" %}
