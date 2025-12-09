---
description: 'Step 8: Test MariaDB MaxScale'
---

# Step 8: Test MariaDB MaxScale

## Overview

This page details step 8 of the 9-step procedure "Deploy ColumnStore Object Storage Topology".

This step tests MariaDB MaxScale 22.08.

{% include "../../../../../.gitbook/includes/the-instructions-were-teste....md" %}

Interactive commands are detailed. Alternatively, the described operations can be performed using automation.

## Check Global Configuration

Use [maxctrl show maxscale](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-maxscale) command to view the global MaxScale configuration.

This action is performed **on the MaxScale node**:

```bash
$ maxctrl show maxscale
```

```sql
┌──────────────┬───────────────────────────────────────────────────────┐
│ Version      │ 22.08.15                                              │
├──────────────┼───────────────────────────────────────────────────────┤
│ Commit       │ 3761fa7a52046bc58faad8b5a139116f9e33364c              │
├──────────────┼───────────────────────────────────────────────────────┤
│ Started At   │ Thu, 05 Aug 2021 20:21:20 GMT                         │
├──────────────┼───────────────────────────────────────────────────────┤
│ Activated At │ Thu, 05 Aug 2021 20:21:20 GMT                         │
├──────────────┼───────────────────────────────────────────────────────┤
│ Uptime       │ 868                                                   │
├──────────────┼───────────────────────────────────────────────────────┤
│ Config Sync  │ null                                                  │
├──────────────┼───────────────────────────────────────────────────────┤
│ Parameters   │ {                                                     │
│              │     "admin_auth": true,                               │
│              │     "admin_enabled": true,                            │
│              │     "admin_gui": true,                                │
│              │     "admin_host": "0.0.0.0",                          │
│              │     "admin_log_auth_failures": true,                  │
│              │     "admin_pam_readonly_service": null,               │
│              │     "admin_pam_readwrite_service": null,              │
│              │     "admin_port": 8989,                               │
│              │     "admin_secure_gui": false,                        │
│              │     "admin_ssl_ca_cert": null,                        │
│              │     "admin_ssl_cert": null,                           │
│              │     "admin_ssl_key": null,                            │
│              │     "admin_ssl_version": "MAX",                       │
│              │     "auth_connect_timeout": "10000ms",                │
│              │     "auth_read_timeout": "10000ms",                   │
│              │     "auth_write_timeout": "10000ms",                  │
│              │     "cachedir": "/var/cache/maxscale",                │
│              │     "config_sync_cluster": null,                      │
│              │     "config_sync_interval": "5000ms",                 │
│              │     "config_sync_password": "*****",                  │
│              │     "config_sync_timeout": "10000ms",                 │
│              │     "config_sync_user": null,                         │
│              │     "connector_plugindir": "/usr/lib64/mysql/plugin", │
│              │     "datadir": "/var/lib/maxscale",                   │
│              │     "debug": null,                                    │
│              │     "dump_last_statements": "never",                  │
│              │     "execdir": "/usr/bin",                            │
│              │     "language": "/var/lib/maxscale",                  │
│              │     "libdir": "/usr/lib64/maxscale",                  │
│              │     "load_persisted_configs": true,                   │
│              │     "local_address": null,                            │
│              │     "log_debug": false,                               │
│              │     "log_info": false,                                │
│              │     "log_notice": true,                               │
│              │     "log_throttling": {                               │
│              │         "count": 10,                                  │
│              │         "suppress": 10000,                            │
│              │         "window": 1000                                │
│              │     },                                                │
│              │     "log_warn_super_user": false,                     │
│              │     "log_warning": true,                              │
│              │     "logdir": "/var/log/maxscale",                    │
│              │     "max_auth_errors_until_block": 10,                │
│              │     "maxlog": true,                                   │
│              │     "module_configdir": "/etc/maxscale.modules.d",    │
│              │     "ms_timestamp": false,                            │
│              │     "passive": false,                                 │
│              │     "persistdir": "/var/lib/maxscale/maxscale.cnf.d", │
│              │     "piddir": "/var/run/maxscale",                    │
│              │     "query_classifier": "qc_sqlite",                  │
│              │     "query_classifier_args": null,                    │
│              │     "query_classifier_cache_size": 289073971,         │
│              │     "query_retries": 1,                               │
│              │     "query_retry_timeout": "5000ms",                  │
│              │     "rebalance_period": "0ms",                        │
│              │     "rebalance_threshold": 20,                        │
│              │     "rebalance_window": 10,                           │
│              │     "retain_last_statements": 0,                      │
│              │     "session_trace": 0,                               │
│              │     "skip_permission_checks": false,                  │
│              │     "sql_mode": "default",                            │
│              │     "syslog": true,                                   │
│              │     "threads": 1,                                     │
│              │     "users_refresh_interval": "0ms",                  │
│              │     "users_refresh_time": "30000ms",                  │
│              │     "writeq_high_water": 16777216,                    │
│              │     "writeq_low_water": 8192                          │
│              │ }                                                     │
└──────────────┴───────────────────────────────────────────────────────┘
```

