---
description: >-
  MariaDB Cloud Observability exposes runtime logs and metrics through APIs and
  integrations like Datadog and Splunk, requiring an API key and Database ID for
  instrumentation and dashboard configuration.
icon: telescope
---

# Observability

This page provides a high-level overview of the Observability functionality in MariaDB Cloud.

In order to interact with our Observability APIs, an [API KEY](../security/managing-api-keys.md) must be generated. Throughout this document, we will refer to it as `{{SKYSQL_API_KEY}}`.

Additionally, you will need the MariaDB Cloud Database ID, available by clicking on any of your existing services from the [MariaDB Cloud Console](https://app.skysql.com/) and navigating to the Details page. We will refer to the Database ID as `{{SKYSQL_DATABASE_ID}}` throughout this document.

For the impatient reader, we jump right to the [Integrations section](observability.md#integrations), then for ones who are building custom instrumentation, we provide a detailed list of [APIs](observability.md#apis) and their relevant documentation.

## Integrations

### Datadog

Using the [Datadog](https://www.datadoghq.com/) integration, you can instrument Observability metrics from MariaDB Cloud into your Datadog account. This integration allows you to monitor and visualize MariaDB Cloud metrics alongside other services in your Datadog dashboard.

#### Requirements

You will need your Datadog API key to set up the integration. We will refer to it as `{{DD_API_KEY}}` throughout this document.

#### Agent Setup

You will need to configure the Datadog Agent to pull metrics from us. Here is an example of how you can set up the [DataDog Agent](https://docs.datadoghq.com/agent/):

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

3. Send the metrics to the correct DataDog Site. You should refer to the [DataDog Site documentation](https://docs.datadoghq.com/getting_started/site/) to determine the correct `SITE PARAMETER` for your account. This resource provides a comprehensive list of Datadog sites and their corresponding `SITE PARAMETER` values, ensuring that your data is sent to the correct regional Datadog instance. We will refer to it as `{{DD_SITE_PARAMETER}}` throughout this document.
4. Run the Datadog Agent Docker Container with the following command:

```shell
docker run -v /home/datadog-agent/openmetrics:/etc/datadog-agent/conf.d/openmetrics.d:ro \
  -e DD_API_KEY={{DD_API_KEY}} -e DD_HOSTNAME="my-agent" -e DD_SITE="{{DD_SITE_PARAMETER}}" \ 
  -e DD_LOG_LEVEL="info" gcr.io/datadoghq/agent:7
```

5. You should see the metrics soon to be available in [DataDog Metrics Explorer](https://app.datadoghq.com/metric/explorer).

#### Testing [MariaDB Cloud APIs](observability.md#apis)

If you can always check if the Observability API is working successfully by calling it directly:

```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```

### Splunk

Using the [Splunk](https://www.splunk.com/) integration, you can send MariaDB Cloud logs and metrics to Splunk Cloud Platform, where you can search them with SPL and chart them on dashboards next to the rest of your monitored infrastructure.

The integration is distributed as a package in the public [mariadb-corporation/splunk-integration](https://github.com/mariadb-corporation/splunk-integration) repository, which holds the collector scripts, deployment examples, dashboard examples, and the full setup instructions.

#### Requirements

* A MariaDB Cloud API key (`{{SKYSQL_API_KEY}}`) with read access to the Observability API.
* A Splunk Cloud Platform instance with the HTTP Event Collector (HEC) enabled.
* A HEC token with write access to the target index. Logs go to an events index (`mariadb_logs` by default); metrics go to a **Metrics**-type index (`mariadb_metrics` by default).
* Python 3.7 or later with the `requests` library.

A Splunk universal forwarder is not required. Both collectors push data directly to Splunk Cloud through HEC.

#### What the package provides

The package contains two collectors. They are independent, so you can deploy either one on its own or both together.

| Collector | Endpoints used                                                     | What it sends to Splunk                                                                                                                                                              |
| --------- | ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Logs      | `observability/v2/logs/query`, `observability/v2/logs/archive`     | Error log, audit log, and MaxScale log lines, extracted from the downloaded log archives and converted to HEC events. A per-archive checkpoint keeps already-ingested lines from being sent again. |
| Metrics   | `observability/v2/metrics`                                         | The Prometheus-format metric series from the [metrics](observability.md#metrics) endpoint, parsed and converted to HEC metric events.                                                 |

#### Deployment options

Each collector runs in any of these modes:

* **Daemon** (recommended) — a persistent process that polls on a fixed interval (`--daemon --interval <seconds>`), managed by systemd, launchd, or a Kubernetes deployment. The repository includes an example unit file for each.
* **Standalone run** — a single collection cycle, useful for verifying end-to-end delivery before you set up a service.
* **AWS Lambda** — scheduled functions triggered by EventBridge Scheduler, with credentials read from AWS Secrets Manager and the logs checkpoint stored in Amazon S3. Both a Terraform stack and a CloudFormation template are included.

Configuration is entirely through environment variables — `MARIADB_API_KEY`, `SPLUNK_HEC_URL`, and `SPLUNK_HEC_TOKEN` are required, with optional overrides for the index, source, sourcetype, batch size, and retry behavior. There is no configuration file. See the repository for the complete list.

{% hint style="info" %}
The repository also ships example Splunk dashboards and SPL searches for both signals, in `logs/SPLUNK_DASHBOARDS.md` and `metrics/SPLUNK_DASHBOARDS.md`.
{% endhint %}

Detailed documentation on how to interact with our [APIs](observability.md#apis) follows:

## APIs

To build instrumentation around our [Observability APIs](https://apidocs.skysql.com/#/Observability), we expose the following endpoints:

#### Logs

MariaDB Cloud exposes a set of log-related endpoints under `observability/v2/logs`, allowing you to:

* Retrieve logs within a specified date range
* Download log archives
* Query log types and servers
* Manage log retention settings

Refer to the [Observability section of the MariaDB Cloud API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

#### Metrics

You can retrieve metrics (in Prometheus-compatible format) from MariaDB Cloud using the `observability/v2/metrics` endpoint. To learn more about query parameters and usage, see:

Example:

```shell
curl --location 'https://api.skysql.com/observability/v2/metrics' \
--header 'X-API-KEY: {{SKYSQL_API_KEY}}'
```

Refer to the [Observability section of the MariaDB Cloud API docs](https://apidocs.skysql.com/#/Observability) for the full list of parameters and responses.

### API Documentation

For the complete, detailed API reference (including request/response formats, error codes, etc.), please see the official MariaDB Cloud API docs here:

* [MariaDB Cloud Observability (Logs + Metrics) Endpoints](https://apidocs.skysql.com/#/Observability).
* [Prometheus HTTP API](https://prometheus.io/docs/prometheus/latest/querying/api/).

### Appendix

#### Table A. Key Observability Metric Series

The following metrics are exported as part of the [metrics](observability.md#metrics) endpoint. The **Component** column shows what each metric prefix covers:

* `mariadb_global_*`, `mariadb_info_schema_*`, `mariadb_security_*`, `mariadb_slave_status_*`, `mariadb_up`: MariaDB Server status and variables
* `mariadb_galera_*`: Galera cluster replication
* `mariadb_server_*`: CPU, memory, disk, and network usage of the server's container and process
* `mariadb_service_*`: status and role of the service and its servers
* `maxscale_*`: MaxScale
* `mariadb_xpand_*`: Xpand
* `gridgain_*`: GridGain, including the query result cache

The endpoint returns only the metrics for components your services run. For example, `maxscale_*` metrics appear only for services that include MaxScale.

<!-- DOCS-6580: the mariadb_xpand_stats_* rows list the intended names. The cortex-exporter rename rule `ts_(.+)` is unanchored and currently rewrites them (e.g. mariadb_xpand_stamariadb_service_Com_delete); raised with the Cloud team. -->

| Metric                                                    | Component        |
| --------------------------------------------------------- | ---------------- |
| `mariadb_global_status_aborted_clients`                   | MariaDB Server   |
| `mariadb_global_status_aborted_connects`                  | MariaDB Server   |
| `mariadb_global_status_buffer_pool_pages`                 | MariaDB Server   |
| `mariadb_global_status_bytes_received`                    | MariaDB Server   |
| `mariadb_global_status_bytes_sent`                        | MariaDB Server   |
| `mariadb_global_status_commands_total`                    | MariaDB Server   |
| `mariadb_global_status_created_tmp_disk_tables`           | MariaDB Server   |
| `mariadb_global_status_created_tmp_files`                 | MariaDB Server   |
| `mariadb_global_status_created_tmp_tables`                | MariaDB Server   |
| `mariadb_global_status_handlers_total`                    | MariaDB Server   |
| `mariadb_global_status_innodb_data_read`                  | MariaDB Server   |
| `mariadb_global_status_innodb_data_written`               | MariaDB Server   |
| `mariadb_global_status_innodb_num_open_files`             | MariaDB Server   |
| `mariadb_global_status_innodb_page_size`                  | MariaDB Server   |
| `mariadb_global_status_open_files`                        | MariaDB Server   |
| `mariadb_global_status_open_table_definitions`            | MariaDB Server   |
| `mariadb_global_status_open_tables`                       | MariaDB Server   |
| `mariadb_global_status_opened_files`                      | MariaDB Server   |
| `mariadb_global_status_opened_table_definitions`          | MariaDB Server   |
| `mariadb_global_status_opened_tables`                     | MariaDB Server   |
| `mariadb_global_status_queries`                           | MariaDB Server   |
| `mariadb_global_status_questions`                         | MariaDB Server   |
| `mariadb_global_status_rows_read`                         | MariaDB Server   |
| `mariadb_global_status_rows_sent`                         | MariaDB Server   |
| `mariadb_global_status_select_full_join`                  | MariaDB Server   |
| `mariadb_global_status_select_full_range_join`            | MariaDB Server   |
| `mariadb_global_status_select_range`                      | MariaDB Server   |
| `mariadb_global_status_select_range_check`                | MariaDB Server   |
| `mariadb_global_status_select_scan`                       | MariaDB Server   |
| `mariadb_global_status_slave_running`                     | MariaDB Server   |
| `mariadb_global_status_slow_queries`                      | MariaDB Server   |
| `mariadb_global_status_sort_merge_passes`                 | MariaDB Server   |
| `mariadb_global_status_sort_range`                        | MariaDB Server   |
| `mariadb_global_status_sort_rows`                         | MariaDB Server   |
| `mariadb_global_status_sort_scan`                         | MariaDB Server   |
| `mariadb_global_status_table_locks_immediate`             | MariaDB Server   |
| `mariadb_global_status_table_locks_waited`                | MariaDB Server   |
| `mariadb_global_status_table_open_cache_hits`             | MariaDB Server   |
| `mariadb_global_status_table_open_cache_misses`           | MariaDB Server   |
| `mariadb_global_status_table_open_cache_overflows`        | MariaDB Server   |
| `mariadb_global_status_threads_cached`                    | MariaDB Server   |
| `mariadb_global_status_threads_connected`                 | MariaDB Server   |
| `mariadb_global_status_threads_created`                   | MariaDB Server   |
| `mariadb_global_status_threads_running`                   | MariaDB Server   |
| `mariadb_global_status_uptime`                            | MariaDB Server   |
| `mariadb_global_status_wsrep_cert_deps_distance`          | MariaDB Server   |
| `mariadb_global_status_wsrep_cluster_conf_id`             | MariaDB Server   |
| `mariadb_global_status_wsrep_cluster_size`                | MariaDB Server   |
| `mariadb_global_status_wsrep_cluster_status`              | MariaDB Server   |
| `mariadb_global_status_wsrep_connected`                   | MariaDB Server   |
| `mariadb_global_status_wsrep_flow_control_paused`         | MariaDB Server   |
| `mariadb_global_status_wsrep_last_committed`              | MariaDB Server   |
| `mariadb_global_status_wsrep_local_recv_queue`            | MariaDB Server   |
| `mariadb_global_status_wsrep_local_recv_queue_avg`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_recv_queue_max`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_recv_queue_min`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_send_queue`            | MariaDB Server   |
| `mariadb_global_status_wsrep_local_send_queue_avg`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_send_queue_max`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_send_queue_min`        | MariaDB Server   |
| `mariadb_global_status_wsrep_local_state`                 | MariaDB Server   |
| `mariadb_global_status_wsrep_ready`                       | MariaDB Server   |
| `mariadb_global_status_wsrep_replicated`                  | MariaDB Server   |
| `mariadb_global_status_wsrep_replicated_bytes`            | MariaDB Server   |
| `mariadb_global_variables_gtid_current_pos`               | MariaDB Server   |
| `mariadb_global_variables_innodb_buffer_pool_size`        | MariaDB Server   |
| `mariadb_global_variables_innodb_log_buffer_size`         | MariaDB Server   |
| `mariadb_global_variables_key_buffer_size`                | MariaDB Server   |
| `mariadb_global_variables_max_connections`                | MariaDB Server   |
| `mariadb_global_variables_open_files_limit`               | MariaDB Server   |
| `mariadb_global_variables_query_cache_size`               | MariaDB Server   |
| `mariadb_global_variables_read_only`                      | MariaDB Server   |
| `mariadb_global_variables_table_open_cache`               | MariaDB Server   |
| `mariadb_info_schema_engine_table_count_total`            | MariaDB Server   |
| `mariadb_info_schema_table_size`                          | MariaDB Server   |
| `mariadb_security_users_without_passwords`                | MariaDB Server   |
| `mariadb_slave_status_exec_master_log_pos`                | MariaDB Server   |
| `mariadb_slave_status_last_io_errno`                      | MariaDB Server   |
| `mariadb_slave_status_last_sql_errno`                     | MariaDB Server   |
| `mariadb_slave_status_read_master_log_pos`                | MariaDB Server   |
| `mariadb_slave_status_relay_log_pos`                      | MariaDB Server   |
| `mariadb_slave_status_seconds_behind_master`              | MariaDB Server   |
| `mariadb_slave_status_slave_io_running`                   | MariaDB Server   |
| `mariadb_slave_status_slave_sql_running`                  | MariaDB Server   |
| `mariadb_up`                                              | MariaDB Server   |
| `mariadb_galera_evs_repl_latency_max_seconds`             | Galera           |
| `mariadb_galera_state_comments`                           | Galera           |
| `mariadb_galera_wsrep_cluster_status`                     | Galera           |
| `mariadb_galera_wsrep_connected`                          | Galera           |
| `mariadb_galera_wsrep_desync_count`                       | Galera           |
| `mariadb_galera_wsrep_flow_control_paused_ns`             | Galera           |
| `mariadb_galera_wsrep_flow_control_recv`                  | Galera           |
| `mariadb_galera_wsrep_flow_control_sent`                  | Galera           |
| `mariadb_galera_wsrep_local_bf_aborts`                    | Galera           |
| `mariadb_galera_wsrep_local_cert_failures`                | Galera           |
| `mariadb_galera_wsrep_local_recv_queue`                   | Galera           |
| `mariadb_galera_wsrep_local_state`                        | Galera           |
| `mariadb_galera_wsrep_ready`                              | Galera           |
| `mariadb_galera_wsrep_received`                           | Galera           |
| `mariadb_galera_wsrep_received_bytes`                     | Galera           |
| `mariadb_galera_wsrep_replicated`                         | Galera           |
| `mariadb_galera_wsrep_replicated_bytes`                   | Galera           |
| `mariadb_server_cpu`                                      | Server resources |
| `mariadb_server_cpu_system_seconds_total`                 | Server resources |
| `mariadb_server_cpu_user_seconds_total`                   | Server resources |
| `mariadb_server_fs_reads_bytes_total`                     | Server resources |
| `mariadb_server_fs_reads_total`                           | Server resources |
| `mariadb_server_fs_writes_bytes_total`                    | Server resources |
| `mariadb_server_fs_writes_total`                          | Server resources |
| `mariadb_server_memory_cache`                             | Server resources |
| `mariadb_server_memory_rss`                               | Server resources |
| `mariadb_server_network_receive_bytes_total`              | Server resources |
| `mariadb_server_network_receive_errors_total`             | Server resources |
| `mariadb_server_network_receive_packets_dropped_total`    | Server resources |
| `mariadb_server_network_transmit_bytes_total`             | Server resources |
| `mariadb_server_network_transmit_errors_total`            | Server resources |
| `mariadb_server_network_transmit_packets_dropped_total`   | Server resources |
| `mariadb_server_resident_memory_bytes`                    | Server resources |
| `mariadb_server_spec_cpu_period`                          | Server resources |
| `mariadb_server_spec_cpu_quota`                           | Server resources |
| `mariadb_server_spec_memory_limit_bytes`                  | Server resources |
| `mariadb_server_virtual_memory_bytes`                     | Server resources |
| `mariadb_server_volume_stats_available_bytes`             | Server resources |
| `mariadb_server_volume_stats_capacity_bytes`              | Server resources |
| `mariadb_server_volume_stats_used_bytes`                  | Server resources |
| `mariadb_service_server_network_status`                   | Service status   |
| `mariadb_service_server_role`                             | Service status   |
| `mariadb_service_server_status`                           | Service status   |
| `mariadb_service_status`                                  | Service status   |
| `maxscale_modules`                                        | MaxScale         |
| `maxscale_server_active_operations`                       | MaxScale         |
| `maxscale_server_adaptive_avg_select_time`                | MaxScale         |
| `maxscale_server_connection_pool_empty`                   | MaxScale         |
| `maxscale_server_connections`                             | MaxScale         |
| `maxscale_server_max_connections`                         | MaxScale         |
| `maxscale_server_max_pool_size`                           | MaxScale         |
| `maxscale_server_persistent_connections`                  | MaxScale         |
| `maxscale_server_reused_connections`                      | MaxScale         |
| `maxscale_server_routed_packets`                          | MaxScale         |
| `maxscale_server_total_connections`                       | MaxScale         |
| `maxscale_service_connections`                            | MaxScale         |
| `maxscale_threads_count`                                  | MaxScale         |
| `maxscale_threads_current_descriptors`                    | MaxScale         |
| `maxscale_threads_errors`                                 | MaxScale         |
| `maxscale_threads_event_queue_length`                     | MaxScale         |
| `maxscale_threads_hangups`                                | MaxScale         |
| `maxscale_threads_max_queue_time`                         | MaxScale         |
| `maxscale_threads_reads`                                  | MaxScale         |
| `maxscale_threads_stack_size`                             | MaxScale         |
| `maxscale_threads_total_descriptors`                      | MaxScale         |
| `maxscale_threads_writes`                                 | MaxScale         |
| `maxscale_up`                                             | MaxScale         |
| `maxscale_uptime_seconds`                                 | MaxScale         |
| `mariadb_xpand_activity_core0`                            | Xpand            |
| `mariadb_xpand_activity_til`                              | Xpand            |
| `mariadb_xpand_capacity_disk_system_avail_bytes`          | Xpand            |
| `mariadb_xpand_capacity_disk_system_max_bytes`            | Xpand            |
| `mariadb_xpand_capacity_disk_system_usage_ratio`          | Xpand            |
| `mariadb_xpand_capacity_disk_total_usage_percent`         | Xpand            |
| `mariadb_xpand_cluster_nodes_in_quorum`                   | Xpand            |
| `mariadb_xpand_cluster_total_nodes`                       | Xpand            |
| `mariadb_xpand_cluster_uptime_seconds`                    | Xpand            |
| `mariadb_xpand_containers_rows`                           | Xpand            |
| `mariadb_xpand_cpu_load`                                  | Xpand            |
| `mariadb_xpand_io_disk_latency_seconds`                   | Xpand            |
| `mariadb_xpand_io_network_bytes`                          | Xpand            |
| `mariadb_xpand_io_network_latency_seconds`                | Xpand            |
| `mariadb_xpand_memory_bm_bytes`                           | Xpand            |
| `mariadb_xpand_memory_reserved_bytes`                     | Xpand            |
| `mariadb_xpand_memory_total_bytes`                        | Xpand            |
| `mariadb_xpand_memory_working_bytes`                      | Xpand            |
| `mariadb_xpand_qps`                                       | Xpand            |
| `mariadb_xpand_rebalancer_jobs_queued`                    | Xpand            |
| `mariadb_xpand_rebalancer_rebalancer_rebalance`           | Xpand            |
| `mariadb_xpand_rebalancer_rebalancer_reprotects`          | Xpand            |
| `mariadb_xpand_rebalancer_rebalancer_reranks`             | Xpand            |
| `mariadb_xpand_rebalancer_rebalancer_softfail_reprotects` | Xpand            |
| `mariadb_xpand_rebalancer_rebalancer_splits`              | Xpand            |
| `mariadb_xpand_rebalancer_underprotected_slices`          | Xpand            |
| `mariadb_xpand_response_time_seconds`                     | Xpand            |
| `mariadb_xpand_sessions`                                  | Xpand            |
| `mariadb_xpand_sessions_time_in_state`                    | Xpand            |
| `mariadb_xpand_sessions_trx_age`                          | Xpand            |
| `mariadb_xpand_stats_Com_alter_cluster`                   | Xpand            |
| `mariadb_xpand_stats_Com_delete`                          | Xpand            |
| `mariadb_xpand_stats_Com_delete_seconds`                  | Xpand            |
| `mariadb_xpand_stats_Com_insert`                          | Xpand            |
| `mariadb_xpand_stats_Com_insert_seconds`                  | Xpand            |
| `mariadb_xpand_stats_Com_select`                          | Xpand            |
| `mariadb_xpand_stats_Com_select_seconds`                  | Xpand            |
| `mariadb_xpand_stats_Com_set_option`                      | Xpand            |
| `mariadb_xpand_stats_Com_show_slave_status`               | Xpand            |
| `mariadb_xpand_stats_Com_show_status`                     | Xpand            |
| `mariadb_xpand_stats_Com_show_variables`                  | Xpand            |
| `mariadb_xpand_stats_Com_update`                          | Xpand            |
| `mariadb_xpand_stats_Com_update_seconds`                  | Xpand            |
| `mariadb_xpand_stats_connections`                         | Xpand            |
| `mariadb_xpand_tps`                                       | Xpand            |
| `mariadb_xpand_wals_avg_sync_time_seconds`                | Xpand            |
| `gridgain_cache_queryresultcache_cacheevictions`          | GridGain         |
| `gridgain_cache_queryresultcache_cachegets`               | GridGain         |
| `gridgain_cache_queryresultcache_cachehits`               | GridGain         |
| `gridgain_cache_queryresultcache_cachesize`               | GridGain         |
| `gridgain_cluster_totalservernodes`                       | GridGain         |
| `gridgain_io_dataregion_default_maxsize`                  | GridGain         |
| `gridgain_io_dataregion_default_totalallocatedsize`       | GridGain         |

<sub>_This page is: Copyright © 2026 MariaDB. All rights reserved._</sub>
