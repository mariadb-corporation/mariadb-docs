# Observability

This page provides a high-level overview of the Observability functionality in SkySQL.

In order to interact with our Observability APIs, an [API KEY](https://skysqlinc.github.io/skysql-docs/Security/Managing%20API%20keys/) must be generated.
Throughout this document, we will refer to it as `{{SKYSQL_API_KEY}}`.

Additionally, you will need the SkySQL Database ID, available by clicking on any of your existing services from the [SkySQL Console](https://app.skysql.com/), and navigating to the Details page.
We will Refer to the Database ID as `{{SKYSQL_DATABASE_ID}}` throughout this document.

For the impatient reader, we jump right to the [Integrations section](#integrations), then for ones who are building custom
instrumentation, we provide a detailed list of [APIs](#apis) and their relevant documentation.

# Integrations

## Datadog
Using the [Datadog](https://www.datadoghq.com/) integration, you can instrument Observability metrics from SkySQL into your Datadog account. 
This integration allows you to monitor and visualize SkySQL metrics alongside other services in your Datadog dashboard.

### Requirements.
You will need your Datadog API key to set up the integration.  We will refer to it as `{{DD_API_KEY}}` throughout this document.

### Agent Setup.
You will need to configure the Datadog Agent to pull metrics from us.  Here is an example of how you can setup the [DataDog Agent](https://docs.datadoghq.com/agent/):

1. Create a local directory for configuration to be mapped to the Docker Container:
```shell
mkdir -p /home/datadog-agent/openmetrics
```
2. Create a `conf.yaml` file in your `openmetrics` directory with:
```yaml
init_config:

instances:
  - openmetrics_endpoint: https://api.skysql.com/observability/v2/metrics
    namespace: {{SKYSQL_DATABASE_ID}}
    extra_headers:
      X-API-KEY: {{SKYSQL_API_KEY}}
    metrics:
      - '.*'
```
3. Send the metrics to the correct DataDog Site.
You should refer to [DataDog Site documentation](https://docs.datadoghq.com/getting_started/site/) to determine the correct `SITE PARAMETER` for your account.
This resource provides a comprehensive list of Datadog sites and their corresponding `SITE PARAMETER` values, ensuring that your data is sent to the correct regional Datadog instance.
We will refer to it as `{{DD_SITE_PARAMETER}}` throughout this document.

4. Run the Datadog Agent Docker Container with the following command:
```shell
docker run -v /home/datadog-agent/openmetrics:/etc/datadog-agent/conf.d/openmetrics.d:ro \
  -e DD_API_KEY={{DD_API_KEY}} -e DD_HOSTNAME="my-agent" -e DD_SITE="{{DD_SITE_PARAMETER}}" \ 
  -e DD_LOG_LEVEL="info" gcr.io/datadoghq/agent:7
```
5. You should see the metrics soon to be available in [DataDog Metrics Explorer](https://app.datadoghq.com/metric/explorer) 

### Testing [SkySQL APIs](#apis)
If you can always check if the Observability API is working successfully by calling it directly:
```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```
Detailed documentation on how to interact with our [APIs](#apis) follows:

# APIs
To build instrumentation around our [Observability APIs](https://apidocs.skysql.com/#/Observability), we expose the following endpoints:

### Logs
SkySQL exposes a set of log-related endpoints under `observability/v2/logs`, allowing you to:
- Retrieve logs within a specified date range
- Download log archives
- Query log types and servers
- Manage log retention settings

Refer to the [Observability section of the SkySQL API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

### Metrics
You can retrieve metrics (in Prometheus-compatible format) from SkySQL using the `observability/v2/metrics` endpoint. To learn more about query parameters and usage, see:

Example:
```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```

Refer to the [Observability section of the SkySQL API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

## API Documentation
For the complete, detailed API reference (including request/response formats, error codes, etc.), please see the official SkySQL API docs here:

- [SkySQL Observability (Logs + Metrics) Endpoints](https://apidocs.skysql.com/#/Observability).
- [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

## Appendix

### Table A. Key Observability Metric Series
We export the folowing metrics as part of the [metrics](#metrics) endpoint:


| Metric                                              |
|-----------------------------------------------------|
| mariadb_galera_evs_repl_latency_avg_seconds         |
| mariadb_galera_evs_repl_latency_max_seconds         |
| mariadb_galera_evs_repl_latency_min_seconds         |
| mariadb_galera_status_info                          |
| mariadb_global_status_aborted_clients               |
| mariadb_global_status_aborted_connects              |
| mariadb_global_status_buffer_pool_pages             |
| mariadb_global_status_bytes_received                |
| mariadb_global_status_bytes_sent                    |
| mariadb_global_status_commands_total                |
| mariadb_global_status_created_tmp_disk_tables       |
| mariadb_global_status_created_tmp_files             |
| mariadb_global_status_created_tmp_tables            |
| mariadb_global_status_handlers_total                |
| mariadb_global_status_innodb_data_read              |
| mariadb_global_status_innodb_data_written           |
| mariadb_global_status_innodb_num_open_files         |
| mariadb_global_status_innodb_page_size              |
| mariadb_global_status_open_files                    |
| mariadb_global_status_open_table_definitions        |
| mariadb_global_status_open_tables                   |
| mariadb_global_status_opened_files                  |
| mariadb_global_status_opened_table_definitions      |
| mariadb_global_status_opened_tables                 |
| mariadb_global_status_queries                       |
| mariadb_global_status_questions                     |
| mariadb_global_status_rows_read                     |
| mariadb_global_status_rows_sent                     |
| mariadb_global_status_select_full_join              |
| mariadb_global_status_select_full_range_join        |
| mariadb_global_status_select_range                  |
| mariadb_global_status_select_range_check            |
| mariadb_global_status_select_scan                   |
| mariadb_global_status_slave_running                 |
| mariadb_global_status_slow_queries                  |
| mariadb_global_status_sort_merge_passes             |
| mariadb_global_status_sort_range                    |
| mariadb_global_status_sort_rows                     |
| mariadb_global_status_sort_scan                     |
| mariadb_global_status_table_locks_immediate         |
| mariadb_global_status_table_locks_waited            |
| mariadb_global_status_table_open_cache_hits         |
| mariadb_global_status_table_open_cache_misses       |
| mariadb_global_status_table_open_cache_overflows    |
| mariadb_global_status_threads_cached                |
| mariadb_global_status_threads_connected             |
| mariadb_global_status_threads_created               |
| mariadb_global_status_threads_running               |
| mariadb_global_status_uptime                        |
| mariadb_global_status_wsrep_cert_deps_distance      |
| mariadb_global_status_wsrep_cluster_conf_id         |
| mariadb_global_status_wsrep_cluster_size            |
| mariadb_global_status_wsrep_cluster_status          |
| mariadb_global_status_wsrep_connected               |
| mariadb_global_status_wsrep_flow_control_paused     |
| mariadb_global_status_wsrep_last_committed          |
| mariadb_global_status_wsrep_local_recv_queue        |
| mariadb_global_status_wsrep_local_recv_queue_avg    |
| mariadb_global_status_wsrep_local_recv_queue_max    |
| mariadb_global_status_wsrep_local_recv_queue_min    |
| mariadb_global_status_wsrep_local_send_queue        |
| mariadb_global_status_wsrep_local_send_queue_avg    |
| mariadb_global_status_wsrep_local_send_queue_max    |
| mariadb_global_status_wsrep_local_send_queue_min    |
| mariadb_global_status_wsrep_local_state             |
| mariadb_global_status_wsrep_ready                   |
| mariadb_global_status_wsrep_replicated              |
| mariadb_global_status_wsrep_replicated_bytes        |
| mariadb_global_variables_gtid_current_pos           |
| mariadb_global_variables_innodb_buffer_pool_size    |
| mariadb_global_variables_innodb_log_buffer_size     |
| mariadb_global_variables_key_buffer_size            |
| mariadb_global_variables_max_connections            |
| mariadb_global_variables_open_files_limit           |
| mariadb_global_variables_query_cache_size           |
| mariadb_global_variables_read_only                  |
| mariadb_global_variables_table_open_cache           |
| mariadb_info_schema_engine_table_count_total        |
| mariadb_info_schema_table_size                      |
| mariadb_security_users_without_passwords            |
| mariadb_slave_status_exec_master_log_pos            |
| mariadb_slave_status_last_io_errno                  |
| mariadb_slave_status_last_sql_errno                 |
| mariadb_slave_status_read_master_log_pos            |
| mariadb_slave_status_relay_log_pos                  |
| mariadb_slave_status_seconds_behind_master          |
| mariadb_slave_status_slave_io_running               |
| mariadb_slave_status_slave_sql_running              |
| mariadb_up                                          |
| mariadb_xpand_activity_core0                        |
| mariadb_xpand_activity_til                          |
| mariadb_xpand_capacity_disk_system_avail_bytes      |
| mariadb_xpand_capacity_disk_system_max_bytes        |
| mariadb_xpand_capacity_disk_system_usage_ratio      |
| mariadb_xpand_capacity_disk_total_usage_percent     |
| mariadb_xpand_cluster_nodes_in_quorum               |
| mariadb_xpand_cluster_total_nodes                   |
| mariadb_xpand_cluster_uptime_seconds                |
| mariadb_xpand_containers_rows                       |
| mariadb_xpand_cpu_load                              |
| mariadb_xpand_io_disk_latency_seconds               |
| mariadb_xpand_io_network_bytes                      |
| mariadb_xpand_io_network_latency_seconds            |
| mariadb_xpand_memory_bm_bytes                       |
| mariadb_xpand_memory_reserved_bytes                 |
| mariadb_xpand_memory_total_bytes                    |
| mariadb_xpand_memory_working_bytes                  |
| mariadb_xpand_qps                                   |
| mariadb_xpand_rebalancer_jobs_queued                |
| mariadb_xpand_rebalancer_rebalancer_rebalance       |
| mariadb_xpand_rebalancer_rebalancer_reprotects      |
| mariadb_xpand_rebalancer_rebalancer_reranks         |
| mariadb_xpand_rebalancer_rebalancer_softfail_reprotects |
| mariadb_xpand_rebalancer_rebalancer_splits          |
| mariadb_xpand_rebalancer_underprotected_slices      |
| mariadb_xpand_response_time_seconds                 |
| mariadb_xpand_sessions                              |
| mariadb_xpand_sessions_time_in_state                |
| mariadb_xpand_sessions_trx_age                      |
| mariadb_xpand_stats_Com_alter_cluster               |
| mariadb_xpand_stats_Com_delete                      |
| mariadb_xpand_stats_Com_delete_seconds              |
| mariadb_xpand_stats_Com_insert                      |
| mariadb_xpand_stats_Com_insert_seconds              |
| mariadb_xpand_stats_Com_select                      |
| mariadb_xpand_stats_Com_select_seconds              |
| mariadb_xpand_stats_Com_set_option                  |
| mariadb_xpand_stats_Com_show_slave_status           |
| mariadb_xpand_stats_Com_show_status                 |
| mariadb_xpand_stats_Com_show_variables              |
| mariadb_xpand_stats_Com_update                      |
| mariadb_xpand_stats_Com_update_seconds              |
| mariadb_xpand_stats_connections                     |
| mariadb_xpand_tps                                   |
| mariadb_xpand_wals_avg_sync_time_seconds            |
| maxscale_modules                                    |
| maxscale_server_active_operations                   |
| maxscale_server_adaptive_avg_select_time            |
| maxscale_server_connection_pool_empty               |
| maxscale_server_connections                         |
| maxscale_server_max_connections                     |
| maxscale_server_max_pool_size                       |
| maxscale_server_persistent_connections              |
| maxscale_server_reused_connections                  |
| maxscale_server_routed_packets                      |
| maxscale_server_total_connections                   |
| maxscale_service_connections                        |
| maxscale_threads_count                              |
| maxscale_threads_current_descriptors                |
| maxscale_threads_errors                             |
| maxscale_threads_event_queue_length                 |
| maxscale_threads_hangups                            |
| maxscale_threads_max_queue_time                     |
| maxscale_threads_reads                              |
| maxscale_threads_stack_size                         |
| maxscale_threads_total_descriptors                  |
| maxscale_threads_writes                             |
| maxscale_up                                         |
| maxscale_uptime_seconds                             |
| process_resident_memory_bytes                       |