Output should align to the global MaxScale configuration in the new configuration file you created.

Check Server Configuration\
Use the [maxctrl list servers](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-servers) and [maxctrl show server](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-server) commands to view the configured server objects.

This action is performed **on the MaxScale node**:

1. Obtain the full list of servers objects:

```bash
$ maxctrl list servers
```

```sql
┌────────┬────────────────┬──────┬─────────────┬─────────────────┬────────┐
│ Server │ Address        │ Port │ Connections │ State           │ GTID   │
├────────┼────────────────┼──────┼─────────────┼─────────────────┼────────┤
│ mcs1   │ 192.0.2.1      │ 3306 │ 1           │ Master, Running │ 0-1-25 │
├────────┼────────────────┼──────┼─────────────┼─────────────────┼────────┤
│ mcs2   │ 192.0.2.2      │ 3306 │ 1           │ Slave, Running  │ 0-1-25 │
├────────┼────────────────┼──────┼─────────────┼─────────────────┼────────┤
│ mcs3   │ 192.0.2.3      │ 3306 │ 1           │ Slave, Running  │ 0-1-25 │
└────────┴────────────────┴──────┴─────────────┴─────────────────┴────────┘
```

For each server object, view the configuration:

```bash
$ maxctrl show server mcs1
```

```sql
┌─────────────────────┬───────────────────────────────────────────┐
│ Server              │ mcs1                                      │
├─────────────────────┼───────────────────────────────────────────┤
│ Address             │ 192.0.2.1                                 │
├─────────────────────┼───────────────────────────────────────────┤
│ Port                │ 3306                                      │
├─────────────────────┼───────────────────────────────────────────┤
│ State               │ Master, Running                           │
├─────────────────────┼───────────────────────────────────────────┤
│ Version             │ 11.4.5-3-MariaDB-enterprise-log           │
├─────────────────────┼───────────────────────────────────────────┤
│ Last Event          │ master_up                                 │
├─────────────────────┼───────────────────────────────────────────┤
│ Triggered At        │ Thu, 05 Aug 2021 20:22:26 GMT             │
├─────────────────────┼───────────────────────────────────────────┤
│ Services            │ connection_router_service                 │
│                     │ query_router_service                      │
├─────────────────────┼───────────────────────────────────────────┤
│ Monitors            │ columnstore_monitor                       │
├─────────────────────┼───────────────────────────────────────────┤
│ Master ID           │ -1                                        │
├─────────────────────┼───────────────────────────────────────────┤
│ Node ID             │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Slave Server IDs    │                                           │
├─────────────────────┼───────────────────────────────────────────┤
│ Current Connections │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Total Connections   │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Max Connections     │ 1                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Statistics          │ {                                         │
│                     │     "active_operations": 0,               │
│                     │     "adaptive_avg_select_time": "0ns",    │
│                     │     "connection_pool_empty": 0,           │
│                     │     "connections": 1,                     │
│                     │     "max_connections": 1,                 │
│                     │     "max_pool_size": 0,                   │
│                     │     "persistent_connections": 0,          │
│                     │     "reused_connections": 0,              │
│                     │     "routed_packets": 0,                  │
│                     │     "total_connections": 1                │
│                     │ }                                         │
├─────────────────────┼───────────────────────────────────────────┤
│ Parameters          │ {                                         │
│                     │     "address": "192.0.2.1",               │
│                     │     "disk_space_threshold": null,         │
│                     │     "extra_port": 0,                      │
│                     │     "monitorpw": null,                    │
│                     │     "monitoruser": null,                  │
│                     │     "persistmaxtime": "0ms",              │
│                     │     "persistpoolmax": 0,                  │
│                     │     "port": 3306,                         │
│                     │     "priority": 0,                        │
│                     │     "proxy_protocol": false,              │
│                     │     "rank": "primary",                    │
│                     │     "socket": null,                       │
│                     │     "ssl": false,                         │
│                     │     "ssl_ca_cert": null,                  │
│                     │     "ssl_cert": null,                     │
│                     │     "ssl_cert_verify_depth": 9,           │
│                     │     "ssl_cipher": null,                   │
│                     │     "ssl_key": null,                      │
│                     │     "ssl_verify_peer_certificate": false, │
│                     │     "ssl_verify_peer_host": false,        │
│                     │     "ssl_version": "MAX"                  │
│                     │ }                                         │
└─────────────────────┴───────────────────────────────────────────┘
```

