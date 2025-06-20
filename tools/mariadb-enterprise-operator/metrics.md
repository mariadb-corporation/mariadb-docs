
# Metrics

MariaDB Enterprise Operator is able to configure [Prometheus operator](https://prometheus-operator.dev/) resources to scrape metrics from MariaDB and MaxScale instances. These metrics can be used later on to build [Grafana dashboards](#grafana-dashboards) or trigger [Alertmanager](https://prometheus.io/docs/alerting/latest/alertmanager/) alerts.

## Operator metrics

In order to expose the operator internal metrics, you can install the operator Helm chart passing the `metrics.enabled = true` value. Refer to the [Helm documentation](mariadb-enterprise-operator-installation/helm.md) for further detail.

## Exporters


The operator configures exporters to query MariaDB and MaxScale, exposing metrics in Prometheus format through an HTTP endpoint.

It is important to note that these exporters run as standalone `Deployments` rather than as sidecars for each data-plane replica. Since they can communicate with all replicas of MariaDB and MaxScale, there is no need to run a separate exporter for each replica.

As a result, the lifecycle of MariaDB and MaxScale remains independent from the exporters, allowing for upgrades without impacting the availability of either component.

## `ServiceMonitor`

Once the exporter `Deployment` is ready, the operator creates a [ServiceMonitor](https://prometheus-operator.dev/docs/api-reference/api/#monitoring.coreos.com/v1.ServiceMonitor) object that will be eventually reconciled by the [Prometheus operator](https://github.com/prometheus-operator/prometheus-operator), resulting in the Prometheus instance being configured to scrape the exporter endpoint.

As you scale MariaDB and MaxScale by adjusting the number of replicas, the operator will reconcile the `ServiceMonitor` to dynamically add or remove targets corresponding to the updated instances.

## Configuration

The easiest way to setup metrics in your MariaDB and MaxScale instances is just by setting `spec.metrics.enabled = true`:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
...
  metrics:
    enabled: true
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
...
  metrics:
    enabled: true
```

The rest of the fields are defaulted by the operator. If you need a more fine grained configuration, refer to the [API reference](api-reference.md) and the following examples:

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MariaDB
metadata:
  name: mariadb
spec:
...
  metrics:
    enabled: true
    exporter:
      image: mariadb/mariadb-prometheus-exporter-ubi:v0.0.2
      resources:
        requests:
          cpu: 50m
          memory: 64Mi
        limits:
          cpu: 300m
          memory: 512Mi
      port: 9104
    serviceMonitor:
      prometheusRelease: kube-prometheus-stack
      jobLabel: mariadb-monitoring
      interval: 10s
      scrapeTimeout: 10s
    username: monitoring
    passwordSecretKeyRef:
      name: mariadb
      key: password
```

```yaml
apiVersion: enterprise.mariadb.com/v1alpha1
kind: MaxScale
metadata:
  name: maxscale
spec:
...
  auth:
    metricsUsername: metrics
    metricsPasswordSecretKeyRef:
      key: password
      name: maxscale-galera-metrics
  metrics:
    enabled: true
    exporter:
      image: mariadb/maxscale-prometheus-exporter-ubi:v0.0.2
      resources:
        requests:
          cpu: 50m
          memory: 64Mi
        limits:
          cpu: 300m
          memory: 512Mi
      port: 9105
    serviceMonitor:
      prometheusRelease: kube-prometheus-stack
      jobLabel: mariadb-monitoring
      interval: 10s
      scrapeTimeout: 10s
```



## Grafana dashboards


The following community dashboards available on [grafana.com](https://grafana.com/grafana/dashboards/) are compatible with the [MariaDB metrics](#mariadb-metrics), and therefore they can be used to monitor `MariaDB` instances:


**[MySQL Overview](https://grafana.com/grafana/dashboards/7362-mysql-overview/)**


**[MySQL Exporter Quickstart and Dashboard](https://grafana.com/grafana/dashboards/14057-mysql/)**


**[MySQL Replication](https://grafana.com/grafana/dashboards/7371-mysql-replication/)**


**[Galera/MariaDB - Overview](https://grafana.com/grafana/dashboards/13106-galera-mariadb-overview/)**


## MariaDB metrics


The following metrics are available for `MariaDB` instances:


| Metric Name | Description | Type |
| --- | --- | --- |
| Metric Name | Description | Type |
| mysql_exporter_collector_duration_seconds | Collector time duration. | GAUGE |
| mysql_exporter_collector_success | mysqld_exporter: Whether a collector succeeded. | GAUGE |
| mysql_galera_evs_repl_latency_avg_seconds | PXC/Galera group communication latency. Avg value. | GAUGE |
| mysql_galera_evs_repl_latency_max_seconds | PXC/Galera group communication latency. Max value. | GAUGE |
| mysql_galera_evs_repl_latency_min_seconds | PXC/Galera group communication latency. Min value. | GAUGE |
| mysql_galera_evs_repl_latency_sample_size | PXC/Galera group communication latency. Sample Size. | GAUGE |
| mysql_galera_evs_repl_latency_stdev | PXC/Galera group communication latency. Standard Deviation. | GAUGE |
| mysql_galera_gcache_size_bytes | PXC/Galera gcache size. | GAUGE |
| mysql_galera_status_info | PXC/Galera status information. | GAUGE |
| mysql_galera_variables_info | PXC/Galera variables information. | GAUGE |
| mysql_global_status_aborted_clients | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aborted_connects | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aborted_connects_preauth | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_access_denied_errors | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_column_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_database_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_function_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_package_body_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_package_spec_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_procedure_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_proxy_users | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_role_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_roles | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_table_grants | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_acl_users | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_blocks_not_flushed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_blocks_unused | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_blocks_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_read_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_write_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_pagecache_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_aria_transaction_log_syncs | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_bytes_written | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_cache_disk_use | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_cache_use | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_commits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_disk_use | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_group_commit_trigger_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_group_commit_trigger_lock_wait | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_group_commit_trigger_timeout | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_group_commits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_gtid_index_hit | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_gtid_index_miss | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_snapshot_position | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_stmt_cache_disk_use | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_binlog_stmt_cache_use | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_buffer_pool_dirty_pages | Innodb buffer pool dirty pages. | GAUGE |
| mysql_global_status_buffer_pool_page_changes_total | Innodb buffer pool page state changes. | COUNTER |
| mysql_global_status_buffer_pool_pages | Innodb buffer pool pages by state. | GAUGE |
| mysql_global_status_busy_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_bytes_received | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_bytes_sent | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_column_compressions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_column_decompressions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_commands_total | Total number of executed MySQL commands. | COUNTER |
| mysql_global_status_compression | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_connection_errors_total | Total number of MySQL connection errors. | COUNTER |
| mysql_global_status_connections | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_cpu_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_created_tmp_disk_tables | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_created_tmp_files | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_created_tmp_tables | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_delayed_errors | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_delayed_insert_threads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_delayed_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_delete_scan | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_empty_queries | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_executed_events | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_executed_triggers | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_application_time_periods | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_check_constraint | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_custom_aggregate_functions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_delay_key_write | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_dynamic_columns | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_fulltext | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_gis | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_insert_returning | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_into_outfile | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_into_variable | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_invisible_columns | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_json | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_locale | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_subquery | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_system_versioning | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_timezone | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_trigger | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_window_functions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_feature_xml | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_handlers_total | Total number of executed MySQL handlers. | COUNTER |
| mysql_global_status_innodb_adaptive_hash_hash_searches | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_adaptive_hash_non_hash_searches | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_available_undo_logs | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_background_log_sync | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_bytes_data | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_bytes_dirty | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_load_incomplete | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_read_ahead | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_read_ahead_evicted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_read_ahead_rnd | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_read_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_wait_free | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_buffer_pool_write_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_bulk_operations | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_checkpoint_age | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_checkpoint_max_age | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_fsyncs | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_pending_fsyncs | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_pending_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_pending_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_read | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_data_written | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_dblwr_pages_written | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_dblwr_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_deadlocks | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_merge_blocks_decrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_merge_blocks_encrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_rowlog_blocks_decrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_rowlog_blocks_encrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_temp_blocks_decrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_n_temp_blocks_encrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_num_key_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_rotation_estimated_iops | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_rotation_pages_flushed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_rotation_pages_modified | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_rotation_pages_read_from_cache | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_encryption_rotation_pages_read_from_disk | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_bzip2 | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_lz4 | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_lzma | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_lzo | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_punch_hole | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_have_snappy | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_history_list_length | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_instant_alter_column | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_log_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_log_write_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_log_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_lsn_current | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_lsn_flushed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_lsn_last_checkpoint | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_master_thread_active_loops | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_master_thread_idle_loops | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_max_trx_id | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_mem_adaptive_hash | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_mem_dictionary | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_open_files | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_page_compressed_trim_op | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_pages_decrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_pages_encrypted | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_pages_page_compressed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_pages_page_compression_error | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_num_pages_page_decompressed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_onlineddl_pct_progress | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_onlineddl_rowlog_pct_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_onlineddl_rowlog_rows | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_os_log_written | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_page_compression_saved | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_page_size | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_pages_created | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_pages_read | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_pages_written | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_row_lock_current_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_row_lock_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_row_lock_time_avg | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_row_lock_time_max | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_row_lock_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_truncated_status_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_innodb_undo_truncations | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_blocks_not_flushed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_blocks_unused | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_blocks_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_blocks_warm | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_read_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_write_requests | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_key_writes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_last_query_cost | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_master_gtid_wait_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_master_gtid_wait_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_master_gtid_wait_timeouts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_max_statement_time_exceeded | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_max_tmp_space_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_max_used_connections | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_max_used_connections_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_memory_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_memory_used_initial | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_not_flushed_delayed_rows | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_open_files | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_open_streams | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_open_table_definitions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_open_tables | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_opened_files | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_opened_plugin_libraries | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_opened_table_definitions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_opened_tables | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_opened_views | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_optimizer_join_prefixes_check_calls | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_performance_schema_lost_total | Total number of MySQL instrumentations that could not be loaded or created due to memory constraints. | COUNTER |
| mysql_global_status_prepared_stmt_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_free_blocks | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_free_memory | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_hits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_inserts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_lowmem_prunes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_not_cached | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_queries_in_cache | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_qcache_total_blocks | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_queries | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_questions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_resultset_metadata_skipped | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rows_read | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rows_sent | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rows_tmp_read | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_clients | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_get_ack | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_net_avg_wait_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_net_wait_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_net_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_no_times | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_no_tx | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_request_ack | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_status | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_timefunc_failures | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_tx_avg_wait_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_tx_wait_time | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_tx_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_wait_pos_backtraverse | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_wait_sessions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_master_yes_tx | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_slave_send_ack | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_semi_sync_slave_status | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_rpl_transactions_multi_engine | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_select_full_join | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_select_full_range_join | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_select_range | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_select_range_check | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_select_scan | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_server_audit_active | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_server_audit_writes_failed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_connections | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_heartbeat_period | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_open_temp_tables | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_received_heartbeats | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_retried_transactions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_running | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slave_skipped_errors | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slaves_connected | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slaves_running | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slow_launch_threads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_slow_queries | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_sort_merge_passes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_sort_priority_queue_sorts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_sort_range | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_sort_rows | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_sort_scan | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_accept_renegotiates | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_accepts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_callback_cache_hits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_client_connects | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_connect_renegotiates | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_ctx_verify_depth | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_ctx_verify_mode | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_default_timeout | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_finished_accepts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_finished_connects | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_session_cache_hits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_session_cache_misses | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_session_cache_overflows | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_session_cache_size | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_session_cache_timeouts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_sessions_reused | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_used_session_cache_entries | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_verify_depth | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_ssl_verify_mode | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_subquery_cache_hit | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_subquery_cache_miss | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_syncs | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_locks_immediate | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_locks_waited | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_open_cache_active_instances | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_open_cache_hits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_open_cache_misses | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_table_open_cache_overflows | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_tc_log_max_pages_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_tc_log_page_size | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_tc_log_page_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threadpool_idle_threads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threadpool_threads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threads_cached | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threads_connected | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threads_created | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_threads_running | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_tmp_space_used | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_transactions_gtid_foreign_engine | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_transactions_multi_engine | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_update_scan | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_uptime | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_uptime_since_flush_status | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_applier_thread_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_apply_oooe | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_apply_oool | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_apply_waits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_apply_window | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_causal_reads | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cert_deps_distance | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cert_index_size | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cert_interval | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cluster_conf_id | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cluster_size | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cluster_status | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_cluster_weight | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_commit_oooe | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_commit_oool | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_commit_window | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_connected | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_desync_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_flow_control_paused | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_flow_control_paused_ns | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_flow_control_recv | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_flow_control_sent | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_gmcast_segment | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_last_committed | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_bf_aborts | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_cached_downto | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_cert_failures | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_commits | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_index | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_recv_queue | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_recv_queue_avg | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_recv_queue_max | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_recv_queue_min | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_replays | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_send_queue | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_send_queue_avg | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_send_queue_max | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_send_queue_min | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_local_state | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_open_connections | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_open_transactions | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_protocol_version | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_ready | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_received | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_received_bytes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_repl_data_bytes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_repl_keys | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_repl_keys_bytes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_repl_other_bytes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_replicated | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_replicated_bytes | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_rollbacker_thread_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_status_wsrep_thread_count | Generic metric from SHOW GLOBAL STATUS. | UNTYPED |
| mysql_global_variables_allow_suspicious_udfs | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_analyze_sample_percentage | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_checkpoint_interval | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_checkpoint_log_activity | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_encrypt_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_force_start_after_recovery_failures | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_group_commit_interval | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_log_file_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_max_sort_file_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_page_checksum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_pagecache_age_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_pagecache_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_pagecache_division_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_pagecache_file_hash_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_repair_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_sort_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_aria_used_for_temp_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_auto_increment_increment | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_auto_increment_offset | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_autocommit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_automatic_sp_privileges | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_back_log | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_big_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_alter_two_phase | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_annotate_row_events | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_commit_wait_count | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_commit_wait_usec | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_direct_non_transactional_updates | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_expire_logs_seconds | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_file_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_gtid_index | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_gtid_index_page_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_gtid_index_span_min | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_legacy_event_pos | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_optimize_thread_scheduling | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_row_event_max_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_space_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_binlog_stmt_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_bulk_insert_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_check_constraint_checks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_column_compression_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_column_compression_zlib_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_column_compression_zlib_wrap | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_connect_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_core_file | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_deadlock_search_depth_long | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_deadlock_search_depth_short | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_deadlock_timeout_long | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_deadlock_timeout_short | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_default_password_lifetime | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_default_week_format | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_delay_key_write | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_delayed_insert_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_delayed_insert_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_delayed_queue_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_disconnect_on_expired_password | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_div_precision_increment | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_encrypt_binlog | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_encrypt_tmp_disk_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_encrypt_tmp_files | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_eq_range_index_dive_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_event_scheduler | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_expensive_subquery_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_expire_logs_days | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_explicit_defaults_for_timestamp | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_extra_max_connections | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_extra_port | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_flush | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_flush_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_foreign_key_checks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_ft_max_word_len | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_ft_min_word_len | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_ft_query_expansion_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_general_log | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_group_concat_max_len | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_gtid_cleanup_batch_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_gtid_domain_id | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_gtid_ignore_duplicates | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_gtid_strict_mode | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_compress | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_crypt | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_dynamic_loading | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_geometry | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_openssl | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_profiling | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_query_cache | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_rtree_keys | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_ssl | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_have_symlink | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_histogram_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_host_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_idle_readonly_transaction_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_idle_transaction_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_idle_write_transaction_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_ignore_builtin_innodb | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_in_predicate_conversion_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_adaptive_flushing | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_adaptive_flushing_lwm | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_adaptive_hash_index | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_adaptive_hash_index_parts | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_alter_copy_bulk | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_autoextend_increment | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_autoinc_lock_mode | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buf_dump_status_frequency | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_chunk_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_dump_at_shutdown | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_dump_now | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_dump_pct | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_load_abort | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_load_at_startup | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_load_now | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_buffer_pool_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_cmp_per_index_enabled | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_compression_default | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_compression_failure_threshold_pct | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_compression_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_compression_pad_pct_max | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_data_file_buffering | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_data_file_write_through | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_deadlock_detect | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_default_encryption_key_id | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_disable_sort_file_cache | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_doublewrite | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encrypt_log | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encrypt_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encrypt_temporary_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encryption_rotate_key_age | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encryption_rotation_iops | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_encryption_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_fast_shutdown | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_fatal_semaphore_wait_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_file_per_table | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_fill_factor | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_flush_log_at_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_flush_log_at_trx_commit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_flush_neighbors | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_flush_sync | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_flushing_avg_loops | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_force_primary_key | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_force_recovery | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_enable_diag_print | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_enable_stopword | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_max_token_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_min_token_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_num_word_optimize | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_result_cache_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_sort_pll_degree | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_ft_total_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_immediate_scrub_data_uncompressed | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_io_capacity | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_io_capacity_max | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_lock_wait_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_file_buffering | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_file_mmap | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_file_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_file_write_through | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_spin_wait_delay | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_log_write_ahead_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_lru_flush_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_lru_scan_depth | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_dirty_pages_pct | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_dirty_pages_pct_lwm | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_purge_lag | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_purge_lag_delay | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_purge_lag_wait | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_max_undo_log_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_old_blocks_pct | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_old_blocks_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_online_alter_log_max_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_open_files | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_optimize_fulltext_only | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_page_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_prefix_index_cluster_optimization | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_print_all_deadlocks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_purge_batch_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_purge_rseg_truncate_frequency | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_purge_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_random_read_ahead | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_read_ahead_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_read_io_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_read_only | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_read_only_compressed | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_rollback_on_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_snapshot_isolation | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_sort_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_spin_wait_delay | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_auto_recalc | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_include_delete_marked | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_modified_counter | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_on_metadata | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_persistent | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_persistent_sample_pages | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_traditional | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_stats_transient_sample_pages | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_status_output | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_status_output_locks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_strict_mode | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_sync_spin_loops | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_table_locks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_truncate_temporary_tablespace_now | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_undo_log_truncate | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_undo_tablespaces | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_use_atomic_writes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_use_native_aio | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_innodb_write_io_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_interactive_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_join_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_join_buffer_space_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_join_cache_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_keep_files_on_create | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_cache_age_threshold | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_cache_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_cache_division_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_cache_file_hash_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_key_cache_segments | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_large_files_support | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_large_page_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_large_pages | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_local_infile | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_lock_wait_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_locked_in_memory | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_bin | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_bin_compress | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_bin_compress_min_len | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_bin_trust_function_creators | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_queries_not_using_indexes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slave_updates | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_admin_statements | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_max_warnings | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_min_examined_row_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_query | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_query_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_rate_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_slow_slave_statements | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_tc_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_log_warnings | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_long_query_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_low_priority_updates | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_lower_case_file_system | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_lower_case_table_names | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_master_verify_checksum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_allowed_packet | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_binlog_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_binlog_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_binlog_stmt_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_binlog_total_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_connect_errors | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_connections | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_delayed_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_digest_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_error_count | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_heap_table_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_insert_delayed_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_join_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_length_for_sort_data | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_password_errors | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_prepared_stmt_count | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_recursive_iterations | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_relay_log_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_rowid_filter_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_seeks_for_key | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_session_mem_used | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_sort_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_sp_recursion_depth | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_statement_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_tmp_session_space_usage | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_tmp_total_space_usage | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_user_connections | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_max_write_lock_count | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_metadata_locks_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_metadata_locks_hash_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_min_examined_row_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_mrr_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_data_pointer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_max_sort_file_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_mmap_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_repair_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_sort_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_myisam_use_mmap | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_mysql56_temporal_format | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_net_buffer_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_net_read_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_net_retry_count | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_net_write_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_old | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_old_passwords | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_open_files_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_adjust_secondary_key_costs | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_disk_read_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_disk_read_ratio | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_extra_pruning_depth | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_index_block_copy_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_join_limit_pref_ratio | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_key_compare_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_key_copy_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_key_lookup_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_key_next_find_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_max_sel_arg_weight | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_max_sel_args | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_prune_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_row_copy_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_row_lookup_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_row_next_find_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_rowid_compare_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_rowid_copy_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_scan_setup_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_search_depth | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_selectivity_sampling_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_trace_max_mem_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_use_condition_selectivity | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_optimizer_where_cost | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_accounts_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_digests_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_stages_history_long_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_stages_history_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_statements_history_long_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_statements_history_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_transactions_history_long_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_transactions_history_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_waits_history_long_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_events_waits_history_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_hosts_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_cond_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_cond_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_digest_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_file_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_file_handles | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_file_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_index_stat | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_memory_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_metadata_locks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_mutex_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_mutex_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_prepared_statements_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_program_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_rwlock_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_rwlock_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_socket_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_socket_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_sql_text_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_stage_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_statement_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_statement_stack | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_table_handles | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_table_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_table_lock_stat | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_thread_classes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_max_thread_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_session_connect_attrs_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_setup_actors_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_setup_objects_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_performance_schema_users_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_port | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_preload_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_profiling | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_profiling_history_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_progress_report_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_protocol_version | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_alloc_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_min_res_unit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_strip_comments | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_type | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_cache_wlock_invalidate | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_query_prealloc_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_range_alloc_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_read_binlog_speed_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_read_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_read_only | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_read_rnd_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_relay_log_purge | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_relay_log_recovery | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_relay_log_space_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_replicate_annotate_row_events | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_report_port | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_require_secure_transport | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rowid_merge_buff_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_master_enabled | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_master_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_master_trace_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_master_wait_no_slave | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_slave_delay_master | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_slave_enabled | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_slave_kill_conn_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_rpl_semi_sync_slave_trace_level | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_secure_auth | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_secure_timestamp | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_file_rotate_now | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_file_rotate_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_file_rotations | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_load_on_error | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_logging | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_mode | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_query_log_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_audit_reload_filters | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_server_id | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_session_track_schema | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_session_track_state_change | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_session_track_transaction_info | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_shutdown_wait_for_slaves | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_simple_password_check_digits | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_simple_password_check_letters_same_case | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_simple_password_check_minimal_length | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_simple_password_check_other_characters | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_skip_external_locking | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_skip_grant_tables | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_skip_name_resolve | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_skip_networking | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_skip_show_database | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_compressed_protocol | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_connections_needed_for_purge | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_domain_parallel_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_max_allowed_packet | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_max_statement_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_net_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_parallel_max_queued | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_parallel_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_parallel_workers | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_run_triggers_for_rbr | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_skip_errors | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_sql_verify_checksum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_transaction_retries | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slave_transaction_retry_interval | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slow_launch_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_slow_query_log | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sort_buffer_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_auto_is_null | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_big_selects | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_buffer_result | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_if_exists | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_log_bin | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_log_off | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_notes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_quote_show_create | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_safe_updates | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_select_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_slave_skip_counter | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sql_warnings | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_standard_compliant_cte | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_stored_program_cache | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_strict_password_validation | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sync_binlog | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sync_frm | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sync_master_info | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sync_relay_log | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_sync_relay_log_info | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_system_versioning_insert_history | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_table_definition_cache | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_table_open_cache | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_table_open_cache_instances | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tcp_keepalive_interval | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tcp_keepalive_probes | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tcp_keepalive_time | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tcp_nodelay | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_cache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_dedicated_listener | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_exact_stats | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_idle_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_max_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_oversubscribe | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_prio_kickup_timer | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_reshuffle_group_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_pool_stall_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_thread_stack | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tmp_disk_table_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tmp_memory_table_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tmp_table_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_transaction_alloc_block_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_transaction_prealloc_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_transaction_read_only | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_tx_read_only | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_unique_checks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_updatable_views_with_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_userstat | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wait_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_auto_increment_control | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_black_box_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_certificate_expiration_hours_warning | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_certify_nonpk | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_convert_lock_to_trx | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_desync | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_dirty_reads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_drupal_282555_workaround | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_gtid_domain_id | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_gtid_mode | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_ignore_apply_errors | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_load_data_splitting | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_log_conflicts | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_max_ws_rows | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_max_ws_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_mysql_replication_bundle | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_on | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_base_port | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_cert_log_conflicts | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_cert_optimistic_pa | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_debug | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_auto_evict | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_causal_keepalive_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_delay_margin | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_delayed_keep_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_inactive_check_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_inactive_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_info_log_mask | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_install_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_join_retrans_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_keepalive_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_max_install_timeouts | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_send_window | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_stats_report_period | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_suspect_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_use_aggregate | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_user_send_window | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_version | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_evs_view_forget_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_keep_pages_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_keep_plaintext_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_mem_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_page_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_recover | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcache_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_fc_debug | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_fc_factor | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_fc_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_fc_master_slave | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_fc_single_primary | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_max_packet_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_max_throttle | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_recv_q_hard_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_recv_q_soft_limit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_sync_donor | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gcs_vote_policy | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gmcast_mcast_ttl | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gmcast_peer_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gmcast_segment | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gmcast_time_wait | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_gmcast_version | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_announce_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_bootstrap | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_checksum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_ignore_quorum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_ignore_sb | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_linger | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_npvo | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_recovery | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_version | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_wait_prim | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_wait_prim_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_pc_weight | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_protonet_version | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_repl_causal_read_timeout | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_repl_commit_order | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_repl_max_ws_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_repl_proto_max | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_checksum | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_dynamic | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_ssl | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_ssl_cipher | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_ssl_compression | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_provider_socket_ssl_reload | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_recover | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_restart_slave | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_retry_autocommit | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_slave_fk_checks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_slave_threads | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_slave_uk_checks | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_sst_donor_rejects_queries | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_sync_wait | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_global_variables_wsrep_trx_fragment_size | Generic gauge metric from SHOW GLOBAL VARIABLES. | GAUGE |
| mysql_info_schema_innodb_cmp_compress_ops_ok_total | Number of times a B-tree page of the size PAGE_SIZE has been successfully compressed. | COUNTER |
| mysql_info_schema_innodb_cmp_compress_ops_total | Number of times a B-tree page of the size PAGE_SIZE has been compressed. | COUNTER |
| mysql_info_schema_innodb_cmp_compress_time_seconds_total | Total time in seconds spent in attempts to compress B-tree pages. | COUNTER |
| mysql_info_schema_innodb_cmp_uncompress_ops_total | Number of times a B-tree page of the size PAGE_SIZE has been uncompressed. | COUNTER |
| mysql_info_schema_innodb_cmp_uncompress_time_seconds_total | Total time in seconds spent in uncompressing B-tree pages. | COUNTER |
| mysql_info_schema_innodb_cmpmem_pages_free_total | Number of blocks of the size PAGE_SIZE that are currently available for allocation. | COUNTER |
| mysql_info_schema_innodb_cmpmem_pages_used_total | Number of blocks of the size PAGE_SIZE that are currently in use. | COUNTER |
| mysql_info_schema_innodb_cmpmem_relocation_ops_total | Number of times a block of the size PAGE_SIZE has been relocated. | COUNTER |
| mysql_info_schema_innodb_cmpmem_relocation_time_seconds_total | Total time in seconds spent in relocating blocks. | COUNTER |
| mysql_transaction_isolation | MySQL transaction isolation. | GAUGE |
| mysql_up | Whether the MySQL server is up. | GAUGE |
| mysql_version_info | MySQL version and distribution. | GAUGE |


## MaxScale metrics


The following metrics are available for `MaxScale` instances:


| Metric Name | Description | Type |
| --- | --- | --- |
| Metric Name | Description | Type |
| maxscale_exporter_collector_duration_seconds | Collector time duration. | GAUGE |
| maxscale_exporter_last_scrape_error | Whether the last scrape of metrics from MariaDB resulted in an error (1 for error, 0 for success). | GAUGE |
| maxscale_exporter_scrapes_total | Total number of times MariaDB was scraped for metrics. | COUNTER |
| maxscale_logging_high_precision | Whether high precision logging is active. | GAUGE |
| maxscale_logging_level | The current logging levels active. | GAUGE |
| maxscale_logging_maxlog | Whether maxlog is active. | GAUGE |
| maxscale_logging_syslog | Whether syslog is active. | GAUGE |
| maxscale_logging_throttling_count | The number of logging throttling. | GAUGE |
| maxscale_logging_throttling_suppress_milliseconds | The value of throttling suppress_ms. | GAUGE |
| maxscale_logging_throttling_suppress_window_milliseconds | The value of throttling window_ms. | GAUGE |
| maxscale_modules | Maxscale modules currently enabled. | GAUGE |
| maxscale_monitor | Maxscale Monitor. | GAUGE |
| maxscale_server_active_operations | The number of active operations. | GAUGE |
| maxscale_server_adaptive_avg_select_time | The adaptive average select time. This is always zero. | GAUGE |
| maxscale_server_connection_pool_empty | The current connection pool empty | GAUGE |
| maxscale_server_connections | The current number of connections to the server. | GAUGE |
| maxscale_server_max_connections | The max number of connections. | GAUGE |
| maxscale_server_max_pool_size | The current max pool size, | GAUGE |
| maxscale_server_persistent_connections | The number of persistent connections to the server. | GAUGE |
| maxscale_server_reused_connections | The number of Re-used Connections by the server. | GAUGE |
| maxscale_server_routed_packets | The number of routed packets to the server, | GAUGE |
| maxscale_server_state | The current state of the server. | GAUGE |
| maxscale_server_total_connections | The total number of connections to the server. | COUNTER |
| maxscale_service_active_connections | The total number of active operations to the service. | GAUGE |
| maxscale_service_connections | The current number of connections to the server. | GAUGE |
| maxscale_service_state | The current state of each service. | GAUGE |
| maxscale_service_statistics_connections | The total number of connections to the service. | GAUGE |
| maxscale_service_statistics_failed_auths | The total number of failed authentications to the service. | COUNTER |
| maxscale_service_statistics_max_connections | The max number of connections to the service. | GAUGE |
| maxscale_service_statistics_routed_packets | The total number of routed packets to the service. | GAUGE |
| maxscale_service_statistics_total_connections | The total number of connections to the service. | COUNTER |
| maxscale_service_total_connections | The total number of connections to the server. | COUNTER |
| maxscale_threads_accepts | The number of accept events. | COUNTER |
| maxscale_threads_blocking_polls | The number of non-blocking poll cycles that will be done before a blocking poll takes place. | GAUGE |
| maxscale_threads_count | The number of threads | GAUGE |
| maxscale_threads_current_descriptors | The current number of descriptors handled by each thread. | GAUGE |
| maxscale_threads_errors | The number of error events. | COUNTER |
| maxscale_threads_event_queue_length | The amount of I/O events returned by one call to epoll_wait(). | GAUGE |
| maxscale_threads_hangups | The number of hangup events. | COUNTER |
| maxscale_threads_load_last_hour | The load during the last 60m. | GAUGE |
| maxscale_threads_load_last_minute | The load during the last 60s. | GAUGE |
| maxscale_threads_load_last_second | The load during the last second. | GAUGE |
| maxscale_threads_max_event_queue_length | The maximum amount of I/O events returned by one call to epoll_wait(). | GAUGE |
| maxscale_threads_max_exec_time | The maximum time it took to process an I/O event. | GAUGE |
| maxscale_threads_max_queue_time | The maximum time it took before an I/O event became ready for processing (ms). | GAUGE |
| maxscale_threads_reads | The number of read events. | COUNTER |
| maxscale_threads_stack_size | The stack size of each worker. | GAUGE |
| maxscale_threads_total_descriptors | The total number of descriptors handled by each thread since MaxScale startup. | GAUGE |
| maxscale_threads_writes | The number of write events. | COUNTER |
| maxscale_up | Whether the Maxscale server is up. | GAUGE |
| maxscale_uptime_seconds | Maxscale uptime in seconds | GAUGE |
| maxscale_version | Maxscale Version | GAUGE |


<sub>_This page is licensed: CC BY-SA / Gnu FDL_</sub>


{% @marketo/form formId="4316" %}
