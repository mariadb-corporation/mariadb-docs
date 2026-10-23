---
description: >-
  An overview of the new features, changed defaults, and removed settings in
  MariaDB MaxScale 26.10
---

# What's New in MariaDB MaxScale 26.10

This page describes the features that are new in MaxScale 26.10 compared to MaxScale 25.10. For per-release details, see the [MaxScale release notes](../README.md).

## Upgrade Notes

Review these changes before upgrading. They can change behavior without any configuration change.

* The default of `ssl` for servers and listeners is now `allow` (it was off). See [TLS and security](#tls-and-security).
* Log timestamps are now ISO 8601 with a UTC offset. Set `log_timestamp_format=datetime` to keep the old format.
* The default of `max_auth_errors_until_block` changed from 10 to 0, and the default of `max_connect_errors` changed from 0 to 100.
* `telemetry_url` is now a base URL (default `http://localhost:4318`) and cannot be empty. It was `http://localhost:4318/v1/metrics`.
* The avrorouter, the CDC protocol and `storage_memcached` are removed.
* Several Exasol router and binlogrouter settings were renamed without a compatibility alias. See [Renamed and removed settings](#renamed-and-removed-settings).

## Monitors and Switchover

### Replication SSL in MariaDB Monitor and Galera Monitor (MXS-3577)

`replication_master_ssl` is no longer a plain boolean. It accepts `auto`, `on` and `off` (booleans are still accepted) and defaults to `auto`. The setting exists in both [MariaDB Monitor](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/mariadb-monitor) and [Galera Monitor](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-monitors/galera-monitor) and can be changed at runtime.

With `auto`, redirecting an existing replication connection leaves `MASTER_SSL` unset, so the server keeps its value. When a connection is created or moved, the monitor uses the `Master_SSL_Allowed` value it saw on the previous connection. If nothing is known, it chooses from the SSL policy of the target server: `require` gives on, `disable` gives off. `on` and `off` always write `MASTER_SSL=1` or `0`. `MASTER_SSL_VERIFY_SERVER_CERT` is carried over when a connection is created and its previous value is known.

### External Replication Management (MXS-4819, MXS-6233)

Both monitors can keep the primary of their cluster replicating from a server in another cluster. Set `external_replication_monitor` to the name of the other monitor. The server that monitor selects is chosen by `external_replication_primary_role`, an ordered list of `primary`, `replica` and `running` (default `primary`). Both settings can be changed at runtime.

The monitor acts only when the other monitor is running and has completed a new tick, and when its own cluster has a primary. As the external primary changes, the monitor creates or redirects the replication connection. A stopped connection is restarted only when the external primary has changed. When no valid external primary exists, the monitor removes the connection and remembers its settings for later reuse. MariaDB Monitor requires `assume_unique_hostnames=true`.

Galera Monitor also removes replication connections from Joined non-primary nodes, reads `SHOW ALL SLAVES STATUS` and sets a transaction lag value on servers. Its new `replication_user` and `replication_password` settings must be set together. Nothing is done while MaxScale is passive.

### Smoother Switchovers With readwritesplit (MXS-5555)

At the start of a switchover, MariaDB Monitor marks the old primary as demoting. [readwritesplit](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-readwritesplit) then refuses new connections to it and lets transactions that are already open finish. The monitor waits until the open transaction count of the old primary reaches zero, or until one third of the time left in `switchover_timeout` has passed, and then continues the demotion. `switchover_wait_for_trx` controls this behavior (default `true`, dynamic). The wait applies to any demotion that uses the shared demote step, not only to switchover.

### Healing a Truncated Primary (MXS-6765)

With `heal_primary_truncated_binlog=true` (default `false`, dynamic), MariaDB Monitor detects a primary whose binary log lost transactions: a replica has a `Gtid_IO_Pos` ahead of the primary `gtid_binlog_pos` in the cluster domain. Detection starts after a monitor reconnect or when `read_only` suddenly turns on, and the monitor waits at least one tick before acting. Replicas need `log_slave_updates` and a valid `gtid_binlog_pos`.

The monitor withholds the Master status from the primary and makes it replicate from the most advanced replica, with the replication settings copied from that replica. When the primary reaches the replica GTID, the connection is removed. Failures delay automatic cluster operations, and nothing is done if the primary is in maintenance.

### Write Throttling (MXS-6572, MXS-7561)

A server can be put into a throttling state through the REST API (`state=throttle`). This is also allowed on the primary. No monitor sets the state automatically.

When readwritesplit commits a transaction on a throttled primary, it synchronizes the commit with a timeout that grows linearly by `sync_transaction_throttle_rate` for every minute of continuous throttling, capped by `sync_transaction_timeout`. The reply is released early if a replica acknowledges the GTID first. Throttling applies whenever `sync_transaction` is not `hard`. With `sync_transaction=none` (the default), a throttled primary behaves as if `sync_transaction=soft`: synchronization is turned on after a commit if no results are pending and there is more than one backend, and turned off again after throttling ends. No lag probes are done in this automatic mode, and GTID tracking stays on once enabled.

Service diagnostics show `sync_transaction_throttle_duration` and `sync_transaction_throttle_amount`, and servers report `transaction_lag`.

| Setting | Description | Default |
|---------|-------------|---------|
| `sync_transaction_throttle_rate` | Delay added per minute of throttling. Minimum 1ms. Dynamic. | `5ms` |
| `sync_transaction_percent` | Percentage (0 to 100) of committed transactions that are synchronized, counted deterministically. Dynamic. | `100` |
| `sync_transaction_probe` | Probe replication lag by synchronizing at least one transaction when `sync_transaction_percent` is below 100. Dynamic. | `true` |

### Forced Maintenance and Drain (MXS-6513, MXS-6514)

The `force` option of `set server` ([server resource](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api/maxscale-server-resource)) (`maxctrl --force`, REST `force=yes`) overrides the monitor's refusal to put a primary (MariaDB Monitor), or a master that is being drained (Galera Monitor), into maintenance or drain. Forced maintenance still closes all connections to the server. Forced drain only skips the check.

When a server is set to drain, sessions release idle backend connections to it. readwritesplit closes connections to a draining server once no response is pending and no transaction is active, instead of waiting for the client to disconnect. Replica selection treats a draining server as unsuitable.

### Cooperative Monitoring (MXS-6921, MXS-6239, MXS-6102)

* `cooperative_monitoring_arbitrator_nodes` (MariaDB Monitor, dynamic) lists servers that take part in cooperative monitoring locks only as tie-breakers. These servers never get the Master or Slave status and are left out of switchover, failover, rejoin and replica redirection. A server cannot also be listed in `servers_no_cooperative_monitoring_locks`.
* When `cooperative_monitoring_locks` is enabled and MaxScale is passive, the monitor no longer takes server locks and releases the ones it holds. A passive MaxScale cannot become the lock majority.
* If the monitor connection to a server times out but a routing session has read data from that server within the monitor timeout, the server stays `Running` and a rate-limited notice is logged. The status information shows the reason `Monitor timed out`.

### Preserved Replication Settings (MXS-6268)

MariaDB Monitor now reads `Master_SSL_Verify_Server_Cert`, `Replicate_Ignore_Server_Ids`, `Replicate_Do_Domain_Ids`, `Replicate_Ignore_Domain_Ids` and `SQL_Delay` from `SHOW ALL SLAVES STATUS`. It keeps them when it moves, redirects or rejoins replication connections.

### Deprecated Unique Hostname Assumption (MXS-6538)

`assume_unique_hostnames` is deprecated. A warning is logged whenever the setting is present in the configuration, advising you to define `private_address` on the servers. It must be `true` when `external_replication_monitor` is used.

## TLS and Security

### Encrypted and Unencrypted Connections (MXS-5594, MXS-6383)

The `ssl` setting of listeners and servers (see the [configuration guide](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide)) is now an enum: `disable`, `allow` and `require`. The default is `allow`. The values `true` (`require`) and `false` (`disable`) are still accepted. The setting can be changed at runtime.

* On a listener, `allow` accepts both TLS and plain text clients. `require` forces TLS for every client. With `require_secure_transport=true`, a TCP listener must use `ssl=require`.
* On a server, `allow` uses TLS when the backend supports it and falls back to an unencrypted connection when it does not. `require` fails the connection if the server has no TLS. With `require_secure_transport=true`, servers defined by address are forced to `ssl=require`.

### TLS Certificate Selection and Routing by SNI (MXS-5976, MXS-6010, MXS-5990)

A listener can point `sni_mapping_file` (dynamic, default empty) at a JSON file that maps TLS server names to certificates and services. The file has a `certificates` object that maps a name to an `ssl_cert` and `ssl_key` pair, and a `hostname_to_service_mapping` array of entries with `hostnames`, `certificate` and `service`.

When a client sends a server name that exactly matches a mapped host name (wildcards are not supported), MaxScale presents the mapped certificate and routes the session to the mapped service instead of the listener's default service. Clients that send an unknown name get the listener certificate. A file with invalid or duplicate host names, or with certificates or services that do not exist, is rejected. Only the MariaDB client protocol uses SNI mapping.

When MaxScale opens a TLS connection to a backend server, it sends the configured address of the server as the TLS server name. No setting controls this.

## Logging and Telemetry

### Connection and Disconnection Logging (MXS-5975)

Client connects and disconnects are logged as the `session_start` and `session_stop` events, each on one line with the service, session id, user, client address, listener and worker. The log level (default `LOG_INFO`) and syslog facility (default `LOG_USER`) of each event are set with `event_session_start_level`, `event_session_start_facility`, `event_session_stop_level` and `event_session_stop_facility`. All four can be changed at runtime.

### Time Zone in Log Timestamps (MXS-6550)

[`log_timestamp_format`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide) accepts `default`, `iso_8601` and `datetime` (default `default`, dynamic). `default` now means ISO 8601 with the local UTC offset, for example `2026-10-13T12:00:00+03:00`. `datetime` restores the old `YYYY-MM-DD HH:MM:SS` format. After an upgrade, MaxScale warns at startup if the first lines of the existing `maxscale.log` still have the old format, unless the format is set explicitly. `ms_timestamp` still adds milliseconds.

### Exporting Logs Through OpenTelemetry (MXS-6294)

With [`telemetry`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-telemetry) enabled and `telemetry_signals` including `logs`, every log message that passes the log level filter is also sent as an OTLP/HTTP log record. The record carries the severity mapped from the syslog priority and, when present, the session, module and scope as attributes.

| Setting | Description | Default |
|---------|-------------|---------|
| `telemetry_signals` | `metrics`, `logs` or both. Dynamic. | `metrics,logs` |
| `telemetry_logs_url` | Logs endpoint. When empty, `telemetry_url` followed by `/v1/logs`. Dynamic. | empty |
| `telemetry_metrics_url` | Metrics endpoint. When empty, `telemetry_url` followed by `/v1/metrics`. Dynamic. | empty |
| `telemetry_sql_count` | Number of SQL statements to export. Dynamic. | `50` |
| `telemetry_sql_match` | Export only statements matching this regular expression. Dynamic. | empty |
| `telemetry_sql_exclude` | Do not export statements matching this regular expression. Dynamic. | empty |

## Query Statistics and Metrics

### Query Statistics (MXS-5768, MXS-6237)

For every canonical SQL statement and backend server, MaxScale tracks a latency distribution with approximate quantiles (2 percent error, 1 ms to 24 hours). The [REST endpoint](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api/maxscale-maxscale-resource) `/maxscale/query_classifier/cache` returns the count, total duration and average duration. It also returns `duration_moving` (the last five minutes) and `duration_cumulative` (the whole run), each with the count, sum, mean and the 25th, 50th, 75th, 90th, 95th and 99th percentiles, with a per-target breakdown. The data is also exported as the telemetry metric `maxscale.query.latency`. [`maxctrl show query_statistics`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-maxctrl) displays it. Set `statistics=false` (default `true`, dynamic) to turn the tracking off.

The endpoint accepts `sort=hits|duration|last_used` (default `hits`), `top=N` (default 20) and `match=REGEX`, which filters on the canonical statement. An invalid `sort` value or regular expression returns HTTP 400. The maxctrl commands expose only `--top`.

### Memory and Transaction Metrics (MXS-6202, MXS-6512)

* The `memory` object of a session in the REST API has a `modules` object with the memory used by the router session and by each filter session, with a total per service.
* Servers and services count active and completed transactions: `active_transactions` and `total_transactions` in the REST statistics, and the telemetry metrics `maxscale.server.transactions` and `maxscale.service.transactions`.

### Worker Assignment (MXS-6153)

[`worker_assignment=local`](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/maxscale-management/deployment/installation-and-configuration/maxscale-configuration-guide) (default) keeps a new client connection on the worker thread that accepted it. `roundrobin` gives each accepted connection to the next worker in turn. The setting can be changed at runtime.

## Exasol and GridGain

### GridGain Router (MXS-6226)

The new `gridgainrouter` module presents a GridGain cluster to MariaDB clients. Clients connect with a normal MariaDB client, and the router runs the SQL over ODBC using `odbc_connection_string`. The client must name a default schema at connect time, and switching schemas is not supported. A running query is stopped by labeling each statement with a comment, finding it in `SYS.SQL_QUERIES` and issuing `KILL QUERY`. The router is in the `maxscale` package.

| Setting | Description | Default |
|---------|-------------|---------|
| `appearance` | `read_only` or `read_write`. Not dynamic. | `read_only` |
| `kill_connection_timeout` | How long to wait for the connection used to kill a query. Not dynamic. | `10s` |

### Exasol and GridGain Router Settings (MXS-7630, MXS-6025, MXS-6623)

The [Exasol router](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-exasolrouter), GridGain router and the Exasol CDC in [binlogrouter](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-binlogrouter) now share setting names, and the routers share one ODBC implementation. In the routers, the values of `UID`, `USER`, `USERNAME`, `PWD`, `PASSWORD` and `PASSWD` in `odbc_connection_string` are masked in output and logs.

| Setting | Description | Default |
|---------|-------------|---------|
| `odbc_connection_string` | ODBC connection string. Not dynamic. | |
| `odbc_login_timeout` | Login timeout. Dynamic; changes affect new sessions. | `30s` |
| `odbc_query_timeout` | Query timeout. Dynamic; changes affect new sessions. | `30s` |
| `impersonate` | Exasol router only. Runs `IMPERSONATE "USER"` after connecting, so each client acts as its own Exasol user. Not dynamic. | `false` |
| `gtid_polling` | Poll the GTID position that Exasol CDC writes into Exasol. Used by SmartRouter causal reads. No effect for GridGain. Dynamic. | `true` |
| `gtid_poll_interval` | How often the GTID position is polled. Minimum 100ms. No effect for GridGain. Dynamic. | `1s` |

With `impersonate`, MaxScale sends the MariaDB user name unchanged, quoted. Session setup SQL runs before `IMPERSONATE`, so the impersonated user must be allowed to run it. `COM_CHANGE_USER` closes such a session.

### Correct Column Types (MXS-7570)

Result set column definitions from the ODBC routers now declare the real type of each column. Before, every column was `VARCHAR(255)` in the binary character set. The Exasol router adds `ANSIDATAENCODING=UTF-8` to `odbc_connection_string` if it is missing.

### Exasol CDC in binlogrouter (MXS-6264, MXS-6612, MXS-6772, MXS-6781, MXS-6881, MXS-6924, MXS-6821)

**Module commands.** `cdc-start`, `cdc-stop`, `cdc-stats`, `cdc-reset-stats` and `cdc-copy-users` control and inspect Exasol CDC.

* `cdc-stop` suspends CDC. The stopped or running state is saved in `cdc-state.json` in the binlog directory and survives a restart. `cdc-start` fails if CDC is already running or if `odbc_connection_string` is empty.
* The service diagnostics gain a `CDC` object with the state (`stopped`, `copying`, `connecting` or `replicating`), the GTIDs and the statistics.

**Initial data migration.** `cdc-start SERVICE bulk-copy=FILE` bulk-copies existing MariaDB schemas and tables into Exasol before replication starts. `bulk-copy` cannot be combined with `gtid=`. The file is JSON with the source connection (`host`, `user`, `password`, `port`) and a list of schemas, each given by name or as a schema with a list of tables. The copy refuses to run if the source has running replication threads, warns if the source is not read-only, fails if the source GTID moves during the copy or if the binary logs do not reach back to the source position, and does not start replication after an incomplete copy.

**Synchronizing users.** With `odbc_manage_user_grants=true`, `CREATE USER`, `DROP USER`, `ALTER USER`, `GRANT` and `REVOKE` statements (including role grants) in the binary log are translated to Exasol. Passwords are redacted in logs. Enabling the setting forces `odbc_create_table_from_sql=true`.

`cdc-copy-users SERVICE host=HOST [port=3306]` copies the users, roles and grants of a MariaDB server into Exasol in its own thread. It creates the roles first, then the users with random passwords, skips names that already exist, and then applies the translated grants. The state is shown in the CDC diagnostics.

**Insert-only tables.** `odbc_insert_only_tables` lists tables (`schema.table` or `schema.*`) for which `DELETE` row events are dropped, so deleted rows stay in Exasol. `UPDATE` and `INSERT` events still apply. `TRUNCATE`, `DROP TABLE` and `DROP COLUMN` are blocked for these tables, and `DROP SCHEMA` is skipped when the schema holds an insert-only table. A listed table is replicated even if `odbc_include_tables` does not list it. `odbc_include_tables` now requires `schema.table` or `schema.*` entries.

**Buffering and statistics.** The buffering of CDC is limited by time as well as by size. `odbc_perf_max_buffer_time` and `odbc_perf_max_buffer_time_in_idle` set the time limits, `odbc_perf_batch_size` sets the size of a load in bytes (default 200 MiB), and `odbc_perf_max_buffered_rows` remains a row-count trigger (default 750000). `cdc-stats` and the CDC diagnostics report cycles, rows, rows per cycle, rows in the last 60 seconds, replication lag, average CDC lag, cycle time, commit times and, per table, the rows, inserts, updates, deletes, loads, bytes and the durations of the pipeline stages. `cdc-reset-stats` clears them.

| Setting | Description | Default |
|---------|-------------|---------|
| `odbc_connection_string` | ODBC connection string of the Exasol target. Not dynamic. | |
| `odbc_case` | `keep`, `sensitive` or `insensitive`. Not dynamic. | `keep` |
| `odbc_insert_only_tables` | See above. Not dynamic. | |
| `odbc_manage_user_grants` | See above. Not dynamic. | `false` |
| `odbc_perf_max_buffer_time` | Maximum time spent buffering rows before a cycle starts. Not dynamic. | `2s` |
| `odbc_perf_max_buffer_time_in_idle` | Maximum buffering time when the pipeline is idle. Not dynamic. | `500ms` |

The default of `odbc_create_table_from_sql` changed from `true` to `false`. The minimum of `odbc_perf_ncycles` changed from 0 to 1.

### SmartRouter (MXS-6764, MXS-6262, MXS-6593)

| Setting | Description | Default |
|---------|-------------|---------|
| `eviction_schedule` | Comma-separated ascending durations. A cached routing decision is measured again after each step, and the last value repeats. Dynamic. | `2m,5m,10m,20m` |
| `causal_reads` | `none` or `local`. With `local`, a query sent to another target waits until that target has caught up with the last write of the session. Dynamic. | `none` |
| `causal_reads_timeout` | How long to wait for the target to catch up. Dynamic. | `10s` |
| `causal_reads_on_timeout` | `master` routes the query to the master, `stale` sends it anyway, `error` returns an error. Dynamic. | `master` |

With `causal_reads=local`, SmartRouter tracks the GTID of the last write the session made on the master. The position of an Exasol target is polled by the Exasol router from the table `maxscale_cdc.gtid_current_pos` every `gtid_poll_interval`, and SmartRouter rechecks the cached position every 20 ms while a query waits. GridGain has no GTID source, so causal reads cannot be satisfied for it.

For `COM_QUERY` statements that are not writes and are not inside a transaction, [SmartRouter](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-routers/maxscale-smartrouter) honors routing hints. `route to master` sends the query to the first cluster, and `route to server NAME` sends it to the target of that name. The measurement step is skipped, and other hint types are ignored.

## Filters, GUI and Platform

### Kafka Support in the Query Log Filter (MXS-5999)

The `log_type` setting of [qlafilter](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-filters/maxscale-query-log-all-filter) accepts the new value `kafka`, which can be combined with `session`, `unified` and `stdout`. Each logged query entry (the same text as in the unified log) is produced to `kafka_topic` on the servers in `kafka_bootstrap_servers`. The message key is the session id and the timestamp is the time the query was received. Producer errors are logged and do not affect the query. The shared `kafka_ssl*` and `kafka_sasl*` settings apply.

| Setting | Description | Default |
|---------|-------------|---------|
| `kafka_bootstrap_servers` | Kafka servers. Mandatory when `log_type` includes `kafka`. Dynamic. | |
| `kafka_topic` | Kafka topic. Mandatory when `log_type` includes `kafka`. Dynamic. | |
| `kafka_enable_idempotence` | Enable the idempotent producer. Dynamic. | `false` |
| `logged_query_max_length` | Maximum length of a logged query, `0` means unlimited. Dynamic. | `1024` |

### MaxGUI (MXS-5375, MXS-5609, MXS-5335)

* The listener page has Start and Stop actions next to Destroy. They ask for confirmation and call the listener start and stop REST endpoints.
* In parameter lists, mandatory parameters and address, port and socket are listed first by default, and the order can still be changed. The toggle is now called Show required only and shows only the mandatory parameters. The choice is stored per user.
* The new Report page, reached from the help menu, collects the REST resources `maxscale`, `servers`, `services`, `monitors`, `listeners`, `filters`, `sessions`, `users`, `modules`, `query_classifier`, `threads`, `logs` and server diagnostics into one JSON document. A setting controls how many log lines are included (default 1000). The page has a filter to leave out sections and a find bar with match case, whole word, regular expression and find in selection options. Export downloads `maxscale-report.json`.

### Automatic Download of the MariaDB ODBC Driver (MXS-6000)

The admin-only [REST endpoint](https://app.gitbook.com/o/diTpXxF5WsbHqTReoBsS/s/0pSbu5DcMSW4KwAkUcmX/reference/maxscale-rest-api/maxscale-sql-resource) `POST /v1/sql/odbc/drivers/install` downloads the MariaDB ODBC driver into the `drivers` directory under the data directory. The JSON body has `type` (`mariadb`), an optional `version` (default latest, minimum 3.2.9) and optional `arch`, `os_type` and `os_version`, which are detected from the system when omitted. Only one installation can run at a time, and installing a version that is already installed is an error. `GET /v1/sql/odbc/drivers` lists the downloaded drivers. At startup, if drivers have been downloaded, MaxScale checks for a newer version and logs a notice.

### Packaging (MXS-7571, MXS-6090, MXS-7574)

* There is no separate `maxscale-exasol` package. The Exasol router, the GridGain router, their Python preprocessing files and the Exasol ODBC driver (a tarball unpacked by the post-install script, x86_64 only) are in the `maxscale` package, which replaces `maxscale-exasol` (DEB `Conflicts` and `Replaces`, RPM `Obsoletes` older than 26.10). Removing the package removes the driver directory.
* For builds that are not Debug builds, DEB and RPM packages come with separate debug symbol packages. RPM debuginfo packages contain only `/usr/lib/debug`.
* The C++ implementation of maxctrl is now the `maxctrl` command in the package `maxscale-maxctrl` and needs no Node.js. The Node.js version is now the package `maxscale-maxctrl-legacy`. The `maxscale` package recommends `maxscale-maxctrl`. `maxctrl show query_statistics` exists only in the C++ version.

### License Key and Feedback (MXS-6230)

This applies to licensed builds only (built with `MAXSCALE_LICENSE`, which is on by default in the build system). `license_key` is mandatory and is a JWT, either the token or an absolute path to a file that contains it. MaxScale verifies the signature locally against a key set embedded at build time. Expiry messages follow a schedule that starts 180 days before the end of the contract, and MaxScale shuts down when the license lifetime ends.

With `enable_feedback=true` (default, not dynamic), MaxScale sends a JSON document with the license id and system information (CPU cores, memory, operating system, thread count, query classifier cache size, backend server versions and module types in use) 30 seconds after startup. The document is saved as `feedback.json` in the data directory. It is skipped if the content is unchanged or `feedback.json` was written within the last 24 hours.

## Renamed and Removed Settings

| Change | Details |
|--------|---------|
| Renamed | Exasol router: `connection_string`, `login_timeout` and `query_timeout` are now `odbc_connection_string`, `odbc_login_timeout` and `odbc_query_timeout`. binlogrouter: `odbc_connection_str` is now `odbc_connection_string`. There is no compatibility alias. |
| Removed | binlogrouter (Exasol CDC): `odbc_perf_max_idle_rows`. |
| Removed with the avrorouter and CDC protocol (MXS-7582) | The avrorouter module, the CDC listener protocol, the `BUILD_CDC` build option and the Avro library build. The avrorouter settings `binlogdir`, `avrodir`, `filestem`, `group_rows`, `group_trx`, `start_index`, `block_size`, `codec`, `match`, `exclude`, `server_id`, `gtid_start_pos`, `cooperative_replication`, `max_file_size` and `max_data_age` no longer exist for it. The module commands `convert`, `purge` and `rotate` are gone. A configuration with `router=avrorouter` or `protocol=CDC` no longer loads. `match`, `exclude`, `server_id` and `cooperative_replication` remain settings of kafkacdc, and `server_id` remains a setting of binlogrouter. |
| Removed (MXS-7620) | The cache filter module `storage_memcached`. The remaining storages are `storage_inmemory`, `storage_redis` and `storage_gridgain`. |