Output should align to the Server Object configuration you performed.

## Check Monitor Configuration

Use the [maxctrl list monitors](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-monitors) and [maxctrl show monitor](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-monitor) commands to view the configured monitors.

This action is performed on the MaxScale node:

1. Obtain the full list of monitors:

```bash
$ maxctrl list monitors
```

```sql
┌─────────────────────┬─────────┬──────────────────┐
│ Monitor             │ State   │ Servers          │
├─────────────────────┼─────────┼──────────────────┤
│ columnstore_monitor │ Running │ mcs1, mcs2, mcs3 │
└─────────────────────┴─────────┴──────────────────┘
```

2. For each monitor, view the monitor configuration:

```bash
$ maxctrl show monitor columnstore_monitor
```

```sql
┌─────────────────────┬─────────────────────────────────────┐
│ Monitor             │ columnstore_monitor                 │
├─────────────────────┼─────────────────────────────────────┤
│ Module              │ mariadbmon                          │
├─────────────────────┼─────────────────────────────────────┤
│ State               │ Running                             │
├─────────────────────┼─────────────────────────────────────┤
│ Servers             │ mcs1                                │
│                     │ mcs2                                │
│                     │ mcs3                                │
├─────────────────────┼─────────────────────────────────────┤
│ Parameters          │ {                                   │
│                     │     "backend_connect_attempts": 1,  │
│                     │     "backend_connect_timeout": 3,   │
│                     │     "backend_read_timeout": 3,      │
│                     │     "backend_write_timeout": 3,     │
│                     │     "disk_space_check_interval": 0, │
│                     │     "disk_space_threshold": null,   │
│                     │     "events": "all",                │
│                     │     "journal_max_age": 28800,       │
│                     │     "module": "mariadbmon",         │
│                     │     "monitor_interval": 2000,       │
│                     │     "password": "*****",            │
│                     │     "script": null,                 │
│                     │     "script_timeout": 90,           │
│                     │     "user": "mxs"                   │
│                     │ }                                   │
├─────────────────────┼─────────────────────────────────────┤
│ Monitor Diagnostics │ {}                                  │
└─────────────────────┴─────────────────────────────────────┘
```

Output should align to the MariaDB Monitor (mariadbmon) configuration you performed.

## Check Service Configuration

Use the [maxctrl list services](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-services) and [maxctrl show service](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#show-service) commands to view the configured routing services.

This action is performed on the MaxScale node:

1. Obtain the full list of routing services:

```bash
$ maxctrl list services
```

```sql
┌───────────────────────────┬────────────────┬─────────────┬───────────────────┬──────────────────┐
│ Service                   │ Router         │ Connections │ Total Connections │ Servers          │
├───────────────────────────┼────────────────┼─────────────┼───────────────────┼──────────────────┤
│ connection_router_Service │ readconnroute  │ 0           │ 0                 │ mcs1, mcs2, mcs3 │
├───────────────────────────┼────────────────┼─────────────┼───────────────────┼──────────────────┤
│ query_router_service      │ readwritesplit │ 0           │ 0                 │ mcs1, mcs2, mcs3 │
└───────────────────────────┴────────────────┴─────────────┴───────────────────┴──────────────────┘
```

2. For each service, view the service configuration:

```bash
$ maxctrl show service query_router_service
```

```sql
┌─────────────────────┬─────────────────────────────────────────────────────────────┐
│ Service             │ query_router_service                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Router              │ readwritesplit                                              │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ State               │ Started                                                     │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Started At          │ Sat Aug 28 21:41:16 2021                                    │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Current Connections │ 0                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Total Connections   │ 0                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Max Connections     │ 0                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Cluster             │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Servers             │ mcs1                                                        │
│                     │ mcs2                                                        │
│                     │ mcs3                                                        │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Services            │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Filters             │                                                             │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Parameters          │ {                                                           │
│                     │     "auth_all_servers": false,                              │
│                     │     "causal_reads": "false",                                │
│                     │     "causal_reads_timeout": "10000ms",                      │
│                     │     "connection_keepalive": "300000ms",                     │
│                     │     "connection_timeout": "0ms",                            │
│                     │     "delayed_retry": false,                                 │
│                     │     "delayed_retry_timeout": "10000ms",                     │
│                     │     "disable_sescmd_history": false,                        │
│                     │     "enable_root_user": false,                              │
│                     │     "idle_session_pool_time": "-1000ms",                    │
│                     │     "lazy_connect": false,                                  │
│                     │     "localhost_match_wildcard_host": true,                  │
│                     │     "log_auth_warnings": true,                              │
│                     │     "master_accept_reads": false,                           │
│                     │     "master_failure_mode": "fail_instantly",                │
│                     │     "master_reconnection": false,                           │
│                     │     "max_connections": 0,                                   │
│                     │     "max_sescmd_history": 50,                               │
│                     │     "max_slave_connections": 255,                           │
│                     │     "max_slave_replication_lag": "0ms",                     │
│                     │     "net_write_timeout": "0ms",                             │
│                     │     "optimistic_trx": false,                                │
│                     │     "password": "*****",                                    │
│                     │     "prune_sescmd_history": true,                           │
│                     │     "rank": "primary",                                      │
│                     │     "retain_last_statements": -1,                           │
│                     │     "retry_failed_reads": true,                             │
│                     │     "reuse_prepared_statements": false,                     │
│                     │     "router": "readwritesplit",                             │
│                     │     "session_trace": false,                                 │
│                     │     "session_track_trx_state": false,                       │
│                     │     "slave_connections": 255,                               │
│                     │     "slave_selection_criteria": "LEAST_CURRENT_OPERATIONS", │
│                     │     "strict_multi_stmt": false,                             │
│                     │     "strict_sp_calls": false,                               │
│                     │     "strip_db_esc": true,                                   │
│                     │     "transaction_replay": false,                            │
│                     │     "transaction_replay_attempts": 5,                       │
│                     │     "transaction_replay_max_size": 1073741824,              │
│                     │     "transaction_replay_retry_on_deadlock": false,          │
│                     │     "type": "service",                                      │
│                     │     "use_sql_variables_in": "all",                          │
│                     │     "user": "mxs",                                          │
│                     │     "version_string": null                                  │
│                     │ }                                                           │
├─────────────────────┼─────────────────────────────────────────────────────────────┤
│ Router Diagnostics  │ {                                                           │
│                     │     "avg_sescmd_history_length": 0,                         │
│                     │     "max_sescmd_history_length": 0,                         │
│                     │     "queries": 0,                                           │
│                     │     "replayed_transactions": 0,                             │
│                     │     "ro_transactions": 0,                                   │
│                     │     "route_all": 0,                                         │
│                     │     "route_master": 0,                                      │
│                     │     "route_slave": 0,                                       │
│                     │     "rw_transactions": 0,                                   │
│                     │     "server_query_statistics": []                           │
│                     │ }                                                           │
└─────────────────────┴─────────────────────────────────────────────────────────────┘
```

Output should align to the [Read Connection Router (readconnroute)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readconnroute) or [Read/Write Split Router (readwritesplit)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit) configuration you performed.

## Test Application User

Applications should use a dedicated user account. The user account must be created on the primary server.

When users connect to MaxScale, MaxScale authenticates the user connection before routing it to an Enterprise Server node. Enterprise Server authenticates the connection as originating from the IP address of the MaxScale node.

The application users must have one user account with the host IP address of the application server and a second user account with the host IP address of the MaxScale node.

The requirement of a duplicate user account can be avoided by enabling the `proxy_protocol` parameter for MaxScale and the proxy\_protocol\_networks for Enterprise Server.

### Create a User to Connect from MaxScale

This action is performed on the primary Enterprise ColumnStore node:

1. Connect to the primary Enterprise ColumnStore node:

```bash
$ sudo mariadb
```

2. Create the database user account for your MaxScale node:

```sql
CREATE USER 'app_user'@'192.0.2.10' IDENTIFIED BY 'app_user_passwd';
```

Replace 192.0.2.10 with the relevant IP address specification for your MaxScale node.

Passwords should meet your organization's password policies.

3. Grant the privileges required by your application to the database user account for your MaxScale node:

```sql
GRANT ALL ON test.* TO 'app_user'@'192.0.2.10';
```

The privileges shown are designed to allow the tests in the subsequent sections to work. The user account for your production application may require different privileges.

### Create a User to Connect from the Application Server

This action is performed on the primary Enterprise ColumnStore node:

1. Create the database user account for your application server:

```sql
CREATE USER 'app_user'@'192.0.2.11' IDENTIFIED BY 'app_user_passwd';
```

Replace 192.0.2.11 with the relevant IP address specification for your application server.

Passwords should meet your organization's password policies.

2. Grant the privileges required by your application to the d database user account for your application server:

```sql
GRANT ALL ON test.* TO 'app_user'@'192.0.2.11';
```

The privileges shown are designed to allow the tests in the subsequent sections to work. The user account for your production application may require different privileges.

### Test Connection with Application User

To test the connection, use the MariaDB Client from your application server to connect to an Enterprise ColumnStore node through MaxScale.

This action is performed **on a client connected to the MaxScale node**:

```bash
$ mariadb --host 192.0.2.10 --port 3307
      --user app_user --password
```

## Test Connection with Read Connection Router

If you configured the Read Connection Router, confirm that MaxScale routes connections to the replica servers.

On the MaxScale node, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to view the available listeners and ports:

```bash
$ maxctrl list listeners
```

```
┌────────────────────────────┬──────┬──────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host │ State   │ Service                   │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │ ::   │ Running │ connection_router_service │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ query_router_listener      │ 3307 │ ::   │ Running │ query_router_service      │
└────────────────────────────┴──────┴──────┴─────────┴───────────────────────────┘
```

2. Open multiple terminals connected to your application server, in each, use MariaDB Client to connect to the listener port for the Read Connection Router (in the example, 3308):

```bash
$ mariadb --host 192.0.2.10 --port 3308 \
      --user app_user --password
```

Use the application user credentials you created for the `--user and --password` options.

3. In each terminal, query the hostname and server\_id system variable and option to identify to which you're connected:

```sql
SELECT @@global.hostname, @@global.server_id;

+-------------------+--------------------+
| @@global.hostname | @@global.server_id |
+-------------------+--------------------+
|              mcs2 |                  2 |
+-------------------+--------------------+
```

Different terminals should return different values since MaxScale routes the connections to different nodes.

Since the router was configured with the slave router option, the Read Connection Router only routes connections to replica servers.

## Test Write Queries with Read/Write Split Router

If you configured the Read/Write Split Router, confirm that MaxScale routes write queries on this router to the primary Enterprise ColumnStore node.

**on the MaxScale node**, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to view the available listeners and ports:

```bash
$ maxctrl list listeners
```

```sql
┌────────────────────────────┬──────┬──────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host │ State   │ Service                   │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │ ::   │ Running │ connection_router_service │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ query_router_listener      │ 3307 │ ::   │ Running │ query_router_service      │
└────────────────────────────┴──────┴──────┴─────────┴───────────────────────────┘
```

2. Open multiple terminals connected to your application server, in each, use MariaDB Client to connect to the listener port for the Read/Write Split Router (in the example, 3307):

```bash
$ mariadb --host 192.0.2.10 --port 3307 \
      --user app_user --password
```

Use the application user credentials you created for the `--user and --password` options.

3. In one terminal, create the test table:

```sql
CREATE TABLE test.load_balancing_test (
   id INT PRIMARY KEY AUTO_INCREMENT,
   hostname VARCHAR(256),
   server_id INT
);
```

4. In each terminal, issue an insert.md statement to add a row to the example table with the values of the hostname and server\_id system variable and option:

```sql
INSERT INTO test.load_balancing_test (hostname, server_id)
VALUES (@@global.hostname, @@global.server_id);
```

5. In one terminal, issue a SELECT statement to query the results:

```sql
SELECT * FROM test.load_balancing_test;
```

```
+----+----------+-----------+
| id | hostname | server_id |
+----+----------+-----------+
|  1 | mcs1     |         1 |
|  2 | mcs1     |         1 |
|  3 | mcs1     |         1 |
+----+----------+-----------+
```

While MaxScale is handling multiple connections from different terminals, it routed all connections to the current primary Enterprise ColumnStore node, which in the example is `mcs1#.`

## Test Read Queries with Read/Write Split Router

If you configured the [Read/Write Split Router (readwritesplit)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit), confirm that MaxScale routes read queries on this router to replica servers.

1. On the MaxScale node, use the [maxctrl list listeners](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-reference/mariadb-maxscale-2302-maxctrl#list-listeners) command to view the available listeners and ports:

```bash
$ maxctrl list listeners
```

```
┌────────────────────────────┬──────┬──────┬─────────┬───────────────────────────┐
│ Name                       │ Port │ Host │ State   │ Service                   │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ connection_router_listener │ 3308 │ ::   │ Running │ connection_router_service │
├────────────────────────────┼──────┼──────┼─────────┼───────────────────────────┤
│ query_router_listener      │ 3307 │ ::   │ Running │ query_router_service      │
└────────────────────────────┴──────┴──────┴─────────┴───────────────────────────┘
```

2. In a terminal connected to your application server, use MariaDB Client to connect to the listener port for the [Read/Write Split Router (readwritesplit)](https://app.gitbook.com/s/0pSbu5DcMSW4KwAkUcmX/mariadb-maxscale-23-02/mariadb-maxscale-23-02-routers/mariadb-maxscale-2302-readwritesplit) (in the example, 3307):

```bash
$ mariadb --host 192.0.2.10 --port 3307 \
      --user app_user --password
```

Use the application user credentials you created for the --user and --password options.

3. Query the hostname and server\_id to identify which server MaxScale routed you to.

```sql
SELECT @@global.hostname, @@global.server_id;
```

```
+-------------------+--------------------+
| @@global.hostname | @@global.server_id |
+-------------------+--------------------+
|              mcs2 |                  2 |
+-------------------+--------------------+
```

4. Resend the query:

```sql
SELECT @@global.hostname, @@global.server_id;
```

```
+-------------------+--------------------+
| @@global.hostname | @@global.server_id |
+-------------------+--------------------+
|              mcs3 |                  3 |
+-------------------+--------------------+
```

Confirm that MaxScale routes the SELECT statements to different replica servers.

For more information on different routing criteria, see `slave_selection_criteria`

## Next Step

Navigation in the procedure "Deploy ColumnStore Object Storage Topology":

This page was **step 8 of 9**.

[Next: Step 9: Import Data](step-9-import-data.md)

{% include "https://app.gitbook.com/s/SsmexDFPv2xG2OTyO5yV/~/reusable/pNHZQXPP5OEz2TgvhFva/" %}

{% @marketo/form formId="4316" %}
